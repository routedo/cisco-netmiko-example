"""
This example shows how to use netmiko to query the ARP table and running config of a cisco device.
"""

import sys
from getpass import getpass
from netmiko import ConnectHandler
from csconnect import cisco_arp_to_mac
from csconnect import cisco_get_config

def main():
    """ Example """
    try:
        ## Login credentials
        username = input("Cisco username: ")
        passwd = getpass('Enter Cisco Password: ')

        ## Network device IP address
        dev_ip = '10.10.10.11'

        ## Specify IP address to find
        arp_to_find = '1.1.1.1'

        ## Location to store config
        config_location = 'config/cisco.conf'

        ## Create ssh connection to Cisco device
        dev_connect = ConnectHandler(device_type='cisco_ios', ip=dev_ip, username=username, password=passwd)

        ## Find MAC address of IP address
        mac_addr = cisco_arp_to_mac(dev_connect, arp_to_find)

        ## Pull running config from network device
        config_save = cisco_get_config(dev_connect)

        ## Write running config to file
        with open(config_location, 'w') as f:
            for line in config_save:
                f.write(line)

        print('\n MAC address for IP : ' + arp_to_find + ' is ' + mac_addr)

        ## Disconnect from device
        dev_connect.disconnect()

    except Exception as err:
        print(err)
        sys.exit(1)

if __name__ == '__main__':
    main()
