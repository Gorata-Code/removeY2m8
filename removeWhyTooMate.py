import os


def script_summary() -> None:
    print('''
        \t\tDUMELANG means GREETINGS! ~ G-CODE\n
        \t"REMOVE-Y2MATE" Version 1.1.0\n
        This Program will help you remove variations of "y2mate" and aspect ratios (e.g.'1080p')\n
        from all your file names in a heartbeat. No need for installation. Just put this "y2m8.exe"\n
        file in the same folder as all the files you want to rename and then double-click it to run it.
    ''')


VARIATIONS: list[str] = ['y2mate.com', 'y2mate.is', 'y2mate']


def get_the_target_files() -> [str]:

    current_working_directory = os.listdir()

    target_files = []

    for file in current_working_directory:
        _, file_extn = os.path.splitext(file)
        if file_extn != '.exe' and file_extn != '.py':
            for word in VARIATIONS:
                if word.casefold() in file.casefold():
                    target_files.append(file)
                    break
    return target_files


def remove_y2_mate() -> None:

    the_target_files = get_the_target_files()

    for file in the_target_files:
        try:
            file_name, file_ext = os.path.splitext(file)
            new_name = ''

            if file_name.casefold().split('-')[0].strip() == (VARIATIONS[0].casefold()):
                new_name = (file_name.split('-')[1].split('_')[0].strip())
            elif file_name.casefold().split('-')[0].strip() == (VARIATIONS[1].casefold()):
                if len(file_name.split('-')) == 5:
                    new_name = (file_name.split('-')[1].strip())
                elif len(file_name.split('-')) > 5:
                    new_name = (file_name.split('-')[1].strip() + ' -' + file_name.split('-')[-4])

            final_name = new_name + file_ext
            os.rename(file, final_name)

            print(f'SUCCESS:\n\tBEFORE: "{file}"\n\tAFTER:  "{final_name}"\n')

        except WindowsError:
            print(f'**FAIL**:\n\t"{file}"')
            print(f"\tIf renamed, the file name above will match another file name in this folder.\n")


def finalise() -> None:

    the_targeted_files = get_the_target_files()
    the_eligible_files = len(the_targeted_files)

    if the_eligible_files > 0:

        print('\t\t------------------------------------------------------------------')
        print('        \t\t\tYOU WILL RENAME A TOTAL OF: ' + str(the_eligible_files) + ' FILE(S)')
        print('\t\t------------------------------------------------------------------\n')

        go_or_no_go = input('Type Yes to continue or No to cancel: ').title()

        if go_or_no_go == 'Yes':

            print('\n\t\t\t\t--------> FINAL NAMES <--------\n')

            remove_y2_mate()
            files_renamed = (the_eligible_files - len(get_the_target_files()))

            if files_renamed > 0:
                print(f'\n \t\t--------> SUCCESSFUL! You have removed "y2mate" from {files_renamed} File Name(s) '
                      f'<--------')
                if len(get_the_target_files()) > 0:
                    print(f'\n\tNOTE: {len(get_the_target_files())} File(s) with "y2mate" in their name(s) was/were '
                          f'not renamed\n\t\tbecause the name(s) already exist(s) in this folder.')
                input('\nPress Enter to Exit.\n')

            elif files_renamed == 0:
                print(f'\tFAILED! You have not removed "y2mate" from any file names.')
                input('\nPress Enter to Exit.\n')

        else:
            print('\nCANCELLED!')
            print('\tNo changes were made to your file names.\n')
            input('\nPress Enter to Exit.\n')

    elif the_eligible_files == 0:

        print('''\tNOTHING TO RENAME HERE\n\n\tThere are no files with "y2mate" in their names in this folder. Please 
        make sure you are running this script from the folder containing the\n\tfiles you want to rename.\n''')

        input('\nPress Enter to Exit.\n')


def main() -> None:
    script_summary()
    finalise()


if __name__ == '__main__':
    main()
