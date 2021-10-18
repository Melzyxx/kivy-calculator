from kivy.app import App

#objects
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

#layouts
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

chars = [
	["(", ")", "%", "/"],
	["1", "2", "3", "+"],
	["4", "5", "6", "-"],
	["7", "8", "9", "*"],
	[".", "0", "<", "="]
]

class Calculator(App):
	
	def __init__(self):
		super().__init__()
		self.input = TextInput(text = "", padding_x = (50, 50), padding_y = (50, 50))
	
	def on_click(self, symbol):
		try:
			if symbol.text in "1234567890-+/*.=()%":
				if symbol.text in ".=":
					if symbol.text == ".":
						if self.input.text[-1:] != ".":
							self.input.text += symbol.text
					else:
						self.input.text = str(eval(self.input.text))
				else:
					self.input.text += symbol.text
			elif symbol.text == "<":
				self.input.text = self.input.text[:-1]
		except:
			pass
	
	def build(self):
		main_layout = BoxLayout(orientation = "vertical")
		buttons_layout = GridLayout(rows = 5)
		
		for rows in chars:
			for index in rows:
				buttons_layout.add_widget(Button(text = index, on_press = self.on_click))
		
		main_layout.add_widget(self.input)
		main_layout.add_widget(buttons_layout)
		
		return main_layout

if __name__ == "__main__":
	Calculator().run()