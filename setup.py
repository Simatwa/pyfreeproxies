from pathlib import Path

from setuptools import setup

from setuptools import find_packages

DOCS_PATH = Path(__file__).parents[0] / "docs/README.md"
PATH = Path("README.md")
if not PATH.exists():
    with Path.open(DOCS_PATH, encoding="utf-8") as f1:
        with Path.open(PATH, "w+", encoding="utf-8") as f2:
            f2.write(f1.read())

setup(
    name="pyfreeproxies",
    version="0.1.0",
    license="GNUv3",
    author="Smartwa",
    maintainer="Smartwa",
    author_email="simatwacaleb@proton.me",
    description="Free to use http, socks4 and socks5 proxies",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/Simatwa/pyfreeproxies",
    project_urls={
        "Bug Report": "https://github.com/Simatwa/pyfreeproxies/issues/new",
        "Homepage": "https://github.com/Simatwa/pyfreeproxies",
        "Source Code": "https://github.com/Simatwa/pyfreeproxies",
        "Issue Tracker": "https://github.com/Simatwa/pyfreeproxies/issues",
        "Download": "https://github.com/Simatwa/pyfreeproxies/releases",
        "Documentation": "https://github.com/Simatwa/pyfreeproxies/blob/main/docs",
    },
    entry_points={
        "console_scripts": [
            "pytgpt = pytgpt.console:main",
        ],
    },
    install_requires=["requests>=2.31.0", "pydantic>=2.6.4"],
    python_requires=">=3.9",
    keywords=[
        "freeproxies",
        "proxies",
        "socks4",
        "socks5",
        "http",
    ],
    long_description=Path.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Developers",
        "Topic :: Internet :: Proxy Servers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
