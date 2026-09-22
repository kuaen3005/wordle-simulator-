import random , re , sys, os
from colors import WHITE , GREEN , YELLOW

with open ("words.txt" , "r") as view:
    words = [w.upper().strip() for w in view]
wordle_list = [i for i in words if (len(i) == 5 and i.isalpha()) ]

def main():
    print("HINT: " , "To play Wordle, guess a 5-letter English word " , sep = "\n")
    print("You have to rely on the color of the tiles to know:")
    print("🟩: correct letter, correct position","🟨: correct letter, wrong position ","⬜: letter not in the word" , sep = "\n")
    print("let's start!")
    while(True):
        wordle()
        print("\nPlay again?", "1: Yes" , "2: No" , sep = "\n")
        continues = input()
        if not(continues == "1"):
            sys.exit("GOOD BYE!")


def wordle():
    real_word = random.choice(wordle_list)
    incorrect_letters = []
    words = []
    states = []
    remain = 0

    while(remain < 6):
        if(remain >= 1):
            os.system('clear')
            print("incorrect letters: " , end = "")
            print(*incorrect_letters , sep = ", ")
            for x in range(remain):
                for i in range(5):
                    y = states[x][i]
                    if(y == "v"):
                        GREEN(i , words[x])
                    elif(y == "."):
                        YELLOW(i , words[x])
                    else:
                        WHITE(i , words[x])

        word = type_word()
        words.append(word)
        state = check_word(word , real_word , incorrect_letters)
        states.append(state)
        if(state == "vvvvv"):
            print("YOU WIN!")
            break
        remain += 1
    if(remain == 6):
        print("YOU LOSE" , f"The word is: {real_word}" , sep = "\n")


def type_word():
    while(True):
        temp = input("Your word: ")
        word = re.search(r"[a-zA-Z]{5}" , temp)
        if(word):
            temp = temp.upper()
            if(temp in wordle_list):
                 return temp
            else:
                print("Word no found")
        print("Type again!")


def check_word(word , real_word, incorrect_letters = list):
    t = {}
    num = {}
    ans =""
    for i in range(5):
        t[word[i]] = 0
        num[real_word[i]] = 0
    for i in range(5):
        if not(word[i] == real_word[i]):
            num[real_word[i]] += 1

    for i in range(5):
        if(word[i] == real_word[i]):
            ans +="v"
        elif(word[i] in real_word):
            if(t[word[i]] + 1 <= num[word[i]]):
                t[word[i]] += 1
                ans +="."
            else:
                ans +="x"
        else:

            if not(word[i] in incorrect_letters):
                incorrect_letters.append(word[i])
            ans +="x"
    return ans

if __name__ == "__main__":
    main()

