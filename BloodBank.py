def bookBlood(groupBlood):
    if(list1[0][0] == groupBlood and list1[0][1] > 0 and list1[0][1] <=9):
        print("Blood group booked successfully!")
        list1[0][1] = int(lines[9]) - 1
        # print(list1[0][1])
        with open("AvailableBloodGroup.txt", "w") as f:
            f.write(str(list1))

    elif(list1[1][0] == groupBlood and list1[1][1] > 0 and list1[1][1] <=9):
        print("Blood group booked successfully!")
        list1[1][1] = int(lines[20]) - 1
        # print(list1[1][1])
        with open("AvailableBloodGroup.txt", "w") as f:
            f.write(str(list1))

    elif(list1[2][0] == groupBlood and list1[2][1] > 0 and list1[2][1] <=9):
        print("Blood group booked successfully!")
        list1[2][1] = int(lines[31]) - 1
        # print(list1[2][1])
        with open("AvailableBloodGroup.txt", "w") as f:
            f.write(str(list1))
        
    elif(list1[3][0] == groupBlood and list1[3][1] > 0 and list1[3][1] <=9):
        print("Blood group booked successfully!")
        list1[3][1] = int(lines[43]) - 1
        # print(list1[3][1])
        with open("AvailableBloodGroup.txt", "w") as f:
            f.write(str(list1))

    elif(list1[4][0] == groupBlood and list1[4][1] > 0 and list1[4][1] <=9):
        print("Blood group booked successfully!")
        list1[4][1] = int(lines[54]) - 1
        # print(list1[4][1])
        with open("AvailableBloodGroup.txt", "w") as f:
            f.write(str(list1))

    elif(list1[5][0] == groupBlood and list1[5][1] > 0 and list1[5][1] <=9):
        print("Blood group booked successfully!")
        list1[5][1] = int(lines[65]) - 1
        # print(list1[5][1])
        with open("AvailableBloodGroup.txt", "w") as f:
            f.write(str(list1))
        
    else:
        print("We dont have the blood group you want!")


def donateBlood(bloodGroup, donar):
    if(list1[0][0] == bloodGroup and list1[0][1] <9):
        print("Blood group Donated successfully!")
        list1[0][1] = int(lines[9]) + 1
        # print(list1[0][1])
        with open("BloodDonation.txt", "a") as f:
            f.write(f"{donar} => {bloodGroup} Time=> {currentTimeAndDate}\n")
        with open("AvailableBloodGroup.txt", "w") as f:
            f.write(str(list1))

    elif(list1[1][0] == bloodGroup and list1[1][1] <9):
        print("Blood group Donated successfully!")
        list1[1][1] = int(lines[20]) + 1
        # print(list1[0][1])
        with open("BloodDonation.txt", "a") as f:
            f.write(f"{donar} => {bloodGroup} Time=> {currentTimeAndDate}\n")
        with open("AvailableBloodGroup.txt", "w") as f:
            f.write(str(list1))

    elif(list1[2][0] == bloodGroup and list1[2][1] <9):
        print("Blood group Donated successfully!")
        list1[2][1] = int(lines[31]) + 1
        # print(list1[0][1])
        with open("BloodDonation.txt", "a") as f:
            f.write(f"{donar} => {bloodGroup} Time=> {currentTimeAndDate}\n")
        with open("AvailableBloodGroup.txt", "w") as f:
            f.write(str(list1))

    elif(list1[3][0] == bloodGroup and list1[3][1] <9):
        print("Blood group Donated successfully!")
        list1[3][1] = int(lines[43]) + 1
        # print(list1[0][1])
        with open("BloodDonation.txt", "a") as f:
            f.write(f"{donar} => {bloodGroup} Time=> {currentTimeAndDate}\n")
        with open("AvailableBloodGroup.txt", "w") as f:
            f.write(str(list1))

    elif(list1[4][0] == bloodGroup and list1[4][1] <9):
        print("Blood group Donated successfully!")
        list1[4][1] = int(lines[54]) + 1
        # print(list1[0][1])
        with open("BloodDonation.txt", "a") as f:
            f.write(f"{donar} => {bloodGroup} Time=> {currentTimeAndDate}\n")
        with open("AvailableBloodGroup.txt", "w") as f:
            f.write(str(list1))

    elif(list1[5][0] == bloodGroup and list1[5][1] <9):
        print("Blood group Donated successfully!")
        list1[5][1] = int(lines[65]) + 1
        # print(list1[0][1])
        with open("BloodDonation.txt", "a") as f:
            f.write(f"{donar} => {bloodGroup} Time=> {currentTimeAndDate}\n")
        with open("AvailableBloodGroup.txt", "w") as f:
            f.write(str(list1))

    else:
        print("Our maximum limit to store the number of bottles of per blood group is 10 only so sorry we are at out full capacity")
    

from datetime import datetime
now = datetime.now()
currentTimeAndDate = now.strftime("%d/%m/%Y %H:%M:%S")
if __name__ == '__main__':
    while(True):
        with open("AvailableBloodGroup.txt", "r") as avGroups:
           print("\nAvailable Blood Groups with the no of Bottles are per blood groups are:")
           lines = avGroups.read()
           # print(type(lines))
           list1 = [["AB+",int(lines[9])],["B+",int(lines[20])],["O-",int(lines[31])],["AB-",int(lines[43])],["B-",int(lines[54])],["O+",int(lines[65])]]
           print(list1)

        print("Enter Your choice:")
        print("1.Donate Blood")
        print("2.Need Blood")
        print("3.Exit")

        choice = int(input())
        
        if(choice == 1):
            donar = input("Enter the Name of the Donar:\n")
            bloodGroup = input("Enter the blood Group donar want to donate:\n")
            donateBlood(bloodGroup, donar)

        elif(choice == 2):
            needBlood = input("Enter the blood group you needed according to above list corresponding with their no of bottles:");
            bookBlood(needBlood)

        elif(choice == 3):
            print("Thanks for using our service ! Have a great day!")
            break

        else:
            print("Please enter valid input only 1 or 2 not others!")

