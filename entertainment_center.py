import media
import fresh_tomatoes

movies = []

iron_man = media.Movie("Iron Man", "May 2, 2008")
movies.append(iron_man)

the_incredible_hulk = media.Movie("The Incredible Hulk", "June 13, 2008")
movies.append(the_incredible_hulk)

iron_man_2 = media.Movie("Iron Man 2", "May 7, 2010")
movies.append(iron_man_2)

thor = media.Movie("Thor", "May 6, 2011")
movies.append(thor)

captain_america_the_first_avenger = media.Movie("Captain America: The First Avenger", "July 22, 2011")
movies.append(captain_america_the_first_avenger)

the_avengers = media.Movie("Marvel's The Avengers", "May 4, 2012")
movies.append(the_avengers)

iron_man_3 = media.Movie("Iron Man 3", "May 3, 2013")
movies.append(iron_man_3)

thor_the_dark_world = media.Movie("Thor: The Dark World", "November 8, 2013")
movies.append(thor_the_dark_world)

captain_america_the_winter_soldier = media.Movie("Captain America: The Winter Soldier", "April 4, 2014")
movies.append(captain_america_the_winter_soldier)

guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy", "August 1, 2014")
movies.append(guardians_of_the_galaxy)

avengers_age_of_ultron = media.Movie("Avengers: Age of Ultron", "May 1, 2015")
movies.append(avengers_age_of_ultron)


fresh_tomatoes.open_movies_page(movies)