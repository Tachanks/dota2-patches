"""Core (pos 1-3) tier boards for patch 7.42, updated with 7.42 data.

Each hero: (name, trend, base line, reason). Trend is relative to the Nov 18 day-one list:
up, down, steady, or new (added this update). A reason of None keeps the text already on the page.
Numbers: Dota2ProTracker meta, 7000+ MMR, patch 7.42 only (Nov 18-23, 2026).
"""

PICKS = [("Pos 1 first picks", "Riki, Sven, Phantom Assassin"),
         ("Pos 2 first picks", "Earthshaker, Primal Beast, Riki"),
         ("Pos 3 first picks", "Beastmaster, Lycan, Abaddon")]

CALLOUT_LABEL = "What changed since day one:"
CALLOUT = ("The biggest misses upward were Phantom Assassin, Riki and Earthshaker at mid. The biggest misses downward were "
           "Chaos Knight, Juggernaut, Anti-Mage, Invoker and Outworld Destroyer. Reworks went both ways. Lycan, Beastmaster and "
           "Abaddon are now the top offlaners, while Juggernaut, Death Prophet and Pugna are losing badly.")

POS1 = {
    "S": [
        ("Riki", "up", "7.42: 55.0% WR, 2,507 games · rated 75",
         "The best carry win rate with a real sample. Backstab's new Item Potency bonus makes his on-hit items hit harder from behind, and he wins 54.7% at mid too."),
        ("Sven", "steady", "7.42: 53.4% WR, 4,691 games · rated 72",
         "Right where the day-one list put him. He was barely changed in 7.42 and is still one of the most reliable carries."),
        ("Phantom Assassin", "up", "7.42: 53.2% WR, 5,984 games · rated 71",
         "The biggest miss on the day-one list. She's the most-picked carry and wins over 53%, so the Blur rework outweighed the evasion nerfs. Her most-played build wins 54.3%."),
    ],
    "A": [
        ("Phantom Lancer", "down", "7.42: 50.9% WR, 4,089 games · rated 75",
         "Still picked and banned constantly, but he only wins about 51%. Strong, just short of the top pick I called him."),
        ("Spectre", "steady", "7.42: 55.2% WR, 958 games · rated 57",
         "Wins as often as Riki on a smaller sample. Haunt illusions now carry 40% Item Potency, and the Radiance into Manta and Skadi build wins 57.4%."),
        ("Monkey King", "up", "7.42: 53.1% WR, 1,556 games · rated 53",
         "Boundless Strike's lower cooldown and longer stun paid off. He wins 56.1% at mid as well."),
        ("Wraith King", "up", "7.42: 54.1% WR, 849 games",
         "More skeletons early and a longer Wraithfire stun made him a strong, simple carry again."),
        ("Troll Warlord", "up", "7.42: 54.0% WR, 956 games",
         "Cheaper Sange and Yasha and the Battle Trance change are working. Most players go Battle Fury first."),
    ],
    "B": [
        ("Slark", "down", "7.42: 49.8% WR, 2,858 games",
         "Average this patch. The base damage cut and the Pounce change seem to matter more than the BKB-piercing items."),
        ("Lycan", "new", "7.42: 53.4% WR, 599 games",
         "His Pack Hunter rework works from every core role. He's an S tier offlaner and solid as a carry."),
        ("Muerta", "new", "7.42: 54.3% WR, 440 games",
         "New to the list. Gunslinger procs more often and her minimum base damage went up. Good carry on a smaller sample."),
        ("Broodmother", "new", "7.42: 56.4% WR, 415 games",
         "New to the list. Spider's Milk heals more and spiderlings hit harder per attack. Small sample."),
        ("Dragon Knight", "steady", "7.42: 53.2% WR, 449 games",
         "Better than his talent nerfs suggested, on a small carry sample."),
        ("Kez", "up", "7.42: 50.1% WR, 1,102 games",
         "The Raptor Dance rework brought him back to average."),
        ("Faceless Void", "steady", "7.42: 50.1% WR, 647 games",
         "Average. The Time Dilation buffs kept him playable without making him strong."),
    ],
    "C": [
        ("Anti-Mage", "down", "7.42: 47.9% WR, 3,255 games",
         "Slower jungle gold hurts a hero who needs a long farm, and it shows."),
        ("Luna", "down", "7.42: 48.3% WR, 3,343 games",
         "The agility gain cut outweighed the new on-hit glaive bounces."),
        ("Chaos Knight", "down", "7.42: 48.6% WR, 1,467 games",
         "The biggest miss in the other direction. The rework reads well on paper, but he's losing as carry and even more at offlane (42.0%)."),
        ("Lifestealer", "down", "7.42: 48.8% WR, 2,095 games",
         "The Infest nerfs show."),
        ("Ursa", "down", "7.42: 47.6% WR, 1,199 games",
         "Doing worse than his Earthshock buff suggested."),
        ("Terrorblade", "steady", "7.42: 49.8% WR, 1,443 games",
         "Close to average, which is an improvement on 7.41f."),
        ("Morphling", "down", "7.42: 47.9% WR, 1,607 games",
         "The new Scepter hasn't lifted him."),
        ("Naga Siren", "down", "7.42: 47.2% WR, 578 games",
         "Illusion on-hit items haven't been enough for her yet."),
        ("Lone Druid", "down", "7.42: 44.1% WR, 177 games",
         "Small sample, but a bad start for the rework."),
    ],
    "X": [
        ("Juggernaut", "down", "7.42: 43.6% WR, 3,073 games · rated 18",
         "The Blade Fury rework hurt him badly. Losing Swiftslash and the strong dispel shows."),
        ("Drow Ranger", "down", "7.42: 43.5% WR, 1,149 games",
         "Her buffs weren't close to enough."),
        ("Gyrocopter", "down", "7.42: 34.0% WR, 677 games",
         "The worst carry in the game this week."),
        ("Medusa", "down", "7.42: 45.3% WR, 428 games",
         "The Gorgon's Grasp rework hasn't helped."),
        ("Templar Assassin", "steady", "7.42: 46.0% WR, 561 games",
         "Still weak."),
        ("Shadow Fiend", "steady", "7.42: 38.5% WR, 117 games",
         "Still losing in every role he's played."),
    ],
}

