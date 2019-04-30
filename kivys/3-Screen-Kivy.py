''' 

CREDITS=https://pythonprogramming.net/buttons-events-kivy-application-python-tutorial/

Today  we're going to be working on buttons and events.

Our objective here is to let the user type in the server IP, port, and pick a username, then join the server.

'''
import kivy

from kivy.app import App # required base class for your app.

from kivy.uix.label import Label # uix element that will hold text

from kivy.uix.textinput import TextInput #to get text iput

from kivy.uix.gridlayout import GridLayout # to set arrangement for various widgets on screen of App


from kivy.uix.button import Button

from kivy.uix.screenmanager import ScreenManager,Screen

import os
kivy.require("1.10.1")

class ConnectPage(GridLayout): #    This class is used as a Base for our Root Widget (ConnectPage) defined here
    
    def __init__(self):
        super().__init__()# this is just calling init method of GridLayout

        self.cols=2# create 2 Columns and infinite rows

        if os.path.isfile('prev_details.txt'):
            with open('prev_details.txt','r') as f:
                d=f.read().split(',')

                prev_ip=d[0]
                prev_port=d[1]
                prev_username=d[2]

        else:
            prev_ip=''
            prev_port=''
            prev_username=''



        #We ask the GridLayout to manage its children in two columns and add a Label and a TextInput for the IP and Username and Port.


        self.add_widget(Label(text="IP:"))# First Columns

        self.ip=TextInput(text=prev_ip,multiline=False)#take text input from user only in Single Line
        self.add_widget(self.ip)


        self.add_widget(Label(text="Port:"))

        self.port=TextInput(text=prev_port,multiline=False)
        self.add_widget(self.port)

        self.add_widget(Label(text="Username:"))

        self.username=TextInput(text=prev_username,multiline=False)
        self.add_widget(self.username)

        self.join = Button(text="Join")
        self.join.bind(on_press=self.join_button) #Joining Function for a button Click so that Button Can Work
        self.add_widget(Label())  # We're doing that to just take up the grid spot that is currently the lower-left.
        self.add_widget(self.join) # define a button and assign it to a widget


    def join_button(self,instance):
        port = self.port.text
        ip=self.ip.text
        username=self.username.text
        

        with open('prev_details.txt','w') as f:
            f.write('{},{},{}'.format(ip,port,username))
            #print("Joining {}:{} as {}".format(ip,port,username))
        info='Joining {} as {}'.format(ip,username)
        
        # to update the info on our screen
        
        chat_app.info_page.update_info(info)
        
        chat_app.screen_manager.current='Info'


        
class InfoPage(GridLayout):
    def __init__(self):
        super().__init__()
        
        self.cols=1
        # And one label with bigger font and centered text
        self.message=Label(halign='center',valign='bottom',font_size=30)
        
        # By default every widget returns it's side as [100, 100], it gets finally resized,
        # but we have to listen for size change to get a new one
        # more: https://github.com/kivy/kivy/issues/1044
        self.message.bind(width=self.update_text_width)

        # Add text widget to the layout
        self.add_widget(self.message)

    # Called with a message, to update message text in widget
    def update_info(self, message):
        self.message.text = message

    # Called on label width update, so we can set text width properly - to 90% of label width
    def update_text_width(self, *_):
        self.message.text_size = (self.message.width * 0.9, None)



class SahibApp(App):
    def build(self):
        # We are going to use screen manager, so we can add multiple screens
        # and switch between them
        self.screen_manager = ScreenManager()# Creating Object of Screen Manger
        
        
        # First create a page, then a new screen, add page to screen and screen to screen manager
        self.connect_page = ConnectPage()
        screen = Screen(name='Connect')
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)
        
         # Info page
        self.info_page = InfoPage()
        screen = Screen(name='Info')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == '__main__':
    chat_app = SahibApp()
    chat_app.run()


#Now, every time you run the script, your previous connection details are saved you wont need to re-enter them.
