from os import system, path
from sys import exit
from json import load

from openutils import Console, Importer

console:Console = Console()
importer:Importer = Importer()

importer.checkListInstalled(["flask","requests","waitress"])
importer.checkInstalled(importName="dotenv",pypiName="python-dotenv")

console.clear()

print("Launching sequence completed!\nInitializing OpenStories...")

proj_dir:str = path.dirname(path.realpath(__file__))

if path.exists(f"{proj_dir}/config.json"):
	with open(f"{proj_dir}/config.json","r") as file:
		config:dict = load(file)
		file.close()
else:
	print("Missing configuration file!\n- config.json")
	exit()

if __name__ == "__main__":
	try:
		system(f"cd \"{proj_dir}\"/ && waitress-serve --listen={config['Web']['Host']}:{config['Web']['Port']} main:app")
	except KeyboardInterrupt:
		console.clear()
		print("OpenStories instance was terminated.")
	except Exception:
		console.clear()
		print("OpenStories instance has closed unexpectedly.")
