#menu
logins = []
menu_options = input("login: 1\nregister: 2\nexit: 3\nChoice: ")
#if for 1
if menu_options == "1":
    login_username = input("username: ")
    #opens file to check if username and password are in
    with open("logins.csv") as file:
        print(login_username)
        for line in file:
            if login_username in file:
                listusername = []
                listpassword = []
                login_password = input("Whats your password: ")
                username, password = line.rstrip().split(",")
                password = password.strip()
                # print(f"{username},{password}")
                #get the index
                index = login_password[1]
                for line in file:
                    if password in line:
                        login_options = input("change password: 1\nLogout: 2\nChoice: ")
                        if login_options == "1":
                            with open("logins.csv") as file:
                                for line in file:
                                    tempfile = []
                                    
                        else:
                            exit
                    else:
                        print("invalid password")
                        print(password)
            else:
                print("username not found")
#if for register 2
elif menu_options == "2":
    register_username = input("new username: ")
    register_password = input("New password: ")
    if len(register_password) < 4:
        print("to small")
    else:
        logins.append(f"{register_username},{register_password}")
    #add usernames to file
    with open("logins.csv", "a") as file:
        # logins.append(f"{register_username},{register_password}")
        file.write(f"\n{register_username},{register_password}")
#if for exit
elif menu_options == "3":
    exit
else:
    print("pick a valid option")
