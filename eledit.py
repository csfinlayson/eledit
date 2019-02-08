#!/usr/bin/python

import argparse
import re

def txtget(filename):
    # open file read-only, get file contents and close
    try:
        file = open(filename, 'r')
        file_contents = file.read()
        file.close()
    except:
        file_contents = 'Error reading file'
    return file_contents

def menu():
    parser = argparse.ArgumentParser(description='Easily edit an elasticsearch yml file')
    parser.add_argument('-f', action='store', dest='location', default='/etc/elasticsearch/elasticsearch.yml',
                        help='Location of elastic yml file to edit')
    parser.add_argument('-i', action='store', dest='ip', default='127.0.0.1', help='IP for elastic bind')
    parser.add_argument('-z', action='store', dest='node', default='127.0.0.1', help='Single IP for node discovery')
    parser.add_argument('-Z', action='store', dest='zen_location', help='Path to file with IPs for zen discovery')
    results = parser.parse_args()
    return results

def replace_ip(ipAddr, location):
    contents = txtget(location)
    modified = re.sub('#{0,1}network.host:[\d \.]*', 'network.host: '+ipAddr, contents)
    print(modified)

def main():
    results = menu()
    print(results.ip)
    replace_ip(results.ip, results.location)

if __name__ == "__main__":
    main()