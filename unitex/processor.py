#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unitex import UnitexException, LOGGER



class UnitexProcessor:

    def __init__(self):
        raise NotImplementedError

    def open(self, path, mode=None, encoding=None):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