POS2 = {
    "S": [
        ("Earthshaker", "new", "7.42: 54.0% WR, 3,851 games · rated 86 (top mid)",
         "The biggest surprise of the patch. Mid Earthshaker wins 54% over almost 4,000 games. Echo Slam's lower cooldown and the 50% Scepter totem cleave look like the reason."),
        ("Primal Beast", "up", "7.42: 57.5% WR, 1,082 games · rated 71",
         "The highest mid win rate with a real sample. Rock Throw now scales with strength, and he's strong at offlane too (53.9%)."),
    ],
    "A": [
        ("Riki", "new", "7.42: 54.7% WR, 1,853 games · rated 76",
         "Strong at mid as well as carry."),
        ("Sand King", "new", "7.42: 54.6% WR, 2,466 games · rated 72",
         "New to the list. Burrowstrike now has the Scepter upgrade, and Stinger hits harder with 60% Item Potency."),
        ("Meepo", "steady", "7.42: 57.8% WR, 618 games",
         "The XP rework is working. Small sample, very high win rate."),
        ("Monkey King", "new", "7.42: 56.1% WR, 1,140 games",
         "He wins even more at mid than as a carry."),
        ("Marci", "new", "7.42: 56.2% WR, 760 games",
         "New to the list. Better base agility and a bigger Bodyguard barrier made her a strong mid."),
        ("Puck", "steady", "7.42: 52.1% WR, 1,558 games",
         "Solid, as the day-one list expected."),
    ],
    "B": [
        ("Storm Spirit", "steady", "7.42: 51.1% WR, 2,094 games", "Above average after his small buffs."),
        ("Keeper of the Light", "steady", "7.42: 52.2% WR, 672 games", "Fine despite his nerfs."),
        ("Lycan", "steady", "7.42: 53.7% WR, 503 games", "Good at mid and better at offlane."),
        ("Tinker", "up", "7.42: 50.6% WR, 917 games", "Better than the Laser nerf suggested."),
        ("Arc Warden", "steady", "7.42: 50.3% WR, 903 games", "Average."),
        ("Queen of Pain", "up", "7.42: 50.0% WR, 2,427 games", "Average, which is a step up from 7.41f."),
        ("Leshrac", "down", "7.42: 50.0% WR, 1,090 games",
         "The Nihilism rework is fine, but it hasn't been the anti-carry tool I expected. He wins 65% as a carry in a tiny sample."),
    ],
    "C": [
        ("Invoker", "down", "7.42: 48.9% WR, 4,000 games",
         "Still the most-picked mid, but the Sun Strike and Chaos Meteor nerfs dragged him below 50%."),
        ("Dragon Knight", "down", "7.42: 49.4% WR, 1,193 games", "The talent nerfs hurt more at mid than at carry."),
        ("Ember Spirit", "down", "7.42: 48.3% WR, 1,579 games", "The Sleight of Fist potency cut shows."),
        ("Void Spirit", "down", "7.42: 49.1% WR, 2,283 games", "Slightly below average despite his buffs."),
        ("Tiny", "down", "7.42: 48.1% WR, 588 games", "His buffs weren't enough."),
        ("Zeus", "steady", "7.42: 48.7% WR, 392 games", "Still below average."),
    ],
    "X": [
        ("Outworld Destroyer", "down", "7.42: 46.1% WR, 1,637 games",
         "The Arcane Orb and Sanity's Eclipse nerfs hit harder than I expected. Skip him for now."),
        ("Death Prophet", "down", "7.42: 42.8% WR, 1,571 games", "The Witchcraft rework is losing badly at mid."),
        ("Lina", "down", "7.42: 43.9% WR, 592 games", "The Laguna Blade nerf shows."),
        ("Pugna", "down", "7.42: 44.9% WR, 332 games", "The rework is losing in every role so far."),
        ("Shadow Fiend", "steady", "7.42: 45.5% WR, 955 games", "Still weak."),
        ("Sniper", "steady", "7.42: 47.4% WR, 837 games", "Still below average."),
    ],
}

