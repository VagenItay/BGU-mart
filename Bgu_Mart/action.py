from numbers import Real
from persistence import *

import sys

def main(args : list):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            #TODO: apply the action (and insert to the table) if possible
            ProductOutPut=repo.products.find(id=splittedline[0])
            quantity = ProductOutPut[0].quantity
            if(int(splittedline[1])>0):
                #this is a supplier
                repo.products.updateQuantity(quantity+int(splittedline[1]),splittedline[0])
                repo.activities.insert(Activitie(splittedline[0],splittedline[1],splittedline[2],splittedline[3]))
            else:
                #this is an employee
                if(quantity>(0-int(splittedline[1]))):
                    repo.products.updateQuantity(quantity+int(splittedline[1]),splittedline[0])
                    repo.activities.insert(Activitie(splittedline[0],splittedline[1],splittedline[2],splittedline[3]))

      
                


if __name__ == '__main__':
    main(sys.argv)