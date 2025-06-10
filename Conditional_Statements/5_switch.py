month= int(input("Enter a month :"))

match(month):
    case 1|2|12:
        print("Winter")
    case 3|4|5:
        print("Spring")
    case 6|7|8:
        print("Summer")
    case 9|10|11:
        print("Fall")
    case _:
        print("Enter a valid month between 1 to 12")