import sys, argparse
import ipaddress

def checkIP(ip):
    arr = ["173.245.48.0/20",
            "103.21.244.0/22",
            "103.22.200.0/22",
            "103.31.4.0/22",
            "141.101.64.0/18",
            "108.162.192.0/18",
            "190.93.240.0/20",
            "188.114.96.0/20",
            "197.234.240.0/22",
            "198.41.128.0/17",
            "162.158.0.0/15",
            "104.16.0.0/12",
            "172.64.0.0/13",
            "131.0.72.0/22"]

    for ip_range in arr:
        if ipaddress.ip_address(ip) in ipaddress.ip_network(ip_range):
            return True
            break

def init_argparse():
    parser = argparse.ArgumentParser(description='Print non CF IPs')
    parser.add_argument('-i','--inputfile', type=argparse.FileType('r', encoding='UTF-8'), required=True, help='Input file')
    return parser

def main():
    parser = init_argparse()
    args = parser.parse_args()
    f = open(args.inputfile.name, "r")
    for i in f:
        i = i.rstrip()
        if checkIP(i) == True:
            print(i)
    args.inputfile.close()

if (__name__ == "__main__"):
   main()
