import os
print("Enter Your First Filename")
firstFile = raw_input()
if os.path.isfile(firstFile):
	if os.path.splitext(firstFile)[1] !="exe":
		print("Enter Your Second Filename")
		secondFile = raw_input()
		if os.path.isfile(secondFile):
			if os.path.splitext(secondFile)[1] !="exe":
				file = open(firstFile,"r")
				first = file.read()
				file2 = open(secondFile,"r")
				second = file2.read()
				if os.stat(firstFile).st_size == os.stat(secondFile).st_size:
					i = 0
					while i < len(first):
						if i == len(first)-1:
							print("Files Are The Same")
							break
						if first[i] != second[i]:
							print("Files Are Not Same")
							break
						i +=1
				else:
					print("Files Are Not Same")			
			else:
				print("Ups.I Can't Read This File")
		else:
			print("Ups.Only Files Enabled")		
	else:
		print("Ups.I Can't Read This File")
else:
	print("Ups.Only Files Enabled")

