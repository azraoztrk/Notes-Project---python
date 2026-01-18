#import json
import sqlite3
import re
from datetime import datetime
 
#try:
#    with open("notesList.json", "r") as file:
#        notesList = json.load(file)
#except:
#    notesList = []

conn = sqlite3.connect("notes.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS notes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    note TEXT NOT NULL,
    date TEXT NOT NULL     
)
""")

print("--🎀 Welcome to Notes App 🎯--")
print("1-Add Note ➕ ")
print("2-List The Notes 🗒️")
print("3-Delete Note 🗑️")
print("4-Search Notes 🔍")
print("5-Exit 👋")

while True:
    try:
        userInput = int(input("Please choose one of the options(1-5): "))
    except ValueError:
        print("Invalid option. Please enter a valid option!")
        continue

    if userInput == 1:
        textInput = input("\nEnter note: \n")
        now = datetime.now()
        today = now.strftime("%Y-%m-%d")
        #notesList.append(f"{today}: {textInput}")

        cursor.execute("INSERT INTO notes (note, date) VALUES (?, ?)", (textInput, today))
        conn.commit()

        print("Note added successfully ✅")
        
    elif userInput == 2:
        #if not notesList:
        #    print("\nThere is no note yet, please add one.\n")
        #else:
        #    for index,value in enumerate(notesList):
        #        print(f"\n{index + 1}: {value}\n")

        cursor.execute("SELECT id, note, date FROM notes")
        notes = cursor.fetchall()

        if not notes:
            print("\nThere is no note yet, please add one.\n")
        else:
            for note in notes:
                print(f"\n{note[0]}: {note[2]} - {note[1]}\n")

    elif userInput == 3:
        popInput = int(input("\nPlease choose a note to delete: \n"))
        #notesList.pop(popInput - 1)

        cursor.execute("DELETE FROM notes WHERE id = ?", (popInput,))
        conn.commit()

        print("\nNote deleted succesfully! 🗑️ ✅\n")

    elif userInput == 4:
        searchInput = input("Enter keyword to search: ")
    
        #found = False
        #for index, note in enumerate(notesList):
        #    if re.search(searchInput, note, re.IGNORECASE):
        #        print(f"{index + 1}: {note}")
        #        found = True
        #if not found:
        #    print("No notes found with keyword " + searchInput)

        cursor.execute("SELECT id, note, date FROM notes WHERE note LIKE ?", (f"%{searchInput}%",))
        results = cursor.fetchall()

        if not results:
            print("No notes found with keyword " + searchInput)
        else:
            for note in results:
                print(f"{note[0]}: {note[2]} - {note[1]}")

    elif userInput == 5:
        #with open("notesList.json", "w") as file:
        #    json.dump(notesList, file)

        conn.close()
        print("\nThanks for using Notes App. Goodbye👋")
        break

    else:
        print("\nInvalid Option!\n")