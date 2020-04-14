import operator

employees = [
    {
        'Position': 'Manager',
        'Name': 'James',
        'Department': 'Finance',
        'City': 'Philadelphia',
        'State': 'PA'
    },
    {
        'Position': 'Accountant',
        'Name': 'George',
        'Department': 'Finance',
        'City': 'Buffalo',
        'State': 'NY'
    },
    {
        'Position': 'Guard',
        'Name': 'Henrietta',
        'Department': 'Operations',
        'City': 'King of Prussia',
        'State': 'PA'
    },
    {
        'Position': 'President',
        'Name': 'Phillip',
        'Department': 'Leadership',
        'City': 'Cherry Hill',
        'State': 'NJ'
    }
]

pets = {
    'dogs': [
        {
            'Name': 'James',
            'Breed': 'Bulldog',
            'Color': 'Brown'
        },
        {
            'Name': 'George',
            'Breed': 'Greyhound',
            'Color': 'Brindle'
        },
    ],
    'cats': [
        {
            'Name': 'Henry',
            'Breed': 'Shorthair',
            'Color': 'White'
        },
        {
            'Name': 'Phillip',
            'Breed': 'Siamese',
            'Color': 'Gray'
        }
    ]
}


def example_1():
    print('Example 1 - demonstrate nesting and white space')

    price = 100
    quantity = 20

    # If price is greater than 100 and quantity is greater than 20, discount is 10
    # If price is greater than 100 and quantity is less than or equal to 20, discount is 5
    # Otherwise if quantity is greater than 20 then discount is 3
    # Otherwise no discount
    discount = 0
    if price > 100:
        if quantity > 20:
            discount = 10
        else:
            discount = 5
    elif quantity > 20:
        discount = 3


def example_2():
    print('Example 2 - collections')

    # Set (no duplicates, unordered)
    my_set: set = { 'a', 'b', 'c' }

    # Arrays not commonly used

    # List 
    my_list: list = ['a', 'b', 'c']

    # Dictionary
    my_dict: dict = { 
        'a': '1',
        'b': '2',
        'c': '3'
    }

    # Tuple
    my_tuple: tuple = ('a', 'b', 'c')


def my_join_function(my_list: list, separator: str = ',') -> str:
    """Return all items in list joined by supplied separator
    
    Return empty string if list is None or empty.  

    Args:
      my_list: List to concatenate
      separator: Separator to use, defaults to comma

    Returns:
      Joined list
    """
    result = ''
    if my_list:
        for item in my_list:
            result += f'{item}{separator}'
        # Remove final separator
        result = result[:-1]
    return result


def example_3():
    print('Example 3 - function declaration')
    print(my_join_function(['a', 'b', 'c'], ';'))


def example_4():
    print('Example 4 - strings and quotes')

    # Simple string
    print('Simple string - The quick brown fox')

    # Preserve escape characters
    print(r'Preserve escape char literals - \tTab and newline\n')

    # Expand variables
    adjective = 'quick'
    noun = 'fox'
    print(f'Expand variables - The {adjective} brown {noun}')

    # Preserve embedded newlines
    print('''Preserve embedded newlines - 
The quick brown fox
jumped over
the lazy dog.''')


def example_5():
    print('Example 5 - string concatenation')

    str = \
        'When I am outside a function ' \
        + 'I have to manually concatenate strings ' \
        + 'and use backslash line continuation'
    print(str)

    print('When I am inside a function '
        'it will automatically concatenate strings without '
        'a line continuation mark '
    )



def example_6():
    print('Example 6 - truthiness')

    # no value
    no_value = None
    if no_value:
        print('Variable "no_value" has a value')
    else:
        print('Variable "no_value" has no value')

    # empty string
    empty_string = ''
    if empty_string:
        print('Variable "empty_string" has a value')
    else:
        print('Variable "empty_string" has no value')

    # white space
    white_space = '     '
    if white_space:
        print('Variable "white_space" has a value')
    else:
        print('Variable "white_space" has no value')

    # normal string
    normal_string = 'test'
    if normal_string:
        print('Variable "normal_string" has a value')
    else:
        print('Variable "normal_string" has no value')

    # empty list
    empty_list = []
    if empty_list:
        print('Variable "empty_list" has a value')
    else:
        print('Variable "empty_list" has no value')

    # non-empty list
    non_empty_list = ['a']
    if non_empty_list:
        print('Variable "non_empty_list" has a value')
    else:
        print('Variable "non_empty_list" has no value')

    # empty dict
    empty_dict = {}
    if empty_dict:
        print('Variable "empty_dict" has a value')
    else:
        print('Variable "empty_dict" has no value')

    # non-empty dict
    non_empty_dict = { 'a': 1 }
    if non_empty_dict:
        print('Variable "non_empty_dict" has a value')
    else:
        print('Variable "non_empty_dict" has no value')


