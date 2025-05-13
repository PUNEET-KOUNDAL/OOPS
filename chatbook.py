class chatbook :
    def __init__(self) :
        self.username = ' '
        self.password = ' '
        self.loggdin = False 
        self.menu()

                


    def menu(self) :
        user_input = input('''welcome to chatbook !! how you you like to procedd ?
                           1. presee 1 to sing up 
                           2. press 2 to signin 
                           3. press 3 to write a post 
                           4. press 4 to message a friend 
                           5. press any orhter key to exit \n ''')


        if user_input == '1' :
            self.singup() 
        elif user_input == '2' :
            self.singin()
        elif user_input == '3':
            print('upcoming are in line up')
        else :
            exit()



    
    def singup(self):
        email = input('enter your email -- >  ')
        password = input('enter you password here -- >  ')
        self.username =  email
        self.password = password
        print('you have singup successfully\n')
        self.menu()

    def singin(self) :
        if self.username == ' ' and self.password == ' ' :
            print("please singup first")
        else :
            username = input('enter your usename/email correctly')
            password = input('enter your password ')
            if self.username == username and self.password == password :
                print('thanks for using our services')
                self.loggdin = True 
            else :
                print("please enter the correct crendentials")
        self.menu()

        
        



obj = chatbook()
