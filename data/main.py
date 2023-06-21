import re
#read a fila with bch extension
#read the file with bch extension
file = open("./benchmarks/optim/easy/ackley_5.bch", "r")
list = []
for line in file:
    #print(line)
    #extract only the characters with x with numbers using a regex
    regex = re.compile(r'x\d+')
    #use the regex on lines
    matches = regex.finditer(line)
    for match in matches:
        #print(match.group(), "found at", match.start(), "-", match.end())
        # save all the matches in a list but not repeated
        if match.group() not in list:
             list.append(match.group())
        
print(list)
print(len(list))