weight = float(input("Please input weight in kg: "))
feet = int(input("Please input your feet: "))
inch = int(input("Please input you inch: "))
height = (feet*0.3048)+(inch * 0.0254)
BMI = weight/(height**2.0)
print("Your BMI is: {}".format(BMI))