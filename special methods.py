### The magic method of plus operator
'''
add_two_numbers = 28 + 33
print(add_two_numbers)

add_two_numbers = (28).__add__(333)
print(add_two_numbers)

try_this = (-1233).__abs__()
print(try_this)


## Example: 3D


class Point3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def sqaure_dimension(self):
        if self.x > 10:
            return self.x ** 2
        else:
            return "wrong"


my_three_dimensions = Point3D(10, 12, 15)
print(my_three_dimensions)

square_number = my_three_dimensions.sqaure_dimension()
print(square_number)


## University student ID
class Student:

    def __init__(self, student_id, name, age, GPA):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.GPA = GPA

    def __str__(self):
        return f"Student: {self.name}" \
                f"| Student ID: {self.student_id}" \
                f"| Age: {self.age}"\
                f"| GPA: {self.GPA}"


student_1 = Student("42AB9", "Nora Nav", 34, 3.76)
print(student_1)

student_2 = Student("4R667", "Daniel", 45, 4.7)
print(student_2)


class MovieFavs:
    """A Class of MOvies

    create a list of favourite movies
    """


    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("This movie is not in my list of favourites")


my_movie_list = MovieFavs()

my_movie_list.add_item("jack and the bean stock")
my_movie_list.add_item("Spider Man")
print(my_movie_list)

print(my_movie_list.items)

my_movie_list.remove_item("Spider Man")
print(my_movie_list.items)


print(3 + 4)
print((3).__add__(4))

print("where can i find you")
print("where".__add__(" can i find you!"))

print([1, 2, 3] + [4, 5, 6])
print([1, 2, 3].__add__([4, 5, 6]))


class Point3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, another):
        new_x = self.x + another.x
        new_y = self.y + another.y
        new_z = self.z + another.z
        return Point3D(new_x, new_y, new_z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


point3d1 = Point3D(12, 13, 15)
print(point3d1)

point3d2 = Point3D(13, 7, 9)
print(point3d2)

point3d3 = point3d1 + point3d2
print(point3d3)
'''

class Bookshelf:
    """A Class of book shelves

    Create a bookshelf that maps different books to embedded lists
    The shelve is a list of three lists. Each list is a shelve on its own.



    Arguements:
        The class does not take any arguements
    """

    def __init__(self):
        self.shelf_content = [[],
                            [],
                            [],
                            []]

    def add_book(self, book, location):
        """Returns the book added to the shelf

        This is a list that represents the books added to the books added to
        the shelf
        """
        self.shelf_content[location].append(book) ##The codes reads: append this book in the location of the shelve

    def take_book(self, book, location):
        """ Returns the book taken out of the shelf

        The books are removed from the shelf using the remove method
        """
        self.shelf_content[location].remove(book)

    def __getitem__(self, location):
        return self.shelf_content[location]


my_bookshelf = Bookshelf()

my_bookshelf.add_book("quantum computing for dummies", 0)
my_bookshelf.add_book("field effec physics", 0)
my_bookshelf.add_book("nano-physics", 0)

my_bookshelf.add_book("lock up the house", 1)
my_bookshelf.add_book("in the midst of the dark", 1)
my_bookshelf.add_book("action time", 1)

my_bookshelf.add_book("AN aspect of god", 2)
my_bookshelf.add_book("A brief history of time", 2)
my_bookshelf.add_book("Into the mean field", 2)


class BankAccount:

    def __init__(self, account_owner, account_number, initial_balance):
        self.account_owner = account_owner
        self.account_number = account_number
        self.balance = initial_balance

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds")


my_account = BankAccount("Afam Madu", "2234-5567-2499", 45990)
print(bool(my_account))

if my_account:
    print("True")
else:
    print("False")

my_account.balance = 0
print(bool(my_account))


## Example after defining the __bool__() method.

class BankAccount:

    def __init__(self, account_owner, account_number, initial_balance):
        self.account_owner = account_owner
        self.account_number = account_number
        self.initial_balance = initial_balance

    def make_deposit(self, amount):
        self.initial_balance =self.initial_balance + amount

    def make_withdrawal(self, amount):
        if self.initial_balance - amount >= 0:
            self.initial_balance -= amount
        else:
            print("Insufficient funds")

    def __bool__(self):
        return self.initial_balance > 0


my_account = BankAccount("Daniel", "080-666-1092234", 45080.23)
print(my_account.initial_balance)
print(bool(my_account))





