def evaluation():
    a = int(input('Insert a number (0-100): '))
    assert 0 <= a <= 100 , "The number must be 0-100"
    
    match a:
        case _ if a <= 59: grade = 'F'
        case _ if a <= 69: grade = 'D'
        case _ if a <= 79: grade = 'C'
        case _ if a <= 89: grade = 'B'
        case _: grade = 'A'
    
    print(f'Your number is evaluated as: {grade}')
try:
    evaluation()
except Exception as e:
    print('Error: ', e, type(e))