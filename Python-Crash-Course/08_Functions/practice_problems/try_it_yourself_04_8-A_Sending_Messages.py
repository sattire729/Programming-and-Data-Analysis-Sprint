# 8-9 Sending Messages: Start with a copy of your program from 8-9. Write a function called send_messages() that prints each message and moves each message to a new list called sent_messages as its printed. After calling the function, print both of your lists to make sure the messages were moved correctly.

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)



messages = ['hello gng', 'wbu twin?', "I'm gay", 'Its today!', "I hate 'em"]
sent_messages = []
send_messages(messages, sent_messages)

print("\nThe updated lists are:")
print(messages)
print(sent_messages)
