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



def getinterfaceerrors(ip, user, password):
    url = 'http://%s/ins' % (ip)
    type = "cli_show"
    command = "show interface counters errors"
    output = "json"

    raw_data = send_command(url, user, password, type, command, output)

    return raw_data


def gettotalerrors(ip, user, password):
    raw_errors = getinterfaceerrors(ip, user, password)
    raw_errors = json.dumps(raw_errors, indent=2)

    str_errors = (str(raw_errors))
    error_count = 0
    #print(str_errors)

    for x in str_errors.splitlines(keepends=False):
        if "eth_giants" in x or "eth_inmacrx_err" in x or "eth_inmactx_err" in x or "eth_deferred_tx" in x or "eth_symbol_err" in x or "eth_align_error" in x or "eth_rcv_err" in x or "eth_fcs_err" in x or "eth_xmit_err" in x or "eth_undersize" in x or "eth_outdisc" in x or "eth_runts" in x or "eth_carri_sen" in x or "eth_excess_col" in x or "eth_multi_col" in x or "eth_late_col" in x or "eth_single_col" in x:
            #print(x)
            y = x.split(": ", 1)[1]
            #print(y)
            #print(y.split(",", 1)[0])
            error_count += int(y.split(",", 1)[0])
    return(error_count)




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

