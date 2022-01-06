class User:
    nextId = 1      # zmienna klasowa/statyczna, tutaj przydatna przy iteracji

    def __init__(self, name="unnamed"):
        self.name = name
        self.id = User.nextId
        User.nextId += 1
