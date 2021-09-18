def midpoint():
    sarim = input("input x1 ")
    shaikh = input("input x2 ")
    mohammed = input("input y1 ")
    khalil = input("input y2 ")

    midpoint1 = (float(sarim)+float(shaikh))/2
    midpoint2 = (float(mohammed)+float(khalil))/2

    print(str(midpoint1) + "," + str(midpoint2))

QUESTION = input("do u want to calculate midpoint? YES or NO ")

QUESTION = QUESTION.lower()

if QUESTION == "yes":
    midpoint()


elif QUESTION == "no":
    print("ok, C U LATER")
