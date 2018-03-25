#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

import thrift.py3.types
import thrift.py3.exceptions
from thrift.py3.types import NOTSET, NOTSETTYPE
from thrift.py3.serializer import Protocol
import typing as _typing

import sys
import itertools
import enum as __enum


class MyEnumA(__enum.Enum, _typing.SupportsInt):
    fieldA = ...
    fieldB = ...
    fieldC = ...
    value: int
    def __int__(self) -> int: ...


class SmallStruct(thrift.py3.types.Struct, _typing.Hashable, _typing.Iterable[_typing.Tuple[str, _typing.Any]]):
    def __init__(
        self, *,
        small_A: _typing.Optional[bool]=None,
        small_B: _typing.Optional[int]=None
    ) -> None: ...

    def __call__(
        self, *,
        small_A: _typing.Union[bool, NOTSETTYPE, None]=NOTSET,
        small_B: _typing.Union[int, NOTSETTYPE, None]=NOTSET
    ) -> SmallStruct: ...

    def __reduce__(self) -> _typing.Tuple[_typing.Callable, _typing.Tuple[_typing.Type['SmallStruct'], bytes]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Any]]: ...
    def __bool__(self) -> bool: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __lt__(self, other: 'SmallStruct') -> bool: ...

    @property
    def small_A(self) -> bool: ...
    @property
    def small_B(self) -> int: ...


