print('''                     
                     _                    _
                  ,/                        \,
        _________{(                          })_________
       /.-------./\\                        //\.-------.
       //@@@@@@@//@@\\  )                (  //@@\\@@@@@@@\\
     //@@@@@@@//@@@@>>/                  \<<@@@@\\@@@@@@@\\
    //O@O@O@O//@O@O//                      \\O@O@\\O@O@O@O\\
  //OOOOOOOO//OOOO||          \  /          ||OOOO\\OOOOOOOO\\
 //O%O%O%O%//O%O%O%\\         ))((         //%O%O%O\\%O%O%O%O\\
||%%%%%%%%//'  `%%%%\\       //  \\       //%%%%'   `\\%%%%%%%||
((%%%%%%%((      %%%%%\\    ((    ))    //%%%%%       ))%%%%%%))
 \:::' `::\\      `:::::\\   \)~~(/    //:::::'      //::' `:::/
  )'     `;)'      (`  ` \\ `<@  @>' / / '  ')      `(;'     `(
          (               \`\ )^^( /  /               )
        _                  ) \\oo/   (
       (@)                  \  `'   /                      _
       |-|\__________________\__^__<________oOo__________ (@)
       | |                                  VVV          \|-|
       |-|                                                |-|
       |_|\_____________________________________________  | |
       (@)                 / ,/ \_____/ \\ ~\/~         `\|-|
        ~             ___//^~      \____/\\               (@)
                     <<<  \     __  <____/||               ~
                               <   \ <___/||
                                  || <___//
                                  \ \/__//
                                   ~----~''')

print("Welcome to Dragon Island.")
print("Your mission is to survive without waking the sleeping dragons while finding a way to escape.")
print("You\'ve just arrived on the island. Choose your path wisely.\nOptions: Forest, Cave")
choice1 = input("Enter your choice: ").lower()

if choice1 == "forest":
    print("You venture into the Forest and spot a bear calmly eating a fish. It locks eyes with you.\nOptions: Stay still, Run away")
    choice2 = input("What will you do: ").lower()

    if choice2 == "stay still":
        print("You remain still, holding the bear's gaze. Sensing no threat, it eventually wanders off.")
        print("Deeper into the forest, you encounter four portals, each glowing a different color: Red, Blue, Yellow, Green.")
        choice3 = input("Which portal will you enter: ").lower()

        if choice3 == "yellow":
            print("You step into the yellow portal and find yourself transported to a human settlement.\nCongratulations, you have won!")
            print('''             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
          GG  `"""""""`''')
        elif choice3 == "green":
            print("You enter the green portal and are plunged into the deep sea. You drown!\nGAME OVER!")
        elif choice3 == "blue":
            print("You step into the blue portal, but before you can react, a dragon incinerates you with its flames.\nGAME OVER!")
        else:
            print("You step into the red portal and are crushed under the feet of an enraged dragon.\nGAME OVER!")
    else:
        print("You attempt to run, but the bear quickly overtakes and kills you brutally.")
        print('''               _
              (\\  _                      ___
             .-"`"(\\                _.""`   `"-.
            /      ` `-._        _.-"            `\__
           6   6)        `-.__.-'                    `",
          /                                         `;-`
         /     ,                                     |
        ()    /  /`                                  |
         `---`"~``\                                  |
                   \                                 |
                    \            \      /           /
                    /`,   ,      |     |           /
                   /   "-.|      |     |         /'
                  /     / |     /,__   |       /`\ ''')
else:
    print("You enter the Cave.\nThe temperature rises as you notice two eyes glaring at you. You try to flee, but it's too late...\nThe dragon's fiery breath engulfs you, the heat overwhelming your senses as your vision fades and the world burns to ash.\nGAME OVER!")
    print('''
 \----------/(           ___              ###########
   \``````/ |,,\        / @.\_       ###################
     \``/,,,|,,,,\   _ / /____%>**@@#### YOU'RE TOAST! ####
      \`____|,,,,,\/...//          ###################
              ~\, .... /             ##############
              /....____

''')
