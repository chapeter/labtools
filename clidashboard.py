#!/usr/bin/env python3
__author__ = 'chapeter@cisco.com'
import dashboard
def cli_display():
    print('{0:15} {1:14} {2:6} {3:6} {4:30} {5:12} {6:10}'.format("Device Name", "IP address", "User", "Pass", "Uptime", "Version", "Latest Release"))
    devicecache = dashboard.build_devicecache()
    for x in devicecache:
        print('{0:15} {1:14} {2:6} {3:6} {4:30} {5:12} {6:10}'.format(devicecache[x]['id'],devicecache[x]['ip'],devicecache[x]['user'], devicecache[x]['pass'],devicecache[x]['uptime'],devicecache[x]['runversion'],devicecache[x]['latestversion']))

cli_display()