import nltk
nltk.download('punkt')
class NLPHandler:

    def __init__(self):
            self.current_shape = None  # Initialize the current_shape variable

    def interpret_command(self, command):
        interpreted_command = command.lower()
        words = nltk.word_tokenize(interpreted_command)

        if 'circle' in interpreted_command:
            self.current_shape = 'circle'
        elif 'rectangle' in interpreted_command:
            self.current_shape = 'rectangle'
        elif 'pentagon' in interpreted_command:
             self.current_shape = 'pentagon'
        elif 'hexagon' in interpreted_command:
             self.current_shape = 'hexagon'
        elif 'ellipse' in interpreted_command:
             self.current_shape = 'ellipse'
        elif 'triangle' in interpreted_command:
             self.current_shape = 'triangle'
        elif 'square' in interpreted_command:
             self.current_shape = 'square'
        else:
            print("I don't understand the command.")

        return interpreted_command

    def get_current_shape(self):
        return self.current_shape