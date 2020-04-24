import sys

def show_size(x, level=0):
    print('\t' * level, f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')

    if hasattr(x, '__iter__'):
        if not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)