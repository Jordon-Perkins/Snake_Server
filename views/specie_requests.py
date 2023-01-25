import sqlite3
import json

from models import Specie



def get_all_species():
    with sqlite3.connect("./snake.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name
        FROM Species a
        """)
        species = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            specie = Specie(row['id'], row['name'])
            species.append(specie.__dict__)
    return species

def get_single_specie(id):
    requested_specie = None
    for specie in Specie:
        if specie["id"] == id:
            requested_specie = specie
    return requested_specie


def create_specie(specie):
    max_id = Specie[-1]["id"]
    new_id = max_id + 1
    specie["id"] = new_id
    Specie.append(specie)
    return specie


def update_specie(id, new_specie):
    with sqlite3.connect("./snake.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        UPDATE Specie
            SET
                name = ?
        WHERE id = ?
        """, (new_specie['name'], id, ))
        rows_affected = db_cursor.rowcount
    if rows_affected == 0:
        return False
    else:
        return True