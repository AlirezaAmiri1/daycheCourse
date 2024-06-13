import sys
l1=list(range(10))
l2=[0,1,2,3,4,5,6,7,8,9]
print(sys.getsizeof(l1)==sys.getsizeof(l2))
print(f'l1:{sys.getsizeof(l1)}, l2:{sys.getsizeof(l2)}')