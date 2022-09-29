"""
This module is a component of the VPN Util command line tool, and is not intended to be a standalone package. This software is provided "as-is", with no warranties or guarantees of any kind

Copyright (c) 2022 HudsonOnHere
Released under the MIT License
"""

import json
import subprocess

# connected         = False
cmd               = '/usr/sbin/system_profiler SPNetworkDataType -json'
cmd_output        = subprocess.check_output(cmd, shell=True).decode()
SPNetworkDataType = json.loads(cmd_output)
SPNetworkDataType = SPNetworkDataType["SPNetworkDataType"]

# print(json.dumps(SPNetworkDataType[7]["IPv4"]["ConfigMethod"], indent=4))

def list_available_PPP_connections():
    print(f"Available VPN Connections:")
    print(f"-------------------------", "\n")

    for i in range(len(SPNetworkDataType)):
        for k in SPNetworkDataType[i]:
            if k == "IPv4":
                if SPNetworkDataType[i][k]["ConfigMethod"] == "PPP":
                    # print(json.dumps(SPNetworkDataType[i], indent=4)) #debug

                    print(f"""   Name: {SPNetworkDataType[i]["_name"]}""")
                    print(f"""   Type: {SPNetworkDataType[i]["type"]}""")
                    print('\n')


list_available_PPP_connections()

# active_int = subprocess.check_output("scutil --nwi | grep "Network interfaces" | awk '{print $3}'", shell=True).decode()

# print(active_int)
# def list_current_PPP_connections():
