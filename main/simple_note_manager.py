
import os
FILE_NAME = "ulohy_skillmea/notes.txt"


def clear_screen():
    os.system("cls")
#delete terminal 


def load_notes(FILE_NAME):
    with open(FILE_NAME, "r") as file:
            print(file.read())
#loading the created notes


def add_note():
    max_id = 0
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            block = []
            for line in file:
                block.append(line)
                if line.strip() == "==========":
                    for blk_line in block:
                        if blk_line.strip().startswith("Id:"):
                            try:
                                current_id = int(blk_line.strip().split(":")[1].strip())
                                if current_id > max_id:
                                    max_id = current_id
                            except ValueError:
                                continue
                    block = []
            # Processes the last block if the file did not end "=========="
            if block:
                for blk_line in block:
                    if blk_line.strip().startswith("Id:"):
                        try:
                            current_id = int(blk_line.strip().split(":")[1].strip())
                            if current_id > max_id:
                                max_id = current_id
                        except ValueError:
                            continue

    note_id = max_id + 1

    date = input("Note date: ")
    note = input("Note: ")
    importance = input("Is the note important: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"Id: {note_id}\n")
        file.write(f"Note Date: {date}\n")
        file.write(f"Note: {note}\n")
        file.write(f"Important: {importance}\n")
        file.write("==========\n")
# creating list



def delete_note_by_id(FILE_NAME):
    Id_to_Delete = input("Insert number of Id: ").strip()
    
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    new_lines = []
    block = []
    note_deleted = False

    for line in lines:
        block.append(line)
        if line.strip() == "==========":
            should_delete = False
            for l in block:
                if l.startswith("Id:"):
                    note_id = l.strip().split(":")[1].strip()
                    if note_id == Id_to_Delete:
                        should_delete = True
                        note_deleted = True
                        break
            if not should_delete:
                new_lines.extend(block)
            block = []  # clear block for next note

    with open(FILE_NAME, "w") as file:
        file.writelines(new_lines)

    if note_deleted:
        print("Note deleted. ✅")
    else:
        print("No note found with that ID. ❌")
#delete note from notes.txt



while True :
    clear_screen()
    print("Simple Notes Manager")
    print("====================")
    print("1 List Notes")
    print("2 Add a Note ")
    print("3 Delete a Note")
    print("4 Exit")
   
    choice = input("Choose an option (1-4):").strip()



    if choice == "1":
        clear_screen()
        if not os.path.exists(FILE_NAME):
            print("No saved notes.")
        
        else:
            clear_screen()
            load_notes(FILE_NAME)
        input("\nPress ENTER for return to MENU: ")
            

    elif choice == "2":
        clear_screen()
        add_note()
        print("Notes successfully saved.",u"\u2705")
        input("\nPress ENTER for return to MENU: ")
    
    elif choice == "3":
        clear_screen()
        delete_note_by_id(FILE_NAME)
        input("\nPress ENTER for return to MENU: ")
    
    elif choice == "4":
        clear_screen()
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1-4.")
        input("\nPress ENTER to return to MENU: ")
    
