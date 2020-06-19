import random

s= "Abcdefghijkl\
     lmonpqrstuvwxyz1234\
     567890ABCDEFGHIJKLM\
     NOPQRSTUVWXYZ\ "


passwordlen=16
password="".join(random.sample(s,passwordlen))
print(password)
