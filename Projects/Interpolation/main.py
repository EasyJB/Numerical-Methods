from interpolation_methods import Lagrange, Splyne
from data_init import Data_init

if __name__ == '__main__':
	profile_points = [50, 25, 10, 5, 2]
	files = ['WielkiKanionKolorado','SpacerniakGdansk','MountEverest']
	for file in files:
		for points in profile_points:
			full_route = Data_init.route_init(file)
			profile_route = full_route[::points]
			Lagrange.lagrange(full_route, profile_route, file)
			Splyne.splyne(full_route, profile_route, file)
