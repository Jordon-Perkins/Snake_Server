import sqlite3
import json

from models import Snake


def get_all_snakes():
    with sqlite3.connect("./snake.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name, 
            a.owner_id,
            a.species_id,
            a.gender,
            a.color
        FROM Snakes a
        """)
        snakes = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            snake = Snake(row['id'], row['name'], row['owner_id'],
                    row['species_id'], row['gender'], row['color'])
            snakes.append(snake.__dict__)
    return snakes


def get_single_snake(id):
    with sqlite3.connect("./snake.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name, 
            a.owner_id,
            a.species_id,
            a.gender,
            a.color
        FROM Snakes a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        snake = Snake(data['id'], data['name'], data['owner_id'],
                    data['species_id'], data['gender'], data['color'])

        return snake.__dict__


def create_snake(new_snake):
    with sqlite3.connect("./snake.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Snakes
            ( name, owner_id, species_id, gender, color )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_snake['name'], new_snake['owner_id'],
              new_snake['species_id'], new_snake['gender'],
              new_snake['color'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_snake['id'] = id


    return new_snake


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


def get_snakes_by_species_id(species_id):

    with sqlite3.connect("./snake.sqlite3") as conn:
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
        FROM Snakes a
        WHERE a.species_id = ?
        """, ( species_id, ))

        snakes = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            snake = Snake(row['id'], row['name'], row['owner_id'], row['species_id'],
                            row['gender'], row['color'])
            snakes.append(snake.__dict__)

    return snakes
