new_file = open("myfile.txt", "x")
fname = input('Enter the file name:')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There was', count, 'subject line in', fname)