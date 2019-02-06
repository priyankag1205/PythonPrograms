'''Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.'''
from math import sqrt

def isPrime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for divisor in range(3, int(sqrt(number)+1), 2):
            if number % divisor == 0:
                return False
        return True
    return False

def genPrime(currentNumber):
    if isPrime(currentNumber):
        return currentNumber
    

def main():  

    currentNumber = 2
    while True:

        decision = input('Would you like to continue to generate the next prime? (YES/NO) ')

        if decision.lower() == 'yes':
            currentPrime = genPrime(currentNumber)
            if currentPrime:
                print(currentPrime)

        elif decision.lower()=='no' :
            break    
        else:
            print('Please enter valid choice from YES or No')
         
        currentNumber = currentNumber + 1

   

if __name__ == '__main__':
    main()


	
	
