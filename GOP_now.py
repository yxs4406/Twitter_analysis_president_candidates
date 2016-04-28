#!/usr/bin/env python
import tools
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

Candidates = ['realDonaldTrump','TedCruz','JohnKasich','HillaryClinton','BernieSanders']
opinion = pd.DataFrame(columns=['Positive','Negative','Ratio'],index=Candidates)
number_tweets = 20
for candidate in Candidates:
    gCT = tools.wrap_tweet.get_tweet(number_tweets,candidate)
    (p,n) = tools.emotion_check.PNrate(gCT)
    if p ==0 or n ==0:
        print 'Data too small for candidate',candidate
    else:
        print 'Candidate ',candidate, '   Positive: ',p,'Negative:',n
        opinion.ix[candidate]['Positive'] = p
        opinion.ix[candidate]['Negative'] = -n
        opinion.ix[candidate]['Ratio'] = float(p)/float(n)
print opinion

opinion[['Positive','Negative']].plot(kind='bar',stacked=True,fontsize=15)
plt.tight_layout()
plt.savefig('emotional.jpg')

fig, ax = plt.subplots()
ind = np.arange(5)+0.3
width = 0.5
mea = opinion['Ratio']
ax.set_xlim(-width,len(ind)+width)
ax.set_xticks(ind)
ax.set_ylabel('positive/negative',fontsize=15)
ax.bar(ind, mea, width, color='r')
ax.set_xticklabels(('Donald Trump', 'Ted Cruz', 'John Kasich', 'Hillary Clinton', 'Bernie Sanders'),rotation=45)
plt.tight_layout()
plt.savefig('opinion.jpg')
