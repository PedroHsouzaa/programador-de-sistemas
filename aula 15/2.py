matriz=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]
ctt = 0
for i in range(4):
    for j in range(4):
        if matriz[i][j]>=10:
            ctt += 1 
print(ctt)
