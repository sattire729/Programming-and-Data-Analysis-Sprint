# 8-9 Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.

def show_messages(messages):
    for message in messages:
        print(message)

messages = ['hello gng', 'wbu twin?', "I'm gay", 'Its today!', "I hate 'em"]
show_messages(messages)
