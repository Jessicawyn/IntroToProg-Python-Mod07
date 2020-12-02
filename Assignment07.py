# ------------------------------------------------- #
# Title: Assignment07
# Description: Collect blood pressure readings from user and save in binary file
# ChangeLog: (Who, When, What)
# jcarnes,20201130,Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
file_name = 'blood_pressure.dat'  # Binary file storing blood pressure history
blood_pressure_dic = {}  # Dictionary to store user's systolic and diastolic blood pressure
blood_pressure_history_lst = []  # List of dictionaries containing blood pressure

# Processing -------------------------------------- #


def load_blood_pressure_history(file):
    """This function loads the list from a binary file if the file exists.
    If the file doesn't exist then one is created and the list becomes an empty list.
    :param file: (obj) binary file containing list of dictionary rows
    :return: (list) containing the contents of the file or an empty list if the file doesn't exist"""

    try:
        f = open(file, 'rb')
        list_of_rows = pickle.load(f)
        f.close
    except:
        f = open(file, 'wb')
        list_of_rows = []
        f.close()
    return list_of_rows


def add_bp_to_list(blood_pressure_dictionary, list_of_rows):
    """This function adds a dictionary containing systolic and diastolic bp values to a list
    :param blood_pressure_dictionary: (dictionary) containing systolic and diastolic blood pressure
    :param list_of_rows: (list) of dictionary rows
    :return (list) of dictionary rows
    """
    if blood_pressure_dic != {}:
        list_of_rows.append(blood_pressure_dictionary)
    return list_of_rows

def save_blood_pressure_history(file, list_of_rows):
    """This function writes a list (containing dictionaries) to a binary file

    :param file: (obj) binary file to save list into
    :param list_of_rows: (list) of dictionary rows to write into binary file
    :return: none
    """
    f = open(file, 'wb')
    pickle.dump(list_of_rows, f)
    f.close()


# Presentation ------------------------------------ #
def get_user_blood_pressure():
    """Asks user to input systolic and diastolic blood pressure values then stores them to a dictionary

    :return: (dictionary) containing systolic and diastolic blood pressure values
    """
    systolic = None
    diastolic = None
    blood_pressure = {}
    print("Please enter your blood pressure...")
    try:
        systolic = input("Systolic: ").strip()
        if not(systolic.isnumeric()):
            raise Exception('\n Error: Blood pressure must be an integer! \n Values not saved! ')
        diastolic = input("Diastolic: ").strip()
        if not(diastolic.isnumeric()):
            raise Exception('\n Error: Blood pressure must be an integer! \n Values not saved!')
        blood_pressure = {'Systolic': systolic, "Diastolic": diastolic}
    except Exception as e:
        print(e, '\n')
    return blood_pressure


def display_current_list(list_of_rows):
    """Prints the current list of blood pressure readings to the screen

    :param list_of_rows: (list) of dictionary rows containing systolic and diastolic values
    :return: None
     """
    print('\nCurrent List of Blood Pressure Readings: ')
    for row_dic in list_of_rows:
        print(row_dic['Systolic'], '/', row_dic['Diastolic'])
    print()

# Main() ------------------------------------ #


# Load existing blood pressure data to list from existing binary file, if file doesn't exist create file
blood_pressure_history_lst = load_blood_pressure_history(file_name)

# Display existing blood pressure data
display_current_list(blood_pressure_history_lst)

# Get user's current blood pressure
blood_pressure_dic = get_user_blood_pressure()

# Add user's current blood pressure to the list of blood pressures
add_bp_to_list(blood_pressure_dic, blood_pressure_history_lst)

# Save the updated list of blood pressures to the binary file
save_blood_pressure_history(file_name, blood_pressure_history_lst)

# Display existing blood pressure data
display_current_list(blood_pressure_history_lst)
