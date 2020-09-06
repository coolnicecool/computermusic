import musicalbeeps as music
import inspect
from os.path import exists
from os import system as system
play=music.Player(volume=.8,mute_output=True)
note_len=1
bol=False
def NoteLen(notel):
    global note_len
    note_len=notel
def output(b00l):
    global bol
    if b00l==True:
        b00l=False
    elif b00l==False:
        b00l=True   
    bol=b00l
def volume(float):
    global play
    global bol
    play=music.Player(volume=float,mute_output=bol)           
def note(note="C4",lenght=1,wait=-1.0): 
    try:
        wait=float(wait) 
        if wait>0:
            wait=wait*note_len
        lenght=lenght*note_len
        play.play_note(note,lenght,wait)
    except KeyboardInterrupt:
        system("python music2.py") 
def unfinshed():
    NoteLen(.09868421052)
    output(True)    
    volume(.7) 
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("") 
    note("")      
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("") 
    note("")      
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("") 
    note("")      
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("") 
    note("")      
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("") 
    note("")      
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("") 
    note("")      
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")
    note("")                                                                                                                                                                                 
def instruction_converter(song):     
    instructions=inspect.getsource(song[0])  
    instructions = instructions.split("\n",1)[1]
    instructions=instructions.replace(" ","")  
    save_as=input("Type what name you want for instruction file\nType here:")
    save_as=save_as.replace(".txt","")
    save_as=save_as.replace(".SI","")
    if exists(save_as+".SI")==True:
        check=input("This File Already Exist Are You Sure You Want To Replace It[Y/N]:")
        check=check.lower()
        if check!="y":
            return
    enter=open(save_as+".SI","w+")
    enter.write(instructions)
    enter.close()
def main():
    choice=input("-------------------------------------------------------\nType 1 to listen to unfinshed\nType 2 to listen to a song text file\nType 3 to convert song into instruction song file\nType 4 to reload program\nType 5 to exit progarm\n-------------------------------------------------------\nYour choice:")  
    if choice =="1":
        unfinshed()    
    if choice == "2": 
        document=input("Type the name of the document\nType name here:")  
        document=document.replace(".SI","")
        document+=".SI"
        exec(open(document).read()) 
    if choice =="3":
        song=[unfinshed]
        instruction_converter(song) 
    if choice=="4":
        system("python music2.py") 
    if choice=="5":
        exit()                
while True:
    main()