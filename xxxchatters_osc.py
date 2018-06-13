from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client
from threading import Thread
import time

from progressbar import ProgressBar, Bar, Percentage

num_sentences = 500


class OscReceiver(object):
    def __init__(self):
        self.group_01 = []
        self.group_02 = []
        self.group_03 = []
        self.group_04 = []
        self.group_05 = []

        self.bar = ProgressBar(widget=[Percentage(), Bar()], maxval=num_sentences).start()
        self.outfile = open("osc_config_500_late_slowexp.csv", 'w')

    def receive(self, path, value):
        if path == "/group_01":
            self.group_01.append(value)
        if path == "/group_02":
            self.group_02.append(value)
        if path == "/group_03":
            self.group_03.append(value)
        if path == "/group_04":
            self.group_04.append(value)
        if path == "/group_05":
            self.group_05.append(value)

        self.print_sizes()
        self.bar.update(len(self.group_01))
        if self.all_finished():
            self.write_file()

    def write_file(self):
        self.outfile.write("group_01 group_02 group_03 group_04 group_05\n")
        for index in range(num_sentences):
            g_01 = self.group_01[index]
            g_02 = self.group_02[index]
            g_03 = self.group_03[index]
            g_04 = self.group_04[index]
            g_05 = self.group_05[index]
            self.outfile.write(
                str(g_01) + '\t' + str(g_02)+ '\t' + str(g_03)+ '\t' + str(g_04)+ '\t' + str(g_05) + '\n')

        self.outfile.close()

    def all_finished(self):
        return len(self.group_01) == num_sentences and len(self.group_02) == num_sentences and len(self.group_03) == num_sentences and len(self.group_04) == num_sentences and len(self.group_05) == num_sentences

    def print_sizes(self):
        print("group_01: " + str(len(self.group_01)))
        print("group_02: " + str(len(self.group_02)))
        print("group_03: " + str(len(self.group_03)))
        print("group_04: " + str(len(self.group_04)))
        print("group_05: " + str(len(self.group_05)))


if __name__ == '__main__':
    osc_receiver = OscReceiver()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/group_01", osc_receiver.receive)
    dispatcher.map("/group_02", osc_receiver.receive)
    dispatcher.map("/group_03", osc_receiver.receive)
    dispatcher.map("/group_04", osc_receiver.receive)
    dispatcher.map("/group_05", osc_receiver.receive)

    server = osc_server.BlockingOSCUDPServer(("localhost", 12345), dispatcher)
    thread = Thread(target=server.serve_forever)
    thread.start()

    client = udp_client.SimpleUDPClient("localhost", 12346)

    for i in range(num_sentences):
        position = float(i) / (num_sentences+1)
        client.send_message("/duration/seektoposition", position)
        time.sleep(0.04)

server.shutdown()