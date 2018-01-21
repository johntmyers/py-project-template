"""
Test Lambda Entry Point
"""
import time

from proj import base

logger = base.LOGGER


def handle(event, context):
    logger.info('Starting...')
    time.sleep(3)
    main = base.Main('a wild string', 10)
    logger.info(main.run())