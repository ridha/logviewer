# -*- coding: utf-8 -*-

import asyncio
import os
import sys


class AsyncTail:

    def __init__(self, filepath=None):
        self.file_obj = sys.stdin if filepath is None else open(filepath)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        self.file_obj.close()

    async def __aiter__(self):
        async for line in self.tail():
            yield line

    async def tail(self):
        if self.file_obj is not sys.stdin:
            self.file_obj.seek(0, os.SEEK_END)
        while True:
            try:
                line = self.file_obj.readline()
                if not line:
                    await asyncio.sleep(0.01)
                else:
                    yield line
            except (ValueError, KeyboardInterrupt):
                break
