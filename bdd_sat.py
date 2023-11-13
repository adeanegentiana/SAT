import re
import itertools
import fileinput

# for line in fileinput.input():
# 	inputString = line.rstrip()

f = open("testcases/input/input00.txt", "r")
inputString = f.read()

clause = re.split('\^', inputString) # lista de clause
# aici am facut lista de variabile si am eliminat duplicatele
varList = list(dict.fromkeys(list(filter(None, re.split('\)|V|~|\(|\^', inputString)))))
# apoi am sortat-o in functie de numar, crescator
varList.sort(key = int)

# Creez o lista care contine lin liste cu col elemente,
# initializate toate cu 0, pentru a imita o matrice.
col, lin = len(varList), len(clause)
Matrix = [[0 for x in range(col)] for y in range(lin)]
for j in range(0, lin):
	clausa = list(filter(None, re.split('\)|V|\(', clause[j])))
	for i in range(0, col):
		if varList[i] in clausa:
			Matrix[j][i] = 1
		elif "~" + varList[i] in clausa:
			Matrix[j][i] = -1
		else:
			Matrix[j][i] = 0


# clausa = list(filter(None, re.split('\)|V|\(', clause[0])))
# if root not in clausa:
# am eliminat clausele in care se afla aceasta variabila pentru ca sunt true
# newMatrix1 = [l for l in newMatrix if l[1] != 1]
# newMatrix2 = [l for l in newMatrix1 if l[2] != 1]
# newMatrix3 = [l for l in newMatrix2 if l[3] != 1]
# newMatrix4 = [l for l in newMatrix3 if l[4] != 1]
# newMatrix5 = [l for l in newMatrix4 if l[5] != 1]
# print(newMatrix5)




def recMatrix(Matrix, i):
	newMatrix = [l for l in Matrix if l[i] != 1]
	i += 1
	if i < col:
		recMatrix(newMatrix, i)
	else:
		print("Matricea returnata:")
		print(newMatrix)
		print("i = " + str(i))
		print("Numar variabile: " + str(len(varList)))
		return newMatrix



print(recMatrix(Matrix, 0))




f.close()
