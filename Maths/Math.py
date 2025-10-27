class Multiply:

    def __init__(self, type, num1, num2):
        self.type = type
        self.num1 = num2
        self.num2 = num2

    def get_type(self):
        return self.type

    def get_num1(self):
        return self.num1

    def get_num2(self):
        return self.num2

    def calculate_numbers(self):
        return self.num1 * self.num2


class Add:
    def __init__(self, type, num1, num2):

        self.type = type
        self.num1 = num2
        self.num2 = num2

    def get_type(self):
        return self.type

    def get_num1(self):
        return self.num1

    def get_num2(self):
        return self.num2

    def calculate_numbers(self):
        return self.num1 + self.num2


class Sub:

    def __init__(self, type, num1, num2):

        self.type = type
        self.num1 = num2
        self.num2 = num2

    def get_type(self):
        return self.type

    def get_num1(self):
        return self.num1

    def get_num2(self):
        return self.num2

    def calculate_numbers(self):
        return self.num1 - self.num2


class Divide:

    def __init__(self, type, num1, num2):

        self.type = type
        self.num1 = num2
        self.num2 = num2

    def get_type(self):
        return self.type

    def get_num1(self):
        return self.num1

    def get_num2(self):
        return self.num2

    def calculate_numbers(self):
        return int(self.num1 / self.num2)