POS3 = {
    "S": [
        ("Beastmaster", "up", "7.42: 53.5% WR, 3,872 games · rated 100 (top offlaner)",
         "The new Thunderhide Scepter made him the best offlaner of the patch."),
        ("Lycan", "up", "7.42: 53.7% WR, 3,336 games · rated 91",
         "Pack Hunter turned him into a top offlaner."),
        ("Abaddon", "up", "7.42: 53.2% WR, 3,396 games · rated 82",
         "The Mist Coil Scepter rework is a big success at offlane, and he wins at pos 5 too."),
    ],
    "A": [
        ("Primal Beast", "up", "7.42: 53.9% WR, 1,721 games", "Strong in both of his roles."),
        ("Dark Seer", "down", "7.42: 52.7% WR, 1,295 games", "Good, but a step below the S tier I gave him."),
        ("Magnus", "up", "7.42: 52.5% WR, 1,892 games", "The early Shockwave buff helped his lane."),
        ("Night Stalker", "down", "7.42: 51.0% WR, 2,527 games", "Above average, short of the top."),
        ("Visage", "steady", "7.42: 53.0% WR, 674 games", "Still strong on a smaller sample."),
    ],
    "B": [
        ("Omniknight", "new", "7.42: 53.1% WR, 875 games",
         "New to the list. Hammer of Purity's new healing works from the offlane too."),
        ("Enigma", "down", "7.42: 51.7% WR, 873 games",
         "Still above 50%, but far below his 59.5% in 7.41f, and he's picked much less."),
        ("Dawnbreaker", "steady", "7.42: 51.1% WR, 1,956 games", "Slightly above average."),
        ("Brewmaster", "down", "7.42: 51.0% WR, 878 games", "Fine, nothing special."),
        ("Sand King", "new", "7.42: 50.2% WR, 1,992 games", "Average at offlane and strong at mid."),
        ("Legion Commander", "down", "7.42: 49.8% WR, 1,875 games", "Average after the strength gain nerf."),
    ],
    "C": [
        ("Axe", "down", "7.42: 46.9% WR, 2,271 games", "The Battle Hunger nerf shows."),
        ("Doom", "down", "7.42: 46.5% WR, 1,524 games", "Doing much worse than his small nerfs suggested."),
        ("Dragon Knight", "down", "7.42: 48.8% WR, 1,278 games", "Below average in every core role except carry."),
        ("Pudge", "down", "7.42: 49.7% WR, 1,261 games", "Close to average."),
        ("Mars", "down", "7.42: 48.4% WR, 1,903 games", "His buffs didn't help."),
        ("Tidehunter", "steady", "7.42: 48.7% WR, 1,352 games", "Below average."),
        ("Timbersaw", "steady", "7.42: 49.3% WR, 1,214 games", "Below average."),
        ("Slardar", "steady", "7.42: 48.0% WR, 685 games", "Below average."),
        ("Underlord", "steady", "7.42: 47.5% WR, 438 games", "Below average."),
    ],
    "X": [
        ("Chaos Knight", "down", "7.42: 42.0% WR, 922 games", "The worst common offlaner this week."),
        ("Bristleback", "down", "7.42: 41.2% WR, 835 games", "His buffs haven't helped at all."),
        ("Centaur Warrunner", "down", "7.42: 43.0% WR, 337 games", "The Stampede and Horsepower nerfs hurt."),
    ],
}

