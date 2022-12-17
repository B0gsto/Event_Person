from DOMAIN.event import *


class DuplicateEventError(Exception):
    def __init__(self, message):
        self.message = message

    def getMess(self):
        return self.message

    def __str__(self):
        return self.message


class ValidationError(Exception):
    def __init__(self, message):
        self.message = message

    def getMess(self):
        return self.message

    def __str__(self):
        return self.message


class DuplicatePersonInEventError(Exception):
    def __init__(self, message):
        self.message = message

    def getMess(self):
        return self.message

    def __str__(self):
        return self.message
