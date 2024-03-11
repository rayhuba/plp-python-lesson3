class Python_Switch:
    def day(self, month):
        default = "Incorrect day"
        return getattr(self, 'case_' + str(month), lambda: default)()

    def case_1(self):
        return "Jan"

    def case_2(self):
        return "Feb"

    def case_3(self):
        return "Mar"
    
# Create an instance of the Python_Switch class
switch = Python_Switch()

# Call the day method on the instance
print(switch.day(1))
print(switch.day(2))
print(switch.day(3))
