import csv
import os

exerciseLibrary = [{'Intensity': 'Light', 'CaloriesBurnedPer30mins': 100},
                   {'Intensity': 'Moderate', 'CaloriesBurnedPer30mins': 200},
                   {'Intensity': 'Intense', 'CaloriesBurnedPer30mins': 300}]

class User():
    def __init__(self, username, password, goal):
        self.username = username
        self.password = password
        self.goal = goal
    
    caloriesConsumed = 0
    caloriesBurned = 0

    def addCaloriesConsumed(self):
        newCals = input("Type how many calories as an integer: ")
        self.caloriesConsumed = self.caloriesConsumed + int(newCals)
        print(f'Calories consumed: {self.caloriesConsumed}')
    def addExercise(self):
        caloriesCalculation = 0

        exercise = input("1. Light Exercise \n2. Moderate Exercise \n3. Intense Exercise \nChoose number for your exercise:")
        time = int(input("How long was the exercise(in minutes): "))
        if exercise == '1':
            caloriesCalculation = (exerciseLibrary[0]['CaloriesBurnedPer30mins']//30) * time
            self.caloriesBurned = self.caloriesBurned + caloriesCalculation
            print(f'So you have burned approx: {caloriesCalculation} calories with this workout')
        elif exercise == '2':
            caloriesCalculation = (exerciseLibrary[1]['CaloriesBurnedPer30mins']//30) * time
            self.caloriesBurned = self.caloriesBurned + caloriesCalculation
            print(f'So you have burned approx: {caloriesCalculation} calories with this workout')
        elif exercise == '3':
            caloriesCalculation = (exerciseLibrary[2]['CaloriesBurnedPer30mins']//30) * time
            self.caloriesBurned = self.caloriesBurned + caloriesCalculation
            print(f'So you have burned approx: {caloriesCalculation} calories with this workout')
        else:
            print("Input unrecognized")
            return
    
    def getSummary(self):

        # Summary for weight loss, weight gain, and maintain
        summary = ""
        if self.goal == "Lose weight":
            summary = f'\n{self.username}`s Summary: \nYour goal was to {self.goal}. In order to do so you must eat at a calorie deficit.\nYou consumed: {self.caloriesConsumed} calories\nYou burned: {self.caloriesBurned + 1400}\nSo therefore your count for today is {self.caloriesConsumed-(self.caloriesBurned + 1400)} calories. \nThe lower this number is, The better! (Not too low though)'
        elif self.goal == "Gain weight":
            summary = f'\n{self.username}`s Summary: \nYour goal was to {self.goal}. In order to do so you must eat at a calorie surplus.\nYou consumed: {self.caloriesConsumed} calories\nYou burned: {self.caloriesBurned + 1400}\nSo therefore your count for today is {self.caloriesConsumed-(self.caloriesBurned + 1400)} calories. \nThe higher this number is, The better! (Not too high though)'
        elif self.goal == "Maintain weight":
            summary = f'\n{self.username}`s Summary: \nYour goal was to {self.goal}. In order to do so you must eat at calorie maintenance.\nYou consumed: {self.caloriesConsumed} calories\nYou burned: {self.caloriesBurned + 1400}\nSo therefore your count for today is {self.caloriesConsumed-(self.caloriesBurned + 1400)} calories. \nThe closer this number is to Zero 0, The better!'
        return summary

    
def initializeUser(username, password, goal):
        global current_user
        current_user = User(username, password, goal)

class UserSystem():
    def __init__(self, database="UserBase.csv"):
        self.database = database
        self.users = self.LoadUsers()

    def LoadUsers(self):
        # Check if the database exists
        if os.path.isfile(self.database):
            with open(self.database, 'r') as f:
                reader = csv.DictReader(f)
                return list(reader)
        else:
            return []

    def SaveUsers(self):
        with open(self.database, 'w') as f:
            fieldnames = ['Username', 'Password', 'Goal']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for user in self.users:
                writer.writerow(user)

    def sign_up(self):
        username = input("Enter a username: ")

        # Check if username is already in database
        if any(username == user['Username'] for user in self.users):
            print("Username already taken.")
            return

        password = input("Enter a password: ")

        goal = input("Choose a goal: \n1. Lose weight \n2. Gain weight \n3. Maintain weight \n(1/2/3): ")

        if goal == '1':
            self.users.append({'Username': username, 'Password': password, 'Goal': 'Lose weight'})
        elif goal == '2':
            self.users.append({'Username': username, 'Password': password, 'Goal': 'Gain weight'})
        elif goal == '3':
            self.users.append({'Username': username, 'Password': password, 'Goal': 'Maintain weight'})
        else:
            print("Unknown input")
            return

        self.SaveUsers()
        initializeUser(username, password, goal)
        print("Congrats on signing up!")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        userFound = False
        for user in self.users:
            if username == user['Username'] and password == user['Password']:
                initializeUser(username, password, user['Goal'])
                userFound = True
                print(f'Logged in! Welcome {username}')
                break
        if not userFound:
            print("Invalid username or password")
            self.login()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # user system is us
    us = UserSystem()

    while True:
        print("1. Sign Up \n2. Login \n3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            us.sign_up()
        elif choice == '2':
            us.login()
            break
        elif choice == '3':
            break
        else:
            print("Invalid input. Please choose again.")

    print(f'Your goal is to {current_user.goal}')

    while True:
        print("\n1. Add Calories \n2. Add Exercises \n3. Summary")

        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            current_user.addCaloriesConsumed()
        elif choice == '2':
            current_user.addExercise()
        elif choice == '3':
            print(current_user.getSummary())
            break
        else:
            print("Invalid input. Please choose again.")




