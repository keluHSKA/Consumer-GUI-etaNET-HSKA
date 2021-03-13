import csv
import random
import time

class liveDataGenerator(object):
    def liveDataGen(self):
        Nr = 0
        Temperature = 100
        Duration = 120

        fieldnames =["Nr","Temperature","Duration in min"]
        with open('tableData.csv','w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
        i = 0
        while i <=5:
            with open('tableData.csv','a') as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                info ={
                    "Nr": Nr,
                    "Temperature": Temperature,
                    "Duration in min": Duration,
                }
                csv_writer.writerow(info)
                print(Nr, Temperature, Duration)
                Nr = Nr + 1
                Temperature = Temperature+random.randint(-20,20)
                Duration = Duration + random.randint(-20, 20)
            i = i+1
            time.sleep(1)

if __name__ == '__main__':
    myGen = liveDataGenerator
    myGen.liveDataGen(None)
