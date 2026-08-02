from abc import ABC, abstractmethod


class Player(ABC):

    def __init__(self, name, runs, balls):
        self.__name = name
        self.__runs = runs
        self.__balls = balls

    # Getters
    def get_name(self):
        return self.__name

    def get_runs(self):
        return self.__runs

    def get_balls(self):
        return self.__balls

    # Setters
    def set_runs(self, runs):
        self.__runs = runs

    def set_balls(self, balls):
        self.__balls = balls

    # Common Method
    def strike_rate(self):
        return (self.__runs / self.__balls) * 100

    # Abstract Method
    @abstractmethod
    def display(self):
        pass

    def display_details(self):

        print(f"Name        : {self.__name}")
        print(f"Runs        : {self.__runs}")
        print(f"Balls       : {self.__balls}")
        print(f"Strike Rate : {self.strike_rate():.2f}")
