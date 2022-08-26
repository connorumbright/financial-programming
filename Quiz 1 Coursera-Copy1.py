#!/usr/bin/env python
# coding: utf-8

# In[74]:


import pandas as pd
import numpy as np


# In[103]:


returns = pd.read_csv('C:\\Users\\Connor Umbright\\Downloads\\Portfolios_Formed_on_ME_monthly_EW.csv',
                     header=0, index_col=0, parse_dates=True,na_values=-99.99)


# In[104]:


returns.head()


# In[105]:


columns =['Lo 20', 'Hi 20']
returns = returns[columns]
returns.head()


# In[106]:


returns = returns/100
returns.head()


# In[107]:


returns.plot.line()


# In[108]:


returns.index = pd.to_datetime(returns.index, format="%Y%m")
returns.head()


# In[109]:


returns.index


# In[110]:


returns.index = returns.index.to_period('M')
returns.head()


# In[111]:


returns.head()


# In[112]:


returns[:"1950"]["Lo 20"].plot()


# In[113]:


returns["1999":][:"2015"]["Lo 20"].plot()


# In[114]:


returns.head()


# In[115]:


returns[:'1996']


# In[116]:


returns['199901':'2015']


# In[124]:


returns1 = returns.loc['199901':'2015']


# In[129]:


returns1.head()


# In[130]:


returns1.shape


# In[131]:


n_months = returns1.shape[0]
return_per_month = (returns1+1).prod()**(1/n_months) - 1
return_per_month


# In[132]:


annualized_return = (return_per_month+1)**12 - 1
annualized_return


# In[133]:


returns1.std()


# In[134]:


annualized_vol = returns1.std()*np.sqrt(12)
annualized_vol


# In[136]:


drawdown(returns1["Lo 20"])["Drawdowns"].min()


# In[137]:


returns1.head()


# In[143]:


def drawdown(returns1_series: pd.Series):
    """Takes a time series of asset returns.
       returns a DataFrame with columns for
       the wealth index, 
       the previous peaks, and 
       the percentage drawdown
    """
    wealth_index = 1000*(1+returns1_series).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdowns = (wealth_index - previous_peaks)/previous_peaks
    return pd.DataFrame({"Wealth": wealth_index, 
                         "Previous Peak": previous_peaks, 
                         "Drawdown": drawdowns
                        })


# In[145]:


drawdown(returns1["Lo 20"]).min()


# In[146]:


drawdown(returns1["Lo 20"]).idxmin()


# In[147]:


drawdown(returns1["Hi 20"]).min()


# In[148]:


drawdown(returns1["Hi 20"]).idxmin()


# In[149]:


import pandas as pd
import edhec_risk_kit_104 as erk
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[150]:


hfi = erk.get_hfi_returns()


# In[151]:


hfi.std(ddof=0)


# In[152]:


hfi[hfi<0].std(ddof=0)


# In[153]:


erk.semideviation(hfi)


# In[158]:


hfi = pd.read_csv("edhec-hedgefundindices.csv",header=0, index_col=0, parse_dates=True, infer_datetime_format=True)


# In[159]:


hfi.head()


# In[166]:


hfi['20090101':]


# In[167]:


hfi = hfi.loc['20090101':]


# In[168]:


hfi.head()


# In[171]:


erk.semideviation(hfi)


# In[172]:


erk.skewness(hfi)


# In[173]:


erk.kurtosis(hfi)


# In[ ]:




