#!/usr/bin/python3
import requests
import sys, subprocess
from configparser import SafeConfigParser
import logging
from logging import getLogger,StreamHandler,DEBUG, INFO

DEBUG_MODE = 10
INFO_MODE  = 20

class Notificator:
    def __init__(self):
        config = SafeConfigParser()
        config.read('config.ini')
        self.slack_web_api        = config['slack_config']['slack_web_api']
        self.channel_name         = config['slack_config']['channel_name']
        self.user_to_be_mentioned = config['slack_config']['user_to_be_mentioned']

        self.parse_argments()
        self.execute_the_command()
        self.post_message()


    def parse_argments(self):
        """
        引数から実行するコマンド、コマンドの引数を取得
        """
        argc = len(sys.argv)
        if argc < 2:
            print("Usage: notificate COMMAND")
            sys.exit(1)

        self.command  = sys.argv[1]
        self.argments = " ".join(sys.argv[2:])
        logger.debug(self.command)
        logger.debug(self.argments)


    def execute_the_command(self):
        """
        コマンドを実行し、終了ステータスによりメッセージを作成
        """
        cmd = "{cmd} {args}".format(cmd=self.command, args=self.argments)
        process = subprocess.run(cmd, shell=True, executable='/bin/bash')

        if process.returncode == 0:
            status_msg = "Done successfully."
        else:
            status_msg = "Error occurred."

        self.msg_to_post = "@{user} {cmd} {msg}".format(
            user=self.user_to_be_mentioned,
            cmd=self.command,
            msg=status_msg
        )
        logger.debug(self.msg_to_post)


    def post_message(self):
        """
        メッセージを送信
        """
        slack_config = {
            'token': self.slack_web_api,
            'text': self.msg_to_post,
            'channel': self.channel_name,
            'username': 'Notificator',
            'link_names': 1
        }

        URL = 'https://slack.com/api/chat.postMessage'
        requests.post(URL, data=slack_config)


if __name__ == "__main__":
    fmt = "%(levelname)s %(name)s %(funcName)s:%(message)s"
    logging.basicConfig(format=fmt)
    logger = getLogger(__name__)

    # logger.setLevel(DEBUG_MODE)

    logger.debug("DEBUG MODE")

    Notificator()
