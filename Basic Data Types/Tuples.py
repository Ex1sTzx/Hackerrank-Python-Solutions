if __name__ == '__main__':
    n = int(input())
    numbers = map(int, input().split())
    
    num_tuple = tuple(numbers)
    print(hash(num_tuple))