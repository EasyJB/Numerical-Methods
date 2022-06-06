#mnożenie macierzy i wektra ze wzoru
def matrix_vector(x,A):
	result = []
	for i in range(len(A[0])):
		tmp = 0
		for j in range(len(x)):
			tmp+=A[i][j]*x[j]
		result.append(tmp)
	return result
#odejmowanie 2 wektorów
def vectorSub(v,r):
	result = []
	for i in range(len(v)):
		tmp = v[i]-r[i]
		result.append(tmp)
	return result
#obliczanie błędu residuum na podstawię normy 2
def sumVector(v):
	sum=0
	for i in v:
		sum+=(i**2)
	return sum**0.5
#tworzenie macierzy jednostkowej (I), z jedynkami na diagonali
def create_I(N):
	tmp = []
	for i in range(N):
		tmp.append([0]*N)
		tmp[i][i]=1
	return tmp

