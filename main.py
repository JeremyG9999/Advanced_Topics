import os
import time
from scripts.ML_Random_Forests import TitanicClassifier
from scripts.multi_threader_parser import ThreadedParsing
from scripts.web_crawler import WebCrawler

class Menu:
    def main_menu(self):
        while True:
            print("\nSelect a program to run:")
            print("1. Titanic Classifier")
            print("2. Threaded Int Parsing")
            print("3. Web Crawler")
            print("4. Clear Terminal")
            print("5. Exit")
            option = input("Enter your choice: ")
            if option == "1":
                self.cls()
                TitanicClassifier.main()
            elif option == "2":
                self.cls()
                ThreadedParsing.main()
            elif option == "3":
                self.cls()
                WebCrawler.main()
            elif option == "4":
                self.cls()
            elif option == "5":
                break
            else:
                print("Invalid choice.")

    def cls(self):
        time.sleep(0.2)
        os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    Menu().main_menu()
