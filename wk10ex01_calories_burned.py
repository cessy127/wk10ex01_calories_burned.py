def computeSessionCalories(code, mins):
    if code == 1:
        sessionCalories = 4 * mins
    else:
        if code == 2:
            sessionCalories = 10 * mins
        else:
            if code == 3:
                sessionCalories = 8 * mins
            else:
                sessionCalories = 0
    return sessionCalories
 
# Main
caloriesList = [0] * (10)
 
totalCalories = 0
sessions = int(input())
index = 1
while index <= sessions:
    activityCode = int(input())
    minutes = int(input())
    sessionCalories = computeSessionCalories(activityCode, minutes)
    caloriesList[index - 1] = sessionCalories
    totalCalories = totalCalories + sessionCalories
    index = index + 1
print("Total calories burned: " + str(totalCalories))
