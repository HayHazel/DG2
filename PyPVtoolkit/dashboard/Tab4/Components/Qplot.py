from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

class Create():
    def __init__(self):
        self.PlotData = {
            'Q': [0],
            'T': [0]
        }
        self.Source = ColumnDataSource(self.PlotData)
        self.Plot = figure(plot_width=850, plot_height=350, title="Reactive power / Time plot")
        self.Plot.toolbar.logo = None
        self.Plot.xaxis.axis_label = 'Time [h]'
        self.Plot.yaxis.axis_label = 'Reactive power [kvar]'
        self.Plot.line(x='T', y='Q', source=self.Source, color='blue')
        self.final_layout = self.Plot
        return

    def layout(self):
        return self.final_layout

    def updatePlot(self, Data):
        self.Source.data = Data