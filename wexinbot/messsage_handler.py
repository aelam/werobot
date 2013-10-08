__author__ = 'ryan'


from google.appengine.api import xmpp

chat_url = "/_ah/xmpp/message/chat/"

class message_handler:

    def send_message(self, receiver):
        chat_message_sent = False
        msg = "Someone has sent you a gift on Example.com. To view: http://example.com/gifts/"
        status_code = xmpp.send_message(receiver, msg)
        chat_message_sent = (status_code == xmpp.NO_ERROR)

        #if not chat_message_sent:


    #def handling_message(self):

