# Tower defense game 

Step.01 Building game window
-----
>Items
* Background
* Enemy and its health bar
* Game menu
  * Start button 
  * Pause button
  * Sound button
  * Muse button
* HP
* Game timer

Step.02 Enemy move and generate
-----
> List
* Let the enemy move along the path
* Let the enemies campaign in sequence in a round
* Re-generate the enemies (when user press the “n” button)
* Let the enemy move along the right path and alternate the enemy path to the other one in the next wave

Step.03 Drop enemy health and display tower attack range
-----
>Process
* Establish a tower then set the attack range
* Generate enemy and its health bar
* Determine whether enemy is in the attack range
  * Attack range : extend a circle with a radius of 150 from the center of the tower
  * Calculate whether the enemy distance <= radius (If yes launch an attack)
* The attack range is displayed when clicking on the tower

Step.04 Upgrade the attack range of tower and sell tower
-----
>Process
* Create the menu
* The “upgrade” button and “sell” button on the menu

Step.05 Show the building menu
-----
>Process
* Its buttons on the yellow spot

* The PCR tower is built when someone clicks the corresponding button on the build menu

* Change the attack mode of a PCR tower. (Note: The ability is one shot one kill)

Step.06 Finish the simple tower defence game
-----
>Process
* Create the buttons that can play the music or mute the game when we click the corresponding button
  * The buttons can show a white frame when we move the cursor to the button

* Show the information on the black region

* When an enemy is killed, we get 15 unit of money; When an enemy reach the base, our hp drop 1 unit

Till now we have finished this simple tower defence game .
