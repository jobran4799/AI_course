# START

oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman",
                 "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth",
                   "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}

oscar_winners.add("Emma Watson")
copy_oscar = oscar_winners.copy()
copy_oscar.remove("Meryl Streep")
copy_oscar.clear()
print(titanic_actors & dark_knight_actors)
isTrue = True if iron_man_actors & avengers_actors != "" else False
print(isTrue)
print(actor_list.issubset(oscar_winners))
print(avengers_actors.issubset(actor_list))
movie_cast.pop()
movie_cast.remove("Matt Damon")
print(titanic_actors - oscar_winners)
print(titanic_actors ^ dark_knight_actors)
oscar_winners.update({"Cate Blanchett", "Daniel Day-Lewis"})

print(titanic_actors | dark_knight_actors)

# END
