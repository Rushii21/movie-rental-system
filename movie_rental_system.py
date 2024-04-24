import mysql.connector

# Establish connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Rushiii@@21',
    database='movie_rental'
)

cursor = conn.cursor()

def add_movie(title, genre):
    """Add a new movie to the database."""
    sql = "INSERT INTO movies (title, genre, available) VALUES (%s, %s, %s)"
    values = (title, genre, True)
    cursor.execute(sql, values)
    conn.commit()
    return "Movie added successfully!"

def delete_movie(movie_id):
    """Delete a movie from the database."""
    cursor.execute("DELETE FROM movies WHERE movie_id = %s", (movie_id,))
    conn.commit()
    return "Movie deleted successfully!"

def add_customer(name, email):
    """Add a new customer to the database."""
    sql = "INSERT INTO customers (name, email) VALUES (%s, %s)"
    values = (name, email)
    cursor.execute(sql, values)
    conn.commit()
    return "Customer added successfully!"

def show_all_customers():
    """Retrieve and show all customers."""
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    return customers

def get_available_movies():
    """Retrieve a list of available movies."""
    sql = "SELECT * FROM movies WHERE available = %s"
    values = (True,)
    cursor.execute(sql, values)
    movies = cursor.fetchall()
    return movies

def rent_movie(customer_id, movie_id):
    """Rent a movie to a customer."""
    cursor.execute("SELECT available FROM movies WHERE movie_id = %s", (movie_id,))
    result_movie = cursor.fetchone()

    if result_movie is None:
        return "Invalid movie ID. Please try again."

    available = result_movie[0]

    cursor.execute("SELECT * FROM customers WHERE customer_id = %s", (customer_id,))
    result_customer = cursor.fetchone()

    if result_customer is None:
        return "Invalid customer ID. Please try again."

    if available:
        sql = "INSERT INTO rentals (customer_id, movie_id, rental_date) VALUES (%s, %s, DATE(NOW()))"
        values = (customer_id, movie_id)
        cursor.execute(sql, values)
        cursor.execute("UPDATE movies SET available = %s WHERE movie_id = %s", (False, movie_id))
        conn.commit()
        return "Movie rented successfully!"
    else:
        return "Sorry, this movie is not available for rent."

def return_movie(rental_id):
    """Return a rented movie."""
    cursor.execute("SELECT movie_id FROM rentals WHERE rental_id = %s", (rental_id,))
    result = cursor.fetchone()

    if result is None:
        return "Invalid rental ID. Please try again."

    movie_id = result[0]

    cursor.execute("UPDATE rentals SET return_date = DATE(NOW()) WHERE rental_id = %s", (rental_id,))
    cursor.execute("SELECT * FROM rentals WHERE rental_id = %s", (rental_id,))
    rental_info = cursor.fetchone()
    cursor.execute("UPDATE movies SET available = %s WHERE movie_id = %s", (True, movie_id))
    conn.commit()
    return "Movie returned successfully!"

def delete_customer(customer_id):
    """Delete a customer from the database."""
    cursor.execute("DELETE FROM customers WHERE customer_id = %s", (customer_id,))
    conn.commit()
    return "Customer deleted successfully!"

def list_all_rentals():
    """Retrieve and list all rentals."""
    cursor.execute("SELECT * FROM rentals")
    rentals = cursor.fetchall()
    return rentals
