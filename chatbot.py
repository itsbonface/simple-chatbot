import re
import responses
import sys

your_name = input('Name: ')

print(f'Bot: How can I help you today {your_name}')


def message_probability(user_message, recorgnised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recorgnised_words:
            message_certainty += 1

    # Calculates the percentage of recorgnised words in user message
    percentage = float(message_certainty) / float(len(recorgnised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    
    return 0


def check_all_messages(message):
    highest_prob_list = {}

    # To add values to the dictionary
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # responses
    response('Hello!', ['hello', 'hi', 'what\'s up', 'hey', 'holla'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how', 'are'])
    response('thank you!', ['I', 'like', 'coding', 'in', 'python'], required_words=['coding', 'python'])
    response(responses.about_me, ['who', 'are', 'you'], required_words=['who', 'you'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    print(highest_prob_list)

    return responses.unknown_message() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response
while True:
    print("Bot: " + get_response(input(f'{your_name}: ')))
