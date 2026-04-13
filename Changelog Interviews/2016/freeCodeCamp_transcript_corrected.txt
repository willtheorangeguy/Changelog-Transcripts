[0.00 → 3.22] I'm Quincy Larson, and you're listening to The Change Log.
[12.50 → 16.62] Welcome back, everyone. This is The Change Log, and I'm your host, Adam Stachowiak.
[16.80 → 21.86] This is episode 195, and today we're talking to Quincy Larson about a big subject,
[22.22 → 27.12] learning to code at FreeCodeCamp. We talked to Quincy about the secret to getting good at coding.
[27.12 → 33.58] We learned about their curriculum, spending a solid year, 2,080 hours of deliberate coding practice.
[34.02 → 36.58] We discussed plans for financial sustainability of the project.
[36.88 → 40.66] We talked about the people behind it, both on the leading and the teaching side,
[40.82 → 43.52] as well as the camper side, and so much more.
[43.94 → 50.06] We have four sponsors for the show today, Code Ship, DigitalOcean, Upbeat, and True Sight Pulse.
[50.70 → 55.62] Our first sponsor is Code Ship, and they have a free webinar coming up on February 25th,
[55.62 → 61.18] where co-founders Florian and Manuel will discuss their new continuous integration and delivery platform
[61.18 → 63.00] with native Docker support.
[63.48 → 66.08] They will give a walkthrough of how the platform works,
[66.48 → 69.16] examples of working with Docker Compose features,
[69.66 → 73.46] as well as live, real-world examples of working with the platform.
[73.80 → 75.28] Two killer features I have to mention.
[75.42 → 79.62] Number one, you can use existing Docker files in your Docker Compose YAML files
[79.62 → 81.38] with the Code Ship Docker platform.
[81.38 → 83.76] There's no need to rewrite service definitions.
[84.50 → 88.94] And number two, you can use the Code Ship Docker CLI tool to run tests locally,
[88.94 → 92.82] so you ensure absolute parity with your CI environment.
[92.98 → 97.88] If that gets you excited, head to resources.codeship.com slash webinars.
[98.24 → 102.34] And the very first webinar in the list is the webinar I'm talking about.
[102.44 → 105.04] Click through to that, sign up, you'll be good to go.
[105.04 → 106.72] And now on to the show.
[114.36 → 117.10] All right, everyone, we're here today joined by Quincy Larson.
[117.36 → 119.28] And Quincy started an open source community.
[119.38 → 120.34] We had to get him on the show.
[120.38 → 122.46] He's been trending on Change All Nightly.
[122.56 → 123.72] It's called Free Code Camp.
[123.80 → 126.18] And we're here to talk about his journey and the plans
[126.18 → 128.54] and the impact of Free Code Camp
[128.54 → 131.72] and how it's having an impact on the software development world.
[132.60 → 133.84] Quincy, welcome to the show, my friend.
[133.84 → 135.36] Thank you for having me.
[135.86 → 138.40] And I think that the best way, Jared, might be to kick the show-off
[138.40 → 141.92] with yet another mention to this awesome thing we have called Change All Nightly.
[142.08 → 143.52] It's our own radar.
[143.64 → 146.10] That's how we found out about Free Code Camp.
[146.46 → 149.38] And this is an email we ship out every single night
[149.38 → 153.10] that features top repos on GitHub in the last 24 hours.
[153.20 → 156.22] So if you're on a web browser or able to do so,
[156.28 → 157.86] go to changelog.com slash nightly.
[157.94 → 158.76] Subscribe to that.
[159.58 → 162.30] But, Jared, let's kick things off with you telling us a bit about
[162.30 → 165.98] how we found Free Code Camp through Change All Nightly
[165.98 → 167.52] and how it kind of bubbled up to get our attention.
[168.34 → 170.96] Yeah, well, lots of times certain projects will get our attention
[170.96 → 173.68] because they pop up into the top new list.
[174.50 → 175.98] And then eventually they'll,
[176.08 → 178.60] sometimes they'll show up in the top overall list as well,
[178.82 → 181.32] which means they're not just creating the last 24 hours,
[181.40 → 184.52] but overall the most starred repos on GitHub for the day.
[185.24 → 189.16] Free Code Camp is one of those that has been chilling in Nightly for months.
[189.16 → 194.06] I mean, it routinely is the top-starred repository,
[194.56 → 196.04] or at least in the top five.
[196.72 → 197.54] And we started wondering,
[197.76 → 199.80] what the heck's going on with this Free Code Camp?
[199.92 → 200.68] Everybody loves it.
[200.72 → 201.64] It's getting starred like crazy.
[202.86 → 204.36] In fact, we checked it out,
[204.42 → 208.40] and it looks like it's number two overall starred repo on GitHub
[208.40 → 213.12] with something like 72,000 stars currently,
[213.84 → 215.16] second only to Bootstrap,
[215.52 → 217.18] which everybody knows and loves,
[217.18 → 218.88] and which has been around for quite a bit longer.
[219.10 → 221.78] So we almost just couldn't even ignore it.
[221.86 → 223.90] It was just there in our inbox every single night.
[224.86 → 226.02] Quincy, what does that make you feel like, man?
[226.04 → 227.96] Does that make you feel like a rock star or what?
[228.08 → 229.16] Or you're doing something right?
[229.52 → 231.02] How does that impact you?
[231.88 → 236.52] I'm extremely humbled by the attention Free Code Camp's been getting.
[237.22 → 238.92] And yeah, I feel great.
[239.06 → 241.76] And I'm excited about the prospects.
[241.76 → 245.96] It's definitely steered a lot of developers
[245.96 → 249.08] that regularly contribute to open source
[249.08 → 253.68] to coming and putting in pull requests and filing issues.
[254.22 → 257.76] And including Sadat,
[258.20 → 260.02] is S-A-H-A-T.
[260.82 → 263.12] He created the hackathon starter,
[263.34 → 267.80] which was actually the Node.js rollout, if you will,
[267.86 → 270.58] the boilerplate that I started Free Code Camp with.
[270.58 → 274.52] So he actually had a ton of commits on Free Code Camp to begin with.
[274.66 → 277.84] And he came back the other day and followed the PR.
[278.80 → 280.58] So was it a surprise to you, I guess, to...
[281.54 → 283.32] One, were you familiar with Chainsaw Nightly?
[283.62 → 285.86] Did you know you had been trending for months now, basically?
[286.52 → 286.92] No.
[287.10 → 287.84] I mean, obviously on GitHub,
[288.02 → 290.44] but you've been appearing every single time in this email?
[291.24 → 292.28] I wasn't aware of that.
[292.54 → 295.24] I, of course, people will mention occasionally,
[295.40 → 297.84] like, hey, you're trending on GitHub and stuff.
[297.84 → 299.66] And I'll be like, awesome, check it out.
[299.86 → 301.84] And I remember the first day that we were trending,
[302.62 → 305.76] it was, I think, during jQuery SF,
[306.12 → 308.26] which was a big event here in San Francisco.
[309.14 → 312.08] And I just remember the feeling, like, whoa.
[313.54 → 317.22] We're right behind Facebook and Google
[317.22 → 318.62] and some other major companies
[318.62 → 321.78] that were really, you know, open sourcing tools at the time.
[321.92 → 324.54] I think, like, React Play framework
[324.54 → 327.08] or something was being open sourced partially.
[327.50 → 330.22] And, yeah, so it was definitely
[330.22 → 334.58] a big shot in the arm in terms of morale.
[336.00 → 337.32] Behind the scenes, you don't know this,
[337.38 → 338.68] but Jared and I have kind of been watching
[338.68 → 339.76] what you've been doing
[339.76 → 343.88] simply because you're daily on our nightly radar,
[343.96 → 344.44] so to speak.
[344.50 → 346.68] And so we kind of feel like we know what you're doing already,
[346.68 → 348.56] but it's great to finally get you on the show.
[349.46 → 350.22] I'm excited to be here.
[350.38 → 352.16] I'm a long-time Changelog listener,
[352.44 → 354.82] so I was honoured and thrilled
[354.82 → 357.82] when you submitted that GitHub issue
[357.82 → 360.44] requesting that, like, I come on the show.
[361.50 → 363.66] That's cool, too, because, Jared,
[363.70 → 365.78] how often do we have long-time listeners on the show?
[365.92 → 368.76] Is it often or is it few and far between?
[368.78 → 369.18] Every once in a while.
[369.18 → 373.14] Yeah, I mean, it's less often than I'd like to hear,
[373.34 → 376.70] but it's always nice when somebody both listens
[376.70 → 377.64] and comes on the show.
[378.14 → 380.22] And since we're mentioning the show,
[380.74 → 383.60] Quincy, you really enjoyed the show just before this show,
[383.68 → 385.44] so this is episode 195.
[386.40 → 390.10] Episode 194 featured Jose Valid talking about Elixir.
[390.28 → 391.38] You like that show a lot, too,
[391.40 → 392.54] but long-time listener of the show.
[392.64 → 396.16] It's always nice to have someone on the show
[396.16 → 397.40] that's listened.
[397.80 → 398.18] It's great.
[398.18 → 400.76] So in this case, you probably know what's coming next,
[400.90 → 402.72] which is the same thing we did with Jose,
[403.38 → 406.78] is we like to hear about our guests' origin stories,
[407.06 → 409.10] how you got to where you are now,
[409.56 → 411.52] because we find those to be informative,
[411.84 → 413.76] inspiring, and really help us
[413.76 → 415.60] and the listeners relate to you
[415.60 → 417.30] and what you're doing at FreeCodeCamp.
[417.42 → 420.70] So could you tell us your hacker origin story?
[421.52 → 421.92] Absolutely.
[422.62 → 425.66] So I started out as a teacher
[425.66 → 428.68] and progressed to a school director
[428.68 → 432.42] over kind of process of about 10 years.
[432.82 → 436.22] I ran schools in both the U.S. and China.
[437.16 → 438.82] And along the way,
[438.88 → 441.52] I was doing these very repetitive workflows,
[441.76 → 443.14] you know, involving immigration,
[443.44 → 445.68] involving grade reports
[445.68 → 448.22] and enrolment documentation.
[448.22 → 456.20] And I just kind of decided that I wanted to learn more about how to automate those processes
[456.20 → 462.14] and speed things up so that I could free my school's administrative staff
[462.14 → 465.46] and teachers from the tedium of just filling in work,
[465.80 → 467.42] you know, paperwork the old-fashioned way.
[467.42 → 471.14] And so that kind of kicked off a journey into, you know,
[472.58 → 474.70] writing Excel macros
[474.70 → 480.10] and ultimately writing little scripts that did things.
[480.60 → 486.72] And once I was able to basically facilitate my entire staff
[486.72 → 489.60] being able to spend more time with the students
[489.60 → 493.70] and less time in front of their computer in their offices by themselves,
[493.70 → 497.26] I started to really think about how
[497.26 → 501.94] this technology could be applied more broadly
[501.94 → 505.62] to help teachers and school administrators.
[506.46 → 510.62] And that's when I decided to kind of take the plunge and leave my job
[510.62 → 514.02] and just focus on learning to develop software full-time.
[514.68 → 519.30] So I did that for several years.
[520.36 → 523.00] I can go a little bit into how that went.
[523.00 → 527.80] Basically, I shuttered myself in a hacker space
[527.80 → 532.32] because I couldn't find the motivation to work at home at my kitchen table,
[532.58 → 533.84] which was my original plan.
[534.00 → 535.88] I just, there was too much to distract me.
[535.96 → 536.70] There was the fridge.
[537.64 → 540.66] There were all these little things, little excuses.
[540.82 → 545.08] Whenever I hit like a brick wall, I had some convenient chore that I had to go do.
[545.76 → 546.34] I know the feeling.
[547.24 → 548.60] So I locked myself in.
[548.68 → 551.64] At the time I was living in Santa Barbara, Santa Barbara hacker space.
[551.64 → 553.68] It was just a room at the time.
[554.38 → 562.00] It was very small and was stacked high with dead Roomba's and other drone-type gear and stuff.
[562.12 → 567.44] And I just sat in there on their Wi-Fi and crunched through a lot of programming books
[567.44 → 572.16] and worked through a lot of online courses through Coursera and EDX.
[572.80 → 575.12] And I was really all over the map.
[575.76 → 580.12] And it took me a long time to get good enough that I could actually go,
[580.38 → 584.50] I mean, like basically seven months of just going to hackathons nonstop
[584.50 → 587.12] and coding, you know, 60, 80 hours a week.
[587.12 → 592.14] And then finally, I was able to get a software engineering job.
[593.14 → 601.54] And of course, that itself was a completely brutal process of being told I was wrong repeatedly
[601.54 → 603.82] by both humans and machines.
[603.82 → 612.32] And I just continued learning to code because I was really passionate about helping teachers
[612.32 → 617.96] and school directors like myself just automate these workflows.
[618.24 → 620.72] And I figured that there would be a way that I could do that at the end.
[621.18 → 626.18] But along the way, I kind of discovered that the real struggle was just learning to code itself.
[626.18 → 630.12] That what I was doing, you know, this self-directed learning thing,
[630.70 → 636.64] where I was spending days and days going off in the wrong direction down these rabbit holes
[636.64 → 641.14] with, you know, debugging Linux drivers and all these other things,
[641.50 → 644.34] that this wasn't necessarily the optimal way of doing it.
[645.48 → 650.62] So that's when I started seriously thinking about coding education.
[650.62 → 660.80] And that eventually led me to put up the prototype for FreeCodeCamp and see if we could get any traction.
[661.84 → 666.38] I think it's interesting to, you know, hopefully repaint this, what you, the story you just shared.
[666.46 → 674.80] So it sounds like you came from a teacher background with no formal or traditional training in software development.
[674.80 → 678.74] You taught yourself through, you know, the school of hard knocks, basically,
[679.36 → 684.26] either finding community and, you know, immersing yourself in that,
[684.46 → 690.42] and then finding out that essentially software is the is a way to help people back into your original position,
[690.48 → 691.14] which was a teacher.
[691.64 → 694.00] And that's sort of been your path.
[694.04 → 694.58] Is that about right?
[694.62 → 695.20] Is that fair to say?
[695.66 → 696.32] Yeah, absolutely.
[696.82 → 701.62] It was a circuitous path, but I've always been interested in education.
[701.98 → 703.42] That's, that's my calling.
[703.42 → 710.56] You know, I decided a long time ago that I, that was what I thought the major bottleneck to the progress of civilization was,
[710.62 → 711.50] was education.
[711.66 → 715.56] It wasn't, you know, a lot of other things that people seem to think it is,
[715.58 → 720.06] like access to capital or, you know, rule of law.
[720.18 → 722.24] There are so many other things that you could consider,
[722.38 → 727.96] but I think education is really fundamental and is, is causing a lot of the issues that we're experiencing.
[727.96 → 735.98] And, you know, technology education is going to be the biggest solution to income inequality
[735.98 → 740.60] and a lot of these other problems that we're facing in the 21st century.
[740.60 → 745.86] So just to think back through some of your struggle to learn, you know, software development
[745.86 → 751.90] and the resources and tools that were available to you, you said you had books, which you read.
[752.26 → 757.44] Maybe you could tell us, you know, some of the specifics there, but also, you know, some,
[757.56 → 758.92] some online learning tools.
[758.92 → 764.78] You also seem to be really in surrounding yourself with developers, at least physically.
[764.92 → 771.24] I don't know if you're, you know, working with them or asking them for help, but what were the biggest struggles?
[771.40 → 772.58] Like, what was the hardest part?
[772.64 → 774.24] You said, you know, just learning the code.
[774.72 → 776.42] Can you, can you give us more on that?
[776.46 → 777.26] Can you go into that further?
[778.18 → 778.32] Yeah.
[778.44 → 780.84] I mean, I think learning the code is a struggle.
[781.48 → 786.68] First, I just want to say, as I've said like a million times before, and I'll continue to say,
[786.84 → 788.02] anybody can learn to code.
[788.02 → 789.52] It's just a matter of persistence.
[790.54 → 796.28] I don't think there are any innate properties that give an individual a significant advantage over another
[796.28 → 799.22] in terms of learning to code.
[799.48 → 801.46] It's just a matter of sitting down and doing it.
[801.54 → 804.86] So really at the, at the end of the day, it's a motivational issue.
[806.12 → 811.40] And it's easy to get demotivated when you're reading a book that you checked out from the library
[811.40 → 817.46] where none of the code examples run because you're, you're in Python 3 instead of Python 2, for example,
[817.46 → 818.68] and you didn't realize it.
[819.24 → 827.64] Or, you know, you're enrolling in a machine learning course, and you realize halfway through
[827.64 → 831.98] that you were supposed to have knowledge of this, you know, relatively advanced mathematical
[831.98 → 836.06] subject that you know nothing about.
[836.16 → 840.98] And you basically just had to put that class on hold and, and switch over to learning mathematics,
[841.16 → 841.62] for example.
[841.62 → 850.48] So, so there are a lot of dependency issues, if you will, where if you imagine like learning is a
[850.84 → 852.92] you're learning a big hierarchical thing.
[852.92 → 859.78] And there are so many moving parts underneath that thing that you need to understand before you can get all the way up there.
[860.52 → 866.00] So that was, that was a big part of the problem was there wasn't a clear path.
[866.32 → 868.36] There, there certainly are clear paths.
[868.48 → 873.14] People will every once in a while put up a blog post like, here's how you should learn machine learning
[873.14 → 875.52] and like do this and then this and then this and then this.
[875.52 → 880.44] But this kind of get stale after a while and resources are no longer available.
[881.22 → 884.58] Better resources come out and those are not necessarily updated.
[884.84 → 891.16] So we wanted to make sure that we had like a living curriculum that addressed that specific concern and,
[891.16 → 896.10] and that we really focused on just teaching like one very specific thing, which is web development.
[897.16 → 901.82] So maybe this is fast tracking the whole entire story a bit, but I guess the question I have at this point is like,
[901.82 → 907.08] how do you go from the story you just painted teacher to, you know,
[907.16 → 908.42] and no negative words,
[908.58 → 921.72] want to be coder to immersing yourself in hackathons and around people who are developing software to being the person leading the charge of free code camp and encouraging others and leading people through that struggle to actually program.
[921.86 → 924.80] Like what makes, what made you the right person to do this?
[925.74 → 927.12] Honestly, it could have been anybody.
[927.32 → 929.92] I just happened to be in the right place at the right time.
[929.92 → 931.98] There was a critical mass.
[932.10 → 937.54] I remember very like right when I was considering leaving my career as a school director.
[938.26 → 947.44] That's when Marc Andreessen published the famous now famous software is eating the world essay in the Wall Street Journal.
[947.44 → 960.34] This was right after Sebastian Thrun and also Daphne Collar and Andrew had recently published the
[960.44 → 966.20] their machine learning and computer science classes that were extremely popular.
[966.76 → 969.58] The AI class and the machine learning class respectively, I think.
[969.66 → 973.96] And that really launched Moons in earnest, massive open online courses.
[973.96 → 980.96] So like this was a big discussion in education already and the shift toward technology.
[982.02 → 994.10] Like I really feel that I was on the leading edge of that in the sense that like I was one of the first people in my field to like really realize how significant and permanent that,
[994.10 → 995.76] that shift was.
[995.76 → 1004.76] I think a lot of people to this day kind of even downplay the importance of these scaling technologies where you,
[1004.88 → 1010.40] where you can literally teach hundreds of thousands of people instead of teaching a class of 30 at a time.
[1011.32 → 1017.74] So I think that that was a major part of it was I just happened to be receptive to these things.
[1017.74 → 1022.58] And I was in a position within a school where I could directly take these concepts and apply them.
[1023.72 → 1023.80] And,
[1023.84 → 1026.14] and another thing was,
[1026.22 → 1026.52] you know,
[1026.60 → 1026.74] I,
[1026.86 → 1032.20] I was extremely thrifty, and I'd saved half of what I'd earned for like the past decade.
[1032.42 → 1037.74] So I had like a little baseline in terms of like a runway to support myself.
[1037.86 → 1037.92] Well,
[1037.94 → 1039.76] I just turn through these things.
[1039.76 → 1040.06] I mean,
[1040.06 → 1047.92] most people don't have the resources to just be able to stop what they're doing and spend literally years of their life learning the code.
[1049.56 → 1057.60] And my hope is that they won't have to have those resources because hopefully free code camp will address that partially, and they don't have to leave their jobs or do anything drastic.
[1058.48 → 1061.02] But at the time free code camp didn't exist.
[1061.26 → 1065.22] And I felt that that was the only way that I could really dive into it.
[1065.22 → 1070.28] Cause everybody I saw who was taking like a half-hearted approach just wasn't really getting anywhere.
[1070.56 → 1071.16] So I,
[1071.18 → 1073.22] I would say that it was mostly luck and,
[1073.60 → 1073.74] you know,
[1073.74 → 1073.98] like,
[1074.62 → 1076.72] like Oprah and all these other people have said,
[1076.82 → 1077.58] you know,
[1077.60 → 1079.62] luck is just opportunity and preparation.
[1079.62 → 1081.92] And the opportunity was definitely there.
[1082.78 → 1083.90] I think at this point,
[1083.90 → 1088.24] our listeners probably know what free code camp is in a very nebulous way.
[1088.34 → 1091.56] It's obviously an online learning community or tool.
[1092.12 → 1094.12] But maybe you could give us kind of the
[1094.12 → 1097.52] the summary pitch of it for those,
[1097.62 → 1097.80] you know,
[1097.82 → 1098.72] who are driving or whatnot,
[1098.86 → 1101.54] can't go to free code camp.com and just check it out as we talk,
[1101.92 → 1102.58] give the high level,
[1102.62 → 1104.36] like what it is and what sets it apart.
[1104.76 → 1105.60] And then we'll,
[1105.68 → 1107.16] we'll continue from there.
[1108.02 → 1108.42] Sure.
[1108.42 → 1117.62] Free code camp is an open source community that helps you learn how to code and helps you practice coding by building projects,
[1117.80 → 1124.10] including projects for real life nonprofits that need software solutions to be able to,
[1124.12 → 1125.72] do their jobs more effectively.
[1127.00 → 1127.62] We launched,
[1127.62 → 1128.26] we launched,
[1128.44 → 1129.28] I think in October,
[1129.60 → 1130.56] 2014.
[1131.76 → 1133.84] And along the way,
[1133.84 → 1137.98] we've accumulated like a pretty large core team of contributors,
[1137.98 → 1147.28] both teachers and developers who are working on building this very large open source curriculum that covers web development from end to end,
[1147.28 → 1149.44] starting with basic HTML,
[1149.44 → 1149.84] CSS,
[1150.12 → 1150.48] jQuery,
[1150.78 → 1154.12] and moving all the way through the front end with,
[1154.12 → 1154.72] you know,
[1154.78 → 1159.80] tools like jQuery and react and D3 and,
[1159.80 → 1160.68] and data visualization.
[1160.68 → 1170.60] And then also covers the backend with tools like Node.js express and covers some database ORM stuff as well.
[1171.36 → 1175.50] And ultimately throughout the course of free code camp,
[1175.50 → 1180.70] you're not just sitting there like reading tutorials or watching videos.
[1180.70 → 1182.72] You're actually coding the entire time.
[1183.50 → 1184.00] It's,
[1184.00 → 1189.18] it's approximately 2,080 hours of coding practice,
[1189.18 → 1194.56] which is like a calendar year worth of 40 hours a week work.
[1194.56 → 1195.44] Um,
[1195.88 → 1198.30] and that involves,
[1198.30 → 1199.74] among other things,
[1199.96 → 1200.36] building,
[1200.36 → 1200.82] uh,
[1200.82 → 1202.04] 10 front end projects,
[1202.14 → 1204.68] 10 data visualization projects,
[1204.88 → 1205.18] uh,
[1205.18 → 1208.46] 10 backend projects that are like APIs and microservices,
[1208.46 → 1210.52] and then building,
[1210.52 → 1211.06] uh,
[1211.10 → 1215.80] two projects for nonprofits and maintaining two other legacy projects.
[1216.32 → 1216.72] Um,
[1216.74 → 1219.18] because we think working with legacy code is really important.
[1219.18 → 1221.14] And then we're working on an
[1221.14 → 1221.44] uh,
[1221.44 → 1224.10] interview preparation component as well that'll cover like,
[1224.10 → 1224.66] you know,
[1224.72 → 1227.54] pair programming on the interview and,
[1227.58 → 1227.76] uh,
[1227.76 → 1229.58] whiteboard coding and things like that.
[1229.62 → 1229.98] Um,
[1229.98 → 1230.28] and we,
[1230.30 → 1232.94] we focus a lot on pair programming throughout.
[1233.58 → 1234.10] Um,
[1234.18 → 1234.38] we,
[1234.48 → 1239.62] we have live chat rooms where community members just volunteer to,
[1239.62 → 1240.58] to help each other.
[1240.58 → 1241.40] So at any time,
[1241.40 → 1242.86] if you get stuck on a coding challenge,
[1242.86 → 1243.96] you can just click a help button.
[1244.00 → 1248.34] It'll open up a chat room, and you can immediately get help on whatever your issue is.
[1248.84 → 1249.28] And,
[1249.32 → 1249.52] uh,
[1249.52 → 1249.66] we,
[1249.74 → 1251.98] we've made extensive use of external tools.
[1252.10 → 1252.68] So we use Gitter,
[1252.68 → 1254.18] which is a great,
[1254.36 → 1254.74] um,
[1254.92 → 1255.98] it's kind of like Slack,
[1256.12 → 1261.42] but it's for open source communities, and it's really well-built and maintained by these,
[1261.42 → 1261.78] uh,
[1261.78 → 1262.58] gentlemen out in,
[1262.58 → 1263.50] uh,
[1263.72 → 1264.04] London.
[1264.04 → 1265.80] So,
[1265.80 → 1266.50] uh,
[1266.54 → 1266.80] yeah,
[1266.86 → 1267.10] it's,
[1267.10 → 1268.86] it's a community first and foremost,
[1268.86 → 1270.52] it's spread across Reddit,
[1271.14 → 1271.88] across medium.
[1272.76 → 1273.16] Uh,
[1273.28 → 1281.78] and of course we have almost a thousand local groups called campsites throughout the world where campers,
[1281.98 → 1284.04] that's what we call community members.
[1284.16 → 1286.08] Campers will get together and,
[1286.08 → 1286.52] uh,
[1286.52 → 1287.10] code together.
[1287.10 → 1288.58] We call them coffee and codes.
[1288.58 → 1295.74] They'll like to buy some coffee and sit down in the Starbucks or whatever café and just code together for a while.
[1295.74 → 1298.00] So it's like live in-person pair programming.
[1298.26 → 1298.48] And some,
[1298.72 → 1299.88] sometimes it'll be two people.
[1299.96 → 1303.54] Sometimes it'll be 40 people in like Delhi or Seoul or some of these bigger cities.
[1304.08 → 1308.58] It's a mix of coding to learning to code through,
[1308.66 → 1308.98] you know,
[1309.26 → 1309.82] resources,
[1309.96 → 1310.76] actual curriculum,
[1311.38 → 1312.06] a community,
[1312.06 → 1313.14] uh,
[1313.26 → 1315.94] leveraging some social media aspects like medium Reddit,
[1315.94 → 1318.20] or even not so many meetups,
[1318.24 → 1319.60] but your local meetups,
[1319.60 → 1320.54] uh,
[1320.54 → 1321.56] something you got like a thousand.
[1321.70 → 1322.62] It seemed like,
[1322.62 → 1324.62] I think when I zoom back out,
[1324.76 → 1324.80] I,
[1324.96 → 1326.76] I think that sounds really,
[1326.90 → 1327.40] really awesome.
[1327.70 → 1331.36] But I also heard you say earlier that you bootstrap this thing on your own dime.
[1331.36 → 1331.60] It's,
[1331.64 → 1332.24] it sounded like,
[1332.24 → 1335.02] so there's a little bit of a story I'm kind of missing there,
[1335.02 → 1335.62] which is like,
[1335.62 → 1337.26] if you put away for 10 years,
[1337.26 → 1338.02] a decade,
[1338.02 → 1338.94] uh,
[1338.96 → 1339.20] you know,
[1339.20 → 1340.22] half of what you earned,
[1340.22 → 1341.92] it sounds like you fit the bill.
[1341.96 → 1342.14] You,
[1342.52 → 1344.88] I'm not trying to like harp on how much money it takes.
[1344.88 → 1348.38] I'm trying to just figure out how this thing moves and how this thing operates.
[1348.38 → 1349.52] Because it's not just you.
[1349.62 → 1349.82] It's a
[1349.90 → 1350.10] we,
[1350.56 → 1351.60] so what I want to figure out the
[1351.68 → 1351.90] we,
[1352.28 → 1353.22] and I also want to figure out,
[1353.30 → 1353.64] you know,
[1353.68 → 1356.34] if you bankrolled it and then now it's free for all,
[1356.40 → 1358.02] like how in general,
[1358.02 → 1359.10] uh,
[1359.44 → 1361.98] I guess the bootstrapping process was,
[1361.98 → 1363.60] and then obviously it's,
[1363.66 → 1365.30] it's free for all now,
[1365.32 → 1366.88] but you have some ways you're making money.
[1366.88 → 1368.62] So over the course of our conversation,
[1368.62 → 1370.60] I'll let you pull some of that out as you,
[1370.68 → 1371.66] as you're able to.
[1371.74 → 1373.28] So what do you think about the bootstrapping,
[1373.50 → 1374.62] bootstrapping process of,
[1374.72 → 1375.94] of this thing?
[1376.82 → 1376.92] Sure.
[1377.08 → 1377.36] So,
[1377.36 → 1378.04] I mean,
[1378.04 → 1379.52] like bootstrapping is a term,
[1379.52 → 1383.96] like that is generally used with products to charge and free code camp will never charge.
[1384.76 → 1387.74] We're never going to charge campers to learn.
[1388.58 → 1390.18] We're never going to charge the nonprofits.
[1390.38 → 1390.72] We help.
[1390.82 → 1395.22] We're never going to sell your data to somebody so that we can make money.
[1395.22 → 1395.96] Uh,
[1396.02 → 1396.48] in fact,
[1396.48 → 1399.50] we give away basically all the anonymized data.
[1399.58 → 1400.22] It's not even,
[1400.32 → 1401.48] it's only semi-anonymized,
[1401.54 → 1402.20] but basically,
[1402.20 → 1402.90] uh,
[1402.90 → 1403.46] you can,
[1403.58 → 1404.94] you can opt out of that if you want,
[1405.10 → 1407.26] but we're not going to give away like your email address,
[1407.30 → 1407.78] for example.
[1408.40 → 1408.82] Um,
[1408.96 → 1413.42] but basically we have almost no income.
[1413.42 → 1415.82] Almost all the income right now comes through,
[1415.82 → 1416.20] uh,
[1416.20 → 1416.54] merchandise.
[1416.86 → 1417.06] We,
[1417.14 → 1418.04] we sell t-shirts.
[1418.30 → 1421.04] Occasionally we'll have like a tee spring campaign and,
[1421.14 → 1421.46] uh,
[1421.46 → 1425.94] we're getting ready to start selling some stickers and some other cool stuff through our shop.
[1426.06 → 1427.22] We don't accept donations.
[1427.70 → 1428.06] Um,
[1428.08 → 1428.94] we don't accept,
[1428.94 → 1430.34] like I've turned down funding.
[1431.22 → 1431.66] Um,
[1431.96 → 1432.22] wow.
[1432.36 → 1432.54] I,
[1432.64 → 1434.06] I think that my,
[1434.14 → 1434.34] my,
[1434.44 → 1439.04] my goal with free code camp is free code camp as independent as possible.
[1439.80 → 1440.24] And,
[1440.24 → 1440.62] uh,
[1440.80 → 1441.02] to,
[1441.12 → 1443.16] to retain as much control as possible,
[1443.16 → 1447.02] because I see free code camp is something that could easily be screwed up.
[1447.02 → 1448.66] If we brought in like a lot of,
[1449.24 → 1449.62] uh,
[1450.34 → 1450.94] a lot of,
[1450.96 → 1451.14] uh,
[1451.14 → 1455.38] corporate interests or like angel VC funding people.
[1455.84 → 1455.98] Um,
[1456.20 → 1457.16] we just had a show on that.
[1457.16 → 1457.40] Actually.
[1457.42 → 1458.54] I don't know if you listened to that one with,
[1458.54 → 1458.86] uh,
[1458.92 → 1459.52] Nadia Equal,
[1459.70 → 1460.02] uh,
[1460.06 → 1460.20] one,
[1460.32 → 1460.60] three.
[1460.76 → 1464.22] And so obviously you can kind of see where I'm coming from or where job not coming
[1464.22 → 1465.22] from this because we're,
[1465.30 → 1466.46] we're at this,
[1466.76 → 1469.80] there's a lot of altruistic goals and ideas out there.
[1469.80 → 1471.52] And I'm not saying one little bit,
[1471.52 → 1472.90] just trying to do some digging,
[1473.08 → 1474.44] investigating with you out loud.
[1475.06 → 1475.42] And,
[1475.62 → 1476.22] uh,
[1476.22 → 1477.84] we've got to go to a break here in just a second,
[1477.84 → 1480.76] but I think what I'm trying to figure out is,
[1480.76 → 1481.38] is,
[1481.50 → 1481.68] uh,
[1481.70 → 1482.12] one,
[1482.26 → 1482.48] you know,
[1482.50 → 1485.16] you spent some money doing this, and then it's not just you,
[1485.22 → 1485.70] it's we,
[1486.32 → 1486.72] um,
[1486.76 → 1488.24] we haven't shared some of your personal life,
[1488.26 → 1489.32] but you've got a family,
[1489.38 → 1490.30] you've got things like that.
[1490.30 → 1491.34] So I think,
[1491.34 → 1491.96] you know,
[1491.96 → 1494.34] we're always looking for the sustainability side of,
[1494.34 → 1496.28] of ideas like this.
[1496.46 → 1497.30] Cause one,
[1497.36 → 1498.58] you built something really awesome to,
[1498.64 → 1500.00] it's super popular three.
[1500.10 → 1500.72] It's helping people.
[1500.72 → 1502.34] I see you tweeting, and I see people saying,
[1502.44 → 1503.02] you know,
[1503.02 → 1503.70] in 20 hours,
[1503.70 → 1504.68] I learned some stuff and boom,
[1504.72 → 1505.68] I built this calculator.
[1505.68 → 1507.36] I built this thing with node or whatever.
[1507.56 → 1509.44] So obviously there are results.
[1510.02 → 1510.46] Uh,
[1510.46 → 1511.78] and I'm just kind of figuring out how,
[1512.12 → 1512.40] you know,
[1512.40 → 1513.46] how we keep it moving,
[1513.72 → 1514.36] how you're,
[1514.40 → 1515.40] how you're funded,
[1515.50 → 1516.76] how you keep funding,
[1516.82 → 1517.66] how you keep people,
[1517.66 → 1518.38] uh,
[1518.38 → 1518.84] motivated,
[1519.02 → 1519.34] invested,
[1519.46 → 1519.76] whatever.
[1519.76 → 1522.04] So hopefully you're taking us on that,
[1522.04 → 1522.58] on that journey,
[1522.64 → 1523.38] but let's,
[1523.50 → 1524.60] let's pause there since we're,
[1524.68 → 1526.56] we're sort of at a pause moment here.
[1527.04 → 1527.34] Uh,
[1527.34 → 1528.26] we'll take this quick break.
[1528.26 → 1531.44] We'll come back, and we'll dive a bit deeper on those topics.
[1531.44 → 1532.32] So right back.
[1533.50 → 1536.82] Digital ocean is simple cloud hosting built for developers.
[1536.82 → 1542.16] If you have not tried digital ocean yet in 55 seconds,
[1542.16 → 1548.42] you can have a blazing fast SSD cloud server up and running with your choice of Linux distro,
[1548.92 → 1549.34] CPU,
[1549.72 → 1550.02] Ram,
[1550.10 → 1554.28] and even create new droplets based on backups or snapshots in time,
[1554.34 → 1557.18] which is a cool feature for those that operate in teams.
[1557.18 → 1565.96] You can invite multiple users to access and manage your accounts' infrastructure resources while keeping all of your sensitive information totally private.
[1566.16 → 1573.26] Head to digital ocean.com and make sure you use our code change law to get a $10 credit when you create a new account.
[1575.76 → 1576.20] All right,
[1576.20 → 1577.16] we're back from the break.
[1577.20 → 1579.80] We're here with Quincy Larson talking about free code camp.
[1580.36 → 1580.38] And,
[1580.38 → 1580.66] uh,
[1580.94 → 1581.08] Jared,
[1581.14 → 1581.58] during the break,
[1581.60 → 1583.94] we kind of talked a little bit to kind of realign some,
[1584.08 → 1584.74] some thoughts here.
[1584.84 → 1585.98] And you brought up something,
[1586.12 → 1586.30] Jared,
[1586.30 → 1587.72] and people may not know this about you,
[1587.80 → 1588.26] but you're,
[1588.26 → 1588.96] uh,
[1588.96 → 1591.20] part of interface school there in Omaha,
[1591.30 → 1591.72] Nebraska.
[1592.16 → 1594.52] And we kind of just talked about how it's a capitalistic,
[1594.52 → 1595.04] uh,
[1595.04 → 1595.88] endeavour and that,
[1595.88 → 1596.60] you know,
[1596.94 → 1597.68] people are,
[1598.00 → 1598.36] you know,
[1598.86 → 1601.64] they're getting value from the teaching that goes on at this coding school.
[1601.74 → 1604.20] And the same Quincy with what he's doing,
[1604.20 → 1604.90] uh,
[1604.90 → 1606.78] with this and those who have joined the
[1606.84 → 1607.16] the
[1607.26 → 1608.64] the efforts with the rest of the campers,
[1608.64 → 1609.16] so to speak.
[1609.54 → 1610.24] And Quincy,
[1610.24 → 1612.42] I think what we're trying to do really is just figure out,
[1612.42 → 1613.16] uh,
[1613.16 → 1615.34] for the listener's sake and everyone who wants to invest,
[1615.34 → 1622.92] whether it's getting involved in learning or pitching in on becoming a teacher or just becoming a camper and whatever that entails,
[1622.92 → 1623.98] you know,
[1623.98 → 1625.16] from a revenue perspective,
[1625.16 → 1625.80] from a
[1625.80 → 1626.48] uh,
[1626.48 → 1627.38] bootstrapping perspective,
[1627.38 → 1629.10] you mentioned its kind of focused on products,
[1629.10 → 1629.42] but,
[1629.42 → 1630.32] uh,
[1630.32 → 1630.70] you know,
[1630.74 → 1632.42] what kind of endeavour is this for you?
[1632.48 → 1636.08] Is this a capitalistic endeavour or is this a give back to community endeavour?
[1636.22 → 1639.62] How do you frame sustainability when it comes to this project?
[1640.62 → 1640.76] Sure.
[1640.98 → 1641.48] First,
[1641.48 → 1642.72] this is an endeavour of,
[1643.10 → 1643.46] you know,
[1643.52 → 1653.20] this is an idealistic venture in the sense that my goal is to remake the world more in the likeness of how I think it should be,
[1653.20 → 1654.62] uh,
[1654.62 → 1658.88] which is obviously something that has to be funded somehow,
[1658.88 → 1664.14] but it's important to note that I am not interested in getting rich.
[1664.14 → 1670.50] I'm happy to spend the rest of my days sitting in my closet where I am now eating microwave burritos and,
[1670.50 → 1670.72] uh,
[1670.72 → 1673.50] coding all day and going for runs around the Bay Area.
[1673.50 → 1674.64] Um,
[1675.82 → 1676.82] what I think,
[1676.96 → 1686.96] I think that free code camp can absolutely fund itself through helping campers find jobs after they finish free code camp.
[1687.06 → 1687.98] So far,
[1688.22 → 1694.48] maybe several hundred campers have found jobs after they've worked through free code camps curriculum.
[1695.24 → 1695.54] And,
[1695.60 → 1695.92] uh,
[1696.58 → 1698.82] we're not doing anything to capture that value.
[1698.96 → 1699.30] Basically,
[1699.30 → 1701.86] they're just going and getting the jobs on their own.
[1701.86 → 1704.26] There are a lot of ways that we could potentially,
[1704.26 → 1705.36] um,
[1705.96 → 1707.28] become kind of a
[1707.34 → 1707.72] uh,
[1708.38 → 1709.48] an intermediary.
[1709.88 → 1726.26] And one of them is through our job board that we've already built that basically our job board is special in that it is for campers and for employers who specifically want to hire campers who've completed some of our certifications.
[1726.26 → 1730.66] And that's a very hands-off kind of,
[1730.66 → 1731.38] uh,
[1731.52 → 1745.12] laissez-faire approach to matchmaking campers with employers that will work really well in the long term when we have a high volume of campers completing those certifications.
[1745.12 → 1745.36] Now,
[1745.36 → 1751.38] right now we only have less than a thousand people who've completed a certification out of the
[1751.38 → 1751.78] I think,
[1751.92 → 1752.24] uh,
[1752.24 → 1753.52] 225,000,
[1753.52 → 1754.34] uh,
[1754.34 → 1758.22] campers that have registered at all on free code camp so far.
[1758.22 → 1758.54] Yeah,
[1758.54 → 1763.80] we saw 222,000 campers, and it sounds like you said a thousand have completed a certification.
[1763.94 → 1764.62] That's not challenges.
[1764.76 → 1765.52] That's just certification.
[1766.24 → 1766.96] That's a certification.
[1766.96 → 1770.04] So it's approximately 400 hours of,
[1770.04 → 1770.50] uh,
[1770.86 → 1771.40] coursework.
[1771.40 → 1777.30] So a lot of it is all this stuff is so new that people just haven't had time to work through it.
[1777.52 → 1778.12] But we,
[1778.12 → 1783.32] we think that people will have time as free code camp continues.
[1784.14 → 1784.58] Um,
[1784.62 → 1787.42] it's just so far free code camp is very,
[1787.54 → 1789.34] very new in the big scheme of things.
[1789.48 → 1789.50] Yeah.
[1789.58 → 1789.94] I mean,
[1790.58 → 1790.92] like I,
[1790.96 → 1791.44] like we said,
[1791.54 → 1791.78] you know,
[1791.78 → 1792.70] in the early person of the call,
[1792.78 → 1795.50] it's been on our radar because it's been training on GitHub.
[1795.64 → 1796.86] It's getting started like crazy.
[1797.52 → 1797.80] Um,
[1797.80 → 1798.50] obviously it's,
[1798.56 → 1801.08] it's doing something that's getting the attention.
[1801.08 → 1802.10] of the masses,
[1802.26 → 1806.22] those who are on GitHub and forking projects and contributing back.
[1806.42 → 1809.20] The number does seem a little skewed to me with,
[1809.20 → 1809.90] you know,
[1810.06 → 1812.82] quarter million campers and a thousand certifications.
[1813.30 → 1815.72] And obviously you're still sort of figuring things out.
[1815.76 → 1816.72] How do you feel about,
[1816.72 → 1817.68] uh,
[1817.78 → 1818.06] you know,
[1818.08 → 1818.70] that number,
[1818.82 → 1819.82] that skew basically,
[1819.88 → 1820.16] or that,
[1820.16 → 1820.34] that,
[1820.48 → 1821.12] that ratio.
[1821.74 → 1822.14] Uh,
[1822.18 → 1822.64] and what,
[1822.98 → 1823.36] I guess,
[1823.40 → 1826.18] given the fact that you're still new and still figuring things out,
[1826.18 → 1828.98] what are you doing to sort of match those numbers to,
[1829.06 → 1830.16] to higher ratios?
[1831.14 → 1831.54] Sure.
[1831.68 → 1831.88] Well,
[1831.98 → 1834.32] we're comfortable with a relatively low ratio.
[1834.94 → 1835.34] Um,
[1835.58 → 1836.02] you know,
[1836.10 → 1836.82] Daphne Collar,
[1836.92 → 1837.80] who founded Coursera,
[1838.10 → 1838.94] uh,
[1838.98 → 1839.20] is,
[1839.28 → 1840.24] you know,
[1840.28 → 1841.98] fond of answering the question of like,
[1842.16 → 1842.50] uh,
[1842.60 → 1842.96] you know,
[1843.04 → 1843.26] uh,
[1843.26 → 1844.28] attrition essentially,
[1844.48 → 1846.70] like attrition is a red herring.
[1846.76 → 1847.16] Right.
[1847.16 → 1847.82] Um,
[1847.82 → 1850.58] because these are people that wouldn't have learned any coding at all.
[1851.22 → 1851.62] And,
[1851.62 → 1852.62] uh,
[1852.62 → 1855.00] if they hadn't come to free code camp,
[1855.06 → 1855.74] they may have just,
[1855.84 → 1856.28] you know,
[1856.48 → 1856.76] said,
[1856.84 → 1857.06] well,
[1857.06 → 1859.76] I'm not going to bother learning, or maybe they'll,
[1859.88 → 1860.86] they'll come to free code camp.
[1860.92 → 1861.60] They'll use it for a while.
[1861.64 → 1862.70] They'll switch to another resource.
[1862.74 → 1863.44] They'll come back.
[1863.44 → 1863.88] We,
[1863.88 → 1865.08] we see that all the time,
[1865.08 → 1866.06] uh,
[1866.06 → 1867.32] because free code camp is hard.
[1867.32 → 1867.86] I mean,
[1867.86 → 1868.12] we,
[1868.20 → 1868.80] we definitely,
[1868.80 → 1869.80] we're not like the
[1869.80 → 1871.14] the weeder class,
[1871.56 → 1872.98] your first year of physics or whatever,
[1872.98 → 1875.14] but we are definitely,
[1875.14 → 1875.76] we,
[1875.84 → 1876.66] we make no,
[1876.66 → 1877.34] uh,
[1878.04 → 1881.04] pretenses about learning to code being an easy endeavour.
[1881.18 → 1881.28] No,
[1881.34 → 1882.68] it's a serious endeavour that,
[1882.84 → 1886.88] that takes a lot of commitment and a lot of effort on your part in time
[1886.88 → 1887.28] investment.
[1887.28 → 1889.08] And you have to allocate your time accordingly.
[1889.40 → 1890.10] I mean,
[1890.18 → 1890.50] uh,
[1890.78 → 1892.34] 2,080 hours.
[1892.34 → 1892.76] That's,
[1892.84 → 1894.38] that's really to get started.
[1894.38 → 1894.90] That's to,
[1894.98 → 1897.28] to be jobbed ready and really,
[1897.28 → 1900.98] just take the first step as a developer of actually getting a job and
[1900.98 → 1901.76] working for a while.
[1902.34 → 1902.70] Um,
[1902.88 → 1903.28] uh,
[1903.28 → 1904.32] Peter Norvig,
[1904.42 → 1905.10] uh,
[1905.10 → 1906.94] the director of,
[1907.08 → 1907.32] uh,
[1907.86 → 1908.34] Google's,
[1908.36 → 1909.04] I think research,
[1909.28 → 1909.80] uh,
[1910.02 → 1910.86] right now,
[1910.92 → 1911.82] I think is what he's doing.
[1912.18 → 1912.66] Um,
[1912.72 → 1913.16] he,
[1913.16 → 1914.06] uh,
[1914.28 → 1915.16] famously said,
[1915.38 → 1915.82] you know,
[1915.90 → 1917.62] learn to code in 10,000 hours.
[1918.40 → 1918.88] And,
[1919.02 → 1919.32] uh,
[1919.80 → 1923.00] he believes that learning to code is like a serious,
[1923.00 → 1924.28] um,
[1925.04 → 1927.18] input of time and energy is,
[1927.18 → 1927.48] it's,
[1927.68 → 1930.18] it's not something that you just trivially choose.
[1930.32 → 1930.84] And of course,
[1930.90 → 1933.38] a lot of people just want to try it out and see if it's for them.
[1934.00 → 1934.16] Uh,
[1934.20 → 1940.02] now I certainly believe everybody can learn to code if they persist in their effort.
[1940.92 → 1941.84] In practice,
[1941.84 → 1946.08] a lot of people are going to procrastinate, or they're going to,
[1946.08 → 1946.96] um,
[1946.96 → 1948.14] just decide that like,
[1948.14 → 1950.04] they don't want to worry about it right now.
[1950.04 → 1954.14] And invariably those people come back with several months later,
[1954.14 → 1955.96] they'll come back, and they'll start working on it again.
[1956.12 → 1957.80] So what we're experiencing is,
[1957.90 → 1958.62] you know,
[1958.62 → 1962.52] we have more than a hundred thousand people use free code camp every month.
[1962.98 → 1965.36] And a lot of times it's like,
[1965.36 → 1970.32] it's like they're strobing in and out of free code camp as their motivation waxes and wanes.
[1970.32 → 1971.80] And then at some point they'll,
[1971.88 → 1972.92] they'll lock in, and they'll be like,
[1972.96 → 1973.22] all right,
[1973.22 → 1974.24] I can really do this.
[1974.58 → 1974.88] They'll,
[1974.88 → 1977.16] they'll kind of clear the proverbial,
[1977.30 → 1977.82] um,
[1979.48 → 1980.18] the proverbial,
[1980.18 → 1980.62] uh,
[1980.62 → 1981.22] log jam.
[1981.54 → 1985.40] And they'll just keep jamming forward through the curriculum.
[1985.40 → 1985.84] And,
[1985.92 → 1990.14] and once they get that momentum, and they really start to believe that they can learn to code,
[1990.26 → 1992.30] that's when they start clearing these certifications.
[1992.30 → 1994.04] And that's when they go out and get jobs.
[1994.04 → 1995.02] Uh,
[1995.10 → 1995.26] but,
[1995.38 → 1995.72] but it,
[1995.98 → 1999.18] it's just an innately challenging process.
[1999.58 → 2001.74] So as Daphne Culler says,
[2001.86 → 2002.36] you know,
[2002.82 → 2004.34] when a MOOC has,
[2004.60 → 2004.92] you know,
[2004.96 → 2006.70] one or 2% completion rate,
[2006.82 → 2007.02] she,
[2007.16 → 2010.50] she's quick to point out that of the people who put forth a serious effort,
[2010.76 → 2012.32] it's much higher.
[2012.52 → 2018.92] It's like 60 or 70% of people who really do spend the time to complete the first or second week's assignment.
[2019.08 → 2023.54] Those people will go on to complete it at about the same rate that a university class will.
[2023.54 → 2025.18] And for us,
[2025.20 → 2026.72] I think it's probably very similar.
[2026.84 → 2026.96] Our,
[2026.98 → 2028.52] our numbers are very similar to that.
[2029.00 → 2032.88] It's just that we're so new that it's not reflected directly in,
[2033.02 → 2033.32] um,
[2033.32 → 2034.14] our outcomes yet.
[2034.88 → 2036.26] So if we could just back up a little,
[2036.32 → 2037.20] or maybe not back up,
[2037.24 → 2039.86] but zoom out a little bit and talk philosophically a little bit.
[2040.38 → 2040.86] Um,
[2040.98 → 2041.64] as Adam said,
[2041.70 → 2041.98] I've,
[2042.04 → 2042.46] you know,
[2042.46 → 2043.82] I'm co-founder of a
[2043.94 → 2045.42] of a web school here in Omaha.
[2045.92 → 2046.36] So,
[2046.88 → 2047.22] uh,
[2047.22 → 2050.60] definitely seen the need and kind of taking a hybrid approach,
[2050.74 → 2051.00] both,
[2051.12 → 2051.50] you know,
[2051.88 → 2052.54] IRL plus,
[2052.54 → 2055.30] plus adjunct of online tools,
[2055.30 → 2056.28] um,
[2056.74 → 2057.50] as a strategy,
[2057.60 → 2057.76] you know,
[2057.76 → 2058.92] teaching 10 people at a time,
[2058.96 → 2059.74] not going for the
[2059.90 → 2060.74] for the massive numbers.
[2060.90 → 2061.04] But,
[2061.50 → 2061.84] um,
[2061.92 → 2063.18] we profile our students,
[2063.22 → 2064.38] like our potential students.
[2064.38 → 2069.14] And one thing that we look for in a potential student is exactly what you said you had,
[2069.20 → 2072.66] which is why you made it through the slog of learning,
[2072.66 → 2074.02] which is that perseverance,
[2074.40 → 2074.50] you know,
[2074.54 → 2075.30] hardheadedness,
[2075.30 → 2076.30] um,
[2076.38 → 2078.90] that like some sort of intrinsic self motivation.
[2079.46 → 2079.98] And,
[2080.24 → 2080.84] um,
[2081.28 → 2081.50] you know,
[2081.50 → 2084.20] most people that I've had experience with,
[2084.20 → 2085.76] with online only,
[2085.76 → 2086.44] uh,
[2086.44 → 2089.14] self learning is that problem that you,
[2089.36 → 2090.58] you've kind of been touching on,
[2090.58 → 2093.80] which is the waxing and waning of interest or,
[2093.80 → 2094.60] uh,
[2095.04 → 2097.04] not able to get through that log jam.
[2097.22 → 2097.88] And so,
[2098.48 → 2098.86] um,
[2099.54 → 2100.46] it seems like,
[2100.46 → 2101.62] and in my experience,
[2102.04 → 2103.02] having somebody,
[2103.02 → 2103.92] uh,
[2103.92 → 2106.14] a real life instructor or a mentor,
[2106.14 → 2106.80] or,
[2106.96 → 2108.40] or I guess maybe in your guy's case,
[2108.48 → 2109.00] a pair,
[2109.50 → 2110.00] um,
[2110.18 → 2114.60] is a good way to get more people through that log jam and move,
[2114.66 → 2114.92] you know,
[2115.20 → 2116.96] beyond the ones who are going to be,
[2116.96 → 2117.64] you know,
[2117.64 → 2121.40] the Quincy Larson's of the world who are just going to teach themselves no matter what,
[2121.44 → 2121.70] you know,
[2121.76 → 2124.46] come hell or high water and get more people through,
[2124.46 → 2125.62] through the course,
[2125.70 → 2125.92] you know,
[2125.92 → 2126.64] to success.
[2127.44 → 2127.80] Um,
[2128.24 → 2130.00] is that something that you guys are thinking about how,
[2130.12 → 2130.60] I know you said,
[2130.66 → 2133.72] you mentioned you have these camp outs or these coffee and codes.
[2134.44 → 2134.76] Um,
[2134.76 → 2137.34] is there any sort of angle of taking the
[2137.40 → 2137.86] the tech,
[2137.94 → 2138.14] you know,
[2138.16 → 2138.86] you guys have the
[2138.86 → 2140.90] the broad swath approach of like,
[2140.94 → 2141.46] let's get it,
[2141.88 → 2143.82] let's get the curriculum online for everybody.
[2144.46 → 2144.86] Um,
[2144.86 → 2145.58] and then a lot of,
[2145.64 → 2147.64] a lot of the code schools are taking the other approach of like,
[2147.66 → 2149.38] let's get it in real life for a few people.
[2150.32 → 2150.68] And,
[2150.68 → 2151.52] um,
[2151.52 → 2153.48] it seems like if you can meet in the middle and say,
[2153.54 → 2153.64] well,
[2153.64 → 2156.48] we can take this online thing where we're having,
[2156.48 → 2156.96] you know,
[2156.96 → 2158.22] less than 1% at this point,
[2158.22 → 2160.62] I understand your point with its kind of new.
[2160.62 → 2163.32] So it takes time to get people through the certification,
[2163.32 → 2166.00] but let's just call it a 1% success rate.
[2166.54 → 2166.82] Um,
[2166.86 → 2168.22] if a certification is,
[2168.34 → 2168.70] you know,
[2168.72 → 2170.52] the definition of success and like,
[2170.58 → 2172.26] let's work on bolstering that with,
[2172.26 → 2172.96] you know,
[2172.98 → 2176.94] real other people to come alongside and get people to the log jam.
[2177.84 → 2178.32] Sure.
[2178.54 → 2178.74] I,
[2178.84 → 2179.96] I'll tell you,
[2179.96 → 2180.54] um,
[2181.28 → 2183.76] I strongly believe that in-person,
[2183.76 → 2184.76] um,
[2185.02 → 2188.76] learning is critical to establishing that motivation.
[2188.76 → 2189.60] I was talking about earlier,
[2189.60 → 2189.92] because,
[2190.14 → 2190.92] um,
[2190.92 → 2192.48] if you're literally alone,
[2192.48 → 2192.92] uh,
[2193.54 → 2194.36] in your closet,
[2194.36 → 2195.34] like I am right now,
[2195.40 → 2197.26] it can be very isolating.
[2197.26 → 2197.70] However,
[2198.28 → 2198.74] uh,
[2199.34 → 2199.62] you know,
[2199.68 → 2199.80] we,
[2199.84 → 2201.46] we have the online community component,
[2201.46 → 2202.54] but that's just a part of it.
[2202.60 → 2204.68] We have the in-person coffee and codes.
[2205.08 → 2205.52] Um,
[2205.52 → 2205.84] that's,
[2205.92 → 2206.94] that's a big part of it too,
[2206.94 → 2214.04] but we actively encourage our campers to go and participate in as many hackathons as they can to,
[2214.12 → 2214.32] uh,
[2214.32 → 2215.20] to go to tech talks,
[2215.24 → 2218.10] to go to conferences if they feel so motivated to,
[2218.20 → 2219.46] to enrol in an intensive,
[2219.46 → 2220.60] uh,
[2221.00 → 2222.92] coding bootcamp or other,
[2222.92 → 2223.42] um,
[2223.42 → 2224.24] short-term program.
[2224.74 → 2225.14] Uh,
[2225.16 → 2225.34] and,
[2225.44 → 2227.40] and I see tremendous value in those.
[2227.46 → 2227.76] Um,
[2227.76 → 2229.16] a lot of coding schools are,
[2229.16 → 2231.82] are adopting free code camp as part of their,
[2231.82 → 2232.78] uh,
[2232.78 → 2235.06] their pre-course work or even part of their core curriculum.
[2235.42 → 2235.80] Yeah.
[2235.80 → 2236.08] And,
[2236.32 → 2236.64] um,
[2236.64 → 2236.92] we,
[2236.98 → 2237.78] we definitely,
[2238.12 → 2243.48] I just want to say that we support what they're doing, and we think that,
[2243.48 → 2243.90] um,
[2244.26 → 2247.06] there should be a wide variety of modalities for learning to code.
[2247.60 → 2248.02] Um,
[2248.32 → 2253.04] there are certain people for whom attending one of those programs is simply not plausible.
[2253.36 → 2254.62] Maybe they have a lot of kids,
[2254.62 → 2255.58] um,
[2255.58 → 2258.22] and they've got a full-time job, and they simply can't,
[2258.22 → 2258.56] uh,
[2259.02 → 2261.70] do anything that's intensive at all.
[2261.76 → 2266.62] So what we're hoping free code camp can do is just give them a slow trickle over the course of years.
[2266.62 → 2267.62] Um,
[2267.62 → 2268.40] because,
[2268.40 → 2268.62] um,
[2268.62 → 2269.44] I mean,
[2269.44 → 2270.86] if you're only doing it two hours a day,
[2270.86 → 2275.72] it probably is going to take you years to get good enough to be able to transition your career.
[2275.72 → 2276.20] Yeah.
[2276.20 → 2278.72] You may be able to transition within your company,
[2278.72 → 2280.22] which is what a lot of our campers do.
[2280.28 → 2280.46] They'll,
[2280.52 → 2284.28] they'll apply for slightly more technical positions within their current company.
[2284.28 → 2285.04] And,
[2285.04 → 2286.52] and that's been like kind of,
[2286.52 → 2290.70] a path to success because they get more practical experience, and they can keep their,
[2290.70 → 2292.62] their income stream and all that.
[2293.12 → 2293.52] Um,
[2293.68 → 2294.90] but yeah,
[2294.90 → 2297.46] I think that in-person activities is,
[2297.54 → 2302.36] is critical to maintaining motivation and to contextualizing a lot of the lessons.
[2302.36 → 2302.62] I mean,
[2302.62 → 2305.34] if you see somebody stand in front of the whiteboard and diagram out,
[2305.50 → 2306.14] you know,
[2306.14 → 2309.26] a design pattern or how a schema actually looks,
[2309.26 → 2309.58] it's,
[2309.58 → 2309.60] it's,
[2309.60 → 2313.48] it's no longer so abstract, and you can kind of internalize it and,
[2313.52 → 2317.68] and suddenly it becomes part of your gestalt of how,
[2317.80 → 2318.04] right.
[2318.46 → 2320.56] Works or how this different technology works.
[2321.22 → 2322.76] The other huge aspect of it,
[2322.78 → 2328.80] which I've seen firsthand is all of those speed bumps that you hit that are actually just barriers.
[2328.90 → 2330.12] You were called on dependencies earlier.
[2330.12 → 2332.28] Like you got the wrong version of Python or,
[2332.42 → 2332.98] you know,
[2332.98 → 2334.20] you're typing this command wrong.
[2334.36 → 2335.40] Some of those things are,
[2335.48 → 2335.62] it's like,
[2335.70 → 2338.64] it's useful to get through that on your own because it's that,
[2338.98 → 2339.32] again,
[2339.42 → 2339.70] you've,
[2339.70 → 2340.48] you've proven to yourself,
[2340.60 → 2344.00] I can solve this problem, or I can get over the speed bump.
[2344.10 → 2348.60] But a lot of those are just gigantic wastes of time, and you're not actually learning,
[2348.76 → 2348.94] right?
[2348.96 → 2350.74] You're just banging your head against a wall.
[2351.24 → 2351.64] And,
[2351.74 → 2352.28] uh,
[2352.28 → 2355.06] if you only have two hours a day to do this,
[2355.08 → 2355.54] you're investing,
[2355.80 → 2355.96] you know,
[2355.96 → 2359.80] I'm going to invest two hours a day, and you spend that entire time hitting these,
[2359.80 → 2363.62] these dependencies or whatever the problem happens to be and not learning,
[2364.02 → 2368.72] having somebody who can in a moment move that thing out of your way, and you can just continue
[2368.72 → 2371.28] on your learning path is hugely valuable.
[2372.28 → 2372.36] Yeah,
[2372.42 → 2372.76] I agree.
[2372.92 → 2377.64] And I would say that that's one of the major reasons that free code camp exists is to
[2377.64 → 2382.50] give you like a clear path forward so that you can spend less time,
[2382.50 → 2383.10] uh,
[2383.10 → 2383.86] out in the sticks,
[2383.86 → 2384.62] so to speak,
[2384.72 → 2386.24] going down rabbit holes and,
[2386.30 → 2387.12] and,
[2387.18 → 2387.46] uh,
[2387.56 → 2387.82] you know,
[2387.88 → 2388.78] fixing things that,
[2388.96 → 2389.42] that are not,
[2389.42 → 2391.32] like a lot of people get caught up in,
[2391.32 → 2393.98] in deploying servers and doing all this like,
[2394.04 → 2394.30] uh,
[2394.62 → 2397.08] ops or DevOps type stuff early on.
[2397.08 → 2397.32] And,
[2397.62 → 2400.04] and it feels like you're being productive because you're following this tutorial,
[2400.14 → 2400.86] you're getting a server up,
[2400.88 → 2401.94] but you're not actually coding.
[2402.24 → 2402.68] Right.
[2402.74 → 2406.68] And if you think about like becoming a software developer,
[2406.68 → 2407.78] what is the biggest,
[2407.96 → 2408.86] you know,
[2409.12 → 2413.10] the biggest aspect of that career,
[2413.10 → 2413.94] it's coding.
[2413.94 → 2415.92] And I think that,
[2415.92 → 2416.60] uh,
[2416.60 → 2420.92] people should spend as much time coding as possible and as little time worrying about,
[2420.92 → 2421.20] you know,
[2421.26 → 2424.56] configuring their flavour of VIM shortcuts or whatever,
[2424.56 → 2425.66] uh,
[2425.66 → 2429.74] or whatever ancillary stuff that can seem like it's a productive,
[2430.10 → 2431.10] relevant use of your time,
[2431.10 → 2436.36] but in fact is not an optimal amount or an optimal application of your time,
[2436.42 → 2441.52] considering that you need to get thousands of hours of coding under your belt before you're really going to be very good.
[2441.52 → 2442.74] Maybe,
[2442.74 → 2443.20] um,
[2443.74 → 2451.62] maybe to help us guide this call a bit would be to help us understand what your version of success for this would be.
[2451.70 → 2453.34] Maybe not right now,
[2453.34 → 2455.28] but where do you hope to go?
[2455.36 → 2455.56] What,
[2455.92 → 2457.72] what are some of the milestones,
[2458.16 → 2459.24] success goals that you,
[2459.68 → 2460.48] maybe not numbers,
[2460.58 → 2461.14] but just,
[2461.14 → 2462.40] you know,
[2462.52 → 2463.62] aspirational ideas.
[2463.74 → 2466.52] What do you think success for this is?
[2466.52 → 2473.20] Is success for free code camp would be helping a lot of people in aggregate,
[2473.30 → 2475.66] not necessarily a high percentage of applicants,
[2475.82 → 2482.92] but a lot of people in aggregate be able to transition from whatever they're doing right now to working as software engineers.
[2482.92 → 2484.18] And,
[2484.22 → 2484.90] um,
[2485.34 → 2486.90] in terms of the goal,
[2487.16 → 2488.46] the scope of free code camp,
[2488.82 → 2489.26] you know,
[2489.30 → 2497.74] this isn't some project that I'm going to get bored with and move on and go start building different JavaScript libraries or something like that.
[2497.86 → 2499.96] This is where I literally see my career.
[2500.06 → 2502.00] Like I'm hoping that 50 years from now,
[2502.06 → 2503.58] free code camp is still going strong.
[2503.58 → 2505.34] I would like my,
[2505.64 → 2507.36] one of my personal heroes is Jimmy Wales,
[2507.60 → 2508.40] um,
[2508.44 → 2512.88] who founded Wikipedia and really got the critical mass necessary to,
[2513.00 → 2517.00] to sustain that and make this incredible resource that if you,
[2517.10 → 2521.60] if you look at the total amount of time that went into building Wikipedia,
[2521.60 → 2522.28] I mean,
[2522.28 → 2525.24] it's the equivalent of building the Egyptian pyramid several times over.
[2525.46 → 2526.66] And it's all,
[2527.00 → 2531.34] it's all because he just planted the seed and,
[2531.34 → 2531.68] and,
[2531.68 → 2533.36] and kind of nurtured it early on.
[2533.36 → 2535.50] And then got a bunch of other people to come over and contribute.
[2535.70 → 2538.12] And my hope is that with free code camp,
[2538.18 → 2539.00] we can,
[2539.14 → 2540.80] we can get even more,
[2540.80 → 2541.20] uh,
[2541.20 → 2543.62] teachers and even more developers coming in to,
[2543.74 → 2547.90] to really build this amazing online resource so that anyone,
[2548.10 → 2553.40] anywhere in the world who has the motivation can sit down and learn to code in a very efficient,
[2553.68 → 2554.12] um,
[2554.24 → 2557.96] way that is free of a lot of the
[2558.04 → 2558.40] uh,
[2558.72 → 2559.96] issues associated with,
[2559.96 → 2560.36] you know,
[2560.42 → 2563.28] self-directed learning in general of not knowing exactly,
[2563.36 → 2566.62] what to do or having to deal with like,
[2566.62 → 2567.38] uh,
[2567.38 → 2570.32] resources that do not interoperate properly,
[2570.32 → 2571.38] um,
[2571.38 → 2572.14] because they're,
[2572.26 → 2575.64] they're dealing with different content or maybe excessive overlap between different resources.
[2575.64 → 2576.22] For example,
[2576.22 → 2579.92] there's this resource density of early content,
[2579.92 → 2580.50] uh,
[2580.50 → 2580.56] that,
[2580.56 → 2582.70] that teaches you the most fundamental aspects.
[2582.82 → 2586.24] And there's also this density of advanced tutorials,
[2586.24 → 2590.56] but there's very little in between that would help you bridge from one side to the other.
[2590.56 → 2598.08] So what we want to do is create a reliable bridge from the people who are stuck in kind of beginner resource mode,
[2598.08 → 2610.66] where they're jumping from tutorial to actually have something where they can hunker down for the long term and spend a lot of time and energy just learning all the intermediary aspects of coding.
[2610.66 → 2614.48] And then there'll be in the advanced state where they can rely on,
[2614.48 → 2614.66] uh,
[2615.40 → 2617.26] the gamut of tutorials and,
[2617.26 → 2619.60] and effectively use Google stack overflow,
[2619.74 → 2623.10] all these other tools to be able to accomplish whatever they need to accomplish.
[2623.46 → 2626.26] So that's what I see free code camp is like,
[2626.34 → 2630.76] ideally it's a bridge from a novice to a fairly advanced job ready,
[2630.76 → 2631.60] uh,
[2631.78 → 2636.50] coder that can be used by anybody anywhere in the world for free at their own,
[2636.50 → 2637.36] uh,
[2637.36 → 2638.18] at their own pace.
[2639.30 → 2641.32] So like any strong bridge out there,
[2641.32 → 2642.74] you've got a lot of support,
[2642.74 → 2643.22] right?
[2643.94 → 2645.56] Free code camp is not just you.
[2645.56 → 2646.50] It's not just Quincy.
[2646.72 → 2649.76] I'm sure you don't want it to be because that would be a lonely track.
[2650.44 → 2650.80] Um,
[2651.22 → 2654.58] help us understand because we really haven't talked about who else is involved.
[2654.70 → 2655.76] You mentioned teachers,
[2655.94 → 2656.72] you mentioned mentors,
[2656.82 → 2657.24] you mentioned,
[2657.24 → 2658.18] uh,
[2658.26 → 2659.32] in real life opportunities,
[2659.32 → 2659.98] you mentioned,
[2659.98 → 2661.02] um,
[2661.28 → 2662.02] pair programming,
[2662.38 → 2662.92] uh,
[2663.00 → 2663.34] curriculum.
[2663.46 → 2664.70] I'm sure there's somebody creating curriculum.
[2664.70 → 2668.22] So paint a picture for who's behind this.
[2668.64 → 2671.00] And I guess as a dovetail to that,
[2671.04 → 2671.42] after that,
[2671.44 → 2673.78] maybe if you can lead into some motivations,
[2673.78 → 2674.66] how you're motivating,
[2674.76 → 2678.76] what people are motivated by and how hard it might be to get them to buy into
[2678.76 → 2679.36] your dream.
[2680.82 → 2682.16] Free code camp is,
[2682.60 → 2682.94] uh,
[2683.04 → 2683.62] our core team,
[2683.68 → 2685.08] I think currently 17 people.
[2685.56 → 2686.00] Um,
[2686.00 → 2687.28] I can tell you some of the people on,
[2687.36 → 2688.34] on that core team,
[2688.44 → 2688.88] uh,
[2688.92 → 2689.52] name some people.
[2690.18 → 2692.06] So Michael Johnson in Washington,
[2692.18 → 2694.68] DC is in charge of our nonprofit project.
[2694.70 → 2698.08] And when we've broken everything out in terms of like product ownership and
[2698.08 → 2699.10] traditional agile,
[2699.10 → 2700.10] uh,
[2700.76 → 2701.20] practice.
[2701.20 → 2706.58] So Michael Johnson owns the nonprofit projects in terms of like coordinating
[2706.58 → 2707.70] our volunteer,
[2707.70 → 2708.20] uh,
[2709.26 → 2712.50] agile project managers who are working toward getting,
[2712.50 → 2712.88] uh,
[2712.88 → 2714.56] experience for their certifications.
[2714.56 → 2718.00] And he also goes out and identifies and,
[2718.00 → 2722.38] and vets all of these nonprofits that want different projects built.
[2722.96 → 2726.80] And then he actually oversees the entire process of pairing up two campers who
[2726.80 → 2727.70] completed our,
[2727.80 → 2728.02] you know,
[2728.08 → 2730.14] three outstanding certifications,
[2730.52 → 2730.80] uh,
[2730.80 → 2732.46] which is 1200 hours worth of work.
[2732.46 → 2737.04] And then like pairing them up and getting them on a team with the agile project manager
[2737.04 → 2738.32] and the
[2738.42 → 2738.90] um,
[2739.86 → 2742.76] in the nonprofit stakeholder to actually build the project.
[2742.76 → 2747.12] And we've repeated this process almost 20 times now done more than half a million
[2747.12 → 2749.00] dollars worth of pro bono coding for nonprofits.
[2749.26 → 2749.96] So he,
[2750.02 → 2750.82] he owns that.
[2751.28 → 2752.80] Berkeley Martinez owns,
[2752.80 → 2753.34] uh,
[2753.34 → 2754.48] our open source code base.
[2754.48 → 2758.34] And he is responsible for,
[2758.34 → 2759.18] uh,
[2759.18 → 2760.52] making sure that we have,
[2760.52 → 2760.78] you know,
[2760.88 → 2766.08] CI that runs and that we're using a style guide that's enforced by ESLint.
[2766.22 → 2768.00] We're using Airbnb's JavaScript style guide.
[2768.46 → 2769.04] Um,
[2769.20 → 2770.18] and that,
[2770.28 → 2770.52] uh,
[2770.52 → 2776.48] generally like stuff is not introduced that makes free code camp buggier or less
[2776.48 → 2776.90] secure.
[2777.26 → 2777.78] Uh,
[2777.78 → 2779.06] so he's kind of like the
[2779.06 → 2779.32] uh,
[2779.32 → 2781.38] the fun police in many ways on,
[2781.38 → 2781.62] uh,
[2781.62 → 2782.54] the free code camp repo.
[2783.90 → 2784.38] Um,
[2784.48 → 2785.62] Rex,
[2786.18 → 2787.10] um,
[2787.14 → 2788.40] is over in,
[2788.40 → 2789.18] uh,
[2789.36 → 2795.50] Sacramento area, and he's an electrical engineer who is also quite good at coding.
[2795.50 → 2797.84] And he's in charge of our JavaScript curriculum.
[2798.56 → 2799.12] Um,
[2799.82 → 2805.08] Brianna Swift is a K through 12 music teachers.
[2805.32 → 2808.20] Who's also quite good at coding and very good at teaching.
[2808.46 → 2810.48] And she's in charge of our video curriculum.
[2810.48 → 2814.40] So she stands in front of the whiteboard and records these two minute,
[2814.40 → 2820.80] videos that talk about everything from computer security to a big O notation and all these
[2820.80 → 2823.24] other concepts that are more theoretical rather than practical.
[2823.62 → 2824.78] So that she,
[2824.88 → 2826.54] she basically is the ownership.
[2826.54 → 2827.54] Um,
[2827.54 → 2831.38] she has ownership of the theory curriculum and Rex has ownership of the practical curriculum
[2831.38 → 2833.28] in terms of coding challenges.
[2833.92 → 2834.28] Um,
[2834.90 → 2835.94] then we have,
[2835.94 → 2836.26] uh,
[2836.26 → 2837.48] Justin Richardson,
[2837.48 → 2838.60] who's in Toronto,
[2838.60 → 2841.12] who's in charge of our campsites.
[2841.12 → 2842.38] And as I said,
[2842.38 → 2844.68] we have nearly a thousand of these campsites,
[2844.68 → 2847.06] each of which has its own Facebook group.
[2847.50 → 2847.94] Um,
[2847.94 → 2852.42] and basically we coordinate these coffee and code events and,
[2852.50 → 2852.78] uh,
[2853.50 → 2857.62] other events like people will go to hackathons together and things like that through these
[2857.62 → 2858.30] Facebook groups.
[2858.96 → 2859.42] Um,
[2859.42 → 2860.84] we have,
[2860.84 → 2861.16] uh,
[2861.16 → 2862.32] Nathan Lin is,
[2862.44 → 2864.82] who has built a lot of our ancillary tools.
[2865.42 → 2865.86] Um,
[2865.86 → 2866.70] he's a
[2866.78 → 2867.08] uh,
[2867.08 → 2868.02] he's in Washington.
[2868.58 → 2870.78] He's in the army bomb squad.
[2870.92 → 2872.50] He literally takes apart bombs all day.
[2872.66 → 2873.64] That's his day job.
[2873.64 → 2876.68] And then afterward he comes and pulls another shift,
[2876.68 → 2877.60] uh,
[2877.64 → 2878.04] doing,
[2878.04 → 2878.58] uh,
[2878.58 → 2878.88] you know,
[2878.94 → 2879.82] node development.
[2879.96 → 2880.28] Wow.
[2880.34 → 2881.02] For free code camp.
[2881.08 → 2881.64] Shipping bombs.
[2881.64 → 2885.32] And then we've got like a lot of other people.
[2885.38 → 2885.54] I mean,
[2885.54 → 2885.80] I could,
[2885.96 → 2886.84] I could go on.
[2887.16 → 2887.64] Uh,
[2887.64 → 2889.94] we have just a lot of issue moderators.
[2890.28 → 2890.72] Uh,
[2890.72 → 2892.82] we have moderators in our chat room.
[2893.02 → 2895.88] When you have thousands and thousands of people in your chat system,
[2895.88 → 2901.26] you do need to keep out the occasional teenager who decided to come in and harass people.
[2901.90 → 2902.26] Um,
[2902.38 → 2905.60] so we're very vigilant about that.
[2905.84 → 2906.16] Um,
[2906.66 → 2908.14] there are so many people involved.
[2908.24 → 2908.38] I,
[2908.38 → 2908.64] I,
[2908.72 → 2911.62] I feel embarrassed that I can't name them all right off the top of my head.
[2911.64 → 2912.32] But,
[2912.84 → 2913.28] um,
[2913.38 → 2917.08] I am extremely grateful for all of these people and,
[2917.22 → 2917.42] uh,
[2917.46 → 2920.82] they are doing 95,
[2921.10 → 2924.88] 99% of the work that is done on free code camp.
[2924.88 → 2925.12] And,
[2925.24 → 2926.54] and my percentage,
[2926.66 → 2932.80] my overall percentage of things that I do keeps decreasing because there are just so many more contributors coming in.
[2932.88 → 2935.80] We have almost 300 contributors on our open source repo.
[2936.64 → 2937.08] Um,
[2937.34 → 2940.72] and then we have just a ton of people that are going out and like,
[2940.82 → 2941.32] uh,
[2941.64 → 2946.24] evangelizing our campsites in various cities and,
[2946.24 → 2947.42] and getting people to,
[2947.56 → 2949.52] to come in and sit down and learn to code with them.
[2950.52 → 2950.84] Wow.
[2950.92 → 2951.42] That's a big,
[2951.54 → 2951.80] yeah,
[2951.84 → 2952.84] you got a lot going on there,
[2952.90 → 2953.12] Quincy.
[2953.20 → 2953.56] I think,
[2953.62 → 2953.98] uh,
[2954.32 → 2956.66] I think we do want to touch on like how you motivate all these people.
[2956.66 → 2957.10] A lot of,
[2957.10 → 2958.42] a lot of people in open source,
[2958.58 → 2959.18] you know,
[2959.18 → 2961.00] they want their project to get traction.
[2961.00 → 2961.50] You know,
[2961.54 → 2961.68] they,
[2961.78 → 2963.54] they have a great idea.
[2963.66 → 2969.34] They have some valuable software that they've written and maybe people aren't paying attention to it.
[2969.74 → 2970.14] Um,
[2970.14 → 2974.26] maybe they haven't been able to motivate others to help them with a PR or a bug request.
[2975.06 → 2978.10] And I think that's an insight that people like to have is when,
[2978.10 → 2978.28] when,
[2978.28 → 2980.20] when we see somebody who's been successful in,
[2980.28 → 2981.26] in two things,
[2981.26 → 2983.04] you brought a lot of users.
[2983.54 → 2983.90] Okay.
[2983.90 → 2986.36] I think some of that can be explained by your,
[2986.36 → 2986.86] uh,
[2986.92 → 2988.90] hardcore curriculum and the free aspect of it.
[2988.98 → 2993.96] You've also brought a lot of contributors as you just listed off a bunch of them and can't even remember them all.
[2994.12 → 2995.26] So we're going to take a break,
[2995.26 → 2996.26] but we really want to hear,
[2996.38 → 2996.96] uh,
[2996.96 → 2997.82] from both sides,
[2997.82 → 3001.54] how you motivate people to become a part of the community on the help outside,
[3001.64 → 3002.56] especially with your,
[3002.72 → 3003.30] uh,
[3003.34 → 3004.28] the freeness of everything.
[3004.28 → 3005.18] And then on the other side,
[3005.22 → 3008.14] some success stories of users that have used free code camp.
[3008.26 → 3011.26] And I'm sure these are some of the motivation as you see,
[3011.36 → 3011.82] you know,
[3011.82 → 3013.34] kind of transforming people's lives.
[3013.34 → 3014.80] So we'll take a break.
[3014.84 → 3016.96] We'll give you a second to think about a few of those things.
[3016.96 → 3017.74] And we'll be right back.
[3019.10 → 3022.12] I'm here with Thomas Watson of Upbeat.
[3022.24 → 3023.72] And as listeners of the show,
[3023.80 → 3028.46] you know that we love to turn things on their heads and that's no different from sponsorships.
[3028.46 → 3032.52] And one thing we're doing is we're going deeper into the organizations we work with.
[3032.98 → 3036.86] Upbeat is doing some fascinating things around application performance monitoring,
[3037.22 → 3038.50] specifically around Node.js.
[3038.80 → 3042.16] And Thomas has an interesting story on how he got started with Upbeat.
[3042.16 → 3044.74] and also starting off their Node support.
[3044.88 → 3045.16] So Thomas,
[3045.24 → 3045.60] say hello.
[3046.34 → 3046.72] Hey,
[3046.80 → 3047.32] hello everybody.
[3048.06 → 3048.40] Thomas,
[3049.02 → 3053.04] you got an interesting story here with how you came to be at Upbeat.
[3053.12 → 3056.64] It seems like the Node support is kind of in thanks to you.
[3056.70 → 3057.00] So what,
[3057.12 → 3058.34] what's the backstory on that?
[3058.34 → 3059.26] Yeah,
[3059.26 → 3065.10] so I've been doing Node.js for almost five years and I found Upbeat, and they were doing,
[3065.10 → 3071.14] they were doing application performance monitoring and I wanted to have that for my stuff that I was doing, and they didn't have Node support.
[3071.14 → 3073.60] So I basically approached them and said,
[3073.68 → 3073.76] Hey,
[3073.82 → 3076.20] can I do an unofficial Node.js implementation?
[3076.20 → 3078.48] And they were like,
[3078.54 → 3078.70] yeah,
[3078.78 → 3079.16] sure,
[3079.36 → 3080.08] we would love that.
[3080.24 → 3081.36] And I did that.
[3082.16 → 3086.62] And then slowly we started to work more and more together.
[3086.84 → 3091.20] And all of a sudden I find myself being employed now at Upbeat,
[3091.74 → 3092.38] being there,
[3092.50 → 3093.22] the Node.js lead.
[3093.22 → 3097.30] and I'm now responsible for this agent that I,
[3097.38 → 3099.60] that I started back in the days as an open source project.
[3099.60 → 3102.44] I'm now responsible for that at Upbeat.
[3102.62 → 3108.70] And that's the one you install on your production servers to monitor the health and performance of your application.
[3109.28 → 3109.72] And so that's,
[3109.90 → 3111.34] that module is Upbeat Node.
[3111.62 → 3114.18] And so things began with that open source repo.
[3114.32 → 3115.78] Is that how things began for you with this?
[3115.96 → 3116.20] Yeah,
[3116.38 → 3118.06] I started it under my,
[3118.14 → 3123.20] my own GitHub account and just did it for myself and my own project.
[3123.22 → 3127.30] And then people started using it and the Upbeat guys were really happy with it.
[3127.78 → 3130.14] And then when we decided to,
[3130.24 → 3130.76] to,
[3130.84 → 3131.80] to join forces,
[3132.06 → 3134.68] we moved it to the Upbeat org on GitHub.
[3135.08 → 3139.54] So now it's resides on GitHub.com slash Opbeat Node.
[3140.00 → 3141.32] That's fascinating to,
[3141.40 → 3142.14] to see like,
[3142.44 → 3143.50] because we'll get into this here in a second,
[3143.56 → 3145.36] but you have this passion for open source,
[3145.46 → 3146.62] but how,
[3146.90 → 3147.24] you know,
[3147.26 → 3151.54] your own personal drive and desire for something on a particular,
[3151.54 → 3152.68] you know,
[3152.68 → 3153.88] language platform like Node.
[3154.14 → 3158.68] And then a service like Upbeat to get that application performance monitoring into your own apps.
[3158.90 → 3159.42] You were like,
[3159.46 → 3159.54] Hey,
[3159.56 → 3160.12] you don't have it,
[3160.16 → 3161.30] but I can write this.
[3161.44 → 3161.46] And,
[3161.52 → 3163.70] and now you actually work there, and you're building it out.
[3164.02 → 3164.42] Yeah.
[3164.42 → 3165.38] That's the beauty of open source.
[3165.82 → 3166.18] It,
[3166.18 → 3166.20] it,
[3166.20 → 3167.72] it connects you with a lot of people and,
[3167.76 → 3169.56] and you can basically do what you want for yourself.
[3169.56 → 3171.44] And then if people like it,
[3171.44 → 3173.24] you see where it takes you.
[3173.24 → 3173.60] Uh,
[3173.60 → 3174.24] in this case is,
[3174.32 → 3175.70] it took me to this really awesome place.
[3175.76 → 3177.46] I'm doing this really awesome stuff with,
[3177.46 → 3177.94] with Node.
[3177.94 → 3179.42] That's really down in the
[3179.46 → 3180.36] in the machine room,
[3180.36 → 3181.12] so to speak.
[3181.52 → 3181.84] Uh,
[3181.84 → 3182.42] which is really,
[3182.52 → 3183.36] fascinating to,
[3183.50 → 3183.72] to,
[3183.72 → 3184.10] to do.
[3184.30 → 3185.12] And right now we actually,
[3185.12 → 3185.54] uh,
[3185.54 → 3186.06] we're just,
[3186.10 → 3186.24] uh,
[3186.24 → 3187.22] going out of beta soon.
[3187.44 → 3187.84] Uh,
[3187.84 → 3190.62] you can go to Opbeat.com slash Node.js and sign up for the beta.
[3191.02 → 3191.46] Uh,
[3191.46 → 3192.04] if you want to,
[3192.04 → 3192.18] uh,
[3192.18 → 3193.38] want to try out the stuff.
[3193.38 → 3196.14] So the Upbeat Node module,
[3196.14 → 3197.66] can you talk a bit about what it does?
[3198.18 → 3199.34] So basically sits on your,
[3199.42 → 3200.00] on your server,
[3200.00 → 3200.68] uh,
[3200.72 → 3201.62] inside your,
[3201.70 → 3202.50] your Node.js app.
[3202.60 → 3202.78] Uh,
[3202.78 → 3204.74] you require it at the top of your,
[3204.86 → 3207.66] your main program, and it just monitors the
[3207.66 → 3209.64] the overall health of your application,
[3209.64 → 3210.34] uh,
[3210.34 → 3211.48] on a request basis.
[3211.48 → 3213.68] So incoming HTTP requests to your,
[3213.68 → 3214.36] to your,
[3214.36 → 3215.14] to your Node server,
[3215.14 → 3215.64] uh,
[3215.64 → 3216.72] figures out what's slow,
[3216.86 → 3217.48] what's performing,
[3217.48 → 3218.04] uh,
[3218.04 → 3218.40] badly.
[3218.50 → 3218.64] What,
[3218.98 → 3219.16] uh,
[3219.16 → 3220.26] what should you take a look at,
[3220.26 → 3220.66] uh,
[3220.66 → 3221.22] to optimize?
[3221.34 → 3222.40] Maybe it's a database thing.
[3222.46 → 3223.34] Maybe it's a Reddish,
[3223.38 → 3223.80] a cache,
[3224.20 → 3224.64] uh,
[3224.66 → 3225.38] or something else.
[3225.38 → 3225.82] Uh,
[3225.82 → 3226.74] and it also monitors,
[3226.74 → 3227.52] uh,
[3227.60 → 3228.76] errors happening in production.
[3228.96 → 3229.32] So,
[3229.50 → 3229.78] uh,
[3229.78 → 3231.16] we will break down the error,
[3231.28 → 3233.30] figure out who made that code.
[3233.40 → 3234.24] When was it committed,
[3234.24 → 3235.32] uh,
[3235.40 → 3235.84] to get,
[3235.90 → 3237.20] when was it pushed to production?
[3237.52 → 3237.92] Uh,
[3237.92 → 3239.76] so we can order assign errors as well to,
[3239.88 → 3242.40] to the developers who actually is responsible for the
[3242.44 → 3243.38] for the code that is breaking.
[3243.78 → 3248.04] So obviously your passion for open source and your passion for giving back,
[3248.04 → 3249.26] um,
[3249.50 → 3249.72] you know,
[3249.78 → 3253.06] got you to doing some of this stuff with Upbeat and what we just described there with
[3253.06 → 3254.44] your node support and whatnot.
[3254.78 → 3255.94] Can you talk a bit about your,
[3256.14 → 3257.62] your work at node school,
[3257.84 → 3258.38] uh,
[3258.38 → 3259.30] the open source you've written,
[3259.38 → 3263.08] just some of your passions around open source and kind of how you think about open source?
[3263.08 → 3264.02] Yeah,
[3264.10 → 3265.00] I really love,
[3265.00 → 3265.20] uh,
[3265.20 → 3266.84] open source, and I've been a big open source,
[3266.84 → 3267.24] uh,
[3267.24 → 3269.34] software user for over 20 years.
[3269.52 → 3269.84] Um,
[3269.84 → 3274.74] so when I joined the Node.js community five years ago and finding such a big open source spirit,
[3274.90 → 3275.42] um,
[3275.80 → 3276.62] in the community,
[3276.62 → 3277.32] it was really exciting.
[3277.32 → 3281.04] So I've now gone from an open source user to an open source developer.
[3281.36 → 3282.12] I love to,
[3282.12 → 3282.28] to,
[3282.42 → 3282.96] to teach.
[3283.10 → 3284.46] That's one of my passions.
[3284.46 → 3285.16] And especially,
[3285.32 → 3285.52] of course,
[3285.54 → 3286.42] I love to teach programming.
[3286.76 → 3287.14] Um,
[3287.14 → 3289.28] so there's something called a node school where,
[3289.54 → 3292.46] where I try to help out as much as I can to teach,
[3292.46 → 3292.88] uh,
[3292.88 → 3293.92] other people Node.js.
[3294.24 → 3295.88] And you get to do that not only,
[3296.24 → 3296.52] you know,
[3296.52 → 3297.38] on the web,
[3297.42 → 3297.72] you know,
[3297.72 → 3298.46] kind of remotely,
[3298.58 → 3298.94] so to speak,
[3298.96 → 3300.76] but you also get to do it face to face.
[3301.18 → 3301.54] Yeah.
[3301.62 → 3301.82] It's,
[3301.82 → 3302.04] it's,
[3302.04 → 3302.42] you can,
[3302.42 → 3305.26] you can go into node school.io, and you can,
[3305.26 → 3306.56] you can take some courses online,
[3306.56 → 3308.90] but you can also join some of the
[3308.90 → 3311.02] the regional chapters, and you can meet up at a city.
[3311.32 → 3311.60] Uh,
[3311.62 → 3316.34] there'll be a node school event where we will have a tutor who can help you out with your,
[3316.34 → 3316.98] your node questions.
[3316.98 → 3319.50] And you can actually do some of these online courses.
[3319.50 → 3320.24] You can do them in,
[3320.28 → 3320.42] in,
[3320.42 → 3320.88] in person,
[3320.96 → 3322.82] in real life with people who,
[3322.96 → 3323.50] who,
[3323.56 → 3324.74] who know node really well.
[3324.84 → 3326.46] And I try to do that as much as I can.
[3326.50 → 3328.58] I'd be organizing one here in Copenhagen where I'm from.
[3328.82 → 3329.18] Well,
[3329.22 → 3329.34] cool.
[3329.34 → 3330.94] If you want to follow up with Thomas,
[3331.14 → 3334.38] you can check him out at GitHub.com slash Watson.
[3334.38 → 3335.26] That's his last name.
[3335.36 → 3337.46] W A T S O N.
[3337.54 → 3340.62] If you want to sign up for the op beat Node.js beta,
[3340.70 → 3343.48] you can do so at op beat.com slash Node.js.
[3344.06 → 3345.14] And now back to the show.
[3347.76 → 3348.24] All right.
[3348.26 → 3354.00] We are back with Quincy Larson talking about free code camp and the community that he's built around it.
[3354.06 → 3356.54] Community of contributors of users.
[3356.54 → 3360.16] I think you named 17 core contributors and,
[3360.26 → 3360.54] uh,
[3361.26 → 3361.56] many,
[3361.70 → 3362.14] many more.
[3362.74 → 3364.08] And before the break,
[3364.08 → 3367.12] we were wondering how you went about building this community.
[3367.20 → 3369.58] How do you motivate people when there's no,
[3369.58 → 3370.38] uh,
[3370.44 → 3372.04] promise of money,
[3372.04 → 3373.08] uh,
[3373.54 → 3377.16] to be so involved and give so much of their time to this awesome community?
[3377.16 → 3377.60] Um,
[3377.60 → 3383.56] it's really challenging initially to get people to care about you.
[3383.84 → 3384.06] You know,
[3384.22 → 3384.94] um,
[3385.60 → 3386.80] I really felt like,
[3386.98 → 3391.08] like for the first month after I'd put together the Node.js prototype and,
[3391.08 → 3392.56] and thrown it online.
[3392.56 → 3393.10] And,
[3393.22 → 3393.46] uh,
[3393.60 → 3393.96] like we,
[3394.02 → 3395.54] we immediately created a chat room,
[3395.64 → 3397.90] which I think in retrospect was very wise.
[3398.14 → 3398.58] Um,
[3398.58 → 3401.36] I didn't attempt to create all the resources myself.
[3401.46 → 3401.72] Initially,
[3401.72 → 3402.86] we were using a lot of,
[3402.86 → 3403.06] uh,
[3403.06 → 3403.26] you know,
[3403.26 → 3404.18] Stanford classes,
[3404.18 → 3406.16] things like that as our challenges.
[3406.30 → 3408.86] And we've since moved to like almost all internal,
[3408.86 → 3409.94] um,
[3410.00 → 3410.46] content,
[3410.88 → 3411.34] but,
[3411.52 → 3411.76] uh,
[3411.92 → 3412.12] we,
[3412.20 → 3414.46] we got that live, and I would just hang out in the chat room.
[3414.54 → 3416.50] And whenever somebody came in,
[3416.52 → 3416.88] I'd be like,
[3416.90 → 3417.06] Hey,
[3417.08 → 3417.52] how's it going?
[3417.68 → 3417.84] Blah,
[3417.84 → 3418.00] blah,
[3418.00 → 3418.14] blah,
[3418.14 → 3418.28] blah,
[3418.28 → 3418.46] blah.
[3418.52 → 3421.70] Probably scared more people away than I actually like to retain that way.
[3422.08 → 3422.70] Bombard them.
[3423.24 → 3423.60] Yeah.
[3424.32 → 3425.28] But I,
[3425.36 → 3425.80] I mean,
[3426.30 → 3427.08] I literally,
[3427.08 → 3428.00] this is my life.
[3428.14 → 3428.34] You know,
[3428.46 → 3428.62] I,
[3428.68 → 3431.62] I have a young daughter and I spend as much time as I can with her,
[3431.72 → 3434.10] but often like the time I'm spending with her is me,
[3434.18 → 3436.20] like running around the city,
[3436.46 → 3438.10] pushing a stroller on the phone with,
[3438.44 → 3438.60] with,
[3438.74 → 3439.00] uh,
[3439.00 → 3439.72] a contributor.
[3440.56 → 3441.00] Um,
[3441.64 → 3444.76] I answer all of our team email myself still.
[3445.48 → 3445.92] Um,
[3446.76 → 3449.20] I spent a good amount of time in the chat room,
[3449.30 → 3449.76] uh,
[3449.76 → 3450.84] looking at GitHub issues.
[3450.84 → 3455.88] I just try to like lead by example by being as involved as possible and being
[3455.88 → 3457.42] completely down to earth and approachable.
[3457.42 → 3462.74] Like if you send me a message on Gitter or on Twitter or on Quora or any of
[3462.74 → 3463.18] these other,
[3463.18 → 3463.74] uh,
[3463.74 → 3464.74] platforms on Mac Devon,
[3464.88 → 3466.14] I will get back to you.
[3466.18 → 3467.32] I can't promise it'll be immediate,
[3467.32 → 3468.92] but I will get back to you.
[3469.02 → 3469.40] And,
[3469.72 → 3470.04] um,
[3470.12 → 3473.00] I think it's worth the time to accept that,
[3473.00 → 3473.40] uh,
[3473.42 → 3473.82] additional,
[3473.82 → 3474.70] you know,
[3474.98 → 3476.32] communication overhead,
[3476.42 → 3477.14] so to speak of,
[3477.20 → 3478.00] of trying to,
[3478.00 → 3478.98] uh,
[3479.02 → 3481.94] answer everybody's questions and make sure everybody feels their,
[3482.08 → 3483.08] their feedback is heard.
[3483.36 → 3485.90] Cause a lot of times great feedback just comes out of nowhere.
[3485.90 → 3486.78] And it's like,
[3486.82 → 3487.02] wow,
[3487.02 → 3488.36] why didn't we think of this before?
[3489.36 → 3491.48] So I would say that,
[3491.48 → 3491.98] um,
[3492.80 → 3496.06] that by trying to establish personal relationships at scale,
[3496.06 → 3496.92] um,
[3496.92 → 3497.62] just by,
[3497.62 → 3498.20] you know,
[3498.26 → 3501.10] cordoning off 50 hours of my week to talk to people,
[3501.10 → 3502.28] um,
[3502.52 → 3504.46] that has been instrumental in,
[3504.52 → 3505.80] in helping us build a team.
[3505.80 → 3506.22] I mean,
[3506.26 → 3506.66] uh,
[3506.66 → 3511.56] I can tell you some of the people that have joined that just kind of wandered in
[3511.56 → 3514.14] and started talking to me, and I was able to convince them to contribute,
[3514.30 → 3514.90] uh,
[3514.92 → 3515.24] you know,
[3515.34 → 3515.98] Raphael,
[3516.42 → 3516.98] uh,
[3517.68 → 3518.22] up in,
[3518.22 → 3518.50] uh,
[3518.50 → 3518.82] Brooklyn,
[3519.04 → 3522.22] he took over our wiki, and he's done an amazing job.
[3522.22 → 3523.96] And I think it was just like a casual,
[3524.46 → 3525.00] you know,
[3525.00 → 3529.82] he messaged me with some question on Gitter, and I was able to like wrangle him
[3529.82 → 3530.48] into like,
[3530.58 → 3530.70] Hey,
[3530.72 → 3531.44] you should write a wiki,
[3531.54 → 3531.98] uh,
[3532.10 → 3533.38] wiki entry on this.
[3533.44 → 3533.66] And we,
[3533.66 → 3534.40] we have our own wiki,
[3534.52 → 3535.66] which we're moving from GitHub.
[3535.80 → 3536.80] We were using GitHub as wiki.
[3536.94 → 3538.62] We're moving it over to our own wiki,
[3538.74 → 3541.52] using an awesome React driven tool called Gas,
[3541.56 → 3542.62] if you haven't heard of it,
[3542.64 → 3543.04] it's great.
[3543.68 → 3544.06] Um,
[3545.26 → 3546.82] Wesley McCann,
[3546.94 → 3547.62] uh,
[3547.64 → 3548.86] is kind of this,
[3548.86 → 3549.38] uh,
[3549.52 → 3550.96] nomad out in,
[3551.12 → 3551.46] uh,
[3552.02 → 3552.86] on the East coast.
[3553.28 → 3554.00] And he,
[3554.08 → 3557.52] he's the kind of guy that hops on a bicycle and bikes from Tampa to
[3557.52 → 3557.92] Boulder.
[3558.84 → 3559.28] Um,
[3559.66 → 3560.70] and he,
[3560.88 → 3561.18] uh,
[3561.38 → 3563.04] he took over our Twitch live-streaming.
[3563.94 → 3564.42] Um,
[3564.56 → 3568.62] and there's a guy named Everest who's from,
[3568.80 → 3569.54] I think the Netherlands.
[3569.54 → 3569.98] Um,
[3569.98 → 3573.56] and he was a data scientist and had this,
[3573.62 → 3573.88] you know,
[3573.92 → 3575.50] academic stats background and everything.
[3575.62 → 3580.36] And he was really interested in our data, and he created the data science
[3580.36 → 3584.52] chat room on Gitter and has basically been leading a lot of other
[3584.52 → 3587.74] academics and statisticians who are interested in working with our data.
[3588.10 → 3588.58] And,
[3588.62 → 3589.12] you know,
[3589.12 → 3590.02] learning more from,
[3590.44 → 3590.64] I guess,
[3590.70 → 3593.02] what amounts to a new paradigm in education.
[3593.20 → 3595.86] I don't think free code camp is precedented in terms of,
[3595.86 → 3596.78] uh,
[3596.88 → 3599.78] this specific combination of her mutations anyway.
[3600.32 → 3600.80] Um,
[3600.84 → 3601.36] and then,
[3601.36 → 3601.92] um,
[3603.42 → 3604.76] Vladimir Tamara,
[3605.36 → 3607.48] he's like a church director down in,
[3607.48 → 3608.14] uh,
[3608.22 → 3608.62] Bogotá,
[3609.32 → 3609.62] Colombia.
[3609.88 → 3610.38] And,
[3610.50 → 3610.70] uh,
[3610.86 → 3615.78] he was very interested in translating free code camp into Spanish and he
[3615.78 → 3616.88] did it so quickly.
[3617.48 → 3617.84] Uh,
[3618.32 → 3621.20] he did it very quickly, and we wrote the logic to like actually display the
[3621.20 → 3621.86] Spanish and we just,
[3622.42 → 3622.60] just,
[3622.82 → 3626.70] we just launched that during our big live stream a couple of days ago on
[3626.70 → 3627.02] Twitch.
[3627.16 → 3628.10] But basically,
[3628.10 → 3628.76] uh,
[3628.78 → 3629.02] he,
[3629.24 → 3632.76] he handled the Spanish translation so well and,
[3632.76 → 3636.48] and coordinated the volunteer effort so well that I was like,
[3636.54 → 3636.78] man,
[3636.86 → 3640.54] you should own our internationalization effort.
[3640.86 → 3646.14] So recognizing people that are doing great things and just giving them the
[3646.14 → 3648.26] reins and trusting that they're going to do a good thing.
[3648.48 → 3649.72] Here's an interesting anecdote.
[3649.72 → 3651.24] There's a guy,
[3651.24 → 3651.72] uh,
[3652.88 → 3656.72] who Bill Gates has only met one time or two times ever.
[3657.90 → 3660.46] And Bill Gates trusts his entire like $80 billion,
[3660.98 → 3661.66] you know,
[3661.70 → 3663.36] estate with this one finance guy.
[3663.50 → 3665.00] Because he just got a good impression.
[3665.22 → 3665.26] He,
[3665.28 → 3666.58] he didn't want to micromanage it.
[3666.64 → 3669.38] He didn't want to tell this guy how to do his job because he didn't have the
[3669.38 → 3671.72] domain expertise to do that with any level of reliability.
[3672.40 → 3673.10] So he's like,
[3673.16 → 3673.38] look,
[3673.74 → 3675.42] you're clearly doing a good job with this,
[3676.38 → 3677.04] you know,
[3677.20 → 3678.46] take it over.
[3678.46 → 3681.04] And I think that approach has worked really well.
[3681.10 → 3681.88] I've delegated,
[3681.88 → 3682.24] uh,
[3682.24 → 3682.48] things,
[3682.66 → 3683.36] Ben McMahon,
[3683.96 → 3685.56] a high school student out in,
[3685.64 → 3685.98] uh,
[3686.10 → 3686.34] Dublin,
[3686.46 → 3686.74] Ireland.
[3687.18 → 3687.62] Uh,
[3687.62 → 3689.28] we just gave him this project,
[3689.38 → 3689.68] uh,
[3689.68 → 3690.98] called the challenge-o-magic,
[3691.20 → 3693.90] which was like kind of gooey way to,
[3693.90 → 3694.20] uh,
[3694.20 → 3694.72] create,
[3694.80 → 3695.40] uh,
[3695.40 → 3696.98] challenges for free code games curriculum.
[3696.98 → 3699.24] So you didn't have to go in and just build them in JSON.
[3699.24 → 3701.06] Like I was building them back in the old day.
[3701.58 → 3701.98] Um,
[3701.98 → 3702.26] and,
[3702.26 → 3704.60] and he just took it and ran and built it.
[3705.42 → 3705.52] And,
[3705.56 → 3705.86] uh,
[3705.92 → 3710.52] like so much of our code base is the product of these people that just kind of
[3710.52 → 3712.46] wandered in and ended up being,
[3712.46 → 3713.48] uh,
[3713.98 → 3715.12] extremely productive.
[3715.12 → 3717.06] It's kind of like they follow a power law,
[3717.22 → 3721.62] like 90% of the people who come forward are going to put in a pull request and,
[3721.62 → 3723.54] and be of some level of,
[3723.54 → 3724.32] uh,
[3724.78 → 3725.66] of utility,
[3725.66 → 3727.48] which we greatly appreciate of course.
[3727.72 → 3734.34] And then occasionally we get these proverbial whales who just come in and like are extreme
[3734.34 → 3735.00] dynamo,
[3735.12 → 3738.54] dynamos of energy and just code nonstop all day,
[3738.62 → 3738.94] all night.
[3739.02 → 3739.92] That's what they love doing.
[3739.92 → 3740.16] I,
[3740.38 → 3740.58] you know,
[3740.60 → 3742.84] the guy I talked with or talked about earlier,
[3742.94 → 3743.20] Nathan,
[3743.20 → 3743.74] who's in,
[3743.94 → 3744.62] in the army,
[3744.74 → 3745.48] New Year's Eve,
[3746.02 → 3746.82] 2015,
[3747.86 → 3748.38] 2014,
[3748.80 → 3749.34] New Year's Eve.
[3749.70 → 3750.40] Like I,
[3750.50 → 3757.16] we didn't even realize that new year's had come and gone because we were so in depth on our,
[3757.16 → 3757.62] on our,
[3757.62 → 3757.84] uh,
[3757.84 → 3758.98] pair programming session.
[3759.04 → 3759.74] That's deep.
[3760.54 → 3761.02] Yeah.
[3761.04 → 3761.34] I mean,
[3761.34 → 3762.80] like we were just in the zone.
[3762.90 → 3764.12] We were like bonded,
[3764.12 → 3765.32] uh,
[3765.44 → 3766.64] at like the soul level.
[3767.46 → 3767.94] Wow.
[3768.48 → 3769.90] That's the testament to pair programming.
[3769.92 → 3770.50] I mean,
[3770.84 → 3771.00] to,
[3771.12 → 3773.24] to have that kind of attention span and,
[3773.24 → 3776.60] and be totally zoned in totally in flow.
[3777.24 → 3777.68] Yeah.
[3777.74 → 3778.84] And pair programming is great.
[3778.88 → 3780.36] And I can't say enough good things about it.
[3780.38 → 3781.78] Like that's the
[3781.94 → 3785.24] that's the main modality of me coding these days because it's,
[3785.24 → 3786.10] it's simultaneously,
[3786.10 → 3787.36] um,
[3787.50 → 3788.72] it produces better code,
[3788.76 → 3795.60] which is proven they've done research, and it produces less buggy code than individuals coding for commissive amount of time.
[3796.04 → 3796.44] Um,
[3796.44 → 3797.70] and at the same time,
[3797.70 → 3797.92] it's,
[3797.92 → 3800.84] it's like bonding, and you get to understand a person,
[3800.98 → 3801.36] you know,
[3801.36 → 3801.64] it's,
[3801.80 → 3802.48] it's like,
[3802.48 → 3803.58] like the heat of battle.
[3803.68 → 3805.26] You truly know a man's soul,
[3805.46 → 3805.90] you know?
[3805.98 → 3806.36] I mean,
[3806.36 → 3806.62] that's,
[3806.68 → 3808.20] that's how I feel about pair programming,
[3808.68 → 3809.06] you know?
[3809.20 → 3809.64] Love it.
[3810.18 → 3812.90] You don't really know somebody unless you pair program with them.
[3813.28 → 3813.68] So,
[3813.68 → 3814.18] uh,
[3814.38 → 3815.88] it's a great way to like,
[3815.96 → 3816.58] not only,
[3816.82 → 3817.30] um,
[3817.98 → 3820.30] understand them better and get meaningful work done.
[3820.30 → 3820.74] and,
[3820.96 → 3822.18] and at the same time I can,
[3822.46 → 3822.74] uh,
[3823.38 → 3823.66] you know,
[3823.70 → 3825.22] teach them a little bit about my,
[3825.38 → 3831.74] my particular worldview in terms of like features and how to like keep free code camp as simple as possible,
[3831.74 → 3837.14] which we're constantly culling features that get in there just because they complicate the user experience.
[3837.38 → 3838.56] I want to keep things simple.
[3838.74 → 3838.86] So,
[3839.10 → 3839.70] um,
[3839.74 → 3844.50] we've got a lot of other people that are coming forward that look like they're going to be incredible contributors as well.
[3844.50 → 3846.60] Like every day I'm getting,
[3846.60 → 3847.20] uh,
[3847.56 → 3847.78] you know,
[3847.84 → 3849.80] messages from various professionals with,
[3849.80 → 3852.28] with lots of domain expertise that want to help out.
[3852.44 → 3856.74] So my key to sustaining this chain reaction,
[3856.86 → 3863.32] which I was lucky enough to kick off is just listening to people and giving them agency.
[3864.72 → 3865.80] While we're on that,
[3865.80 → 3866.24] uh,
[3866.24 → 3866.78] that note,
[3866.82 → 3868.06] then since you're talking about pair programming,
[3868.32 → 3869.78] let's talk about the stack behind this.
[3869.78 → 3869.94] Like,
[3869.98 → 3870.74] what is it built in?
[3870.78 → 3871.62] How do you ship it?
[3871.92 → 3872.58] Who's involved?
[3872.58 → 3874.38] And you talked about,
[3874.46 → 3874.74] you know,
[3874.78 → 3876.18] during the process of pair programming,
[3876.18 → 3879.86] you get a chance to share your philosophies and keeping things simple.
[3879.86 → 3885.02] So it sounds like there's some core values that get shared through these interactions you have with,
[3885.02 → 3885.32] uh,
[3885.32 → 3885.98] the team.
[3886.10 → 3886.84] What's it like?
[3886.90 → 3887.82] What's it built on and,
[3887.82 → 3889.20] and share that with us.
[3889.62 → 3890.10] Sure.
[3890.12 → 3892.24] We started out with basically the mean stack,
[3892.24 → 3893.58] um,
[3894.56 → 3896.22] MongoDB express,
[3896.46 → 3897.52] angular and node.
[3897.70 → 3899.34] And now we're using,
[3899.34 → 3900.02] uh,
[3900.78 → 3901.54] MongoDB,
[3901.54 → 3902.74] still,
[3902.74 → 3903.44] and,
[3903.44 → 3903.72] uh,
[3903.72 → 3904.38] node still.
[3904.50 → 3905.86] We're using a loop back,
[3906.66 → 3907.10] uh,
[3907.68 → 3908.26] which is,
[3908.40 → 3908.70] uh,
[3908.70 → 3911.90] also by strong loop that I think created and maintain express.
[3912.54 → 3913.06] And,
[3913.18 → 3913.42] uh,
[3913.42 → 3914.56] we're also using,
[3914.56 → 3915.12] uh,
[3915.26 → 3918.64] we've moved to react, and we're moving from our own,
[3918.64 → 3919.60] uh,
[3919.84 → 3922.20] open source implementation of flux,
[3922.46 → 3922.86] um,
[3923.62 → 3924.88] called thunder cast JS,
[3924.88 → 3925.62] which Berkeley,
[3926.28 → 3926.84] um,
[3927.10 → 3928.62] who I said is in charge of our,
[3928.66 → 3929.06] our,
[3929.06 → 3929.36] uh,
[3929.36 → 3929.66] repo.
[3930.36 → 3930.70] Um,
[3930.98 → 3931.84] he built this,
[3931.94 → 3932.26] uh,
[3932.46 → 3932.66] this,
[3932.86 → 3934.90] this flux tool called thunder cast JS,
[3934.90 → 3942.34] but he's recently come around to the fact that Dan Sermon is a genius and has the
[3942.34 → 3942.90] like,
[3943.08 → 3944.50] you can't top redux.
[3944.50 → 3946.84] So we're moving to redux as well.
[3947.38 → 3947.56] So,
[3947.56 → 3947.90] uh,
[3947.90 → 3949.28] Berkeley's transitioning to that.
[3949.80 → 3950.20] And,
[3950.30 → 3950.60] uh,
[3950.86 → 3953.22] so soon free code camp will be like a full,
[3953.22 → 3953.70] uh,
[3953.70 → 3953.92] you know,
[3953.92 → 3955.60] single page react experience.
[3956.82 → 3957.72] What about curriculum?
[3957.84 → 3958.76] How do you author curriculum?
[3958.84 → 3960.12] And how do you get that into the system?
[3960.12 → 3960.20] Um,
[3960.48 → 3966.22] so what we do is we just create these JSON files, and we used to just do it manually.
[3966.22 → 3970.38] Like I would insert HTML into JSON and the seed it in that way.
[3970.38 → 3976.42] It's really easy because instead of having it in some database somewhere that it just gets blown up every time you reseed it.
[3976.94 → 3977.30] Um,
[3977.30 → 3978.08] and,
[3978.20 → 3978.50] uh,
[3978.52 → 3979.08] that way,
[3979.08 → 3984.82] like it's very easy to go in and add a translation to it or add a new feature to all the challenges.
[3986.40 → 3989.16] So we just stored in all this JSON and,
[3989.28 → 3989.48] uh,
[3989.86 → 3991.22] in terms of curriculum development,
[3991.22 → 3992.40] if you're curious about that too,
[3992.96 → 3993.78] it's very incremental.
[3993.78 → 3995.48] Like we basically say,
[3995.56 → 3997.82] like what we did in December was we said,
[3997.94 → 4001.42] we want to have React D3 and SAS covered SAS.
[4001.66 → 4005.24] We were switching from less to SAS because bootstraps moving from less to SAS.
[4005.24 → 4006.16] And we,
[4006.28 → 4009.92] we're going to continue using and teaching bootstrap because we think it's awesome.
[4010.64 → 4011.00] Um,
[4011.32 → 4013.52] and if bootstrap is using SAS,
[4013.66 → 4013.84] well,
[4014.10 → 4015.20] if it's good enough for bootstrap,
[4015.26 → 4016.14] it's probably good enough for us.
[4016.18 → 4018.16] So we're moving over to SAS and,
[4018.52 → 4019.80] we wanted to teach all those,
[4020.26 → 4024.72] but what we wanted to do is we're very focused on evaluation criteria rather than process.
[4025.20 → 4032.28] So we'd start with the evaluation criteria, and then we build the curriculum to work people up to it.
[4032.34 → 4034.48] So what we did first was our community,
[4034.48 → 4041.56] we put together 15 new challenges or 10 new challenges specifically for the data visualization component.
[4041.94 → 4045.68] And we lumped react and SAS in with data visualization because it was convenient,
[4045.80 → 4048.78] even though you could argue it's part of a front end development more so.
[4049.38 → 4049.56] But,
[4049.64 → 4050.04] um,
[4050.58 → 4053.02] we created like five D3 challenges,
[4053.02 → 4054.22] uh,
[4054.22 → 4054.86] where you build,
[4054.92 → 4055.36] you know,
[4055.42 → 4058.26] visualizations of increasing complexity.
[4058.26 → 4062.96] And five react SAS challenges where you can use any tools you want,
[4063.00 → 4064.28] but you have to use React and SAS,
[4064.40 → 4067.58] including on up to creating a roguelike,
[4067.58 → 4068.56] um,
[4068.96 → 4069.76] RPG game,
[4069.86 → 4070.08] right.
[4070.20 → 4071.34] In browser that runs.
[4071.34 → 4075.66] And all of these projects ideally run right on code pen.
[4076.06 → 4077.60] So you don't have to,
[4077.60 → 4078.08] uh,
[4078.08 → 4079.04] spend a lot of time,
[4079.04 → 4079.86] uh,
[4080.18 → 4080.40] you know,
[4080.42 → 4080.98] bootstrapping,
[4081.08 → 4081.48] uh,
[4081.48 → 4082.92] development environment thing.
[4083.30 → 4084.32] Code pen has been great.
[4084.44 → 4084.80] And,
[4084.94 → 4085.28] um,
[4085.82 → 4090.00] and we use a cloud nine for the backend challenges just because it's simpler than trying to say,
[4090.06 → 4090.28] okay,
[4090.28 → 4091.54] now go download this VM.
[4091.54 → 4091.86] No.
[4092.32 → 4095.50] And so run all these commands to set up your Linux environment,
[4095.64 → 4095.88] you know?
[4096.36 → 4104.82] So are those companies involved by any chance that you mentioned Twitch earlier in that your live channel and people giving back and pouring in may not be monetarily,
[4104.98 → 4106.64] but just free resources.
[4106.64 → 4107.96] Are they pitching in any way?
[4108.54 → 4108.94] No,
[4109.20 → 4109.48] uh,
[4109.48 → 4109.62] we,
[4109.66 → 4112.12] we looked into doing corporate sponsorships.
[4112.46 → 4112.94] Um,
[4112.96 → 4114.84] it's something we may explore again in the future,
[4114.84 → 4116.14] but it is like,
[4116.32 → 4118.80] we didn't want to,
[4119.04 → 4119.34] uh,
[4119.40 → 4120.32] we didn't need to,
[4120.68 → 4121.06] frankly.
[4121.06 → 4121.78] Um,
[4121.78 → 4122.44] we still have,
[4122.60 → 4123.30] you know,
[4123.32 → 4124.50] a couple of years worth of runway,
[4124.70 → 4125.64] even on my savings.
[4126.10 → 4126.46] Uh,
[4126.88 → 4129.50] so we're kind of slow rolling,
[4129.96 → 4130.36] uh,
[4130.56 → 4132.26] getting revenue,
[4132.36 → 4133.04] if you will.
[4133.20 → 4133.44] Um,
[4133.44 → 4133.78] I think,
[4134.08 → 4134.38] I think,
[4134.48 → 4134.90] um,
[4134.90 → 4136.46] if we can get it through our community,
[4136.46 → 4137.50] through merchandise,
[4138.32 → 4138.62] like,
[4138.66 → 4138.98] um,
[4138.98 → 4139.20] you know,
[4139.20 → 4139.62] stickers,
[4140.22 → 4140.58] uh,
[4141.10 → 4141.84] laptop stickers,
[4142.24 → 4142.70] t-shirts,
[4143.36 → 4143.62] um,
[4143.62 → 4147.42] potentially like raspberry pies loaded up with our curriculum and things like that.
[4147.56 → 4148.00] Um,
[4148.06 → 4148.78] then we will,
[4148.86 → 4149.04] uh,
[4149.04 → 4150.24] absolutely do that first.
[4150.24 → 4150.36] Um,
[4151.06 → 4152.70] and then we'll consider,
[4152.70 → 4153.28] you know,
[4153.92 → 4156.78] doing things that might compromise our perceived,
[4156.78 → 4157.56] uh,
[4158.44 → 4158.98] uh,
[4159.12 → 4159.74] neutrality.
[4159.74 → 4160.22] I mean,
[4160.28 → 4161.30] I don't think it's a big deal.
[4161.44 → 4161.54] I,
[4161.74 → 4163.98] every good podcast I listen to has corporate sponsors.
[4164.08 → 4165.00] I don't think anything of it.
[4165.00 → 4165.78] Uh,
[4165.78 → 4166.20] so,
[4166.20 → 4166.64] but,
[4166.64 → 4166.66] but,
[4166.66 → 4167.70] but we just personally,
[4167.70 → 4168.26] we're like,
[4168.36 → 4168.44] well,
[4168.44 → 4169.30] we can cross that bridge.
[4169.80 → 4174.46] Part of it was like a lot of people didn't understand a lot of the organizations we approached
[4174.46 → 4176.90] to just kind of feel out for this,
[4176.96 → 4178.52] didn't understand what free cook camp was.
[4178.80 → 4180.30] And they thought we were like a hackathon.
[4180.96 → 4181.32] Uh,
[4181.32 → 4182.76] and they were just used to,
[4182.76 → 4184.10] to bankrolling hackathons,
[4184.20 → 4184.58] for example.
[4184.58 → 4185.86] So they've been thus and that.
[4186.38 → 4187.04] And it,
[4187.38 → 4188.30] as a result,
[4188.40 → 4189.12] like they,
[4189.34 → 4191.66] it's complicated,
[4191.78 → 4194.20] but we're going to consider that maybe down the road,
[4194.24 → 4196.28] but if we can support ourselves purely through,
[4196.28 → 4196.84] um,
[4197.12 → 4198.68] through matching,
[4198.68 → 4199.04] uh,
[4199.04 → 4201.96] campers who complete our curriculum with employers who want to hire them,
[4201.96 → 4204.58] which if you look at the recruitment business,
[4204.58 → 4205.26] um,
[4205.26 → 4207.28] and like hire.com and all these other companies,
[4207.28 → 4208.56] obviously there's money there.
[4208.94 → 4209.38] Um,
[4209.38 → 4213.36] and if we're creating hundreds of thousands of skilled developers,
[4213.36 → 4216.20] I'm not concerned about us being able to sustain ourselves.
[4216.44 → 4216.88] Right.
[4217.34 → 4217.54] I mean,
[4217.54 → 4219.86] I didn't want to bring up the sustainability thing again,
[4219.86 → 4221.38] just because I mean,
[4221.38 → 4224.60] I mentioned those opportunities just as like,
[4224.64 → 4226.10] are they giving back in some sort of way?
[4226.62 → 4227.16] But yeah.
[4227.44 → 4227.76] Yeah.
[4227.76 → 4230.84] You talked about a runway and things like that.
[4231.00 → 4233.22] And not quite Jared,
[4233.30 → 4235.24] I really hate this late in the game,
[4235.32 → 4236.58] but I really hate bringing it back up.
[4236.64 → 4237.16] But since you mentioned,
[4237.28 → 4237.86] I have to,
[4238.38 → 4238.74] you know,
[4239.00 → 4240.02] is there a burn rate?
[4240.12 → 4241.16] Do you have expenses?
[4241.16 → 4241.72] Like how,
[4241.78 → 4243.16] how do these things work for you?
[4243.18 → 4243.78] Like you said,
[4243.80 → 4245.30] you've got your own savings.
[4245.30 → 4247.64] And so you're essentially fitting the bill,
[4247.68 → 4250.60] so to speak for everything going on with a
[4250.68 → 4254.10] with a plan to eventually somehow figure out,
[4254.10 → 4255.28] because there are opportunities,
[4255.28 → 4256.58] but you're going to figure out later on,
[4256.58 → 4259.10] once you hit some sort of place,
[4259.16 → 4260.30] some sort of milestone to say,
[4260.36 → 4260.52] okay,
[4260.52 → 4264.38] now it's time to think about how we can generate some revenue.
[4264.56 → 4264.96] T-shirts,
[4265.10 → 4267.62] obviously stickers back to the community makes sense for,
[4267.70 → 4268.26] for a short term,
[4268.32 → 4269.30] but not a long-term gain.
[4270.66 → 4271.06] Yeah.
[4271.18 → 4271.48] I mean,
[4271.48 → 4271.66] we,
[4271.66 → 4271.90] we,
[4271.90 → 4274.60] we've been thinking about these for a long time,
[4274.60 → 4277.58] because obviously we want free code camp to continue and,
[4277.58 → 4278.38] and make no mistake,
[4278.38 → 4279.38] like worst case scenario,
[4279.38 → 4281.00] we shut down free code camp.
[4281.08 → 4281.22] The
[4281.32 → 4283.26] the effort it's open source.
[4283.38 → 4283.58] I mean,
[4283.58 → 4286.96] somebody could just relaunch it, and we certainly do everything we could.
[4286.96 → 4288.30] It's kind of like parse is shutting down,
[4288.36 → 4290.54] but they're open sourcing pretty much everything.
[4290.54 → 4290.84] Yeah.
[4290.84 → 4292.50] So it's not really a loss.
[4292.56 → 4293.34] It's just an inconvenience.
[4293.34 → 4294.00] It's Facebook.
[4294.22 → 4295.24] So you expect that in a way.
[4295.70 → 4295.90] Yeah,
[4295.90 → 4296.82] I think it's good.
[4297.04 → 4297.26] Yeah.
[4297.38 → 4297.78] But,
[4297.98 → 4301.66] but I don't think we're in any risk of doing that.
[4301.70 → 4303.62] Like worst case scenario,
[4303.62 → 4305.46] we could open it up to donations.
[4305.46 → 4306.16] And I mean,
[4306.16 → 4309.04] with hundreds of thousands of people using free code camp right now,
[4309.04 → 4312.62] and we're hoping to hit a million by 2017.
[4312.62 → 4313.62] Um,
[4314.62 → 4316.28] you know,
[4316.36 → 4316.46] I,
[4316.52 → 4319.52] I think that we could generate enough to cover the server costs,
[4319.58 → 4320.96] which are not that significant.
[4321.68 → 4322.08] And,
[4322.24 → 4322.50] uh,
[4322.60 → 4322.82] and,
[4322.98 → 4327.32] and the main cost associated with free code camp is my opportunity cost.
[4327.32 → 4328.28] If you're familiar with the
[4328.28 → 4331.94] the economic concept of opportunity costs as a software engineer,
[4331.94 → 4334.04] I could go out and get a pretty good job.
[4334.34 → 4337.30] So that's income that I'm foregoing working on a free code camp.
[4337.30 → 4337.60] But,
[4337.72 → 4338.46] you know,
[4338.52 → 4341.24] I don't really care about money that much.
[4341.48 → 4342.40] I'm like I said,
[4342.40 → 4345.54] I'm happy to just eat microwave burritos and sit in my closet and coat all
[4345.54 → 4345.72] day,
[4345.76 → 4346.88] which costs almost nothing.
[4346.88 → 4350.30] Like my daily expenses would be like 20 bucks.
[4350.64 → 4351.14] And then,
[4351.34 → 4351.62] you know,
[4351.62 → 4354.38] my wife has a good job, and she has benefits.
[4354.58 → 4356.10] I'm very fortunate for that,
[4356.44 → 4356.78] you know,
[4356.78 → 4357.24] because,
[4357.24 → 4358.22] um,
[4358.22 → 4360.82] if we need to go see a doctor or take our baby to the doctor,
[4360.82 → 4361.48] we can do that.
[4361.56 → 4362.02] No problem.
[4362.40 → 4362.52] So,
[4362.64 → 4365.12] so there are two reasons why we asked that question.
[4365.22 → 4365.66] Uh,
[4365.66 → 4366.52] and I,
[4366.62 → 4369.40] the only reason I'm going to clarify this is that I don't want anyone to
[4369.40 → 4370.32] think we have,
[4370.32 → 4373.86] or I have the wrong idea with trying to drive that question home.
[4373.86 → 4374.24] It's like,
[4374.24 → 4376.32] we think like the change log,
[4376.40 → 4379.22] this show is listened to by all sorts of kinds of people,
[4379.22 → 4379.58] right?
[4379.90 → 4381.86] People come to this show and maybe this one in particular,
[4381.86 → 4384.46] because of who you are and what you're doing,
[4384.46 → 4386.66] because they aspire to be like,
[4386.72 → 4388.46] or they have the same dreams as you do.
[4388.62 → 4389.84] And it's not to say,
[4389.84 → 4390.48] you know,
[4390.48 → 4391.26] like negatively,
[4391.38 → 4392.18] how are you getting there?
[4392.18 → 4393.94] But more like how are you getting there?
[4393.94 → 4397.46] Cause somebody else might be wanting to ask that same question and follow
[4397.46 → 4400.56] the same path and jump on the same ship you're already on.
[4400.78 → 4403.32] And so I just want to clarify that.
[4403.40 → 4405.18] So it's not mistaken anyway.
[4405.30 → 4406.22] I know it's probably not,
[4406.30 → 4407.60] and I'm over clarifying it,
[4407.98 → 4409.12] but I had to say it.
[4409.22 → 4409.32] So,
[4409.84 → 4409.94] yeah,
[4409.96 → 4410.24] I mean,
[4410.24 → 4410.98] if I could give it,
[4411.04 → 4413.00] if anybody's interested in my advice,
[4413.14 → 4413.40] right?
[4413.70 → 4415.80] I really want you to help these people listening,
[4415.96 → 4417.52] know what you're doing and how you're doing this.
[4417.58 → 4418.54] They can get involved.
[4419.04 → 4420.20] The advice is burritos.
[4420.20 → 4420.80] Yeah.
[4421.16 → 4422.28] Like keep costs low,
[4422.74 → 4422.98] uh,
[4422.98 → 4423.50] save money.
[4423.96 → 4424.32] Uh,
[4424.48 → 4425.00] I mean,
[4425.10 → 4428.08] if you're going out and buying brand-new cars off the lot,
[4428.16 → 4430.66] like there's a good chance that you're not able to afford to,
[4430.66 → 4431.04] uh,
[4431.04 → 4432.04] to finance a
[4432.08 → 4433.04] an operation like this.
[4433.04 → 4434.36] And you're going to be at to behead,
[4434.48 → 4434.86] you know,
[4434.86 → 4439.32] you're going to be beholden to these bankers and other people that are,
[4439.32 → 4440.10] you know,
[4440.28 → 4441.88] maybe not the most savoury types,
[4441.94 → 4442.24] frankly.
[4442.76 → 4443.04] Uh,
[4443.04 → 4444.10] and don't share your,
[4444.30 → 4446.10] their interests are not aligned with you.
[4446.18 → 4449.68] They want to pump you full of steroids and run you up to a liquidation.
[4450.20 → 4450.60] Uh,
[4450.60 → 4451.48] a liquidity event,
[4451.56 → 4451.80] which,
[4451.80 → 4452.36] uh,
[4452.36 → 4452.76] DHH,
[4453.12 → 4453.44] uh,
[4453.52 → 4453.84] the found,
[4453.94 → 4455.06] like the guy who created rails,
[4455.06 → 4458.48] wrote an awesome article on medium about how,
[4458.48 → 4459.02] you know,
[4459.04 → 4461.90] you should figure out a way to sustain your organization without financing.
[4461.90 → 4463.06] Um,
[4463.06 → 4464.38] so if you can save up money,
[4464.38 → 4466.80] that's one easy way you can just self fund.
[4467.48 → 4467.84] Um,
[4468.04 → 4470.62] but even if you do self fund,
[4470.66 → 4471.52] how do you get traction?
[4472.00 → 4472.40] Well,
[4472.66 → 4473.98] if you look at how,
[4473.98 → 4474.38] uh,
[4474.38 → 4475.26] Pinterest took off,
[4475.30 → 4475.56] you know,
[4475.56 → 4476.62] the guy wrote handwritten,
[4476.62 → 4477.64] uh,
[4477.68 → 4481.30] letters to every single person who signed up for Pinterest and mail them to
[4481.30 → 4481.80] them physically.
[4481.80 → 4482.10] Like,
[4482.18 → 4486.22] can you imagine opening up your mailbox, and you've got a letter from the
[4486.22 → 4488.76] founder of the service you just signed up for?
[4488.76 → 4490.52] Like it takes grit.
[4490.60 → 4490.82] It's,
[4490.94 → 4491.36] it's not,
[4491.80 → 4493.14] it's not something you should take trivial.
[4493.66 → 4493.78] Right.
[4493.82 → 4497.72] It's extremely difficult to get past that initial indifference towards your
[4497.72 → 4498.18] project.
[4499.18 → 4500.48] And you know,
[4500.48 → 4502.76] like no amount of money is going to get you past that.
[4502.82 → 4505.78] You can't Google ads your way out of people just not giving a damn about
[4505.78 → 4506.38] your project.
[4506.38 → 4507.30] Well,
[4507.30 → 4508.54] let's,
[4508.62 → 4508.92] uh,
[4508.92 → 4512.06] let's take that opportunity to turn into a break real quick.
[4512.54 → 4512.94] Um,
[4513.34 → 4514.32] when we come back,
[4514.32 → 4518.30] some closing questions we have are obviously some of the traditional closing
[4518.30 → 4519.24] questions we have,
[4519.24 → 4520.44] um,
[4520.52 → 4521.84] which is open source,
[4521.84 → 4522.62] uh,
[4522.68 → 4523.16] radar.
[4523.36 → 4524.06] Who's your hero.
[4524.50 → 4525.70] But specifically,
[4525.70 → 4527.28] since we're on this topic,
[4527.78 → 4528.80] we want to talk about your needs.
[4528.80 → 4529.02] You know,
[4529.02 → 4531.12] if there's somebody out there that wants to get involved,
[4531.24 → 4532.00] wants to help out,
[4532.04 → 4532.98] whether it's teaching,
[4532.98 → 4533.70] uh,
[4533.70 → 4534.46] helping with curriculum,
[4534.46 → 4535.38] whether it's mentoring,
[4535.80 → 4536.46] whatever it might be.
[4536.50 → 4537.74] Let's talk about some of your needs.
[4538.16 → 4538.82] And then,
[4538.88 → 4539.12] uh,
[4539.12 → 4539.24] we,
[4539.46 → 4542.66] we haven't quite touched on getting started, and I feel like maybe there's
[4542.66 → 4544.16] tons of people out there that already started,
[4544.16 → 4545.08] but nonetheless,
[4545.20 → 4548.42] let's voice out at least what it takes to get started with pre-code camp
[4548.42 → 4549.94] and what that process is like.
[4549.94 → 4552.58] So let's touch on that when we come back from this break.
[4553.86 → 4557.48] We're excited to be working with BMC to spread the word about true site
[4557.48 → 4558.00] pulse.
[4558.00 → 4563.32] They're SAS based monitoring service for cloud and server infrastructure that lets
[4563.32 → 4564.00] you monitor,
[4564.54 → 4567.74] visualize and alert with one second resolution.
[4568.10 → 4570.18] I had a chance to talk to Mike Moran,
[4570.28 → 4574.22] the senior architect about what real time monitoring is.
[4574.30 → 4574.84] Take a listen.
[4575.54 → 4577.34] Real time obviously means different things,
[4577.42 → 4578.48] different people to us.
[4578.56 → 4579.76] Real time is one second.
[4579.92 → 4580.44] So for us,
[4580.44 → 4583.42] we have one-second metrics on everything that we collect.
[4583.42 → 4584.46] We'll pull all of that,
[4584.60 → 4588.46] push it to our servers, and you can see it roughly in about four to eight
[4588.46 → 4588.90] seconds,
[4588.90 → 4591.68] depending on where that falls in the interval.
[4591.68 → 4594.32] So we'll pull one-second data and within eight seconds,
[4594.32 → 4596.00] you can see it streaming live on your dashboard.
[4596.70 → 4597.88] So during this conversation with Mike,
[4597.92 → 4600.70] I was trying to figure out what real time monitoring means to them.
[4601.08 → 4604.82] And I was also trying to figure out who might use it and why they would care
[4604.82 → 4608.38] about one second resolution timing when it comes to monitoring their
[4608.38 → 4608.94] infrastructure.
[4609.46 → 4611.04] And this is how Mike broke it down for me.
[4611.04 → 4614.36] I think at the beginning you kind of looked at it and went,
[4614.48 → 4616.10] that's a very niche set of the market.
[4616.10 → 4617.86] But I think as things have changed,
[4618.06 → 4618.18] you know,
[4618.20 → 4621.12] you can look at e-commerce companies, or you can look at anybody who's running
[4621.12 → 4621.76] an application.
[4622.18 → 4626.04] We now have stacks that are very nimble, and we end up with things like
[4626.04 → 4629.24] restarts that are quick, or our stats change very,
[4629.36 → 4630.06] very quickly now.
[4630.06 → 4632.32] So our spikes maybe aren't something that,
[4632.62 → 4632.82] you know,
[4633.08 → 4636.38] it's not Black Friday and you end up with this gradual spike or this
[4636.38 → 4638.04] immediate spike that lasts for a long time.
[4638.20 → 4640.66] You now have a lot of things happening because you have so many
[4640.66 → 4643.94] interconnected systems, and you have microservices and dependencies
[4643.94 → 4644.42] everywhere.
[4644.74 → 4647.42] Something happening in one obviously affects other things,
[4647.52 → 4649.94] but if it's something small or happens very quickly,
[4650.00 → 4650.80] you don't notice that.
[4651.36 → 4652.66] And at this point with Mike,
[4652.70 → 4653.08] I was like,
[4653.14 → 4653.28] well,
[4653.38 → 4654.44] what's a better example?
[4654.56 → 4660.00] Give me a real world example that everyone knows about that can really,
[4660.00 → 4666.64] explain how important it is to have one second near real time monitoring on
[4666.64 → 4667.70] infrastructure level stuff,
[4667.76 → 4668.54] stuff that really matters,
[4668.62 → 4669.16] the heartbeat,
[4669.30 → 4671.14] so to speak of an infrastructure.
[4671.24 → 4672.02] And this is what he had to say.
[4672.04 → 4672.64] It's pretty interesting.
[4673.22 → 4675.50] If you're looking at your EKG, and you're looking at your heartbeat,
[4675.68 → 4679.58] how many doctors would ever look at your heartbeat at a minute interval or a
[4679.58 → 4680.40] 15 second interval?
[4680.52 → 4683.56] You'd be crazy because you'd miss whatever was happening with your heart.
[4683.56 → 4685.78] And that's something that you wouldn't want to screw with.
[4686.56 → 4686.72] Wow.
[4686.72 → 4691.00] What a great real world example of what that exactly means.
[4691.10 → 4691.72] I don't know about you,
[4691.78 → 4692.98] but I don't want to mess with my heart.
[4693.46 → 4694.70] My heart keeps me going.
[4694.82 → 4695.78] Your heart keeps you going.
[4695.88 → 4698.30] And if you value the heart of your business,
[4698.40 → 4699.48] the heart of your infrastructure,
[4699.48 → 4702.28] you're going to care about one second resolution timing.
[4702.36 → 4704.00] You're going to care about real time monitoring.
[4704.72 → 4708.84] And BMC's true site pulse truly is something you should take a look at.
[4708.84 → 4712.26] Head to BMC.com slash true site pulse,
[4712.54 → 4713.32] all one word,
[4713.66 → 4716.36] no hyphens and telling the Ching's long sent you.
[4719.12 → 4719.60] All right,
[4719.62 → 4722.24] we're back from our final break of the show.
[4722.24 → 4723.28] And Quincy,
[4723.70 → 4726.58] obviously we've loved diving deep in this conversation with you.
[4726.68 → 4729.50] We've talked about where you personally came from.
[4729.66 → 4731.30] We've talked about your,
[4731.38 → 4732.24] your goals and motivations.
[4733.24 → 4736.82] A lot of give back to those who are involved.
[4736.82 → 4738.60] Those who are actually making it through.
[4739.96 → 4743.00] And I think there's a lot of people out there right now who are thinking,
[4743.20 → 4744.68] I want to get involved,
[4744.76 → 4749.66] whether it's becoming a camper and getting taught or mentored or,
[4749.66 → 4750.14] you know,
[4750.22 → 4751.26] taking part of,
[4751.26 → 4752.68] you know,
[4752.98 → 4754.94] pair programming and all these different things you've,
[4755.00 → 4756.08] you've mentioned on the show here today,
[4756.08 → 4758.34] but there's a lot of people out there who want to get involved somehow.
[4758.50 → 4759.64] So what are your needs?
[4759.98 → 4760.98] How can people help out?
[4761.00 → 4761.90] How can they get involved?
[4762.24 → 4763.34] And not only how,
[4763.46 → 4766.26] but if they want to do it specifically,
[4766.26 → 4768.94] where can they go to like to take the next step?
[4770.36 → 4773.58] One thing we're huge on is internationalization.
[4773.58 → 4780.34] A lot of people are not native English speakers and would benefit tremendously from not having to
[4780.34 → 4782.28] simultaneously learn English and coding.
[4782.28 → 4788.86] So we are basically all of our video challenges where,
[4788.86 → 4789.36] you know,
[4789.42 → 4794.32] Brianna stands in front of the whiteboard and draws diagrams and explains theoretical concepts.
[4794.48 → 4798.58] We would love to have those re-recorded by native Portuguese speakers,
[4799.18 → 4800.56] native Chinese speakers,
[4801.14 → 4802.28] you know,
[4802.32 → 4803.70] various world languages.
[4803.70 → 4803.84] languages.
[4805.26 → 4809.22] We would also like to have our entire wiki translated into all these different languages
[4809.22 → 4811.28] because our wiki is like,
[4811.44 → 4811.62] we're,
[4811.66 → 4819.24] we're trying to build a kind of very easy to read and friendly version of maybe Mozilla's developer network
[4819.24 → 4819.68] or,
[4819.80 → 4820.86] or some of these other resources.
[4820.86 → 4823.76] They're maybe a little bit more esoteric and not quite as beginner-friendly.
[4823.76 → 4824.74] We want to make it really,
[4824.86 → 4829.10] really beginner-friendly and issue as much jargon as possible.
[4830.20 → 4830.64] So,
[4830.78 → 4833.06] so that is one area where we could definitely use help.
[4833.60 → 4834.48] So the
[4834.74 → 4838.12] both the translation and the creation of those challenges of the
[4838.16 → 4841.26] of those videos and of those wiki articles is,
[4841.38 → 4842.44] is one place where you could,
[4842.90 → 4845.10] if you're listening, and you want to get some open source contributions,
[4845.10 → 4847.06] like Matt Mel wig from,
[4847.20 → 4847.46] uh,
[4847.94 → 4857.98] WordPress was saying like everybody who goes to a bootcamp or some sort of intensive program should try to get as many open source contributions under his or her belt as possible.
[4857.98 → 4858.20] Well,
[4858.24 → 4862.58] we absolutely will take any contribution seriously and look at them and,
[4862.64 → 4863.44] um,
[4863.44 → 4867.28] we would love your contributions, and you can contribute all those and all that stuff will go through GitHub.
[4867.44 → 4868.98] So you'll get GitHub credit for it.
[4869.76 → 4870.58] GitHub credit.
[4870.74 → 4871.30] Love that idea.
[4872.48 → 4873.72] PRs as credit.
[4873.72 → 4874.52] Uh,
[4874.52 → 4875.80] what about on the teaching side and,
[4875.80 → 4877.00] and curriculum mentoring?
[4877.36 → 4877.64] You know,
[4877.66 → 4878.24] you mentioned,
[4878.42 → 4885.10] I think just through conversation that some of the people that have stepped up and gotten involved have done so through their,
[4885.10 → 4885.46] you know,
[4885.46 → 4887.16] smaller contributions, and you've sort of,
[4887.16 → 4887.94] uh,
[4887.94 → 4888.66] noted that they,
[4888.80 → 4889.48] they're perfect at it.
[4889.50 → 4892.80] And so you handed them more responsibility based on doing perfect with small responsibilities.
[4893.30 → 4894.98] But what about those teachers out there who are like,
[4895.02 → 4895.32] you know what?
[4895.34 → 4896.34] I just want to give back.
[4896.40 → 4898.30] I got like five hours a week.
[4898.36 → 4899.72] Are there opportunities for teachers,
[4899.90 → 4900.30] mentors,
[4900.62 → 4901.10] you know,
[4901.10 → 4901.88] how can they step in?
[4901.90 → 4902.88] Is that an opportunity for them?
[4903.72 → 4904.00] Well,
[4904.06 → 4907.10] there is one immediate way that anyone can give back,
[4907.16 → 4909.32] which is to just jump into our chat rooms.
[4909.78 → 4910.18] And,
[4910.26 → 4910.44] uh,
[4910.44 → 4912.74] we have help rooms on a variety of topics,
[4912.92 → 4913.32] uh,
[4913.32 → 4914.88] data visualization,
[4915.72 → 4916.48] backend development,
[4916.72 → 4917.42] things like that.
[4917.42 → 4921.40] and if you were interested in jumping into one of those,
[4921.40 → 4922.56] you could help answer,
[4922.56 → 4923.18] uh,
[4923.18 → 4932.52] questions from our community because people will frequently get blocked, or they'll stumble, and they'll just click the help button and go in and explain their problem.
[4932.98 → 4936.28] And often just explaining it to somebody and having somebody listen,
[4936.36 → 4937.38] even if you don't know the answer,
[4937.48 → 4939.84] you've helped them just by having them articulate their problem.
[4939.84 → 4940.96] Uh,
[4940.96 → 4941.62] and,
[4941.78 → 4942.06] uh,
[4942.06 → 4942.60] of course,
[4942.68 → 4943.80] if you have time,
[4943.80 → 4947.10] if you're a teacher, and you actually have,
[4947.10 → 4947.98] uh,
[4948.06 → 4949.26] a good presence and are,
[4949.36 → 4950.54] are good in front of the whiteboard,
[4950.62 → 4950.92] you could,
[4951.30 → 4951.70] you could,
[4951.80 → 4952.04] uh,
[4952.48 → 4955.58] help write some scripts and record some scripts of,
[4955.58 → 4958.06] that we could include in our theory curriculum.
[4958.90 → 4959.38] The
[4959.52 → 4964.74] another way you can help out is if you become part of the campsite nearest your city,
[4964.76 → 4966.76] which there's a good chance that there's one within,
[4966.76 → 4967.48] you know,
[4967.48 → 4970.78] a 30-minute drive or bus ride of where you live.
[4970.78 → 4972.56] If you want to take a
[4972.56 → 4972.64] uh,
[4972.64 → 4972.98] you know,
[4973.00 → 4977.66] a Thursday evening and go over to one of the coffee and code events and,
[4977.66 → 4981.50] and offer to help people out and just be there and be an example.
[4981.70 → 4982.14] If you're already,
[4982.14 → 4982.68] uh,
[4983.20 → 4984.40] an experienced software engineer,
[4984.66 → 4985.44] that would be wonderful.
[4985.44 → 4989.22] If you're an experienced teacher, and you just want to kind of help people
[4989.22 → 4992.36] understand by applying general teaching methods,
[4992.36 → 4993.76] help them,
[4993.76 → 4994.40] uh,
[4994.40 → 4994.94] understand,
[4994.94 → 4995.34] uh,
[4995.34 → 4996.66] concepts that they're struggling with,
[4996.66 → 4998.22] that would be wonderful.
[4998.22 → 4999.84] And I guarantee you,
[4999.84 → 5003.04] you'll meet a lot of interesting people, and they'll be extremely grateful.
[5004.40 → 5004.92] Fantastic.
[5005.24 → 5005.48] Well,
[5005.72 → 5006.16] obviously,
[5006.16 → 5006.86] as you know,
[5006.98 → 5007.40] listeners,
[5007.86 → 5008.40] uh,
[5008.44 → 5009.90] we have some awesome show notes.
[5010.12 → 5011.98] This is episode one 95.
[5011.98 → 5015.42] You can find those notes at changelaw.com slash,
[5015.64 → 5016.54] one nine five.
[5016.54 → 5018.56] Or if you're listening on a podcast app,
[5018.56 → 5022.88] just go ahead and find the show notes or link back to free code camp.com,
[5022.92 → 5023.62] which is the website.
[5023.62 → 5027.24] And I'm sure that there are lots of links and lots of navigation to the right
[5027.24 → 5029.06] kind of places that Quincy just mentioned.
[5029.06 → 5031.34] So follow links as needed,
[5031.34 → 5032.16] uh,
[5032.16 → 5033.92] to find your way to,
[5033.92 → 5034.26] uh,
[5034.26 → 5036.00] get her in other places you can chat with people.
[5036.00 → 5036.32] But,
[5036.32 → 5037.18] um,
[5037.50 → 5039.18] could this where we turn it back on you and,
[5039.18 → 5040.14] and figure out,
[5040.14 → 5041.08] uh,
[5041.12 → 5041.88] who you might,
[5042.10 → 5042.76] uh,
[5042.76 → 5043.78] I don't want to say idolize,
[5043.84 → 5046.88] but someone you look up to someone that's inspired you,
[5047.30 → 5048.04] impressed you,
[5048.04 → 5049.18] uh,
[5049.42 → 5050.32] motivated you.
[5050.32 → 5053.18] Who is someone you consider a programming hero?
[5054.18 → 5054.78] Well,
[5054.78 → 5055.64] there's a gentleman,
[5055.64 → 5060.38] I think in France who runs a community called LI chess.org.
[5060.70 → 5061.34] Uh,
[5061.34 → 5063.20] that's L as in Lima,
[5063.56 → 5065.48] I as in India chess,
[5065.70 → 5066.12] like the
[5066.12 → 5067.62] the game.org.
[5068.08 → 5071.28] And his name is Tybalt Duplesis.
[5071.78 → 5073.20] If I'm pronouncing that correctly,
[5073.22 → 5073.86] it's a French name.
[5074.30 → 5074.86] And,
[5074.90 → 5075.46] um,
[5075.46 → 5077.06] over the past couple of years,
[5077.18 → 5080.50] his open source project is basically,
[5080.50 → 5085.48] he's building this incredible chess platform where literally tens of
[5085.48 → 5088.82] thousands of people are playing chess at it every day.
[5088.82 → 5091.34] And he,
[5091.46 → 5094.74] the thing that's amazing about it is it's totally open source, and he's
[5094.74 → 5095.98] managed to build it.
[5096.10 → 5097.24] He's built all this infrastructure,
[5097.24 → 5099.22] I think using Scala and,
[5099.28 → 5099.80] um,
[5100.56 → 5106.24] he is able to do all of this for like $400 a month,
[5106.28 → 5107.00] which is sponsored,
[5107.00 → 5109.80] which is covered completely through donations from the community.
[5110.68 → 5110.96] And,
[5111.02 → 5111.40] uh,
[5111.72 → 5113.18] he doesn't even do it full-time.
[5113.24 → 5118.00] I think he has a day job, and he is already like LHS.org.
[5118.82 → 5122.50] It's already the second most popular place to play chess on the internet.
[5123.22 → 5126.22] And it's closing in on chess.com,
[5126.32 → 5126.68] which is,
[5126.76 → 5126.88] you know,
[5126.88 → 5127.72] the big corporate,
[5127.72 → 5128.88] you know,
[5129.06 → 5132.64] chess company that has banner ads everywhere and wants to charge you a ton of
[5132.64 → 5134.84] money in a recurring membership and everything.
[5135.50 → 5135.58] And,
[5135.58 → 5135.88] uh,
[5135.94 → 5136.16] you know,
[5136.22 → 5138.66] Tybalt's LI chess is free forever.
[5139.12 → 5139.24] He,
[5139.28 → 5140.54] he never wants to charge anybody.
[5140.66 → 5144.44] He just wanted to build an incredible platform because he's passionate about
[5144.44 → 5144.80] chess.
[5144.80 → 5147.30] You can watch him stream on Twitch and everything.
[5147.44 → 5147.58] I mean,
[5147.62 → 5153.14] I think he's so down to earth, and he so symbolizes everything that I personally,
[5153.40 → 5153.62] as a
[5153.62 → 5157.60] as a developer and an open source project maintainer want to,
[5157.60 → 5158.02] uh,
[5158.36 → 5159.12] want to go for.
[5160.14 → 5162.00] I see that this simplicity of,
[5162.06 → 5162.22] uh,
[5162.22 → 5162.40] I mean,
[5162.40 → 5165.00] obviously chess dot was a chess.com was the
[5165.08 → 5166.66] the bigger version.
[5166.76 → 5167.08] Yes.
[5167.16 → 5167.80] Of LHS.
[5168.64 → 5169.26] I mean,
[5169.36 → 5169.72] you know,
[5169.78 → 5172.30] whenever you go to a website, and you just plaster with ads and you,
[5172.42 → 5175.98] and you totally make it only about making money, and you don't make it about
[5175.98 → 5179.00] enriching the community that you're trying to serve.
[5179.78 → 5180.38] I mean,
[5180.80 → 5182.44] I just don't understand how anybody,
[5182.96 → 5183.98] even a company,
[5184.44 → 5187.18] how silly you must be to think that's a good model.
[5187.96 → 5189.04] You got to love people,
[5189.12 → 5189.46] right?
[5189.82 → 5189.96] Jerry,
[5189.96 → 5191.24] we said it when we went on,
[5191.32 → 5191.40] well,
[5191.40 → 5194.10] I said it when we went on a giant robot,
[5194.20 → 5195.44] smashing into other giant robots.
[5195.44 → 5196.32] And I,
[5196.32 → 5198.32] I don't remember saying it on the show,
[5198.38 → 5199.40] but you reminded me afterwards.
[5199.40 → 5199.82] I said,
[5199.86 → 5200.12] you know,
[5200.70 → 5201.04] uh,
[5201.10 → 5201.86] Ben Johnston said,
[5201.90 → 5202.16] you know,
[5202.62 → 5203.46] what are you trying to do,
[5203.58 → 5203.70] Adam?
[5203.70 → 5204.48] Or what are you guys trying to do?
[5204.50 → 5205.48] I forget the exact question.
[5205.52 → 5205.78] I'm like,
[5206.12 → 5206.94] you got to get in the trenches.
[5207.12 → 5207.40] You have to,
[5207.80 → 5208.26] you know,
[5208.26 → 5209.58] you have to love,
[5209.76 → 5211.68] buddy your knuckles and hug some people.
[5211.82 → 5211.90] Like,
[5211.92 → 5213.24] that's what you have to do to,
[5213.34 → 5219.70] to earn the love and respect of the people you're trying to actually serve is not treat them like,
[5219.70 → 5220.70] you know,
[5220.96 → 5221.90] piggy banks or something like that.
[5221.90 → 5222.40] I don't know.
[5222.62 → 5224.10] And treat them with respect,
[5224.10 → 5226.94] actually do something right and give back.
[5227.52 → 5229.08] I feel like that's what you're doing,
[5229.20 → 5229.42] Quincy.
[5229.46 → 5232.02] And I feel like that's what you kind of embodied in your,
[5232.08 → 5235.22] your respect for LHS and what he's doing at LHS.org.
[5235.78 → 5236.60] Correct me if I'm wrong.
[5237.12 → 5237.70] That's correct.
[5237.82 → 5238.84] LHS.org.
[5239.26 → 5240.10] I didn't mean the URL.
[5240.26 → 5240.72] I meant my,
[5240.72 → 5241.12] my,
[5241.12 → 5241.40] uh,
[5241.40 → 5242.04] pontification.
[5244.20 → 5244.60] Yeah.
[5244.76 → 5245.04] Oh,
[5245.12 → 5245.52] I,
[5245.74 → 5246.02] you know,
[5246.08 → 5247.74] that's certainly what I aspire to.
[5248.18 → 5248.50] Yeah.
[5248.50 → 5248.98] Sorry.
[5249.04 → 5250.08] I had to rant there for a second.
[5250.14 → 5251.22] You kind of inspired me.
[5251.42 → 5251.66] I,
[5251.66 → 5251.76] I,
[5251.76 → 5253.24] I wind up a go sometime.
[5253.42 → 5254.58] I didn't mean to do that,
[5254.58 → 5255.76] but anyway,
[5255.76 → 5256.90] we are definitely rambling.
[5256.98 → 5257.32] We're,
[5257.40 → 5258.80] we're definitely getting close to,
[5258.88 → 5259.84] we got two minutes left.
[5259.88 → 5260.26] Oh my,
[5260.38 → 5260.70] come on,
[5260.72 → 5260.98] come on.
[5260.98 → 5261.40] I'm just kidding.
[5261.50 → 5261.96] I'm just kidding.
[5262.22 → 5262.50] I'll,
[5262.50 → 5262.72] I'll,
[5262.72 → 5262.74] I'll,
[5262.74 → 5262.76] I'll,
[5262.76 → 5262.78] I'll,
[5262.78 → 5262.80] I'll,
[5262.80 → 5262.82] I'll,
[5262.82 → 5262.84] I'll,
[5262.84 → 5262.86] I'll,
[5262.86 → 5262.90] I'll,
[5262.90 → 5262.94] I'll,
[5262.94 → 5263.04] I'll,
[5263.04 → 5263.08] I'll,
[5263.08 → 5263.10] I'll,
[5263.10 → 5263.12] I'll,
[5263.12 → 5263.34] I'll,
[5263.34 → 5263.90] I'll,
[5263.90 → 5263.94] I'll,
[5263.94 → 5264.52] I'll,
[5264.52 → 5264.54] I'll,
[5264.54 → 5265.24] question or two.
[5265.66 → 5265.84] Well,
[5265.84 → 5267.56] we're going to punt on open source radar.
[5267.82 → 5268.36] We might,
[5268.58 → 5269.92] we might do that in the after dark,
[5270.20 → 5270.70] uh,
[5270.70 → 5272.20] and put that on sound cloud or something like that.
[5272.20 → 5274.22] We're going to put on that because we definitely are shorting on time.
[5274.82 → 5275.22] Um,
[5275.64 → 5275.82] yeah,
[5275.86 → 5276.34] I don't know.
[5276.36 → 5279.14] Is there anything else you want to add to this call before we tail off?
[5279.58 → 5279.98] Honestly,
[5280.48 → 5280.88] um,
[5281.06 → 5282.88] I'm a huge fan of the change log.
[5283.12 → 5283.48] I,
[5283.58 → 5284.08] uh,
[5284.08 → 5287.06] wrote about it on medium a few weeks ago.
[5287.06 → 5287.38] What?
[5287.66 → 5288.28] How do we not know?
[5288.96 → 5293.28] I included you go in my list of like five podcasts that every,
[5293.28 → 5293.72] uh,
[5293.72 → 5295.30] beginning programmer should listen to.
[5295.50 → 5295.58] And,
[5296.24 → 5296.64] um,
[5296.84 → 5297.10] you know,
[5297.16 → 5301.24] you all do so much for open source and,
[5301.38 → 5301.58] uh,
[5302.08 → 5305.86] and it's been a great resource for me to learn from other open source project
[5305.86 → 5306.46] maintainers.
[5306.46 → 5306.70] And,
[5306.80 → 5309.48] and I think you're a great vector for,
[5309.48 → 5310.16] uh,
[5310.40 → 5312.38] knowledge within the field.
[5313.10 → 5313.28] Wow.
[5313.56 → 5313.80] Wow.
[5313.86 → 5315.38] That's thank you so much.
[5315.74 → 5316.66] Didn't expect that.
[5316.84 → 5318.18] That's really appreciated.
[5318.44 → 5319.38] Almost makes me cry.
[5319.48 → 5320.22] I'm not even kidding.
[5320.30 → 5320.44] Yeah.
[5321.04 → 5321.60] I lost more.
[5321.72 → 5322.06] I'm just kidding.
[5323.12 → 5323.60] Well,
[5324.04 → 5324.30] you know,
[5324.32 → 5324.74] on that note,
[5324.78 → 5324.96] we,
[5325.20 → 5326.20] we just,
[5326.66 → 5327.04] uh,
[5327.28 → 5328.88] I think I said it kind of best,
[5329.00 → 5329.26] not,
[5329.36 → 5329.60] not,
[5329.70 → 5330.66] not intending to,
[5330.76 → 5332.28] but we try to get in the trenches.
[5332.84 → 5334.64] We try to bloody our uncles,
[5334.94 → 5335.22] you know,
[5335.50 → 5335.82] you know,
[5335.86 → 5338.02] do what needs to be done to get the work done.
[5338.02 → 5339.08] And we try to hug some people.
[5339.08 → 5340.80] We love open source.
[5340.88 → 5342.52] We love the people of open source.
[5342.82 → 5343.60] Doesn't matter,
[5343.60 → 5344.48] uh,
[5344.48 → 5345.52] what gender you are,
[5345.60 → 5346.38] what background you are.
[5346.42 → 5347.52] We care about everybody.
[5347.52 → 5349.20] And we want Jared and me,
[5349.24 → 5350.64] our mission is much like your mission.
[5350.64 → 5352.48] We want to enrich the lives of developers.
[5352.48 → 5353.66] That's our mission.
[5353.66 → 5353.92] Like,
[5353.98 → 5355.04] that's why we do this podcast.
[5355.04 → 5356.96] That's why we have people like you on.
[5357.02 → 5358.64] It's why we challenge you in some ways,
[5359.18 → 5359.52] you know,
[5359.56 → 5359.80] in,
[5359.86 → 5362.76] in respectful ways to move the ball forward,
[5363.04 → 5363.46] you know?
[5363.46 → 5363.92] And,
[5364.00 → 5365.74] and I think that more people should do that,
[5365.74 → 5366.78] but,
[5366.90 → 5367.30] uh,
[5367.38 → 5370.62] we are at the point where we have to tell off the call.
[5370.84 → 5376.50] So we have some upcoming awesome shows in the schedule up next.
[5377.24 → 5379.04] This is the third time I'm seeing this Tiddly Wiki.
[5379.20 → 5381.52] It's the funniest name to say for a Wiki.
[5381.60 → 5382.02] I love it,
[5382.06 → 5382.18] Jared.
[5382.24 → 5383.28] I can't wait to have Jeremy on,
[5383.36 → 5386.88] but Jeremy Huston is coming on to talk about this awesome Wiki called Tiddly Wiki.
[5387.24 → 5387.84] Wiki's man.
[5387.94 → 5388.58] There's like the
[5388.58 → 5391.32] the quintessential web is Wiki's right.
[5391.32 → 5393.26] And what Quincy said earlier,
[5393.26 → 5394.12] like Wikipedia,
[5394.66 → 5395.24] uh,
[5395.24 → 5396.16] build your own wikis.
[5396.38 → 5397.72] Lots of talk about there for sure.
[5397.90 → 5398.10] Yeah.
[5398.64 → 5400.76] And we have two big,
[5400.78 → 5401.26] and I mean,
[5401.36 → 5401.96] B.I.G.
[5402.48 → 5402.84] Capital,
[5402.98 → 5403.54] B.I.G.
[5404.14 → 5404.92] Upcoming shows,
[5405.06 → 5406.56] the future of WordPress and Calypso.
[5406.66 → 5406.80] We're,
[5406.84 → 5408.84] we're looking forward to that one with Matt Male.
[5409.20 → 5410.38] So that's coming up soon.
[5410.48 → 5411.20] Don't even know exactly.
[5411.30 → 5412.40] We got the date pinned down,
[5412.50 → 5412.70] but,
[5412.82 → 5413.06] uh,
[5413.32 → 5414.54] don't know what show number it's going to be.
[5414.84 → 5415.28] Uh,
[5415.34 → 5419.82] and we also have potentially for show number 200 for us,
[5420.46 → 5421.30] 20 years,
[5421.32 → 5423.74] of Ruby with Matt's,
[5423.88 → 5424.54] Matt's himself.
[5425.14 → 5426.84] So we're excited about that show.
[5426.94 → 5427.20] If you,
[5427.72 → 5428.02] uh,
[5428.02 → 5428.86] if you haven't yet,
[5428.92 → 5430.84] this is your first time listening to the change log,
[5430.96 → 5434.32] go to change law.com and find the subscribe button.
[5434.36 → 5435.22] It's really hard to find,
[5435.28 → 5436.36] but subscribe to the podcast.
[5436.46 → 5437.08] We're on iTunes,
[5437.32 → 5438.40] open up a podcast app,
[5438.46 → 5439.20] subscribe there.
[5439.72 → 5440.12] Uh,
[5440.12 → 5441.54] follow the emails we send out.
[5441.62 → 5442.98] Change law.com slash weekly.
[5443.42 → 5445.02] Change law.com slash nightly.
[5445.16 → 5447.28] Those are two awesome emails and follow us on Twitter.
[5447.88 → 5448.24] Uh,
[5448.32 → 5448.84] and,
[5448.94 → 5449.26] uh,
[5449.26 → 5450.18] yeah,
[5450.18 → 5450.50] that's,
[5450.58 → 5450.78] that's,
[5450.88 → 5451.76] that's the best way to,
[5451.84 → 5452.98] to kind of tail up one of the shows.
[5453.06 → 5454.18] We're excited about those shows.
[5454.72 → 5455.08] And,
[5455.12 → 5455.42] uh,
[5456.02 → 5456.30] let's see,
[5456.34 → 5459.48] we're thankful so much for all of your effort towards free code camp.
[5459.60 → 5461.28] We highly encourage,
[5461.28 → 5461.98] uh,
[5461.98 → 5462.66] the fight you're,
[5462.72 → 5465.58] you're fighting and whatever we can do to support you in the future.
[5465.58 → 5468.10] We want to do that for you and the listeners out there.
[5468.12 → 5470.96] We thank you for listening and to the members who support us as well.
[5471.04 → 5471.78] We love you.
[5471.80 → 5473.18] And we thank you for supporting us,
[5473.18 → 5473.50] but,
[5473.56 → 5473.80] uh,
[5474.08 → 5475.12] that's it for this show.
[5475.60 → 5475.92] So,
[5475.98 → 5476.16] uh,
[5476.16 → 5476.70] let's say goodbye.
[5477.62 → 5478.34] Bye everyone.
[5478.90 → 5479.20] Bye.
[5479.28 → 5479.48] Thanks,
[5479.54 → 5479.78] Quincy.
[5479.78 → 5480.78] Bye.
[5509.78 → 5510.32] Bye.
[5513.18 → 5514.00] Bye.
[5516.20 → 5518.18] Bye.
[5518.70 → 5520.64] Bye.
[5520.64 → 5522.70] Bye.
[5525.70 → 5525.74] Bye.
[5536.84 → 5537.24] Bye.
[5537.24 → 5537.90] Bye.
[5537.90 → 5538.84] Bye.
