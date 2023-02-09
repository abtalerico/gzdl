import os
import gi
from gzdl.model import GzdlModel


gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if os.path.isfile("gzdl.ini"):
            gzdl_model = GzdlModel.from_config("gzdl.ini")
        else:
            gzdl_model = GzdlModel()

        hb = Adw.HeaderBar()
        launch_button = Gtk.Button()
        launch_button.set_label("Launch")
        launch_button.get_style_context().add_class("suggested-action")

        hb.pack_start(launch_button)
        self.set_titlebar(hb)

        grid = Gtk.Grid()
        label = Gtk.Label()
        label.set_label("gzdoom Path:")
        grid.attach(label, 0, 0, 1, 1)
        gz_path_entry_buffer = Gtk.EntryBuffer()
        gz_path_entry_buffer.set_text(gzdl_model.gzdoom_path, len(gzdl_model.gzdoom_path))
        gz_path_entry = Gtk.Entry()
        gz_path_entry.set_buffer(gz_path_entry_buffer)
        grid.attach_next_to(gz_path_entry, label, Gtk.PositionType.RIGHT, 1, 1)

        iwad_section_label = Gtk.Label()
        iwad_section_label.set_label("Select IWAD")
        grid.attach(iwad_section_label, 0, 1, 1, 1)

        iwad_dir_label = Gtk.Label()
        iwad_dir_label.set_label("IWAD Directory:")
        grid.attach(iwad_dir_label, 0, 2, 1, 1)
        iwad_entry_buffer = Gtk.EntryBuffer()
        iwad_entry_buffer.set_text(gzdl_model.iwad_directory, len(gzdl_model.iwad_directory))
        iwad_entry = Gtk.Entry()
        iwad_entry.set_buffer(iwad_entry_buffer)
        grid.attach_next_to(iwad_entry, iwad_dir_label, Gtk.PositionType.RIGHT, 1, 1)


        iwad_list = Gtk.ListBox()
        iwad_label = Gtk.Label()
        iwad_label.set_label("IWADS GO HERE")
        iwad_label2 = Gtk.Label()
        iwad_label2.set_label("IWADS GO HERE")
        iwad_list.append(iwad_label)
        iwad_list.append(iwad_label2)

        grid.attach(iwad_list, 0, 3, 3, 3)

        self.set_child(grid)


class GzdlApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app, title="GZDL")
        self.win.present()
