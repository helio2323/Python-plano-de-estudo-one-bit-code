# contagem regressiva e no final deve fazer um barulh "beep"
import os
import time
import sys

maxCount = 10
minCount = 1

def beep():
    sys.system("echo '\a'")
    sys.stdout.flush()


for i in range(maxCount):
    print(maxCount - i)
    time.sleep(0.5)
    if (maxCount - i) == minCount:
        beep()

number = int(input("Tabuada de: "))
begin = int(input("De: "))
end = int(input("Até: "))
x = begin
while x <= end:
    print(f"{number} x {x} = {number * x}")
    x = x + 1