import builtins
from watch_imports.import_watcher import make_import_printer


builtins.__import__ = make_import_printer()

