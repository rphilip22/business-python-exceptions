while True:
    #Ask user for profit and revenue amounts, calculate profit margin, and handle exceptions
    try:
        profit = float(input("Enter profit amount: "))
        revenue = float(input("Enter revenue amount: "))

        ratio = profit / revenue

    except ValueError:
        pass

    except ZeroDivisionError:
        pass

    else:
        percentage = ratio * 100
        print("Profit Margin:", percentage, "%")
        break