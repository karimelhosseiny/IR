from os import name
import kimoproject
from flask import Flask, render_template, url_for, request
from flask.templating import render_template

app = Flask(__name__)


@app.route('/')
def log():
    return render_template('design.html')


@app.route('/STM', methods=['GET', 'POST'])
def STM():
    if request.method == "POST":
        q = request.form['nm']
        query = kimoproject.writenumber(q)
        if (not query):
            return "Can't"
        stm = kimoproject.conversiontuple(kimoproject.statisticalmodel(query))
        return "<h1>statistical model</h1><br>" + stm


@app.route('/VSM', methods=['GET', 'POST'])
def VSM():
    if request.method == "POST":
        q = request.form['nm']
        query = kimoproject.writenumber(q)
        if (not query):
            return "Can't"
        vsm = kimoproject.conversiontuple(kimoproject.vectorspace(query))
        return "<h1>Vector space model</h1><br>" + vsm


@app.route('/filesgeneration')
def filesgeneration():
    kimoproject.FilesCreation()
    return "generated"


if __name__ == "__main__":
    app.run(debug=True)
