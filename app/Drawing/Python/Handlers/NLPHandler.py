import nltk
nltk.download('punkt')
class NLPHandler:
    """Handles natural language processing for shape commands."""

    def __init__(self):
        """Initialize the NLPHandler."""
        self.shape_mapping = {
            'circle': 'circle',
            'rectangle': 'rectangle',
            'pentagon': 'pentagon',
            'hexagon': 'hexagon',
            'ellipse': 'ellipse',
            'triangle': 'triangle',
            'square': 'square'
        }
        self.current_shape = None

    def interpret_command(self, command):
        """Interpret a natural language command and set the current shape.

        Args:
            command (str): The natural language command.

        Returns:
            None

        Note:
            Updates the `current_shape` attribute.
        """
        interpreted_command = command.lower()
        words = nltk.word_tokenize(interpreted_command)

        for word in words:
            if word in self.shape_mapping:
                self.current_shape = self.shape_mapping[word]
                break
        else:
            print("I don't understand the command.")
        return interpreted_command