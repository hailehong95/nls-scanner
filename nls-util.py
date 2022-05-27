#!/usr/bin/env python

from utils.clean import clean_task
from utils.build import build_task
from utils.version import version_task
from utils.extract import extract_task

import click


@click.group()
def cli():
    """A CLI Utility for NLS Scanner"""
    pass


@cli.command(name='version', help='Show Utility version')
def version():
    version_task()


@cli.command(name='clean', help='Clean all temporary working files')
def clean():
    clean_task()


@cli.command(name='build', help='Build NLS Scanner')
def build():
    extract_task()
    build_task()
    pass


if __name__ == '__main__':
    cli()
