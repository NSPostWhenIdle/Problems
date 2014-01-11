def volumeFromList(heights):

	volume = 0
	n = len(heights)
	last = 0

	for i in range(n):

		h = heights[i]

		if i > 0 and i < n - 1:
			if h < last:
				volume += last - h
			else:
				last = h	
		else:
			last = h

	return volume





lst = [2,5,1,2,3,4,7,7,6]

print volumeFromList(lst)