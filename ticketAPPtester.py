import unittest
from uuid import uuid4

class User:
    def __init__(self, email: str):
        self.user_id = str(uuid4())
        self.email = email

    def login(self):
        return True


class Ticketing:
    def __init__(self):
        self.tickets = {}

    def ticket(self, seat_number):
        return self.tickets.get(seat_number)

    def bookSeat(self, user: User, seat_number: str):
        if not isinstance(seat_number, str) or seat_number == "":
            raise ValueError("Invalid seat number.")

        if seat_number in self.tickets:
            return False

        self.tickets[seat_number] = user.user_id
        return True

    def cancelSeat(self, seat_number: str):
        if not isinstance(seat_number, str) or seat_number == "":
            raise ValueError("Invalid seat number.")

        if seat_number not in self.tickets:
            return False

        self.tickets.pop(seat_number)
        return True


class Membership:
    def __init__(self, user: User):
        self.member_id = str(uuid4())
        self.user = user
        self.active = False

    def join(self):
        self.active = True
        return True

    def cancel(self):
        self.active = False
        return True


class TheatreVenue:
    def __init__(self, verify: str):
        self.venue_id = str(uuid4())
        self.verify = verify

    def login(self):
        return bool(self.verify)


class TestUser(unittest.TestCase):

    def test_user_creation(self):
        u = User("john@example.com")
        self.assertIsNotNone(u.user_id)
        self.assertEqual(u.email, "john@example.com")

    def test_user_login(self):
        u = User("john@example.com")
        self.assertTrue(u.login())


class TestTicketing(unittest.TestCase):

    def setUp(self):
        self.user = User("test@example.com")
        self.ticketing = Ticketing()

    def test_book_seat_success(self):
        result = self.ticketing.bookSeat(self.user, "A1")
        self.assertTrue(result)
        self.assertEqual(self.ticketing.ticket("A1"), self.user.user_id)

    def test_book_seat_already_taken(self):
        self.ticketing.bookSeat(self.user, "A1")
        result = self.ticketing.bookSeat(self.user, "A1")
        self.assertFalse(result)

    def test_book_seat_invalid_input(self):
        with self.assertRaises(ValueError):
            self.ticketing.bookSeat(self.user, "")

        with self.assertRaises(ValueError):
            self.ticketing.bookSeat(self.user, None)

    def test_cancel_seat_success(self):
        self.ticketing.bookSeat(self.user, "B2")
        result = self.ticketing.cancelSeat("B2")
        self.assertTrue(result)
        self.assertIsNone(self.ticketing.ticket("B2"))

    def test_cancel_seat_not_booked(self):
        result = self.ticketing.cancelSeat("C3")
        self.assertFalse(result)

    def test_cancel_seat_invalid_input(self):
        with self.assertRaises(ValueError):
            self.ticketing.cancelSeat("")

        with self.assertRaises(ValueError):
            self.ticketing.cancelSeat(None)


class TestMembership(unittest.TestCase):

    def setUp(self):
        self.user = User("member@example.com")
        self.membership = Membership(self.user)

    def test_join_membership(self):
        result = self.membership.join()
        self.assertTrue(result)
        self.assertTrue(self.membership.active)

    def test_cancel_membership(self):
        self.membership.join()
        result = self.membership.cancel()
        self.assertTrue(result)
        self.assertFalse(self.membership.active)


class TestTheatreVenue(unittest.TestCase):

    def test_venue_login_success(self):
        venue = TheatreVenue("SECURE123")
        self.assertTrue(venue.login())

    def test_venue_login_fail_invalid_verify_code(self):
        venue = TheatreVenue("")
        self.assertFalse(venue.login())

if __name__ == "__main__":
    unittest.main()