"""
This module is a component of the VPN Util command line tool, and is not intended to be a standalone package. This software is provided "as-is", with no warranties or guarantees of any kind

Copyright (c) 2022 HudsonOnHere
Released under the MIT License
"""

import subprocess


class ConnectionError(Exception):
    pass


def check_connected():
    
    cmd = 'ifconfig | grep ppp0 &> /dev/null'
    cmd_exit_code = subprocess.call(cmd, shell=True)

    if cmd_exit_code == 0:
        return True

    elif cmd_exit_code == 1:
        return False

    else:
        raise ConnectionError("Unable to determine connection status")