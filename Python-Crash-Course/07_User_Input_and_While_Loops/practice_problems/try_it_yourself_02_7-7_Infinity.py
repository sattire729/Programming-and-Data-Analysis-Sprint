# 7-7 Infinity: Write a loop that never ends, and run it.

x = 1
while x <= 3:
    if x == 1:
        x += 1
    else:
        x -= 1
    
    print(x)