#!/usr/bin/env python3

import os
import sys

def current_version():
    return '0.1.1'

def valid_commands():
    return ['help', 'create', 'about']

def create_files(name, user_generated=False):
    """
    
    """
    path = os.path.dirname(name)
    if path != '' and not os.path.exists(path):
        return False
    if os.path.exists(name):
        return False
    os.mkdir(name)

    if user_generated:
        print('csfolder$ Starting generation of files...')
        print('csfolder$')

        if input('csfolder$ Generate a README.md file? (y/n) ').lower() in ['y', 'yes']:
            user = input('csfolder$ Who is the owner of the files: ')
            uni = input('csfolder$ What is the institution offering the course: ')
            code = input('csfolder$ Enter the course code: ')
            course = input('csfolder$ Enter the course title: ')
            year = input('csfolder$ Enter the year: ')
            semester = input('csfolder$ Enter the semester: ')

            print('csfolder$ Generating \'README.md\'...')
            with open(f'{name}/README.md', 'w') as f:
                f.write(
f"""# {code.upper()}

#### *{course}*

This is a collection of work from {user} for the {year[-2:]}{semester} offering of {code.upper()}, {course} at {uni}.

The work done in this folder is for the purposes of the course. Some of the work may be created or written by course staff, and some work may have been created in collaboration with other students. These should be acknowledged where necessary.
"""
                )
        
        print('csfolder$')
        
        if input('csfolder$ Generate tutorial (tut) folders? (y/n) ').lower() in ['y', 'yes']:
            start = int(input('csfolder$ Enter the number to start at: '))
            end = int(input('csfolder$ Enter the number to end at: '))
            skip = input('csfolder$ Enter any numbers to skip (space sep): ')
            skip = [int(x) for x in skip.split(' ')]
            
            print('csfolder$ Generating tutorial folders...')
            os.mkdir(f'{name}/tut')
            for i in range(start, end + 1):
                if i not in skip:
                    os.mkdir(f'{name}/tut/{i:02}')
                    with open(f'{name}/tut/{i:02}/README.md', 'w') as f:
                        f.write(
f"""# Tutorial Week {i}
"""
                        )
        print('csfolder$')

        if input('csfolder$ Generate labratory (lab) folders? (y/n) ').lower() in ['y', 'yes']:
            start = int(input('csfolder$ Enter the number to start at: '))
            end = int(input('csfolder$ Enter the number to end at: '))
            skip = input('csfolder$ Enter any numbers to skip (space sep): ')
            skip = [int(x) for x in skip.split(' ')]
            
            print('csfolder$ Generating labratory folders...')
            os.mkdir(f'{name}/lab')
            for i in range(start, end + 1):
                if i not in skip:
                    os.mkdir(f'{name}/lab/{i:02}')

        print('csfolder$')

        if input('csfolder$ Generate test (tst) folders? (y/n) ').lower() in ['y', 'yes']:
            start = int(input('csfolder$ Enter the number to start at: '))
            end = int(input('csfolder$ Enter the number to end at: '))
            skip = input('csfolder$ Enter any numbers to skip (space sep): ')
            skip = [int(x) for x in skip.split(' ')]
            
            print('csfolder$ Generating test folders...')
            os.mkdir(f'{name}/tst')
            for i in range(start, end + 1):
                if i not in skip:
                    os.mkdir(f'{name}/tst/{i:02}')

        print('csfolder$')
        if input('csfolder$ Generate assignment (ass) folders? (y/n) ').lower() in ['y', 'yes']:
            values = input('csfolder$ Enter values for assigments (space sep): ')
            values = [int(x) for x in values.split(' ')]
            
            print('csfolder$ Generating assignment folders...')
            os.mkdir(f'{name}/ass')
            if values != [1]:
                for i in values:
                    os.mkdir(f'{name}/ass/{i:02}')
        
        print('csfolder$')

        if input('csfolder$ Generate project (prj) folders? (y/n) ').lower() in ['y', 'yes']:
            values = input('csfolder$ Enter values for projects (space sep): ')
            values = [int(x) for x in values.split(' ')]
            
            print('csfolder$ Generating project folders...')
            os.mkdir(f'{name}/prj')
            if values != [1]:
                for i in values:
                    os.mkdir(f'{name}/prj/{i:02}')
        
        print('csfolder$')

        if input('csfolder$ Generate exam (exam) folders? (y/n) ').lower() in ['y', 'yes']:
            print('csfolder$ Generating exam folders...')
            os.mkdir(f'{name}/exm')
            os.mkdir(f'{name}/exm/prac')
            os.mkdir(f'{name}/exm/final')
        
        print('csfolder$')
        print('csfolder$ Finished generation of files.')
        

def show_help():
    print(
"""usage: csfolder [--help] [--version] <command> [<args>]

options:
    --help, -h
        Show this help message and exit.
    --version, -v
        Show the current version and exit.

commands:
    help <command>
        Show help for <command>.
    create <name>
        Create a new folder with the given name.
        Starts the generation of necessary folders.

Use 'csfolder help' for more help.
"""
    )

def do_help(args):
    if len(args) == 0:
        show_help()
    elif args[0] in valid_commands():
        command = args[0]
        if command == 'help':
            show_help()
        elif command == 'create':
            print(
"""usage: csfolder create <name>

Create a new folder with the given name in the
current directory. <name> can also be a path
to the desired location.

Runs the generation of necessary folders based
on input from the user.
"""
            )
        elif command == 'about':
            print(
"""usage: csfolder about

Displays some general info about the program.
"""
            )

def do_create(args):
    if len(args) == 0:
        print(f'usage: csfolder create <name>')
        sys.exit(1)
    name = args[0]
    path = os.path.dirname(name)
    # Check that the path up to the last directory exists
    if path != '' and not os.path.exists(path):
        print(f'error: path to \'{name}\' does not exist')
    # Check that the last directory does not exist so create new directory
    elif not os.path.exists(name):
        print('csfolder$ Starting generation of necessary folders...')
        create_files(name, user_generated=True)
    else:
        print(f'error: \'{name}\' already exists')

def do_about(args):
    print(
"""CSFolder is a simple command line utility
for generating folders for a CSE course.

It is not designed to be used for anything
else and was just made for fun to simplify
the creation of folders for myself.
"""
    )

def main():
    # Check for generic arguments
    args = sys.argv[1:]
    if len(args) == 0 or args[0] in ['--help', '-h']:
        show_help()
        sys.exit(1)
    elif args[0] in ['--version', '-v']:
        print(f'CSFolder v{current_version()}')
        sys.exit(1)
    # `args` contains at least one argument and does not start with help or version

    # Check if the command is valid
    # Find the location of a valid command
    command_location = None
    for i, arg in enumerate(args):
        if arg in valid_commands():
            command_location = i
            break
    if command_location is None:
        if args[0].startswith('-'):
            print(f'unknown option: {args[0]}')
        else:
            print(f'unknown command: {args[0]}')
        show_help()
        sys.exit(1)
    # `args` has a valid command and `command_location` is the index of the command
    
    # Run the command
    command = args[command_location]
    args = args[command_location + 1:]
    if command == 'help':
        do_help(args)
    elif command == 'create':
        do_create(args)
    elif command == 'about':
        do_about(args)

if __name__ == "__main__":
    main()
