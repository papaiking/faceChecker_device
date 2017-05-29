"""
@Author: Thuc VX<vxthuc@labsofthings.com>
@ORG: labsofthings.com
@date: 27 May 2017

Purpose: This package parse running parameters and dave into option object.
"""

from argparse import ArgumentParser


class Options:

    def __init__(self, config):
        self.config = config
        self._init_parser()

    def _init_parser(self):
        usage = 'bin/facechecker -f frequency -i idle_time'
        self.parser = ArgumentParser(usage=usage)
        self.parser.add_argument('-c',
                                 '--checking', type=int,
                                 default=self.config['DEFAULT'].getint('CHECKING_INTERVAL'),
                                 dest='checking_interval',
                                 help='Option for time interval (in second) between two face checkings')

        self.parser.add_argument('-i',
                                 '--idle', type=int,
                                 default=self.config['DEFAULT'].getint('IDLE_INTERVAL'),
                                 dest='idle_internal',
                                 help='Option for idle time interval between founded event and next face checking')

    def parse(self, args=None):
        return self.parser.parse_args(args)
