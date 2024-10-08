import hashlib
import io
import os
import subprocess


class Utility(object):
    def parse_int(self, candidate_int):
        try:
            dummy_int = int(candidate_int)
        except ValueError:
            return False
        return True

    # https://docs.python.org/3/library/hashlib.html
    def get_hash_from_string(self, text_to_hash):
        print(text_to_hash)
        return hashlib.sha224(text_to_hash).hexdigest()

    def get_hash_from_file(self, file_to_hash):
        file_text = ""
        with io.open(file_to_hash, "rb") as f:
            chunk = 0
            while chunk != b'':
                chunk = file.read(1024)
            for line in f:
                file_text.__add__(line)
        print(self.get_hash_from_string(file_text))

    def files_are_same(self, file1, file2):
        digests = []
        for file in [file1, file2]:
            hash = hashlib.md5()
            with io.open(file, 'rb') as f:
                buf = f.read()
                hash.update(buf)
                a = hash.hexdigest()
                digests.append(a)

        return digests[0] == digests[1]

    def file_exists(self, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"no file [{filepath}]")

    # pylint: disable=R0201
    def run_subprocess(self, args_for_subprocess):
        """
            Execute subprocess.check_output().
            This is a separate method to allow mocking and to avoid needing to
            commit 3rd party software (specifically ExifTool) to Github, 
            just to allow testing by Github Actions.
        """
        exe = args_for_subprocess[0]
        try:
            result = subprocess.run(args_for_subprocess, capture_output=True)
        except (FileNotFoundError):
            print(f"Executable [{exe}] was not found.Exiting...")
            raise (FileNotFoundError)

        sout = str(result.stdout)
        serr = str(result.stdout)
        print(sout)
        print(serr)

        return sout

    def generate_self_assignments(self, line):
        #Extract the arguments from the function definition
        start = line.find("(") + 1
        end = line.find(")")
        args = line[start:end].split(", ")

        assignments = []
        for arg in args:
            if arg != 'self':
                assignments.append(f"self.{arg} = {arg}")

        return "\n".join(assignments)
    
