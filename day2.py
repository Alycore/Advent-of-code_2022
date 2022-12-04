"""Note score :
A/X : 1 (rock)
B/Y : 2 (paper)
C/Z : 3 (scissors)

Win : 6
Lose : 0
Draw : 3"""

def main():
    score = 0
    with open('day2_input.txt', 'r') as file:
        for l in file:
            sp = l.split()
            me = ord(sp[1])-87
            you = ord(sp[0])-64
            print(me,you)
            # BASE SCORE 
            score += me

            # DRAW
            if ((ord(sp[0])-64) == (ord(sp[1])-87)):
                score += 3
                print("DRAW")
            else: #LOSE
                if ((me==1) and (you==2)) or ((me==2) and (you==3)) or ((me==3) and (you==1)) :
                    score += 0
                    print("LOSE")
                else:
                    score += 6
                    print("WIN")
            print("New score :", score)

    print('Total score :', score)


def main2():
    score = 0
    with open('day2_input.txt', 'r') as file:
        for l in file:
            sp = l.split()
            cond = ord(sp[1])-87
            you = ord(sp[0])-64
            #print(you, cond)

            if cond==1 :
                score+= 0 + (((you-1)-1)%3 + 1)
                print("LOSE", (((you-1)-1)%3 + 1))
            else :
                if cond == 2 :
                    score+= 3 + you
                    print("DRAW", you)
                else :
                    score+= 6 + (((you-1)+1)%3 + 1)
                    print("WIN", (((you-1)+1)%3 + 1))

    print('Total score :', score)

if __name__ == "__main__":
    main2()