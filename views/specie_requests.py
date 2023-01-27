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
    with sqlite3.connect("./snake.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name
        FROM Species a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        specie = Specie(data['id'], data['name'])

        return specie.__dict__

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