# Read a text file and return the list of to-do items

def get_todos(filepath="todos.txt"):
    """ Read a text file and 
        return a list of todo-items."""
    with open(filepath,'r') as file:
            todos_local = file.readlines()
    return todos_local
    
# Write to-do items in a text file
  
def write_todos(todos_arg,filepath="todos.txt"):
    """Write the todos-item list in the file"""
    with open(filepath,'w') as file:
            file.writelines(todos_arg)
    
if __name__== "__main__":
    print("Hello")