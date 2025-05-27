import sys
import time
import threading

class ThreadedParsing:
    @staticmethod
    def main():
        sys.set_int_max_str_digits(1500000)
        digit_values = [100000, 500000]

        def times():
            for digits in digit_values:
                start = time.time()
                int('1' * digits)
                print(f"{digits} digits parsed in: {time.time() - start:.5f} seconds")

        threads = []
        for _ in range(1):
            thread = threading.Thread(target=times)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
