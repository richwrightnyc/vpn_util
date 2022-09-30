"""
This module is a component of the VPN Util command line tool, and is not intended to be a standalone package. This software is provided "as-is", with no warranties or guarantees of any kind

Copyright (c) 2022 HudsonOnHere
Released under the MIT License
"""


import subprocess

def disconnect(vpn_name):

    cmd = f"scutil --nc stop {vpn_name}"
    subprocess.check_output(cmd, shell=True).decode()