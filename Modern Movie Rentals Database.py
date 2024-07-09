#Description: A program designed for MMR to add new movie purchases to their database
#Author: DCE
#Date: Jul 8

#Program libraries
import datetime
import time


#Program constants

MOVIE_NUM = 10285
GENRES = ['D', 'C', 'SF', 'M', 'H']
RATINGS =['G', 'P', 'R']
MIN_RENT = 1.99
MAX_RENT = 8.99


#Program functions

def GenreTag(genre):
    #Turns user letter choice into full text for storage
    if genre == 'D':
        full_genre = "Drama"
    if genre == 'C':
        full_genre = "Comedy"
    if genre == 'SF':
        full_genre = "Science Fiction"
    if genre == 'M':
        full_genre = "Musical"
    if genre == 'H':
        full_genre = "History"
    return full_genre


def RatingTag(rating):
    #Turns user letter choice into full text for storage
    if rating == 'G':
        full_rating = "General"
    if rating == 'P':
        full_rating = "Parental Guidance"
    if rating == 'R':
        full_rating = "Restricted"
    return full_rating

def Money(enter_num):
    #Formats a float into a cash value.
    price_dsp = "${:,.2f}".format(enter_num)
    return price_dsp

def Progress():
    #Creates a simple progress bar 
    for i in range (51):
        print('\r[' + '*' * i + ' ' * (50 - i) + ']', end='')
        time.sleep(0.01)
    print()

#checks for movieID file to keep listing updated.
try:
    with open ("CurrentID.dat") as file:
        movie_id = file.read()
        movie_id =int(movie_id)
except:
    movie_id = MOVIE_NUM
    

print (movie_id)
print()  
print()
print("**************************************************************************************")
print()
print ("Welcome to Modern movie Rental's Movie Database. Complete all fields. Enter 'END' for title to exit.")
print()
while True:
    movieid_dsp = movie_id
    movie_title = input ("Enter the title of the movie: ").upper()
    if movie_title == 'END':
        break
    else:

        while True: 
            print()
            movie_genre = input ("Enter the movie's genre: 'D' for Drama, 'C' for Comedy, 'SF' for Science Fiction, 'M' for Musical, or 'H' for Horror: ").upper()
            if movie_genre in GENRES:
                genre_dsp =GenreTag(movie_genre)
                break
            else:
                print ("Data Entty Error: Invalid Genre entered, try again,")

        while True:
            print()
            movie_rating = input ("Enter the movie's rating: 'G' for General, 'P' for Parental Guidance, or 'R' for Restricted: ").capitalize()
            if movie_rating in RATINGS:
                rating_dsp = RatingTag(movie_rating)
                break
            else:
                print ("Data Entty Error: Invalid Rating entered, try again,")

        while True:
            print()
            try:
                rent_price = float(input("Enter the rental price for the movie: "))
            except:
                print ("Data Entry Error: Value must be in the form 999,999.99.")
            if rent_price < MIN_RENT or rent_price > MAX_RENT:
                print (f"Data Entry Error: Rental price must be between {MIN_RENT} and {MAX_RENT}.")
            else:
                price_dsp = Money(rent_price)
                break
                
        print()
        print()
        Progress()
        print()
        print()
        f = open("Movies.dat", "a")

        f.write(f"{movieid_dsp}, {movie_title}, {genre_dsp}, {rating_dsp}, {price_dsp}\n")

        f.close()
        print()
        print("This has been saved.")
        print()
        movie_id += 1

        f = open("CurrentID.dat", "w")
        f.write(f"{movie_id}")
        f.close()


print()
print()
print ("Thank you and have a nice day.")
print()
print()
