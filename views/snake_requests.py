import sqlite3
import json

from models import Snake


def get_all_snakes():
    # Open a connection to the database
    with sqlite3.connect("./snake.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name, 
            a.owner_id,
            a.species_id,
            a.gender,
            a.color
        FROM snake a
        """)

        # Initialize an empty list to hold all animal representations
        snakes = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            snake = Snake(row['id'], row['snake'])

            snakes.append(snake.__dict__)

    return snakes


def get_single_snake(id):
    requested_snake = None
    for snake in Snake:
        if snake["id"] == id:
            requested_snake = snake
    return requested_snake


def create_snake(snake):
    max_id = Snake[-1]["id"]
    new_id = max_id + 1
    snake["id"] = new_id
    Snake.append(snake)
    return snake


def update_snake(id, new_snake):
    with sqlite3.connect("./snake.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        UPDATE Snakes
            SET
                name = ?
                owner_id = ?
                species_id = ?
                gender = ?
                color = ?
        WHERE id = ?
        """, (new_snake['name'], new_snake['owner_id'], new_snake['species_id'], new_snake['gender'], new_snake['color'], id, ))
        rows_affected = db_cursor.rowcount
    if rows_affected == 0:
        return False
    else:
        return True