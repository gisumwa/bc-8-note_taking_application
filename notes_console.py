"""
NoteBook
Usage:
    note createnote <note_content>
    note create_note <note_content>
    note searchnotes <query_string>
    note next
    note viewnote <note_id>
    note listnotes [--limit]
    note deletenote <note_id>
    note quit
    note (-i | --interactive)
    note (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""
import sys
import cmd
from docopt import docopt, DocoptExit
from database import MyDatabase
from functionalitites import NoteFunctionalities
from pyfiglet import figlet_format
from termcolor import cprint, colored


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyNotes(cmd.Cmd):
    def __init__(self):
        self.my_note = NoteFunctionalities()
        cmd.Cmd.__init__(self)
        self.what_function = ['temp']
        self.search_limit = 5
        self.list_limit = 0
        self.search_offset = 0
        self.list_offset = 0
        self.search_string = ''

    def intro(self):
        print('\t ')
        cprint(figlet_format("MAKE A NOTE"), 'green')
        print('-------------------------------------------------------------------------')
        print('\t\t Hello, Welcome to NoteBook')
        print('\t A Simple interactive console app for making and modifying notes')
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ')
        print('\t\t For any help please print help then enter')
        print('-------------------------------------------------------------------------')

    intro = intro('Welcome')
    prompt = 'NoteBook>> '
    file = None
    def do_deletenote(self, note_id):
        """
        Usage: deletenote <note_id>
        """
        self.what_function.append("deletenote")
        return self.my_note.deletenote(note_id)

    def do_create_note(self, note_content):
        """
            Usage: create_note <note_content>
            """
        self.what_function.append("createnote")
        return self.my_note.createnote(note_content)

    def do_listnotes(self, limit):
        """
        Usage: listnotes [--limit]
        """
        self.what_function.append('list')
        if limit == '':
            return self.my_note.listnotes(limit, offset='')
        elif not isinstance(int(limit), int):
            print("The limit must be an integer value")
        else:
            if self.what_function[-1] == 'next':
                self.list_limit = int(limit)
                self.list_offset += self.list_limit
                return self.my_note.listnotes(self.list_limit, self.list_offset)
            else:
                self.list_limit = int(limit)
                self.list_offset += self.list_limit
                return self.my_note.listnotes(int(limit), 0)

    def do_searchnotes(self, search_arg):
        """
        Usage: searchnotes <query_string> [--limit]
        """
        self.search_string = search_arg
        parameters = search_arg.split(' ')
        if len(parameters) > 2:
            print("Enter only two parameters")
        else:
            self.search_string = parameters[0]
            self.what_function.append('search')
            if len(parameters) < 2:
                search_arg = parameters[0]
                return self.my_note.searchnotes(search_arg, limit='', offset='')
            else:
                self.search_string = parameters[0]
                limit = parameters[1]
                print(limit)
                if isinstance(int(limit), str):
                    print("Your limit must be an integer")
                elif isinstance(int(limit), int) and self.what_function[-1] == 'next':
                    self.search_limit = limit
                    self.search_offset += limit
                    return self.my_note.searchnotes(self.search_string, self.search_limit, self.search_offset)
                else:
                    self.search_limit = int(limit)
                    self.search_offset += self.search_limit
                    return self.my_note.searchnotes(self.search_string, self.search_limit, 0)

    def do_viewnote(self, note_id):
        """
        Usage: viewnote <note_id>
        """
        self.what_function.append("viewnote")
        return self.my_note.viewnote(note_id)

    def do_next(self, search_string):
        """
        Usage: next
        """
        self.what_function.append('next')
        if len(self.what_function) > 2:
            if self.what_function[-2] == 'search':
                print(self.what_function[-2])
                # Next will return the next specified number of files for the
                # searchnotes method
                # 
                return self.my_note.searchnotes(self.search_string, self.search_limit, self.search_offset)
            elif self.what_function[-2] == 'list':
                print(self.what_function[-2])
                # Next will return the next specified number of files for the
                #     searchnotes method
                #    
                return self.my_note.listnotes(self.list_limit, self.list_offset)
            elif self.what_function[-1] == 'next':
                function_list = [x for x in reversed(self.what_function)]
                for function in function_list:
                    if function == 'search':
                        self.search_offset += self.search_limit
                        return self.my_note.searchnotes(self.search_string, int(self.search_limit), self.search_offset)
                    elif function == 'list':
                        self.list_offset += self.list_limit
                        return self.my_note.listnotes(int(self.list_limit), self.list_offset)

            else:
                print(self.what_function[-2])
                print("Next only preceeds listnotes or searchnotes commands")

        else:
            print("Next cannot be the first command")
            # return self.note_obj.next(arg)

    def do_quit(self):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    obj = MyNotes()
    obj.cmdloop()

print(opt)
