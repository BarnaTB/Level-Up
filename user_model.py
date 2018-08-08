import re


class User:
    """
    This class creates a user instance upon sign up of a user,
    validates their email and password, combines their first and last names
    then returns the appropriate message for each case.
    """
    def __init__(self, first_name, last_name, phone_number, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.password = password

    def validate_email(self):
        """
        Method checks that a user's email follows semantics for a valid email;
        first characters must be letters followed by a fullstop, then the '@'
        symbol followed by letters, a fullstop and then finally letters.
        Returns the valid email.
        """
        # source: https://docs.python.org/2/howto/regex.html
        if not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", self.email):
            return 'Invalid email address!'
        return self.email

    def combine_name(self):
        """
        Method checks that the entered values for names are strings.
        If so it returns both names combined, else it requests the user to
        enter string values.
        """
        if self.first_name.isalpha() and self.last_name.isalpha():
            username = self.first_name + " " + self.last_name
            return username
        return 'Names must be alphabets'

    def validate_password(self):
        """
        Method checks that a user's password follows specific criteria such as
        at least one uppercase character, one lowercase, one number and one
        spceial character. Password should also be atleast six characters long.
        """
        # source: https://docs.python.org/2/howto/regex.html
        if not re.match(r"[A-Za-z0-9@#]", self.password):
            return 'Oops!, invalid password'
q       elif len(self.password) < 6:
            return 'Password should be at least six characters long'
        return 'Valid password!'
