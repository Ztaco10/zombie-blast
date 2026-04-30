"""
Unit tests for the ``economy`` module.

These tests validate the currency and reward logic implemented in the
``Economy`` class against the provided currency test cases. Each test
addresses a specific scenario such as earning coins, capping the balance
when a maximum is reached, spending coins, handling invalid inputs and
granting unique rewards. The tests can be run from the terminal with
``python -m unittest test_currency.py``.
"""

import unittest

from economy import Economy, BASE_CORRECT_REWARD, BASE_MONSTER_REWARD, DIFFICULTY_MULTIPLIERS, LEVEL_SCALING_FACTOR

class TestEconomy(unittest.TestCase):
    def setUp(self) -> None:
        # Use easy difficulty and default max balance for most tests
        self.econ = Economy(difficulty="easy")

    # UT-CR-TC001: Verify positive earnings update balance correctly without exceeding maximum
    def test_add_currency_positive(self):
        self.econ.balance = 100
        self.econ.add_currency(50)
        self.assertEqual(self.econ.balance, 150)

    # UT-CR-TC002: Earnings that would exceed the maximum balance cap at max
    def test_add_currency_caps_at_max(self):
        self.econ.balance = 950
        self.econ.add_currency(100)
        self.assertEqual(self.econ.balance, self.econ.max_balance)

    # UT-CR-TC003: Negative or zero earnings do not change the balance
    def test_add_currency_non_positive(self):
        self.econ.balance = 200
        self.econ.add_currency(-20)
        self.assertEqual(self.econ.balance, 200)
        self.econ.add_currency(0)
        self.assertEqual(self.econ.balance, 200)

    # UT-CR-TC004: Spending deducts when balance is sufficient
    def test_spend_currency_sufficient(self):
        self.econ.balance = 100
        success = self.econ.spend_currency(50)
        self.assertTrue(success)
        self.assertEqual(self.econ.balance, 50)

    # UT-CR-TC005: Spending equal to balance reduces balance to zero
    def test_spend_currency_equal(self):
        self.econ.balance = 100
        success = self.econ.spend_currency(100)
        self.assertTrue(success)
        self.assertEqual(self.econ.balance, 0)

    # UT-CR-TC006: Spending more than available is rejected
    def test_spend_currency_insufficient(self):
        self.econ.balance = 75
        success = self.econ.spend_currency(100)
        self.assertFalse(success)
        self.assertEqual(self.econ.balance, 75)

    # UT-CR-TC007: Granting a new reward adds it to the collection
    def test_grant_reward_new(self):
        granted = self.econ.grant_reward("R01")
        self.assertTrue(granted)
        self.assertIn("R01", self.econ.rewards)

    # UT-CR-TC008: Granting the same reward twice does not duplicate
    def test_grant_reward_duplicate(self):
        self.econ.grant_reward("R01")
        granted_again = self.econ.grant_reward("R01")
        self.assertFalse(granted_again)
        self.assertEqual(len(self.econ.rewards), 1)

    # UT-CR-TC009: Multiple different rewards can be granted uniquely
    def test_grant_multiple_rewards(self):
        self.econ.grant_reward("R02")
        self.econ.grant_reward("R03")
        self.assertEqual(self.econ.rewards, {"R02", "R03"})

    # Additional tests specific to scaling
    def test_scaled_reward_easy_level(self):
        # Easy difficulty, level 1 should yield base correct reward
        reward = self.econ._scaled_reward(BASE_CORRECT_REWARD)
        self.assertEqual(reward, BASE_CORRECT_REWARD)

    def test_scaled_reward_hard_level(self):
        hard_econ = Economy(difficulty="hard")
        reward = hard_econ._scaled_reward(BASE_CORRECT_REWARD)
        expected = int(BASE_CORRECT_REWARD * DIFFICULTY_MULTIPLIERS["hard"])
        self.assertEqual(reward, expected)

    def test_scaled_reward_level_scaling(self):
        # Level up the economy to level 3 and verify scaling factor
        self.econ.level = 3
        scaled = self.econ._scaled_reward(BASE_CORRECT_REWARD)
        expected_scale = 1.0 + (3 - 1) * LEVEL_SCALING_FACTOR
        expected = int(BASE_CORRECT_REWARD * expected_scale)
        self.assertEqual(scaled, expected)

    def test_monster_defeat_bonus_once(self):
        # Award monster bonus only once per id
        self.econ.level = 1
        bal1 = self.econ.award_monster_defeat("zombie1")
        bal2 = self.econ.award_monster_defeat("zombie1")
        self.assertEqual(bal1, bal2)

if __name__ == "__main__":
    unittest.main()
