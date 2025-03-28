
from utils.common import *
# class Driver:
#     Instance =None

    # @staticmethod
    # def Initialize():
    #     Instance = webdriver.Firefox()
    #     return I.nstance
def write_to_file(txt):
    file=load_config('logsfilepath')
    with open(file, "w") as file:
        file.write(txt)
        file.close()