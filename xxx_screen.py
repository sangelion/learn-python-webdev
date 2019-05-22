#!/usr/bin/env python

import argparse
import difflib
import logging
import multiprocessing
import os, sys
from screenutils import list_screens, Screen
import shutil
import subprocess
import time


SCRIPT_DIR = os.getcwd()
LOG_DIR = SCRIPT_DIR + '/logs'

FILENAME = os.path.splitext(os.path.basename(__file__))[0]
SCREENLOG = 'screenlog.0'
FILELOG = LOG_DIR + '/' + 'xxx_update_log' + '.log'
SESSION = 'xxx'

class xxxSession(object):

    def __init__(self, session_name):
        if session_name == None:
            self.session_name = 'xxx'
        else:
            self.session_name = session_name


    def start_session(self):
        # check if the session already exist
        if self.check_session():
            self.kill_session()
            
        # remove the log
        log_exists = os.path.isfile(SCREENLOG)

        # before remove make sure gnu-screen list is empty
        # TODO

        if log_exists:
            os.system('rm -rf ' + SCREENLOG)
        else:
            pass

        time.sleep(0.5)
        # start screen session and put into detach mode
        multiprocessing.Process(target=self.detach_session).start()
        os.system('screen -UR -L -S ' + self.session_name)


    def detach_session(self):
        time.sleep(5)
        os.system("screen -d " + self.session_name)


    def kill_session(self):
        Screen(self.session_name).kill()

    def check_session(self):
        return Screen(self.session_name).exists


    def execute(self):
        pass

def update_log():
    try:
        os.makedirs(LOG_DIR)
    except xxxrror:
        pass
    shutil.copyfile(SCREENLOG, FILELOG)

def compare_changes():
    before = open(SCREENLOG, 'r') 
    after = open(FILELOG, 'r')

    lines1 = before.readlines()
    lines2 = after.readlines()

    diff = difflib.unified_diff(lines2, lines1)
    lines = list(diff)[2:]
    added = [line[1:] for line in lines if line[0] == '+']
    res = str("".join(added))
    return res


def parse_arguments():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.fromfile_prefix_chars = "+"

    parser.add_argument_group("To use run below commands in the simics host",
                                            """
Example:
    $ sudo screen -L -S xxx /dev/ttyUSB0 115200   
    Then:  
        The default log will be created eg: screenlog.0
        To have the log timestamp of before and after are needed for log comparison
        Steps:
            1. update the log
            2. execute the commandline to screen session
            3. compare changes
    """)
    parser.add_argument("-session", nargs="?", const="")
    parser.add_argument("-cs", "--check_session", nargs=1,
            help="TODO check_session")
    parser.add_argument("-start", "--start_session",action='store_true',
            help="TODO start_session")
    parser.add_argument("-exec", "--execute", nargs=1,
            help="TODO execute")
    parser.add_argument("-ul", "--update_log", nargs=1,
            help="TODO update log")
    parser.add_argument("-cmp", "--compare", nargs=1,
            help="TODO compare changes")
    return parser.parse_args()


def main(args=None):
    # start_time = time.time()
    
    print(type(list_screens()))
    
    # if os.getenv("USER") == "root":
    #     options = parse_arguments()
    #     xxx = xxxSession(options.session)

    #     if options.start_session:
    #         xxx.start_session()
    # else:
    #     print "Please run as root (with sudo)"

    # duration = time.time() - start_time


if __name__ == "__main__":
    sys.exit(main())