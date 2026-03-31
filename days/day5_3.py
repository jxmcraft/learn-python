class user():
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.login_attempts = 0
    
    def describe_user(self):
        print(self.first, self.last)
    
    def greet(self):
        print("Hello " + self.first + " " + self.last)

    def increment(self):
        self.login_attempts = self.login_attempts + 1
        print("Login attempts:" + str(self.login_attempts))
    def reset(self):
        self.login_attempts = 0
        print("Resetted login attempts")
