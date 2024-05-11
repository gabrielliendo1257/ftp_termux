import subprocess
import sys


class CheckDependencies:

    @staticmethod
    def exist_executables(dependencies):
        for dependency, exec in dependencies.items():
            subprocess.run(exec, text=True, shell=True)
            out = subprocess.run("powershell.exe $?", text=True, shell=True)
            if not bool(out):
                print(f"La dependencia ´{dependency}´ no se reconoce en su sistema.")
