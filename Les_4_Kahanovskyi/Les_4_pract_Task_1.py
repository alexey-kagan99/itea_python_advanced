from abc import ABC, abstractmethod
class Person(ABC):

    def __init__(self, name, surname, date_of_birth):

        self._name = name
        self.surname = surname
        self._date_of_birth = date_of_birth


    @abstractmethod
    def get_person_age(self):

        self._age =2019 - self._date_of_birth
        return self._age


    @abstractmethod
    def get_information(self):

        self._info_list = []
        self._info_list.append(self._name)
        self._info_list.append(self.surname)
        self._info_list.append(self._date_of_birth)

        return self._info_list


class Applicans(Person):


    def __init__(self, *args, **kwargs):

        super().__init__(name = input(' Enter name : '), surname= input(' Enter surname : '), date_of_birth= int(input(' Enter date : ')))
        faculty = input(' Enter a faculty : ')
        self._faculty = faculty


    def get_person_age(self):

        return super().get_person_age()


    def get_information(self):

        self._info_list = super().get_information()
        self._info_list.append(self._faculty)

        return self._info_list



class Students(Person):

    def __init__(self, *args, **kwargs):

        super().__init__(name = input(' Enter name : '), surname= input(' Enter surname : '), date_of_birth= int(input(' Enter date : ')))
        self._faculty = input(' Enter a faculty : ')
        self._year = input(' Enter your year at university : ')

    def get_person_age(self):

        return super().get_person_age()

    def get_information(self):
        self._info_list = super().get_information()
        self._info_list.append(self._faculty)
        self._info_list.append(self._year)

        return self._info_list


class Teachers(Person):

    def __init__(self, *args, **kwargs):

        super().__init__(name = input(' Enter name : '), surname= input(' Enter surname : '), date_of_birth= int(input(' Enter date : ')))
        self._faculty = input(' Enter a faculty : ')
        self._position = input(' Enter your position : ')
        self._experience = input(' Enter your experience : ')


    def get_person_age(self):

        return super().get_person_age()


    def get_information(self):
        self._info_list = super().get_information()
        self._info_list.append(self._faculty)
        self._info_list.append(self._position)
        self._info_list.append(self._experience)

        return self._info_list


person_list = []
person_in_age_range_list = []
applicants_list = []

for enrolee in range(int(input(' How many applicants in your database ? '))):

    print(f' enrolee number {enrolee + 1} ')
    enrolee = Applicans()
    applicants_list.append(enrolee)
    person_list.append(enrolee)

students_list = []
for student in range(int(input(' How many students in your database ? '))):

    print(f' student number {student + 1} ')
    student = Students()
    students_list.append(student)
    person_list.append(student)

teachers_list = []
for teacher in range(int(input(' How many teachers in your database ? '))):

    print(f' teacher number {teacher + 1} ')
    teacher = Teachers()
    teachers_list.append(teacher)
    person_list.append(teacher)

print(' Whole database ')

for person in person_list:

    print(person.get_information())

choice = input(' Do you want to find people in some age range ? (yes/no) ')

if choice.isalpha() and choice.lower() == 'yes':

    start_age_poin = int(input(' Range Since : '))
    finish_age_point = int(input(' Fore : '))

    for person in person_list:

        if person.get_person_age() in range(start_age_poin, finish_age_point):

            person_in_age_range_list.append(person.surname)

    print(person_in_age_range_list)
