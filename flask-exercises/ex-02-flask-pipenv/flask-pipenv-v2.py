from flask import Flask, render_template
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
#     $env:FLASK_APP = "flask-pipenv-v2.py"
#     $env:FLASK_ENV = "development"
# and then:
#     flask run
#
#   Note: to avoid adding always the FLASK_APP, we can rename the application to app.py
#

@app.route("/")
def hello():
    return render_template('home.html', name = 'Julian')

@app.route("/about")
def about():
    return 'This is a test'


if __name__ == "__main__":
    app.run()


