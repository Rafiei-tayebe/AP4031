n, m = map(int,input().split())
k = int(input())
Map = []
for i in range(n) :
    Map.append([])
    for j in range(m) :
        Map[i].append(0)
        
        ###

for i in range(k) :
    x, y = map(int,input().split())
    x, y = x - 1 , y - 1
    Map[x][y] = '*'
    
    for a in range(x-1,x+2) :
        for b in range(y-1,y+2):
            if n > a >= 0 and m > b >= 0 and Map[a][b] != '*' :
                Map[a][b] += 1

        ###
        
for i in range(n):
    for j in range(m):
        print(Map[i][j],end=" ")
    print()
