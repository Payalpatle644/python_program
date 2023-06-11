file=open("File.txt", 'r')

reader=file.readlines()

lines_count =0

word_count=0

for lines in reader:

   lines_count+=1

   for word in lines:

       word_count+=1

print(f"There are {lines_count} lines and {word_count/8} byte data in {file.name}" )