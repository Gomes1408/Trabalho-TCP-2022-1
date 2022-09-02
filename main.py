from sys import argv

def main(argv):
    print("Ola trabalho!")

    if(argv):
        print(f"Recuperou: {argv}")

if(__name__ == "__main__"):
    main(argv)