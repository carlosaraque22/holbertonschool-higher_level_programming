#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for listnames in names:
        if listnames[0] != "_":
            print("{}".format(listnames))
