class Importer:
    def __init__(self):
        from os import name, system
        self.__name:str = name
        self.__system:system = system
    def checkListInstalled(self,imports:list):
        for v in imports:
            self.checkInstalled(v)
    def checkInstalled(self,importName:str,pypiName:str=""):
        if pypiName == "":
            pypiName:str = importName
        if self.__name in ["nt"]:
            try:
                exec(f"import {importName}")
            except ImportError:
                self.__system(f"python -m pip install {pypiName}")
        else:
            try:
                exec(f"import {importName}")
            except ImportError:
                self.__system(f"python3 -m pip install {pypiName}")