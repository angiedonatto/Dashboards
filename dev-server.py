from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


HOST = "127.0.0.1"
START_PORT = 8000


def run():
    handler = partial(SimpleHTTPRequestHandler, directory=".")
    last_error = None
    for port in range(START_PORT, START_PORT + 50):
        try:
            server = ThreadingHTTPServer((HOST, port), handler)
        except OSError as exc:
            last_error = exc
            continue

        print(f"Serving dashboard at http://{HOST}:{port}/index.html", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
        finally:
            server.server_close()
        return

    raise SystemExit(f"No free port found from {START_PORT}: {last_error}")


if __name__ == "__main__":
    run()
