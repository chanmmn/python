import scipy.stats as stats
data = [14, 14, 16, 13, 12, 17, 15, 14, 15, 13, 15, 14]
#perform one sample t-test
stats.ttest_1samp(a=data, popmean=15)