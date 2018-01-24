"""Class for use with the sqlalchemy ORM. Contains cache of OHLCV candles.
"""

from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime

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
    timestamp = Column(Integer)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)

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
