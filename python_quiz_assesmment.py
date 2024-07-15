import numpy as np
f = open("C:/Users/vinil jn/OneDrive/Desktop/MYpython/file.txt")
q = f.readlines()
f.close()

a =[]
b =[]
for e in q:
    c = e.split(',')
    print(f'Q.{c[0]}')
    print(f'1.{c[1]}')
    print(f'2.{c[2]}')
    print(f'3.{c[3]}')
    a.append(int(c[4]))
    print('Enter your option: ')
    opt = int(input(' '))
    b.append(opt)

print(a)
print(b)
r = list((np.array(a)) == (np.array(b)))
s = r.count(True)
print(f'{s}/{len(q)} is your score')

i = 0
while i < len(r):
    if r[i] == False:
        col = q[i].split(',')
        print(f'For the question {c[0]}, the right option is {4}')
    i+=1
