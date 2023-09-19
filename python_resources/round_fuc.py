def round_more_5():
    y = 5.5
    X = round(y)
    print(f"X is {y} and X round is {X}".format(y, X))
    y = 5.42
    X = round(y, 1)
    print(f"If X.4 or less 5 round to down {y} to {X} with 1 decimal point.".format(y, X))


round_more_5()