class containerStruct(thrift.py3.types.Struct, _typing.Hashable, _typing.Iterable[_typing.Tuple[str, _typing.Any]]):
    def __init__(
        self, *,
        fieldA: _typing.Optional[bool]=None,
        fieldB: _typing.Optional[_typing.Mapping[str, bool]]=None,
        fieldC: _typing.Optional[_typing.AbstractSet[int]]=None,
        fieldD: _typing.Optional[str]=None,
        fieldE: _typing.Optional[str]=None,
        fieldF: _typing.Optional[_typing.Sequence[_typing.Sequence[_typing.Sequence[int]]]]=None,
        fieldG: _typing.Optional[_typing.Mapping[str, _typing.Mapping[str, _typing.Mapping[str, int]]]]=None,
        fieldH: _typing.Optional[_typing.Sequence[_typing.AbstractSet[int]]]=None,
        fieldI: _typing.Optional[bool]=None,
        fieldJ: _typing.Optional[_typing.Mapping[str, _typing.Sequence[int]]]=None,
        fieldK: _typing.Optional[_typing.Sequence[_typing.Sequence[_typing.Sequence[_typing.Sequence[int]]]]]=None,
        fieldL: _typing.Optional[_typing.AbstractSet[_typing.AbstractSet[_typing.AbstractSet[bool]]]]=None,
        fieldM: _typing.Optional[_typing.Mapping[_typing.AbstractSet[_typing.Sequence[int]], _typing.Mapping[_typing.Sequence[_typing.AbstractSet[str]], str]]]=None,
        fieldN: _typing.Optional[_typing.Sequence[int]]=None,
        fieldO: _typing.Optional[_typing.Sequence[float]]=None,
        fieldP: _typing.Optional[_typing.Sequence[int]]=None,
        fieldQ: _typing.Optional[MyEnumA]=None,
        fieldR: _typing.Optional[_typing.Mapping[str, bool]]=None,
        fieldS: _typing.Optional['SmallStruct']=None,
        fieldT: _typing.Optional['SmallStruct']=None,
        fieldU: _typing.Optional['SmallStruct']=None,
        fieldX: _typing.Optional['SmallStruct']=None
    ) -> None: ...

    def __call__(
        self, *,
        fieldA: _typing.Union[bool, NOTSETTYPE, None]=NOTSET,
        fieldB: _typing.Union[_typing.Mapping[str, bool], NOTSETTYPE, None]=NOTSET,
        fieldC: _typing.Union[_typing.AbstractSet[int], NOTSETTYPE, None]=NOTSET,
        fieldD: _typing.Union[str, NOTSETTYPE, None]=NOTSET,
        fieldE: _typing.Union[str, NOTSETTYPE, None]=NOTSET,
        fieldF: _typing.Union[_typing.Sequence[_typing.Sequence[_typing.Sequence[int]]], NOTSETTYPE, None]=NOTSET,
        fieldG: _typing.Union[_typing.Mapping[str, _typing.Mapping[str, _typing.Mapping[str, int]]], NOTSETTYPE, None]=NOTSET,
        fieldH: _typing.Union[_typing.Sequence[_typing.AbstractSet[int]], NOTSETTYPE, None]=NOTSET,
        fieldI: _typing.Union[bool, NOTSETTYPE, None]=NOTSET,
        fieldJ: _typing.Union[_typing.Mapping[str, _typing.Sequence[int]], NOTSETTYPE, None]=NOTSET,
        fieldK: _typing.Union[_typing.Sequence[_typing.Sequence[_typing.Sequence[_typing.Sequence[int]]]], NOTSETTYPE, None]=NOTSET,
        fieldL: _typing.Union[_typing.AbstractSet[_typing.AbstractSet[_typing.AbstractSet[bool]]], NOTSETTYPE, None]=NOTSET,
        fieldM: _typing.Union[_typing.Mapping[_typing.AbstractSet[_typing.Sequence[int]], _typing.Mapping[_typing.Sequence[_typing.AbstractSet[str]], str]], NOTSETTYPE, None]=NOTSET,
        fieldN: _typing.Union[_typing.Sequence[int], NOTSETTYPE, None]=NOTSET,
        fieldO: _typing.Union[_typing.Sequence[float], NOTSETTYPE, None]=NOTSET,
        fieldP: _typing.Union[_typing.Sequence[int], NOTSETTYPE, None]=NOTSET,
        fieldQ: _typing.Union[MyEnumA, NOTSETTYPE, None]=NOTSET,
        fieldR: _typing.Union[_typing.Mapping[str, bool], NOTSETTYPE, None]=NOTSET,
        fieldS: _typing.Union['SmallStruct', NOTSETTYPE, None]=NOTSET,
        fieldT: _typing.Union['SmallStruct', NOTSETTYPE, None]=NOTSET,
        fieldU: _typing.Union['SmallStruct', NOTSETTYPE, None]=NOTSET,
        fieldX: _typing.Union['SmallStruct', NOTSETTYPE, None]=NOTSET
    ) -> containerStruct: ...

    def __reduce__(self) -> _typing.Tuple[_typing.Callable, _typing.Tuple[_typing.Type['containerStruct'], bytes]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Any]]: ...
    def __bool__(self) -> bool: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __lt__(self, other: 'containerStruct') -> bool: ...

    @property
    def fieldA(self) -> bool: ...
    @property
    def fieldB(self) -> _typing.Mapping[str, bool]: ...
    @property
    def fieldC(self) -> _typing.AbstractSet[int]: ...
    @property
    def fieldD(self) -> str: ...
    @property
    def fieldE(self) -> str: ...
    @property
    def fieldF(self) -> _typing.Sequence[_typing.Sequence[_typing.Sequence[int]]]: ...
    @property
    def fieldG(self) -> _typing.Mapping[str, _typing.Mapping[str, _typing.Mapping[str, int]]]: ...
    @property
    def fieldH(self) -> _typing.Sequence[_typing.AbstractSet[int]]: ...
    @property
    def fieldI(self) -> bool: ...
    @property
    def fieldJ(self) -> _typing.Mapping[str, _typing.Sequence[int]]: ...
    @property
    def fieldK(self) -> _typing.Sequence[_typing.Sequence[_typing.Sequence[_typing.Sequence[int]]]]: ...
    @property
    def fieldL(self) -> _typing.AbstractSet[_typing.AbstractSet[_typing.AbstractSet[bool]]]: ...
    @property
    def fieldM(self) -> _typing.Mapping[_typing.AbstractSet[_typing.Sequence[int]], _typing.Mapping[_typing.Sequence[_typing.AbstractSet[str]], str]]: ...
    @property
    def fieldN(self) -> _typing.Sequence[int]: ...
    @property
    def fieldO(self) -> _typing.Sequence[float]: ...
    @property
    def fieldP(self) -> _typing.Sequence[int]: ...
    @property
    def fieldQ(self) -> MyEnumA: ...
    @property
    def fieldR(self) -> _typing.Optional[_typing.Mapping[str, bool]]: ...
    @property
    def fieldS(self) -> _typing.Optional['SmallStruct']: ...
    @property
    def fieldT(self) -> _typing.Optional['SmallStruct']: ...
    @property
    def fieldU(self) -> _typing.Optional['SmallStruct']: ...
    @property
    def fieldX(self) -> _typing.Optional['SmallStruct']: ...


