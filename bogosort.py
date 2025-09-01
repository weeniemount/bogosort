from random import *
from time import *
listtosort = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
sortedlist = sorted(listtosort)
shuffle(listtosort)
print (listtosort)
t = time()
while listtosort != sortedlist:
	shuffle(listtosort)
print('Done')
print('the time was --- %s seconds ---' % (time() - t))
print(listtosort)