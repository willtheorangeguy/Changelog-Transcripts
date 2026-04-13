[0.18 --> 4.18]  This week on the Change Log, we're talking about open source on Mars.
[4.66 --> 7.78]  Martin Woodward, Senior Director of Developer Relations at GitHub,
[8.20 --> 11.34]  joins us to talk about the new Mars badge GitHub introduced.
[11.70 --> 15.66]  This collaboration between GitHub and NASA confirmed nearly 12,000 people
[15.66 --> 19.40]  contributed code, documentation, graphic design, and more
[19.40 --> 23.00]  to the open source software that made Ingenuity's launch possible.
[23.36 --> 26.52]  Today's show is a celebration of this human achievement
[26.52 --> 31.12]  and the impact of open source on space exploration as we know it.
[31.44 --> 35.52]  Of course, big thanks to our partners Fastly, Linode, and LaunchDarkly.
[35.76 --> 39.50]  Our bandwidth is provided by Fastly. Learn more at Fastly.com.
[39.60 --> 42.12]  We love Linode. They keep it fast and simple.
[42.26 --> 44.86]  Check them out at Linode.com slash changelog
[44.86 --> 47.10]  and get your feature flags powered by LaunchDarkly.
[47.24 --> 49.06]  Check them out at LaunchDarkly.com.
[49.06 --> 58.44]  This episode of the Change Log is brought to you by our friends at Influx Data
[58.44 --> 64.62]  and their upcoming Influx Days EMEA virtual event happening May 18th and 19th.
[64.62 --> 69.86]  If you've never been to an Influx Days, it's an event focused on the impact of time series data.
[69.86 --> 74.08]  Find out why time series databases are the fastest growing database segment
[74.08 --> 76.92]  providing real-time observability of your solutions.
[77.34 --> 82.20]  Get practical advice and insight from the engineers and developers behind InfluxDB,
[82.56 --> 84.18]  the leading time series database.
[84.84 --> 87.56]  Learn from real-world use cases and deep technology presentations
[87.56 --> 89.08]  from leading companies worldwide.
[89.68 --> 93.02]  Learn more and register for free at InfluxDays.com.
[93.24 --> 95.40]  Again, InfluxDays.com.
[95.40 --> 112.78]  So we're here with Mark Wilberg.
[113.36 --> 117.30]  And Mark, you do a cool job at GitHub, leading a pretty interesting mission.
[117.30 --> 121.84]  And recently, I mean, we had a space achievement happen, powered by open source,
[122.04 --> 124.40]  in part at least, not so much in total, but in part.
[124.40 --> 129.36]  And this is a big deal, this Mars mission badge, the involvement with NASA and JPL.
[129.48 --> 131.82]  Can you kind of take us into what that's all about?
[132.22 --> 132.46]  Sure.
[132.66 --> 134.28]  What's going on open source to make us go to Mars?
[135.30 --> 137.20]  Building on the shoulders of giants, as always.
[137.48 --> 138.44]  As it always is.
[138.44 --> 138.62]  Yeah.
[138.76 --> 141.02]  It's funny, you sort of found out this news.
[141.26 --> 144.88]  Linux was running on the rover kind of thing and running on the helicopter.
[145.12 --> 146.30]  We sort of found that out.
[146.36 --> 148.28]  And I remember, I think it was end of February,
[148.58 --> 152.56]  some dev from Stripe tweeted, Nat, my boss, to sort of say,
[152.56 --> 154.80]  hey, you know, this is like the Martian code roll, isn't it?
[154.86 --> 155.70]  This is amazing.
[155.82 --> 157.14]  We've got Linux running on Mars.
[157.20 --> 157.66]  This is cool.
[157.80 --> 160.02]  And that was just, oh, that's such a good idea.
[160.24 --> 160.66]  That is cool.
[160.78 --> 162.86]  We reached out to some friends over at JPL.
[163.00 --> 165.44]  JPL, you know, been a long time sort of users of GitHub,
[165.58 --> 167.52]  a long time contributors to open source as well.
[167.60 --> 169.52]  And we reached out to some buddies over there.
[169.64 --> 171.70]  And we're like, hey, what's running on that helicopter then?
[171.74 --> 172.96]  Is that something that we could do?
[173.04 --> 174.28]  You know, is that something we could talk about?
[174.54 --> 175.42]  And they were very kind.
[175.42 --> 177.82]  They provided us a list of open source dependencies,
[178.60 --> 181.50]  the helicopter depended on, and we can dig into some of those if you want.
[181.62 --> 184.86]  And then created a badge that we sort of analyzed the projects
[184.86 --> 188.48]  and then took the exact versions that JPL would tell us that they were using
[188.48 --> 194.06]  and then analyzed those back and did a match if those people have GitHub accounts.
[194.20 --> 197.10]  And then if they do, we stuck a badge on them and saying that,
[197.26 --> 199.28]  well done, your code made it to Mars kind of thing.
[199.32 --> 202.60]  You contributed to the fix of the Ingenuity helicopter.
[202.60 --> 204.56]  And so, yeah, did that.
[204.86 --> 208.72]  And yeah, it's just over 12,000 people actually have got the badge.
[208.86 --> 209.52]  So it's pretty cool.
[209.68 --> 213.26]  Because that's like just over double how many people work at JPL as well.
[213.40 --> 217.70]  It sort of shows you the power and all the developers that you can kind of work with
[217.70 --> 221.44]  and the size of your community when you do engage with open source
[221.44 --> 224.80]  and when you contribute back as well as when you're consuming open source.
[225.00 --> 225.84]  And yeah, it's cool.
[226.04 --> 228.74]  We couldn't have done it in large, like you say, large part without them.
[228.82 --> 232.58]  Obviously the team of scientists at JPL had a large amount to do with it as well.
[232.60 --> 235.54]  And the American taxpayers, thank you for that, for funding it.
[235.70 --> 236.92]  But yeah, it's just awesome.
[237.24 --> 238.50]  That's why I said partly for sure.
[238.78 --> 239.10]  Partly.
[239.32 --> 241.48]  Not in whole, in total, but partly for sure.
[241.80 --> 244.30]  And it certainly couldn't have come together on the timescales that came together
[244.30 --> 247.82]  without building on a bunch of, JPL call them like COTS products,
[247.90 --> 250.80]  but like off-the-shelf components and things, pulling those together
[250.80 --> 253.56]  and then pulling together open source components.
[253.82 --> 257.66]  It certainly couldn't have come together as quickly as it did as a technology demonstrator
[257.66 --> 259.00]  without building on open source.
[259.08 --> 260.42]  So that's a fantastic achievement.
[260.42 --> 262.86]  And we just wanted to share it with everybody and let people know.
[263.14 --> 265.68]  And it's funny, I was listening to an episode you had with Dan, you know,
[265.72 --> 266.42]  from the Curl Project.
[266.66 --> 269.20]  And we were working on this at the time that episode got broadcast.
[269.34 --> 270.82]  I'm not sure when you recorded it, but anyway.
[271.34 --> 271.90]  I saw that tweet.
[271.98 --> 272.74]  I was like, wow, okay.
[272.86 --> 273.60]  Yeah, yeah, yeah.
[273.74 --> 276.42]  He was trying to reach out to people at JPL to sort of see if
[276.42 --> 279.42]  the random people that always bother you when you're an open source maintainer
[279.42 --> 282.30]  asking you to fill out like random compliance documents and things.
[282.36 --> 285.28]  He was asking those to, hey, did my code make it to Mars?
[285.42 --> 288.22]  And this person's so far down the procurement chain, they don't know, you know.
[288.22 --> 291.12]  So, yeah, we went and asked the people and, yeah, it turns out it did.
[291.28 --> 292.78]  And PyCurl made it to Mars.
[292.82 --> 293.46]  So that's pretty awesome.
[293.70 --> 294.18]  That's interesting.
[294.26 --> 296.34]  Now there's a process to discover that.
[296.46 --> 300.46]  Instead of being a maintainer wondering, it's more like GitHub helping to sort of
[300.46 --> 304.36]  pin back to GitHub accounts and repository commitments and whatnot.
[304.60 --> 305.38]  So, I mean, that's interesting.
[305.66 --> 308.76]  I didn't consider really that this would be a Mars code vault as well.
[308.76 --> 312.72]  We talked with John Evans, Jared did at least, talking about GitHub's Arctic code vault,
[312.82 --> 317.50]  which is an interesting topic in itself just to preserve the long-term future of our source code
[317.50 --> 321.66]  because it's really that important to leave the planet, escape velocity and all that
[321.66 --> 326.24]  to get to another planet and fly a helicopter, which is a massive human achievement to do.
[326.64 --> 327.46]  How does that play out, though?
[327.54 --> 330.96]  Is that really a code vault or is it just sort of just named that to some degree?
[331.06 --> 332.24]  Is it really that way?
[332.38 --> 333.36]  Yeah, we didn't name it that.
[333.36 --> 338.96]  We named it the Mars 2020 mission contributor or something like that because unlike the
[338.96 --> 342.66]  Arctic code vault where they've actually archived the actual source code storage and
[342.66 --> 343.84]  stuck it in the Arctic.
[343.92 --> 344.46]  Yeah, exactly.
[344.62 --> 348.10]  In Mars, they were under very, very, very strict weight limits to the grams.
[349.06 --> 350.12]  Every kilobyte counts.
[350.40 --> 352.00]  Yeah, every kilobyte counts.
[352.16 --> 356.34]  Plus, a helicopter is not the best place to put your code vault, you know, on a helicopter.
[356.98 --> 358.18]  So, yeah, so it's all compiled code.
[358.24 --> 358.66]  That's what I figured.
[358.72 --> 362.88]  And in fact, the engineering to the helicopter itself is basically, there's a bunch of papers
[362.88 --> 367.42]  on it that you can go read, but it's kind of basically two Arduinos and a Raspberry Pi
[367.42 --> 367.82]  Zero.
[368.06 --> 370.66]  Like that level of technology is what powers the helicopter.
[371.26 --> 373.78]  And the reason why there's two, so it's two microcontrollers.
[373.88 --> 379.76]  They act as flight controllers, ARM-based, and then a larger sort of Qualcomm-powered board,
[379.94 --> 382.06]  which is where Linux is running, embedded Linux.
[382.26 --> 385.82]  It's a 3.4 kernel, Lanero-based distribution, 3.4 kernel.
[386.10 --> 391.40]  And these, again, on off the shelf Qualcomm kind of dev board for building drones and things.
[391.40 --> 396.24]  And they grabbed that, and it was running Lanero 3.4, like a distribution of Linux on
[396.24 --> 396.34]  it.
[396.40 --> 397.10]  I'm like, okay, that'll do.
[397.20 --> 398.32]  It's got all the IO I need.
[398.40 --> 402.10]  It's got working cameras, because we all know how fun cameras and audio can be to get
[402.10 --> 404.12]  running on Linux at times.
[404.36 --> 406.74]  But yeah, working camera drivers, working everything.
[406.82 --> 407.12]  Let's go.
[407.20 --> 407.80]  Let's use this.
[407.98 --> 408.56]  Yeah, I took those.
[408.64 --> 410.60]  And that's what we ran with once we got the dependencies.
[410.78 --> 411.80]  All compiled down, though.
[411.80 --> 416.16]  So we asked the JPL team which open source dependencies have contributed to the success.
[416.16 --> 418.44]  So we don't have access to their code or anything like that.
[418.48 --> 422.18]  They told us the dependencies, and then we did the analysis from those.
[422.30 --> 425.76]  But they included things that were essential for the Mars mission that are actually part
[425.76 --> 428.32]  of the flight software, like Bootstrap and stuff.
[428.42 --> 430.66]  I'm guessing Bootstrap isn't running on the helicopter.
[431.08 --> 434.60]  I'm guessing that that's part of the flight control systems where they're running that and
[434.60 --> 434.88]  things.
[435.00 --> 437.76]  And some of the Python analysis stuff is definitely happening locally.
[437.76 --> 441.40]  There is Python running on Mars, for sure, but not so much in the helicopter.
[441.80 --> 441.98]  But yeah.
[442.16 --> 443.92]  So not exactly on Mars.
[444.06 --> 449.74]  In terms of the Mars mission badge, it's more like involved in getting us to Mars as part
[449.74 --> 452.10]  of this mission, to be super clear.
[452.24 --> 455.18]  Yeah, and getting the data back, analyzing that data as well.
[455.26 --> 459.66]  From the helicopter, we limited as well to the helicopter mission in particular, because
[459.66 --> 464.74]  there are actually three, I think three Linux boxes that I know of on Mars.
[464.74 --> 469.30]  The helicopter itself, then there's the radio system, the control board that it talks to
[469.30 --> 469.88]  on the rover.
[470.22 --> 474.90]  And then there's another Linux box that we're not actually including because it's currently
[474.90 --> 477.30]  not being used as part of the Ingenuity mission.
[477.48 --> 482.60]  You know, when you saw the rover landing, you saw those amazing videos of the parachute,
[482.80 --> 486.62]  and you saw the parachute flying, and you saw the videos as it's coming down, all that
[486.62 --> 487.10]  sort of stuff.
[487.74 --> 489.88]  That's actually running on a Linux.
[489.88 --> 495.08]  It's a ruggedized PC that's powering that one, because it, again, had a bunch of USB
[495.08 --> 498.02]  cameras plugged into it, because it was all working, and they could get it going.
[498.22 --> 501.88]  And so because it wasn't mission critical, they could run on what they call a Class D
[501.88 --> 503.28]  system, like Ingenuity.
[503.42 --> 505.36]  So it's a lower risk, experimental.
[505.66 --> 509.26]  If it didn't work, they just didn't get video of a sky crane flying away and all that sort
[509.26 --> 510.32]  of stuff, but it wasn't the end of the world.
[510.62 --> 513.84]  But that's running a 415 kernel, I think.
[513.94 --> 518.16]  And that's actually got Python on and FFmpeg and all those cool things, because it took the
[518.16 --> 522.72]  video, and it did the compressing on board the little PC before sending it over to the
[522.72 --> 522.98]  rover.
[523.32 --> 525.34]  So I'm a bit of a space nerd, as you probably tell.
[525.46 --> 526.04]  I'm liking it.
[526.16 --> 526.68]  Yeah, keep going.
[526.80 --> 527.34]  Yeah, yeah, yeah.
[527.44 --> 529.16]  This is, we can talk about the open source.
[529.28 --> 532.98]  But so I did my degree in physics, which is why it's an astronomy and all that sort of
[532.98 --> 533.10]  stuff.
[533.14 --> 534.16]  So kind of, this is my background.
[534.26 --> 537.86]  But anyway, it did all the compression on the ruggedized PC and sent it over, and then
[537.86 --> 538.58]  they sent it back.
[538.64 --> 543.30]  Because the rover itself's like a, it's radiation hardened, like power PC, is what the rover
[543.30 --> 543.70]  runs.
[543.70 --> 549.44]  And so it's like a 1990s era Mac kind of thing is what it's basically running on, but
[549.44 --> 552.94]  takes a lot of power because it's like a big radiation hardened processor.
[553.36 --> 557.34]  So the helicopter is the most powerful computer on Mars, but like a hundred times.
[557.58 --> 563.08]  The rover itself is a hundred times slower than the helicopter in terms of processing, but
[563.08 --> 565.14]  it's 10 times faster than the previous rovers.
[565.38 --> 566.72]  You see progress going along.
[566.84 --> 568.12]  But yeah, it's good stuff.
[568.34 --> 572.10]  And that's running two Arduinos and a Raspberry Pi Zero?
[572.48 --> 572.96]  Equivalent.
[572.96 --> 575.14]  It's actually, it's a Qualcomm chip, not a Broadcom chip.
[575.24 --> 577.66]  So yeah, but it's a Qualcomm chip that runs on the helicopter.
[577.80 --> 580.28]  And that runs as a navigation computer.
[580.84 --> 585.48]  Because over here on Earth, drones navigate using GPS and all that sort of stuff.
[585.66 --> 587.78]  But yeah, it ain't got no GPS on Mars.
[588.08 --> 590.42]  So the way it navigates is using actual reckoning.
[590.56 --> 595.72]  So, you know, looking at dead reckoning, basically, how far are we moving, you know, using a gyroscope
[595.72 --> 597.98]  that's built into this same board, this drone board.
[597.98 --> 600.94]  And it has a black and white camera that looks down.
[601.36 --> 605.00]  And the black and white camera takes, I think it's a number of frames per second.
[605.14 --> 605.38]  I can't remember.
[605.48 --> 607.48]  It's like 50 frames per second or whatever, or 500.
[607.68 --> 607.98]  I can't remember.
[608.20 --> 610.50]  But it takes a bunch of black and white photos looking down.
[610.50 --> 612.32]  And then it looks at surface features.
[612.50 --> 618.02]  And then it maps the tracking of surface features and uses that to basically dead reckon where it is on the surface.
[618.38 --> 620.76]  That's why the navigation computer needs to be powerful.
[620.76 --> 623.72]  Because it's taking all those images, looking down.
[624.00 --> 626.50]  It's handling all the processing from all the I.O.
[626.84 --> 628.70]  And then it talks to the microcontrollers.
[628.74 --> 629.50]  So there are two microcontrollers.
[630.50 --> 634.06]  And it talks to them to say, move me up, move me forward where it wants to go.
[634.20 --> 634.82]  Move me down.
[635.14 --> 638.42]  And those flight control computers are the things that are actually keeping it in the air.
[638.44 --> 639.50]  Because they need their real time.
[639.58 --> 641.78]  So they need to work so fast and respond to things.
[641.98 --> 643.36]  So that's kind of how all that works.
[643.52 --> 647.14]  And the reason there's two of them is in case one of them argues with the other.
[647.28 --> 649.54]  Because, again, none of this is radiation hardwood and stuff.
[649.54 --> 652.26]  It's just literally you've got a block of batteries.
[652.76 --> 654.54]  And then all four sides are PCBs.
[655.28 --> 657.78]  Very lightweight, like really small PCBs around the batteries.
[657.98 --> 658.92]  And then it's a heater.
[659.32 --> 660.98]  And then you've got the motors and the propeller and things.
[661.08 --> 662.56]  It's mostly batteries from what I've seen.
[662.80 --> 663.12]  So, yeah.
[663.48 --> 664.80]  But those microcontrollers, if they did,
[664.82 --> 666.52]  disagree with each other, they reboot.
[668.12 --> 670.48]  They switch it off and on again in mid-air.
[670.50 --> 671.10]  That's going to be pretty fast.
[671.74 --> 673.82]  And so that's how they handle it.
[673.86 --> 675.08]  I don't know if it's actually rebooted or not.
[675.10 --> 677.82]  But that was the plan as far as I could read from looking at these papers.
[678.08 --> 678.26]  Wow.
[678.48 --> 678.82]  It was cool.
[679.08 --> 679.74]  It was a cool mission.
[679.74 --> 680.52]  It was amazing.
[680.62 --> 681.46]  It was an amazing achievement.
[681.82 --> 685.92]  And remember the photo of the black hole at the Event Horizon?
[686.10 --> 686.28]  Yeah.
[686.34 --> 689.40]  The Event Horizon telescope team took a picture of this black hole.
[689.68 --> 690.78]  Did you do a show about that?
[690.94 --> 691.28]  I can't remember.
[691.58 --> 692.16]  I don't remember either.
[692.38 --> 693.38]  We talked about it.
[693.44 --> 693.80]  I'm not sure.
[693.80 --> 694.12]  Yeah.
[694.18 --> 695.32]  It might have been mentioned.
[695.58 --> 695.74]  Yeah.
[695.90 --> 698.48]  Because I recall talking about it somehow, some way on a show.
[699.12 --> 703.60]  We do have our transcript open source on GitHub, so we can grab those to see what's in there for that.
[703.72 --> 708.34]  But we can confirm that a little bit easier than Daniel could confirm his code running on Mars.
[708.60 --> 708.76]  You know?
[709.10 --> 709.46]  Yeah.
[709.62 --> 709.98]  That's right.
[709.98 --> 710.88]  Yeah, there we are.
[710.88 --> 712.88]  Yeah, it's similar to that.
[713.02 --> 719.72]  With the Event Horizon telescope, we looked who was all involved in helping the team pull together this image of a black hole.
[719.94 --> 724.12]  It's a massive distributed team, and they were doing all that work on GitHub as well.
[724.44 --> 732.34]  It ended up being like 21,500 people, roughly, had contributed to all the, you know, it was all Python and all SciPy and NumPy and all this sort of stuff.
[732.34 --> 732.66]  Mm-hmm.
[732.66 --> 736.46]  And it was, yeah, over 20,000 people had ended up contributing to this project.
[736.68 --> 740.48]  And back then, we didn't have this notion of the badges of what we could have done.
[740.56 --> 743.30]  So when we were doing the Mars stuff, we were thinking, oh, this is cool.
[743.34 --> 744.24]  We've got to do something here.
[744.26 --> 745.90]  So we decided to do a badge.
[745.98 --> 746.12]  Yeah.
[746.12 --> 751.12]  And then we made it in achievements because we wanted it to be a nice, colorful badge rather than the old black and white badges we used to have.
[751.20 --> 753.20]  Is this badging thing new?
[753.80 --> 755.22]  I mean, GitHub was social coding.
[755.36 --> 756.80]  Like, that was, like, what it came out as.
[756.86 --> 757.04]  Yeah.
[757.16 --> 761.84]  And a lot of the social sites, like achievements, badges, is kind of a thing that they do.
[761.98 --> 769.50]  I remember Coderwall, back in the day, was kind of like a badging sister site to GitHub, in a sense, not related in terms of the people operating it.
[769.54 --> 771.44]  But it was kind of like they would link back and forth to each other.
[771.44 --> 778.02]  But, you know, Stack Overflow, Dev Platform, a lot of these social sites, like badges, badges, win stuff, achievements.
[778.20 --> 780.04]  And that's supposed to, like, encourage use.
[780.30 --> 783.56]  But I don't remember GitHub really having anything like that until recently.
[783.72 --> 785.70]  We had highlights.
[786.06 --> 787.82]  So, like, the Arctic Code Vault was a highlight.
[788.04 --> 790.80]  And if you're a sponsor as well, that was a highlight before.
[791.16 --> 794.42]  But we didn't have anything that was quite as big or prominent.
[794.94 --> 800.90]  So with the Mars achievement, with the Mars highlight, we did the initial designs.
[800.90 --> 803.76]  And the black and white sort of helicopter things looked a bit boring.
[804.06 --> 806.66]  And then the designer did this amazing color version.
[806.82 --> 807.96]  Oh, that's so cool.
[808.02 --> 808.92]  We've got to use that.
[809.34 --> 812.42]  And so we kind of, well, let's do an achievement section and we'll bring that in.
[812.70 --> 816.28]  Very mindful of, though, is we don't want to, like, this is obviously new for this.
[816.38 --> 817.66]  We added in the Arctic Code Vault.
[817.80 --> 820.52]  We sort of backdated it as an achievement now rather than a highlight.
[820.70 --> 820.72]  As an achievement, yeah.
[820.72 --> 821.44]  Similar responses.
[821.64 --> 822.86]  So you get a nice colorful badge.
[823.12 --> 826.08]  But what we don't, there, you're being rewarded for things that you've done.
[826.08 --> 830.88]  Like, what we want to be careful of is going too far down the gamification front.
[831.04 --> 835.02]  Because, you know, we don't want to encourage burnout with open source maintaining.
[835.08 --> 837.24]  Like a streak badge would be counterproductive.
[837.28 --> 837.70]  Yeah, exactly.
[837.88 --> 838.00]  Yeah.
[838.34 --> 838.64]  Nuh-uh.
[839.10 --> 843.08]  And then anyway, we've got the legendary kind of the green graph of commits kind of thing.
[843.16 --> 846.52]  That's good enough as a streak badge encouragement for the new people.
[846.52 --> 846.98]  Yeah, totally.
[846.98 --> 850.62]  Whereas you're more experienced, you get quite proud of seeing the gaps in there.
[850.62 --> 854.04]  And the fact that I'm always, you know, and you say, oh, yeah, look, I took a proper vacation.
[854.52 --> 855.76]  I can prove it to my family.
[855.90 --> 858.00]  I actually didn't log into GitHub this weekend.
[858.90 --> 865.54]  I saw somebody recently who is, somebody who is more deep in the code, became a founder and then CEO.
[865.80 --> 866.86]  And you can see their GitHub graph.
[866.94 --> 868.06]  They shared this on Twitter recently.
[868.46 --> 874.82]  Where when they were CEO and founder, or I guess more CEO, and this is no knock against CEOs, by any means.
[874.82 --> 876.60]  It's just this person's history.
[876.60 --> 881.28]  Where you can see their graph essentially being more white and less green, which is how it works.
[881.66 --> 887.88]  As they became this new founder, stepping away from their CEO role into this new founder role, where they're sort of coding more and exploring more.
[888.00 --> 890.38]  You can see that the green come back, essentially.
[890.52 --> 893.28]  Like, this is my journey from CEO to founder, for example.
[893.58 --> 893.78]  Yeah.
[893.96 --> 894.80]  And you see that.
[894.90 --> 895.58]  It's a journey.
[895.70 --> 896.20]  It's informant.
[896.28 --> 898.32]  Did you hear about the Skyline project?
[898.62 --> 900.72]  Have you heard about that one that we did as well?
[900.84 --> 901.02]  Mm-mm.
[901.02 --> 901.52]  Oh, wow.
[901.74 --> 902.98]  We did this project.
[902.98 --> 910.78]  If you go to skyline.github.com, it was a thing we did just in the new year where we kind of had a bit of fun with the commit graph.
[910.92 --> 913.76]  Kind of one of these in-house, look at it, isn't this fun kind of thing?
[913.92 --> 922.20]  We did it because we were shipping contribution graphs to sort of some of the, you know, some of the top maintainers, some of the people who've just done amazing work over the year.
[922.20 --> 923.32]  Like Dan, for example.
[923.60 --> 926.72]  We sent them a steel contribution graph.
[926.80 --> 928.50]  We 3D printed in steel.
[928.86 --> 931.20]  Oh, I did see a few of those coming up on Twitter.
[931.34 --> 932.00]  People were sharing.
[932.00 --> 933.74]  A version of a contribution graph.
[933.78 --> 934.62]  And we sent it to them.
[934.68 --> 940.84]  But we wanted a link for them to go to to be able to kind of share it with their friends because it's quite hard to share a picture.
[941.12 --> 942.12]  So we built this site.
[942.26 --> 946.74]  Originally, it was some dodgy PM code that then, like, got made pretty by our awesome team.
[946.88 --> 947.24]  Yeah.
[947.38 --> 947.86]  It shipped that.
[948.06 --> 948.62]  And it's cool.
[948.68 --> 949.98]  And you can sort of zoom around in it.
[949.98 --> 953.90]  If you've got an Oculus, you can go in and, you know, go in around it in 3D and things.
[953.98 --> 954.46]  So that's cool.
[954.62 --> 954.84]  That is cool.
[954.84 --> 962.20]  But what I like about that is that we're actually encouraging, like, it looks better if there is variance.
[962.50 --> 971.58]  You know, like the most valuable real estate like Manhattan has, the most valuable real estate in Manhattan is the stuff around a gap, around Central Park or whatever.
[971.58 --> 974.38]  And it's the same with it should be the same with contribution.
[974.48 --> 975.68]  It looks better when there's variance.
[975.80 --> 977.60]  It looks better if there isn't too much stuff at the weekend.
[977.86 --> 983.34]  If there is some gaps and you've got the peaks and then you can, like, think, oh, yeah, I remember that.
[983.42 --> 986.08]  That was when I was coming to this release of my library or whatever.
[986.08 --> 990.40]  Or that was when I was coming up to this particular demo or go live or whatever it was.
[990.44 --> 993.12]  And you can look at those highlights and kind of, oh, yeah, I remember those.
[993.20 --> 994.44]  But also look at the gaps.
[994.58 --> 996.78]  Yes, that was an amazing vacation.
[996.96 --> 998.28]  What a great Thanksgiving that was.
[998.64 --> 999.12]  It's good stuff.
[999.26 --> 1002.70]  So is this the kind of projects that you head up as the executive director?
[1003.08 --> 1004.50]  Oh, sorry, I'm reading the wrong thing.
[1004.66 --> 1009.12]  You were the executive director of the .NET Foundation, but you're senior director of DevRel.
[1009.82 --> 1011.94]  Is this like the Skyline project, this thing?
[1011.98 --> 1013.32]  Is this like what DevRel is all about?
[1013.32 --> 1016.44]  Or is there other things that are...
[1016.44 --> 1016.82]  DevRel-y.
[1017.10 --> 1018.88]  ...tangential to these kind of cool...
[1018.88 --> 1020.90]  Yeah, what is DevRel exactly?
[1021.44 --> 1021.86]  DevRel-y.
[1022.02 --> 1022.44]  I like that.
[1022.78 --> 1026.44]  Yeah, so it's different, again, from what it is in quite a lot of places.
[1026.78 --> 1032.64]  Because quite a lot of places, if you're doing DevRel, you're trying to raise awareness of your product amongst developers.
[1033.54 --> 1034.24]  That's like your GitHub.
[1034.44 --> 1035.46]  Help people use it.
[1035.54 --> 1038.66]  Exactly, but your GitHub is a different problem.
[1039.14 --> 1041.84]  So what we try to do, what my team's doing, it's a small team.
[1041.84 --> 1044.88]  And we're just basically trying to help open source maintain...
[1044.88 --> 1055.00]  We spend a lot of our time talking to open source maintainers and also just regular developers and helping them get the most out of GitHub and trying to see what we can do to help them be successful.
[1055.14 --> 1063.46]  So in some ways as well, it's like a traditional DevRel because you're going out, you're talking to people all the time, you're talking to developers, you're helping them use stuff.
[1063.46 --> 1068.74]  Hey, did you know you could go, you do this and I'll save you a bunch of time and you can, you know, do all that or something.
[1068.86 --> 1070.26]  So you can help people.
[1070.44 --> 1075.32]  And then you can also bring that feedback back into the engineering team as well because we kind of sit on the engineering team.
[1075.46 --> 1083.54]  So we come in and we sort of say, hey, you know, this pull request thing, like it would be great if you could do auto-merge or sponsors.
[1083.54 --> 1093.96]  It would be great if X, Y, if you could do one-time payments in sponsors, like we're hearing this around and we're just an extra data point then for the people who are building the features and they can help make the product better over time, hopefully.
[1094.28 --> 1095.54]  And it's trying to have these connections between...
[1096.40 --> 1098.88]  Because GitHub's great and it's amazing it's scaled.
[1099.14 --> 1102.94]  But for a lot of people, a lot of people don't really think of GitHub as a thing.
[1103.38 --> 1104.26]  GitHub is just GitHub.
[1104.42 --> 1105.14]  It's just there.
[1105.32 --> 1106.24]  It's like water.
[1106.24 --> 1120.78]  And because, again, because of the sort of large scale that GitHub's working at, sometimes with our, like the maintainers who are running massive projects, they wouldn't know anybody at GitHub they could go talk to to go help them with a problem.
[1121.30 --> 1122.72]  And that's bad.
[1122.90 --> 1124.50]  Like these people are incredibly busy.
[1124.76 --> 1130.72]  And, you know, so I want to kind of try and help put the human face in, make sure the team are out there putting the human face in front of the company.
[1130.72 --> 1136.56]  And so when a maintainer has an issue or a problem and they're having trouble, you know, we've got full on support and everything else.
[1136.66 --> 1138.28]  And that's what we should all use all the time.
[1138.68 --> 1144.92]  But also I want them to know that they know people at GitHub if they need to help or if they want to give some feedback or something.
[1145.04 --> 1147.06]  So what's the best way for a maintainer to get your attention?
[1148.02 --> 1154.64]  They can, for personally, as I say, at martinwoodwood on Twitter or just martinwoodwood at gilb.com on email if you want to drop me a line.
[1154.84 --> 1156.38]  Very happy for people to reach out.
[1156.60 --> 1156.98]  And they do.
[1156.98 --> 1160.22]  Probably easier than if you're at Nat Friedman.
[1160.44 --> 1161.24]  That also works.
[1161.40 --> 1164.84]  But it's generally better, you know, not to go straight to the Nat.
[1165.00 --> 1169.08]  You know, he does get a lot of tweets sent to him and he tends to forward them along to me.
[1169.32 --> 1171.72]  So, yep, just hit me up anyway that way.
[1171.84 --> 1175.70]  Or, you know, as I say, the community support, the community forums are all great places.
[1175.82 --> 1178.06]  That's where we tend to hang out as well a lot of the times.
[1178.48 --> 1181.18]  If you need particular attention, feel free to just reach out for sure.
[1181.18 --> 1191.64]  Yeah, speaking of Nat, I saw a recent Twitter exchange between Max Lynch talking about when you view a file in the commit history, being able to actually see that file at the exact point in the history.
[1192.04 --> 1192.16]  Yeah.
[1192.30 --> 1194.16]  And he just said, number one feature I want to see on GitHub.
[1194.40 --> 1196.48]  And he at GitHub on Twitter.
[1196.48 --> 1199.68]  And then at the very end, CC at Nat Friedman.
[1200.34 --> 1204.26]  And then like three days later, Nat responds, new button below.
[1204.40 --> 1207.82]  And then boom, you can kind of see that this is being driven in the wild.
[1208.06 --> 1210.84]  So person on Twitter dating their best request.
[1210.98 --> 1212.94]  He's the CEO founder of Iconic Framework.
[1213.02 --> 1219.96]  So somebody out there in open source, a maintainer, of course, but getting the attention of Nat and making that possible pretty quickly.
[1219.96 --> 1226.12]  Yeah, that one actually, it's one of those ones where it kind of had been in the hopper for a week or two.
[1226.36 --> 1227.60]  But yeah, it was OK.
[1227.82 --> 1228.70]  It wasn't like a three day.
[1228.78 --> 1231.14]  Hey, let's do this now because Max says it is.
[1231.28 --> 1231.48]  Yeah.
[1231.64 --> 1233.16]  Well, let's let Max think that.
[1233.28 --> 1233.94]  But yeah, no.
[1234.26 --> 1234.90]  OK, gotcha.
[1234.98 --> 1236.56]  It might have even been a feature already.
[1236.76 --> 1237.12]  Wasn't it?
[1237.16 --> 1238.38]  I mean, I feel like I've done that.
[1238.66 --> 1239.06]  View file.
[1239.20 --> 1240.96]  No, you could view the problem.
[1241.22 --> 1244.78]  I mean, it drove me mad for ages because I was one of the ones that put it on the backlog, actually.
[1244.88 --> 1245.06]  OK.
[1245.06 --> 1250.26]  You could go in and you could browse the history at that point in the commits.
[1250.36 --> 1253.38]  You hit browse history in a web UI of a file.
[1253.54 --> 1254.92]  It would show you where that file changed.
[1255.32 --> 1258.90]  But then all you could do was browse to the repository at that point in time.
[1259.06 --> 1261.74]  And then you had to go navigate back to the file and find it.
[1261.80 --> 1262.78]  It was infuriated.
[1263.08 --> 1271.12]  So yeah, somebody called Carl Delgo added a button which takes you straight to that file at that point in history, which is like, why did we never have that?
[1271.30 --> 1271.78]  It's, you know.
[1272.08 --> 1274.30]  That's exactly what you wanted as the UX anyway.
[1274.30 --> 1274.60]  Exactly.
[1274.60 --> 1279.68]  But there's a lot of these like little small things that you can do that really help improve the quality of life of everybody.
[1280.00 --> 1283.48]  And that's one of the things I enjoy the most is just like going out, listening and chatting to people.
[1283.58 --> 1283.94]  Oh, yeah.
[1283.98 --> 1286.28]  If we just did this tiny little thing over here.
[1286.36 --> 1287.72]  Like, what did we do the other day?
[1287.74 --> 1288.32]  It was just simple.
[1288.54 --> 1291.98]  It was, you know, on a pull request or when you're assigning it.
[1292.52 --> 1296.12]  Like, if you're assigning a pull request, your name's at the top now.
[1296.26 --> 1299.10]  And it's there before you like, well, duh, of course it is.
[1299.10 --> 1304.94]  But again, there's little things like that that just speed things up rather than just typing your name in every time and having to find it.
[1304.98 --> 1306.16]  Let's just put your name on top.
[1306.16 --> 1308.86]  Using code inside of a pull request.
[1308.86 --> 1315.62]  If you want to like include some code in the code snippet inside of the title of the pull request or you want to improve markdown.
[1315.76 --> 1317.44]  And it's just all these little things.
[1317.54 --> 1325.96]  So while we're building the big features, while we're building things like GitHub code spaces or while we're building the next version of actions and improving actions and all that sort of good stuff.
[1325.96 --> 1333.74]  We want to do those, but we can't forget the paper cuts we quite often call them, you know, like just general quality of life improvements.
[1333.74 --> 1336.04]  How can we make the platform faster?
[1336.12 --> 1338.10]  How can we make it better for everybody to use?
[1338.18 --> 1340.70]  How can we improve maintainers lives?
[1340.74 --> 1343.48]  Because again, these people are just doing awesome stuff.
[1344.08 --> 1351.54]  The genuinely like most maintainers are the nicest people you'll ever meet in the world, as you know, because you talk to them all the time.
[1351.58 --> 1353.14]  Like they're just lovely people.
[1353.42 --> 1353.50]  Yeah.
[1353.50 --> 1358.14]  You know, you get people who volunteer, you get the people who like stand up in the community and volunteer and go do stuff.
[1358.20 --> 1359.44]  And then you get the people who take anything.
[1359.72 --> 1360.32]  They just give.
[1360.42 --> 1363.84]  They just give all the time, sometimes too much more than they've got.
[1364.12 --> 1373.92]  It's just trying to do what you can to help these people, help them like be able to do things fast, to help them be able to spend more time with fingers on keyboards and less time taking care of stuff they don't really want to worry about.
[1374.18 --> 1375.04]  At the place of value.
[1375.14 --> 1375.74]  That's the job.
[1375.88 --> 1378.00]  It's the best job in the world because you just get to have fun.
[1378.04 --> 1378.68]  You get to talk to people.
[1378.74 --> 1379.60]  You get to go build stuff.
[1379.60 --> 1381.66]  You get to help people, you know, use things.
[1381.66 --> 1388.26]  And then you get to go talk to JPL occasionally and do fancy Mars badges and nerd out over the hardware that's running in space.
[1388.38 --> 1389.30]  And it was awesome.
[1389.30 --> 1398.34]  This episode is brought to you by Retool.
[1398.66 --> 1405.74]  Retool is a local platform built specifically for developers that makes it fast and easy to build internal tools.
[1405.74 --> 1413.60]  Instead of building internal tools from scratch, the world's best teams from startups to Fortune 500s are using Retool to build their internal apps.
[1414.00 --> 1419.74]  Assemble your app in 30 seconds by dragging and dropping from the complete set of powerful pre-built components.
[1420.18 --> 1427.70]  From there, you write custom code, connect any data source, API, and build custom logic and queries to create exactly the right tools for your business.
[1428.06 --> 1432.70]  Spend your time getting UI in front of your stakeholders, not hunting down the best React table library.
[1432.70 --> 1438.12]  Retool is also highly hackable, so you're never limited by what's available out of the box.
[1438.42 --> 1441.70]  If you can write it in JavaScript and an API, you can build it in Retool.
[1442.04 --> 1445.18]  Try Retool out for yourself at retool.com slash changelog.
[1445.32 --> 1448.62]  Again, retool.com slash changelog.
[1448.62 --> 1465.90]  So the timing of this whole thing was really funny for us.
[1465.90 --> 1471.06]  Like you said, we had that episode with Daniel Stenberg of Curl, and we were speculating about whether or not I was on Mars.
[1471.18 --> 1473.50]  And Adam and I were both pretty sure, like, hey, you're on Mars.
[1473.64 --> 1474.86]  You know, we just got to get some confirmation.
[1475.06 --> 1476.32]  Daniel probably thought he was as well.
[1476.32 --> 1476.50]  Yeah.
[1477.04 --> 1483.14]  And of course, I think it was just days later that this whole announcement came out, and maybe days later after the episode came out.
[1483.18 --> 1486.30]  So we had a lot of listeners who had just listened to that conversation, and then here it was.
[1486.38 --> 1488.70]  It was really cool, and Daniel had this great chart.
[1488.80 --> 1493.22]  I'm not sure if you saw the chart he put out, where he's like, number of planets that Curl runs on,
[1493.28 --> 1497.22]  and it's like, all this years where it's just one, it's a flat line, up until this year.
[1497.28 --> 1498.02]  And it's like, two.
[1498.22 --> 1499.60]  And it just launches up to two.
[1499.60 --> 1502.38]  So, I mean, he was just tickled to have that confirmation.
[1502.64 --> 1511.36]  And I'm sure there's many other people, like you said, around 12,000 that got the badge, also probably tickled to find out, hey, you know, you've contributed to this awesome mission.
[1511.46 --> 1518.00]  So you want to tell us, in addition to Curl, and you mentioned Python generally, some of the other projects that are involved in ingenuity?
[1518.00 --> 1518.40]  Yeah.
[1519.00 --> 1527.40]  On that graph, I saw another one of those graphs, by the way, which was planets with the highest ratio of working audio drivers in Linux, and like Mars is at 100%.
[1527.40 --> 1529.00]  So, yeah, there is that.
[1530.06 --> 1531.06]  That's a good one, too.
[1531.16 --> 1531.84]  I like that one.
[1532.06 --> 1532.62]  That's good.
[1532.72 --> 1538.00]  Yeah, I mean, so there's a bunch of, like, you know, in the scientific community, Python is massively big.
[1538.00 --> 1553.26]  So, obviously, in a lot of the analysis of the data that comes back, that's a lot of Python, that's a lot of, like, SciPy and NumPy and all those sorts of projects that allow you to do big data analysis, as well as things, you know, some of the charting, like Matplotlib.
[1553.40 --> 1562.96]  I saw the maintainer of Matplotlib, like, saw a Matplotlib graph on screen that proved the helicopter had taken off.
[1562.96 --> 1572.42]  That was really weird, was watching Mission Control during the analysis of the data as it was inbound, because you sort of see them bringing up GitHub, which everyone's at GitHub's like, ah, this is amazing.
[1572.64 --> 1585.50]  And then, yeah, you see people using, like, executing Python commands, executing charts, and then somebody stuck the altitude data into Matplotlib and then brings up this graph on screen of going up to three meters and then back down again, kind of thing.
[1585.54 --> 1586.90]  So, that was really cool.
[1587.02 --> 1590.06]  It was just great to see, kind of, the recognition.
[1590.06 --> 1599.76]  You know, we, as well as the stuff for doing the data analysis and the data transfer, obviously, curl used in data transfer between devices and all that sort of stuff.
[1599.94 --> 1604.84]  There's also all the things on the analysis side, which is where a lot of that Python code runs.
[1604.98 --> 1609.78]  And then in, just in rendering of that stuff and doing what they call, like, the flight control system.
[1610.00 --> 1611.94]  So, that's where you've got a website.
[1612.10 --> 1615.08]  Everybody needs a website to be able to show data internally and all this.
[1615.08 --> 1620.52]  So, that's where you've got kind of bootstrap and Elasticsearch and some of those sorts of applications.
[1620.76 --> 1621.28]  But, yeah, it's great.
[1621.68 --> 1624.18]  And then another project that's used very, very heavily.
[1624.56 --> 1626.24]  So, that's on the Python side.
[1626.36 --> 1636.52]  A lot of that Python, while there is Python running on Mars, we're told, the vast majority of, like, the Python stuff that we mentioned in the helicopter projects running planet side, Earth side.
[1636.52 --> 1642.30]  But F Prime is a project that NASA have up on GitHub, and that's a seed project.
[1642.72 --> 1651.90]  It's a framework for building flight control systems that's used in the helicopter, but it's also used in, like, CubeSats.
[1652.14 --> 1654.82]  That's primarily where it had come from, was, like, a CubeSat system.
[1655.06 --> 1656.58]  And it's a framework that they open source.
[1656.74 --> 1663.92]  So, the entire code base of that helicopter, you can't go send a pull request to make the helicopter do donuts or something, you know, sadly.
[1664.06 --> 1664.68]  That's too bad, yeah.
[1664.70 --> 1665.42]  Yeah, too bad, yeah.
[1665.42 --> 1670.84]  But the entire flight control system for that actual instance of F Prime that's running isn't all available.
[1670.98 --> 1672.26]  Some of it's JPL proprietary.
[1672.44 --> 1673.50]  You know, it's not publicly available.
[1673.68 --> 1678.32]  But the F Prime framework that they use to build that flight control system is.
[1678.42 --> 1683.74]  And you can take that F Prime framework and the people over at, oh, I'm trying to remember the name of the company.
[1684.08 --> 1685.14]  Oh, it's just blank my name.
[1685.24 --> 1687.18]  It's where they bought the laser altimeter from.
[1687.42 --> 1687.96]  And I'm blanking.
[1688.12 --> 1693.04]  It's a shop I've been to many times to spend ridiculous amounts of money on random bits of Raspberry Pi hardware.
[1693.04 --> 1698.14]  You can take the F Prime project and run it on a Raspberry Pi locally.
[1698.30 --> 1705.54]  You can take it and run it in, like, different systems locally and have it running and build your own simulated environments or use real hardware.
[1705.54 --> 1712.24]  And we're seeing, like, there's this massive boom of kind of space tech, you know, as access into space is getting cheaper.
[1712.38 --> 1716.06]  And we're starting to see a bunch of these startups getting into space technology now.
[1716.06 --> 1729.18]  And so while the Mars mission is, like, the first mission where consumer-grade electronics hardware has kind of made it onto the surface of another planet and it's proving itself, consumer-grade electronics hardware has been running for a long time in orbit.
[1729.60 --> 1731.28]  And it's been working fine.
[1731.54 --> 1733.88]  And, you know, and so you're sort of seeing more and more those sorts of things.
[1734.02 --> 1739.14]  So I think there's a lot more open source in space than we probably know and that we probably, you know, even we're aware of.
[1739.14 --> 1744.32]  And there'll be more and more as we get, you know, more and more cube sets and more and more access into space.
[1744.52 --> 1745.38]  So it's cool.
[1745.66 --> 1747.46]  Open source is not just one this planet.
[1747.56 --> 1748.82]  It's winning the universe, dude.
[1749.04 --> 1749.30]  Yeah.
[1749.80 --> 1750.20]  Right.
[1750.72 --> 1760.16]  I was even thinking even in our local atmosphere, you know, with a lot of the military-grade drones and stuff, there's a lot of open sources penetrated the drone market like crazy as well.
[1760.40 --> 1762.08]  So all over the place.
[1762.08 --> 1769.18]  They used was this Qualcomm demo board, which is basically was a board for building drone hardware.
[1769.18 --> 1772.96]  And it's a very lightweight, like sort of credit card size, two-sided PCB.
[1773.26 --> 1775.32]  And that was the base of this of their platform.
[1775.70 --> 1785.50]  So that was all sort of drone hardware, but the helicopter, it's a counter-rotational thing because of they couldn't do like a quadcopter or something like that because the propellers need to be so big to run in the atmosphere.
[1785.86 --> 1789.52]  And there's only a certain amount of room that they could take under the rover's belly.
[1789.74 --> 1791.52]  So that's why they ended up with that design.
[1791.52 --> 1795.68]  Is that what differentiates a helicopter from a drone is the quad, the four?
[1795.88 --> 1796.32]  I don't know.
[1796.38 --> 1797.62]  I don't think there is actually.
[1797.84 --> 1798.08]  Yeah.
[1798.38 --> 1799.72]  Because people overuse that word.
[1799.84 --> 1799.98]  Yeah.
[1800.10 --> 1807.28]  Like from my reading, drones is kind of one of these words like hackers that really people don't often use in the real world kind of thing.
[1807.42 --> 1807.52]  Yeah.
[1807.62 --> 1809.72]  The people in the field don't tend to use it as much.
[1809.76 --> 1816.84]  It tends to be people outside the field talking about it because drone can be anything that's autonomous and sort of self-managing kind of like is the rover a drone?
[1816.84 --> 1816.96]  Yeah.
[1817.32 --> 1826.08]  But I think people when these would like when my my my 70 year old father talks about drones, he's talking about one of those quadcopter or exocopter thing that.
[1826.24 --> 1826.40]  Right.
[1826.54 --> 1831.58]  Might not even be autonomous, might be flown by radio control, but they think of it as a drone, even though it's been.
[1831.58 --> 1831.94]  Yeah.
[1832.18 --> 1832.92]  Stick controlled.
[1832.92 --> 1836.02]  The blue correct term is unmanned aerial vehicle.
[1836.34 --> 1836.90]  UAV.
[1837.06 --> 1837.52]  There we go.
[1838.36 --> 1839.02]  You got to say that.
[1839.34 --> 1839.36]  Unmanned.
[1839.52 --> 1839.78]  Yeah.
[1839.90 --> 1840.80]  Aerial vehicle.
[1841.08 --> 1841.94]  Unmanned aerial vehicle.
[1841.94 --> 1842.22]  Okay.
[1842.50 --> 1842.74]  Yeah.
[1842.94 --> 1845.00]  But people call drones like that.
[1845.04 --> 1846.10]  And that's the UAVs.
[1846.18 --> 1848.10]  That's and that's like the military grade and all that sort of stuff.
[1848.26 --> 1851.18]  But people call like DGI kind of thing.
[1851.26 --> 1852.42]  They call that, you know, that's a drone.
[1852.42 --> 1853.50]  DGI calls it a drone themselves.
[1853.62 --> 1856.02]  Not like just people like the company even calls it that.
[1856.08 --> 1856.22]  Right.
[1856.32 --> 1856.88]  Yeah, exactly.
[1857.50 --> 1860.06]  But that's not a like doesn't run in autonomous mode all that time.
[1860.10 --> 1861.38]  It's like kind of like a fly by wire.
[1861.52 --> 1861.86]  Yeah, totally.
[1861.86 --> 1865.88]  Well, I think they're starting to have they're starting to have some they can fly themselves sometimes.
[1865.88 --> 1869.08]  Like there's modes, but like it's controlled by a remote generally.
[1869.38 --> 1869.44]  Yeah.
[1869.44 --> 1869.62]  Yeah.
[1869.84 --> 1878.76]  But if you've ever tried to fly one of those without like the computer helping you, it's I built one once and tried to fly it like myself and it didn't stay in one piece for very, very long.
[1878.88 --> 1881.14]  So, yeah, the computer is doing a lot to help you.
[1881.20 --> 1882.86]  So I guess it's fly by wire like a plane.
[1883.84 --> 1884.16]  Mm hmm.
[1884.66 --> 1890.80]  In regards to Daniel on this two planets thing and low Earth orbit and drones and where code might be.
[1890.80 --> 1891.58]  I responded back.
[1891.70 --> 1900.16]  I said, hey, I know curls on Mars not because of this confirmation, but I would like to also think it's probably on the ISS or in low Earth orbit with other space things.
[1900.28 --> 1901.02]  I mean, there's more hope.
[1901.18 --> 1905.34]  And then we also have the Artemis mission happening soon, which is this mission to back to the moon.
[1905.82 --> 1905.92]  Yeah.
[1905.92 --> 1914.78]  I got to consider like how, you know, with badges and this achievements thing, how will GitHub continue to track open source, not on the planet, essentially?
[1915.30 --> 1918.02]  Low Earth orbit, ISS, the moon, Mars.
[1918.88 --> 1919.14]  Yeah.
[1919.14 --> 1920.60]  I think the Artemis one is great.
[1920.66 --> 1923.10]  So if you hadn't read that, that's NASA mission to the moon.
[1923.28 --> 1923.48]  Yeah.
[1923.60 --> 1926.22]  And that's really interesting because it's so much closer.
[1926.60 --> 1930.38]  And so you've only got like eight minutes delay rather than an hour's delay of communication.
[1930.96 --> 1934.24]  And, you know, modern, you can build on a bunch of this has already confirmed.
[1934.34 --> 1937.02]  It's going to use some of the same lessons that we've learned from this rover.
[1937.32 --> 1938.26]  So that's fantastic.
[1938.26 --> 1944.78]  In terms of how GitHub are tracking it, like we can do like one offs to this sort of thing because it's just cool.
[1945.00 --> 1950.12]  And we celebrate this amazing achievement of powered flight on another planet, which is awesome.
[1950.48 --> 1954.48]  It doesn't scale once that becomes common and, you know, once that becomes every day.
[1954.58 --> 1959.64]  So what we're trying to do is help people see their dependencies.
[1959.64 --> 1971.58]  And then what I'd love to do is do some stuff that help like gave more visibility to maintainers about like where their stuff was being used or how much it was being used.
[1971.68 --> 1975.56]  You throw something out into the world and then like six years later, somebody sends you a pull request.
[1975.70 --> 1981.36]  And then you learn that actually they've been taking a critical dependency on this for their entire lives as far as they're concerned.
[1981.56 --> 1985.10]  You didn't know anybody but you was using this particular bit of code.
[1985.20 --> 1987.10]  Like I think we've all had that kind of experience.
[1987.10 --> 1992.40]  So it'd be very, very cool to kind of get some feedback loops going on there in terms of people using it.
[1992.52 --> 1999.78]  And when you've got things like actions coming into play as well, you can see the potential there would be amazing if you could kind of say, oh, hey, people who are dependent on my release.
[1999.94 --> 2003.84]  Let's go try the new release and see if it breaks your code, that sort of stuff.
[2003.96 --> 2006.36]  So, yeah, there's lots of opportunities, I think, in the future.
[2006.62 --> 2007.36]  That would be cool for sure.
[2007.56 --> 2008.72]  Yeah, we should see the planet.
[2008.84 --> 2011.36]  Like you're talking about co-running like International Space Station.
[2011.46 --> 2013.06]  There's a thing called AstroPie.
[2013.06 --> 2017.40]  There are a couple of Raspberry Pis running on the International Space Station from ESA.
[2017.82 --> 2023.96]  And kids can like send up code to run on a Raspberry Pi in nearer for a bit on the International Space Station.
[2024.20 --> 2024.60]  Well, that's neat.
[2024.72 --> 2024.94]  So, yeah.
[2025.08 --> 2026.08]  So, Raspberry Pi is in space.
[2026.34 --> 2031.86]  So, Kirl is almost 100% multiple copies of Kirl running on the space station.
[2031.98 --> 2034.68]  I was speculating more with McGann because he's like, you know, just planets.
[2034.82 --> 2038.30]  And I'm like, great achievement, of course, knocking this slide that Jared had mentioned from Daniel.
[2038.30 --> 2040.92]  But more like it's probably more than just you think.
[2041.02 --> 2044.32]  I mean, we've heard about, I believe, China landing on an asteroid, I think.
[2044.46 --> 2047.26]  I pay attention to some space science news.
[2047.48 --> 2049.46]  I think there's an asteroid landing to some degree.
[2049.50 --> 2051.76]  So, I can imagine that where you can't confirm that.
[2051.82 --> 2054.54]  But speculation is interesting because it's a source of motivation.
[2054.78 --> 2055.88]  As you said, the feedback loop.
[2056.02 --> 2056.14]  Yeah.
[2056.20 --> 2058.42]  I think that we all do things in this world sometimes.
[2058.42 --> 2060.26]  And we're generous and we put it out there.
[2060.28 --> 2063.14]  And sometimes, as you said before, beyond what we're capable of doing.
[2063.14 --> 2069.94]  But it's that feedback loop and it's that motivation because I think of it like when you ask a child in school or whatever, like, hey, what do you want to be when you grow up?
[2070.32 --> 2074.08]  Fireman, police officer, doctor, veterinarian, astronaut, right?
[2074.30 --> 2077.86]  We might not all make it to astronaut status, but our code might.
[2078.38 --> 2078.42]  Yeah.
[2078.86 --> 2079.10]  Yeah.
[2079.30 --> 2080.34]  It's amazing.
[2080.78 --> 2083.72]  But I just like just anyone using your stuff.
[2083.88 --> 2086.46]  There's two things that kind of motivate you, isn't there, when you're creating things.
[2086.64 --> 2088.26]  There's A, what it does.
[2088.46 --> 2090.36]  So, you create a bit of code and then you run it.
[2090.36 --> 2094.68]  And you're like, wow, this is cool when you keep clicking the button 10 times because you're just impressed that it even works at all.
[2094.92 --> 2102.16]  But then you also have the seeing other people using your code, like 65 million people using GitHub every day.
[2102.26 --> 2103.34]  You kind of get used to that.
[2103.34 --> 2108.76]  We were all giggling like schoolchildren when we see them using it during the NASA mission control.
[2108.90 --> 2109.80]  That's GitHub.
[2110.00 --> 2112.58]  That's like, that's the button that I did, you know.
[2112.64 --> 2115.20]  And it's just amazing seeing people use your stuff.
[2115.20 --> 2123.62]  And so, the more we can help people know when their stuff is being used, then hopefully there is that reward of, hey, yeah, isn't this cool?
[2123.72 --> 2124.36]  You're being used.
[2124.72 --> 2132.56]  And then what we also need to do, of course, is help companies especially be more cognizant of the open source dependencies that they've got.
[2132.56 --> 2139.66]  And then, like, think about that and try and help them make sure that they're supporting some of their open source dependencies.
[2139.92 --> 2140.34]  Help it.
[2140.44 --> 2142.88]  That's what you've spoken to Devin about, sponsors and things.
[2142.96 --> 2147.38]  That's where kind of some of the motivation for that comes from, but also showing dependency trees.
[2147.54 --> 2150.34]  So, you can think, what open source have I got a critical dependency on?
[2150.44 --> 2153.88]  What am I doing to help make this sustainable in the future?
[2154.36 --> 2155.82]  How can I contribute back there?
[2155.82 --> 2162.12]  And the minute we're kind of leaving money on the table, that we could be helping people to do more work on the projects that they love.
[2162.26 --> 2164.18]  So, yeah, we're trying to do that as well.
[2164.52 --> 2172.78]  I also see, like, the Arduino and the Raspberry Pi you mentioned on the International Space Station, that the Ingenuity was powered by these microcontrollers.
[2172.94 --> 2175.10]  Like, that's something that I can go buy today.
[2175.24 --> 2175.40]  Yeah.
[2175.46 --> 2176.52]  It's kind of representation.
[2176.72 --> 2185.70]  It's like, if you want to be able to influence not only just this world, but humanity's possibility of exploration of space, well, you can go and buy a Raspberry Pi today.
[2186.70 --> 2188.62]  You know, you can play on the same kind of hardware, for example.
[2189.40 --> 2191.68]  And you can advance the state of the art as well.
[2191.78 --> 2194.54]  You can figure out how to do inertial navigation.
[2194.88 --> 2201.40]  You can do these machine learning applications that are looking for surface features and then showing which direction they're moving in and all that sort of stuff.
[2201.40 --> 2205.98]  Like, you can advance the state of the art, which then other people can use to go build other stuff.
[2206.22 --> 2209.38]  And what's great is that it's not like competition either.
[2209.46 --> 2215.38]  You look at the countries that were contributing to F-Prime and all the projects that got the Mars badge.
[2215.38 --> 2220.74]  Like, nearly half of the contributors were based in the US that contributed to those projects.
[2220.88 --> 2225.28]  But a huge chunk of contributions to those libraries didn't come from the United States.
[2225.46 --> 2230.10]  And whereas previously these sorts of missions would be kind of like national, rah, rah, aren't we amazing?
[2230.22 --> 2230.74]  What can we do?
[2230.80 --> 2231.18]  Kind of thing.
[2231.18 --> 2237.30]  It becomes a lot more about the science and a lot more about what humanity can do together, which is what the scientists have always wanted.
[2237.44 --> 2238.84]  Sometimes the politicians get in the way.
[2238.94 --> 2243.92]  But it's just amazing when you see the scale of international collaboration, international cooperation that happens.
[2244.16 --> 2244.86]  None of it.
[2244.94 --> 2246.90]  So we could put a helicopter on Mars.
[2246.98 --> 2249.58]  It was done to solve problems and everybody come together.
[2249.58 --> 2257.18]  And then it was by doing that and by sharing the goodness that we've got out there and by the generosity of people by saying, you know, you might find this useful.
[2257.40 --> 2260.68]  Then somebody from JPL can come along and go, oh, that's a cool building block.
[2260.74 --> 2261.66]  That's a cool bit of Lego.
[2261.80 --> 2266.98]  You know, stick them together and build a helicopter, land it on another planet and take it for some flights.
[2267.56 --> 2268.44]  So, yeah, it's just tremendous.
[2269.02 --> 2269.14]  Yep.
[2269.44 --> 2271.74]  You've got to love just being part of that community as well.
[2271.82 --> 2273.76]  And the people that got the badge is awesome.
[2273.76 --> 2278.64]  And seeing the reactions from a lot of these people, like, they're like, I don't know what the people are.
[2278.64 --> 2279.70]  I should not know what code is.
[2279.76 --> 2280.50]  I don't know what the planet is.
[2280.52 --> 2281.24]  Like, that's cool.
[2281.48 --> 2284.92]  But what's also cool is seeing the reactions of people.
[2284.96 --> 2285.72]  I've got teenage kids.
[2285.82 --> 2286.94]  I've seen the reactions of those.
[2287.12 --> 2288.98]  And I'm like, wait, did you have something to do with that?
[2289.04 --> 2290.04]  Like, Mars mission?
[2290.14 --> 2290.70]  Not really.
[2290.82 --> 2291.38]  Like, I didn't.
[2291.50 --> 2292.78]  None of my code made it to Mars.
[2292.88 --> 2294.62]  But I talked to somebody whose code was there.
[2294.90 --> 2296.56]  Like, I know somebody who knows somebody.
[2296.82 --> 2297.46]  Yeah, exactly.
[2297.60 --> 2298.00]  I know somebody.
[2298.50 --> 2299.10]  Now I'm cool.
[2299.10 --> 2303.04]  But now I'm also, like, getting into software development, getting into open source is cool.
[2303.04 --> 2305.28]  And like, oh, yeah, I see where this is going.
[2305.48 --> 2309.14]  So having these moments is great for us as a community as well to kind of celebrate.
[2309.38 --> 2310.40]  And look at what we're doing.
[2310.50 --> 2311.02]  This is amazing.
[2311.02 --> 2311.32]  Exactly.
[2311.60 --> 2312.60]  This is celebrating a win.
[2312.90 --> 2313.08]  Yeah.
[2313.34 --> 2315.82]  This is celebrating a win, which I'm a huge fan of.
[2315.86 --> 2316.56]  And Jared knows this.
[2316.66 --> 2320.70]  Like, I think too often, not so much we don't celebrate the wins, but like, we don't give them enough attention.
[2321.00 --> 2324.54]  And, you know, we talked about the gamification and sort of hedging that to some degree.
[2324.60 --> 2326.08]  And I don't think that's what you're doing here at all.
[2326.22 --> 2330.26]  And I'm glad you asked that question, Jared, because we don't want GitHub to become a game.
[2330.34 --> 2332.86]  It may be behind the scenes if you make it that.
[2333.04 --> 2336.62]  To win open source or to become an awesome maintainer or whatever it might be that you want to achieve.
[2336.90 --> 2340.14]  But too often do we just not celebrate the wins and take the time for that.
[2340.16 --> 2341.04]  I think that's what that is.
[2341.34 --> 2341.44]  Yeah.
[2341.72 --> 2345.64]  And you've got, what, nearly 12,000 people that contributed code to this.
[2345.96 --> 2348.18]  That's a lot of people involved in open source.
[2348.40 --> 2349.60]  And that's a big win for them.
[2349.62 --> 2352.02]  And it's a big win for, I suppose, open source at large.
[2352.02 --> 2352.46]  Yeah.
[2352.66 --> 2359.80]  Because we recognized everybody in that project who commits up to the period where JPL said, this is the commit that we use.
[2359.86 --> 2361.20]  You know, this is the version that we used.
[2361.20 --> 2368.20]  And so I saw some people who were like, well, all I did was fix a one line change in a readme or a doc or something like that.
[2368.30 --> 2369.40]  And, you know, now I've got the badge.
[2369.58 --> 2370.32]  That's awesome.
[2370.66 --> 2371.58]  Like, that's cool.
[2371.72 --> 2372.76]  Like, you helped.
[2372.90 --> 2377.88]  You helped make this project be a success no matter how small you might think your contribution was.
[2377.88 --> 2386.32]  That line in the documentation you might have fixed might have been the line that helped the team at JPL understand how to use this particular library and help make it more accessible to them.
[2386.54 --> 2387.10]  It's just cool.
[2387.34 --> 2388.74]  And so let's celebrate the wins.
[2388.88 --> 2394.62]  Let's try not to be too much, you know, you see a few comments about their code not making it.
[2394.80 --> 2396.06]  And it's like, whatever.
[2396.06 --> 2398.56]  So you've got to celebrate the wins and just be successful.
[2399.06 --> 2402.54]  Well, I was excited about Arctic Code Vault as an achievement for me.
[2402.78 --> 2404.56]  And I got to say, I've fixed a lot of readmes.
[2404.88 --> 2408.68]  And I went to my profile very excited and no Mars badge for me.
[2408.72 --> 2409.66]  So I was pretty bummed.
[2409.80 --> 2410.68]  Oh, man, I'm sorry.
[2410.84 --> 2412.82]  If it helps, I didn't have a Mars badge either.
[2412.86 --> 2413.54]  I'm joking, of course.
[2413.54 --> 2417.22]  And you can guarantee that was the first thing I did when I got access to the query results.
[2417.38 --> 2417.90]  Am I in it?
[2418.02 --> 2418.30]  No.
[2418.54 --> 2418.96]  Damn it.
[2419.10 --> 2420.56]  What's the point of doing all this work?
[2420.84 --> 2422.48]  I didn't expect the Arctic Code Vault either.
[2422.66 --> 2424.30]  I just, not everybody gets that one.
[2424.30 --> 2426.66]  And so I was like, yeah, that was a little easier to get.
[2426.74 --> 2429.94]  You had to have your code in by a certain day and make sure you could uncheck it.
[2429.96 --> 2432.26]  You could opt it out of the Arctic Code Vault if you wanted.
[2432.40 --> 2436.16]  But yeah, it does worry me because like most of the time I seem to be trying to delete my
[2436.16 --> 2437.40]  code out of code bases nowadays.
[2437.40 --> 2441.22]  I've got like, I mean, I think I've got one change that's in GitHub, which is like to help
[2441.22 --> 2443.30]  Gradle do something like super small.
[2443.42 --> 2444.66]  It was tiny, tiny, tiny thing.
[2444.84 --> 2445.60]  Now we are where we are.
[2445.68 --> 2446.22]  So that's great.
[2446.50 --> 2452.30]  So we used to do this badge, a changelog badge, and we would give it to you on your readme
[2452.30 --> 2453.72]  where it'd be like your episode number.
[2453.72 --> 2455.66]  And it was just a nice way to link to your episode.
[2455.90 --> 2460.06]  And so I used to open pull requests on a lot of repos, a lot of popular repos because they'd
[2460.06 --> 2461.50]  come on the show and we'd do it for you.
[2461.54 --> 2462.58]  So it was the easy button.
[2462.86 --> 2467.66]  And so I got a lot of merges onto, you know, pretty prominent, but just like, I'm like
[2467.66 --> 2469.06]  literally just adding the changelog badge.
[2469.10 --> 2471.52]  I'm not improving anything or even fixing a typo.
[2471.58 --> 2475.68]  And so I thought, well, there's an outside chance that I've put a badge on one of these.
[2475.78 --> 2479.78]  And so I actually had high expectations to be on Mars and I got to my profile.
[2479.92 --> 2480.94]  Nope, I'm not on there.
[2480.94 --> 2482.22]  I'm like, ah, so close.
[2482.88 --> 2483.20]  Yeah.
[2483.38 --> 2484.90]  You need to have more Python people on.
[2484.90 --> 2485.22]  Clearly.
[2485.56 --> 2488.64]  If we're going to do more of these things, that seems to be a little cool kids around.
[2488.88 --> 2489.36]  Or curl.
[2489.70 --> 2490.84]  Like you've got a curl on now.
[2490.96 --> 2491.30]  We're good.
[2491.40 --> 2491.98]  Curls everywhere.
[2492.28 --> 2492.70]  Curls in there.
[2492.70 --> 2492.88]  Yeah.
[2493.14 --> 2495.86]  One of my favorite things I like to do is you probably do the same.
[2496.02 --> 2500.54]  Well, you probably did is go to the license on things you're using and go see how many
[2500.54 --> 2501.88]  people, you know, in that list.
[2501.88 --> 2505.10]  Like let's see, go, you know, see how many of my friends I can find in this particular
[2505.10 --> 2507.24]  third party usages, text file or whatever.
[2507.62 --> 2508.50]  Daniel's always up there.
[2508.60 --> 2510.94]  You know, he has his email address in his third party usages.
[2511.04 --> 2511.24]  Yes.
[2511.62 --> 2511.74]  He's mad.
[2512.48 --> 2514.40]  We talked about that, which you probably know.
[2514.48 --> 2517.84]  We cover some of those things where he got random emails because of his email being out
[2517.84 --> 2519.96]  there so much in the license and whatnot.
[2520.20 --> 2523.36]  Oh, he had the one about somebody thought you'd hacked him or something like that.
[2523.68 --> 2523.92]  Yeah.
[2524.18 --> 2524.30]  Yeah.
[2524.30 --> 2525.12]  An Instagram hack.
[2525.20 --> 2526.62]  Again, he's so nice.
[2526.74 --> 2527.90]  He actually answers people.
[2528.02 --> 2529.88]  He actually replies back to them like that.
[2530.00 --> 2531.36]  You find this across the board.
[2531.56 --> 2535.58]  Most of the maintainers you talk to are just such lovely humans and just take time and are
[2535.58 --> 2535.94]  nice.
[2536.06 --> 2539.52]  And especially once they've got large communities around them, because the reason they have a community
[2539.52 --> 2544.14]  is because they've been so nice, so inclusive and so welcoming to people and they just can't
[2544.14 --> 2547.72]  help themselves even when it's emails that are obviously from confused people.
[2547.72 --> 2548.50]  So, yeah.
[2569.52 --> 2573.46]  This episode is brought to you by our friends at O'Reilly.
[2573.82 --> 2577.46]  Many of you know O'Reilly for their animal tech books and their conferences, but you may
[2577.46 --> 2579.94]  not know they have an online learning platform as well.
[2580.30 --> 2584.74]  The platform has all their books, all their videos, and all their conference talks.
[2585.10 --> 2590.14]  Plus, you can learn by doing with live online training courses and virtual conferences, certification
[2590.14 --> 2595.56]  practice exams, and interactive sandboxes and scenarios to practice coding alongside what you're
[2595.56 --> 2595.86]  learning.
[2595.86 --> 2601.70]  They cover a ton of technology topics, machine learning, AI, programming languages, DevOps,
[2602.22 --> 2608.38]  data science, cloud, containers, security, and even soft skills like business management
[2608.38 --> 2609.80]  and presentation skills.
[2609.94 --> 2611.72]  You name it, it is all in there.
[2612.02 --> 2615.68]  If you need to keep your team or yourself up to speed on their tech skills, then check
[2615.68 --> 2617.20]  out O'Reilly's online learning platform.
[2617.72 --> 2621.30]  Learn more and keep your team skills sharp at O'Reilly.com slash changelog.
[2621.30 --> 2623.68]  Again, O'Reilly.com slash changelog.
[2625.86 --> 2643.36]  So, Mark, you mentioned that you got some education behind you.
[2643.66 --> 2644.86]  Physicist is what I understand.
[2645.26 --> 2649.86]  So, you're in a good place to be, I suppose, in DevRel with GitHub and all this fun stuff
[2649.86 --> 2652.86]  happening around science and space and whatnot.
[2652.86 --> 2654.08]  What other fun things are happening?
[2654.20 --> 2657.84]  Like, I mean, as a physicist or someone who studied it, kind of give me an understanding
[2657.84 --> 2661.44]  of what your education was and then how that dovetails into some of the, I guess, things
[2661.44 --> 2667.08]  you get to tinker with or play with or communities to sort of encourage in their open source journeys.
[2667.60 --> 2667.94]  Yeah, sure.
[2668.00 --> 2669.48]  So, I did my undergrad in physics.
[2669.82 --> 2673.52]  So, I was always doing a bunch of sort of astronomy and a bunch of that research.
[2673.66 --> 2677.86]  So, originally, I was like playing with Hubble Space Telescope data and doing data analysis
[2677.86 --> 2678.30]  of that.
[2678.30 --> 2683.54]  And that was back in the days where to even having a TCP stack wasn't guaranteed.
[2683.78 --> 2688.42]  And using, trying to do a bunch of that sort of stuff back then involved getting DVDs sent
[2688.42 --> 2693.58]  over and paying for them with Hubble Space data on them and putting them in the one computer
[2693.58 --> 2695.06]  in the lab that has a SCSI interface.
[2695.06 --> 2699.24]  So, you could actually load that data up and do some analysis, write some code.
[2699.40 --> 2700.70]  It was very hard to share that code.
[2700.70 --> 2705.82]  And that's why kind of astronomers and physicists and, you know, all the scientific community
[2705.82 --> 2710.24]  have been kind of quick to latch on to open source and always been sharing a bunch of their
[2710.24 --> 2710.42]  code.
[2710.52 --> 2714.34]  That's obviously where a lot of the internet infrastructure came along as well, especially
[2714.34 --> 2717.02]  if it was from a lot of those networks of sharing those things.
[2717.28 --> 2717.84]  So, we did that.
[2718.10 --> 2723.16]  And then me personally went from doing kind of doing some of that sort of stuff to, I had
[2723.16 --> 2724.38]  like real jobs for a while.
[2724.48 --> 2728.26]  I had like working in banks and insurance companies and all the good stuff that you do.
[2728.26 --> 2733.34]  But when I was doing those jobs, I was always involved in open source on the side to, you
[2733.34 --> 2737.98]  know, scratch that itch that everybody has that you're trying to do, whether that be using
[2737.98 --> 2739.84]  a different language or using a different thing.
[2739.90 --> 2740.82]  And so, that's what we do.
[2741.00 --> 2744.32]  And so, I was doing some open source, ended up getting together with a few friends who
[2744.32 --> 2745.64]  were also interested in the same project.
[2745.72 --> 2747.14]  And we ended up building a company around it.
[2747.22 --> 2750.92]  It's a company called Team Price, but it was a super small, like five person company.
[2751.12 --> 2755.04]  But we started on open source, working together, did a commercial application.
[2755.54 --> 2757.72]  And then we ended up selling that to Microsoft, actually.
[2757.72 --> 2759.54]  Funnily enough, about like 10 years ago.
[2760.06 --> 2763.62]  So, we got acquired as this little five person startup coming in.
[2764.04 --> 2767.72]  I figured I would last a couple of years, just do my time and then move on because I
[2767.72 --> 2770.74]  was coming from this Java, Eclipse-y, kind of open source-y world.
[2771.04 --> 2774.76]  And I didn't, you know, back then, it wasn't really kind of the thing it is now.
[2775.18 --> 2776.38]  And so, yeah.
[2776.48 --> 2780.96]  And then I was around, helped kind of change, you know, you've interviewed a cast of characters
[2780.96 --> 2782.70]  on that side of things in the past.
[2782.70 --> 2784.22]  So, don't need to dig into that.
[2784.36 --> 2788.48]  But, you know, worked on that team, helping change Microsoft and kind of change how we,
[2788.68 --> 2789.80]  how they approach open source.
[2789.96 --> 2790.96]  Brought Git into the company.
[2791.16 --> 2793.58]  And then I created, I was the one that created Microsoft's GitHub account.
[2793.68 --> 2793.96]  There you go.
[2794.02 --> 2794.80]  There's my client to say.
[2795.14 --> 2795.62]  So, yeah.
[2795.66 --> 2797.26]  I was running on my credit card for a little while.
[2797.72 --> 2797.92]  Yeah.
[2797.94 --> 2799.60]  And then did the open source stuff and then moved over.
[2799.86 --> 2802.76]  So, and then, and then came to GitHub like February last year.
[2802.86 --> 2803.76]  So, that was a great move.
[2803.84 --> 2807.96]  And now I'm just, I feel like I'm home because everybody cares about the same things I care about.
[2807.96 --> 2808.94]  You know, we're all remote.
[2809.10 --> 2809.70]  It's fantastic.
[2809.84 --> 2810.62]  So, I love it over here.
[2811.08 --> 2814.74]  But in terms of like what's new, there's a lot of stuff going on in the science space.
[2814.96 --> 2817.62]  I mentioned like a lot of these space tech startups.
[2817.84 --> 2823.24]  But even what we're seeing is the more established players like NASA and people like that and ESA.
[2823.52 --> 2828.64]  And they're finding ways to use open source technology and to use more rapid technology
[2828.64 --> 2830.54]  and integrate them as part of missions.
[2830.66 --> 2836.32]  So, that's what you saw with Ingenuity was part of the main Perseverance mission.
[2836.32 --> 2842.16]  And NASA have these like levels of risk that they like class A, class B, C, D.
[2842.66 --> 2848.44]  And the rover itself is a class B mission in terms of like how important it is in terms of scientific results
[2848.44 --> 2849.18]  and all that sort of stuff.
[2849.64 --> 2853.76]  So, that's a very, very high level of compliance they do to manage that risk.
[2854.24 --> 2859.38]  But instruments on it, like the helicopter is classed as kind of an instrument that's attached to the rover.
[2859.64 --> 2862.86]  They can be of different risk categories because if they fail, so what?
[2862.86 --> 2866.84]  As long as it doesn't hit the rover, then the helicopter, you know, they haven't lost anything.
[2866.96 --> 2867.50]  They've tried it.
[2867.64 --> 2868.24]  You know, it failed.
[2868.32 --> 2868.70]  It's fine.
[2868.76 --> 2868.96]  Whatever.
[2869.04 --> 2869.86]  We didn't lose anything.
[2869.98 --> 2875.26]  So, as long as it doesn't affect the main mission, then they've got a little bit more risk, a bit more to play with.
[2875.64 --> 2878.42]  So, that's why the helicopter can happen.
[2878.50 --> 2883.10]  That's why the things like the DVR box, you know, the thing that the Linux box that recorded the video landing.
[2883.54 --> 2884.94]  That's why those things can happen.
[2885.34 --> 2891.88]  But then you also get them doing stuff like there's a James Webb telescope that's coming up, which is this kind of a successor to Hubble.
[2892.02 --> 2899.58]  So, back when I, before I started my career, back when I was doing analysis on Hubble data, this new James Webb telescope is going to be launching soon.
[2899.58 --> 2904.68]  And that's, you know, massive, massive investment from NASA and, you know, set to be like Hubble.
[2905.00 --> 2911.02]  Hubble's revolutionized astrophysics and revolutionized so many areas of humanity's knowledge.
[2911.12 --> 2913.18]  And the James Webb telescope is set to do the same thing.
[2913.44 --> 2915.60]  And it's got a bunch of technologies to keep things cold.
[2915.74 --> 2918.40]  The platform itself is very class A.
[2918.52 --> 2918.90]  You know what I mean?
[2918.92 --> 2922.16]  It's like super, like they're making sure everything works.
[2922.16 --> 2926.60]  And they don't particularly want to send astronauts to go fix mirrors and things like they had previously.
[2926.90 --> 2930.64]  But on the ground, the innovation never stops.
[2930.84 --> 2934.96]  You know, you send hardware, you send a platform up in space and you can get data from it.
[2935.04 --> 2941.60]  But just like when you're collecting data from IoT devices or from little, I've got a little Raspberry Pi set up my windowsill here,
[2941.68 --> 2945.48]  collecting data about like plant because I'm trying to grow some basil and I fail.
[2945.64 --> 2950.00]  So I'm sciencing that and I've stuck a Raspberry Pi on it because now I'm bound to grow basil.
[2950.42 --> 2951.62]  Exactly, with Alex, yeah.
[2951.62 --> 2954.60]  I was paying attention to that little grow lab thing.
[2954.68 --> 2957.48]  I was like, I should try that because I love tinkering.
[2957.96 --> 2959.44]  So just like that, you can innovate.
[2959.62 --> 2961.96]  You can keep innovating on the data and the analysis data.
[2962.40 --> 2968.40]  And so with the James Webb telescope, you know, it's this big, important, massive mission with like billions of dollars being invested into it.
[2968.48 --> 2973.78]  On the ground, all that analysis and all just like with the Event Horizon telescope,
[2974.16 --> 2977.76]  all the analysis done using Python, using lots of, you know, machine learning,
[2978.00 --> 2981.06]  using lots of new, like different data techniques and things.
[2981.06 --> 2986.80]  And it helps really kind of innovate and extend the life of these missions way past people,
[2986.92 --> 2988.06]  what people originally thought.
[2988.30 --> 2993.00]  And the scientific community and open source has got so much in common because with open source,
[2993.24 --> 2994.18]  code is what matters.
[2994.36 --> 2996.44]  You know, like talk is easy in open source.
[2996.44 --> 2998.10]  As we all know, everyone can talk.
[2998.34 --> 3002.96]  But if you show up and you regularly show up and you bring code and you help all the time,
[3003.00 --> 3005.62]  then that's when people value what you're saying, what you're doing.
[3005.62 --> 3011.72]  In the scientific community, this whole notion of peer review and the whole notion of showing your workings is what's important.
[3012.08 --> 3017.40]  And so open source is amazing for that because you can show exactly how we analyze this data.
[3017.54 --> 3021.40]  You can give the code to the people so they can run exactly these experiments again,
[3021.68 --> 3025.18]  take the data, run their analysis through it, look for issues, you know,
[3025.18 --> 3027.54]  make sure you haven't made mistakes and repeat things.
[3027.54 --> 3031.96]  So we see more and more scientific papers actually linking to GitHub repos, which is just super cool.
[3032.14 --> 3032.94]  So, yeah.
[3033.32 --> 3034.30]  And so I love it.
[3034.32 --> 3038.20]  And it's like an electronics kind of physics nerd, not a comp sci person.
[3038.20 --> 3042.96]  So I always have a bit of C++ envy kind of thing of people who did proper comp sci degrees,
[3042.96 --> 3048.02]  whereas I was just sat like coding Fortran in a lab in physics and just doing coding on the side at home.
[3048.20 --> 3050.48]  But yeah, I love doing what I do.
[3050.70 --> 3051.52]  Seems like it served you well.
[3051.74 --> 3052.28]  It was good.
[3052.46 --> 3055.56]  The Fortran side wasn't probably not the most useful thing I've ever done.
[3055.56 --> 3059.24]  But I was building websites also to show my results of Fortran.
[3059.32 --> 3060.18]  And that definitely is.
[3060.36 --> 3062.82]  I definitely paid off because that was back in the mosaic days.
[3062.88 --> 3063.62]  That's how old I am.
[3063.76 --> 3063.92]  But yeah.
[3064.08 --> 3067.46]  So you mentioned you only have like one commit as of late, which was a deletion.
[3067.82 --> 3070.92]  Did you get to break the code editor out or is it mostly hobby stuff?
[3071.00 --> 3072.94]  I mean, at work, you're the senior director.
[3073.22 --> 3073.70]  Oh, yeah.
[3073.78 --> 3078.28]  I mean, on GitHub, GitHub, it's mostly just little fixes and things they let me get away with.
[3078.38 --> 3082.32]  And then my code is just all hobby stuff generally or demo stuff or showing things off.
[3082.32 --> 3083.82]  So like some examples.
[3083.82 --> 3085.60]  I'm building the Raspberry Pi.
[3085.66 --> 3088.02]  This is with Alex Ellis, the GrowLab project right now.
[3088.18 --> 3092.00]  So if you want to check out GrowLab, I can send you a link for the show notes or whatever.
[3092.12 --> 3100.86]  But it's using Raspberry Pis and cameras and sensors and just having for some fun and doing data capture and sending that data up and doing that.
[3100.98 --> 3102.38]  So I'm playing with that in a minute.
[3102.58 --> 3105.68]  I've got like my Raspberry Pi cluster behind me.
[3105.92 --> 3107.06]  You can't quite see it in your case.
[3107.12 --> 3110.00]  But I've got a Raspberry Pi cluster that I'm trying to play with at the moment.
[3110.00 --> 3113.18]  I've got like, you know, automate my Christmas trees.
[3113.58 --> 3116.98]  Obviously, everybody hooked them up to GitHub Actions, you know, whatever.
[3117.22 --> 3117.92]  Just a bit of fun.
[3118.08 --> 3126.00]  I mostly spend most of my time kind of helping other people with their open source projects and helping make sure they can be successful and try to get them what they need.
[3126.16 --> 3129.76]  In fact, one of the things that we're doing is we're bringing all these maintainers together.
[3129.76 --> 3135.04]  We're trying to do the best thing that we can do to do an unconference given COVID times.
[3135.46 --> 3138.76]  So we're running this thing called GlobalMaintainerSummit.github.com.
[3139.00 --> 3146.66]  And what we're going to try and do is bring maintainers together and like have a big group therapy session in a way, but also share knowledge.
[3146.74 --> 3148.82]  Because, again, maintainers are awesome.
[3149.26 --> 3153.60]  And people have developed different tricks for handling different situations and different people.
[3153.68 --> 3159.04]  So we kind of want to bring those people together and provide a space for maintainers to get together.
[3159.04 --> 3165.04]  So if you are a maintainer of a big project, then feel free to come along to GlobalMaintainerSummit.github.com.
[3165.70 --> 3167.04]  I actually got the domain name maintain.
[3167.78 --> 3172.04]  I misspelled maintainers the other day and spelt it as maintain nerds.
[3172.70 --> 3172.80]  Oh.
[3173.44 --> 3175.64]  And that was too good a typo to miss.
[3175.72 --> 3177.26]  So I went and registered all those domains.
[3177.50 --> 3182.26]  So if you do maintain nerds as well, that'll forward you off to GlobalMaintainerSummit because I just thought that was an awesome,
[3182.46 --> 3187.06]  an awesome domain name to add to my collection of domain name side projects that I'll probably never, ever get to.
[3187.06 --> 3187.70]  That's a nice one.
[3187.90 --> 3188.86]  But worth collecting.
[3189.24 --> 3189.42]  Yeah.
[3189.98 --> 3190.38]  Yeah.
[3191.02 --> 3191.76]  I'll need it one day.
[3192.08 --> 3192.70]  Very cool.
[3193.08 --> 3193.22]  Yeah.
[3193.30 --> 3195.42]  This upcoming thing with Maintainer Week is pretty cool.
[3195.72 --> 3197.76]  We're hoping to play a fun role in it.
[3198.04 --> 3202.38]  We have a special secret, very secret guest that we're hoping to appear.
[3202.44 --> 3202.74]  We'll see.
[3202.96 --> 3203.28]  We'll see.
[3203.34 --> 3204.00]  But it's going to be fun.
[3204.26 --> 3205.84]  June 7th is the week of Maintainer Week.
[3205.96 --> 3206.26]  That's right.
[3206.34 --> 3207.54]  Well, Maintainer Summit's part of that.
[3207.64 --> 3208.22]  We're a part of that.
[3208.26 --> 3210.04]  And some others are part of that from TideLift and whatnot.
[3210.04 --> 3216.00]  And so it's all about finding ways to support maintainers because, as you said before, burnout is totally possible.
[3216.34 --> 3216.44]  Yeah.
[3216.52 --> 3219.76]  We don't want to gamify, get up to the point where you feel like you have to overachieve.
[3219.84 --> 3220.88]  It's really about participation.
[3221.20 --> 3226.28]  It's about showing up, as you said before, consistently bringing what you have of value to the table of open source.
[3226.28 --> 3227.38]  And it could be docs.
[3227.50 --> 3228.60]  It could be code.
[3228.70 --> 3229.74]  It could be community.
[3229.88 --> 3230.46]  It could be governance.
[3230.62 --> 3231.70]  It could be project management.
[3231.82 --> 3232.76]  It could be all these different things.
[3232.90 --> 3237.36]  It definitely is everybody working to the greater good of what open source can do.
[3237.44 --> 3242.12]  And I think coming back to celebrating this mission to Mars as part of that, that's a win.
[3242.44 --> 3245.14]  So Maintainer Summit, Maintainer Week, awesome.
[3245.42 --> 3245.90]  I like it.
[3246.22 --> 3246.94]  I'm excited about it.
[3247.26 --> 3247.38]  Great.
[3247.64 --> 3253.52]  And going back to what you said earlier about surfacing to maintainers, their dependence in better ways.
[3253.52 --> 3259.80]  I think that's such a great goal because when you think about open source and its purest, it's a gift to the world.
[3260.08 --> 3263.58]  Like you said, these people are like the most helpful, nice, giving people.
[3263.66 --> 3265.96]  I mean, they're givers, like you said, because it's what it is.
[3266.02 --> 3272.02]  You're giving your code out there for anybody to have and to hold and to change and to do what they're going to do according to the license.
[3272.20 --> 3272.88]  And that's a gift.
[3273.30 --> 3280.04]  And it's a weird gift because so often you're standing there giving something to somebody and you hand it to them, right?
[3280.26 --> 3281.50]  And you say, oh, open it quick.
[3281.60 --> 3282.46]  I want to see your reaction.
[3282.46 --> 3286.62]  I want to have that delight of like you receiving this and enjoying it.
[3286.74 --> 3288.92]  And in open source, you don't always get that part of it, right?
[3288.98 --> 3293.48]  Like you give it to the world and then you find out six years later somebody was using it.
[3293.78 --> 3303.18]  It's also weird that like it's one of the only places where you give somebody a gift and then they complain about your gift and tell you how much it sucks and how you need to fix it and stuff and all those things.
[3303.18 --> 3311.86]  And so I like the idea of letting people know without having to get reports back from your users and teasing.
[3312.06 --> 3316.98]  I was teasing Daniel about putting a phone home in curl so he can know his actual use, his actual use.
[3317.14 --> 3318.10]  Those kind of things.
[3318.18 --> 3321.14]  I mean, some people do put metrics in like, no, I want to know who's using this.
[3321.22 --> 3322.74]  And so here's what I do.
[3322.74 --> 3325.14]  And that's their prerogative with their software.
[3325.44 --> 3330.96]  But it'd be great if we could let people know how much impact because there's lots of motivations for open source.
[3331.14 --> 3334.46]  One of those motivations is I want to maximize my impact with my software.
[3334.74 --> 3338.70]  And like helping power a mission to Mars is one of those things.
[3338.74 --> 3339.58]  Like look at that leverage.
[3339.58 --> 3344.80]  Like you wrote this code and now you are part of something bigger than yourself and you have massive amounts of impact.
[3345.10 --> 3348.22]  And sometimes you just don't know if you're having the impact you want to have.
[3348.34 --> 3352.82]  So if you guys can help in that way, I know there's like the dependency graph and stuff like that.
[3352.86 --> 3357.98]  Now there's a new section like how many repos depend upon this package or this repo.
[3358.14 --> 3359.66]  Like that stuff starting to get in there.
[3359.66 --> 3361.66]  How are you thinking it could go further?
[3361.92 --> 3368.28]  Or what else could you do beyond what you've already done, which is some dependency stuff inside GitHub.com
[3368.28 --> 3371.40]  to help maintainers really know who's out there using their stuff?
[3372.44 --> 3373.42]  Yeah, I think it's two ways.
[3373.56 --> 3378.70]  So we need to help people know what their dependencies are and then help them keep them up to date as well.
[3378.78 --> 3384.44]  Because the amount of sort of old security vulnerabilities and things you got kicking around you didn't realize because you, you know.
[3384.48 --> 3385.52]  So we need to do that side.
[3385.52 --> 3391.84]  So we need to, for people who are consuming, help them figure out what it is they are consuming and how to keep it up to date.
[3392.04 --> 3393.56]  Because that's kind of the problem they have.
[3393.82 --> 3397.54]  And then how to support the projects that they're taking the critical dependencies on.
[3397.54 --> 3398.86]  Which projects are out there?
[3399.04 --> 3403.52]  Can they, if they can't support them with time, if they can't support them with resources,
[3403.70 --> 3408.24]  then maybe they can provide financial resources to, again, help that project if that's something that we can do.
[3408.56 --> 3413.58]  On the user developer side, yeah, helping know how many people are dependent on this project would be awesome.
[3413.88 --> 3418.28]  My dream would be to someday do even more stuff around that.
[3418.40 --> 3422.02]  You know, like it's tricky to do, but I would, now we've got actions and things,
[3422.02 --> 3427.34]  I would love to do a way where, if you've got a dependency, one of the ways you could donate would be to say like,
[3427.40 --> 3433.26]  yeah, I will donate anonymously the results of my bold to these dependencies, you know.
[3433.30 --> 3438.76]  And then as a dependency, you could say, okay, well, let's go run this thing and go, you know,
[3438.76 --> 3441.94]  run it with people who take a dependency on me and see if I break them.
[3441.94 --> 3444.76]  Because I'm going to release this as a minor release kind of thing.
[3444.76 --> 3449.54]  I don't think it should break anybody, but oh, apparently it broke 90% of my dependencies,
[3449.92 --> 3451.22]  people who are dependent on my code.
[3451.32 --> 3454.58]  Oh, that's something I would, you know, I would love to know if I was an open source maintainer.
[3454.64 --> 3457.22]  Now doing the compute for that is a different question.
[3457.22 --> 3462.76]  And doing the opt-ins and making that be done in a GitHub way that's kind of invisible to you
[3462.76 --> 3465.82]  and lightweight and easy and things like that, it's all hard to do.
[3466.12 --> 3471.36]  But I think there's just tons that we could go do to give value back to the maintainers,
[3471.40 --> 3473.02]  because they're the ones that are doing the awesome.
[3473.02 --> 3475.66]  They're the ones that are like giving all these gifts out to the world.
[3476.10 --> 3481.70]  And so the more things that we can go build to try to give that value back, I think the better.
[3481.88 --> 3483.66]  So, yeah, we keep on looking, see what we can do.
[3484.22 --> 3488.46]  And that's the kind of stuff that you are seeking maintainer input on, right?
[3488.54 --> 3491.66]  Like what could we do to maintain your input on anything?
[3492.30 --> 3494.06]  But also, you know what I mean?
[3494.22 --> 3498.62]  Like bearing in mind, like if it's, I'm trying to think of an example,
[3499.24 --> 3502.46]  that, you know, certain changes we probably know,
[3502.46 --> 3504.80]  and there's probably good reasons why we've got them that way.
[3505.04 --> 3507.42]  But what it is that we can do to help you?
[3507.62 --> 3513.02]  Like what is it we can do to make your life more sustainable, easier as a maintainer,
[3513.14 --> 3515.54]  more, you know, give you more joy as a maintainer?
[3515.58 --> 3517.62]  How can we help your communities work better?
[3518.02 --> 3519.90]  Hacking communities is fascinating.
[3519.90 --> 3523.44]  How the psychology of crowds works and all that sort of stuff, you know,
[3523.60 --> 3525.10]  Stack Overflow obviously do a lot in that space.
[3525.18 --> 3528.96]  And we're doing stuff in that space as well when it comes to like discussions and how we,
[3529.10 --> 3534.16]  you know, we've added capabilities recently where you can like temporarily switch interaction limits on and things.
[3534.32 --> 3538.72]  So if the community needs a bit of a timeout or if you need a timeout or whatever,
[3538.82 --> 3541.42]  if you want to go on vacation, then add these capabilities in.
[3541.52 --> 3546.62]  I like the, we added the ability to set your status and you can sort of say you're on vacation and stuff like that.
[3546.62 --> 3552.08]  Things like that, even though it doesn't mean anything really, like it doesn't stop too much.
[3552.34 --> 3556.50]  It is you as a maintainer, me being able to say I'm on vacation right now.
[3556.88 --> 3558.14]  I'm not going to answer for two weeks.
[3558.16 --> 3561.92]  Makes me feel less guilty about taking a vacation for two weeks.
[3562.16 --> 3567.56]  And so there's little things we can do like that, that help you psychologically not get burnt out
[3567.56 --> 3571.36]  and help you survive and help you maintain as well as the things of value, you know.
[3571.40 --> 3573.90]  So it's about managing the entire person.
[3573.90 --> 3574.42]  It's fascinating.
[3574.42 --> 3577.54]  And so this is one of the reasons why I'm looking towards forwarders maintain a week as well.
[3577.66 --> 3584.30]  You mentioned I'm just to try and like tease out kind of the humans behind how we can kind of make some changes
[3584.30 --> 3588.84]  to help everybody's lives and help everybody thrive when we are getting these wins.
[3588.94 --> 3591.46]  Because it's open source is amazing.
[3591.64 --> 3594.54]  And the communities in the, I owe my career to open source.
[3594.68 --> 3599.66]  I owe my children's education to open source and to the friends I've made.
[3599.66 --> 3605.48]  And I owe, like most of my friends I've made from the open source communities, I've been lucky to be a part of.
[3605.54 --> 3608.22]  And so I just want more and more people to be able to have these experiences.
[3608.72 --> 3610.10]  This is such a breath of fresh air, honestly.
[3610.14 --> 3616.08]  I want to celebrate this win because there was a day when it seemed like that kind of response wasn't coming from GitHub.
[3616.60 --> 3619.18]  And I think this is prior to the Microsoft acquisition.
[3619.18 --> 3622.46]  If you recall, there was a dear GitHub repository out there.
[3622.58 --> 3627.46]  And it wasn't so much, it was around maintainers and the voices of maintainers not being heard.
[3628.08 --> 3633.24]  And so I think, you know, just together with you, Martin, celebrating that win for GitHub, that you are listening,
[3633.36 --> 3640.52]  that you are inviting maintainers to come and speak to you and to evolve the all things GitHub essentially to make it better for maintainers and better for everybody, really.
[3640.52 --> 3647.48]  But there was a time when it seemed like it was listening less, that they were dogmatic in their ways or whatever it might have been.
[3647.80 --> 3651.08]  And there were pause stories out there with Lincoln in the show notes for just posterity's sake.
[3651.22 --> 3658.02]  But, you know, I think that's a good thing to celebrate that win because you are listening and you've already sent your email on this podcast.
[3658.34 --> 3659.14]  So you're on the hook.
[3659.40 --> 3660.02]  Yeah, exactly.
[3660.24 --> 3662.78]  Somebody emails you, you're going to have to answer, right?
[3663.12 --> 3663.92]  And that's how it works.
[3664.04 --> 3667.52]  I'll send you my screenshot of my unread email account as well.
[3667.52 --> 3668.36]  But yeah, no, yeah.
[3668.48 --> 3672.02]  That email again is martinwoodwood.github.com or at martinwood on Twitter.
[3672.18 --> 3673.58]  But yeah, that's all good.
[3673.84 --> 3674.20]  Exactly.
[3674.36 --> 3676.96]  Or when you're talking on Twitter, CC Nat Freeman.
[3677.40 --> 3677.88]  And there you go.
[3677.92 --> 3678.92]  You might get your change.
[3678.98 --> 3680.04]  It might already be in the works.
[3680.30 --> 3680.64]  Yeah, yeah.
[3680.72 --> 3682.28]  Try to go to me first.
[3682.60 --> 3683.18]  That would be great.
[3683.44 --> 3684.52]  Make my life easier.
[3684.88 --> 3685.56]  Have less dramas.
[3688.14 --> 3689.78]  That's it for this episode of The Change Law.
[3689.86 --> 3690.78]  Thanks for tuning in.
[3690.78 --> 3697.02]  If you aren't subscribed yet to our weekly newsletter, you are missing out on what's moving and shaking in software
[3697.02 --> 3698.32]  and why it's important.
[3698.98 --> 3699.88]  It's 100% free.
[3700.02 --> 3702.80]  Fight your FOMO at changelog.com slash weekly.
[3703.08 --> 3706.04]  Huge thanks to our partners, Linode Fastly and LaunchDarkly.
[3706.32 --> 3709.04]  When we need music, we summon the Beat Freak Breakmaster Cylinder.
[3709.34 --> 3711.40]  Huge thanks to Breakmaster for all their awesome work.
[3711.84 --> 3717.34]  And last but not least, subscribe to our master feed at changelog.com slash master.
[3717.82 --> 3720.36]  Get all our podcasts in a single feed.
[3720.58 --> 3721.66]  That's it for this week.
[3721.88 --> 3722.70]  We'll see you next week.
[3722.70 --> 3752.68]  We'll see you next week.
[3752.70 --> 3782.68]  We'll see you next week.
