from py_mini_racer import MiniRacer
import os

full_path = os.path.join(os.getcwd(), "encrypt", "a_bogus.js")
print(full_path)


def init_ctx():
    with open(full_path, "r", encoding="utf-8") as f:
        js_code = f.read()
    ctx = MiniRacer()
    ctx.eval(js_code)
    return ctx
