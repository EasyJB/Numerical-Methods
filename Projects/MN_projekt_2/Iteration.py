import copy
import MatrixFunctions
#Metody odpowiedzialne za funkcje obliczające równania, na podstawie pseudokodu
def Jacobi(A,x,b,N):
	tmp = copy.deepcopy(x)
	for i in range (0,N):
		x[i] = b[i]
		for j in range(0,N):
			if i !=j:
				x[i] -= A[i][j] * tmp[j]
		x[i] = x[i]/A[i][i]


def GaussSeidel(A,x,b,N):
	for i in range(0, N):
		x[i] = b[i]
		for j in range(0, N):
			if i != j:
				x[i] -= A[i][j] * x[j]
		x[i] = x[i] / A[i][i]
#tworzenie macierzy L(OVER), U(PPER)
def LU_create(A,N):
	U = copy.deepcopy(A)
	L = MatrixFunctions.create_I(N)
	for i in range(0, N - 1):
		for j in range(i + 1, N):
			L[j][i] = U[j][i] / U[i][i]
			for o in range(i, N):
				U[j][o] -= L[j][i] * U[i][o]
	return U,L
#przeprowadzenie dekompozycji
def LU_decomposition(A,N,b):
	x=[0]*N
	U, L = LU_create(A, N)
	#Podstawianie w przód
	y = []
	y.append(b[0] / L[0][0])
	for i in range(1, N):
		sum = 0
		for j in range(0, i):
			sum += L[i][j] * y[j]
		y.append((b[i] - sum) / L[i][i])
	# Podstawianie w tył
	x[N - 1] = y[N - 1] / U[N - 1][N - 1]
	for i in range(N - 2, -1, -1):
		sum = 0
		for j in range(i + 1, N):
			sum += U[i][j] * x[j]
		x[i] = ((y[i] - sum) / U[i][i])
	return x