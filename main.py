# Program make a simple calculator

# import the functinos for the calculation
import calculation_functions as cal

# make the logger
import logging
def makeLogger():
    # setting the log file path
    logFilePath = "./output.log"

    # setting the logger and formatter
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(u"%(asctime)s [%(levelname)8s] %(message)s")

    #--- handler for Streaming Logging
    #streamingHandler = logging.StreamHandler()
    #streamingHandler.setFormatter(formatter)

    fileHandler = logging.FileHandler(logFilePath)
    fileHandler.setFormatter(formatter)

    # logger.addHandler(streamingHandler) # Add handler for Streaming logging
    logger.addHandler(fileHandler)
    return logger


logger = makeLogger()
startMsg = "============Start the Program============"
endMsg = "============Finish the Program============"
cur_version = "1.3.1"

logger.info(startMsg)
# Print current version.
print("< Calculator Ver.", cur_version, ">")
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 


while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", cal.add(num1, num2))
            msg = "Result: " + str(num1) + " + " + str(num2) + " = " + str(cal.add(num1, num2))
            logger.info(msg)

        elif choice == '2':
            print(num1, "-", num2, "=", cal.subtract(num1, num2))
            msg = "Result: " + str(num1) + " - " + str(num2) + " = " + str(cal.subtract(num1, num2))
            logger.info(msg)

        elif choice == '3':
            print(num1, "*", num2, "=", cal.multiply(num1, num2))
            msg = "Result: " + str(num1) + " * " + str(num2) + " = " + str(cal.multiply(num1, num2))
            logger.info(msg)
            
        elif choice =='4':
            if cal.divide(num1, num2) != "error":
                print(num1, "/", num2, "=", cal.divide(num1,num2))
                msg = "Result: " + str(num1) + " / " + str(num2) + " = " + str(cal.divide(num1, num2))
                logger.info(msg)
            else:
                print("[Error] Cannot be Divided by Zero !")
                msg = "Divided by Zero ERROR! Caused by x: " + str(num1) + "/ y: " + str(num2)
                logger.error(msg)
            

        # check if user wants another calculation
        # break the while loop if answer is no
        flag = 0; # if flag == -1 then loop is finished.
        while True:
            next_calculation = input("Let's do next calculation? (yes/no): ")
            next_calculation = next_calculation.lower()
            if next_calculation == "no":
                sure = input("Are you sure to exit? (yes/no): ")
                sure = sure.lower()
                if sure == "yes":
                    flag = -1
                    break
                elif sure != "no":
                    print("[Error]Invalid Input! Please type yes or no.")
                else:
                    break
            elif next_calculation != "yes":
                print("[Error] Invalid Input! Please type yes or no.")
            else:
                break
        if flag == -1:
            break    

    else:
        print("[Error]Invalid Input")
        msg = "Invalid input for the menu. Caused by choice: " + str(choice)
        logger.error(msg)

logger.info(endMsg)