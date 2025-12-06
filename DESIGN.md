Main class structures:
User
userID()
email: string
login()

Ticketing
ticket()
bookSeat()
cancelSeat()

Membership
memberID()
join()
cancel()

Theatre/Venue
venueID()
login()

Design Patterns:
Decorator: This allows behavior to be added to an individual object without affecting other objects. This is very important for the ticketing system, because booking one seat in the system should not affect other bookings.

Observer: Similar to the Decorator, this is also important for the ticketing system, because when one class is modified the whole system must be notified/updated for both users and administrators so that double bookings do not occur. 

OOP Principles:
Abstraction: A simplistic user interface will only show the consumer what they need to see, everything else will be available for backend by the administration side.

Encapsulation: The internal structure of the software will be entirely contained not have to rely on external softwares for data. This principle is the most important as it is one of the selling points for why the app is different from others. 

Polymorphism: The network system of the software will allow multiple theatres and venues to join. This means the methods used for the membership classes may be overloaded.

Inheritance: Booking/reserving seats will be a relatively similar process every time. Reusing code between the child and parent classes will simplify the process.

Reflection:
At first I struggled to find a problem that needed to be solved and that could be solved using technology. I decided to take on something that already exists like a ticketing system, and try to expand on it. 

