from setuptools import setup

setup(
    name="asciinema_clip",
    version="0.1.2",
    author="Aria Ghora Prabono",
    author_email="hello@ghora.net",
    description="Clip the displaying delay on asciicast produced by asciinema",
    license="MIT",
    packages=["asciinema_clip"],
    scripts=["bin/asciinema-clip"]
)
