error = "Error, Please try again"
while True:
    number = input("Please enter a number: ")
    if not number.isnumeric():
        print(error)
        continue
    else:
        number = int(number)
        break
for i in range(0, number+1):
    print("*"*i)
    i += 1
    if i == number+1:
        i = number-1
        while range(0, number+1):
            print("*"*i)
            i -= 1
            if i == 0:
                break