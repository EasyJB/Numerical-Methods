import copy
from Matrix_methods import MatrixFunctions, Methods_for_solving
import matplotlib.pyplot as plt
#Functions to use in splyne method

def matrix_Create(MAT):

	n= len(MAT)
	ANS = []
	res = [0]*4*(len(MAT)-1)
	for i in range(4*(n-1)):
		ANS.append([0]*(4*(n-1)))
	for i in range(len(MAT)-1):
		ANS[i*2][i*4] =1
		res[i*2]=MAT[i][1]
		res[i*2+1]=MAT[i+1][1]
		h=1
		for j in range (4):
			ANS[i*2+1][j+i*4] = 1 * h
			h *= MAT[i + 1][0] - MAT[i][0]
	for i in range(len(MAT) - 2):
		h = 1
		for j in range(1,4):
			ANS[2*i+2*(n-1)] [i*4 + j] = j * h
			h *= MAT[i + 1][0] - MAT[i][0]
		ANS[2*i+2*(n-1)] [(i+1) * 4 + 1] -= 1
		h = 1
		for j in range(2,4):
			ANS[2 * (n - 1) + 2 * i+1][i*4+j] = j*(j-1) * h
			h *= MAT[i + 1][0] - MAT[i][0]
		ANS[2 * (n - 1) + 2*i+1][(i+1)*4 + 2] -= 2
	ANS[-2][2] = 2
	ANS[-1][-2] = 2
	ANS[-1][-1] = 6 * (MAT[-1][0] - MAT[-2][0])
	return ANS,res


def pivoting(MAT, b):
	m = len(MAT)
	L = MatrixFunctions.create_I(m)
	P = MatrixFunctions.create_I(m)
	U = copy.deepcopy(MAT)
	r = copy.deepcopy(b)
	for k in range(m-1):
		pivot = abs(U[0][k])
		ind = 0
		for i in range(k,m):
			if abs(U[i][k])>pivot:
				pivot = abs (U[i][k])
				ind = i

		U[k][k:m], U[ind][k:m] = U[ind][k:m], U[k][k:m]

		L[k][:k],L[ind][:k] = L[ind][:k],L[k][:k]

		P[k],P[ind] = P[ind],P[k]

		for j in range(k+1,m):
			L[j][k] = U[j][k]/U[k][k]
			for z in range(k,m):
				U[j][z] -= L[j][k] * U [k][z]

	r = MatrixFunctions.matrix_vector(b, P)
	x = Methods_for_solving.LU_decomposition(U, L, m, r)
	return x


#solve with splyne method
def splyne(full_route, profile_route,file):
	tab, b = matrix_Create(profile_route)
	x = pivoting(tab, b)
	interpolated_splyne = []

	for i in range(profile_route[-1][0]):
		sum = 0.0
		for j in range(len(profile_route)):
			if profile_route[j][0] <= i <= profile_route[j + 1][0]:
				for k in range(4):
					sum += x[j * 4 + k] * (i - profile_route[j][0]) ** k
				interpolated_splyne.append(sum)
				break
	#Creating graph for visualization
	full_route_values = list(map(lambda x: x[1], full_route))
	name = f"graphs/{file}Splyne{len(profile_route)}.png"
	plt.clf()
	plt.cla()
	plt.plot(range(0, len(interpolated_splyne)), full_route_values[0:profile_route[-1][0]], label="Profil wysokościowy")
	plt.plot(range(0, len(interpolated_splyne)), interpolated_splyne, label="Interpolowane wartości")
	plt.xlabel("iteracja")
	plt.ylabel("Wysokość")
	plt.title("Splyne - ilość próbek - " + str(len(profile_route)))
	plt.legend()
	plt.savefig(name)


