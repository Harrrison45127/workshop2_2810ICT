import sys
import string

words = sys.stdin.read().split()

dict = {}
arr = []
arrCount = []
percentages = []


for word in words:
    if word not in dict:
        #print('hit')
        dict[word] = 1
    else:
        dict[word] += 1

for word in words:
    if word not in arr:
        arr.append(word)
        arrCount.append(1)
    else:
        arrCount[arr.index(word)] += 1



for i in arrCount:
    percentages.append(int(((i/sum(arrCount))*100)//1))  

for i in range(len(arr)):
    index = arrCount.index(max(arrCount))
    padding = ''
    for i in range(10 -len(arr[index])):
        padding += ' '
    stars = '['
    for i in range(arrCount[index]):
        stars += '**'
    stars += ']'
    print(arr[index].upper(),padding,stars,percentages[index],'%') #arrCount[index]
    
    del arr[index]
    del arrCount[index]







#print(dict)
#sortedDict = sorted(dict.items(), key=lambda x:x[1])
#print(sortedDict)
#print(sortedDict.keys())



    
