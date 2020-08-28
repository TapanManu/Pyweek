#removing duplicate using list

origin = [1,2,2,3,4,4,1,0]
duplicates=[]
new =[]
for x in origin:
  if x not in duplicates:
    new.append(x)
    duplicates.append(x)
print(new)

#fibonacci with recursion specified with count 

def fibonacci(x):
  if(x<=1):
    return x
  return fibonacci(x-1)+fibonacci(x-2)

for i in range(5):
  print(fibonacci(i))

