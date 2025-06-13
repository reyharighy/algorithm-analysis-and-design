"""A module to help validate functions in a decorator-way."""

def validate_labels(*label_args):
    """Decorator to validate labels of vertices and edges."""
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]
            arg_map = dict(zip(arg_names, (self, *args))) | kwargs

            for label in label_args:
                value: str | None = arg_map.get(label)

                if value is None:
                    raise ValueError(f"Label cannot be empty for argument '{label}'")

                if not isinstance(value, str) or not value.isalpha():
                    raise ValueError(f"Invalid label: '{value}' for argument '{label}'")

            return func(self, *args, **kwargs)
        return wrapper
    return decorator

def validate_param_keyword(keyword_args):
    """Decorator to prevent alteration on the attribute if one keyword parameter does not exist"""
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            for key in kwargs:
                if key not in keyword_args:
                    raise AttributeError(f"Invalid parameter: {key}")

            return func(self, *args, **kwargs)
        return wrapper
    return decorator
