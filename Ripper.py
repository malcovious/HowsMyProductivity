sudo yum install autoconf automake intltool pkgconfig glib2 gtk2 dbus-glib xfconf gio2.0 libglade2 perl libwnck* gudev-1.0


IF(EndsWith([Coordinates Generated Id], “0”), Concat(Coordinates, “X”), Coordinates)

import time
import subprocess
import select

f = subprocess.Popen([‘tail’,‘-F’, “*”, filename],\
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
p = select.poll()
p.register(f.stdout)

while True:
    if p.poll(1):
        print f.stdout.readline()
        #if line = headers, break
        #divide line into an array using split
        #see if key is already in the processed keys list (we make)
        #if it isn’t, create the query and hit MSSQL
    time.sleep(1)
