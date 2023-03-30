#Functions
def pw(word):
    print(word,end=' ')

def index(num):
    if num > 999999999999:
        return 4
    elif num > 999999999:
        return 3
    elif num > 999999:
        return 2
    elif num > 999:
        return 1
    elif num > 99:
        return 0
        
def count(num):
    count = 0
    while num>0:
        num //= 10
        count += 1
    return count

def printwords(num):
    n = count(num)
    base = 10**2 if n < 4 else 10**3 if n < 7 else 10**6 if n < 10 else 10**9 if n < 13 else 10**12
    if n == 0:
        return 0
    elif n == 1:
        pw(ones[num - 1])
    elif n == 2:
        if num < 20:
            pw(teens[num%10])
        else:
            pw(tens[num//10 - 2])
            if num%10:
                print('\b-',end = '')
                printwords(num%10)
    else:
        printwords(num//base)
        pw(deno[index(num)])
        printwords(num%base)    
                 
ones = ('One','Two','Three','Four','Five','Six','Seven','Eight','Nine')
teens = ('Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen')
tens = ('Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety')
deno = ('Hundred','Thousand','Million','Billion','Trillion')
        #100       #1000      #1,000,000   #1000,000,000   #10¹²
try:
    num = int(input('Enter the Number: '))
    if num == 0:
        print('Zero')
    if num < 0:
        num = -1*num
        print('Negative',end=' ')
    printwords(num)
except ValueError:
    print('Enter Only Numbers')