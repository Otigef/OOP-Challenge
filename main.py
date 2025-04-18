from digital_pet import Pet

def main():
    # Create a new pet
    pet_name = input("Name your pet: ")
    my_pet = Pet(pet_name)
    
    print(f"\nWelcome, {pet_name}! Let's take care of your new digital pet!")
    
    while True:
        print("\nOptions:")
        print("1. 🥩 Feed")
        print("2. 🛌 Put to sleep")
        print("3. 🎾 Play")
        print("4. 📊 Check status")
        print("5. 🧠 Teach trick")
        print("6. 🎩 Show tricks")
        print("7. ❌ Quit")
                
        choice = input("\nChoose an action (1-7): ")
        
        if choice == '1':
            my_pet.eat()
        elif choice == '2':
            my_pet.sleep()
        elif choice == '3':
            my_pet.play()
        elif choice == '4':
            my_pet.get_status()
        elif choice == '5':
            trick = input("Enter the trick to teach: ")
            my_pet.train(trick)
        elif choice == '6':
            my_pet.show_tricks()
        elif choice == '7':
            print("\nThanks for playing with your digital pet!")
            break
        else:
            print("Invalid choice. Please enter 1-7.")

if __name__ == "__main__":
    main()