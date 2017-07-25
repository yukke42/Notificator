#!/usr/bin/python3
import os
import requests
import argparse
import subprocess
from configparser import SafeConfigParser
import logging
from logging import getLogger, DEBUG

class Notificator:
    def __init__(self):
        path_to_dir = os.path.dirname(os.path.realpath(__file__))
        logger.debug("path to the directory the file exists." + path_to_dir)

        config = SafeConfigParser()
        config.read(path_to_dir + '/config.ini')
        self.slack_web_api = config['slack_config']['slack_web_api']


    def execute_command(self, command):
        """
        @param command(str): got on the command line
        """
        process = subprocess.run(command, shell=True, executable='/bin/bash')
        if process.returncode == 0:
            status_msg = "Done successfully."
        else:
            status_msg = "Error occurred."

        logger.debug(status_msg)
        return status_msg


    def post_message(self, channel, username, status_msg):

        to_user = "@" + username if username != '' else ''

        msg_to_post = to_user + "\n```{cmd}```\n{msg}".format(
            cmd=command,
            msg=status_msg
        )

        slack_config = {
            'token': self.slack_web_api,
            'text': msg_to_post,
            'channel': channel,
            'username': 'Notificator',
            'link_names': 1
        }

        URL = 'https://slack.com/api/chat.postMessage'
        requests.post(URL, data=slack_config)



if __name__ == "__main__":
    fmt = "%(levelname)s %(name)s %(funcName)s:%(message)s"
    logging.basicConfig(format=fmt)
    logger = getLogger(__name__)

    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description='Post a message on slack after the command exits.')
    parser.add_argument("command", help="enclose command in double quotes")
    parser.add_argument("--debug", action='store_true', default=False, help="print log to debug")
    parser.add_argument("-c", "--channel", default='general', help="the destination channel[default: general]")
    parser.add_argument("-u", "--user", default='', help="the username of receiving a message[default: Nobody]")
    arg = parser.parse_args()

    command = arg.command
    channel = arg.channel
    username = arg.user
    logger.debug(command)
    logger.debug(channel)
    logger.debug(username)

    if arg.debug == True:
        logger.setLevel(DEBUG)


    notificator = Notificator()
    status_msg = notificator.execute_command(command)
    notificator.post_message(channel, username, status_msg)
