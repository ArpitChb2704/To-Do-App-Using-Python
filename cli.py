# from functions import get_todos and write_todos
import functions
import time

now = time.strftime("%b %d %Y %H:%M:%S")
print("It is ",now)

while True:
    # Getting user input and strip the blank spaces after it
    
    a = input( "Type add/show/edit/exit/complete : ")
    user_action = a.strip()
    if user_action.startswith("add") :
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()
            
        todos.append(todo)
        
        functions.write_todos(todos)
    
    elif user_action.startswith("show") :
        
        todos = functions.get_todos()
            
        for index,element in enumerate(todos):
            print(f"{index+1}-{element.strip()}")
    
    elif user_action.startswith("edit") :
        try:
            n = int(user_action[5:])
            todos = functions.get_todos()
            
            print("Existing todo is: ",(todos[n-1]).split())
            a = input("Enter a new Todo:")
            todos[n-1] = a+ '\n'
            
            functions.write_todos(todos)
                
        except ValueError:
            print("Your Command is not valid!")
            continue
            
    
    elif user_action.startswith("complete") :
        try:
            n = int(user_action[9:])
            todos = functions.get_todos()
            
            index = n-1
            todo_completed = todos[index].strip('\n')
            todos.pop(index)
            functions.write_todos(todos)
                
            m = f"Todo {todo_completed} was removed from the list."
            print(m)
        
        except IndexError:
            print("There is no itme with that number.")
            continue 
        
    # exiting the loop
    elif user_action.startswith("exit") :
        break
    
    # when user entered any other input
    else:
      print("You entered a wrong command !")
    

print("........Thank You!......")