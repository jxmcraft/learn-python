class permissions():
    def __init__(self):
        self.permissions = ["can add post", "can delete post", "can ban user"]

    def show_perms(self):
        for perm in self.permissions:
            print(perm)