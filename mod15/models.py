import sqlite3
from datetime import datetime
from typing import List, Any

class Room:
    def __init__(self, id: int, floor: int, beds: int, guestNum: int, price: float) -> None:
        self.id = id
        self.floor = floor
        self.beds = beds
        self.guestNum = guestNum
        self.price = price

    def __getitem__(self, item: str) -> Any:
        return getattr(self, item)

class Order:
    def __init__(self, id: int, checkIn: datetime, checkOut: datetime, firstName: str, lastName: str, roomId: int):
        self.id = id
        self.checkIn = checkIn
        self.checkOut = checkOut
        self.firstName = firstName
        self.lastName = lastName
        self.roomId = roomId

def init_db() -> None:
    with sqlite3.connect("hotel.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS table_rooms (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                floor INTEGER,
                beds INTEGER,
                guestNum INTEGER,
                price REAL
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS table_orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                checkIn DATETIME,
                checkOut DATETIME,
                firstName TEXT,
                lastName TEXT,
                roomId INTEGER,
                FOREIGN KEY (roomId) REFERENCES table_rooms(id)
            );
        """)

def get_all_rooms(checkIn: str = None, checkOut: str = None) -> List[Room]:
    with sqlite3.connect('hotel.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM table_rooms")
        return [Room(*row) for row in cursor.fetchall()]

def insert_room_to_bd(room: Room) -> None:
    with sqlite3.connect('hotel.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO table_rooms (floor, beds, guestNum, price)
            VALUES (?, ?, ?, ?)
        """, (room.floor, room.beds, room.guestNum, room.price))

def add_order(order: Order) -> int:
    with sqlite3.connect('hotel.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO table_orders (checkIn, checkOut, firstName, lastName, roomId)
            VALUES (?, ?, ?, ?, ?)
        """, (order.checkIn, order.checkOut, order.firstName, order.lastName, order.roomId))
        connection.commit()
        cursor.execute("SELECT last_insert_rowid()")
        order_id = cursor.fetchone()[0]
        return order_id

def get_order(order: Order) -> List[Order]:
    with sqlite3.connect('hotel.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM table_orders WHERE checkIn >= ? AND checkIn <= ? AND roomId = ?
        """, (order.checkIn, order.checkOut, order.roomId))
        return [Order(*row) for row in cursor.fetchall()]
