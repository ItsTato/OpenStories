from sys import exit
if __name__ == "__main__":
	print("Uh oh! You cannot launch this file by itself,\nuse the OpenStories launcher @ launch.py instead!")
	exit()

from os import path
from json import load
from flask import Flask, render_template

proj_dir:str = path.dirname(path.realpath(__file__))

with open(f"{proj_dir}/config.json","r") as file:
	config:dict = load(file)
	file.close()

app = Flask(__name__)

@app.route("/",methods=["GET"])
def index():
	return render_template("index.html",title=config["Site Name"])
