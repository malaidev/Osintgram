#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Osintgram import Osintgram
import argparse
from src import printcolors as pc
import sys


def printlogo():
    pc.printout("________         .__        __                               \n", pc.YELLOW)
    pc.printout("\_____  \   _____|__| _____/  |_  ________________    _____  \n", pc.YELLOW)
    pc.printout(" /   |   \ /  ___/  |/    \   __\/ ___\_  __ \__  \  /     \ \n", pc.YELLOW)
    pc.printout("/    |    \\\___ \|  |   |  \  | / /_/  >  | \// __ \|  Y Y  \\\n", pc.YELLOW)
    pc.printout("\_______  /____  >__|___|  /__| \___  /|__|  (____  /__|_|  /\n", pc.YELLOW)
    pc.printout("        \/     \/        \/    /_____/            \/      \/ \n", pc.YELLOW)
    print('\n')
    pc.printout("Version 0.6 - Developed by Giuseppe Criscione - 2019\n\n", pc.YELLOW)
    pc.printout("Type 'list' to show all allowed commands\n")
    pc.printout("Type 'FILE=y' to save results to files like '<target username>_<command>.txt (deafult is disabled)'\n")
    pc.printout("Type 'FILE=n' to disable saving to files'\n")
    pc.printout("Type 'JSON=y' to export results to a JSON files like '<target username>_<command>.json (deafult is "
                "disabled)'\n")
    pc.printout("Type 'JSON=n' to disable exporting to files'\n")


def cmdlist():
    pc.printout("FILE=y/n\t")
    print("Enable/disable output in a '<target username>_<command>.txt' file'")
    pc.printout("JSON=y/n\t")
    print("Enable/disable export in a '<target username>_<command>.json' file'")
    pc.printout("addrs\t\t")
    print("Get all registered addressed by target photos")
    pc.printout("captions\t")
    print("Get target's photos captions")
    pc.printout("comments\t")
    print("Get total comments of target's posts")
    pc.printout("followers\t")
    print("Get target followers")
    pc.printout("followings\t")
    print("Get users followed by target")
    pc.printout("hashtags\t")
    print("Get hashtags used by target")
    pc.printout("info\t\t")
    print("Get target info")
    pc.printout("likes\t\t")
    print("Get total likes of target's posts")
    pc.printout("mediatype\t")
    print("Get target's posts type (photo or video)")
    pc.printout("photodes\t")
    print("Get description of target's photos")
    pc.printout("photos\t\t")
    print("Download target's photos in output folder")
    pc.printout("propic\t\t")
    print("Download target's profile picture")
    pc.printout("stories\t\t")
    print("Download target's sories")
    pc.printout("tagged\t\t")
    print("Get list of users tagged by target")
    pc.printout("target\t\t")
    print("Set new target")

printlogo()

parser = argparse.ArgumentParser(description='Osintgram is a OSINT tool on Instagram. It offers an interactive shell to perform analysis on Instagram account of any users by its nickname ')
parser.add_argument('id', type=str,  # var = id
                    help='username')
parser.add_argument('-j', '--json', help='save commands output as JSON file', action='store_true')
parser.add_argument('-f', '--file', help='save output in a file', action='store_true')

args = parser.parse_args()

api = Osintgram(args.id, args.file, args.json)

while True:
    pc.printout("Run a command: ", pc.YELLOW)
    cmd = input()
    if cmd == "quit" or cmd == "exit":
        pc.printout("Goodbye!\n", pc.RED)
        sys.exit(0)
    elif cmd == "list" or cmd == "help":
        cmdlist()
    elif cmd == "addrs":
        api.getAddrs()
    elif cmd == "captions":
        api.getCaptions()
    elif cmd == "comments":
        api.getTotalComments()
    elif cmd == "followers":
        api.getFollowers()
    elif cmd == "followings":
        api.getFollowings()
    elif cmd == "hashtags":
        api.getHashtags()
    elif cmd == "info":
        api.getUserInfo()
    elif cmd == "likes":
        api.getTotalLikes()
    elif cmd == "mediatype":
        api.getMediaType()
    elif cmd == "photodes":
        api.getPhotoDescription()
    elif cmd == "photos":
        api.getUserPhoto()
    elif cmd == "propic":
        api.getUserPropic()
    elif cmd == "stories":
        api.getUserStories()
    elif cmd == "tagged":
        api.getPeopleTaggedByUser()
    elif cmd == "target":
        api.changeTarget()
    elif cmd == "FILE=y":
        api.setWriteFile(True)
    elif cmd == "FILE=n":
        api.setWriteFile(False)
    elif cmd == "JSON=y":
        api.setJsonDump(True)
    elif cmd == "JSON=n":
        api.setJsonDump(False)
    else:
        pc.printout("Unknown command\n", pc.RED)
