class Node:
    def tick(self, indent=0):
        raise NotImplementedError
    
    def _indent(self, level):
        """Return indentation string for the given level."""
        return "  " * level
    
    def _format_args_kwargs(self, args, kwargs):
        """Format args and kwargs for logging."""
        parts = []
        if args:
            # Format args nicely - truncate long strings
            formatted_args = []
            for arg in args:
                if isinstance(arg, str):
                    if len(arg) > 60:
                        formatted_args.append(f"'{arg[:57]}...'")
                    else:
                        formatted_args.append(repr(arg))
                else:
                    formatted_args.append(repr(arg))
            parts.append(", ".join(formatted_args))
        if kwargs:
            # Format kwargs nicely - truncate long strings
            formatted_kwargs = []
            for k, v in kwargs.items():
                if isinstance(v, str) and len(v) > 40:
                    formatted_kwargs.append(f"{k}='{v[:37]}...'")
                else:
                    formatted_kwargs.append(f"{k}={repr(v)}")
            parts.append(", ".join(formatted_kwargs))
        return ", ".join(parts) if parts else ""

