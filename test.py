import speedtest
import random
import matplotlib.pyplot as plt
class Test():

    def __init__(self):
        self.servers = []
        self.net_history = []
        self.current_stats = {}
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

        print(results_dict['timestamp'])
        self.current_stats = results_dict
    
    #Grab the values we need from our results.
    def parse_results(self):
        values = [ 'download', 'upload', 'ping', 'timestamp' ]
        plot_points = {}
        if self.current_stats and len(self.current_stats) > 0:
            for val in values:
                plot_points[val] = self.current_stats[val]

            self.net_history.append(plot_points)
            return plot_points

    def plot(self):
        print('About to start plotting...')
        colors = ["black", "blue", "green", "purple", "red", "yellow"]

        fig = plt.figure()
        ax = fig.add_subplot(111)

        ax.set_xlabel("Time", fontsize=15)
        ax.set_ylabel("Speed", fontsize=15)

        for i, item in enumerate(self.net_history):
            ax.plot(item[])



