#!/usr/bin/env python


def main():
    config = {}
    execfile("project.conf", config)
    print config["value1"]
    print "Main function ran"


if __name__ == "__main__":
    main()