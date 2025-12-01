import sys
import pathlib
import runpy
import builtins
import os

def about():
    print("This program prints everything that is imported.")

def main():
    sys.argv.pop(0)

    if len(sys.argv) < 1:
        print("\n\nThis program requires one argument. The name of a python program or module to execute.")
        sys.exit()

    print("-"*80)
    print("{0:-^80}".format('   Imports above here belong to watch_imports. Now beginning your imports.   '))
    print("-"*80)

    builtins.__import__.indented[0] = 0

    target = pathlib.Path(sys.argv[0])
    sys.path.insert(0, os.getcwd())
    if target.is_file():
        exec(target.read_text())
    else:
        runpy.run_module(sys.argv[0], init_globals=globals())

if __name__ == "__main__":
    main()