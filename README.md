What is this ?
==============

A fork of https://github.com/jeremyw/stamp, written in Python

Usage:
======

Use `pystamp.format_like` to format your date, datetime and time

Example
=======

```python

>>> from pystamp.pystamp import format_like
>>> import datetime
>>>
>>> example = datetime.date(2010, 10, 10)
>>> format_like(example, "March 10, 2010")
>>> "October 10, 2010"
```
