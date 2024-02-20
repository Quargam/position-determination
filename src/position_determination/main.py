import argparse
import typing

from .commands import analysis


def parse_arguments(cmd_args: typing.Optional[typing.List[str]]) -> argparse.Namespace:
    arg_parser = argparse.ArgumentParser()
    subparsers = arg_parser.add_subparsers()
    analysis.parse_arguments(subparsers.add_parser(
        'analys',
    ))
    return arg_parser.parse_args(cmd_args)


def main(cmd_args: typing.Optional[typing.List[str]]) -> None:
    args = parse_arguments(cmd_args)
    args.command(args)  # Running a command with an argument.
