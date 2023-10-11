import random
import string
import json
import requests

data1 = {
    "user_name": "admin",
    "password": "Admin@123"
}

class randomdata:
    def header():
        base_url = "https://keel-api-dev.talentship.io/api"
        login_url = base_url + "/login"
        res = requests.post(url=login_url, data=data1)
        resp = res.json()
        token1 = resp['access_token']
        head = {"Authorization": f"Bearer {token1}"}
        return head


    data2 = {
        "firstName": "super1",
        "lastName": "admin1",
        "userName": "admin1",
        "email": "admin1@123",
        "password": "Admin1@123"
    }

    files = {
        "orgLogo": ("logo.svg", open("C:/Users/aravi/PycharmProjects/pythonProject1/Utilities/logo.svg", "rb"), "image/svg+xml")
    }
    data6 = {
        "orgLogo": "C:/Users/aravi/PycharmProjects/pythonProject1/Utilities/logo.svg",
        "orgName": "Image"
    }

    data8 = {
        "packageId": 1,
        "featureName": "Add Employee",
        "featureDescription": "Add Employee in order to proceed the process"
    }

    def modifyJsonfile(logopath):
        with open("C:/Users/aravi/PycharmProjects/pythonProject1/Utilities/LoadData/loads.json", 'r') as json_file:
            data = json.load(json_file)
        data["logoPath"] = logopath

        with open("C:/Users/aravi/PycharmProjects/pythonProject1/Utilities/LoadData/loads.json", 'w') as json_file:
            json_file.write("\n")
            json.dump(data, json_file, indent=4)

    def generate_random_name(length=5):
        random_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        return random_name

    def generate_random_email(length=6):
        random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        email = random_string + "@mailinator.com"
        return email

    def generete_random_number():
        random_num = random.randint(1, 250)
        return random_num

    def generate_data():
        name = randomdata.generate_random_name()
        name1 = randomdata.generate_random_name()
        email = randomdata.generate_random_email()
        num = randomdata.generete_random_number()

        dataDes = {
            "designation": [name]
        }
        with open("C:/Users/aravi/PycharmProjects/pythonProject1/Utilities/LoadData/load1.json", "w") as file:
            json.dump(dataDes, file, indent=4)

        data5 = {
            "roleName": name1,
            "roleShortName": name1,
            "permissionNo": num,
            "roleDesceiption": "Can able change all of his own data"
        }
        with open("C:/Users/aravi/PycharmProjects/pythonProject1/Utilities/LoadData/load2.json", "w") as file:
            json.dump(data5, file, indent=4)

        data7 = {
            "packageName": name,
            "packageDescription": "The Business Analysis is a comprehensive platform that streamlines the recruitment process, allowing employers to post job openings, review applications, and schedule interviews."
        }
        with open("C:/Users/aravi/PycharmProjects/pythonProject1/Utilities/LoadData/load3.json", "w") as file:
            json.dump(data7, file, indent=4)
        bdata = {
            "organizationName": name,
            "subDomain": name1,
            "companyCategory": "IT",
            "logoPath": "https://hrms-poc.s3.eu-west-1.amazonaws.com/test-company2.svg",
            "active": True,
            "orgAddress": "dfdfsdf",
            "orgPincode": "34545",
            "orgCountry": 9,
            "orgState": None,
            "orgCity": None,
            "primary": {
                "firstName": "ram",
                "lastName": "kumar",
                "phone": "+91333543245",
                "designation": "CEO",
                "role": 1,
                "email": email,
                "address": "123 Main Street",
                "country": num,
                "state": None,
                "city": None,
                "pincode": "641006",
                "isPrimary": 1
            },
            "packages": [
                1
            ]
        }

        with open("C:/Users/aravi/PycharmProjects/pythonProject1/Utilities/LoadData/loads.json", "w") as file:
            file.write("\n")
            json.dump(bdata, file, indent=4)
    def json_data():
        with open("C:/Users/aravi/PycharmProjects/pythonProject1/Utilities/LoadData/loads.json", "r") as json_file0:
            json_data =json.load(json_file0)
        return json_data
    with open("C:/Users/aravi/PycharmProjects/pythonProject1/Utilities/LoadData/load1.json", "r") as json_file1:
        data4 = json.load(json_file1)
    def data5():
        with open("C:/Users/aravi/PycharmProjects/pythonProject1/Utilities/LoadData/load2.json", "r") as json_file2:
            data5 = json.load(json_file2)
        return data5

    with open("C:/Users/aravi/PycharmProjects/pythonProject1/Utilities/LoadData/load3.json", "r") as json_file2:
        data7 = json.load(json_file2)

