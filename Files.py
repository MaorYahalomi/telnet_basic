file = open("C:\Python27\sars.txt", "w")
strin = "hi world"
file.write(strin)
file = open("C:\Python27\sars.txt", "r")
i=0
for line in file:
    i+=1
file.close()

print "size of row in file", i