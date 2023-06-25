from os import system, name, path
from sys import exit
from json import load

def clearConsole():
    system("cls" if name in ["nt"] else "clear")

def safeImport(pack, packPypi: str = None):
	if packPypi == None:
		packPypi = pack
	if name == "nt":
		try:
			exec(f"import {pack}")
		except:
			system(f"py -3 -m pip install {packPypi}")
	else:
		try:
			exec(f"import {pack}")
		except:
			system(f"python3 -m pip install {packPypi}")

safeImport("flask")
safeImport("requests")
safeImport("waitress")

clearConsole()

print("Launching sequence completed!\nInitializing OpenStories...")

proj_dir:str = path.dirname(path.realpath(__file__))

if path.exists(f"{proj_dir}/config.json"):
	with open(f"{proj_dir}/config.json","r") as file:
		config:dict = load(file)
		file.close()
else:
	print("Missing configuration file!\n- config.json")
	exit()

system(f"cd {proj_dir}/ && waitress-serve --listen={config['Web']['Host']}:{config['Web']['Port']} main:app")
