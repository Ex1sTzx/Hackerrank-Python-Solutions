if __name__ == '__main__':
 L = []
N = int(input())
for _ in range(N):
    user_input = input().split()
    operation = user_input[0]
    arg = user_input[1:]
    if operation != "print":
        operation += "(" + ",".join(arg) + ")"
        eval("L." + operation)
    else:
        print(L)