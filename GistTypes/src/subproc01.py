import subprocess

# test scenarios:
# 1. exe ok, other args ok. Result: CompletedArgs return is populated
# args = ["c:/temp/exiftool.exe","-subject","c:/temp/tpaste.jpg"]
# result = subprocess.run(args, capture_output=True)
# sout = str(result.stdout)
# serr = str(result.stderr)
# print(sout)
# print(serr)

# 2. exe bad, other args ok. 
# # Result: No file found exception
# exe = "c:/temp/xexiftool.exe"
# args = [exe,"-subject","c:/temp/tpaste.jpg"]
# try:
#     result = subprocess.run(args, capture_output=True)
# except(FileNotFoundError):
#     print(f"Executable [{exe}] was not found.Exiting...")


# 3. exe good, other args bad - 1. 
# # Result: stdout empty, stderr empty, returncode 0
# exe = "c:/temp/exiftool.exe"
# args = [exe,"-xsubject","c:/temp/tpaste.jpg"]
# try:
#     result = subprocess.run(args, capture_output=True)
# except(FileNotFoundError):
#     print(f"Executable [{exe}] was not found.Exiting...")

# sout = str(result.stdout)
# serr = str(result.stderr)
# print(sout)
# print(serr)


# 4. exe good, other args bad - 2. 
# # Result: returncode: 1,
# stderr: b'Error: File not found - c:/temp/xtpaste.jpg\r\n'
# stdout: empty

# exe = "c:/temp/exiftool.exe"
# args = [exe,"-subject","c:/temp/xtpaste.jpg"]
# try:
#     result = subprocess.run(args, capture_output=True)
# except(FileNotFoundError):
#     print(f"Executable [{exe}] was not found.Exiting...")

# sout = str(result.stdout)
# serr = str(result.stderr)
# print(sout)
# print(serr)