KICKER = "Patch 7.42 · Core roles · Updated with 7.42 data"
LEDE = ("A guide to 7.42 for a position 1 player who flexes mid and offlane. The tiers now use five days of real 7.42 games at 7000+ MMR "
        "from Dota2ProTracker, Nov 18 to 23. The arrows show how each hero moved since the day-one list, which was based on 7.41f stats and the patch notes.")
CHIPS = ["7.42 released Nov 18, 2026", "7.42 data: Dota2ProTracker, 7000+ MMR, Nov 18–23", "Updated Nov 23, 2026", "Focus: carry, mid, offlane"]
SUBS = {
    "carry": "Your main role, so this list is the deepest. Numbers are carry-role results from 7.42 at 7000+ MMR, with D2PT's 0–100 rating where it gave one. Builds for these heroes are in the next section.",
    "mid": "Mid changed the most from the day-one list. Earthshaker and Primal Beast lead, while Invoker and Outworld Destroyer fell below 50%. Numbers are mid-role results from 7.42.",
    "off": "Three reworked heroes, Beastmaster, Lycan and Abaddon, now lead the offlane. Numbers are offlane-role results from 7.42.",
}
BUILDS_SUB = ("One recommended and one alternative build for every S and A tier carry, plus the lower-tier carries that had a build last week. "
              "Items are in buy order after your laning items. Where a build matches the most-played 7.42 build on Dota2ProTracker, the note says so and gives its win rate. "
              "Juggernaut's build is gone because I'd skip him right now.")
METHOD = ("Tier numbers come from Dota2ProTracker's meta page at 7000+ MMR, filtered to patch 7.42 (Nov 18 to 23, 2026) and read on November 23. "
          "The day-one version of this page used the last 8 days of 7.41f instead. Builds marked as most-played come from each hero's D2PT page for 7.42. "
          "High-MMR results can differ from lower brackets, and samples under about 500 games are flagged on each card.")
