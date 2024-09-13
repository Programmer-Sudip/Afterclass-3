class Robot:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def introduce(self):
        print(f"Hello, I am {self.name}. I am a {self.role} robot.")

# Creating instances of Robot
tom = Robot("Tom", "assistant")
jerry = Robot("Jerry", "security")

# Introducing each robot
tom.introduce()
jerry.introduce()
