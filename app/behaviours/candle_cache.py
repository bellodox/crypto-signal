"""Candle caching behaviour.
"""

import structlog

class CandleCacheBehaviour():
    """Candle caching behaviour.
    """

    def __init__(self, behaviour_config, exchange_interface,
                 strategy_analyzer, notifier, db_handler):
        """Initialize SimpleBotBehaviour class.

        Args:
            behaviour_config (dict): A dictionary of configuration for this behaviour.
            exchange_interface (ExchangeInterface): Instance of the ExchangeInterface class for
                making exchange queries.
            strategy_analyzer (StrategyAnalyzer): Instance of the StrategyAnalyzer class for
                running analysis on exchange information.
            notifier (Notifier): Instance of the notifier class for informing a user when a
                threshold has been crossed.
            db_handler (DatbaseHandler): Instance of the DatabaseHandler class for reading and
                storing transaction data.
        """
