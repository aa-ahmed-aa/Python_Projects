class Parent():
    def print_last_name(self):
        print("Robert")

class Child(Parent):
    def print_first_name(self):
        print("Bucky")

    def print_last_name(self):
        print("Myami")

p=Child()
p.print_first_name()
p.print_last_name()