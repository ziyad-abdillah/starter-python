from cgi import print_arguments


def myFunction(*tous):
    print(tous)
myFunction(4, 4, 4)