from data_to_model.models import ClassData


def test_get_types_for_import(data_class_different_types: ClassData):
    types_for_import = data_class_different_types.get_types_for_import()
    assert len(types_for_import) == 4
    assert "Dict" in types_for_import
    assert "Optional" in types_for_import
    assert "List" in types_for_import
    assert "Any" in types_for_import
