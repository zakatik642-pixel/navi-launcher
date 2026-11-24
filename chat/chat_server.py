"""Общий чат лаунчера: минимальный HTTP-сервер на стандартной библиотеке.

Запуск:  python chat_server.py [порт]
Клиент обращается к http://<адрес>:<порт>/messages (GET — список, POST — сообщение).
Сообщения хранятся в памяти процесса, последние 300 штук.
"""

import json
import os
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

MESSAGES = []
LIMIT = 300


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, payload):
        body = json.dumps(payload, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path.split("?")[0] != "/messages":
            return self._send(404, {"error": "not found"})
        self._send(200, {"messages": MESSAGES[-LIMIT:]})

    def do_POST(self):
        if self.path.split("?")[0] != "/messages":
            return self._send(404, {"error": "not found"})
        length = int(self.headers.get("Content-Length") or 0)
        try:
            data = json.loads(self.rfile.read(length) or b"{}")
        except ValueError:
            return self._send(400, {"error": "bad json"})
        nick = str(data.get("nick") or "").strip()[:16]
        text = str(data.get("text") or "").strip()[:300]
        if not nick or not text:
            return self._send(400, {"error": "nick and text required"})
        MESSAGES.append({"nick": nick, "text": text, "ts": int(time.time())})
        del MESSAGES[:-LIMIT]
        self._send(200, {"ok": True})

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    port = int(os.getenv("PORT") or (os.sys.argv[1] if len(os.sys.argv) > 1 else "8765"))
    print(f"чат слушает 0.0.0.0:{port}")
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()
