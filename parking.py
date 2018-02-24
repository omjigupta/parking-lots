
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

    def leave_parking(self, dslot):
        ''' Empty specified parking lot '''
        if (self.max_slot == 0):
            print("Parking lot is under construction")
        elif dslot < 0  or dslot > self.max_slot:
            print("Parking slot number is wrong")
        elif (len(self.car_slot) > 0):
            lcar = self.car_slot.get(dslot, False)
            if lcar:
                self.car_slot.pop(dslot)
                self.reg_slot.pop(lcar.reg_number)
                colorlist = self.col_reg[lcar.color]
                if lcar.reg_number in colorlist:
                    colorlist.remove(lcar.reg_number)
                self.avail_slots.append(dslot)
                print("Slot number " + str(dslot) + " is free")
            else:
                print("No car parked!!!!")
        else:
            print("Parking lot is empty")

    def status_parking(self):
        ''' Print Car details parked inside parking lot '''

        if (self.max_slot == 0):
            print("Parking lot is under construction")
        elif (len(self.car_slot) > 0):
            print("Slot No.\tRegistration No.\tColor")
            for i in range(1, self.max_slot+1):
                if self.car_slot.get(i, None):
                    car = self.car_slot.get(i, None)
                    print(str(i) + "\t\t" + car.reg_number + "\t\t" + car.color)
        else:
            print("Parking lot is empty")

    def reg_for_cars_parking(self, color):
        ''' Get registeration for cars with specific colour '''

        if (self.max_slot == 0):
            print("Parking lot is under construction")
        elif color in self.col_reg:
            print(", ".join(self.col_reg[color]))
        else:
            print("Not found")

    def slot_for_color_car_parking(self, color):
        ''' Get Slots for cars with specific colour '''

        if (self.max_slot == 0):
            print("Parking lot is under construction")
        elif color in self.col_reg:
            reg_num_list = self.col_reg[color]
            print(", ".join(list(map(str,sorted({self.reg_slot[i] for i in reg_num_list})))))
        else:
            print("Not found")

    def slot_for_reg_car_parking(self, reg_num):
        ''' Get Slots for cars with specific registeration number '''

        if (self.max_slot == 0):
            print("Parking lot is under construction")
        elif reg_num in self.reg_slot:
            print(self.reg_slot[reg_num])
        else:
            print("Not found")
