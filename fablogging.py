import logging
from fabulous.color import *
import re

class CFormatter(logging.Formatter):

	cheader = {
		logging.DEBUG: lambda x: bold(blue(x)),
		logging.INFO: lambda x: bold(green(x)),
		logging.WARNING: lambda x: bold(yellow(x)),
		logging.ERROR: lambda x: bold(red(x)),
		logging.CRITICAL: lambda x: bold(highlight_red(x))
	}


	def __init__(self, fmt='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S'):
		logging.Formatter.__init__(self, fmt, datefmt)


	def format(self, record):

		# Save the original format configured by the user
		# when the logger formatter was instantiated
		format_orig = self._fmt
		
		# Replace the original format with one customized by logging level
		parts = dict(before ="", after = "", levelname = "%(levelname)-8s")
		regex = re.compile("(?P<before>.*)(?P<levelname>%\(levelname\).*?s)(?P<after>.*)")
		r = regex.search(self._fmt)
		if r:
			parts.update(r.groupdict())

		self._fmt = str(bold(parts["before"]))+ str(self.cheader[record.levelno](parts["levelname"])) + parts["after"]


		# Call the original formatter class to do the grunt work
		result = logging.Formatter.format(self, record)

		# Restore the original format configured by the user
		self._fmt = format_orig

		return result
	
def getLogger(modulename = "", format = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG):
	fmt = CFormatter(format, datefmt)
	hdlr = logging.StreamHandler(sys.stdout)
	hdlr.setFormatter(fmt)
	logger = logging.getLogger(modulename)
	logger.addHandler(hdlr)
	logger.setLevel(level)

	return logger

