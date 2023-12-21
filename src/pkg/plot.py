import os

import matplotlib.pyplot as plt
import seaborn as sns
import mpl_toolkits.mplot3d.axes3d
from IPython.display import Image

from sklearn import decomposition
from sklearn.manifold import TSNE

# Util

plt.style.use('ggplot')

def save(savename, saving_function):
    parent_abs = os.path.abspath(os.path.join(os.getcwd(),os.pardir))
    parent = 'reports'
    path = os.path.join(parent_abs, parent, savename)
    
    saving_function(path)
    
    print('figure saved on ', path)
# 
# _____________________________
# 
# Feature visualization


def pca_2d(X, hue=[], title="PCA 2 dimension reduction", savename=False):
    '''
    receives X features
    return a scatter plot of 2 components pca
    and color it with third component
    '''
    fig = plt.figure(figsize=(10,10))

    pca = decomposition.PCA(n_components=3)
    view = pca.fit_transform(X)

    if len(hue) > 0:
        c=hue
    else:
        c=view[:,2]

    plt.scatter(view[:,0], view[:,1], c=c)
    plt.xlabel('PCA-1')
    plt.ylabel('PCA-2')

    plt.title(title)

    if savename :
        save(savename, fig.savefig)

    plt.show()


def pca_3d(X, hue=[],  title="PCA 3 dimension reduction", multiple_graph=False, savename=False):
    '''
    plot a 3 components pca
    if multiple_graph: more 3 2d combinations        
    '''

    pca = decomposition.PCA(n_components=4)
    view = pca.fit_transform(X)

    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(221, projection='3d')
    fig.patch.set_facecolor('white')
    alpha = 0.4

    if len(hue) > 0:
        c=hue
    else:
        c=view[:,3]

    ax.scatter(view[:,0], view[:,1], view[:,2], c=c, alpha=alpha)
    ax.set_xlabel('PCA-1')
    ax.set_ylabel('PCA-2')
    ax.set_zlabel('PCA-3')
    ax.grid(color='gray',linewidth=1.2)

    if multiple_graph:

        views = [(0,1,'PCA-2','PCA-3'),
                 (0,2,'PCA-1','PCA-3'),
                 (1,2,'PCA-1','PCA-2')]
        for i, v in enumerate(views):
            ax = fig.add_subplot(222+i)
            ax.scatter(view[:,v[0]], view[:,v[1]], c=c, alpha=alpha)
            ax.set_xlabel(v[2])
            ax.set_ylabel(v[3])
            ax.grid(color='gray',linewidth=0.2)
        

    plt.title(title, loc='center')

    if savename :
        save(savename, fig.savefig)

    plt.show()


def t_sne(X, hue=[], title="t-SNE dimensionality reduction", savename=False):
    '''
    plot two component t_SNE
    '''
    view = TSNE(n_components=3, random_state=123).fit_transform(X)
    
    if len(hue) > 0:
        c = hue
    else:
        c = view[:,2]
    
    fig = plt.figure(figsize=(10,10))
    plt.scatter(view[:,0], view[:,1], c=c, alpha=0.5)
    plt.xlabel('t-SNE-1')
    plt.ylabel('t-SNE-2')
    plt.title(title)

    if savename :
        save(savename, fig.savefig)
    plt.show()


def template(savename=False, title=""):

    fig = plt.figure(figsize=(10,10))
    plt.title(title)

    if savename:
        save(savename, fig.savefig)
    plt.show()

def corr_map(correlation_matrix, title="Correlation matrix", savename=False):
    fig = plt.figure(figsize=(12,10))
    sns.heatmap(correlation_matrix, annot=False, cmap='coolwarm', fmt=".2f")
    plt.title(title)
    
    if savename:
        save(savename,fig.savefig)
    plt.show()
