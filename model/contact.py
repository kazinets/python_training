from sys import maxsize
class Contact:

    def __init__(self, first_name=None, last_name=None, address_1=None, home_1=None, mobile_phone=None, work=None, email_1=None,
                        email_2=None, bday=None, bmonth=None, byear=None, address_2=None, home_2=None, id=None):
        self.first_name=first_name
        self.last_name=last_name
        self.address_1=address_1
        self.home_1=home_1
        self.mobile_phone=mobile_phone
        self.work=work
        self.email_1=email_1
        self.email_2=email_2
        self.bday=bday
        self.bmonth=bmonth
        self.byear=byear
        self.address_2=address_2
        self.home_2=home_2
        self.id = id


    def __repr__(self):
        return "%s:%s" % (self.id, self.first_name)


    def __eq__(self, other):
       return (self.id is None or other.id is None or self.id == other.id) and self.last_name == other.last_name


    def id_or_max(self):
       if self.id:
          return int(self.id)
       else:
          return maxsize

