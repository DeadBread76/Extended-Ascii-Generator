import random
import string

ascii = ""

for x in range(1985):
    num = random.randrange(13000)
    ascii = ascii + chr(num)
print (ascii)

