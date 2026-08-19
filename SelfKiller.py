#!/usr/bin/env python3
import ctypes
import os
import signal
import tempfile
import time
import tkinter as tk
import locale
import json
from pathlib import Path

# 初始化 locale 設定為使用者環境
current_lang = None
try:
    locale.setlocale(locale.LC_ALL, '')
    current_lang = locale.getlocale()[0]
except:
    env_lang = os.environ.get('LANG', '').split('.')[0]
    if env_lang:
        current_lang = env_lang

locale_file = Path(__file__).parent / "i18n" / f"{current_lang}.json"
if not locale_file.is_file():
    locale_file = Path(__file__).parent / "i18n"  / "en_US.json"

with open(locale_file, "r", encoding="utf-8") as f:
    text = json.load(f)

def raising():
    raise Exception("Custom exception")

def block():
    while True:
        time.sleep(1000)

root = tk.Tk()
root.geometry("700x200")
root.title(text["title"])


# Warning
tk.Label(
    root,
    font=("Noto Sans", 14),
    text=text["warn"],
).pack()


# Signals
tk.Label(root, text=text["signals"]).pack()

signals_canvas = tk.Canvas(root)
signals_canvas.pack()

tk.Button(
    signals_canvas,
    text=text["sigterm"],
    command=lambda: signal.raise_signal(signal.SIGTERM),
).pack(side="left")

tk.Button(
    signals_canvas,
    text=text["sigkill"],
    command=lambda: signal.raise_signal(signal.SIGKILL),
).pack(side="left")

tk.Button(
    signals_canvas,
    text=text["sigsegv"],
    command=lambda: signal.raise_signal(signal.SIGSEGV),
).pack(side="left")

tk.Button(
    signals_canvas,
    text=text["sigbus"],
    command=lambda: signal.raise_signal(signal.SIGBUS),
).pack(side="left")

tk.Button(
    signals_canvas,
    text=text["sigill"],
    command=lambda: signal.raise_signal(signal.SIGILL),
).pack(side="left")


# Python exceptions
tk.Label(root, text=text["exceptions"]).pack()

exceptions_canvas = tk.Canvas(root)
exceptions_canvas.pack()

tk.Button(
    exceptions_canvas,
    text=text["name_error"],
    command=lambda: print(a),
).pack(side="left")

tk.Button(
    exceptions_canvas,
    text=text["type_error"],
    command=lambda: print("1" + 1),
).pack(side="left")

tk.Button(
    exceptions_canvas,
    text=text["value_error"],
    command=lambda: print(int("abc")),
).pack(side="left")

tk.Button(
    exceptions_canvas,
    text=text["index_error"],
    command=lambda: print("abcdef"[6]),
).pack(side="left")

tk.Button(
    exceptions_canvas,
    text=text["key_error"],
    command=lambda: print({"a": "A", "b": "B"}["c"]),
).pack(side="left")

tk.Button(
    exceptions_canvas,
    text=text["zero_division_error"],
    command=lambda: print(1 / 0),
).pack(side="left")


# Other
tk.Label(root, text=text["other"]).pack()

other_canvas = tk.Canvas(root)
other_canvas.pack()

tk.Button(
    other_canvas,
    text=text["raise_exception"],
    command=raising,
).pack(side="left")

tk.Button(
    other_canvas,
    text=text["null_pointer"],
    command=lambda: ctypes.string_at(0),
).pack(side="left")

tk.Button(
    other_canvas,
    text=text["abort"],
    command=os.abort,
).pack(side="left")

tk.Button(
    other_canvas,
    text=text["blocking"],
    command=block,
).pack(side="left")


root.mainloop()
