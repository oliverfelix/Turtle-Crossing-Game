import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle crossing Game')
screen.tracer(0)

player1 = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player1.move_front,'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.new_car()
    car.move_car()


    # Detect collision with car
    for car1 in car.new_cars:
        if car1.distance(player1) < 20:
            game_is_on = False

    # Detect successful crossing
    if player1.is_at_finish_line():
        player1.go_to_start()
        car.level_up()
        score.increase_level()

screen.exitonclick()



