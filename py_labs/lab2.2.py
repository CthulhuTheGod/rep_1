def prime_number_seq():
    prime_number_list = list()
    a = input('Input an integer positive number: ')
    assert a.isnumeric(), f"{a} is inappropriate input"
    my_range = range(2, int(a))
    for i in my_range:
        div_count = 0
        for j in my_range:
            if i % j == 0:
                div_count += 1
        if div_count == 1:
            # Если от 2 до a было только одно деление (a/a), дополняем список
            prime_number_list.append(i)
    print(f"Prime number list: {prime_number_list}")

prime_number_seq()