registered_class = {} # to store key information for certain class
# book: ISBN13,

def register_class(object_class):
    registered_class[object_class.get_key()] = object_class

def check_cache(key):
    if key in registered_class:
        return registered_class[key]
    return False