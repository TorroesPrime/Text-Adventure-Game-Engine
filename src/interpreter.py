"""main input functions when run in a terminal. """
from test_game_state import game_state_instance as gsi
from commandFactory import commandFactory


def prompt_user():
    '''provides the '>' character for the interpreter'''
    command_prompt = input("> ")
    return command_prompt

def interpreter():
    '''Primary interaction method. Initialized Game state, sets player character.'''
    print(f"\nWelcome to {gsi.dungeon.title}")
    print(gsi.adventurers_current_room.describe())
    parser = commandFactory(gsi)
    command = prompt_user()
    while command != "q":
        action = parser.executeCommand(command)
        action.execute()
        command = prompt_user()
    print("Logging off...")

interpreter()
