[0.00 → 6.34] This is The Changelog.
[6.42 → 11.42] We're a member-supported blog and podcast that covers what's fresh and what's new in open source.
[11.94 → 15.42] The show is hosted by myself, Adam Stachowiak, and Andrew Thorpe.
[15.80 → 21.40] You can tune in live every Tuesday at 5 p.m. Central Standard Time right here on 5x5.
[21.52 → 25.80] And you can check out the past shows at 5x5.tv slash changelog.
[25.80 → 31.44] This is episode 88, and we're joined by Mitchell Hashimoto, the creator of Vagrant.
[31.72 → 32.32] Enjoy the show.
[37.40 → 38.60] All right, we're back, everybody.
[38.72 → 40.08] This is The Changelog.
[40.26 → 40.94] We're live.
[41.08 → 42.12] It's Tuesday.
[42.64 → 46.06] It's 5 o'clock here in the big old state of Texas.
[46.38 → 48.26] And Andrew, you're in Texas too, aren't you?
[48.58 → 49.04] Yes, sir.
[49.22 → 50.96] Normally you're not in Texas, though.
[51.44 → 51.62] Nope.
[51.62 → 56.98] Normally in Nashville, we give a shout-out to the Common Desk in Deep Vellum of Dallas.
[57.30 → 61.72] It's a nice little co-working space down here in Dallas.
[61.84 → 64.98] It's got a cool vibe, so you should definitely check it out if you're in town.
[65.68 → 70.10] And as you know, we take this show live every Tuesday at 3 p.m. Pacific, 6 p.m. Eastern.
[70.56 → 73.50] If you're on the East Coast there, just tune in.
[73.50 → 75.68] And thechangelog.com slash live.
[75.76 → 78.32] And for those of you who are listening live, we appreciate it.
[78.48 → 80.48] We've got a fun, fun show lined up today.
[80.58 → 83.50] It's actually a throwback to a guest.
[83.80 → 86.32] Andrew, do you know what the show was that Mitchell was on?
[86.44 → 87.22] What the show number was?
[87.40 → 89.88] I want to say 0.7.5.
[90.26 → 90.68] Is that right?
[90.78 → 91.26] Okay, good.
[91.32 → 93.52] So we've got Mitchell Hashimoto on the show.
[93.62 → 96.60] He is the creator of Vagrant and also the founder of HashiCorp.
[96.72 → 98.28] So, Mitchell, it's time to say hello.
[98.68 → 99.04] Hello.
[99.88 → 101.14] Glad to be here again.
[101.14 → 103.62] It was 0.7.2, by the way.
[103.94 → 104.76] I did a quick Google.
[105.12 → 105.38] Sorry.
[105.88 → 106.76] I don't care.
[107.04 → 108.62] I was just curious for myself.
[109.04 → 109.70] Get it right.
[111.26 → 122.18] Yeah, it was actually, we, when did the original show with you, that was November 27th last year, 2012, we did that show.
[123.32 → 125.62] Or no, sorry, I'm totally wrong.
[125.70 → 128.60] That was actually, man, I got my dates all messed up.
[128.66 → 130.20] That's the day you announced HashiCorp.
[130.20 → 130.60] HashiCorp.
[130.70 → 131.02] Aha.
[132.02 → 135.18] It looks like the show was February something.
[135.50 → 136.72] Yeah, February that year.
[136.96 → 137.78] And it was, yeah.
[138.06 → 138.36] Oops.
[138.52 → 139.42] Sorry about that.
[140.32 → 141.16] My bad.
[141.30 → 142.22] Amateur hour over here.
[142.78 → 143.02] Yeah.
[144.26 → 144.66] Jeez.
[144.92 → 145.14] Jeez.
[145.50 → 147.62] You know, it's been, it's just been a crazy day, man.
[147.80 → 148.92] You know, crazy day of pure charity.
[150.26 → 151.72] Crazy day of getting prepped for the show.
[151.80 → 152.34] A lot of stuff.
[152.46 → 153.34] A lot of stuff going on.
[153.36 → 154.16] So it's just been crazy.
[154.16 → 158.24] But Mitchell, enough about what we've been, what I've been doing all day.
[158.42 → 160.80] What, we're excited to have you back.
[160.88 → 163.18] I know, Andrew, you're excited about having him on the show.
[163.46 → 164.86] We're excited about HashiCorp.
[164.98 → 167.48] So we'd like to just like, you know, where do you want to dive in, Andrew?
[167.50 → 169.56] Do you have a particular area you want to just jump into?
[169.56 → 174.08] Well, I think first, Mitchell, if you just give us an update, like what's changed
[174.08 → 176.64] for you since going full-time at HashiCorp?
[176.92 → 179.54] Or I guess kind of start with the beginning.
[179.90 → 183.06] Like the last time we spoke to you was before your 1.0.
[183.34 → 184.74] So how did that go?
[185.80 → 188.66] So yeah, you spoke to me about a month before the 1.0.
[188.74 → 190.44] I think at that point, the 1.0 was actually done.
[190.52 → 193.10] I was working on blockers, like design and stuff.
[193.20 → 194.84] But the release went super well.
[194.84 → 201.82] So I was kind of surprised how many people wait until they see a 1.0 version to actually
[201.82 → 202.88] adopt some software.
[203.16 → 211.36] So after I just kind of upped the version to 1.0 and blessed it as such, the download numbers,
[211.62 → 213.46] like adoption, everything went way up.
[213.62 → 217.16] And I was unexpected how big of an impact that would make.
[217.22 → 217.74] So that's good.
[218.62 → 219.74] But it's been going well.
[219.78 → 220.72] It's been super stable.
[220.88 → 222.18] There's been some bug fix releases.
[222.18 → 226.42] But for the most part, they're pretty minor or really, really specific bugs.
[226.60 → 228.46] So I've been really happy about it.
[229.18 → 233.38] And maybe before we dive super deep in, we got a lot of new listeners and followers of
[233.38 → 233.98] the changelog.
[234.36 → 238.74] So for those who didn't catch the original show, give us just a quick breakdown of what
[238.74 → 239.34] Vagrant is.
[239.64 → 240.00] Sure.
[240.16 → 247.14] So what Vagrant is, is a command line tool that lets you manage virtual machines pretty
[247.14 → 248.98] much in a dead simple way.
[248.98 → 253.58] It automatically creates development environments, test environments for you.
[253.70 → 257.74] So if you're running on Windows, it'll automatically create you like a Linux virtual machine that
[257.74 → 261.02] has all the software you need installed in there to work.
[261.50 → 262.72] And that's pretty much it.
[263.40 → 268.22] And for those who listened to the last show with Jeff Atwood, he mentioned Vagrant.
[268.22 → 271.30] And that's how he does his environment.
[271.46 → 272.24] So he's on Windows.
[272.48 → 273.58] He just built Discourse.
[273.72 → 275.72] Discourse is an open source project built in Ruby.
[276.28 → 278.74] New to Jeff, aka Coding Hoarder.
[279.14 → 279.92] Coding Hoarder.
[280.02 → 280.84] I don't know why I said Hoarder.
[281.36 → 284.28] I have the TV show Hoarders on my brain for some reason.
[284.38 → 284.80] I don't know why.
[284.90 → 290.98] But that's how he does his virtual machines to run like a Linux box, I guess, to develop
[290.98 → 291.56] Ruby.
[291.92 → 292.32] Sweet.
[293.44 → 294.20] Pretty neat.
[294.62 → 295.10] Super neat.
[295.98 → 296.32] Flattered.
[297.16 → 297.58] Flattered.
[297.58 → 301.66] I read his blog when I was in high school.
[302.10 → 303.62] So that's crazy.
[304.36 → 304.58] Yeah.
[304.74 → 306.90] So that's probably been one of the craziest things for you.
[306.98 → 312.28] I mean, on the last time we had John, you were talking about some guys that were using
[312.28 → 313.72] your product.
[314.16 → 318.28] So since then, I mean, who else are you aware of that's been using it now?
[318.42 → 321.16] And what's it been like to see some of those big guys using it?
[323.08 → 323.88] A lot.
[324.14 → 325.76] I'm actually surprised on a date.
[325.76 → 326.90] Because it's open source.
[326.90 → 329.14] You know, they don't have to register or anything to get it.
[329.22 → 332.14] So I'm actually not aware always when people start using Vagrant.
[332.62 → 338.56] I think the biggest surprise to me was I was at a conference in L.A. scale Linux Expo.
[338.56 → 341.92] And I met this guy that worked at Disney.
[342.24 → 343.62] And he didn't recognize me.
[343.70 → 345.18] I'm not that sort of person.
[345.18 → 349.88] But then he saw the name and kind of put the pieces together and had this face that was like,
[349.94 → 351.26] holy shit, you're the Vagrant guy.
[351.30 → 351.98] We need to talk.
[352.72 → 353.98] And I was like, what?
[354.38 → 355.68] What do you know about Vagrant?
[355.68 → 357.28] He's like an ops guy at Disney.
[357.28 → 364.88] And he's like, oh, well, we have like 200 test machines running Vagrant tests, Vagrant machines like all day, 24 hours a day.
[364.88 → 365.82] And they're kind of melting.
[366.40 → 369.14] And I was just taking it back because I was like, what?
[369.52 → 375.08] You got up to like 200 machines running Vagrant automatically in a CI without ever talking to me?
[375.46 → 375.72] Yeah.
[375.72 → 377.90] Like, yeah, yeah, we definitely need to fix that.
[379.10 → 380.92] So that sort of thing happens all the time.
[381.12 → 383.26] And it's always surprising to me.
[383.82 → 387.24] Speaking of that, you need to get yourself a shirt that says, I'm the Vagrant guy.
[388.02 → 389.72] I think, I don't know.
[389.92 → 393.02] Whenever people call me the Vagrant guy, I'm never quite sure if it's a compliment or not.
[393.02 → 395.30] Because it's either like, you made Vagrant, so that's cool.
[395.44 → 400.10] Or it's like a subtle, like, dude, you're pretty dirty kind of jab.
[400.14 → 400.62] And I don't know.
[401.24 → 405.02] You mentioned Disney, but like on your homepage for Vagrant.
[405.02 → 408.18] So the homepage for Vagrant is vagrantup.com.
[408.78 → 409.04] Yes.
[409.04 → 411.20] And you got trusted by lots of cool brands on there.
[411.38 → 418.00] Everybody from Discus to the BBC and the I guess, lots of others.
[418.56 → 421.10] Mozilla, big influencers and open source as well.
[421.46 → 421.68] Yeah.
[421.68 → 423.22] Lots of cool people on there.
[423.66 → 427.46] Unfortunately, that list is tiny compared to how many I would like to put on there.
[428.42 → 429.96] But it is what it is.
[430.40 → 432.12] How do you normally hear from these people?
[432.30 → 434.22] How do you find out that these guys are using here?
[434.22 → 435.00] Are you using Vagrant?
[435.62 → 436.44] A few ways.
[436.64 → 437.68] Conferences are a big way.
[437.94 → 439.88] I talk to a lot of people at conferences.
[440.04 → 440.78] It's pretty social there.
[440.94 → 446.96] And then sometimes I'll just see a mailing list post or get a direct email from someone where I just notice their email address.
[447.02 → 449.44] You know, it's like at Expedia.com.
[449.44 → 451.76] And then I'm kind of, you know, piqued my interest.
[451.86 → 452.48] Like, why?
[452.68 → 453.20] Who are you?
[454.48 → 455.48] That's pretty much it.
[456.82 → 457.18] Gotcha.
[457.86 → 458.22] Cool.
[458.32 → 458.48] Yeah.
[458.54 → 463.24] I mean, it's really neat to see Vagrant, you know, growing so much.
[463.24 → 471.62] And this is kind of the beauty of open source is you see projects like this that just start to catch on and kind of catch fire and grow in the right direction.
[471.86 → 476.82] So obviously a lot has changed for you personally in the last year.
[477.46 → 477.60] Yes.
[477.60 → 479.18] What's your life like now?
[479.24 → 480.66] What's your daily life now?
[480.74 → 482.96] You're not going to the 9 to 5 or anymore?
[484.02 → 490.04] It's still pretty 9 to 5, but like seven days a week now and maybe some more hours at night.
[490.04 → 499.16] I'm probably working more than I did before, but now I'm working completely on Vagrant and Vagrant-related things, which is nice.
[499.20 → 499.74] And I like it.
[499.82 → 500.38] I enjoy it.
[500.76 → 503.08] So that's pretty much it.
[503.12 → 508.92] I guess the biggest lifestyle change is I could – I mean, I don't need to be at work, so I could be anywhere.
[509.24 → 513.94] And Google now currently thinks that I work at Disneyland because I go to Disneyland so much.
[513.94 → 527.20] I actually will sometimes take my bag and my Mini and go into Disneyland and just work at a café in Disneyland, which I think is pretty cool.
[527.50 → 531.22] I get some weird looks from families like, why is this guy on a laptop in Disneyland?
[532.22 → 534.76] Yeah, I did that with one of my previous employees.
[535.00 → 537.20] I did a lot of work down at Disney World in Florida.
[537.60 → 543.88] And I found this one little – it was like on this little pond, and it was this real old-fashioned hotel.
[544.04 → 549.14] But they had a really awesome outdoor bar area that I would go sit and work at and everyone would give me those dirty looks like.
[549.48 → 553.12] Who's this weirdo going to the Disney bar and bringing his laptop and sitting here for six hours?
[553.68 → 555.40] Yeah, I think it's – I don't know.
[555.46 → 558.56] I have an annual pass, so I just kind of just float in there when I can.
[559.24 → 559.60] Nice.
[559.90 → 564.62] So you mentioned how your life's changed, but how has Vagrant changed since the last time we talked to you?
[565.34 → 566.48] Vagrants changed a lot.
[566.48 → 569.12] So last time you talked to me was before 1.0.
[569.26 → 575.10] So 1.0 came out over a year past since then, and I released 1.1 and even 1.2.
[575.20 → 578.24] Basically, the way Vagrants changed is it's iterating a lot, lot faster.
[578.68 → 586.92] So there's been – since I've quit my job and started HashiCorp full-time, there's been something like six or seven Vagrant releases,
[587.80 → 592.28] a ton of VMware Fusion provider releases, AWS provider releases, stuff like that.
[592.28 → 597.98] So it's just like a lot of stuff is getting shipped that would have taken much longer if I couldn't do it full-time.
[599.04 → 605.84] You know, it's funny because I was saying HashiCorp and literally – and I'm going to out myself because I don't mind.
[606.02 → 606.94] This is how I am.
[607.32 → 614.36] I didn't connect the fact that your last name, Hashimoto, and HashiCorp were –
[614.36 → 616.18] I'm just slow, man.
[616.18 → 617.32] I'm really sorry about that.
[617.32 → 618.52] That's actually really common.
[618.68 → 619.16] I don't know.
[619.70 → 624.22] I mean I don't care, but I'm surprised a little bit by how many don't make the connection.
[624.76 → 627.80] Because I was – my next question was like, why did you name it HashiCorp?
[627.96 → 628.12] Yeah.
[628.26 → 629.26] It's not Hash.
[629.44 → 629.92] It's Hash.
[630.60 → 631.02] It's Hash.
[631.22 → 631.70] Yeah, Hash.
[631.84 → 632.26] HashiCorp.
[632.50 → 634.60] Did you just – you just figured that out, Stack, right there?
[635.16 → 636.00] I told you.
[636.10 → 637.42] I'm doing it on the air live.
[637.74 → 639.86] If you're listening right now, you can laugh.
[640.30 → 641.88] I'm just a little silly today.
[642.00 → 642.76] It's been a day.
[643.18 → 644.02] Shooting at the hit, man.
[644.02 → 647.44] But I don't mind telling you guys, and I'll admit it.
[647.90 → 649.20] I did that just now.
[649.74 → 655.62] So when we last spoke, we need to figure out something else to say rather than when we last spoke because we'll say that all.
[656.54 → 657.30] Since the last time.
[657.30 → 659.06] Since the last time.
[659.38 → 665.14] I remember Won would ask you about like do you miss the web development side of things?
[665.14 → 676.20] With the new HashiCorp, sorry, and with the Vagrant Up website and stuff, have you found yourself doing more of the web development of your company per se?
[676.96 → 678.54] Not at all, no.
[678.74 → 681.78] There's – I mean I built – no, not really.
[681.98 → 687.18] I made a web application to fill together like the VMware purchase flow.
[687.42 → 691.32] But for the most part, I was stitching together a bunch of services, so I didn't really code anything.
[691.32 → 698.10] No, and the website itself is static, and it's – no, I'm not really doing any web dev.
[698.92 → 699.40] Gotcha.
[699.54 → 702.54] So you've been obviously doing mostly DevOps still then.
[702.84 → 703.14] Have you –
[703.14 → 704.50] Mostly tool.
[705.06 → 707.60] Like I mean I've just been mostly working on Vagrant now.
[707.82 → 713.56] So I mean I don't really have any big ops responsibilities anymore or anything.
[713.80 → 715.54] So it's just building the tool.
[716.30 → 717.12] Yeah, I guess that's true.
[717.20 → 719.00] You're not really doing ops work technically.
[719.00 → 720.94] You're just supporting ops work now at this point.
[720.94 → 722.80] Yeah, and it's good and bad.
[723.14 → 735.82] Like it was nice to work at Keep before because as a full-time ops person, it kind of gave me a sandbox to try some of my crazy ideas and know how things are done and not done and stuff like that.
[735.90 → 740.84] And now I'm kind of like blind to what's going on in that world in a way.
[740.96 → 743.32] I mean I talk to people all the time about what's going on.
[743.32 → 747.32] But it's different not executing on it firsthand.
[748.84 → 748.92] Yeah.
[749.14 → 754.60] How do you find – I mean how do you find yourself now like solving the problems of – that you were solving in the ops world?
[754.82 → 761.22] Like if Vagrant has issues, and you don't have any real circumstances to deal with it, how do you get around that?
[763.12 → 763.68] It's hard.
[763.68 → 770.12] It's – well, so if there are issues, then I could easily recreate that environment usually to test the issue.
[770.36 → 776.38] The hard part is there are a lot of things in Vagrant that as I was working I would just find, you know, like usability things.
[776.44 → 782.32] Like it would be cool if Vagrant did this new thing and I would see a lot of value in that because I knew exactly the problem that it was solving.
[782.96 → 784.22] And I don't see that anymore.
[784.38 → 788.90] So if someone gives me a feature request that's like it would be cool if Vagrant did this, I might agree.
[789.02 → 789.82] Like that's cool.
[789.94 → 791.78] But I don't know how important that is.
[792.58 → 797.94] And it's hard to know how important that is now because I can't, you know, compare it to what I do on a day-to-day basis.
[798.64 → 801.60] And I think so far that's been okay because it's not been that long.
[801.60 → 804.22] It's been still only like six months since I quit my job.
[804.32 → 806.16] So I'm still like, you know, pretty relevant.
[806.16 → 815.00] But I think I could easily see how like if I keep doing this, you know, five years or something that I could definitely get out of touch and I don't want that to happen.
[815.72 → 816.16] Yeah.
[816.28 → 825.86] Originally, well, at least like you said, Andrew, the last time we had you on this show, you had actually said that people were suggesting to pay you for a feature.
[825.86 → 828.96] And it's just kind of funny how that's like how that's worked out.
[828.96 → 834.92] So we haven't we've mentioned HashiCorp, but we kind of haven't really mentioned how it got started.
[834.92 → 836.86] I think it's kind of funny to look in retrospect.
[837.06 → 842.30] That's why I was saying before the call that like on that previous show, it's kind of foreshadowing.
[842.52 → 846.88] You know, somebody saying, hey, I'll pay you for a feature is like, ah, makes sense.
[846.98 → 847.42] HashiCorp.
[848.42 → 848.94] You know?
[849.12 → 849.96] Yeah, it was.
[850.14 → 850.36] Yeah.
[850.44 → 855.72] I mean, when we last talked, I didn't I didn't know I was going to quit my job and start this thing.
[855.78 → 856.86] It was not known yet.
[856.98 → 859.34] So it's kind of neat how it worked out.
[859.34 → 868.42] One of the things that we've kind of talked about a lot since we relaunched the changelog has been open source, you know, sustainability and preventing.
[870.40 → 871.42] Stay excited about it.
[871.42 → 877.30] So with you, now that you've gone, you've gone corporate, you've sold out.
[877.84 → 878.48] I've sold out.
[878.84 → 885.40] And now that you've gone corporate, you've kind of got to handle the day to day, not the day to day, but just the business side of things.
[885.40 → 891.22] So how are you preventing burnout now with a product and running a business and doing all that stuff?
[893.56 → 893.92] Burnout?
[894.04 → 895.34] How am I preventing burnout?
[895.54 → 896.10] I don't know.
[896.26 → 900.10] I think it's, you know, it's always been something I love to do.
[900.20 → 901.60] I haven't burnt out in it.
[902.28 → 905.80] Even when I had a full-time job, I'd work on paranormals every night for like six hours.
[906.04 → 909.76] So I think burnout is not a concern at the moment.
[909.76 → 914.40] I take a lot of, I mean, I go to Disneyland a lot, so that's a good, that's a good part.
[914.48 → 916.28] That's a good medicine for that.
[916.36 → 919.54] But I'm not too concerned about that.
[919.64 → 922.12] But then the business side of things is harder.
[922.50 → 932.10] So, I mean, it's, it became very clear to me when I quit my job that I could support myself through, you know, consulting or building features or stuff like that.
[932.14 → 934.62] Like I could be very comfortable doing something like that.
[934.62 → 938.20] But at the same time, I'm not, I don't, I'm not a big services person.
[938.42 → 942.88] So the goal of HashiCorp is actually to build it into like a product company.
[943.08 → 945.48] It's at, hopefully this year, you'll see something this year.
[945.98 → 947.24] And that's what I'm working towards.
[947.34 → 951.58] So like it's, you can't really see what the business of HashiCorp is going to be.
[951.66 → 955.58] And I'm not sure, you know, you can't say if it's going to be successful or not because I don't know yet.
[956.38 → 958.62] But I'm avoiding services if I can.
[958.96 → 964.04] Well, now you, you kind of teased it, but you can't leave us like that.
[964.04 → 967.92] So are you saying that there will be other products that HashiCorp will?
[970.02 → 970.50] Yes.
[970.72 → 974.74] So I've, so I released Vagrant 1.2.2 or something.
[975.00 → 984.04] And ever since that release, I've pretty much been focusing completely on a new project that should be out in the next couple of months that I think will solve another problem.
[984.92 → 991.36] And what I'm trying to do with HashiCorp is basically build the best DevOps tools I can and solve problems I can.
[991.36 → 996.44] And then I see a bunch of problems still from when I worked in it full-time that I want to make better.
[996.64 → 1000.80] And I think I can make it better by building multiple tools that work really well together.
[1001.06 → 1001.96] So that's what I'm trying to do.
[1002.92 → 1003.00] Gotcha.
[1003.18 → 1006.46] So you can't tease us on the name or the idea at all?
[1007.12 → 1009.20] The name of the new thing is Packer.
[1009.44 → 1011.42] But you could try to figure out what that does on its own.
[1011.42 → 1013.46] So I don't know.
[1013.88 → 1014.40] Thanks.
[1016.68 → 1017.62] No, that's cool, man.
[1017.66 → 1019.90] It's really cool to see a product evolve.
[1020.16 → 1025.56] So a simple product that was built to solve a need evolve into essentially a corporation.
[1025.70 → 1027.90] It's cool to kind of watch this thing unfolds before our eyes.
[1027.90 → 1033.08] Speaking of that, I just like where your roots start from, Mitchell.
[1033.60 → 1042.18] At least on your about page, you said, I started building Vagrant in my college dorm room in 2010 as an attempt to solve a specific problem I had.
[1042.20 → 1044.14] I was kind of curious what that specific problem was.
[1044.28 → 1051.12] But just leaning on what you just said, Andrew, to see where you're at now, considering where you came from, and that journey in between is pretty neat.
[1051.12 → 1053.26] Yeah, yeah.
[1053.68 → 1057.84] I mean, the specific problem was just I worked for a consultancy.
[1057.98 → 1063.22] So I was like one developer of many, and I was seeing a lot of new clients every six weeks or so.
[1063.28 → 1070.26] And it was just a huge pain in the butt after working there for three years to keep setting up my laptop with new stuff every six weeks.
[1070.68 → 1078.12] So I reached a tipping point where I was so frustrated that I needed to find a solution to this because I couldn't handle it anymore.
[1078.12 → 1080.88] And I didn't know if the Vagrant idea would work.
[1081.02 → 1085.64] It definitely wasn't called Vagrant then, but it was just like this virtualization idea I had, and I tried it.
[1085.96 → 1091.56] And it seemed to work okay, and I'm glad over the long term it's shown to be very effective.
[1093.08 → 1094.18] Where'd you come up with the name at?
[1095.12 → 1098.22] You said V, so you didn't know it was going to be called Vagrant.
[1098.50 → 1100.74] But it's virtualization of some sort, right?
[1100.84 → 1103.16] So is that like a have to have?
[1103.26 → 1104.66] No, no, it's really not, actually.
[1104.72 → 1105.46] I didn't come up with the name.
[1105.46 → 1110.90] John Bender, who made 0.1 with me, he came up with the name.
[1111.56 → 1116.44] I was actually notoriously bad in 2010 with coming up with names somehow.
[1116.88 → 1120.48] So every name I come up with, he was like, that's terrible.
[1120.58 → 1121.72] He was just very honest with me.
[1121.92 → 1123.86] And now when I look back, I—
[1123.86 → 1125.58] You can't say that without sharing some with us.
[1125.74 → 1127.12] What are some of the bad names?
[1127.36 → 1128.90] Okay, let's see.
[1129.22 → 1131.36] One of the first names I had was Box cutter.
[1132.04 → 1132.78] That wasn't good.
[1132.78 → 1133.42] Yeah.
[1133.98 → 1135.00] No, it's not good.
[1135.64 → 1136.04] Hobo.
[1136.16 → 1137.30] It's close to boxing, though.
[1137.36 → 1138.98] I mean, you were so close.
[1139.22 → 1142.32] Box cutter sounds like it came from maybe like Gem cutter kind of idea.
[1142.86 → 1143.08] Yeah.
[1143.08 → 1143.34] Yeah.
[1143.48 → 1145.94] And then I had Hobo for a while.
[1146.08 → 1147.58] That's pretty politically not correct.
[1147.88 → 1148.54] So there's that.
[1150.54 → 1151.06] Oh, man.
[1151.16 → 1157.16] Every week we have another politically incorrect topic on this show, it seems like.
[1157.54 → 1157.92] Yeah.
[1158.20 → 1159.12] This week's Hobo.
[1159.86 → 1161.58] Yeah, so that's it.
[1161.66 → 1164.66] And then John Bender came up with Vagrant, and that stuck.
[1164.82 → 1165.40] It's a very good name.
[1165.98 → 1167.00] That is a good name.
[1167.04 → 1167.64] Good name, John.
[1167.80 → 1168.62] Good job, John.
[1168.68 → 1169.08] Thank you.
[1169.74 → 1174.18] So one of the things that seems like it's changed, obviously, is the original you only
[1174.18 → 1176.50] had support for Oracle's VirtualBox.
[1176.92 → 1177.14] Mm-hmm.
[1177.14 → 1178.44] And it seems like that may have changed.
[1179.12 → 1179.46] Yep.
[1179.46 → 1184.56] So what else are you supporting, and what has that done for you?
[1184.94 → 1185.24] Yeah.
[1185.34 → 1189.16] So officially, I support VMware as well.
[1189.16 → 1193.30] And I have a personal open source project to support AWS.
[1194.36 → 1197.02] But the VMware one has official email support and stuff.
[1197.02 → 1202.26] But as you said, Vagrant now works with anything, not just VirtualBox.
[1202.42 → 1203.88] And it's a complete plug-in interface.
[1204.00 → 1206.36] So it could actually work with anything out there.
[1207.16 → 1212.34] And it's changed things because there are a lot of use cases that people had for Vagrant
[1212.34 → 1217.74] that they couldn't actually do because VirtualBox wasn't the correct answer for it.
[1217.74 → 1223.70] So, for example, people wanted to use Vagrant to test their ops stuff in a CI.
[1223.96 → 1228.00] Like, they pushed, for example, Chef Cookbooks, and they wanted to run Vagrant up and make
[1228.00 → 1230.12] sure that it ran properly.
[1230.42 → 1232.90] And you need a new machine to kind of try new Chef stuff.
[1233.08 → 1234.48] So they wanted to do that.
[1234.54 → 1237.74] But VirtualBox has terrible parallelism.
[1238.50 → 1242.36] So if you run, like, more than one VirtualBox machine at a time, it gets unhappy.
[1242.36 → 1249.52] And, yeah, so now, like, with the provider stuff, they could use whatever's best for them.
[1249.58 → 1253.36] So if they're in AWS, maybe they'll use an AWS provider that spins up new EC2 instances.
[1253.74 → 1258.64] If they're in dedicated hardware, maybe they'll use the VMware one, which has much better parallelization.
[1258.80 → 1260.64] You know, they could choose what's best for them.
[1260.70 → 1261.90] And that's really neat.
[1261.98 → 1265.48] And it's still so new that new use cases are coming out all the time.
[1265.52 → 1267.26] So I'm not quite sure where this is going to go.
[1267.76 → 1270.52] But it was very clear to me that it was the right move to make.
[1271.36 → 1271.76] Gotcha.
[1271.76 → 1276.34] So your project is the Vagrant AWS is the open source one that you have for.
[1276.98 → 1277.20] Yeah.
[1277.80 → 1281.12] Yeah, I started Vagrant AWS and the Rackspace one, too.
[1281.38 → 1286.82] And I kind of did that as to have an open source one that people could see how to build one of these things
[1286.82 → 1288.38] because the VMware one's closed source.
[1288.50 → 1291.16] So I didn't want to just come out with the VMware one and say,
[1291.26 → 1292.98] well, if you want to build your own, you got to figure it out.
[1293.10 → 1295.00] Like, I came to the AWS one.
[1295.14 → 1299.36] So then I could point people at various points like, oh, here's how you do this.
[1299.40 → 1300.14] And here's how you do this.
[1300.44 → 1300.84] Gotcha.
[1300.84 → 1307.82] So have you seen any other, I don't know, plugins that have come out that have been popular that other people have developed?
[1310.30 → 1311.74] Provider-wise, there are some cool ones.
[1311.98 → 1315.82] So there's an LXC one that's very good, Vagrant LXC.
[1316.06 → 1319.56] But, I mean, there's like a new provider every week, and it's been awesome to watch that happen.
[1319.56 → 1321.54] So there's like joint ones.
[1322.62 → 1323.74] What else is there?
[1326.62 → 1327.02] KVM.
[1329.18 → 1330.62] I'm blinking, but there's a lot.
[1331.02 → 1331.24] Yeah.
[1331.32 → 1332.28] There's a lot more than I'm saying.
[1332.28 → 1335.28] So it's not just the product itself that's growing.
[1335.42 → 1337.32] It's this whole ecosystem around it that's growing.
[1337.42 → 1339.64] It must be fun to kind of watch that happen around you.
[1340.10 → 1340.84] Yeah, it's perfect.
[1340.88 → 1345.32] It makes me feel good because that's what makes it hum pretty much.
[1345.32 → 1351.14] So when you were building the plugin system in Vagrant, were you – kind of in what order did you go?
[1351.30 → 1354.90] Like did you build out the idea and then build Vagrant AWS?
[1355.28 → 1357.42] Or I guess you said VMware was the first one.
[1357.70 → 1359.64] So kind of what it sounds like.
[1359.64 → 1367.24] So between 1.0 and 1.1, the plugin – 1.0 had plugins, but there was no real plugin system.
[1367.56 → 1370.58] It was just like run your own Ruby code inside Vagrant.
[1371.50 → 1373.02] And it was kind of messy.
[1373.28 → 1379.68] But Vagrant 1.1 had a whole new plugin system, and I knew one of the things I wanted to support was providers.
[1379.68 → 1390.22] So I wrote the VMware provider alongside the plugin system because I believe that the best way to test like an API is to dog food it and use it yourself.
[1390.72 → 1396.34] And so I built it while I was building the plugin system, and that's kind of what guided how it works today.
[1397.26 → 1398.48] I dog food it.
[1398.86 → 1399.30] That's nice.
[1399.54 → 1399.94] Dog food it.
[1400.06 → 1401.14] And actually, this is really cool.
[1401.20 → 1406.80] A lot of people don't know this unless you look at the Vagrant source, but Vagrant is actually built on its own plugin.
[1406.80 → 1411.30] So like when you're on Vagrant up, the up command is actually a plugin that is running.
[1411.98 → 1415.20] So everything is a plugin in Vagrant pretty much today.
[1415.92 → 1416.36] Cool.
[1416.94 → 1419.86] So on the last episode, we talked about WWI.
[1420.52 → 1420.82] Yes.
[1420.82 → 1422.82] It looks like WWI is still in active development.
[1423.34 → 1423.58] Yes.
[1423.58 → 1429.02] So what's kind of changed there, and have they kept up with you in a lot of ways?
[1430.00 → 1435.18] WWI has changed a little bit, and not for bad or not negatively,
[1435.18 → 1442.82] but it's changed in a way that it was originally Patrick's idea to build WWI as a way to build Vagrant boxes,
[1443.34 → 1445.92] and that's what it launched with, and it is awesome.
[1446.62 → 1450.88] And since then, people have wanted to build other kind of machine images,
[1451.20 → 1454.98] so now it supports like KVM and Fusion and all sorts of things,
[1455.16 → 1459.08] and it kind of lost its tie to Vagrant, and so it's kind of gone off on its own.
[1459.08 → 1462.94] So it doesn't work anymore, I don't think, as a Vagrant plugin by design.
[1462.94 → 1469.50] It stands as its own product now, and yeah, they're doing their own thing over there and keeping it going.
[1471.30 → 1472.40] Gotcha. Gotcha.
[1472.52 → 1476.60] So we're just kind of like lightning round through some of these questions.
[1476.60 → 1476.90] I know.
[1476.90 → 1477.22] It's kind of cool.
[1477.62 → 1478.18] I got a question.
[1479.22 → 1479.62] Yes.
[1479.84 → 1480.32] Go ahead, call it.
[1480.82 → 1482.94] I'm going to go first-time call, a long-time listener here.
[1482.94 → 1485.92] I'm just kind of curious.
[1486.22 → 1490.22] So for – I mean it's kind of easy to step into this conversation,
[1490.50 → 1495.70] but for some who may be like kind of brand new to this idea of Vagrant and what it offers and all that,
[1495.76 → 1498.50] they hear things like Puppet, Chef, and then they also hear Vagrant.
[1498.68 → 1500.80] They hear – now they hear Docker as well.
[1501.24 → 1507.98] How does one choose – I guess now that you have HashiCorp, and you're building commercial add-ons and supporting it,
[1507.98 → 1514.48] there's lots of stuff you're doing there, but how does one choose between these different options that they have to virtualize
[1514.48 → 1515.80] or to automate and stuff like that?
[1516.44 → 1517.20] It's tough.
[1517.38 → 1522.18] It's really tough out there because it's – to me, it seems like – yeah, like you said,
[1522.22 → 1524.30] there are just a lot of names that don't really mean anything.
[1524.30 → 1528.56] Like you don't tell anyone Vagrant, and they don't know of the bat what that means.
[1528.80 → 1529.58] It doesn't mean anything.
[1529.80 → 1536.16] So it's hard to know like what tool to use and what it's even going to do and if it's a problem you have until you have it,
[1536.16 → 1543.28] stuff like that, if you're just getting into ops today, I mean I think the best way is still to –
[1543.28 → 1548.02] I think Vagrant is one of the best ways to get into it because it allows you to basically have a free disposable server
[1548.02 → 1552.38] on your own machine, and then you could really just screw that up as much as you can.
[1553.32 → 1553.68] Nice.
[1554.02 → 1555.78] And so I usually recommend –
[1555.78 → 1556.64] Learn by doing, right?
[1556.78 → 1557.02] Yeah.
[1557.22 → 1560.68] So whenever people come to it, I usually recommend they get Vagrant.
[1560.68 → 1566.84] They just manually do things for a long time and then – long time being set up a project manually.
[1567.40 → 1571.66] And then when they're comfortable with Vagrant so that they're not trying to learn multiple things at one time,
[1571.94 → 1574.56] then they pick up Chef or Puppet or choose whatever they want.
[1574.90 → 1576.76] I always say Chef or Puppet, it doesn't matter.
[1576.86 → 1580.04] Just choose which one you connect more with.
[1580.76 → 1580.88] Yeah.
[1581.04 → 1587.40] So with Chef and Puppet, I think on the last episode you were saying that you didn't really have a preference between the two.
[1587.40 → 1588.60] Has that changed?
[1588.70 → 1590.58] Do you recommend one over the other anymore?
[1591.12 → 1591.36] No.
[1591.66 → 1591.98] No.
[1592.36 → 1597.30] I spoke at Chevron like last week, and I'm going to be probably speaking at PuppetConf this year.
[1597.76 → 1600.60] So I'm still Switzerland on that front.
[1601.94 → 1602.20] Gotcha.
[1603.64 → 1604.32] It's cool.
[1604.50 → 1607.40] So now your project is sponsored.
[1608.10 → 1610.46] I see a few of your sponsors are Type kit and Vastly.
[1611.22 → 1614.04] What does that look like for you on the business side?
[1614.04 → 1621.92] You don't get to get too much into any of the details, but are these mostly financial contributors or guys that actually jump in and help you with the code?
[1622.22 → 1624.34] What is the relationship like between you and them?
[1624.86 → 1625.06] Yeah.
[1625.20 → 1630.04] So I'm actually really happy you asked because it's really not clear on that thing and I should make it clear.
[1630.20 → 1636.14] But those sponsors are only people who help the org side of things, which is like the open source side of things.
[1636.32 → 1639.82] I don't – from a business perspective, I don't take anything from them.
[1639.82 → 1646.82] So Vastly, for example, provides the CDN service for vagrantup.com, the docs, stuff like that.
[1648.82 → 1653.04] Type kit, I mean all the fonts on the website are rendered from Type kit web fonts.
[1653.32 → 1656.04] Soft layer gives me some free servers for public testing.
[1656.26 → 1657.34] Like I can't use them privately.
[1657.34 → 1666.90] And Keep is my last employer, and they host all the S3 costs for the public boxes, which are a lot of money.
[1667.10 → 1671.88] So it all helps, but it's all the public stuff and I want to make it clear that that's what it is.
[1672.20 → 1677.34] I specifically didn't want any sponsorships for business stuff because I think that's a little questionable.
[1678.18 → 1678.34] Yeah.
[1678.62 → 1678.92] Gotcha.
[1679.06 → 1679.40] Absolutely.
[1679.40 → 1687.76] So when you left Keep to do this full-time, did they kind of – not see it coming, but did they kind of know that that was on the horizon?
[1688.36 → 1688.64] Yeah.
[1688.74 → 1694.34] When I sat down with my boss in the room and told him, he kind of asked me why I didn't do it sooner.
[1694.64 → 1700.14] He thought I was going to leave like in March of last year and I left in November, so way later.
[1700.66 → 1701.96] And he was all for it.
[1702.00 → 1703.18] He's very supportive.
[1703.18 → 1705.96] And I'm actually recording this from the Keep offices.
[1706.28 → 1708.70] They still let me come in here whenever I want.
[1709.06 → 1709.68] Very friendly.
[1709.86 → 1710.72] So Keep is in Disneyland.
[1711.02 → 1711.50] That's awesome.
[1712.38 → 1712.58] Yeah.
[1712.84 → 1713.02] Yeah.
[1713.18 → 1714.00] Keep in Disneyland.
[1716.36 → 1716.88] Cool.
[1717.76 → 1718.14] Yeah.
[1719.42 → 1724.46] So in the last show, you mentioned being a fan of ROC.
[1724.52 → 1730.00] And since we're talking a little tiny bit about HashiCorp, did you happen to get inspired?
[1730.00 → 1737.46] Because I'm really curious about this open source turned profitability, turned into corporation and long-term business plan product company.
[1737.70 → 1737.78] Yep.
[1737.84 → 1739.50] I'm kind of curious about this shift.
[1739.68 → 1743.10] But in the last show, you mentioned being a fan of ROC.
[1743.14 → 1747.40] And for those who are tuning in, ROC is essentially a database.
[1747.86 → 1752.18] You get into this NoSQL, No MySQL stuff.
[1752.28 → 1753.32] That's basically ROC.
[1753.38 → 1755.78] But they're a paid version, I guess.
[1755.92 → 1756.28] They do.
[1756.46 → 1758.56] It's open source, but they also have a paid component to it.
[1758.56 → 1761.92] And so you mentioned being inspired or being a fan of them.
[1761.98 → 1768.64] Were you inspired by them when thinking of HashiCorp and Vagrant and the direction you were going to take?
[1770.52 → 1770.92] No.
[1771.80 → 1772.20] No?
[1772.20 → 1772.60] No.
[1772.76 → 1774.96] I like the way they're doing things.
[1775.56 → 1776.92] But it's just one option.
[1777.20 → 1780.14] And I'm not sure if I'm going to follow that option.
[1780.14 → 1782.96] So I'm good friends with them.
[1783.14 → 1787.12] But I wouldn't say they're inspiring certain decisions I'm making.
[1787.32 → 1792.08] I'm definitely trying to learn as much as I can from companies like Basho, who makes ROC.
[1792.40 → 1792.60] Right.
[1792.60 → 1797.26] But I'm not trying to follow in the footsteps currently of any specifically.
[1797.44 → 1802.74] I'm just trying to understand what the options are out there to make this into a business.
[1802.92 → 1804.06] And I think I have a good grasp now.
[1805.40 → 1805.52] Yeah.
[1805.66 → 1812.64] So do you plan on, like, will Vagrant always be how Vagrant is now, like a free product that you can use?
[1812.68 → 1816.18] And then other products will be where you would sell and do things like that?
[1816.18 → 1816.46] Yeah.
[1817.22 → 1819.28] So my, I mean, I'm happy to talk about that.
[1819.66 → 1828.32] What I want to do is basically build a set of open source tools that stand on their own, are totally free, liberally licensed, like awesome tools.
[1828.70 → 1839.86] And then build kind of, you know, like a layer on top to integrate them and present it maybe in a more user-friendly way, like less command lining, more UI focused, stuff like that.
[1839.88 → 1842.42] And charge for that layer rather than the tools themselves.
[1842.42 → 1848.04] So I know that Vagrant is, Vagrant, I'm charging for the VMware stuff.
[1848.32 → 1854.66] And honestly, long term, I want to make the VMware stuff free and open source too because that's not my business plan.
[1854.84 → 1860.72] I only charge for it because I think it's fair because VMware costs money to begin with, and it supports me.
[1861.36 → 1862.40] And that was pretty much it.
[1862.44 → 1865.56] It gave me the runway to work on my own without pressure.
[1865.56 → 1878.46] So with that in mind, I'm basically building out these other open source tools, going to release them, going to love them, going to liberally, you know, license them, and then build in this proprietary layer on top of it.
[1878.58 → 1887.08] But the nice thing is, since it'll be built on top of open source tools, if you get tired, or you don't like what I'm doing there, you could always like to leave it and work with the tools yourself.
[1890.78 → 1892.12] I'm not sure if we lost Andrew.
[1892.18 → 1892.86] Maybe he's gone.
[1893.62 → 1894.56] We do have a...
[1894.56 → 1895.34] I think we did.
[1895.86 → 1896.62] Yeah, I think we might have.
[1896.70 → 1898.16] He'll come back in a second, so I'll pick up.
[1898.22 → 1902.54] I wasn't going to stomp on his toes if he had some good questions to ask there.
[1902.64 → 1906.44] But it seems like you might know a guest in our IRC chat room.
[1906.52 → 1910.00] So for those listening on the podcast feed, you can't listen to the show live.
[1910.04 → 1911.34] We do broadcast every Tuesday.
[1912.28 → 1915.56] And right now, I'm saying this live to some people that are listening.
[1915.56 → 1917.40] But we also run an IRC chat room.
[1917.56 → 1921.26] So when we have people like Mitchell on the show, you can hop in and ask questions.
[1921.26 → 1927.46] And in regard to that, we have K776 underscore, which is an awesome, awesome username.
[1927.58 → 1936.94] He says, is Packer being designed as a self-contained app, solves a different problem in parentheses, or a complement of Vagrant, used for better experience?
[1936.94 → 1937.98] Good question.
[1938.52 → 1941.28] So everything I'm working on are self-contained.
[1941.76 → 1945.08] Each thing I'm working on should stand on its own as a very useful thing.
[1945.22 → 1947.16] They're solving very specific problems.
[1947.16 → 1956.64] But at the same time, they're going to integrate super well with each other, being that they're made by the same mind on top of it.
[1956.92 → 1959.04] So Packer will be on its own.
[1959.18 → 1960.90] And I think a lot of people will use it without Vagrant.
[1961.34 → 1968.24] I spent a long time at Chevron last week talking to people, seeing if the problem Packer solves is a problem people have.
[1968.30 → 1969.72] And 100% of people want it.
[1970.24 → 1972.42] So once it's out, I think they'll adopt it.
[1972.50 → 1974.50] And whether they're using Vagrant or not doesn't matter.
[1974.84 → 1976.82] But it'll complement Vagrant as well.
[1976.82 → 1980.82] So do you have a release?
[1980.98 → 1981.56] Welcome back.
[1981.96 → 1982.60] Yeah, I'm back.
[1982.80 → 1984.82] I was trying to sneak in there all the time.
[1985.60 → 1987.02] Yeah, you can't sneak past me.
[1987.20 → 1987.62] I know.
[1987.78 → 1988.06] Sorry.
[1988.76 → 1990.88] So do you have a release date in mind for Packer?
[1991.00 → 1991.82] You may have already said it.
[1993.72 → 1996.22] Not release date, but let's say release month.
[1996.22 → 1998.88] My personal goal is June.
[2000.06 → 2001.60] It's hard now.
[2001.70 → 2005.82] It's harder for me now in a way because there's a lot more personal pressure I put on myself.
[2005.82 → 2014.46] Because I think that when I release Vagrant, I think if I release Vagrant now, it wouldn't have succeeded as well.
[2014.60 → 2019.60] Because people kind of expect a higher level of quality out of what I push out.
[2020.16 → 2022.22] And so I'm working.
[2022.22 → 2026.54] I think three or four years ago, I probably would already release Packer.
[2026.68 → 2027.84] Like it's in a working state.
[2028.48 → 2032.78] But I'm spending a lot more time polishing it, getting air handling down, stuff like that.
[2034.30 → 2038.48] And I think the result will be much stabler, but it sucks because people have to wait longer.
[2038.48 → 2039.48] Gotcha.
[2040.98 → 2045.20] I think we're actually being visited by John Bender in the IRC chat room right now.
[2045.22 → 2045.80] Yeah, yeah, yeah.
[2046.46 → 2047.54] Speaking of John.
[2047.72 → 2049.10] The John Bender.
[2050.16 → 2050.92] John Bender.
[2051.12 → 2052.54] He's a vagrant neighbour himself.
[2052.76 → 2053.58] He's soon going to be.
[2054.00 → 2058.04] So Kyran asked another question, which is what John's doing.
[2058.04 → 2061.18] But John is soon to be Dr. Bender.
[2061.66 → 2062.26] Not soon.
[2062.42 → 2064.86] He has a few years or some years down the road.
[2064.96 → 2071.06] But he's starting a PhD program and doing crazy programming math.
[2071.46 → 2074.02] Isn't Dr. Bender the guy on Fukuyama?
[2074.22 → 2075.22] Or no, Bender's the robot.
[2075.48 → 2076.30] Bender's the robot, yeah.
[2076.56 → 2077.12] Yeah, my bad.
[2077.34 → 2078.26] Sorry, rookie mistake.
[2079.38 → 2081.54] But yeah, so John actually left.
[2082.22 → 2082.82] Not left.
[2082.88 → 2085.98] He's always used Vagrant and been a huge fan of Vagrant.
[2085.98 → 2090.60] But he, I'm laughing at what he's saying.
[2090.92 → 2096.68] But he left the project kind of, I don't know, last two years ago or a year and a half ago sometime.
[2096.92 → 2101.02] And he was a full-time, is a full-time committer on jQuery Mobile.
[2101.28 → 2104.30] So he went the front-end route, whereas I went the ops route.
[2105.02 → 2106.66] But we've always talked like every day.
[2107.10 → 2109.82] And he's a big, he gives a lot of feedback to the project.
[2110.06 → 2111.50] And like I said, a big evangelist.
[2112.42 → 2113.16] And yeah.
[2113.92 → 2114.32] Gotcha.
[2114.32 → 2118.92] So John was kind of the driving force behind the Windows side of things, right?
[2119.34 → 2120.06] Yeah, yeah.
[2120.32 → 2121.06] What's that like now?
[2121.84 → 2123.58] What's Windows support looking like?
[2123.62 → 2125.80] And is John still active in that area?
[2127.24 → 2135.68] So John was the one who, John was the one who made me, like he made the original Windows support and pushed me towards supporting Windows.
[2135.76 → 2136.90] I didn't think it was that important.
[2136.90 → 2140.00] But he was pretty serious about it.
[2140.08 → 2141.18] So he made the first support.
[2141.42 → 2145.14] And since then, like the latest release supports Windows really, really well.
[2145.54 → 2150.08] It works in basically any shell environment that exists on Windows because there are many different ones.
[2150.58 → 2152.50] And it just works super well.
[2153.06 → 2159.84] And John had incredible foresight there because now if you look at the download numbers, they aren't public.
[2159.84 → 2165.06] But if you look at the download numbers, the total number of users are actually two to one Windows to Mac.
[2165.54 → 2166.36] And then there's Linux.
[2166.78 → 2170.00] So a lot of people on Vagrant and Windows.
[2170.76 → 2172.34] That probably has to do with Disney.
[2173.80 → 2174.62] I don't know.
[2175.22 → 2176.54] I think, yeah, I don't know.
[2176.62 → 2179.02] It's kind of interesting because I've met a lot of people who are really smart.
[2179.02 → 2186.06] And they like Windows, but they prefer a Linux dev environment, but they prefer a Windows like desktop environment.
[2186.88 → 2188.14] And now you can have both.
[2188.60 → 2189.26] That's pretty cool.
[2190.20 → 2194.80] It looks like 1.1 was the VMware Fusion release.
[2195.50 → 2199.02] And what was 1.2?
[2199.22 → 2201.04] Like kind of what are your major releases?
[2201.04 → 2210.76] So the way the versioning works with Vagrant, I get kind of flack at open source conferences because I don't really follow semantic versioning.
[2211.36 → 2214.50] But the idea is that the first number is stable.
[2214.80 → 2221.56] So like 1.0 is stable, but then like 1.1, 1.2 are experimental up towards a stable 2.0.
[2222.56 → 2229.42] So I'm going to make that clear on the downloads page in the future by highlighting that if you still want a stable release, you should go with 1.0.
[2229.42 → 2237.60] But also the Vagrant project, I think since the beginning has been known for pushing very, very stable experimental builds.
[2237.70 → 2244.62] Like I say experimental kind of as a disclaimer to myself, but there's usually very few major issues.
[2244.62 → 2246.58] Or if there are, I push out new releases very quickly.
[2246.84 → 2254.06] So the 1.x's that are coming out are just kind of experiments working towards what my vision is for 2.0.
[2255.92 → 2256.40] Marker.
[2257.90 → 2258.96] Did you say marker?
[2258.96 → 2260.12] Yeah, I got disconnected.
[2261.20 → 2261.60] Nice.
[2262.22 → 2265.70] Hey, Mitchell, I'm just really curious about this.
[2265.76 → 2267.74] I was just kind of reflecting on this while you guys were chatting there.
[2267.86 → 2272.92] But in your Twitter bio, you mentioned being automation obsessed.
[2273.28 → 2275.30] What does that look like to be automation obsessed?
[2275.66 → 2277.02] It's a disease, man.
[2278.38 → 2281.28] It's basically whenever I do anything, I can't.
[2281.74 → 2287.04] If I have to do it even like twice, I get really frustrated if I can't automate it away.
[2287.04 → 2293.76] I don't know why, but I've always just had this interest in just making computers do things for me.
[2293.82 → 2296.46] That's how I got into programming actually, which is kind of a cool story.
[2297.28 → 2301.74] I just wanted – I was playing video games and I wanted to – there was like – I was playing a web video game.
[2301.74 → 2305.22] And I was doing the same stuff every day to get this virtual currency.
[2305.68 → 2308.02] And I was getting pissed off that I was doing it.
[2308.12 → 2311.90] So I learned how to program in Visual Basic to do it for me.
[2312.80 → 2313.16] Nice.
[2313.72 → 2313.98] Yeah.
[2313.98 → 2322.08] It kind of reminds me of – I'm not sure if you're – if Kenneth, if you're listening to this even on the podcast, I'm sure you're going to put your hands up in the air when I say this.
[2322.20 → 2326.44] But super huge fan of like Castlemaine Symphony of the Night.
[2326.68 → 2336.82] And that game required you to like – if you didn't have an automation controller, you would never really finish the game to the degree you really want to do.
[2336.82 → 2342.12] Yeah, I think one of the coolest things I made that no one ever saw, no one ever will see because it's legally questionable.
[2342.40 → 2344.00] So I may or may not have made this.
[2344.28 → 2345.92] I'm not admitting to anything.
[2346.26 → 2349.20] But I made – well, so I did make it.
[2349.28 → 2349.42] Whatever.
[2350.48 → 2351.16] He made it.
[2351.18 → 2351.94] Yeah, I made it.
[2352.02 → 2352.20] Fine.
[2352.28 → 2354.48] That was the worst disclaimer ever.
[2355.48 → 2357.00] I don't know how to disclaim this.
[2357.06 → 2358.00] I'm just going to admit to it.
[2358.00 → 2362.98] But I made a World of Warcraft bot for Mac in like 2007.
[2362.98 → 2381.86] And I never got caught because I realized that since Mac is a Unix process model that if I ran – and it ran as a user-level process, that if I just ran a root-level bot, that it could never detect that it's actually running unless I make a mistake, you know, make it obvious by what modifications I'm making.
[2381.96 → 2385.18] So I think – I want to say I made the first one that did that.
[2385.28 → 2387.44] But I never released it publicly, so I can't prove that.
[2387.86 → 2388.86] But it worked.
[2389.18 → 2389.70] It was fun.
[2390.44 → 2391.42] We'll take your word for it.
[2391.42 → 2399.10] The only types of bots that I ever programmed for games like that were like holding my finger on the space bomb.
[2399.96 → 2400.78] That's next to it.
[2400.86 → 2402.44] Those have their place.
[2404.38 → 2405.12] Oh, man.
[2405.36 → 2406.50] So I got a question on Twitter.
[2407.24 → 2407.66] Let's do it.
[2407.88 → 2411.22] And I don't really have any knowledge of this.
[2411.22 → 2418.72] So Byron Miller, it's at Byron underscore Miller, said to ask you if there is any movement on Hyper-V support.
[2418.72 → 2422.30] There's not any movement.
[2422.62 → 2425.70] But there are a lot of requests for it.
[2426.20 → 2427.72] So I am looking into it.
[2427.80 → 2433.20] The main issue is that I don't have a Windows machine powerful enough to run Hyper-V, which is kind of a silly excuse.
[2433.34 → 2434.26] But that's kind of what it is.
[2434.74 → 2436.96] So I'm working on fixing that problem.
[2437.18 → 2439.86] And then I'm going to look into it.
[2439.86 → 2440.70] But no promises.
[2440.70 → 2447.48] So for the hecklers who might be listening to the show now thinking where is the Hyper-V support, what exactly is it?
[2447.72 → 2451.84] Oh, Hyper-V is Windows virtualization technology.
[2452.16 → 2456.28] It could run Linux, but it's their hypervisor to run virtual machines.
[2456.60 → 2461.22] And the cool thing about Hyper-V is it ships with Windows 8 Standard, I think.
[2461.78 → 2463.02] So it's free.
[2463.24 → 2468.18] Like if you buy Windows 8 Standard, which is the majority of people, then you already have the virtualization thing.
[2468.18 → 2474.10] So one problem with Windows that sucks on Windows are there's VirtualBox on the very low end, which is free.
[2474.44 → 2478.54] And then the next step-up is VMware Workstation, which is $250.
[2479.16 → 2482.66] So there's like a huge gap there in virtualization pricing.
[2482.92 → 2489.16] And Hyper-V would make a really nice middle ground because of it shipping with Windows Standard.
[2490.92 → 2491.52] Cool.
[2493.12 → 2493.96] Super cool.
[2493.96 → 2498.26] You talked a little bit about I think you had just recently made a switch from Emacs to Vim.
[2498.86 → 2501.34] Have you gone back or have you stayed in that realm?
[2503.10 → 2504.62] I'm in Vim full-time.
[2504.68 → 2505.76] And that started as a joke.
[2505.86 → 2506.44] Oh, my gosh.
[2506.62 → 2510.54] I mean, I worked at Keep and everyone here uses Vim, and I was the only Emacs holdout.
[2510.86 → 2513.28] And I would get so much crap every day for using Emacs.
[2513.38 → 2516.60] So finally one day I was like, all right, I'm going to use Vim.
[2516.66 → 2519.88] I promise I'm going to go all the way and use Vim for a month.
[2519.88 → 2523.22] And then after I use month, I might go back to Emacs or I might not.
[2523.32 → 2526.04] But if I go back to Emacs, you guys can't say anything anymore.
[2526.52 → 2529.94] So I did that, and I stuck with it.
[2530.16 → 2532.44] So last on me, I guess.
[2533.74 → 2535.32] I have no more questions, Andrew.
[2537.16 → 2537.48] Yeah.
[2537.94 → 2540.34] In our back channel, Andrew has asked me if I have questions.
[2540.70 → 2544.84] I kind of do have a couple of questions, but I don't want to interject because it kind of goes back in time a little bit.
[2544.98 → 2545.66] No, go for it.
[2545.66 → 2550.56] I mean we – through all those questions, Mitchell, you answer questions faster than anyone we've ever had on the show.
[2550.58 → 2550.84] I know.
[2550.88 → 2552.04] I had like a –
[2552.04 → 2553.14] I could talk more.
[2553.60 → 2555.74] You could just ask more details about what you want to hear about.
[2555.86 → 2556.70] I could do it.
[2557.10 → 2560.16] Well, can we – let's dive into this part because I'm –
[2560.16 → 2565.56] one thing I'm going to be an advocate for on this show is people who don't know everything because I'm that person.
[2566.36 → 2567.62] I don't think anybody knows everything.
[2567.62 → 2570.70] But I've never really had a chance to hack on this.
[2571.22 → 2572.80] And by this, I mean vagrant.
[2572.80 → 2577.24] But I'm kind of curious to like the getting started, the installation process.
[2578.04 → 2585.58] You know, you have a page getting started on vagrant up and the docs and whatnot about how to get started and how you install it.
[2585.66 → 2588.12] And apparently it's pretty easy to install.
[2588.12 → 2602.84] So what was – when you design like how to start working with this – I guess the easiest way to say it is like working with vagrant or working with a software like this, how do you go about designing that initial user experience?
[2602.94 → 2608.62] You mentioned if you get into DevOps too deeply, you'll kind of forget what the front end is of the web.
[2608.62 → 2614.62] And how do you design the UX of getting involved in using vagrant?
[2615.06 → 2621.16] I mean the design of that experience just comes from making it as easy as possible.
[2621.50 → 2631.84] I think a lot of tools just assume that the people who are going to use it are not – not that they're dumb, but that they're – or not that they're smart,
[2631.84 → 2636.40] but that they're capable of just figuring – or patient enough to figure things out on their own.
[2637.48 → 2640.24] And I mean even I don't have that sort of patience.
[2640.42 → 2645.74] I kind of – unless I'm like really know something's going to solve a problem, I'm not going to spend very much time trying to get something working.
[2645.92 → 2653.72] So the whole goal when making the vagrant getting started process going was how can I make this the minimum number of commands necessary,
[2653.82 → 2659.56] the minimum number of steps, the most guaranteed way to work properly, stuff like that.
[2659.56 → 2667.90] So out of that whole thing came various commands like before Vagrant 0.1, for example, there was no vagrant in it.
[2668.00 → 2672.46] So you would have to create your own vagrant file and configure it before you could run a vagrant up.
[2672.54 → 2675.12] And that's a lot of domain knowledge to even get to that point.
[2675.24 → 2679.58] So to get to the initial gratification of seeing the tool work was a lot of steps.
[2679.82 → 2681.82] So we introduced vagrant in it.
[2682.18 → 2684.98] And then that brought it down to two steps, which is awesome.
[2685.22 → 2688.88] And then with two steps is pretty much like where I'm comfortable there.
[2688.88 → 2691.64] And then we took a look at the installer situation.
[2691.84 → 2693.22] So it used to be Ruby Gems-based.
[2693.46 → 2699.22] And I made a fatal assumption when I started using – not fatal because I'm still around, but it could have been fatal –
[2699.22 → 2703.42] assumption when I released vagrant, which is that people would like that.
[2703.78 → 2705.14] And Ruby people love it.
[2705.44 → 2708.52] But the problem is that most people who use vagrant aren't Ruby people.
[2708.74 → 2710.20] And they hate it.
[2710.84 → 2712.22] AKA coding whore.
[2712.22 → 2712.66] Yeah.
[2713.14 → 2713.84] I mean, oh, yeah.
[2713.92 → 2715.42] Try to set up Ruby Gems on Windows.
[2715.60 → 2716.20] That's fun.
[2716.28 → 2717.58] That's a fun experiment.
[2718.06 → 2726.70] So basically after that, I realized that I need to separate the installation process from the language that Vagrant's written in,
[2726.78 → 2729.46] meaning I can't use Ruby Gems even though Vagrant's written in Ruby.
[2730.00 → 2731.58] And so I switched to installers.
[2731.58 → 2738.86] So now people just grab the installer that's built for their platform, and you use their really standard process on Windows.
[2739.02 → 2740.24] You just double-click the installer.
[2740.82 → 2741.32] Next, next.
[2741.48 → 2742.56] You know, reboot at the end.
[2742.74 → 2743.44] Really normal.
[2745.04 → 2746.40] And, yeah, it's running.
[2746.82 → 2747.92] So that's pretty much it.
[2747.92 → 2751.50] And then so then from then on, it's pretty much the same command line from now on.
[2751.68 → 2757.66] So the CLI is the same Vagrant unit and Vagrant up and Vagrant destroy and all these different commands you have available.
[2757.76 → 2758.40] Exactly, yeah.
[2759.28 → 2762.44] And that's the cool part about Vagrant is that the workflow is the same on any platform.
[2762.44 → 2766.82] So you mentioned the first version didn't ship like that.
[2767.48 → 2770.50] Was it GitHub issues?
[2770.84 → 2771.46] Was it emails?
[2771.80 → 2775.54] Was it just like long nights of trying to figure this out that made you turn the boat and say,
[2775.54 → 2781.50] okay, I should actually ship an installer versus, you know, sticking to my guns of being the Ruby way?
[2782.32 → 2787.28] I think it's being like, you know, it's being aware of every sort of feedback you could get
[2787.28 → 2790.80] and kind of weighing what's coming in more often than others.
[2790.90 → 2793.32] So I get feedback from GitHub issues.
[2793.54 → 2795.70] People find my personal email address pretty easily.
[2796.52 → 2801.44] Conferences, Twitter, hacker news comments, you know, blogs that are coming around,
[2801.60 → 2804.50] like all stack overflow questions, you know, all sorts of things.
[2804.50 → 2809.60] I get all this feedback, and it's kind of just taking everything you see and then trying to figure out what's important.
[2809.76 → 2813.34] And one of the things that I kept seeing over and over was, for example,
[2813.50 → 2817.94] bugs having to do with the way people set up Ruby because people don't know how to set up Ruby.
[2818.64 → 2818.94] Uh-oh.
[2819.36 → 2820.80] Yeah, so it's like it sucked.
[2821.04 → 2826.46] It sucked for me when people were hating on Vagrant because they couldn't install Ruby.
[2826.46 → 2829.66] And I'm not blaming them.
[2829.90 → 2831.26] I mean, I would too.
[2831.38 → 2835.12] I mean, if I had to set up all this, you know, environment stuff just to get some software running,
[2835.16 → 2835.86] I'd be pretty pissed.
[2836.02 → 2839.62] But that's the sort of thing that kind of pushed me to making the installers.
[2840.28 → 2841.66] And that's one example of things.
[2841.78 → 2848.58] But on a smaller scale, on every individual issue, that's kind of how I figure it out is looking at everything available to me.
[2848.58 → 2854.84] And since we talked a little bit about the history and I guess where you came from in the last show,
[2855.54 → 2861.98] Wynn asked you a pretty pointed question, which was how influential has GitHub been?
[2862.36 → 2863.62] And this is a while ago, right?
[2863.70 → 2866.84] So how influential has GitHub been in the development of Vagrant?
[2867.06 → 2869.72] And I'm kind of curious how you'd answer that question now.
[2870.36 → 2874.40] I honestly think that it needed to exist.
[2874.40 → 2880.66] I think, yeah, I just can't imagine Vagrant without GitHub.
[2880.94 → 2890.78] I can explain it further, but basically I can't imagine that level of involvement in a software project on any other platform other than GitHub even today.
[2891.90 → 2897.06] I have some projects on Bitbucket and some other stuff, and I see a lot of projects in Google Code.
[2897.06 → 2906.20] And none of them have the same social power that GitHub has, and that's what I think made Vagrant very, very successful initially.
[2907.54 → 2912.94] I guess you probably, I mean, especially when we talk about the iterations.
[2913.24 → 2920.88] I mean, you mentioned earlier in the show that Vagrant is really iterative, that you're kind of in this experimental stage until you get to 2.0.
[2920.88 → 2926.80] So I could imagine that GitHub issues, those are probably, is that like your campground?
[2926.92 → 2928.06] Do you hang out there most of the day?
[2928.96 → 2930.74] I try not to because it's depressing.
[2932.18 → 2934.30] Too many requests or just too much broken?
[2934.42 → 2942.94] It's not a lot broken, but just a lot of things that, you know, they're half bug issues but half feature requests.
[2942.94 → 2947.92] It's hard to feature better with my time at the moment.
[2948.88 → 2954.72] And so I try to, all my ideas, and I don't like, I don't like publishing my ideas half-baked.
[2954.84 → 2957.88] So I don't use GitHub issues to, as a roadmap or anything.
[2957.98 → 2961.20] And I don't publish a Vagrant roadmap, and some people don't like that.
[2961.32 → 2965.58] But I do like to develop it in private and see if it even makes sense.
[2965.58 → 2980.08] Because definitely in the 13 months that existed between 1.0 and 1.1, I threw away a lot of code that features, like a lot of features I built that just at the end were not up to the standards that I want for something.
[2985.56 → 2988.10] I'm not sure if Andrew is here or not.
[2988.24 → 2988.88] Andrew, are you here?
[2989.20 → 2989.66] I'm here.
[2989.68 → 2993.10] Okay, because we keep losing Andrew, and I keep bringing him back.
[2993.10 → 2995.24] And sorry about that, Mitchell.
[2995.40 → 2996.92] And sorry to the listeners who are listening.
[2997.56 → 3000.46] Sometimes Skype messes up, and right now Andrew's doing a little bit of travelling.
[3000.60 → 3001.96] Like you said, he's in Dallas.
[3002.18 → 3006.44] So he's probably on some skittish co-working Wi-Fi or something like that.
[3006.78 → 3007.58] So anyway.
[3007.78 → 3008.12] No problem.
[3008.56 → 3013.08] Then I wanted to say, too, so now you guys may have obviously already said this.
[3013.14 → 3015.54] I can't hear half the stinking things going on.
[3016.28 → 3022.76] But so now you have, I mean, the project on GitHub, you have 750 forks, 3,500 stars.
[3023.10 → 3026.82] But you have 55 open pull requests and 195 open issues.
[3026.98 → 3030.32] So that's obviously much greater than before.
[3030.32 → 3038.02] And do you find that you're, are you unable to keep up with the amount, with the growth in popularity?
[3038.34 → 3039.76] Or is that just kind of the one?
[3041.44 → 3042.92] So it's tricky.
[3042.92 → 3048.86] So like when I talked to Wynn a year ago, there was like 20 issues.
[3049.02 → 3052.36] And that was because I was winding down issues in order to release 1.0.
[3052.86 → 3054.60] And everything was stable.
[3054.76 → 3056.00] Like things weren't changing that much.
[3056.18 → 3065.38] And then now things are very, not unstable in the crashing sense, but unstable in how is this feature going to look in the future kind of sense.
[3065.38 → 3069.86] And so there are a lot of issues that are, that are suggestions for how to change things.
[3070.04 → 3072.10] There are a lot of issues that are bugs.
[3072.22 → 3074.78] There are a lot of feature requests, stuff like that.
[3075.08 → 3077.46] And, and so that that's obviously ballooned up.
[3077.52 → 3078.88] It'll, it'll go back down for sure.
[3079.24 → 3085.20] And then the other thing is also, like I said, since bigger one, two, two, I've been focusing on this other software project.
[3085.20 → 3091.78] So as part of that, I find it very distractive if I'm bouncing back and forth between projects like context switching.
[3092.06 → 3100.18] So unless there's a huge crashing bug that I need to address, I kind of just skim over the issues and, and recognize that, oh, that'd probably be easy to fix.
[3100.30 → 3102.82] But I'm just going to go ahead and fix that some other day.
[3102.92 → 3111.74] And so on of the days coming up, probably this week, actually, one of the days I'll, I'll sit down and just triage and fix vagrant issues for probably eight hours and, and get a release out.
[3111.74 → 3116.84] But for the most part, I kind of let them grow, and then I just attack them one day.
[3116.98 → 3117.10] Gotcha.
[3117.38 → 3119.80] So how many contributors do you have on the project now?
[3121.18 → 3124.56] Contributors, like core contributors, I'm still the only person with the commit access.
[3124.70 → 3127.66] Actually, John has commit access too, but he doesn't use it right now.
[3127.98 → 3137.94] But in terms of contributors, there's each release has dozens, I would say, of, of code contributors, but they're mostly one-off things, but like very, very helpful.
[3137.94 → 3146.86] Most of the code contributions coming in are for platform-specific things where they're like, oh, if I'm running a Polaris virtual machine, then it's not changing my host name properly.
[3147.42 → 3151.38] And those are sort of things that are really hard for me to know how to do, especially because I'm not a Polaris person.
[3151.76 → 3154.02] So when that sort of stuff's contributed, it's really helpful.
[3154.12 → 3156.48] And that's where a majority of the contributions come in.
[3156.68 → 3164.54] But at the same time, I have been reaching out to a few other people to bring in more core contributors.
[3164.54 → 3176.66] I think what's neat is since the release of providers, providers have given people a stage to make a big difference to Vagrant that they wanted to contribute a lot before, but they couldn't because they were afraid of what to do.
[3177.14 → 3180.56] And now people are being very passionate about their Vagrant plugins.
[3181.52 → 3191.42] And I'm looking to take some of those third-party providers and offer them commit access to make Vagrant better, but also to more officially work on their provider work.
[3191.42 → 3197.36] I guess you can almost look at the people developing those providers as core contributors on those wings of the project.
[3198.08 → 3199.78] Yeah. Yeah, definitely.
[3200.40 → 3210.60] It seems like with the new products that you're working on that there's going to come a point where you're going to have to allow commit access to someone or something to help you kind of keep up with this stuff.
[3210.74 → 3215.24] I mean, it seems like you're going to hit a point of critical mass where you're going to have a ton.
[3215.24 → 3229.00] So what are you looking – I'm not trying to apply or anything, but do you want somebody from the – would you want somebody more from the ops world or more from your past contributors?
[3229.50 → 3233.38] What kind of would you look for somebody to kind of come on the team as a core contributor?
[3234.14 → 3235.36] It doesn't matter to me.
[3235.36 → 3243.30] It's more about whether they understand the goals of the project and whether their vision is kind of in line with what Vagrant's vision is.
[3243.50 → 3244.52] And that's pretty much what matters.
[3245.00 → 3246.08] As long as they're not a hobo.
[3246.64 → 3247.44] No, yeah.
[3247.86 → 3250.00] I mean, they can be if their code's good.
[3251.48 → 3254.56] Their personal life choices aren't my issue.
[3254.86 → 3255.34] That's funny.
[3256.54 → 3256.94] Cool.
[3256.94 → 3257.94] Yeah.
[3259.20 → 3261.36] I don't think there's any more questions in IRC, though.
[3262.58 → 3262.84] No.
[3262.92 → 3265.38] It seemed that you were answering everybody's questions.
[3265.72 → 3266.48] You're like a rock star.
[3267.02 → 3268.86] I'm trying to jump in where I can.
[3269.64 → 3269.94] Cool.
[3270.08 → 3272.94] So we kind of hit on this before, but what's next steps for you?
[3273.04 → 3276.86] Where are you going from today on in the immediate future?
[3277.34 → 3278.00] The immediate future.
[3278.32 → 3279.90] There's a lot coming.
[3280.34 → 3282.36] So more Vagrant releases, of course.
[3282.36 → 3285.26] I'm going to keep pushing forward towards 2.0.
[3285.26 → 3288.24] So I'm working on this new software project, Packer.
[3288.48 → 3290.00] Hopefully you guys will see that soon.
[3290.28 → 3291.40] I'm excited about it.
[3291.74 → 3295.46] From a business standpoint, I'm doing a lot there.
[3295.62 → 3300.96] I don't really want to talk about any of that right now, but you should see news that's pretty exciting in the next couple of months.
[3302.26 → 3303.48] And that's pretty much it.
[3303.52 → 3308.54] It's mostly just iterating forward and one new project, which is cool.
[3308.54 → 3311.16] But other than that, just iterating and pushing forward.
[3311.70 → 3315.02] And if they're following you, what's the best way to catch up with this news?
[3315.02 → 3315.94] Is this newsletter you mentioned?
[3316.02 → 3317.66] Is it a newsletter or is it following you on Twitter?
[3317.82 → 3318.84] What's the best channel to follow?
[3319.52 → 3325.42] The best place to follow is my Twitter, probably, which is at Mitchell H.
[3326.28 → 3327.00] Pretty easy to find.
[3329.50 → 3333.38] And I announce some things on the Vagrant mailing list, too.
[3333.48 → 3335.10] Like releases and stuff are there.
[3335.10 → 3343.66] But for the most part, personal, like I try to push all my announcements more quickly on Twitter, like incremental announcements if you care about the details.
[3346.84 → 3350.00] That's a good question, actually, that Finns has there.
[3351.02 → 3351.88] What's the question?
[3353.38 → 3354.98] So Finns just asked me.
[3355.28 → 3355.80] Let's see.
[3356.00 → 3357.32] Finns just asked me.
[3357.62 → 3359.92] The inmates are running the insane asylum.
[3359.92 → 3360.36] Yeah.
[3361.78 → 3364.06] Finns just asked me what about the medium-term future.
[3364.22 → 3365.20] So is HashiCorp going to grow?
[3365.34 → 3366.80] What sort of company is HashiCorp going to be?
[3367.88 → 3368.98] HashiCorp is going to grow.
[3369.70 → 3374.18] I mean, most people know I haven't taken any venture capital.
[3374.38 → 3378.00] So I'm not able to hire suddenly like 10 people out of nowhere.
[3378.00 → 3382.56] But I'm at a point where I am looking to hire someone, and I have someone in mind.
[3382.74 → 3388.46] I'm not ready to talk about whom, but they're so far on board, and hopefully you'll hear about that in the future.
[3388.62 → 3391.34] And then I think in the next, like, Finns, sorry.
[3391.74 → 3396.00] And then the next year or so, hopefully grow even more than that.
[3396.08 → 3399.96] I think the company HashiCorp is going to be, I want it to just be a big DevOps.
[3400.14 → 3403.96] I want it to be associated with DevOps very strongly.
[3403.96 → 3410.02] So I want people to, the way that when you make open source code, you kind of associate GitHub with it.
[3410.54 → 3420.22] When you work on the ops or the DevOps side of a website, I want the HashiCorp tools to be the obvious answer to things.
[3420.98 → 3421.06] Gotcha.
[3421.44 → 3422.80] So give us a call to ARMS.
[3423.00 → 3427.96] What is something that the community, you would love to see the community do for you in the future?
[3428.78 → 3429.70] A call to ARMS.
[3429.70 → 3443.48] I would love just for people to keep building awesome 1.x plugins and keep pushing that forward because that's, I mean, every new provider that comes out is a whole new community of people that could use Vagrant, and that helps a lot.
[3443.78 → 3449.56] And, you know, blog posts of your experiences, complaints are really helpful if they're said nicely.
[3451.02 → 3452.14] Yeah, all that stuff.
[3452.14 → 3463.76] And on the last show, you mentioned your programming heroes were unnamed, I think you said Tim, your coworker, and then you said, you know, the Yehuda cats and all those guys of the world.
[3464.14 → 3465.92] In the last year, has that changed at all for you?
[3465.96 → 3466.78] Got any new heroes?
[3468.26 → 3468.90] That's hard.
[3470.36 → 3480.66] I'm not sure of specific people, but I would say I have a newfound respect for people that try to commercialize open source because it is hard.
[3480.66 → 3484.38] Yeah, it seems like this is the year of commercializing open source.
[3484.54 → 3488.36] A lot of these projects are kind of going commercial, which is kind of neat to see it happen.
[3489.26 → 3493.36] It's scary and neat because, you know, you could go the scary route, which is like MySQL.
[3493.72 → 3494.32] They did it wrong.
[3494.70 → 3498.02] But you could also go the friendly route, too, so it's scary.
[3499.30 → 3499.66] Yeah.
[3499.92 → 3501.64] All right, well, it was a pleasure to have you on here, man.
[3501.74 → 3506.60] Even though my internet kept on kicking me out, I feel like we had a lot of cool questions and answers.
[3506.68 → 3507.80] I really enjoyed having you on, Mitchell.
[3507.80 → 3509.58] Yeah, thank you.
[3509.76 → 3510.66] It was fun to be on again.
[3510.76 → 3511.24] I love the show.
[3512.02 → 3517.66] And I think you already said it, but his Twitter is at Mitchell H., so give him a follow.
[3517.82 → 3518.64] Ask him some questions.
[3518.78 → 3519.66] Just be nice about it.
[3520.34 → 3521.88] Just be nice.
[3522.90 → 3523.88] Just be nice, people.
[3523.88 → 3525.64] We'll see you then.
[3525.86 → 3526.32] starting.
[3526.50 → 3527.40] We'll see you then.
[3527.46 → 3527.86] We'll see you then.
[3527.86 → 3527.92] Yeah.
[3527.92 → 3528.92] We'll see you then.
[3528.92 → 3529.70] Let's see you then.
[3533.22 → 3533.64] We'll see you then.
[3533.76 → 3535.92] We'll see you then.
[3535.98 → 3536.16] Bye.
[3544.16 → 3552.88] We'll see you then.
