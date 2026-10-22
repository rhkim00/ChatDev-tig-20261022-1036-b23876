import math

def calculate_characteristic():
    characteristic = 2
    return characteristic

def calculate_symmetric_group_elements(n):
    elements = math.factorial(n)
    return elements

def main():
    characteristic = calculate_characteristic()
    print('The characteristic of 2Z is:', characteristic)
    
    n = 10
    elements = calculate_symmetric_group_elements(n)
    print('The number of elements in S_10 is:', elements)

if __name__ == '__main__':
    main()