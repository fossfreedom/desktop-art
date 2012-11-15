desktop-art
===========

rhythmbox v2.9x plugin to display the coverart and control rhythmbox from your desktop

Current Situation

 - Basics do work
 - Right-click preference menu option to be ported to GTK3
 - Window background is not transparant - no clue yet how to do this. Patches welcome!

To Install

<pre>
sudo apt-get install gir1.2-gconf-2.0 gir1.2-rsvg-2.0
cd ~/.local/share/rhythmbox/plugins
git clone https://fossfreedom/desktop-art.git
</pre>

i.e. use the equivalent package names `gir1.2-gconf-2.0 gir1.2-rsvg-2.0` for your distro

Enable the plugin in rhythmbox