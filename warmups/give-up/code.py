a = [33,38,24,11,47,60,37,80,23,82,48,78,69,38,10,78,67,35,00,16,48,99,22,1,34,3,73,98,12,78,67,68,78,22,54,74,21,17,16,3,31,4,44,16,74,79,1]
print(''.join(map(str,a)))
done = False
while(not done):
	for o in range(0,255):
		#for i in range(1,len(a)):
		if (chr(a[i]+o) == 'f') and (i==0):
			print(o, 'f')
			break
		if (chr(a[i]+o) == 'l') and (i==1):
			print(o, 'l')
			break
		if (chr(a[i]+o) == 'a') and (i==2):
			print(o, 'a')
			break
		if (chr(a[i]+o) == 'g') and (i==3):
			print(o ,'g')
			break
		if (chr(a[i]+o) == '{') and (i==4):
			print(o, '{')
			done = True
			break


