class ProgrammingLanguage:
    def __init__(self,name="", typing="", reflection="", year=""):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year


    def __str__(self):
        return f"{self.name},{self.typing} typing, reflection={self.reflection}, First append in {self.year}"

    def is_dynamic(self):
        return self.typing == "Dynamic"