from netmiko import ConnectHandler
import re
import sys

## dev = Cisco device connection 
## ip_find = IP address
## return = Returns MAC address for specified IP address

def cisco_arp_to_mac(dev, ip_find):
    try:

        ## Regex term
        search_term = '\w*\s*(\d+\.\d+.\d+.\d+)\s*(-|\d+)\s*(.{14})\s*ARPA\s*(.*)'

        ## Run show arp command
        output = dev.send_command("show arp  "+ ip_find)
        output = output.split('\n')

        ## Search for MAC address
        for search in output:
            result = re.match(search_term, search)
            if result:
                mac_has = result.group(3).split('.')
                mac_has = ''.join(mac_has)
                mac_has = ':'.join(format(s, '02x') for s in bytes.fromhex(mac_has))    
            else:
                mac_has = 'MAC not found'
       
        return(mac_has)
        
    except Exception as err: 
        print(err)
        sys.exit(1)

## dev = Cisco device connection 
## return = Returns running-config      

def cisco_get_config(dev):
    try:
        
        ## Run show running-config
        output = dev.send_command("show running-config")

        return(output)

    except Exception as err: 
        print(err)
        sys.exit(1)