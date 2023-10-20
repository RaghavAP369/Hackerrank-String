def print_formatted(number):
    width = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        decimal_str = str(i).rjust(width)
        octal_str = oct(i)[2:].rjust(width)
        hexadecimal_str = hex(i)[2:].upper().rjust(width)
        binary_str = bin(i)[2:].rjust(width)
        
        print(f"{decimal_str} {octal_str} {hexadecimal_str} {binary_str}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
