def decimal_to_binary(n):
    if n == 0:
        return '0'
    else:
        binary = ''
        while n>=1:
            remainder = n%2
            binary = str(remainder)+binary
            n = n//2
    return binary
        
print(decimal_to_binary(45))