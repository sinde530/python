# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

import requests

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSearchBing(Action):

    def name(self) -> Text:
        return "action_search_bing"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        search_query = tracker.latest_message['text']

        headers = {
            'Ocp-Apim-Subscription-Key': 'A04B44E5C70846D3AFE6D937EC43DB6B'
        }

        params = {
            'q': search_query,
            'count': 3,
            'offset': 0,
            'mkt': 'en-US',
            'safesearch': 'Moderate'
        }

        response = requests.get(
            'https://api.cognitive.microsoft.com/bing/v7.0/search', headers=headers, params=params).json()

        results = response['webPages']['value']
        for result in results:
            title = result['name']
            url = result['url']
            snippet = result['snippet']
            dispatcher.utter_message(f"{title}: {snippet} ({url})")

        return []
