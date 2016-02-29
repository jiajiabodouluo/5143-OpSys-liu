# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 13:26:10 2016
"""
#import the class commands from commands.py
from Commands import Commands

#class to append commands to a list, get the commands, and return command counts
class History(object):
    def __init__(self):
        #variable to be used to store history
        self.command_list =[]
        
    #function to push command passed to the list
    def push_command(self, command):
        #append passed value to the list
        self.command_list.append(command)
        
    #function to return all commands stored for the current session to user
    def get_command(self):
        #return command list to user
        return self.command_list
        
    #get number of commands passed in the current session
    def number_of_commands(self):
        #return integer value of length of list
        return len(self.command_list)

    #print history
    def print_history(self):
        #loop through list
        count =0
        for commands in self.command_list:
            count = count + 1
            print(str(count) + ". " +commands)
        
#class that helps split command into parts
class Parse_manager(object):
    def __init__(self):
        #list that contains parts of the command
        self.parts = []
        
    #when called splits user input based on space and returns the output
    def splitter(self,user_input):
        self.parts = user_input.split(" ")
        #return the list
        return self.parts
        
#class that acts on commands inherits from the parse_manager class
class Command_manager(Parse_manager):
    def __init__(self):
        self.user_input = None 
        self.command = None
        self.length = None
        self.history = History()
        
        #list of commands the user can run
        self.command_list = ["cat","chmod","cd","cp","history","ls","mv","rm","wc"]
        
    def start_processing(self,passed_input):
         #add user input to history
        self.history.push_command(passed_input)
        
        #calls the splitter function and assigns returned array to user_input
        self.user_input= self.splitter(passed_input)
        
        #get the length of the split array
        self.length = len(self.user_input)
        
        #get the first part the user passed which should be the command
        self.command = self.user_input[0]

        #check if the "command" part is in the command list
        if self.command in self.command_list:
            #check statements aand call appropriate functions
            #calls the cat function from the command class
            if(str.upper(self.command) == "CAT"):
                Commands.Cat(self.user_input, self.length)
                
            #calls word count function
            elif(str.upper(self.command) == "WC"):
                Commands.WC(self.user_input, self.length)
                
            #calls history function
            elif(str.upper(self.command) == "HISTORY"):
                self.history.print_history()
               # print(command)
                
            #calls the list function
            elif(str.upper(self.command) == "LS"):
                Commands.Ls(self.user_input,self.length)
                
            #calls the remove function
            elif(str.upper(self.command) == "RM"):
                Commands.Rm(self.user_input,self.length)
                
            #calls the change directory function
            elif(str.upper(self.command) == "CD"):
                Commands.Cd(self.user_input,self.length)
                
             #calls the copy function
            elif(str.upper(self.command) == "CP"):
                Commands.Cp(self.user_input,self.length)
                
            #calls the move function
            elif(str.upper(self.command) == "MV"):
                Commands.Move(self.user_input,self.length)
                
            #calls the move function
            elif(str.upper(self.command) == "CHMOD"):
                Commands.Chmod(self.user_input,self.length)
            
        #return error and suggestions
        else:
            print("command doesn't exist \nDo you mean any of these:")
        
            #get the first letter of command
            first_letter = self.command[0]
            
            #variables for suggestion
            count =0
            suggestion_list=[]
            
            #loop through commands list to get suggestions
            for commands in self.command_list:
                #check if commands starts with first letter
                if(commands.startswith(first_letter)):
                    suggestion_list.append(commands)
                    count+=1
            
            #if there is no similar word
            if(count==0):
                print(self.command_list)
            #if there are similar words
            else:
                print(suggestion_list)
    
        
#class that runs the whole program
class Run_shell(object):
    def __init__(self):
      #create an object of the History,command_manager class
      self.history_manager = History()
      self.command_manager = Command_manager()
      
    #function that is called hat starts the whole process
    def kick_start(self):
        #set condition for looping to be true
        Run = True
        
        #run till user types exit or close
        while Run:
            #get user input
            self.user_input = input("$:")
            
            #check what user input is also converts user input to upper case
            if str.upper(self.user_input) == "EXIT" or str.upper(self.user_input) == "CLOSE" :
                Run = False
                
            #if user enters an empty space it should continue the loop    
            elif self.user_input == "":
                continue
            
            #what runs if the user doesn't exit 
            else: 
                #call command manager
                self.command_manager.start_processing(self.user_input)
                
                
                
                

if __name__ == "__main__":
    #create an object of run shell
    start_program = Run_shell()
    
    #call the kick start method of class run shell
    start_program.kick_start()
