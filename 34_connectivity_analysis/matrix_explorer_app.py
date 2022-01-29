from random import random

from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, curdoc


def neuroglancer_callback(attr, old, new):
    print('attribute: ', attr)
    print('selected old: ', old)
    print('selected new: ', new)


x = [random() for x in range(500)]
y = [random() for y in range(500)]

tools = ["wheel_zoom", "save", "box_select", "lasso_select", "hover", "reset"]

source = ColumnDataSource(data=dict(x=x, y=y))
p = figure(plot_width=400, plot_height=400, tools=tools, title="Select Here")
p.circle('x', 'y', source=source, alpha=0.6)

p.output_backend = 'svg'
source.on_change('data', neuroglancer_callback)

curdoc().add_root(p)
