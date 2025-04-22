# I am using the SQlite(file base) database rather than MYSQL(serverbase) because SQlite donot need any instalation

import sqlite3
DB_name="JOHN_Project.db"

def init_db():
    conn=sqlite3.connect(DB_name) # It connect the programm ti the file name DB_name, if file is not exist then it creat that file
    cursor =conn.cursor() # its creates the cursor object which allow us to exsucute the queries
    # creat the user table
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS user (
            id TEXT PRIMARY KEY,
            name TEXT
                )
        """)
    conn.commit() # to save the change 
    conn.close() # to colse the database connection
    # It is the sql code that help to create a table if not exist, and id and name are coloum 
    
    # Creat task table 
    cursor.execute("""
        CREATE TABLE IF NOT EXIXTS task( 
            id INTEGER PRIMARY KEY AUTOINCREMENT 
            user_id TEXT
            details TEXT
            due_date TEXT
            priroty TEXT
            catagory TEXT
            complete TEXT
            FOREIGN KEY(user_id) REFRENCES user(id)
            )              
        """
        #This links each task to a user from the user table (like a relationship). It ensures user_id must exist in user(id) — prevents orphan tasks with no user.
        )
    # this function is use to interst data into user table id there is already data then it ingore the entry
    def add_user( user_id,Password):
        conn=sqlite3.connect(DB_name)
        cursor=conn.cursor()

        cursor.execute("""
            INSERT OR INGORE INTO user(id,name) VALUE(?, ?)
             """,(user_id,Password))
        conn.commit()
        conn.close()

        
    def add_task(user_id, task):
        conn=sqlite3.connect(DB_name)
        cursor=conn.cursor()
        cursor.execute(""" INSERT INTO task(user_id, detail, due_date, priroty, catagory, complete) VALUE (?, ?, ?, ?, ?, ?)""",
                       (
                           user_id,
                           task.detail,
                           task.due_date,
                           task.priroty,
                           task.catagary,
                           task.complete
                       )  
            
        )
        conn.commit()    
        conn.close()


        def update_task(task_id, **dics):
            conn = sqlite3.connect(DB_name)
            cursor=conn.cursor()
            for key, value in dics.items():
                cursor.execute(f"UPADTE tasks SET {key}=? where id =?",(value, task_id))
            conn.commit()
            conn.close()

        def delete_task(task_id):
            conn = sqlite3.connect(DB_name)

            cursor= conn.cursor()
            cursor.execute(" DELETE FROM task WHERE id=?", (task_id))
            conn.commit()
            conn.close()       
            

        
    def get_data_from_user(user_id):
        from Data import Security_task
        conn= sqlite3.connect(DB_name)
        cursor=conn.cursor()
        tasks=[]
        

        cursor.execute( """
            SELECT detail, user_id,priroty,catagory,complete
            FROM task
            WHERE user_id = ?"""
            (user_id))
        rows = cursor.fetchall()
        for row in rows:
            a=0

        conn.commit()
        conn.close()


def search_task(user_id, keyword):
    conn= sqlite3.connect(DB_name)
    cursor =conn.cursor()
    cursor.execute()
        
        

#  return [SecurityTask(details, due_date, category, priority, bool(completed))
#             for (details, due_date, priority, category, completed) in rows]