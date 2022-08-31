import subprocess
import platform


# Installation script for pipreqs package
def install_pipreqs():
    python_executable = "venv/bin/python" if platform.system() != "Windows" else "venv/Scripts/python"

    subprocess.run([python_executable, "-m", "pip", "install", "pipreqs"])


def main():
    install_pipreqs()
    print("pipreqs installed.")


if __name__ == "__main__":
    main()
