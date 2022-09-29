"""
This module is a component of the VPN Util command line tool, and is not intended to be a standalone package. This software is provided "as-is", with no warranties or guarantees of any kind

Copyright (c) 2022 HudsonOnHere
Released under the MIT License
"""

import json
import subprocess
from vpn_check_connected import check_connected



def get_status():

    # connected         = False
    cmd               = '/usr/sbin/system_profiler SPNetworkDataType -json'
    cmd_output        = subprocess.check_output(cmd, shell=True).decode()
    SPNetworkDataType = json.loads(cmd_output)
    SPNetworkDataType = SPNetworkDataType["SPNetworkDataType"]
    # print(json.dumps(SPNetworkDataType["SPNetworkDataType"], indent=4))

    for i in range(len(SPNetworkDataType)):
        for k in SPNetworkDataType[i]:
            # print(SPNetworkDataType[i][k])
            # print(f"{k}: {SPNetworkDataType[i][k]}\n")

            if SPNetworkDataType[i][k] == "ppp0":
                # connected = True

                # print(json.dumps(SPNetworkDataType[i], indent=4))
                name      = SPNetworkDataType[i]["_name"]
                interface = SPNetworkDataType[i]["interface"]
                ipaddr    = SPNetworkDataType[i]["ip_address"][0]
                protocol  = SPNetworkDataType[i]["type"]


    # if connected == True:
    print(f"Active VPN Connection:")
    print(f"----------------------", "\n")
    print(f"        Name: {name}")
    print(f"   Interface: {interface}")
    print(f"          IP: {ipaddr}")
    print(f"        Type: {protocol}\n")
    # return True

    # elif connected == False:
    #     print(f"Active VPN Connections:")
    #     print(f"----------------------", "\n")
    #     print(f"   Disconnected\n")
    #     return False

    # else:
    #     print("Something else happened")
    #     return False


def validate_connection():

    if check_connected() == False:
            print(f"Active VPN Connections:")
            print(f"-----------------------", "\n")
            print(f"   Disconnected\n")

    elif check_connected() == True:
        get_status()


validate_connection()