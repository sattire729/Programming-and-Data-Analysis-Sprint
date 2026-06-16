# 8-4 Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a small shirt with a different message.

def make_shirt(size='L', text='I love Python'):
    """
    Print a sentence summarizing the size of the shirt
    and the message printed on it.
    """
    print(f"The shirt size is {size} and the message is {text}.")

make_shirt('L')
make_shirt(size='M')
make_shirt(size='XXXL', text='I love Furina')