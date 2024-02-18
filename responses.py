import random

# all responses can also be stored here
about_me = "Well, I'm a simple chatbot for now. But who knows?\n\
     I might get complex and take over your world with time.\n\
     Maybe I'm just kidding, maybe not."

def unknown_message():
    response = [
        'Could you please re-phrase that?',
        'What does that even mean, nigga?',
        'That sound great with me.',
        'Okay, I\'m lost'
    ][random.randrange(4)]

    return response

