import matplotlib.pyplot as plt

def lagrange(full_route, profile_route, file):
	interpolated_lagrange = []
	for k in range(0, profile_route[-1][0] + 1):
		value = 0
		for i in range(0, len(profile_route)):
			dividend = 1.0
			for j in range(0, len(profile_route)):
				if i != j:
					dividend *= float((k - profile_route[j][0]) / (profile_route[i][0] - profile_route[j][0]))
			value += profile_route[i][1] * dividend
		interpolated_lagrange.append(value)
	full_route_values = list(map(lambda x: x[1], full_route))
	plt.clf()
	plt.cla()
	name = f"graphs/{file}Lagrange{len(profile_route)}.png"
	plt.plot(range(0, len(interpolated_lagrange)), full_route_values[0:profile_route[-1][0] + 1], label="Profil wysokościowy")
	plt.plot(range(0, len(interpolated_lagrange)), interpolated_lagrange, label="Interpolowane wartości")
	plt.yscale('log')
	plt.legend()
	plt.xlabel("iteracja")
	plt.ylabel("Wysokość")
	plt.title("Lagrange - ilość próbek - " + str(len(profile_route)))
	plt.savefig(name)
	# plt.show()