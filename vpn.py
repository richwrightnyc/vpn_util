"""
VPN Util command line tool

Copyright (c) 2022 HudsonOnHere
Released under the MIT License

This software is provided "as-is", with no warranties or guarantees of any kind.
"""

import argparse

from sources import check_connected
from sources import list
from sources import status
from sources import connect
from sources import disconnect

is_connected = check_connected.check_connected()


parser = argparse.ArgumentParser()
parser.add_argument('-c', '--connect', type=str, help="Use this flag to connect", required=False)
parser.add_argument('-d', '--disconnect', type=str, help="Use this flag to disconnect", required=False)
parser.add_argument('-l', '--list', help="List available VPN connections", action='store_true', required=False)
parser.add_argument('-s', '--status', help="Show VPN status", action='store_true', required=False)

args = parser.parse_args()

if args.list:
    list.list_available_PPP_connections()

if args.status:
    status.get_status(is_connected)

if args.connect:
    connect.connect(vpn_name=args.connect)

if args.disconnect:
    disconnect.disconnect(vpn_name=args.disconnect)