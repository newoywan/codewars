def high_and_low(numbers):
    it = map(int, numbers.split())
    high = low = next(it)
    
    for n in it:
        if n > high:
            high = n
        elif n < low:
            low = n
    
    return f"{high} {low}"