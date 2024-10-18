from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('form_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS form_data
                 (fullname TEXT, cnic TEXT, dob TEXT, email TEXT, phone TEXT)''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        fullname = request.form['fullname']
        cnic = request.form['cnic']
        dob = request.form['dob']
        email = request.form['email']
        phone = request.form['phone']
        
        # Save the data to the database
        conn = sqlite3.connect('form_data.db')
        c = conn.cursor()
        c.execute("INSERT INTO form_data (fullname, cnic, dob, email, phone) VALUES (?, ?, ?, ?, ?)",
                  (fullname, cnic, dob, email, phone))
        conn.commit()
        conn.close()
        
        return 'Data saved successfully!'
    return render_template('index.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
