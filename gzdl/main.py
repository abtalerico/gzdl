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
            self.gzdl_model = GzdlModel.from_config("gzdl.ini")
        else:
            self.gzdl_model = GzdlModel()
        self.gzdl_model.load_iwads()

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
        gz_path_entry_buffer.set_text(self.gzdl_model.gzdoom_path, len(self.gzdl_model.gzdoom_path))
        gz_path_entry = Gtk.Entry()
        gz_path_entry.set_buffer(gz_path_entry_buffer)
        grid.attach_next_to(gz_path_entry, label, Gtk.PositionType.RIGHT, 2, 1)
        gz_path_button = Gtk.Button()
        gz_path_button.set_label("Set gzdoom Path")
        grid.attach_next_to(gz_path_button, gz_path_entry, Gtk.PositionType.RIGHT, 1, 1)

        iwad_section_label = Gtk.Label()
        iwad_section_label.set_label("Select IWAD")
        grid.attach(iwad_section_label, 0, 1, 1, 1)

        iwad_dir_label = Gtk.Label()
        iwad_dir_label.set_label("IWAD Directory:")
        grid.attach(iwad_dir_label, 0, 2, 1, 1)
        iwad_entry_buffer = Gtk.EntryBuffer()
        iwad_entry_buffer.set_text(self.gzdl_model.iwad_directory, len(self.gzdl_model.iwad_directory))
        iwad_entry = Gtk.Entry()
        iwad_entry.set_buffer(iwad_entry_buffer)
        grid.attach_next_to(iwad_entry, iwad_dir_label, Gtk.PositionType.RIGHT, 2, 1)
        iwad_path_button = Gtk.Button()
        iwad_path_button.set_label("Set IWAD Path")
        grid.attach_next_to(iwad_path_button, iwad_entry, Gtk.PositionType.RIGHT, 1, 1)

        iwad_list = Gtk.ListBox()
        for iwad in self.gzdl_model.available_iwads:
            iwad_label = Gtk.Label()
            iwad_label.set_label(iwad["filename"])
            iwad_list.append(iwad_label)
        grid.attach(iwad_list, 0, 3, 4, 4)

        command_line_label = Gtk.Label()
        command_line_label.set_text("Command Line:")
        command_line_entry_buffer = Gtk.EntryBuffer()
        command_line_entry_buffer.set_text("to implement", len("to implement"))
        command_line_entry = Gtk.Entry()
        command_line_entry.set_buffer(command_line_entry_buffer)
        grid.attach(command_line_label, 0, 7, 1, 1)
        grid.attach_next_to(command_line_entry, command_line_label, Gtk.PositionType.RIGHT, 1, 2)

        self.set_child(grid)
        self.connect("destroy", self.on_destroy)

    def on_destroy(self, widget):
        self.gzdl_model.write_config()

class GzdlApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app, title="GZDL")
        self.win.present()
