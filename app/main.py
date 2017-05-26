import sys

from lib import FaceChecker, Options, Config


if __name__ == '__main__':
    config = Config().getConfig()

    options = Options(config)
    opts = options.parse(sys.argv[1:])

    fc = FaceChecker(opts, config)

    fc.start()
    #v.print_example_arg()
