from Library_Management_System_B import *

if __name__=="__main__":
    print("\n-----------LIBRARY MANAGEMENT SYSTEM-------------")
    while(True):
        print("\n1. Creating Student Account\n"
              "2. Student Account Details\n"
              "3. Delete Student Account\n"
              "4. Update Student Account\n"
              "5. Student's Book Info\n"
              "6. Exit")
        choice = int(input("\nEnter your choice: "))
        if choice==1:
            name = input("\nEnter your name(full-name): ")
            clg = input("Enter your college: ")
            br = input("Enter your branch: ")
            yr = int(input("Enter your year: "))
            lib = input("Enter your library(central/college/outside city): ")
            ph = int(input("Enter your phone number: "))
            try:
                s=create(name,clg,br,yr,lib,ph)
                s.create_acc()
                print("\nNOTE: Remember your student id!!!")
            except:
                print("Failed to create account. Please come after some time")
                break
        elif choice==2:
            id=int(input("\nEnter your student id: "))
            ph = int(input("Enter your phone number: "))
            try:
                s=select(id,ph)
                s.show_details()
            except:
                print("\nThis id has no account.\n"
                      "You might be typed wrong student id or phone number!!!")
                break
        elif choice==3:
            id = int(input("\nEnter student id: "))
            ph = int(input("Enter your phone number: "))
            try:
                s = delete(id,ph)
                a = book_i(id,ph)
                a.up_book(id)
                s.del_acc()
                print("\nYour Account Deleted Successfully!")
            except:
                print("\nFailed to Delete Account\n"
                      "You might be typed wrong student id or phone number!!!")
                break

        elif choice==4:
            id = int(input("\nEnter student id: "))
            ph = int(input("Enter your phone number: "))
            try:
                s = update(id, ph)
                print("\nWhat do you want to update:-\n"
                      "a. Student Name\n"
                      "b. College\n"
                      "c. Branch\n"
                      "d. Year\n"
                      "e. Library\n"
                      "f. Phone Number")
                ch=input("\nEnter your choice for updation(recommended to use small letter): ")
                try:
                    print("\nPlease file the data you want to update")
                    if ch=='a':
                        name=input("\nEnter name: ")
                        s.sname(name)
                        print("\nUpdated Successfully!")
                    elif ch=='b':
                        clg = input("\nEnter college: ")
                        s.college(clg)
                        print("\nUpdated Successfully!")
                    elif ch=='c':
                        br = input("\nEnter branch: ")
                        s.branch(br)
                        print("\nUpdated Successfully!")
                    elif ch=='d':
                        yr = input("\nEnter year: ")
                        s.year(yr)
                        print("\nUpdated Successfully!")
                    elif ch=='e':
                        lib = input("\nEnter library: ")
                        s.library(lib)
                        print("\nUpdated Successfully!")
                    elif ch=='f':
                        ph = input("\nEnter phone number: ")
                        s.phno(ph)
                        print("\nUpdated Successfully!")
                    else:
                        print("You give wrong choice!!!")
                        break
                except:
                    print("\nFailed to Update Account!!!")
                    break
            except:
                print("\nFailed to Update Account!!!\n"
                      "You might be typed wrong student id or phone number!!!")

        elif choice==5:
            id = int(input("\nEnter student id: "))
            ph = int(input("Enter your phone number: "))
            try:
                s=book_i(id,ph)
                print("\n!!!You will take 1 book at a time!!!")
                while(True):
                    print("\na. Book Issue\n"
                          "b. Return Book\n"
                          "c. Check your Book status")
                    ch = input("\nEnter your choice(recommended to use small letter): ")
                    try:
                        if ch=='a':
                            bk = input("\nEnter book name: ")
                            aut = input("Enter author: ")
                            isbn=input("Enter isbn: ")
                            s.issue(id,bk,aut,isbn)
                            print("\nBook Issued Successfully!")
                        elif ch=='b':
                            bk = input("\nEnter book name: ")
                            aut = input("Enter author: ")
                            isbn = input("Enter isbn: ")
                            s.up_book(id)
                            print("\nBook Returned. Successfully!!!")
                        elif ch=='c':
                            try:
                                s.sel_book(id)
                            except:
                                print("\nYou don't have a book yet. Issue book first!")
                        else:
                            print("\nYou entered wrong choice!!!")
                            break
                        book=int(input("\n1. Back\t2. Exit\n"))
                        if book==1:
                            continue
                        elif book==2:
                            break
                        else:
                            print("Wrong choice!!!")
                            break
                    except:
                        print("\nFailed to Issue Book!!!")
                        break
            except:
                print("\nYou might be typed wrong student id or phone number!!!")
                break

        elif choice==6:
            print("Thankyou")
            exit()

        else:
            print("Wrong choice!!!")
            break
