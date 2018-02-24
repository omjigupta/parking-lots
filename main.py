from parking import ParkingLot
from settings import Settings

def check_command_type(line, parking_lot):
    ''' Check if command is correct or not
        if correct call parkingLot methods for specified task
    '''
    try:
        command = line.split()
        if command[0] == "create_parking_lot":
            parking_lot.create_parking(command[1])
        elif command[0] == "park":
            try:
                parking_lot.do_parking(command[1], command[2])
            except Exception as e:
                print("arguments with park command are not proper")
        else:
            print(" Wrong Command!!! Please check it.")
    except Exception as e:
        print(" Wrong Command!!! Please check it. ")



# Only work when called by terminal (not as module)
if __name__ == "__main__":
    parking_lot = ParkingLot()
    input_type = Settings()

    try:
        # When Input is file
        if input_type.get_input_type():
            # read input from text file
            with open(input_type.get_input_file()) as inps:
                for inp_line in inps:
                    check_command_type(inp_line, parking_lot)
        # When Input is from terminal
        else:
            while(1):
                print("Type exit/Exit/EXIT for exit !!")
                inp_line = input("Input:  ")
                if 'exit' == inp_line or 'Exit' == inp_line or 'EXIT' == inp_line:
                    print("Good Bye !!")
                    print("*** Milte hai phir se *** "*5)
                    break
                else:
                    check_command_type(inp_line, parking_lot)
    except Exception as e:
        print("Wrong INPUT TYPE,  Choose 1 for Input From File  or  Choose 0 for Input From Terminal !!!!")
