"""Pos 1 build data for the 7.42 tier list. One recommended and one alternative build per hero."""

BUILDS = [
    {
        "hero": "Chaos Knight", "tier": "S",
        "start": "Tango, Quelling Blade, Gauntlets of Strength, Iron Branches",
        "rec": {
            "name": "Phantasm on-hit",
            "items": ["Phase Boots", "Armlet of Mordiggian", "Desolator", "Skull Basher", "Black King Bar", "Abyssal Blade", "Sabatons of Mordiggian"],
            "note": "Phantasms now have 100% Item Potency, so every illusion applies Desolator and rolls Basher at full strength. Start with Phase instead of Treads because Phase plus Armlet becomes Sabatons later, and take the Shard from the second Tormentor since the Chaos Bolt illusion now deals full damage.",
        },
        "alt": {
            "name": "Blink initiator",
            "items": ["Power Treads", "Armlet of Mordiggian", "Blink Dagger", "Aghanim's Shard", "Black King Bar", "Assault Cuirass", "Overwhelming Blink"],
            "note": "Use this when your team needs you to start fights. Ahead, Armageddon only works while a Phantasm is alive, so Blink is your way in before ult is up, and Assault's armor aura covers your illusions too.",
        },
    },
    {
        "hero": "Phantom Lancer", "tier": "S",
        "start": "Tango, Quelling Blade, 2 Slippers of Agility (they build into Corrosion)",
        "rec": {
            "name": "Tank and burn",
            "items": ["Orb of Corrosion", "Power Treads", "Diffusal Blade", "Manta Style", "Heart of Tarrasque", "Eye of Skadi", "Disperser"],
            "note": "Diffusal's mana burn now works on every illusion hit, which is the main reason PL gets better this patch. Heart keeps you and your illusions alive against AoE, and Skadi adds a slow and heal cut that goes through BKB.",
        },
        "alt": {
            "name": "Damage race",
            "items": ["Orb of Corrosion", "Power Treads", "Diffusal Blade", "Manta Style", "Butterfly", "Abyssal Blade", "Eye of Skadi"],
            "note": "Go this way against physical lineups or when you're already ahead. Butterfly is 450g cheaper now and Abyssal adds +15 agility and +25 melee range.",
        },
    },
    {
        "hero": "Sven", "tier": "S",
        "start": "Tango, Quelling Blade, Gauntlets of Strength, Iron Branches",
        "rec": {
            "name": "Cleave carry",
            "items": ["Power Treads", "Mask of Madness", "Echo Sabre", "Black King Bar", "Daedalus", "Satanic", "Aghanim's Scepter"],
            "note": "Mask of Madness is 100g cheaper and now gives attack speed. Scepter's Storm Hammer range bonus went from +25% to +30%.",
        },
        "alt": {
            "name": "Harpoon pick-off",
            "items": ["Phase Boots", "Echo Sabre", "Blink Dagger", "Black King Bar", "Harpoon", "Daedalus", "Swift Blink"],
            "note": "Harpoon now builds from Echo Sabre and Dragon Lance and gives +30 strength, +15 agility and +25 melee range. Pick this when the enemy carry kites or blinks away from you.",
        },
    },
    {
        "hero": "Spectre", "tier": "A",
        "start": "Tango, Quelling Blade, Circlet, Iron Branches",
        "rec": {
            "name": "Radiance",
            "items": ["Power Treads", "Radiance", "Manta Style", "Eye of Skadi", "Heart of Tarrasque", "Butterfly"],
            "note": "The classic farm route. Haunt illusions now have 40% Item Potency, so Skadi's slow and heal cut land even while you're on the other side of the map.",
        },
        "alt": {
            "name": "Diffusal tempo",
            "items": ["Orb of Corrosion", "Power Treads", "Diffusal Blade", "Manta Style", "Eye of Skadi", "Heart of Tarrasque"],
            "note": "This fights earlier than Radiance. Use it against mana-hungry heroes or when your team needs Haunt at 20 minutes instead of 30.",
        },
    },
    {
        "hero": "Ursa", "tier": "A",
        "start": "Tango, Quelling Blade, Iron Branches, Magic Stick",
        "rec": {
            "name": "Blink and bash",
            "items": ["Phase Boots", "Morbid Mask", "Blink Dagger", "Skull Basher", "Black King Bar", "Abyssal Blade", "Satanic"],
            "note": "Abyssal now needs Dragon Lance, which adds +15 agility and +25 melee range. It lost its slow resistance, so get BKB before Abyssal against heavy disables. Morbid Mask turns into Satanic at the end.",
        },
        "alt": {
            "name": "Kite-proof",
            "items": ["Phase Boots", "Blink Dagger", "Diffusal Blade", "Black King Bar", "Eye of Skadi", "Abyssal Blade", "Satanic"],
            "note": "Pick this against heroes who kite or blink out. Skadi now pierces BKB, so the slow stays on their carry while you finish the swipes.",
        },
    },
    {
        "hero": "Slark", "tier": "A",
        "start": "Tango, Quelling Blade, 2 Slippers of Agility",
        "rec": {
            "name": "Silver Edge",
            "items": ["Orb of Corrosion", "Power Treads", "Diffusal Blade", "Silver Edge", "Abyssal Blade", "Eye of Skadi", "Butterfly"],
            "note": "Corrosion and Skadi both pierce BKB now, which makes Essence Shift fights against BKB carries easier. Silver Edge's break is extra useful because a lot more innates can be broken in 7.42.",
        },
        "alt": {
            "name": "Basher into BKB",
            "items": ["Power Treads", "Skull Basher", "Black King Bar", "Abyssal Blade", "Eye of Skadi", "Satanic"],
            "note": "Use this against lineups with a lot of stuns and silences, where you need BKB before you can afford Silver Edge.",
        },
    },
    {
        "hero": "Luna", "tier": "A",
        "start": "Tango, Slippers of Agility, Circlet, Iron Branches",
        "rec": {
            "name": "Glaive Skadi",
            "items": ["Power Treads", "Mask of Madness", "Manta Style", "Eye of Skadi", "Black King Bar", "Butterfly", "Satanic"],
            "note": "Glaive bounces now carry on-hit effects with 40% less potency per bounce, so Skadi's slow spreads through a fight. Lifesteal still only works on your main target.",
        },
        "alt": {
            "name": "Range and save",
            "items": ["Power Treads", "Mask of Madness", "Dragon Lance", "Manta Style", "Black King Bar", "Hurricane Pike", "Satanic"],
            "note": "Go this way when the enemy has gap-closers like Slark, Ursa or PA. Pike's push can no longer be dispelled.",
        },
    },
    {
        "hero": "Anti-Mage", "tier": "A",
        "start": "Tango, Quelling Blade, Slippers of Agility, Iron Branch",
        "rec": {
            "name": "Battle Fury",
            "items": ["Power Treads", "Battle Fury", "Manta Style", "Skull Basher", "Abyssal Blade", "Butterfly", "Eye of Skadi"],
            "note": "The standard farm route. Manta illusions now carry your on-hit items at 35% and Abyssal adds +15 agility.",
        },
        "alt": {
            "name": "Manta first",
            "items": ["Power Treads", "Yasha", "Manta Style", "Skull Basher", "Abyssal Blade", "Butterfly", "Black King Bar"],
            "note": "Skip Battle Fury when the enemy can punish a slow farm with early aggression. Yasha is 100g cheaper now, and you're fighting by 15 minutes for the first Tormentor.",
        },
    },
    {
        "hero": "Faceless Void", "tier": "B",
        "start": "Tango, Quelling Blade, Slippers of Agility, Iron Branches",
        "rec": {
            "name": "Mjollnir",
            "items": ["Power Treads", "Mask of Madness", "Maelstrom", "Black King Bar", "Mjollnir", "Eye of Skadi", "Butterfly"],
            "note": "Pick up the Shard. Its Time Dilation attack speed swing went from 9-12 to 17-20, and Dilation itself now has a 15s cooldown at max level.",
        },
        "alt": {
            "name": "Burst",
            "items": ["Power Treads", "Mask of Madness", "Desolator", "Black King Bar", "Daedalus", "Satanic"],
            "note": "Use this in fight-heavy drafts where you want every Chronosphere to end in kills fast.",
        },
    },
    {
        "hero": "Naga Siren", "tier": "B",
        "start": "Tango, Quelling Blade, 2 Slippers of Agility",
        "rec": {
            "name": "Diffusal tank",
            "items": ["Orb of Corrosion", "Power Treads", "Diffusal Blade", "Heart of Tarrasque", "Butterfly", "Eye of Skadi", "Disperser"],
            "note": "Diffusal's burn now applies through illusion hits, and Rip Tide's armor shred starts at 3.5 instead of 2.",
        },
        "alt": {
            "name": "Split push",
            "items": ["Orb of Corrosion", "Power Treads", "Diffusal Blade", "Manta Style", "Skull Basher", "Abyssal Blade", "Butterfly"],
            "note": "More bodies for pushing three lanes. Manta illusions get 35% potency, higher than the 20% your Mirror Image illusions have.",
        },
    },
    {
        "hero": "Riki", "tier": "B",
        "start": "Tango, Slippers of Agility, Circlet, Iron Branches",
        "rec": {
            "name": "Diffusal bash",
            "items": ["Power Treads", "Diffusal Blade", "Skull Basher", "Black King Bar", "Abyssal Blade", "Eye of Skadi", "Disperser"],
            "note": "Backstab hits now get 10% extra Item Potency plus 10% more per 15 levels, so Diffusal burns more and Basher procs more often from behind.",
        },
        "alt": {
            "name": "Burst pick-off",
            "items": ["Power Treads", "Desolator", "Black King Bar", "Daedalus", "Abyssal Blade", "Butterfly"],
            "note": "Use this for picking off supports. Desolator's armor cut also scales with Backstab's extra potency.",
        },
    },
    {
        "hero": "Morphling", "tier": "B",
        "start": "Tango, Slippers of Agility, Circlet, Iron Branches",
        "rec": {
            "name": "Agility carry",
            "items": ["Power Treads", "Manta Style", "Linken's Sphere", "Eye of Skadi", "Butterfly", "Satanic"],
            "note": "Keep agility high for Adaptive Strike and Waveform. Manta illusions now bring your Skadi with them.",
        },
        "alt": {
            "name": "Scepter morph",
            "items": ["Power Treads", "Ethereal Blade", "Linken's Sphere", "Aghanim's Scepter", "Manta Style", "Butterfly"],
            "note": "Only when the enemy has strong unit-target spells to copy, like Lion, Lina, Doom or Bane. While morphed, each unit-target spell you cast gets recast on nearby enemies at 50% and then 25% strength.",
        },
    },
    {
        "hero": "Troll Warlord", "tier": "B",
        "start": "Tango, Quelling Blade, Circlet, Iron Branches",
        "rec": {
            "name": "S&Y bash",
            "items": ["Phase Boots", "Sange and Yasha", "Black King Bar", "Skull Basher", "Abyssal Blade", "Butterfly", "Satanic"],
            "note": "Sange and Yasha is 200g cheaper and now gives 20% health restoration. Abyssal's +25 range applies to your melee form.",
        },
        "alt": {
            "name": "Battle Fury",
            "items": ["Phase Boots", "Battle Fury", "Black King Bar", "Eye of Skadi", "Butterfly", "Satanic"],
            "note": "Faster farm when your lane is safe. Skadi now goes through BKB, so targets stay in reach of your melee form.",
        },
    },
    {
        "hero": "Juggernaut", "tier": "B",
        "start": "Tango, Quelling Blade, Slippers of Agility, Iron Branches",
        "rec": {
            "name": "Battle Fury",
            "items": ["Phase Boots", "Battle Fury", "Manta Style", "Skull Basher", "Abyssal Blade", "Butterfly", "Eye of Skadi"],
            "note": "The safe pick while the rework settles. Blade Fury now fully disarms you without Scepter, so use it for farming and escaping more than for fighting.",
        },
        "alt": {
            "name": "Spin Scepter",
            "items": ["Phase Boots", "Maelstrom", "Aghanim's Scepter", "Manta Style", "Mjollnir", "Eye of Skadi", "Butterfly"],
            "note": "Try this in unranked first. With Scepter you keep attacking while you spin and move, at 75% damage and Item Potency, so Maelstrom and Skadi still proc during Blade Fury.",
        },
    },
    {
        "hero": "Lifestealer", "tier": "B",
        "start": "Tango, Quelling Blade, Gauntlets of Strength, Iron Branches",
        "rec": {
            "name": "Desolator",
            "items": ["Phase Boots", "Armlet of Mordiggian", "Desolator", "Skull Basher", "Abyssal Blade", "Eye of Skadi", "Sabatons of Mordiggian"],
            "note": "Phase plus Armlet turns into Sabatons late. The Shard now adds Open Wounds to every Infest explosion, which is worth grabbing from the second Tormentor.",
        },
        "alt": {
            "name": "Radiance",
            "items": ["Phase Boots", "Armlet of Mordiggian", "Radiance", "Skull Basher", "Abyssal Blade", "Satanic"],
            "note": "Slower and tankier. Radiance speeds up your farm and keeps damage ticking on everyone near you in long fights.",
        },
    },
    {
        "hero": "Lone Druid", "tier": "B",
        "start": "Druid: Tango, Iron Branches. Bear: Quelling Blade",
        "rec": {
            "name": "Bear carry",
            "items": ["Phase Boots", "Mask of Madness", "Maelstrom", "Desolator", "Skull Basher", "Abyssal Blade", "Assault Cuirass"],
            "note": "These are Bear items. Get Aghanim's Scepter on the Druid by midgame: if he dies near the Bear, his spirit is stored and you resummon him at full health. The Bear's Scepter disarm range is no longer global.",
        },
        "alt": {
            "name": "Fast push",
            "items": ["Phase Boots", "Maelstrom", "Assault Cuirass", "Mjollnir", "Eye of Skadi", "Abyssal Blade"],
            "note": "Bear items again. Take the 15:00 Tormentor and use its mega creep horn to end before the enemy carry is ready.",
        },
    },
    {
        "hero": "Dragon Knight", "tier": "B",
        "start": "Tango, Gauntlets of Strength, Iron Branches",
        "rec": {
            "name": "Blink Desolator",
            "items": ["Power Treads", "Blink Dagger", "Desolator", "Black King Bar", "Aghanim's Scepter", "Assault Cuirass", "Satanic"],
            "note": "DK is better spent at mid or offlane this patch, but this build works from the safe lane.",
        },
        "alt": {
            "name": "Tank",
            "items": ["Power Treads", "Blink Dagger", "Aghanim's Scepter", "Assault Cuirass", "Heart of Tarrasque", "Satanic"],
            "note": "Go this way against physical lineups, when you need to soak damage and take towers more than you need kills.",
        },
    },
]
