class Robot:
    #pass = neřeší
    #constructor
    #atributy
    def __init__(self, batery, arm_lenght):
        self.bat = batery
        self.arm_len = arm_lenght
        self.tasks_to_check = 1000 #defaultní nastavení
        
    def step_ahead(self):
        print("Robot udělal krok vpřed")
        self.tasks_to_check -= 1
        print(f"Úkonů do kontroly: {self.tasks_to_check}")
        
    def step_backwards(self):
        print("Robot udělal krok vzad.")
        self.tasks_to_check -= 1
        print(f"Úkonů do kontroly: {self.tasks_to_check}")
        
#Tvoření objektů podle classy    
robot_1 = Robot(24, 0.6)
robot_2 = Robot(48, 0.5)
robot_3 = Robot(36, 0.4)
robot_4 = Robot(42, 0.7)
#Self se vztahuje k robotům, tzn. konkrétním objektům.


print(robot_1.bat)
print(robot_1.arm_len)
print(robot_1.tasks_to_check)

robot_1.step_ahead()
robot_1.step_backwards()
robot_1.step_ahead()
robot_1.step_backwards()
robot_1.step_ahead()
robot_1.step_backwards()


# print(robot_2.bat)
# print(robot_2.arm_len)
# print(robot_2.revision_days)

# print(robot_3.bat)
# print(robot_3.arm_len)
# print(robot_3.revision_days)

# print(robot_4.bat)
# print(robot_4.arm_len)
# print(robot_4.revision_days)