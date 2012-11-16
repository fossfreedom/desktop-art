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

GConf_plugin_path = '/apps/rhythmbox/plugins/desktop-art/'

defaults = {'roundness'            : 0.3,
            'background_color'     : '#0000000000004ccc',
            'text_color'           : '#ffffffffffffb332',
            'text_shadow_color'    : '#000000000000b332',
            'draw_reflection'      : True,
            'window_x'             : 50,
            'window_y'             : Gdk.Screen.height() - 190 - 40,
            'window_w'             : Gdk.Screen.width() - 100,
            'window_h'             : 190,
            'text_position'        : 'se',
            'blur'                 : 1,
            'reflection_height'    : 0.4,
            'reflection_intensity' : 0.4,
            'hover_size'           : 0.7,
            'border'               : 0.06,
            'text_font'            : 'Normal'}

def GConf_path(key):
    return '%s%s' % (GConf_plugin_path, key)

gc = GConf.Client.get_default()

for key, val in defaults.items():
    path = GConf_path(key)
    if gc.get_without_default(path) == None:
        if isinstance(val, bool):
            gc.set_bool(path, val)
        elif isinstance(val, int):
            gc.set_int(path, val)
        elif isinstance(val, float):
            gc.set_float(path, val)
        elif isinstance(val, str):
            gc.set_string(path, val)
        else:
            print 'Datatype %s is not supported' % type(val)
