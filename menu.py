import argparse
import textwrap

def menu():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-a', '--app', help=textwrap.dedent('''\
        Select one of the following "APP":
            lUDP: Starts UDP listener
                -t Sets the socket timeout
            sUDP: Sends UDP data
    '''))
    parser.add_argument('-t', help='Set timeout for listeners')
    args = parser.parse_args()
    return args