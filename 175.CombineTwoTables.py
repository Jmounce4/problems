import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    personFiltered = person[["personId", "firstName", "lastName"]]
    addressFiltered = address[["personId", "city", "state"]]
    merged = pd.merge(personFiltered, addressFiltered, on="personId", how="left")
    result = merged.drop(columns=["personId"])
    return result
