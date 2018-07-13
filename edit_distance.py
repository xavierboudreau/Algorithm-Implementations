def printTable(table):
	for i in range(len(table)):
		for j in range(len(table[i])):
			print(table[i][j], "\t", end="")
		print("\n")
	
def diff(str1, str2, i,j):
	'''
	Returns 1 if two characters at indicies i-1 and j-1 in str1 and str2 are different
	and 0 if they are the same
	'''
	#adjust character position to reflect strings starting at 0 rather than 1
	if str1[i-1]==str2[j-1]:
		return 0
	return 1

def traceBack(pointers, str1, str2):
	'''
	Traces the pointers along the DAG to find the characters in the optimal edited strings
	'''
	m = len(str1)
	n = len(str2)
	returnString1 = ""
	returnString2 = ""
	next = pointers[m][n]
	current = (m,n)
	while (current!=(0,0)):
		if(current[0]-1==next[0] and current[1]-1==next[1]):
			returnString1 = str1[current[0]-1] + returnString1
			returnString2 = str2[current[1]-1] + returnString2
		elif(current[0]==next[0]):
			returnString1 = "-" + returnString1
			returnString2 = str2[current[1]-1] + returnString2
		else:
			returnString1 = str1[current[0]-1] + returnString1
			returnString2 = "-" + returnString2
		
		current = next
		next = pointers[current[0]][current[1]]
	return returnString1, returnString2
	
def editDistance(str1, str2):
	'''
	Finds the minimum cost alignment of two strings (str1, str2), where cost is
	defined as the number of columns in which the letters differ. 
	Runs in O(mn) where m and n are the lengths of str1 and str2.
	
	For example: one, none
	
	one-
	none 
	has cost 4
	
	-one
	none
	has cost 1
	'''
	m = len(str1)
	n = len(str2)
	costTable = [[0 for j in range(n+1)] for i in range(m+1)]
	pointerTable = [[(0,0) for j in range(n+1)] for i in range(m+1)]
	costTable[0][0] = 0
	for i in range(1,m+1):
		costTable[i][0] = i
		pointerTable[i][0] = (i-1,0)
	for j in range(1,n+1):
		costTable[0][j] = j
		pointerTable[0][j] = (0,j-1)
	for i in range(1, m+1):
		for j in range(1, n+1):
			#greedily choose whether to add '-' at each index combination
			costTable[i][j] = min(costTable[i-1][j]+1, costTable[i][j-1]+1, costTable[i-1][j-1] + diff(str1, str2, i,j))
			#process pointers
			if costTable[i][j] == costTable[i-1][j]+1:
				pointerTable[i][j] = (i-1, j)
			elif costTable[i][j] == costTable[i][j-1]+1:
				pointerTable[i][j] = (i, j-1)
			elif costTable[i][j] == costTable[i-1][j-1] + diff(str1, str2, i,j):
				pointerTable[i][j] = (i-1, j-1)	
			
	edited_string_1, edited_string_2 = traceBack(pointerTable, str1, str2)
	return costTable[m][n], edited_string_1, edited_string_2


if __name__ == '__main__':
	X = 'CATAAGCTTCTGACTCTTACCTCCCTCTCTCCTACTCCTGCTCGCATCTGCTATAGTGGAGGCCGGAGCAGGAACAGGTTGAACAG'
	Y = 'CGTAGCTTTTTGGTTAATTCCTCCTTCAGGTTTGATGTTGGTAGCAAGCTATTTTGTTGAGGGTGCTGCTCAGGCTGGATGGA'

	M1 = "EXPONENTIAL"
	M2 = "POLYNOMIAL"
	edit_distance, edited_string_1, edited_string_2 = editDistance(X, Y)
	print("edit distance is: " + str(edit_distance))
	print(edited_string_1)
	print(edited_string_2)