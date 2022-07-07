#! /bin/bash

readonly arg="${1}"
readonly FILE=/usr/local/bin/vpn
readonly SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
readonly version="0.1"


err() {

    # Simple error handler
    # Writes all input to stderr

    echo "$*" >&2
}


usage() {

    echo "VPN Util Setup Tool, Version: $version"
    echo
    echo "USAGE: $0 [flag...] (-h|-i|-u)"
    echo
    echo "      -h | --help         Print this message"
    echo "      -i | --install      Install VPN util"
    echo "      -u | --uninstall    Uninstall VPN util"
    echo

}


checkInstalled() {

    # Check to see if the binary is already in /usr/local/bin
    # returns 1 if true, returns 0 if false
    # anything else throws an exception

    if test -f "$FILE"; then
        return 1

    elif test ! -f "$FILE"; then
        return 0

    else
        err "ERROR: Unhandled exception occured"
        exit 1

    fi
}


install() {

    # Checks if binary is already in /usr/local/bin
    # If not, copies it there

    if checkInstalled; then
      
        cd $SCRIPT_DIR && cp ../bin/vpn $FILE
        echo "$0: vpn has been installed to $FILE successfully."
        exit 0


    elif ! checkInstalled; then

        err "$0: ERROR: vpn is already installed at $FILE"
        exit 1

    fi
}


uninstall() {

    # Checks if binary is in /usr/local/bin
    # If true, prompts user to delete it

    if ! checkInstalled; then

        rm -i $FILE
        echo "$0: vpn has been uninstalled successfully."
        exit 0

    elif checkInstalled; then

        err "$0: ERROR: vpn is not installed, nothing to uninstall."
        exit 1

    fi
}


validateArg() {

    # Ensures at least 1 argument has been passed

    if [[ -z "${arg}" ]]; then
    
        echo "$0: Invalid argument, run '$0 --help' to see example usage."
        echo
        err "ERROR: $0 expected at least 1 argument, but $# were given."
        exit 1

    fi
}


main() {

    # Input is validated
    # After all checks passed runs specified function

    validateArg

    case "${arg}" in

        -h | --help)
            usage
            exit 0
            ;;
        
        -i | --install)
            install
            ;;
        
        -u | --uninstall)
            uninstall
            ;;
        
        *)
            echo "$0: Invalid argument '${arg}', see usage for available commands."
            echo
            err "ERROR: Unrecognized command '${arg}', run '$0 --help' for help."
            exit 1
            ;;

    esac
}

main "${@}"