
# class user:

#     def __init__(self, user_name, email, password) -> None:
#         self.user_name = user_name
#         self.password = password
#         self.email = email

def signup(usernamegi, emailgi, passwordgi):
    
    accept = False
    while not accept:
        checkpassword = input('Confirm password:' )
        if checkpassword == passwordgi:
            accept = True
            userfile = open('userData.txt', 'w')
            userfile.writelines([usernamegi+'\n', emailgi+'\n', passwordgi+'\n'])
            userfile.close()
            print('Account creation successful')
        else: 
            print('passwords dont match')

def signin(usernamegi, passwordgi):
    userfile = open('userData.txt', 'r')
    content = userfile.readlines()
    if (usernamegi == content[0].rstrip('\n')) and (passwordgi == content[2].rstrip('\n')) :
        print('Login successful')
    else:
        print('Login not successful')
    userfile.close()
