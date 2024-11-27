import os
import platform

def shutdown():
    confirm = input("Are you sure you want to shut down the computer? (yes/no): ").strip().lower()
    if confirm == "yes":
        if platform.system() == "Windows":
            os.system("shutdown /s /t 0")  # Shut down immediately
        elif platform.system() in ["Linux", "Darwin"]:  # Linux or macOS
            os.system("sudo shutdown now")
        else:
            print("Unsupported operating system!")
    else:
        print("Shutdown canceled.")

shutdown()