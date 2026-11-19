
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


'''
{{ }} - Expression to print output in HTML
{%...%} - Conditions and for loops
{#...#} - Comments
'''


# Variable rule
@app.route('/success/<int:score>')
def success(score):

    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"

    return render_template('result.html', results=res)


# Dictionary result
@app.route('/successres/<float:score>')
def successres(score):

    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

    result = {
        "score": round(score, 2),
        "res": res
    }

    return render_template('result1.html', result=result)


# If condition
@app.route('/successif/<int:score>')
def successif(score):

    return render_template('result.html', results=score)


@app.route('/fail/<int:score>')
def fail(score):

    return render_template('result.html', results=score)


# Display HTML form
@app.route('/')
def home():
    return redirect(url_for('submit'))


# GET and POST requests
@app.route('/submit', methods=['GET', 'POST'])
def submit():

    # GET request: Display form
    if request.method == 'GET':
        return render_template('getresult.html')

    # POST request: Process form data
    science = float(request.form['science'])
    maths = float(request.form['maths'])
    c = float(request.form['c'])
    data_science = float(request.form['datascience'])

    total_score = (science + maths + c + data_science) / 4

    return redirect(url_for('successres', score=total_score))


if __name__ == '__main__':
    app.run(debug=True)
