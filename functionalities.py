from datetime import datetime

'''
This file will contain the createnote,viewnote,deletenote,listnotes and searchnotes
'''


class NoteFunctionalities(object):
    def __init__(self):
        self.time_created = datetime.now()
        self.notes_list = []

    def create_note(self, note):
        if note not in self.notes_list:
            self.notes_list.append(note)
            # formatted_note = self.note_display_format(note)
            with open('Notes.txt', 'a') as file:
                file.write(self.note_display_format(note))
        else:
            raise Exception("The note you want to insert already exists")

    def note_display_format(self, note):
        formatted_note = "\n {}. Created at: {}\n \t{} \n".format(self.notes_list.index(note) + 1, self.time_created,
                                                                  note)
        return formatted_note

    '''
        the view_note method checks returns a single note based on the id
    '''

    def view_note(self, search_criteria):
        if isinstance(search_criteria, int) and search_criteria <= len(self.notes_list):
            return self.note_display_format(self.notes_list[search_criteria])
        else:
            if not isinstance(search_criteria, int):
                raise ValueError("Your input parameter should be an integer")
            else:
                raise IndexError("The Item you are trying to access is not in the list")

    def delete_note(self, note_id):
        if isinstance(note_id, int):
            self.notes_list.remove(self.notes_list[note_id])
        else:
            raise ValueError("Note_id can only accept an integer paramater")

    def list_notes(self):
        self.formatted_note = ''
        for note in self.notes_list:
            self.formatted_note += self.note_display_format(note)
        return self.formatted_note

    def search_notes(self, search_string):
        if isinstance(search_string, int):
            formatted_note = ''
            for note in self.notes_list:
                if search_string in note:
                    formatted_note += self.note_display_format(note)
            return formatted_note
        else:
            if len(self.notes_list) == 0:
                raise Exception("Your search string cannot be Empty")
            else:
                formatted_note = ''
                for note in self.notes_list:
                    if search_string in note:
                        formatted_note += self.note_display_format(note)
            return formatted_note


NA = NoteFunctionalities()
NA.create_note("Sample Note 1")
NA.create_note("Sample Note 2")
NA.create_note("Sample Note 3")
print("Notes before delete", NA.list_notes())
# print(NA.view_note(2))
# NA.delete_note(1)
# print("Notes after delete", NA.list_notes())
# print(NA.notes_list.count("Sample Note 3"))
# print(NA.view_note(""))
