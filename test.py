#!/usr/bin/python

import logging
import optparse

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

def main():
    logging.info('Start python Script')
    logging.info('End python Script')
    
if __name__ == "__main__":
    main()
