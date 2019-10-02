import tkinter

import tkinter.messagebox



top = tkinter.Tk()



def helloCallBack():

   import tkinter

   window= tkinter.Tk()

   window.title("Launcher")

   window.geometry("200x600")

   window.configure(background="#85D6FF")

   lbl=tkinter.Label(window, text="Launch Bar", font=("Calibri", 18), bg="#85D6FF", fg="white")

   spc=tkinter.Label(window, text="", font=("Calibri", 9), bg="#85D6FF")

   spc1=tkinter.Label(window, text="", font=("Calibri",9), bg="#000000")

   spc2=tkinter.Label(window, text="", font=("Calibri", 9))

   spc3=tkinter.Label(window, text="", font=("Calibri", 9))

   spc4=tkinter.Label(window, text="", font=("Calibri", 9))

   spc5=tkinter.Label(window, text="", font=("Calibri", 9))

   spc6=tkinter.Label(window, text="", font=("Calibri", 9))

   spc7=tkinter.Label(window, text="", font=("Calibri", 9))

   spc8=tkinter.Label(window, text="", font=("Calibri", 9))

   spc9=tkinter.Label(window, text="", font=("Calibri", 9))

   spc10=tkinter.Label(window, text="", font=("Calibri", 9))

   spc11=tkinter.Label(window, text="", font=("Calibri", 9))

   spc11=tkinter.Label(window, text="", font=("Calibri", 9))

   spc12=tkinter.Label(window, text="", font=("Calibri", 9))



   def callback():

         x=input("Are you sure you want to shutdown?")

         if x=="Yes":

               import subprocess

               subprocess.call(["shutdown.exe", "-f", "-s", "-t", "10"])

         else:

               exit()

   shutdown=tkinter.Button(window, text="Shut Down", command=callback, fg="red", font=("calibri", 9), bg="white" )





            

   def callback():

         import webbrowser

         webbrowser.open('www.google.com')



   net=tkinter.Button(window, text="Internet",font=("calibri", 9), command=callback, bg="white")



   def callback():

          import webbrowser

          webbrowser.open('www.youtube.com')

   youtube=tkinter.Button(window, text="Youtube", command=callback, font=("calibri", 9), bg="white" )





   def callback():

          import subprocess

          subprocess.Popen("C:\Program Files\Microsoft Office\Office15\WINWORD")

   mword=tkinter.Button(window, text="Microsoft Word", command=callback, font=("calibri", 9), bg="white" )





   def callback():

         import subprocess

         subprocess.Popen("C:\Windows\system32\calc")

   calc=tkinter.Button(window, text="Calculator", command=callback, font=("calibri", 9), bg="white" )





   def callback():

         import webbrowser

         webbrowser.open("http://www.miniclip.com/games/en/")

   games=tkinter.Button(window, text="Games", command=callback, font=("calibri", 9), bg="white" )





   def callback():

         import ctypes

         ctypes.windll.user32.ExitWindowsEx(0, 1)

   log=tkinter.Button(window, text="Log Off", command=callback, fg="#19A319", font=("calibri", 9), bg="white" )





   def callback():

         import webbrowser

         webbrowser.open("http://www.facebook.com")

   facebook=tkinter.Button(window, text="Facebook", command=callback, font=("calibri", 9), bg="white" )





   def callback():

        import webbrowser

        webbrowser.open("http://www.bbc.co.uk/iplayer")

   BBC=tkinter.Button(window, text="BBC IPlayer", command=callback, font=("calibri", 9), bg="white" )





   def callback():

        import subprocess

        subprocess.Popen("C:\Program Files\Microsoft Office\Office15\POWERPNT")

   mPowerPoint=tkinter.Button(window, text="Microsoft Powerpoint", command=callback, font=("calibri", 9), bg="white" )





   def callback():

        import subprocess

        subprocess.Popen("C:\Program Files\Microsoft Office\Office15\EXCEL")

   mExcel=tkinter.Button(window, text="Microsoft Excel", command=callback, font=("calibri", 9), bg="white" )





   def callback():

        import subprocess

        subprocess.Popen("C:\Program Files\Microsoft Office\Office15\MSPUB")

   mpublisher=tkinter.Button(window, text="Microsoft Publisher", command=callback, font=("calibri", 9), bg="white" )







   lbl.pack()

   spc.pack()

   net.pack()

   spc2.pack()

   youtube.pack()

   spc3.pack()

   facebook.pack()

   spc4.pack()

   BBC.pack()

   spc5.pack()

   calc.pack()

   spc6.pack()

   mword.pack()

   spc7.pack()

   mPowerPoint.pack()

   spc8.pack()

   mExcel.pack()

   spc9.pack()

   mpublisher.pack()

   spc10.pack()

   games.pack()

   spc11.pack()

   log.pack()

   spc12.pack()

   shutdown.pack()

   window.mainloop()





B = tkinter.Button(top , text ="Hello", command = helloCallBack)

B.pack()


