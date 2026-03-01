import json
import os

def insert_song(song, artist, genre, position, filename="music.json"):
    new_entry = {
        "song": song,
        "artist": artist,
        "genre": genre
    }

    # Load existing data
    if not os.path.exists(filename):
        raise FileNotFoundError("JSON file does not exist.")

    with open(filename, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("JSON file is empty or invalid.")

    if not isinstance(data, list):
        raise ValueError("JSON file must contain a list.")

    if position == 'end':
        index = len(data)
    else:
        try:
            position = int(position)
        except ValueError:
            raise ValueError("Position must be a number or 'end'.")

    if position < 0 or position > len(data):
        raise IndexError("Position out of range.")

    # Convert to zero-based index
    index = position - 1

    # Insert (this shifts items to the right)
    data.insert(index, new_entry)

    # Save back to file
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Inserted at position {position}.")

if __name__ == "__main__":
    while True:
        song = input("Enter song name: ")
        artist = input("Enter artist name: ")
        genre = input("Enter genre: ")
        position = input("Enter position (1-based index or 'end'): ")

        insert_song(song, artist, genre, position)
