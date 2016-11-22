import math
import random
import pprint
import pylab
import os


def dist(x, y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return math.sqrt(d_x ** 2 + d_y ** 2)


def to_file(input_var):
	if os.path.isfile(filename):
		for root, dir, files in os.walk("."):
			print("root: {}".format(root))
			print("dir: {}".format(dir))
			print("files: {}".format(files))

	else:
		f = open(filename, 'w')
		for a in L:
			f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
		f.close()


L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
covering_density = 0.6
sigma_sq = covering_density / (len(L) * math.pi)
sigma = math.sqrt(sigma_sq)
delta = 0.1
n_steps = 1000
filename = 'disk_configuration_delta%i_sigma%.2f.txt' % (delta, sigma)


for steps in range(n_steps):
    a = random.choice(L)


    new_x = (a[0] + random.uniform(-delta, delta)) % 1.0
    new_y = (a[0] + random.uniform(-delta, delta)) % 1.0
    b = [(a[0] + random.uniform(-delta, delta)) % 1.0, (a[1] + random.uniform(-delta, delta)) % 1.0]


    min_dist = min(dist(b, c) for c in L if c != a)
    if not (min_dist < 2.0 * sigma):
        a[:] = b


to_file(L, )


# def show_conf(L, sigma, title, fname):
#     pylab.axes()
#     for [x, y] in L:
#         cir = pylab.Circle((x, y), radius=sigma,  fc='g')
#         pylab.gca().add_patch(cir)
#     pylab.axis('scaled')
#     pylab.title(title)
#     pylab.axis([0.0, 1.0, 0.0, 1.0])
#     pylab.savefig(fname)
#     pylab.show()
#     pylab.close()


# show_conf(L, sigma, 'test graph', 'one_disk.png')