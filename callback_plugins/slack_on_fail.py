# (C) 2014-2015, Matt Martz <matt@sivel.net>
# (C) 2017 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''

'''

import json
import os
import uuid

try:
    from __main__ import cli
except ImportError:
    cli = None

from ansible.module_utils.urls import open_url
from ansible.plugins.callback import CallbackBase
from ansible.utils.display import Display

display = Display()


class CallbackModule(CallbackBase):
    """This is an ansible callback plugin that sends status
    updates to a Slack channel on playbook failure.
    """
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'notification'
    CALLBACK_NAME = 'slack_on_fail'
    CALLBACK_NEEDS_WHITELIST = False

    def __init__(self, display=None):

        super(CallbackModule, self).__init__(display=display)

    def v2_playbook_on_play_start(self, play):
        """Parse out extra_vars to be used to for dynamically assigning 
        slack configuration"""
        self.play = play
        self.extra_vars = self.play.get_variable_manager().extra_vars
        #display.vvvv(self.extra_vars)
        #display.vvvv('Job ID:')
        display.vvvv(os.environ)
