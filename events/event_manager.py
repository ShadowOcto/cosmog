import importlib
import os

events = []

def init():
    global bot_commands

    for event_file in os.listdir('./events/impl/'):
        if event_file.endswith('.py'):
            file_name = event_file.split('.')[0]
            event_module = importlib.import_module(f"events.impl.{file_name}")
            events.append(event_module)