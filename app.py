# app.py
import click
import time
from Game import Cards


@click.command()
def play():
    """Simple program that tests your memory skills."""
    is_game_over = False

    click.clear()
    click.echo('How many different cards do you want to play with?')
    count = int(click.prompt('Enter a number no greater than 20'))

    if count > 20:
        return

    cards = Cards.Cards(count)

    while not is_game_over:

        cards.print()
        first = int(click.prompt('Open first card'))
        cards.play(first)
        second = int(click.prompt('Open second card'))
        # TODO: Validate that first isn't the same as second
        is_game_over = cards.play(second)
        if is_game_over:
            click.echo('You won!')
        else:
            time.sleep(2)
            click.clear()


if __name__ == '__main__':
    play()
