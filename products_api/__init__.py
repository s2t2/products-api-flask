from flask import Flask

app = Flask(__name__)
app.secret_key = 'my super secret' #todo: get from environment variable (and provide generation instructions)

from products_api import routes

app.run # app.run(debug=True)
