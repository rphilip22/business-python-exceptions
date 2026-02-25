while True:
    try:
        # Get inventory and threshold values from user input
        inventory = int(input("Enter current inventory level: "))
        threshold = int(input("Enter minimum reorder threshold: "))
        

        percentage = (inventory / threshold) * 100

        print("Inventory is", percentage, "% of the threshold.")

        if inventory < threshold:
            print("Reorder Alert: Inventory below threshold!")
        else:
            print("Inventory level is sufficient.")

        break

    # Handle potential exceptions for invalid input and division by zero
    except ValueError:
        print("Invalid input. Please enter whole numbers only.")

    except ZeroDivisionError:
        print("Threshold cannot be zero. Please enter a valid threshold.")