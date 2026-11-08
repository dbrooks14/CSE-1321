# Class:CSE 1321L
# Section:B10
# Term:Fall 2026
# Instructor:Lan Vu
# Name:Dyllan Brooks
# Lab:8B
import time as t

timeStamp = int(input('Enter a timestamp in seconds: '))
print(f'Timestamp: {timeStamp}')
date = t.ctime(timeStamp)
print(f'Date and time: {date}')
pause = int(input('Enter pause length in seconds: '))
print('Waiting...')
t.sleep(pause)
print('Done!')