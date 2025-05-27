import random

# all responses can also be stored here
about_me = "Well, I'm a simple chatbot for now. But who knows?\n\
     My algorithm might get complex with time.\n\
     Maybe I'm just kidding, maybe not."

def unknown_message():
    response = [
        'Could you please re-phrase that?',
        'What does that even mean?',
        'That sound great with me.',
        'Okay, I\'m lost'
    ][random.randrange(4)]

    return response

