How to Use Music2.py
1.Choose a song to produce
2.In this program go to unfinished this where you will write the song
3.Do you output on your song then type output() in the parentheses type true or false depending on your choice
4.Find how fast a quarter note is the type it in Notlen() parentheses Ex. Notelen(.5) 
5.Then from zero to one put in the loudness in volume()
6.Now you're ready to start producing type note(the note in Concert C sharp or flat(which is represent as b) after note name and octave ,length in quarter notes if no answer it's one, wait after note in beats if nothing waits till done)
Example
you play trumpet or clarinet and the notes C4 for one beat
note("B3b")
Now if it is for three
note("B3b",3)
or it an eight note 
note("B3b",.5)
Now let’s say you have a whole note at the third beat a half note so you would wait two beats if zero happens immediately
note("B3b",2,2)
Example of what is should look like:
def unfinished():
    output(False)
    Notelen(.5)
    volume(.6)
    note("B3b",3)
    note("D4",2,1)
