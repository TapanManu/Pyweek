#removing duplicate using list

origin = [1,2,2,3,4,4,1,0]
duplicates=[]
new =[]
for x in origin:
  if x not in duplicates:
    new.append(x)
    duplicates.append(x)
print(new)

#given a string ,print only unique values in that string(any order)
#and print number of combinations of output

str="1001001023241441011101010"
list=[x for x in str]
s = set(list)
print(''.join(s)) 

#recursive function for factorial
'''
def fact(x):
	if(x<=1):
		return x
	return fact(x-1)
	'''
#print(fact(len(s)))

#or use loops

i=1
fact=1
for i in range(1,len(s)+1):
	fact=fact*i

print("no of combinations of output",fact)


