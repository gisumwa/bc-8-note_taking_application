import sqlite3
from datetime import datetime


class MyDatabase(object):
    def __init__(self):
        """Connecting to the Database"""
        self.connection = sqlite3.connect('notes.db')
        if self.connection:
            '''Creating a cursor object for sql statement execution'''
            self.cursor = self.connection.cursor()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS NotesEntries(id INTEGER PRIMARY KEY AUTOINCREMENT,"
                                " time_created TIMESTAMP, note_title TEXT, note_content TEXT)")
        else:
            print("Could not connect to the database")

    def create_note(self, note_title, note_content):
        """Inserting a note into the database
        :rtype: object
        :param note_content:
        :param note_title:
        """
        with self.connection:
            self.cursor.execute(
                "INSERT INTO NotesEntries(time_created,note_title,note_content) VALUES ('{}','{}','{}')".format(
                    datetime.now(), note_title, note_content))

    def search_notes(self, search_string):
        """Searching for a given record or records
        :param search_string:
        """
        with self.connection:
            search_list = self.cursor.execute(
                "SELECT * FROM NotesEntries WHERE note_content LIKE %{}% ORDER BY id ASC".format(search_string))
        formatted_output = ''
        for note in search_list:
            formatted_output = self.note_display_format(formatted_output, note)
        return formatted_output

    def note_display_format(self, formatted_output, note):
        formatted_output += "\n {}. Created at: {}\n\t\t Title:  {} \n\t\tContent: {} \n".format(note[0], note[1],
                                                                                                 note[2], note[3])
        return formatted_output

    def view_note(self, note_id):
        try:
            note = self.cursor.execute("SELECT * FROM NotesEntries WHERE id = {} LIMIT 1".format(note_id))
            formatted_output = ''
            for note in note:
                formatted_output = self.note_display_format(formatted_output, note)
            return formatted_output
        except IndexError:
            return "The note you are trying to access is not available"

    def list_notes(self):
        with self.connection:
            notes_list = self.cursor.execute("SELECT * FROM NotesEntries LIMIT 15")
        formatted_output = ''
        for note in notes_list:
            formatted_output = self.note_display_format(formatted_output, note)
        return formatted_output

    def delete_note(self, note_id):
        try:
            self.cursor.execute("DELETE FROM NotesEntries WHERE id = {}".format(note_id))
        except IndexError:
            return "The note you are trying to access is not available"

    def next(self, current_function):
        obj = MyDatabase()
        current_function = obj.search_notes or obj.list_notes
        if current_function is obj.search_notes:
            with self.connection:
                notes_list = self.cursor.execute("SELECT * FROM NotesEntries LIMIT 15 OFFSET 15")
            formatted_output = ''
            for note in notes_list:
                formatted_output = self.note_display_format(formatted_output, note)
            return formatted_output
        else:
            with self.connection:
                search_list = self.cursor.execute(
                    "SELECT * FROM NotesEntries WHERE note_content LIKE %{}% LIMIT 15 OFFSET 15 ORDER BY id ASC".format(
                        self.search_notes))
            formatted_output = ''
            for note in search_list:
                formatted_output = self.note_display_format(formatted_output, note)
            return formatted_output


# Testing whether the commit database is create_note and list_notes functions are working
db = MyDatabase()
# print(db.list_notes())
# print(db.view_note(5))
# db.enter_note("This title","Sample content")
# db.enter_note("This title","Sample content")
# print('initial list\n ',db.list_notes())
# print("Results for searched note\n",db.view_note(1))
# db.delete_note(1)
# db.delete_note(2)
# print(db.list_notes())
# print(next(db.list_notes))
