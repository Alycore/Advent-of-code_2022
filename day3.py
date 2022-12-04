def main():
    all_common = []
    with open('day3_input.txt', 'r') as file:
        for l in file:
            sp = l.split()
            n = len(sp[0])
            part1 = sp[0][:n//2]
            part2 = sp[0][n//2:]
            common = set(part1).intersection(part2)
            all_common.append(' '.join(common))
    sum = 0
    for com in all_common :
        if com.isupper():
            #print("UPPER", com)
            sum+= ord(com) -64 +26
        else :
            #print(com)
            sum+= ord(com) -96
    
    print("Total:", sum)

def main2():
    all_common = []
    buffer = []
    with open('day3_input.txt', 'r') as file:
        for l in file:
            sp = l.split()
            buffer.append(sp[0])
            if len(buffer) == 3: #GROUP OF 3
                #print("Buffer :", buffer)
                common = set(buffer[0]).intersection(buffer[1]).intersection(buffer[2])
                #print("Common char :", common)
                all_common.append(' '.join(common))
                buffer = []
            '''else :
                print(" ")'''

    sum = 0
    for com in all_common :
        if com.isupper():
            sum+= ord(com) -64 +26
        else :
            sum+= ord(com) -96
    
    print("Total:", sum)

if __name__ == "__main__":
    main2()