import threading as th


class Container:
    def __init__(self):
        self.Content = 0
        self.ContentLock = th.Lock()
        self.newContentEvent = th.Event()

    def set(self, content):
        with self.ContentLock:
            self.Content = content
        self.newContentEvent.set()

    def asyncget(self):
        with self.ContentLock:
            content = self.Content
        return content

    def get(self):
        self.newContentEvent.wait()
        content = self.asyncget()
        self.newContentEvent.clear()
        return content

    def isNew(self):
        if self.newContentEvent.isSet():
            return True
        return False
