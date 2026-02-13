import datetime
import time
import pygame

def set_alarm(alarm_time):
    sound="Alarm Clock.mp3"
    is_running = True
    while is_running:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time==alarm_time:
            print("""Wake up!
                     Wake up 
                     Wake up""")
            pygame.mixer.init()
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy(): # y isliy kia ha tky jb alarm 1 bar bj jyay to loop wahin khtm hojy
                is_running=False
        time.sleep(1)




# current_time=datetime.datetime.now().strftime("%H:%M:%S")
alarm_time=input("Enter alarm time: ")
set_alarm(alarm_time)


# for i in range(5, 0, -1):
#     print(i)
#     time.sleep(1)   # wait 1 second
# print("Boom!")



#print(datetime.datetime.now())
# print(datetime.datetime.now().strftime("%H:%M:%S"))