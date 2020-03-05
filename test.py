import speedtest

class Test():

    def __init__(self):
        self.servers = []
        # If you want to test against a specific server
        # servers = [1234]

        self.threads = None
        # If you want to use a single threaded test
        # threads = 1

    #run our tests.
    def run_test(self):
        test = speedtest.Speedtest()
        test.get_servers(self.servers)
        test.get_best_server()
        test.download(threads=self.threads)
        test.upload(threads=self.threads)
        test.results.share()

        results_dict = test.results.dict()

        return results_dict
    
    #Grab the values we need from our results.
    def parse_results(self, results={}):
        values = [ 'download', 'upload', 'ping', 'timestamp' ]
        plot_points = {}
        if results and len(results) > 0:
            for val in values:
                plot_points[val] = results[val]
            
            return plot_points


