from typing import Optional
from click import Command

def sample(transformation: Optional[str] = "") -> None: ...
def couple(transformation: Optional[str] = "") -> None: ...
def dog(transformation: Optional[str] = "") -> None: ...
def _handle_sample_command(source: str, transformation: Optional[str] = None, open_in_browser: bool = False, resource_type: str = "image") -> None: ...

commands: list[Command]