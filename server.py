from flask import Flask, render_template, request, redirect, session

app = Flask (__name__)
#We need a secret key in order to use session
app.secret_key = "I am a secret key"


#This route will render the index.html file
@app.route('/')
def index():
    return render_template("index.html")

#This route will 
@app.route('/handle_results', methods = ['POST'])
def receive_form():

    session['full_name'] = request.form['full_name']
    session['m_name'] = request.form['m_name']
    session['pet_name'] = request.form['pet_name']
    session['ssn'] = request.form['ssn']

    # return render_template("login.html", 
    #     full_name = request.form['full_name'],
    #     m_name = request.form['m_name'], 
    #     pet_name = request.form['pet_name'], 
    #     ss = request.form['ssn'])
    return redirect('/show_results')

@app.route('/show_results')
def show_results():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug = True)