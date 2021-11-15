from typing import Any

def relative_error(known: float, measured: float) -> float:
    return (measured - known) / known

def average_dict_val(mapping: dict[str, Any], key: str) -> float:
    return sum(p[key] for p in mapping.values()) / len(mapping)

