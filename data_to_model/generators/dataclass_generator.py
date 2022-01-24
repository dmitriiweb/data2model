from typing import List

from data_to_model.generators.base_generator import BaseGenerator

from ._types import ClassData, ClassField


class DataClassGenerator(BaseGenerator):
    def generate_file_content(self) -> str:
        self.content.extend(
            ["from dataclasses import dataclass", "from typing import Any, Dict\n\n"]
        )

        for class_ in self.classes:
            self._add_class_content(class_)

        content = "\n".join(self.content)
        content += "\n"
        print(content)
        return content

    def _add_class_content(self, class_: ClassData) -> None:
        self.content.append(f"@dataclass\nclass {class_.name}:")
        self._add_fields_data(class_.fields)
        self._add_methods(class_)

    def _add_fields_data(self, fields: List[ClassField]) -> None:
        for field in fields:
            self.content.append(f"    {field.name}: {field.type}")

    def _add_methods(self, class_: ClassData) -> None:
        self._add_from_dict_method(class_)
        self._add_to_dict_method(class_)

    def _add_from_dict_method(self, class_: ClassData) -> None:
        self.content.append("\n    @classmethod")
        self.content.append(
            f'    def from_dict(cls, data: Dict[str, Any]) -> "{class_.name}":'
        )
        for field in class_.fields:
            getter = self.generate_dict_getter(field)
            self.content.append(f"        {getter}")

        return_statements = ", ".join([f"{i.name}={i.name}" for i in class_.fields])
        self.content.append(f"        return cls({return_statements})")

    def _add_to_dict_method(self, class_: ClassData) -> None:
        pass

    @staticmethod
    def generate_dict_getter(field: ClassField) -> str:
        types = {"str", "int", "float", "bool"}
        if field.type not in types:
            return f'{field.name} = data["{field.original_name}"]'

        return f'{field.name} = {field.type}(data["{field.original_name}"])'
