class AI:
    def check(self):
        return "AI's check"
    def display(self):
        print(self.check(),end=" ")

class ML(AI):
    def check(self):
        return "ML's check"

AI().display()
ML().display()