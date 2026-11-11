'''
Student Managament System
Operations
------------------
1. Add Student --> Field --> id, name, mobile, marks, city
2. Display all student
3. Search Student
4. Update marks 
5. Delete Student by using id
6. Exit
Complete the project with validations
'''
from colorama import Fore,Back,Style,init
init()

#emplty list
stud = []
while True:
    print("---------------Student Managament System App---------------")
    print("-" * 80)
    print("1. Add Student")
    print("2. Display Student")
    print("3. Search Student By using ID")
    print("4. Update the Marks By using ID")
    print("5. Delete the Student By using ID")
    print("6. Exit")
    print("-" * 80)
    choice = input("Enter the choice = ").strip()
    if choice == "":
        print(Fore.RED + "Please enter the choice"+Style.RESET_ALL)
    elif not choice.isdigit():
        print(Fore.RED + "Only digit allowed"+Style.RESET_ALL)
   
    else:
     choice = int(choice)
     match choice:
            case 1:
                id = input("Enter the student id = ").strip()
                if id == "":
                    print("Please enter student id")
                    continue
                if not id.isdigit():
                    print("Only digit allowed")
                    continue
                # check id already exist
                found = False
                for s in stud:
                    if s[0] == id:
                        found = True
                        break
                if found:
                    print(f"{id} already exist")
                    continue
                # id = int(id)

                name = input("Enter the name of student =").strip().title()
                if name == "":
                    print("Please enter the name")
                    continue
                if not name.replace(" ","").isalpha():
                    print("Only Character allowed")
                    continue
                mob = input("Enter the mobile number = ").strip()
                if mob == "":
                    print("Please enter mobile number")
                    continue
                if not mob.isdigit():
                    print("Only digits allowed")
                    continue
                
                if mob[0] not in "6789":
                    print("Please enter valid mobile number")
                    continue
                
                # mob = int(mob)
                if len(mob) != 10:
                    print("Please check the mobile number")
                    continue
        
                mark = input("Enter the marks of student = ").strip()

                if mark == "":
                    print("Please enter the mark")
                    continue

                if not mark.isdigit():
                    print("Only digit allowed")
                    continue
                mark = int(mark)

                if mark < 0 or mark > 100:
                    print("Please enter the mark between 0 to 100")
                    continue

                city = input("Enter the city name = ").strip().title()

                # add the data inside the list
                stud.append([id,name,mob,mark,city])
                print(Fore.GREEN+"Data inserted successfully"+Style.RESET_ALL)

            case 2:
             if len(stud) == 0:
                print("Empty Database")
             else:
                 print("-"*80)
                 print("{:<5}{:<20}{:<15}{:<6}{:<10}".format("ID","Name","Mobile","Marks","City"))
                 print("-"*80)
                 for s in stud:
                     print("{:<5}{:<20}{:<15}{:<10}{:<10}".format(s[0],s[1],s[2],s[3],s[4]))
                
                 print("-"*80) 

            case 3:
                if len(stud) == 0:
                    print("No data found")
                
                search_id = input("Enter the id to search = ")
                if search_id == 0:
                    print("please enter to serach")
                    continue
                if not search_id.isdigit():
                    print("Only digit allowed")
                    continue
                found = False
                for s in stud:
                    if s[0] == search_id:
                        print("\n Data Found")
                        print("-"*50)
                        print("ID       :",s[0])
                        print("Name     :",s[1])
                        print("Mobile   :",s[2])
                        print("Marks    :",s[3])
                        print("City     :",s[4])
                        found = True
                        break
                if not found:
                    print("No reacord found.Please check the ID")

            case 4:
                print("Code under construction....")
            case 5:
                if len(stud) == 0:
                    print("No data found")
                search_id_del = input("Enter the id to delete = ")

                if search_id_del == 0:
                    print("Please eneter the id to delete")
                    continue
                if not search_id_del.isdigit():
                    print("Only digit allowed")
                    continue
                found = False
                for s in stud:
                    if s[0] == search_id_del:
                        stud.remove(s)
                        print("Data deleted successfully")
                        found = True
                        break
                if not found:
                    print("No record found. Please check the id")
         
                    
            case 6:
                print("Thanks for using our App. Visit again")
                break
            case _:
                print("Invalid choce")