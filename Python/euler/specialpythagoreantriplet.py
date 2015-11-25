def num_of_fac(num):
	count = 0
	for i in xrange(1, num / 2):
		if num % i == 0:
			count += 1
	return count + 1

def generate_triangles():
	num_list = []
	for i in xrange(60000000, 61000000):
		num_list.append(i)
		yield sum(num_list)

# for ele in generate_triangles():
# 	if num_of_fac(ele) > 500:
# 		print ele
# 		break

# for i in generate_triangles():
# 	print i
print num_of_fac(120000001)