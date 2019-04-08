'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
#---------------------------------------------------------------
# palin = []
# for x in range (100, 1000):
#     for y in range (100, 1000) :
#         num = x*y
#         intnum = num
#         num = str(num)
#         if num == num[::-1] :
#             palin.append(intnum)
# palin.sort()
# print(palin)
#---------------------------------------------------------------
# palindrom = 0
# for i in range(100, 1000):
#     for j in range(100, 1000):
#         a = i * j
#         if str(a) == str(a)[:: -1] and a > palindrom:
#             palindrom = a
# print(palindrom)
#---------------------------------------------------------------
# listOfPalindromes = []
# for i in range(999, 100,-1):
#     for j in range(999, 100,-1):
#         number = i * j
#         num_string = str(number)
#         if len(num_string) == 5:
#             if num_string[0] == num_string[-1]:
#                 if num_string[1] == num_string[-2]:
#                     listOfPalindromes.append(number)
#         elif len(num_string) == 6:
#             if num_string[0] == num_string[-1]:
#                 if num_string[1] == num_string[-2]:
#                     if num_string[2] == num_string[-3]:
#                         listOfPalindromes.append(number)
#         else:
#             print("There has been an error.")
# # print(max(listOfPalindromes))
# listOfPalindromes.sort()
# print(listOfPalindromes)
#---------------------------------------------------------------
palindrom = []
for i in range(100, 1000):
    for j in range(100, 1000):
        a = i * j
        if str(a) == str(a)[:: -1]:
            palindrom.append(a)
palindrom.sort()
print(palindrom)