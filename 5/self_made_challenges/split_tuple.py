#  mini challenge ! find positive numbers with more than one digit and split the number each into individual digits
# of a tuple
#(1,2,3,4,555)
#(1,2,3,4,5,5,5)
import math
def split_number(num):
	temp=[int(x) for x in str(num)]
	return temp

t=(1,2,34,45,22,14,8,456,77)
count = list(map(lambda x:int(math.floor(math.log(x,10)+1)),list(t))) #count number of digits of each element
lst = list(t)
new=[y for x in lst for y in split_number(x) ]
print(t)		#original tuple
print(tuple(new))	#split tuple
