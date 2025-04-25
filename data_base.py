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
            name TEXT,
            password TEXT
            
                )
        """)

    # It is the sql code that help to create a table if not exist, and id and name are coloum 
    
    # Creat task table 
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS task
            ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            detail TEXT,
            due_date TEXT,
            priroty TEXT,
            catagory TEXT,
            complete TEXT,           
            FOREIGN KEY(user_id) REFERENCES user(id) 
            )                       
        """
        )
    #This links each task to a user from the user table (like a relationship). It ensures user_id must exist in user(id) — prevents orphan tasks with no user.
    
    conn.commit() # to save the change 
    conn.close() # to colse the database connection


    # this function is use to interst data into user table id there is already data then it ingore the entry
def add_user( user_id,Password):
        conn=sqlite3.connect(DB_name)
        cursor=conn.cursor()

        cursor.execute("""
            INSERT OR IGNORE INTO user(id,password) VALUES(?, ?)
             """,(user_id,Password))
        conn.commit()
        conn.close()

# this a method that is use to add task from the user     
def add_task(user_id, task):
        conn=sqlite3.connect(DB_name)
        cursor=conn.cursor()
        cursor.execute(""" INSERT INTO task(user_id, detail, due_date, priroty, catagory, complete) VALUES(?, ?, ?, ?, ?, ?)""",
                       (
                           user_id,
                           task.detail,
                           task.due_date,
                           task.priroty,
                           task.catagory,
                           task.complete
                       )  
            
        )
        conn.commit()    
        conn.close()

# this is the function that is used to update task 
def update_task(task_id, **dics):
            conn = sqlite3.connect(DB_name)
            cursor=conn.cursor()
            # this for loop add task in dic 
            for key, value in dics.items():
                cursor.execute(f"UPDATE task SET {key}=? where id =?",(value, task_id))
            conn.commit()
            conn.close()
#this is the method that is used to delete the task ( row ) by taking id as input
def delete_task(task_id):
            conn = sqlite3.connect(DB_name)

            cursor= conn.cursor()
            cursor.execute(" DELETE FROM task WHERE id=?", (task_id,))# changing task_id into tuple by giving , at last
            conn.commit()
            conn.close()       
            
# this is the method that is used to show all the data of the file in the screen     
def get_task(user_id):
        from Data import security_task
        conn= sqlite3.connect(DB_name)
        cursor=conn.cursor()
        tasks=[]
        

        cursor.execute( """
            SELECT  id,detail,due_date,priroty,catagory,complete
            FROM task
            WHERE user_id= ?""",(user_id,))
        rows = cursor.fetchall()
        #this is used to fetch all data of rows at once
        conn.close()
        # for loop for check the data of row
        for row in rows:
            task= security_task(
                detail=row[1],
                due_date=row[2],
                priroty=row[3],
                catagory=row[4],
                complete=row[5]
            )
            task.id=row[0]
            tasks.append(task)
        return tasks

        
# this is a function that is used to search the whole row by using the keyword that user enters
def search_task(user_id, keyword):
    from Data import security_task
    conn= sqlite3.connect(DB_name)
    cursor =conn.cursor()
    cursor.execute(
        """ SElECT * FROM task WHERE user_id=? AND (detail LIKE ? OR catagory LIKE ?)""", (user_id,f"%{keyword}%",f"%{keyword}%")
        
    )
    rows=cursor.fetchall()
    conn.close()
    to_show=[]
    for row in rows:
        to_do= security_task(
            detail=row[2],
            due_date=row[3],
            priroty=row[4],
            catagory=row[5],
            complete=row[6]
        )
        to_do.id=row[0]
        to_show.append(to_do)
    return(to_show)


        

