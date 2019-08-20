  
fat_cals = 1
cals = 0
while cals < fat_cals:
    cals = int(input("Please input the number of calories: "))
    grams_fat = int(input("Please input the number of grams of fat: "))
    fat_cals = grams_fat*9
    percent_cals_fat = round((fat_cals/cals)*100, 1)
    if cals < fat_cals:
        print("Calories from fat cannot be greater than the total number of calories in food item.")
    else:
        print("Calories from fat: ", fat_cals)
        print("Total calories: ", cals)
        print("Percentage of calories from fat: ", percent_cals_fat, "%", sep = "")
        if percent_cals_fat < 30.0:
            print("Food is low in fat.")

  

        

