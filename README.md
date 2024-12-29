# SeterraVibrationSupport
Adds vibration support to seterra (geoguesser version) for controllers.

Uses node.js, tampermonkey, and python

showcase: https://cdn.discordapp.com/attachments/1290687009777778810/1322727554292912158/IMG_0275.mov?ex=6771ed88&is=67709c08&hm=ad210885ab43ad855b4ce5dec6f8fdf0160cd5eb1bbda623cf97f0b3c84353ff&

Officially permited for speedruns

![image](https://github.com/user-attachments/assets/ebd08120-311d-45fe-a633-5b73806d6123)

# Requirements
Python version compatible with evdev
python libraries: evdev

Node.js
Tested on node.js 22.12.0 but others should work.
  you will also need ws: a Node.js WebSocket library (npm install ws)

Tampermonkey addon for your browser.
  I have not tested other monkeys.

# Usage.

Source code is the release.

Download the scripts, and save them to a folder. (make sure they are all* in the same directory)

1. In tampermonkey, import the seterrahapticfeedbacktampermonkeyscript.txt
    you can do this by either creating a new script and pasting the full contents in or clicking  utilities -> import from file
  If you desire a different port to be used by the seterra vibration server, you will need to specify it in both the server.js file and the tampermonkey script.
2. CD into your directory of downloaded scripts in a terminal.
3. run the server.js with "node server.js"
4. Enable the tamper monkey script and go onto any seterra (geoguesser version) page.
5. Your controller should vibrate on every element correctly clicked and upon reset.
