matrix=[[1,2,3],
		[4,5,6],
		[7,8,9]]

#possible_indices=[[(i,j) for j in range(len(matrix))] for i in range(len(matrix)) ]

#for i,j in zip(range(len(matrix)),range(len(matrix))):

for i in range(len(matrix)):
	print()
	for j in range(len(matrix)):
		if(j<=i):
			print(matrix[i][j],end=" ")
