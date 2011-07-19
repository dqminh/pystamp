import unittest
import datetime
from pystamp import DateTimeTranslator, format_like

class PystampTest(unittest.TestCase):

    def test_extract_time(self):
        response = DateTimeTranslator.extract_time("March 1, 2010 10:10")
        self.assertEqual(response, ("March 1, 2010 ", "10:10", ""))
        response = DateTimeTranslator.extract_time("March 1, 2010 10:10 am")
        self.assertEqual(response, ("March 1, 2010 ", "10:10 am", ""))
        response = DateTimeTranslator.extract_time("10:10 am, March 1, 2010")
        self.assertEqual(response, ("", "10:10 am", ", March 1, 2010"))
        response = DateTimeTranslator.extract_time("10:10, March 1, 2010")
        self.assertEqual(response, ("", "10:10", ", March 1, 2010"))

    def test_convert_time_directive(self):
        translator = DateTimeTranslator()
        response = translator.convert_time_directive("am", None)
        self.assertEqual(response, "%p")
        response = translator.convert_time_directive("AM", None)
        self.assertEqual(response, "%p")
        response = translator.convert_time_directive("10", None)
        self.assertEqual(response, "%I")
        response = translator.convert_time_directive("20", None)
        self.assertEqual(response, "%H")
        response = translator.convert_time_directive("2", None)
        self.assertEqual(response, "%I")
        response = translator.convert_time_directive("02", "%H")
        self.assertEqual(response, "%M")
        response = translator.convert_time_directive("02", "%M")
        self.assertEqual(response, "%S")

    def test_convert_date_directive(self):
        translator = DateTimeTranslator()
        response = translator.convert_date_directive("1999", None)
        self.assertEqual(response, "%Y")
        response = translator.convert_date_directive("March", None)
        self.assertEqual(response, "%B")
        response = translator.convert_date_directive("Apr", None)
        self.assertEqual(response, "%b")
        response = translator.convert_date_directive("Monday", None)
        self.assertEqual(response, "%A")
        response = translator.convert_date_directive("Mon", None)
        self.assertEqual(response, "%a")
        response = translator.convert_date_directive("60", None)
        self.assertEqual(response, "%y")
        response = translator.convert_date_directive("20", None)
        self.assertEqual(response, "%d")
        response = translator.convert_date_directive("12", None)
        self.assertEqual(response, "%m")
        response = translator.convert_date_directive("11", None)
        self.assertEqual(response, "%m")
        response = translator.convert_date_directive("11", "%m")
        self.assertEqual(response, "%d")
        response = translator.convert_date_directive("11", "%b")
        self.assertEqual(response, "%d")

    def test_translate(self):
        translator = DateTimeTranslator()
        response = translator.translate("March 10, 1999 10:10")
        self.assertEqual(response, "%B %d, %Y %I:%M")
        response = translator.translate("March 10, 1999 10:10:10")
        self.assertEqual(response, "%B %d, %Y %I:%M:%S")
        response = translator.translate("Mar 10, 99 10:10:10 am")
        self.assertEqual(response, "%b %d, %y %I:%M:%S %p")

    def test_format_like_with_datetime(self):
        cur = datetime.datetime.utcnow()
        curstr = cur.strftime("%B %d, %Y %I:%M %p")
        formatted = format_like(cur, "March 19, 2010 01:00 am")
        self.assertEqual(curstr, formatted)

    def test_format_like_with_date(self):
        cur = datetime.date(2010, 10, 10)
        curstr = cur.strftime("%B %d, %Y")
        formatted = format_like(cur, "March 19, 2010")
        self.assertEqual(curstr, formatted)

    def test_format_like_with_time(self):
        cur = datetime.time(12, 02, 02)
        curstr = cur.strftime("%I:%M:%S %p")
        formatted = format_like(cur, "10:10:10 am")
        self.assertEqual(curstr, formatted)


if __name__ == "__main__":
    unittest.main()
