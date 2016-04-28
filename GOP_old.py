#! usr/bin/env python
import process_old_tweets
from matplotlib import pyplot as plt
import pandas as pd

can1 = process_old_tweets.readin('hillary_100.csv').columns=['tweets1']
can2 = process_old_tweets.readin('trump_100.csv').columns=['tweets2']
print type(can1), can1
df = [can1,can2]
old_tweet = pd.concat(df,axis=1)

ax=ddf.plot()
ax.legend(['Trump','Hillary'],loc='best')
ax.set_ylabel('Positive / Negative')
ax.set_xticklabels(['2015-04-01','2015-06-01','2015-08-01','2015-10-01','2015-12-01','2016-02-01','2016-04-01'],rotation=40)
plt.tight_layout()
plt.savefig('long_run_10_tweets.jpg')
