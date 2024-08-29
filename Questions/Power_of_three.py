# def power(n:int)->bool:
#     for i in range(n):
#         result = pow(3,i)
#         if(n == result):
#             return True
#     return False
# print(power(590))

def power(n: int) -> bool:
    if n < 1:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1

print(power(45))  # This should return True
