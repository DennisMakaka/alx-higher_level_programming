def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Expectation('Too far')
            result += (A ** b) / i
        except:
            result += a + b

    return result 
