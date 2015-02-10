#!/usr/bin/env python3
__author__ = 'chapeter@cisco.com'

import requests
import json


def showver(ip, user, password):
    url = 'http://%s/ins' % (ip)
    type = "cli_show"
    command = "show ver"
    output = "json"

    raw_data = send_command(url, user, password, type, command, output)

    return (raw_data['ins_api']['outputs']['output']['body']['kickstart_ver_str'])


def getuptime(ip, user, password):
    url = 'http://%s/ins' % (ip)
    type = "cli_show"
    command = "show ver"
    output = "json"

    raw_data = send_command(url, user, password, type, command, output)

    uptime2 = raw_data['ins_api']['outputs']['output']['body']['kern_uptm_days'], "days", raw_data['ins_api']['outputs']['output']['body']['kern_uptm_hrs'],"hrs", raw_data['ins_api']['outputs']['output']['body']['kern_uptm_mins'],"min", raw_data['ins_api']['outputs']['output']['body']['kern_uptm_secs'], "sec"

    uptime = "%s days %s hours %s min %s sec" % (raw_data['ins_api']['outputs']['output']['body']['kern_uptm_days'], raw_data['ins_api']['outputs']['output']['body']['kern_uptm_hrs'], raw_data['ins_api']['outputs']['output']['body']['kern_uptm_mins'],raw_data['ins_api']['outputs']['output']['body']['kern_uptm_secs'])
    return uptime




#def showiparp(ip, user, password, targetip, vrf):
#    url = 'http://%s/ins' % (ip)
#    type = "cli_show"
#    command = "show ip arp %s vrf %s" % (targetip, vrf)
#    output = "json"

#    raw_data = send_command(url, user, password, type, command, output)


def send_command(url, user, password, type, myinput, output):
    myheaders={'content-type':'application/json'}
    payload={
        "ins_api": {
            "version": "1.0",
            "type": type,
            "chunk": "0",
            "sid": "1",
            "input": myinput,
            "output_format": output
        }
    }
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(user,password)).json()
    return response


#print(showver("10.94.238.75","admin","cisco"))

