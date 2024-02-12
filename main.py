from turtle import Turtle, Screen
from random import randint
from typing import List

class TurtleRace:
    """Class to manage a turtle race game."""
    
    def __init__(self):
        """Initialize the TurtleRace object."""
        self.screen: Screen = Screen()
        self.screen.setup(width=500, height=400)
        self.screen.bgcolor('black')
        self.user_input: str = None
        self.colors: List[str] = ["red", "green", "blue", "yellow", "orange", 'purple']
        self.all_turtles: List[Turtle] = []

    def get_user_input(self) -> None:
        """Prompt the user to make a bet."""
        try:
            self.user_input = self.screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ').lower()
        except AttributeError:
            self.user_input = None

    def create_turtles(self) -> None:
        """Create and position turtles at the start line."""
        start_x: int = -230
        start_y: int = -70
        for color in self.colors:
            turtle = Turtle(shape='turtle')
            turtle.penup()
            turtle.color(color)
            turtle.goto(x=start_x, y=start_y)
            start_y += 30
            self.all_turtles.append(turtle)

    def notify(self, message: str, color: str = 'white') -> None:
        """Display notification message on the screen."""
        notify_turtle = Turtle(visible=False)
        notify_turtle.penup()
        notify_turtle.color(color)
        notify_turtle.goto(0, -180)
        notify_turtle.write(message, align="center", font=("Arial", 16, "normal"))

    def race(self) -> None:
        """Run the race until a turtle crosses the finish line."""
        is_race_on: bool = self.user_input in self.colors if self.user_input else False
        while is_race_on:
            for turtle in self.all_turtles:
                if turtle.xcor() > 230:
                    is_race_on = False
                    winner = turtle.pencolor()
                    if winner == self.user_input:
                        self.notify("You've won!", 'green')
                    else:
                        self.notify(f"Oh no, {self.user_input} didn't win. Winner is {winner}", 'red')
                    break
                random_distance = randint(a=0, b=10)
                turtle.forward(random_distance)

    def start_race(self) -> None:
        """Start the turtle race game."""
        self.get_user_input()
        self.create_turtles()
        self.race()
        play_again = self.screen.textinput(title='Play Again?', prompt='Do you want to play again? Type "yes" or "no": ').lower()
        if play_again == 'yes':
            self.reset_game()
            self.start_race()
        else:
            self.screen.bye()

    def reset_game(self) -> None:
        """Reset the game for a new race."""
        for turtle in self.all_turtles:
            turtle.hideturtle()
        self.all_turtles.clear()
        self.user_input = None
        self.screen.clear()

        self.screen.bgcolor('black')

if __name__ == '__main__':
    # Instantiate the TurtleRace object and start the race
    turtle_race = TurtleRace()
    turtle_race.start_race()
