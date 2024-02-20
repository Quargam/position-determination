import sys

from .main import main


def app() -> None:
    main(sys.argv[1:])
