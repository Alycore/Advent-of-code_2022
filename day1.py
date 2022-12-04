def main():
    max = 0 
    tmp = 0
    with open('day1_input.txt', 'r') as file:
        for l in file:
            sp = l.split()
            if sp :
                #print(int(sp[0]))
                tmp += int(sp[0])
                if tmp > max :
                    max = tmp
            else :
                tmp = 0
    print('First :', max)

def main2():
    max = [] 
    tmp = 0
    with open('day1_input.txt', 'r') as file:
        for l in file:
            sp = l.split()
            if sp :
                tmp += int(sp[0])
            else :
                max.append(tmp)
                tmp = 0
    max.sort()
    print('First :', max[-1])
    print('Second :', max[-2])
    print('Third :', max[-3])
    print('Total :', max[-1]+max[-2]+max[-3])

if __name__ == "__main__":
    main2()