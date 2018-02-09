"""Class for use with the sqlalchemy ORM. Contains cache of user crypto holdings.
"""

from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime

from db.base import BASE

class Holdings(BASE):
    """Class for use with the sqlalchemy ORM. Contains cache of user crypto holdings.
    """

    __tablename__ = 'holdings'

    id = Column(Integer, primary_key=True)
    create_time = Column(DateTime, default=datetime.now())
    update_time = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    exchange = Column(String)
    symbol = Column(String)
    volume_free = Column(Float)
    volume_used = Column(Float)
    volume_total = Column(Float)
    btc_last_value = Column(Float, default=0)
    btc_stop_loss = Column(Float, default=0)
    stop_loss_cooldown = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return "<Holdings(\
            exchange='%s',\
            create_time='%s',\
            update_time='%s',\
            symbol='%s',\
            volume_free='%s',\
            volume_used='%s',\
            volume_total='%s',\
            btc_last_value='%s',\
            btc_stop_loss='%s',\
            stop_loss_cooldown='%s')>" % (
                self.exchange,
                self.create_time,
                self.update_time,
                self.symbol,
                self.volume_free,
                self.volume_used,
                self.volume_total,
                self.btc_last_value,
                self.btc_stop_loss,
                self.stop_loss_cooldown
            )
