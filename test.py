import os
import re
import time
import shutil
import subprocess
from subprocess import Popen, PIPE

try:
	 subprocess.call(["java", "assignment2"])
except Exception, e:
	raise e
finally:
	pass