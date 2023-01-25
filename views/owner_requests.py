import sqlite3
import json

from models import Owner



def get_all_owners():
    return Owner

def get_single_owner(id):
    requested_owner = None
    for owner in Owner:
        if owner["id"] == id:
            requested_owner = owner
    return requested_owner


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