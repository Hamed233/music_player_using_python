# Steps:
	# 1) Install & import Required Libraries (tkinter, pygame)
	# 2) Design app using tkinter
	# 3) Create functions to:
		# addSongs()
		# playSong()
        # stopSong()
		# pauseSong()
		# resumeSong()
		# nextSong()
		# previousSong()

#importing libraries 
from pygame import mixer
from tkinter import *
from tkinter import filedialog

# add many songs to the playlist of python mp3 player
def addSongs():
    #to open a file  
    temp_song=filedialog.askopenfilenames(initialdir="Music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    ##loop through every item in the list to insert in the listbox
    for s in temp_song:
        # s=s.replace("C:/Users/future/Downloads","")
        songs_list.insert(END,s)
     
def deleteSong():
    curr_song=songs_list.curselection()
    songs_list.delete(curr_song[0])
    
def playSong():
    song=songs_list.get(ACTIVE)
    song=f'{song}'
    mixer.music.load(song)
    mixer.music.play()

#to pause the song 
def pauseSong():
    mixer.music.pause()

#to stop the  song 
def stopSong():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

#to resume the song
def resumeSong():
    mixer.music.unpause()

#Function to navigate from the current song
def previousSong():
    #to get the selected song index
    previous_one=songs_list.curselection()
    #to get the previous song index
    previous_one=previous_one[0]-1
    #to get the previous song
    temp2=songs_list.get(previous_one)
    temp2=f'{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    #activate new song
    songs_list.activate(previous_one)
    #set the next song
    songs_list.selection_set(previous_one)

def nextSong():
    #to get the selected song index
    next_one=songs_list.curselection()
    #to get the next song index
    next_one=next_one[0]+1
    #to get the next song 
    temp=songs_list.get(next_one)
    temp=f'{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    #activate newsong
    songs_list.activate(next_one)
     #set the next song
    songs_list.selection_set(next_one)

#creating the root window 
root=Tk()
root.title('Python MP3 Music player App ')
#initialize mixer 
mixer.init()

normalFont = ("arial")
listBoxFont = ("arial", 15)

#menu 
my_menu = Menu(root)
root.config(menu=my_menu)
control_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=control_song_menu)
control_song_menu.add_command(label="Add songs",command=addSongs)
control_song_menu.add_command(label="Delete song",command=deleteSong)

# Column specifies which column you wish the widget to appear in
# columnspan tells the layout manager that you wish for this widget to occupy more than 1 column i.e. spans across 2 columns.

#create the listbox to contain songs
songs_list=Listbox(root, bg="black", fg="white", font=listBoxFont, height=12, width=47, selectmode=SINGLE, selectbackground="gray", selectforeground="black")
songs_list.grid(columnspan=9)

#play button
play_button=Button(root,text="Play", font=normalFont, width =7,command=playSong)
play_button.grid(row=1,column=0)

#pause button 
pause_button=Button(root,text="Pause",font=normalFont, width =7,command=pauseSong)
pause_button.grid(row=1,column=1)

#stop button
stop_button=Button(root,text="Stop",font=normalFont,width =7,command=stopSong)
stop_button.grid(row=1,column=2)

#resume button
Resume_button=Button(root,text="Resume", font=normalFont, width =7,command=resumeSong)
Resume_button.grid(row=1,column=3)

#previous button
previous_button = Button(root,text="Prev",font=normalFont, width =7,command=previousSong)
previous_button.grid(row=1,column=4)

#nextbutton
next_button=Button(root,text="Next",font=normalFont,width =7,command=nextSong)
next_button.grid(row=1, column=5)


mainloop()