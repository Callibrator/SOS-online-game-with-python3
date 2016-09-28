#Ena aplo paixnidi gia triliza
#Created by Callibrator
#using python 3.x
#callibrator21@gmail.com

from tkinter import *
from tkinter.messagebox import showerror,showinfo
import _thread as thread
import socket
from os import sep
import random
import time




class game():
         def __init__(self,game="single"):
                  self.o = PhotoImage(file="graphics"+sep+"O.gif")
                  self.x = PhotoImage(file="graphics"+sep+"X.gif")
                  self.turn = "p1" #player 1 = p1 or player 2 = p2
                  self.game= game
                  self.winvar = 0
                  self.winmsg = ""

         def reset(self):
                  self.player1score = 0
                  self.player2score = 0
                  self.turn = random.randint(0,2)
                  if self.turn == 1:
                           self.turn = "p1"
                  else:
                           self.turn = "p2"
                  self.reset_lines()
         def reset_lines(self):
                  self.line1 = ['','','']
                  self.line2 = ['','','']
                  self.line3 = ['','','']
         def close(self,win):
                  if self.game == "online":
                           try:
                                    self.client.send(b"!exit")
                           except:
                                    pass
                  win.destroy()
                  root.update()
                  root.deiconify()
         def reset_canvas(self):
                  self.canvas.create_rectangle(0,0,225,225,fill="black")
                  self.canvas.create_line(75,0,75,225,fill="blue")
                  self.canvas.create_line(150,0,150,225,fill="blue")

                  self.canvas.create_line(0,75,225,75,fill="blue")
                  self.canvas.create_line(0,150,225,150,fill="blue")
         def update_score(self,p1="Player 1 score: ",p2="Player 2 score: "):
                  if self.game == "online":
                           self.scorebox1.config(text=self.player1 +": "+str(self.player1score))
                           self.scorebox2.config(text=self.player2 +": "+str(self.player2score))

                           return 0
                           
                  self.scorebox1.config(text=p1 + str(self.player1score))
                  self.scorebox2.config(text=p2 + str(self.player2score))
         def check(self):


                  for i in [self.line1,self.line2,self.line3]:
                           if i[0] == i[1] and i[1] == i[2] and i[0] != "" or self.line1[0] == self.line2[1] and self.line2[1] == self.line3[2] and self.line1[0] != "" or self.line1[2] == self.line2[1] and self.line2[1] == self.line3[0] and self.line1[2] != "" or self.line1[0] == self.line2[0] and self.line2[0] == self.line3[0] and self.line3[0] != "" or self.line1[1] == self.line2[1] and self.line2[1] == self.line3[1] and self.line3[1] != "" or self.line1[2] == self.line2[2] and self.line2[2] == self.line3[2] and self.line3[2] != "":
                                    self.reset_lines()
                                    self.reset_canvas()
                                    self.update_score()
                                    if self.turn == "p1":
                                             self.player2score += 1
                                             if self.game != "online":
                                                      showinfo("Win","Player 2 win")
                                             if self.game == "online":
                                                      self.messages.config(state="normal")
                                                      self.messages.insert(END,self.player2+" Won\n")
                                                      self.messages.config(state="disabled")
                                                                        
                                    else:
                                             self.player1score += 1
                                             if self.game != "online":
                                                      showinfo("Win","Player 1 win")
                                             if self.game == "online":
                                                      self.messages.config(state="normal")
                                                      self.messages.insert(END,self.player1+" Won\n")
                                                      self.messages.config(state="disabled")

                                                      
                  
                  self.update_score()

                  if ("" in self.line1) == False and ("" in self.line2) == False and ("" in self.line3) == False:
                           self.reset_lines()
                           self.reset_canvas()
                           self.update_score()                           
                                    
                           
                  
         def play(self,event,x="0",y="0"):
                  if x != '0' or y != '0':
                           class ev:
                                    def __init__(self,var1,var2):
                                             self.x = var1
                                             self.y = var2
                           event = ev(x,y) #LOL


                           
                           
                  #print("X: %d, Y: %d"%(event.x,event.y))
                  if event.x < 75 and event.y < 75 and self.line1[0] == '':
                           if self.turn == "p1":
                                    self.canvas.create_image(35,35,image=self.x)
                                    self.line1[0] ="X"
                                    self.turn = "p2"
                           else:
                                    self.canvas.create_image(35,35,image=self.o)
                                    self.line1[0] ="O"
                                    self.turn = "p1"
                  elif event.x > 75 and event.y < 75 and event.x < 150 and self.line1[1] == "":
                           if self.turn == "p1":
                                    self.canvas.create_image(111,35,image=self.x)
                                    self.line1[1] = "X"
                                    self.turn = "p2"
                           else:
                                    self.canvas.create_image(111,35,image=self.o)
                                    self.line1[1] = "O"
                                    self.turn = "p1"
                  elif event.x> 150 and event.y < 75 and event.x < 225 and self.line1[2] =="":
                           if self.turn == "p1":
                                    self.canvas.create_image(186,35,image=self.x)
                                    self.line1[2] = "X"
                                    self.turn = "p2"
                           else:
                                    self.canvas.create_image(186,35,image=self.o)
                                    self.line1[2] = "O"
                                    self.turn = "p1"
                  elif event.x < 75 and event.y < 150 and self.line2[0] == '' and event.y > 75:
                           if self.turn == "p1":
                                    self.canvas.create_image(35,111,image=self.x)
                                    self.line2[0] ="X"
                                    self.turn = "p2"
                           else:
                                    self.canvas.create_image(35,111,image=self.o)
                                    self.line2[0] ="O"
                                    self.turn = "p1"
                  elif event.x > 75 and event.y < 150 and event.x < 150 and self.line2[1] == "" and event.y > 75:
                           if self.turn == "p1":
                                    self.canvas.create_image(111,111,image=self.x)
                                    self.line2[1] = "X"
                                    self.turn = "p2"
                           else:
                                    self.canvas.create_image(111,111,image=self.o)
                                    self.line2[1] = "O"
                                    self.turn = "p1"
                  elif event.x> 150 and event.y < 150 and event.x < 225 and self.line2[2] =="" and event.y > 75:
                           if self.turn == "p1":
                                    self.canvas.create_image(186,111,image=self.x)
                                    self.line2[2] = "X"
                                    self.turn = "p2"
                           else:
                                    self.canvas.create_image(186,111,image=self.o)
                                    self.line2[2] = "O"
                                    self.turn = "p1"
                  elif event.x < 75 and event.y < 225 and self.line3[0] == '' and event.y > 150:
                           if self.turn == "p1":
                                    self.canvas.create_image(35,186,image=self.x)
                                    self.line3[0] ="X"
                                    self.turn = "p2"
                           else:
                                    self.canvas.create_image(35,186,image=self.o)
                                    self.line3[0] ="O"
                                    self.turn = "p1"
                  elif event.x > 75 and event.y < 225 and event.x < 150 and self.line3[1] == "" and event.y > 150:
                           if self.turn == "p1":
                                    self.canvas.create_image(111,186,image=self.x)
                                    self.line3[1] = "X"
                                    self.turn = "p2"
                           else:
                                    self.canvas.create_image(111,186,image=self.o)
                                    self.line3[1] = "O"
                                    self.turn = "p1"
                  elif event.x> 150 and event.y < 225 and event.x < 225 and self.line3[2] =="" and event.y > 150:
                           if self.turn == "p1":
                                    self.canvas.create_image(186,186,image=self.x)
                                    self.line3[2] = "X"
                                    self.turn = "p2"
                           else:
                                    self.canvas.create_image(186,186,image=self.o)
                                    self.line3[2] = "O"
                                    self.turn = "p1"

                  self.check()

                  if self.game == "single" and self.turn=="p2":
                           while True:
                                    a = random.randint(0,8)
                                    lines = self.line1 + self.line2 + self.line3
                                    if lines[a] == "":
                                             break

                           if a == 0:
                                    self.canvas.create_image(35,35,image=self.o)
                                    self.line1[0] ="O"
                                    self.turn = "p1"
                           elif a == 1:
                                    self.canvas.create_image(111,35,image=self.o)
                                    self.line1[1] = "O"
                                    self.turn = "p1"
                           elif a == 2:
                                    self.canvas.create_image(186,35,image=self.o)
                                    self.line1[2] = "O"
                                    self.turn = "p1"
                           elif a == 3:
                                    self.canvas.create_image(35,111,image=self.o)
                                    self.line2[0] ="O"
                                    self.turn = "p1"
                           elif a == 4:
                                    self.canvas.create_image(111,111,image=self.o)
                                    self.line2[1] = "O"
                                    self.turn = "p1"
                           elif a == 5:
                                    self.canvas.create_image(186,111,image=self.o)
                                    self.line2[2] = "O"
                                    self.turn = "p1"
                           elif a == 6:
                                    self.canvas.create_image(35,186,image=self.o)
                                    self.line3[0] ="O"
                                    self.turn = "p1"
                           elif a == 7:
                                    self.canvas.create_image(111,186,image=self.o)
                                    self.line3[1] = "O"
                                    self.turn = "p1"
                           elif a == 8:
                                    self.canvas.create_image(186,186,image=self.o)
                                    self.line3[2] = "O"
                                    self.turn = "p1"
                           self.check()
         def online_playp1(self,event):
                  if self.turn == "p1":
                           self.play(event)
                           self.client.send(("XY:"+str(event.x)+","+str(event.y)+":XY").encode())
                                    

         def online_playp2(self,event):
                  if self.turn == "p2":
                           self.play(event)
                           self.client.send(("XY:"+str(event.x)+","+str(event.y)+":XY").encode())
                                    

                                 
                  
         def create_box(self,frm):
                  self.canvas = Canvas(frm,bg="black",width=225,height=225)
                  self.canvas.pack()

                  self.canvas.create_line(75,0,75,225,fill="blue")
                  self.canvas.create_line(150,0,150,225,fill="blue")

                  self.canvas.create_line(0,75,225,75,fill="blue")
                  self.canvas.create_line(0,150,225,150,fill="blue")
                           
         def multiplayer(self,game):
                  self.game = game
                  self.reset()
                  self.reset_lines()
                  if self.game == "single":
                           self.turn = "p1"
                  root.withdraw()
                  win = Toplevel()
                  win.protocol("WM_DELETE_WINDOW",lambda:self.close(win))

                  
                  win.title("TIC TAC TOE")
                  win.config(bg="black")

                  win.focus_force() #Bring window to the top

                  scoreframe = Frame(win,bg="black")
                  scoreframe.pack(fill=X)

                  self.scorebox1 = Label(scoreframe,text="Player 1 Score: "+str(self.player1score),bg="black",fg="red")
                  self.scorebox1.pack(side=LEFT)
                  self.scorebox2 = Label(scoreframe,text="Player 2 Score: "+str(self.player2score),bg="black",fg="red")
                  self.scorebox2.pack(side=RIGHT)

                  frame1 = Frame(win,bg="black")
                  frame1.pack()
                  self.create_box(frame1)



                  frame2 = Frame(win,bg="black")
                  frame2.pack()

                  Button(frame2,text="Go Back",bg="black",fg="red",command=lambda:self.close(win)).pack()

                  self.canvas.bind("<Button-1>",self.play)

                  win.mainloop()
         def listening(self):
                  while True:
                           try:
                                    buffer = self.client.recv(1024)
                                    buffer = buffer.decode()
                                    if buffer.find("MSG!!!:") != -1:
                                             msg = buffer[buffer.find("MSG!!!:")+7:]
                                             msg = msg[:msg.find(":MSG!!!")]
                                             self.messages.config(state="normal")
                                             self.messages.insert(END,msg)
                                             self.messages.config(state="disabled")

                                    if buffer.find("XY:") != -1:
                                             xy = buffer[buffer.find("XY:")+3:]
                                             xy = xy[:xy.find(":XY")]
                                             xy = xy.split(",")
                                             print(xy)

                                             if self.turn == self.p:
                                                      self.play(None,int(xy[0]),int(xy[1]))

                                    if buffer.find("!exit") != -1:
                                             #self.close(self.win)
                                             self.messages.config(state="normal")
                                             self.messages.insert(END,"Your enemy have disconect the game\n")
                                             self.messages.config(state="disabled")
                                             break
                                             return 0

                                    #if buffer.find("!NAME:") != -1:
                                             ##name = buffer.find("!NAME:")
                                             #nm = buffer[name+5:buffer.find("!NAMEEND:")]
                                             #self.player2 = nm
                                                      
                                    

                           except:
                                    #showerror("Error","Your enemy exit the game")
                                    #self.close(self.win)
                                    self.messages.config(state="normal")
                                    self.messages.insert(END,"Your enemy have disconect the game\n")
                                    self.messages.config(state="disabled")
                                    return 0
                  
         def wait_to_connect(self):
                  showinfo("INFO","Click ok to start waiting your partener to connect")
                  self.client,self.address = self.server_sock.accept()
                  self.client.send(self.player1.encode())
                  self.player2 = self.client.recv(1024).decode()
                  self.scorebox1.config(text=self.player1 +": 0")
                  self.scorebox2.config(text=self.player2 +": 0")
                  thread.start_new_thread(self.listening,())
                  #self.listening()
                  showinfo("INFO","The game is redy to begin")

         def send_message(self):
                  msg = self.tosend.get()
                  if msg == "" or msg == "None" or msg ==" ":
                           return 0
                  
                  self.client.send(("MSG!!!:"+self.name+": "+msg+"\n"+":MSG!!!").encode())
                  self.messages.config(state="normal")
                  self.messages.insert(END,self.name+": "+msg+"\n")
                  self.messages.config(state="disabled")
                  self.tosend.delete(0,END)
                  
                  
         def create_online_server(self,name,ip,port):

                  self.reset()
                  self.reset_lines()
                  self.turn = "p1"
                  self.win.destroy()
                  win = Toplevel()
                  win.protocol("WM_DELETE_WINDOW",lambda:self.close(win))
                  self.game = "online"
                  self.turn = "p1"
                  self.p = "p2"
                  self.player1 = name
                  self.player2 = "NULL"


                  

                  
                  win.title("TIC TAC TOE")
                  win.config(bg="black")

                  win.focus_force()

                  

                  scoreframe = Frame(win,bg="black")
                  scoreframe.pack(fill=X)

                  self.scorebox1 = Label(scoreframe,text="Player 1 Score: "+str(self.player1score),bg="black",fg="red")
                  self.scorebox1.pack(side=LEFT)
                  self.scorebox2 = Label(scoreframe,text="Player 2 Score: "+str(self.player2score),bg="black",fg="red")
                  self.scorebox2.pack(side=RIGHT)

                  frame1 = Frame(win,bg="black")
                  frame1.pack()
                  self.create_box(frame1)
                  
                  
                  #Creating the server. listening etc
                  try:
                           self.name = name
                           self.server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                           self.server_sock.bind((ip,int(port)))
                           self.server_sock.listen(55)
                           self.wait_to_connect()
                           
                  except:
                           showerror("Error","Error Unable to create server")
                           self.close(win)
                           return 0

                  #print(frame1.winfo_width()," ",frame1.winfo_height())

                  messageframe = Frame(win,bg="black")
                  messageframe.pack()
                  Label(messageframe,text="Message:",bg="black",fg="red").pack()
                  self.messages = Text(messageframe,bg="black",fg="red",state ="disabled")
                  self.messages.pack()

                  messagesframe1 = Frame(win,bg="black")
                  messagesframe1.pack(fill=X)

                  self.tosend = Entry(messagesframe1,bg="black",fg="red")
                  self.tosend.pack(fill=X)
                  Button(messagesframe1,bg="black",text="Send",fg="red",command=self.send_message).pack(side=RIGHT)
                  self.tosend.bind("<Return>",lambda event:self.send_message())                  
                  
                  self.canvas.bind("<Button-1>",self.online_playp1)

                  self.win = win
                  win.mainloop()

         def connect_to_game(self,name,ip,port):
                  self.reset()
                  self.reset_lines()
                  self.win.destroy()
                  win = Toplevel()
                  win.protocol("WM_DELETE_WINDOW",lambda:self.close(win))
                  self.game = "online"
                  self.turn = "p1"
                  self.p = "p1"
                  self.player2 = name
                  self.player1 = "NULL"

                  
                  win.title("TIC TAC TOE")
                  win.config(bg="black")

                  win.focus_force()

                  

                  scoreframe = Frame(win,bg="black")
                  scoreframe.pack(fill=X)

                  self.scorebox1 = Label(scoreframe,text="Player 1 Score: "+str(self.player1score),bg="black",fg="red")
                  self.scorebox1.pack(side=LEFT)
                  self.scorebox2 = Label(scoreframe,text="Player 2 Score: "+str(self.player2score),bg="black",fg="red")
                  self.scorebox2.pack(side=RIGHT)

                  frame1 = Frame(win,bg="black")
                  frame1.pack()
                  self.create_box(frame1)

                  try:
                           self.name = name
                           self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                           self.client.connect((ip,int(port)))         
                           self.player1 = self.client.recv(1024).decode()
                           self.client.send(self.player2.encode())

                           self.scorebox1.config(text=self.player1 +": 0")
                           self.scorebox2.config(text=self.player2 +": 0")
                           
                           thread.start_new_thread(self.listening,())
         
                           
                  except:
                           showerror("Error","Unable to connect")
                           self.close(win)
                           return 0

                  
                  messageframe = Frame(win,bg="black")
                  messageframe.pack()
                  Label(messageframe,text="Message:",bg="black",fg="red").pack()
                  self.messages = Text(messageframe,bg="black",fg="red",state ="disabled")
                  self.messages.pack()

                  messagesframe1 = Frame(win,bg="black")
                  messagesframe1.pack(fill=X)

                  self.tosend = Entry(messagesframe1,bg="black",fg="red")
                  self.tosend.pack(fill=X)
                  Button(messagesframe1,bg="black",text="Send",fg="red",command=self.send_message).pack(side=RIGHT)
                  self.tosend.bind("<Return>",lambda event:self.send_message())                  
                  
                  self.canvas.bind("<Button-1>",self.online_playp2)





                  self.win = win
                  win.mainloop()
                  
                  
                  
                  
         def online_game(self):
                  win = Toplevel()
                  win.protocol("WM_DELETE_WINDOW",lambda:self.close(win))

                  
                  win.title("TIC TAC TOE")
                  win.config(bg="black")

                  win.focus_force()
                  root.withdraw()

                  frame1 = Frame(win,bg="black")
                  frame1.pack()
                  Label(frame1,text="Online Game",bg="black",fg="red").pack()

                  frame2 = Frame(win,bg="black")
                  frame2.pack(fill=X)

                  Label(frame2,text="Connect to game",bg="black",fg="red").pack(side=LEFT)

                  frame3 = Frame(win,bg="black")
                  frame3.pack(fill=X)

                  Label(frame3,text="Name: ",bg="black",fg="red").pack(side=LEFT)
                  name = Entry(frame3)
                  name.pack(side=LEFT)
                  name.insert(0,"Player")

                  Label(frame3,text="Server ip: ",bg="black",fg="red").pack(side=LEFT)
                  serverip = Entry(frame3)
                  serverip.pack(side=LEFT)
                  serverip.insert(0,"0.0.0.0")

                  Label(frame3,text="Port: ",bg="black",fg="red").pack(side=LEFT)
                  port = Entry(frame3,width=4)
                  port.pack(side=LEFT)
                  port.insert(0,350)

                  Button(frame3,text="Connect",bg="black",fg="red",command = lambda:self.connect_to_game(name.get(),serverip.get(),port.get())).pack(fill=X)

                  frame4 = Frame(win,bg="black")
                  frame4.pack(fill=X)

                  Label(frame4,text="Create Server",bg="black",fg="red").pack(side=LEFT)

                  frame5 = Frame(win,bg="black")
                  frame5.pack(side=LEFT)

                  Label(frame5,text="Name: ",bg="black",fg="red").pack(side=LEFT)
                  namecr = Entry(frame5)
                  namecr.pack(side=LEFT)
                  namecr.insert(0,"Player")

                  Label(frame5,text="Server ip: ",bg="black",fg="red").pack(side=LEFT)
                  serveripcr = Entry(frame5)
                  serveripcr.pack(side=LEFT)
                  serveripcr.insert(0,"0.0.0.0")

                  Label(frame5,text="Port: ",bg="black",fg="red").pack(side=LEFT)
                  portcr = Entry(frame5,width=4)
                  portcr.pack(side=LEFT)
                  portcr.insert(0,350)

                  Button(frame5,text="Create Game",bg="black",fg="red",command=lambda:self.create_online_server(namecr.get(),serveripcr.get(),portcr.get())).pack(side=LEFT)


                  self.win = win
                  
                  win.mainloop()
                  
                  


#Creating Basic GUI



root = Tk()
root.title("TIC TAC TOE") #elpizo sto tic tac toer na paizoun me X kai O
root.config(bg="black")

#Loading Graphics


g = game()



Label(root,text="TIC TAC TOER GAME",fg="red",bg="black").grid(row=0,column=0)
Label(root,text="Created by Callibrator",fg="red",bg="black").grid(row=1,column=0)

Button(root,text="Single Player",fg="red",bg="black",command=lambda:g.multiplayer("single")).grid(row=2,column=0,sticky=NSEW)
Button(root,text="Multi Player",fg="red",bg="black",command=lambda:g.multiplayer("multi")).grid(row=3,column=0,sticky=NSEW)
Button(root,text="Online Game",fg="red",bg="black",command=g.online_game).grid(row=4,column=0,sticky=NSEW)
Button(root,text="Exit To Desktop",fg="red",bg="black",command=lambda:root.destroy()).grid(row=5,column=0,sticky=NSEW)


root.mainloop()
