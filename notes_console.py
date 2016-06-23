"""
ThoughtBook

Usage:
    note create <note>
    note search <args>
    note open <id>
    note list_all
    note delete_note <id>
    note quit
    note (-i | --interactive)
    note (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""
import sys
import cmd
from docopt import docopt,DocoptExit
#from database import MyDatabase
from functionalitites import NoteFunctionalities
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
        self.note_obj = NoteFunctionalities()
        cmd.Cmd.__init__(self)

    def intro(self):
        print('\t ')
        print('\t    __ _    __        ___    __     __   ___  ___  __')
        print("\t   |  | |  /__\ |_/  |__    /__\   |  | |   |  |  |__ ")
        print("\t   |    |  |  | | |  |___   |  |   |  | |___|  |  |__ ")
        print('-------------------------------------------------------------------------')
        print('\t\t Hello, Welcome to NoteBook')
        print('\t A Simple interactive console app for making and modifying notes')
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ')
        print('\t\t For any help please print help then enter')
        print('-------------------------------------------------------------------------')

    intro = intro('Welcome')
    prompt = 'NoteBook>> '
    file = None

    @docopt_cmd
    def do_create(self, note):
        """
        Usage: create <note>...
        """
        return self.note_obj.create_note(note)

    @docopt_cmd
    def do_list_notes(self, args):
        """
        Usage: list_all
        """
        return self.note_obj.list_notes()

    def do_delete_note(self, note_id):
        """
        Usage: delete_note <id>
        """
        return self.note_obj.delete_note(note_id)

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    obj=MyNotes()
    obj.cmdloop()

print(opt)