from persistence import *
from datetime import datetime

def main():
    #TODO: implement
    suppliersAll = repo.suppliers.find_all()
    employeesAll = repo.employees.find_all()
    activitiesAll = repo.activities.find_all()
    branchesAll = repo.branches.find_all()
    productsAll = repo.products.find_all()
    activitiesAll.sort(key=lambda x : x.date)
    employeesAll.sort(key=lambda x : x.name)
    print("A"+repo.activities._table_name[1:])
    for i in activitiesAll:
        print(i)
    print("B"+repo.branches._table_name[1:])
    for i in branchesAll:
        print(i) 
    print("E"+repo.employees._table_name[1:])
    for i in employeesAll:
        print(i)
    print("P" + repo.products._table_name[1:])
    for i in productsAll:
        print(i)
    print("S"+repo.suppliers._table_name[1:])
    for i in suppliersAll:
        print(i)
    #employees report
    print("E" + repo.employees._table_name[1:] + " report")
    EmployeesWithActivities = repo.execute_command("SELECT employees.name,employees.salary,branches.location,SUM(activities.quantity*products.price*-1),employees.id FROM activities JOIN employees ON activities.activator_id=employees.id JOIN branches ON employees.branche=branches.id JOIN products ON activities.product_id=products.id GROUP BY activities.activator_id")
    AllEmployees = repo.execute_command("SELECT employees.name,employees.salary,branches.location,0,employees.id FROM employees JOIN branches ON employees.branche=branches.id")
    UnionOfEmployees = EmployeesWithActivities+AllEmployees
    UnionOfEmployees.sort(key=lambda x: x[0])
    #if there are duplicates, do not print
    for i in range(len(UnionOfEmployees)):
        if i+1!=len(UnionOfEmployees):
            if UnionOfEmployees[i][4]==UnionOfEmployees[i+1][4]:
                if UnionOfEmployees[i][3]==0:
                    continue
        if i>0:
            if UnionOfEmployees[i][4]==UnionOfEmployees[i-1][4]:
                if UnionOfEmployees[i][3]==0:
                    continue
        print(UnionOfEmployees[i][0]+' '+str(UnionOfEmployees[i][1])+' '+UnionOfEmployees[i][2]+' '+str(UnionOfEmployees[i][3]))
    #activities report
    print("")
    print("A"+repo.activities._table_name[1:] + " report")  
    ActivitiesOfEmployees =repo.execute_command("SELECT activities.date,products.description,activities.quantity,employees.name,suppliers.name FROM activities JOIN products ON activities.product_id=products.id JOIN employees ON activities.activator_id=employees.id LEFT JOIN suppliers ON activities.activator_id=suppliers.id")
    ActivitiesOfSuppliers = repo.execute_command("SELECT activities.date,products.description,activities.quantity,employees.name,suppliers.name FROM activities JOIN products ON activities.product_id=products.id JOIN suppliers ON activities.activator_id=suppliers.id LEFT JOIN employees ON activities.activator_id=employees.id")
    UnionOfActivities = ActivitiesOfSuppliers+ActivitiesOfEmployees
    UnionOfActivities.sort(key=lambda x: x[0])
    for i in UnionOfActivities:
        print(i)
    
    pass
if __name__ == '__main__':
    main()