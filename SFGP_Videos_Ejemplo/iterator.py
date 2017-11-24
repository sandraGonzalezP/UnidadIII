"""Sandra Fabiola Gonzalez Puente"""
"""must provide a method for obtaining each object that you can create."""


def count_to(count):
    """Our iterator implementation"""

    # Our list
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

    # Our built-in iterator
    # Creatres a tuple such as (1, "eins")
    iterator = zip(range(count), numbers_in_german)

    # Iterate though our iterable list
    # Extract the German numbers
    # Put them in a generator called number
    for position, number in iterator:
        # Returns a 'generator' containing numbers in German
        yield number


# Let´s test the generator returned by our iterator
for num in count_to(3):
    print("{}".format(num))

for num in count_to(4):
    print("{}".format(num))
