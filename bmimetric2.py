weight = float(input("Please enter weight in kilograms: "))
height = float(input("Please enter height in meters: "))

bmi = weight/(height * height)
bmi = round(bmi,2)

if(bmi < 18.5):
    cdc_standard = "Underweight"
elif(bmi >= 18.5 and bmi <= 24.9):
    cdc_standard = "Normal"
elif(bmi >= 20.05 and bmi <= 29.9):
    cdc_standard = "Overweight"
elif(bmi >= 30.0):
    cdc_standard = "Obese"    

print("BMI is: " + str(bmi) + ". status is " + str(cdc_standard))