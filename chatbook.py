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
            pass 
        elif user_input == '2' :
            pass 
        elif user_input == '3':
            print('upcoming are in line up')
        else :
            exit()
        



obj = chatbook()
