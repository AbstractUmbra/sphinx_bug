from __future__ import annotations

from os import PathLike
from typing import Literal

MyLiteralAlias = Literal[1, 2, 3]

__all__: tuple[str] = ("foo",)

def foo(path: PathLike[str], literal: MyLiteralAlias) -> None:
    print(path, literal)

