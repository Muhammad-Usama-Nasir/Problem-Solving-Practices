
temp_list = []
num_list = []

def func(n):
    if n <= 1:
        return n
    
    r1 = func(n-1) 
    r2 = func(n-2) 
    result = r1 + r2
    temp_list.extend([r1, r2, result])

    for num in temp_list:
        if num not in num_list:
            num_list.append(num)
    print(result)
    print(num_list)
    return result


def main():
    user_input = int(input("Enter a Number: "))
    if user_input <= 1:
        print("Number not valid for this Operation!!!")
        return
    
    func(user_input)
    
main()