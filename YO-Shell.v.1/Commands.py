# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 00:32:05 2016
"""
import os
import stat
import datetime
import shutil

from os.path import expanduser


#perform file system operations such as permissions, owner and the rest
class File_system_operations(object):
   def  __init__(self):
       self.group =[]
       self.user = []
       self.others=[]
       self.list_of_all_permissions =[]
       self.object_permission = ""
       
   def group_permissions(self,object_passed):
       self.group=[]
       current_object = os.stat(object_passed)
       if(current_object.st_mode & stat.S_IRGRP):
           self.group.append("r")
       else:
           self.group.append("-")
           
       if(current_object.st_mode & stat.S_IWGRP):
           self.group.append("w")
       else:
           self.group.append("-")
      
       if(current_object.st_mode & stat.S_IXGRP):
           self.group.append("x")
       else:
           self.group.append("-")
       
           
   def user_permissions(self,object_passed):
       self.user=[]
       current_object = os.stat(object_passed)
       if(current_object.st_mode & stat.S_IRUSR):
           self.user.append("r")
       else:
           self.user.append("-")
           
       if(current_object.st_mode & stat.S_IWUSR):
           self.user.append("w")
       else:
           self.user.append("-")

       if(current_object.st_mode & stat.S_IXUSR):
           self.user.append("x")
       else:
           self.user.append("-")

   def others_permissions(self,object_passed):
       self.others= []
       current_object = os.stat(object_passed)
       if(current_object.st_mode & stat.S_IROTH):
           self.others.append("r")
       else:
           self.others.append("-")
           
       if(current_object.st_mode & stat.S_IWOTH):
           self.others.append("w")
       else:
           self.others.append("-")

       if(current_object.st_mode & stat.S_IXOTH):
           self.others.append("x")
       else:
           self.others.append("-")
    
   def get_object_permission(self):
        self.list_of_all_permissions = self.user + self.group + self.others

        self.object_permission = ''.join(self.list_of_all_permissions)
        return self.object_permission
    
   #def owner(self, object_passed):
       #current_object = os.stat(object_passed)
       
       #owner_Id = current_object.st_uid
       #owner = pwd.getpwuid(owner_Id)[0]

       #return owner
   
   def date_modified(self, object_passed):
       current_object_time = os.path.getmtime(object_passed)
       
       current_object_time = str(datetime.datetime.fromtimestamp(current_object_time))[:19]
       
       return current_object_time
       
   def date_changed(self, object_passed):
       current_object_time = os.path.getctime(object_passed)
       
       current_object_time = str(datetime.datetime.fromtimestamp(current_object_time))[:19]
       
       return current_object_time
       
   def date_accessed(self, object_passed):
       current_object_time = os.path.getatime(object_passed)
       
       current_object_time = str(datetime.datetime.fromtimestamp(current_object_time))[:19]
       
       return current_object_time
      
   def object_size(self, object_passed):
       total_size = 0
       #if object passed is a file
       if(os.path.isfile(object_passed)):
           total_size = os.path.getsize(object_passed)
       
           if(total_size >= 0 and total_size < 1000000):
               total_size= total_size /1024
               total_size = str(total_size)[:4] + "Kb"
                   
           elif(total_size>= 1000000 and total_size < 1000000000  ):
               total_size= total_size /1000000
               total_size = str(total_size)[:4] + "Mb"
               
           elif(total_size>= 1000000000  ):
               total_size= total_size /1000000000
               total_size = str(total_size)[:4] + "Gb"
           
           return total_size
        
       #if object passed is a folder
       elif(os.path.isdir(object_passed)):
           total_size = os.path.getsize(object_passed)
           for item in os.listdir(object_passed):
                itempath = os.path.join(object_passed, item)
                if os.path.isfile(itempath):
                    total_size += os.path.getsize(itempath)
                elif os.path.isdir(itempath):
                    total_size += self._total_size(itempath)
                    
           if(total_size >=0 and total_size < 1000000):
               total_size= total_size /1024
               total_size = str(total_size)[:4] + "Kb"
               
           elif(total_size>= 1000000 and total_size < 1000000000  ):
               total_size= total_size /1000000
               total_size = str(total_size)[:4] + "Mb"
               
           elif(total_size>= 1000000000  ):
               total_size= total_size /1000000000
               total_size = str(total_size)[:4] + "Gb"
               
           return total_size
        
       else:
           return total_size

#store and act on commands
class Commands(object):
    def __init__(self):
        pass
    
    #function "cat": outputs text to screen
    def Cat(command_passed, command_length):
        #cat command is to be of length 2, command and argument
        if(command_length == 2):
            #get the argument passed which is the second index/also file name
            argument_passed = command_passed[1]
            
            #check if argument is a file
            if os.path.isfile(argument_passed):
                #check if user has access to read file
                if(os.access(argument_passed, os.R_OK)):
                    #open the file for reading
                    open_file = open(argument_passed,"r")  
                    
                    #read enter file
                    read_data = open_file.read()
                    print(read_data)
                else:
                    print("You don't have permission to view this file")
            else:
                print("Passed argument is not a file")
                
        else:
            print("Check command, Should be of the form \n[cat filename]")
            
    #function "CHMOD": outputs text to screen
    def Chmod(command_passed, command_length, command_mod):
        #CHMOD command is to be of length 3, command and argument
        if(command_length == 3):
            #get the argument passed which is the second index/also file name
            argument_passed = command_passed[2]            
            #check if argument is a file
            if os.path.isfile(argument_passed):
                             
                #change mod                                     
                os.chmod(argument_passed,int(command_passed[1]))   
                #os.chmod(argument_passed, stat.S_IRWXU|stat.S_IRGRP|stat.S_IROTH)                                                   
                print('mod has been changed to '+command_passed[1])
                                                                    
            else:
                print("Passed argument is not a file")
                
        else:
            print("Check command, Should be of the form \n[chmod filename]") 
    
    #function WC: counts words and lines in a file
    def WC(command_passed,command_length):
        flags = ["-l"]        
        second_argument = command_passed[1]
        hyphen = second_argument[0]        
        
        #word count shouldn't have length  less than two
        if(command_length < 2 or command_length > 3):
            print("Check command, Should be of the form \n[wc filename] or [wc -l filename] ")
        
        #check if command is two i.e should be command and file name
        elif(command_length==2):
            argument_passed = command_passed[1]
            
            #check if argument is a file
            if os.path.isfile(argument_passed):
                #check if user has permission
                if(os.access(argument_passed, os.R_OK)):  
                    #open the file for reading
                    open_file = open(argument_passed,"r")
                    
                    #get each line
                    line = open_file.readline()
                    #create list for splitting
                    words =[]
                    #create a variable count for words
                    count=0
                    
                    #read till there is no line
                    while(line):
                        #split each line to a list using space as delimiter
                        words = line.split(" ")
                        #add length of list words to count
                        count += len(words)
                        #read another line
                        line = open_file.readline()
                    #print output
                    print("WC " + str(count) +" " +argument_passed)
                else:
                    print("You don't have permission to view this file")
            
            #check if a flag is passed as the second argument
            elif(hyphen == "-"):
                print("Add an Argument; \nCommand Should be of the form [wc -l filename]")
                    
            else:
                print("Passed argument is not a file")  
                
        #if second argument starts with an hyphen
        
        #check if ccommand has three arguments i.e includes a flag and filename
        elif(command_length==3):
            #get flag
            flag_passed = command_passed[1]
            #get file
            argument_passed = command_passed[2]
            
            #if flag passed doesn't exist
            if(not flag_passed in flags):
                print("Check Flag should be one of the following" )
                print(flags)
            
            #check if flag is good and passed argument is a file
            elif(flag_passed in flags and os.path.isfile(argument_passed) ):
                #check if user has permission
                if(os.access(argument_passed, os.R_OK)): 
                    #open the file for reading
                    open_file = open(argument_passed,"r")
                    
                    #get each line
                    line = open_file.readline()
                    #create a variable for line count
                    count =0
                    
                    #read till there is no line
                    while(line):
                        count +=1
                        
                        #read another line
                        line = open_file.readline()
                     #print output
                    print("Line count " + str(count) +" " +argument_passed)
                    
                else:
                    print("You don't have permission to view this file")
            
            else:
                print("File is not a file")
                
    #function for listing contents of a directory
    def Ls(command_passed, command_length):
        file_operations = File_system_operations()
        
        #flags for list
        flags_list = ["-l","-s","-m","-a","-c"]
        
        #check if the command length meets the ls requirement
        if(command_length > 3):
           print ("Too many arguments passed should have the format \n[ls -flag]")
           
        elif(command_length == 1):
             #get contents of current directory and print
             contents_of_directory = os.listdir(".")
             for contents in contents_of_directory:
                 print(contents)
        
        #if the length of the command is 2
        elif(command_length ==2):
            #get second item in the command
            second_value = command_passed[1]
            
            #if second is a flag
            if(second_value in flags_list):
                
                #if flag is "-l"
                if(second_value == "-l"):
                    print('{:>35} {:>20} {:>20} {:>20} {:>20} {:>20}'.format("File Name", "Size", "Permissions", "Accessed","Modified", "Changed"))
                    print('{:>35} {:>20} {:>20} {:>20} {:>20} {:>20}'.format("__________","__________", "__________"," __________" ,"__________"," __________"))
                    #get long list of current directory
                    contents_of_directory = os.listdir(".")
                    for contents in contents_of_directory:
                            #check if content is accessible
                            if(os.access(contents, os.R_OK)):
                                #call functions that check the permission status of an object 
                                file_operations.user_permissions(contents)
                                file_operations.group_permissions(contents)
                                file_operations.others_permissions(contents)
                            
                               #get the combined permission of an object
                                object_permission = str(file_operations.get_object_permission())
                                #get the time values of an object
                                object_time_modified = str(file_operations.date_modified(contents))
                                object_time_changed  = str(file_operations.date_changed(contents))
                                object_time_accessed = str(file_operations.date_accessed(contents))
                                object_size = str(file_operations.object_size(contents))
                                
                                print('{:>35} {:>20} {:>20} {:>20} {:>20} {:>20}'.format(contents, object_size ,object_permission , object_time_accessed, object_time_modified, object_time_changed))
               
                #if flag is "-m"
                elif(second_value == "-m"):
                    print('{:>35} {:>20} {:>20} {:>20} {:>20} {:>20}'.format("File Name", "Size", "Permissions", "Accessed","Modified", "Changed"))
                    print('{:>35} {:>20} {:>20} {:>20} {:>20} {:>20}'.format("__________","__________", "__________"," __________" ,"__________"," __________"))
                   
                    #create aray for each column
                    object_name= []
                    permissions =[]
                    time_modified = []   
                    time_change = []
                    time_accessed = []
                    size = []
                    
                    #get long list of current directory
                    contents_of_directory = os.listdir(".")
                    for contents in contents_of_directory:
                            #check if content is accessible
                            if(os.access(contents, os.R_OK)):
                                #call functions that check the permission status of an object 
                                file_operations.user_permissions(contents)
                                file_operations.group_permissions(contents)
                                file_operations.others_permissions(contents)
                            
                               #get the combined permission of an object
                                object_permission = str(file_operations.get_object_permission())
                                #get the time values of an object
                                object_time_modified = str(file_operations.date_modified(contents))
                                object_time_changed  = str(file_operations.date_changed(contents))
                                object_time_accessed = str(file_operations.date_accessed(contents))
                                object_size = str(file_operations.object_size(contents))
                                
                                #add each value to appropriate list
                                object_name.append(contents)
                                permissions.append(object_permission)
                                time_modified.append(object_time_modified)
                                time_change.append(object_time_changed)
                                time_accessed.append(object_time_accessed)
                                size.append(object_size)                                
                                
                                #create a sorted zipped list based on time modified
                                zipped_list_m = sorted(zip(time_modified,object_name,size,permissions, time_change, time_accessed), reverse = True)
                                
                                object_name = [object_name for (time_modified,object_name,size,permissions, time_change, time_accessed) in zipped_list_m]
                                size = [size for (time_modified,object_name,size,permissions, time_change, time_accessed) in zipped_list_m]
                                permissions = [permissions for (time_modified,object_name,size,permissions, time_change, time_accessed) in zipped_list_m]
                                time_accessed = [time_accessed for (time_modified,object_name,size,permissions, time_change, time_accessed) in zipped_list_m]
                                time_modified = [time_modified for (time_modified,object_name,size,permissions, time_change, time_accessed) in zipped_list_m]
                                time_change = [time_change for (time_modified,object_name,size,permissions, time_change, time_accessed) in zipped_list_m]
                                
                                
                                
                    for i in range(len(object_name)):
                       print('{:>35} {:>20} {:>20} {:>20} {:>20} {:>20}'.format(object_name[i], size[i] ,permissions[i] , time_accessed[i],time_modified[i], time_change[i]))
             
                #if flag is "-a"
                elif(second_value == "-a"):
                    print('{:>35} {:>20} {:>20} {:>20} {:>20} {:>20}'.format("File Name", "Size", "Permissions", "Accessed","Modified", "Changed"))
                    print('{:>35} {:>20} {:>20} {:>20} {:>20} {:>20}'.format("__________","__________", "__________"," __________" ,"__________"," __________"))
                   
                    #create aray for each column
                    object_name= []
                    permissions =[]
                    time_modified = []   
                    time_change = []
                    time_accessed = []
                    size =[]
                    
                    #get long list of current directory
                    contents_of_directory = os.listdir(".")
                    for contents in contents_of_directory:
                            #check if content is accessible
                            if(os.access(contents, os.R_OK)):
                                #call functions that check the permission status of an object 
                                file_operations.user_permissions(contents)
                                file_operations.group_permissions(contents)
                                file_operations.others_permissions(contents)
                            
                               #get the combined permission of an object
                                object_permission = str(file_operations.get_object_permission())
                                #get the time values of an object
                                object_time_modified = str(file_operations.date_modified(contents))
                                object_time_changed  = str(file_operations.date_changed(contents))
                                object_time_accessed = str(file_operations.date_accessed(contents))
                                object_size = str(file_operations.object_size(contents))
                                
                                #add each value to appropriate list
                                object_name.append(contents)
                                permissions.append(object_permission)
                                time_modified.append(object_time_modified)
                                time_change.append(object_time_changed)
                                time_accessed.append(object_time_accessed)
                                size.append(object_size)
                                
                                #create a sorted zipped list based on time modified
                                zipped_list_a = sorted(zip(time_accessed,object_name,size,permissions, time_change, time_modified),reverse = True)
                                
                                object_name = [object_name for (time_accessed,object_name,size,permissions, time_change, time_modified) in zipped_list_a]
                                size = [size for (time_accessed,object_name,size,permissions, time_change, time_accessed) in zipped_list_a]
                                permissions = [permissions for (time_accessed,object_name,size,permissions, time_change, time_modified) in zipped_list_a]
                                time_accessed = [time_accessed for (time_accessed,object_name,size,permissions, time_change, time_modified) in zipped_list_a]
                                time_modified = [time_modified for (time_accessed,object_name,size,permissions, time_change, time_modified) in zipped_list_a]
                                time_change = [time_change for (time_accessed,object_name,size,permissions, time_change, time_modified) in zipped_list_a]
                    
                    
                    for i in range(len(object_name)):
                       print('{:>35} {:>20} {:>20} {:>20} {:>20} {:>20}'.format(object_name[i], size[i] ,permissions[i] , time_accessed[i],time_modified[i], time_change[i]))
               
                #if flag is "-c"
                elif(second_value == "-c"):
                    print('{:>35} {:>20} {:>20} {:>20} {:>20} {:>20}'.format("File Name", "Size", "Permissions", "Accessed","Modified", "Changed"))
                    print('{:>35} {:>20} {:>20} {:>20} {:>20} {:>20}'.format("__________","__________", "__________"," __________" ,"__________"," __________"))
                   
                    #create aray for each column
                    object_name= []
                    permissions =[]
                    time_modified = []   
                    time_change = []
                    time_accessed = []
                    size =[]
                  
                    
                    #get long list of current directory
                    contents_of_directory = os.listdir(".")
                    for contents in contents_of_directory:
                            #check if content is accessible
                            if(os.access(contents, os.R_OK)):
                                #call functions that check the permission status of an object 
                                file_operations.user_permissions(contents)
                                file_operations.group_permissions(contents)
                                file_operations.others_permissions(contents)
                            
                               #get the combined permission of an object
                                object_permission = str(file_operations.get_object_permission())
                                #get the time values of an object
                                object_time_modified = str(file_operations.date_modified(contents))
                                object_time_changed  = str(file_operations.date_changed(contents))
                                object_time_accessed = str(file_operations.date_accessed(contents))
                                object_size = str(file_operations.object_size(contents))
                                
                                #add each value to appropriate list
                                object_name.append(contents)
                                permissions.append(object_permission)
                                time_modified.append(object_time_modified)
                                time_change.append(object_time_changed)
                                time_accessed.append(object_time_accessed)
                                size.append(object_size)
                                
                                #create a sorted zipped list based on time modified
                                zipped_list_c = sorted(zip(time_change,object_name,size,permissions, time_accessed, time_modified),reverse = True)
                                
                                object_name = [object_name for (time_change,object_name,size,permissions, time_accessed, time_modified) in zipped_list_c]
                                size = [size for (time_change,object_name,size,permissions, time_change, time_accessed) in zipped_list_c]
                                permissions = [permissions for (time_change,object_name,size,permissions, time_accessed, time_modified) in zipped_list_c]
                                time_accessed = [time_accessed for (time_change,object_name,size,permissions, time_accessed, time_modified) in zipped_list_c]
                                time_modified = [time_modified for (time_change,object_name,size,permissions, time_accessed, time_modified) in zipped_list_c]
                                time_change = [time_change for (time_change,object_name,permissions,size, time_accessed, time_modified) in zipped_list_c]
                    
                    
                    for i in range(len(object_name)):
                       print('{:>35} {:>20} {:>20} {:>20} {:>20} {:>20}'.format(object_name[i], size[i] ,permissions[i] , time_accessed[i],time_modified[i], time_change[i]))
              
                               
           #if second value is not a flag            
            elif(not second_value in flags_list):
                hyphen = second_value[0]                
                
                #check if second value is a directory
                if (os.path.isdir(second_value)):
                    contents_of_directory = os.listdir(second_value)
                    for contents in contents_of_directory:
                        print(contents)
                
                
                elif (hyphen == '-'):
                    print("Invalid Flag")
                
                else:
                    print("Passed argument isn't a directory")
                    
        elif (command_length==3):
            
            second_argument = command_passed[1]
            third_argument = command_passed[2]
            
            #if second value is a flag and third value is a direcory
            if(second_argument in flags_list and os.path.isdir(third_argument)):
                
                if(second_argument == "-l"):
                    print('{:>35} {:>20} {:>20} {:>20} {:>20}'.format("File Name", "Permissions", "Accessed","Modified", "Changed"))
                    print('{:>35} {:>20} {:>20} {:>20} {:>20}'.format("__________", "__________"," __________" ,"__________"," __________"))
                    #get long list of current directory
                    contents_of_directory = os.listdir(third_argument)
                    for contents in contents_of_directory:
                            #check if it is accessible
                            if(os.access(contents, os.R_OK)):
                                #call functions that check the permission status of an object 
                                file_operations.user_permissions(contents)
                                file_operations.group_permissions(contents)
                                file_operations.others_permissions(contents)
                            
                               #get the combined permission of an object
                                object_permission = str(file_operations.get_object_permission())
                                #get the time values of an object
                                object_time_modified = str(file_operations.date_modified(contents))
                                object_time_changed  = str(file_operations.date_changed(contents))
                                object_time_accessed = str(file_operations.date_accessed(contents))
                                
                                print('{:>35} {:>20} {:>20} {:>20} {:>20}'.format(contents ,object_permission , object_time_accessed, object_time_modified, object_time_changed))
              
              #if flag is "-m"
                elif(second_argument == "-m"):
                    print('{:>35} {:>20} {:>20} {:>20} {:>20} {:>20}'.format("File Name", "Size", "Permissions", "Accessed","Modified", "Changed"))
                    print('{:>35} {:>20} {:>20} {:>20} {:>20} {:>20}'.format("__________","__________", "__________"," __________" ,"__________"," __________"))
                   
                    #create aray for each column
                    object_name= []
                    permissions =[]
                    time_modified = []   
                    time_change = []
                    time_accessed = []
                    size = []
                    
                    #get long list of current directory
                    contents_of_directory = os.listdir(third_argument)
                    for contents in contents_of_directory:
                        #check if content is accessible
                        if(os.access(contents, os.R_OK)):
                             #call functions that check the permission status of an object 
                            file_operations.user_permissions(contents)
                            file_operations.group_permissions(contents)
                            file_operations.others_permissions(contents)
                        
                           #get the combined permission of an object
                            object_permission = str(file_operations.get_object_permission())
                            #get the time values of an object
                            object_time_modified = str(file_operations.date_modified(contents))
                            object_time_changed  = str(file_operations.date_changed(contents))
                            object_time_accessed = str(file_operations.date_accessed(contents))
                            object_size = str(file_operations.object_size(contents))
                            
                            #add each value to appropriate list
                            object_name.append(contents)
                            permissions.append(object_permission)
                            time_modified.append(object_time_modified)
                            time_change.append(object_time_changed)
                            time_accessed.append(object_time_accessed)
                            size.append(object_size)                                
                            
                            #create a sorted zipped list based on time modified
                            zipped_list_m = sorted(zip(time_modified,object_name,size,permissions, time_change, time_accessed), reverse = True)
                            
                            object_name = [object_name for (time_modified,object_name,size,permissions, time_change, time_accessed) in zipped_list_m]
                            size = [size for (time_modified,object_name,size,permissions, time_change, time_accessed) in zipped_list_m]
                            permissions = [permissions for (time_modified,object_name,size,permissions, time_change, time_accessed) in zipped_list_m]
                            time_accessed = [time_accessed for (time_modified,object_name,size,permissions, time_change, time_accessed) in zipped_list_m]
                            time_modified = [time_modified for (time_modified,object_name,size,permissions, time_change, time_accessed) in zipped_list_m]
                            time_change = [time_change for (time_modified,object_name,size,permissions, time_change, time_accessed) in zipped_list_m]
                            
                                
                                
                    for i in range(len(object_name)):
                       print('{:>35} {:>20} {:>20} {:>20} {:>20} {:>20}'.format(object_name[i], size[i] ,permissions[i] , time_accessed[i],time_modified[i], time_change[i]))
             
                
                #if flag is "-a"
                elif(second_argument == "-a"):
                    print('{:>35} {:>20} {:>20} {:>20} {:>20} {:>20}'.format("File Name", "Size", "Permissions", "Accessed","Modified", "Changed"))
                    print('{:>35} {:>20} {:>20} {:>20} {:>20} {:>20}'.format("__________","__________", "__________"," __________" ,"__________"," __________"))
                   
                    #create aray for each column
                    object_name= []
                    permissions =[]
                    time_modified = []   
                    time_change = []
                    time_accessed = []
                    size =[]
                  
                    
                    #get long list of current directory
                    contents_of_directory = os.listdir(third_argument)
                    for contents in contents_of_directory:
                        #check if content is accessible
                        if(os.access(contents, os.R_OK)):
                            #call functions that check the permission status of an object 
                            file_operations.user_permissions(contents)
                            file_operations.group_permissions(contents)
                            file_operations.others_permissions(contents)
                        
                           #get the combined permission of an object
                            object_permission = str(file_operations.get_object_permission())
                            #get the time values of an object
                            object_time_modified = str(file_operations.date_modified(contents))
                            object_time_changed  = str(file_operations.date_changed(contents))
                            object_time_accessed = str(file_operations.date_accessed(contents))
                            object_size = str(file_operations.object_size(contents))
                            
                            #add each value to appropriate list
                            object_name.append(contents)
                            permissions.append(object_permission)
                            time_modified.append(object_time_modified)
                            time_change.append(object_time_changed)
                            time_accessed.append(object_time_accessed)
                            size.append(object_size)
                            
                            #create a sorted zipped list based on time modified
                            zipped_list_a = sorted(zip(time_accessed,object_name,size,permissions, time_change, time_modified),reverse = True)
                            
                            object_name = [object_name for (time_accessed,object_name,size,permissions, time_change, time_modified) in zipped_list_a]
                            size = [size for (time_accessed,object_name,size,permissions, time_change, time_accessed) in zipped_list_a]
                            permissions = [permissions for (time_accessed,object_name,size,permissions, time_change, time_modified) in zipped_list_a]
                            time_accessed = [time_accessed for (time_accessed,object_name,size,permissions, time_change, time_modified) in zipped_list_a]
                            time_modified = [time_modified for (time_accessed,object_name,size,permissions, time_change, time_modified) in zipped_list_a]
                            time_change = [time_change for (time_accessed,object_name,size,permissions, time_change, time_modified) in zipped_list_a]
                
                    
                    for i in range(len(object_name)):
                       print('{:>35} {:>20} {:>20} {:>20} {:>20} {:>20}'.format(object_name[i], size[i] ,permissions[i] , time_accessed[i],time_modified[i], time_change[i]))
               
                
                
                #if flag is "-c"
                elif(second_argument == "-c"):
                    print('{:>35} {:>20} {:>20} {:>20} {:>20} {:>20}'.format("File Name", "Size", "Permissions", "Accessed","Modified", "Changed"))
                    print('{:>35} {:>20} {:>20} {:>20} {:>20} {:>20}'.format("__________","__________", "__________"," __________" ,"__________"," __________"))
                   
                    #create aray for each column
                    object_name= []
                    permissions =[]
                    time_modified = []   
                    time_change = []
                    time_accessed = []
                    size = []
                  
                    
                    #get long list of current directory
                    contents_of_directory = os.listdir(third_argument)
                    for contents in contents_of_directory:
                        #check if content is accessible
                         if(os.access(contents, os.R_OK)):
                            #call functions that check the permission status of an object 
                            file_operations.user_permissions(contents)
                            file_operations.group_permissions(contents)
                            file_operations.others_permissions(contents)
                        
                           #get the combined permission of an object
                            object_permission = str(file_operations.get_object_permission())
                            #get the time values of an object
                            object_time_modified = str(file_operations.date_modified(contents))
                            object_time_changed  = str(file_operations.date_changed(contents))
                            object_time_accessed = str(file_operations.date_accessed(contents))
                            object_size = str(file_operations.object_size(contents))
                            
                            #add each value to appropriate list
                            object_name.append(contents)
                            permissions.append(object_permission)
                            time_modified.append(object_time_modified)
                            time_change.append(object_time_changed)
                            time_accessed.append(object_time_accessed)
                            size.append(object_size)
                            
                            #create a sorted zipped list based on time modified
                            zipped_list_c = sorted(zip(time_change,object_name,size,permissions, time_accessed, time_modified),reverse = True)
                            
                            object_name = [object_name for (time_change,object_name,size,permissions, time_accessed, time_modified) in zipped_list_c]
                            size = [size for (time_change,object_name,size,permissions, time_change, time_accessed) in zipped_list_c]
                            permissions = [permissions for (time_change,object_name,size,permissions, time_accessed, time_modified) in zipped_list_c]
                            time_accessed = [time_accessed for (time_change,object_name,size,permissions, time_accessed, time_modified) in zipped_list_c]
                            time_modified = [time_modified for (time_change,object_name,size,permissions, time_accessed, time_modified) in zipped_list_c]
                            time_change = [time_change for (time_change,object_name,permissions,size, time_accessed, time_modified) in zipped_list_c]
                    
                    
                    for i in range(len(object_name)):
                       print('{:>35} {:>20} {:>20} {:>20} {:>20} {:>20}'.format(object_name[i], size[i] ,permissions[i] , time_accessed[i],time_modified[i], time_change[i]))
                 
                               
               
                else:
                    print("Invalid flag")
            
            #if second argument is not a flag
            elif(not second_argument in flags_list):
                print("Enter a valid flag and command should be of format:\n[ls -flag dir]")
            
            #if third argument is not a directory
            elif(not os.path.isdir(third_argument)):
                print("Incorrect directory")
    
    #remove files or directory            
    def Rm(command_passed, command_length):
        
        #check if command length is 2
        if(command_length==2):
            object_passed = command_passed[1]
            #check if the second argument is a file
            if(os.path.isfile(object_passed)):
                #check if user has access
                if(os.access(object_passed, os.R_OK)):
                    #delete the object
                    os.remove(object_passed)
            #check if it is a directory
            elif(os.path.isdir(object_passed)):
                #check if user has access
                if(os.access(object_passed, os.R_OK)):
                    #delete the object
                    shutil.rmtree(object_passed)
            else:
                print("Argument not a File or Folder")
        
        else:
            print ("Command should be of the format \n[rm file/directory]")
            
    #change directory
    def Cd(command_passed, command_length):
        #check if only "cd is passed"
        if(command_length==1):
            #assigns home directory to home
            home = expanduser("~")
            os.chdir(home)
            
        elif(command_length==2):
            second_argument = command_passed[1]
            
            #change directory to  home directory
            if(second_argument=="~" ):
                 #assigns home directory to home
                home = expanduser("~")
                os.chdir(home)
           
            #go one directory up
            elif(second_argument==".."):
                os.chdir("..")
            
            #go to user defined path
            elif(os.path.isdir(second_argument)):
                directory = second_argument
                os.chdir(directory)
            
            else:
                print ("Invalid argument")
        else:
            print("Invalid command length should be of the form \n[Cd directory_name]")
            
    #copy a file or folder
    def Cp(command_passed, command_length):
        #copy always has a length of three
        if(command_length==3):
            #get second argument
            second_argument = command_passed[1]
            #check if there is a third argument
            if( not command_passed[2] == ""):
                third_argument = command_passed[2]
             
                #if second argument is a file or directory
                if(os.path.isfile(second_argument) or os.path.isdir(second_argument)):
                    if(second_argument == third_argument):
                        print("Can't be copied check names")
                    else:
                        shutil.copy(second_argument,third_argument)
                        if(os.path.isfile(third_argument) or os.path.isdir(third_argument)):
                            print("Copied")
                
                else:
                    print("Passed argument isn't a file or directory")
            else:
                print("Destination not included")
        else:
            print("Wrong command should be of the from \n[cp source destination]")
                
    #move a file or folder
    def Move(command_passed, command_length):
        #copy always has a length of three
        if(command_length==3):
            #get second argument
            second_argument = command_passed[1]
            #check if there is a third argument
            if( not command_passed[2] == ""):
                third_argument = command_passed[2]
             
                #if second argument is a file or directory
                if(os.path.isfile(second_argument) or os.path.isdir(second_argument)):
                    if(second_argument == third_argument):
                        print("Can't be moved check names")
                    else:
                        shutil.move(second_argument,third_argument)
                        if(os.path.isfile(third_argument) or os.path.isdir(third_argument)):
                            print("Moved")
                
                else:
                    print("Passed argument isn't a file or directory")
            else:
                print("Destination not included")
        else:
            print("Wrong command should be of the from \n[cp source destination]")           
            
             
