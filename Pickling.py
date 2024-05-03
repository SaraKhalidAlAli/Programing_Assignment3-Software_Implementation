#pickling
import pickle
from Classes import Employee, Client, Event, Guest, Venue, Supplier, Caterer

def save_object(obj, filename):
    """Save an object to a file using pickle.
    Args:
        obj (object): The Python object to pickle.
        filename (str): The file path where the object will be saved."""
    with open(filename, 'wb') as outp:  # Open the file for writing in binary mode
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)  # Pickle the object and write to the file

def load_object(filename):
    """ Load an object from a pickle file.
    Args:
        filename (str): The file path from where the object will be loaded.
    Returns: object: The unpickled Python object."""
    with open(filename, 'rb') as inp:  # Open the file for reading in binary mode
        return pickle.load(inp)  # Return the unpickled object
