from copy import deepcopy
import cmath
import matplotlib.pyplot as plt


class ChannelStateInformation():
    timestamp_low = None
    bfee_count = None
    Nrx = None
    Ntx = None
    rssi_a = None
    rssi_b = None
    rssi_c = None
    noise = None
    agc = None
    perm = None
    rate = None
    csi_raw = None
    csi = None
    powers = None
    phases = None

    def __init__(self, csi_state):
        self.timestamp_low = csi_state['timestamp_low']
        self.bfee_count = csi_state['bfee_count']
        self.Nrx = csi_state['Nrx']
        self.Ntx = csi_state['Ntx']
        self.rssi_a = csi_state['rssi_a']
        self.rssi_b = csi_state['rssi_b']
        self.rssi_c = csi_state['rssi_c']
        self.noise = csi_state['noise']
        self.agc = csi_state['agc']
        self.perm = csi_state['perm']
        self.rate = csi_state['rate']
        self.csi_raw = csi_state['csi']
        self.csi = deepcopy(self.csi_raw)
        for i, csi_in_channel in enumerate(self.csi):
            for j, csi_in_ntx in enumerate(csi_in_channel):
                for k, csi_value in enumerate(csi_in_ntx):
                    self.csi[i][j][k] = complex(
                        self.csi[i][j][k].replace("i", "j"))
        powers = [[], [], []]
        phases = [[], [], []]
        for csi_in_channel in self.csi:
            powers[0].append(cmath.polar(csi_in_channel[0][0])[0])
            powers[1].append(cmath.polar(csi_in_channel[0][1])[0])
            powers[2].append(cmath.polar(csi_in_channel[0][2])[0])
            phases[0].append(cmath.polar(csi_in_channel[0][0])[1])
            phases[1].append(cmath.polar(csi_in_channel[0][1])[1])
            phases[2].append(cmath.polar(csi_in_channel[0][2])[1])
        self.powers = powers
        self.phases = phases

    def get_x_for_predict(self):
        x = []
        for power in self.powers:
            x.extend(power)
        for phase in self.phases:
            x.extend(phase)
        # x = self.powers[0]
        # x = self.powers[0][20:24]
        # x = self.powers[0][20:22]
        # x = self.powers[0][21:23]
        # x = self.powers[0][22:24]
        # x = self.phases[0]
        return x

    def plot_power(self):
        plt.plot(self.powers[0], label="antenna 1")
        plt.plot(self.powers[1], label="antenna 2")
        plt.plot(self.powers[2], label="antenna 3")
        plt.legend(loc=1)
        plt.show()

    def plot_phase(self):
        plt.plot(self.phases[0], label="antenna 1")
        plt.plot(self.phases[1], label="antenna 2")
        plt.plot(self.phases[2], label="antenna 3")
        plt.legend(loc=1)
        plt.show()
