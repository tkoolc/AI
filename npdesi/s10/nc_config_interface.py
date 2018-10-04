#!/usr/bin/env python

from ncclient import manager

if __name__ == '__main__':

    with manager.connect(host='nxosv', port=22, username='cisco', password='cisco',
                         hostkey_verify=False, device_params={'name': 'nexus'},
                         allow_agent=False, look_for_keys=False) as device:

        commands = ['config t', 'interface Ethernet2/6', 'switchport', 'description Configured by Python ncclient']
        nc_config_reply = device.exec_command(commands)
        print nc_config_reply.xml
