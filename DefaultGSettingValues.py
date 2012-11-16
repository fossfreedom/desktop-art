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

from gi.repository import Gdk, Gio

gsetting_plugin_path = 'org.gnome.rhythmbox.plugins.desktop_art'

defaults = {'roundness'            : 0.3,
            'background-color'     : '#0000000000004ccc',
            'text-color'           : '#ffffffffffffb332',
            'text-shadow-color'    : '#000000000000b332',
            'draw-reflection'      : True,
            'window-x'             : 50,
            'window-y'             : Gdk.Screen.height() - 190 - 40,
            'window-w'             : Gdk.Screen.width() - 100,
            'window-h'             : 190,
            'text-position'        : 'se',
            'blur'                 : 1,
            'reflection-height'    : 0.4,
            'reflection-intensity' : 0.4,
            'hover-size'           : 0.7,
            'border'               : 0.06,
            'text-font'            : 'Normal'}

def gsetting():
    return Gio.Settings(gsetting_plugin_path)

def gsetting_path(key):
    setting = gsetting()
    return setting[key] #'%s%s' % (gsetting_plugin_path, key)

def gsetting_defaults():
    setting = gsetting()
    if setting['window-y'] == -1:
        setting['window-y'] = defaults['window-y']
        
    if setting['window-w'] == -1:
        setting['window-w'] = defaults['window-w']

#gc = GConf.Client.get_default()

#for key, val in defaults.items():
#path = GConf_path(key)
#if gc.get_without_default(path) == None:
#        if isinstance(val, bool):
#            gc.set_bool(path, val)
#        elif isinstance(val, int):
#            gc.set_int(path, val)
#        elif isinstance(val, float):
#            gc.set_float(path, val)
#        elif isinstance(val, str):
#            gc.set_string(path, val)
#        else:
#            print 'Datatype %s is not supported' % type(val)
