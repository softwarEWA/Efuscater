import sys
import os

print("\nEfuscater için gereken kütüphaneler indiriliyor:")

# Common libraries to install on both platforms
gereken_kutuphaneler = [
     "pprint",
]

# Function to install libraries on Windows
def windows_kutuphanelerini_indir(libs):
    for lib in libs:
        os.system(f"pip install {lib}")

# Function to install libraries on Linux
def install_libraries_linux(libs):
    for lib in libs:
        os.system(f"pip3 install {lib}")

# Platform-specific installation
if sys.platform.startswith("win"):
    print("WINDOWS")
    os.system("python.exe -m pip install --upgrade pip")
    os.system("pip install --upgrade pip setuptools wheel")
    windows_kutuphanelerini_indir(gereken_kutuphaneler)
    print("Finish.")
    os.system("python Efuscater.py")

elif sys.platform.startswith("linux"):
    print("LINUX")
    os.system("python3 -m pip install --upgrade pip")
    os.system("pip3 install --upgrade pip setuptools wheel")
    install_libraries_linux(gereken_kutuphaneler)
    print("Finish.")
    os.system("python3 Efuscater.py")
