from Classes.Main import Powerball  # Import the main class for using there methods

user1 = Powerball()  # Create an instance in the game class(Powerball)
user2 = Powerball()
user3 = Powerball()
user1.powerball()
user1.__setrange__(38, 1)  # set the rang of whiteball drawing from 20 to 37
user1.__setrange__(8, 2)  # set the rang of powerball drawing from 10 to 7
user1.powerball()
user2.powerball()
user3.__setrange__(50, 3)  # Using The Method of setrange for set an new range of drawing in this scanario the output
# will be stderr
user3.powerball()  # The range of the drawing numbers will stay 20 for the whiteballs and 10 for the powerball
