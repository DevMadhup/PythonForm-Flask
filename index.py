from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route('/getdata', methods=['post'])
def getdata():
    a = request.form['fname']
    b = request.form['lname']
    c = request.form['email']
    d = request.form['pass']
    e = request.form['dob']
    return render_template('output.html',a=a, b=b, c=c, d=d, e=e) 

app.run(debug=True)