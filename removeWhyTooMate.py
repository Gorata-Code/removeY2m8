import os


def script_summary():
    print('''
        This Program will help you remove "y2mate.com" from all your file names\n
        in a flash. No need for installation. Just put this y2m8.exe file in the\n
        same folder as all the files you want to rename and then double-click it to
        run it.
    ''')


def get_the_target_files():
    try:
        current_working_directory = os.listdir()

        target_files = []

        for file in current_working_directory:
            if file.__contains__('y2mate.com - '):
                target_files.append(file)

        return target_files

    except Exception as e:
        print(str(e))


def remove_y2_mate():
    the_target_files = get_the_target_files()

    for file in the_target_files:
        try:
            file_name, file_ext = os.path.splitext(file)
            new_name = file_name.replace('y2mate.com - ', '').title()
            semi_final_name = new_name.replace('_', ' ')
            final_name = semi_final_name + file_ext
            os.rename(file, final_name)
            print('SUCCESS: \n' + final_name + '\n')

        except Exception as e:
            if 'file already exists' in str(e):
                print('FAILED: \n' + file)
                print(f"If renamed, this file name will match an existing file name.\n")


def finalise():
    the_targeted_files = get_the_target_files()
    count = len(the_targeted_files)

    if count > 0:

        print('You will rename a total of: ' + str(count) + ' File(s).\n')

        print('Type Yes to continue or No to cancel: \n')

        go_or_no_go = input(' ').title()

        if go_or_no_go == 'Yes':

            try:
                print('\nFINAL NAMES\n')

                remove_y2_mate()
                files_renamed = (count - len(get_the_target_files()))
                if files_renamed > 0:
                    print(f'\n SUCCESSFUL! You have removed "y2mate.com" from {files_renamed} file names.')
                    if len(get_the_target_files()) > 0:
                        print(f'\n\tNOTE: {len(get_the_target_files())} Files with "y2mate.com" in their names were '
                              f'not renamed because their names already exist in this folder.')
                    input('\nPress Enter to Exit.\n')

                elif files_renamed == 0:
                    print(f'\tFAILED! You have not removed "y2mate.com" from any file names.')
                    input('\nPress Enter to Exit.\n')

            except Exception as e:
                print(str(e))
                input('\nPress Enter to Exit.')

        else:
            print('\nNo changes were made to your file names.\n')
            input('\nPress Enter to Exit.\n')

    elif count == 0:

        print('''\tNOTHING TO RENAME HERE\n\n\tThere are no files with "y2mate.com" in their names in this folder. 
        Please make sure you are running this script from the folder containing\n\tthe files you want to rename.\n''')

        input('\nPress Enter to Exit.\n')


def main():
    script_summary()
    finalise()


if __name__ == '__main__':
    main()
