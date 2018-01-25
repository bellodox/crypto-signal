"""Candle caching behaviour.
"""

import structlog

class CandleCacheBehaviour():
    """Candle caching behaviour.
    """

    def __init__(self, behaviour_config, exchange_interface, db_handler):
        """Initialize SimpleBotBehaviour class.

        Args:
            behaviour_config (dict): A dictionary of configuration for this behaviour.
            exchange_interface (ExchangeInterface): Instance of the ExchangeInterface class for
                making exchange queries.
            db_handler (DatbaseHandler): Instance of the DatabaseHandler class for reading and
                storing transaction data.
        """

        self.logger = structlog.get_logger()
        self.behaviour_config = behaviour_config
        self.exchange_interface = exchange_interface
        self.db_handler = db_handler


    def run(self, market_pairs):
        """The behaviour entrypoint

        Args:
            market_pairs (list): List of symbol pairs to operate on, if empty get all pairs.
        """

        self.logger.info("Starting candle cache behaviour...")

        if market_pairs:
            self.logger.debug("Found configured symbol pairs.")
            market_data = self.exchange_interface.get_symbol_markets(market_pairs)
        else:
            self.logger.debug("No configured symbol pairs, using all available on exchange.")
            market_data = self.exchange_interface.get_exchange_markets()

        for exchange in market_data:
            for market_pair in market_data[exchange]:
                historical_data = self.exchange_interface.get_historical_data(
                    market_data[exchange][market_pair]['symbol'],
                    exchange,
                    self.behaviour_config['timeframe']
                )

                for entry in historical_data:
                    ohlcv_payload = {
                        'exchange': exchange,
                        'symbol_pair': market_pair,
                        'timestamp': entry[0],
                        'open': entry[1],
                        'high': entry[2],
                        'low': entry[3],
                        'close': entry[4],
                        'volume': entry[5]
                    }

                    if not self.db_handler.read_rows('candles', ohlcv_payload).count():
                        self.db_handler.create_row('candles', ohlcv_payload)
