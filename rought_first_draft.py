
# coding: utf-8

# In[87]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize 
from scipy.interpolate import interpn
from mpl_toolkits.mplot3d import Axes3D

# CB_color_cycle = ['#377eb8', '#ff7f00', '#4daf4a',
#                   '#f781bf', '#a65628', '#984ea3',
#                   '#999999', '#e41a1c', '#dede00']


# In[119]:


def density_scatter( x , y, zz, ax = None, sort = True, bins = 20, **kwargs )   :
    """
    https://stackoverflow.com/questions/20105364/how-can-i-make-a-scatter-plot-colored-by-density-in-matplotlib
    https://stackoverflow.com/questions/25286811/how-to-plot-a-3d-density-map-in-python-with-matplotlib
    https://github.com/matplotlib/matplotlib/blob/master/lib/matplotlib/mpl-data/stylelib/tableau-colorblind10.mplstyle
    """
    if ax is None :
        fig = plt.figure(figsize=(10,10))
        ax = fig.add_subplot(111, projection='3d')
        # Hide grid lines
        ax.grid(False)
        plt.axis('off')
        # Hide axes ticks
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_zticks([])
        #ax.set_facecolor('black')
        ax.set_facecolor((0.0, 0.135112, 0.304751, 1.0))
        plt.style.use('tableau-colorblind10')
        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False


    # https://numpy.org/doc/stable/reference/generated/numpy.histogramdd.html
    data , [x_e, y_e, zz_e] = np.histogramdd(
        [ x, y, zz],
        bins = bins,
        density = True
    )
    
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interpn.html
    z = interpn( 
        ( 0.5*(x_e[1:] + x_e[:-1]), 
          0.5*(y_e[1:]+y_e[:-1]), 
          0.5*(zz_e[1:] + zz_e[:-1])), 
        data,
        np.vstack([x,y,zz]).T,
        method = "linear",
        bounds_error = False
    )

    #To be sure to plot all data
    z[np.where(np.isnan(z))] = 0.0

    # Sort the points by density, so that the densest points are plotted last
    if sort :
        idx = z.argsort()
        x, y, zz, z = x[idx], y[idx], zz[idx], z[idx]

    # https://github.com/matplotlib/matplotlib/blob/d4bd4e70161ea438ba39080fd9168b34c0276250/doc/users/prev_whats_new/whats_new_2.2.rst
    ax.scatter( x, y, zz, c=z, cmap='cividis', **kwargs) # cmap='tableau-colorblind10', **kwargs )
   
#     u = np.linspace(0, 2 * np.pi, 13)
#     v = np.linspace(0, np.pi, 7)
#     xx = 2 * np.outer(np.cos(u), np.sin(v))
#     yy = 2 * np.outer(np.sin(u), np.sin(v))
#     zzz = 2 * np.outer(np.ones(np.size(u)), np.cos(v))
    
#     u = np.linspace(0,  2*np.pi, 20)
#     v = np.linspace(0, np.pi, 20)
#     radius = 4
#     xx = radius * np.outer(np.sin(u), np.sin(v))
#     yy = radius * np.outer(np.sin(u), np.cos(v))
#     zzz = radius * np.outer(np.cos(u), np.ones_like(v))
#     # https://pythonskills.co.uk/2020/01/22/plotting-a-sphere/
#     # https://stackoverflow.com/questions/40460960/how-to-plot-a-sphere-when-we-are-given-a-central-point-and-a-radius-size
#     # https://stackoverflow.com/questions/18897786/transparency-for-poly3dcollection-plot-in-matplotlib
    
#     ax.plot_wireframe(xx, yy, zzz, rstride=1, cstride=1, color='w') #, shade=0, alpha=0.5)
    norm = Normalize(vmin = np.min(z), vmax = np.max(z))
#     cbar = fig.colorbar(cm.ScalarMappable(norm = norm), ax=ax)
#     cbar.ax.set_ylabel('Density')

    return ax


# In[123]:


x = np.random.normal(size=100000)
y = np.random.normal(size=100000) #x * 3 + np.random.normal(size=100000)
z = np.random.normal(size=100000)
density_scatter( x, y, z, bins = [20,20,20] )


# In[122]:


# https://thomas-cokelaer.info/blog/2014/09/about-matplotlib-colormap-and-how-to-get-rgb-values-of-the-map/
# https://arxiv.org/pdf/1712.01662.pdf
from matplotlib import cm
cm.cividis(0)

