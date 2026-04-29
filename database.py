import sqlite3

DB_NAME = "zombie_overflow.db"

def connect():
    return sqlite3.connect(DB_NAME)