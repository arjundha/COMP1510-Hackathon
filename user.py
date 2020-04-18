"""
Class constructor for an application User.
"""
import doctest


class User:

    def __init__(self, name: str, age: int, income: int, country: str, student: bool):
        """
        Initialize a User class object.

        :param name: Name as a user as a string
        :param age: Age of a user as an integer
        :param income: Average annual income of a user as an integer
        :param country: Country of user residence as a string
        :param student: Boolean representing whether or not the user is a student
        :precondition: User has entered in well-formed parameters that meet the data type requirements
        :postcondition: User class object will be created

        >>> test_user = User("Arjun Dhaliwal", 24, 0, "Canada", True)
        >>> test_user
        User("Arjun Dhaliwal", 24, $0, Canada, True)

        >>> test_user = User("Chris Thompson", 30, 500000, "Canada", False)
        >>> test_user
        User("Chris Thompson", 30, $500000, Canada, False)
        """
        # Initialize each variable into the class object
        self.__name = name
        self.__age = age
        self.__income = income
        self.__country = country
        self.__student = student

    def get_name(self) -> str:
        """
        Return the name in a User object.

        :return: User name as a string

        >>> test_user = User("Arjun Dhaliwal", 24, 0, "Canada", True)
        >>> test_user.get_name()
        'Arjun Dhaliwal'
        """
        return self.__name

    def get_age(self) -> int:
        """
        Return the age in a User object.

        :return: User age as an int

        >>> test_user = User("Arjun Dhaliwal", 24, 0, "Canada", True)
        >>> test_user.get_age()
        24
        """
        return self.__age

    def get_income(self) -> int:
        """
        Return the annual income in a User object.

        :return: User income as an int

        >>> test_user = User("Arjun Dhaliwal", 24, 0, "Canada", True)
        >>> test_user.get_income()
        0
        """
        return self.__income

    def get_country(self) -> str:
        """
        Return the country of residence in a User object.

        :return: User country as a string

        >>> test_user = User("Arjun Dhaliwal", 24, 0, "Canada", True)
        >>> test_user.get_country()
        'Canada'
        """
        return self.__country

    def get_student(self) -> bool:
        """
        Return the student enrollment status in a User object.

        :return: User student status as a Boolean

        >>> test_user = User("Arjun Dhaliwal", 24, 0, "Canada", True)
        >>> test_user.get_student()
        True
        """
        return self.__student

    def set_name(self, new_name: str):
        """
        Alter the name in a User object.

        :param new_name: Name to replace current name value in a object
        :precondition: parameter is a well-formed string
        :postcondition: will change the name in an object

        >>> test_user = User("Arjun Dhaliwal", 24, 0, "Canada", True)
        >>> test_user.set_name("Chris")
        >>> test_user.get_name()
        'Chris'
        """
        self.__name = new_name

    def set_age(self, new_age: int):
        """
        Alter the age in a User object.

        :param new_age: Age to replace current age with in a User object
        :precondition: parameter is an integer
        :postcondition: will change the age in an object

        >>> test_user = User("Arjun Dhaliwal", 24, 0, "Canada", True)
        >>> test_user.set_age(999)
        >>> test_user.get_age()
        999
        """
        self.__age = new_age

    def set_income(self, new_income: int):
        """
        Alter the annual income of a User object.

        :param new_income: Income to replace current income with in a User object
        :precondition: parameter is an integer
        :postcondition: will change the income in an object

        >>> test_user = User("Arjun Dhaliwal", 24, 0, "Canada", True)
        >>> test_user.set_income(999)
        >>> test_user.get_income()
        999
        """
        self.__income = new_income

    def set_country(self, new_country: str):
        """
        Alter the country of residence in a User object.

        :param new_country: Country to replace current country with in a User object
        :precondition: parameter is an string
        :postcondition: will change the country in an object
        """
        self.__country = new_country

    def set_student(self, new_student: bool):
        """
        Alter the student status in a User object.

        :param new_student: Boolean to replace current boolean with in a User object
        :precondition: parameter is a boolean (true or false)
        :postcondition: will change the student status in an object
        """
        self.__student = new_student

    def __str__(self) -> str:
        """
        Return a string representing a User object.

        :return: A message of a User's information as a string
        """
        return "Name: \"%s\"\nAge: %d\nIncome: $%d\nCountry: %s\nCurrent Student: %s" % \
               (self.get_name(), self.get_age(), self.get_income(), self.get_country(), self.get_student())

    def __repr__(self) -> str:
        """
        Return a string representing a User object.

        :return: Object as a string.
        """
        return "User(\"%s\", %d, $%d, %s, %s)" % (self.get_name(), self.get_age(), self.get_income(),
                                                  self.get_country(), self.get_student())


def main():
    """
    Test the functions in the module.
    """
    doctest.testmod()
    test_user = User("Arjun", 24, 0, "Canada", True)
    print(test_user)
    test_user.set_name("Arjunnnnnn")
    test_user.set_age(475345834758934795)
    test_user.set_income(32545345)
    test_user.set_country("france")
    test_user.set_student(False)
    print(test_user)
    print(test_user.get_student())


if __name__ == '__main__':
    main()
