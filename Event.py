#importing

import pickle
from tkinter import Tk, Button


#adding the classes

class Employee:
class Client:
class Event:
class Guest:
class Venue:
class Supplier:
class Caterer:

#pickling
def save_data(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


def load_data(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)


#GUI buttons

# Create buttons for user interaction


# Pack buttons into the GUI window



#displaying the output
#Run the GUI main loop