class Map__string_bool(_typing.Mapping[str, bool], _typing.Hashable):
    def __init__(self, items: _typing.Mapping[str, bool]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __getitem__(self, key: str) -> bool: ...
    def __iter__(self) -> _typing.Iterator[str]: ...


class Set__i32(_typing.AbstractSet[int], _typing.Hashable):
    def __init__(self, items: _typing.AbstractSet[int]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def isdisjoint(self, other: _typing.AbstractSet[int]) -> bool: ...
    def union(self, other: _typing.AbstractSet[int]) -> 'Set__i32': ...
    def intersection(self, other: _typing.AbstractSet[int]) -> 'Set__i32': ...
    def difference(self, other: _typing.AbstractSet[int]) -> 'Set__i32': ...
    def symmetric_difference(self, other: _typing.AbstractSet[int]) -> 'Set__i32': ...
    def issubset(self, other: _typing.AbstractSet[int]) -> bool: ...
    def issuperset(self, other: _typing.AbstractSet[int]) -> bool: ...
    def __iter__(self) -> _typing.Iterator[int]: ...


_List__i32T = _typing.TypeVar('_List__i32T', bound=_typing.Sequence[int])


class List__i32(_typing.Sequence[int], _typing.Hashable):
    def __init__(self, items: _typing.Sequence[int]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    @_typing.overload
    def __getitem__(self, i: int) -> int: ...
    @_typing.overload
    def __getitem__(self, s: slice) -> _typing.Sequence[int]: ...
    def count(self, item: _typing.Any) -> int: ...
    def index(self, item: _typing.Any, start: int = ..., stop: int = ...) -> int: ...
    def __add__(self, other: _typing.Sequence[int]) -> 'List__i32': ...
    def __radd__(self, other: _List__i32T) -> _List__i32T: ...
    def __reversed__(self) -> _typing.Iterator[int]: ...
    def __iter__(self) -> _typing.Iterator[int]: ...


_List__List__i32T = _typing.TypeVar('_List__List__i32T', bound=_typing.Sequence[_typing.Sequence[int]])


class List__List__i32(_typing.Sequence[_typing.Sequence[int]], _typing.Hashable):
    def __init__(self, items: _typing.Sequence[_typing.Sequence[int]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    @_typing.overload
    def __getitem__(self, i: int) -> _typing.Sequence[int]: ...
    @_typing.overload
    def __getitem__(self, s: slice) -> _typing.Sequence[_typing.Sequence[int]]: ...
    def count(self, item: _typing.Any) -> int: ...
    def index(self, item: _typing.Any, start: int = ..., stop: int = ...) -> int: ...
    def __add__(self, other: _typing.Sequence[_typing.Sequence[int]]) -> 'List__List__i32': ...
    def __radd__(self, other: _List__List__i32T) -> _List__List__i32T: ...
    def __reversed__(self) -> _typing.Iterator[_typing.Sequence[int]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.Sequence[int]]: ...


_List__List__List__i32T = _typing.TypeVar('_List__List__List__i32T', bound=_typing.Sequence[_typing.Sequence[_typing.Sequence[int]]])


class List__List__List__i32(_typing.Sequence[_typing.Sequence[_typing.Sequence[int]]], _typing.Hashable):
    def __init__(self, items: _typing.Sequence[_typing.Sequence[_typing.Sequence[int]]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    @_typing.overload
    def __getitem__(self, i: int) -> _typing.Sequence[_typing.Sequence[int]]: ...
    @_typing.overload
    def __getitem__(self, s: slice) -> _typing.Sequence[_typing.Sequence[_typing.Sequence[int]]]: ...
    def count(self, item: _typing.Any) -> int: ...
    def index(self, item: _typing.Any, start: int = ..., stop: int = ...) -> int: ...
    def __add__(self, other: _typing.Sequence[_typing.Sequence[_typing.Sequence[int]]]) -> 'List__List__List__i32': ...
    def __radd__(self, other: _List__List__List__i32T) -> _List__List__List__i32T: ...
    def __reversed__(self) -> _typing.Iterator[_typing.Sequence[_typing.Sequence[int]]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.Sequence[_typing.Sequence[int]]]: ...


class Map__string_i32(_typing.Mapping[str, int], _typing.Hashable):
    def __init__(self, items: _typing.Mapping[str, int]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __getitem__(self, key: str) -> int: ...
    def __iter__(self) -> _typing.Iterator[str]: ...


class Map__string_Map__string_i32(_typing.Mapping[str, _typing.Mapping[str, int]], _typing.Hashable):
    def __init__(self, items: _typing.Mapping[str, _typing.Mapping[str, int]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __getitem__(self, key: str) -> _typing.Mapping[str, int]: ...
    def __iter__(self) -> _typing.Iterator[str]: ...


class Map__string_Map__string_Map__string_i32(_typing.Mapping[str, _typing.Mapping[str, _typing.Mapping[str, int]]], _typing.Hashable):
    def __init__(self, items: _typing.Mapping[str, _typing.Mapping[str, _typing.Mapping[str, int]]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __getitem__(self, key: str) -> _typing.Mapping[str, _typing.Mapping[str, int]]: ...
    def __iter__(self) -> _typing.Iterator[str]: ...


_List__Set__i32T = _typing.TypeVar('_List__Set__i32T', bound=_typing.Sequence[_typing.AbstractSet[int]])


class List__Set__i32(_typing.Sequence[_typing.AbstractSet[int]], _typing.Hashable):
    def __init__(self, items: _typing.Sequence[_typing.AbstractSet[int]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    @_typing.overload
    def __getitem__(self, i: int) -> _typing.AbstractSet[int]: ...
    @_typing.overload
    def __getitem__(self, s: slice) -> _typing.Sequence[_typing.AbstractSet[int]]: ...
    def count(self, item: _typing.Any) -> int: ...
    def index(self, item: _typing.Any, start: int = ..., stop: int = ...) -> int: ...
    def __add__(self, other: _typing.Sequence[_typing.AbstractSet[int]]) -> 'List__Set__i32': ...
    def __radd__(self, other: _List__Set__i32T) -> _List__Set__i32T: ...
    def __reversed__(self) -> _typing.Iterator[_typing.AbstractSet[int]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.AbstractSet[int]]: ...


class Map__string_List__i32(_typing.Mapping[str, _typing.Sequence[int]], _typing.Hashable):
    def __init__(self, items: _typing.Mapping[str, _typing.Sequence[int]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __getitem__(self, key: str) -> _typing.Sequence[int]: ...
    def __iter__(self) -> _typing.Iterator[str]: ...


_List__List__List__List__i32T = _typing.TypeVar('_List__List__List__List__i32T', bound=_typing.Sequence[_typing.Sequence[_typing.Sequence[_typing.Sequence[int]]]])


class List__List__List__List__i32(_typing.Sequence[_typing.Sequence[_typing.Sequence[_typing.Sequence[int]]]], _typing.Hashable):
    def __init__(self, items: _typing.Sequence[_typing.Sequence[_typing.Sequence[_typing.Sequence[int]]]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    @_typing.overload
    def __getitem__(self, i: int) -> _typing.Sequence[_typing.Sequence[_typing.Sequence[int]]]: ...
    @_typing.overload
    def __getitem__(self, s: slice) -> _typing.Sequence[_typing.Sequence[_typing.Sequence[_typing.Sequence[int]]]]: ...
    def count(self, item: _typing.Any) -> int: ...
    def index(self, item: _typing.Any, start: int = ..., stop: int = ...) -> int: ...
    def __add__(self, other: _typing.Sequence[_typing.Sequence[_typing.Sequence[_typing.Sequence[int]]]]) -> 'List__List__List__List__i32': ...
    def __radd__(self, other: _List__List__List__List__i32T) -> _List__List__List__List__i32T: ...
    def __reversed__(self) -> _typing.Iterator[_typing.Sequence[_typing.Sequence[_typing.Sequence[int]]]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.Sequence[_typing.Sequence[_typing.Sequence[int]]]]: ...


class Set__bool(_typing.AbstractSet[bool], _typing.Hashable):
    def __init__(self, items: _typing.AbstractSet[bool]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def isdisjoint(self, other: _typing.AbstractSet[bool]) -> bool: ...
    def union(self, other: _typing.AbstractSet[bool]) -> 'Set__bool': ...
    def intersection(self, other: _typing.AbstractSet[bool]) -> 'Set__bool': ...
    def difference(self, other: _typing.AbstractSet[bool]) -> 'Set__bool': ...
    def symmetric_difference(self, other: _typing.AbstractSet[bool]) -> 'Set__bool': ...
    def issubset(self, other: _typing.AbstractSet[bool]) -> bool: ...
    def issuperset(self, other: _typing.AbstractSet[bool]) -> bool: ...
    def __iter__(self) -> _typing.Iterator[bool]: ...


class Set__Set__bool(_typing.AbstractSet[_typing.AbstractSet[bool]], _typing.Hashable):
    def __init__(self, items: _typing.AbstractSet[_typing.AbstractSet[bool]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def isdisjoint(self, other: _typing.AbstractSet[_typing.AbstractSet[bool]]) -> bool: ...
    def union(self, other: _typing.AbstractSet[_typing.AbstractSet[bool]]) -> 'Set__Set__bool': ...
    def intersection(self, other: _typing.AbstractSet[_typing.AbstractSet[bool]]) -> 'Set__Set__bool': ...
    def difference(self, other: _typing.AbstractSet[_typing.AbstractSet[bool]]) -> 'Set__Set__bool': ...
    def symmetric_difference(self, other: _typing.AbstractSet[_typing.AbstractSet[bool]]) -> 'Set__Set__bool': ...
    def issubset(self, other: _typing.AbstractSet[_typing.AbstractSet[bool]]) -> bool: ...
    def issuperset(self, other: _typing.AbstractSet[_typing.AbstractSet[bool]]) -> bool: ...
    def __iter__(self) -> _typing.Iterator[_typing.AbstractSet[bool]]: ...


class Set__Set__Set__bool(_typing.AbstractSet[_typing.AbstractSet[_typing.AbstractSet[bool]]], _typing.Hashable):
    def __init__(self, items: _typing.AbstractSet[_typing.AbstractSet[_typing.AbstractSet[bool]]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def isdisjoint(self, other: _typing.AbstractSet[_typing.AbstractSet[_typing.AbstractSet[bool]]]) -> bool: ...
    def union(self, other: _typing.AbstractSet[_typing.AbstractSet[_typing.AbstractSet[bool]]]) -> 'Set__Set__Set__bool': ...
    def intersection(self, other: _typing.AbstractSet[_typing.AbstractSet[_typing.AbstractSet[bool]]]) -> 'Set__Set__Set__bool': ...
    def difference(self, other: _typing.AbstractSet[_typing.AbstractSet[_typing.AbstractSet[bool]]]) -> 'Set__Set__Set__bool': ...
    def symmetric_difference(self, other: _typing.AbstractSet[_typing.AbstractSet[_typing.AbstractSet[bool]]]) -> 'Set__Set__Set__bool': ...
    def issubset(self, other: _typing.AbstractSet[_typing.AbstractSet[_typing.AbstractSet[bool]]]) -> bool: ...
    def issuperset(self, other: _typing.AbstractSet[_typing.AbstractSet[_typing.AbstractSet[bool]]]) -> bool: ...
    def __iter__(self) -> _typing.Iterator[_typing.AbstractSet[_typing.AbstractSet[bool]]]: ...


class Set__List__i32(_typing.AbstractSet[_typing.Sequence[int]], _typing.Hashable):
    def __init__(self, items: _typing.AbstractSet[_typing.Sequence[int]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def isdisjoint(self, other: _typing.AbstractSet[_typing.Sequence[int]]) -> bool: ...
    def union(self, other: _typing.AbstractSet[_typing.Sequence[int]]) -> 'Set__List__i32': ...
    def intersection(self, other: _typing.AbstractSet[_typing.Sequence[int]]) -> 'Set__List__i32': ...
    def difference(self, other: _typing.AbstractSet[_typing.Sequence[int]]) -> 'Set__List__i32': ...
    def symmetric_difference(self, other: _typing.AbstractSet[_typing.Sequence[int]]) -> 'Set__List__i32': ...
    def issubset(self, other: _typing.AbstractSet[_typing.Sequence[int]]) -> bool: ...
    def issuperset(self, other: _typing.AbstractSet[_typing.Sequence[int]]) -> bool: ...
    def __iter__(self) -> _typing.Iterator[_typing.Sequence[int]]: ...


class Set__string(_typing.AbstractSet[str], _typing.Hashable):
    def __init__(self, items: _typing.AbstractSet[str]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def isdisjoint(self, other: _typing.AbstractSet[str]) -> bool: ...
    def union(self, other: _typing.AbstractSet[str]) -> 'Set__string': ...
    def intersection(self, other: _typing.AbstractSet[str]) -> 'Set__string': ...
    def difference(self, other: _typing.AbstractSet[str]) -> 'Set__string': ...
    def symmetric_difference(self, other: _typing.AbstractSet[str]) -> 'Set__string': ...
    def issubset(self, other: _typing.AbstractSet[str]) -> bool: ...
    def issuperset(self, other: _typing.AbstractSet[str]) -> bool: ...
    def __iter__(self) -> _typing.Iterator[str]: ...


_List__Set__stringT = _typing.TypeVar('_List__Set__stringT', bound=_typing.Sequence[_typing.AbstractSet[str]])


class List__Set__string(_typing.Sequence[_typing.AbstractSet[str]], _typing.Hashable):
    def __init__(self, items: _typing.Sequence[_typing.AbstractSet[str]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    @_typing.overload
    def __getitem__(self, i: int) -> _typing.AbstractSet[str]: ...
    @_typing.overload
    def __getitem__(self, s: slice) -> _typing.Sequence[_typing.AbstractSet[str]]: ...
    def count(self, item: _typing.Any) -> int: ...
    def index(self, item: _typing.Any, start: int = ..., stop: int = ...) -> int: ...
    def __add__(self, other: _typing.Sequence[_typing.AbstractSet[str]]) -> 'List__Set__string': ...
    def __radd__(self, other: _List__Set__stringT) -> _List__Set__stringT: ...
    def __reversed__(self) -> _typing.Iterator[_typing.AbstractSet[str]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.AbstractSet[str]]: ...


class Map__List__Set__string_string(_typing.Mapping[_typing.Sequence[_typing.AbstractSet[str]], str], _typing.Hashable):
    def __init__(self, items: _typing.Mapping[_typing.Sequence[_typing.AbstractSet[str]], str]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __getitem__(self, key: _typing.Sequence[_typing.AbstractSet[str]]) -> str: ...
    def __iter__(self) -> _typing.Iterator[_typing.Sequence[_typing.AbstractSet[str]]]: ...


class Map__Set__List__i32_Map__List__Set__string_string(_typing.Mapping[_typing.AbstractSet[_typing.Sequence[int]], _typing.Mapping[_typing.Sequence[_typing.AbstractSet[str]], str]], _typing.Hashable):
    def __init__(self, items: _typing.Mapping[_typing.AbstractSet[_typing.Sequence[int]], _typing.Mapping[_typing.Sequence[_typing.AbstractSet[str]], str]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __getitem__(self, key: _typing.AbstractSet[_typing.Sequence[int]]) -> _typing.Mapping[_typing.Sequence[_typing.AbstractSet[str]], str]: ...
    def __iter__(self) -> _typing.Iterator[_typing.AbstractSet[_typing.Sequence[int]]]: ...


_List__Foo__i64T = _typing.TypeVar('_List__Foo__i64T', bound=_typing.Sequence[int])


class List__Foo__i64(_typing.Sequence[int], _typing.Hashable):
    def __init__(self, items: _typing.Sequence[int]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    @_typing.overload
    def __getitem__(self, i: int) -> int: ...
    @_typing.overload
    def __getitem__(self, s: slice) -> _typing.Sequence[int]: ...
    def count(self, item: _typing.Any) -> int: ...
    def index(self, item: _typing.Any, start: int = ..., stop: int = ...) -> int: ...
    def __add__(self, other: _typing.Sequence[int]) -> 'List__Foo__i64': ...
    def __radd__(self, other: _List__Foo__i64T) -> _List__Foo__i64T: ...
    def __reversed__(self) -> _typing.Iterator[int]: ...
    def __iter__(self) -> _typing.Iterator[int]: ...


_List__Bar__doubleT = _typing.TypeVar('_List__Bar__doubleT', bound=_typing.Sequence[float])


class List__Bar__double(_typing.Sequence[float], _typing.Hashable):
    def __init__(self, items: _typing.Sequence[float]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    @_typing.overload
    def __getitem__(self, i: int) -> float: ...
    @_typing.overload
    def __getitem__(self, s: slice) -> _typing.Sequence[float]: ...
    def count(self, item: _typing.Any) -> int: ...
    def index(self, item: _typing.Any, start: int = ..., stop: int = ...) -> int: ...
    def __add__(self, other: _typing.Sequence[float]) -> 'List__Bar__double': ...
    def __radd__(self, other: _List__Bar__doubleT) -> _List__Bar__doubleT: ...
    def __reversed__(self) -> _typing.Iterator[float]: ...
    def __iter__(self) -> _typing.Iterator[float]: ...


_List__Baz__i32T = _typing.TypeVar('_List__Baz__i32T', bound=_typing.Sequence[int])


class List__Baz__i32(_typing.Sequence[int], _typing.Hashable):
    def __init__(self, items: _typing.Sequence[int]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    @_typing.overload
    def __getitem__(self, i: int) -> int: ...
    @_typing.overload
    def __getitem__(self, s: slice) -> _typing.Sequence[int]: ...
    def count(self, item: _typing.Any) -> int: ...
    def index(self, item: _typing.Any, start: int = ..., stop: int = ...) -> int: ...
    def __add__(self, other: _typing.Sequence[int]) -> 'List__Baz__i32': ...
    def __radd__(self, other: _List__Baz__i32T) -> _List__Baz__i32T: ...
    def __reversed__(self) -> _typing.Iterator[int]: ...
    def __iter__(self) -> _typing.Iterator[int]: ...


IndirectionA = int
IndirectionC = int
IndirectionB = float
