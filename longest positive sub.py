# Given an array of integers, print out the longest sequence of positive integers.  For example, given {6, 12, 8, 9,-1, 2, 3, -4, -3, -5, 4, 5,6,7,8}, print out {4，5，6，7，8}

array=[6, 12, 8, 9,-1, 2, 3, -4, -3, -5, 4, 5,6,7,8]
def longestPositive(array):
	result=[]
	final=[]
	for i in range(0,len(array)):
		if array[i]>0:
			result.append(array[i])
		if array[i]<0 or i==(len(array)-1): #Attention to "i==(len(array)-1)"!!!!!!
			final.append(result) #put the all of the right subarray into format like :[[6, 12, 8, 9], [2, 3], [], [], [4, 5, 6, 7, 8]]
			result=[]
	maxi =0
	maxlen=0 #really need max i and max len....
	for i in range(0,len(final)):
		if len(final[i])>maxlen:
			max=i
			maxlen=len(final[i])
	return(final[max])
	
print(longestPositive(array))
