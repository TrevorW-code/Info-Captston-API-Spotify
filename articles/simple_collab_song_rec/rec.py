from pandas import read_csv

# Literally just a csv of ratings by author
data_url = 'https://gist.githubusercontent.com/jackbandy/5cd988ab5c3d95b79219364dce7ee5ae/raw/731ecdbecc7b33030f23cd919e6067dfbaf42feb/song-ratings.csv'
ratings = read_csv(data_url,index_col=0)

# finding the euclidean distance (basically cosine similarity)
from scipy.spatial.distance import euclidean
def distance(person1,person2):
  distance = euclidean(person1,person2)
  return distance

def most_similar_to(name):
  person = ratings.loc[name]
  closest_distance=float('inf')
  closest_person=''
  for other_person in ratings.itertuples():
    if other_person.Index==name:
      # don't compare a person to themself
      continue
    distance_to_other_person = distance(person,ratings.loc[other_person.Index])
  if distance_to_other_person < best_similarity:
      # new high score! save it
      closest_distance = distance_to_other_person
      closest_person = other_person.Index
  return closest_person