def example_7():
    print('Example 7 - conditional operator')

    items = ['a', 'b', 'c']
    message = str(len(items)) + ' ' + ('item' if len(items) == 1 else 'items')
    print(f'The list {items} contains {message}')

    items = ['a']
    message = str(len(items)) + ' ' + ('item' if len(items) == 1 else 'items')
    print(f'The list {items} contains {message}')


def example_8():
    print('Example 8 - iterate list')
    my_list_1 = ['a', 'b', 'c']
    for my_item in my_list_1:
        print(f'Item: {my_item}')

    my_list_2 = 'oops'
    for my_item in my_list_2:
        print(f'Item: {my_item}')


def example_9():
    print('Example 9 - iterate dictionary')

    # "pets" is a list
    for breed in pets:
        print(f'Breed: {breed}')
        # "pets[breed]" is a dictionary
        for animal in pets[breed]:
            print(f'  Name: {animal["Name"]}')
            print(f'  Breed: {animal["Breed"]}')
            print(f'  Color: {animal["Color"]}')
            print(f'')


def example_10a():
    print('Example 10a - filter, map, sort')

    # This is Python list filter
    matches = list(filter(lambda x: x['State'] == 'PA', employees))
    matches = list(map(lambda x: (x['Name'], x['Position']), matches))
    matches.sort(key=operator.itemgetter(1))

    print('Employees in PA:')
    for (name, position) in matches:
        print(f'{name}: {position}')


def example_10b():
    print('Example 10b - filter, map, sort via list comprehension')

    # This is Python "list comprehension"
    matches = [
        # Like C# LINQ ".Select()"
        (x['Name'], x['Position'])
        # Sort of like C# LINQ Lamba expression variable
        for x
        in employees
        # Like C# LINQ ".Where()"
        if x['State'] == 'PA'
    ]
    matches.sort(key=operator.itemgetter(1))

    print('Employees in PA:')
    for (name, position) in matches:
        print(f'{name}: {position}')


def example_11():
    print('Example 11 - error handling')

    a = 1
    b = a - a
    c = 0
    try:
        c = a/b
    except ZeroDivisionError as ex:
        print(f'Error: {ex}')
    finally:
        print(f'finally, c={c}')



def example_12():
    print('Example 12 - variable scope')

    x = 1
    if(x == 1):
        # This variable is introduced inside a sub-scope, but 
        # is available to the other scope within this function
        y = 2
    else:
        # This code isn't reached
        z = 3
    # Python is perfectly happy with this and will print "2"
    print(y)
    # Python compiles just fine, but gives a runtime error
    # "UnboundLocalError: local variable 'z' referenced before assignment"
    try:
        print(z)
    except Exception as ex:
        print(ex)


class Animal:
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species

    def display(self):
        print(f'Species: {self.species}, name: {self.name}')

    
def example_13():
    print('Example 13 - classes')

    my_animal = Animal('Koko', 'gorilla')
    my_animal.display()


def give_me_a_list(*args):
    for arg in args:
        print(f'arg={arg}')


def give_me_a_diciontary(**kwargs):
    for key in kwargs:
        print(f'{key}={kwargs[key]}')


def example_14():
    print('Example 14 - variable arguments')

    give_me_a_list('z')
    my_list = ['a', 'b', 'c']
    give_me_a_list(*my_list)
    my_dictionary = {'a': 1, 'b': 2, 'c': 3}
    give_me_a_diciontary(**my_dictionary)


def check_type(obj):
    if isinstance(obj,  str):
        print(f'{obj} is a string')
    elif isinstance(obj, int):
        print(f'{obj} is an integer')
    else:
        print(f'{obj} is some other type')


def example_15():
    print('Example 15 - check type')
    check_type('abc')
    check_type(123)


def main():
    print('Start')
    example_1()
    example_2()
    example_3()
    example_4()
    example_5()
    example_6()
    example_7()
    example_8()
    example_9()
    example_10a()
    example_10b()
    example_11()
    example_12()
    example_13()
    example_14()
    example_15()
    print('End')


main()