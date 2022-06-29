import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches
import matplotlib.colors as colors

if __name__ == '__main__':

    #read in data
    data = pd.read_csv('movies_metadata_cleaner.csv')

    #look at movies dataframe
    data
    
    #scale budget
    budget = data['budget'].tolist()
    scaler = (10**6)
    scaled_budget = np.divide(budget, scaler)
    scaled_budget
    
    #add scaled_budget column to movies df
    data['scaled_budget'] = scaled_budget
    data
    
    #keywords
    fem_words = ' her | hers | she |herself'
    mal_words = ' he | him | his |himself'

    #Dataframe with female protagonists
    data_fem = data[data["overview"].str.contains(fem_words)]
    data_fem = data_fem[data_fem["overview"].str.contains(mal_words) == False]
    data_fem

    #Dataframe with male protagonists
    data_mal = data[data["overview"].str.contains(mal_words)]
    data_mal = data_mal[data_mal["overview"].str.contains(fem_words) == False]
    data_mal
    
    #budget data
    fem_budg = data_fem['scaled_budget'].tolist()
    mal_budg = data_mal['scaled_budget'].tolist()
    
    #drop movies with budget = 0
    fem_budg = [i for i in fem_budg if i != 0]
    mal_budg = [i for i in mal_budg if i != 0]
    
    #number of movies
    len(fem_budg)
    len(mal_budg)
    
    #budget figure
    title = "Does Protagonist Gender affect the Budget?"
    values = [fem_budg, mal_budg]
    labels = ['Female   \n n=1159  ','Male    \n n=3724  ']
    xlabel = 'Movie Budget\n(millions of dollars)'
    filename = 'Budget.png'
    fig, ax = plt.subplots(figsize=(16, 10))
    bplot = ax.boxplot(values, labels = labels, vert = False, patch_artist = True, flierprops=dict(marker='s', markersize=4))
    colors = ['pink', 'cornflowerblue']
    for patch, color in zip(bplot['boxes'], colors):
      patch.set_facecolor(color)
    for median in bplot['medians']:
        median.set_color('black')
    ax.set_title(title, fontsize = 20, pad = 35)
    ax.set_xlabel(xlabel, fontsize = 18, labelpad = 30)
    ax.set_xlim([0,300])
    ax.grid(axis = 'x', color = 'black', linewidth = 0.2, linestyle = '-.')
    ax.tick_params(axis = 'x', size = 0, labelsize = 16)
    ax.tick_params(axis = 'y', size = 0, labelsize = 16)
    [ax.spines[i].set_visible(False) for i in ax.spines]
    plt.savefig(filename, bbox_inches = 'tight')
    plt.show()
    
    #revenue data
    fem_rev = data_fem['revenue'].tolist()
    mal_rev = data_mal['revenue'].tolist()

    #drop movies with revenue = 0
    fem_rev = [i for i in fem_rev if i != 0]
    mal_rev = [i for i in mal_rev if i != 0]
    
    #number of movies
    num_rfem = len(fem_rev)
    num_rmal = len(mal_rev)
    
    #log transformation
    fem_rev_log = np.log10(fem_rev)
    mal_rev_log = np.log10(mal_rev)

    #revenue figure
    plt.figure(figsize = [16, 10])
    colors = ['pink','cornflowerblue']
    ax = sns.stripplot(data = [fem_rev_log, mal_rev_log],
             palette = colors, alpha = 0.6, edgecolor = 'k', linewidth = 0.6,
                  size = 6.5)
    [ax.spines[i].set_visible(False) for i in ax.spines]
    labels = [item.get_text() for item in ax.get_xticklabels()]
    labels[0] = 'Female'
    labels[1] = 'Male'
    ax.set_xticklabels(labels)
    ax.tick_params(axis = 'x', labelsize = 18, pad = 20)
    plt.tick_params(size = 0, labelsize = 18)
    n_rows = [0,1]
    counts = [num_rfem, num_rmal]
    for i in n_rows:
        ax.text(i,-1.75, 'n = ' + str(counts[i]), fontsize = 16,
           horizontalalignment = 'center')
    title = "Does Protagonist Gender affect Movie Revenue?"
    ax.set_title(title, fontsize = 20, pad = 20)
    plt.grid(axis = 'y', color = 'grey', linestyle = '--', linewidth = 0.2)
    plt.ylabel('Movie Revenue\n(log10)', fontsize = 18, labelpad = 20)
    filename = 'Revenue.png'
    plt.savefig(filename, bbox_inches = 'tight')
    plt.show()
    
    #popularity data
    data1 = data_fem['popularity'].tolist()
    data2 = data_mal['popularity'].tolist()
    
    #drop movies with popularity = 0
    data1 = [i for i in data1 if i != 0]
    data2 = [i for i in data2 if i != 0]
    
    #log transformation
    data1_log = np.log10(data1)
    data2_log = np.log10(data2)
    
    #number of movies
    len(data1_log)
    len(data2_log)

    #popularity figure
    f,[ax_hist1,ax_hist2] = plt.subplots(2, figsize = (16,10), sharex = True, gridspec_kw = {'height_ratios':[0.5,0.5]})

    ax_hist1.set_title('Does Protagonist Gender affect Movie Popularity?          ', fontsize = 20, pad = 40)
    ax_hist2.set_xlabel('Movie Popularity           \n(log10)            ', fontsize = 18, labelpad = 30)

    bins = 30
    ax_hist1.hist(data1_log, bins = bins, rwidth = 0.9, color = 'pink')
    [ax_hist1.spines[i].set_visible(False) for i in ax_hist1.spines]
    ax_hist1.tick_params(size = 0, labelsize = 18, pad = 20)
    ax_hist1.set_ylabel('Female\nn=5883', fontsize = 18, labelpad = 50, rotation = 0)
    ax_hist1.yaxis.set_label_position("right")

    ax_hist2.hist(data2_log, bins = bins, rwidth = 0.9, color = 'cornflowerblue')
    [ax_hist2.spines[i].set_visible(False) for i in ax_hist2.spines]
    ax_hist2.tick_params(size = 0, labelsize = 18, pad = 20)
    ax_hist2.set_ylabel('Male\nn=16992', fontsize = 18, labelpad = 50, rotation = 0)
    ax_hist2.yaxis.set_label_position("right")
    ax_hist2.set_xlim([-6,2])
    
    ax_hist1.grid(axis = 'y', color = 'black', linestyle = '--', linewidth = 0.2)
    ax_hist2.grid(axis = 'y', color = 'black', linestyle = '--', linewidth = 0.2)
    filename = 'Popularity.png'
    plt.savefig(filename, bbox_inches = 'tight')
    plt.show()