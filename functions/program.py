def calcTime(args):
    def inner():
        import time
        t1=time.time()
        args()#calling the fuctions indirectly
        t2=time.time()
        print(f'Time = {t2-t1}')
    return inner
@calcTime
def fibo():
    fn=int(input('Enter first numer:'))
    sn=int(input('Enter second numer:'))
    n=int(input('No.of values:'))
    if n==1:
        print(fn,end=' ')
    elif n==2:
        print(fn,sn,end=' ')
    else:
        print(fn,sn,end=' ')
        for i in range(n-2):
            tn=fn+sn
            print(tn,end=' ')
            fn,sn=sn,tn
        print()
@calcTime
def primeNumbers():
    LL=int(input('Enter the lower range:'))
    UL=int(input('Enter the Upper range:'))
    count=0
    L=[]
    for n in range(LL,UL+1):
        if n>0:
            for i in range(2,n//2+1):
                if n%i==0:
                    break
            else:
                L.append(n)
    print(L)

@calcTime
def palindromeNum():
    n=int(input('Enter a number:'))
    rev=0
    dummy=n
    while dummy>0:
        r=dummy%10
        dummy//=10
        rev=rev*10+r
    if n==rev:
        print(True)
    else:
        print(False)
@calcTime
def palindrome():
    word=input('Enter a String:')
    rev=''
    for i in word:
        rev=str(i)+rev
    if word==rev:
        print(f'{word} is a palindrome')
    else:
        print(f'{word} is not a palindrome')
    
palindrome()