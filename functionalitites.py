from datetime import datetime
from database import MyDatabase


class NoteFunctionalities(object):
    def __init__(self):
        self.NoteObject = MyDatabase()

    def create_note(self, note):
        """
        Adding a note to the database
        """
        note = ("\t".join(note['<note>']))
        title = input("Title: ")
        self.NoteObject.create_note(title, note)
        print("Note Successfully Created")

    def view_note(self, note_id):
        NoteObject = MyDatabase()
        NoteObject.view_note(note_id)

    def delete_note(self, note_id):
        NoteObject = MyDatabase()
        NoteObject.delete_note(note_id)

    def list_notes(self):
        NoteObject = MyDatabase()
        NoteObject.list_notes()

    def search_notes(self, search_string):
        NoteObject = MyDatabase()
        NoteObject.search_notes(search_string)

    def next(self, current_query):
        return "To be implemented"


"""
NA = NoteFunctionalities()
#NA.create_note("Sample","Sample for person 1")
print(NA.list_notes())

NA2 = NoteFunctionalities()
NA2.create_note("Sample2","Sample Note 1 for person 2")
NA.create_note("Sample3","Sample Note 2 for person 1")
"""
# print("Notes before delete", NA.list_notes())
# print(NA.view_note(2))
# NA.delete_note(1)
# print("Notes after delete", NA.list_notes())
# print(NA.notes_list.count("Sample Note 3"))
# print(NA.view_note(""))
#print(NA.view_note(5))
