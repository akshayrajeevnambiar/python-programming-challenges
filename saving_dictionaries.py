# creating a function to save the dictionary values into a file
import pickle

# defining a function to save the dictonary into file system
def save_dict(dict, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(dict, f)
        f.close()

# creating a funcition to retrevie the dictuinary from the file system
def load_dict(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)
    
fruits = {
    1: "banana",
    2: "apple",
    3: "orange",
    4: "watermeon"
}

save_dict(fruits, "fruits.pickle")
        
