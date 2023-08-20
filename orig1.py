#    def on_join(self, join_info):     #ORIGINAL
#
#        _user = self.users.add(join_info)
#        if _user.account:
#            tc_info = apis.tinychat.user_info(_user.account)
#
#            if tc_info is not None:
#                _user.tinychat_id = tc_info['tinychat_id']
#                _user.last_login = tc_info['last_active']
#
#            if _user.is_owner:
#                _user.user_level = 1
#                self.console_write(COLOR['red'], 'Room owner: %s:%s:%s' %
#                                   (_user.nick, _user.id, _user.account))
#
#            elif _user.is_mod:
#                _user.user_level = 3
#                self.console_write(COLOR['bright_red'], 'Moderator: %s:%s:%s' %
#                                   (_user.nick, _user.id, _user.account))
#            else:
#                self.console_write(COLOR['bright_yellow'], '%s:%s has account: %s' %
#                                   (_user.nick, _user.id, _user.account))
#        else:
#            self.console_write(COLOR['cyan'], '%s:%s joined the room' % (_user.nick, _user.id))
