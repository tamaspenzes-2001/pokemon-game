# pokemon-game
This game is based on this Codecademy challenge: https://www.codecademy.com/projects/practice/become-a-pokemon-master

## Gameplay
A turn-based CLI Pokémon game which can be played by 2 to 7 players. Each player can choose a trainer and an active pokémon. Each trainer has 3 pokémons to choose from, each pokémon is a specific type.
Each turn trainers can heal themselves or their active pokémon (requires healing potion), revive a knocked out pokémon (requires revive potion), change active pokémon and choose another trainer to attack.
During an attack, a trainer can deal `[random number between 1 and 4] + [level]` damage. Their active pokémon also attacks the enemy's active pokémon, deals `([level] + 1) * [attack multiplier based on the two pokémons' types]` damage (type-based attack powers can be checked in-game).
After each attack, both trainer and pokémon can earn `[damage dealt] - ([level]) / 2)` xp. Trainers can level up after every 8th, pokémons after every 6th xp (both starting from level 1). Trainers earn 1 healing and 1 revive potion.
> **Pro tip:** When choosing a trainer or active pokémon and each turn, players can check pokémons' attack power based on attacker and target type. Each turn, there's also an option to view a specific player's stat, including trainer and active pokémon health, xp and level, all their available pokémons and number of potions. These information can help in decision making.
> Oh, and watch out for the number of pokémons alive. If all your pokémons are knocked out you lose the game, no matter if you have a revive potion!