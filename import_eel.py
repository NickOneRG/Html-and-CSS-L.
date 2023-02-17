
import eel


eel.init('C:/Users/robid/OneDrive/Desktop/Program')

@eel.expose
def App():
    print('App Running')

App()

eel.start('work1.html',size=(500,600))