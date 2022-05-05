
#CALCOLATRICE BY LUIGI.EXE

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y

print("CALCOLATRICE BY LUIGI.EXE") 


print("Quale operazione vuoi scegliere ??")

print("1.SOTTRAZIONE")
print("2.SOMMA")
print("3.DIVISIONE")
print("4.MOLTIPICAZIONE")
while True:
   
    choice = input("ALLORA QUALE SCEGLI?(1/2/3/4): ")

    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("METTI IL PRIMO NUMERO: "))
        num2 = float(input("METTI IL SECONDO NUMERO: "))

        if choice == '2':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '1':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '4':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '3':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        next_calculation = input("CONTINUIAMO [SI O NO] ?? ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")