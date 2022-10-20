from lib2to3.pytree import convert


def main():

    print('This application changes US dollars to Pounds Sterling.')

    dollars = eval(input("Enter amount of dollars you wish to convert =   "))
    convert_to_pounds = dollars * 0.879
    pounds = convert_to_pounds
    print("The amount is" , pounds, "Pounds Sterling")

main()