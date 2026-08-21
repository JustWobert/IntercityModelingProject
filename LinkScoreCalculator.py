class LinkScoreCalculator:


    def __init__ (self):
        with open('weights.txt', 'r') as f:
            self.weights = [float(line.strip()) for line in f]
            
            self.distanceMinimumWeight = self.weights[0]
            self.distanceScaleWeight = self.weights[1]
            self.distancePowerModifierWeight = self.weights[2]
            self.distancePowerWeight = self.weights[3]

            self.populationMinimumWeight = self.weights[4]
            self.populationScaleWeight = self.weights[5]
            self.populationPowerModifierWeight = self.weights[6]
            self.populationPowerWeight = self.weights[7]

    def distance_score(self, distance, minValue, scaleValue, powerModifier, powerValue):
        return(minValue+scaleValue**(powerModifier-powerValue*distance))

    def population_score(self, population, minValue, scaleValue, powerModifier, powerValue):
        return(minValue+scaleValue**(powerModifier+powerValue*population))

    def calculate_link_score(self, distance, population):
        distanceScore = self.distance_score(distance, self.distanceMinimumWeight, self.distanceScaleWeight, self.distancePowerModifierWeight, self.distancePowerWeight)
        populationScore = self.population_score(population, self.populationMinimumWeight, self.populationScaleWeight, self.populationPowerModifierWeight, self.populationPowerWeight)

        return distanceScore * populationScore        