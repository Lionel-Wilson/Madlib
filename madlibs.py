import random

class Madlib:
    def __init__(self, adj, verb1, verb2, famous_person):
        """
        Create a Madlib object

        :param str adj: An adjective e.g. fascinating
        :param str verb1: The first verb e.g. eat
        :param str verb2: The second verb
        :param str famous_person: The name of a famous person e.g. David Beckham
        :param str stories: A lists of story or sentences that you want to modify with the parameters above.
        """
        self.adj = adj
        self.verb1 = verb1
        self.verb2 = verb2
        self.famous_person = famous_person
        self.stories = [f"Computer programming is so {self.adj}! it makes me so excited all the time because I love to {self.verb1}. Stay hydrated and {self.verb2} like you are {self.famous_person}!", 
        f"Learning Japanese is so {self.adj}! it makes me so sad all the time because I hate to {self.verb1}. Stay in the zone and {self.verb2} like you are {self.famous_person}!"]
        

    def mad_lib(self):
        """
        A function that returns a random story/sentence that uses the parameters you inputted when intatiating the Madlib Object.
        """
        selector = random.randint(0, len(self.stories)-1)
        return print(self.stories[selector])


my_madlib = Madlib("hard","eat","fight","Jackie Chan")

my_madlib.mad_lib()

