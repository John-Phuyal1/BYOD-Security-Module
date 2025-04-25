#creating the class for security task

class security_task:
    #example of class attributes
    #collage_name="abc collage" / no slef 


    #this is a counstructor for this class 
    def __init__(self,detail,due_date,catagory,priroty,complete):
        # creating the obj atributies
        self.detail=detail
        self.due_date=due_date # formate dd/mm/yy
        self.catagory=catagory
        self.priroty=priroty
        self.complete=complete 
    
    



        
# creating class for user 
class user:
    # creating the counster for class user
    def __init__(self,user_id, Password=None):
        # creating the obj attribute
        self.user_ID=user_id
        self.password=Password

    # creating the methods that is use to add the task 
    def add_task(self,task):
        self.task.append(task)
      # creating the method that is used to del the task  
    def dle_task(self,index):
        if 0<= index < len(self.task):
            del self.task[index]
    # creating the method that is used to update task 
    def upd_task(self,index,**dic_info):
        # cheaking the index
        if 0<=index < len(self.task):
            task=self.task[index]
            # checking the key and value from dic
            for key, value in dic_info.items():
                if hasattr(task,key):# check and give true and false
                    setattr(task,key,value) # to update, its updated in task 
                    
    def to_dic(self):
        return{
    
            "user_ID ":self.user_ID,
            "Password" :self.password


        }
    # this is A static function 
    @staticmethod
    def from_dic(data):
        user = user(data["user_id"], data.get("password"))
        user.tasks = [security_task.from_dict(t) for t in data["tasks"]]
        return user