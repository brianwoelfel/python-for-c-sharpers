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

def test_1():
    print('Test 1 - iterate list')
    my_list_1 = ['a', 'b', 'c']
    for my_item in my_list_1:
        print(f'Item: {my_item}')

    my_list_2 = 'oops'
    for my_item in my_list_2:
        print(f'Item: {my_item}')


def test_2():
    # "pets" is a list
    for breed in pets:
        print(f'Breed: {breed}')
        # "pets[breed]" is a dictionary
        for animal in pets[breed]:
            print(f'  Name: {animal["Name"]}')
            print(f'  Breed: {animal["Breed"]}')
            print(f'  Color: {animal["Color"]}')
            print(f'')


def test_3a():
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


def test_3b():
    # This is Python list filter
    matches = list(filter(lambda x: x['State'] == 'PA', employees))
    matches = list(map(lambda x: (x['Name'], x['Position']), matches))
    matches.sort(key=operator.itemgetter(1))

    print('Employees in PA:')
    for (name, position) in matches:
        print(f'{name}: {position}')


def test_4():
    print('Test 4 - conditional operator')

    items = ['a', 'b', 'c']
    message = str(len(items)) + ' ' + ('item' if len(items) == 1 else 'items')
    print(f'The list {items} contains {message}')

    items = ['a']
    message = str(len(items)) + ' ' + ('item' if len(items) == 1 else 'items')
    print(f'The list {items} contains {message}')


def test_5():
    print('Test 5')

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


def test_6():
    print('Test 6')

    str = \
        'When I am outside a function ' \
        + 'I have to manually concatenate strings ' \
        + 'and use backslash line continuation'
    print(str)

    print('When I am inside a function '
        'it will automatically concatenate strings without '
        'a line continuation mark '
    )


def test_7():
    print('Test 7')

    a = 1
    b = a - a
    c = 0
    try:
        c = a/b
    except ZeroDivisionError as ex:
        print(f'Error: {ex}')
    finally:
        print(f'finally, c={c}')


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


def test_8():
    print('Test 8')

    print(my_join_function(['a', 'b', 'c'], ';'))


def test_9():
    print('Test 9')

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


def test_10():
    print('Test 10')

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


def test_11():
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


class Animal:
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species

    def display(self):
        print(f'Species: {self.species}, name: {self.name}')

    
def test_12():
    my_animal = Animal('Gregory', 'lion')
    my_animal.display()


def test_13():
    print('Test 13 - demonstrate nesting and white space')
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


def give_me_a_list(*args):
    for arg in args:
        print(f'arg={arg}')


def give_me_a_diciontary(**kwargs):
    for key in kwargs:
        print(f'{key}={kwargs[key]}')


def test_14():
    print('Test 14 - variable arguments')

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


def test_15():
    print('Test15 - check type')
    check_type('abc')
    check_type(123)


def main():
    print('Start')
    test_1()
    test_2()
    test_3a()
    test_3b()
    test_4()
    test_5()
    test_6()
    test_7()
    test_8()
    test_9()
    test_10()
    test_11()
    test_12()
    test_13()
    test_14()
    test_15()
    print('End')


main()