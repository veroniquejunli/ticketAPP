from uuid import uuid4

class User:
    def __init__(self, email: str):
        self.user_id = str(uuid4())
        self.email = email

    def login(self):
        # Placeholder for real authentication logic
        print(f"[LOGIN] User {self.email} logged in.")
        return True

    def __repr__(self):
        return f"User(user_id={self.user_id}, email={self.email})"
    
class Ticketing:
    def __init__(self):
        self.tickets = {}  # seat_number -> user_id

    def ticket(self, seat_number):
        """Returns the user who booked the seat (if any)."""
        return self.tickets.get(seat_number, None)

    def bookSeat(self, user: User, seat_number: str):
        if seat_number in self.tickets:
            print(f"[BOOK] Seat {seat_number} is already booked.")
            return False

        self.tickets[seat_number] = user.user_id
        print(f"[BOOK] Seat {seat_number} booked by {user.email}.")
        return True

    def cancelSeat(self, seat_number: str):
        if seat_number not in self.tickets:
            print(f"[CANCEL] Seat {seat_number} not currently booked.")
            return False

        removed_user = self.tickets.pop(seat_number)
        print(f"[CANCEL] Seat {seat_number} booking cancelled (was user {removed_user}).")
        return True
    

class Membership:
    def __init__(self, user: User):
        self.member_id = str(uuid4())
        self.user = user
        self.active = False

    def join(self):
        self.active = True
        print(f"[MEMBERSHIP] User {self.user.email} joined membership.")
        return True

    def cancel(self):
        self.active = False
        print(f"[MEMBERSHIP] Membership cancelled for {self.user.email}.")
        return True

    def __repr__(self):
        status = "Active" if self.active else "Inactive"
        return f"Membership(member_id={self.member_id}, user={self.user.email}, status={status})"

class TheatreVenue:
    def __init__(self, verify: str):
        self.venue_id = str(uuid4())
        self.verify = verify

    def login(self):
        # Some simple verification
        print(f"[VENUE LOGIN] Venue {self.venue_id} verified with code: {self.verify}")
        return True

    def __repr__(self):
        return f"TheatreVenue(venue_id={self.venue_id}, verify={self.verify})"


if __name__ == "__main__":
    user = User(email="alice@example.com")
    user.login()

    membership = Membership(user)
    membership.join()

    ticket_system = Ticketing()
    ticket_system.bookSeat(user, "A1")
    ticket_system.cancelSeat("A1")

    venue = TheatreVenue(verify="SECURE-123")
    venue.login()


class Diagram
    class User {
        userID()
        email : string
        login()
    }

    class Ticketing {
        ticket()
        bookSeat()
        cancelSeat()
    }

class Membership {
       memberID()
        join()
        cancel()
    }

   class TheatreVenue {
        venueID()
        login()
        verify: string
    }

