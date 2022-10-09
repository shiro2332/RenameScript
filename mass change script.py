#import module
import os

counter = 0
for file in os.listdir():
    if not file.endswith(".txt"):
        counter += 1
        os.rename(file, str(counter) + ".txt")