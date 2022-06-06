import time
import math
import Iteration
import MatrixFunctions
import matplotlib.pyplot as plt
#Inicjalizacja danych
f = 4
N = 900+30+8
A = []
b = [0]*N
x = [1]*N
time_lu = []
time_gaus = []
time_jacobi = []
list_n = [100,500,1000,2000,3000]
def dataInit(N):
	global A,b,x
	A = []
	b = [0] * N
	x = [1] * N
	for i in range(0, N):
		A.append([0]*N)
	for i in range(0, N):
		A[i][i] = float(14)
	for i in range(1, N):
		A[i-1][i] = float( -1)
		A[i][i-1] = float( -1)
	for i in range(2, N):
		A[i-2][i] = float( -1)
		A[i][i-2] = float( -1)
	for i in range(0, len(b)):
		b[i] = math.sin((i+1) * (f+1))
#Złe dane oznaczają 3na diagonali (nie zbieżne dla iteracyjnych)
def wrongDataInit(N):
	global A, b, x
	A = []
	b = [0] * N
	x = [1] * N
	for i in range(0, N):
		A.append([0] * N)
	for i in range(0, N):
		A[i][i] = 3
	for i in range(1, N):
		A[i - 1][i] = float( -1)
		A[i][i - 1] = float( -1)
	for i in range(2, N):
		A[i - 2][i] = float( -1)
		A[i][i - 2] = float( -1)
	for i in range(0, len(b)):
		b[i] = math.sin(i * (f + 1))

dataInit(N)
#Najpierw wykonywanie programu dla zadań A-D, czyli dla N=938
print("=======Jacobi========")
dataInit(N)
r = 1
k = 0
start = time.time()
while r > 10**(-9) and r<10**12 :
	k += 1
	Iteration.Jacobi(A, x, b, N)
	r = MatrixFunctions.sumVector(MatrixFunctions.vectorSub(MatrixFunctions.matrix_vector(x,A),b))
end = time.time()
if(r>10**12):
	print("Brak zbieżności")
else:
	print("Liczba iteracji: ", k)
print("Czas trwania: ",end-start)
# operacje odpowiedzalne za GS
print("=======Gauss-Seidel========")
dataInit(N)
r = 1
k = 0
start = time.time()
while r > 10**(-9) and r<10**12:
	k += 1
	Iteration.GaussSeidel(A, x, b, N)
	r = MatrixFunctions.sumVector(MatrixFunctions.vectorSub(MatrixFunctions.matrix_vector(x,A),b))
end = time.time()
if(r>10**12):
	print("Brak zbieżności")
else:
	print("Liczba iteracji: ", k)
end = time.time()
print("Czas trwania: ", end-start)
#operacje odpowiedzalne za LU
print("=======LU=======")
dataInit(N)
start = time.time()
x = Iteration.LU_decomposition(A,N,b)
print("Norma residuum: ",MatrixFunctions.sumVector(MatrixFunctions.vectorSub(MatrixFunctions.matrix_vector(x,A),b)))
end = time.time()
print("Czas trwania: ", end-start)
print("======DZIALANIA DLA 500...3000======")
for i in range(len(list_n)):
	N = list_n[i]
	# operacje odpowiedzalne za Jacobiego
	print("=======Jacobi========")
	dataInit(N)
	r = 1
	k = 0
	start = time.time()
	while r > 10**(-9):
		k += 1
		Iteration.Jacobi(A, x, b, N)
		r = MatrixFunctions.sumVector(MatrixFunctions.vectorSub(MatrixFunctions.matrix_vector(x,A),b))
	end = time.time()
	time_jacobi.append(end-start)
	print("Czas trwania: ",end-start)
	print("Liczba iteracji: ",k)
	# operacje odpowiedzalne za GS
	print("=======Gauss-Seidel========")
	dataInit(N)
	r = 1
	k = 0
	start = time.time()
	while r > 10**(-9):
		k += 1
		Iteration.GaussSeidel(A, x, b, N)
		r = MatrixFunctions.sumVector(MatrixFunctions.vectorSub(MatrixFunctions.matrix_vector(x,A),b))
	end = time.time()
	time_gaus.append(end - start)
	print("Czas trwania: ", end-start)
	print("Liczba iteracji: ", k)
#operacje odpowiedzalne za LU
	print("=======LU=======")
	dataInit(N)
	start = time.time()
	x = Iteration.LU_decomposition(A,N,b)
	print("Norma residuum: ",MatrixFunctions.sumVector(MatrixFunctions.vectorSub(MatrixFunctions.matrix_vector(x,A),b)))
	end = time.time()
	time_lu.append(end - start)
	print("Czas trwania: ", end-start)
#wykres
plt.plot(  list_n,time_lu, label = "LU")
plt.plot(  list_n,time_jacobi, label = "Jacobi")
plt.plot(  list_n,time_gaus, label = "Gauss_Seidel")
plt.legend()

plt.yscale('log')
plt.show()
plt.savefig('time.png')