import os
import LongLatToKmConverter
import math
import LinkScoreCalculator

class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.listOfPairs = []
        self.linkScoreCalculator = LinkScoreCalculator.LinkScoreCalculator()
        

    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
                getTownCount = len(content.splitlines())
                line1 = 0
                line2 = 0
                linkScore = 0.0
        
                while line1 < getTownCount - 1:
                    line2 = line1 + 1
                    #print(f"Processing Town {line1}")
                    line1Data = content.splitlines()[line1].split(",")
                    while line2 < getTownCount:
                        line2Data = content.splitlines()[line2].split(",")
                        pairPop = int(line1Data[1]) + int(line2Data[1])
                        pairDist = LongLatToKmConverter.LongLatToKmConverter().convert(float(line1Data[2]), float(line1Data[3]), float(line2Data[2]), float(line2Data[3]))

                        linkScore = self.linkScoreCalculator.calculate_link_score(pairPop, pairDist)
                        self.listOfPairs.append([line1Data[0], line2Data[0], pairPop, pairDist, linkScore])
                        #print(f"{line1Data[0]} to {line2Data[0]}: Combined Population = {pairPop}, Distance = {pairDist}")
        
                        line2 += 1
                    line1 += 1
                return self.listOfPairs
        except FileNotFoundError:
            print(f"Error: The file {self.file_path} was not found.")
            return None
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return None



        