# Wanderlust game

Wanderlust game

Imports back-end classes from game.py
Player gets in different rooms (kitchen, dining hall, ballroom).
In these rooms can be items player can take and enemies player
can talk or fight with. To defeat the enemy player has to have
appropriate item. The game ends when player defeats two enemies
or when player is defeated. Once player has successfully used
the item it is removed from his/her backpack.

Playing this game we will have an infinite amount of joy so 
that user will be happy till the end of the day ^_^

The example of run

In every room player has a few oprions to consider: talk, take, fight, globe side (to move to another room)

1) Player starts from kitchen and has all options to choose. 
![Зображення 11 03 23 о 10 51](https://user-images.githubusercontent.com/116552240/224475003-8292ac90-64e1-4f53-a546-abb6d01278f4.jpg)

2) If player chooses talk, take or fight it will be provided with negative response in
this particular room no items to take, persons to fight or talk with

![Зображення 11 03 23 о 10 54](https://user-images.githubusercontent.com/116552240/224475114-33167ef1-ad7d-4d85-a509-bdf3aaec89dd.jpg)
![Зображення 11 03 23 о 10 54](https://user-images.githubusercontent.com/116552240/224475119-28a3d446-e8e9-439f-869e-709079fe3d92.jpg)
![Зображення 11 03 23 о 10 55](https://user-images.githubusercontent.com/116552240/224475133-bf75546a-1535-4e3a-bc75-6f515d095232.jpg)

If there is an item to take or the enemy to fight with user will be provided with this information
![Зображення 11 03 23 о 10 56](https://user-images.githubusercontent.com/116552240/224475171-448ea089-30ba-4e10-804f-d0728a7596c5.jpg)

3) So the only option here is to move to another room by typing the appropriate globe side
![Зображення 11 03 23 о 10 57](https://user-images.githubusercontent.com/116552240/224475214-6d819e3c-b39f-47ff-b3ee-209735da5afd.jpg)

If the globe side is incorrect player receives appropriate message:
![Зображення 11 03 23 о 10 58](https://user-images.githubusercontent.com/116552240/224475253-99995b4b-7606-49f2-aa02-360ed6986aee.jpg)

If there is no rooms linked to that globe sede the game simply asks to make a desicion again
![Зображення 11 03 23 о 10 59](https://user-images.githubusercontent.com/116552240/224475292-4b8d6518-454a-4da9-878a-273ccc0113fb.jpg)

4) Once we moved to the room that has item and enemy player can interact with each objects like that
![Зображення 11 03 23 о 11 01](https://user-images.githubusercontent.com/116552240/224475373-55707534-b5a1-4ac1-8187-3b15ed94987c.jpg)
![Зображення 11 03 23 о 11 01 (1)](https://user-images.githubusercontent.com/116552240/224475387-aacb381b-7461-4ce4-b9d4-c159296896bb.jpg)

If player takes the item it disappers from the room but is in the player's backpack

5) If playes chooses fight, it is provided with option to choose the item to fight with
![Зображення 11 03 23 о 11 02](https://user-images.githubusercontent.com/116552240/224475444-2e357fd4-aa28-482c-a2b8-bba779c1f206.jpg)

If player chooses the item it doesn't have the appropriate message appears and player is redirected to the main menu of the room
![Зображення 11 03 23 о 11 03](https://user-images.githubusercontent.com/116552240/224475486-29e7b55c-7d37-4679-b76b-02da4961dad7.jpg)

If the item player choosed can not defeat the enemy, enemy defeats player and game stops
![Зображення 11 03 23 о 11 04](https://user-images.githubusercontent.com/116552240/224475509-c14417da-6844-4def-906f-8b9ae5bd96d7.jpg)

If the item player choosed is appropriate to defeat the enemy the message appears
![Зображення 11 03 23 о 11 05](https://user-images.githubusercontent.com/116552240/224475569-56425065-d14a-47a9-bdad-179b35686ed3.jpg)

6) If player defeats two enemies, it wins the game
![Зображення 11 03 23 о 11 06](https://user-images.githubusercontent.com/116552240/224475596-78667f4c-a7bb-4eab-a5a2-41ce6ace84b0.jpg)
