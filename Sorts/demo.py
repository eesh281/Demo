def binary_dec(x):
    # x = 37
    # import ipdb; ipdb.set_trace()
    value_1 = x%2
    value_2 = x//2
    obj1 = ""
    while(value_2 != 1 or 0):
        value_3 = value_2%2 
        value_4 = value_2//2
        value_2 = value_4
        obj1 += str(value_3)
        # print(obj1)
    if value_2 == 1:
        y = str(value_1)+str(obj1)+str(value_2)
    if value_2 == 0:
        y = str(value_1)+str(obj1)+str(value_2)
    return print(y[::-1])
    
# x=456678899234567898765456678899234567898765
# binary_dec(x)

def rev(x):
    # import ipdb;ipdb.set_trace()
    last_digit = x % 10
    quo = x // 10
    print(last_digit)
    # print(quo)
    count=0
    while quo>10:
        last_digit_1 = quo % 10
        quo_1 = quo // 10
        print(last_digit_1)
        print(quo_1)
        quo = quo_1
        count+=1
    final_count = count+1
    # if final_count == 2:
    #     y=100
    while final_count > 0:
        y = 10^final_count
        first_digit = last_digit*y
        final_count-=1
        


x=124
rev(x)