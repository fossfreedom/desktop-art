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

from __future__ import division

def roundedrec(cc, x, y, w, h, r):
    r = min(1,r)
    r = r * 0.7 * min(w, h)
    cc.move_to(x+r,y)
    cc.line_to(x+w-r,y)
    cc.curve_to(x+w,y,x+w,y,x+w,y+r)
    cc.line_to(x+w,y+h-r)
    cc.curve_to(x+w,y+h,x+w,y+h,x+w-r,y+h)
    cc.line_to(x+r,y+h)
    cc.curve_to(x,y+h,x,y+h,x,y+h-r)
    cc.line_to(x,y+r)
    cc.curve_to(x,y,x,y,x+r,y)
