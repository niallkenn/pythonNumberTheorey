running = True 

def convertBase():
    n = int(input('Enter Number: '))
    base = int(input('Enter Base: '))
    
    digits = []
    strr = ""
    
    remainder = 0
    
    while n != 0:
        remainder = n % base
        n = (n - remainder) // base
        digits.append(remainder)
    
    for digit in digits:
        strr = str(digit) + ', ' + strr

    if base <= 10:
        strPrint = ''
        for digit in digits:
            strPrint += str(digit)
        print(strPrint)
    else:
        print('(' + strr[0:-2] + ')' + '\n')
    
    
while running:
    print("1: Convert Base")
    mode = int(input("Select Mode: "))
    
    if mode == 1:
        
        convertBase()    
