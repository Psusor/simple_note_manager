# Simple note manager (terminal application)

## Goal:
Create a program in Python that allows the user to work with simple notes in the
terminal.
The program will allow the user to:
- add new notes,
- display existing notes,
- delete notes by ID,
- work with the notes.txt file, where notes are stored and loaded.
Format of a saved note:
Date: 2025-04-28
Note: Buy groceries
Important: True
----------------------------------
This data is stored in the notes.txt file, with each note separated by a line break.
Application functionality:
After launching, the menu is displayed :

Simple Notes Manager:
- 1 List Notes
- 2 Add a Note
- 3 Delete a Note
- 4 Exit
Choose an option (1?4):
## 1. Add a note
After selecting option 2, you will be asked:
Note date:
Note:
Is the note important:
The note is saved to the notes.txt file.
Project: Simple note manager (terminal application)
## 2. Display notes
After selecting 1, the notes are listed as follows :
- Id: 1
- Date: 2025-04-28
- Note: Buy groceries
- Important: True
----------------------------------
## 3. Delete note
After selecting option 3, you will be asked:
Enter the ID of the note to delete:
If the ID exists, the note is deleted. If not, the following is displayed:
Please enter a valid numeric ID.
## 4. Exiting the program
After selecting 4, the program ends with the following message:
Goodbye!
Working with the file
- The notes.txt file is automatically loaded at startup.
- If it does not exist, the following is displayed: No notes found.
- The file format must be preserved.
