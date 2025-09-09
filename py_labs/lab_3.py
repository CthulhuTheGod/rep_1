def triangle_check():

    a = input('Insert A side of triangle: ')
    b = input('Insert B side of triangle: ')
    c = input('Insert C side of triangle: ')
    assert (float(a) > 0 and float(b) > 0 and float(c) > 0), "A side can't be <= 0"

    if a == b == c:
        print('The triangle is equilateral')
    elif a == b or b == c or c == a:
        print('The triangle is isosceles')
    else:
        print('The triangle is scalene')

try:
    triangle_check()
except Exception as e:
    print(f"Error: {e}")