from dataclasses import dataclass
from typing import List


class NameFormatter:
    def __init__(self, original_name: str):
        self.original_name = original_name
        self.formatted_chars: List[str] = []

    def format(self) -> str:
        for idx, current_char in enumerate(self.original_name):
            self._format_current_char(current_char, idx)

        return "".join(self.formatted_chars)

    def _format_current_char(self, current_char: str, idx: int) -> None:
        if not current_char.isalpha() and not current_char.isdigit():
            self.formatted_chars.append("_")

        elif current_char.isdigit() and idx == 0:
            self.formatted_chars.append(f"_{current_char}")

        elif current_char.isupper():
            self.formatted_chars.append(self._format_upper(current_char, idx))

        else:
            self.formatted_chars.append(current_char)

    def _format_upper(self, upper: str, idx: int) -> str:
        prev_char = self._get_char_by_idx(idx - 1)
        next_char = self._get_char_by_idx(idx + 1)

        if idx == 0 or idx == len(self.original_name) - 1:
            return upper.lower()

        if prev_char.isupper() and not next_char.isupper():
            return f"{upper.lower()}_"

        if not prev_char.isupper():
            return f"_{upper.lower()}"

        return upper.lower()

    def _get_char_by_idx(self, idx: int) -> str:
        if idx < 0:
            return ""
        try:
            return self.original_name[idx]
        except IndexError:
            return ""


@dataclass()
class ClassField:
    original_name: str
    type: str

    @property
    def name(self) -> str:
        formatter = NameFormatter(self.original_name)
        return formatter.format()
