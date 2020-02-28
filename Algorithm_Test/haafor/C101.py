# Calculate the value of exp( x ) upto p-th decimal place.
# exp(x) = 1/0! + x/1! + x^2/2! + x^3/3! + x^4/4! + ....

# exp(x) = 1 + (x/1) * (1+(x/2)) * (1+(x/3) * (1+(x/4) ....


def check_exp(x):
    sum = 1
    for i in range(100, 0, -1):
        sum = 1 + x * sum / i
    print(sum)

check_exp(2)


##########################################################
# import math
#
# solve = math.exp(2)
# print(solve)