from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def main():
  return render_template('index.html')


@app.route("/exercise-of-the-day")
def exercise_of_the_day():
  return render_template('exercise-of-the-day.html')


@app.route("/motivation")
def motivation():
  return render_template("motivation.html")


@app.route("/workouts")
def workouts():
  return render_template("workouts.html")


@app.route("/notes")
def notes():
  return render_template("notes.html")


##############################################
# User signup/login/logout


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
  if request.method == 'POST':
    email = request.form.get('email')
    firstName = request.form.get('firstName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    if len(email) < 4:
      flash('Email must be greater than 3 characters.', category='error')
    elif len(firstName) < 2:
      flash('First name must be greater than 1 characters.', category='error')
    elif password1 != password2:
      flash('Passwords don\'t match.', category='error')
    elif len(password1) < 7:
      flash('Password must be atleast 7 characters.', category='error')
    else:
      flash('Account created!', category='success')

  return render_template('sign-up.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
  return render_template("login.html", boolean=True)


@app.route("/logout")
def logout():
  return render_template("logout.html")

if __name__ == '__main__':
  # Run the Flask app
  app.run(host='0.0.0.0', debug=True, port=8080)

