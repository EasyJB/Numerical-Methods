import csv
def route_init (name):
	full_route = []
	directory_for_data = 'data_init/2018_paths/'
	with open(f'{directory_for_data}{name}.csv', 'r') as file:
		tmp = 0
		reader = csv.reader(file)
		next(reader)
		for row in reader:
			full_route.append(tuple((tmp, float(row[1]))))		# tmp - point to show order
			tmp+=1
	return full_route
