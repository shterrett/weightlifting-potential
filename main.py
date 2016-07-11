#!/Users/stuart/Envs/weightlifting/bin/python

import sys,os
sys.path.append(os.path.abspath('..'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.xkcd()

from weightlifting import import_data as data

wl_df = data.build_joined_data_frame()
wl_df["weight_height"] = wl_df.weight / wl_df.height

wl_df.plot.scatter(x="weight_height", y="snatch")
plt.xlabel("weight / height")
plt.ylabel("Maximum Snatch (kg)")
plt.savefig("plot/Weight:HeightvSnatch")
wl_df.plot.scatter(x="weight_height", y="cj")
plt.xlabel("weight / height")
plt.ylabel("Maximum Clean & Jerk (kg)")
plt.savefig("plot/Weight:HeightvC&J")

wl_df["normalized_snatch"] = wl_df.snatch / wl_df.weight
wl_df["normalized_cj"] = wl_df.cj / wl_df.weight

wl_df.plot.scatter(x="weight_height", y="normalized_snatch")
plt.xlabel("weight / height")
plt.ylabel("Maximum Snatch / Weight")
plt.savefig("plot/Weight:HeightvNormSnatch")
wl_df.plot.scatter(x="weight_height", y="normalized_cj")
plt.xlabel("weight / height")
plt.ylabel("Maximum Clean & Jerk / Weight")
plt.savefig("plot/Weight:HeightvNormC&J")
