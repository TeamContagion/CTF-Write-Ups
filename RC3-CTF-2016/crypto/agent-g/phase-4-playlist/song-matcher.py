message = "Secret Key Num Nickel year front side greggernaut com one cipher plox"
message = message.replace(" ", "").upper()
key = "0096 2251 2110 8105".replace(" ", "")
key = (key * (len(message) // len(key) + 1))[:len(message)]


songs = {
    "Safe and Sound / Capital Cities": "I could lift you up ",
    "Houdini / Foster the People": "Rise above gonna start a war",
    "Heathens / Twenty One Pilots": "All my f_iends are heathens", #R
    "Cometas por el cielo / La Oreja de Van Gogh": "Quédate esta fría madrugada",
    "Lazuli / Beach House": "In the blue, of this life",
    "My Type / Saint Motel": "Take a look around the room",
    "Elephant Parade / Reliant K": "H_phip _ooray for the elephants on parade)", # Hiphip hooray for the elephants on parade)
    "Forever / Youngblood Hawke": "You say you won't wait forever on me",
    "Spaceman / The Killers": "The star maker says",
    "Bows & Arrows / Kaiser Chiefs": "Hold onto your hearts, if you can",
    "Lions on the Astroturf / Zibra Zibra": "Burn Burn your bedsheets on bombshells",
    "Different Trains / Reverend and the Makers": "I invented penicillin",
    "When he died / Lemon Demon": "When he died Turns out",
    "Shut up and Dance / Walk the Moon": "Oh don't you dare look back",
    "Bulletproof / La Roux": "Been there, done that, messed around",
    "Shark Attack / Grouplove": "Yeah, I left my body in a sea",
    "Lets Dance to Joy Division / The Wombats": "Let's dance to joy division",
    "Fall into these arms / New Politics": "Fall into these arms",
    "Colours / Grouplove": "It's the colors you have",
    "Believe / The Bravery": "The faces all around me they",
    "Apart / Elkland": "You and I will never be apart, apart",
    "Take me Out / Franz Ferdinand": "So if you're lonely",
    "Rifles Spiral / The Shins": "Dead lungs command it",
    "Middle of Nowhere / Hot Hot Heat": "Don't get mad if I'm laughing",
    "Ize of the World / The Strokes": "I think I know what you",
    "It makes my heart break / Birds of paradise": "Been livin' on a cloud",
    "Everybody Hurts": "When your day is long",
    "Bust your kneecaps": "Johnny don't leave me",
    "The Song that Goes Like This lyrics / Spamalot Cast": "Once in every show",
    "_xs and Ohs / Elle King": "_x's and the oh, oh, oh's they haunt me",
    "The last goodbye / Billy Boyd": "I saw the light fade from the sky",
    "Daylight / Matt and Kim": "And in the daylight we can hitchhike",
    "The device has been modified": "Hello,Hello, and welcome to the enrichment",
    "Mary Jane / Jürgen Peter": "Ich träum von dir, wenn du nicht bei mir bist",
    "Hooked on a feeling / Blue Suede": "I'm hooked on a feeling",
    "Welcome to your wedding day": "And you know its begun from ",
    "Let it Rain / Living Things": "Babe Why are you still inside",
    "Pumpin Blood / NONONO": "Hey heart on the road again",
    "The kind and all of his men / Wolf Gang": "You took her soul, so incomplete",
    "Alone at Home / Jonathan Coulton": "I am glad to be shopping here with you",
    "Hero / Family of the Year": "Let me go I don't wanna be your hero",
    "Is This It / The Strokes": "Can't you see I'm trying",
    "Plastic Soldiers / Portugal. The Man": "Could it be we got lost in the summer",
    "Clouds / Zach Sobiach": "And we'll go up, up, up",
    "Cosmic Love / Florence + the Machine": "A falling star fell from your heart and landed in my eyes",
    "The Boxer / Simon and Garfunkle": "I am just a poor boy",
    "Boston / Augustana": "In the light of the sun",
    "Birdhouse in your soul / They Might Be Giants": "I'm your only friend I'm not your only friend",
    "Dust in the Wind / Kansas": "I close my e_es only for a moment, and the moment's gone", #Y
    "Rules Don't Stop / The Scientists": "Rules don't stop me forget about it",
    "Showbiz / Muse": "Controlling my feelings for too long",
    "Thoughts Of A Dying Atheist / Muse": "Eerie whispers",
    "Taco Bell / Apollo XVIII": "I'm bangin___",
    "Ten Little Indians lyrics / Bloody Bloody Andrew Jackson Cast ": "Ten little indians standing in a line",
    "At the End of the Day / Anne Hathaway, Hugh Jackman": "At the end of the day you're another day older",
    "In the Garage / Weezer": "I've got Dungeon Master's Guide",
    "Back in Time / Keane": "I've got time to kill I'm not living",
    "Tongue Tied / Grouplove": "Take me to your best friend's house",
    "Your Vegas / Your Vegas": "Watch her run, watch her run",
    "Millionaire / White Lies": "We wait for the fear to come alive",
    "Octopus's Garden / The Beatles": "I'd like to be under the sea",
    "I Believe / Nico Vega": "I was standing in the corner",
    "Mr. Synthetic / ZibraZibra": "I'm mister synthetic",
    "Mayday / People in Planes": "There's another way",
    "Move / Saint Motel": "Move / This man, this dutiful man has got this sense of devotion",
    "Brand New Day / Ryan Star": "I stayed in one place for too long",
    "Sound of Madness / Shinedown": "Yeah, I get it You're an outcast",
    "Rosas / La Oreja de Van Gogh": "En un día de estos en que suelo pensar",
    "Wisdom / Gran Ronde": " I wanna get by Just",
    "Electro Gypsy / Savlonic": "There he is - the Electro Gypsy",
    "Anyone's Ghost / The National": "Say you stayed at home",
    "All in Wait / Static-X": "Drowning myself, over and over",
    "Am I Awake / They Might Be Giants": "Am I awake? What time is it?",
    "99 Red Balloons / Goldfinger": "You and I in a little toy shop",
    "Take it all away / Red": "You've stripped me down",
    "Mutiny / Pendulum": "In through rays of your reflection",
    "No / They Might Be Giants": "No is no No is always no",
    "In Your Head / Rooney": "I told you before",
    "All That Shit is Gone / Carolina Liar": "I never got it right",
    "Hatefuck / The Bravery": "If I put my hands around your wrists",
    "People Say / Portugal. The Man": "Save me, I can't be saved",
    "Dancing With The Devil / WolfGang": "If you're the chosen one",
    "Good Days Bad Days / Kaiser Chiefs": "Follow the underdog",
    "Sweater Weather / The Neighbourhood": "All I am is a man",
    "A Place to Hide / White Lies": "Could I sit alone and ask about my future?",
    "Smashing the Opponent / Infected Mushroom": "Smack me again",
    "Punching In A Dream / The Naked and Famous": "All the lights go down as I crawl into the spaces",
    "56k  / Ronald Jenkees": "Top of the ’93, I woke up, drove to the store",
    "Satin in a Coffin / Modest Mouse": "You were laying on the carpet",
    "Henrietta / The Fratellis": "Henrietta, we got no flowers for you",
    "Creepin' Up the Backstairs / The Fratellis": "She said Im Rosie",
    "On Top Of The World / Imagine Dragons": "If you love somebody",
    "Our Mouths Were Wet / Oh No! Oh My!": "I paint the fields that your mouth sent",
    "Never Miss A Beat Lyrics / Kaiser Chiefs": "What did you learn today",
    "Keelhauled / Alestorm": "My friends I stand before you",
    "Elektronik Supersonik / Zlad!": "Hey, baby, wake up from your asleep",
    "No One Knows / Queens of the Stone Age": "We get some rules to follow",
    "The Fake Sound of Progress / Lostprophets": "Somebody told me that I'd always have to bow",
    "Miss it so much / Röyksopp": "I miss it so much",
    "Suego Faults / Wolg Gang": "You went so long to find, to find you",
    "Empire / OF MONSTERS AND MEN": "Feel the ocean as it breathes",
    "Taking A Bath In Rust / Eels": "Why don't you Get me",
    "O We / They Might By Giants": "O we o we o we O we o we o we ",
    "The Wanting Comes In Waves / The Decemberists": "Mother I can hear your foot-fall now",
    "Access Denied / Scaramouche": "Take it all, everything",
    "ET___________ / a": "asdfasdf",
    "E_____________ / b": "asdfasdf",
    "E______________ / c": "asdfasdf",
    "E_______________ / d": "asdfasdf",
}


for song in songs:
    songs[song] = song.replace(" ", "").replace(",", "").replace("'", "").upper().split('/')[0]
    l = len(songs[song])
    if l < 10:
        songs[song] += "_" * (10-l)


alpha = "abcdefghijklmnopqrstuvwxyz".upper()
diff = "01110225134233134100244444"

lookup = dict(zip(alpha, diff))

encoded = []
i = 0
for m, k in zip(message, key):
    encoded.append([m, k, i])
    i += 1
sorted_by_diff = sorted(encoded, key=lambda x: int(lookup[x[0].upper()]), reverse=True)
print(sorted_by_diff)

remaining = []
for l in sorted_by_diff:
    letter, index, ordering = l
    print(letter, index, end="\t")
    match = None
    for song, lyrics in songs.items():
        if song[int(index)].lower() == letter.lower():
            match = (letter, index, ordering, song)
            break

    if match:
        print(match)
        l.append(match)
        songs.pop(match[3])
    else:
        print("?")
        remaining += [(letter, index)]



sorted_by_message = sorted(encoded, key=lambda x: x[2])
print("Unused:")
for song in songs:
    print(song)


if remaining:
    print("fuck")
    for word, index in remaining:
        print(word, index)
else:
    for letter, index, ord, song in sorted_by_message:
        print("%s (%s) %-10s (%s)" % (letter, index, song.replace(" ", "").replace(",", "").replace("'", "").upper().split('/')[0][:10], song))
