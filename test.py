import itchat
import random
from time import strftime, localtime

LOVE_USR_NAME = '@7abe2915ad882418f64c0d8558293127'
MY_USR_NAME = '@1ec7c3caa7eb7967b192d41f7d451ea8ff7511c9e3a7af2448c1d32db6789c24'

# configurations
sweetReplySet = []
with open('sweetReplies.love','r') as f:
	for line in f:
		sweetReplySet.append(line);
# debug
for reply in sweetReplySet:
	print(reply)

# reply methods
@itchat.msg_register(itchat.content.TEXT)
def sweetReply(msg):
	curMsg = msg['Text']
	fromUsr = msg['FromUserName']
	if fromUsr == LOVE_USR_NAME:
		itchat.send(random.choice(sweetReplySet), LOVE_USR_NAME)

def parrotReply(msg):
	curMsg = msg['Text']
	fromUsr = msg['FromUserName']
	print('Received a messge from ' + fromUsr + ':' + curMsg)
	itchat.send(curMsg, fromUsr)

# user login
itchat.auto_login(hotReload = True)
# login message to FileHelper
itchat.send('Hello World. Bot Login @' + strftime("%a, %d %b %Y %X %Z", localtime()), toUserName='filehelper')
# get a updated list of friends
friendsList = itchat.get_friends(update = True)
with open('friendList.info', 'w') as f:
	for friend in friendsList:
		print(str(friend), file=f);
# start auto reply
itchat.run()