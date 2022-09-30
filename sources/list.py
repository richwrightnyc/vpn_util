"""
This module is a component of the VPN Util command line tool, and is not intended to be a standalone package. This software is provided "as-is", with no warranties or guarantees of any kind

Copyright (c) 2022 HudsonOnHere
Released under the MIT License
"""

import json
import subprocess


def list_available_PPP_connections():
    cmd               = '/usr/sbin/system_profiler SPNetworkDataType -json'
    cmd_output        = subprocess.check_output(cmd, shell=True).decode()
    SPNetworkDataType = json.loads(cmd_output)
    SPNetworkDataType = SPNetworkDataType["SPNetworkDataType"]

    print(f"Available VPN Connections:")
    print(f"-------------------------", "\n")

    for i in range(len(SPNetworkDataType)):
        for k in SPNetworkDataType[i]:
            if k == "IPv4":
                if SPNetworkDataType[i][k]["ConfigMethod"] == "PPP":

                    print(f"""   Name: {SPNetworkDataType[i]["_name"]}""")
                    print(f"""   Type: {SPNetworkDataType[i]["type"]}""")
                    print('\n')