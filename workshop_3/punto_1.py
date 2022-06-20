#!/usr/bin/python3

"""
Ace would like to volunteer to travel to K-Pax, for which the Canadian Space Agency requires him to fill out a form to help obtain more information about him and his family. You must help Ace by creating a program to complete the requested information without overwriting the file.  Keep in mind that the data with * are the most important, if one of those fields is not filled, you will not be admitted, in case the requested data is not important, the program should put "unknown".
File: required_data.txt

"""
import os


def get_file_path() -> str:
    """ Get absolute path to the file """
    path = os.path.abspath(os.getcwd())
    path_file = path + '/required_data.txt'
    return path_file


def open_and_update_file(path_file: str):
    """ Read file and complete form """
    try:
        # Read and create new file simultaniuslty
        with open(path_file, 'r', encoding='utf-8') as fi, open('new_file.txt', 'w', encoding='utf-8') as fo:
            print("\n --- Welcome to K-Pax travel, please fill the next form: --- \n")
            items = set()
            for line in fi:
                line = line.strip()
                # Create set with all fields to compare in each iteration
                if line.find(':') > 0 and line.find('•') < 0:
                    items.add(line)

                # Print the titles to fill form
                if line.startswith('|') or line.startswith('•'):
                    print(f"\n{line}\n")

                # Get new info and create file
                if line in items:
                    # Check if field is mandatory
                    if line.find('*') > 0:
                        flag = True
                        while flag:
                            new_info = str(input(f"{line} "))
                            if new_info == "":
                                print("**Field mandatory**")
                            else:
                                flag = False
                        fo.write('    ' + line + ' ' + new_info)
                        fo.write('\n')
                    else:
                        new_info = str(input(f"{line} "))
                        if new_info == "":
                            new_info = "unknown"
                        fo.write('    ' + line + ' ' + new_info)
                        fo.write('\n')
                else:
                    fo.write(line)
                    fo.write('\n')
    except Exception:
        print("The file could not be opened")


if __name__ == "__main__":
    path_file = get_file_path()
    open_and_update_file(path_file)
