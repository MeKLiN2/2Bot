    def nigtimer(self):
        self.send_chat_msg('testing bot')
        #self.send_chat_msg('Anti-Nigger Defense System Activated.')
        #time.sleep(1 * 5)
        #self.send_chat_msg('Preparing Nigger Detection Sensors...')
        #time.sleep(1 * 3)
        #self.send_chat_msg('Powering on Lethal Force Nigger Kill Bot 1.0...')
        #time.sleep(1 * 3)
        #self.send_chat_msg('Nigger Kill Bot MODE: [INTERROGATE]')
        time.sleep(1 * 3)
        question = input("your question")
        if question == ("yes")
            self.send_chat_msg('Are you a nigger?')
           "1" in msg:
            sleep(randint(1,2))
            self.send_chat_msg("%s has admitted to being a nigger. Checking intelligence level for Slavery Services Vocational Aptitude Battery (SSVAB)" % self.active_user.nick)
            self.send_chat_msg('!acc kan %s' % self.active_user.account)
        elif "no" in msg:
            sleep(randint(1,2))
            self.send_chat_msg("%s must prove they are not a nigger by answering a White Security Question" % self.active_user.nick)
            sleep(randint(1,2))
            self.send_chat_msg('If you are traveling 60 Miles per Hour, how long does it take to travel one mile?)')
            sleep(randint(10,15))
            self.send_chat_msg('!acc kan %s' % self.active_user.account)




----------------------------------------------------

    def check_msg(self, msg):
        should_be_banned = False
        chat_words = msg.split(' ')
        for bad in pinylib.CONFIG.B_NIGWORDS:
            if bad.startswith('*'):
                _ = bad.replace('*', '')
                if _ in msg:
                    should_be_banned = True
            elif bad in chat_words:
                should_be_banned = True
        if should_be_banned:
            if pinylib.CONFIG.B_USE_KICK_AS_AUTOBAN:
                self.send_kick_msg(self.active_user.id)
            else:
                self.send_ban_msg(self.active_user.id)

----------------------------------------------------

            #threading.Thread(target=self.check_msg, args=(msg,)).start()

----------------------------------------------------
#self.send_kick_msg(self.active_user.id)
#self.send_ban_msg(self.active_user.id)
----------------------------------------------------
#        Question = input ("how are you?")
#        if Question == ("good")
#            print ("good to hear that")
#        elif Question == ("not good")
#            print ("my well wishes get well soon")
----------------------------------------------------
         elif cmd == prefix + "whiteknight":
             self.send_chat_msg('White Knight has been awarded to %s' % cmd_arg)
----------------------------------------------------

----------------------------------------------------

----------------------------------------------------

----------------------------------------------------

----------------------------------------------------

                     #self.send_chat_msg('Anti-Nigger Defense System Activated.')
                     #time.sleep(1 * 5)
                     #self.send_chat_msg('Preparing Nigger Detection Sensors...')
                     #time.sleep(1 * 3)
                     #self.send_chat_msg('Powering on Lethal Force Nigger Kill Bot 1.0...')
                     #time.sleep(1 * 3)
                     #self.send_chat_msg('Nigger Kill Bot MODE: [INTERROGATE]')
        time.sleep(1 * 3)
        self.send_chat_msg('Are you a nigger?')
        if "yes" in msg:
            sleep(randint(1,2))
            self.send_chat_msg("%s has admitted to being a nigger. Checking intelligence level for Slavery Services Vocational Aptitude Battery (SSVAB)" % self.active_user.nick)
            self.send_chat_msg('!acc kan %s' % self.active_user.account)
        elif "no" in msg:
            sleep(randint(1,2))
            self.send_chat_msg("%s must prove they are not a nigger by answering a White Security Question" % self.active_user.nick)
            sleep(randint(1,2))
            self.send_chat_msg('If you are traveling 60 Miles per Hour, how long does it take to travel one mile?)')
            sleep(randint(10,15))
            self.send_chat_msg('!acc kan %s' % self.active_user.account)








    def do_ban(self, user_name):
        """
        Ban a user from the room.

        :param user_name: The username to ban.
        :type user_name: str
        """
        if self.is_client_mod:
            if len(user_name) is 0:
                self.send_chat_msg('Missing username.')
            elif user_name == self.nickname:
                self.send_chat_msg('Action not allowed.')
            else:
                if user_name.startswith('*'):
                    user_name = user_name.replace('*', '')
                    _users = self.users.search_containing(user_name)
                    if len(_users) > 0:
                        for i, user in enumerate(_users):
                            if user.nick != self.nickname and user.user_level > self.active_user.user_level:
                                if i <= pinylib.CONFIG.B_MAX_MATCH_BANS - 1:
                                    self.send_ban_msg(user.id)
                else:
                    _user = self.users.search_by_nick(user_name)
                    if _user is None:
                        self.send_chat_msg('No user named: %s' % user_name)
                    elif _user.user_level < self.active_user.user_level:
                        self.send_chat_msg('Not allowed.')
                    else:
                        self.send_ban_msg(_user.id)

