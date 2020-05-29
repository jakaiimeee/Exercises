
def ranger(number):
    if number >=0 and number <=100:
        data="GREATNESS"
    else:
        data="Oops"
    return data
number=int(input("Any number"))
result=ranger(number)
print(result)
