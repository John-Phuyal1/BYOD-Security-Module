from Data import security_task
import data_base

# this is the function that is use to take the task info from the user 
def get_task_input():
    detail=input("Enter task detail:")
    due_date=input("Enter the due date in the form of dd/mm/yy")    
    catagory=input("Enter the catagory of task")
    priroty=input("Enter the priority like A, B, C")
    complete=input("complete or not")
    return security_task(detail,due_date,priroty,catagory,complete)# complete object is still none completed so i used the string none for thistak

def display_task(task_info):
    if not task_info:
        print("No tasks found")
    else:
        for i, info in enumerate(task_info):
            print(f"{i+1}. {info.detail} | due: {info.due_date} | priroty: {info.priroty} | catagory: {info.catagory} | completed: {info.completed}")




# this is the main function of the python
def main():
    data_base.init_db() #calling the function init_db from data_base.py file

#taking ID and password from the user
    print("UNISC BOYD Seurity Module")
    user_ID=input("ENter the ID of student or staff ")
    password= input("Enter the password of the student")
     
    data_base.add_user(user_ID,password) # calling the function add user from data_base.py

    while True: # lopping for infinite time, It will excute unless we broke it out
        print("\nMenu\n1 for add_task\n2 for update_task\n3 for delete_task\n4 for gate_task\n5 for search_task\n6 for exist")
        #testing the input is integer or not
        try:
            choose=int(input("Choose from 1-6"))
        except ValueError:
            print(" Invalid number--> Please, choose from 1-5")
            continue # if the user input the worn input then the code repet the same loop

        if(choose==1):# if the user enter the 1 then the add task method will play main role in database
            info=get_task_input()
            data_base.add_task(user_ID,info)
            print("Info/ task added successfully")
        elif(choose==3):
            task=data_base.get_task(user_ID)
            display_task(task)
            index=int(input("inter index to update")) -1 
            data_base.delete_task(task_id)
            print("delete sucessfully")
        elif(choose==6):
            print("good__Bye::")
            break
        elif(choose==5):
            keyword=input("Enter the keyword to search data")
            if keyword.strip()!="":#.strip is the function that is used to remove the extra spaces from the string
                keyword=keyword
                task=data_base.search_task(user_ID,keyword)
                display_task(task)

            else:
                keyword=None
                print("Please use some keyword")
        elif(choose==4):
            task=data_base.get_task(user_ID)
            display_task(task)
        elif(choose==2):
            task=data_base.get_task(user_ID)
            display_task(task)
            index=int (input("Enter the index to update the task"))-1
            key=input("Field to update (details/due_date/category/priority/completed):").strip()
            value=input("New value").strip()
            task_id=task[index].id
            data_base.update_task(task_id,**{key:value})
            print("Task Update")
        else:
            print("invalid, error in code")

if __name__ == "__main__":
    main()
        
    



   
