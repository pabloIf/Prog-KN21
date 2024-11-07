from datetime import datetime

while (True):
    print("Time: 1 \nExit: 0")
    i = "Input num:";
    user_input = int(input(i))
    if user_input == 1:
        now = datetime.now()
        print("Time now: ", now,  "\n\n\n")
    else:
        break
