from pwd import getpwnam
import os
import subprocess

from mycroft.util.log import LOG
from mycroft.skills.core import MycroftSkill
from adapt.intent import IntentBuilder


def set_user(uid, gid):
    LOG.info('Setting group and user to ' + str(gid) + ':' + str(uid))
    os.setgid(gid)
    os.setuid(uid)


class CmdSkill(MycroftSkill):
    def __init__(self):
        super(CmdSkill, self).__init__('CmdSkill')
        self.uid = None
        self.gid = None
        self.alias = {}

    def get_config(self, key):
        print(self.settings)
        return (self.settings.get(key) or
                self.config_core.get('CmdSkill', {}).get(key))

    def initialize(self):
        user = self.get_config('user')
        if user:
            pwnam = getpwnam(user)
            self.uid = pwnam.pw_uid
            self.gid = pwnam.pw_gid
        self.alias = self.get_config('alias') or {}

        for alias in self.alias:
            print("adding {}".format("alias"))
            self.register_vocabulary(alias, 'Script')

        intent = IntentBuilder('RunScriptCommandIntent')\
            .require('Script').require('Run').build()
        self.register_intent(intent, self.run)

        self.bus.on('CmdSkillRun', self.run)

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
            self.log.debug('Could not run script ' + script, exc_info=True)


def create_skill():
    return CmdSkill()
