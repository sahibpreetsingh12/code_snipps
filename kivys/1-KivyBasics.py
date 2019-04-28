import kivy
from kivy.app import App # required base class for your app.

from kivy.uix.label import Label # uix element that will hold text

from kivy.uix.textinput import TextInput #to get text iput

from kivy.uix.gridlayout import GridLayout # to set arrangement for various widgets on screen of App

kivy.require("1.10.1")

class ConnectPage(GridLayout): #	This class is used as a Base for our Root Widget (ConnectPage) defined here
	
	def __init__(self,**kwargs):
		super().__init__()# this is just calling init method of GridLayout

		self.cols=2# create 2 Columns and infinite rows


		#We ask the GridLayout to manage its children in two columns and add a Label and a TextInput for the IP and Username and Port.


		self.add_widget(Label(text="IP:"))# First Columns

		self.ip=TextInput(multiline=False)#take text input from user only in Single Line
		self.add_widget(self.ip)


		self.add_widget(Label(text="Port:"))

		self.port=TextInput(multiline=False)
		self.add_widget(self.port)

		self.add_widget(Label(text="Username:"))

		self.username=TextInput(multiline=False)
		self.add_widget(self.username)

class SahibApp(App):
	def build(self):
		return ConnectPage()

if __name__ == '__main__':
	SahibApp().run()


# App title is Name of Class to be run using run method 
# If name of the class is ABCApp then Screen Title will be ABC but if name of class is ABCapp then it will be ABCapp
