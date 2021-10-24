from tkinter import *

root = Tk()

root.title('chat bot')

root.geometry('400x500')

# create a menu bar
main_menu = Menu(root)

# creat the submenu
file_menu = Menu(root)
file_menu.add_command(label = "new..")
file_menu.add_command(label = "save as..")
file_menu.add_command(label = "exit")




main_menu.add_cascade(label = 'file', menu = file_menu)
main_menu.add_command(label = 'edit')
main_menu.add_command(label = 'quit')
main_menu.add_command(label = "about")
main_menu.add_command(label = 'search')
main_menu.add_command(label = 'file')
main_menu.add_command(label = 'settings')

root.config(menu = main_menu)
chatwindow = Text(root,bd =1,bg ='pink',width = '50',height = 8)
chatwindow.place(x =6 ,y =6,height =385,width = 370)

messagewindow = Text(root ,bg = 'black',width = 30,height =4)
messagewindow.place(x =128 ,y =400 ,height =88 ,width =260)

button = Button(root,text = 'send',bg = 'blue',activebackground = 'light blue', height = 5,width =12)
button.place(x = 6 ,y =400 ,height = 88,width =120)

scrollbar =Scrollbar(root ,command = chatwindow.yview())
scrollbar.place(x =375,y =5 ,height = 285)

root.mainloop()