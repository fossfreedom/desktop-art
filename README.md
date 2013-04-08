desktop-art
===========

rhythmbox v2.9x plugin to display the coverart and control rhythmbox from your desktop

[![Flattr Button](http://api.flattr.com/button/button-static-50x60.png "Flattr This!")](https://flattr.com/thing/1237263/fossfreedomdesktop-art-on-GitHub "Rhythmbox Desktop Art")

![Imgur](http://i.imgur.com/Kj1JL.png)

... and on mouse-over...

![Imgur](http://i.imgur.com/mq3TT.png)

Current Situation

 - Basics do work - see To Do list below
 - Mouse focus control to be restricted to cover i.e. lines 276-284 commented out needs to be GTK3 converted.  Patches welcome!

To Install

<pre>
sudo apt-get install gir1.2-gconf-2.0 gir1.2-rsvg-2.0
cd ~/.local/share/rhythmbox/plugins
git clone https://fossfreedom/desktop-art.git
</pre>

i.e. use the equivalent package names `gir1.2-gconf-2.0 gir1.2-rsvg-2.0` for your distro

Enable the plugin in rhythmbox

To Do:

**patches welcome**

 - code cleanup - remove various gnome2 bits such as the path `~/.gnome2/rhythmbox/covers/` in CoverManager.py
 - GConf needs to be converted to GSettings
 - is the rsvg module really needed?  Need to investigate further and if necessary strip the rsvg code elemnents from the source.
 - Investigate the 1 second polling method to update the cover. Inefficient - possible use the standard playing-changed event to upate.
 - Preferences Dialog - two or more increments to the x, y, w or h values causes a segmentation fault.
 
 
 **Bug #1028115 in pygobject**
 
 To have full functionality, this bug needs to be fixed in the pygobject-Packages: 
 https://bugs.launchpad.net/ubuntu/+source/pygobject/+bug/1028115
 
 You can find scripts for Ubuntu 12.04/12.10 to patch the packages.
 If you're running Ubuntu 12.04/12.10 AMD64, you can download the
 resulting binaries as .deb packages.
 
 see https://github.com/andrenam/desktop-art/downloads
