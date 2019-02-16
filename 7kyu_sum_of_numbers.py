# Sum of Numbers

def get_sum(a,b):
	if a > b:
		print(sum(range(b,a)) + a)
		return sum(range(b,a)) + a
	elif a < b:
		print(sum(range(a,b)) + b)
		return sum(range(a,b)) + b
	else:
		print(a)
		return a

get_sum(1,0) == 1		# 1 + 0 = 1
get_sum(1,2) == 1		# 1 + 2 = 3
get_sum(0,1) == 1		# 0 + 1 = 1
get_sum(1,1) == 1		# 1 Since both are same
get_sum(-1,0) == -1		# -1 + 0 = -1
get_sum(-1,2) == 2		# -1 + 0 + 1 + 2 = 2
get_sum(1,6) == 21		# 1 + 2 + 3 +4 +5 +6 = 21
