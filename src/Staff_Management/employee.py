

class Employee:
    def __init__(self, id, name, email, password, phone, date_of_birth, role, gender, **kwargs):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.role = role
        self.gender = gender 
        self.designation = kwargs.get("designation", "")
        self.country = kwargs.get("country", "")
        self.state = kwargs.get("state", "")
        self.district = kwargs.get("district", "")
        self.city_village = kwargs.get("city_village", "")
        self.pincode = kwargs.get("pincode", "")
        self.joining_date = kwargs.get("joining_date", "")
        self.salary = kwargs.get("salary", "")
        self.status = "active"  
        self.resign_date = None

    def to_dict(self):
        return self.__dict__
