import os


listing = os.walk('C:\\Users\\moham\\OneDrive\\Study_WorkInProgress-26Oct2022'
                  '\\CorePython\\LearnPythonProgrammingMasterclass_Udemy\\'
                  'O8_ModulesAndFunctions')
# listing = os.walk('.')  # Uses current directory

for root, directories, files in listing:
    print(root)
    for d in directories:
        print(d)

    for file in files:
        print(file)
