import random
def num_gen():
    random_number = random.randint(1, 100)
    return random_number
int_num_gen = int(num_gen())

a = 0
tries = 0
diff = int(input('Choose difficulty (1-100): '))
while a != int_num_gen:
    try:
        a = input('Guess a number: ')
        assert a.isnumeric, f'{a} is not a numeric!'
        a = int(a)        
        match a:
            case _ if a < int_num_gen: print(f'The number is bigger than {a}, try again!')
            case _ if a > int_num_gen: print(f'The number is smaller than {a}, try again!')
            case _ if a == int_num_gen: print(f'Congrats! {a} is the hidden number! 🎉🎉🎉')
        tries += 1
        # Подсказка после 5 попыток:
        if tries == diff:
            print(f'the number is {bin(int_num_gen)} 😉')
    except:
        print(f'{a} is a bad value')
