from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class TraceNode:
    function_name: str
    id: str
    kwargs: Dict[Any, Any]
    depth: int
    return_val: Any
