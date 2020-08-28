#reverse a string without built in function
'''
str="hello world"
rev=""

for i in range(len(str)-1,-1,-1):
	rev = rev+str[i]

print(rev)
'''

#prime number

'''
start=1
end=10

for i in range(start,end):
	flag=False
	for j in range(2,i):
		if(i%j==0):
			flag=True
	if(flag==False):
		print(i,)

'''

#string without vowels
'''
string = "string contains vowels"

for s in string:
	if s not in 'aeiou':
		print(s)

'''


