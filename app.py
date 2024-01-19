from flask import Flask, render_template, request, redirect, url_for
import pyrebase

app = Flask(__name__)

# Replace these values with your Firebase project credentials
Config = {
  "apiKey": "AIzaSyDj41TmsHxt-W--RgpgyI0oV65TLAlCE7I",
  "authDomain": "music-streaming-platform-bac9a.firebaseapp.com",
  "projectId": "music-streaming-platform-bac9a",
  "storageBucket": "music-streaming-platform-bac9a.appspot.com",
  "messagingSenderId": "374702597612",
  "appId": "1:374702597612:web:68b09ba638c8739fd98cc9",
  "measurementId": "G-5W36BZ55FC",
  "databaseURL":"https://music-streaming-platform-bac9a-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()

@app.route('/')
def index():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = auth.create_user_with_email_and_password(email, password)
        # You can customize this part to store additional user information in your database
        # For example, you might want to create a 'users' collection and store user details there
        # user_info = {"email": email, "uid": user['localId']}
        # db.child("users").child(user['localId']).set(user_info)

        return redirect(url_for('success'))
    except Exception as e:
        error_message = str(e)
        return render_template('signup.html', error=error_message)

@app.route('/success')
def success():
    return "Signup successful!"

if __name__ == '__main__':
    app.run(debug=True)
