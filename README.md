fablogging.py
=============

Python basic color logger based on logging and fabulous

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

