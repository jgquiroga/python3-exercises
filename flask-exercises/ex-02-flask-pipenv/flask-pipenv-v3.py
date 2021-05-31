from flask import Flask, render_template, request, redirect, url_for
import json
import os.path
app = Flask(__name__)

# TODO: Add this information in a Readme file
# Prerequisites:
#   Install pipenv (I'm using anaconda)
#       conda install -c conda-forge pipenv
#   Install pipenv in the current project:
#        pipenv install
# run this application in a pipenv environment:
#     pipenv shell
# To run this application in a windows terminal, first we need to execute:
#     $env:FLASK_APP = "flask-pipenv-v3.py"
#     $env:FLASK_ENV = "development"
# and then:
#     flask run
#
#   Note: to avoid adding always the FLASK_APP, we can rename the application to app.py
#

@app.route("/")
def home():
    return render_template('home-v3.html')

@app.route("/your-url", methods = ['GET', 'POST'])
def your_url():
    if request.method == 'POST':

        urls = {}

        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)

        if request.form['code'] in urls.keys():
            return redirect(url_for('home'))

        urls[request.form['code']] = { 'url': request.form['url'] }
        with open('urls.json', 'w') as url_file:
            json.dump(urls, url_file)

        # args is for querystring
        # form is for post
        return render_template('your_url.html', code = request.form['code'] )
    else:
        # url_for receives the url of an action
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run()


