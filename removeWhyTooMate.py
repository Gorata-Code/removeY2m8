import os
import sys
import glob


def script_summary() -> None:
    print('''
    ***----------------------------------------------------------------------------------------***
    \t***------------------------ DUMELANG means GREETINGS! ~ G-CODE -----------------------***
        \t***------------------------------------------------------------------------***\n
        \t\t"REMOVE-Y2MATE" Version 1.1.1\n
        This Program will help you remove variations of "y2mate" and aspect ratios (e.g.'1080p')\n
        from all your file names in a heartbeat. No need for installation. Just put this "y2m8.exe"\n
        file in the same folder as all the files you want to rename and then double-click it to run it.
        
        ***--------------------------------- LET THE RENAMING BEGIN -------------------------------***
    ''')


VARIATIONS: [str] = ['y2mate.com', 'y2mate.is', 'y2mate']


def get_the_target_files(locality=None) -> [str]:
    target_files: [str] = []
    pre_filtered_target_files: [str] = []
    recursion = locality

    if locality == 'All':
        recursion: bool = True

    elif locality == 'Current':
        recursion: bool = False

    elif locality != 'All' or locality != 'Current':
        print('Please type either "Current" or "All".')
        sys.exit(1)

    for filename in glob.iglob(os.getcwd() + '**/**', recursive=recursion):
        file: str = filename.split('\\')[-1]
        pre_filtered_target_files.append(file)

    for file in pre_filtered_target_files:
        _, file_extn = os.path.splitext(file)
        if not os.path.isdir(file) and file_extn != '.exe' and file_extn != '.py' and not _ == 'y2mate'.casefold():
            for word in VARIATIONS:
                if word.casefold() in file.casefold():
                    target_files.append(file)
                    break

    return target_files


def remove_y2_mate(locality, preview=False) -> None:
    the_target_files: [str] = get_the_target_files(locality)
    recursion: bool = False

    if locality == 'All':
        recursion: bool = True

    for filename in glob.iglob(os.getcwd() + '**/**', recursive=recursion):
        file: str = filename.split('\\')[-1].strip()

        if file.split('-')[0].strip().casefold() in VARIATIONS and not os.path.isdir(filename) and os.path.splitext(file
                                                                                                                    )[
                -1] != '.exe' and os.path.splitext(file)[-1] != '.py':
            try:
                file_name, file_ext = os.path.splitext(file)
                new_name: str = ''

                if file_name.casefold().split('-')[0].strip() == (VARIATIONS[0].casefold()):
                    new_name = (file_name.split('-')[1].split('_')[0].strip())

                elif file_name.casefold().split('-')[0].strip() == (VARIATIONS[1].casefold()):
                    if len(file_name.split('-')) == 5:
                        new_name = (file_name.split('-')[1].strip())
                    elif len(file_name.split('-')) > 5:
                        new_name = (file_name.split('-')[1].strip() + '-' + file_name.split('-')[-4])
                    else:
                        new_name = (file_name.split('-')[1].strip())

                elif file_name.casefold().split('-')[0].strip() == (VARIATIONS[2].casefold()):
                    new_name = (file_name.split('-')[1].split('_')[0].strip())

                final_name: str = new_name + file_ext

                if not preview:
                    file_absolute_path: [str] = filename.split('\\')[:-1]
                    os.rename(filename.strip(), f"\\".join(map(str, file_absolute_path)) + '\\' + final_name.strip())

                if preview:
                    print(
                        f'PREVIEW {str(the_target_files.index(file) + 1)}:\n\tBEFORE: "{file}"\n\tAFTER:  "{final_name}'
                        f'"\n')

            except WindowsError:
                print(f'\n** FAIL **:\n\t\t!!!"{file}"')
                print(f"\tIf renamed, the file name above will match another file name in this folder.\n")


