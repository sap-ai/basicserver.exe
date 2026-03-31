from distutils.core import setup
import py2exe

setup(
    console = [
        {
            "script": "serve.py",
            "icon_resources": [(1, "severimg.ico")]
        }
    ],
)
