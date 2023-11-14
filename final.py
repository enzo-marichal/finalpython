import pandas as pd
import os

while True:
    print("------------------------------------------")
    print("\nWelcome to the client and sales analysis\n")
    print("1) Create a new client in Txt file")
    print("2) Show all the clients in Txt file")
    print("3) Show Excel file clients and sales")
    print("4) Analyse Excel file clients and sales")
    print("5) Analyse CSV file")
    print("6) Quit\n")

    # Allow user to make a choice
    userchoice = int(input("Choose an option between 1 and 6: "))
    print("------------------------------------------")

    if userchoice == 1:
        class Client:
            def __init__(self, name, date_birth, city_birth, email, phone, gender, mission, job, country):
                self.name = name
                self.date_birth = date_birth
                self.city_birth = city_birth
                self.email = email
                self.phone = phone
                self.gender = gender
                self.mission = mission
                self.job = job
                self.country = country

            def show_info(self):
                print("\nClient Information:")
                print("Name:", self.name)
                print("Date of Birth:", self.date_birth)
                print("City of Birth:", self.city_birth)
                print("Email:", self.email)
                print("Phone:", self.phone)
                print("Gender:", self.gender)
                print("Mission:", self.mission)
                print("Job:", self.job)
                print("Country:", self.country)

        # Ask the user for the client attributes
        print("CLIENT CREATION\n")
        name = input("What is the name of the client? ")
        date_birth = input("What is the date of birth of the client? ")
        city_birth = input("What is the city of birth of the client? ")
        email = input("What is the email of your client? ")
        phone = input("What is the phone number of your client? ")
        gender = input("What is the gender of your client? ")
        mission = input("What is the mission of your client? ")
        job = input("What is the job of your client? ")
        country = input("What is the country of your client? ")

        new_client = Client(name, date_birth, city_birth, email, phone, gender, mission, job, country)
        new_client.show_info()

        # Save information in Txt file
        with open("clients.txt", "a") as myfile:
            myfile.write(f"{name},{date_birth},{city_birth},{email},{phone},{gender},{mission},{job},{country}\n")

        # Save information in Excel file
        new_client_data = pd.DataFrame([{
            'Name': name,
            'Date of Birth': date_birth,
            'City of Birth': city_birth,
            'Email': email,
            'Phone': phone,
            'Gender': gender,
            'Mission': mission,
            'Job': job,
            'Country': country
        }])

        excel_file = 'clients.xlsx'
        if os.path.exists(excel_file):
            existing_data = pd.read_excel(excel_file)
            updated_data = existing_data.append(new_client_data, ignore_index=True)
        else:
            updated_data = new_client_data

        updated_data.to_excel(excel_file, index=False)
        print("\nThe client has been created and saved to both text and Excel files.\n")

    elif userchoice == 6:
        break
