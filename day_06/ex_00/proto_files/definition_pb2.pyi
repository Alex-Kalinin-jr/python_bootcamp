from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Alignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ALIGN_CENTER: _ClassVar[Alignment]
    ALIGN_TOP: _ClassVar[Alignment]
    ALIGN_BOTTOM: _ClassVar[Alignment]

class ShipClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CORVETTE: _ClassVar[ShipClass]
    FRIGATE: _ClassVar[ShipClass]
    CRUISER: _ClassVar[ShipClass]
    DESTROYER: _ClassVar[ShipClass]
    CARRIER: _ClassVar[ShipClass]
    DREADNOUGHT: _ClassVar[ShipClass]
ALIGN_CENTER: Alignment
ALIGN_TOP: Alignment
ALIGN_BOTTOM: Alignment
CORVETTE: ShipClass
FRIGATE: ShipClass
CRUISER: ShipClass
DESTROYER: ShipClass
CARRIER: ShipClass
DREADNOUGHT: ShipClass

class Officer(_message.Message):
    __slots__ = ["firstname", "lastname", "rank"]
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    firstname: str
    lastname: str
    rank: str
    def __init__(self, firstname: _Optional[str] = ..., lastname: _Optional[str] = ..., rank: _Optional[str] = ...) -> None: ...

class ShipData(_message.Message):
    __slots__ = ["alignment", "name", "ship_class", "length", "size", "armed", "officer", "status"]
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SHIP_CLASS_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    ARMED_FIELD_NUMBER: _ClassVar[int]
    OFFICER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    alignment: Alignment
    name: str
    ship_class: ShipClass
    length: float
    size: int
    armed: bool
    officer: _containers.RepeatedCompositeFieldContainer[Officer]
    status: str
    def __init__(self, alignment: _Optional[_Union[Alignment, str]] = ..., name: _Optional[str] = ..., ship_class: _Optional[_Union[ShipClass, str]] = ..., length: _Optional[float] = ..., size: _Optional[int] = ..., armed: bool = ..., officer: _Optional[_Iterable[_Union[Officer, _Mapping]]] = ..., status: _Optional[str] = ...) -> None: ...

class coords(_message.Message):
    __slots__ = ["coords"]
    COORDS_FIELD_NUMBER: _ClassVar[int]
    coords: str
    def __init__(self, coords: _Optional[str] = ...) -> None: ...
