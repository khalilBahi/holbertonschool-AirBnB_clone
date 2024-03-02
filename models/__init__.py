#!/usr/bin/python3
"""
Initialization module
 
"""

from models.engine.file_storage import FileStorage

# Initialize FileStorage instance
storage = FileStorage()
storage.reload()
