# Predicting maximum Snatch and Clean & Jerk by height/weight ratios

## Data sources
+ [IWF London Olympics results](http://www.iwf.net/results/results-by-events/?event=214)
+ [All Things Gym London Olympics Statistics](http://www.allthingsgym.com/london-2012-weightlifting-athletes-statistics/)

### Local copies
+ [IWF results](data/iwf_london_results.csv)
+ [ATG statistics](data/atg_london_weightlifting.csv)

The IWF data lacks heights, and the ATG data lacks competition totals. The data
sources can be matched on name. IWF has the name as `LAST First` and ATG has the
name as `First Last`.

Height will be pulled from ATG.

Weight, Snatch (max), C&J (max), Category will be pulled from IWF

NOTE: Units will be SI throughout:
+ Weight in kg
+ Height in cm


