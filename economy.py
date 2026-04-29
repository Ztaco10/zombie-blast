"""
Economy module for managing currency and reward logic in the math zombie game.

This module encapsulates all calculations and state tracking related to player
currency, reward distribution and progression scaling. It exposes a small
API that the rest of the game can call to credit coins for correct answers,
apply defeat bonuses when monsters are defeated, spend coins in the shop and
grant unique rewards. By centralising this logic in one place it becomes
easier to adjust reward formulas and ensure that the rules for earning and
spending are applied consistently across the game.

Key features:
* Rewards for correct answers scale with difficulty and player level.
* Bonuses are awarded when a monster is defeated and can only be claimed
  once per monster.
* A maximum balance caps how many coins the player can accumulate.
* Attempts to earn zero or negative currency simply return the current balance.
* Spending coins fails gracefully if the player cannot afford the cost.
* Unique reward IDs can be granted only once per player.

Constants at the top of the module define base reward values and multipliers
to avoid magic numbers scattered throughout the code. Feel free to tweak
these values to tune the pace of progression or difficulty.
"""

from dataclasses import dataclass, field
from typing import Set, Dict

# Base amount of coins awarded for a correct answer before scaling.
BASE_CORRECT_REWARD: int = 10
# Base amount of coins awarded when a monster is defeated before scaling.
BASE_MONSTER_REWARD: int = 20
# Difficulty multipliers applied to all rewards. Harder difficulties earn more.
DIFFICULTY_MULTIPLIERS: Dict[str, float] = {
    "easy": 1.0,
    "medium": 1.5,
    "hard": 2.0,
}
# Amount by which rewards scale up per player level (10% per level).
LEVEL_SCALING_FACTOR: float = 0.10
# Maximum number of coins a player can hold. Further earnings are capped.
MAX_BALANCE: int = 1000

@dataclass
class Economy:
    """Manages currency and reward scaling for a single player.

    Attributes:
        difficulty: The difficulty level as chosen by the player. Should be
            one of the keys in ``DIFFICULTY_MULTIPLIERS``.
        level: The player's current level. Levels start at 1 and can be
            incremented to increase reward scaling over time.
        balance: The current amount of coins the player has.
        rewards: A set of unique reward identifiers that have been granted.
        defeated_monsters: A set of monster identifiers that have already
            yielded their defeat bonus. Prevents awarding the same bonus twice.
        max_balance: Maximum allowed coin balance. Defaults to ``MAX_BALANCE``.
    """

    difficulty: str
    level: int = 1
    balance: int = 0
    rewards: Set[str] = field(default_factory=set)
    defeated_monsters: Set[str] = field(default_factory=set)
    max_balance: int = MAX_BALANCE

    def _scaled_reward(self, base_amount: int) -> int:
        """Compute a reward amount factoring in difficulty and level.

        Args:
            base_amount: The unscaled base reward.

        Returns:
            The scaled reward as an integer.
        """
        # Normalize difficulty key to lower‑case for robust lookup.
        diff_key = self.difficulty.lower()
        diff_multiplier = DIFFICULTY_MULTIPLIERS.get(diff_key, 1.0)
        # Level scaling grows by ``LEVEL_SCALING_FACTOR`` per level above 1.
        scaling = 1.0 + max(self.level - 1, 0) * LEVEL_SCALING_FACTOR
        # Multiply and round down to the nearest integer.
        scaled = int(base_amount * diff_multiplier * scaling)
        return scaled

    def add_currency(self, amount: int) -> int:
        """Add a positive amount of coins to the player's balance.

        If the amount is non‑positive, the balance remains unchanged. The
        resulting balance will not exceed ``max_balance``.

        Args:
            amount: The number of coins to add. Must be positive to have
                any effect.

        Returns:
            The player's new balance.
        """
        if amount <= 0:
            # Negative or zero additions are ignored as per test cases.
            return self.balance
        # Prevent overflow beyond the maximum.
        new_balance = self.balance + amount
        if new_balance > self.max_balance:
            new_balance = self.max_balance
        self.balance = new_balance
        return self.balance

    def earn_correct_answer(self) -> int:
        """Award coins for a correct answer based on current settings.

        This method calculates a reward using the base correct answer
        constant, difficulty multiplier and level scaling, then applies it
        to the player's balance.

        Returns:
            The player's updated balance after awarding the reward.
        """
        reward = self._scaled_reward(BASE_CORRECT_REWARD)
        return self.add_currency(reward)

    def award_monster_defeat(self, monster_id: str, base_reward: int = BASE_MONSTER_REWARD) -> int:
        """Award a one‑off bonus for defeating a monster.

        A monster bonus is only granted once per unique ``monster_id`` to
        prevent duplicate rewards. The reward is scaled similarly to the
        correct answer reward. Subsequent calls with the same ``monster_id``
        will return the current balance without any change.

        Args:
            monster_id: A unique identifier for the monster (e.g. name).
            base_reward: The unscaled base reward for defeating a monster.

        Returns:
            The player's updated balance.
        """
        if monster_id in self.defeated_monsters:
            # Bonus already claimed for this monster.
            return self.balance
        reward = self._scaled_reward(base_reward)
        self.defeated_monsters.add(monster_id)
        return self.add_currency(reward)

    def spend_currency(self, cost: int) -> bool:
        """Attempt to spend coins from the player's balance.

        If the player has enough coins, the cost is deducted and ``True``
        is returned. Otherwise the balance is left unchanged and ``False``
        is returned.

        Args:
            cost: The number of coins to spend.

        Returns:
            ``True`` if the spend succeeded, ``False`` otherwise.
        """
        if cost <= 0:
            # Spending zero or negative amounts does nothing but is allowed.
            return True
        if self.balance < cost:
            return False
        self.balance -= cost
        return True

    def grant_reward(self, reward_id: str) -> bool:
        """Grant a unique reward to the player.

        Rewards are tracked by their identifier. If a reward with the
        provided ID has not been granted before it will be added to the
        internal set and ``True`` returned. If the reward has already been
        granted this call has no effect and ``False`` is returned.

        Args:
            reward_id: A string uniquely identifying the reward.

        Returns:
            ``True`` if the reward was newly granted, ``False`` if it was
            already present.
        """
        if reward_id in self.rewards:
            return False
        self.rewards.add(reward_id)
        return True

    def level_up(self) -> None:
        """Increment the player's level by one.

        Raising the level increases the reward scaling applied by
        ``earn_correct_answer`` and ``award_monster_defeat``. Levels may be
        advanced automatically by the game logic based on player
        progression.
        """
        self.level += 1

    def get_balance(self) -> int:
        """Return the player's current coin balance."""
        return self.balance
