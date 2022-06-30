import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import parallel_coordinates as pcp
import matplotlib.patches as mpatches
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE


def plot_groups(data, group, colors = ['cadetblue','#3D0035'], xlabel = f'$PC_1$', ylabel = f'$PC_2$', labels = [], legend_title = '', figsize = [8,8], group_size = [0,1], ticks = False, lab = True, fontsize = 14, leg = True, labelsize = 16, filename = 'image.png'):
    plt.figure(figsize = figsize)
    for yi in group_size:
        idx = group == labels[yi]
        plt.scatter(data[idx,0], data[idx,1], color = colors[yi],
               alpha = 0.8, label = labels[yi])
    if ticks is False:
        plt.xticks([])
        plt.yticks([])
    if lab is True:
        plt.xlabel(xlabel, fontsize = labelsize, labelpad = 15)
        plt.ylabel(ylabel, fontsize = labelsize, labelpad = 15)
    if leg is True:
        plt.legend(title = legend_title, title_fontsize = fontsize, loc = 1, fontsize = fontsize)
    plt.savefig(filename, bbox_inches = 'tight')

if __name__ == '__main__':

    #load in data
    data = pd.read_csv('OTUS_Adjusted.csv')
    #preprocessing for figure 1
    collist = []
    for i in data.columns:
        collist.append(i)
    collist.remove('Indiv')
    collist.remove('Finger_or_Key')
    correlation = data.corr()

    #figure 1
    plt.figure(figsize = [8,8])
    ax = sns.heatmap(correlation, mask = np.triu(correlation), cbar_kws={"location":'top', "pad":0.01}, center = -0.9, cmap = 'twilight_r', annot = True, vmin = -0.8, vmax = 0.8, yticklabels = ([' '] + collist[1:]), xticklabels = collist[:-1], annot_kws = {'fontsize':12})
    plt.tick_params(size = 0, labelsize = 14, pad = 15)
    cbar = ax.collections[0].colorbar
    cbar.ax.tick_params(labelsize = 12, pad = 10)
    ax = plt.gca()
    t = plt.text(7,4, "Correlations Between the Relative\n Abundances of Bacteria\n on your Fingers",
            horizontalalignment = 'center', fontsize = 15)
    t.set_bbox(dict(facecolor = 'white', alpha=0.5,edgecolor='white'))
    plt.savefig('heatmap.png', bbox_inches = 'tight')

    #preprocessing for figure 2
    parallel = data.drop('TM7', axis = 1)
    parallel = parallel.drop('Thermi', axis = 1)
    parallel = parallel.drop('Finger_or_Key', axis = 1)

    #figure 2
    plt.figure(figsize = (12,6))
    ax = pcp(parallel, 'Indiv', color = ['lightblue','#493BE3', '#3D0035'], axvlines_kwds = {'alpha':0.6, 'color':'k'}, alpha = 0.5)
    ax.grid(axis = 'y',color = 'k', alpha = 0.5, linestyle = '-.')
    ax.grid(axis = 'x', color = 'k', alpha = 0.5)
    ax.tick_params(labelsize = 14, size = 0, pad = 20)
    ax.set_ylim(top=1)
    labels = ['M3', 'M9', 'M2']
    a = mpatches.Patch(color = 'lightblue', alpha = 1, label = labels[0])
    b = mpatches.Patch(color = '#493BE3', alpha = 1, label = labels[1])
    c = mpatches.Patch(color = '#3D0035', alpha = 1, label = labels[2])
    artists = [a, b, c]
    plt.legend(handles = artists, labels = labels, fontsize = 14, markerfirst = False, bbox_to_anchor = [1.15, 0.665], frameon = True)
    plt.title('Relative Abundances of Bacteria by Individual', fontsize = 16, pad = 20)
    plt.savefig('parallel.png', bbox_inches = 'tight')
    
    #preprocessing for figure 3
    no_fing = data.drop(columns = ['Finger_or_Key'])
    no_fing
    num_indiv = data.drop(columns = ['Indiv','Finger_or_Key'])
    pca = PCA()
    pca_scaled = pca.fit_transform(num_indiv)
    
    #figure 3
    plot_groups(data=pca_scaled, colors = ['cadetblue','#3D0035', '#493BE3'], group_size = [0,1,2], legend_title = 'Bacteria by Individual', group = no_fing['Indiv'], labels = ['M3', 'M9', 'M2'], filename = 'Indiv.png')
    
    #preprocessing for figure 4
    no_indiv = data.drop(columns = ['Indiv'])
    all_loc = no_indiv['Finger_or_Key'].unique()
    fing = ['Thmr', 'Thml','Pinr', 'Pinl', 'Rinr', 'Rinl', 'Indr','Indl', 'Midr', 'Midl']
    key = np.setdiff1d(all_loc,fing)
    no_indiv['Dicot'] = no_indiv['Finger_or_Key'].replace(fing, 'Finger')
    no_indiv['Dicot'] = no_indiv['Dicot'].replace(key, 'Key')
    no_indiv = no_indiv.drop('Finger_or_Key', axis = 1)
    no_indiv
    numeric_dicot = no_indiv.drop(columns = ['Dicot'])
    numeric_dicot
    pca = PCA()
    pc_dicot = pca.fit_transform(numeric_dicot)
    
    #figure 4
    plot_groups(data=pc_dicot, legend_title = 'Location of Bacteria', group = no_indiv['Dicot'], labels = ['Key', 'Finger'], filename = 'Location.png')
    
    #preprocessing for figure 5
    all_loc = data['Finger_or_Key'].unique()
    fing = ['Thmr', 'Thml','Pinr', 'Pinl', 'Rinr', 'Rinl', 'Indr','Indl', 'Midr', 'Midl']
    key = np.setdiff1d(all_loc,fing)
    data['Dicot'] = data['Finger_or_Key'].replace(fing, 'Finger')
    data['Dicot'] = data['Dicot'].replace(key, 'Key')
    data = data.drop('Finger_or_Key', axis = 1)
    m3 = data[data.Indiv == 'M3']
    tsne_data = m3.drop('Indiv', axis = 1)
    tsne_num = tsne_data.drop(columns = ['Dicot'])
    tsne = TSNE(random_state = 146, perplexity = 10)
    tsne_scaled = tsne.fit_transform(tsne_num)
    
    #figure 5
    plot_groups(data=tsne_scaled, legend_title = 'Bacteria Location for M3', group = tsne_data['Dicot'], xlabel = f'$TSNE_1$', ylabel = f'$TSNE_2$', labels = ['Key', 'Finger'], filename = 'M3.png')