from datetime import datetime
from database import MyDatabase


class NoteFunctionalities(object):
    def __init__(self):
        self.NoteObject = MyDatabase()

    def createnote(self, note):
        """
        Adding a note to the database
        """
        # print(note)
        # note = (" ".join(note['<note>']))
        title = input("Title: ").upper()
        self.NoteObject.createnote(title, note)
        print("Note Successfully Created")

    def viewnote(self, note_id):
        noteobject = MyDatabase()
        noteobject.viewnote(note_id)

    def deletenote(self, note_id):
        if isinstance(note_id,dict):
        note_id = note_id['<note_id>']
        note_id=int(note_id)
        else:
            note_id=int(note_id)
        noteobject = MyDatabase()
        noteobject.deletenote(note_id)

    def listnotes(self, limit, offset):
        noteobject = MyDatabase()
        noteobject.listnotes(limit, offset)
        print("Open records.json to view the notes in a file")

    def searchnotes(self, search_string, limit, offset):
        noteobject = MyDatabase()
        if limit == '':
            noteobject.searchnotes(search_string, limit='', offset='')
        else:
            limit = int(limit)
            offset = int(offset)
            noteobject.searchnotes(search_string, limit, offset)

    def syncnotes(self):
        noteobject = MyDatabase()
        noteobject.syncnotes()

