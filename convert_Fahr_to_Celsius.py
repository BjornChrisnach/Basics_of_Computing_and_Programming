def main():
    print("Please enter the temperature in Fahrenheit: ")
    temp_fahr = float(input())
    temp_celsius = fahrenheit_to_celsius(temp_fahr)
    print(temp_fahr, "Fahrenheit is", temp_celsius, "Celcius")

def fahrenheit_to_celsius(F):
    temp_celc = (F - 32) * (5/9)
    temp_celc = round(temp_celc, 3)
    return temp_celc
    # print(F, "Fahrenheit is", temp_celc, "Celcius")

main()