import strategy as strat
import data

workingList = []

def main():
    startingPositions = data.stageEdgePositions + data.platformEdgePositions + data.ledgeGetupPositions
    for startingPosition in startingPositions:
        startingPositonFlow = [startingPosition] # form [[dfgd,34534]]
        make_movement(startingPosition[1], startingPositonFlow, 2)

    print_working_list()
    
def print_working_list():
    workingList.sort(key=lambda x: (x.totalFrames, x.moves, -x.finalPosition), reverse=False)

    for strategy in workingList:
        print("Frames: ", strategy.totalFrames, " Moves: ", strategy.moves, "\nPosition: ", round(strategy.finalPosition, 5), " Strategy: ", strategy.strategyList)

        
def make_movement(startPosition, startFlow, recursion):
    for movement in data.movements:
        position = startPosition + movement[1]  
        flow = [] + startFlow
        flow.append(movement) # form [[sdf,43534],[dfgd,34534]]

        if data.off_stage(position):
            continue
        if data.working_position(position):
            add_new_strategy(flow)
            continue
        
        if(recursion > 0):
            make_movement(position, flow, recursion-1)   

def add_new_strategy(flow):
    # Check if strategy with different order already exists
    for strategy in workingList:
        if(sorted(strategy.strategyList) == sorted(flow)):
            return

    # Check if the same move is used to go back and forth pointlessly
    for move1 in flow:
        for move2 in flow:
            if(move1[1] == -move2[1]):
                return

    newStrategy = strat.Strategy(flow)
    workingList.append(newStrategy)


    
def list_test():
    emptyList = []
    move = ["sdfds", 8.87989]
    flowList = [["sdfds", 8.87989],["df", 8.87989],["f", 8.87989]]

    flowList.append(move)
    print(flowList)
    emptyList.append(move)
    print(emptyList)


if __name__ == "__main__":
    main()