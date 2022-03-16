# Powered By: © Love_Dear_Comrades
# Copyright (C) 2022 @The_Death_Soul

import sys
import logging
import importlib
from pathlib import Path

def load_plugins(plugin_name):
    path = Path(f"assistant/plugins/{plugin_name}.py")
    name = "assistant.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["assistant.plugins." + plugin_name] = load
    print("Bot has Started Successfully " + plugin_name)
