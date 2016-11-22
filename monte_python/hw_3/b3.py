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


def to_file(input_var, N):
	line_counter=0
	if os.path.isfile(filename):
		f = open(filename, 'r')
		for line in f:
		    a, b = line.split()
		    input_var.append([float(a), float(b)])
		    line_counter+=1
		f.close()
	while(N>line_counter):
		line_counter+=1
		input_var.append([random.uniform(25, 75), random.uniform(25, 75)])
	f = open(filename, 'w')
	for a in input_var:
		f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
	f.close()


def get_info_from_init_conf(filename):
	output =[]
	f = open(filename, 'r')
	for line in f:
		a, b =line.split()
		output.append([float(a), float(b)])
	return output


def show_conf(L, sigma, title, fname):
	pylab.axes()
	for [x, y] in L:
		cir = pylab.Circle((x, y), radius=sigma,  fc='g')
		pylab.gca().add_patch(cir)
	pylab.axis('scaled')
	pylab.title(title)
	pylab.axis([0.0, 1.0, 0.0, 1.0])
	pylab.savefig(fname)
	pylab.show()
	pylab.close()

L = []
N=64
filename = 'disk_configuration_N%i.txt' % (N)

for i in range(0, 10):
	to_file(L, N)
	L.extend(get_info_from_init_conf(filename))

covering_density = 0.42
sigma_sq = covering_density / (len(L) * math.pi)
sigma = math.sqrt(sigma_sq)
delta = 0.3
n_steps = 10000

for steps in range(n_steps):
    a = random.choice(L)
    new_x = (a[0] + random.uniform(-delta, delta)) % 1.0
    new_y = (a[0] + random.uniform(-delta, delta)) % 1.0
    b = [(a[0] + random.uniform(-delta, delta)) % 1.0, (a[1] + random.uniform(-delta, delta)) % 1.0]
    min_dist = min(dist(b, c) for c in L if c != a)
    if not (min_dist < 2.0 * sigma):
        a[:] = b

img_name="disks_N=%i.png" % (N)
graph_name="N=%i" % (N)
show_conf(L, sigma, graph_name, img_name)