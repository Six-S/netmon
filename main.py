import test
import utils

if __name__ in "__main__":
    nettest = test.Test()
    logger = utils.Logger()

    logger.log('[INFO] Starting netmon....', False)

    testval = nettest.run_test()
    print('finished!')
    nettest.parse_results(testval)
