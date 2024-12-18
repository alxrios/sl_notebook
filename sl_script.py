################################################################################
# This script is intended for helping with the creation of the kaggle notebook #
# that uses the spotify + lastfm dataset.                                      #
################################################################################

# Necessary libraries.
import polars as pl

# Data load
user_lis = pl.read_csv("C://Users//riosa//documents//datasets//spoty_last//User Listening History.csv")
music_info = pl.read_csv("C://Users//riosa//documents//datasets//spoty_last//Music Info.csv")

# Let's explore the datasets dimensions
user_lis.shape
music_info.shape

# user_lis only has three columns let's explore what they contain
user_lis.columns
# The columns are: track_id, user_id and playcount, let's see what kind of 
# information contains each one.
# 1) Variable: track_id
user_lis["track_id"].head()
len(user_lis["track_id"].unique())
# Only 30459 elements are unique
# Let's explore the frequencies of the elements
user_lis["track_id"].value_counts(sort = True).head(10)
user_lis["track_id"].value_counts(sort = True).tail(10)