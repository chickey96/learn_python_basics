# returns all self dividing numbers in range from left to right
# self dividing numbers are divisible by every digit they contain
def find_self_dividing_numbers(left, right):
    self_dividing_nums = []
   
    # loop through numbers starting with left up to and including right
    for num in range(left, right + 1):
       
        if(is_self_dividing(num)):
            self_dividing_nums.append(num)
    
    return self_dividing_nums

# determines whether a number is divisible by all the digits it contains
# self dividing numbers may not contain the digit 0
def is_self_dividing(num):
    digits_to_check = num

    # loop through each digit in num
    while(digits_to_check > 0):
        last_digit = digits_to_check % 10
      
        # numbers containing the digit 0 are not self dividing 
        if(last_digit == 0):
            return False 
        # check if original num is divisible by the last digit
        if(num % last_digit != 0):
            return False 

        # remove last digit
        digits_to_check //= 10

    return True 

# tested more thoroughly using leetcode interface
test_case = find_self_dividing_numbers(1, 22)
print(f'{test_case} should equal [1,2,3,4,5,6,7,8,9,11,12,15,22]')
print(test_case == [1,2,3,4,5,6,7,8,9,11,12,15,22])
