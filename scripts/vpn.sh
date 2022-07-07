#! /bin/bash

readonly cmd="${1}"
readonly vpnType="${2}"
readonly version="0.1"

err() {
    
    # Simple error handler
    # Writes all input to stderr

    echo "$*" >&2
}


usage() {

    echo "VPN Util Version $version - A lightweight utility for quick access to VPN settings."
    echo
    echo "USAGE: $0 [command...] (connect|disconnect|list) [vpn...] (personal|work)"
    echo
    echo "      -h | --help         Print this message"
    echo
    echo "      Example:            '$0 connect personal'"
    echo

}


validateCmd() {

    # Validate Argument 1 - Command
    # Verifies at least 1 argument is given, errors out if not.
    # Validates input in case statement below

    if [[ -z "${cmd}" ]]; then
        echo "$0: Invalid argument, run '$0 --help' to see example usage."
        echo
        err "ERROR: $0 expected at least 1 argument, but $# were given."
        exit 1
    fi

}


validateName() {

    # Validate Argument 2 - VPN
    # Verifies that a 2nd argument is given, converts to actual connection name.
    
    if [[ -z "${vpnType}" ]]; then
        usage
        exit 1
    fi

    if [[ "${vpnType}" == "personal" ]]; then
        vpn="PrivateVPN"
    elif [[ "${vpnType}" == "work" ]]; then
        vpn="G1H VPN"
    else
        echo "$0: Invalid argument '${vpnType}', choose from available VPN types (personal or work)."
        echo
        err "ERROR: Unrecognized VPN type, specify VPN type as the second argument"
        exit 1
    fi
}



checkStatus() {

    # validate connection status
    # returns 1 for active connection, 0 for inactive connection

    if [ "$(scutil --nc status "${vpn}" | head -1)" == "Disconnected" ]; then
        return 0
    elif [ "$(scutil --nc status "${vpn}" | head -1)" == "Connected" ]; then
        return 1
    fi

}



listStatus() {

    # show me what I can use

    scutil --nc list
}


connect() {

    # Check if VPN is already connected
    # If validation passes, connect specified service

    if ! checkStatus; then
            err "ERROR: '${vpn}' is already connected, run '$0 list' to check connections."
            exit 1
    fi

    networksetup -connectpppoeservice "${vpn}"
}


disconnect() {

    # Check if VPN is disconnected
    # Disconnects if valid

    if checkStatus; then
        err "ERROR: '${vpn}' is already disconnected, run '$0 list' to check connections."
        exit 1
    fi

    scutil --nc stop "${vpn}"
}


main() {

    # Validate 1st argument against list of available commands
    # If it checks out, run the operation
    # Anything else not outlined will throw an exception.

    validateCmd

    case "${cmd}" in
        connect)
            validateName
            connect "${vpn}"
            ;;
        disconnect)
            validateName
            disconnect "${vpn}"
            ;;
        list)
            listStatus
            exit 0
            ;;
        -h | --help)
            usage
            exit 0
            ;;
        *)
            echo "$0: Invalid argument '${cmd}', see usage for available commands."
            echo
            err "ERROR: Unrecognized command '${cmd}', run '$0 --help' for help."
            exit 1
            ;;
    esac
}

main "${@}"