def finalise() -> None:
    locality = input(
        '\tType "Current" to rename files in the current folder as this "y2m8.exe" only.\n\tType "All" to rename'
        ' files in the current folder and all its sub-folders: ').title().strip()

    the_targeted_files = get_the_target_files(locality)
    the_eligible_files = len(the_targeted_files)

    if the_eligible_files > 0:
        pluralise: str = ''
        if the_eligible_files > 1:
            pluralise: str = 's'
        print('\n\t\t------------------------------------------------------------------')
        print('        \t\t\tYOU WILL RENAME A TOTAL OF: ' + str(the_eligible_files) + f' FILE{pluralise.title()}')
        print('\t\t------------------------------------------------------------------\n')

        print('\t\t\tAll the Current File Names and the New File Names are listed below:\n')

        remove_y2_mate(locality, preview=True)

        rename_status: str = input('\t\t*** "All my New File Names look good" ***. \n\n\tPlease type "Yes" to '
                                   'continue or "No" to fix the New File Names \n\tthat still appear to be incorrect:'
                                   ' ').title()
        try:
            while rename_status == 'No':
                to_pre_edit: [str] = input(
                    '\n\tPlease type all the PREVIEW numbers belonging to the incorrect New File Names. \n\tUse a '
                    'comma(,) to separate them; for example: 1, 4, 7 \t\n\tPress Enter when you are done: ')

                temp_to_pre_edit_array: [str] = []

                for _ in to_pre_edit.split(','):
                    recursion: bool = False

                    if locality == 'All':
                        recursion: bool = True

                    for filename in glob.iglob(os.getcwd() + '**/**', recursive=recursion):
                        file: str = filename.split('\\')[-1].strip()

                        if file.split('-')[0].strip().casefold() in VARIATIONS and file.split('-')[-1] != file.split('-'
                                                                                                                     )[0
                                                                                                                    ]:
                            temp_to_pre_edit_array.append(file)

                            if temp_to_pre_edit_array.index(file) + 1 == int(_):
                                file_name, file_ext = os.path.splitext(file)
                                isolate_last_word: [str] = file_name.split('-')
                                new_file_name: str = file_name.replace(f'-{isolate_last_word[-1]}', '')
                                newest_file_name: str = new_file_name + file_ext
                                file_absolute_path: [str] = filename.split('\\')[:-1]
                                os.rename(filename.strip(),
                                          f"\\".join(map(str, file_absolute_path)) + '\\' + newest_file_name.strip())

                print('\t\t\t\n   ***---------------------- THE NEW FILE NAMES PREVIEW ---------------------***\n')

                remove_y2_mate(locality, preview=True)

                rename_status: str = input('\t\t*** "All my New File Names look good" ***. \n\n\tPlease type "Yes" to '
                                           'continue or "No" to fix the New File Names \n\tthat still appear to be '
                                           'incorrect: '
                                           ' ').title()
        except ValueError:
            print('\n!!!Please type a valid number!!!\n')
            finalise()

        go_or_no_go = input('\nType "Yes" to rename or "No" to cancel: ').title()

        if go_or_no_go == 'Yes':

            remove_y2_mate(locality)
            files_renamed = (the_eligible_files - len(get_the_target_files(locality)))

            if files_renamed > 0:
                print(
                    f'\n \t\t--------> SUCCESSFUL! You have removed "y2mate" from {files_renamed} File Name{pluralise} '
                    f'<--------')
                if len(get_the_target_files(locality)) > 0:
                    print(
                        f'\n\tNOTE: {len(get_the_target_files(locality))} File{pluralise} with "y2mate" in their name'
                        f'{pluralise} was/were not renamed\n\t\tbecause the name{pluralise} already exist('
                        f's) in this folder.')

                input('\nPress Enter to Exit.\n')

            elif files_renamed == 0:
                print(f'\tFAILED! You have not removed "y2mate" from any file name{pluralise}.')
                input('\nPress Enter to Exit.\n')

        else:
            print('\nCANCELLED!')
            print(f'\tNo changes were made to your file name{pluralise}.\n')
            input('\nPress Enter to Exit.\n')

    elif the_eligible_files == 0:

        print('''\tNOTHING TO RENAME HERE\n\n\tThere are no files with "y2mate" in their names in this folder. Please 
        make sure you are running this script from the folder containing the\n\tfiles / folders you want to 
        rename.\n''')

        input('\nPress Enter to Exit.\n')


def main() -> None:
    script_summary()
    finalise()


if __name__ == '__main__':
    main()
