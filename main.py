from sys import exit
from flask import Flask

if not __name__ == "__main__":
	exit()

app = Flask(__name__)

@app.route("/",methods=["GET"])
def index():
	return "Hi mom!"

app.run("0.0.0.0",80)
