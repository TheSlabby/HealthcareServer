import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ClientHandler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def send(self):
    
    def onButtonPressed(self, button):
        print("Hello World!")

builder = Gtk.Builder()
builder.add_from_file("clientWindow.glade")
builder.connect_signals(ClientHandler())

window = builder.get_object("window")
window.show_all()

Gtk.main()
