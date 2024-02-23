a=0
pmarks = ['.', '!', '?']
with open('input.txt', 'r') as f1, open('output.txt', 'w') as f2:
    lines=f1.readlines()
    for i in range(len(lines)):
        line = lines[0]
        line = line.split()
        print(line)
        for i in range(len(line)): 
            print(line[i][-1])
            if str(line[i][-1]) in pmarks:
                a+=1
            else:
                a+=0

    f2.writelines(str(a))
print(a)




