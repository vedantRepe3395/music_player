from tkinter import *  # this is used to  gui
from pygame import mixer  # used for music player oparation
from tkinter import filedialog  # used for file oprations
import tkinter.messagebox  # to show massage box lik
import os

mixer.init()  # intialize mixer

root = Tk()  # start gui named root
root.title("Audio Player")  # titel
root.iconbitmap('data/images/icon.ico')  # icon
root.config(bg="white")

if __name__ == "__main__":

    statusbar = Label(root, text="browse file frist", relief=SUNKEN, anchor=W, bg="white")
    statusbar.pack(side=BOTTOM, fill=X, )

    def add_to_playlist(f):
        f=os.path.basename(f)
        index=0
        list.insert(index,f)



    def file_open():

        global file
        file = filedialog.askopenfile()
        global s
        s=file
        add_to_playlist(s)

    def abt_us():
        tkinter.messagebox.showinfo("abot us",  'This app is made by "Vedant Repe"')
        # used to open new gui foe show info

    # cerate menubar

    menubar = Menu(root)
    root.config(menu=menubar)
    sunmenu = Menu(menubar, tearoff=0)	
    menubar.add_cascade(label="file", menu=sunmenu)
    sunmenu.add_cascade(label="open", command=file_open)
    sunmenu.add_cascade(label="close", command=root.destroy)
    sunmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="about", menu=sunmenu)
    sunmenu.add_cascade(label="about us", command=abt_us)
    menubar.add_cascade(label="about", menu=sunmenu)
    sunmenu.add_cascade(label="about us", command=abt_us)
    # menubar starts here

    menubar = Menu(root)  # cerate menubar
    root.config(menu=menubar)
    sunmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="file", menu=sunmenu)
    sunmenu.add_cascade(label="open", command=file_open)
    sunmenu.add_cascade(label="close", command=root.destroy)
    sunmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="about", menu=sunmenu)
    sunmenu.add_cascade(label="about us", command=abt_us)


    # menubar program finished

    def play_music():

                try:
                    pause
                    mixer.music.unpause()
                    statusbar['text'] = "now playing" + file.name
                except NameError:
                    try:
                        f = list.curselection()
                        f = int(f)
                        f = list[f]
                        mixer.music.load(f)
                        mixer.music.play()
                        statusbar['text'] = "now playing" + f
                    except NameError:

                        try:

                            mixer.music.load(file)
                            mixer.music.play()
                            statusbar['text'] = "now playing" + file.name

                        except:
                            # used to new gui showing error
                            tkinter.messagebox.showerror("ERROR", "Error to detect file\n It detects audio files only ")


    def rewimd_music():
        mixer.music.rewind()
        statusbar['text'] = "music rewined"
        play_music()


    def pause_music():
        global pause
        pause = TRUE
        mixer.music.pause()
        statusbar['text'] = "music paused"


    def stop_music():
        mixer.music.stop()
        statusbar['text'] = "music stoped"


    def vol_set(volume):
        vol = int(volume) / 100
        mixer.music.set_volume(vol)

        if vol == 0:
            unmute_button.config(image=mute_image)
            statusbar['text'] = "muted"

        else:
            unmute_button.config(image=unmute_image)


    global muted
    muted = False


    def mute_music():
        global muted
        if muted:
            mixer.music.set_volume(0.3)
            volume.set(30)
            unmute_button.config(image=unmute_image)
            muted = False
            statusbar['text'] = "now playing" + file.name

        else:
            mixer.music.set_volume(00)
            volume.set(0.0)
            unmute_button.config(image=mute_image)
            muted = True
            statusbar['text'] = "muted"

        # play list


    playlist_frame = Frame(root, bg="white")
    playlist_frame.pack(side=LEFT, padx=10)
    list = Listbox(playlist_frame, bg="white")
    list.pack()
    add_button = Button(playlist_frame, text="+add", command=file_open)
    add_button.pack(side=LEFT)
    remove_button = Button(playlist_frame, text="-remove")
    remove_button.pack(side=LEFT)

    # play list ends


    text = Label(root, text="Let's create some noice",bg="white")
    text.pack(pady=10)

    frist_frame = Frame(root)
    frist_frame.config(bg="white")
    frist_frame.pack(pady=10)

    play_iamge = PhotoImage(file="data/images/play.png")
    pause_image = PhotoImage(file="data/images/pause.png")
    stop_image = PhotoImage(file="data/images/stop.png")
    rewind_image = PhotoImage(file="data/images/rewind.png")

    play_button = Button(frist_frame, image=play_iamge, command=play_music)
    pause_button = Button(frist_frame, image=pause_image, command=pause_music)
    rewind_button = Button(frist_frame, image=rewind_image, command=rewimd_music)
    stop_button = Button(frist_frame, image=stop_image, command=stop_music)

    play_button.pack(side=LEFT,padx=5)
    rewind_button.pack(side=LEFT,padx=5)
    pause_button.pack(side=LEFT,padx=5)
    stop_button.pack(side=LEFT,padx=5)

    second_frame = Frame(root)
    second_frame.pack(pady=10)
    second_frame.config(bg="white")

    mute_image = PhotoImage(file="data/images/mute.png")
    unmute_image = PhotoImage(file="data/images/unmute.png")

    mute_button = Button(second_frame, image=mute_image, command=mute_music)
    unmute_button = Button(second_frame, image=unmute_image, command=mute_music)

    unmute_button.pack(side=LEFT)

#    volume = Scale(second_frame, from_=0, to=100, orient=HORIZONTAL, command=vol_set, bg="white")
    volume.set(70)
    mixer.music.set_volume(0.7)
    volume.pack(side=LEFT)


root.mainloop()