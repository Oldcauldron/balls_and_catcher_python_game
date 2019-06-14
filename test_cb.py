
import random
from settings_cb import Settings

sett = Settings()


def rand(a, b):
    num = round(random.random(), 2)
    print(num)

qw = []

for i in range(100):
    qw.append(sett.rand(-4, 4))
x = (sorted(list(set(qw))))
for i in x:
    print(i)



#