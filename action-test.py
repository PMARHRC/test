#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from snipsTools import SnipsConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io
# import requests
# import HTMLParser

CONFIG_INI = "config.ini"

# If this skill is supposed to run on the satellite,
# please get this mqtt connection info from <config.ini>
# Hint: MQTT server is always running on the master device
MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

class Test(object):
    """Class used to wrap action code with mqtt connection

        Please change the name refering to your application
    """

    def __init__(self):
        # get the configuration if needed
        try:
            self.config = SnipsConfigParser.read_configuration_file(CONFIG_INI)
        except :
            self.config = None

        # start listening to MQTT
        self.start_blocking()

    # --> Sub callback function, one per intent
    def test_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
        joke_msg = "Ceci est un test et il fonctionne ! Magnifique !"
        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, joke_msg, "test")
		
    def Apres_midi_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
        joke_msg = "Bon après-midi"
        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, joke_msg, "Apres_midi")
		
    def Appetit_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
        joke_msg = "Merci ! Bon appetit !"
        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, joke_msg, "Appetit")

    def Bonsoir_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
        joke_msg = "A vous aussi ! Je vous souhaite une bonne soirée."
        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, joke_msg, "Bonsoir")
		
    def Bonjour_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
        joke_msg = "Bonjour ! J'espère que vous allez bien aujourd'hui !"
        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, joke_msg, "Bonjour")
		
    def Bonne_nuit_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
        joke_msg = "Moi aussi je suis fatigué ! Passez une bonne nuit !"
        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, joke_msg, "Bonne_nuit")
    # More callback function goes here...

    # --> Master callback function, triggered everytime an intent is recognized
    def master_intent_callback(self,hermes, intent_message):
        coming_intent = intent_message.intent.intent_name
        if coming_intent == 'PierreMarteau:test':
            self.test_callback(hermes, intent_message)
        if coming_intent == 'Darghorn:Apres_midi':
            self.Apres_midi_callback(hermes, intent_message)
		if coming_intent == 'Darghorn:Appetit':
            self.Appetit_callback(hermes, intent_message)
		if coming_intent == 'Darghorn:Bonsoir':
            self.Bonsoir_callback(hermes, intent_message)
        if coming_intent == 'Darghorn:Bonjour':
            self.Bonjour_callback(hermes, intent_message)
		if coming_intent == 'Darghorn:Bonne_nuit':
            self.Bonne_nuit_callback(hermes, intent_message)
        # more callback and if condition goes here...

    # --> Register callback function and start MQTT
    def start_blocking(self):
        with Hermes(MQTT_ADDR) as h:
            h.subscribe_intents(self.master_intent_callback).start()

if __name__ == "__main__":
    Test()
