#!/usr/bin/python3
# coding: utf-8
import click


@click.command()
@click.option('-n', is_flag=True, help="Output line numbers")
@click.option('-f', is_flag=True, help="Output name files")
@click.option('-i', is_flag=True, help="Case-insensitive output")
@click.option('-v', is_flag=True, help="Output string inversion")
@click.argument('string')
@click.argument('filename', nargs=-1, type=click.Path(exists=True))
def search_string(n, f, i, v, string, filename):
    """Argument STRING and FILENAME is required"""

    if n:
        for x in filename:
            with open(x, 'r', errors='ignore') as file:
                for index, line in enumerate(file):
                    if string in line:
                        print(index)
    if f:
        for x in filename:
            with open(x, 'r', errors='ignore') as file:
                if any(string in line for line in file):
                    print(x)

    if i:
        sup = str.upper(string)
        slow = str.lower(string)
        for x in filename:
            with open(x, 'r', errors='ignore') as file:
                for line in file:
                    if sup in line:
                        print(line)
                    if slow in line:
                        print(line)

    if v:
        for x in filename:
            with open(x, 'r', errors='ignore') as file:
                for line in file:
                    if string not in line:
                        print(line)

    if not (n or f or i or v):
        for x in filename:
            with open(x, 'r', errors='ignore') as file:
                for index, line in enumerate(file):
                    if string in line:
                        print(index, line)


if __name__ == '__main__':
    search_string()
