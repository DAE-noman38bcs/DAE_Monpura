# Developer: Mahmud Abdullah Al Naman (মাহমুদ আব্দুল্লাহ আল নোমান)
# Email: noman38bcs@gmail.com
# Phone: 01623015273
# File: monpuragrok_ai_infer.py
"""Lightweight local inference stub for MonpuraGrok (offline demo mode)."""
import random

INTENTS = ["crop_advice", "fertilizer_dose", "pest_alert", "weather_note"]


def infer(text: str) -> dict:
    intent = random.choice(INTENTS)
    return {"intent": intent, "confidence": round(random.uniform(0.6, 0.99), 2), "input": text}


if __name__ == "__main__":
    print(infer("সূর্যমুখী চাষের পরামর্শ দরকার"))
