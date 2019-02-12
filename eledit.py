#!/usr/bin/python

import argparse
import re


def txtget(filename):
    """Opens a file at the location specified by filename. Reads and returns the contents of said file.  
    Also backs up the file to a location given by filename.cal.  Returns 'Error reading file' for exception
    """
    try:
        # Open the file in read-only mode, read it and close
        file = open(filename, 'r')
        file_contents = file.read()
        file.close()
        # Write to the filename.cal, just a backup
        wr = open(filename + '.cal', 'w')
        wr.write(file_contents)
        wr.close()
    except:
        file_contents = 'Error reading file'
    return file_contents

def writefile(filename, content):
    """Writes the content to a specified file name"""
    try:
        file = open(filename, 'w')
        file.write(content)
        file.close()
    except:
        print("Oops, something went wrong!")


def menu():
    """Provides the functionality for a command line menu using argparse. Returns the parsed arguments"""
    parser = argparse.ArgumentParser(description='Easily edit an elasticsearch yml file')
    parser.add_argument('-f', action='store', dest='location', default='/etc/elasticsearch/elasticsearch.yml',
                        help='Location of elastic yml file to edit')
    parser.add_argument('-i', action='store', dest='ip', help='IP for elastic bind')
    parser.add_argument('-z', action='store', dest='node', default='127.0.0.1', help='Single IP for node discovery')
    parser.add_argument('-Z', action='store', dest='zen_location', help='Path to file with IPs for zen discovery')
    results = parser.parse_args()
    return results

def replace_ip(ipAddr):
    """Replaces the network host IP Address in the elastic yaml file"""
    modified = re.sub('#{0,1}network.host:[\d \.]*', 'network.host: '+ipAddr, contents)
    return modified

def main():
    """Calls various other functions as specified in the menu arguments"""
    results = menu()
    contents = txtget(results.location)
    if results.ip:
        replace_ip(results.ip)

if __name__ == "__main__":
    main()