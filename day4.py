def main():
    count = 0
    with open('day4_input.txt', 'r') as file:
        for l in file:
            sp = l.split()
            div = sp[0].split(",")
            div1 = div[0].split("-")
            div2 = div[1].split("-")
            #print(div1, div2)
            if ((int(div1[0])<=int(div2[0])) and (int(div1[1])>=int(div2[1]))) or ((int(div1[0])>=int(div2[0])) and (int(div1[1])<=int(div2[1]))) :
                #print("IN RANGE", div1, div2)
                count += 1
            '''
            else :
                print("NOT IN RANGE", div1, div2)'''
    print("Total :", count)

def main2():
    count = 0
    with open('day4_input.txt', 'r') as file:
        for l in file:
            sp = l.split()
            div = sp[0].split(",")
            div1 = div[0].split("-")
            div2 = div[1].split("-")
            if ((int(div1[0])<=int(div2[0])) and (int(div1[1])>=int(div2[0]))) or ((int(div1[0])<=int(div2[1])) and (int(div1[1])>=int(div2[1]))) or ((int(div2[0])<=int(div1[0])) and (int(div2[1])>=int(div1[0]))) or ((int(div2[0])<=int(div1[1])) and (int(div2[1])>=int(div1[1]))):
                count += 1
    print("Total :", count)

if __name__ == "__main__":
    main2()