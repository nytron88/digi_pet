class Pet:

    def __init__(self, name):
        self.name = name
        self.sleep = 5
        self.love = 5
        self.exercise = 5
        self.water = 5
        self.feed = 5

    @property
    def on_birth(self):
        if self.name is not "":
            respond = self.name + " says Wahhhhh"
            return respond
        else:
            respond: str = "Something went wrong, please restart the program"
            return respond

    def on_sleep(self):
        self.sleep += 1
        self.exercise -= 1
        self.love -= 1
        self.water += 1
        self.feed -= 1
        print(self.name + " says the sleep was great")

    def on_exercise(self):
        self.sleep -= 1
        self.exercise += 1
        self.love += 1
        self.water -= 1
        self.feed -= 1
        print(self.name + " says I am tired, I did a lot of exercise")

    def on_love(self):
        self.love += 1
        self.exercise -= 1
        self.water -= 1
        self.feed += 1
        self.sleep -= 1
        print(self.name + " says I love you too")

    def on_water(self):
        self.love += 1
        self.exercise -= 1
        self.water += 1
        self.feed -= 1
        self.sleep -= 1
        print(self.name + " says Thanks, I am not thirsty anymore")

    def on_feed(self):
        self.love -= 1
        self.exercise -= 1
        self.water -= 1
        self.feed += 1
        self.sleep += 1
        print(self.name + " says Thanks for feeding me, I am not hungry anymore")

    def stats(self):
        return "Sleep: " + str(self.sleep), "Exercise: " + str(self.exercise), "Love: " + str(
            self.love), "Water: " + str(self.water), "Feed: " + str(self.feed)
