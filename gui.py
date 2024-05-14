import functions
import FreeSimpleGUI as gui
import time

now = time.strftime("%b %d %Y %H:%M:%S")
clock = gui.Text('', key = "Clock")
label = gui.Text("Type in a to-do:")
input_box = gui.InputText(tooltip="Enter to-do", key="todo")
add_button = gui.Button("Add")
list_box = gui.Listbox(values= functions.get_todos(), key="todos",
                       enable_events="True", size=[45,10])
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")
exit_button = gui.Button("Exit")

window=gui.Window('My to-do App',
                            layout=[[clock],
                                    [label],
                                    [input_box,add_button],
                                    [list_box,edit_button,complete_button],
                                    [exit_button]], 
                            font=("Helvetica",20))

while True:
    event,value = window.read()
    window["Clock"].update(value = time.strftime("%b %d %Y %H:%M:%S"))
    #print(event)
    #print(1,value)
    
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values= todos)
        case "Edit":
            try:
                todo_to_edit = value["todos"][0]
                new_todo = value["todo"]
                
                todo = functions.get_todos()
                index = todo.index(todo_to_edit)
                todo[index] = new_todo
                functions.write_todos(todo)
                window['todos'].update(values= todo)
            except IndexError:
               gui.popup("Select an Item First.",font=("Helvetica",20))
        case "todos":
            window['todo'].update(value= value['todos'][0])
        case "Complete":
            try:
                todos = functions.get_todos()
                completed_todo = value["todo"]
                todos.remove(completed_todo)
                functions.write_todos(todos)
                window['todos'].update(values= todos)
                window['todo'].update(value = "")
            except ValueError:
                gui.popup("Select an Item First.",font=("Helvetica",20))
        case "Exit":
            exit()
        case gui.WIN_CLOSED:
            break
window.close()