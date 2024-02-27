
while True:
    n = float(input('Digite um número: '))

    def fatorial(n):
        return 1 if n <= 1 else n * fatorial(n-1)
            
            # if n > 1:
        #     n = n
        # else:
        #     n = 1
        
    print(fatorial(n))