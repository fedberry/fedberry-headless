# Fedberry-headless
Headless mode is a system configuration which enables access to FedBerry (at first boot) using ssh from another computer on a network. When this feature is enabled, the initial-setup service is bypassed and disabled.

## Enable Headless mode
1) After copying Fedberry to your SD card, mount the /boot partition and create a text file called `headless` or `headless.txt` (if using Windows).

2) If your RPi requires a static IP Address, add the following lines to your /boot/headless config file:
```
IPADDR=<Required RPi static IP address>
NETMASK=<Network subnet mask>
GATEWAY=<Router/gateway IP address>
```
  For example:
```
IPADDR=192.168.1.20
NETMASK=255.255.255.0
GATEWAY=192.168.1.1
```

3) Unmount your SD card and use it to boot Fedberry in headless mode.
