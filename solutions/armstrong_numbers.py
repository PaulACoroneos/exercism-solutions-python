
# def is_armstrong_number(number):
#     orig_num = number
#     sum = 0
#     count = 0;
#     num_arr = []
#     while(number > 0):
#         num_arr.append(number% 10)
#         number = number // 10
#         count +=1
#     for digit in range(count):
#         sum = sum + num_arr[digit]**count
        
#     return orig_num - sum == 0



def is_armstrong_number(number):
    str_num = str(number)
    sum = 0
    for digit in str_num:
        sum = sum + int(digit) ** len(str(number));
    return number - sum == 0