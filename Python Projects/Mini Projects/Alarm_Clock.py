# Stopwatch
# first implemented functionality is a stopwatch where user provides how long it should run for ,and it counts down in the terminal

from playsound import playsound
import time

# escape characters to make the stopwatch UI look better
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def stopwatch(seconds):

    time_elapsed = 0
    print(CLEAR) # get rid of the text in the terminal
    while time_elapsed < seconds: # run the loop until the countdown is over
        time.sleep(1) # stop for 1s to simulate time passing by, not very accurate if the stopwatch runs for a long time
        time_elapsed += 1
        time_left = seconds - time_elapsed # calculate the remaining time in order to work out how many seconds/minutes left
        minutes_left = time_left //60
        seconds_left = time_left %60

        print(f"{CLEAR_AND_RETURN} Stopwatch: {minutes_left:02d}:{seconds_left:02d}") # prints the current time in the terminal
    playsound("Music.mp3") # plays the alarm once the loop has stopped running

# asks the user how long the stopwatch should run for
minutes = int(input("Please enter the number of minutes the stop watch should run for:"))
seconds = int(input("Please enter the number of seconds the stop watch should run for:"))

# calculates total seconds in order to pass it to the function
total_seconds = minutes*60+seconds
stopwatch(total_seconds)