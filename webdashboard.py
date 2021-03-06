#!/usr/bin/env python3
__author__ = 'chapeter@cisco.com'

import dashboard
import webtools3

def dict_to_table():
    devicecache = dashboard.build_devicecache()
    print('<table border="1">')
    print("<tr><th>Device Name</th><th>IP Address</th><th>User</th><th>Pass</th><th>Uptime</th><th>Version</th><th>Latest Release</th><th>Total Errors</th><th>Total TCNs</th><th>Last TCN</th></tr>")
    for host in devicecache:
        print("<tr>")
        print(maketd(devicecache[host]["id"]),maketd(devicecache[host]["ip"]),maketd(devicecache[host]["user"]),maketd(devicecache[host]["pass"]),maketd(devicecache[host]["uptime"]),maketd(devicecache[host]["runversion"]),maketd(devicecache[host]["latestversion"]),maketd(devicecache[host]["totalerrors"]),maketd(devicecache[host]["totaltcn"]),maketd(devicecache[host]["lasttcn"]))
        print("</tr>")
    print("</table>")


#def maketr(data):
#    data = "<tr>%s</td>" % (data)
#    return data

def maketd(data):
    data = "<td>%s</td>" % (data)
    return data

webtools3.HTMLHeader()
dict_to_table()
print('''
<a href="configure.html">Add another device</a>
<a href="webdashboard.html">Web Dashboard</a>
''')
webtools3.HTMLFooter()

