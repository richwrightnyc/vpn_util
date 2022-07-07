# VPN Util

## A lightweight utility to quickly manage your VPN connections

### Setup

***Some assembly required*** -- In it's current state, the vpn connection names in `scripts/vpn.sh` are labeled according to my own. You'll have to modify them to match the vpn connection names on your local machine. Change the values of `personal` and `work` inside the `validateName()` function to achieve this. ***This step is necessary in order to run the script properly on your local machine.***

Once that script is configured you should be able to run it.

I recommend recompiling the script into the executable binary that will be installed to `/usr/local/bin`. If you don't already know about it, take a look at [neurobin/shc](https://github.com/neurobin/shc), it's a fantastic tool that can be used to acheive this.

Once recompiled, store the binary in the `vpn_util/bin` directory, be sure to name it `vpn`.

### Installation

After configuring the above, you can run `scripts/setup.sh` to install `vpn`.

1. Clone this repo and `cd` into it.
2. run `scripts/setup.sh --install` to install the binary to you /usr/local/bin
    * verify installation by running `vpn --help`
3. run `vpn list` to see available vpn connections
4. manage your VPN connections quickly from your terminal :)

### Uninstall

If this tool isn't for you, you can use the `setup.sh` script to uninstall it.

1. Run `scripts/setup.sh --uninstall` to remove the compiled binary from your `/usr/local/bin` directory.
    * if you did not compile the script, or if you named it something else, the uninstall will not complete successfully
    * If this is the case for you, you can simply remove it from you `/usr/local/bin`.