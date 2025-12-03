from collections.abc import Mapping

type ValueType = Mapping[str, bool] | bool | None
type SubCategoryDict = Mapping[str, ValueType]
type SubCategoryType = SubCategoryDict | bool | None
type CategoryType = Mapping[str, SubCategoryType] | Mapping[str, ValueType] | bool | None
type PolicyType = Mapping[str, CategoryType]
