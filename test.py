import speedtest
import random
import matplotlib.pyplot as plt
class Test():

    def __init__(self):
        self.servers = []
        self.net_history = [ [], [], [] ]
        self.values = [ 'download', 'upload', 'ping' ]
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
        if self.current_stats and len(self.current_stats) > 0:
            for i, val in enumerate(self.values):
                self.net_history[i].append(self.current_stats[val])

    def plot(self):
        if len(self.net_history[0]) > 5:
            print('About to start plotting...')
            colors = ["black", "blue", "green", "purple", "red", "yellow"]

            fig = plt.figure()
            ax = fig.add_subplot(111)

            ax.set_xlabel("Time", fontsize=15)
            ax.set_ylabel("Speed", fontsize=15)
            plt.title("Internet Speed Over Time")

            for i, item in enumerate(self.net_history):
                print(i, item)
                plt.plot(item)
                # for val in item:
                    # print(val)
                    # plt.plot(self.net_history[i], )
            plt.legend()
            plt.show()

        # for i in range(len(y[0])):
        #     plt.plot(x,[pt[i] for pt in y],label = 'id %s'%i)


