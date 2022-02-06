def findPair(arr,n):
	flag=0
	for i in range(n):
		if arr[i]>0:
			for j in range(n):
				if -arr[i]==arr[j]:
					flag=1
					print(arr[i],-arr[i])
					break
	if flag==0:
		print("no pair exits")


arr=[3,7,-3,9,10,-8,8]
n=len(arr)
findPair(arr,n)