import logging
from django.http import HttpResponse
from google.appengine.api import xmpp


def home(request):
    return HttpResponse('HOME')


def reply(request):
    #print("reply")
    #if request.method == 'POST':
        #print "reply.POST"
    #message = xmpp.Message(request.POST)
    #msg = "Someone has sent you a gift on Example.com. To view: http://example.com/gifts/"
        #
    #status_code = xmpp.send_message(message.sender, msg)
    #chat_message_sent = (status_code == xmpp.NO_ERROR)
    message = xmpp.Message(request.POST)
    logging.debug('Start guestbook signing request')
    #if message.body[0:5].lower() == 'hello':
    message.reply("Greetings!")

    #elif request.method == 'GET':
        #print "reply.GET"

    return HttpResponse('')


def send(request):
    msg = "Someone has sent you a gift on Example.com. To view: http://example.com/gifts/"
    user_address = 'wanglun02@gmail.com'
    status_code = xmpp.send_message(user_address, msg)
    chat_message_sent = (status_code == xmpp.NO_ERROR)

    return HttpResponse('')


def subscribe(request):
    print("subscribe")
    #sender = request.get('from').split('/')[0]

    return HttpResponse('')


def subscribed(request):
    print("subscribed")
    return HttpResponse('')


def unsubscribe(request):
    print("unsubscribe")
    return HttpResponse('')


def unsubscribed(request):
    print("unsubscribed")
    return HttpResponse('')


def probe(request):
    print("probe")
    return HttpResponse('')


def available(request):
    print("available")
    return HttpResponse('')


def unavailable(request):
    print("unavailable")
    return HttpResponse('')
