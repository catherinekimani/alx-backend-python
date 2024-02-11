#!/usr/bin/env python3
""" parametize a unit test """
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Tuple, Any, Dict
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap class """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self, nested_map: Dict[str, Any], path: Tuple[str], expected: Any
    ) -> None:
        """ TestAccessNestedMap """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)),
                           ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(
        self, nested_map: Dict[str, Any], path: Tuple[str]
    ) -> None:
        """ TestAccessNestedMap """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ TestGetJson class """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("requests.get")
    def test_get_json(
        self, test_url: str, test_payload: Dict[str, Any], mock_get: Mock
    ) -> None:
        """ Mock HTTP calls """
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ TestMemoize class """
    def test_memoize(self) -> None:
        """ test_memoize"""
        class TestClass:
            """ TestClass """
            def a_method(self):
                """ a_method """
                return 42

            @memoize
            def a_property(self):
                """ a_property """
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mocked:
            tets_class = TestClass()
            self.assertEqual(tets_class.a_property, 42)
            self.assertEqual(tets_class.a_property, 42)
            mocked.assert_called_once()
