numericString='76,0.945273,-47,0,65289413,6,28'
numericList=numericString.split(',')

mySum=0
numericList=numericString.split(',')
print(numericList)
for num in numericList:
    mySum+=float(num)
print("،The sum is equals to:" ,mySum)

print('='*40)
#Pythonic
print("Pythonic Output:", sum([float(num) for num in numericString.split(',')]))

