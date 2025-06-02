"""A module to help validate labels of vertices and edges in a graph."""

def validate_labels(*label_args):
    """Decorator to validate labels of vertices and edges."""
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]
            arg_map = dict(zip(arg_names, (self, *args))) | kwargs

            for label in label_args:
                value = arg_map.get(label)

                if not isinstance(value, str) or not value.isalpha() or len(value) == 0:
                    raise ValueError(f"Invalid label: '{value}' for argument '{label}'")

            return func(self, *args, **kwargs)
        return wrapper
    return decorator
