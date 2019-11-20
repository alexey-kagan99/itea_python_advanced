class Registration:
    DATA_LIST = {'admen': 'admen', 'Alex': 'Kahanovskyi'}

    def __init__(self):

        self._log = input(' login : ')
        self._pas = input(' password (min 8 symbols: min 3 numbers and 5 letters) : ')
        self._mail = input(' mail : ')

    def get_blank(self):

        while not self.validator_login():
            self._log = input('Enter new login, this login is already used : ')

        while not self.validator_sym_passwod() or not self.validator_len_password():
            self._pas = input(' Enter your password (min 8 symbols: min 3 numbers and 5 letters) : ')

    def set_data_list(self):

        self.DATA_LIST[f'{self._log}'] = f'{self._pas}'

    def validator_login(self):

        if self._log not in list(self.DATA_LIST.keys()):
            return True

    def validator_len_password(self):

        if len(self._pas) >= 8:
            return True

    def validator_sym_passwod(self):

        self.num = []
        self.laters = []

        for i in self._pas:

            if i.isdigit():

                self.num.append(i)

            elif i.isalpha():

                self.laters.append(i)

        if len(self.num) >= 3 and len(self.laters) >= 5:
            return True


class Login(Registration):

    def __init__(self):

        super().__init__()

    def get_blank(self):

        while self.validator_login():
            self._log = input('incorrect login, try again please : ')

        while not self.check_pas():
            self._pas = input('Incorrect password, try again please : ')

    def check_pas(self):

        if self.DATA_LIST[self._log] == self._pas:
            return True

    def admin_validator(self):

        if self._log.lower() == 'admen' and self._pas.lower() == 'admen':
            return True


class Admen:
    POST_LIST = ['post1']

    def get_post(self):
        return self.POST_LIST

    def set_post(self, value):
        self.POST_LIST.append(value)


class User(Admen):

    def get_post(self):
        return self.POST_LIST


while True:

    choice = input(' Registration or Login : (r or l)')

    if choice.lower() == 'r':

        user = Registration()
        user.get_blank()
        user.set_data_list()
        print(Registration.DATA_LIST)

    elif choice.lower() == 'l':

        user = Login()
        user.get_blank()

        while user.admin_validator():

            new_user = Admen()

            admen_choice = input(' Do you want to add a post or watch all posts ? (add/watch/exit) ')

            while admen_choice.lower() != 'exit':

                if admen_choice.lower() == 'add':

                    new_user.set_post(input(' Write new post : '))
                    break

                elif admen_choice.lower() == 'watch':

                    print(new_user.get_post())
                    break

            if admen_choice.lower() == 'exit':
                break

        if not user.admin_validator():
            new_user = User()
            print(new_user.get_post())
