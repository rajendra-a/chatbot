# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import smtplib, ssl

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet



class ActionSendEmail(FormAction):

    def name(self) -> Text:
        return "action_send_mail"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        username = tracker.get_slot("username")
        email = tracker.get_slot("email-address")
        phone = tracker.get_slot("phone-number")

        smtp_server = syberzen.com
        port = 465
        sender_email = "rajendrareddy.akkala@gmail.com"
        receiver_email = "rajendra@syberzen.com"
        password = input("Please enter password")

        message = f"this message is sent from chatbot {username}, {email}, {phone}"    

        # create secure ssl context
        context = ssl.create_default_context()

        # try to login server
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, receiver_email)
            server.sendemail(sender_email, receiver_email, message)

        dispatcher.utter_message(text="Soon we will contact you")

        return [Slotset("username", None),
                SlotSet("email-address", None),
                SlotSet("phone-number", None)]
