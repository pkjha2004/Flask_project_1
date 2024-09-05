'''
{{} expression to buitl output in html
{%...%}expression for loops
{#...#}e expressin for comments
'''

from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)
@app.route("/")
def welcome():
    return '<html><h1>Welcome to the Flask courses</h1></html'
@app.route("/index",methods = ['GET'])### Get is used to request data from a specific data
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/form',methods = ['GET','POST'])###  post is used to update a data 
def form():
    if request.method =='POST':
        name = request.form['name']
        return f"Hello {name}!"
    return render_template('form.html')

@app.route("/success/<int:score>")
def success(score):
    res = " "
    if score>=50:
       res = "You have passed the exam"
    else:
        res = "You have failed the exam"
    return render_template('result.html',results = res)

@app.route("/successres/<int:score>")
def successres(score):
    res = " "
    if score>=50:
       res = "You have passed the exam"
    else:
        res = "You have failed the exam"
    exp = {'score':score,"res":res }
    return render_template('result1.html', results = exp)

@app.route("/submit",methods = ['POST','GET'])
def submit():
    total_score = 0
    if request.method =='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        cs = float(request.form['cs'])
        english = float(request.form['english'])
        total_score = (science+maths+cs+english)/4
    else:
        return render_template('getresults.html')
    return redirect(url_for('successres',score = total_score))
    
 
    
if __name__ =="__main__":
    app.run(debug = True)


     