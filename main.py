import test
import utils
import sys
import matplotlib.pyplot as plt

if __name__ in "__main__":

    try:
        logger = utils.Logger(int(sys.argv[1]))
    except IndexError:
        print('[WARN] Log level not set, defaulting to normal.')
        logger = utils.Logger(1)

    nettest = test.Test()
    should_quit = False

    logger.log('[INFO] Starting netmon....', True)
    while not should_quit:
        logger.log('[INFO] Starting test.', False)
        nettest.run_test()
        testval = nettest.parse_results()
        logger.log('[INFO] Test completed at {}'.format(testval['timestamp']), False)


