with open("AvailableBloodGroup.txt", "r") as f:
    lines = f.read()


listt = [["AB+",4],["B+",3],["O-",1],["AB-",1],["B-",2],["O+",0]]
print(listt[1][0])