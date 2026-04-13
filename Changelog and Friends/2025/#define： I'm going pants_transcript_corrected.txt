[0.00 → 21.14] Welcome to Changelog and friends, a weekly talk show about Sound.
[21.80 → 28.14] Thanks to our partners at fly.io, the public cloud built for developers who ship.
[28.14 → 34.68] We love to fly. You might too. Learn all about it at fly.io. Okay, let's play.
[42.76 → 47.90] Friends, I'm here with Terrence Lee talking about what's coming for the next generation of Heroku.
[48.20 → 53.50] They're calling this next gen fur. Terrence, one of the biggest moves for fur in this next generation of Heroku,
[53.50 → 58.80] it's being built on open standards and cloud native. What can you share about this journey?
[59.04 → 63.68] If you look at the last half a decade or so, like there's been a lot that's changed in the industry.
[63.92 → 67.72] A lot of the 12 factor isms that have been popularized and are well accepted,
[67.98 → 74.58] even outside the Ruby community, are things that are thought table stakes for building modern applications, right?
[74.66 → 79.32] And so being able to take all those things from kind of 10, 14 years ago,
[79.32 → 83.16] being able to revisit and be like, okay, we helped popularize a lot of these things.
[83.38 → 85.72] We now don't need to be our own island of this stuff.
[85.84 → 88.26] And it's just better to be part of the broader ecosystem.
[88.64 → 92.68] Like you said, since Heroku's existence, there's been people who've been trying to rebuild Heroku.
[92.84 → 96.38] I feel like there's a good Kelsey quote, where are we going to stop trying to rebuild Heroku?
[96.72 → 100.02] It's like people keep trying to like to build their own version of Heroku,
[100.26 → 103.22] like internally at their own company, let alone the public offerings out there.
[103.22 → 106.60] I mean, I feel like Heroku has been the gold standard.
[106.60 → 112.72] Yeah, I mean, I think it's the gold standard because there's a thing that like Heroku's hit,
[112.82 → 115.84] this like piece of magic around developer experience,
[115.84 → 118.58] but giving you enough flexibility and power to do what you need to do.
[118.78 → 124.56] Okay, so part of Fur and this next generation of Heroku is adding support for .NET.
[124.82 → 126.06] What can you share about that?
[126.16 → 128.02] Why .NET and why now?
[128.30 → 131.62] I think if you look at .NET over the last decade, it's changed a lot.
[131.86 → 134.46] .NET is known for being this Windows only platform.
[134.46 → 138.76] You have Informs, use it to build Windows stuff, double IS.
[139.38 → 142.48] And it's moved well beyond that over the last decade.
[142.70 → 145.32] You can build .NET on Linux, on Mac.
[145.48 → 148.68] There's this whole cross-platform open source ecosystem,
[148.96 → 152.10] and it's become this juggernaut of an ecosystem around it.
[152.14 → 156.36] And we've gotten this ask to support .NET for a long time, and it isn't a new ask.
[156.68 → 158.68] And regardless of our support of it,
[158.76 → 162.18] like people have been running .NET on Heroku in production today.
[162.18 → 166.32] There's been a mono build pack since the early days when you couldn't run .NET on Linux,
[166.32 → 168.88] and now with .NET Core, the fact that it's cross-platform,
[168.88 → 172.86] this .NET Core build pack that people are using to run their apps on Heroku.
[173.04 → 176.62] The kind of shift now is to take it from that to a first-class citizen.
[176.62 → 179.66] And so what that means for Heroku is we have this languages team.
[179.66 → 184.74] We're now staffing someone to basically live, breathe, and eat being a .NET person, right?
[184.80 → 190.52] Someone from the community that we plucked to be this person to provide that day zero support
[190.52 → 192.08] for the language and runtimes that you expect,
[192.24 → 194.22] and like we have for all of our languages, right?
[194.50 → 199.26] To answer your support and deal with all those things when you open support tickets on Heroku,
[199.64 → 205.18] and kind of all the documentation that you expect for having quality language support in the platform.
[205.18 → 210.98] In addition to that, one of the things that it means to be first class is that when we are building out new features and things,
[211.24 → 217.54] it is now one of the languages as part of this ecosystem that we're going to test and make sure runs smoothly, right?
[217.58 → 219.32] So you can get this kind of end-to-end experience.
[219.80 → 220.82] You can go to Deventer.
[221.18 → 223.98] There's a .NET icon to find all the .NET documentation.
[224.56 → 228.90] Take your app, create a new Heroku app, run Git Push Heroku Main, and you're off to the races.
[228.90 → 233.18] So with the coming release of Fur and this next generation of Heroku,
[233.74 → 243.78] .NET is officially a first class language on the platform, dedicated support, dedicated documentation, all the things.
[244.06 → 250.96] If you haven't yet, go to Heroku.com slash changelog podcast and get excited about what's to come for Heroku.
[251.24 → 254.90] Once again, Heroku.com slash changelog podcast.
[258.90 → 262.70] Welcome to Pound Define.
[262.94 → 268.80] This is a game of obscure jargon, fake definitions, and expert tomfoolery.
[269.50 → 275.44] Our contestants checked their imposter syndrome at the door because they either know what these words mean
[275.44 → 279.44] or they're going to fake it till they make their peers think they know.
[280.26 → 284.32] Let's introduce our players in the order they will be playing.
[284.42 → 288.30] First up, she's our female equivalent of Matt Refer.
[288.30 → 292.84] And if you don't know what I mean, you will know as soon as she begins talking, it's Angelica Hill.
[293.56 → 294.08] Hello.
[294.80 → 296.92] I'm very excited to be here.
[297.64 → 304.60] I hope to prove my worth outside just being the female replacement for Matt Refer because he couldn't make it today.
[305.44 → 311.50] That is the goal is to win and also usurp Matt Refer as the best Brit on this podcast.
[311.94 → 313.28] Well, I like your odds.
[313.62 → 314.56] I like your odds.
[314.56 → 315.16] Yes.
[316.26 → 322.40] Plain second, our friend, fresh off of Oxide and Friends, Matthew Calabria.
[322.48 → 322.94] What's up, Matt?
[323.52 → 324.20] Hey, what's up?
[324.34 → 327.58] Glad to be here and fake it even though I made it.
[328.00 → 328.20] Right?
[328.38 → 329.08] You did make it.
[329.16 → 334.12] You showed up in the right place at the right time, but you still might have to fake some things.
[335.46 → 336.98] Plain third, he's mysterious.
[337.28 → 338.06] He's a brake master.
[338.22 → 339.42] He's our beat freak.
[339.66 → 340.96] He's brake master cylinder.
[341.90 → 342.18] Hi.
[342.86 → 343.60] What's up, BMC?
[343.64 → 344.10] How are you?
[345.32 → 346.04] Fine, I think.
[346.60 → 348.46] Thank you for having me on Science Layer.
[349.00 → 350.62] We are very excited.
[350.72 → 355.56] We wanted to have you to talk about the new album, After Party, but you're like, we've talked about music a lot.
[355.66 → 356.44] Let's do something else.
[356.50 → 358.02] And so I was like, come play a game with us.
[358.26 → 358.68] Yeah, thanks.
[359.12 → 360.72] I know nothing about this, so it's perfect.
[361.20 → 362.12] I can talk about music.
[362.12 → 366.58] But if I were to ask you about our brand-new album called After Party, what would you say about it?
[366.58 → 367.32] Oh, God.
[367.32 → 368.44] It's just the best.
[368.98 → 369.84] Oh, man.
[370.42 → 375.14] The sounds, the notes, the levels.
[375.58 → 375.86] The beats.
[376.38 → 376.74] Yes.
[376.74 → 377.10] Unreal.
[377.10 → 377.24] Unreal.
[379.78 → 382.50] And new to the changelog, but not new to me.
[382.60 → 385.04] We've been Omaha acquaintances for many years.
[385.16 → 386.26] It's John Henry Moeller.
[386.56 → 387.00] What's up, man?
[387.40 → 387.74] Oh, hey.
[388.26 → 389.36] Hello from Omaha.
[390.06 → 390.58] You're somewhere.
[390.94 → 392.06] Hello also from Omaha.
[393.06 → 395.36] Well, the greater Omaha area.
[395.88 → 397.60] Not better than, but just outside.
[397.72 → 398.82] That's where I live.
[399.12 → 399.42] All right.
[400.20 → 401.04] Maybe also better.
[401.12 → 401.54] I don't know.
[401.70 → 402.26] We'll see.
[402.54 → 408.98] And playing last, because we are gracious hosts around these parts, my partner in podcasting,
[409.10 → 410.58] Adam Stachowiak.
[410.68 → 411.14] What's up, man?
[411.36 → 411.82] What's up?
[411.88 → 412.26] What's up?
[412.82 → 413.48] I'm here to win.
[414.56 → 415.44] Fifth time's a charm.
[416.92 → 418.12] Time to find five.
[418.32 → 418.68] Here we go.
[420.82 → 424.22] And, of course, I'll be your not-so-humble host, Jared Santo.
[424.22 → 426.04] Here is how the game works.
[426.04 → 434.06] So we have 10 rounds of play, or 15 points scored, whichever comes first.
[435.26 → 436.34] I will present a word.
[437.14 → 441.68] You all will either know the definition of the word and submit that to me, or you will
[441.68 → 446.86] make up a fake definition that acts as if it's the actual definition and see if you can
[446.86 → 449.08] trick everyone else into selecting yours.
[449.66 → 454.98] If you know the correct definition immediately, you get three points, and you also get to take
[454.98 → 458.56] a break and sit that round out, because you already know the answer.
[459.30 → 465.00] If after I read all the definitions, you guess the correct one, you get two points, and for
[465.00 → 470.08] each person you trick into selecting your definition, you get one point.
[471.18 → 479.08] Now, if all five of you fail in any given round to select the correct definition, I,
[479.08 → 485.50] you are not-so-humble host, receive four points, and if I do that enough times, you all lose,
[485.72 → 487.10] which would be rad, I think.
[488.10 → 492.26] And your word for round one is Baryon.
[493.98 → 494.50] Baryon.
[494.62 → 497.26] B-A-R-Y-O-N.
[498.48 → 502.66] Please submit to me your definitions now.
[502.66 → 503.26] B-A-R-Y-O-N.
[504.28 → 506.58] I'm just adding some finesse to mine.
[506.92 → 511.28] I know the definition, I just need to, you know, make sure I've explained it clearly
[511.28 → 511.62] enough.
[512.12 → 512.32] B-A-R-Y-O-N.
[512.32 → 512.50] B-A-R-Y-O-N.
[512.50 → 512.60] B-A-R-Y-O-N.
[512.60 → 512.66] B-A-R-Y-O-N.
[513.52 → 513.82] B-A-R-Y-O-N.
[513.82 → 513.86] B-A-R-Y-O-N.
[513.86 → 514.22] B-A-R-Y-O-N.
[514.22 → 514.26] B-A-R-Y-O-N.
[515.26 → 515.32] B-A-R-Y-O-N.
[515.32 → 515.52] B-A-R-Y-O-N.
[515.52 → 516.32] B-A-R-Y-O-N.
[516.32 → 516.86] B-A-R-Y-O-N.
[516.86 → 517.72] B-A-R-Y-O-N.
[517.86 → 518.32] B-A-R-Y-O-N.
[519.04 → 519.10] B-A-R-Y-O.
[519.28 → 519.44] B-A-R-Y-O.
[520.20 → 520.84] B-A-R-Y-O-N.
[520.84 → 521.10] B-B-A-R-Y-O-N.
[521.10 → 524.42] It's not like a typical podcast where you have to be on the whole time.
[524.58 → 524.70] B-A-R-Y-O-N.
[524.70 → 524.90] B-A-R-Y-O-N.
[524.90 → 524.96] B-A-R-Y-O-N.
[524.96 → 525.10] B-A-R-Y-O-N.
[525.10 → 525.46] B-A-R-Y-O-N.
[525.46 → 529.38] B-A-R-Y-O-N.
[529.38 → 529.90] B-A-R-Y-O-N.
[529.90 → 530.38] B-A-R-Y-O-N.
[530.38 → 538.30] enough time we are not allowed to use no the internet I just assume yeah I mean you don't
[538.30 → 543.06] want to ruin the game I mean nobody wants that can you hear this
[543.06 → 555.18] we're off on a quest are you here you do hear it have you ever played um bomb corp it's one of
[555.18 → 564.10] those like jack box party games no this sounds like the intro music for it basically you defuse bombs
[564.10 → 569.52] you know I was going to say I played bomber man yeah check it out it sounds very similar vibe
[569.52 → 575.38] all right so Adam and BMC are both trailing indicators
[575.38 → 582.58] this I think is the actual track that I use in the produced episode during this time
[582.58 → 589.94] it's kind of nice right it's giving me black mirror vibes from the recent season
[589.94 → 593.12] this is a BMC original it's called study hall adventure
[593.12 → 597.68] do you remember making this one I do
[597.68 → 603.64] I remember the video game I was picturing while writing it
[603.64 → 607.80] was it bomb corp nope
[607.80 → 616.92] you've made so much music in your life I wonder if you like to forget songs you know
[616.92 → 618.00] yeah
[618.00 → 621.74] yes titles especially
[621.74 → 623.28] yeah
[623.28 → 626.36] all right Adam's in
[626.36 → 633.72] I'm also known for going last yeah so BMC's winning beating you
[633.72 → 639.78] it's good you're thoughtful before submission
[639.78 → 645.72] I said I got stressed out and submitted it and then ended up uh I ended up editing the message after
[645.72 → 647.56] I sent it do you want to resubmit
[647.56 → 652.06] no i i can edit the message once I've sent it to you
[652.06 → 655.40] well but I copy it out of there and put it somewhere else I'll recopy it
[655.40 → 659.24] it was just it was just slight grammatical errors that I needed to correct
[659.24 → 661.04] I'll recopy it then so I get your
[661.04 → 661.46] thank you
[661.46 → 662.50] I appreciate it
[662.50 → 666.86] and I added a little clarification on the end just to make it crystal clear
[666.86 → 670.62] is this on the album
[670.62 → 678.78] no it is not this is actually a really long it's like 50 minutes long they were like make it one level
[678.78 → 682.86] like if it was a hard level, and you keep playing it over and over for like an hour
[682.86 → 685.72] yeah you sort of get used to the same music
[685.72 → 687.68] do it like that
[687.68 → 696.08] I have all definitions for baryon I will read them now, and then you all will guess which one you think is correct
[696.08 → 699.46] starting with angelica and going from there so
[699.46 → 707.96] baryon a universally recognized culinary term for a cooking technique that covers the entirety of a cake or pastry in various berries
[707.96 → 715.62] berry covered or enrobed in berries it originates from the Greek berry for berry and on to put on so baryon
[715.62 → 718.06] that was number one
[718.06 → 718.90] number two
[718.90 → 723.14] the byproduct of a chemical reaction between two or more gases
[723.14 → 725.68] number three
[725.68 → 730.48] a particle used as a comparison marker in microscopic weight measurements
[730.48 → 732.16] number four
[732.16 → 735.74] a chemical mixture often used in sterilization for surgery
[735.74 → 737.52] number five
[737.52 → 741.46] a new element under review to be added to the periodic table of elements
[741.46 → 743.12] and number six
[743.12 → 745.54] composite particles made up of three quarks
[745.54 → 747.86] such as protons and neutrons
[747.86 → 749.82] there you have it
[749.82 → 751.96] six possible definitions
[751.96 → 753.96] for baryon
[753.96 → 757.72] it's now up to you all to decide which one is the actual definition
[757.72 → 760.46] starting with angelica which one do you think is
[760.46 → 760.96] real
[760.96 → 762.56] I mean I feel like
[762.56 → 763.88] they're chemical
[763.88 → 765.62] molecular or culinary
[765.62 → 767.32] these are my three options
[767.32 → 768.42] yes
[768.42 → 770.64] can I hear the third one again
[770.64 → 774.68] yeah the third one was a particle used as a comparison marker in microscopic
[774.68 → 776.10] weight measurements
[776.10 → 776.84] okay
[776.84 → 780.38] the one about medical procedures I think isn't right
[780.38 → 783.96] the one about a chemical mixture often used in sterilization
[783.96 → 784.96] so that's number four
[784.96 → 786.20] you think that's it or not it
[786.20 → 786.54] no
[786.54 → 787.04] not it
[787.04 → 787.44] why not
[787.44 → 790.74] i just don't I just don't think it's correct
[790.74 → 792.76] something in my bones tells me
[792.76 → 793.36] okay
[793.36 → 793.74] it just doesn't
[793.74 → 796.52] I feel like if a doctor came into my room and said
[796.52 → 798.90] oh we're about to inject you with baryon
[798.90 → 800.10] I'd be like no you're not
[800.66 → 802.10] um
[802.10 → 804.54] very assertive of you
[804.54 → 806.44] based on the sound alone
[806.44 → 807.98] I'm not going to
[807.98 → 808.48] yeah
[808.48 → 809.18] let you
[809.18 → 811.52] do the thing that you are uh
[811.52 → 812.60] went to school to do
[812.60 → 813.08] okay
[813.08 → 814.44] no I mean I won't
[814.44 → 816.00] I'd, I'd ask a little bit more
[816.00 → 817.68] you know I need a little bit more context
[817.68 → 820.96] on this strangely named chemical you're about to put to my body
[820.96 → 822.66] is that vibe doctoring
[822.66 → 824.44] oh I think that might be
[824.44 → 826.00] it's just not the vibe
[826.00 → 826.34] yeah
[826.34 → 827.58] let's call it something else
[827.58 → 828.02] all right
[828.02 → 832.14] I think it's I think it might need to be the second one that I asked you to repeat
[832.14 → 832.70] okay
[832.70 → 833.70] which one was that one
[833.70 → 834.76] the second one
[834.76 → 836.34] or the second one you asked me to repeat
[836.34 → 839.22] the first one that I asked you to repeat
[839.22 → 839.96] okay
[839.96 → 841.10] number three
[841.10 → 841.80] was the second
[841.80 → 845.80] number three was a particle used as a comparison marker in microscopic
[845.80 → 847.48] that's your that's yours right there okay
[847.48 → 848.54] we'll lock that in
[848.54 → 849.10] yes
[849.10 → 849.84] all right Matthew
[849.84 → 851.28] which one do you think is real
[851.28 → 853.82] there was a number of them
[853.82 → 855.96] of the definitions around
[855.96 → 858.56] chemical sort of deals
[858.56 → 860.40] I think there were maybe
[860.40 → 861.74] two or three of them
[861.74 → 862.74] can you repeat those
[862.74 → 868.42] so definition number four was a chemical mixture often used in sterilization for surgery
[868.42 → 869.04] okay
[869.04 → 871.02] number five was a new element
[871.02 → 873.10] is that the one you're thinking of or no
[873.10 → 873.94] possibly
[873.94 → 877.08] and number six was composite particles made up of three quarks
[877.08 → 878.60] quarks
[878.60 → 879.38] quarks
[879.38 → 880.38] quarks
[880.38 → 880.70] quarks
[880.70 → 881.54] can you
[881.54 → 883.22] I'm going to need to say that better
[883.22 → 883.84] cool
[883.84 → 885.72] q-u-a-r-k-s
[885.72 → 886.84] say it better jarred
[886.84 → 889.06] I'm saying it as best as I can
[889.06 → 894.26] there's also number two the byproduct of a chemical reaction between two or more gases
[894.26 → 897.00] oh so it was like four chemically definitions
[897.00 → 899.60] there's a lot that are in the same little category
[899.60 → 900.16] yes
[900.16 → 901.18] okay what are you thinking
[901.18 → 902.56] i I think
[902.56 → 905.14] since there's so many chemically things
[905.14 → 906.18] maybe it's wrong
[906.18 → 908.16] it sounds like it would be around
[908.16 → 909.92] maybe it's yeah it could either go one way
[909.92 → 911.16] it's either it's completely wrong
[911.16 → 911.62] or
[911.62 → 913.82] it's like in the area
[913.82 → 915.06] it's a lot of stuff man
[915.06 → 915.88] that's what it is
[915.88 → 916.36] uh okay
[916.36 → 917.06] I'm
[917.06 → 919.68] I think I'm going to choose the one that you couldn't pronounce well
[919.68 → 921.24] okay
[921.24 → 923.10] so quarks
[923.10 → 924.24] yeah that one
[924.24 → 925.02] quarks
[925.02 → 925.78] quarks
[925.78 → 926.28] quarks
[926.28 → 927.88] that choice was quirky
[927.88 → 928.40] okay
[928.40 → 930.64] now we go to BMC
[930.64 → 932.00] what do you think
[932.00 → 932.90] gases
[932.90 → 935.78] yeah I have notes
[935.78 → 938.38] good job
[938.38 → 940.34] I like how efficient you are
[940.34 → 941.52] yeah it says gases right there
[941.52 → 942.08] tangible
[942.08 → 943.30] I like having a pencil
[943.30 → 944.44] it's gas
[944.44 → 945.82] BMC takes two
[945.82 → 946.50] john Henry
[946.50 → 947.18] your turn
[947.18 → 950.02] number three was the one that was the measurement one
[950.02 → 950.80] yes
[950.80 → 951.56] that's correct
[951.56 → 953.10] I'm going to go with that one
[953.10 → 953.58] I think
[953.58 → 954.56] all right so you're
[954.56 → 956.38] you're going with angelica
[956.38 → 957.50] she picked that one as well
[957.50 → 958.80] so we have two
[958.80 → 960.08] for that one
[960.08 → 961.02] and
[961.02 → 962.10] lastly Adam
[962.10 → 963.38] would it be a
[963.38 → 964.92] total pain to have you repeat them all
[964.92 → 966.20] absolutely
[966.20 → 968.90] which one do you need
[968.90 → 970.74] all of them
[970.74 → 975.26] which one specifically
[975.26 → 977.08] let me summarize all six
[977.08 → 977.72] in order
[977.72 → 978.34] okay
[978.34 → 979.64] I'm not going to read them verbatim
[979.64 → 980.68] number one
[980.68 → 982.10] was the culinary one
[982.10 → 983.92] number two
[983.92 → 984.96] was the byproduct
[984.96 → 986.68] of two or more gases
[986.68 → 987.76] number three
[987.76 → 990.46] was the one that's used in microscopic weight measurements
[990.46 → 991.78] number four
[991.78 → 992.74] is the chemical mixture
[992.74 → 994.38] used in surgery
[994.38 → 996.00] except for not angelica surgeries
[996.00 → 997.64] number five
[997.64 → 998.62] a new element
[998.62 → 999.60] under review
[999.60 → 1001.36] to be in the table of elements
[1001.36 → 1002.32] and then number six
[1002.32 → 1003.54] composite particles
[1003.54 → 1004.70] made up of three quarks
[1004.70 → 1005.88] I'm thinking
[1005.88 → 1006.58] element
[1006.58 → 1007.62] it's a new element
[1007.62 → 1009.52] you're going for a new element
[1009.52 → 1010.24] that's right
[1010.24 → 1011.94] okay
[1011.94 → 1013.54] all right
[1013.54 → 1014.14] all six
[1014.14 → 1015.18] answers are in
[1015.18 → 1015.94] but who
[1015.94 → 1017.86] landed on the right
[1017.86 → 1018.82] definition
[1018.82 → 1020.08] let's start right there
[1020.08 → 1020.96] where we left off
[1020.96 → 1021.46] Adam
[1021.46 → 1023.44] you selected
[1023.44 → 1024.48] a new element
[1024.48 → 1025.74] under review
[1025.74 → 1026.28] to be added
[1026.28 → 1026.96] by the parent
[1026.96 → 1027.32] to the
[1027.32 → 1028.68] Adam that was yours
[1028.68 → 1031.30] you have to go away boy
[1031.30 → 1032.48] I love you
[1032.48 → 1033.46] he's distracted
[1033.46 → 1034.54] he was distracted
[1034.54 → 1035.94] did you see Patrick
[1035.94 → 1036.48] I know
[1036.48 → 1037.66] go with Patrick
[1037.66 → 1039.90] mom's away
[1039.90 → 1041.56] dads will play okay
[1041.56 → 1043.42] I had to watch a little bit of SpongeBob real quick
[1043.42 → 1044.02] but I'm back
[1044.02 → 1044.80] he's back
[1044.80 → 1045.88] are you distracted Adam
[1045.88 → 1047.76] because you selected your own definition
[1047.76 → 1048.52] oh no
[1048.52 → 1049.26] that was on purpose
[1049.26 → 1050.08] okay
[1050.08 → 1052.38] okay so selecting
[1052.38 → 1053.36] your own
[1053.36 → 1055.06] while I made trick other people
[1055.06 → 1056.72] you get zero points for doing that
[1056.72 → 1057.96] and you went last
[1057.96 → 1059.52] so the trick couldn't happen either
[1059.52 → 1060.72] interesting
[1060.72 → 1062.34] let's move on
[1062.34 → 1063.22] oh yeah
[1063.22 → 1064.64] to
[1064.64 → 1065.96] it's safe though
[1065.96 → 1066.32] right
[1066.32 → 1067.20] because then you're not
[1067.20 → 1068.58] it is a safe flight
[1068.58 → 1070.60] let's move on to what BMC thought it was
[1070.60 → 1072.34] the byproduct of a chemical reaction
[1072.34 → 1073.60] between two more gases
[1073.60 → 1076.06] he even wrote down gas right there on a piece of paper
[1076.06 → 1077.06] that was Matthews
[1077.06 → 1077.38] so
[1077.38 → 1079.12] one point to Matthew
[1079.12 → 1080.82] speaking of Matthew
[1080.82 → 1082.74] he thought it was the quarry one
[1082.74 → 1083.54] that I couldn't pronounce
[1083.54 → 1084.06] and you know what
[1084.06 → 1085.92] that's exactly what baryon is
[1085.92 → 1088.00] so he got it correct
[1088.00 → 1088.66] baryon
[1088.66 → 1089.56] composite particles
[1089.56 → 1090.80] made up of three quarks
[1090.80 → 1093.10] such as protons and neutrons
[1093.10 → 1094.20] you get two points
[1094.20 → 1095.64] so everyone you mispronounce
[1095.64 → 1096.38] is the definition
[1096.38 → 1096.86] got it
[1096.86 → 1097.10] okay
[1097.10 → 1097.98] we're in this
[1097.98 → 1099.06] we know what we're doing now
[1099.06 → 1100.70] but there are more points to give out
[1100.70 → 1102.72] because both angelica and john Henry
[1102.72 → 1105.44] piled on to BMC's definition
[1105.44 → 1106.78] the weight measurements
[1106.78 → 1107.74] that was BMC
[1107.74 → 1108.94] so two points BMC
[1108.94 → 1109.48] not bad
[1109.48 → 1111.26] oh I thought I was tricked
[1111.26 → 1113.02] I thought I was tricked by angelica
[1113.02 → 1114.02] no
[1114.02 → 1116.16] nope you're tricked by BMC
[1116.16 → 1116.66] yeah
[1116.66 → 1117.84] but I was right
[1117.84 → 1119.98] it was not used for surgical procedures
[1119.98 → 1122.08] so my gut instinct was correct
[1122.08 → 1122.98] 100%
[1122.98 → 1123.88] that was his
[1123.88 → 1124.60] yeah
[1124.60 → 1126.78] now there is a
[1126.78 → 1127.58] bear yum
[1127.58 → 1128.32] isn't there
[1128.32 → 1130.04] it's not a thing that they do
[1130.04 → 1131.48] for like enemas and stuff
[1131.48 → 1132.38] over beryllium
[1132.38 → 1134.72] maybe
[1134.72 → 1136.86] I'm just a vibe doctor
[1136.86 → 1137.68] not a real doctor
[1137.68 → 1141.10] all right
[1141.10 → 1142.66] so after round one
[1142.66 → 1144.18] Matthew's in the lead with three
[1144.18 → 1145.26] BMC has two
[1145.26 → 1146.20] and the rest of us
[1146.20 → 1148.58] have not scored quite yet
[1148.58 → 1150.74] we move now to round two
[1150.74 → 1152.18] and the word for round two
[1152.18 → 1153.54] is jaggies
[1153.54 → 1155.02] jaggies
[1155.02 → 1158.04] j-a-g-g-i-e-s
[1158.04 → 1158.98] jaggies
[1158.98 → 1159.62] please submit
[1159.62 → 1161.10] your definition
[1161.10 → 1162.60] for jaggies
[1162.60 → 1163.10] now
[1163.10 → 1165.78] are we saying
[1165.78 → 1167.06] these are all stem words
[1167.06 → 1169.32] um
[1169.32 → 1170.44] they are in the
[1170.44 → 1172.06] general world of that
[1172.06 → 1173.10] but they're not specifically
[1173.10 → 1175.42] they just call them like
[1175.42 → 1176.38] Jewish
[1176.38 → 1177.58] so no
[1177.58 → 1181.80] they aren't
[1181.80 → 1183.22] strictly stem
[1183.22 → 1184.74] but they are
[1184.74 → 1185.46] certainly
[1185.46 → 1186.76] steamy
[1186.76 → 1188.72] because like one time
[1188.72 → 1189.38] you were like
[1189.38 → 1191.16] oh what was that word
[1191.16 → 1192.64] gallery
[1192.64 → 1193.44] getting
[1193.44 → 1194.48] yes
[1194.48 → 1195.20] with food
[1195.20 → 1196.40] it was a big stew
[1196.40 → 1198.08] right
[1198.08 → 1198.80] uh
[1198.80 → 1200.00] in previous games
[1200.00 → 1200.80] we've had
[1200.80 → 1201.94] stem rounds
[1201.94 → 1203.30] and non-stem rounds
[1203.30 → 1205.16] and today I just decided
[1205.16 → 1206.40] just throw out the rules
[1206.40 → 1207.36] and just do words
[1207.36 → 1208.68] okay
[1208.68 → 1210.66] um all right
[1210.66 → 1211.38] Adam is in
[1211.38 → 1212.44] he's not the last one
[1212.44 → 1213.18] this time around
[1213.18 → 1214.40] I'm fighting for my
[1214.40 → 1215.22] right to party man
[1215.22 → 1216.70] get your jaggies on
[1216.70 → 1218.02] I'm trying to move
[1218.02 → 1218.66] like jaggies
[1218.66 → 1220.00] mmm
[1220.00 → 1224.10] if I didn't know the definition
[1224.10 → 1224.68] I would have
[1224.68 → 1226.02] I would have gone that direction
[1226.02 → 1227.14] and made you all laugh
[1227.14 → 1228.34] oh
[1228.34 → 1229.72] there's BMC
[1229.72 → 1230.98] coming in hot
[1230.98 → 1232.28] I mean I submitted myself
[1232.28 → 1232.94] mine right away
[1232.94 → 1234.10] because I already knew what it was
[1234.10 → 1235.54] simpatico
[1235.54 → 1236.12] angelica
[1236.12 → 1236.94] simpatico
[1236.94 → 1237.64] you and me
[1237.64 → 1239.14] all right
[1239.14 → 1240.58] we have six definitions
[1240.58 → 1241.34] for jaggies
[1241.34 → 1242.22] only one of them
[1242.22 → 1243.34] is actually
[1243.34 → 1244.22] the definition
[1244.22 → 1245.80] here they are
[1245.80 → 1246.54] number one
[1246.54 → 1248.30] containers used
[1248.30 → 1250.02] to hold raw mining material
[1250.02 → 1250.72] being
[1250.72 → 1252.74] for being processed
[1252.74 → 1254.02] number two
[1254.02 → 1255.36] stair-stepped edges
[1255.36 → 1256.76] in pixelated graphics
[1256.76 → 1257.90] due to low resolution
[1257.90 → 1258.86] or aliasing
[1258.86 → 1260.34] number three
[1260.34 → 1261.34] comfortable pants
[1261.34 → 1262.30] for remote working
[1262.30 → 1263.70] a play on leggings
[1263.70 → 1267.94] number four
[1267.94 → 1270.14] an irregular pathway
[1270.14 → 1271.22] taken by an object
[1271.22 → 1271.88] in response
[1271.88 → 1273.16] to magnetic stimuli
[1273.16 → 1274.80] number five
[1274.80 → 1275.88] in digital photography
[1275.88 → 1276.76] when an image
[1276.76 → 1277.46] is not clear
[1277.46 → 1278.16] the image
[1278.16 → 1279.16] will have jaggies
[1279.16 → 1280.84] and number
[1280.84 → 1282.98] six
[1282.98 → 1285.60] a gen z slang term
[1285.60 → 1286.42] initially used
[1286.42 → 1287.28] in colloquial
[1287.28 → 1288.46] typing and texting
[1288.46 → 1289.22] to refer to the
[1289.22 → 1290.24] lightning bolt emoji
[1290.24 → 1291.72] and this usage
[1291.72 → 1292.62] has now transitioned
[1292.62 → 1293.34] into the realm
[1293.34 → 1294.24] of software engineering
[1294.24 → 1295.60] in this technical context
[1295.60 → 1296.64] jaggies indicates
[1296.64 → 1297.28] sections
[1297.28 → 1298.06] within
[1298.06 → 1299.56] within code
[1299.56 → 1300.18] where high
[1300.18 → 1301.18] computational load
[1301.18 → 1302.38] or intensive processing
[1302.38 → 1302.94] is handled
[1302.94 → 1303.94] drawing a visual
[1303.94 → 1305.04] parallel to the sharp
[1305.04 → 1306.02] energetic nature
[1306.02 → 1307.08] of a lightning bolt
[1307.08 → 1308.02] and its link
[1308.02 → 1308.76] to electricity
[1308.76 → 1310.82] okay
[1310.82 → 1312.92] oh my gosh
[1312.92 → 1314.04] now you've heard
[1314.04 → 1315.04] all six definitions
[1315.04 → 1316.70] we start with Matthew
[1316.70 → 1317.92] which one do you think
[1317.92 → 1318.94] is actual
[1318.94 → 1320.68] uh can you repeat
[1320.68 → 1321.40] please
[1321.40 → 1323.14] number two
[1323.14 → 1325.46] four and five
[1325.46 → 1326.28] yes
[1326.28 → 1326.90] I wrote them down
[1326.90 → 1327.26] this time
[1327.26 → 1327.86] but I didn't get a chance
[1327.86 → 1328.36] to write them all down
[1328.36 → 1328.80] it's all good
[1328.80 → 1329.70] it's hard to keep track
[1329.70 → 1330.36] of all this stuff
[1330.36 → 1331.14] okay number two
[1331.14 → 1332.40] was the stair-stepped edges
[1332.40 → 1333.46] in pixelated graphics
[1333.46 → 1335.28] number
[1335.28 → 1336.40] do you want the full thing
[1336.40 → 1337.66] due to low resolution
[1337.66 → 1338.36] or aliasing
[1338.36 → 1340.84] number four
[1340.84 → 1341.72] is an irregular pathway
[1341.72 → 1342.70] taken by an object
[1342.70 → 1344.18] in response to magnetic stimuli
[1344.18 → 1345.30] and number five
[1345.30 → 1346.48] is in digital photography
[1346.48 → 1347.24] when an image
[1347.24 → 1348.00] is not clear
[1348.00 → 1349.02] the image will have
[1349.02 → 1349.58] jaggies
[1349.58 → 1350.86] okay
[1350.86 → 1352.36] I'm between two and four here
[1352.36 → 1352.94] okay
[1352.94 → 1354.26] stair-stepped edges
[1354.26 → 1355.32] due to aliasing
[1355.32 → 1356.00] that sounds
[1356.00 → 1357.00] that sounds right
[1357.00 → 1357.86] but
[1357.86 → 1358.98] so does
[1358.98 → 1360.64] the magnetic stimuli
[1360.64 → 1361.84] of irregular pathways
[1361.84 → 1362.88] that sounds fun too
[1362.88 → 1363.54] right
[1363.54 → 1364.22] I'm gonna lock in
[1364.22 → 1364.64] number four
[1364.64 → 1365.70] with the magnetic stuff
[1365.70 → 1366.26] all right
[1366.26 → 1367.40] number four locked in
[1367.40 → 1369.72] I go now to BMC
[1369.72 → 1371.10] can you rapid fire
[1371.10 → 1372.82] go through all of them
[1372.82 → 1373.82] as short as you like
[1373.82 → 1374.60] I just want to hear
[1374.60 → 1375.20] how you say it
[1375.20 → 1375.74] go
[1375.74 → 1377.02] number one
[1377.02 → 1377.70] was the containers
[1377.70 → 1378.96] the whole raw mining material
[1378.96 → 1380.60] number two
[1380.60 → 1382.00] was the pixelated graphics
[1382.00 → 1383.54] number three
[1383.54 → 1384.60] was comfortable pants
[1384.60 → 1386.76] number four
[1386.76 → 1388.26] was the irregular pathway
[1388.26 → 1389.54] number five
[1389.54 → 1390.98] is the digital photography
[1390.98 → 1392.72] and number six
[1392.72 → 1394.10] was the Gen Z slang term
[1394.10 → 1396.32] I'm going pants
[1396.32 → 1399.36] I love your conviction
[1399.36 → 1400.80] he's going pants
[1400.80 → 1401.86] all right
[1401.86 → 1402.24] John Henry
[1402.24 → 1402.72] your turn
[1402.72 → 1403.32] oof
[1403.32 → 1404.46] pants sounds
[1404.46 → 1405.78] pretty convincing there
[1405.78 → 1407.20] also
[1407.20 → 1408.84] the very run on
[1408.84 → 1411.62] Gen Z term
[1411.62 → 1412.26] wow
[1412.26 → 1413.42] there was so much detail
[1413.42 → 1414.76] how can it be wrong
[1414.76 → 1415.20] right
[1415.20 → 1416.88] I mean that's
[1416.88 → 1418.82] but I think I'm going to have to go
[1418.82 → 1419.50] with number four
[1419.50 → 1420.80] the pathways
[1420.80 → 1421.58] that
[1421.58 → 1422.92] that was convincing
[1422.92 → 1423.62] and
[1423.62 → 1425.20] not an obvious
[1425.20 → 1426.78] sound to the term
[1426.78 → 1427.42] so
[1427.42 → 1428.34] I like that
[1428.34 → 1429.60] piling on with Matthew
[1429.60 → 1431.06] on number four
[1431.06 → 1432.06] how about you Adam
[1432.06 → 1433.16] I'll spread it out
[1433.16 → 1434.56] I'm going for the last one
[1434.56 → 1435.46] because whoever wrote that
[1435.46 → 1437.00] deserves some points
[1437.00 → 1438.76] Adam picks the
[1438.76 → 1440.70] Gen Z slang term
[1440.70 → 1442.94] for the lightning bolt emoji
[1442.94 → 1444.08] that turned into a software
[1444.08 → 1444.98] engineering term
[1444.98 → 1446.14] well you guys know the rest
[1446.14 → 1447.30] next up
[1447.30 → 1448.08] Angelica
[1448.08 → 1449.38] last up Angelica
[1449.38 → 1450.48] can you
[1450.48 → 1450.80] I mean
[1450.80 → 1451.64] I wrote down
[1451.64 → 1452.10] two
[1452.10 → 1453.12] four and six
[1453.12 → 1453.52] so
[1453.52 → 1454.66] four I remember
[1454.66 → 1455.32] two
[1455.32 → 1456.74] was the jagged edge
[1456.74 → 1457.76] what was the two one
[1457.76 → 1458.88] yeah the stair stepped
[1458.88 → 1460.26] edges in pixelated graphics
[1460.26 → 1461.20] due to low resolution
[1461.20 → 1461.76] or aliasing
[1461.76 → 1464.02] and four is the one
[1464.02 → 1464.96] that Matthew and John Henry
[1464.96 → 1465.46] both picked
[1465.46 → 1466.28] okay
[1466.28 → 1467.52] and six is the
[1467.52 → 1469.88] lightning bolt emoji
[1469.88 → 1471.44] jaggy's just
[1471.44 → 1472.26] just too fun
[1472.26 → 1473.02] to not be to do
[1473.02 → 1473.94] with something that's visual
[1473.94 → 1475.46] but I don't think
[1475.46 → 1476.44] it's a photography one
[1476.44 → 1477.76] as someone who
[1477.76 → 1479.30] aspires to be able
[1479.30 → 1480.64] to understand Gen Z
[1480.64 → 1481.68] I think I'll go
[1481.68 → 1482.56] with the last one
[1482.56 → 1483.70] so you are picking
[1483.70 → 1484.50] the last one
[1484.50 → 1485.48] maybe it'll make me cool
[1485.48 → 1486.76] yeah I can whip it out
[1486.76 → 1487.50] if it's correct
[1487.50 → 1489.40] talk to the
[1489.40 → 1490.62] the Gen Z's
[1490.62 → 1491.18] get some
[1491.18 → 1491.84] some cred
[1491.84 → 1492.96] that would be cool
[1492.96 → 1494.92] well Adam also
[1494.92 → 1495.52] picked that one
[1495.52 → 1496.14] so let's start
[1496.14 → 1496.96] right there
[1496.96 → 1497.80] and see maybe
[1497.80 → 1498.64] that is what
[1498.64 → 1499.60] jaggies are
[1499.60 → 1501.28] however Angelica
[1501.28 → 1502.00] didn't you write
[1502.00 → 1502.44] that one
[1502.44 → 1503.56] yeah I did
[1503.56 → 1504.76] yeah you're right
[1504.76 → 1505.88] it was so cool
[1505.88 → 1506.94] it deserved to be selected
[1506.94 → 1507.72] so you don't get any
[1507.72 → 1508.52] points for selecting it
[1508.52 → 1509.64] yourself, but you do get
[1509.64 → 1510.46] one point for
[1510.46 → 1512.10] getting Adam to select it
[1512.10 → 1512.26] see
[1512.26 → 1513.08] well done
[1513.08 → 1513.86] simpatico
[1513.86 → 1515.40] now Matthew and
[1515.40 → 1515.94] John Henry
[1515.94 → 1517.68] piled on to number
[1517.68 → 1518.16] four
[1518.16 → 1519.34] an irregular pathway
[1519.34 → 1520.74] taken by an object
[1520.74 → 1522.32] in response to
[1522.32 → 1523.08] magnetic stimuli
[1523.08 → 1523.92] well that was
[1523.92 → 1524.78] very convincing
[1524.78 → 1525.50] and that was
[1525.50 → 1526.36] BMC's
[1526.36 → 1527.50] made up definition
[1527.50 → 1528.24] good job BMC
[1528.24 → 1528.88] very nice
[1528.88 → 1530.18] two points for you
[1530.18 → 1531.30] which means it's up
[1531.30 → 1531.90] to BMC
[1531.90 → 1533.02] to actually select
[1533.02 → 1533.58] correctly
[1533.58 → 1534.22] otherwise
[1534.22 → 1535.70] your not so humble
[1535.70 → 1536.40] host gets to the
[1536.40 → 1537.06] points this round
[1537.06 → 1538.58] you thought it was
[1538.58 → 1539.42] comfortable pants
[1539.42 → 1540.38] for remote work
[1540.38 → 1542.44] play on leggings
[1542.44 → 1544.82] what do you think
[1544.82 → 1545.42] is that right
[1545.42 → 1547.02] do I think it's right
[1547.02 → 1548.14] it's either that
[1548.14 → 1548.96] or the stairs' thing
[1548.96 → 1549.76] but yeah let's go
[1549.76 → 1550.82] all in on pants
[1550.82 → 1554.44] all in on pants
[1554.44 → 1555.20] and all out
[1555.20 → 1556.12] on the correct
[1556.12 → 1556.74] answer
[1556.74 → 1557.72] so four points
[1557.72 → 1558.76] for me the correct
[1558.76 → 1560.14] definition of jaggies
[1560.14 → 1560.90] is stair-stepped
[1560.90 → 1561.82] edges in pixelated
[1561.82 → 1562.54] graphics due to
[1562.54 → 1563.24] low resolution
[1563.24 → 1564.58] or aliasing
[1564.58 → 1565.58] that's what I was
[1565.58 → 1565.90] trying to say
[1565.90 → 1566.52] with my photography
[1566.52 → 1566.90] one
[1566.90 → 1567.82] you were somewhat
[1567.82 → 1568.76] close I almost
[1568.76 → 1569.48] gave you
[1569.48 → 1570.18] you should give it
[1570.18 → 1570.58] to me that's what
[1570.58 → 1571.08] it is
[1571.08 → 1571.74] that's what I know
[1571.74 → 1572.56] it's from photography
[1572.56 → 1573.66] you use the word
[1573.66 → 1574.58] jaggies in the
[1574.58 → 1575.54] definition and you
[1575.54 → 1576.24] can't do that
[1576.24 → 1576.80] so I just
[1576.80 → 1577.78] I couldn't
[1577.78 → 1578.22] give it to you
[1578.22 → 1578.50] that's what I meant
[1578.50 → 1580.20] these are tough
[1580.20 → 1580.64] rules
[1580.64 → 1582.32] I'm getting robbed
[1582.32 → 1583.40] wait are you not
[1583.40 → 1584.18] allowed to put the
[1584.18 → 1585.14] name the word
[1585.14 → 1585.86] in the definition
[1585.86 → 1586.88] well you I mean
[1586.88 → 1587.66] technically when you
[1587.66 → 1588.30] define something
[1588.30 → 1588.76] you're not supposed
[1588.76 → 1589.52] to use the word
[1589.52 → 1590.22] in the definition
[1590.22 → 1590.72] I didn't know
[1590.72 → 1592.16] the clinical version
[1592.16 → 1592.98] of it I just knew
[1592.98 → 1593.68] when an image
[1593.68 → 1594.34] isn't clear
[1594.34 → 1595.60] you get those
[1595.60 → 1596.44] jaggies
[1596.44 → 1596.76] jaggies
[1596.76 → 1597.78] the jaggies
[1597.78 → 1598.86] I don't think
[1598.86 → 1599.22] that's usually
[1599.22 → 1599.96] for photography
[1599.96 → 1600.40] though that's
[1600.40 → 1601.22] usually more like
[1601.22 → 1603.16] the context
[1603.16 → 1604.00] is more video game
[1604.00 → 1604.24] dev
[1604.24 → 1605.24] yeah that's what
[1605.24 → 1605.80] I figured it would
[1605.80 → 1605.90] be
[1605.90 → 1606.10] yeah
[1606.10 → 1607.06] if you had said
[1607.06 → 1607.60] video games
[1607.60 → 1607.98] I probably would
[1607.98 → 1608.44] have given it to
[1608.44 → 1608.64] you
[1608.64 → 1609.50] well I only know
[1609.50 → 1609.94] it in the context
[1609.94 → 1610.36] of photography
[1610.36 → 1610.76] I'm sorry
[1610.76 → 1612.20] that's alright
[1612.20 → 1613.12] it's like saying
[1613.12 → 1614.24] a bite is not a
[1614.24 → 1614.82] bite because you
[1614.82 → 1615.54] experience it somewhere
[1615.54 → 1615.84] else
[1615.84 → 1616.32] so you know
[1616.32 → 1616.82] still a bite
[1616.82 → 1617.34] what are you
[1617.34 → 1617.72] biting into
[1617.72 → 1618.12] over there
[1618.12 → 1618.68] like someone's
[1618.68 → 1618.98] leg
[1618.98 → 1619.80] a bit
[1619.80 → 1620.34] or a bite
[1620.34 → 1621.20] that'd be
[1621.20 → 1621.64] jaggy
[1621.64 → 1622.76] alright let's
[1622.76 → 1623.06] move down
[1623.06 → 1623.46] to round 3
[1623.46 → 1623.86] well hold on
[1623.86 → 1624.60] let's add up
[1624.60 → 1625.58] these totals
[1625.58 → 1626.10] because you know
[1626.10 → 1626.70] what I might have
[1626.70 → 1627.12] just moved in
[1627.12 → 1627.68] the first place
[1627.68 → 1628.46] ooh I did
[1628.46 → 1629.28] I am tied
[1629.28 → 1630.12] with BMC
[1630.12 → 1630.90] in first place
[1630.90 → 1631.80] with 4 points
[1631.80 → 1632.74] Matthew has 3
[1632.74 → 1633.60] Angelica won
[1633.60 → 1634.40] and so far
[1634.40 → 1635.38] sir I think
[1635.38 → 1635.94] your math is
[1635.94 → 1636.42] incorrect
[1636.42 → 1637.94] isn't it 3
[1637.94 → 1638.50] for getting
[1638.50 → 1638.86] someone
[1638.86 → 1640.38] or isn't it
[1640.38 → 1641.10] 3 for guessing
[1641.10 → 1641.80] the correct definition
[1641.80 → 1642.82] it's 3 if you
[1642.82 → 1643.26] guess it
[1643.26 → 1643.86] initially
[1643.86 → 1645.30] it's 2 if you
[1645.30 → 1645.78] guess it at the
[1645.78 → 1646.06] end
[1646.06 → 1647.64] so had Adam
[1647.64 → 1648.16] actually just
[1648.16 → 1648.72] given me the
[1648.72 → 1649.42] correct definition
[1649.42 → 1649.96] even though he
[1649.96 → 1650.32] was somewhat
[1650.32 → 1650.68] close
[1650.68 → 1651.30] he would have
[1651.30 → 1651.64] got 3
[1651.64 → 1652.10] immediately
[1652.10 → 1652.88] but if you
[1652.88 → 1653.16] guess it
[1653.16 → 1653.64] correctly at the
[1653.64 → 1654.00] end you get
[1654.00 → 1654.26] 2
[1654.26 → 1655.10] oh ok
[1655.10 → 1655.48] if you guess
[1655.48 → 1655.76] it correctly
[1655.76 → 1656.14] during
[1656.14 → 1657.10] ok I understand
[1657.10 → 1657.66] after you hear
[1657.66 → 1658.20] the definitions
[1658.20 → 1658.92] ok so your
[1658.92 → 1659.72] math is correct
[1659.72 → 1660.26] I understand
[1660.26 → 1660.48] thank you
[1660.48 → 1661.10] and you get
[1661.10 → 1661.46] a point
[1661.46 → 1662.16] when somebody
[1662.16 → 1664.02] guesses yours
[1664.02 → 1664.26] gets fooled
[1664.26 → 1664.52] yeah
[1664.52 → 1665.32] that's right
[1665.32 → 1665.98] like picks
[1665.98 → 1666.50] your pants
[1666.50 → 1667.76] oh my bad
[1667.76 → 1668.16] you're right
[1668.16 → 1668.94] oh, thank you
[1668.94 → 1669.40] fair
[1669.40 → 1671.12] my math is wrong
[1671.12 → 1673.32] I just didn't
[1673.32 → 1674.16] write that point down
[1674.16 → 1674.92] he was the pants one
[1674.92 → 1675.22] John
[1675.22 → 1676.18] yeah he was the pants one
[1676.18 → 1676.72] I just forgot
[1676.72 → 1677.32] because I was moving
[1677.32 → 1677.94] on to the fact
[1677.94 → 1678.58] that I won the round
[1678.58 → 1679.32] yeah that was a good
[1679.32 → 1679.96] one leggings
[1679.96 → 1680.68] I liked it
[1680.68 → 1681.48] I feel like I'm
[1681.48 → 1682.04] learning already
[1682.04 → 1682.62] in this game
[1682.62 → 1683.60] the more detailed
[1683.60 → 1684.08] the answer
[1684.08 → 1684.86] other than Adam
[1684.86 → 1686.28] who appreciates it
[1686.28 → 1687.82] gotta keep it short
[1687.82 → 1688.32] and sweet
[1688.32 → 1689.22] yeah you're writing
[1689.22 → 1690.00] books over there
[1690.00 → 1690.82] just letting my
[1690.82 → 1692.20] creativity fly
[1692.20 → 1693.04] that was very creative
[1693.04 → 1693.62] I liked it
[1693.62 → 1694.20] it's hard for me
[1694.20 → 1695.04] to read that long
[1695.04 → 1696.08] without starting to laugh
[1696.08 → 1696.78] yeah I'm sorry
[1696.78 → 1697.44] I'll try to make
[1697.44 → 1698.26] I'll make them short
[1698.26 → 1698.54] ok
[1698.54 → 1699.64] I just want to
[1699.64 → 1700.36] I want to represent
[1700.36 → 1701.82] your definitions well
[1701.82 → 1702.44] and it's just
[1702.44 → 1703.52] the more I'm reading
[1703.52 → 1704.32] the more it gets
[1704.32 → 1705.94] become kind of
[1705.94 → 1706.84] funny
[1706.84 → 1707.18] ok
[1707.18 → 1707.78] I hear you Jared
[1707.78 → 1708.62] I hear you
[1708.62 → 1709.48] now I don't want
[1709.48 → 1710.20] to shut out John Henry
[1710.20 → 1710.70] he's
[1710.70 → 1711.82] has a point
[1711.82 → 1712.40] so he got
[1712.40 → 1713.70] Adam locked in the dungeon
[1713.70 → 1714.70] now all by himself
[1714.70 → 1715.94] and the rest of us
[1715.94 → 1716.42] on the board
[1716.42 → 1717.48] let's move now
[1717.48 → 1718.22] to round three
[1718.22 → 1719.34] where the word
[1719.34 → 1721.02] for round three
[1721.02 → 1722.12] is oobleck
[1722.12 → 1723.18] oobleck
[1723.18 → 1726.16] that's O-O-B-L-E-C-K
[1726.16 → 1727.74] oobleck
[1727.74 → 1728.84] it's fun to say
[1728.84 → 1729.30] at least
[1729.30 → 1730.86] it is fun to say
[1730.86 → 1732.68] is it fun to define
[1732.68 → 1734.56] we'll find out
[1734.56 → 1737.00] right after this
[1737.00 → 1738.58] well friends
[1738.58 → 1739.00] I'm here with
[1739.00 → 1739.46] David Hsu
[1739.46 → 1740.64] CEO of
[1740.64 → 1741.44] Retool
[1741.44 → 1742.34] David I want to
[1742.34 → 1742.98] talk about
[1742.98 → 1744.42] awareness beyond
[1744.42 → 1745.40] Silicon Valley
[1745.40 → 1746.50] Retool has a
[1746.50 → 1747.34] great presence
[1747.34 → 1748.12] and a great
[1748.12 → 1748.70] awareness
[1748.70 → 1750.10] inside Silicon Valley
[1750.10 → 1750.54] but what about
[1750.54 → 1750.90] beyond
[1750.90 → 1752.24] what's really cool
[1752.24 → 1752.68] is I think
[1752.68 → 1753.54] we've done a
[1753.54 → 1754.44] perfect job
[1754.44 → 1754.88] of building
[1754.88 → 1755.46] awareness
[1755.46 → 1756.10] inside
[1756.10 → 1756.76] Silicon Valley
[1756.76 → 1757.64] and so when
[1757.64 → 1758.32] you look at
[1758.32 → 1758.96] customers that
[1758.96 → 1759.52] use Retool
[1759.52 → 1760.38] pretty much
[1760.38 → 1761.06] every big
[1761.06 → 1761.44] company in
[1761.44 → 1761.90] Silicon Valley
[1761.90 → 1762.44] about a thousand
[1762.44 → 1763.08] people today
[1763.08 → 1763.94] now uses Retool
[1763.94 → 1764.24] and builds
[1764.24 → 1764.94] internal apps
[1764.94 → 1765.80] via Retool
[1765.80 → 1766.22] so that's
[1766.22 → 1766.86] really awesome
[1766.86 → 1767.32] and I'm really
[1767.32 → 1767.78] proud of the
[1767.78 → 1768.42] progress we've made
[1768.42 → 1768.66] there
[1768.66 → 1769.24] but I think
[1769.24 → 1769.70] the larger
[1769.70 → 1770.24] opportunity
[1770.24 → 1770.70] for us
[1770.70 → 1771.08] actually
[1771.08 → 1771.38] it's
[1771.38 → 1771.94] outside
[1771.94 → 1772.44] Silicon Valley
[1772.44 → 1772.88] when you think
[1772.88 → 1773.28] about for
[1773.28 → 1773.46] example
[1773.46 → 1774.14] the Kroger's
[1774.14 → 1774.68] of the world
[1774.68 → 1775.76] the Coca-Cola's
[1775.76 → 1776.26] of the world
[1776.26 → 1777.12] many of them
[1777.12 → 1777.66] are customers
[1777.66 → 1778.34] already today
[1778.34 → 1778.98] but I think
[1778.98 → 1779.60] we haven't done
[1779.60 → 1780.04] as good as
[1780.04 → 1780.44] a job
[1780.44 → 1781.28] building awareness
[1781.28 → 1781.96] if you will
[1781.96 → 1783.40] around the
[1783.40 → 1783.84] developers
[1783.84 → 1784.26] and all these
[1784.26 → 1784.62] companies
[1784.62 → 1785.74] and that to me
[1785.74 → 1786.28] is where the
[1786.28 → 1787.30] opportunity lies
[1787.30 → 1788.64] because so much
[1788.64 → 1789.30] of these companies
[1789.30 → 1790.44] run on software
[1790.44 → 1791.32] software is so
[1791.32 → 1791.84] important
[1791.84 → 1792.42] if you think
[1792.42 → 1792.94] about Coca-Cola
[1792.94 → 1793.44] for example
[1793.44 → 1794.06] Coca-Cola's
[1794.06 → 1794.58] not really gotten
[1794.58 → 1795.00] any cheaper
[1795.00 → 1795.58] to manufacture
[1795.58 → 1796.26] in the last
[1796.26 → 1797.00] 10 or 20 years
[1797.00 → 1797.70] instead
[1797.70 → 1799.06] the reason why
[1799.06 → 1799.48] Coca-Cola's
[1799.48 → 1799.82] doing well
[1799.82 → 1800.26] as a company
[1800.26 → 1800.90] is because they
[1800.90 → 1801.30] are getting
[1801.30 → 1801.96] more productive
[1801.96 → 1802.78] by a better
[1802.78 → 1803.34] software
[1803.34 → 1804.02] and so every
[1804.02 → 1804.76] company needs
[1804.76 → 1805.26] to become
[1805.26 → 1805.70] a software
[1805.70 → 1806.22] company
[1806.22 → 1806.88] and Retool
[1806.88 → 1807.34] lets you
[1807.34 → 1807.88] do that
[1807.88 → 1808.80] so Coke
[1808.80 → 1809.72] is a big
[1809.72 → 1810.12] company
[1810.12 → 1810.52] but the
[1810.52 → 1811.04] principle
[1811.04 → 1812.60] rings true
[1812.60 → 1813.70] become more
[1813.70 → 1814.30] efficient by
[1814.30 → 1814.94] using better
[1814.94 → 1815.48] software
[1815.48 → 1816.36] there you go
[1816.36 → 1817.02] well if you're
[1817.02 → 1818.08] beyond Silicon
[1818.08 → 1818.64] Valley
[1818.64 → 1819.70] raise your hand
[1819.70 → 1820.06] we want to
[1820.06 → 1820.54] hear from you
[1820.54 → 1820.86] I want to
[1820.86 → 1821.36] tell Dave
[1821.36 → 1821.68] that we've
[1821.68 → 1822.18] reached people
[1822.18 → 1822.84] beyond Silicon
[1822.84 → 1823.26] Valley
[1823.26 → 1823.78] that we're
[1823.78 → 1824.28] raising the
[1824.28 → 1824.62] awareness
[1824.62 → 1825.36] of what
[1825.36 → 1826.22] Retool is
[1826.22 → 1826.58] and what
[1826.58 → 1827.32] Retool does
[1827.32 → 1827.96] and some
[1827.96 → 1828.58] big announcements
[1828.58 → 1829.44] coming soon
[1829.44 → 1830.14] here on
[1830.14 → 1830.50] Changelog
[1830.50 → 1831.00] which is cool
[1831.00 → 1831.56] well if you
[1831.56 → 1831.92] haven't yet
[1831.92 → 1832.38] go to
[1832.38 → 1833.86] Retool.com
[1833.86 → 1834.48] get a demo
[1834.48 → 1835.08] try it out
[1835.08 → 1835.66] for free
[1835.66 → 1836.44] all that
[1836.44 → 1837.10] good stuff
[1837.10 → 1837.76] again
[1837.76 → 1839.66] Retool.com
[1839.66 → 1844.20] how do we know
[1844.20 → 1844.66] that you're giving
[1844.66 → 1845.06] us the right
[1845.06 → 1845.80] pronunciation of
[1845.80 → 1846.24] these words
[1846.24 → 1847.46] I just take my
[1847.46 → 1848.08] word for it
[1848.08 → 1848.60] okay
[1848.60 → 1849.08] understood
[1849.08 → 1850.06] but are you
[1850.06 → 1850.60] claiming to
[1850.60 → 1850.86] you've lied
[1850.86 → 1851.48] about math
[1851.48 → 1851.82] yeah
[1851.82 → 1853.66] I make no
[1853.66 → 1854.08] claims
[1854.08 → 1855.14] neither express
[1855.14 → 1855.66] or implied
[1855.66 → 1857.12] most of these
[1857.12 → 1857.72] I looked up
[1857.72 → 1858.38] the pronunciation
[1858.38 → 1859.20] I actually
[1859.20 → 1860.22] forgot to
[1860.22 → 1860.54] on this
[1860.54 → 1860.78] one
[1860.78 → 1861.78] but don't
[1861.78 → 1862.26] google it
[1862.26 → 1862.60] because you'll
[1862.60 → 1862.80] know the
[1862.80 → 1863.16] definition
[1863.16 → 1863.90] let me make
[1863.90 → 1864.22] sure I'm
[1864.22 → 1864.54] saying it
[1864.54 → 1864.72] right
[1864.72 → 1865.48] hold on
[1865.48 → 1865.82] maybe this
[1865.82 → 1866.16] will work
[1866.16 → 1867.28] hey Siri
[1867.28 → 1867.72] define
[1867.72 → 1868.26] oobleck
[1868.26 → 1868.94] no, no
[1868.94 → 1869.68] no
[1869.68 → 1870.52] anyone
[1870.52 → 1870.94] anyone
[1870.94 → 1871.34] anyone
[1871.34 → 1871.76] things go
[1871.76 → 1871.98] off
[1871.98 → 1872.30] no
[1872.30 → 1873.28] damn it
[1873.28 → 1873.60] why are you
[1873.60 → 1873.96] trying to get
[1873.96 → 1874.48] other people
[1874.48 → 1874.94] to answer
[1874.94 → 1875.52] yeah
[1875.52 → 1875.94] you think I
[1875.94 → 1876.50] have Siri
[1876.50 → 1876.98] enabled on my
[1876.98 → 1877.22] phone
[1877.22 → 1879.10] we don't like
[1879.10 → 1879.36] her
[1879.36 → 1880.42] I don't call her
[1880.42 → 1880.98] Siri anymore
[1880.98 → 1882.62] she never called
[1882.62 → 1883.02] me back
[1883.02 → 1883.26] so
[1883.26 → 1885.16] my brother's
[1885.16 → 1885.70] ex-girlfriend
[1885.70 → 1885.96] is called
[1885.96 → 1886.40] Siri
[1886.40 → 1887.84] I'm sorry
[1887.84 → 1888.18] for her
[1888.18 → 1888.42] loss
[1888.42 → 1889.82] was that her
[1889.82 → 1890.36] name or he
[1890.36 → 1890.74] just called
[1890.74 → 1891.12] her that
[1891.12 → 1892.18] no that was
[1892.18 → 1893.02] her legit name
[1893.02 → 1894.12] that hurts
[1894.12 → 1895.28] so are you
[1895.28 → 1895.86] giving us the
[1895.86 → 1896.58] proper pronunciation
[1896.58 → 1898.28] or I was
[1898.28 → 1898.86] waiting for that
[1898.86 → 1899.28] personally
[1899.28 → 1900.04] oh my bad
[1900.04 → 1900.98] I actually got
[1900.98 → 1901.44] distracted
[1901.44 → 1901.80] and started
[1901.80 → 1902.42] with someone else
[1902.42 → 1903.18] oh okay
[1903.18 → 1904.68] I was just
[1904.68 → 1905.20] waiting for that
[1905.20 → 1905.66] I was just
[1905.66 → 1905.90] you know
[1905.90 → 1906.50] just curious
[1906.50 → 1907.54] okay I just
[1907.54 → 1908.24] confirmed it's
[1908.24 → 1908.94] oobleck
[1908.94 → 1910.28] specifically as I
[1910.28 → 1910.74] said it
[1910.74 → 1911.94] so since you
[1911.94 → 1912.44] said you check
[1912.44 → 1912.92] your email
[1912.92 → 1913.72] during this
[1913.72 → 1914.68] and you also
[1914.68 → 1915.24] said that not
[1915.24 → 1915.80] every email gets
[1915.80 → 1916.36] a response
[1916.36 → 1917.04] is now a good
[1917.04 → 1918.04] time to email
[1918.04 → 1918.28] you
[1918.28 → 1918.76] this would be a
[1918.76 → 1919.20] great time
[1919.20 → 1920.24] okay perfect
[1920.24 → 1922.92] this reminds me
[1922.92 → 1923.32] while we wait
[1923.32 → 1923.96] for BMC
[1923.96 → 1925.62] you guys may or
[1925.62 → 1926.20] may not know
[1926.20 → 1927.08] that I have an
[1927.08 → 1928.14] entire soundboard
[1928.14 → 1929.90] of BMC noises
[1929.90 → 1930.84] really
[1930.84 → 1932.14] I dislike anything
[1932.14 → 1932.56] that makes me
[1932.56 → 1933.42] happy and I do
[1933.42 → 1934.46] that and then I
[1934.46 → 1935.02] do the next thing
[1935.02 → 1936.08] you're welcome
[1936.08 → 1939.34] uh
[1939.34 → 1940.40] words to live
[1940.40 → 1940.66] by
[1940.66 → 1944.06] do this thing
[1944.06 → 1945.46] you like glitchy
[1945.46 → 1946.32] things and
[1946.32 → 1948.02] you know
[1948.02 → 1949.04] things
[1949.04 → 1950.90] okay that's my
[1950.90 → 1951.34] definition
[1951.34 → 1953.12] here's my favourite
[1953.12 → 1953.78] one
[1953.78 → 1954.98] heck ins yeah
[1954.98 → 1955.60] I said to
[1955.60 → 1956.14] myself
[1956.14 → 1961.30] sometimes I throw
[1961.30 → 1961.82] those in at the
[1961.82 → 1962.40] end of the show
[1962.40 → 1963.16] when I'm thanking
[1963.16 → 1963.72] you for making
[1963.72 → 1964.12] our beats
[1964.12 → 1964.74] yes I've heard
[1964.74 → 1965.86] oh you've heard
[1965.86 → 1966.78] nice
[1966.78 → 1968.78] this one I'll
[1968.78 → 1969.22] usually throw in
[1969.22 → 1969.58] this one
[1969.58 → 1970.40] I'm here for
[1970.40 → 1971.12] your sound needs
[1971.12 → 1972.50] I'm here for
[1972.50 → 1973.14] your sound needs
[1973.14 → 1975.26] hold on I'm
[1975.26 → 1975.90] getting distracted
[1975.90 → 1976.78] by all the smart
[1976.78 → 1977.80] funny things I say
[1977.80 → 1978.34] one second
[1978.34 → 1979.00] do you still need
[1979.00 → 1979.42] jobs
[1979.42 → 1980.58] if you're listening
[1980.58 → 1981.54] I need jobs
[1981.54 → 1982.46] thank you
[1982.46 → 1984.42] that was just me
[1984.42 → 1984.70] talking
[1984.70 → 1986.66] please give me
[1986.66 → 1986.98] work
[1986.98 → 1989.12] please give me
[1989.12 → 1989.60] work
[1989.60 → 1991.72] you sound like
[1991.72 → 1992.26] Batman
[1992.26 → 1993.42] he's already
[1993.42 → 1993.86] does
[1993.86 → 1995.70] you're both
[1995.70 → 1996.94] Batman and
[1996.94 → 1998.18] a spider-man
[1998.18 → 1999.00] evil
[1999.00 → 2000.28] octopus man
[2000.28 → 2000.92] at the same
[2000.92 → 2002.10] aww thank you
[2002.10 → 2004.26] you're welcome
[2004.26 → 2006.24] I love a
[2006.24 → 2006.72] backhanded
[2006.72 → 2007.18] compliment
[2007.18 → 2007.96] oh cool
[2007.96 → 2009.62] aww man
[2009.62 → 2011.26] aww
[2011.26 → 2015.92] I actually
[2015.92 → 2016.30] really do
[2016.30 → 2016.64] like your
[2016.64 → 2016.94] goggles
[2016.94 → 2017.84] if I could
[2017.84 → 2018.46] get prescription
[2018.46 → 2018.88] goggles
[2018.88 → 2019.34] that would
[2019.34 → 2019.74] be awesome
[2019.74 → 2020.00] that would
[2020.00 → 2020.36] be awesome
[2020.36 → 2020.84] but I can't
[2020.84 → 2021.56] see past
[2021.56 → 2022.18] like two
[2022.18 → 2022.62] inches
[2022.62 → 2023.48] on my face
[2023.48 → 2023.98] so
[2023.98 → 2024.66] right
[2024.66 → 2025.82] I would
[2025.82 → 2026.12] need them
[2026.12 → 2026.36] to be
[2026.36 → 2026.94] very heavy
[2026.94 → 2027.38] yeah
[2027.38 → 2028.56] I like
[2028.56 → 2028.78] these
[2028.78 → 2029.20] they have
[2029.20 → 2029.52] saved
[2029.52 → 2030.12] my face
[2030.12 → 2031.30] from what
[2031.30 → 2032.30] uh
[2032.30 → 2033.76] doorways
[2033.76 → 2036.96] door frames
[2036.96 → 2038.02] one of these
[2038.02 → 2038.56] is shattered
[2038.56 → 2039.78] I was gonna
[2039.78 → 2040.24] say you
[2040.24 → 2040.72] can't hit
[2040.72 → 2041.34] doorways
[2041.34 → 2041.76] we can hit
[2041.76 → 2042.26] door frames
[2042.26 → 2042.88] or doors
[2042.88 → 2043.68] this was
[2043.68 → 2044.18] going to be
[2044.18 → 2044.82] my face
[2044.82 → 2045.42] instead it
[2045.42 → 2046.10] shattered this
[2046.10 → 2046.72] and I find
[2046.72 → 2047.32] it is very lucky
[2047.32 → 2048.54] oh okay
[2048.54 → 2049.64] the end
[2049.64 → 2050.48] do you routinely
[2050.48 → 2051.00] hit into
[2051.00 → 2051.82] door frames
[2051.82 → 2052.30] I did that
[2052.30 → 2052.70] one time
[2052.70 → 2053.14] like a
[2053.14 → 2054.42] regular
[2054.42 → 2055.24] oh okay
[2055.24 → 2055.62] that's why
[2055.62 → 2055.92] I bought
[2055.92 → 2056.14] these
[2056.14 → 2056.76] it was like
[2056.76 → 2057.36] one day
[2057.36 → 2058.38] I'm going to go
[2058.38 → 2059.16] face first
[2059.16 → 2059.74] into a door
[2059.74 → 2060.50] for no reason
[2060.50 → 2061.70] all right
[2061.70 → 2062.24] we have all
[2062.24 → 2063.22] definitions for
[2063.22 → 2063.84] oobleck
[2063.84 → 2064.70] and this round
[2064.70 → 2065.64] will be a little
[2065.64 → 2066.18] different from the
[2066.18 → 2066.80] rest because
[2066.80 → 2067.82] two of our
[2067.82 → 2068.28] contestants
[2068.28 → 2069.36] actually got the
[2069.36 → 2069.90] correct
[2069.90 → 2070.74] definition
[2070.74 → 2072.36] for oobleck
[2072.36 → 2072.98] three points
[2072.98 → 2073.48] awarded to
[2073.48 → 2074.76] angelica and
[2074.76 → 2075.92] john Henry
[2075.92 → 2077.12] you guys both
[2077.12 → 2077.74] know what
[2077.74 → 2078.32] oobleck is
[2078.32 → 2080.04] the rest of us
[2080.04 → 2081.76] will have to
[2081.76 → 2082.42] find out
[2082.42 → 2082.96] so
[2082.96 → 2084.90] we'll actually
[2084.90 → 2085.52] only have four
[2085.52 → 2086.06] definitions
[2086.06 → 2087.42] since those two
[2087.42 → 2087.90] were the correct
[2087.90 → 2088.58] definition they
[2088.58 → 2089.44] merge down onto
[2089.44 → 2090.04] the real one
[2090.04 → 2090.82] and we start
[2090.82 → 2091.34] with
[2091.34 → 2092.18] oobleck
[2092.18 → 2092.88] a non
[2092.88 → 2093.92] newtonian fluid
[2093.92 → 2095.26] that acts as
[2095.26 → 2095.90] both a liquid
[2095.90 → 2096.82] and solid
[2096.82 → 2097.62] under stress
[2097.62 → 2099.24] number two
[2099.24 → 2100.50] oobleck
[2100.50 → 2101.56] similar to an
[2101.56 → 2101.96] umlaut
[2101.96 → 2102.56] the oobleck
[2102.56 → 2103.10] is used to
[2103.10 → 2103.64] indicate the
[2103.64 → 2104.44] pronunciation of
[2104.44 → 2104.80] a word
[2104.80 → 2106.38] number three
[2106.38 → 2106.98] a piece of
[2106.98 → 2108.10] communication network
[2108.10 → 2108.94] that filters some
[2108.94 → 2109.72] data while setting
[2109.72 → 2110.64] aside others for
[2110.64 → 2111.46] future dispatch
[2111.46 → 2112.72] and number four
[2112.72 → 2113.64] a gritty adhesive
[2113.64 → 2114.58] formed by mixing
[2114.58 → 2115.56] sand water and
[2115.56 → 2116.10] epoxy
[2116.10 → 2118.12] so four definitions
[2118.12 → 2118.78] of oobleck
[2118.78 → 2119.50] one of those is
[2119.50 → 2120.08] correct
[2120.08 → 2121.04] angelica and john
[2121.04 → 2121.82] Henry sit this
[2121.82 → 2122.58] round out since
[2122.58 → 2123.14] they already know
[2123.14 → 2124.08] what it is
[2124.08 → 2125.76] and BMC gets
[2125.76 → 2126.68] to pick first
[2126.68 → 2128.32] first one
[2128.32 → 2130.34] first one
[2130.34 → 2131.24] the non-newtonian
[2131.24 → 2131.70] fluid
[2131.70 → 2132.24] okay
[2132.24 → 2133.48] BMC
[2133.48 → 2134.04] you said it
[2134.04 → 2134.22] funny
[2134.22 → 2134.84] is there
[2134.84 → 2135.92] we go
[2135.92 → 2136.54] to Adam
[2136.54 → 2138.28] it is funny
[2138.28 → 2139.38] what's the last
[2139.38 → 2139.80] one again
[2139.80 → 2140.68] the gritty
[2140.68 → 2141.20] substance
[2141.20 → 2141.74] a gritty
[2141.74 → 2142.42] adhesive formed
[2142.42 → 2142.82] by mixing
[2142.82 → 2143.52] sand water
[2143.52 → 2144.16] and epoxy
[2144.16 → 2145.08] oh yeah
[2145.08 → 2145.46] that's it
[2145.46 → 2146.42] that's it
[2146.42 → 2147.02] Adam takes
[2147.02 → 2147.70] that one
[2147.70 → 2148.80] we go now
[2148.80 → 2149.32] to
[2149.32 → 2150.76] Matthew
[2150.76 → 2151.92] so I heard
[2151.92 → 2152.62] the first one
[2152.62 → 2154.08] was a non-newtonian
[2154.08 → 2155.08] something or other
[2155.08 → 2155.68] correct
[2155.68 → 2156.54] the last one
[2156.54 → 2156.90] was gritty
[2156.90 → 2157.28] adhesive
[2157.28 → 2157.78] what were the
[2157.78 → 2158.20] second two
[2158.20 → 2158.74] the middle two
[2158.74 → 2159.30] the middle two
[2159.30 → 2160.08] was similar to
[2160.08 → 2160.74] an umlaut
[2160.74 → 2162.68] an oobleck is used
[2162.68 → 2163.26] to indicate the
[2163.26 → 2164.22] pronunciation of a word
[2164.22 → 2164.92] and the other
[2164.92 → 2165.64] middle one
[2165.64 → 2166.74] was a piece of a
[2166.74 → 2167.54] communication network
[2167.54 → 2168.52] that filters some data
[2168.52 → 2169.82] while setting aside
[2169.82 → 2171.48] other for future
[2171.48 → 2171.94] dispatch
[2171.94 → 2173.14] that one's spelled
[2173.14 → 2173.62] incorrectly
[2173.62 → 2174.66] there are some mistakes
[2174.66 → 2175.14] in that one
[2175.14 → 2175.60] so I'm going to
[2175.60 → 2176.38] pass on that one
[2176.38 → 2176.92] okay
[2176.92 → 2177.84] uh
[2177.84 → 2178.56] I'm thinking
[2178.56 → 2179.16] one
[2179.16 → 2181.48] one
[2181.48 → 2182.40] one sounds
[2182.40 → 2183.48] the best
[2183.48 → 2183.86] here
[2183.86 → 2185.86] and I don't
[2185.86 → 2186.70] know if it
[2186.70 → 2187.32] if this group
[2187.32 → 2187.70] would say
[2187.70 → 2188.12] something like
[2188.12 → 2188.88] non-newtonian
[2188.88 → 2190.10] so I think
[2190.10 → 2190.56] I'm gonna lock
[2190.56 → 2191.18] in for one
[2191.18 → 2191.66] actually
[2191.66 → 2192.30] okay
[2192.30 → 2194.84] so not only
[2194.84 → 2195.94] does he select
[2195.94 → 2196.76] number one
[2196.76 → 2197.46] he also disses
[2197.46 → 2197.94] everybody
[2197.94 → 2200.62] this group
[2200.62 → 2201.12] wouldn't say
[2201.12 → 2202.04] non-newtonian
[2202.04 → 2202.98] they are smart
[2202.98 → 2203.22] enough
[2203.22 → 2203.54] yeah
[2203.54 → 2206.72] but we knew
[2206.72 → 2207.66] what it was
[2207.66 → 2208.46] so
[2208.46 → 2209.38] that's a good
[2209.38 → 2209.86] point
[2209.86 → 2211.08] so angelica
[2211.08 → 2211.62] and john Henry
[2211.62 → 2212.40] already knew
[2212.40 → 2213.40] that
[2213.40 → 2215.00] oobleck
[2215.00 → 2216.20] was a non-newtonian
[2216.20 → 2217.14] fluid that acts
[2217.14 → 2217.78] as both a liquid
[2217.78 → 2218.50] and a solid
[2218.50 → 2220.18] under stress
[2220.18 → 2220.82] so
[2220.82 → 2222.40] BMC and
[2222.40 → 2222.78] Matthew
[2222.78 → 2223.74] each get two
[2223.74 → 2224.14] points
[2224.14 → 2225.28] for guessing
[2225.28 → 2225.88] it correctly
[2225.88 → 2226.64] did you guys
[2226.64 → 2227.54] not go to
[2227.54 → 2228.42] elementary school
[2228.42 → 2229.26] or
[2229.26 → 2231.20] like uh
[2231.20 → 2232.52] you guys don't
[2232.52 → 2233.26] know what this is
[2233.26 → 2233.88] I just skipped
[2233.88 → 2234.36] straight to
[2234.36 → 2234.96] uh
[2234.96 → 2235.64] I don't know
[2235.64 → 2236.34] how you know
[2236.34 → 2236.80] what it is
[2236.80 → 2237.22] so can you
[2237.22 → 2237.84] please explain
[2237.84 → 2238.28] see what
[2238.28 → 2238.70] contents
[2238.70 → 2239.04] we're all
[2239.04 → 2239.34] missing
[2239.34 → 2239.76] uh
[2239.76 → 2241.08] the cornstarch
[2241.08 → 2242.18] and water
[2242.18 → 2242.62] mixture
[2242.62 → 2243.34] that you can
[2243.34 → 2243.78] punch
[2243.78 → 2244.74] and this feels
[2244.74 → 2245.24] solid
[2245.24 → 2246.00] and then you
[2246.00 → 2246.52] hold it
[2246.52 → 2247.32] and it drips
[2247.32 → 2247.80] through your
[2247.80 → 2248.32] fingers
[2248.32 → 2249.64] I went outside
[2249.64 → 2250.18] as a kid
[2250.18 → 2250.50] I don't know
[2250.50 → 2250.72] what you're
[2250.72 → 2251.30] talking about
[2251.30 → 2255.44] so this is also
[2255.44 → 2255.90] a commercial
[2255.90 → 2256.68] product I guess
[2256.68 → 2257.28] when angelica
[2257.28 → 2257.74] you were talking
[2257.74 → 2258.32] about the
[2258.32 → 2259.10] commercial product
[2259.10 → 2259.38] right
[2259.38 → 2260.34] yeah
[2260.34 → 2260.98] yeah
[2260.98 → 2261.58] an obey gooey
[2261.58 → 2262.98] she called it
[2262.98 → 2263.50] an obey gooey
[2263.50 → 2264.02] kids toy
[2264.02 → 2264.68] like slime
[2264.68 → 2266.16] and with specks
[2266.16 → 2266.92] in it
[2266.92 → 2267.62] which is true
[2267.62 → 2268.18] never heard
[2268.18 → 2268.60] this in my
[2268.60 → 2268.92] life
[2268.92 → 2269.56] i actually
[2269.56 → 2270.00] hadn't heard
[2270.00 → 2270.18] it in a
[2270.18 → 2270.52] oobleck
[2270.52 → 2270.78] either
[2270.78 → 2271.42] and so
[2271.42 → 2272.88] I'm very
[2272.88 → 2273.20] impressed
[2273.20 → 2273.48] by you
[2273.48 → 2273.70] two
[2273.70 → 2274.50] oh
[2274.50 → 2274.92] we say
[2274.92 → 2275.28] me and
[2275.28 → 2275.48] john
[2275.48 → 2275.84] we're just
[2275.84 → 2276.42] slimy
[2276.42 → 2277.32] that's all
[2277.32 → 2277.44] right
[2277.44 → 2278.84] and then Adam
[2278.84 → 2279.66] selected the gritty
[2279.66 → 2280.62] adhesive formed by
[2280.62 → 2281.38] mixing sand water
[2281.38 → 2281.88] and epoxy
[2281.88 → 2282.30] and that's
[2282.30 → 2282.98] Matthew so he
[2282.98 → 2283.46] gets another
[2283.46 → 2284.20] point so three
[2284.20 → 2285.00] points for you
[2285.00 → 2285.52] three points
[2285.52 → 2286.20] for angelica
[2286.20 → 2287.04] two for BMC
[2287.04 → 2287.66] three for john
[2287.66 → 2288.04] Henry
[2288.04 → 2289.10] Adam and i
[2289.10 → 2289.58] shut out
[2289.58 → 2290.36] this round
[2290.36 → 2291.98] so after
[2291.98 → 2292.78] three rounds
[2292.78 → 2293.84] tied for
[2293.84 → 2294.64] first is
[2294.64 → 2295.44] Matthew and
[2295.44 → 2296.10] BMC with
[2296.10 → 2296.94] six tied for
[2296.94 → 2297.94] second is
[2297.94 → 2298.82] angelica john
[2298.82 → 2299.48] Henry myself
[2299.48 → 2300.02] with four
[2300.02 → 2301.94] and we leave
[2301.94 → 2302.44] Adam where he
[2302.44 → 2303.26] was previously
[2303.26 → 2305.26] let's move
[2305.26 → 2305.96] now to
[2305.96 → 2306.88] round four
[2306.88 → 2310.48] I have faith
[2310.48 → 2311.00] in you
[2311.00 → 2312.26] I do not
[2312.26 → 2313.44] I do not
[2313.44 → 2315.12] there's a
[2315.12 → 2315.64] strategy
[2315.64 → 2316.72] that's right
[2316.72 → 2317.14] he has a
[2317.14 → 2317.54] strategy
[2317.54 → 2319.30] this round is
[2319.30 → 2319.68] a little different
[2319.68 → 2320.20] we call this
[2320.20 → 2320.98] give it a
[2320.98 → 2321.50] good
[2321.50 → 2322.54] give it a
[2322.54 → 2322.88] good
[2322.88 → 2324.82] where i
[2324.82 → 2325.16] went out
[2325.16 → 2325.72] to google
[2325.72 → 2326.24] in an
[2326.24 → 2326.96] incognito
[2326.96 → 2327.52] browser
[2327.52 → 2328.26] window
[2328.26 → 2328.76] so no
[2328.76 → 2329.44] personalization
[2329.44 → 2330.16] and i
[2330.16 → 2330.60] started
[2330.60 → 2331.50] giving it
[2331.50 → 2332.00] a good
[2332.00 → 2333.02] then i
[2333.02 → 2333.44] stopped
[2333.44 → 2334.02] and checked
[2334.02 → 2334.38] for the
[2334.38 → 2334.74] first
[2334.74 → 2335.60] autocomplete
[2335.60 → 2336.34] your job
[2336.34 → 2336.76] is to
[2336.76 → 2337.24] come up
[2337.24 → 2337.68] with what
[2337.68 → 2338.12] the first
[2338.12 → 2338.76] autocomplete
[2338.76 → 2339.50] was or
[2339.50 → 2340.06] ostensibly
[2340.06 → 2341.10] what you
[2341.10 → 2341.66] you can
[2341.66 → 2342.20] trick other
[2342.20 → 2342.92] people into
[2342.92 → 2343.32] thinking that
[2343.32 → 2343.76] it was
[2343.76 → 2345.06] the query
[2345.06 → 2345.42] that i
[2345.42 → 2345.88] queried
[2345.88 → 2347.38] was when
[2347.38 → 2348.60] does the
[2348.60 → 2349.28] I typed
[2349.28 → 2349.68] windows
[2349.68 → 2350.12] the
[2350.12 → 2351.22] and then
[2351.22 → 2351.96] I stopped
[2351.96 → 2353.40] what do
[2353.40 → 2353.76] you think
[2353.76 → 2354.20] google
[2354.20 → 2355.40] suggested
[2355.40 → 2355.82] as the
[2355.82 → 2356.16] number one
[2356.16 → 2356.66] autocomplete
[2356.66 → 2357.20] please
[2357.20 → 2358.04] submit to
[2358.04 → 2358.56] me your
[2358.56 → 2359.28] autocompletes
[2359.28 → 2359.60] now
[2359.60 → 2360.84] did you do
[2360.84 → 2361.56] this
[2361.56 → 2361.94] search
[2361.94 → 2362.82] or this
[2362.82 → 2363.62] autocomplete
[2363.62 → 2365.24] yourself
[2365.24 → 2365.64] on your
[2365.64 → 2366.04] machine
[2366.04 → 2367.06] incognito
[2367.06 → 2367.46] window
[2367.46 → 2368.96] a VPN
[2368.96 → 2369.84] and it
[2369.84 → 2370.82] can you put
[2370.82 → 2371.22] the text
[2371.22 → 2371.68] that you put
[2371.68 → 2372.28] in the
[2372.28 → 2372.78] channel
[2372.78 → 2373.28] for sure
[2373.28 → 2374.68] Adam was the
[2374.68 → 2375.18] first one in
[2375.18 → 2375.58] this time
[2375.58 → 2376.42] so he's
[2376.42 → 2377.62] oh that's
[2377.62 → 2377.88] because I know
[2377.88 → 2378.30] the answer
[2378.30 → 2379.00] he's changing
[2379.00 → 2379.34] the things
[2379.34 → 2379.74] around
[2379.74 → 2381.04] how often
[2381.04 → 2381.62] do you
[2381.62 → 2382.30] how often
[2382.30 → 2382.88] do you
[2382.88 → 2383.54] write that
[2383.54 → 2384.24] into google
[2384.24 → 2384.82] to know the
[2384.82 → 2385.58] answer to that
[2385.58 → 2386.68] well this one's
[2386.68 → 2387.12] obvious
[2387.12 → 2388.38] well the cool
[2388.38 → 2388.90] thing about it
[2388.90 → 2390.24] is its kind
[2390.24 → 2390.70] of a proxy
[2390.70 → 2391.52] for the human
[2391.52 → 2392.16] condition is it
[2392.16 → 2393.38] not like what
[2393.38 → 2394.02] were people
[2394.02 → 2394.86] asking it
[2394.86 → 2396.12] what do people
[2396.12 → 2396.86] wonder when
[2396.86 → 2397.40] does the
[2397.40 → 2398.58] when does the
[2398.58 → 2399.60] fox say
[2399.60 → 2400.16] I was gonna
[2400.16 → 2400.64] I was thinking
[2400.64 → 2401.04] that too
[2401.04 → 2401.46] that's what
[2401.46 → 2401.78] does the
[2401.78 → 2402.24] fox say
[2402.24 → 2403.24] very close
[2403.24 → 2403.46] though
[2403.46 → 2404.08] oh dang
[2404.08 → 2404.90] that's what
[2404.90 → 2405.28] I said
[2405.28 → 2406.30] and did you
[2406.30 → 2406.66] do this
[2406.66 → 2407.00] today
[2407.00 → 2408.06] this search
[2408.06 → 2408.76] such a
[2408.76 → 2408.98] search
[2408.98 → 2409.32] I don't
[2409.32 → 2409.80] answer any
[2409.80 → 2410.00] further
[2410.00 → 2410.44] questions
[2410.44 → 2411.28] okay that's
[2411.28 → 2411.52] fair
[2411.52 → 2413.22] that's very
[2413.22 → 2414.04] relevant though
[2414.04 → 2414.92] it is really
[2414.92 → 2415.30] relevant
[2415.30 → 2416.80] what does the
[2416.80 → 2417.24] fox say
[2417.24 → 2418.52] no when you
[2418.52 → 2419.40] when you did
[2419.40 → 2419.50] it
[2419.50 → 2420.32] you did this
[2420.32 → 2423.24] yeah like if it was
[2423.24 → 2424.18] like six years ago
[2424.18 → 2425.58] he's super different
[2425.58 → 2426.88] he prepared for this
[2426.88 → 2427.74] show a long time ago
[2427.74 → 2428.98] he's been doing this
[2428.98 → 2430.28] yeah he planned this
[2430.28 → 2430.98] where did he come
[2430.98 → 2431.84] from where did he go
[2431.84 → 2439.64] VMC's here for our
[2439.64 → 2440.30] sound if you're
[2440.30 → 2441.14] listening I need
[2441.14 → 2442.56] jobs thank you
[2442.56 → 2444.52] I'm here for your
[2444.52 → 2445.10] sound needs
[2445.10 → 2447.38] it's kind of more
[2447.38 → 2448.74] fun when VMC's here
[2448.74 → 2449.56] than it even is when
[2449.56 → 2449.90] he's not
[2449.90 → 2451.62] I'm having fun
[2451.62 → 2452.40] that with he's here
[2452.40 → 2453.44] That's a... oh god.
[2454.82 → 2460.16] Alright, we're just down to one person.
[2460.46 → 2460.94] Not in.
[2461.16 → 2461.90] Buy my music!
[2462.72 → 2463.90] Buy my music!
[2464.48 → 2465.50] Buy my music!
[2466.04 → 2467.16] That's a good soundbite.
[2467.72 → 2470.92] Next time we release an album, we'll just play that one.
[2470.92 → 2471.24] At the end.
[2471.62 → 2472.22] On repeat.
[2473.14 → 2473.78] At the beginning.
[2474.58 → 2475.64] Yeah, yeah, yeah, yeah, yeah, do it.
[2477.26 → 2479.68] You chose phrases that have like...
[2479.68 → 2480.12] I don't know.
[2480.86 → 2482.26] They don't have much...
[2482.26 → 2482.70] Yeah!
[2484.52 → 2485.54] That's a good one, right?
[2486.40 → 2486.84] Yeah.
[2486.86 → 2487.24] Yeah, okay.
[2487.44 → 2488.18] I'm on board with that.
[2489.06 → 2489.50] Okay.
[2490.40 → 2494.48] Six potential Google auto-completes for when does the...
[2494.48 → 2497.80] Number one, when does the current administration end?
[2499.46 → 2501.92] Number two, when does the sun rise?
[2502.96 → 2505.62] Number three, when does the time change?
[2506.48 → 2508.86] Number four, when does the stock market open?
[2509.38 → 2511.70] Number five, when does the sun set near me?
[2512.26 → 2514.66] And number six, when does the world end?
[2515.88 → 2516.36] Existential.
[2516.80 → 2517.30] All right.
[2517.44 → 2518.90] Six potential, when does those?
[2519.86 → 2520.48] John Henry.
[2521.28 → 2523.48] So going through these...
[2524.14 → 2525.60] What was the first one?
[2525.68 → 2525.94] Current?
[2526.94 → 2528.18] The current administration.
[2528.18 → 2529.68] Oh, that...
[2529.68 → 2531.06] Yeah, that's...
[2531.06 → 2532.66] I'm certainly wondering that.
[2533.62 → 2535.76] But I don't know.
[2535.82 → 2538.76] I don't know if Google would go there.
[2539.14 → 2539.88] Maybe, maybe not.
[2539.94 → 2540.42] I'm not sure.
[2541.02 → 2541.60] Oh, it would.
[2541.94 → 2542.36] It would?
[2542.70 → 2543.04] Oh, yeah.
[2543.04 → 2544.90] But also, is this global Google, though?
[2544.98 → 2546.40] Or is this US-based?
[2546.44 → 2547.50] This is Jared's...
[2547.50 → 2548.50] Well...
[2548.50 → 2549.50] Incognito.
[2549.50 → 2551.40] Jared's IP address in Omaha or whatever.
[2551.40 → 2552.96] Yeah, I didn't VPN very far.
[2554.10 → 2555.14] Sunrise is plausible.
[2556.00 → 2557.12] They're all plausible, actually.
[2557.52 → 2558.24] Stock market.
[2558.96 → 2559.68] Sunset near me.
[2559.76 → 2560.62] I like the near me.
[2560.62 → 2563.64] Does that mean the sun sets, like, as close to you as possible?
[2563.94 → 2564.14] Or...
[2564.14 → 2564.52] I don't know.
[2564.92 → 2568.50] Google just always, like, adds that in those searches.
[2568.50 → 2571.34] And so that's what made me think...
[2571.34 → 2572.60] I'm going with number five.
[2573.02 → 2574.08] Number five.
[2574.16 → 2575.96] When is the sunset near me?
[2576.06 → 2577.18] Okay, Adam, what do you think?
[2577.64 → 2578.72] I haven't been paying attention.
[2578.90 → 2579.14] Sorry.
[2582.72 → 2583.72] What are we doing here?
[2583.72 → 2585.28] Well, the scoreboard accurately reflects that.
[2585.40 → 2585.76] Yes.
[2585.76 → 2587.16] What are we doing here?
[2587.56 → 2589.00] Are you still watching SpongeBob?
[2590.16 → 2591.40] Yeah, I am, actually.
[2593.46 → 2594.30] Patrick's so awesome.
[2595.08 → 2595.98] Let's see here.
[2596.74 → 2598.24] There are two that are near me.
[2598.24 → 2599.06] Which ones are those?
[2599.16 → 2599.96] Read those to me, please.
[2600.58 → 2602.40] Well, one was, when does the sunset near me?
[2602.46 → 2603.24] That's number five.
[2603.36 → 2606.78] And then the other one was, when does the sun rise but does not say near me?
[2607.52 → 2609.38] Number five is the only one that says near me.
[2609.66 → 2610.98] That's a Mandela fact, I think, right?
[2611.46 → 2613.32] I remember both of them saying near me.
[2614.28 → 2617.00] No, we would all have to remember it.
[2617.02 → 2618.32] Otherwise, it's just you being wrong.
[2622.50 → 2623.32] Let's see here.
[2623.32 → 2624.20] What was the first one again?
[2624.56 → 2627.90] The first one was, when does the current administration end?
[2628.24 → 2629.26] We want number two.
[2630.60 → 2632.30] You think number two is the right answer?
[2632.72 → 2633.82] When does the sun rise?
[2635.08 → 2635.62] Near me?
[2636.38 → 2636.72] No.
[2640.46 → 2642.40] That could be your additional add-on.
[2642.66 → 2642.98] Yeah.
[2643.70 → 2646.44] Would it change your answer if it said near me on it?
[2646.78 → 2649.72] I feel like a near me is probably accurate, but I'm not going to go that route.
[2650.50 → 2651.22] I'm going to go with number two.
[2651.32 → 2652.12] Locking it in tight.
[2652.58 → 2652.84] Tight.
[2653.16 → 2653.64] So tight.
[2653.72 → 2654.36] Locking in.
[2654.66 → 2655.82] When does the sun rise?
[2655.82 → 2656.12] Okay.
[2656.46 → 2656.82] Angelica.
[2657.16 → 2660.86] I don't think it's the administration one, and I don't think it's the world end one.
[2661.24 → 2661.52] Okay.
[2661.66 → 2662.60] So you're down to four then.
[2662.84 → 2667.32] So I've got the two sun ones and the time zone stock market.
[2667.62 → 2670.32] I don't think the stock market is broadly applicable to the world.
[2670.44 → 2672.38] So I don't think that many people will Google that.
[2674.24 → 2675.86] Famous last words, if it is that.
[2677.62 → 2678.98] Going on what I would care about.
[2678.98 → 2680.84] I care about when the sun rises and sets.
[2681.20 → 2685.66] So I'm also on the line of thinking of, is there near me?
[2686.44 → 2686.84] Couldn't it be?
[2687.72 → 2689.98] I think last time I locked in with Adam, it was good.
[2690.08 → 2690.80] So I'm going to lock in.
[2691.46 → 2692.30] You're going with Adam.
[2692.94 → 2693.24] Okay.
[2693.24 → 2694.54] When does the sun rise?
[2694.64 → 2696.40] You're sympathetically incorrect.
[2697.18 → 2698.72] I put my faith in you, Adam.
[2698.98 → 2699.56] So I'm like.
[2699.84 → 2700.70] Oh, you know.
[2701.30 → 2701.86] All right.
[2702.72 → 2703.08] Matt.
[2703.08 → 2706.62] Can you give me the quick rundown of all of them again?
[2707.10 → 2708.56] Number one is the current administration.
[2708.96 → 2710.60] Number two is the sun rising.
[2710.80 → 2712.28] Number three is time changing.
[2712.58 → 2714.66] Number four is the market opening.
[2714.94 → 2717.16] Number five is the sun setting near me.
[2717.56 → 2718.88] And number six is the world ending.
[2719.38 → 2719.74] Okay.
[2719.94 → 2722.64] I haven't used Google in a very long time.
[2723.44 → 2725.42] So I don't know what Google even suggests anymore.
[2726.60 → 2729.70] I've also never seen a suggestion ever say near me.
[2729.70 → 2731.46] So I think that one's out for me.
[2731.68 → 2732.54] Yeah, that's not true.
[2732.54 → 2733.50] Nor am I, honestly.
[2733.60 → 2735.50] I also don't autocorrect much.
[2735.52 → 2735.70] Yeah.
[2735.70 → 2737.64] I've never seen a near me thing pop up.
[2738.02 → 2739.06] It already knows where you're at.
[2739.78 → 2740.06] It's context.
[2740.06 → 2740.26] Right.
[2740.34 → 2740.70] Exactly.
[2741.32 → 2742.02] It already knows.
[2742.14 → 2742.76] It already knows where you are.
[2743.12 → 2745.06] Near me is our specific nouns.
[2745.20 → 2747.34] Like, where is the nearest gas station?
[2747.58 → 2747.98] Near me.
[2748.56 → 2748.74] Yeah.
[2748.74 → 2752.22] I think if you had started with that, then the near me would have autocorrect.
[2752.24 → 2755.48] Well, sunrise and sunset are geographically dependent, right?
[2755.58 → 2757.66] It sets a different time, different places.
[2758.04 → 2758.48] Yeah.
[2758.54 → 2762.18] But like, I feel like Google, I feel like Google has evolved that it knows my geo.
[2762.82 → 2763.08] All right.
[2763.08 → 2763.78] What are you thinking, Matthew?
[2764.24 → 2764.58] All right.
[2764.64 → 2772.26] So if you're doing this from Omaha, I'm torn between the sunrise and the stock market,
[2772.34 → 2772.70] honestly.
[2772.94 → 2775.24] But I think we have, we've over indexed on the sunrise.
[2775.40 → 2779.28] So I think I'm going to go the other way and do the stock market opening.
[2779.60 → 2780.56] He's playing the spread.
[2780.70 → 2780.98] Okay.
[2781.24 → 2782.04] When the world ends, huh?
[2782.12 → 2782.44] Okay.
[2782.66 → 2783.10] Good job.
[2783.16 → 2783.66] You're going to lose.
[2783.66 → 2785.76] That's a good, that's a good choice.
[2785.92 → 2786.50] When the world ends.
[2786.60 → 2787.22] It's not right.
[2787.38 → 2787.86] Is that what you picked?
[2788.42 → 2790.12] No, he picked the stock market.
[2790.56 → 2791.98] Oh, I thought he said, where are the wind ends?
[2792.08 → 2793.46] I mean, come on, that's the right answer.
[2793.64 → 2794.16] Come on.
[2794.20 → 2794.68] That's the right answer.
[2794.86 → 2796.34] Lastly, BMC.
[2796.34 → 2797.24] What do you think?
[2797.58 → 2797.96] World end?
[2799.58 → 2800.28] Oh, he's not.
[2802.18 → 2804.04] I wonder who wrote that one.
[2804.20 → 2805.00] End of days.
[2805.80 → 2806.46] Fan finger.
[2806.56 → 2807.28] What are those things called?
[2807.42 → 2808.10] Giant hand?
[2808.10 → 2811.58] I got this in 2020, and it's going to be useful sometime.
[2811.58 → 2814.24] Eventually it will apply.
[2814.24 → 2815.04] Every five years.
[2815.18 → 2815.54] Useful.
[2816.30 → 2816.72] All right.
[2816.80 → 2819.54] So BMC picks the world ending.
[2820.10 → 2825.36] Adam was very excited that you were interested in the world ending because Adam wrote the world ending.
[2825.46 → 2826.48] So one point for Adam.
[2826.96 → 2828.46] When the world ends.
[2829.02 → 2830.18] See, I had faith in you, Adam.
[2830.52 → 2831.58] I would keep doing that.
[2831.96 → 2832.46] It's amazing.
[2833.54 → 2836.76] John Henry was interested in the sun setting near him.
[2838.34 → 2840.16] And nobody else was interested in that one.
[2840.26 → 2841.28] It happened to be his own.
[2841.28 → 2842.62] So he gets zero points.
[2843.62 → 2846.38] Couldn't quite bring people along for the ride.
[2846.58 → 2847.78] He's trying to lobby that.
[2848.02 → 2848.30] Yeah.
[2848.34 → 2849.16] It almost worked.
[2849.30 → 2851.82] But then they were all using logic and stuff.
[2852.74 → 2853.32] Let's see.
[2853.40 → 2853.98] What else?
[2854.42 → 2855.16] I see that.
[2855.32 → 2857.04] I see the near me all the time.
[2857.04 → 2857.48] Oh, do you?
[2857.76 → 2858.00] Yeah.
[2858.10 → 2859.28] No, you guys don't.
[2859.46 → 2859.82] No.
[2859.92 → 2860.50] I don't use me.
[2860.88 → 2861.24] Yeah.
[2861.30 → 2863.38] I guess I don't really think about the autocomplete much.
[2863.56 → 2868.72] Well, I mean, like in maps, maybe, you know, when I'm like looking for like a Chick-fil-A near me.
[2868.90 → 2869.46] Like search nearby.
[2869.46 → 2869.70] Yeah.
[2870.06 → 2870.34] Yeah.
[2870.34 → 2871.22] That's where I see the near me.
[2871.46 → 2872.66] That's like a button though.
[2872.80 → 2873.88] You can press near me.
[2874.14 → 2874.50] Right.
[2874.76 → 2875.90] Do the GPS thing.
[2875.90 → 2880.46] I saw a dentist that was named something like near me for SEO reasons.
[2880.46 → 2880.60] Smart.
[2880.82 → 2881.48] What was his last name?
[2882.26 → 2882.82] Near me.
[2883.00 → 2883.78] It was his last name.
[2883.80 → 2884.36] Dr. Near me.
[2884.44 → 2885.26] Dr. Near me.
[2885.68 → 2886.76] Paging Dr. Near me.
[2887.24 → 2889.22] If I was a doctor, I'd name myself on the plane.
[2889.42 → 2890.76] You know, is there a doctor on the plane?
[2890.80 → 2891.88] I'd just get hit every time.
[2893.34 → 2896.46] The Sun Rising was also popular with Adam and Angelica.
[2896.82 → 2898.26] Adam picked it because he thought it was right.
[2898.26 → 2901.50] Angelica picked it because she thought she could fool more people, I guess, because that's
[2901.50 → 2901.88] hers.
[2902.88 → 2903.76] It worked.
[2904.14 → 2904.98] She gets one point.
[2905.30 → 2907.64] You reduce the addition to others.
[2907.84 → 2910.20] See, I had faith in you giving me points, Adam.
[2910.68 → 2911.58] I was doing it on purpose.
[2911.58 → 2917.94] I was, you know, I felt the brainwaves coming through like a, like an oblique or what the
[2917.94 → 2918.94] heck is that thing called?
[2919.20 → 2920.62] Like an oblique.
[2920.86 → 2921.16] Oblique.
[2921.74 → 2922.52] Like an oblique.
[2923.10 → 2923.96] A jaggy oblique.
[2924.84 → 2926.14] Nobody picked the time change.
[2926.22 → 2926.96] That was Matthews.
[2927.00 → 2928.88] Nobody picked the current administration ending.
[2929.18 → 2929.92] That was BMCs.
[2930.08 → 2931.98] Also, there's a time limit on it, right?
[2932.06 → 2933.62] So people don't ask that question.
[2933.78 → 2936.56] It's four years minus whatever a hundred days.
[2936.72 → 2939.60] No, it's going to be like 12 years if he has anything to do with it.
[2939.60 → 2943.38] Well, yeah, we'll see how many administrations there are.
[2943.94 → 2949.14] And then Matthew picked the stock market, which was the actual answer, Angelica.
[2949.26 → 2950.68] So you need to eat some crow here.
[2950.68 → 2955.70] When does the stock market open is the number one autocomplete for when does the.
[2955.96 → 2956.58] Oh, no.
[2957.08 → 2957.98] Can I check this now?
[2958.02 → 2963.18] Here's the number two, three and four and five autocompletes.
[2963.26 → 2964.90] When does the time change?
[2965.32 → 2968.10] So, Matthew, you actually had the second-best autocomplete.
[2968.10 → 2969.64] I've Googled that before.
[2969.82 → 2971.02] I got where I've searched that before.
[2971.48 → 2975.02] You get zero points, but you do get two for getting it right.
[2975.16 → 2975.92] So good job there.
[2976.58 → 2978.84] When does the WNBA season start?
[2979.26 → 2983.26] So shout out to Caitlin Clark for, you know, probably affecting those results.
[2984.14 → 2985.64] WNBA very popular all of a sudden.
[2985.76 → 2987.54] And then when do the NBA playoffs start?
[2987.64 → 2990.18] Of course, that's their going on right now.
[2990.28 → 2993.58] And then the last one, number five was when does the sun set?
[2994.20 → 2995.20] No near me, though, John.
[2995.20 → 2997.72] So you're close.
[2998.38 → 3002.54] But I only care about near me because you're a narcissist.
[3002.98 → 3006.62] It's rolling, you know, it's something somewhere all the time.
[3006.80 → 3007.04] Right.
[3007.42 → 3007.92] That's fair.
[3007.98 → 3012.02] I think I tried this out right now after submitting.
[3012.32 → 3015.18] I think it's objective to where you are, subjective to where you are.
[3015.20 → 3018.60] Because my top one is when does the Minecraft movie come out?
[3018.88 → 3019.74] Are you logged in?
[3019.98 → 3021.00] That is my top.
[3021.10 → 3022.62] I'm incognito mode.
[3022.62 → 3026.34] And I put when does the Minecraft movie.
[3026.56 → 3026.76] Okay.
[3026.80 → 3029.28] Everybody right now go incognito and do a search.
[3029.94 → 3033.48] And John Henry and I are very closely approximate to each other.
[3033.60 → 3034.92] So we'll see if he gets what I got.
[3035.04 → 3036.58] When does the Minecraft movie come out?
[3036.60 → 3037.96] And then when does the time change?
[3038.02 → 3039.28] And then when does the time change?
[3039.54 → 3039.94] 2025.
[3040.44 → 3041.54] My three options.
[3041.54 → 3043.32] I pretty much have that same thing.
[3043.32 → 3043.56] Really?
[3043.76 → 3043.92] Yeah.
[3044.02 → 3044.16] Yeah.
[3044.26 → 3045.84] My top search is when does the world end?
[3045.94 → 3046.14] Jeez.
[3048.70 → 3051.10] Mine is when does the sun rise?
[3052.10 → 3054.42] And then number two is, yeah.
[3054.42 → 3059.68] And then number two is, when does the MLB season start near me?
[3060.10 → 3061.70] I don't know how that got into it.
[3063.02 → 3063.96] Near me.
[3064.72 → 3067.52] That's spectacular because it starts at the same time everywhere.
[3067.74 → 3071.52] But maybe they just, maybe Google fingerprinted me somehow.
[3072.64 → 3073.88] Even though I'm incognito.
[3074.02 → 3076.20] And it's like, this guy wants to know when the stock market opens.
[3076.76 → 3078.90] Even though I've never searched that in my life.
[3079.66 → 3081.50] You did mention Slack shares and stuff.
[3081.50 → 3082.18] So, you know.
[3083.10 → 3083.64] It knows.
[3084.42 → 3085.56] You have stocks in your mind.
[3085.56 → 3087.12] I do know what the stock market is.
[3087.28 → 3088.00] This is true.
[3088.26 → 3089.14] I do know what it is.
[3089.70 → 3092.02] I feel like mine was the number one on Jordan's browser.
[3092.12 → 3094.02] So, I should at least get like a half point.
[3094.38 → 3094.82] Come on.
[3095.12 → 3096.22] It's integers only.
[3096.30 → 3096.64] I'm sorry.
[3096.82 → 3097.18] Hold on.
[3097.22 → 3098.36] John Henry's doing another one now.
[3098.80 → 3100.24] Different from my browser?
[3100.58 → 3101.48] No, it's not, John.
[3101.62 → 3102.36] It's cracked.
[3102.54 → 3105.82] But then when I go to Google.com and the autocomplete, that's different.
[3105.94 → 3106.68] Well, that's what I did.
[3106.94 → 3107.66] Google.com.
[3107.76 → 3109.66] I think the browser is definitely cracked.
[3109.66 → 3112.76] I think the browser address bar is probably using your stuff there.
[3113.66 → 3114.06] Anyway.
[3114.42 → 3115.34] I'm going to go see Minecraft.
[3118.64 → 3119.26] All right.
[3119.32 → 3126.02] So, after four rounds now, we have Matthew in a commanding lead with eight, followed by
[3126.02 → 3128.32] BMC with six, Angelica with five.
[3129.06 → 3133.40] John Henry and I are tied with four, and Adam's on the board now with one.
[3133.78 → 3134.52] Half a point.
[3135.20 → 3136.18] How many points, BMC?
[3137.18 → 3138.42] This many points for Adam.
[3139.20 → 3140.06] You have the finger.
[3140.06 → 3140.54] That's right.
[3140.54 → 3140.84] That's right.
[3140.98 → 3141.22] Yes.
[3141.56 → 3141.92] BMC.
[3142.50 → 3143.32] One finger.
[3146.62 → 3148.18] It's the right finger, at least.
[3148.70 → 3149.20] That's true.
[3149.50 → 3149.72] All right.
[3149.76 → 3151.12] We moved now to round five.
[3151.20 → 3152.70] This is a brand-new format.
[3152.86 → 3153.96] We've never done this one before.
[3153.96 → 3156.14] I call it weird flicks, but okay.
[3157.44 → 3163.94] Where I have gone out and found a weird old movie.
[3163.94 → 3171.20] And your job, I will give you the title and the date of the year that movie came out, and
[3171.20 → 3179.38] your job is to write the tagline or the synopsis, the one sentence synopsis of the movie, having
[3179.38 → 3182.38] no nothing but the title and the year it came out.
[3182.72 → 3183.48] Make sense?
[3184.38 → 3184.74] Mm-hmm.
[3184.74 → 3185.26] Yes.
[3185.26 → 3185.40] Okay.
[3186.12 → 3193.78] The movie, that's tagline you're going to write, was a 1924 flick called He Who Gets Slapped.
[3194.56 → 3196.26] He Who Gets Slapped.
[3196.34 → 3200.12] Now you are in charge of the actual synopsis.
[3200.32 → 3202.50] Please submit those to me whenever they're ready.
[3204.04 → 3204.70] Is it a talkie?
[3205.56 → 3207.90] Like those chips that are real spicy?
[3208.32 → 3208.62] No.
[3208.98 → 3214.24] Like a movie that had spoken, what's it, and they ate chips.
[3214.24 → 3216.12] Today we call those movies.
[3217.34 → 3220.20] Well, I haven't been on Earth for a while.
[3220.54 → 3221.74] I actually haven't seen it.
[3222.86 → 3225.38] I do know its title and the synopsis, though.
[3226.64 → 3227.48] It could have been a talkie.
[3227.56 → 3228.76] It's from 19 black and white.
[3229.50 → 3232.02] I tried to find one of the most obscure movies I could.
[3232.86 → 3234.44] Just hoping nobody has seen it.
[3235.26 → 3236.02] I think I did good.
[3236.36 → 3238.88] Are you going to be reading these in a cinematic voice, Jared?
[3240.26 → 3241.62] I feel like you should.
[3242.22 → 3243.24] Just fully commit.
[3243.24 → 3244.30] In a world.
[3244.96 → 3246.16] I don't have a Batman voice.
[3246.70 → 3247.18] What is it?
[3247.20 → 3247.92] Like a horror?
[3248.26 → 3249.96] So, dark and foreboding.
[3250.56 → 3252.10] I do try to be foreboding, though.
[3252.84 → 3254.16] Weird flicks, but okay.
[3254.54 → 3261.30] We have six potential synopses for the 1924 movie,
[3261.58 → 3262.88] He Who Gets Slapped.
[3263.74 → 3266.10] I will read you these now.
[3266.10 → 3267.26] Number one.
[3267.82 → 3272.32] Young George's mischievous childhood was punctuated by the sharp sting of a cane.
[3273.00 → 3277.24] Now an adult, he wakes to phantom slams and inexplicable cane-shaped bruises.
[3278.00 → 3278.78] Is it madness?
[3279.12 → 3279.72] His imagination?
[3280.46 → 3282.92] Or is his past literally leaving its mark?
[3283.82 → 3287.58] A chilling psychological thriller based on a true story of buried trauma
[3287.58 → 3289.70] and the repercussions of being a naughty boy.
[3292.50 → 3293.00] Okay.
[3293.12 → 3293.80] Number two.
[3294.50 → 3304.58] A high school student hopelessly searches for love while continuously facing rejection,
[3304.92 → 3305.64] often physical.
[3305.64 → 3308.50] Number three.
[3308.50 → 3308.56] Number three.
[3308.94 → 3314.34] A scared, straight, short film describing the purported hazards of befriending communists.
[3316.76 → 3317.84] Number four.
[3317.96 → 3324.28] A bitter clown endeavours to rescue the young woman he loves from the lecherous baron who once betrayed him.
[3324.80 → 3325.78] Number five.
[3325.90 → 3328.16] In a world where hand gestures have gone too far,
[3328.26 → 3333.58] a group of friends vows to change things and restore the old ways of simple handshakes and high-fives.
[3333.58 → 3335.84] And number six.
[3335.92 → 3340.90] When a man decides a raucous night out on the big city is more important than his life back home.
[3342.16 → 3346.58] Which of these six very well written, I might say, synopses,
[3347.02 → 3352.32] is actually the one for the 1924 flick, He Who Gets Slapped.
[3353.12 → 3354.50] We start with Adam.
[3355.32 → 3355.78] Oh gosh.
[3356.46 → 3360.58] I was too busy thinking about who's who and what's what.
[3360.92 → 3361.20] Yeah.
[3361.46 → 3362.28] I forgot to listen.
[3363.58 → 3366.68] You had one job, which was to listen.
[3367.40 → 3370.94] No, actually, I just need two and four in the last one, I think.
[3371.06 → 3372.28] So just two, four, and six.
[3372.38 → 3373.00] So half of them.
[3373.26 → 3373.38] Okay.
[3373.46 → 3373.90] Yeah, please.
[3374.66 → 3375.16] Number two.
[3375.24 → 3379.26] A high school student hopelessly searches for love while continuously facing rejection,
[3379.46 → 3380.22] often physical.
[3380.98 → 3381.22] Oof.
[3381.70 → 3386.82] Four was a bitter clown endeavours to rescue the young woman he loves from the lecherous baron who once betrayed him.
[3387.08 → 3387.62] That's Matt.
[3387.62 → 3394.24] And number six is when a man decides a raucous night out on the big city is more important than his life back home.
[3394.88 → 3396.18] Who do I want to get points to?
[3397.30 → 3397.48] Who?
[3397.70 → 3399.32] So you think you know who wrote each one?
[3399.58 → 3400.08] Oh, yeah.
[3400.26 → 3400.96] Oh, yeah.
[3401.48 → 3401.88] Pegged.
[3402.30 → 3403.46] Can I get some points for that?
[3403.84 → 3404.76] It could be.
[3404.86 → 3405.06] Yeah.
[3405.06 → 3405.78] Guess who?
[3405.88 → 3406.90] You can certainly guess who.
[3407.14 → 3407.48] With a twist.
[3407.70 → 3408.44] Yeah, that'd be a good game.
[3408.50 → 3409.76] I'm going to give BMC some points.
[3410.48 → 3411.70] Read number three again, please.
[3412.12 → 3416.50] A scared straight short film describing the purported hazards of befriending communists.
[3416.90 → 3417.96] Yeah, that's totally BMC.
[3421.16 → 3421.56] Okay.
[3422.08 → 3423.12] What was the clown one?
[3423.26 → 3424.10] That was number four?
[3424.34 → 3424.72] Yeah.
[3425.06 → 3425.38] Okay.
[3425.84 → 3426.62] The clown was four.
[3426.72 → 3427.56] Three was communists.
[3428.14 → 3429.84] Two is physical rejection.
[3429.84 → 3432.06] The first one was young George.
[3432.40 → 3433.34] His mischievous childhood.
[3433.34 → 3436.40] He got caned as a kid.
[3436.80 → 3437.36] Oh, God.
[3440.02 → 3441.14] What are you going to do, Adam?
[3441.82 → 3442.68] I just already said.
[3442.88 → 3443.52] Oh, I couldn't hear you.
[3443.94 → 3445.68] I gave the points to number three, BMC.
[3445.90 → 3447.12] Oh, number three, BMC.
[3447.28 → 3447.52] Okay.
[3447.64 → 3447.96] All the way.
[3447.96 → 3449.46] Adam votes number three.
[3449.70 → 3452.00] Okay, we go now to Angelica.
[3453.52 → 3456.18] Obviously, we all know which one I think it was.
[3456.64 → 3457.22] We do.
[3458.30 → 3458.66] So.
[3458.66 → 3460.24] Which one do you actually think it is?
[3460.80 → 3462.96] What I actually think it is the last one.
[3462.96 → 3463.56] I think.
[3464.56 → 3469.84] The one about the raucous night out and leaving one's family behind.
[3469.98 → 3472.28] It feels very 1920s man to me.
[3472.66 → 3475.28] Angelica picks number six, locks it in.
[3475.36 → 3475.62] Matthew.
[3476.70 → 3478.82] I'm going to double on that.
[3479.32 → 3479.78] Okay.
[3479.86 → 3481.08] She also picks number six.
[3481.16 → 3482.44] The raucous night out is.
[3482.76 → 3485.44] It's very, it gives very 1920 vibes.
[3485.78 → 3487.26] You know, who uses raucous anymore?
[3487.42 → 3488.52] Nobody uses that word anymore.
[3488.52 → 3489.86] Yeah, who says raucous?
[3490.30 → 3490.52] Right.
[3490.72 → 3493.04] The flappers and like jazz music.
[3493.66 → 3496.60] The flappers, the big, the big city, you know.
[3496.64 → 3497.28] Yeah, I can see it.
[3497.28 → 3498.34] Raucous nights out.
[3498.42 → 3498.66] Okay.
[3499.80 → 3501.66] John Henry, are you going to go raucous?
[3502.12 → 3504.04] Oh, I don't know.
[3504.96 → 3509.72] Uh, I mean, yeah, the I like the raucous part, but.
[3509.72 → 3510.46] It's a pile on.
[3510.68 → 3511.24] Oh my gosh.
[3511.24 → 3512.28] Oh, is that a pile on?
[3513.76 → 3515.44] Where's Matt when you need him to sing a song?
[3515.44 → 3522.62] Oh, I'm going to go with number four, the clown.
[3523.50 → 3524.74] He's not piling on.
[3524.80 → 3526.94] He's playing the spread, and he's going with the clown.
[3527.30 → 3528.58] BMC, what are you going with?
[3529.58 → 3529.92] Raucous.
[3530.94 → 3531.92] He's going raucous.
[3532.50 → 3532.94] Wow.
[3534.20 → 3535.58] Now that's a pile on right there.
[3536.40 → 3538.28] Adding to George's poor trauma.
[3538.28 → 3539.32] He never gets picked.
[3540.20 → 3542.72] Oh, young George's mission of childhood.
[3542.92 → 3546.42] Of course, we all do know that Angelica wrote that book.
[3547.20 → 3548.14] About a movie.
[3548.96 → 3550.28] What gave it away?
[3550.54 → 3551.50] She duped all of you.
[3551.50 → 3553.38] She practically had the entire script written.
[3553.54 → 3554.58] It was a screenplay.
[3554.94 → 3556.48] Yeah, it was a screenplay.
[3557.68 → 3559.92] Uh, it was more of a review than even a synopsis.
[3560.00 → 3560.76] Good job, Angelica.
[3560.90 → 3561.58] Very well written.
[3561.68 → 3564.20] I enjoyed it from, you know, it was a raucous night out.
[3565.42 → 3566.62] Uh, that was hers.
[3566.68 → 3567.40] Nobody picked it.
[3567.56 → 3569.36] Uh, scared straight short film.
[3570.04 → 3570.80] All right.
[3570.80 → 3578.28] So one point for BMC and the pile on Angelica, Matthew and BMC were all out on for a raucous night
[3578.28 → 3578.48] out.
[3578.58 → 3581.34] John Henry did not pile on any thoughts as to why.
[3581.34 → 3582.38] Maybe he didn't pick it.
[3582.46 → 3583.68] Well, because he wrote it.
[3583.78 → 3586.12] Oh, big time.
[3586.76 → 3587.32] Big time.
[3587.42 → 3588.26] Three points there.
[3590.14 → 3592.42] And he's no clown.
[3592.60 → 3594.30] He's got the right answer as well.
[3594.50 → 3601.36] He got two because the actual synopsis of he who gets slapped is a bitter clown endeavours
[3601.36 → 3606.14] to rescue the old woman he loves from the lecherous baron who once betrayed him.
[3606.38 → 3606.56] Wow.
[3607.10 → 3607.40] Wow.
[3608.06 → 3609.12] How'd you know that, John Henry?
[3609.86 → 3613.78] Well, uh, my grandfather wrote the screenplay.
[3613.78 → 3622.98] No, it, it, uh, it just seemed like nobody would add a clown into theirs unless they were like,
[3623.38 → 3629.88] it's just like, it's not quite funny, but it's like kind of like too weird to like, uh,
[3629.88 → 3633.66] you wouldn't add that to make it like, Oh no, that's not what a movie is about.
[3633.66 → 3636.30] So I was like, okay, that's just weird enough.
[3636.42 → 3636.88] Good thinking.
[3637.00 → 3637.16] Yeah.
[3637.20 → 3642.52] Like there's nobody, there's no clown inclinations in the title at all.
[3643.14 → 3643.58] Yeah.
[3643.70 → 3649.24] And it's not quite weird enough to be funny, but it is weird enough to be the actual synopsis
[3649.24 → 3653.04] of a 1924 movie and a big score.
[3653.22 → 3656.88] So you got three for flowering and two for getting it correct.
[3657.00 → 3658.00] So that's a five point.
[3658.00 → 3658.44] Wow.
[3659.04 → 3662.10] And BMC is the only other person that scored that round with one.
[3662.46 → 3666.86] So big score bringing you into first place with nine points, passing Matthew with eight,
[3666.96 → 3671.46] BMC with seven, Angelica with five, me with four, Adam with one.
[3672.34 → 3673.74] Still anybody's game there.
[3674.06 → 3678.24] Oh, I got the bonus point for getting the, uh, you know, the, the, the, you know, the side
[3678.24 → 3678.60] quest.
[3679.02 → 3680.00] You drilled the side quest.
[3680.14 → 3682.92] How many points did you get for knowing that BMC wrote that one?
[3683.00 → 3684.20] At least a half a point, you know?
[3684.28 → 3684.50] All right.
[3684.50 → 3685.54] We'll give you a half.
[3685.74 → 3686.10] Sweet.
[3686.10 → 3687.80] Adam with 1.5.
[3688.00 → 3689.12] 1.3.
[3689.18 → 3690.24] Let's go down to 1.3.
[3690.40 → 3690.66] Okay.
[3690.72 → 3691.56] We'll give you a third.
[3691.96 → 3693.60] 1.3 repeating decimal.
[3694.18 → 3698.26] Well, friends building multi-agent software is hard.
[3698.80 → 3704.48] Agent to agent and agent to tool communication is still the wild, wild west.
[3704.90 → 3711.10] So how do you achieve accuracy and consistency in non-deterministic agentic applications?
[3711.62 → 3715.72] That's where the agency, A-G-N-T-C-Y comes in.
[3715.72 → 3720.68] The agency is an open source collective building the internet of agents.
[3720.68 → 3723.58] And what is the internet of agents?
[3723.98 → 3729.16] It's a collaboration layer where AI agents can communicate, discover each other, and work
[3729.16 → 3730.22] across frameworks.
[3730.60 → 3736.06] For developers, this means standardized agent discovery tools, seamless protocols for inter-agent
[3736.06 → 3741.72] communication, and modular components to compose and scale multi-agent workflows.
[3741.72 → 3746.86] You can now build with other engineers who care about high-quality multi-agent software.
[3747.32 → 3750.52] Visit agency.org and add your support.
[3750.90 → 3754.60] That's A-G-N-T-C-Y dot org.
[3754.60 → 3763.38] We move now to round six where the word for round six is penumbra.
[3763.74 → 3766.68] So back to the original definition.
[3767.12 → 3767.76] That's correct.
[3768.10 → 3775.30] This is a regular round penumbra spelled P-E-N-U-M-B-R-A.
[3776.94 → 3780.74] And you can submit to me your definitions whenever you have them.
[3780.74 → 3783.66] I have to think of how to word mine.
[3784.60 → 3786.50] Clearly it's not correct then, is it?
[3786.96 → 3788.62] That's up to Jared to decide.
[3789.24 → 3789.62] Miss.
[3790.12 → 3793.74] I think it's actually up to the Oxford Dictionary to decide.
[3795.10 → 3795.58] Mister.
[3795.96 → 3799.10] Oxford can't even decide where to place a comma, so we don't talk to them.
[3799.10 → 3803.30] Well, you're talking about American English as opposed to the actual English, so.
[3803.86 → 3805.12] Aren't you in America?
[3805.72 → 3806.18] Yes.
[3806.46 → 3809.50] Does that mean I have to adhere to your grammatical errors?
[3809.68 → 3810.06] No.
[3810.50 → 3812.54] Excuse me, I don't make grammatical errors.
[3812.96 → 3813.76] Excuse me.
[3813.84 → 3816.60] No, you just say like 52 times within an hour.
[3816.78 → 3818.18] Listen, okay, I tried.
[3818.18 → 3829.10] All right, we have six definitions for penumbra, one of which is the correct definition.
[3829.52 → 3833.18] And three points before the round begins goes to Matthew.
[3833.34 → 3835.50] He has the correct definition.
[3835.68 → 3837.06] He knows what a penumbra is.
[3838.08 → 3839.36] So you're going to set this one out.
[3839.46 → 3839.88] Congrats.
[3839.96 → 3841.12] You've already scored three.
[3841.12 → 3845.02] And we go now to five definitions.
[3845.74 → 3851.10] Number one, an area in which something exists to a lesser or uncertain degree.
[3852.00 → 3855.42] Number two, the largest in a list of numbers.
[3857.04 → 3862.20] Number three, the second to final stage of a nerve receptor's life cycle.
[3863.88 → 3867.40] Number four, what's the matter with you, huh?
[3867.72 → 3868.20] Penumbra.
[3868.20 → 3868.64] Penumbra.
[3870.14 → 3879.28] Number five, a geographical or astrological term for a peninsula or a concave piece of land that is in shade on a planet.
[3880.18 → 3881.40] Angelica goes first.
[3882.00 → 3884.42] Which one do you think is a penumbra?
[3885.08 → 3887.62] I think I'm between the second one.
[3888.10 → 3889.60] Which was the largest in a list of numbers.
[3890.24 → 3896.14] Yes, like the penultimate penumbra that like resonated with my brain.
[3896.14 → 3896.86] Mm-hmm.
[3897.22 → 3898.26] I'm just going to go with that one.
[3898.38 → 3898.66] Okay.
[3898.66 → 3901.66] Now that I'm talking it through in my brain, it's resonating.
[3901.86 → 3902.88] She's locking that one in.
[3903.32 → 3903.72] Okay.
[3904.06 → 3908.02] Now we go to, we'll skip Matthew because he's correct.
[3908.10 → 3908.64] We go to BMC.
[3909.40 → 3910.80] Could you say the first three again?
[3911.46 → 3915.88] Number one was an area in which something exists to a lesser or uncertain degree.
[3916.52 → 3919.42] Number two was the largest in a list of numbers.
[3919.42 → 3925.22] And number three was the second to final stage of a nerve receptor's life cycle.
[3925.96 → 3928.72] My knowledge of prefixes is getting in my way.
[3929.70 → 3930.98] I hate it when that happens.
[3931.16 → 3932.02] Me too.
[3932.30 → 3933.08] Thank you.
[3933.40 → 3934.52] No one ever says that.
[3936.88 → 3937.80] The first one.
[3938.76 → 3939.76] The first one.
[3939.90 → 3940.24] Okay.
[3940.36 → 3944.44] BMC picks an area in which something exists to a lesser or an uncertain degree.
[3944.76 → 3945.42] That means nothing.
[3946.66 → 3948.10] Go now to John Henry.
[3948.10 → 3950.06] I'm going to go with the largest number.
[3950.34 → 3951.76] That seems the most logical.
[3952.08 → 3952.40] Okay.
[3952.92 → 3954.12] Piling on with Angelica.
[3955.02 → 3956.72] Going now to Adam.
[3957.46 → 3958.34] Angelica chose her own.
[3959.60 → 3960.72] Let's see here.
[3962.02 → 3963.36] She says she didn't.
[3963.56 → 3964.62] I refute that claim.
[3965.14 → 3966.60] No one puts baby in the corner.
[3967.38 → 3968.46] Or in the shadows.
[3969.00 → 3969.42] Oh.
[3969.94 → 3970.72] I'm going with the shadow.
[3971.62 → 3972.58] Where are you putting babies?
[3973.02 → 3974.62] In the penumbra.
[3975.10 → 3976.00] In the penumbra.
[3976.00 → 3977.30] What's the matter with you, huh?
[3977.30 → 3978.22] What number?
[3980.38 → 3980.74] Obviously.
[3980.74 → 3982.54] Which number is the shadow?
[3982.74 → 3982.98] I don't know.
[3983.04 → 3983.76] Like five or something.
[3983.90 → 3984.20] Six.
[3985.20 → 3985.94] It was the last one.
[3986.34 → 3989.74] The peninsula with the shadow occurring deep within the jungle.
[3989.90 → 3990.16] Gotcha.
[3990.66 → 3991.02] All right.
[3991.10 → 3992.16] So Adam goes to that one.
[3993.20 → 3993.62] All right.
[3993.66 → 3994.48] So we'll start right there.
[3994.58 → 3998.10] Adam thought Angelica picked her own, but then Adam picked Angelica's.
[3998.36 → 3998.92] That was.
[3999.34 → 4001.10] See, I was just trying to help you out, Angelica.
[4001.20 → 4003.02] I just cut you down, put you right back up.
[4003.48 → 4004.04] Some way I'd do it.
[4004.04 → 4004.86] I appreciate it.
[4006.14 → 4009.64] Angelica thought it was the largest in a list of numbers.
[4009.64 → 4011.38] So did John Henry.
[4011.56 → 4012.52] That's because he wrote it.
[4012.58 → 4013.72] So he gets one point.
[4013.80 → 4014.06] Oh.
[4014.74 → 4016.22] For fooling one person.
[4016.66 → 4017.92] I knew someone was going with their own.
[4018.80 → 4020.18] This tactic is not getting old.
[4020.46 → 4021.62] You use that tactic.
[4022.02 → 4022.74] One time.
[4022.86 → 4023.44] First round.
[4023.60 → 4024.50] Just to open it up.
[4025.22 → 4026.52] Let you know it could be possible.
[4026.98 → 4028.32] It's just showing you the possibilities.
[4028.54 → 4028.82] That's right.
[4028.82 → 4031.02] I'm here to teach you how to play the game.
[4031.24 → 4031.62] Thanks, man.
[4032.00 → 4032.98] I'm simply level one.
[4033.12 → 4034.00] I'm level one.
[4034.14 → 4038.20] And BMC thought it was an area in which something exists to a lesser or uncertain degree.
[4038.48 → 4040.68] That is a penumbra.
[4041.34 → 4043.08] So two points for BMC.
[4043.58 → 4044.82] That's one of the definitions.
[4045.04 → 4049.78] The other one is a partial shadow cause when an object does not completely block a light source.
[4049.90 → 4051.06] That's what Matthew wrote down.
[4051.52 → 4052.32] Oh, dang.
[4052.34 → 4054.58] Or the diffuse outer part of a sunspot.
[4055.76 → 4056.16] Maybe.
[4056.68 → 4058.26] You're really close, Angelica.
[4058.26 → 4059.16] That's why you convinced.
[4059.38 → 4061.34] I knew it was some shadowy thing.
[4061.80 → 4062.12] I did.
[4062.34 → 4063.68] I like half knew it.
[4063.80 → 4065.30] And I couldn't remember what the actual.
[4065.64 → 4065.76] Okay.
[4065.90 → 4067.10] So close you tricked somebody.
[4067.64 → 4068.00] Penumbra.
[4068.64 → 4069.36] Like umbrella?
[4070.20 → 4071.06] Like umbrella.
[4071.56 → 4071.84] No.
[4072.78 → 4073.98] This one was an interesting one.
[4074.00 → 4075.82] I knew this one immediately when you wrote it.
[4076.42 → 4077.44] For two reasons.
[4077.54 → 4080.32] One, I knew my prefix and suffix here.
[4080.50 → 4080.64] Right?
[4080.72 → 4081.34] Thank you, Pokémon.
[4081.68 → 4081.98] Umbreon.
[4082.20 → 4082.52] Espeon.
[4083.30 → 4086.14] And then also like when I was doing lighting for my kitchen.
[4086.14 → 4089.92] You, there was, when I was placing lights for the ceiling and finding out where to do it,
[4090.00 → 4093.14] there's always that secondary shadow that's cast under the cabinets.
[4093.48 → 4095.28] And I wanted to minimize that as much as possible.
[4095.30 → 4096.14] And I was like, how do I do that?
[4096.14 → 4098.00] And that's where I found that term.
[4098.60 → 4098.92] Gotcha.
[4099.24 → 4101.86] And I was like, oh, that's what that secondary shadow is called.
[4102.02 → 4102.84] It is a science.
[4102.98 → 4104.08] Kitchen lighting is a science.
[4104.72 → 4105.72] So yeah, that's what it is.
[4106.14 → 4106.46] Yeah.
[4106.98 → 4108.24] No penumbrae in my house.
[4108.92 → 4109.24] That's right.
[4109.52 → 4110.50] What's the matter with you, huh?
[4112.50 → 4113.86] I'm not sure what Adam wrote there.
[4115.30 → 4116.32] What's the matter with you, huh?
[4116.32 → 4116.96] Penumbra.
[4118.30 → 4119.90] Can you explain the logic on that one?
[4119.90 → 4121.00] Just make you all laugh a little bit, you know?
[4121.00 → 4121.24] Gotcha.
[4121.76 → 4122.14] Oh yeah.
[4122.34 → 4122.90] Gotta laugh.
[4123.62 → 4123.92] All right.
[4123.96 → 4124.98] So three points for Matthew.
[4125.52 → 4126.46] Two for BMC.
[4126.66 → 4127.48] One for Angelica.
[4127.72 → 4128.90] One for John Henry.
[4130.86 → 4133.16] Bringing Matthew into first place with 11.
[4133.32 → 4134.36] John Henry with 10.
[4134.76 → 4135.86] BMC with nine.
[4136.22 → 4137.14] Angelica with six.
[4137.22 → 4137.90] Me with four.
[4137.90 → 4139.96] And Adam with 1.3 repeating decimal.
[4140.90 → 4141.28] All right.
[4141.30 → 4143.42] We're getting late in the game now.
[4143.88 → 4145.78] Round seven of a potential 10 rounds.
[4146.42 → 4147.62] This is a different round.
[4147.72 → 4150.20] It's called How Do You Do, Fellow Humans?
[4151.26 → 4157.02] Because I have gone out to ChatGPT and given it a prompt.
[4157.54 → 4158.38] And it has responded.
[4158.52 → 4159.48] I wrote down its response.
[4159.48 → 4164.96] Your job is to act as if you are fellow humans and fellow Chapters.
[4164.96 → 4168.42] And write your own response to this prompt.
[4168.90 → 4173.32] The prompt is created a new word in the world of science fiction and give it a one sentence definition.
[4173.52 → 4176.76] It should be both interesting and memorable.
[4176.76 → 4179.74] So I've written down ChatGPT's response.
[4180.52 → 4186.90] You'll write down your response as if you are ChatGPT to this prompt.
[4187.82 → 4188.86] Put it in the chat.
[4189.10 → 4190.32] I'll read it again for our listener.
[4192.20 → 4197.44] Create a new word in the world of science fiction and give it a one sentence definition.
[4197.44 → 4200.86] It should be both interesting and memorable.
[4201.58 → 4203.52] Are you all thinking or done already?
[4204.64 → 4205.16] Thinking.
[4205.54 → 4206.14] They're thinking.
[4206.28 → 4207.68] I have zero submissions.
[4209.86 → 4214.78] I love this game.
[4214.94 → 4216.00] Adam's making himself laugh.
[4218.24 → 4219.42] What's the matter with you?
[4220.08 → 4220.22] Huh?
[4221.28 → 4221.66] Number?
[4222.30 → 4223.80] Is that supposed to be read in the rocky voice?
[4223.80 → 4231.88] If I can't get me, I get Jared.
[4235.72 → 4240.70] Oh, gosh.
[4245.48 → 4246.16] Oh, no.
[4246.18 → 4247.02] It's going to be a good round.
[4247.14 → 4247.56] Oh, no.
[4250.92 → 4252.24] You have to enunciate it.
[4252.52 → 4252.66] Okay.
[4254.36 → 4254.72] Nope.
[4255.38 → 4257.06] Oh, it's going to be a tough one to read.
[4257.12 → 4257.64] All these.
[4261.12 → 4262.34] Got to play it straight.
[4262.94 → 4263.64] I'm crying.
[4264.00 → 4264.34] I'm crying.
[4265.10 → 4266.18] Oh, this one's hard.
[4266.28 → 4266.88] I'm not going to lie to you.
[4266.90 → 4267.60] This is really hard.
[4268.18 → 4268.50] Good.
[4269.06 → 4272.26] A little challenge for your Tuesday afternoon.
[4272.78 → 4274.04] I'm going to keep going there, Jared.
[4274.10 → 4275.78] I'm just going to maybe augment it a little bit.
[4275.80 → 4276.10] Okay.
[4276.66 → 4277.42] You're going to change it now?
[4277.82 → 4279.28] Well, I'm going to go the same direction.
[4279.40 → 4280.48] I just didn't do a good job.
[4282.08 → 4282.48] Okay.
[4283.80 → 4290.84] Angelica, you just submitted a second one or are you just clarifying for me?
[4291.32 → 4292.72] I just thought you thought it would be fun.
[4297.92 → 4300.00] She's like, I just came back for more.
[4300.00 → 4304.50] I just added a supplementary meme.
[4305.30 → 4306.30] I do like that meme.
[4306.30 → 4307.52] It's an illustrative person.
[4307.52 → 4309.52] Am I supposed to include that in your actual...
[4309.52 → 4310.96] It's up to you.
[4311.06 → 4312.58] I'll give you creative discretion.
[4312.90 → 4313.22] Okay.
[4313.22 → 4316.40] This is at your discretion, Jared.
[4316.48 → 4318.14] You just go whichever direction you want to go, okay?
[4318.98 → 4320.32] I just need to enunciate.
[4320.60 → 4321.50] Remember, enunciate.
[4321.50 → 4328.90] I was so close to writing a description of a new word that was fit with my favourite sticker on my water bottle.
[4328.90 → 4330.86] It looks like Rang.
[4331.62 → 4333.78] It kind of does look from Ninja Turtles.
[4334.12 → 4334.50] Yeah.
[4334.74 → 4334.94] Yeah.
[4335.48 → 4336.74] But it's stuck in the Game Boy.
[4337.00 → 4337.38] Oh, yeah.
[4337.44 → 4337.80] It does.
[4337.86 → 4338.04] Yeah.
[4338.78 → 4339.14] Why?
[4339.94 → 4340.30] Where?
[4341.02 → 4341.30] Why?
[4342.66 → 4344.16] Just for like funnies.
[4345.04 → 4346.28] It makes me laugh.
[4346.66 → 4348.76] It is funny, but where'd you get it?
[4348.76 → 4352.70] I also have a worm from Worm Emporium.
[4353.12 → 4354.20] What do they sell there?
[4355.26 → 4355.82] Worms.
[4357.06 → 4358.74] She just answered that one straight.
[4359.28 → 4362.34] But this one is actually made by the Pinky Cat.
[4363.76 → 4366.24] So it's a worm made by the Pinky Cat.
[4366.84 → 4367.56] Can you...
[4367.56 → 4371.00] Have you seen that one thing that's a worm or tiger tail?
[4371.42 → 4372.54] It's a thing, you know?
[4373.18 → 4375.02] Is it a worm or is it a tiger tail?
[4375.58 → 4376.38] I have seen that.
[4376.46 → 4377.64] I'm not very good at guessing, though.
[4378.18 → 4378.56] Mm-mm.
[4378.76 → 4380.40] I feel like if I could touch it, I could tell.
[4381.24 → 4381.60] Yeah.
[4382.38 → 4382.74] Definitely.
[4383.52 → 4384.00] All right.
[4384.36 → 4387.92] We have six potential real responses from ChatGPT.
[4388.02 → 4389.54] Only one of them is the real response.
[4389.68 → 4392.64] To the prompt, create a new word in the world of science fiction
[4392.64 → 4394.08] and give it a one-sentence definition.
[4394.08 → 4397.66] It should be both interesting and memorable.
[4398.98 → 4400.26] Response number one.
[4401.26 → 4401.90] Neurology.
[4402.10 → 4402.60] A noun.
[4403.06 → 4406.34] A clandestine device implanted in the cerebral cortex
[4406.34 → 4411.90] that allows its user to overwrite memories with synthetic experiences,
[4412.40 → 4415.88] blurring the line between reality and engineered perception.
[4415.88 → 4418.42] Number two.
[4418.42 → 4420.16] I would be happy to.
[4420.26 → 4421.36] Here's a new word for you.
[4421.90 → 4422.62] Sound.
[4423.50 → 4429.86] A spherical shield around itself that is completely impenetrable and indestructible to everything.
[4430.80 → 4430.86] Mm.
[4430.86 → 4432.14] Number three.
[4432.14 → 4433.06] Great idea.
[4433.06 → 4434.44] How about Zinn us?
[4434.88 → 4437.32] A rare plant with mystical healing properties.
[4437.88 → 4441.28] That could provide a sci-fi spin on a familiar story element.
[4442.14 → 4443.26] Number four.
[4443.88 → 4444.72] Darlington.
[4445.38 → 4449.60] The powerful hybrid offspring of a rogue, Fabric, and a Gorgon.
[4449.60 → 4450.60] Sorry.
[4452.60 → 4453.24] Sorry.
[4454.14 → 4455.92] Their union was born.
[4456.28 → 4456.78] Sorry.
[4457.88 → 4464.08] Their union was born out of both love and due to the potent essence of the Gorgon spit.
[4464.34 → 4464.78] Sorry.
[4466.78 → 4468.68] As reproductive properties.
[4470.00 → 4474.70] This has resulted in a uniquely resilient new species within the matrix.
[4475.64 → 4476.66] Number five.
[4476.66 → 4477.10] Certainly.
[4477.88 → 4480.64] Here's your new science fiction word that's both interesting and memorable.
[4482.60 → 4483.08] Allocate.
[4484.02 → 4484.52] Allocate.
[4485.22 → 4490.00] The treatment of a porous substance to fill all its vessels and create a single entity.
[4490.84 → 4492.24] Let me know if you'd like more words.
[4492.60 → 4494.18] I can even use it in a sentence for you.
[4494.70 → 4495.62] And number six.
[4496.20 → 4496.68] Jaggies.
[4497.28 → 4498.40] Comfortable pants.
[4499.36 → 4501.12] Comfortable pants for remote working.
[4501.28 → 4502.26] A play on leggings.
[4503.58 → 4504.06] Okay.
[4504.06 → 4513.32] There are six, frankly, spectacular responses by ChatGPT wannabes.
[4514.22 → 4515.98] And we'll see who's who.
[4516.26 → 4517.68] Angelica, you get to pick first.
[4517.76 → 4519.14] Which one do you like the most?
[4520.14 → 4521.16] Can I hit?
[4522.68 → 4523.64] One through six.
[4524.46 → 4525.96] You want to hear number four again?
[4528.20 → 4528.84] Darlington.
[4529.64 → 4530.84] Three and four, please.
[4530.94 → 4531.10] Okay.
[4531.14 → 4531.62] Three and four.
[4531.72 → 4532.74] Three says, great idea.
[4532.74 → 4534.00] How about Minus?
[4535.06 → 4535.70] Or Minus?
[4535.82 → 4536.92] It's Z-I-N-N-U-S.
[4537.36 → 4539.42] A rare plant with mystical healing properties.
[4539.64 → 4542.70] That could provide a sci-fi spin on a familiar story element.
[4543.12 → 4543.52] Okay.
[4543.56 → 4544.74] And number four was Darlington.
[4545.70 → 4549.16] The powerful hybrid offspring of a rogue Fabric and a Gorgon.
[4549.50 → 4554.90] Their union was born out of both love and due to the potent.
[4554.90 → 4563.18] And due to the potent essence of the Gorgon's spit and its reproductive properties.
[4563.64 → 4567.46] This has resulted in a uniquely resilient new species within the matrix.
[4568.58 → 4569.24] That one.
[4569.46 → 4569.98] That one.
[4570.36 → 4570.86] Okay.
[4571.22 → 4573.02] Angelica goes for that one.
[4574.30 → 4574.90] Matthew.
[4575.52 → 4576.98] Can you repeat one and two?
[4576.98 → 4577.66] Yes.
[4577.84 → 4579.42] One was Neurology.
[4579.98 → 4586.74] A clandestine device implanted in the cerebral cortex that allows its user to overwrite memories
[4586.74 → 4592.56] with synthetic experiences blurring the line between reality and engineered perception.
[4593.34 → 4595.60] And number two says, I would be happy to.
[4595.82 → 4597.02] Here's a new word for you.
[4597.56 → 4598.54] Sound.
[4598.54 → 4606.02] A spherical shield around itself that is completely impenetrable and indestructible to everything.
[4607.12 → 4607.42] Number three.
[4607.74 → 4608.12] All right.
[4608.24 → 4610.18] He's going for number three, which is the Genus.
[4611.76 → 4613.50] We go now to BMC.
[4613.74 → 4614.80] Yeah, we go to BMC.
[4615.50 → 4616.50] Were there five or six?
[4616.64 → 4617.18] There were six.
[4617.44 → 4618.04] Can I hear the last two?
[4618.44 → 4619.36] Yeah, the last two.
[4619.44 → 4620.52] Number five says, certainly.
[4620.72 → 4623.12] Here's your new science fiction word that's both interesting and memorable.
[4624.00 → 4624.36] Accurate.
[4624.86 → 4625.56] Or accurate.
[4625.72 → 4627.34] A-P-L-U-R-A-T-E.
[4627.34 → 4631.80] The treatment of a porous substance to fill all its vessels and create a single entity.
[4632.12 → 4633.60] Let me know if you'd like more words.
[4633.92 → 4635.90] I can even use it in a sentence for you.
[4636.52 → 4637.96] And number six is jaggies.
[4638.18 → 4640.18] Comfortable pants for remote working.
[4640.76 → 4641.94] A play on baggings.
[4643.10 → 4645.94] Which may be familiar because you wrote pants down previously.
[4646.72 → 4647.50] I wrote pants down?
[4648.88 → 4649.36] Didn't you?
[4649.78 → 4650.66] Oh, yes.
[4650.66 → 4652.18] I wrote pants down.
[4652.58 → 4653.10] Yeah, you did.
[4653.76 → 4653.92] Yeah.
[4654.60 → 4655.20] Or the first two.
[4655.20 → 4659.54] I will now summarize because I cannot do this again.
[4660.72 → 4662.32] Neurology was the first one.
[4662.58 → 4664.90] And the second one was Sound.
[4665.58 → 4666.20] And the third one?
[4666.80 → 4668.80] The third one was Zinnias.
[4669.24 → 4670.14] Do you want the fourth one, too?
[4670.20 → 4671.16] Because you're just missing that one.
[4671.78 → 4673.82] The one that had the...
[4673.82 → 4675.34] Yeah, I'll do the fourth one.
[4675.62 → 4676.76] I probably know which one that is.
[4677.48 → 4678.20] Wait, what's the fifth?
[4679.42 → 4680.18] Oh, no, no, no.
[4680.28 → 4681.14] You asked for the fifth.
[4681.14 → 4681.48] I don't know.
[4681.98 → 4682.30] Accurate.
[4682.72 → 4683.00] Accurate?
[4683.00 → 4685.00] Which is the one that had the like...
[4685.20 → 4687.84] I'd be so happy to put that in a sentence for you.
[4688.40 → 4688.76] Oh.
[4689.66 → 4691.10] Well, there's a few of those.
[4691.32 → 4695.26] So, number five said, certainly, here's your new science fiction word that's both interesting
[4695.26 → 4695.60] and memorable.
[4695.96 → 4696.26] Oh, yeah.
[4696.34 → 4698.40] And it ends with, I could even use it in a sentence for you.
[4698.52 → 4699.76] I'm going to go with that one.
[4699.84 → 4705.72] It seems a little heavy-handed on the ChatGPT speak, but also I wanna.
[4706.38 → 4706.72] Okay.
[4706.98 → 4707.66] We'll give it to you.
[4708.36 → 4708.98] John Henry?
[4708.98 → 4710.98] I think I'm going to go...
[4712.18 → 4718.20] Doesn't have the ChatGPT speak, but number one is pretty solid.
[4720.52 → 4720.96] Neurology?
[4721.36 → 4721.92] Mm-hmm.
[4722.78 → 4724.50] Are you locking that in, or are you...
[4724.50 → 4726.56] No, I'm going to switch it.
[4726.62 → 4727.40] I'm going to go with number three.
[4727.86 → 4728.68] Number three.
[4728.94 → 4731.30] So, we now have two people on that one.
[4731.84 → 4732.86] That's the Minus.
[4733.84 → 4735.92] Adam, last to select.
[4735.92 → 4736.82] What are you liking?
[4736.92 → 4737.34] What are you thinking?
[4737.52 → 4738.10] What are you seeing?
[4738.30 → 4738.80] What are you doing?
[4739.54 → 4740.48] I'm thinking deeply.
[4741.86 → 4745.40] Which one was the one that really got Angelica?
[4745.90 → 4747.12] Like, made her laugh a lot?
[4748.00 → 4752.60] She really liked when I said their union was born out of both love and due to the potent
[4752.60 → 4754.06] essence of the Gorgon spit.
[4754.54 → 4755.42] That's what got her.
[4756.80 → 4757.16] See?
[4757.28 → 4757.76] Got her again.
[4757.86 → 4758.14] She's going.
[4758.82 → 4760.02] God, I hope that's the one.
[4764.16 → 4765.02] Lock that in.
[4765.02 → 4766.28] Lock that in.
[4766.84 → 4769.80] This is Jared's ChatGPT, right?
[4770.00 → 4771.00] This is mine, yeah.
[4771.36 → 4771.72] Okay.
[4771.88 → 4772.18] All right.
[4772.70 → 4776.12] It's in a temporary chat, so it doesn't have any context or memory.
[4776.92 → 4777.36] All right.
[4777.48 → 4782.20] Six potential responses to the prompt about a science fiction word and a definition.
[4782.74 → 4783.54] Where do we begin?
[4783.68 → 4784.34] Where do we begin?
[4784.48 → 4787.82] Well, let's begin right where we left off, which is the Gorgon spit.
[4787.82 → 4793.22] Which is probably a pretty good show title, honestly.
[4793.36 → 4793.88] Gorgon spit.
[4794.98 → 4796.28] I'm not sure about that.
[4796.66 → 4799.28] The powerful hybrid offspring of a rogue Dark.
[4799.50 → 4801.08] Angelica, how did you come up with this?
[4801.08 → 4806.26] I just thought of random sci-fi stuff.
[4807.08 → 4808.24] It's actually Dark.
[4808.96 → 4809.36] Oh.
[4809.92 → 4810.76] And Gorgon.
[4810.90 → 4811.78] And then the Matrix.
[4811.96 → 4815.58] I basically thought about what ChatGPT would define as sci-fi.
[4815.78 → 4816.16] I see.
[4816.38 → 4819.52] And then just smudged it together with a little bit of spice.
[4819.60 → 4821.94] So I was pronouncing it wrong when I say Dark?
[4822.16 → 4822.46] Yeah.
[4822.64 → 4823.84] I was trying to go for Dark.
[4824.12 → 4824.70] Like in Doctor Who.
[4824.72 → 4824.90] Oh.
[4825.26 → 4826.34] Like from...
[4826.34 → 4827.20] From Doctor Who.
[4828.22 → 4830.00] Your own definition made you laugh that hard?
[4830.84 → 4832.52] When you hear someone else say it.
[4832.88 → 4834.84] When you hear someone else say it.
[4834.86 → 4836.12] Then it sounds weird.
[4837.32 → 4838.68] It sounds really odd.
[4838.90 → 4840.74] When I wrote it, it was perfectly normal.
[4841.16 → 4843.88] Well, you did convince Adam to select it, so you get a point there.
[4844.06 → 4844.46] Good job.
[4845.12 → 4846.12] I called it Dragon.
[4846.54 → 4847.64] Whatever you called it.
[4847.74 → 4848.80] I appreciate it.
[4849.54 → 4851.42] Always just lending a hand around here.
[4851.42 → 4852.06] Matthew.
[4852.56 → 4853.00] Matthew.
[4853.48 → 4854.26] Let's see here.
[4854.56 → 4855.40] Matthew and John Henry.
[4855.54 → 4856.88] They piled on to Zinnias.
[4857.70 → 4859.32] Is that how I should pronounce it, BMC?
[4859.48 → 4859.76] Zinnias?
[4859.86 → 4861.04] He doesn't care what you do.
[4861.80 → 4863.44] He doesn't care, but he made it up.
[4863.60 → 4866.32] That was BMC's response.
[4866.46 → 4867.42] Two points for him.
[4868.70 → 4870.94] Nobody picked Jaggies, unfortunately.
[4871.56 → 4873.14] Nobody picked Sound.
[4873.64 → 4874.78] That's Sound.
[4876.86 → 4878.52] It's more like OSU.
[4878.80 → 4879.10] Nah.
[4881.42 → 4884.02] You should have put a pronunciation guide in there for me.
[4884.54 → 4886.16] I should have, but I figured you'd get it.
[4886.42 → 4886.94] Oh, no.
[4887.10 → 4887.86] I can't get that.
[4888.00 → 4890.48] When you, you know, it's OSU.
[4890.48 → 4892.74] B-O-O-N-A-H.
[4893.38 → 4893.60] Nah.
[4894.00 → 4894.48] OSU?
[4894.78 → 4895.14] Nah.
[4895.44 → 4895.88] OSU.
[4896.00 → 4896.20] Nah.
[4897.30 → 4897.74] Apologize.
[4897.90 → 4899.64] And then BMC picked Applegate.
[4899.74 → 4900.96] Is that how you pronounce that one, Matthew?
[4901.18 → 4901.58] Applegate?
[4902.10 → 4902.32] Yep.
[4902.36 → 4903.12] That sounds right to me.
[4903.18 → 4903.42] Okay.
[4903.46 → 4904.24] One point for you.
[4904.66 → 4905.94] Nobody picked Neurology.
[4906.06 → 4907.94] John Henry almost picked Neurology.
[4907.94 → 4910.14] But then he changed his mind.
[4910.24 → 4912.76] That was the correct response from ChatGPT.
[4912.92 → 4914.80] So four points go to Jared.
[4915.30 → 4915.86] Woo-hoo.
[4916.10 → 4918.48] You know, I don't know how four points go into you on this round.
[4918.64 → 4920.52] There's, this is a fake round.
[4920.84 → 4923.94] Oh, you would say that, Mr. One Point.
[4924.12 → 4927.72] Wait, don't people get a point if other people pick their definition?
[4928.46 → 4928.82] Yeah.
[4929.82 → 4930.14] Yes.
[4930.24 → 4930.98] Do I get points?
[4931.30 → 4931.92] Yeah, you got one.
[4931.98 → 4932.44] I gave you one.
[4933.04 → 4933.48] Oh, I can see.
[4933.48 → 4934.76] You're too busy laughing at it.
[4934.88 → 4935.54] Yeah, you get a point.
[4936.42 → 4937.46] Oh, thank you, Jared.
[4937.66 → 4938.06] You're welcome.
[4938.06 → 4938.46] Appreciate it.
[4938.68 → 4940.12] You can have another one if you'd like.
[4940.38 → 4941.22] I can have another one?
[4941.48 → 4942.42] I don't know if you want to do that.
[4942.70 → 4943.20] No, me.
[4943.36 → 4944.24] I can have another one.
[4944.24 → 4944.44] Oh.
[4945.24 → 4946.26] Why would I like that?
[4946.42 → 4947.86] I could have another one if you like.
[4948.46 → 4948.94] I like that.
[4949.36 → 4951.20] We can both have another one if you'd like.
[4951.38 → 4953.32] We can all have a few more if we'd like.
[4953.32 → 4957.48] After round seven, we're getting near the end, you all.
[4958.98 → 4962.24] Matthew from first with 12, BMC with 11, John Henry with 10.
[4963.02 → 4965.10] I move into fourth with eight points.
[4965.20 → 4968.48] Angelica has seven and Adam has 1.3 repeating decimal.
[4969.34 → 4970.36] 2.3 repeating decimal.
[4970.66 → 4971.32] Did he get somebody?
[4972.00 → 4972.24] Yeah.
[4972.40 → 4973.02] Didn't he get a point?
[4974.02 → 4975.32] No, he got awesome.
[4975.54 → 4975.82] Boo.
[4976.08 → 4976.40] Nah.
[4977.20 → 4977.54] Oh.
[4978.00 → 4979.70] It was so, I thought it was a point.
[4979.70 → 4980.60] It was so like happy.
[4980.92 → 4982.62] Oh, you know, I'm just happy.
[4982.62 → 4983.94] I'm just happy to be here, man.
[4984.12 → 4985.18] He's just happy to be here.
[4986.32 → 4988.08] I wish I would have pronounced it better for you.
[4988.62 → 4989.18] I know.
[4989.40 → 4991.34] Well, the actual definition is pretty solid.
[4992.02 → 4992.80] Yeah, it was good.
[4993.00 → 4994.36] The word's funny, but the definition is solid.
[4994.96 → 4996.18] I didn't really understand it.
[4996.24 → 4998.46] A spherical shield around itself.
[4999.42 → 4999.98] That is completely.
[4999.98 → 5001.82] It's a spherical shield around itself, you know?
[5002.32 → 5003.38] So, like a.
[5004.84 → 5006.54] How does a shield go around itself?
[5007.26 → 5008.14] Is it two shields?
[5008.46 → 5011.34] You should have said a spherical shield encompassing an object.
[5011.34 → 5015.42] It's like, imagine, imagine being, it's like a force field.
[5015.96 → 5016.16] Oh.
[5016.28 → 5016.74] That's what it is.
[5017.00 → 5017.24] Hmm.
[5018.44 → 5020.48] A spherical shield around itself.
[5021.38 → 5022.76] Like a tattle shell.
[5023.14 → 5024.30] So, is it shielding itself?
[5024.42 → 5025.60] Is it shielding itself?
[5025.92 → 5027.38] It's like a it's a sphere.
[5027.56 → 5028.60] So, do you know how spheres work?
[5028.74 → 5031.52] No, I'm a flat farther at this point, so I don't really know.
[5031.74 → 5031.82] No.
[5031.92 → 5032.50] It's not a circle.
[5032.72 → 5033.60] It's not flat Stanley.
[5033.76 → 5034.96] It's a circle.
[5035.22 → 5036.76] You know, a real sphere.
[5037.12 → 5037.38] Right.
[5037.38 → 5038.42] What's inside a sphere?
[5038.90 → 5041.36] Oh, so it's like a it's like a gyroscope.
[5041.60 → 5042.18] A wheel and a wheel.
[5042.30 → 5042.84] It's inside itself.
[5042.98 → 5044.20] What's inside is itself.
[5044.70 → 5045.36] Concentric spheres.
[5045.96 → 5046.36] That's right.
[5046.54 → 5047.72] And it's completely impenetrable.
[5048.42 → 5051.04] And indestructible to everything.
[5051.04 → 5054.00] But it had to be penetrated for another sphere to go in there.
[5054.16 → 5055.48] Well, no, it formed.
[5056.18 → 5057.06] It formed.
[5057.24 → 5057.56] Yeah.
[5057.56 → 5063.56] And so, once it was formed, what was inside could never be, you know, penetrated.
[5064.06 → 5067.38] So, then if it's impenetrable, why would there need to be multiple layers?
[5067.80 → 5068.64] There's no multiple layers.
[5068.72 → 5069.28] It's one layer.
[5069.52 → 5069.94] Oh, okay.
[5069.98 → 5072.72] Itself, what's inside the sphere and the sphere itself.
[5072.98 → 5073.64] Okay, I got it.
[5073.72 → 5074.40] I like this world.
[5074.48 → 5075.02] This is a fun world.
[5075.02 → 5075.20] Yeah.
[5075.42 → 5075.66] Yeah.
[5075.82 → 5078.84] The person who discovered it was with his girlfriend, but she was disagreeable.
[5078.94 → 5080.30] So, he said, that's an awesome boo.
[5080.46 → 5081.40] And she said, nah.
[5084.18 → 5084.78] You know what?
[5084.80 → 5085.74] We should give him a point.
[5085.84 → 5086.80] That's a good story.
[5086.80 → 5087.78] All right.
[5087.92 → 5089.74] We'll give you a third.
[5089.94 → 5091.80] So, you have 1.6 repeating decimal.
[5092.30 → 5092.74] Perfect.
[5093.22 → 5093.66] Okay.
[5094.00 → 5095.50] Let's move down to round eight.
[5096.42 → 5096.94] Clavichord.
[5098.90 → 5099.38] Clavichord.
[5099.56 → 5103.18] C-L-A-V-I-C-H-O-R-D.
[5103.56 → 5104.30] That's our word.
[5104.66 → 5106.52] You have to define a clavichord.
[5107.74 → 5109.86] Adam, why am I thinking about beef bones?
[5110.62 → 5111.70] There are many reasons.
[5112.78 → 5113.26] God, really?
[5113.90 → 5114.68] Maybe you're hungry.
[5115.24 → 5116.30] Is that what Arabic is?
[5117.12 → 5117.72] Asabuco-nah.
[5119.14 → 5120.90] That's when you turn down the Arabic.
[5121.36 → 5123.14] I thought it had like bone marrow in it or something.
[5123.82 → 5125.52] That's like a drink, isn't it?
[5126.18 → 5129.66] If you drink cow juice.
[5130.66 → 5131.06] Osasco.
[5131.06 → 5132.72] Oh, yeah.
[5132.72 → 5134.00] Because ossuary.
[5134.38 → 5134.64] Bone.
[5134.90 → 5137.02] Also, it must be something like that.
[5137.58 → 5139.50] Osasco or Osasco.
[5140.08 → 5143.66] Also known as Buck a la Milanese.
[5143.66 → 5147.58] Is a specialty of Lombard cuisine.
[5148.58 → 5152.06] Of cross veal shanks braised with vegetables.
[5153.38 → 5154.80] Wine that is white.
[5155.68 → 5156.98] As well as broth.
[5156.98 → 5165.66] Sometimes garnished with a little dash of Osasco.
[5165.66 → 5165.90] Oh, so bunch.
[5165.90 → 5172.74] Oh, my goodness.
[5172.74 → 5172.90] There you go.
[5176.82 → 5177.70] No.
[5177.70 → 5182.70] The word in round eight is clavichord.
[5184.74 → 5185.10] Clavichord.
[5186.56 → 5187.56] Six definitions.
[5187.90 → 5192.42] However, two of our contestants know what a clavichord is.
[5192.42 → 5197.38] and those two people are Break master Cylinder and Adam Stachowiak.
[5197.52 → 5199.06] So three points to each of you.
[5200.68 → 5204.32] A default three and the rest will play on.
[5204.32 → 5209.16] So clavichord, is it the muscular and nervous tissue
[5209.16 → 5211.38] in between the clavicle and scapula
[5211.38 → 5216.32] or is it an avant-garde type of body modification
[5216.32 → 5219.22] involving the precise insertion of jewellery
[5219.22 → 5221.34] through the skin above the clavicle bones
[5221.34 → 5224.62] connected by a decorative cord
[5224.62 → 5227.04] that drapes across the upper chest and shoulders?
[5227.98 → 5230.74] Or is it a woodwind instrument
[5230.74 → 5233.28] similar to a clarinet with 14 keys?
[5234.72 → 5238.40] Or is it a quiet archaic keyboard instrument
[5238.40 → 5240.84] with struck strings that's barely audible?
[5242.12 → 5244.88] There's your four definitions, and we start with Matthew.
[5245.52 → 5250.48] So we have two relatively bodily definitions
[5250.48 → 5254.10] and then two instrument definitions.
[5254.50 → 5255.30] Is that correct?
[5255.56 → 5255.82] Yes.
[5256.62 → 5259.80] The bodily definitions are what?
[5260.20 → 5262.60] Tissue and muscle around the clavicle
[5262.60 → 5263.76] and then some...
[5263.76 → 5265.88] Yeah, the muscular and nervous tissue
[5265.88 → 5268.02] and then the other one is a body modification
[5268.02 → 5271.94] involving insertion of jewellery through the skin
[5271.94 → 5273.74] above the clavicle bones.
[5274.08 → 5274.54] Okay.
[5275.10 → 5275.76] So one's...
[5275.76 → 5277.14] Connected by a decorative cord
[5277.14 → 5279.10] that drapes across the upper chest and shoulders.
[5279.54 → 5281.26] And then the other ones are instruments.
[5281.36 → 5283.12] One being a wind instrument?
[5283.18 → 5285.42] A woodwind instrument similar to a clarinet
[5285.42 → 5286.88] with 14 keys.
[5287.04 → 5289.90] And then the other one being a quiet archaic keyboard instrument
[5289.90 → 5292.32] was struck strings that are barely audible.
[5292.74 → 5295.58] So one's a wind and one's a string instrument.
[5296.62 → 5297.14] Correct.
[5297.58 → 5298.02] Okay.
[5298.62 → 5299.14] Hmm.
[5300.32 → 5300.78] I don't know.
[5300.84 → 5301.50] This is a weird one
[5301.50 → 5306.06] because clavicle sounds bony body,
[5306.26 → 5307.12] body-y,
[5307.34 → 5309.90] but then you have chord.
[5310.66 → 5314.38] That sounds more string instrument-like.
[5315.28 → 5316.08] I'm confused.
[5316.24 → 5317.16] Can I call a lifeline?
[5317.26 → 5318.50] How does lifelines work in this game?
[5318.50 → 5319.22] Do we have any of those?
[5319.22 → 5319.66] You can call me.
[5319.90 → 5320.66] I'll listen.
[5321.06 → 5322.12] You can't talk to these two.
[5322.52 → 5323.52] I can't talk to anybody.
[5323.78 → 5323.88] Okay.
[5323.88 → 5324.70] They know what it is.
[5325.34 → 5327.08] I'm in between the instrument ones, honestly.
[5327.08 → 5328.08] I think...
[5328.08 → 5329.34] I don't know.
[5331.14 → 5331.86] Clavichord.
[5333.72 → 5334.72] Clavichord, clavichord.
[5335.08 → 5336.28] I'm trying to say it
[5336.28 → 5338.78] and maybe my mind somewhere will be like,
[5338.86 → 5339.96] you've heard this before, Matt,
[5340.02 → 5340.82] in this context.
[5340.92 → 5341.38] Have fun.
[5342.64 → 5345.08] I think I'll just go with the...
[5345.84 → 5347.10] Not the wind instrument one,
[5347.16 → 5347.68] the other one.
[5347.68 → 5349.02] The one that's an instrument,
[5349.16 → 5349.66] but not...
[5349.66 → 5350.66] The keyboard instrument?
[5351.00 → 5351.40] Yeah.
[5352.14 → 5353.22] Yeah, let's do that one.
[5353.30 → 5353.58] All right.
[5353.62 → 5354.08] There you go.
[5355.22 → 5356.60] And we skip BMC.
[5356.68 → 5357.40] We go to John Henry.
[5357.70 → 5358.00] You know,
[5358.14 → 5359.46] I think I'm going to go
[5359.46 → 5361.60] with the body modification.
[5362.10 → 5363.66] I think it's a made-up word.
[5364.20 → 5365.00] I think that's...
[5365.00 → 5366.70] I think that might be what it is.
[5366.88 → 5367.16] Okay.
[5367.16 → 5367.78] Number two.
[5368.12 → 5368.58] Number two.
[5370.38 → 5371.68] And we go now to...
[5372.72 → 5373.24] Angelica.
[5373.24 → 5376.86] I'm also thinking that it's an instrument.
[5377.42 → 5377.72] Okay.
[5377.82 → 5378.90] There are two instruments to pick from.
[5379.20 → 5380.46] BMC got it right, right?
[5381.06 → 5381.40] Right.
[5381.96 → 5383.44] I feel like I'm going to think
[5383.44 → 5385.10] it's musically driven then.
[5385.76 → 5386.12] Mm.
[5386.84 → 5387.28] Smart.
[5387.68 → 5388.38] Or not smart.
[5388.66 → 5389.00] You decide.
[5389.08 → 5389.34] What was it?
[5389.40 → 5389.94] What were the two options?
[5390.02 → 5391.18] It was the pianist,
[5391.36 → 5392.76] piano-like shenanigan,
[5393.26 → 5394.14] or...
[5394.14 → 5394.86] Correct.
[5394.98 → 5396.52] ...the flute-like thing.
[5396.82 → 5397.62] Clarinet, flute.
[5397.82 → 5399.38] You know, woodwind versus string.
[5400.04 → 5400.52] I think it's...
[5401.78 → 5402.80] And which one did you do, Matthew?
[5403.20 → 5405.80] I did the stringed instrument one, yeah.
[5406.38 → 5407.74] Can you tell me the definition,
[5407.90 → 5408.72] the clavichord one,
[5408.84 → 5409.78] like the words you used?
[5410.32 → 5412.26] Can you give me the exact definition?
[5412.62 → 5413.26] Wait, what now?
[5415.40 → 5416.06] Pardon me?
[5416.84 → 5418.38] Can you give me the words
[5418.38 → 5419.84] that you used for...
[5419.84 → 5420.40] Clavichord.
[5420.40 → 5423.82] ...the clavichord musical instrument leaning to?
[5423.94 → 5424.52] You want me to give you
[5424.52 → 5425.48] those two definitions again?
[5425.60 → 5425.76] Okay.
[5425.76 → 5426.30] Mm-hmm.
[5426.40 → 5427.56] One's a woodwind instrument
[5427.56 → 5429.68] similar to a clarinet with 14 keys.
[5430.28 → 5431.32] And the other ones a quiet,
[5431.46 → 5432.70] archaic keyboard instrument
[5432.70 → 5433.60] with struck strings,
[5433.74 → 5434.28] barely audible.
[5435.22 → 5436.06] Barely audible.
[5436.70 → 5438.10] I'm going to go with the one that Matthew did.
[5438.24 → 5441.32] Okay, she's piling on to the strings.
[5441.88 → 5441.94] Yeah.
[5441.94 → 5443.00] Because Matthew's winning, right?
[5443.78 → 5444.26] Correct.
[5444.72 → 5445.56] I feel like I...
[5445.56 → 5446.98] I feel like I trust...
[5446.98 → 5448.12] I trust his intuition.
[5449.02 → 5450.98] Well, what is, after all,
[5450.98 → 5452.14] a clavichord?
[5452.28 → 5453.44] BMC, do you want to school us?
[5453.50 → 5454.16] What's a clavichord?
[5454.16 → 5456.64] It's like an old piano kind of thingy.
[5457.00 → 5458.86] It predates the piano forte
[5458.86 → 5460.52] and it's harpsichord-like.
[5461.64 → 5462.36] Thank you.
[5462.54 → 5463.02] There you go.
[5463.78 → 5464.48] You're welcome.
[5464.68 → 5465.60] Adam also knew that.
[5466.26 → 5467.88] I made my definition up.
[5467.92 → 5468.74] I had no idea.
[5468.74 → 5469.30] Are you serious?
[5469.76 → 5470.34] I made it up.
[5470.34 → 5470.54] Wait, really?
[5470.90 → 5471.46] No way.
[5471.98 → 5472.56] What is your definition?
[5472.56 → 5473.36] What was his definition?
[5474.20 → 5475.76] A distant relative to the harpsichord
[5475.76 → 5477.30] that uses keys in a linear arrangement.
[5477.48 → 5477.62] Yep.
[5477.62 → 5479.90] That's very...
[5479.90 → 5480.34] I mean, that's...
[5480.34 → 5481.86] That's a very good make-up solution.
[5481.90 → 5482.44] That's pretty good.
[5483.14 → 5484.02] Yeah, it works for me.
[5484.56 → 5486.12] Were you so surprised when you got it right?
[5486.32 → 5486.78] I was.
[5486.94 → 5487.82] I was like...
[5487.82 → 5489.18] I was like...
[5489.18 → 5490.86] Did you know what a harpsichord was?
[5491.10 → 5491.52] Oh, yeah.
[5491.84 → 5492.12] Okay.
[5492.28 → 5493.02] That makes sense.
[5493.04 → 5493.76] I'm going to go with...
[5493.76 → 5495.24] I'm going to be just like...
[5495.24 → 5495.46] Yeah.
[5495.54 → 5496.26] Keep it going.
[5496.40 → 5496.98] Just make it up.
[5496.98 → 5497.28] Yeah.
[5497.36 → 5497.92] Just make it up.
[5497.92 → 5498.64] I'm just going to push it.
[5498.78 → 5500.00] Dude, you made it up pretty closely.
[5500.94 → 5502.14] Close enough that it fooled me.
[5502.36 → 5503.08] I thought you knew it.
[5503.64 → 5504.48] I did, though.
[5504.54 → 5505.00] Three points.
[5505.00 → 5510.30] All right, so yes, it is the archaic keyboard instrument,
[5510.46 → 5512.32] which means Matthew and Angelica got it right.
[5512.42 → 5513.54] So you each get two.
[5513.94 → 5514.66] Thank you, Matthew.
[5515.18 → 5515.80] You're welcome.
[5516.90 → 5519.92] John Henry picked the body modification,
[5520.06 → 5521.02] which was Angelica's,
[5521.06 → 5523.04] so she gets another point there.
[5523.84 → 5526.32] So lots of points this round, except for me.
[5526.96 → 5527.88] Angelica got three.
[5528.06 → 5528.98] BMC got three.
[5529.16 → 5529.92] Adam got three.
[5530.14 → 5531.06] Matthew got two.
[5531.58 → 5532.82] John Henry and I shut out,
[5532.82 → 5535.54] which means we have one more round to play
[5535.54 → 5537.80] because 14 to 14,
[5538.20 → 5538.94] you two are tied,
[5539.08 → 5539.94] Matthew and BMC,
[5540.28 → 5540.80] in first.
[5541.42 → 5542.02] So this will probably,
[5542.10 → 5543.24] this will definitely be the last round
[5543.24 → 5544.12] unless somebody gets shut out,
[5544.18 → 5545.06] unless you both get shut out,
[5545.08 → 5545.50] I suppose.
[5547.24 → 5548.88] And Angelica has 10.
[5548.94 → 5549.82] John Henry has 10.
[5549.90 → 5550.62] I have eight.
[5550.70 → 5552.34] And Adam has 4.6,
[5552.38 → 5553.02] repeating decimal.
[5553.02 → 5557.42] So we have to shut out Matthew and BMC
[5557.42 → 5558.86] and the rest of us have to catch up.
[5558.98 → 5560.38] Now I'll give you guys the option
[5560.38 → 5561.76] for the final round.
[5561.88 → 5563.34] We can do a typical,
[5563.54 → 5564.18] another word,
[5564.32 → 5565.54] or I have another round,
[5565.60 → 5566.16] which is another,
[5566.26 → 5567.14] give it a good.
[5567.64 → 5568.72] We can do that one instead.
[5568.94 → 5570.06] This will be our last round,
[5570.12 → 5570.52] I assume.
[5571.00 → 5572.06] We can pick from those two.
[5572.12 → 5572.76] Which ones do you want to do?
[5573.22 → 5574.00] What was the first one?
[5574.28 → 5575.14] Just another word.
[5575.14 → 5576.32] I can't tell you what the word is
[5576.32 → 5577.56] because that might spoil it,
[5577.66 → 5578.64] but it's a standard round
[5578.64 → 5579.96] or give it a good.
[5580.70 → 5581.10] Good.
[5581.10 → 5581.84] You guys want to good it?
[5581.86 → 5582.80] Because I'll only guess the auto.
[5583.64 → 5584.72] That's the autocomplete one.
[5584.86 → 5585.06] Yeah.
[5585.88 → 5586.46] It's so hard,
[5586.52 → 5587.48] but it's also so easy.
[5588.22 → 5588.50] I mean,
[5588.54 → 5590.20] if it says near me at the end,
[5590.32 → 5590.70] you know.
[5592.50 → 5593.02] All right.
[5593.04 → 5593.20] Well,
[5593.20 → 5594.14] we'll do that round.
[5594.28 → 5595.32] We'll do give it a good.
[5595.38 → 5597.28] And the phrase that I began,
[5597.92 → 5599.02] the words I put in
[5599.02 → 5600.92] for into google.com
[5600.92 → 5601.82] incognito window
[5601.82 → 5603.48] is why is my,
[5604.04 → 5605.44] why is mine.
[5606.52 → 5608.50] And we'll see what we think
[5608.50 → 5609.92] the autocomplete suggested
[5609.92 → 5610.98] for the phrase,
[5611.10 → 5612.82] why is my.
[5613.78 → 5615.06] And this is PG rated.
[5615.56 → 5616.64] This is a family show.
[5617.22 → 5617.52] Okay,
[5617.62 → 5617.92] great.
[5618.24 → 5618.78] Good to know.
[5618.86 → 5620.54] Keep it somewhat relatively.
[5621.44 → 5622.44] I would always.
[5622.64 → 5623.74] I just wanted to clarify.
[5624.60 → 5625.42] So you all want to get together
[5625.42 → 5626.52] and watch that weird clown movie
[5626.52 → 5626.86] or what?
[5632.22 → 5633.58] July 27th.
[5634.16 → 5634.60] Hey,
[5634.68 → 5635.22] I had like a
[5635.74 → 5637.10] didn't have bad reviews, actually.
[5637.90 → 5638.92] He who gets slapped.
[5638.92 → 5639.78] That was the name.
[5640.06 → 5640.26] Yeah.
[5640.34 → 5641.30] He who gets slapped.
[5643.24 → 5644.48] This is for all the marbles
[5644.48 → 5645.04] right here.
[5645.70 → 5646.84] Unless BMC and Matt
[5646.84 → 5648.06] both get shut out
[5648.06 → 5649.04] and then we have to play the
[5649.26 → 5651.14] the last round,
[5651.26 → 5652.72] but unlikely.
[5652.72 → 5654.76] Come on marbles.
[5655.28 → 5655.54] Now,
[5655.60 → 5656.40] what if they both score
[5656.40 → 5657.92] the exact same amount of points?
[5658.66 → 5658.98] Hmm.
[5659.26 → 5660.62] Probably just announce them
[5660.62 → 5661.48] as co-winners.
[5662.20 → 5662.98] Sudden death.
[5663.44 → 5663.98] Single them out.
[5664.56 → 5665.28] Lightning round.
[5666.18 → 5666.76] That's right.
[5666.82 → 5667.70] A good lightning round it.
[5667.82 → 5669.24] A winner was so much nicer than
[5669.24 → 5670.56] sudden death.
[5670.56 → 5670.96] Yeah.
[5671.00 → 5671.80] A co-winner would be nice.
[5671.94 → 5672.28] It's like,
[5672.54 → 5673.90] you know,
[5673.92 → 5674.84] the communist style.
[5675.40 → 5676.14] We all win.
[5676.58 → 5677.44] Participation trophies.
[5678.12 → 5679.24] Speaking of all winning,
[5680.10 → 5681.34] he who gets slapped
[5681.34 → 5682.76] is in the public domain.
[5683.04 → 5683.32] You guys.
[5683.32 → 5683.40] Oh,
[5683.40 → 5683.64] really?
[5683.98 → 5685.74] We can have our own showings.
[5687.08 → 5688.30] That's actually pretty cool.
[5688.82 → 5689.78] January 2020
[5689.78 → 5690.54] is when it,
[5690.54 → 5691.00] when it,
[5691.00 → 5691.02] when it,
[5691.02 → 5691.72] the public domain.
[5691.86 → 5691.94] Oh,
[5691.94 → 5692.76] dang.
[5693.24 → 5693.44] Oh,
[5693.48 → 5695.04] it looks really quite creepy.
[5695.94 → 5696.46] Yes.
[5696.94 → 5697.92] That's the only problem.
[5698.28 → 5700.18] I'm really not a fan of clowns.
[5700.26 → 5700.72] All right.
[5700.74 → 5703.20] We have all the autocompletes.
[5703.82 → 5705.96] I surmise that this will be a hard one
[5705.96 → 5707.76] to identify the correct answer
[5707.76 → 5708.94] because they're all plausible.
[5709.80 → 5710.40] So applause.
[5710.72 → 5711.06] So bull.
[5711.44 → 5712.50] So give it a good.
[5712.60 → 5715.12] Why is my potential answer?
[5715.12 → 5715.64] Number one,
[5715.94 → 5717.12] computer so slow.
[5717.12 → 5718.74] Why is my computer so slow?
[5719.68 → 5720.26] Number two,
[5720.38 → 5721.80] why is my eye twitching?
[5723.52 → 5724.44] Number three,
[5724.56 → 5725.84] why is my leg bruised?
[5727.78 → 5728.74] Number four,
[5728.86 → 5730.42] why is my hair falling out?
[5732.72 → 5733.70] Number five,
[5733.78 → 5735.12] why is my poop green?
[5737.34 → 5738.36] Number six,
[5738.44 → 5739.92] why is my pee red?
[5740.22 → 5740.50] Oh,
[5740.56 → 5741.10] it's Christmas.
[5741.70 → 5742.84] One of those
[5742.84 → 5745.98] was the actual autocomplete suggestion.
[5746.44 → 5748.82] But which one was it?
[5748.90 → 5750.10] First up this round,
[5750.18 → 5750.58] John Henry.
[5751.42 → 5752.60] Can you read the first
[5752.60 → 5753.10] four?
[5753.56 → 5754.40] I can read them all.
[5754.48 → 5754.98] They're fast.
[5755.84 → 5756.48] Number one,
[5756.54 → 5757.76] why is my computer so slow?
[5757.88 → 5758.46] Number two,
[5758.58 → 5759.94] why is my eye twitching?
[5760.06 → 5760.94] Number three,
[5761.06 → 5761.96] why is my leg bruised?
[5762.14 → 5762.90] Number four,
[5763.06 → 5764.26] why is my hair falling out?
[5764.72 → 5765.32] Number five,
[5765.36 → 5766.38] why is my poop green?
[5766.48 → 5767.00] And number six,
[5767.06 → 5768.08] why is my pee red?
[5768.08 → 5769.62] I'm going to go with number one.
[5770.54 → 5771.52] Google's on the computer.
[5772.10 → 5773.74] People have computer issues.
[5774.06 → 5774.46] Okay,
[5774.78 → 5775.14] there you go.
[5775.18 → 5775.80] Number one,
[5775.88 → 5776.10] Adam,
[5776.14 → 5776.56] what about you?
[5776.94 → 5777.90] I'm done with the colours.
[5778.16 → 5779.22] I'm just trying to choose a colour.
[5779.32 → 5779.86] What colour?
[5780.20 → 5780.86] You like green?
[5780.86 → 5782.08] Yeah,
[5782.08 → 5783.04] I'm going red or green.
[5783.18 → 5783.64] Red or green.
[5783.98 → 5784.44] Christmas a lot,
[5784.54 → 5784.84] you know,
[5784.88 → 5786.94] it's a good sign.
[5787.78 → 5789.70] Should I go north or south?
[5789.94 → 5790.24] Right.
[5790.66 → 5791.68] Both of these are concerning.
[5791.78 → 5792.94] Like if your pee is red
[5792.94 → 5794.02] or if your poop is green,
[5794.24 → 5795.28] they're both concerning.
[5795.80 → 5796.36] It's Christmas.
[5796.90 → 5797.30] That's why.
[5797.82 → 5798.38] South Pole?
[5798.38 → 5798.68] It's Christmas.
[5799.74 → 5800.74] Which one are you going with?
[5801.10 → 5801.90] Let's go with the rookie,
[5802.00 → 5802.10] huh?
[5802.10 → 5803.10] Let's go with the rookie.
[5803.10 → 5805.52] There's another show title.
[5805.66 → 5806.44] Go with the rookie.
[5808.44 → 5808.88] Okay.
[5810.02 → 5812.88] How about Angelica?
[5813.40 → 5813.60] I mean,
[5813.60 → 5815.08] I feel like my PG definition
[5815.08 → 5817.58] is a higher bar
[5817.58 → 5818.78] than I think
[5818.78 → 5819.52] because I was thinking
[5819.52 → 5820.52] that it was going to be
[5821.42 → 5823.18] excrement related,
[5823.72 → 5824.94] but that was why I asked.
[5825.04 → 5825.94] So I didn't put that.
[5826.04 → 5826.18] Oh,
[5826.20 → 5826.78] so you didn't.
[5827.42 → 5827.66] See,
[5827.76 → 5827.88] no,
[5827.94 → 5828.74] I didn't put that
[5828.74 → 5830.72] because I thought it was not PG.
[5830.96 → 5831.54] I was unsure.
[5832.50 → 5832.64] So,
[5832.64 → 5833.34] but that is my,
[5833.48 → 5834.68] that was my original thought.
[5834.86 → 5835.14] Okay.
[5835.16 → 5837.22] So I'm also going to go with that one.
[5837.54 → 5838.24] Is it with the
[5838.24 → 5838.58] uh,
[5838.58 → 5840.06] number one or number two?
[5840.44 → 5840.78] The
[5840.84 → 5841.60] the first,
[5842.08 → 5842.92] the number two.
[5843.10 → 5843.58] Number two.
[5843.58 → 5844.08] Number two,
[5844.28 → 5845.42] the first one you said.
[5845.84 → 5846.60] Number two,
[5846.74 → 5847.52] the green one.
[5847.64 → 5848.36] The green.
[5848.72 → 5849.04] The green.
[5849.32 → 5849.64] Yes,
[5849.64 → 5850.12] number two.
[5850.24 → 5851.22] She's going with number two,
[5851.42 → 5851.72] green.
[5852.40 → 5853.34] She's going Duke.
[5855.22 → 5856.70] I'm way too excited about this.
[5856.76 → 5857.06] Okay.
[5857.54 → 5858.54] She's following me,
[5858.60 → 5858.80] man.
[5858.90 → 5859.36] You know what I'm saying?
[5859.76 → 5861.06] That means I'm on the right path.
[5861.26 → 5861.58] Matthew.
[5861.58 → 5864.02] So what do we have here?
[5864.02 → 5864.58] We have,
[5864.68 → 5865.36] what do we have?
[5866.38 → 5866.78] Well,
[5866.82 → 5868.32] we've got one person pick computer.
[5868.40 → 5868.84] So slow.
[5869.26 → 5870.80] Two people have picked poop green.
[5871.20 → 5871.62] Okay.
[5871.62 → 5872.72] So we have computer slow,
[5873.14 → 5873.74] poop green,
[5874.04 → 5874.62] pee red.
[5875.18 → 5876.32] Something about an eye.
[5876.46 → 5877.06] Eye twitching,
[5877.12 → 5877.68] hair falling out,
[5877.84 → 5878.30] leg bruised.
[5878.88 → 5879.60] Hair falling out,
[5879.68 → 5880.26] leg bruised,
[5880.48 → 5881.20] eye twitching,
[5882.08 → 5882.38] pee,
[5882.64 → 5882.92] poop.
[5882.92 → 5888.52] It's literally everything here is bodily related,
[5888.62 → 5889.80] which is funny except for.
[5890.12 → 5890.32] Yeah.
[5890.40 → 5890.62] Well,
[5890.64 → 5890.82] I mean,
[5890.82 → 5891.66] this is what we Google,
[5891.76 → 5892.08] I guess.
[5892.14 → 5892.82] Why is my,
[5893.38 → 5895.92] it is funny that two people already picked the rookie one though.
[5897.38 → 5898.62] It's going to be a third one.
[5898.62 → 5899.00] I just want to,
[5899.14 → 5902.58] I just want to like communally pick the rookie one at this point.
[5902.58 → 5902.70] Rookie.
[5902.86 → 5903.92] Let's go for the rookie.
[5904.92 → 5906.22] I'm going to pile on the poo.
[5906.22 → 5911.00] Pile on the poo.
[5911.10 → 5912.84] This is a first for us here at changelog.
[5914.22 → 5916.14] And hopefully it's a last.
[5916.26 → 5916.62] Okay.
[5916.88 → 5917.30] BMC,
[5917.46 → 5918.88] your final pick here.
[5919.30 → 5919.52] You know,
[5919.54 → 5920.20] pile on the poo.
[5920.84 → 5921.24] Computer.
[5921.48 → 5922.28] So slow.
[5922.68 → 5923.22] Final answer.
[5923.76 → 5924.18] Yes.
[5924.18 → 5926.50] Because it's the last round, and you said it first.
[5927.36 → 5927.62] Oh,
[5927.62 → 5928.66] he's playing the meta game.
[5928.76 → 5928.88] Huh?
[5929.86 → 5932.56] We'll see if that went into my calculus, actually.
[5933.04 → 5935.28] But then he also plans for that.
[5935.34 → 5936.10] So it's never quiet.
[5936.22 → 5936.52] Yeah.
[5936.54 → 5938.04] I randomize the order every round.
[5938.18 → 5939.06] Are we split on two,
[5939.16 → 5940.08] on two this round?
[5940.24 → 5940.72] We are.
[5940.86 → 5941.96] So we have two on computer.
[5942.04 → 5942.48] So slow.
[5942.52 → 5943.82] And we have three on poop green.
[5944.74 → 5949.54] Let me tell you some of the alternates that almost were the top one.
[5950.56 → 5952.06] Why is my eye twitching?
[5952.06 → 5954.10] That was actually the number two autocomplete suggestion.
[5954.22 → 5956.06] It was also Adam's guess.
[5957.04 → 5958.36] So you were very close to hitting it.
[5958.58 → 5959.66] No one selected it though.
[5960.20 → 5961.64] But a lot of people are apparently Googling.
[5961.72 → 5962.68] Why is my eye twitching?
[5963.66 → 5964.90] I was thinking that myself.
[5965.08 → 5965.24] No.
[5965.24 → 5966.70] Why is my pee cloudy?
[5966.88 → 5968.56] That was the number three autocomplete.
[5970.02 → 5971.48] Why is my pee red?
[5971.58 → 5972.38] That was close.
[5972.58 → 5972.96] BMC.
[5973.08 → 5974.56] BMC actually came up with that one.
[5975.12 → 5975.76] If your pee is red,
[5975.80 → 5976.52] that's a problem.
[5976.76 → 5977.00] That's,
[5977.00 → 5978.96] that's a huge problem.
[5978.96 → 5979.44] You're bleeding.
[5979.44 → 5979.66] You're bleeding.
[5979.66 → 5981.34] You're going to be in the hospital right now.
[5981.48 → 5981.68] Yeah.
[5981.68 → 5983.32] Have you ever heard of something called beets?
[5983.76 → 5984.16] Okay.
[5984.24 → 5985.82] Do you have any beets you need to eat?
[5985.94 → 5987.32] We love beets around here.
[5987.40 → 5987.82] BMC.
[5987.90 → 5988.68] I know all about.
[5988.68 → 5991.64] You know all about beets.
[5992.00 → 5993.26] Also getting punched in the kidneys.
[5993.96 → 5999.14] Now the other suggested autocomplete was why is my poop black?
[5999.96 → 6000.32] Mm-hmm.
[6000.32 → 6003.60] But the number one autocomplete in all of Google,
[6003.74 → 6005.28] at least for my incognito tab,
[6005.64 → 6007.50] is why is my poop green?
[6007.66 → 6008.22] So Adam,
[6008.42 → 6008.94] Angelica,
[6009.06 → 6010.86] and Matt all got it.
[6011.72 → 6013.78] People got to be figuring out why the poop's green.
[6013.78 → 6013.86] It's green.
[6013.86 → 6013.96] It's green.
[6013.96 → 6014.04] It's green.
[6014.44 → 6015.86] Two points for Adam.
[6016.04 → 6017.54] Two points for Angelica.
[6017.66 → 6018.62] Two points for Matthew.
[6018.80 → 6021.06] And that puts him over the top.
[6021.12 → 6021.92] But not only that,
[6022.36 → 6023.98] but why is my computer so slow?
[6024.16 → 6024.34] Yeah,
[6024.34 → 6025.82] that was Matt's as well.
[6025.96 → 6029.98] So he got two more points because you guys piled onto Matt.
[6030.46 → 6031.32] We all pooed,
[6031.38 → 6032.12] piled together.
[6032.30 → 6032.66] We did.
[6032.66 → 6033.02] That's great.
[6033.90 → 6035.78] So he got four points that round?
[6035.82 → 6036.74] He got four points.
[6036.82 → 6037.50] Adam gets two.
[6037.60 → 6038.34] Angelica gets two.
[6038.40 → 6042.00] That puts him over the requisite 15 with 18 points.
[6042.00 → 6044.46] Matthew Calabria is our pound-defined winner.
[6044.60 → 6045.08] Congrats, Matt.
[6045.22 → 6046.38] Is that the ultimate number?
[6046.46 → 6047.52] I feel like 18 is high.
[6048.62 → 6051.12] It's about as high as you can get because 15 is the winning amount,
[6051.24 → 6052.08] and you have to go over.
[6052.98 → 6055.08] So good job, Matthew.
[6055.08 → 6057.70] You have any final words before we call the show?
[6057.76 → 6059.54] I know we've kept you all here a long time.
[6060.20 → 6062.12] We should all go see who you get slapped.
[6062.12 → 6063.70] I think that's the takeaway here.
[6063.98 → 6064.76] We should all do it.
[6065.06 → 6065.44] We should.
[6065.50 → 6066.54] We should have like a...
[6066.54 → 6069.42] What are those things called when you stream it all at the same time?
[6069.80 → 6070.60] Yeah, stream party.
[6071.28 → 6072.36] Co-stream party.
[6072.54 → 6074.26] Just entertain me, Jerry.
[6074.32 → 6075.96] Read my definition again for that one.
[6075.96 → 6079.38] For you who gets slapped?
[6079.80 → 6080.20] Yes.
[6080.64 → 6083.04] In a world where hand gestures have gone too far,
[6083.62 → 6086.12] a group of friends vowed to change things
[6086.12 → 6089.80] and restore the old ways of simple handshakes and high-fives.
[6090.98 → 6091.42] It's like...
[6091.42 → 6092.78] That's good stuff.
[6093.32 → 6093.96] That'd be a good movie.
[6094.28 → 6096.64] I feel like if it had been released this year,
[6096.76 → 6097.56] that would be it.
[6098.26 → 6099.28] Well, you know.
[6099.42 → 6102.48] You who gets slapped?
[6102.48 → 6105.18] It kind of gives away the ending and the title, you know?
[6105.82 → 6106.78] Yeah, it kind of does.
[6107.14 → 6109.28] I did learn a lot of new words coming onto this show.
[6109.86 → 6111.36] I feel like it was an educational show.
[6111.92 → 6114.10] Yeah, well, that's what we're here for is to educate.
[6114.34 → 6115.24] That's why we play this game.
[6115.36 → 6116.16] Just pure education.
[6116.26 → 6118.38] There's no faster way, actually, to learn.
[6119.46 → 6120.68] There is no faster way.
[6121.00 → 6121.64] Than this.
[6122.78 → 6123.90] So I feel like my cheeks hurt.
[6124.00 → 6125.02] I've been smiling too much.
[6125.06 → 6127.24] I'm like, I need to do some like exercises
[6127.24 → 6128.54] because my cheeks hurt.
[6128.54 → 6133.24] So the Googles were basically money and bodily function.
[6133.82 → 6136.38] And then AI was just AI.
[6137.08 → 6138.32] AI is always just AI.
[6138.54 → 6139.40] AI is just AI.
[6139.88 → 6141.46] That was what was the...
[6141.46 → 6143.22] Something Core.
[6143.40 → 6143.94] What was it again?
[6144.20 → 6144.50] Oh, yeah.
[6144.54 → 6146.26] It was like Neurology, I think.
[6147.10 → 6147.46] Neurology.
[6147.92 → 6149.62] It was like SourceForge, but not.
[6149.68 → 6151.36] It actually sounded a lot like Neuralink to me,
[6151.92 → 6153.22] which maybe that's where it got it from.
[6153.58 → 6155.82] You know, a device implanted in the cerebral cortex
[6155.82 → 6157.66] sounds like Neuralink, something they're up to.
[6157.66 → 6160.08] I also learned that clearly I didn't have a childhood
[6160.08 → 6161.52] because I didn't know what OOBLECK was.
[6162.06 → 6162.16] No.
[6162.56 → 6163.68] Oh, my gosh.
[6163.82 → 6167.40] Well, as much as I would love to stay in, do more.
[6169.62 → 6170.28] I'm not.
[6172.90 → 6173.46] All right.
[6173.46 → 6174.72] That is our game.
[6174.94 → 6176.12] Congrats to our winner, Matthew.
[6176.32 → 6178.88] Thank you, BMC, Angelica, John Henry,
[6179.10 → 6180.06] everybody for joining us.
[6180.08 → 6181.66] This has been an absolute riot.
[6181.86 → 6184.20] There are other pounds to find game shows in the feed.
[6184.28 → 6185.64] Go find them if you enjoyed this.
[6185.64 → 6188.56] You can listen to other ridiculous games.
[6189.04 → 6190.38] And you can also find other games
[6190.38 → 6191.24] that aren't just pound to find.
[6191.36 → 6191.88] Front End Feud.
[6191.98 → 6192.72] Go for Say.
[6193.42 → 6194.28] JS Danger.
[6194.44 → 6196.50] Other such things at changelog.com
[6196.50 → 6198.38] slash topic slash games.
[6199.62 → 6200.82] That's all for this week.
[6201.06 → 6202.14] Thanks for hanging out, everybody.
[6202.38 → 6204.04] And we'll talk to you on the next one.
[6204.74 → 6205.34] Bye the beats.
[6205.52 → 6205.98] Bye, friends.
[6206.20 → 6206.98] Bye, friends.
[6207.20 → 6207.86] Bye, BMC.
[6208.02 → 6208.12] Bye.
[6209.64 → 6209.98] Bye.
[6210.06 → 6210.82] Bye his album.
[6211.10 → 6211.40] Bye my.
[6211.56 → 6212.38] Bye his music.
[6212.52 → 6212.68] Yeah.
[6213.32 → 6214.18] Bye my music.
[6214.18 → 6214.42] Bye.
[6214.42 → 6214.62] Bye.
[6214.62 → 6214.82] Bye.
[6214.82 → 6214.90] Bye.
[6214.90 → 6214.92] Bye.
[6214.92 → 6214.98] Bye.
[6214.98 → 6215.02] Bye.
[6215.02 → 6215.18] Bye.
[6215.18 → 6215.50] Bye.
[6215.50 → 6215.60] Bye.
[6215.60 → 6215.74] Bye.
[6215.74 → 6215.76] Bye.
[6215.76 → 6215.86] Bye.
[6217.30 → 6219.12] That's the changelog for this week.
[6219.46 → 6221.84] Thanks for pound defining with us.
[6222.10 → 6224.92] We hope you enjoy playing along with these game shows.
[6225.28 → 6228.84] If you want more like this, head to changelog.fm slash games.
[6229.14 → 6233.84] Thanks again to our partners at fly.io and to our sponsors of this episode,
[6234.08 → 6236.24] Heroku, Retool, and Cisco.
[6236.76 → 6239.78] Next week on the pod is going to be a little crazy.
[6240.22 → 6242.86] Adam and I are flying to Seattle for Microsoft Build.
[6242.86 → 6244.90] If you're going to be there, come find us.
[6245.28 → 6246.20] And if not, don't worry.
[6246.42 → 6251.02] We'll bring the best back with us and deliver it to your ear holes on future episodes.
[6251.46 → 6252.54] Have a great weekend.
[6252.86 → 6255.54] Leave us a five-star review to help out the show.
[6255.80 → 6257.72] And let's talk again real soon.
