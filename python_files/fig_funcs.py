def dist_plot_fig(df, col)
    '''Seaborn '''
    
    plt.figure(figsize=(10, 6))
    sns.distplot(df[col],bins=66, hist=True, kde=False, color='#2196f3')
    plt.xlabel(f'{col}')
    #plt.xlim(left=)
    sns.despine()
    plt.show()
    fig.savefig(f'../images/{col}_hist.png', transparent=True, dpi=2000, bbox_inches='tight')
    

def residuals_plot(filepfx):    
    visualizer = ResidualsPlot(linreg_model)
    visualizer.fit(x_train_lin, y_train_lin)
    visualizer.score(x_test_lin, y_test_lin)  
    visualizer.show()                         
    fig.savefig(f'../images/{filepfx}_residual_plot.png', transparent=True, dpi=2000, bbox_inches='tight')

    
    
def roc_curve_plot(filepfx):
    logit_roc_auc = roc_auc_score(y_test_log, logreg.predict(x_test_log))
    fpr, tpr, thresholds = roc_curve(y_test_log, logreg.predict_proba(x_test_log)[:,1])
    plt.figure()
    plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
    plt.plot([0, 1], [0, 1],'r--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic')
    plt.legend(loc="lower right")
    plt.savefig('Log_ROC')
    plt.show()
    fig.savefig(f'../images/{filepfx}_roc_plot.png', transparent=True, dpi=2000, bbox_inches='tight')

    

def heat_map(filepfx):
    mask = np.zeros_like(x_train_lin.corr())
    triangle_indices = np.triu_indices_from(mask)
    mask[triangle_indices] = True

    plt.figure(figsize=(35,30))
    ax = sns.heatmap(x_train_lin.corr(method='pearson'), cmap="coolwarm", 
    mask=mask, annot=True, annot_kws={"size": 18}, square=True, linewidths=4)
    sns.set_style('white')
    plt.xticks(fontsize=14, rotation=45)
    plt.yticks(fontsize=14, rotation=0)
    bottom, top = ax.get_ylim()
    ax.set_ylim(bottom + 0.5, top - 0.5)
    #plt.ylabel(ylabel=' ', labelpad=100)
    plt.show()
    fig.savefig(f'../images/{filepfx}_heat_map.png', transparent=True, dpi=2000, bbox_inches='tight')
