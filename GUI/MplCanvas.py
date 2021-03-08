import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from parameter import pprint



class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=3, height=2, dpi=180): #3, 2
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)
        self.fig.tight_layout()
        #self.manager = self.fig.get_current_fig_manager()
        #self.manager.window.showMaximized()

    def plotData(self, time, data, data2=None, plottype=None):
        self.plottype = plottype
        self.axes.clear()
        if self.plottype =="Power":
            self.axes.plot(time, data, '-',label="Is Power")
            if type(data2) != type(None):
                self.axes.plot(time, data2, '-',label="Set Power")
            self.axes.set_ylabel('Power [W]')
            self.axes.set_xlabel('Time [h]')
            self.axes.set_title('Power Profile')
            handles, labels = self.axes.get_legend_handles_labels()
            # reverse the order
            self.axes.legend(handles[::-1], labels[::-1])
            #self.axes.legend()

        if self.plottype =="Temperature":
            self.axes.plot(time, data, '-',label="Temp OUT")
            if type(data2) != type(None):
                self.axes.plot(time, data2, '-',label="Temp IN")
            self.axes.set_ylabel('Temperature [°C]')
            self.axes.set_xlabel('Time [h]')
            self.axes.set_title('Temperature Profile')
            handles, labels = self.axes.get_legend_handles_labels()
            # reverse the order
            self.axes.legend(handles[::-1], labels[::-1])
        #else:
            #pprint("no plottype given")
        self.draw()
        self.update()