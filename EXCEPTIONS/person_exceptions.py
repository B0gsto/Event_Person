class DuplicatePersonException(Exception):
    def __init__(self, person):
        self.person = person

    def __str__(self):
        return "Duplicate person: " + str(self.person)


class ValidationException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
