import os
import LongLatToKmConverter

class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.listOfPairs = []

    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print(f"Error: The file {self.file_path} was not found.")
            return None
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return None

        getTownCount = len(content.splitlines())
        line1 = 0
        line2 = 1

        while line1 < getTownCount - 1:
            line1Data = content.splitlines()[line1].split(",")
            while line2 < getTownCount:
                line2Data = content.splitlines()[line2].split(",")
                pairPop = toInt(line1Data[1]) + toInt(line2Data[1])
                pairDist = LongLatToKmConverter.convert(toFloat(line1Data[2]), toFloat(line1Data[3]), toFloat(line2Data[2]), toFloat(line2Data[3]))
                self.listOfPairs.append([line1Data[0], line2Data[0], pairPop, pairDist])

                line2 += 1
            line1 += 1
