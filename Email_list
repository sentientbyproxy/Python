# A program designed to pull e-mail data from a text file,
# written in Python 2.7.12.

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0 : continue 
    if words[0] != 'From' : continue
    count = count + 1
    print words[1]
	
print "There were", count, "lines in the file with From as the first word"
