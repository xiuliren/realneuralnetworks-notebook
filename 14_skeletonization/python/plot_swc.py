# pyline: disable=no-member

""" plot3d using existing visuals : LinePlotVisual """

import sys
import random

from reneu.skeleton import Skeleton

from vispy import app, visuals, scene

# build visuals
Plot3D = scene.visuals.create_visual_node(visuals.LineVisual)

# build canvas
canvas = scene.SceneCanvas(keys='interactive', title='neurons', show=True)


# Add a ViewBox to let the user zoom/rotate
view = canvas.central_widget.add_view()
view.camera = 'turntable'
#view.camera.center = (209400.0, 130600.0, 780050.0)
view.camera.center = (141706.03, 138661.87, 757758.06)
view.camera.fov = 45
view.camera.distance = 600000

def rand_web_color_hex():
    return "%06x" % random.randrange(0, 16**6)

def to_rgb(color_str):
    barr = bytearray.fromhex(color_str) 
    return (barr[0]/255, barr[1]/255, barr[2]/255)

def generate_random_color():
    hex_color = rand_web_color_hex()
    return to_rgb( hex_color )

def plot_swc(swc_file):
    # prepare data
    #swc_file = '82291.swc'
    #swc_file = '../01_data/bin/76181'
    
    try:
        sk = Skeleton.from_swc( swc_file )
    except:
        print('skip this neuron: ', swc_file)
        return

    #with open(swc_file, 'rb') as f:
    #    data  = f.read()
    #    sk = Skeleton.from_precomputed(data)

    #print('path length: ', sk.path_length)
    #print('node number: ', len(sk))
    #print('downsampling...')
    #sk.downsample(5000.0)
    #print('path length: ', sk.path_length)
    #print('node number: ', len(sk))

    points = sk.points[:, :3]
    #mean = points.mean(axis=0)
    #min_corner = points.min(axis=0)
    #max_corner = points.max(axis=0)
    #
    #parents = sk.parents
    #P0 = points[ parents >= 0, :]
    #P1 = points[parents[parents >= 0], :]


    Plot3D(points, connect=sk.edges, width=1.0, 
           color=generate_random_color(),
           method='gl', antialias=False,
           parent=view.scene)


if __name__ == '__main__':
    import os
    from tqdm import tqdm
    DATA_DIR = os.path.expanduser('~/seungmount/research/Jingpeng/14_zfish/01_data/20190923/swc')

    n = 0
    for fname in tqdm(os.listdir(DATA_DIR)):
        #print('\nfile name: ', fname)
        n += 1
        plot_swc(os.path.join(DATA_DIR, fname))
        if n > 10000:
            break

    if sys.flags.interactive != 1:
        app.run()
