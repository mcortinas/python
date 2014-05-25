#!/usr/bin/python
import os
import re
import subprocess
import logging
import optparse

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

def main():
    usage = "usage: %prog [options]"
    parser = optparse.OptionParser(usage)
    parser.add_option("-o", "--opt1", dest="opt1",
                    action="opt1",
                    default=False,
                    help="Little comment about opt1")
    options, args = parser.parse_args()

    if not options.opt1 and not options.opt1:
        parser.error('Must choose one-- try --opt1 or -o')
    
    ##SWITCH OPTION
    if options.opt1:
        logging.info('opt1 selected')
    
def call_command(command):
    process = subprocess.Popen(command.split(' '),
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    return process.communicate()
if __name__ == "__main__":
    main()
