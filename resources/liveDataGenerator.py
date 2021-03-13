import csv
import random
import time

class liveDataGenerator(object):
    def liveDataGen(self):
        t_time = 0
        val1 = 100
        val2 = 120
        val3 = 40
        val4 = 40

        fieldnames =["t_time","val1","val2","val3","val4"]
        with open('data.csv','w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()

        while True:
            with open('data.csv','a') as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                info ={
                    "t_time": t_time,
                    "val1": val1,
                    "val2": val2,
                    "val3": val3,
                    "val4": val4
                }
                csv_writer.writerow(info)
                print(t_time, val1, val2, val3, val4)
                t_time = t_time + 1
                val1 = val1+random.randint(-20,20)
                val2 = val2 + random.randint(-20, 20)
                val3 = val3+random.randint(-5,5)
                val4 = val4 + random.randint(-5, 5)
            time.sleep(1)

if __name__ == '__main__':
    myGen = liveDataGenerator
    myGen.liveDataGen(None)
