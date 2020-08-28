#removing duplicate using list

origin = [1,2,2,3,4,4,1,0]
duplicates=[]
new =[]
for x in origin:
  if x not in duplicates:
    new.append(x)
    duplicates.append(x)
print(new)

