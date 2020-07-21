
#利用range(9,-1,-1)建立一個list，名稱為lis1，並將順序由小到大排列，輸出最大值、最小值和總和
lis1 = list(range(9,-1,-1))
lis1.sort()
print("由小至大:",lis1)

total=lis1[0]+lis1[1]+lis1[2]+lis1[3]+lis1[4]+lis1[5]+lis1[6]+lis1[7]+lis1[8]+lis1[9]
print("總和:",total)

#pop會將數值移出陣列(list)
a=lis1.pop(0)
b=lis1.pop()
#print("最大值為:\n",a,"最小值為:",b)
print("最大值為:%s \n最小值為:%s"%(a,b))
print("lis1剩下的數字:",lis1)
