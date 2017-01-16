#!/usr/bin/env python
"""Subnet Calculator
"""

import random
import sys


def subnet_calc():
    ip_address = get_ipaddress()

    if ip_address is None:
        raise IOError

    subnet_mask = get_subnetmasks()

    if subnet_mask is None:
        raise IOError

    print ip_address
    print subnet_mask


def get_ipaddress():
    # Request user to provide IP address
    ip_address = raw_input("Enter an IP address: ")

    # Split IP address into list of octets
    octets = ip_address.split('.')

    # Validating IP address
    # 1. There should be 4 octets in an IP address
    # 2. 1st Octet should be between 1 and 223,
    #    because if it is greater than 224 then it's a multicast or
    #    experimental address
    # 3. 1st Octet should not be 127 because it is a loopback interface
    # 4. 1st Octet and 2nd Octet should not be 169 or 254 because it refers to
    #    DHCP address
    # 5. All octets should be greater than 0 and less than 255
    #    and greater than or equal to previous octet
    if not ((len(octets) == 4) and
            (1 <= int(octets[0]) <= 223) and
            (int(octets[0]) != 127) and
            (int(octets[0]) != 169 or int(octets[1]) != 254) and
            ((0 <= int(octets[1]) <= 255 and
              0 <= int(octets[2]) <= 255 and
              0 <= int(octets[3]) <= 255))):
        print "\nThe IP address is INVALID! Please retry!\n"
        return None

    return ip_address


def get_subnetmasks():
    masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]

    # Checking Subnet Mask validity
    subnet_mask = raw_input("Enter a subnet mask: ")

    # Checking octets
    octets = subnet_mask.split('.')

    oct1 = int(octets[0])
    oct2 = int(octets[1])
    oct3 = int(octets[2])
    oct4 = int(octets[3])

    if not ((len(octets) == 4) and
            (oct1 == 255) and
            (oct2 in masks) and
            (oct3 in masks) and
            (oct4 in masks) and
            (oct1 >= oct2 >= oct3 >= oct4)):
        print "\nThe subnet mask is INVALID! Please retry!\n"
        return None

    return subnet_mask


if __name__ == "__main__":
    subnet_calc()
