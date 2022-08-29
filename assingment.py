import math 

def get_type_of_training(type, per):
    per = (100 - per) * 0.01

    if type == 1:
        print("Gym workout for fat loss\n")

        print(f"""Plate thrusters ({math.ceil(15*per)} reps x 3 sets)\nMountain climbers ({math.ceil(20*per)} reps x 3 sets)\nBox jumps ({math.ceil(10*per)} reps x 3 sets)\nLounges ({math.ceil(10*per)} reps x 3 sets)\nRenegade rows ({math.ceil(10*per)} reps x 3 sets)\nPress ups ({math.ceil(15*per)} reps x 3 sets)\nTreadmill ({math.ceil(10*per)} mins x 2 sets)\nSupermans ({math.ceil(10*per)} reps x 3 sets)\nCrunches ({math.ceil(10*per)} reps x 3 sets) """)
    
    elif type == 2:
        print("Gym workout for stretch and relax\n")

        print(f"""Quad stretchs ({math.ceil(2*per)} mins x 3 sets)\nHamstring stretchs ({math.ceil(2*per)} mins x 3 sets)\nChest and shoulder stretchs ({math.ceil(2*per)} mins x 2 sets)\nUpper back stretchs ({math.ceil(3*per)} mins x 2 sets)\nBiceps stretchs ({math.ceil(2*per)} mins x 2 sets)\nTriceps stretchs ({math.ceil(2*per)} mins x 3 sets)\nHip flexors ({math.ceil(2*per)} mins x 3 sets)\nCalf stretchs ({math.ceil(2*per)} mins x 3 sets)\nLower back stretchs ({math.ceil(2*per)} mins x 3 sets)""")

    elif type == 3:
        print("Gym workout for high-intensity exercises\n") 

        print(f"""Jumping jacks ({math.ceil(20*per)} reps x 4 sets)\nSprints ({math.ceil(20*per)} reps x 3 sets)\nMountain climbers ({math.ceil(20*per)} reps x 4 sets)\nSquat jumps ({math.ceil(20*per)} reps x 4 sets)\nLunges ({math.ceil(20*per)} reps x 3 sets)\nCrunches ({math.ceil(20*per)} reps x 3 sets)\nTreadmill ({math.ceil(15*per)} mins x 2 sets)\nSide planks ({math.ceil(15*per)} reps x 3 sets)\nBurpees ({math.ceil(15*per)} reps x 3 sets)""")

    elif type == 4:
        print("Gym workout for strong legs\n")

        print(f"""Back squats ({math.ceil(10*per)} reps x 5 sets)\nHip thrusts ({math.ceil(12*per)} reps x 3 sets)\nOverhead presses ({math.ceil(10*per)} reps x 5 sets)\nRack pulls ({math.ceil(10*per)} reps x 5 sets)\nSquats ({math.ceil(10*per)} reps x 4 sets)\nDumbbell lunges ({math.ceil(10*per)} reps x 3 sets)\nLeg curls ({math.ceil(15*per)} reps x 3 sets)\nStanding calf raises ({math.ceil(20*per)} reps x 2 sets)""")

    elif type == 5:
        print("Gym workout for strong ABS\n")

        print(f"""Cross crunchs ({math.ceil(12*per)} reps x 3 sets)\nKnee ups ({math.ceil(15*per)} reps x 5 sets)\nHip thrusts ({math.ceil(15*per)} reps x 3 sets)\nMountain climbers ({math.ceil(15*per)} reps x 3 sets)\nVertical hip thrusts ({math.ceil(12*per)} reps x 3 sets)\nBicycles ({math.ceil(15*per)} mins x 2 sets)\nFront planks ({math.ceil(15*per)}) mins x 3 sets)\nDragon flags ({math.ceil(12*per)} reps x 4 sets)\neverse crunches ({math.ceil(10*per)} reps x 3 sets)""")

    elif type == 6:
        print("Gym workout for strong shoulder and arms\n")

        print(f"""Bench presses ({math.ceil(10*per)} reps x 5 sets)\nTriceps dips ({math.ceil(10*per)} reps x 5 sets)\nIncline dumbbell presses ({math.ceil(12*per)} reps x 3 sets)\ndumbbell flyes ({math.ceil(15*per)} reps x 3 sets)\nTriceps extensions ({math.ceil(15*per)} reps x 3 sets)\nPull ups ({math.ceil(10*per)} reps x 5 sets)\nTreadmill ({math.ceil(15*per)} mins x 2 sets)\nBent over rows ({math.ceil(10*per)} reps x 5 sets)\nChin ups ({math.ceil(10*per)} reps x 3 sets)""")

    elif type == 7:
        print("Gym workout for a male younger than 18 years old\n")

        print(f"""High knees ({math.ceil(20*per)} reps x 3 sets)\nSquats ({math.ceil(10*per)} reps x 3 sets)\nCalf raises ({math.ceil(10*per)} reps x 3 sets)\nScissor jumps ({math.ceil(12*per)} reps x 3 sets)\nBurpees ({math.ceil(10*per)} reps x 3 sets)\nTreadmill ({math.ceil(10*per)} mins x 2 sets)""")
    
    elif type == 8:
        print("Gym workout for a female younger than 18 years old\n")

        print(f"""Squats ({math.ceil(10*per)} reps x 3 sets)\nCrunches ({math.ceil(10*per)} reps x 2 sets)\nJumping jacks ({math.ceil(10*per)} reps x 3 sets)\nPush ups ({math.ceil(10*per)} reps x 2 sets)\nBurpees ({math.ceil(10*per)} reps x 3 sets)\nTreadmill ({math.ceil(10*per)} mins x 2 sets)""")

    elif type == 9:
        print("Gym workout for a male at least 18 years old\n")

        print(f"""Standing biceps curls ({math.ceil(20*per)} reps x 3 sets)\nSeated incline curls ({math.ceil(18*per)} reps x 3 sets)\nSeated dumbbell presses ({math.ceil(12*per)} reps x 3 sets)\nLeg presses ({math.ceil(15*per)} reps x 3 sets)\nBench presses ({math.ceil(10*per)} reps x 4 sets)\nTricep kickbacks ({math.ceil(15*per)} reps x 3 sets)\nHip thrusts ({math.ceil(12*per)} reps x 3 sets)\nSeated rows ({math.ceil(10*per)} reps x 4 sets)""")

    elif type == 10:
        print("Gym workout for a female at least 18 years old\n")

        print(f"""Lateral raises ({math.ceil(15*per)} reps x 3 sets)\nReverse flyes ({math.ceil(12*per)} reps x 3 sets)\nHip thrusts ({math.ceil(12*per)} reps x 3 sets)\nIncline dumbbell presses ({math.ceil(15*per)} reps x 3 sets)\nSquats ({math.ceil(10*per)} reps x 4 sets)\nDumbbell lunges ({math.ceil(10*per)} reps x 3 sets)\nLeg presses ({math.ceil(12*per)} reps x 3 sets)\nDumbbell presses ({math.ceil(10*per)} reps x 4 sets)""")

