from sys import exit

if __name__ == "__main__":
	print("Uh oh! You cannot launch this file by itself!\nUse the OpenStories launcher (/launch.py) instead.")
	exit()

from openutils import Console

from threading import Thread
from time import sleep
from os import path, getenv
from dotenv import load_dotenv
from json import load
from flask import Flask, render_template

proj_dir:str = path.dirname(path.realpath(__file__))

with open(f"{proj_dir}/config.json","r") as file:
	config:dict = load(file)
	file.close()

load_dotenv(f"{proj_dir}/web.env")
load_dotenv(f"{proj_dir}/discord_oauth2.env")

console:Console = Console()

app = Flask(__name__)
app.config["SECRET_KEY"] = getenv("SECRET_KEY")

@app.route("/",methods=["GET"])
def index():
	return render_template("index.html",title=config["Site Name"])

@app.route("/app",methods=["GET"])
def webApp():
	return render_template("app.html",title=config["Site Name"])

def Controller():
	sleep(3)
	console.clear()
	print("Welcome to OpenStories: EC!")
	print("A simple, lightweight yet powerful CUI made to manage your OpenStories instance with ease.")
	print("To terminate OpenStories, CTRL+C is your friend!")
	running:bool = True
	while running:
		command:str = input("OpenStories % ").lower()

controller_thread = Thread(target=Controller)
controller_thread.start()
