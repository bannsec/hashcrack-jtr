
import logging
import tempfile
import platform
import os
import lzma
import shutil
import tarfile
import sys
import subprocess
from .config import HERE, PLATFORM

class John:

    def __init__(self, name=None):
        """Meant to be used as a "with" statement.
        
        Example:

            # Extracts appropriate john, then removes it
            with John("zip2john.exe") as j:
                subprocess.check_output([j, something])
        """
        self.name = name or "john.exe" # Because nix doesn't care about extensions

    def _enter_windows(self):
        with tarfile.open(os.path.join(HERE, "static", "john.tar.xz"), "r") as src:
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(src, self._dir_path)

        orig = os.path.join(self._dir_path, "john.exe")
        self.path = os.path.join(self._dir_path, self.name)

        os.rename(orig, self.path)

    def _enter_unix(self):
        self.path = os.path.join(self._dir_path, self.name)

        with tarfile.open(os.path.join(HERE, "static", "john.tar.xz"), "r") as src:
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(src, self._dir_path)

        orig = os.path.join(self._dir_path, "john.exe")
        self.path = os.path.join(self._dir_path, self.name)
        os.rename(orig, self.path)

        os.chmod(self.path, 0o500)

    def __enter__(self):

        self._dir_path = tempfile.mkdtemp()

        if platform.uname().system == "Windows":
            self._enter_windows()

        else:
            self._enter_unix()

        return self.path

    def __exit__(self, *args):
        shutil.rmtree(self._dir_path)

#
# Runners for cli bindings 
#

def cli_john():
    args = [] if len(sys.argv) == 1 else sys.argv[1:]
    
    with John() as john:
        subprocess.run([john] + args)

def cli_zip2john():
    args = [] if len(sys.argv) == 1 else sys.argv[1:]
    
    with John('zip2john.exe' if PLATFORM == "Windows" else "zip2john") as john:
        subprocess.run([john] + args)

def cli_rar2john():
    args = [] if len(sys.argv) == 1 else sys.argv[1:]
    
    with John('rar2john.exe' if PLATFORM == "Windows" else "rar2john") as john:
        subprocess.run([john] + args)

def cli_gpg2john():
    args = [] if len(sys.argv) == 1 else sys.argv[1:]
    
    with John('gpg2john.exe' if PLATFORM == "Windows" else "gpg2john") as john:
        subprocess.run([john] + args)

def cli_unafs():
    args = [] if len(sys.argv) == 1 else sys.argv[1:]
    
    with John('unafs.exe' if PLATFORM == "Windows" else "unafs") as john:
        subprocess.run([john] + args)

def cli_undrop():
    args = [] if len(sys.argv) == 1 else sys.argv[1:]
    
    with John('undrop.exe' if PLATFORM == "Windows" else "undrop") as john:
        subprocess.run([john] + args)

def cli_unshadow():
    args = [] if len(sys.argv) == 1 else sys.argv[1:]
    
    with John('unshadow.exe' if PLATFORM == "Windows" else "unshadow") as john:
        subprocess.run([john] + args)

LOGGER = logging.getLogger(__name__)
