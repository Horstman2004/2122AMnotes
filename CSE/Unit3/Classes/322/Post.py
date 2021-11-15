#from datetime module import datetime
from datetime import datetime

#declare that we have a class
class Post:
    #everything indented in the class

    #"global" varibles
    postID = 0

    #initialize an object -> Constructorge
    #defining when initialize, we need a username and messa
    def __init__(self,username,message):
        #object's username = usernamePassedIn
        self.un=username
        self.msg=message
        #each object needs a unique number for the post
        self.postID = Post.postID
        Post.postID+=1 
        self.timestamp = datetime.now()

    #string printing format
    #define the string format
    def __str__(self):
        return str(self.postID)+" "+ self.un+" "+self.timestamp.__str__()+":\n\t "+self.msg



    
    #other methods
    #function to rset the username
    def setUserName(self,username):
        self.un=username