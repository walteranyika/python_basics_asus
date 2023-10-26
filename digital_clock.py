import time

#16:12:33 PM

# colle
#
while True:
    current_time = time.localtime()
    formatted_time = time.strftime("%H : %M : %S %p %a", current_time)
    print(formatted_time)
    time.sleep(1)