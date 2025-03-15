import datetime
import time

print('<-------------------------------------------->')
print('This is a command line timer ')
#print('choose one option')
print('1. Countdown Timer')
print('2. StopWatch')
response = int(input('choose one option: '))

if response == 1:
    def countdown(h, m, s):
        total_seconds = h*3600+m*60+s
        while total_seconds > 0:
            timer = datetime.timedelta(seconds=total_seconds)
            print(timer)
            time.sleep(1)
            total_seconds-=1
        print('Timer has ended')
    h = int(input('Enter the hours: '))
    m = int(input('Enter the minutes: '))
    s = int(input('Enter the seconds: '))

    countdown(h,m,s)
elif response == 2:

    def timer():
        start_time = time.time()
        end_time = start_time
        lap_num = 1
        value = " "
        while value.lower() != 'q':
            value = input()
            lap_time = round((time.time()-end_time), 2)
            total_time = round((time.time()-start_time), 2)

            print('lap no. '+str(lap_num))
            print('total time: '+str(total_time))
            print('Lap time'+str(lap_time))
            print("*"*20)

            end_time = time.time()
            lap_num+=1
        print("Exercise complete ")

    timer()
