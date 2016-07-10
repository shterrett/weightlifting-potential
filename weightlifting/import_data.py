import pandas as pd

def build_joined_data_frame():
    return pd.merge(import_iwf(), import_atg(), on=["first_name", "last_name"])\
             .rename(columns={"bweight": "weight",
                              "jerk": "cj",
                              "height (cm)": "height"})\
             .convert_objects(convert_numeric=True)

def import_atg():
    atg_df = pd.read_csv("data/atg_london_weightlifting.csv")
    atg_df["first_name"], atg_df["last_name"] = add_name_components(atg_df.Name,
                                                                    0,
                                                                    -1)
    return atg_df

def import_iwf():
    iwf_df = pd.read_csv("data/iwf_london_results.csv")
    iwf_df["first_name"], iwf_df["last_name"] = add_name_components(iwf_df.name,
                                                                    -1,
                                                                    0)
    return iwf_df

def add_name_components(name_column, first_name_idx, last_name_idx):
    names = name_column.map(lambda name: name.lower().split(" "))
    return (names.map(lambda name: name[first_name_idx]),
            names.map(lambda name: name[last_name_idx]))
