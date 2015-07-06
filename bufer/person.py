import datetime
from datetime import date

class Person(object):
    
    SEX = ['M', 'F'] # class variable

    def __init__(self, name, date_of_birth, person_sex):
        """
        Attributes:
            date_of_birth has format YYYY-mm-dd, '1986-04-10'
        """
        self.name = name

        if person_sex in self.SEX:
            self.sex = person_sex
        else:
            raise RuntimeError("Please use M or F.")

        birthday = date_of_birth.split('-')

        self.date_of_birth = datetime.date(
            int(birthday[0]),
            int(birthday[1]),
            int(birthday[2])
        )

    def get_age(self):
        """
        Return age of person.
        """
        return (date.today() - self.date_of_birth).days / 365

    def get_info(self):
        return self.name + ', ' + str(self.get_age())


class Student(Person):
    def __init__(self, name, date_of_birth, person_sex, grade):
        Person.__init__(self, name, date_of_birth, person_sex)
        self.grade = grade

    def get_info(self):
        return self.name + ', ' + str(self.grade)


class Professor(Person):
    def __init__(self, name, date_of_birth, person_sex, department):
        Person.__init__(self, name, date_of_birth, person_sex)
        self.department = department

    def get_info(self):
        return self.name + ', ' + str(self.department)


#stud = Student('Oleg', '1986-10-04', 2)
#print stud.grade
#print stud.name
#print stud.get_age()
if __name__ == '__main__':
    kate = Student('Katia', '1986-10-10', 'F', 2)
    print kate.get_age()
    print kate.get_info()
