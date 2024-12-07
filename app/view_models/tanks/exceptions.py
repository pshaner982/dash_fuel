import logging

logger = logging.getLogger(__name__)


class TankException(Exception):
    """Custom exception type designed should be raised by any business logic when the business
    logic fails.

    Notes:
        log level warning might get changed do to sentry or other observability tool sensitivity
        to warning log level.
    """

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
        logger.warning(self.message)
