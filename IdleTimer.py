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

#
# Thanks to Thomas Perl for the xlib magic:
# http://thpinfo.com/2007/09/x11-idle-time-and-focused-window-in.html
#

import ctypes
import os

class XScreenSaverInfo(ctypes.Structure):
  _fields_ = [('window',      ctypes.c_ulong), # screen saver window
              ('state',       ctypes.c_int),   # off,on,disabled
              ('kind',        ctypes.c_int),   # blanked,internal,external
              ('since',       ctypes.c_ulong), # milliseconds
              ('idle',        ctypes.c_ulong), # milliseconds
              ('event_mask',  ctypes.c_ulong)] # events
  
class IdleTimer():
  def __init__(self):
    self.xlib = ctypes.cdll.LoadLibrary('libX11.so')
    self.dpy = self.xlib.XOpenDisplay(os.environ['DISPLAY'])
    self.root = self.xlib.XDefaultRootWindow(self.dpy)
    self.xss = ctypes.cdll.LoadLibrary('libXss.so')
    self.xss.XScreenSaverAllocInfo.restype = ctypes.POINTER(XScreenSaverInfo)
    self.xss_info = self.xss.XScreenSaverAllocInfo()

  def getIdleTime(self):
    self.xss.XScreenSaverQueryInfo(self.dpy, self.root, self.xss_info)
    return self.xss_info.contents.idle

if __name__== '__main__':
  it = IdleTimer()
  while True:
    print it.getIdleTime()
