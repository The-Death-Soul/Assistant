# Powered By: © Love_Dear_Comrades
# Copyright (C) 2022 @The_Death_Soul

import glob
from pathlib import Path
from assistant.utils.util import load_plugins
import logging
from assistant import Sammy

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "assistant/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
    
print("Successfully Started Your Bot!")

if __name__ == "__main__":
    Sammy.run_until_disconnected()
