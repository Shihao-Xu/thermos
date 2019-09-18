activate_this = '/root/thermos/venv/Scripts/activate_this.py'  
with open(activate_this) as file_:  
	exec(file_.read(), dict(__file__=activate_this))  
  
import sys  
sys.path.insert(0, '/root/thermos')  
from __init__ import app as application 