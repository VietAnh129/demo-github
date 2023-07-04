from typing import Any, Optional
from typing import Tuple


class WebSelector:

    def __init__(self, locator: str, **kwargs: Optional[Any]) -> None:
        if len(locator) == 0:
            raise Exception('Chưa có locator')
        self.locator = locator.format(**kwargs)
    @staticmethod
    def auto_parse_locator(value) -> Tuple[str, str]:
        if value.startswith('/'):
            return 'xpath', value
        return 'id', value

    def get_locator(self) -> Tuple[str, str]:
        return self.auto_parse_locator(self.locator)
