from typing import (
    Generic,
    Iterable,
    List,
    Type,
    TypeVar
)

T = TypeVar("T")


class BaseResponse(Generic[T]):
    def __init__(self, generic_type: Type[T]) -> None:
        self.generic_type = generic_type

    def get_typed_response_multi(self, objects: Iterable) -> List[T]:
        result = []

        if objects is not None:
            for obj in objects:
                result.append(self.generic_type.from_orm(obj))

        return result

    def get_typed_response_single(self, obj) -> T:
        if obj is None:
            return None

        return self.generic_type.from_orm(obj)
