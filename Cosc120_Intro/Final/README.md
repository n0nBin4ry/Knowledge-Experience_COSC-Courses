# Final

Score: 85/100

The final was to come up with our own small project based off a past assignment.
I can't find my proposed prompt but I improved upon my game assignment.

## Features of Game
- Player roams from room to room (in 3-by-3 building) trying to assasinate the enemy AI while the AI tries to assasinate player.
- Player either picks a door to watch or enter, or player enters overwatch mode where they watch over all doors to catch enemy.
	- Based off the decision, the player assassinates (or is assassinated by) the enemy. 
	- If player watches a door and enemy walks through that door, then player instantly kills enemy
		- If enemy walks in other doors, there is a high chance that the player is assasinated
	- If the player is in overwatch mode then there is a chance determined by how many doors in room
- In corner rooms, you can set traps where trapped unit stays still for 2 rounds and has a high chance of being killed
- If two units enter room at same time then 50/50 chance on who is assasinated.
- Different messages for different deaths/kills
- Enemy AI has same choices as player.

### Possible Future Features
- Written in anything but Python, looking back I much rather developing in compiling languages
- Smarter AI and a sound-alert system
- More options (and maybe findable tools/weapons) determined by room.
- Different maps.
- More characters with ability; and maybe multiplayer
- Will make a better, more sleek TUI (or actual graphics if I decide that will look better)
- MAYBE if maps are big enough, player(s) control a team of units to fight each other, tactical RPG style
