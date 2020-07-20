class StringInput():

    def get_string(self):
        self.inputs = input("Enter string: ")

    def print_string(self):
        print(self.inputs.upper())


obj = StringInput()

obj.get_string()
obj.print_string()
