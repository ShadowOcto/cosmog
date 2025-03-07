import importlib
import os

bot_commands = []

def load_commands():
    global bot_commands
    bot_commands.clear()

    for command_file in os.listdir('./commands/impl/'):
        if command_file.endswith('.py'):
            file_name = command_file.split('.')[0]
            command_module = importlib.import_module(f"commands.impl.{file_name}")
            bot_commands.append(command_module)