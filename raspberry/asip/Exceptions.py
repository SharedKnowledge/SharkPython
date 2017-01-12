class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class IdentificationsError(Error):
    """Exception raised for errors in the input.

    """

    def __init__(self, si_dup, name_dup):
        self.error = ""
        self.si = si_dup
        self.name = name_dup
        if (si_dup):
            self.error += "SI has been used already"
            if (name_dup):
                self.error = "Name and " + self.error

            else:
                self.error += " under different Name"
        else:
            self.error += "Name used with different SI"

    def __str__(self):
        return repr(self.error)


class TypeError(Error):
    def __init__(self,var, expected):
        self.exp = expected
        self.var = var

    def __str__(self):
        return repr("TypeError! %s must be Type(%s)") % (self.var, self.exp)
