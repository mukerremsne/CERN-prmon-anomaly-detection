import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def generate_fake_prmon(filename,base_mem,spike=False):
  rows=60
  time=np.arange(rows)
  pss=np.full(rows,base_mem)+np.random.randint(-2000,2000,rows)
  if spike:
     pss[30:45]=pss[30:45]*5
  df=pd.DataFrame({'time':time,'pss':pss, 'vmem':pss*1.2, 'rss':pss*0.8})
  df.to_csv(filename, sep='\t', index=False)
  print(f"Generated{filename}")
generate_fake_prmon('normal test.txt',100000)
generate_fake_prmon('anomaly test.txt',100000,spike=True)
df_n=pd.read_csv('normal test.txt',sep='\t')
df_a=pd.read_csv('anomaly test.txt',sep='\t')
threshold=df_n['pss'].mean()+(3*df_n['pss'].std())
df_a['is_anomaly']=df_a['pss']>threshold
plt.figure(figsize=(10,5))
plt.plot(df_a['time'],df_a['pss'],label='Process Memory(PSS)', color='blue')
plt.axhline(y=threshold, color='red', linestyle='--', label='Anomaly Threshold')
anomalies=df_a[df_a['is_anomaly']]
plt.scatter(anomalies['time'],anomalies['pss'], color='red', label='DECTED ANOMALY')
plt.title("ATLAS Software Monitoring: Anomaly Detection")
plt.xlabel('Time(s)')
plt.ylabel('Memory(KB)')
plt.legend()
plt.show()