def get_percent_of_training(age):

    # 61세 ~ 65세
    if age <= 65 and age > 60:
        per = (age%60)
    # 66세 ~ 75세
    elif age <= 75 and age > 65:
        per = 5 + (age%65 * 2)
    # 76세 ~ 80세
    elif age <= 80 and age > 75:
        per = 25 + (age%75 * 3)
    # 80세 초과 
    elif age > 80:
        per = 40 + (age%80 * 4)
        if per > 80 :   # 최대 80%
            per = 80
    
    return per

def print_routine(age, sex, type_num, day):
    
    i = 1 
    
    # 횟수 계산을 위한 percentage 설정
    if age >= 60:
        per = get_percent_of_training(age)
    else:
        per = 0

    print(f"per is {per}")
    while i <= day:
        print("-------------------------------------------------------------------------------------")
        print(f"Day {i}")
        if i%2 != 0:
            get_type_of_training(type_num, per)
        
        else:
            # 18세 이하의 경우
            if sex == 'male' and age <= 18:
                get_type_of_training(7, per)
            elif sex == 'female' and age <= 18:
                get_type_of_training(8, per)
            
            # 19세 이상
            elif sex == 'male' and age > 18:
                get_type_of_training(9, per)
            elif sex == 'female' and age > 18 :
                get_type_of_training(10, per)

        i = i + 1

    print("-------------------------------------------------------------------------------------\n")

def main():
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    sex = input("Please enter your biological sex (female/male): ")

    print("What do you want to get out of your training?")
    print("     1. Your goal is losing weight")
    print("     2. Your goal is to staying calm and relax")
    print("     3. Your goal is increasing your heart rate")
    print("     4. Your goal is having stronger legs")
    print("     5. Your goal is having stronger ABS")
    print("     6. Your goal is having stronger shoulders and arms")

    type_num = int(input("Choose a number between 1 to 6: "))

    day = int(input("How many days per week you can train: "))

    print(f"Hello {name}! Here is your training:")
    print_routine(age, sex, type_num, day)
    print(f"Bye {name}.")


if  __name__ == "__main__":
    main()

