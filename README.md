fablogging.py
=============

Python basic color logger based on logging, fabulous and [Stackoverflow](http://stackoverflow.com/a/8349076/1540120)

Prerequisites
-------------

pip install fabulous

Example
-------
```python

import fablogging

log = fablogging.getLogger('MyModule')

log.debug("debug msg")
log.info("info msg")
log.warning("warning msg")
log.error("error msg")
log.critical("critical msg")

```

