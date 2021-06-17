input_day = input("Enter the day the call started at: ")
input_time = input("Enter the time the call started at (hhmm): ")
duration = int(input("Enter the duration of the call (in minutes): "))

int_input_time = 0 

if input_time[0] == '0':
    input_time = int(input_time[1:])
else:
    input_time = int(input_time)

rate = 0.0

if input_day == "Sat" or input_day == "Son":
    rate = 0.15
elif input_day == "Mon" or input_day == "Tue" or input_day == "Wed" or input_day == "Thr" or input_day == "Fri":
    if input_time >= 800 <= 1800:
        rate = 0.40
    else:
        rate = 0.25

total_price = rate * duration

print("this call will cost", total_price)