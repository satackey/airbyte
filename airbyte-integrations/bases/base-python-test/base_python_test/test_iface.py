"""
MIT License

Copyright (c) 2020 Airbyte

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from typing import List

from airbyte_protocol import ConfiguredAirbyteCatalog, ConnectorSpecification


class StandardSourceTestIface(object):
    def __init__(self):
        pass

    def get_spec(self) -> ConnectorSpecification:
        raise Exception("Not Implemented")

    def get_config(self) -> object:
        raise Exception("Not Implemented")

    def get_catalog(self) -> ConfiguredAirbyteCatalog:
        raise Exception("Not Implemented")

    def get_regex_tests(self) -> List[str]:
        return []

    def get_state(self) -> object:
        return {}

    def setup(self) -> None:
        pass

    def tear_down(self) -> None:
        pass
