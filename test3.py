from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = '8408db4604e1557252915b5fb973e554'  # Change this to a secure random key

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['usersdata']  # Replace 'your_database' with your database name

# User collection
users_collection = db['users']

# Routes

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('home'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Retrieve the user from the database
        user = users_collection.find_one({'username': username})
        
        if user:
            # Check if the provided password matches the hashed password stored in the database
            if check_password_hash(user['password'], password):
                session['username'] = username
                return redirect(url_for('home'))
            else:
                return render_template('login.html', error='Invalid username or password')
        else:
            return render_template('login.html', error='Invalid username or password')
    
    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        
        # Check if the username is already taken
        existing_user = users_collection.find_one({'username': username})
        if existing_user:
            return render_template('create_account.html', error='Username already exists')
        
        # Add the new user to the database
        new_user = {'username': username, 'password': password}
        users_collection.insert_one(new_user)
        return redirect(url_for('login', success_message='Account created successfully. Please log in.'))

    return render_template('create_account.html')

@app.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/booking_details')
def booking_details():
    booking_details = session.get('booking_details')
    print(booking_details)  # Print session data for debugging
    if not booking_details:
        return redirect(url_for('book_vehicle'))
    return render_template('booking_details.html', booking_details=booking_details)

@app.route('/browse_vehicles')
def browse_vehicles():
    if 'username' in session:
        return render_template('browse_vehicles.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/manage_bookings')
def manage_bookings():
    if 'username' in session:
        return render_template('manage_bookings.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/pickup_dropoff')
def pickup_dropoff():
    if 'username' in session:
        return render_template('pickup_dropoff.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/vehicle_details')
def vehicle_details():
    if 'username' in session:
        return render_template('vehicle_details.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/pricing')
def pricing():
    if 'username' in session:
        return render_template('pricing.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/book_vehicle', methods=['GET', 'POST'])
def book_vehicle():
    if request.method == 'POST':
        session['booking_details'] = {
            'start': request.form.get('start'),
            'end': request.form.get('end'),
            'car': request.form.get('car'),
            'travelTime': request.form.get('travelTime'),
            'estimatedPrice': request.form.get('estimatedPrice')
        }
        print(session['booking_details'])  # Print session data for debugging
        return redirect(url_for('booking_details'))
    return render_template('book_vehicle.html')

if __name__ == '__main__':
    app.run(debug=True)
