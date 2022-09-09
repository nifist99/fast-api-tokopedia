from datetime import datetime
from datetime import date

class ConfigDate:
    def carbonDate():
        today = date.today()

        return today

    def carbonDateTime():
        now = datetime.now()

        return now
