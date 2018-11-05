def feb(n):
    num1 = 0
    num2 = 1
    # In case of n<0
    if n < 0:
        print "not valid number"
    # In case of n=0
    if n == 0:
        print 0
    # In case of n=1
    if n == 1:
        print 1
    # Check if its the first print , in order to print 0 1 in the beginning
    first_print = 1
    i = 1
    while i < n:
        sum_of_2_number = num1 + num2
        print "0 1 " + str(sum_of_2_number) if first_print == 1 else sum_of_2_number,
        first_print = 0
        num1 = num2
        num2 = sum_of_2_number
        i = i + 1


def main():

    # Enter y = yes or n = no
    answer = "y"
    while answer == "y":
        num = input("Enter your number friend ")
        feb(num)
        print "\n"
        answer = raw_input("would you like to try again? ")
        while answer != "y" and answer != "n":
            print "not valid answer"
            answer = raw_input(" \n would you like to try again")

main()
