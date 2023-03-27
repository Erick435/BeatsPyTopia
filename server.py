from flask import Flask, render_template, request, redirect

app = Flask (__name__)

#This route will render the index.html file
@app.route('/')
def index():
    return render_template("index.html")

#This route will 
@app.route('/results', methods = ['POST'])
def receive_form():

    return render_template("login.html", 
        full_name = request.form['full_name'],
        m_name = request.form['m_name'], 
        pet_name = request.form['pet_name'], 
        ss = request.form['ssn'])

if __name__ == "__main__":
    app.run(debug = True)