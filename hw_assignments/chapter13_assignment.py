class Chatbot:
    """ An object that can engage in rudimentary conversation with a human. """

    def __init__(self, name):
        self.name = name

    def greeting(self):
        """ Returns the Chatbot's way of introducing itself. """
        return "Hello, my name is " + self.name

    def response(self, prompt_from_human):
        """ Returns the Chatbot's response to something the human said. """
        return "It is very interesting that you say: '" + prompt_from_human + "'"


# TODO define a class called BoredChatbot
