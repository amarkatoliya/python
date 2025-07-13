import sqlite3

conn = sqlite3.connect("mydb.db")

cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')


def list_all_videos():
    print("\n")
    print("*" * 70)
    cur.execute("SELECT * FROM videos")
    for row in cur.fetchall():
        print(row)
    
        print("\n")
        print("*" * 70)


def add_video(name, time):
    cur.execute("INSERT INTO  videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()


def update_video(name, time, video_id):
    cur.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
    conn.commit()

def delete_video(video_id):
    cur.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()




def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. exit app")
        
        case = input("Enter your choice: ")
        
        if case == '1':
            list_all_videos()
            
        elif case == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
            
        elif case == '3':
            video_id = int(input("Enter the video to update: "))
            name = input("Enter video new name: ")
            time = input("Enter video new time: ")
            update_video(name, time, video_id)
            
        elif case == '4':
            video_id = int(input("Enter the video to delete: "))
            delete_video(video_id)
            
        elif case == '5':
            print("Exit ")
            break
              
        else:
            print("Invalid Choice")
            
    conn.close()
    
    


if __name__ == "__main__":
    main()