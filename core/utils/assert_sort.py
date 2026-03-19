from typing import Callable, Any

def assert_sort(list_of_values: list, key_param: Callable[[Any], Any] | None = None, desc: bool = False):
   tmp_sorted_list = sorted(list_of_values, key = key_param, reverse = desc)
   assert list_of_values == tmp_sorted_list