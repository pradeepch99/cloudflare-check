import sys, argparse
import ipaddress

def ipCheck(ips, ip_type):
    if ip_type == 'private':
        for i in ips:
            if ipaddress.ip_address(i.rstrip()).is_private:
                print(i.rstrip())
    elif ip_type == 'public':
        for i in ips:
            if ipaddress.ip_address(i.rstrip()).is_private == False:
                print(i.rstrip())

def main():
    parser = argparse.ArgumentParser(description='Print non CF IPs')
    parser.add_argument('-i','--inputfile', type=argparse.FileType('r', encoding='UTF-8'), required=False, help='Input file')
    parser.add_argument('-pr','--privateIp', action='store_true', required=False, help='Input file')
    parser.add_argument('-pub','--publicIp', action='store_true', required=False, help='Input file')
    args = parser.parse_args()
    f = open(args.inputfile.name, "r")
    if(args.privateIp == True and args.publicIp == False):
        ipCheck(f, 'private')
    else:
        ipCheck(f, 'public')

if (__name__ == "__main__"):
   main()
