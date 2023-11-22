
# class NLPHandler:
#     def __init__(self, robot):
#         self.robot = robot

#     def process_command(self, command):
#         words = nltk.word_tokenize(command.lower())
#         if words[0] == 'draw' and words[1] in ['circle', 'rectangle', 'triangle']:
#             shape_command = words[1]
#             parameters = [word for word in words[2:] if word.isdigit()]
#             if parameters:
#                 parameters = list(map(int, parameters))
#                 self.robot.draw_handler.draw_shape(shape_command, *parameters)
#             else:
#                 print("Invalid parameters for drawing.")
# #There needs to be a lot more done here but TBD.