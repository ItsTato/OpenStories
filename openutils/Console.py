class Console:
    def __init__(self) -> None:
        from os import system, name
        self.__system = system
        self.__name = name
    def clear(self) -> None:
        self.__system("cls" if self.__name in ["nt"] else "clear")