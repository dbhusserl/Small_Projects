#------------------------------------------------------------------------------------------------------#
# Purpose: Provide a single .py file to house a locally run basic flask application
#------------------------------------------------------------------------------------------------------#


from flask import Flask

app = Flask(__name__)

@app.route('/')
def header_page():
    return 'Author: D. Husserl'