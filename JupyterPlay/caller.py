import sys    

import callee

print("I am the caller. This is caller.py. I have imported callee(.py) and will call the function [aardvark]")
callee.aardvark()
#print("In module products __package__, __name__ ==", __package__, __name__)
#print("In module products sys.path[0], __package__ ==", sys.path[0], __package__)