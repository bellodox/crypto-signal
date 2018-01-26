"""Class for use with the sqlalchemy ORM. Contains cache of OHLCV candles.
"""

from datetime import datetime

from sqlalchemy import Column, Integer, Numeric, String, Float, DateTime

from db.base import BASE

class Candles(BASE):
    """Class for use with the sqlalchemy ORM. Contains cache of OHLCV candles.
    """

    __tablename__ = 'candles'

    id = Column(Integer, primary_key=True)
    create_time = Column(DateTime, default=datetime.now())
    update_time = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    exchange = Column(String)
    symbol_pair = Column(String)
    timestamp = Column(Numeric)
    open = Column(Numeric)
    high = Column(Numeric)
    low = Column(Numeric)
    close = Column(Numeric)
    volume = Column(Numeric)

    def __repr__(self):
        return "<Candles(\
            create_time='%s'\
            update_time='%s'\
            timestamp='%s'\
            open='%s'\
            high='%s'\
            low='%s'\
            close='%s'\
            volume='%s')>" % (
                self.create_time,
                self.update_time,
                self.timestamp,
                self.open,
                self.high,
                self.low,
                self.close,
                self.volume
            )
