"""
This module is a component of the VPN Util command line tool, and is not intended to be a standalone package. This software is provided "as-is", with no warranties or guarantees of any kind

Copyright (c) 2022 HudsonOnHere
Released under the MIT License
"""

import json
import subprocess


def get_status(is_connected):

    if is_connected == True:

        cmd               = '/usr/sbin/system_profiler SPNetworkDataType -json'
        cmd_output        = subprocess.check_output(cmd, shell=True).decode()
        SPNetworkDataType = json.loads(cmd_output)
        SPNetworkDataType = SPNetworkDataType["SPNetworkDataType"]

        for i in range(len(SPNetworkDataType)):
            for k in SPNetworkDataType[i]:

                if SPNetworkDataType[i][k] == "ppp0":

                    name      = SPNetworkDataType[i]["_name"]
                    interface = SPNetworkDataType[i]["interface"]
                    ipaddr    = SPNetworkDataType[i]["ip_address"][0]
                    protocol  = SPNetworkDataType[i]["type"]

        print(f"Active VPN Connection:")
        print(f"----------------------", "\n")
        print(f"        Name: {name}")
        print(f"   Interface: {interface}")
        print(f"          IP: {ipaddr}")
        print(f"        Type: {protocol}\n")

    elif is_connected == False:
        print(f"Active VPN Connections:")
        print(f"-----------------------", "\n")
        print(f"   Disconnected\n")