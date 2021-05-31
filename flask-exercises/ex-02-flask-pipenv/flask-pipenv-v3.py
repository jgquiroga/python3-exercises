from flask import Flask, render_template, request
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
def hello():
    return render_template('home-v3.html')

@app.route("/your-url", methods = ['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        # args is for querystring
        # form is for post
        return render_template('your_url.html', code = request.form['code'] )
    else:
        return 'This is not valid'


if __name__ == "__main__":
    app.run()


