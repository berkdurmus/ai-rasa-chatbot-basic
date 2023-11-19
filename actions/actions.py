from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import requests

class ActionProvideWeather(Action):
    def name(self):
        return "action_provide_weather"

    def run(self, dispatcher, tracker, domain):
        location = tracker.get_slot('location')
        # Fetch weather from a weather API
        weather = get_weather_from_api(location)
        dispatcher.utter_message(text=f"The weather in {location} is {weather}.")
        return []

class ActionBookTable(Action):
    def name(self):
        return "action_book_table"

    def run(self, dispatcher, tracker, domain):
        number = tracker.get_slot('number')
        time = tracker.get_slot('time')
        # Logic to book a table
        booking_confirmation = book_table(number, time)
        dispatcher.utter_message(text=f"Table booked for {number} at {time}.")
        return []
