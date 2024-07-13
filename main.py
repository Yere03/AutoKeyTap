import sys
import gi
import threading
import time
from pynput.keyboard import Controller

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Adw


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Attributtes of the AppWindow
        self.AutoKeyActivated = False
        self.Key = ""
        self.Time = 5.0
        self.GeneralBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, halign=Gtk.Align.CENTER)
        self.KeyBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, halign=Gtk.Align.CENTER, spacing=20)
        self.TimeBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, halign=Gtk.Align.CENTER, spacing=20)
        self.buttonActivar = Gtk.Button(label="Activar")
        self.buttonSetKey = Gtk.Button(label="Establecer tecla")
        self.buttonSetTime = Gtk.Button(label="Establecer intervalo de tiempo (Segundos)")
        self.entryTime = Gtk.Entry()
        self.entryTime.set_text("5")
        self.entryKey = Gtk.Entry()
        # Setting Window Size Title and Resizeable

        self.set_default_size(800, 200)
        self.set_title("AutoKeyTapper")
        self.set_resizable(False)
        # Setting properties to place the items in the GeneralBox
        self.buttonActivar.set_property("margin-top", 200)
        self.buttonSetKey.set_property("margin-top", 200)
        self.entryKey.set_property("margin-top", 200)
        # Setting properties to place the items in the TimeBox
        self.entryTime.set_property("margin-top", 100)
        self.entryTime.set_property("margin-bottom", 200)
        self.buttonSetTime.set_property("margin-top", 100)
        self.buttonSetTime.set_property("margin-bottom", 200)
        # Adding Boxes to GeneralBox
        self.GeneralBox.append(self.KeyBox)
        self.GeneralBox.append(self.TimeBox)
        # Adding items to TimeBox
        self.TimeBox.append(self.buttonSetTime)
        self.TimeBox.append(self.entryTime)
        # Adding items to KeyBox
        self.KeyBox.append(self.buttonActivar)
        self.KeyBox.append(self.buttonSetKey)
        self.KeyBox.append(self.entryKey)
        # Setting Child of the ApplicationWindow
        self.set_child(self.GeneralBox)
        # Setting Signals
        self.buttonSetTime.connect('clicked',self.on_button_SetTime_Clicked)
        self.buttonActivar.connect('clicked',self.on_button_ActivarDesactivar_clicked)
        self.buttonSetKey.connect('clicked', self.on_button_SetKey_Clicked)
        # Setting Dark Theme
        self.set_dark_theme_Using_Adw_StyleManager()


    def tapping_key(self):
        keyboard = Controller()
        while self.AutoKeyActivated:
            time.sleep(self.Time)
            if not self.AutoKeyActivated:
                break
            keyboard.press(self.Key)
            time.sleep(0.5)
            keyboard.release(self.Key)
    def on_button_ActivarDesactivar_clicked(self, button):
        self.AutoKeyActivated = not self.AutoKeyActivated
        if self.AutoKeyActivated:
            thread_tapping_key = threading.Thread(target=self.tapping_key)
            thread_tapping_key.start()
            button.set_label("Desactivar")
        else:
            button.set_label("Activar")


    def on_button_SetKey_Clicked(self, button):
        key = self.entryKey.get_text()
        self.Key = key

    def on_button_SetTime_Clicked(self, button):
        timeInterval = self.entryTime.get_text()
        self.Time = float(timeInterval)
        print(self.Time)

    def set_dark_theme_Using_Adw_StyleManager(self):
        manager = Adw.StyleManager.get_default()
        manager.set_color_scheme(Adw.ColorScheme.FORCE_DARK)

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="Gtk.AutoKeyTapApplication")
app.run(sys.argv)