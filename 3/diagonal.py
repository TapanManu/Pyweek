matrix=[[1,2,3],
		[4,5,6],
		[7,8,9]]

#print diagonal elements of matrix
for i,j in zip(range(len(matrix)),range(len(matrix))):
	print(matrix[i][j],end=" ")
