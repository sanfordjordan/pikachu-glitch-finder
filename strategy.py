class Strategy:

    def __init__(self, strategyList):
        self.strategyList = strategyList
        self.finalPosition = self.calculate_final_position(strategyList)
        self.moves = len(strategyList)-1
        self.totalFrames = self.calculate_total_frames(strategyList)

    def calculate_final_position(self, strategyList):
        finalPosition = 0
        for move in strategyList:
            finalPosition += move[1]

        return finalPosition

    def calculate_total_frames(self, strategyList):
        totalFrames = 0
        for move in strategyList:
            totalFrames += move[2]

        return totalFrames