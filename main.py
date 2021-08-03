from dbhelper import DBHelper


def main():
    db = DBHelper()
    while True:
        print("press 1 to insert new user: ")
        print("press 2 to display all user: ")
        print("press 3 to delete user: ")
        print("press 4 to update new user: ")
        print("press 5 to exit program: ")
        print()
        try:
            choice = int(input())
            if choice == 1:
                # insert user
                uid = int(input("Enter user id: "))
                user_name = input("Enter username: ")
                user_phone = input("Enter user Phone: ")
                db.insert_user(uid, user_name, user_phone)
            elif choice == 2:
                # display user
                db.fetch_all()
            elif choice == 3:
                # delete user
                uid = input("enter userid which you want to delete: ")
                db.delete_user(uid)
                pass
            elif choice == 4:
                # update user
                uid = int(input("Enter user id: "))
                user_name = input("Enter username: ")
                user_phone = input("Enter user Phone: ")
                db.update_user(uid, user_name, user_phone)
                pass
            elif choice == 5:
                break
            else:
                print("Invalid input ! Try again")
        except Exception as e:
            print(e)
            print("Invalid Details !")


if __name__ == "__main__":
    main()
