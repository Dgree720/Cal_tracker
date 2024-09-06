import pandas as pd
from datetime import datetime, date
import csv
from user_management import get_reg_users
from user_management import add_user
from user_management import request_username
from user_management import check_user
from general_functions import clear_terminal
import functionalities




def main():
    current_date = date.today()
    reg_users = get_reg_users()
    user = request_username()
    while not check_user(user, reg_users):
        add_user(reg_users)
        break
    user_cmd = menu_options(user, current_date)




def menu_options(user, current_date):
    pos_cmds = {
        1: "View Dashboard",
        2: "Add new weight",
        3: "Add Calories",
        4: "Add Activity",
        5: "Edit User Profile",
        6: "Delete User Profile",
        7: "Exit App"
    }
    print("")
    print("")
    print("_"*75)
    print("What would you like to do?\n")
    print("Menu:"
          "\n1. View Dashboard"
          "\n2. Add new weight"
          "\n3. Add Calories"
          "\n4. Add Activity"
          "\n5. Edit User Profile"
          "\n6. Delete User Profile"
          "\n7. Exit App")
    while True:
        try:
            user_cmd = int(input("Select: "))
        except ValueError:
            print("please enter a valid selection")
            continue
        if user_cmd not in [1, 2, 3, 4, 5, 6, 7]:
            print("please enter a valid selection")
        else:
            clear_terminal()
            print(f"\nselected to {pos_cmds[user_cmd]}...\n")
            break
    if user_cmd == 1:
        functionalities.show_dashboard(user)
        menu_options(user, current_date)
    elif user_cmd == 2:
        functionalities.update_weight_progress(user, current_date)
        menu_options(user, current_date)
    elif user_cmd == 3:
        functionalities.add_food()
        menu_options(user, current_date)
    elif user_cmd == 4:
        functionalities.add_activity()
        menu_options(user, current_date)
    elif user_cmd == 5:
        functionalities.change_profile()
        menu_options(user, current_date)
    elif user_cmd == 6:
        functionalities.delete_user()
        menu_options(user, current_date)
    elif user_cmd == 7:
        print("_"*75)
        print(".....quitting.....")
        quit("see you next time :)")
    return user_cmd






if __name__ == "__main__":
    main()