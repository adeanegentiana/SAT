import re
import itertools
import fileinput

for line in fileinput.input():
	inputString = line.rstrip()

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

# creez un tabel de adevar pentru variabilele mele
tabel = [list(i) for i in itertools.product([0, 1],repeat=len(varList))]

def testInterpretare(t):
	for linie in Matrix:
		ok = 0
		for i in range(0, col):
			if  linie[i] == 1 and t[i] == 1:
				ok = 1
			elif linie[i] == -1 and t[i] == 0:
				ok = 1
		# daca o singura clausa este falsa, toata formula va returna fals
		if ok == 0:
			return "False"
	return "True"

def simpleSAT():
	# testez formula pentru fiecare interpretare
	for t in tabel:
		# daca gasesc o singura interpretare pentru care formula mea este
		# adevarata, returnez 1
		if testInterpretare(t) == "True":
			return 1
	# daca am testat toate interpretarile si niciuna nu returneaza true,
	# returnez 0
	return 0

print(simpleSAT())