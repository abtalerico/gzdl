import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        hb = Adw.HeaderBar()
        launch_button = Gtk.Button()
        launch_button.set_label("Launch")
        launch_button.get_style_context().add_class(Gtk.STYLE_CLASS_SUGGESTED_ACTION)

        hb.pack_start(launch_button)
        self.set_titlebar(hb)

class GzdlApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app, title="GZDL")
        self.win.present()
