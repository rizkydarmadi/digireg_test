import unittest
from main import Contact, AddresBook, conn


# Create a class that inherits from unittest.TestCase
class MyTest(unittest.TestCase):
    # Each test method should start with "test_"
    def test_add_contact(self):
        taylor = Contact(name="taylor", number="081288422341")
        AddresBook.add_contact(name=taylor.name, phone_number=taylor.number)

        # check data
        cursor = conn.cursor()
        cursor.execute(
            f"select c.name from contact c where name = '{taylor.name}'",
        )
        data_name = cursor.fetchone()
        self.assertEqual(data_name[0], "taylor")

    def test_remove_contact(self):
        taylor = Contact(name="taylor", number="081288422341")
        AddresBook.remove_contact(name=taylor.name)

        # check data
        cursor = conn.cursor()
        cursor.execute(
            f"select c.name from contact c where name = '{taylor.name}'",
        )
        data_name = cursor.fetchone()
        self.assertIsNone(data_name)

    def test_search_contact(self):
        # GIVEN
        taylor = Contact(name="taylor", number="081288422341")
        AddresBook.add_contact(name=taylor.name, phone_number=taylor.number)
        for i in range(3):
            AddresBook.add_contact(name=f"test{i}", phone_number=f"09128334528{i}")

        taylor = Contact(name="taylor", number="081288422341")
        AddresBook.search_contact(name=taylor.name)

        # check data
        cursor = conn.cursor()
        cursor.execute(
            f"select c.name from contact c where name = '{taylor.name}'",
        )
        data_name = cursor.fetchone()
        self.assertEqual(data_name[0], "taylor")


# Run the tests
if __name__ == "__main__":
    unittest.main()
