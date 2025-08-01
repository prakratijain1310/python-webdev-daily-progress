from flask import Flask, render_template, request, redirect
from models import db, Appointment
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def appointment_form():
    return render_template('appointment.html')

@app.route('/submit_appointment', methods=['POST'])
def submit_appointment():
    name = request.form['name']
    number = request.form['number']
    date = request.form['date']
    time = request.form['time']

    date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    time_obj = datetime.strptime(time, "%H:%M").time()

    new_appt = Appointment(name=name, number=number, date=date_obj, time=time_obj)
    db.session.add(new_appt)
    db.session.commit()

    return redirect('/show_appointments')

@app.route('/show_appointments')
def show_appointments():
    appointments = Appointment.query.all()
    return render_template('show_appointments.html', appointments=appointments)

if __name__ == '__main__':
    app.run(debug=True)
