
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

    def do_parking(self, reg_number, color):
        ''' Park car in parking with given registration number and color'''

        if (self.max_slot == 0):
            print("Parking lot is under construction")
        elif (len(self.car_slot) == self.max_slot):
            print("Sorry, parking lot is full")
        else:
            if reg_number in self.reg_slot:
                print("Car with given Register Number is already parked ")
                return
            car = Car(reg_number, color)
            # Sort the available slots, assign minimum number slot
            self.avail_slots = list(sorted(self.avail_slots))
            slot = self.avail_slots[0]
            self.car_slot.update({slot:car})
            self.reg_slot.update({reg_number:slot})
            if self.col_reg.get(color, False):
                self.col_reg.get(color).append(str(reg_number))
            else:
                self.col_reg[color] = [str(reg_number)]
            print("Allocated slot number:",slot)
            self.avail_slots.pop(0)
