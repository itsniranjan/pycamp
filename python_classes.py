# Class for Horse
class Horse:

    # Class Variable
    animal = 'Horse'

    # The init method or constructor
    def __init__(self, breed):

        # Instance Variable
        self.breed = breed

    # Adds an instance variable
    def setColor(self, color):
        self.color = color

    # Retrieves instance variable
    def getColor(self):
        return self.color


# Driver Code
Rod = Horse("Mustang")
Rod.setColor("brown")
Rod.age = 24
print(Rod.age)
