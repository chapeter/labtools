#!/usr/bin/env python3
__author__ = 'chapeter@cisco.com'

import nxostools
import yaml
import feeds


cfgFile = open('devices.cfg', 'r')
devicelist = yaml.load(cfgFile)



def build_devicecache():
    devicecache = {}
    latest3000 = feeds.get_code3000()
    latest9000 = feeds.get_code()
    for x in devicelist['lab']:
        ip = devicelist['lab'][x]['host']
        user = devicelist['lab'][x]['user']
        password = devicelist['lab'][x]['pass']
        id = devicelist['lab'][x]['id']
        total_errors = nxostools.gettotalerrors(ip, user, password)
        if devicelist['lab'][x]['type'] == 'nexus9000' or devicelist['lab'][x]['type'] == 'nexus3000':
            version = nxostools.showver(ip, user, password)
            uptime = nxostools.getuptime(ip, user, password)
            if devicelist['lab'][x]['type'] == 'nexus9000':
                latestversion = latest9000
            else:
                latestversion = latest3000

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
        devicecache[id]['totalerrors'] = total_errors

    return devicecache






