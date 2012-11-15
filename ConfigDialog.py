# -*- coding: utf-8 -*-
#
# This file is part of the Rhythmbox Desktop Art plug-in
#
# Copyright © 2008 Mathias Nedrebø < mathias at nedrebo dot org >
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from gi.repository import Gtk, GConf, Gdk
import rb

widget_names = ['main_area',
                'roundness',
                'background_color', 'text_color', 'text_shadow_color',
                'draw_reflection',
                'window_x', 'window_y', 'window_w', 'window_h',
                'text_position_nw', 'text_position_ne', 'text_position_sw', 'text_position_se']

class ConfigDialog(Gtk.Dialog):
    def __init__(self, glade_file, GConf_plugin_path, desktop_control, plugin):
        Gtk.Dialog.__init__(self, buttons=(Gtk.STOCK_OK, Gtk.ResponseType.ACCEPT))
        self.set_title("Desktop Art preferences")
        #self.set_has_separator(False)

        self.connect("response", lambda w, e: w.hide())
        #self.connect("response", lambda w, e: self.desktop_control.set_draw_border(False))

        self.gc = GConf.Client.get_default()
        self.GConf_plugin_path = GConf_plugin_path
        self.desktop_control = desktop_control
        self.plugin = plugin
        
        self.widgets = {}
        self.get_widgets(self.widgets, glade_file)
        self.set_callbacks(self.widgets)

        self.vbox.add(self.widgets['main_area'])
        self.widgets['main_area'].set_border_width(6)
        
        self.set_resizable(False)

    def get_widgets(self, w, glade_file):
        ui  = Gtk.Builder()
        ui.add_from_file(rb.find_plugin_file(self.plugin, glade_file))
        for name in widget_names:
            w[name] = ui.get_object(name)

    def present(self):
        #self.desktop_control.set_draw_border(True)
        self.get_GConf_values(self.widgets)

    def run(self):
        self.present()
        self.show_all()

    def get_GConf_values(self, w):
        for name in widget_names:
            if isinstance(w[name], Gtk.SpinButton):
                if w[name].get_digits() == 0:
                    value = self.gc.get_int(self.GConf_path(name))
                else:
                    value = self.gc.get_float(self.GConf_path(name))
                if value:
                    w[name].set_value(value)
            elif isinstance(w[name], Gtk.RadioButton):
                key, val = name.rsplit('_', 1)
                w[name].set_active(self.gc.get_string(self.GConf_path(key)) == val)
            elif isinstance(w[name], Gtk.CheckButton):
                value = self.gc.get_without_default(self.GConf_path(name))
                if value:
                    w[name].set_active(value.get_bool())
                else:
                    w[name].set_active(True)
            elif isinstance(w[name], Gtk.ColorButton):
                rgba = self.gc.get_string(self.GConf_path(name))
                _, color = Gdk.Color.parse( rgba[:-4] )
                a = int(rgba[-4:], 16)
                w[name].set_color(color)  
                w[name].set_alpha(a)    

    def set_GConf_value(self, w, key):
        if isinstance(w, Gtk.SpinButton):
            if w.get_digits() == 0:
                self.gc.set_int(self.GConf_path(key), int(w.get_value()))
            else:
                self.gc.set_float(self.GConf_path(key), w.get_value())
        elif isinstance(w, Gtk.RadioButton):
            if w.get_active():
                key, val = key.rsplit('_', 1)
                self.gc.set_string(self.GConf_path(key), val)
        elif isinstance(w, Gtk.CheckButton):
            self.gc.set_bool(self.GConf_path(key), int(w.get_active()))
        elif isinstance(w, Gtk.ColorButton):
            self.gc.set_string(self.GConf_path(key),
                               '%s%s' % (w.get_color().to_string(), hex(w.get_alpha())[2:]))

    def set_callbacks(self, w):
        for name in widget_names:
            if isinstance(w[name], Gtk.SpinButton):
                w[name].connect('value-changed', self.set_GConf_value, name)
            elif isinstance(w[name], Gtk.CheckButton) or isinstance(w[name], Gtk.RadioButton):
                w[name].connect('toggled', self.set_GConf_value, name)
            elif isinstance(w[name], Gtk.ColorButton):
                w[name].connect('color-set', self.set_GConf_value, name)

    def GConf_path(self, key):
        return '%s/%s' % (self.GConf_plugin_path, key)
