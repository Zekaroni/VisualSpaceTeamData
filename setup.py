try:
    import matplotlib
    import scipy
    print("Everything already set up.")
except ImportError:
    if input("Would you like to install the missing packages? (y|n) : "):
        import os
        os.system("pip install -r requirements.txt")
    else:
        print("Set up has been canceled")