from flask.ext.script import Manager, Command
from flask import Flask

import yandexwebdav
import time
import os

app = Flask(__name__)
manager = Manager(app)


@manager.command
def backup():
    conf = yandexwebdav.Config({
        "user": "user",
        "password": "pass"
        })

    directory = "/PATH/"

    for filename in os.listdir(directory):
        current_file = "{0}{1}".format(directory, filename)
        if time.time() - os.path.getmtime(current_file) > (21 * 24 * 60 * 60):
            conf.upload(current_file,
                        "/PATH/{0}".format(filename))
            os.remove(current_file)

if __name__ == "__main__":
    manager.run()