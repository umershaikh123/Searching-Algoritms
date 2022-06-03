T = [(1,25,2) , (3,15,4) , (5,50,6)]

root = 25
x = 15
node = root
n = 1
p = 0

for i in range (len(T)):
    if(x > node):
        n = T[i+2][2]
        node = T[i+2][1]