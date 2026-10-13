# Developer: Mahmud Abdullah Al Naman (মাহমুদ আব্দুল্লাহ আল নোমান)
# Email: noman38bcs@gmail.com
# Phone: 01623015273
# File: monpuracopilot_core.py
"""
MonpuraCopilot Core Engine
মনপুরা অফিসের কোড/রিপোর্ট সহকারী
"""
import json
import logging
from dataclasses import dataclass
from typing import Optional

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("MonpuraCopilot.core")


@dataclass
class BlockUnit:
    union: str
    block: str
    officer: Optional[str] = None


class MonpuraCopilotEngine:
    VERSION = "0.1.0"

    def __init__(self, config_path: str = "config/monpuracopilot.config.xml"):
        self.config_path = config_path
        log.info("Engine initialized :: %s", self.VERSION)

    def load(self):
        log.info("Loading config from %s", self.config_path)
        return True

    def run(self, payload: dict) -> dict:
        return {"status": "ok", "engine": "MonpuraCopilot", "echo": payload}


if __name__ == "__main__":
    eng = MonpuraCopilotEngine()
    eng.load()
    print(json.dumps(eng.run({"ping": True}), ensure_ascii=False))
