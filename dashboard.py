#!/usr/bin/env python3
__author__ = 'chapeter@cisco.com'

import nxostools
import yaml
import feeds


cfgFile = open('devices.cfg', 'r')
devicelist = yaml.load(cfgFile)



def build_devicecache():
    devicecache = {}
    for x in devicelist['lab']:
        ip = devicelist['lab'][x]['host']
        user = devicelist['lab'][x]['user']
        password = devicelist['lab'][x]['pass']
        id = devicelist['lab'][x]['id']
        if devicelist['lab'][x]['type'] == 'nexus9000' or devicelist['lab'][x]['type'] == 'nexus3000':
            version = nxostools.showver(ip, user, password)
            uptime = nxostools.getuptime(ip, user, password)
            if devicelist['lab'][x]['type'] == 'nexus3000':
                latestversion = feeds.get_code3000()
            else:
                latestversion = feeds.get_code()

        else:
            version = "%s dashboard in progress" % (devicelist['lab'][x]['type'])
            uptime = "%s dashboard in progress" % (devicelist['lab'][x]['type'])
            latestversion = "LATEST RELEASE HERE"


        devicecache[id] = {}
        devicecache[id]['id'] = id
        devicecache[id]['ip'] = ip
        devicecache[id]['user'] = user
        devicecache[id]['pass'] = password
        devicecache[id]['uptime'] = uptime
        devicecache[id]['runversion'] = version
        devicecache[id]['latestversion'] = latestversion

    return devicecache






