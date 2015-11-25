#http://www.codechef.com/problems/DCE05/
#!/urs/bin/env python3
count = 1
for i in range(int(input())):
	app_list  = range(1, int(input()) + 1)
	my_dict = dict(enumerate(app_list))
	while len(my_dict) > 1:
		for keys, values in my_dict.items():
			if values % 2 == 0:
				del my_dict[keys]
		for k, v in my_dict.items():
			my_dict[k] = count
			count += 1
print(int(str(my_dict.keys())[1:-1])) 