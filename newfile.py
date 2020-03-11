def nishi (x):
	if (x >= 1):
		return 1
	else:
		return 0

def _and (a, b):
	c = a + b
	if (c == 2):
		return 1
	else:
		return 0
		
def _or (a, b):
	c = a + b
	if (c == 0):
		return 0
	else:
		return 1
		
def _nor (a, b):
	c = a + b
	if (c==1):
		return 1
	else:
		return 0
		
def _nand (a, b):
	c = a + b
	if (c==1):
		return 0
	else:
		return 1

w1 = int(input())
w2 = int(input())
w1 = nishi(w1)
w2 = nishi(w2)

w3 = _or(w1, w2)
w4 = _and(w1, w2)
w5 = _or(w2, w3)
w6 = _nand(w4, w5)
print(w6)