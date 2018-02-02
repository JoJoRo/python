import random

# Basic solution, no pattern searching, of frogs-problem with random initial position
		
def frogCanMove(frogPosition,array):
	voidPosition=array.index('_')
	if (array[frogPosition]=='R'):
		return ((voidPosition-frogPosition)==1 or (voidPosition-frogPosition)==2)
	elif (array[frogPosition]=='L'):
		return ((frogPosition-voidPosition)==1 or (frogPosition-voidPosition)==2)
	else:
		return False
		
def orderArrayFrogs(array):
	global steps
	if (''.join(map(str,array))=='LLL_RRR'):
		return True
	for frogPosition in range(7):
		if (frogCanMove(frogPosition,array)):			
			newArray=array[:]
			voidPosition=newArray.index('_')
			newArray[frogPosition], newArray[voidPosition] = newArray[voidPosition], newArray[frogPosition]		
			if (orderArrayFrogs(newArray[:])):
				steps.append(newArray)
				return True
	return False


## MAIN ##

initialConfiguration=['R','R','R','_','L','L','L']
random.shuffle(initialConfiguration)
steps = list()
ans=orderArrayFrogs(initialConfiguration[:])
print('Initial conf: ',initialConfiguration)
if (ans == False):
	print('Solution not found')
else:
	steps.append(initialConfiguration)
	for step in steps[::-1]:
		print(step)
