## edge of stage
stageEdgePositions = [["Left Edge", -68.40000, 0], ["Right Edge",  68.40000, 0]]
## edge of platforms
platformEdgePositions = [["Left Platform Left Side", -57.60000, 0], ["Left Platform Right Side", -20.00000, 0], 
["Top Platform Left Side",-18.80000, 0], ["Top Platform Right Side", 18.80000, 0], 
["Right Platform Left Side", 20.00000, 0], ["Right Platform Right Side", 57.60000, 0]]
## Normal getup, Attack getup, Roll getup, Jump from ledge, roll backwards from ledge
ledgeGetupPositions = [["Normal Getup Right Ledge", 59.42806, 32], ["Normal Getup Left Ledge", -59.42806, 32], 
["Roll Getup Right Ledge", 31.41302, 49], ["Roll Getup Left Ledge", -31.41302, 49], 
["Attack Getup Right Ledge", 58.43898, 53], ["Attack Getup Left Ledge",-58.43898, 53], 
["Jump From Right Ledge", 40.09690, 39], ["Jump From Left Ledge", -40.09690, 39], 
["Roll Back From Right Ledge", 31.84238, 31], ["Roll Back From Left Ledge", -31.84238, 31],
["Roll Forward From Right Ledge", 31.72763, 30], ["Roll Forward From Left Ledge", -31.72763, 30],
["Jump Right Ledge Drop", 30.95691, 54],["Jump Left Ledge Drop", -30.95691, 54],
["RPlat RSide UpB Up and In (9.875)", 8.56001, 41],["LPlat LSide UpB Up and In (9.875)", -8.56001, 41],
["RPlat LSide UpB Up and In (9.875)", -43.98697, 67],["LPlat RSide UpB Up and In (9.875)", 43.98697, 67],
["RSide UpB Up and In (9.875)", -2.72699, 81],["LSide UpB Up and In (9.875)", 2.72699, 81]]

## roll forward, roll backward, UpB once sideways, SideB perfect, 1 frame dash
movements = [["roll forward right", 36.67236, 30], ["roll forward left",-36.67236, 30], 
["roll backward right", 33.30000, 31], ["roll backward left", -33.30000, 31], 
["UpB right (.9875)", 54.14999, 69], ["UpB left (.9875)", -54.14999, 69],
["SideB perfect right", 59.16667, 98], ["SideB perfect left", -59.16667, 98],
["1 frame dash right", 17.09999, 20],  ["1 frame dash left", -17.09999, 20], 
["UpB right (1.0)", 54.42598, 69], ["UpB left (1.0)", -54.42598, 69],
["UpB right (0.95, 0.2875)", 64.813, 69], ["UpB left (0.95, 0.2875)", -64.813, 69],
["Perfect Wavedash Right (0.2875)", 25.35864, 25], ["Perfect Wavedash Left (0.2875)", -25.35864, 25],
["Double UpB RightLeft (1.0)", 0.98221, 82], ["Double UpB LeftRight (1.0)", -0.98221, 82],
["Double UpB Right (.9875)", 97.50349, 83], ["Double UpB Right (1.0)", 97.73348, 83], 
["Double UpB RightLeft (.9875)", 0.99651, 82], ["Double UpB LeftRight (.9875)", -0.99651, 82]]

## Outer coordinates that do not work but between each could be working coordinates
workingLocations = [[60.01245, 60.10439], [39.80777, 39.91275], [19.60359, 19.70501], [-0.60809, -0.5022], [-20.80922, -20.70017], [-41.02284, -40.91284], [-61.22290, -61.08696],
[-60.01245, -60.10439], [-39.80777, -39.91275], [-19.60359, -19.70501], [0.60809, 0.5022], [20.80922, 20.70017], [41.02284, 40.91284], [61.22290, 61.08696]]

def off_stage(position):
    return position < stageEdgePositions[0][1] or position > stageEdgePositions[1][1]

def working_position(position):
    for workingPosition in workingLocations:
        if (position > workingPosition[0] and position < workingPosition[1]):
            return True

    return False

def off_stage_test():
    print("69 true=" + str(off_stage(69)))
    print("68.4 false=" + str(off_stage(68.4)))
    print("68.3 false=" + str(off_stage(68.3)))
    print("-69 true=" + str(off_stage(-69)))
    print("-68.4 false=" + str(off_stage(-68.4)))
    print("-68.3 false=" + str(off_stage(-68.3)))

def working_position_test():
    print("60.01245 false" + str(working_position(60.01245)))
    print("60.01244 false" + str(working_position(60.01244)))
    print("39.80777 false" + str(working_position(39.80777)))
    print("39.80778 true" + str(working_position(39.80778)))
    print("39.91274 true" + str(working_position(39.91274)))
    print("39.91275 false" + str(working_position(39.91275)))
    print("39.91276 false" + str(working_position(39.91276)))