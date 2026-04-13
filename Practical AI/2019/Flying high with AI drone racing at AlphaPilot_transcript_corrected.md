[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.84] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.22 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[15.72 → 20.34] This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 → 25.10] And we're excited to share they now offer dedicated virtual droplets.
[25.10 → 29.02] And unlike standard droplets, which use shared virtual CPU threads,
[29.02 → 32.86] their two performance plans, general purpose and CPU optimized,
[33.40 → 36.08] they have dedicated virtual CPU threads.
[36.40 → 40.86] This translates to higher performance and increased consistency during CPU intensive processes.
[41.36 → 45.20] So if you have build boxes, CCD, video encoding, machine learning, ad serving,
[45.50 → 49.98] game servers, databases, batch processing, data mining, application servers,
[50.20 → 54.92] or active front end web servers that need to be full duty CPU all day every day,
[55.14 → 57.92] then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 → 61.26] Pricing is very competitive starting at 40 bucks a month.
[61.66 → 66.38] Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 → 69.02] Again, do.co slash Changelog.
[69.02 → 86.38] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.76 → 88.56] productive, and accessible to everyone.
[88.94 → 93.44] This is where conversations around AI, machine learning, and data science happen.
[93.92 → 98.20] Join the community and slack with us around various topics of the show at changelog.com slash community.
[98.20 → 99.38] Follow us on Twitter.
[99.48 → 100.96] We're at Practical AI FM.
[101.46 → 102.28] And now onto the show.
[106.66 → 109.96] Welcome to another episode of the Practical AI podcast.
[110.46 → 112.26] This is Chris Benson speaking.
[112.42 → 114.54] I'm Principal AI Strategist at Lockheed Martin.
[114.76 → 119.76] And with me today is my co-host Daniel, who is a data scientist with SIL International.
[120.14 → 121.02] How's it going today, Daniel?
[121.02 → 123.04] It's going pretty good.
[123.16 → 126.54] I'm working on not my normal amount of sleep.
[126.66 → 136.62] I've been having some extra meetings this week with a team in India I'm working with on some dialogue stuff, some conversational AI.
[137.26 → 140.08] And so it's been early mornings for this week.
[140.16 → 142.26] So I'm looking forward to sleeping in the morning.
[142.48 → 146.42] But it's been good tech, just early mornings.
[146.52 → 147.06] How about yourself?
[147.06 → 148.64] I probably have more sleep.
[148.70 → 150.48] I was a little sleep-deprived earlier in the week.
[150.54 → 151.54] I think I've caught up.
[151.86 → 154.90] But I'm just kind of on cruise control here.
[155.12 → 161.16] I'm about to head over to the UK for a week of work and then a couple of weeks of family vacation.
[161.38 → 162.50] So I'm looking forward to that.
[162.84 → 163.30] Good times.
[163.56 → 163.82] Yeah.
[164.00 → 169.00] Looking forward to some shepherd's pie or jellied eels or something.
[169.62 → 171.50] Strictly vegan everything.
[171.84 → 172.74] Oh, yeah, that's right.
[172.90 → 174.32] I don't even know why I asked that.
[174.32 → 175.88] I'm strictly vegan, my friend.
[175.88 → 182.92] When I think of England, the food scene seems like, you know, meat in a pie is what I think of.
[183.32 → 185.14] And I think traditionally it has been.
[185.42 → 188.04] And since you said that, I'll just say my wife was amazed.
[188.46 → 189.48] She's always grumbling.
[189.62 → 190.46] We're both vegan together.
[190.46 → 194.88] And she's always grumbling that her father is like the epitome of the meat eater.
[195.04 → 196.24] And she was just delighted.
[196.38 → 198.82] She was just gleeful when I came home a few days ago.
[199.18 → 205.82] And she said that her dad had tried some vegan beef and vegan hot dogs and stuff like that.
[205.88 → 206.76] And he liked it.
[206.84 → 207.96] And she was just, oh, it's great.
[208.12 → 209.10] So who knows?
[209.46 → 212.20] Well, you'll have like vegetables and pies or something.
[212.64 → 213.18] There you go.
[213.18 → 218.06] So, you know, apparently even the meat eating folks of the UK may go that way.
[218.18 → 219.80] But this isn't a vegan podcast.
[219.80 → 220.56] So I'll stop.
[220.60 → 221.66] I'll stop going down that.
[222.60 → 223.00] Anyway.
[223.18 → 224.32] But when I get back.
[224.38 → 230.00] So I will kind of be back into the world on this side of the pond early in October.
[230.00 → 233.48] is kind of coming back into work on the 7th.
[233.48 → 236.10] And I'm going to get to do something that's pretty fun.
[236.10 → 242.54] That's participating in a program that Lockheed Martin is has been driving with some partners.
[243.04 → 244.28] And it is called Alpha Pilot.
[244.52 → 252.40] And today with us on this podcast, we have Keith Lynn, who is the program manager at Lockheed Martin for the Alpha Pilot program.
[253.16 → 257.08] And when he tells you about this in a few minutes, it's going to blow your mind.
[257.14 → 258.98] It's a super, super, super cool thing.
[258.98 → 260.72] And he's been working really hard on it.
[260.94 → 262.06] Keith, welcome to the show.
[262.56 → 263.06] Hey, guys.
[263.26 → 263.90] Thanks for having me.
[264.38 → 274.54] We have actually been talking about having you on for quite a long time with some of the events that we've done internally at Lockheed that you have orchestrated.
[274.84 → 278.22] And I've kind of come back and just said, Daniel, this cool thing.
[278.22 → 283.20] And, you know, at some point, you know, when it's the right time, we've got to have an episode about it.
[283.30 → 284.52] And so we've both been excited.
[284.52 → 288.74] I've been asking Chris each week about, hey, can we talk about this thing?
[288.74 → 290.22] You've been talking about now.
[290.42 → 291.54] He really has.
[291.54 → 306.88] So before we dive fully into Alpha Pilot, if you could just kind of tell us a bit about yourself, how you got to where you are, you know, and kind of what's the life path that led you up to this moment where you are running this amazing Alpha Pilot program?
[306.88 → 307.80] Yeah.
[307.80 → 310.90] So I think I've been with Lockheed about 11 years now.
[311.40 → 317.56] I started out graduate in physics and mathematics at a liberal arts college here in Pennsylvania.
[318.22 → 321.44] And my first job was doing signals intelligence.
[321.44 → 326.24] And from there, I guess my curiosity got the best of me.
[326.48 → 331.00] And Lockheed is a perfect place if you like some diversity of what you're working on.
[331.12 → 342.34] So I quickly jumped to doing some research in health care, then in energy management systems, eventually made my way to our corporate office and got to do some international work.
[342.34 → 358.38] Spent a better part of a year and a half managing R&D in the United Kingdom, some nanotechnology research down at Rice University in Texas, and eventually landed in the autonomous systems group at corporate.
[358.74 → 362.14] This is around the time when AI really started to take off.
[362.48 → 367.30] You know, a couple of years back, AI was, you know, if you ask people, what do you know about artificial intelligence?
[367.30 → 368.70] They'd say, you mean like robots.
[369.44 → 374.98] So the term in itself has really blossomed, and it has a much broader field of meaning now.
[375.28 → 385.72] And at Lockheed Martin, we started looking at artificial intelligence and then a subset of that, which is autonomous systems, and really trying to figure out where we can apply that across our different products and services.
[386.38 → 388.18] And that's what really led me into Alpha Pilot.
[388.60 → 391.66] A few years back, we, I'm sorry, a year back.
[391.86 → 393.30] It feels like a few years back already.
[393.30 → 401.22] I know that when I saw you at the event that you probably mentioned a little while back, you were going, pardon the phrase, balls to the wall.
[401.32 → 402.66] You were really working hard.
[402.86 → 405.98] So I can believe it's been, it's felt like three years.
[406.44 → 409.02] It's, it's been one of the longest years for me on record.
[409.02 → 409.64] That's for sure.
[410.04 → 411.48] But I couldn't be happier.
[411.60 → 421.52] You know, I, I might not always say so in the heat of it, but I think I, I always look back, and I say, man, doing this kind of thing where you're, where it's chaos and, you know, things are going haywire,
[421.52 → 424.12] but you somehow manage to, to land the plane.
[424.44 → 426.18] So it was just about a year ago.
[426.34 → 432.86] I was actually sitting at a hotel next to South by Southwest Conference Centre where we were doing a presentation.
[433.60 → 437.34] And I think I was actually telling my boss, like, I'm getting a little bored.
[437.52 → 439.06] I'm not really sure what I want to do next.
[439.24 → 443.92] And I feel like I need my next big thing, something that really pushes me to the limit.
[443.92 → 450.70] And then our, our vice president sat down and, you know, he just said, I just got this new thing, you know, just came on my plate.
[450.98 → 459.84] Lockheed wants to do a global innovation challenge, and they want to do something with autonomy and, you know, maybe drones or something like that.
[459.90 → 461.90] We're not sure, but it's got to be huge.
[462.50 → 463.82] Got to really get people's attention.
[463.96 → 467.38] It's got to really show people that Lockheed cares about artificial intelligence.
[467.38 → 472.90] And now we just need some, you know, poor fool to put in front of this and figure it all out.
[473.20 → 477.76] And, uh, I mean, the timing was just perfect with what I was talking to my boss about.
[477.80 → 479.74] So I just said, Hey, I'm, I'm looking for something.
[479.84 → 481.30] Let, let me take a crack at it.
[482.00 → 493.00] So before we even dive into Alpha Pilot, you know, just to give some background on, on before we even talk about the program, you know, it has to do with, with drone racing and stuff.
[493.00 → 502.04] And I was wondering if you could kind of talk about what that is prior to Alpha Pilot, you know, what, what is drone racing, and what's the interest in it?
[502.08 → 505.82] And is it, is it something that's specific to the U S is it international?
[506.14 → 511.16] If you could talk a little bit about that, and then we'll get into Alpha Pilot and describe its role in that world.
[511.16 → 515.82] I just mentioned that Alpha Pilot involves drones and drone racing specifically.
[516.62 → 519.84] That as a sport is about four years old.
[519.84 → 528.68] And, um, from what I've been told, it was first conceived of in Australia, then made its way to America and really took off.
[528.72 → 531.12] And now it's really, uh, has a global audience.
[531.12 → 534.24] I know it's very big across all across Europe, actually.
[534.24 → 543.42] But what that is basically is humans piloting drones via a what they call FPV or first person view camera.
[543.42 → 547.94] So these pilots have a perfect RF signal.
[547.94 → 549.10] So they have low latency.
[549.44 → 559.88] They see what the drone sees, and they are competing with each other in a traditional first to the finish type race, uh, through various types of courses.
[560.92 → 562.38] Like real life video games.
[562.58 → 562.88] Yeah.
[562.88 → 563.94] Like a real life video game.
[564.14 → 565.36] And how do they see?
[565.36 → 566.82] By wearing these goggles.
[567.26 → 568.90] I've actually tried them on.
[569.06 → 574.02] They just look like, like a pair of lab goggles or something like that, or VR headset kind of.
[574.54 → 578.12] And you put them on, and you get this view from the drone.
[578.28 → 580.48] And a lot of times it's kind of grainy.
[580.66 → 581.60] It's, it's not the best.
[581.74 → 587.30] And if you are at all motion sick, uh, or you type of person that gets motion sick, it's not the most pleasant experience.
[587.30 → 587.54] That's right.
[588.32 → 589.50] That's what I was just thinking.
[589.66 → 600.20] So I can ride regular roller coasters all day, but I remember like we went to Universal Studios recently, and we were in one of those like 3D rides where it is also like shakes you around and stuff.
[600.34 → 601.86] And man, I got so sick.
[601.98 → 606.12] It's like something about that like virtual motion just really does not agree with me.
[606.62 → 606.80] Yeah.
[606.90 → 608.88] The older I get, the more of that affects me.
[608.94 → 610.64] When I was younger, I could kind of do it.
[610.64 → 611.56] But, uh, yeah.
[611.92 → 612.06] Yeah.
[612.10 → 615.28] After a while, your body works with you less and less than that way.
[615.28 → 622.12] So you mentioned that there's like these people, they're wearing headsets, they're piloting these drones.
[622.28 → 627.22] I'm assuming it's like around like a racetrack, like there are gates they have to go through or something.
[627.28 → 627.90] Is that how it works?
[628.42 → 628.56] Yeah.
[628.62 → 632.22] So it's done a little bit differently depending on who you're racing with.
[632.70 → 635.20] There are a lot of different organizations that are doing this.
[635.32 → 636.54] Some are more grassroots.
[636.90 → 637.84] Some are professional.
[637.84 → 646.02] On Alpha Pilot, we're partnered with the Drone Racing League, which is probably the biggest drone racing outfit out there.
[646.44 → 648.02] They're on national television.
[648.38 → 649.50] They have events worldwide.
[650.16 → 652.50] I think over 80 million viewers annually.
[653.30 → 659.02] Their courses are like a traditional racecourse where you're going through different gates and checkpoints.
[659.02 → 666.46] And they try to do them in exciting locations and integrate with the local environment to the extent possible.
[666.64 → 668.72] So you mean like around buildings and such?
[669.02 → 672.48] So I was at one last year that was at the BMW headquarters.
[672.48 → 678.36] So there was literally an indoor track with all these BMW vehicles going back 100 years.
[678.98 → 683.40] And they were flying over top of the cars and between different BMW displays.
[683.40 → 687.76] So they try and make it really, really an exciting environment.
[688.26 → 688.30] Cool.
[688.46 → 689.72] Yeah, that's pretty neat.
[689.94 → 691.72] So how fast are these drones going?
[691.84 → 694.18] Like I'm just imagining having this headset on.
[694.84 → 700.42] And I'm assuming you have to have pretty quick reflexes to kind of make it around this course.
[700.52 → 705.54] What's the sort of speeds that these things are going and like the size of the course?
[705.54 → 708.92] Like are we talking like feet, miles?
[709.32 → 711.08] Like how big of a scale are we talking about?
[711.08 → 717.46] So I think even more than reaction time, it's so darn hard just to control the drone.
[717.58 → 719.66] There's so much sensitivity in the joysticks.
[719.94 → 723.62] I've tried it out with a little, you know, like training wheels drone.
[723.90 → 727.36] And I could not, this thing just pin balled between the floor and the ceiling.
[727.36 → 730.42] So it's incredibly hard just to keep the thing in the air.
[730.64 → 735.04] But they top out around 80 miles an hour, I believe.
[735.22 → 737.08] That's not sustained 80 miles an hour.
[737.48 → 740.64] But, you know, on a straightaway, they get up to about that speed.
[740.64 → 746.92] The laps themselves, they're maybe like a size of an indoor track, I would say.
[747.42 → 749.26] Like a track and field track sort of thing.
[749.34 → 749.52] Yep.
[750.02 → 751.96] And they would do multiple laps.
[752.68 → 756.56] And the interesting thing is the, you know, they're really burning through these batteries
[756.56 → 758.78] going at that speed and with that kind of agility.
[758.78 → 762.56] So the flights themselves don't last very long, maybe a minute total.
[762.56 → 766.88] Like the full race or do they like stop for like pit stop recharge?
[767.10 → 768.52] I imagine that wouldn't be too exciting.
[770.48 → 770.88] Yeah.
[770.94 → 773.64] So when you're there, I mean, you got this safety net in front of you.
[773.70 → 775.74] There's a very intense safety protocol.
[776.28 → 778.12] And these things just go buzzing by you.
[778.18 → 781.50] And really, sometimes all you see is just the LED lights.
[781.50 → 785.92] So it's just kind of a blur of red or blue or yellow or whatever colour that particular
[785.92 → 786.62] racer is.
[786.94 → 792.26] It seems like almost like a horse racing experience where, you know, at least a couple of people on
[792.26 → 794.72] this call don't approve of all things horse racing.
[794.72 → 800.62] But it's like that very short period time of like high excitement and like everything's
[800.62 → 800.90] over.
[800.90 → 805.42] And however long it takes one minute, like you said, it's a very, very intense experience.
[805.42 → 805.98] Yep.
[806.12 → 811.54] You go from looking for it to come around the corner, whiz past you, then your eyes go
[811.54 → 814.28] back to the giant screen to see where it is now.
[814.60 → 819.44] And, you know, the Jordan Racing League is very good with production quality, and they have
[819.44 → 821.70] the whole arena mic'd up.
[821.88 → 827.08] So if one of these things bites it, you know, anywhere, you're going to get that audio as
[827.08 → 828.14] if it's right next to you.
[828.26 → 831.54] And I mean, it's a real intense sound when these things crash going that fast.
[831.54 → 837.28] And part of the guilty pleasure of racing always, you know, seeing a little bit of a hardware
[837.28 → 837.94] go flying.
[838.16 → 839.66] So it's a fun time.
[840.60 → 840.66] Yeah.
[840.84 → 844.60] You can describe it in a minute, but even the thing that I was at, the event that I was
[844.60 → 849.82] at with the teams was quite thrilling, and it wasn't even production quality of what you're
[849.82 → 851.14] describing for everyone.
[851.30 → 856.08] But I was, you know, I think all of us that were new to it were like, wow, which kind of
[856.08 → 859.70] brings me to the next thing is, you know, now that you've kind of described what drone
[859.70 → 864.52] racing is with these human pilots doing their thing really well.
[864.92 → 869.44] Could you kind of describe what Alpha Pilot is and how it fits into that context of drone
[869.44 → 870.68] racing and such?
[871.34 → 871.48] Sure.
[871.82 → 875.86] So Alpha Pilot is a public innovation challenge.
[876.24 → 884.02] So I would compare it to like a DARPA Grand Challenge or an PRIZE where an organization,
[884.02 → 888.00] in this case, Lockheed Martin, puts out a hard problem.
[888.58 → 893.50] So ours was programming a drone to fly in a racecourse autonomously.
[894.16 → 898.42] And that challenge is associated with some kind of award, an award.
[898.56 → 907.76] So ours is $2 million for the top teams and then an additional $250,000 kicker prize if any
[907.76 → 913.26] algorithm can fly faster than a professional human pilot on the same course.
[913.26 → 918.92] So we're having a little friendly rivalry with the professional pilots here in the drone
[918.92 → 919.42] racing league.
[919.70 → 919.78] Gotcha.
[919.96 → 925.48] So there's like, it's almost like a sort of Watson Jeopardy sort of challenge thing going
[925.48 → 927.92] on where there's actually humans racing at the same time.
[928.26 → 933.16] It would be more like if there were four different Watson's competing with each other and then we
[933.16 → 937.10] took the best Watson and put it against the best human Jeopardy player just for fun.
[937.34 → 940.94] So there's, I guess, a series or a bracket or something too.
[940.94 → 946.94] So like people go against each other, the humans go against various drones, other autonomous,
[947.24 → 949.48] and then there's sort of like a grand showdown.
[950.04 → 956.40] So originally we were going to pair the autonomous racing with human racing so we could have more
[956.40 → 957.40] of that side by side.
[957.60 → 962.38] Then we decided to move towards more standalone events because we wanted this to really be
[962.38 → 967.66] not just about the racing, but a celebration of artificial intelligence and create an opportunity
[967.66 → 968.90] for larger STEM engagement.
[968.90 → 974.00] So our events are just going to be autonomous racing, even though we'll have some human
[974.00 → 977.36] pilots there to do some commentary and some demonstrations.
[978.36 → 984.04] And then as we get later in the season, we will have one of the pilots on standby to go
[984.04 → 989.70] head to head against the top autonomous team after the racing for that day is finished.
[989.70 → 1006.18] This episode is brought to you by Brave.
[1006.34 → 1012.02] The Brave team is on a mission to fix the web by building an open source, privacy focused,
[1012.26 → 1014.26] and performance oriented browser.
[1014.26 → 1017.76] Browse the web up to eight times faster than Chrome and Safari.
[1018.26 → 1020.30] Block ads and trackers by default.
[1020.64 → 1024.40] And reward your favourite creators with the built-in basic attention token.
[1024.98 → 1026.24] Yes, you heard that right.
[1026.34 → 1028.42] A real world use case for blockchain.
[1029.02 → 1034.40] Download Brave for free using the link in the show notes and give tipping a try on changelog.com.
[1034.40 → 1049.92] So for these teams that are working on Alpha Pilot, you know, we've talked about kind of the drone
[1049.92 → 1051.60] racers in the manual sense.
[1051.74 → 1057.72] There are these teams that are behind these automated AI enabled drones that Alpha Pilot's
[1057.72 → 1057.94] doing.
[1058.28 → 1062.32] Could you tell us a bit about the teams and, you know, where they're from and a little bit
[1062.32 → 1062.66] about them?
[1062.66 → 1063.36] Sure.
[1063.50 → 1073.62] So Alpha Pilot as an innovation challenge launched late last year, and we had about 430 teams
[1073.62 → 1074.76] sign up to compete.
[1075.82 → 1078.22] And these teams were from all around the world.
[1078.62 → 1085.90] We used a simulation-based process to down select to just nine teams to go into this first year
[1085.90 → 1088.52] season of autonomous racing.
[1088.52 → 1092.44] And the teams that we selected are just fantastic.
[1093.34 → 1095.92] A lot of them are with universities.
[1096.70 → 1104.40] Some of them are small businesses, but we have teams from Georgia Tech, UCLA, University of Zurich,
[1104.98 → 1110.00] team from Brazil, team from Warsaw, team from Heist in South Korea.
[1110.00 → 1116.58] And then we have a team that's really kind of a mix of people from three different continents,
[1116.58 → 1120.96] which is quite impressive considering this is all software-based, and they have to run it
[1120.96 → 1121.26] remotely.
[1121.26 → 1124.86] So we're really impressed with the diversity that we received.
[1125.12 → 1127.36] And there are some pretty impressive folks.
[1128.14 → 1133.00] So on these teams, I'm kind of curious, as you mentioned universities, are there kind of
[1133.00 → 1139.22] mostly student teams that are kind of doing this as a let's say, a senior design project
[1139.22 → 1140.18] or something like that?
[1140.18 → 1141.78] Or is it like graduate researchers?
[1141.78 → 1145.50] Or what's the sort of range of experience there?
[1145.92 → 1146.90] A little bit of everything.
[1147.32 → 1151.84] So we didn't want to put too many restrictions on how teams formed because we wanted people
[1151.84 → 1157.90] to feel comfortable working with the other individuals that made the most sense and that
[1157.90 → 1160.50] they would enjoy being part of this with the most.
[1161.22 → 1164.70] And we do have some teams where it's all undergrad students.
[1165.40 → 1170.66] We have somewhere it's a mix of grad, undergrad, and we have somewhere the professors are even
[1170.66 → 1171.02] involved.
[1171.78 → 1173.54] So yeah, we get a little bit of everything.
[1173.86 → 1177.86] The only rules we put on it were no more than 10 individuals per team.
[1178.02 → 1181.40] So we didn't have anyone with 100 people on the roster.
[1181.74 → 1183.38] And then we have to keep tabs on all of them.
[1183.44 → 1186.78] And they're outsourcing tasks to the web and things like that.
[1187.00 → 1192.64] And then a basic age requirement, just because you're dealing with some flying things that
[1192.64 → 1193.86] are really heavy and go fast.
[1193.92 → 1195.58] So we want to make sure everybody's an adult.
[1196.00 → 1196.66] But that was it.
[1196.66 → 1203.30] And in terms of constraints, like technology wise, is there and forgive me of my ignorance
[1203.30 → 1204.46] of drone racing out there.
[1204.52 → 1206.00] People probably love drones.
[1206.00 → 1209.40] And I'm like butchering a bunch of things or ignorant.
[1209.40 → 1215.08] But is there like in these leagues, is there a specific drone you have to use?
[1215.08 → 1217.86] Or like what are the constraints is like hardware wise?
[1218.06 → 1225.00] Like you have to have a drone that's this model or one of these models, but you can modify
[1225.00 → 1226.70] it in X, Y, Z ways.
[1227.16 → 1229.52] How does that kind of work for the teams?
[1229.52 → 1230.90] Yeah, it's a good question.
[1231.26 → 1234.78] And, you know, in the entirety of drone racing, the answer is all of the above.
[1235.10 → 1238.06] Some leagues will let, you know, it's BYOD.
[1238.26 → 1239.06] Bring your own drone.
[1239.70 → 1242.64] And they'll just give you some basic requirements about size, weight, power.
[1243.48 → 1246.14] Others are a little more structured, but still BYOD.
[1246.60 → 1251.92] So they might say you have to use, you know, six inch props, you have to use these motors.
[1252.50 → 1255.54] But the platform and everything like that, you optimize as you want.
[1255.54 → 1262.42] And then the Drone Racing League, our partner in Alpha Pilot and their new league that they're
[1262.42 → 1267.54] creating for Alpha Pilot, and then will be a standalone event moving forward is called
[1267.54 → 1270.48] AIR, Artificial Intelligence Robotic Racing.
[1271.28 → 1273.48] They use a standardized drone.
[1273.84 → 1275.82] And they do this in their human races as well.
[1276.46 → 1281.44] So each year they, I believe each year, but periodically they release a new model drone
[1281.44 → 1283.86] that is standard for all of their competitors.
[1283.86 → 1287.96] And we really like that, Amati, because we wanted this to be about the quality of the
[1287.96 → 1288.48] algorithms.
[1289.38 → 1292.78] And if a team won, we wanted it to be because they were the best programmers, not because
[1292.78 → 1296.72] they had, you know, better motors or better batteries on the drone or something like that.
[1297.36 → 1297.48] Yeah.
[1297.60 → 1301.94] So I guess to extend that a little bit, you know, we're kind of talking about some of the
[1301.94 → 1302.84] tech with this.
[1302.96 → 1308.60] Could you kind of describe the technologies that are in the drone and, you know, in terms of
[1308.60 → 1312.72] the hardware, what kind of hardware is being used to run the algorithms and do inference?
[1312.72 → 1315.92] Just kind of take wherever you think would be appropriate.
[1315.92 → 1322.08] What are some of the technologies that are being used at this point by DRL's drone for
[1322.08 → 1322.44] these races?
[1323.38 → 1323.50] Yeah.
[1323.58 → 1328.26] So the main difference between drones for autonomous racing and drones for human piloted
[1328.26 → 1331.48] racing is that our drones have to carry a computer on board.
[1332.22 → 1337.06] And to do autonomous racing, you need, you know, there are two ways you could do it.
[1337.06 → 1342.98] Really, you could do edge computing, which is all the decisions that are made by the algorithms
[1342.98 → 1345.06] happen on board the drone.
[1345.14 → 1349.90] Or you could off board, which means you have a low latency comes link between the drone
[1349.90 → 1353.40] and some high performance computer on the sideline somewhere.
[1353.68 → 1356.16] And it reads in signals, sends it to the computer.
[1356.28 → 1358.00] A computer makes a decision, sends it back.
[1358.38 → 1360.26] That's less impressive technically.
[1360.26 → 1364.32] And it could actually create a problem because of the latency and the speed of the drone.
[1364.46 → 1371.22] So we decided to do fully on board edge computing, which means you need a pretty impressive processor
[1371.22 → 1371.90] on this drone.
[1372.38 → 1375.96] And there are some drones that carry an onboard GPU.
[1376.60 → 1381.18] But we wanted to make sure that we were giving people enough computing horsepower.
[1381.66 → 1386.06] We went with the latest NVIDIA model for edge computing, which is the Xavier.
[1386.06 → 1389.08] And that has never been put on a drone before.
[1389.28 → 1392.18] It's a little bit larger than previous model GPUs.
[1392.54 → 1395.42] So we had to design an entirely new platform altogether.
[1396.02 → 1401.08] DRL did a fantastic job doing heat displacement and everything for this drone.
[1401.24 → 1404.30] And it's definitely unique and first of its kind.
[1404.96 → 1410.72] Yeah, I know commenting on it, and I actually have the Xavier listed here in terms of its specs.
[1410.72 → 1417.06] This is the same GPU computer that is used in autonomous vehicles.
[1417.36 → 1431.16] It's a 512 core Volta GPU with tensor cores, 8 core ARM with a 64-bit CPU, 16 gig of 256 LP DDR4X memory,
[1431.66 → 1432.96] 32 gigs of flash storage.
[1433.04 → 1435.50] It's quite a computer without going through the whole thing.
[1435.50 → 1442.46] I know that when I saw you last at the event, you're putting a pretty serious computer on these drones.
[1442.66 → 1446.00] And I was pretty impressed with the performance, even so.
[1447.02 → 1449.30] Yeah, no wonder they run out of battery.
[1450.30 → 1451.90] I mean, I'm kind of impressed.
[1452.14 → 1456.22] This isn't like, you know, the humans are still wearing the headset,
[1456.64 → 1460.46] and they're kind of like augmenting the flight somehow.
[1460.46 → 1464.50] Now, it sounds like more it's like they're, and I don't know how this starts.
[1464.60 → 1465.46] Maybe you can describe it.
[1465.58 → 1469.76] Like there's these autonomous drones that are just kind of hovering there ready to start.
[1469.92 → 1472.02] And like you push the button start.
[1472.02 → 1475.76] And like based on the video feed that they're processing,
[1475.76 → 1481.20] then they sort of accelerate, turn, switch directions, slow down, all of those things.
[1481.20 → 1484.52] Is that the kind of scenario we're dealing with?
[1484.66 → 1488.46] Or what data are they working with to make these decisions?
[1488.46 → 1494.48] So the teams are primarily training for these races in a simulation environment
[1494.48 → 1499.42] that's built off of the DRL training simulator.
[1499.72 → 1502.06] So they modify that for autonomous racing.
[1502.32 → 1506.20] They put in the new drone physics and updated world models.
[1506.46 → 1510.60] And then they also created course models based on the races.
[1510.60 → 1516.82] And we have a permanent training facility in Littleton, Colorado,
[1516.82 → 1520.68] where we set up a small scale course with two gates.
[1521.36 → 1523.72] And that's kind of the gym, so to speak.
[1523.86 → 1530.62] So these teams can write their algorithms and then train them like in a simulated deployment in this gym.
[1530.62 → 1536.12] And then what they can do is when they feel comfortable, they send the code over to our team.
[1536.48 → 1541.20] We load it up on an actual drone at this facility and deploy it in real life.
[1541.46 → 1548.92] And they collect the actual data from the drone, the telemetry, input from the IMU, rangefinder, the cameras,
[1549.32 → 1551.52] and send that back to the teams.
[1551.52 → 1556.86] And then the team uses that in comparison with what they're seeing in simulation to make some modifications.
[1557.42 → 1563.92] And then before each race, we release a model of that course so they can specifically start training
[1563.92 → 1567.06] for the racecourse that they're about to compete in.
[1567.62 → 1571.72] And then about a week out from the race, there's a final code submit.
[1572.22 → 1573.36] So they send us the code.
[1573.64 → 1577.78] We do all of our safety checks on it, make sure it checks out, and it's going to deploy.
[1577.78 → 1583.00] And then on race day, they have absolutely no physical involvement with the drone whatsoever.
[1583.24 → 1588.52] Everything that it does when it takes off on that podium has already been coded and preplanned,
[1588.66 → 1591.26] and it's just ready to go when they get there.
[1591.70 → 1594.30] So I would like to follow up on a couple of things that you just said.
[1594.74 → 1599.78] And first, there's literally a podium that all of these drones are sitting on,
[1599.98 → 1602.70] rather than being all the way down on the ground, and they take off.
[1602.76 → 1606.50] So they're at a slightly elevated position, just for listeners.
[1606.50 → 1610.04] But you mentioned a few things, a little bit of jargon there I want to ask you for some
[1610.04 → 1612.26] definitions for, just so everybody can follow.
[1612.74 → 1616.72] You mentioned simulation and world models, and a couple other things.
[1616.94 → 1619.70] But starting with those two, can you kind of talk about what is a world model?
[1619.82 → 1621.04] What does that mean in simulation?
[1621.54 → 1621.64] Sure.
[1621.74 → 1628.26] So it's really, really hard to train a drone to fly itself when you're primarily doing it
[1628.26 → 1634.02] in a simulation, which means you recreate the world that you want it to fly in,
[1634.02 → 1635.24] in a computer environment.
[1636.12 → 1641.62] And the reason that's hard is that there's always a delta between what's actual and what
[1641.62 → 1643.22] you're simulating, what you're modelling.
[1643.66 → 1645.80] So in order to do that, you need high fidelity.
[1646.02 → 1650.06] You need to model everything the drone's going to encounter.
[1650.30 → 1656.72] Wind, lighting glare, drift in the sensors, or the standard deviation error bar in the sensors
[1656.72 → 1660.24] that you're using, which is specific to the specific brand and the hardware.
[1660.24 → 1664.84] You need good gravity, wind resistance models, drag.
[1665.40 → 1667.94] So all these things have an effect.
[1668.10 → 1672.84] And if you don't model them well, that means your drone isn't going to behave exactly as
[1672.84 → 1673.60] you think it is.
[1673.90 → 1675.26] It's going to behave slightly differently.
[1675.62 → 1679.42] And sometimes that's small enough that it doesn't make a difference.
[1679.64 → 1684.80] But if you're going fast and over a long enough distance, that could be the difference between
[1684.80 → 1687.72] going through the centre of a gate or crashing into the edges of it.
[1687.72 → 1688.24] Gotcha.
[1689.10 → 1691.58] And you also mentioned a couple of other things just for definition.
[1692.02 → 1696.96] You mentioned telemetry, which probably most people know, but I'd like to cover that for
[1696.96 → 1697.24] a second.
[1697.34 → 1698.88] And also you mentioned IMU.
[1698.96 → 1701.62] And I'm betting a lot of people don't know what IMU is referring to.
[1701.98 → 1702.18] Yeah.
[1702.54 → 1704.40] IMU is inertial measurement unit.
[1705.12 → 1709.54] And this is like a you can think of if maybe some people are more familiar with a
[1709.54 → 1715.56] gyroscope, something that essentially can provide data on the three-dimensional positioning
[1715.56 → 1717.98] of a drone at any given time as it's flying.
[1718.22 → 1720.34] So pitch, roll, and yaw are the three measures.
[1720.72 → 1724.24] Could be leaning forward, left or right, or side to side.
[1725.02 → 1730.46] Knowing your position in space is really important if you're trying to figure out how you go from
[1730.46 → 1731.98] where you are to where you want to be.
[1732.32 → 1737.08] And then also knowing your position from your last measurement is important so you can gauge
[1737.08 → 1738.84] your velocity and trajectory.
[1738.84 → 1748.80] And just to kind of separate, so there's like the simulated world in which you can kind of
[1748.80 → 1753.38] train before they ship the code off to you and they kind of go through the training at
[1753.38 → 1754.36] the gym or whatever.
[1754.94 → 1761.00] But in terms of the so there's that simulated world, but in terms of the actual inputs that
[1761.00 → 1767.44] the AI models are working with in order to like to make decisions, is that just like, just
[1767.44 → 1772.86] video like a, like a human operator would see or there are other, some of these other sensors
[1772.86 → 1777.30] that, and these measurements that you're talking about, can those actually be input to the
[1777.38 → 1778.30] to the models as well?
[1779.18 → 1785.32] So the, the simulator that our teams are using as part of what they call the integrated development
[1785.32 → 1785.82] environment.
[1785.82 → 1789.26] And it's a hardware in the loop kit.
[1789.76 → 1793.06] So think of it as a computer that's running a simulator.
[1793.76 → 1798.14] Then the simulator is connected to basically a dissected drone.
[1798.36 → 1803.02] So there are the cameras and this drone in particular has four cameras.
[1803.40 → 1805.60] There's the inertial measurement units that I mentioned.
[1806.22 → 1809.68] There's a laser range finder, which points down at the ground.
[1809.84 → 1815.62] And that gives the drone a measure of its altitude at a pretty high sample rate, something
[1815.62 → 1816.46] like 200 Hertz.
[1816.82 → 1818.62] And then there's the Xavier itself.
[1819.38 → 1823.96] And when they're running the simulator, everything they're getting on the screen.
[1824.06 → 1828.32] So let's say they're, they have an environment that looks like a warehouse, and they're flying
[1828.32 → 1830.56] towards a, a racing gate.
[1830.86 → 1838.20] That visual input is then run through the cameras, which then output that into the GPU, which then
[1838.20 → 1839.06] processes it.
[1839.60 → 1844.04] So it's replicating the exact process that they would be using on the drone.
[1844.04 → 1844.48] Yes.
[1845.42 → 1850.60] So there's definitely various inputs to the AI models, but in this sort of simulated environment,
[1850.60 → 1855.30] those inputs are simulated as if they were flying around the track.
[1855.40 → 1858.36] Of course, like you mentioned, there's like these deltas that they have to deal with.
[1858.40 → 1862.80] And it's not always exactly the same, but it's meant to mimic that as close as possible.
[1863.04 → 1863.42] That's right.
[1863.66 → 1864.16] Makes sense.
[1864.52 → 1870.70] It seems like a heavy, like with four cameras, this laser range finder, the GPU, all of this
[1870.70 → 1873.38] stuff, it's like a, a pretty intense drone.
[1873.66 → 1875.22] How big is this thing?
[1875.22 → 1877.64] And like, how long can it run?
[1877.68 → 1880.96] You mentioned the races were about like, uh, what did you say?
[1881.02 → 1881.90] Like a minute or something?
[1882.72 → 1882.80] Yeah.
[1882.82 → 1885.80] The human piloted races are about a minute-long.
[1885.92 → 1891.68] The drone itself could probably run for about five minutes before the battery started to run
[1891.68 → 1891.88] out.
[1891.88 → 1897.20] And how long it takes really is going to depend on how proficient our teams are with their
[1897.20 → 1902.68] algorithms, which is, you know, partially based on their ability to program, partially
[1902.68 → 1906.06] based on the fidelity of the simulation environment that we're providing.
[1906.62 → 1910.62] And, you know, we're working really hard to continuously upgrade that to make it as accurate
[1910.62 → 1911.26] as possible.
[1911.50 → 1916.30] If everything's looking great, they should be able to fly through this thing and in, you
[1916.30 → 1919.02] know, seconds, you know, 30 seconds, 40 seconds, a minute.
[1919.02 → 1924.36] But if you look at the current state of the art, so to speak, you know, there's been other
[1924.36 → 1926.56] attempts to do autonomous drone racing.
[1927.20 → 1929.08] IRON competition comes to mind.
[1929.72 → 1934.24] They go pretty slow there because it takes a long time to orient and figure out what they're
[1934.24 → 1934.56] doing.
[1934.84 → 1938.26] So still, I don't think it would take more than two, three minutes tops.
[1938.90 → 1944.58] You know, Alpha Pilot is a fantastic way of showing, you know, how current AI technologies
[1944.58 → 1950.88] are driving autonomy kind of in a small, a small scale and stuff, but just in a larger
[1950.88 → 1954.22] sense in general, how do you see AI as an enabler for autonomy?
[1954.90 → 1959.64] What has Alpha Pilot brought you to in terms of how you think about this since you're part
[1959.64 → 1961.20] of this world on a day-to-day basis?
[1962.00 → 1966.78] Well, the work I've been doing with Alpha Pilot and with artificial intelligence in general
[1966.78 → 1969.04] has been pretty enlightening for me.
[1969.28 → 1974.20] It's something I haven't specifically studied, but the range of applications is just so broad.
[1974.20 → 1981.28] And it's not always in the most obvious ways or the way people would think, you know, self-driving
[1981.28 → 1987.82] cars always come to mind, or robotic systems come to mind, but basic optimization of business
[1987.82 → 1994.02] processes or human functions like scheduling and calendars and email and things like that,
[1994.10 → 1996.34] you know, AI is already making a huge difference.
[1997.18 → 2001.48] And I think that it can't be overlooked because that's really how it touches everybody's lives.
[2001.62 → 2003.20] That really gets it out there.
[2003.20 → 2005.06] Everybody gets some level exposure to it.
[2005.52 → 2008.48] Things like home assistants work in the language space.
[2008.58 → 2010.14] Others work in the written space.
[2010.74 → 2015.86] You know, and I think the more we all become familiar with AI and the more we have opportunities
[2015.86 → 2022.12] to see it doing cutting edge things like flying a drone all by itself in a very friendly environment,
[2022.12 → 2029.10] in a competitive environment that's fun and encouraging, the more everybody is going to get inspired
[2029.10 → 2031.46] by it, and we're going to come up with even greater ideas.
[2031.46 → 2038.26] So partly I'm assuming that Lockheed is interested in this sort of innovation challenge because of the
[2038.26 → 2043.40] algorithm and the automation part of it that could be applied even outside of flight.
[2043.40 → 2054.56] But inside of flight, like when we're thinking about maybe like commercial airline flight in the future or even recreational planes or military planes or all that,
[2054.56 → 2063.62] like what do you see as kind of the near term applications of AI within flight?
[2063.62 → 2069.78] I know that like the for example, the car industry, they're kind of going through all, you know, figuring out all of this stuff.
[2069.90 → 2075.48] And there's talk about, oh, well, it's first going to happen in, you know, long range trucking.
[2075.48 → 2078.54] And there's always going to be like a human operator there.
[2078.54 → 2082.10] And like, what does that look like in terms of flight?
[2082.24 → 2090.40] What do you kind of see as the sort of near term applications of AI in flight, whether that's commercial or military or whatever?
[2091.44 → 2094.36] Yeah, so it's always fun to talk about what AI could do.
[2095.04 → 2100.68] But I think it's equally important to talk about what it can't do, what it should do or what it shouldn't do.
[2100.68 → 2112.42] And when you're talking about military aircraft or space exploration or anywhere where you're putting a human in a dangerous or difficult and extreme environment,
[2112.42 → 2120.92] there are certain things that AI should be doing or could be doing that really improve the safety or overall quality of that mission.
[2120.92 → 2141.50] And those are generally lumped into things like cognitive assistance, where somebody under stress has a high cognitive load, and they make mistakes, or they're more prone to make mistakes or where their reaction time is limited, or it suffers to some extent.
[2141.72 → 2144.56] That's where AI can really help save lives.
[2144.98 → 2147.90] And we are using it in that capacity already.
[2147.90 → 2160.52] Another area that's fascinating is teaming environments, where you have a human piloting an aircraft, and you may have that human commanding a fleet of autonomous vehicles.
[2161.30 → 2169.04] So it's really the interchange between human piloted vehicles and unmanned or autonomous vehicles working together.
[2169.24 → 2171.72] And then they really become an extension of the human.
[2171.72 → 2179.44] And they provide additional mission capacities, or they help them with certain functions and basically extend the reach.
[2180.28 → 2185.20] So in terms of like, if I'm thinking of commercial airline flight, for example,
[2185.20 → 2194.00] it seems like if I compare the sort of drone racing you're doing, which already like within this confined space with like a small device,
[2194.00 → 2200.04] we're talking about like four cameras, a laser range finder, all of these inputs that it's receiving.
[2200.30 → 2201.44] And it's a challenge.
[2201.44 → 2212.82] Would I be right in saying that at least in the near term, like AI might be processing inputs like within a flight to, you know, help augment pilots.
[2212.82 → 2220.34] But it may be unlikely that we're going to be seeing like autonomous 747s everywhere really soon.
[2221.32 → 2224.88] Yeah, I think we can certainly get to that point, you know, someday.
[2225.24 → 2231.70] But in the near term, you know, whenever you have, you know, precious cargo or human lives on board, you know,
[2231.70 → 2236.96] this is what I was talking about where you need to think about the limits of AI or what AI shouldn't do.
[2236.96 → 2244.52] And right now, there is a certain need for a human to have a level of control in that decision-making loop.
[2244.92 → 2249.60] And if you're talking about passenger aircraft, I don't think you're going to see them fully automated anytime soon.
[2250.18 → 2257.16] There's a certain level of comfort and dynamics that a human can bring to decision-making that I think you need a pilot for.
[2257.86 → 2262.46] But you might be able to say so let's say there's a pilot flying a 747.
[2263.34 → 2265.54] Mount Davy or 747 is so old.
[2265.54 → 2268.52] Yeah, I was trying to think of a don't make it a max.
[2268.68 → 2276.68] OK, just being fully transparent here, being on a call with two people from Lockheed Martin and trying to come up with a valid aircraft name.
[2277.22 → 2280.04] 747 was the only thing I was really confident in.
[2280.14 → 2281.34] So that's what I went with.
[2281.38 → 2283.92] But I realize that's probably extremely out of date.
[2284.12 → 2287.48] I wouldn't want to go for like the Boeing max, whatever.
[2287.48 → 2299.12] So I think it would be totally feasible in the near future to see a pilot land their 747 and the onboard AI is flying in parallel.
[2299.46 → 2303.68] And then that pilot can compare their performance to the AI's performance.
[2303.68 → 2307.14] And either the AI learns from the pilot or the pilot learns from the AI.
[2307.30 → 2312.70] So those types of things are already in motion, and they have tremendous benefits attached to them.
[2312.70 → 2319.82] So I'm curious outside, you know, we've been talking about light, you know, within air, within the atmosphere.
[2319.82 → 2331.94] I'm just curious what your thoughts are in general about other environments and, you know, you know, whether it be space, whether it be underwater and, you know, where when we might see inroads there.
[2332.04 → 2333.56] Do you have any insight into any of that?
[2334.44 → 2336.30] Yeah. So, you know, we're at Lockheed Martin.
[2336.48 → 2341.88] We're looking now at autonomous vehicles for use in humanitarian aid and disaster relief.
[2341.88 → 2351.74] And there are a lot of different scenarios, especially in that area where you have difficult to reach environments, or you have destruction of local infrastructure.
[2352.14 → 2355.92] And it's really hard to put a human in there, and it's very time-sensitive.
[2356.18 → 2362.24] So that's a great near term application where autonomous vehicles can do a lot of good.
[2362.66 → 2370.26] You're already seeing things in the news about them being used to deliver, you know, blood and medical supplies too hard to reach places.
[2370.26 → 2372.36] That's another immediate application.
[2373.10 → 2386.02] And then as we really start to grow into things like space exploration, going back to the moon or putting a human on Mars, you get in these situations where you have communications latency given to the huge distance.
[2386.80 → 2389.56] And you need to make decisions local.
[2389.90 → 2394.10] So you need an autonomous vehicle that can process information and make its own decisions.
[2394.10 → 2400.40] So I think you'll see as we get into the new space age, you'll see AI playing a huge role there.
[2401.00 → 2402.94] And then I think you mentioned undersea as well.
[2403.06 → 2409.68] And this is an area what's actually already in practice with some of the autonomous vehicles we're developing at Lockheed Martin.
[2409.94 → 2415.78] We've already used them for things like undersea oil rig inspection after some of the hurricanes in the Gulf.
[2415.78 → 2420.32] And just yet another domain where it's hard for a human to go safely.
[2420.74 → 2427.64] And it's also hard for a human to analyze the situation very well because it's not their traditional element.
[2427.94 → 2430.08] So these types of things are just right for AI.
[2430.08 → 2445.94] So if I'm, and I've probably shown my ignorance of drones and flight throughout this interview, but if I'm out there, maybe our listeners are wanting to, you know, get involved with drones and maybe do their own experiments.
[2445.94 → 2458.86] Are there accessible ways that they can kind of experiment with maybe its computer vision or other things with drones without kind of being part of this elite group of teams competing at this level?
[2458.96 → 2465.24] I think if I remember right, there's like there's at least some drones that have AI inference chips on.
[2465.36 → 2466.00] Am I right about that?
[2466.08 → 2468.88] Maybe, you know, of some good ways to get involved.
[2468.88 → 2477.64] So there are a couple of commercial drones that are starting to have onboard computers where you can, you know, you could do some amazing stuff with them.
[2477.68 → 2478.74] And there are a lot of fun things.
[2478.86 → 2482.22] They have like an onboard Raspberry Pi or an NVIDIA NATO.
[2482.84 → 2497.92] And that's enough compute for you to basically learn the basics of how to code so that a drone can read input from its cameras and use that to make guidance, navigation and control decisions and fly autonomously.
[2497.92 → 2500.84] So there are a lot of great beginner kits out there.
[2501.74 → 2516.84] And then if you want to experience what some of the pilots are dealing with for Alpha Pilot and for the air season, we actually have the simulation environment we used in our qualifier, which is different from the one the teams are using now.
[2517.10 → 2525.68] But it's, you know, high calibre simulation environment uses the robotic operating system that has been made available open source through MIT.
[2525.68 → 2527.54] And it is called Flight Goggles.
[2528.14 → 2536.32] It was developed by a consultant on our program, Dr. Sur tosh Karajan at MIT, who's been a huge help in setting this whole thing up.
[2536.60 → 2538.38] And it's a great, fantastic tool.
[2538.52 → 2541.42] I encourage anyone to just go check it out, even if you're just flying manually.
[2541.52 → 2542.16] It's a lot of fun.
[2542.90 → 2543.48] Sounds great.
[2543.48 → 2554.28] So I guess as we finish up, if you could possibly maybe tell us a little bit about the first couple of races that are coming up, where and how people can access them.
[2554.40 → 2563.12] But also, as you do that, as people engage on this and, you know, families and kids are watching, what would you like to see them take away?
[2563.26 → 2569.06] What kind of impact would you like to have on them as they engage on these initial few races?
[2569.06 → 2571.00] Yeah, I'll start with that one.
[2571.12 → 2573.38] This is something that I find really fascinating.
[2573.88 → 2585.46] I'm so thrilled to be doing racing with AI, because racing has a history of being a catalyst for getting people inspired by new technology.
[2585.46 → 2597.06] And I mean, I gave a talk at MIT a few weeks ago, where I was showing photos of London in the 1890s.
[2597.44 → 2610.82] And I showed an article in the London Times about how they were predicting in several years, the city would be buried in horse manure, because the current solution of horses and buggies was just not sustainable.
[2610.82 → 2614.56] And people were really freaked out about this at the time.
[2614.64 → 2619.24] And they thought, you know, we're at the edge, you know, this is as far as society can go, right?
[2620.12 → 2625.22] And, you know, the automobile was invented, and people just kind of wave it off.
[2625.36 → 2626.82] And they're like, that, that thing's a monstrosity.
[2627.64 → 2629.00] You know, I don't know how to use it.
[2629.56 → 2632.50] You know, everybody, all horses are so integral to society.
[2632.50 → 2634.16] And you just want to get rid of them.
[2634.30 → 2637.04] And you want to use these things now, I don't know how to use it.
[2637.50 → 2638.90] And I don't know how to work with it.
[2638.90 → 2642.74] And, you know, it just floundered for quite a few years.
[2643.04 → 2647.88] And because nobody was demanding it, the scale of production was low, the prices were high.
[2648.42 → 2654.76] And I think that, you know, when people started racing cars and made a spectacle of it,
[2655.12 → 2661.38] is when really people started to come around to the idea of these things being a technology of the future.
[2661.38 → 2665.72] And it took kind of the mysticism out of it.
[2665.80 → 2670.24] And if you can watch, if you can, you know, pay a dollar and go watch these things race,
[2670.36 → 2674.76] then they're not something that's reserved for a select few.
[2674.86 → 2675.92] They're part of your life now.
[2676.32 → 2678.78] And that's what we want to do with Alpha Pilot.
[2678.94 → 2682.80] We want to make artificial intelligence and autonomy part of everybody's lives.
[2682.94 → 2688.36] You know, everybody can watch these races on NBC Sports or Twitter and feel some ownership in it.
[2688.36 → 2693.94] Or they can come to our race events, which are free to the public and feel a little bit of ownership in that AI
[2693.94 → 2698.22] and feel like maybe this isn't something that is closed off to them.
[2698.28 → 2700.82] Maybe it's a lot easier to get involved than they initially thought.
[2701.16 → 2707.72] And if they're inspired to go home and do a little more research or maybe try and see what other great things are going on in AI,
[2707.88 → 2711.48] then I feel like we've done our job to help inspire that next generation.
[2711.48 → 2717.66] Fantastic. And when are those first couple of races, and where are they, so people can show up for them or watch them online?
[2717.92 → 2722.52] So the first race is going to be October 8th at the University of Central Florida.
[2722.94 → 2725.52] And it's going to be an all-day event.
[2725.64 → 2729.70] We're going to have some great Lockheed Martin products on display.
[2730.30 → 2735.04] We're going to have the UCF drone racing team there showcasing some of their capabilities.
[2735.28 → 2737.94] Some of the DRL professional pilots will be there doing the same.
[2737.94 → 2744.02] And we'll have some great commentary about what people are seeing in the races and about AI in general.
[2744.46 → 2746.94] So tickets will be made available on Ticketmaster.
[2747.76 → 2750.94] And you can find that through the DRL website.
[2751.12 → 2753.74] It's the droneracingleague.io or drl.io.
[2754.42 → 2762.34] And yeah, the races will also be included in the Drone Racing League's content on NBC Sports and on Twitter.
[2762.34 → 2770.98] And we are filming all of this, all the behind the scenes, what the teams are going through, what we're going through, what happens at the races.
[2771.20 → 2783.02] All this great human drama associated with the AI is going to be put together throughout the season and then hopefully released as a documentary on one of the great on-demand platforms.
[2783.54 → 2784.50] That sounds fantastic.
[2784.72 → 2785.94] I'm personally very excited.
[2785.94 → 2790.08] My small role on the team is to do some AI commentary.
[2790.82 → 2795.16] And so I can't wait to be in Orlando on the 8th of October.
[2795.50 → 2797.34] And looking forward to seeing you there, Keith.
[2797.40 → 2803.44] Thank you so much for coming on Practical AI and kind of taking us into a deep dive into Alpha Pilot.
[2803.84 → 2805.56] And thanks so much.
[2806.08 → 2806.36] Of course.
[2806.42 → 2807.14] This was a lot of fun.
[2807.36 → 2807.76] Thanks, guys.
[2807.76 → 2810.56] All right.
[2810.62 → 2813.24] Thank you for tuning into this episode of Practical AI.
[2813.52 → 2814.96] If you enjoyed this show, do us a favour.
[2815.08 → 2815.66] Go on iTunes.
[2815.78 → 2816.48] Give us a rating.
[2816.72 → 2818.60] Go in your podcast app and favourite it.
[2818.72 → 2821.42] If you are on Twitter or social network, share a link with a friend.
[2821.50 → 2823.86] Whatever you got to do, share the show with a friend if you enjoyed it.
[2824.16 → 2826.82] And bandwidth for Changelog is provided by Vastly.
[2826.94 → 2828.36] Learn more at Fastly.com.
[2828.36 → 2831.76] And we catch our errors before our users do here at Changelog because of Rollbar.
[2831.94 → 2834.38] Check them out at Rollbar.com slash Changelog.
[2834.70 → 2837.18] And we're hosted on Linde cloud servers.
[2837.18 → 2839.14] Head to Linode.com slash Changelog.
[2839.24 → 2839.70] Check them out.
[2839.78 → 2840.60] Support this show.
[2841.02 → 2844.22] This episode is hosted by Daniel Whiten ack and Chris Benson.
[2844.66 → 2846.72] The music is by Break master Cylinder.
[2847.14 → 2850.54] And you can find more shows just like this at Changelog.com.
[2850.72 → 2852.68] When you go there, pop in your email address.
[2852.98 → 2858.98] Get our weekly email keeping you up to date with the news and podcasts for developers in your inbox every single week.
[2859.38 → 2860.16] Thanks for tuning in.
[2860.32 → 2861.04] We'll see you next week.
[2868.10 → 2869.76] Thanks.
[2889.78 → 2890.14] See you next week.
