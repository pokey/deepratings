# -*- coding: utf-8 -*-

import click
import json
from extruct.w3cmicrodata import MicrodataExtractor


@click.command()
def main(args=None):
    """Console script for deepratings"""
    mde = MicrodataExtractor()
    with open('whisky.html') as f:
        data = mde.extract(f.read())
    print(json.dumps(data))


if __name__ == "__main__":
    main()
