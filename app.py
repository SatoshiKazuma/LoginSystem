from Func_Class import signin , signup

#realtime start
initial = input('Signin(si) or Signup(su)\n' )

if initial.lower() == 'si' or 'su':
    if initial.lower() == 'su':    
        usernameg = input('Enter a username: ')       
        emailg = input('Enter an email address: ')
        passwordg = input('Enter your new password: ')
        signup(usernameg, emailg, passwordg)
    elif initial.lower() == 'si':
        usernameg = input('Username:')
        passwordg = input('Password: ')
        try:
            signin(usernameg, passwordg)
        except IndexError:
            print('It seems no accounts have been created yet; \ncreate one first, then attempt to')