import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

# functions go here
def hello(self):
	print('Hello world!')

def gtkIsCool(self):
	print('Gtk seems easy to work with here')

class Win(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Fancy Hello")
		

window = Gtk.Window(title='Test')
button=Gtk.Button(label='What will happen?')
button.connect('clicked', hello)

button2=Gtk.Button(label='Flowlayout lol')
button2.connect('clicked', gtkIsCool)
window.add(button)
window.add(button2)

window.show_all()
window.connect('destroy', Gtk.main_quit)
Gtk.main()
