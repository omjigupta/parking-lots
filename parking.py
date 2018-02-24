
class Car():
    def __init__(self, reg_number, color):
        ''' Initialize basic parameters of Car '''

        self.reg_number = reg_number
        self.color = color
    def __str__(self):
        return self.reg_number


class ParkingLot():
    def __init__(self):
        ''' Initialize basic parameters of parking lot '''

        # Total No. of slots
        self.max_slot = 0
        # Free slots list
        self.avail_slots = []
        # save slot:car mapping (dict)
        self.car_slot = {}
        # save reg_number:slot mapping
        self.reg_slot = {}
        # save color:reg_number mapping
        self.col_reg = {}

    def create_parking(self, N):
        ''' Create new parking lot and assign total parking spaces '''
        try:
            self.max_slot = int(N)
        except Exception as e:
            print("Invalid slot number. Please give valid number!!!")
        for i in range(1, self.max_slot+1):
            self.avail_slots.append(i)
        print("Created a parking lot with " + str(self.max_slot) + " slots")
