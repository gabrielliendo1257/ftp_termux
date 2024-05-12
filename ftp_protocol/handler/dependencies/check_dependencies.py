from typing import Dict
import subprocess


class CheckDependencies:

    @staticmethod
    def exist_executables(dependencies: Dict[str, str]):
        for dependency, exec in dependencies.items():
            out = subprocess.run(exec, text=True, shell=True, capture_output=True)
            if not out.stderr:
                print(f"La dependencia ´{dependency}´ esta en su sistema.")
            else:
                print(f"La dependencia ´{dependency}´ no se reconoce en su sistema.")
