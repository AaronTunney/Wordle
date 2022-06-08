""" Wordle Engine module """

class Wordle:
    """ A Wordle-style game engine. """

    def __init__(self, target):
        """ Standard initialiser. """
        self.target = target

    def guess(self, guess):
        """ Guess at the target word. """
        return "00000"

if __name__ == '__main__':
    wordle = Wordle('hello')
    RESULT = wordle.guess('hello')
    print(RESULT)
