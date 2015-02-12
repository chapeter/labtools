#!/usr/bin/env python3


# list of packages that should be imported for this code to work

import cgi
import yaml
import webtools3

def create():
    cfgFile = 'devices.cfg'
    f = open(cfgFile, 'r')

    devices = yaml.load(f)
    f.close()



    form   = cgi.FieldStorage()
    id = form.getfirst("id")
    ip  = form.getfirst("ip")
    username  = form.getfirst("username")
    password = form.getfirst("password")
    type = form.getfirst("type")
    #print("<br>Adding %s" % id)

    newdevice = {"id" : id, "host" : ip, "user" : username, "pass" : password, "type" : type}
    devices["lab"][id] = newdevice
    #print(devices)
    cfgFile = 'devices.cfg'
    f = open(cfgFile, 'w')
    f.write(yaml.dump(devices, default_flow_style=False))
    #print(yaml.dump(devices, default_flow_style=False))
    f.close()
    #
    #f.write('host : %s\n' % hostname )
    #f.write('name : %s\n' % username)
    #f.write('passwd : %s\n' % password)
    #f.close()



webtools3.HTMLHeader()
create()
print('''
<a href="webdashboard.py">dashboard</a><br>
<a href="configure.html">Add another Device</a>
''')
webtools3.HTMLFooter()

