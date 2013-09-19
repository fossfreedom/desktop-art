# -*- Mode: python; coding: utf-8; tab-width: 4; indent-tabs-mode: nil; -*-
#
# IMPORTANT - WHILST THIS MODULE IS USED BY SEVERAL OTHER PLUGINS
# THE MASTER AND MOST UP-TO-DATE IS FOUND IN THE COVERART BROWSER
# PLUGIN - https://github.com/fossfreedom/coverart-browser
# PLEASE SUBMIT CHANGES BACK TO HELP EXPAND THIS API
#
# Copyright (C) 2012 - fossfreedom
# Copyright (C) 2012 - Agustin Carrasco
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301  USA.

from gi.repository import Gtk
from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import RB
import sys
import rb

def pygobject_version():
    ''' 
    returns float of the major and minor parts of a pygobject version 
    e.g. version (3, 9, 5) return float(3.9)
    '''
    to_number = lambda t: ".".join(str(v) for v in t)
    
    str_version = to_number(GObject.pygobject_version)
    
    return float(str_version.rsplit('.',1)[0])

PYVER = sys.version_info[0]

if PYVER >= 3:
    import urllib.request, urllib.parse, urllib.error
else:
    import urllib
    from urlparse import urlparse as rb2urlparse

if PYVER >= 3:
    import http.client
else:
    import httplib
    
def responses():
    if PYVER >=3:
        return http.client.responses
    else:
        return httplib.responses

def unicodestr(param, charset):
    if PYVER >=3:
        return param#str(param, charset)
    else:
        return unicode(param, charset)
        
def unicodeencode(param, charset):
    if PYVER >=3:
        return param#str(param).encode(charset)
    else:
        return unicode(param).encode(charset)
        
def unicodedecode(param, charset):
    if PYVER >=3:
        return param
    else:
        return param.decode(charset)

def urlparse(uri):
    if PYVER >=3:
        return urllib.parse.urlparse(uri)
    else:
        return rb2urlparse(uri)
        
def url2pathname(url):
    if PYVER >=3:
        return urllib.request.url2pathname(url)
    else:
        return urllib.url2pathname(url)

def urlopen(filename):
    if PYVER >=3:
        return urllib.request.urlopen(filename)
    else:
        return urllib.urlopen(filename)
        
def pathname2url(filename):
    if PYVER >=3:
        return urllib.request.pathname2url(filename)
    else:
        return urllib.pathname2url(filename)

def unquote(uri):
    if PYVER >=3:
        return urllib.parse.unquote(uri)
    else:
        return urllib.unquote(uri)
                
def quote(uri, safe=None):
    if PYVER >=3:
        if safe:
            return urllib.parse.quote(uri,safe=safe)
        else:
            return urllib.parse.quote(uri)
    else:
        if safe:
            return urllib.quote(uri, safe=safe)
        else:
            return urllib.quote(uri)
        
def quote_plus(uri):
    if PYVER >=3:
        return urllib.parse.quote_plus(uri)
    else:
        return urllib.quote_plus(uri)

def is_rb3(*args):
    if hasattr(RB.Shell.props, 'ui_manager'):
        return False
    else:
        return True 
        


