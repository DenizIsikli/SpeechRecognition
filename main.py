from PygameWindow import PygameWindow
import Listener as Ls
import threading

if __name__ == "__main__":
    pg_window = PygameWindow()
    ls = Ls.Listener(pg_window)

    listener_thread = threading.Thread(target=ls.listen, daemon=True)
    listener_thread.start()

    pg_window.run()
