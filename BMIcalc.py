def bmiRating(bmi):
    if(bmi < 20):
        print("You are underweight.")
    if(bmi >= 20 and bmi <= 25):
        print("You are at a normal weight.")
    if(bmi > 25 and bmi <= 30):
        print("You are overweight.")
    if(bmi > 30 and bmi <= 40):
        print("You are obese.")
    if(bmi > 40):
        print("You are extremely obese.")

def bmiImperial():
    h = input("What is your height in inches? ")
    if(float(h) <= 0):
        h = input("Please enter a valid height: ")
    w = input("What is your weight in pounds? ")
    if(float(w) <= 0):
        w = input("Please enter a valid weight: ")
    height = float(h)
    weight = float(w)
    bmi = weight/(height ** 2) * 703
    print("Your BMI is " + str(bmi))
    bmiRating(bmi)

def bmiMetric():
    h = input("What is your height in meters? ")
    if(float(h) <= 0):
        h = input("Please enter a valid height: ")
    w = input("What is your weight in kilograms? ")
    if(float(w) <= 0):
        w = input("Please enter a valid weight: ")
    height = float(h)
    weight = float(w)
    bmi = weight/(height ** 2)
    print("Your BMI is " + str(bmi))
    bmiRating(bmi)

def bmiMetricCm():
    h = input("What is your height in centimeters? ")
    if(float(h) <= 0):
        h = input("Please enter a valid height: ")
    w = input("What is your weight in kilograms? ")
    if(float(w) <= 0):
        w = input("Please enter a valid weight: ")
    height = float(h)
    weight = float(w)
    bmi = weight/(height ** 2) * 10000
    print("Your BMI is " + str(bmi))
    bmiRating(bmi)

def helper():
    units = input("Would you like to use meters, centimeters, or inches for your height unit? ")
    if(units != "meters" and units != "Meters" and units != "centimeters" and units != "Centimeters" and units != "inches" and units != "Inches"):
        while(units != "meters" and units != "Meters" and units != "centimeters" and units != "Centimeters" and units != "inches" and units != "Inches"):
            units = input("Please enter a valid height unit: ")
    if(units == "meters" or units == "Meters"):
        bmiMetric()
    if(units == "centimeters" or units == "Centimeters"):
        bmiMetricCm()
    if(units == "inches" or units == "Inches"):
        bmiImperial()

helper()
