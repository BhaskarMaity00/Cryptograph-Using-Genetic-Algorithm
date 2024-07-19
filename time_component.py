from time import time
from statistics import mean
import aes_gen
import string
import random
N = int(input("Enter length of string: "))
text = ''.join(random.choices(string.ascii_uppercase + string.digits+string.ascii_lowercase+string.punctuation, k=N))
aes_gen_time = []
for i in range(0,10):
    flag = True
    try:
        init = time()
        aes_gen.main(text)
        aes_gen_time.append(time()-init)
    except:
        flag = False
    while(flag == False):
        try:
            init = time()
            aes_gen.main(text)
            aes_gen_time.append(time()-init)
            flag = True
        except:
            flag = False
            
file = open("Result.txt", "a")
content1 = f"\n{N} letters without genetic algo is: {mean(aes_gen_time):e}\n"
file.write(content1)
file.close()