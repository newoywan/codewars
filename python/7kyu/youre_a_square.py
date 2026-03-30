def is_square(n):
    if n < 0:
        return False7
    
    root = int(n ** 0.5)
    return root * root == n

