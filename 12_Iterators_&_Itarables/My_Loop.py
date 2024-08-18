"""

for letter in 'SOME TEXT'               =           inter('SOME TEXT')
    print(letter)                       =

"""
def my_for(iterable):
    it = iter(iterable)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


numbers = [1, 2, 3, 4, 5]

my_for(numbers)

