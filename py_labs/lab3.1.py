def calc(a, op, b):
    a = int(a)
    b = int(b)
    match op:
        case _ if op == '+': return a+b
        case _ if op == '-': return a-b
        case _ if op == '*': return a*b
        case _ if op == '/': return a/b

while True:
    try:
        a, op, b = input('a_?_b: ').split()
        print(f'= {calc(a, op, b)}')
    except Exception as e:
        print(f'Error: {e}, try again 👀')
    finally:
        print('Ctrl + C to interrupt ⛔')