# Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages()with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained it's messages.

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)



messages = ['hello gng', 'wbu twin?', "I'm gay", 'Its today!', "I hate 'em"]
sent_messages = []
send_messages(messages[:], sent_messages)

print("\nThe updated lists are:")
print(messages)
print(sent_messages)