class Company():
    def __init__(self,id,name,planes):
        self.id = id
        self.name =name
        self.planes = []
        print(f"this plane is flight number {self.id} and company {self.name}")


class AirPlane():
    def __init__(self,id,location,company,next_flights):
        self.id =id
        self.location =location
        self.company =company
        self.next_flights = []
    def fly(self,destination):
        self.destination = destination
        print(f"this plane is flight number {self.id} and company {self.company} and"
               f"depart from  {self.location} to {self.destination}")
        return  self.next_flights.append(self.destination)
    def location_on_date(self,date):
        self.date =date
        return  self.date
    def available_on_date(self,date,location):
        self.dat =date
        self.locaction =location
        return f"flight available today to{self.locaction} at a time {self.date}"

class Flight():
    def __init__(self,date,destination,plane,id,origine):
        self.date =date
        self.destination =destination
        self.plane =plane
        self.id =id
        self.origine =origine
    def take_off(self):
        print(f"Boeing flight number {self.id} ,from  {self.origine} ,and the destination is to  {self.destination} Airport")

    def land(self):

        print(f"the plane landed at {self.date} ")


    # class Airport():
    #     def __init__(self,city,planes,departures,arrivals):
    #         self.city =city
    #         self.planes = []
    #         self.departures = []
    #         self.arrivals =[]
    #     def schedule_flights(self,destination,datetime):
    #           self.destination =destination
    #           self.datetime =datetime
    #
    #
    #     def info(self,start_date,end_date):
    #         self.start_date =start_date
    #         self.end_date =end_date

plane1 =Company('ET',"boeing",'emirates')
plane2 = AirPlane('IS','qatar','boeing''dc','monday')
plane2.fly('dalas')
print(plane2.location_on_date('21/9/2021'))
print (plane2.available_on_date('5pm','london'))
plane3 = Flight('4pm','dalas','telviv' 'ISRA','IS','dc')
plane3.take_off()
plane3.land()
        
    