#!/usr/bin/python3
"""
magic method for models direcory
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
