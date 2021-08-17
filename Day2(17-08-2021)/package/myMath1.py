class Math:
    def isPrime(num):
        for i in range(2,num):
            if num%i ==0:
                return False
        return True

    def power(base,pval):
        return base**pval
            
        
