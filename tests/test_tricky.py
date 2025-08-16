from utils4plans.lists import get_unique_items_in_list_keep_order
import pytest
from utils4plans.io import write_json
from pathlib import Path


def test_unique_items_and_keep_order():
    lst = ["j", "jk", "k", "k", "kl", "l", "l", "lm", "m"]
    res = get_unique_items_in_list_keep_order(lst)
    expected = ["j", "jk", "k", "kl", "l", "lm", "m"]
    assert res == expected


def test_write_json(tmp_path):
    obj = {"hi": 10, "bye":[1,2,3,4], "see": {"hi": "bye", 10: None}}
    write_json(obj, tmp_path, "test")
    # TODO assert that this completed? 



if __name__ == "__main__":
    pass