n = 3
num = [i for i in reversed(range(1, n+1))]

# for front in num:
# 	for back in num:
# 		print(front, back, front*back)




def tree(n):
	if(n<2):
		print("*")

	else:
		for i in range(2, n+1):	
			print("*" * (i*2-3))
		print("|")

	
tree(5)

# print(num)