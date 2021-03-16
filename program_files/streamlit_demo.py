import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.header("This is a Steamlit demo")

x = 10
st.write(x)

"""
### Here is a rendered docstring
* streamlit renders docstrings!
* asterisk is markdown for bullets
* bullets are good
* [Link to Markdown Primer](https://stackedit.io)
"""

y = np.random.standard_normal(1000000)
plt.rcParams["figure.figsize"] = 4,2
fig, axes = plt.subplots(figsize=(4,2))
axes.hist(y, bins=50, color='g', edgecolor='w')
st.pyplot(fig)



