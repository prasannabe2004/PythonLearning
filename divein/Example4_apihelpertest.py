#!/usr/bin/python
import logging

def info(myobject, spacing=10, collapse=1, methodtype=1):
	"""Print methods and doc strings.

	Takes module, class, list, dictionary, or string."""
	methodList = [e for e in dir(myobject) if callable(getattr(myobject, e))]
	if methodtype == 1:
		processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
		print "\n".join(["%s %s" %
						 (method.ljust(spacing),
							  processFunc(str(getattr(myobject, method).__doc__)))
						 for method in methodList])
	else:
		# collapse is not working
		print "\n".join(["%s %s" % (method.ljust(spacing), \
			(" ".join((str(getattr(myobject,method).__doc__).split())))) \
			for method in methodList])


if __name__ == "__main__":
	info(logging,spacing=30,collapse=0,methodtype=2)