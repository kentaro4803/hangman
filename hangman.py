def hangman(word):
    wrong=0
    stages=["",
            "_____     ",
            "|         ",
            "|    |    ",
            "|    O    ",
            "|   )|(   ",
            "|   / /   ",
            "|         ",
            ]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("Welcome to hangman!")

    while wrong<len(stages)-1:
        print("\n")
        msg="Guess one charactor:"
        char=input(msg)
        if char in rletters:
            cind=rletters.index(char)#同じ文字が複数あっても一つしか取り出せない
            board[cind]=char
            rletters[cind]="$"#正解した文字を＄に置き換える
        else:
            wrong+=1
        print("".join(board))
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win!")
            print("".join(board))
            win=True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose!The answer is {}".format(word))

hangman("iphone")
    
