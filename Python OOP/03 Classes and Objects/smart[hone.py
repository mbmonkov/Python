class Smartphone:

    def __init__(self, memory: int):
        self. memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        self.is_on = not self.is_on

    def install(self, app, app_memory):
        if self.is_on and self.memory > app_memory:
            self.apps.append(app)
            self.memory -= app_memory
            return f"Installing {app}"
        elif self.memory >= app_memory and not self.is_on:
            f"Turn on your phone to install {app}"
        f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"
