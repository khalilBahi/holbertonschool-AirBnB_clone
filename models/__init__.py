#!/usr/bin/python3
"""
Initialization module

This module initializes a FileStorage instance called 'storage' and reloads it.
"""

from models.engine.file_storage import FileStorage

# Initialize FileStorage instance
storage = FileStorage()
storage.reload()
