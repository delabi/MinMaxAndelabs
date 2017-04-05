def find_max_min(l):
	list_a = l

	maxNo = max(list_a)
	minNo = min(list_a)

	if maxNo == minNo:
		return [len(list_a)]
	return [minNo, maxNo]

# numbers = [23, 1, 23, 34, 13, 343,23343, 2324,12,3,11,]
# find_max_min(numbers)