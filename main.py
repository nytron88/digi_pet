from digi_playground import Pet

print("Welcome to digital pet.")
name = input("Name of the pet: ")
pet1 = Pet(name)
done = False

if pet1.on_birth == "Something went wrong, please restart the program":
    print("Something went wrong, please restart the program")
    done = True
else:
    print(pet1.on_birth)

while not done:
    user_input = input("<f>eed <s>leep <l>ove <e>xercise <w>ater <st>ats <q>uit. Command you want to use: ")
    if user_input == 's':
        pet1.on_sleep()
    elif user_input == 'e':
        pet1.on_exercise()
    elif user_input == 'l':
        pet1.on_love()
    elif user_input == 'w':
        pet1.on_water()
    elif user_input == 'f':
        pet1.on_feed()
    elif user_input == 'st':
        print(pet1.stats())
    elif user_input == 'q':
        done = True
        break
    else:
        done = True
        print("You didn't use a proper command")
        break
    if pet1.sleep == 0 or pet1.sleep == 10:
        done = True
        print("Your pet died")
        break
    elif pet1.feed == 0 or pet1.feed == 10:
        done = True
        print("Your pet died")
        break
    elif pet1.love == 0 or pet1.love == 10:
        done = True
        print("Your pet died")
        break
    elif pet1.water == 0 or pet1.water == 10:
        done = True
        print("Your pet died")
        break
    elif pet1.exercise == 0 or pet1.exercise == 10:
        done = True
        print("Your pet died")
        break
if done:
    print("The program ended")
