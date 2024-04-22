#!/usr/bin/python3

def blob_callback(blob, metadata):
    if "__pycache__" in blob.path:
        return None
    return blob

