from flask import Flask, render_template, redirect, url_for
import sqlite3
from gpio_controller import trigger_zone, reset_alarm, system_status, zone_buttons

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', zone=system_status["zone"], alarm=system_status["alarm"])

@app.route('/reset')
def reset():
    reset_alarm()
    return redirect(url_for('index'))

@app.route('/zone/<int:zone_id>')
def simulate_zone(zone_id):
    trigger_zone(zone_id)
    conn = sqlite3.connect('db.sqlite3')
    conn.execute("INSERT INTO events (zone) VALUES (?)", (zone_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
