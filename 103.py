import jdatetime
import pytz
from persiantools.jdatetime import JalaliDate, JalaliDateTime


# ---------------- Testing Jdatetime ----------------

test = str(jdatetime.datetime.now())
# test2 = str(jdatetime.date.today())
# date = test.split()
# print(date)

# ---------------- 2023 Christmas ----------------

# shamsi = jdatetime.date.fromgregorian(day=25, month=12, year=2023)
# print(shamsi)

# print(JalaliDateTime(1402, 2, 9, 17, 38, 0, 0, pytz.utc).strftime("%c"))
print(JalaliDateTime(1402, 2, 9, 17, 38, 0, 0, pytz.utc).strftime("%A"))
