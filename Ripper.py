sudo yum install autoconf automake intltool pkgconfig glib2 gtk2 dbus-glib xfconf gio2.0 libglade2 perl libwnck* gudev-1.0

IF(EndsWith([Coordinates Generated Id], “0”), Concat(Coordinates, “X”), Coordinates)

import time
import subprocess
import select

str toEnter
f = subprocess.Popen([‘tail’,‘-F’, “*”, filename],\
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
p = select.poll()
p.register(f.stdout)

while True:
    if p.poll(1):
        line = f.stdout.readline()
        if "Domain" and "timeSpent" and "key" not in line:
        # divide line into an array using split
            toEnter = line.split(',')
        # create the query and hit MSSQL
            INSERT INTO [HowsMyProductivity].[dbo].[TestTable] VALUES (toEnter[0],int(toEnter[1]),int(toEnter[2]));
    time.sleep(1)
