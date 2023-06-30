from sys import exit

if __name__ == "__main__":
	print("Uh oh! You cannot launch this file by itself!\nUse the OpenStories launcher (/launch.py) instead.")
	exit()

from openutils import Console
from threading import Thread
from time import sleep
from os import path
from json import load
from flask import Flask, render_template

proj_dir:str = path.dirname(path.realpath(__file__))

with open(f"{proj_dir}/config.json","r") as file:
	config:dict = load(file)
	file.close()

running:bool = True
console:Console = Console()

app = Flask(__name__)

@app.route("/",methods=["GET"])
def index():
	return render_template("index.html",title=config["Site Name"])

def Controller():
	sleep(3)
	console.clear()
	print("Welcome to OpenStories: Controller!")
	print("A simple, lightweight yet powerful CUI made to manage your OpenStories instance.")
	while running:
		command:str = input("> ").lower()

controller_thread = Thread(target=Controller)
controller_thread.start()
