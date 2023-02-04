

# PLANING

## Coming Soon
- Enemy and Player Rework (inheritance from sprite.Sprite)
- Movement reword (use vectors)
- Better map design and less randomness
- better main menu
- Leaderboard
- map borders
- class to manage font styles
- Enemies get different velocities on axis (snake is get better vertical speed)
- better auto aim (fire to the next enemy)
- remove unused stuff
- Big asset rework: different assets for companions, enemies and player 
- Attack animations 

## later
- Big rework how coordinates a calculated (remove display scroll)
- Support for different resolutions and full screen
- Save games

## Maybe later
- Build system
- Controller support
- Multiplayer

# Bugs

- Companion sprites stack
- Sometimes enemy tremble because the change direction on each frame.
- No third try when playing (Respawn player Bug).
- player knock-back don`t work atm (maybe drop it, not sure)

# Sound needed

- eat sound for picking up items that restore live points.
- item dropped sound
- ...

## Done (but still not perfect)

- Enemies keep distance to each other (still needs improvement)
- bots as companions
- Health bars
- better movement AI
- Monsters do not spawn off-screen - FIXED
- Collision with player is buggy - FIXED
- Debug view, coordinates over object and more info
- more env objects (like trees)
- pysics, knock-back
- enemy projectiles
- Kill projectiles that are out of the map - FIXED
- fixed map size
- different projectiles
- Better peng sound
- player projectiles move with the player - FIXED
- player Items
- auto aim bot
- BUG: something is wrong with the enemy knock-back from companion projectiles
