# file: dnd_roller/__init__.py

## Important functions: Make directly accessible when importing the package. 
# This exports the roll function so you can access it just by importing dnd_roller. 
# Without it, you need to reference roll via dice, e.g. from dnd_roller.dice import roll
from .dice import roll
from .dice import dice_roll
from .dice import sequence_rolls