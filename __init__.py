import sys
from os.path import dirname, abspath, basename
import subprocess

from mycroft.skills.core import MycroftSkill
from adapt.intent import IntentBuilder
from mycroft.messagebus.message import Message


import time
from time import mktime

from pwd import getpwnam
import os
from os.path import dirname
from mycroft.util.log import getLogger

sys.path.append(abspath(dirname(__file__)))

logger = getLogger(abspath(__file__).split('/')[-2])
__author__ = 'forslund'

def set_user(uid, gid):
    logger.info('Setting group and user to ' + str(gid) + ':' + str(uid))
    os.setgid(gid)
    os.setuid(uid)

class CmdSkill(MycroftSkill):
    def __init__(self):
        super(CmdSkill, self).__init__('CmdSkill')
        self.uid = None
        self.gid = None
        self.alias = {}
        if self.config:
            user = self.config.get('user')
            if user:
                pwnam = getpwnam(user)
                self.uid = pwnam.pw_uid
                self.gid = pwnam.pw_gid
            self.alias = self.config.get('alias', {})

    def initialize(self):
        self.load_data_files(dirname(__file__))

        intent = IntentBuilder('RunScriptCommandIntent')\
                 .require('Script')\
                 .build()
        self.register_intent(intent, self.run)

        self.emitter.on('CmdSkillRun', self.run)
    
    def run(self, message):
        script = message.data.get('Script')
        script = self.alias.get(script, script)
        args = script.split(' ')
        try:
            if self.uid and self.gid:
                p = subprocess.Popen(args,
                                     preexec_fn=set_user(self.uid, self.gid))
            else:
                p = subprocess.Popen(args)
        except:
            logger.debug('Could not run script ' + script, exc_info=True)

def create_skill():
    return CmdSkill()
