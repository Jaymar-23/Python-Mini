def ageChecker(age):
    if 0 < age < 18:
        return "You are a minor."
    
    elif 18 <= age < 65:
        return "You are an adult."

    elif age >= 65:
        return "You are a senior citizen." 
    
def main():
    while True:
        age_input = input("How old are you? ")
        
        try: 
            age = int(age_input)
            if age <= 0:
                print("Not a valid age!!! Try again. \n")
                continue
                
            print(ageChecker(age))
            break

        except ValueError:
            print("Not a valid age!!! Try again. \n")

if __name__ == "__main__":
    main()