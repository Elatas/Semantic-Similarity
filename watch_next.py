import spacy
nlp = spacy.load('en_core_web_md')

# Defining the function that will provide the user with next movie to watch
def next_movie(description): # The function takes in "description" as parameter
    with open ("movies.txt", "r") as movies_file: # Open the movie.txt file for reading
        movie_list = []
        for line in movies_file:
            movie_list.append(line.split(':'))
            count = len(movie_list)
            similarity_list = []
            
            model_sentence = nlp(description)
        
        for line in range(0, count):
            similarity_list.append(nlp(movie_list[line][1]).similarity(model_sentence)) # Checking similarity
            max_similarity = max(similarity_list)
            max_similarity_index = similarity_list.index(max_similarity)
            return movie_list[max_similarity_index][0]



# The movie watched by the user:
movie_watched = ('''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the 
Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery
and trained as a gladiator.''')


# Printing the outcome
print("We would recommend the following movie to watch next: " + next_movie(movie_watched))