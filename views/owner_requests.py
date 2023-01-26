import sqlite3
import json

from models import Owner



def get_all_owners():
    with sqlite3.connect("./snake.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.first_name,
            a.last_name,
            a.email
        FROM Owners a
        """)
        owners = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            owner = Owner(row['id'], row['first_name'], row ['last_name'], row['email'])
            owners.append(owner.__dict__)
    return owners

def get_single_owner(id):
    with sqlite3.connect("./snake.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.first_name,
            a.last_name,
            a.email
        FROM Owners a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        owner = Owner(data['id'], data['first_name'], data['last_name'], data['email'])

        return owner.__dict__


def create_owner(owner):
    max_id = Owner[-1]["id"]
    new_id = max_id + 1
    owner["id"] = new_id
    Owner.append(owner)
    return owner


def update_owner(id, new_owner):
    with sqlite3.connect("./snake.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        UPDATE Owner
            SET
                first_name = ?
                last_name = ?
                email = ?
        WHERE id = ?
        """, (new_owner['first_name'], new_owner['last_name'], new_owner['email'], id, ))
        rows_affected = db_cursor.rowcount
    if rows_affected == 0:
        return False
    else:
        return True