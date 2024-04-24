from flask import Flask, render_template, request
import movie_rental_system

app = Flask(__name__, static_url_path='/static')


# Add the routes for renting and returning movies
@app.route('/rent_movie', methods=['POST'])
def rent_movie():
    customer_id = request.form['customer_id']
    movie_id = request.form['movie_id']
    message = movie_rental_system.rent_movie(int(customer_id), int(movie_id))
    return render_template('index.html', message=message)

@app.route('/return_movie', methods=['POST'])
def return_movie():
    rental_id = request.form['rental_id']
    message = movie_rental_system.return_movie(int(rental_id))
    return render_template('index.html', message=message)


@app.route('/add_movie', methods=['POST'])
def add_movie():
    title = request.form['title']
    genre = request.form['genre']
    message = movie_rental_system.add_movie(title, genre)
    return render_template('index.html', message=message)

@app.route('/delete_movie', methods=['POST'])
def delete_movie():
    movie_id = request.form['movie_id']
    message = movie_rental_system.delete_movie(int(movie_id))
    return render_template('index.html', message=message)

@app.route('/add_customer', methods=['POST'])
def add_customer():
    name = request.form['name']
    email = request.form['email']
    message = movie_rental_system.add_customer(name, email)
    return render_template('index.html', message=message)

@app.route('/delete_customer', methods=['POST'])
def delete_customer():
    customer_id = request.form['customer_id']
    message = movie_rental_system.delete_customer(int(customer_id))
    return render_template('index.html', message=message)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False)
    movie_rental_system.main()
