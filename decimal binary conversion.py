""" CONVERSION OF DENARY  TO BINARY """

def base2converter(n):
    binaryval  =[]
    ans = 0

    while n > ans:
       remainder = n % 2
       binaryval.append(remainder)
       ans = n // 2
    print(binaryval)

base2converter(5)