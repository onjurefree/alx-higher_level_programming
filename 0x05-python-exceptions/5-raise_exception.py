#!/usr/bin/python3

def raise_exception():
    try:
        raise TypeError("Exception")
    except Exception:
        raise
