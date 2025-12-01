import sys
import inspect



def make_import_printer(ignored_modules = ['io','_io'], indent_chars = "->"):
    indented = [0]
    prev_num_modules = 0
    def print_imports(name, *args, original=__import__, **kwargs):
        nonlocal indented, prev_num_modules
        indent = indent_chars * indented[0]
        indented[0] += 1
        if name not in ignored_modules:
            #technically import_watch is executing on the stack so lets find the thing before us and see who doing the import.
            call_stack = inspect.stack()
            for pos,frame in enumerate(call_stack):
                if frame.filename.endswith("import_watcher.py"):
                   caller = call_stack[pos+1]
                   break
            caller_name = caller.filename
            print(f"{indent} + {caller_name} is importing (executing) {name} code:{caller.code_context}")
        #Print when the thing you are trying to import is in the cache
        if (name in sys.modules) and (name not in ignored_modules):
            print(f"{indent} === {name} Name exists in module cache. (It may or may not have finished executing)")
        result = original(name,*args,**kwargs)
        #If this is the first call we can ignore up to inspect which we imported.
        if prev_num_modules == 0:
            prev_num_modules = list(sys.modules).index("inspect") + 1
        #If the number of modules in the cache changed then print the additions.
        if len(sys.modules) != prev_num_modules:
            print(f"{indent} === Added to module cache {list(sys.modules)[prev_num_modules:]}")
            prev_num_modules = len(sys.modules)
        if name not in ignored_modules:    
            print(f"{indent} - Finished importing (executing or using cached version) {name}")
        if indent == "":
            print()
        indented[0] -= 1
        return result
    print_imports.indented = indented
    return print_imports


