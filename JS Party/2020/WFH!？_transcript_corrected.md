[0.00 → 2.88] And then I'll just be completely crazy and hold up this thing.
[3.30 → 4.98] This is an under desk elliptical.
[5.38 → 6.02] Oh my goodness.
[6.52 → 11.24] It's amazing for incredibly boring, incredibly long meetings that I sometimes have to take.
[13.58 → 14.06] Okay.
[14.26 → 16.10] So real quick, Nick, hold that up high.
[16.18 → 20.28] We're going to put into our show notes, a picture of Nick with his Spider-Man outfit,
[20.28 → 24.54] holding up his whatever that thing is under desk elliptical.
[24.74 → 25.76] So you're not missing out.
[25.86 → 28.26] You'll find it in the show notes, and you definitely want to go there.
[28.26 → 31.74] Bandwidth for Changelog is provided by Vastly.
[32.10 → 34.00] Learn more at Fastly.com.
[34.24 → 37.30] We move fast and fix things here at Changelog because of Rollbar.
[37.44 → 39.12] Check them out at Rollbar.com.
[39.38 → 41.56] And we're hosted on Linde cloud servers.
[41.90 → 43.90] Head to Linode.com slash Changelog.
[44.60 → 47.32] This episode is brought to you by Rollbar.
[47.62 → 49.40] Move fast and fix things.
[49.70 → 51.78] Resolve errors in minutes and deploy with confidence.
[52.34 → 54.62] Head to Rollbar.com slash Changelog.
[54.70 → 55.50] Request a demo.
[55.64 → 56.52] Get started today.
[56.68 → 58.06] It's loved by developers.
[58.06 → 59.18] Trusted by enterprises.
[59.72 → 62.18] And most of all, we use it here at Changelog.
[62.54 → 65.20] Move fast and fix things with Rollbar.
[65.60 → 68.50] Once again, Rollbar.com slash Changelog.
[68.50 → 84.36] Welcome to JS Party, your weekly celebration of JavaScript and the web.
[84.60 → 92.16] If this is your first listen, be sure to subscribe at ChangeLog.com slash JS Party or wherever you get your podcasts.
[92.16 → 94.44] You can be part of the hi jinks.
[94.44 → 100.34] Each and every Thursday we record live at ChangeLog.com slash live 1 p.m. Eastern.
[100.80 → 102.00] Oh, and follow us on Twitter.
[102.22 → 103.48] We're at JS Party FM.
[103.96 → 104.32] Okay.
[104.74 → 105.76] It's party time, you all.
[105.76 → 118.66] What is up, party people?
[118.88 → 119.80] It's your friends.
[120.28 → 120.98] It's Jared.
[121.28 → 122.10] It's Size.
[122.78 → 123.28] It's Nick.
[123.32 → 123.80] And it's K-Ball.
[123.88 → 124.50] Say hi, friends.
[125.10 → 125.80] Hi, friends.
[126.12 → 126.52] POI HOI.
[127.04 → 127.44] Hello.
[127.44 → 139.18] We are calling in from a remote bunker, a.k.a. our houses, which is new and yet not new because many of us here do call in from our houses.
[139.42 → 142.34] But mid-coronavirus or maybe beginning of coronavirus, we don't know.
[142.42 → 143.70] We don't know how long this thing is going to last.
[143.70 → 156.98] But many of us out there in the world either practicing social distancing by choice or being told to do so by local authorities and our works, we thought it would be timely to talk about working from home.
[157.12 → 162.58] Because while many of us work from home, these days pretty much all of us are working from home.
[162.66 → 166.12] And that presents all kinds of challenges and benefits.
[166.12 → 168.56] And there are lots of ins, lots of outs.
[168.56 → 171.68] And we thought, hey, let's do a show all about it.
[171.78 → 178.10] I should also mention our sister podcast, our rivals, those gophers over there at Go Time.
[178.28 → 179.96] Also, did I work from home episode this week?
[180.00 → 181.28] We'll cross-link that.
[181.92 → 184.48] If you just can't get enough of this stuff, you can go listen to Go Time.
[184.64 → 185.30] But don't stay.
[185.58 → 185.92] Don't stay.
[185.98 → 187.36] It's not very nice over there.
[187.50 → 188.00] Just party.
[188.20 → 189.42] Just party is where you want to be.
[190.76 → 192.88] Or you could just get both in the master feed.
[193.16 → 195.04] Ooh, I like your style, K-Ball.
[195.88 → 198.36] I'll give you your five bucks after the show for saying that.
[198.56 → 198.74] Yeah.
[199.94 → 202.28] Ironically, I've been riding more Golang recently.
[202.40 → 205.26] So I feel like I should be over there rather than over here today.
[205.72 → 210.20] Oh, well, the water is warm on both sides of the fence.
[210.28 → 211.22] No, I'm mixing my metaphors.
[212.36 → 215.74] Let's get into the content before I say more ridiculous sentences.
[216.28 → 218.48] And talk about working from home.
[218.48 → 224.72] We should also mention there's another aspect to this particular time in that we're not all just working from home.
[224.82 → 228.36] We're also in more stressful circumstances.
[228.56 → 229.16] More than ever.
[229.80 → 238.80] So as far as the panel here goes and our lives and how we do our work, maybe just go around quick and share what our normal day is like and what we're up to now.
[238.92 → 239.46] I'll start.
[239.46 → 242.94] I've been working from home for my entire career.
[242.94 → 245.52] And so I have a lot of experience at this.
[246.06 → 249.96] I'm thankful that my life right now doesn't feel all that different from it usually does.
[250.06 → 254.20] So I'm probably the least affected from the isolation because I'm so used to it.
[254.58 → 257.72] But I know I'm a little rare in that way.
[258.06 → 258.76] How about you, Size?
[258.76 → 260.74] Are you regularly a worker from Homer?
[260.74 → 264.32] I think K-Vol is actually in the same bucket as me.
[264.52 → 270.04] I did remote work in my last job for quite a bit from both New York and from Seattle.
[270.72 → 272.84] Then I quit that job, got a new job.
[272.92 → 273.86] That job is in an office.
[273.86 → 283.26] So I've spent the last six months commuting into an office and trying to rearrange my lifestyle around actually commuting in and trying to optimize that commute and things like that.
[283.70 → 285.16] Kind of really settled in.
[285.32 → 287.04] You know, I have a plant on my desk and everything.
[287.30 → 288.36] And then I'm back to remote.
[288.58 → 291.00] So that's been my situation.
[291.20 → 294.70] So it hasn't been enough time for me to really forget what it's like.
[294.84 → 299.48] And because I'm naturally very introverted, it hasn't really been a huge social toll on me.
[299.48 → 307.50] In fact, I've been trying to see the silver lining of it, given that it has given me a lot more time, sort of alone and quiet situation.
[308.42 → 308.98] Okay, well.
[309.76 → 310.08] Yeah.
[310.24 → 314.50] So I worked from home for quite a while.
[314.60 → 318.54] I've been remote in different settings for different times of my career.
[318.86 → 324.58] I have been for the last, I guess, almost five months now working at a company where I go in on site.
[324.78 → 325.78] It's a short commute.
[325.92 → 326.82] It's a 10-minute bike ride.
[326.90 → 327.60] So it's been lovely.
[327.60 → 329.76] I haven't had to deal with the commute issue as much.
[330.06 → 335.78] So, I mean, that is one, as we get into pros and cons, one benefit for many folks of the work from home is dropping the commute.
[336.40 → 341.68] And yeah, so in a lot of ways, the same habits and setup that I had, I've been able to just reapply.
[342.26 → 351.66] Because of that juxtaposition, I have very strong visual into why this is very different from typical work from home, particularly because our schools are cancelled, childcare is cancelled.
[351.82 → 354.52] I've been dealing with health issues on my parents and various other things.
[354.52 → 359.84] So, like, there's a lot of stuff that's different this time around, and that's very visible.
[360.54 → 364.70] But yeah, luckily, I, on the work front, had kind of a routine I could fall back into.
[365.90 → 370.56] Nick, I know you've been a remote worker for a while, but you are under extreme stress these days.
[370.60 → 371.02] You want to share?
[371.98 → 372.20] Sure.
[372.34 → 372.52] Yeah.
[372.52 → 376.44] Yeah, I've been working since 2011 from home, and I really like it.
[377.36 → 380.10] Don't want to go back to an office, at least right now.
[380.46 → 382.90] But I don't know, maybe that's changed in the last three days.
[383.24 → 384.64] Yeah, you kind of want to all of a sudden, don't you?
[385.14 → 385.46] Yeah.
[385.72 → 391.16] I typically work, like, I get my kids ready for daycare, and I take them.
[391.38 → 396.10] So I have a little bit of a commute to start my day off, and then I come back home, and I get to work.
[396.32 → 400.10] And, you know, typically work until 5 when they come home, and then I'm done working from there.
[400.10 → 407.02] But with all of this, it's kind of changed quite dramatically, because we're in the same situation as K-Ball with no childcare right now.
[407.46 → 414.04] My parents are around, but we don't want them to watch them because, you know, older populations and such with coronavirus.
[414.72 → 417.32] And my wife is now also working from home.
[417.70 → 422.06] We have a one-year-old who kind of needs 24-hour attention.
[422.28 → 426.04] You know, when he's awake, he needs attention and needs to be watched so he doesn't do anything crazy.
[426.04 → 435.84] And so it's been tough, and I have switched my schedule now to working starting at 4 a.m. and getting off around noon, 1230-ish,
[436.28 → 441.00] and then helping with the kids in the evenings while my wife takes the afternoons and evenings to work.
[441.28 → 444.34] So it's been quite the change in that regard.
[444.50 → 449.00] It's basically two full-time jobs now for each of us, and that's been tough.
[449.44 → 450.46] So you're off work.
[451.72 → 452.54] Technically, yeah.
[454.62 → 455.84] New shift, next shift.
[456.04 → 457.84] Next shift, we're going to start up, right?
[458.36 → 459.28] The daytime shift.
[460.54 → 464.78] So one thing that's nice, at least, is we're not completely talking out of the air.
[464.88 → 471.34] All of us have extensive experience working from home and have dealt with a lot of the challenges.
[471.74 → 472.84] There are benefits.
[473.04 → 474.60] There are drawbacks.
[474.60 → 478.18] As with anything in the world of software, it depends, right?
[478.18 → 484.26] So I thought what we'd talk about a little bit is where we work, and then how we work, and then how we not work.
[484.26 → 492.00] And maybe some of just the pros and cons, giving tips and tricks along the way, or sharing our experiences.
[492.00 → 498.46] I should also mention a JS Party panellist that couldn't make it today but has also extensive experience and has written about it is Chris Miller.
[499.16 → 508.80] He has a great post, which we'll put in the show notes, called Pro Tips for Devs Working from Home, which he spoke about as, I think, a pro tip on an episode of JS Party called,
[508.80 → 514.74] You Don't Have to Dress Up, but You Do Have to Get Dressed, I think is what it's called, which came while you were on that episode.
[514.88 → 515.70] So I'll also link that up.
[516.06 → 521.44] Chris has a lot of good points, and I think we'll probably echo some of those here today.
[522.26 → 524.60] But the first thing I want to talk about is just the wear.
[524.60 → 531.32] And I think this is like one of the keys to success is to get your wear right, because we know the wear is you're at home.
[531.88 → 537.54] But the challenge is your home is your home, and so it's hard to make it your workplace.
[538.66 → 543.10] So what are some tips on how to go about doing that?
[544.50 → 544.90] Absolutely.
[545.32 → 550.90] I'll jump in with the first huge one, which is just make sure you separate space.
[550.90 → 553.26] If you at all possibly can.
[553.32 → 557.42] And I know for some people, if you're stuck in a tiny apartment or something, this is not possible.
[557.42 → 562.16] But even if you can have the corner of the room, that is, this is the work corner,
[562.42 → 566.16] and you don't go there when you're not doing work, and you do when you're working,
[566.46 → 570.60] it makes a huge difference for your mental ability to turn on and off,
[570.60 → 574.64] which is one of the big challenges from working from home is your boundaries can really blur.
[575.16 → 580.16] So number one, absolutely, any way you can possibly create this for yourself,
[580.16 → 585.38] separate out some workspace that is not the same as all the rest of space in your home.
[585.98 → 587.14] I would agree with that.
[587.22 → 590.06] And I've had the fortunate opportunity to build a new house.
[590.20 → 592.06] I've been working from home, like I said, my entire career.
[592.24 → 596.02] And the first part of that entire is a bit much like 95% of my career.
[596.54 → 600.08] And the first part of that, I was in the basement, which at least has separation.
[600.86 → 604.62] But I also have many children, as you all know.
[604.82 → 607.44] Back then, I had four children in that house.
[607.44 → 609.18] I have six children now in this house.
[609.56 → 612.56] But a non-tip is don't be underneath children.
[613.22 → 617.92] So I had preparation, and I had that, you know, I could go downstairs,
[618.08 → 619.50] and like downstairs was I was working.
[619.68 → 621.46] I come upstairs, and upstairs I am living.
[621.64 → 622.90] And I think that's so necessary.
[623.52 → 627.86] And a huge mistake to make is to just like, I think Chris wrote about it in his post,
[627.94 → 632.66] like roll over in the morning from your bed and like get your laptop out and get to work,
[632.66 → 634.72] because it's just not sustainable.
[635.42 → 641.78] But in the basement was, it was hellish, because it was actually harder probably on my wife than myself,
[641.78 → 647.12] because her role in this endeavour was to like to keep the kids from not running around,
[647.18 → 648.12] especially during podcasts.
[648.80 → 652.12] But all the time, there was just noise, there was distraction.
[652.88 → 654.98] And so I was able to actually design a separate space.
[655.06 → 656.66] Now I'm in an office above the garage.
[656.66 → 661.02] And it was a great opportunity to say, okay, I'm going to have a workspace.
[661.60 → 662.62] You know what should it be like?
[662.72 → 663.40] Where should it be?
[663.60 → 665.66] And how much separation do I need?
[665.84 → 670.46] And I'll tell you with six children, I can lock every door, and nobody can get in.
[670.62 → 675.96] And that's like necessary, because it's hard enough for me to like separate work from life.
[675.96 → 677.80] But like for the kids, for them to understand,
[678.42 → 682.08] which we all just waved at Nick's daughter as she walked to the room,
[682.38 → 683.28] like they don't get it.
[683.44 → 685.06] You know, they're just like they see their parent, and they're like,
[685.06 → 687.52] and it's like, well, you just ruined my flow.
[687.66 → 689.68] It's going to take me 20 minutes to get back where I was.
[690.14 → 691.56] Thanks, but you're cute.
[691.64 → 692.90] So I'll forgive you.
[693.64 → 694.80] Yeah, that is a challenge.
[695.06 → 699.14] If you hear kids in the background, it's because I have no choice right now.
[699.32 → 700.02] They can't go anywhere.
[700.20 → 700.84] I can't go anywhere.
[702.86 → 704.18] But we're all having fun together.
[704.48 → 705.68] I'm wearing Spider-Man pajamas.
[705.80 → 706.98] She was wearing Spider-Man pajamas.
[707.22 → 708.66] So, you know, we're having fun.
[709.26 → 709.34] Yeah.
[709.44 → 714.46] And once again, many folks who are being thrust right now into working from home
[715.06 → 718.28] at last minute, no ability to prepare or do anything like that.
[718.34 → 721.42] Like I've seen some pretty inventive setups.
[721.74 → 723.60] Like I saw somebody set up like a working,
[723.78 → 728.90] a standing desk where they had like a cardboard area supported by LaCroix's
[728.90 → 729.76] or something like that.
[729.84 → 730.52] And various other things.
[730.62 → 732.70] Like you can be inventive.
[733.28 → 734.68] Circumstances are less than ideal.
[734.68 → 738.78] You know, we can't, if you're working from home because of an emergency like this,
[739.14 → 741.62] you can't go and build yourself a new room like Jared did.
[741.76 → 746.66] But you can think about how do you create that space and at least a little bit of mental
[746.66 → 748.30] separation as much as possible.
[749.14 → 749.30] Totally.
[749.66 → 753.90] And I think one thing that can go a long ways is a decent pair of headphones with noise
[753.90 → 754.46] cancelling maybe.
[754.80 → 759.10] But being able to tune out what's going on around you a little bit, that can really help.
[759.14 → 760.22] Even if you're just playing white noise.
[760.22 → 761.80] For sure.
[761.92 → 766.98] And there's a like I'll listen to Spotify, but for some things I can't have lyrics on.
[767.24 → 770.30] There's a great service that I've used called Focus at Home.
[770.64 → 771.52] Or sorry, Focus at Will.
[772.24 → 778.00] That plays music without lyrics of a variety of different things where they've done a lot
[778.00 → 781.50] of tuning to try to like to set it up in such a way that it helps you focus rather than
[781.50 → 782.62] interferes with your focus.
[783.44 → 785.50] Which I like that better than white noise.
[785.76 → 789.56] But I think it is a paid service at this point, but there may be a free trial.
[790.22 → 790.94] That sounds nice.
[791.06 → 793.28] I actually really, really despise white noise.
[794.08 → 794.70] I don't know why.
[794.82 → 798.70] It's just that my brain and my ears, I just absolutely hate it.
[798.78 → 802.64] And anytime anyone recommends it to me, it reminds me of how comforting it is to most
[802.64 → 803.02] people.
[803.52 → 807.54] But I can't even stand the sound of a fan or things like that.
[807.68 → 810.64] And so music to me, it has to be variable enough.
[810.72 → 816.14] Otherwise, my brain just starts getting really annoyed at the I don't know, it's very irritating
[816.14 → 816.64] to me.
[816.74 → 817.90] So music has been so comforting.
[817.90 → 821.46] And I'm actually going to check that one out, even though lyrics are not as bad for
[821.46 → 824.14] me, as long as I'm familiar with the song already.
[824.46 → 826.24] But I do want to check out that service.
[826.38 → 826.82] Thanks, Cable.
[827.74 → 833.50] There is a website called musicforprogramming.net, which I've been listening to for years and
[833.50 → 838.64] tried to get the person that created it onto our shows and never quite succeeded because
[838.64 → 839.22] they're very shy.
[839.22 → 841.08] But that's another great one.
[841.18 → 842.90] It's all ambient style.
[843.90 → 846.46] The kind of music you want to listen to when you're programming, basically.
[846.56 → 851.32] There's also an app called Vizio, which is like for macOS, and it goes up in your menu
[851.32 → 851.58] bar.
[852.22 → 852.84] And it's kind of cool.
[852.94 → 855.74] You can toggle it on as soon as you would hate it because it's basically like all the
[855.74 → 857.38] kinds of white noise you might want.
[857.38 → 860.28] And so you can have like the coffee shop sounds.
[860.50 → 862.44] You can have rushing water.
[862.90 → 864.76] You can have lightning.
[865.06 → 867.84] Like basically everything, frogs croaking.
[868.26 → 871.22] And then you can also like turn on multiples at the same time.
[871.28 → 874.02] So you can be like, I'm in a coffee shop, but some frogs in here.
[875.02 → 876.78] It's like Rainforest Café or something.
[877.00 → 877.62] Yeah, exactly.
[877.86 → 881.84] But if you're into that kind of thing, it's a nice, it was free when I used it.
[881.88 → 884.44] I think it's a free app for white noise.
[884.44 → 886.58] I mean, I like nature sounds.
[886.72 → 889.46] It's just like the manufactured white noise I don't like.
[889.64 → 894.34] Along these same veins, free code camps, online vibes are perfect too.
[894.44 → 898.02] They have like a YouTube live channel that they play and that music.
[898.22 → 902.46] It's kind of just like down tempo hip hop beats, but I really like that a lot too.
[902.56 → 904.12] It's kind of like lounge music, I guess.
[904.24 → 908.20] Lounge music is definitely underrated as far as like being able to chill and program.
[908.20 → 914.78] One other thing that I remember noticing a lot the most recent time prior to this when
[914.78 → 918.10] I switched from in the office to work from home was lighting.
[918.40 → 924.58] I was going from being in an office that was brightly lit all the time into my home office,
[924.58 → 926.02] which was not.
[926.80 → 931.94] And it took me a while to realize that my mood was substantially lower because I was just
[931.94 → 935.58] in a less well-lit space for a long period of time.
[935.58 → 940.56] And I invested in getting some better lighting and even just like deliberately, like I still
[940.56 → 944.60] don't have great ambient lighting, but I got like one of those little stand lights and would
[944.60 → 945.78] even just like shine is on me.
[945.78 → 949.90] And it would make such a difference in terms of my mood through the day of just having more
[949.90 → 950.88] light around.
[951.94 → 953.04] I totally agree with that.
[953.06 → 956.78] And that's not something that you would really think about too much, or at least I didn't.
[957.26 → 959.30] It took me a season to figure it out.
[959.30 → 964.56] Like I was like, why am I so much less like happy through the day?
[964.96 → 965.80] Oh shoot.
[965.92 → 967.38] Like it's, it's this lighting.
[968.02 → 968.46] Yeah.
[968.58 → 973.92] I moved to the basement, moved my office when my second kid was born because he got the
[973.92 → 975.64] good room with all the lighting in it.
[976.08 → 980.66] And it took me a long time to realize that maybe it was some lighting that's missing from
[980.66 → 985.10] my life that really would make me happier during work days.
[985.10 → 990.60] So I did get one of those like, um, I don't know, a seasonal effective light that's supposed
[990.60 → 991.36] to simulate sunshine.
[991.64 → 993.30] And I just shined it on me occasionally.
[994.20 → 996.92] I'm very sensitive to lighting and I always have been.
[997.00 → 998.72] That's just like how I am noise and lighting.
[999.08 → 1005.08] And so for me, I always get so upset immediately, and I'll notice if the lighting is off.
[1005.14 → 1011.36] So that's almost like a gift in this particular scenario, because the first thing I do, like
[1011.36 → 1016.40] when I first moved into this apartment that I'm currently in, I changed out every single
[1016.40 → 1020.58] light bulb to be the exact same temperature and not to be like quote unquote bad temperature
[1020.58 → 1023.34] and try to put full spectrum lighting.
[1023.52 → 1026.42] Like you don't necessarily have to have those happy lights because sometimes they're a bit
[1026.42 → 1031.70] expensive, but if you buy a full spectrum light that can actually produce, you know,
[1031.76 → 1034.84] something very similar to sunlight, which is very therapeutic for humans.
[1035.54 → 1040.80] And so for me, I already become miserable just because I'm sort of tuned into spotting like
[1040.80 → 1042.08] bad lighting situations.
[1042.08 → 1047.88] Like when I see apartments at night have that kind of greenish tinged fluorescent light, I
[1047.88 → 1050.62] just want to knock on their door and be like, how can you live with this?
[1050.70 → 1053.76] But I realized that different people are sensitive to different things, right?
[1053.84 → 1059.74] So I'm a huge fan of tuning lighting to make yourself just feel so much better.
[1059.88 → 1064.00] But it's so hard to notice if you don't, if you haven't sort of played with that kind
[1064.00 → 1064.50] of thing before.
[1064.58 → 1065.86] So I'm really glad you brought that up.
[1065.86 → 1071.84] So Lane in the chat says they hear that wearing shoes helps.
[1072.08 → 1075.20] I'm not sure if that helps for at a standing desk.
[1075.32 → 1076.74] Maybe there's some context that I missed there.
[1076.82 → 1077.98] But yes, we do watch the chat.
[1078.12 → 1083.78] If you're listening live, head to the JS Party channel in our team slack.
[1083.86 → 1086.38] If you're not, and would like to participate, we'd love to have live listeners.
[1086.52 → 1090.86] Changeable.com slash live or changeable.com slash community free.
[1091.14 → 1093.28] Hop into our slack and participate.
[1093.28 → 1099.04] I will say that I'm a big fan and advocate for quote unquote treating yourself when it
[1099.04 → 1100.74] comes to the location of your work.
[1101.10 → 1107.78] So whether that's your desk, your monitor, your speakers, wearing some nice shoes or having
[1107.78 → 1111.82] a good throw rug, the lighting, the ambiance.
[1112.00 → 1113.34] I don't understand feng shui.
[1113.48 → 1114.16] I'm not feng shui.
[1114.16 → 1119.02] But if that's your thing, go ahead and take time and take effort and take money.
[1119.74 → 1124.36] Hopefully you can take your company's money if they're making you work from home and spend
[1124.36 → 1130.78] it on the things that you're going to use and be surrounded by on a day-to-day basis
[1130.78 → 1136.92] because you are going to be there at that desk, hopefully at a sustained pace for a sustained
[1136.92 → 1137.52] amount of time.
[1137.52 → 1142.22] And it needs to be an enjoyable and habitable living space.
[1142.32 → 1145.64] It shouldn't be like a place you dread to be.
[1146.74 → 1152.42] Anybody have any specific like picks or hardware or like anything in their space?
[1152.74 → 1157.34] I think my favourite thing that I have that I don't have when I go into an office is I
[1157.34 → 1158.14] have a space heater.
[1159.52 → 1162.98] I just got one of those, and it's made such a difference.
[1163.30 → 1163.50] Totally.
[1163.64 → 1164.66] It's amazing.
[1164.66 → 1166.92] And I mean, I'm a warm weather type person.
[1167.36 → 1172.96] And so like, I tend to like being very warm and even things like, okay, take your
[1172.96 → 1176.02] shoes off, wear socks and stick your feet in front of the space heater.
[1177.08 → 1178.42] It's like luxury.
[1178.74 → 1179.42] It's amazing.
[1179.56 → 1181.38] It makes it so much better.
[1181.62 → 1182.38] Love that.
[1183.28 → 1188.26] For me, I just I like to warm up a space aesthetically and expanding on that.
[1188.46 → 1194.62] What I mean is just having things that don't make it look like your room is very clinical.
[1194.66 → 1198.70] You know, like because you're in your own space, you can actually be a bit more creative than
[1198.70 → 1200.30] perhaps you're allowed to be in an office.
[1200.84 → 1205.34] So even just things like a cork board, is that what you call it in America?
[1205.34 → 1206.32] Like a pin board.
[1206.64 → 1211.94] And I put little knick-knacks and Polaroid photos and things up there as well as like,
[1212.04 → 1215.74] you know, the cheat sheet for open scout and things like that I constantly refer to.
[1216.08 → 1217.44] That makes me really happy.
[1217.44 → 1222.62] And as far as like being able to just cover walls with things, especially if you're in
[1222.62 → 1227.96] a rental, I have a giant tapestry, which is just like a piece of cotton with a printed
[1227.96 → 1230.46] design on it that I got from Society6.
[1230.68 → 1234.52] And it's just pinned with two, I guess, thumbtacks.
[1234.60 → 1234.78] Sorry.
[1234.90 → 1238.04] I'm like, I'm trying to internationalize how I'm describing these items.
[1238.64 → 1239.78] You can localize them.
[1239.82 → 1240.20] No big deal.
[1240.20 → 1245.12] So I use thumbtacks and because they're so small, and they're so high up on the wall that
[1245.12 → 1247.42] they're so close to the ceiling, you would never notice those little holes.
[1248.06 → 1251.94] And so I've been able to hang sort of a tapestry that has just immediately brightened a room
[1251.94 → 1254.46] without actually damaging the wall since I'm in a rental.
[1255.28 → 1256.58] Just little things like that.
[1256.66 → 1260.78] You can spend maybe if you have the budget to spend a hundred bucks, you can do a lot to
[1260.78 → 1266.74] just make the space not feel like some really boring wall, you know, and that's been very,
[1266.86 → 1267.86] very helpful to me.
[1268.66 → 1269.54] And plants too.
[1269.54 → 1269.86] Sorry.
[1270.12 → 1270.52] Plants.
[1271.02 → 1271.70] Very important.
[1272.04 → 1273.96] So I really like having plants around my space.
[1274.04 → 1277.96] So if you're someone who doesn't get anxious about the idea of caring for very easy to
[1277.96 → 1280.36] care for plants, that can really lift your mood as well.
[1280.98 → 1281.98] I will echo that.
[1282.08 → 1284.78] Bring some green into the inside world.
[1284.90 → 1288.96] For those of you who can see my Zoom, you can see my little bonsai.
[1289.34 → 1290.42] Behind me, little bonsai.
[1290.60 → 1292.14] I like to take care of that.
[1292.18 → 1296.78] And I also have access to the out, you know, a place where I can see outside, which is nice
[1296.78 → 1297.18] as well.
[1297.18 → 1299.66] Any other furniture, decor?
[1300.08 → 1301.58] I see in the notes, standing desk.
[1301.64 → 1303.20] I'm an advocate for standing desks as well.
[1303.64 → 1309.04] It's nice to have somewhere where you can sit down if you're a stander because all day
[1309.04 → 1310.32] long can get to be long.
[1310.32 → 1312.20] But Nick or Cable, any other?
[1312.78 → 1314.88] It's probably a longer term investment.
[1314.88 → 1320.28] But having a good office chair makes a huge difference, at least for me, in terms of like
[1320.28 → 1323.48] not having my back messed up at the end of the day and things like that.
[1323.90 → 1328.40] When I was working from home for a longer period, it was a must investment.
[1328.98 → 1333.58] Depending on where you are right now, you may be looking at shorter or longer periods of
[1333.58 → 1334.74] quarantine and isolation.
[1335.10 → 1338.16] And it may or may not be worth that investment.
[1338.16 → 1342.74] So if you can get your company to pay for it, because they are rather expensive if you
[1342.74 → 1346.08] get a good one, yes, it's a very valuable investment.
[1346.32 → 1350.04] And if you're thinking about working from home for the long term, or you have been working
[1350.04 → 1356.06] from home, and you have not invested in a good office chair, it will pay your body back
[1356.06 → 1357.34] so much.
[1357.34 → 1360.32] Yeah, I would echo that as well.
[1360.56 → 1365.40] For standers, a good standing mat would be a good thing as well.
[1365.86 → 1370.50] The one that I have allows you, like it has little bumps in it to kind of force you to
[1370.50 → 1375.94] kind of move around a little bit and squirm just to not stand, you know, in a bad posture
[1375.94 → 1376.32] all day.
[1376.44 → 1378.78] You kind of have to move around, which I really like.
[1378.94 → 1382.02] And then I'll just be completely crazy and hold up this thing.
[1382.42 → 1384.10] This is an underdesk elliptical.
[1384.34 → 1385.32] Oh my goodness.
[1385.32 → 1390.36] It's amazing for incredibly boring, incredibly long meetings that I sometimes have to take.
[1392.80 → 1395.22] Okay, so real quick, Nick, hold that up high.
[1395.32 → 1400.14] We're going to put into our show notes a picture of Nick with his Spider-Man outfit holding up
[1400.14 → 1403.66] his whatever that thing is, underdesk elliptical.
[1403.82 → 1404.88] So you're not missing out.
[1404.98 → 1407.34] You'll find it in the show notes, and you definitely want to go there.
[1415.32 → 1420.98] Hey friends, got some good news for you.
[1421.30 → 1427.28] Linde just added a cluster of Linde's S3 compatible object storage to the Frankfurt
[1427.28 → 1427.86] data centre.
[1427.96 → 1433.20] And celebrating this, they're giving everyone, not just Frankfurt, but everyone three months
[1433.20 → 1435.46] of free object storage starting today.
[1435.64 → 1436.32] There's no bill.
[1436.42 → 1437.22] There's no promo code.
[1437.30 → 1439.02] There's no redemption process.
[1439.24 → 1440.98] Sign up, get object storage from Linde.
[1440.98 → 1443.90] And from March 1st to May 31st, there is no bill.
[1444.10 → 1445.10] It's too easy.
[1445.52 → 1447.06] Head to linode.com slash changelog.
[1447.06 → 1462.60] So we talked about where we work and how we decorate or arrange that location.
[1463.68 → 1469.92] The other big aspect of working from home is managing how you work because a lot of the
[1469.92 → 1473.32] rules change at your house than at an office environment.
[1473.70 → 1475.28] Some for the better, some for the worse.
[1475.28 → 1481.82] And some of this depends somewhat on personality types in regard to like scheduling and
[1481.82 → 1484.38] getting up in the morning and working or staying up late and working.
[1484.56 → 1486.72] Like it's the power is in our hands.
[1486.82 → 1489.46] Of course, depending on where you work, you have to have certain overlaps.
[1490.26 → 1493.36] Maybe your job dictates eight to five within one hour lunch.
[1493.52 → 1495.54] Well, you don't have much of a choice and that's what you're going to do.
[1495.62 → 1498.84] But many of us are in circumstances where we can work asynchronously.
[1499.00 → 1501.36] We have to sync up at meetings, but we can pick and choose.
[1501.36 → 1505.46] Am I going to take a longer lunch and work till 7pm or whatever it is?
[1505.54 → 1510.94] How do we deal with scheduling in a way that's sustainable and beneficial and doesn't just
[1510.94 → 1513.52] wear us down when we're working from home?
[1514.40 → 1519.94] Well, I can highlight some of the things that I had to learn actually, not this time around,
[1520.00 → 1522.06] but the most recent time before this.
[1522.06 → 1524.36] The biggest ones being around...
[1524.36 → 1530.40] So there's a lot of advice out there in the world about planning and scheduling and making
[1530.40 → 1534.12] sure that you list out what you're trying to accomplish and things like that.
[1534.28 → 1538.48] And a lot of times you can kind of skate by if you're in an office without doing stuff
[1538.48 → 1543.28] because the environment and other things keep you moving forward and making progress.
[1544.14 → 1549.82] And I found that for me, at least a lot of those things become much more critical working
[1549.82 → 1550.34] from home.
[1550.34 → 1556.10] So it became much more critical to plan out when I was going to do things and have stuff
[1556.10 → 1560.22] in a calendar, both for me and also to coordinate with other people.
[1560.42 → 1563.88] So because it wasn't as easy to just drop by and figure something out.
[1563.96 → 1565.32] It was like, okay, let's schedule a time.
[1565.42 → 1566.54] Let's connect, things like that.
[1567.04 → 1568.34] The other thing around that was...
[1568.96 → 1574.66] Or a huge thing around that is planning some parts of your day each day, what you're trying
[1574.66 → 1575.28] to accomplish.
[1575.74 → 1579.18] And I think it's valuable to plan things that are not just work-related.
[1579.18 → 1582.68] Yeah, you want your top three things that you need to get done on the work front.
[1582.78 → 1587.26] But also, what are the top three things you need to do personally, whether it's getting
[1587.26 → 1593.42] groceries or taking care of kids or just having some time for yourself to meditate or relax
[1593.42 → 1594.54] or go for a walk or something.
[1595.06 → 1596.38] Plan those things out.
[1596.38 → 1602.46] And the other thing and something that came up a little bit during the break is we should
[1602.46 → 1606.46] probably be thinking about this as something that is at least a medium-term thing.
[1606.74 → 1610.66] And then we can be pleasantly surprised if it passes over quickly, and we're all back to
[1610.66 → 1611.34] the office soon.
[1612.00 → 1616.78] But plan for things that involve your growth and development as well.
[1616.78 → 1621.82] The same way you might do in an office, think about what are you learning about?
[1621.92 → 1622.92] What are you focused on?
[1623.08 → 1627.28] What is going to help you get to someplace that is not the same place you are today in
[1627.28 → 1628.28] six months or a year?
[1628.42 → 1636.16] So that you're having not only what I got to do to get through the day on my job and what
[1636.16 → 1640.26] do I got to do to get through the day in my life, but also what am I doing to make myself
[1640.26 → 1641.20] a better human being?
[1641.20 → 1646.08] What am I doing to help me learn, whether it's career-wise or not?
[1646.74 → 1648.04] I agree with this a lot.
[1648.26 → 1652.66] I think that when you work from home, or you work remotely, the days can blur into each
[1652.66 → 1653.28] other a lot more.
[1653.50 → 1657.28] So keeping your eye on long-term goals can be a little bit harder.
[1657.68 → 1664.52] I feel that I had the double whammy of all of a sudden working remotely for the first time
[1664.52 → 1669.28] when I started my job at Microsoft, but it was also my first almost fully autonomous role.
[1669.28 → 1674.42] So they would say, here are the high-level metrics for this entire year.
[1675.24 → 1679.86] You have to figure out, you have to fill in that entire year gap with what you're going
[1679.86 → 1681.20] to do to achieve that.
[1681.54 → 1685.28] And so imagine working from home, no one's looking over your shoulder, but also you're
[1685.28 → 1688.38] making up your own schedule for your own job at the same time.
[1688.66 → 1692.72] And you might have maybe quarterly check-ins at the most with your manager for them to say,
[1692.80 → 1694.76] yeah, you're sort of like on the right track in general.
[1694.76 → 1701.22] And so I had to set up a very strict routine for myself in order to know what I was getting
[1701.22 → 1703.02] up in the morning for, if that makes sense.
[1703.20 → 1709.78] And so if I wanted to have, oh, I'd like to have this one IoT project that I do, that
[1709.78 → 1714.86] the end result will be that a bunch of people will actually learn Azure IoT in a
[1714.86 → 1715.92] way that's approachable for them.
[1716.04 → 1722.24] I had to break that down into lots of little tiny things in order for me to understand what
[1722.24 → 1727.14] I needed to get done every day, because there was just no mandate coming from management
[1727.14 → 1727.74] in that way.
[1727.96 → 1732.60] And so even if you do work in a role where you're peeling off JIRA tickets, you know,
[1732.64 → 1736.20] especially if you're a software engineer, and you're working on a larger feature, it's
[1736.20 → 1741.40] very similar in that it would be good for you to, especially if you're having fewer meetings
[1741.40 → 1745.64] now, it would be good for you to just make a list of, okay, well, I want to at least
[1745.64 → 1751.34] have like this and this and this part done of the JIRA ticket today, which would be similar
[1751.34 → 1755.40] to how you do things in an office, but you'd be surprised at how quickly that can unravel
[1755.40 → 1758.06] when you're at home as, as was being mentioned before.
[1758.88 → 1759.24] Yeah.
[1759.26 → 1764.08] I think one thing that I really do is try and make the first part of my day being setting
[1764.08 → 1769.94] goals, meaning like I keep a pretty good to-do list and I flag things that I want to
[1769.94 → 1770.20] get done.
[1770.28 → 1772.96] Not too many, maybe three that I really want to get done.
[1773.08 → 1776.16] And then I always try and work on the hardest one first, because I know that that's going
[1776.16 → 1777.12] to take most of the time.
[1777.12 → 1782.84] And I'm going to get sidetracked by meetings and coworkers and now kids and everything.
[1783.12 → 1787.86] So those other things I try and squeeze into like, you know, when I'm in a meeting and everybody
[1787.86 → 1792.68] who is now working remotely is trying to figure out how to use Zoom, then I can start working
[1792.68 → 1793.42] on other things.
[1795.18 → 1796.34] Oh my goodness.
[1796.34 → 1801.82] My wife is in academia, and they're all remote.
[1802.22 → 1806.82] And oh my gosh, some of those folks struggle with things like zoom and etiquette.
[1806.92 → 1809.44] And oh, you have to mute your microphone if you're in a large Zoom meeting.
[1809.50 → 1813.36] And it doesn't necessarily make sense to just have people go around and say they're here.
[1813.52 → 1818.62] And like all these little things that at this point I take for granted about like meeting
[1818.62 → 1820.22] etiquette, like you can see who's there.
[1820.30 → 1824.72] There's a list, you know, and it's, it's interesting.
[1824.72 → 1825.12] Right.
[1825.12 → 1828.00] And that's not unique to academia though.
[1828.06 → 1830.36] I think they're probably way on one side of it.
[1830.42 → 1834.90] I feel like a lot of folks who've never had to deal with this are suddenly dealing with
[1834.90 → 1837.38] these types of etiquette questions.
[1837.38 → 1838.48] How do I do this?
[1838.54 → 1839.38] How do I do that?
[1839.56 → 1844.34] You know, one thing that I think is fascinating.
[1844.54 → 1848.24] So people talk a lot about over-communicate, over-communicate, but they don't necessarily
[1848.24 → 1850.52] talk about what does that mean?
[1850.52 → 1853.68] And that, that in itself can be a little overwhelming, right?
[1853.80 → 1859.14] So I think, you know, one of the big clarifications I've seen there that has been helpful is team
[1859.14 → 1860.14] member to team member.
[1860.30 → 1865.20] You want to over-communicate, meaning you want to talk to each other more, push yourself to
[1865.20 → 1868.98] do it because there's a lot of kind of casual conversation that isn't happening.
[1868.98 → 1874.28] Managers, you don't necessarily want to over-communicate, keep talking, keep harassing your reports.
[1875.10 → 1875.98] Focus on clarity.
[1876.28 → 1879.50] Make sure that everything that you are communicating is crystal clear.
[1880.00 → 1883.68] And then the other thing around for all of this, every type of communication is written stuff
[1883.68 → 1884.12] down.
[1884.12 → 1892.50] A lot of us have this sort of habit of doing things by verbal agreement, which is error-prone
[1892.50 → 1896.56] enough in an in-person setting, but you don't have the same feedback loops when you're remote
[1896.56 → 1897.84] and you're working more independently.
[1898.14 → 1903.74] And so the more you can have things written down and both of you agree that the written
[1903.74 → 1908.32] documents match your understanding of what's going on, the better time you're going to have
[1908.32 → 1913.18] coordinating across people who are sometimes working in different time zones, sometimes
[1913.18 → 1918.22] working at different times, your schedule may be shifted for any number of reasons, including
[1918.22 → 1924.10] childcare and other stuff, and just not having that in-person space to clear things up quickly.
[1924.78 → 1929.86] It's hard to give scheduling advice that geneticizes well because we're all in so many
[1929.86 → 1933.38] different circumstances, and we all thrive and work differently.
[1934.22 → 1939.08] And so I guess a small bit of advice, which may sound cliché, is to really know yourself and know
[1939.08 → 1945.54] in what circumstances you get a lot done and what circumstances you struggle to concentrate
[1945.54 → 1949.50] and then try to devise a schedule around that.
[1949.60 → 1953.46] Now, this, of course, assumes that you are given some autonomy around your schedule.
[1953.56 → 1954.50] Some people don't have that.
[1954.58 → 1959.26] Even if they're working from home, they have to be on Zoom all day, or they have to be, you
[1959.26 → 1961.04] know, eight to five or whatever that is.
[1961.04 → 1963.00] In that case, I guess just do what you got to do.
[1963.00 → 1968.24] So fully realizing that the manager schedule doesn't match a maker schedule very well and
[1968.24 → 1970.00] you probably struggle under those circumstances.
[1970.14 → 1975.56] But if you're given the autonomy to create your own schedule, well, go ahead and take the
[1975.56 → 1982.14] time to do that and analyze what's working, what's not working and adjust because you know
[1982.14 → 1987.86] how well you can be productive when you're inspired, energized, and excited and how hard it
[1987.86 → 1990.22] is when you're not to like power through.
[1990.22 → 1994.52] Well, the nice thing about working from home is if you have the autonomy is you can organize
[1994.52 → 1997.06] yourself around those moments and opportunities.
[1997.78 → 2002.50] And when you're not being productive, and you're distracted, and you're not concentrating, you
[2002.50 → 2007.24] can just go outside, or you can just take a nap, or you can do whatever it is you want to
[2007.24 → 2009.06] do, and you don't have to work during those times.
[2009.30 → 2012.14] So embrace that because that's an opportunity.
[2012.32 → 2015.68] It can be a struggle, but it can also be a huge opportunity.
[2015.68 → 2022.28] I think if you're a knowledge worker too, during this time, you're going to notice just that
[2022.28 → 2028.36] you aren't as productive, and you can't necessarily blame that on a transition to working remotely
[2028.36 → 2028.72] too.
[2029.26 → 2035.14] Like this is a very unprecedented thing for a lot of people to go through, especially
[2035.14 → 2036.16] around the uncertainty.
[2036.52 → 2040.44] Like your brain is going to be constantly running these threads that they've never run before
[2040.44 → 2042.68] around how long is this going to last?
[2042.68 → 2043.80] Like, what can I expect?
[2043.94 → 2046.64] You know, like, am I going to financially be able to pull through?
[2047.12 → 2048.82] The kids are distracting me.
[2048.90 → 2051.26] You know, I'm not in a quiet environment and things like that.
[2051.28 → 2054.42] It's just, you're not necessarily being set up for success.
[2054.42 → 2060.82] And so if you do have days when you just cannot dig out, that's completely to be expected.
[2060.82 → 2062.12] And it's very unfortunate.
[2062.44 → 2067.44] But having, you know, if you are a manager, that is the most important thing to be able to
[2067.44 → 2072.96] communicate to your reports right now that yes, like accomplishing something every day
[2072.96 → 2077.96] at work will make you actually feel probably a lot more settled and a lot more distracted
[2077.96 → 2081.38] from the realities of what's happening right now that can help so, so much.
[2081.38 → 2087.38] But you can't necessarily perform at your optimum level every single day right now, if any day
[2087.38 → 2087.92] at all.
[2087.92 → 2091.44] And so that's something also that I want people to keep in mind.
[2091.44 → 2093.72] Yes, give yourself a little grace.
[2094.06 → 2098.28] This is a terrifying time along many dimensions.
[2099.10 → 2103.76] And there's, you know, the blessing is there are lots of things that, you know, lots of signs
[2103.76 → 2104.12] for hope.
[2104.36 → 2105.78] There's lots of good work being done.
[2105.88 → 2109.96] A lot of, you know, one of the things that I've seen about the working from home that
[2109.96 → 2113.96] I really liked is like, it can feel like, okay, stuff is shutting down, and we're going
[2113.96 → 2115.96] working from home and this is a terrible thing.
[2116.02 → 2120.46] But actually, this is a sign of hope because what this is doing is it is all of us showing
[2120.46 → 2127.08] social solidarity to create the opportunity for our healthcare workers and our scientists
[2127.08 → 2128.70] to beat this thing.
[2129.30 → 2133.24] You know, all of this social distancing and everything like that, it feels terrifying,
[2133.24 → 2137.96] but it is creating the possibility of winning against this thing in a way that is not as
[2137.96 → 2138.20] deadly.
[2138.38 → 2139.84] And so, so many more people survive.
[2140.08 → 2142.62] So, you know, it's, it's super hard.
[2142.70 → 2143.42] It's terrifying.
[2143.42 → 2149.76] But just by doing this, you are helping not just yourself, but everyone around you.
[2150.34 → 2154.90] And you are helping the elderly and the older folks and the more at risk folks.
[2155.10 → 2160.16] And at risk can, can be, you know, lots of people are not obviously at risk, and who are
[2160.16 → 2160.84] at risk, right?
[2160.90 → 2164.40] It's somebody can look completely healthy and have an underlying condition that puts them
[2164.40 → 2165.02] at risk for that.
[2165.08 → 2167.90] So you are helping literally save your friends and coworkers.
[2167.90 → 2170.94] But yeah, that's a lot of emotional burden to bear.
[2171.30 → 2174.56] Give yourself the grace that, yeah, you might not be at your best.
[2174.94 → 2175.46] It's okay.
[2176.22 → 2180.50] On the communication front, I will just go ahead and plug a previous episode that we did because
[2180.50 → 2186.00] we did an entire episode on communication skills, which didn't assume remote work.
[2186.18 → 2192.28] But when you're giving communication skill advice to software developers, you do assume a
[2192.28 → 2196.36] certain amount of remoteness and text-based communication and all these kinds of things.
[2196.36 → 2200.00] And K-Ball, you led that episode, and it was one of my favourites of the last year.
[2200.12 → 2203.40] It's called Remember People Are Humans, episode 93.
[2204.38 → 2206.26] And we will put that one in the show notes.
[2206.36 → 2210.78] So if you want more on communicating while you're at home or with people in remote places,
[2211.34 → 2214.90] we did a whole hour, maybe hour 20 on that on a previous episode.
[2214.90 → 2228.02] We move fast and fix things here at Changelog thanks to Rollbar.
[2228.36 → 2231.40] We've been using Rollbar for years, and they've never let us down.
[2231.80 → 2236.30] Just recently, they rolled out a brand-new user experience with three major steps forward.
[2236.64 → 2241.86] First, they've adopted powerful and consistent multi-project views across the entire user workflow.
[2241.86 → 2247.04] You can get intelligent, real-time alerts on errors across microservices in a single view
[2247.04 → 2248.92] using their new multi-project filter.
[2249.36 → 2252.02] Whether you're looking at the main dashboard, the items view, or versions,
[2252.20 → 2253.50] you'll only see what you care about.
[2254.22 → 2258.90] Next, users now have their own personal workspaces with powerful filters for projects,
[2259.14 → 2262.00] environments, and frameworks that persist across all views.
[2262.80 → 2268.08] Finding new errors is also faster and easier with improved timeframe and new or reactivated filters.
[2268.08 → 2272.70] Finally, get insights on data across multiple projects in one go.
[2273.22 → 2278.06] Run queries and correlate data across services with the multi-project functionality in RQL.
[2279.06 → 2283.10] Visualize those results and look for trends or anomalies easily with graphs.
[2283.72 → 2287.10] Check it out and see what you think at rollbar.com slash changelog.
[2287.48 → 2290.68] Once again, that's rollbar.com slash changelog.
[2290.68 → 2320.66] So one of the hardest things about working from home is putting yourself to work.
[2320.66 → 2322.14] That's no surprise, right?
[2322.26 → 2325.20] Like, well, it's hard to work because I'm at home and I don't want to work at home.
[2325.56 → 2330.44] The surprising thing is sometimes just as hard is stopping working.
[2330.66 → 2336.42] Once you finally get it going, you got to stop because if you don't stop, then you're going to die, I guess.
[2336.50 → 2336.74] I don't know.
[2336.82 → 2337.90] Eventually you have to stop to sleep.
[2338.04 → 2340.88] But, you know, it's a hard time to separate that out.
[2341.08 → 2345.06] And so we want to talk about how you not work when you're at home.
[2345.06 → 2349.32] Because if your home is where you work, and you're at home, you're supposed to be working.
[2349.56 → 2350.86] But you're not supposed to be working all the time.
[2351.52 → 2352.54] How do you all deal with that?
[2353.34 → 2353.60] Kids.
[2355.16 → 2357.42] For me, dinner is my hard stop.
[2357.78 → 2358.86] Dinner is your hard stop, baby.
[2359.56 → 2371.26] I'm very food motivated, and I'll make sure that I have to spend time preparing so that, you know, if you just reheat something in the microwave, which is totally valid because you either have ordered takeout or you have something in the freezer that you thawed out.
[2371.26 → 2376.82] But that two minutes is not enough for your brain to be like, yeah, okay, I'm done.
[2376.98 → 2378.96] It's going to rush back to the computer and keep working.
[2379.14 → 2383.62] So for me, having to just do a few extra steps to prepare dinner gets me out of the mindset.
[2383.94 → 2387.52] So when I eat and come back, I'm like, no, I'm not going to start work.
[2387.60 → 2390.56] Like I've been not working for like a good half hour to 45 minutes now.
[2390.92 → 2393.10] And so that's been the thing that's rescued me.
[2393.10 → 2398.06] I always fall for it every time I have like leftover curry that I made from yesterday and reheat it.
[2398.06 → 2401.88] I'll always just go back to my desk and eat it there, which is really a bad habit.
[2402.76 → 2407.54] I was going to say, try not to eat at your desk if at all possible, but I'm guilty of it.
[2407.58 → 2408.30] Don't look at my desk.
[2409.54 → 2410.96] Do as I say, not as I do.
[2411.78 → 2411.98] Yeah.
[2412.02 → 2414.10] I think that's the single most powerful thing you're right in.
[2414.12 → 2417.06] Just donate at your desk because it will enforce breaks.
[2417.58 → 2417.78] Yeah.
[2418.28 → 2420.24] But sometimes it's just so easy to be like, oh, I'll just work.
[2420.32 → 2422.80] And then, you know, during this meeting, I'll eat while I'm on mute.
[2423.24 → 2425.36] And it sucks too, because you don't enjoy the food.
[2425.44 → 2426.94] You're just totally distracted while you're eating.
[2426.94 → 2430.04] Yeah, it's more like just putting fuel into the container, you know?
[2431.34 → 2432.76] It's like just filling up with gas.
[2433.18 → 2440.76] I will say, if you are, for example, splitting childcare duties with someone, you know, that's a bad practice for general remote work.
[2440.76 → 2444.90] But if you're working in compressed time, that is one way you can compress time a little bit.
[2445.26 → 2447.38] Yeah, that's true.
[2447.58 → 2449.26] Eat while on a meeting or something like that.
[2450.60 → 2453.44] One point that I would put is set yourself a schedule.
[2453.44 → 2458.48] Like, Jared brought up the nice thing that your schedule can probably flex a little bit more because you're at home.
[2458.66 → 2460.48] But that doesn't mean it should flex infinitely.
[2462.14 → 2467.50] You know, and I think piggybacking something he said, like, figure out what are your body rhythms?
[2467.74 → 2470.02] When are you most productive?
[2470.16 → 2472.02] If you're most productive at night, great.
[2472.18 → 2473.08] You can work at night.
[2473.22 → 2475.02] Don't feel like you can't do that.
[2475.08 → 2477.44] If you're most productive early in the morning, work early in the morning.
[2477.44 → 2480.02] But set yourself an on and an off.
[2480.54 → 2481.72] And when you're on, be on.
[2481.88 → 2483.90] And when you're off, actually be off.
[2484.30 → 2485.44] Stop checking your email.
[2485.66 → 2486.84] Stop looking at work slack.
[2487.02 → 2488.12] Stop doing all these things.
[2488.76 → 2490.36] And unplug and do something else.
[2490.60 → 2498.60] And that's where some of that, like, having a to-do item that is not just work-related, but is like, here are the things I need to do in my life, can help you.
[2498.64 → 2500.94] Because then when you unplug, it's not like, oh, what do I do now?
[2501.02 → 2503.68] Well, I'm just going to scroll through news and get terrifying updates.
[2503.68 → 2506.90] Or I'm going to scroll through your work slack or whatever.
[2507.00 → 2508.14] It's like, no, I had these things.
[2508.20 → 2509.42] I got to get done for my life.
[2509.90 → 2509.98] Yeah.
[2510.92 → 2516.54] I think that that does lend a little bit of professionalism to your situation as well.
[2516.76 → 2519.46] Because, you know, that's something that you typically do is you work.
[2519.78 → 2522.34] We're creatures of habit, so we work a set time.
[2522.74 → 2527.28] And if you're only working during those set times and not making exceptions, I think that comes off as being more professional.
[2527.54 → 2530.26] And, you know, you will get things done during these hours.
[2530.70 → 2533.04] And you're setting those levels of expectation.
[2533.04 → 2535.20] And then, as you said, you can enforce that.
[2535.62 → 2544.22] One thing that I do is I don't have work-related stuff on my iPad or on my iPhone so that I don't get Slack messages except for a computer.
[2544.50 → 2549.50] I think the overarching goal is to have a work mode and to have a life mode.
[2549.70 → 2559.26] And then to organize yourself so that it's clear and distinct separation of church and state, so to speak, of work and life.
[2559.60 → 2561.98] And so not work-life balance, but work-life separation.
[2561.98 → 2564.12] Maybe you need some social distancing from your work.
[2564.12 → 2571.76] And so I think the two best tools we have is the location of our work and the schedule, the things we've been talking about.
[2572.32 → 2575.76] So you need to have a distinct location, and you need to have a distinct schedule.
[2575.88 → 2577.94] Whatever the location is, whatever the schedule is, right?
[2578.34 → 2579.42] Organize it for yourself.
[2579.42 → 2581.70] But those things are the two strongest indicators.
[2581.90 → 2585.10] Like for me, when I'm in my office, I'm working.
[2585.50 → 2587.62] And when I'm not in my office, I'm not working.
[2588.26 → 2594.54] Like those, that's not always true as we are admitting that sometimes things do blend and merge.
[2594.54 → 2600.52] But that's a very strong indicator, especially if you do have other people around you who have to deal with this.
[2600.56 → 2601.88] For my children, I'm in my office.
[2601.98 → 2602.46] I'm working.
[2602.70 → 2603.98] Like for them, that's an indicator.
[2604.50 → 2605.98] And then also, I create a schedule.
[2606.24 → 2608.68] If it's this time of the day, I'm working generally.
[2609.56 → 2610.56] So like that's very strong.
[2610.62 → 2613.62] And when that time is done for Size, when it's dinner time, like that's it.
[2613.94 → 2614.98] I'm done for the day.
[2614.98 → 2624.02] And so that, I think, is really the goal is to be able to have modes and then to organize yourself, so those modes are obvious and useful.
[2624.90 → 2636.82] And I think barring any hard and fast limits like kids coming home, for example, or spouse coming home, something like that, something that you can do kind of like what I mentioned, getting started for the day, coming up with a list.
[2636.82 → 2638.82] That's kind of like a routine that you go through.
[2638.82 → 2643.32] You can have a shutdown routine as well where maybe you tidy things up around your desk.
[2643.32 → 2647.06] Maybe you start working on what you want to accomplish tomorrow.
[2647.26 → 2649.20] You get code committed, things like that.
[2649.60 → 2654.64] And then from there, you've kind of used that as a transition period between working and not working.
[2655.18 → 2665.34] This reminds me of a section from Cal Newport's book where he was talking about the sort of has this like really dorky verbalization when he's done for the day.
[2665.48 → 2666.76] And I thought it was really cute.
[2666.88 → 2669.60] I'm trying to remember what it was, but I don't.
[2669.82 → 2671.46] And the book was about focus.
[2671.46 → 2675.02] I'm also trying to remember the title, but I'm sure one of you would be able to remember it.
[2675.14 → 2676.58] It's not his minimalism one.
[2677.14 → 2677.74] I don't know.
[2677.80 → 2680.40] I'm just trying to imagine different like sign off phrases.
[2680.58 → 2682.86] I would say like, well, all done for now.
[2683.46 → 2685.98] It was something like shut down or something like that.
[2686.06 → 2688.12] It was like system shut down, or it was something like that.
[2688.18 → 2689.14] And he would verbalize it.
[2689.16 → 2690.06] And he said, deep work.
[2690.28 → 2690.80] That's the book.
[2690.80 → 2692.60] So the book is called Deep Work.
[2692.80 → 2697.38] And he talks about trying to just do knowledge work with much, much greater focus.
[2697.98 → 2707.90] And part of that is also being able to switch off so that next time that you switch back on, you're all in rather than having this kind of blurry fatigue from not quite switching off.
[2708.14 → 2712.14] And so I forget what his verbalization was, but it was like really cute and dorky.
[2712.22 → 2714.50] And he acknowledges that, but he said it was really helpful for him.
[2714.92 → 2715.34] That's cool.
[2715.74 → 2717.12] I need to come up with my own sign-off.
[2717.12 → 2719.80] So here's another challenge.
[2719.98 → 2729.58] Add a wrinkle to our struggle with work-life separation slash balance is as knowledge workers, as web people, people who work on the web.
[2730.24 → 2732.30] Many of us and many here as well.
[2732.76 → 2735.78] Our hobbies are also related to these technical things.
[2735.78 → 2738.46] Like we enjoy writing software.
[2738.60 → 2740.42] We enjoy being on the internet.
[2741.60 → 2744.20] Maybe we even like live stream as a hobby, right?
[2744.20 → 2747.74] Which is like very much also similar to some of the stuff you might do for your work.
[2748.28 → 2757.22] How do we manage that relationship when it comes time to separating from your work is like, well, I like to be doing this stuff.
[2757.38 → 2765.30] And so it's really hard to stop, especially if you have fortunate enough to have work that is really energizing and enjoyable and mentally stimulating, right?
[2765.34 → 2768.94] Like solving that problem feels perfect.
[2768.94 → 2771.28] And so I don't care if it's past dinner time.
[2771.34 → 2772.60] I just realize how to solve it.
[2772.70 → 2777.00] Like how do you all deal with that separation and the ability to unplug that or not?
[2777.90 → 2779.16] I think ebb and flow.
[2779.56 → 2786.74] Like if I end up with a night like that, I'll either try and reschedule meetings or if I don't have any meetings the next day, I'll just enjoy a really luxurious slow morning.
[2786.74 → 2788.90] So for me, it tends to be tit-for-tat.
[2789.50 → 2799.70] And I think that that sort of system happened as a result of me working remotely for Microsoft where sometimes I would be speaking at meetups at night.
[2799.94 → 2806.34] And so we were just expected to rebalance how much we worked that week based on the fact that, you know, we were working often until 10 p.m.
[2806.74 → 2807.44] You know, that day.
[2807.44 → 2813.54] So we'd either sleep in the next morning or we would have like a slower, you know, start to that specific day.
[2813.74 → 2819.44] And for me, the fact that you're trying to always balance that actually makes you very aware of when you are overworking.
[2820.14 → 2825.04] And so it means that you don't end up burning out because you're affording yourself that extra time, if that makes sense.
[2825.58 → 2828.38] So being strict about that has really helped me a lot.
[2828.38 → 2839.86] But the other thing is having equally exciting hobbies so that you can actually, you know, you can accomplish the work thing, but you know that you also have this really exciting thing the next day that you can switch off for.
[2839.94 → 2841.28] That really helps a lot, too.
[2842.06 → 2843.86] Yes, definitely.
[2843.86 → 2845.88] It ties into a concept that I had.
[2846.24 → 2849.52] I used to struggle greatly with work-life balance.
[2849.52 → 2863.70] And I think the biggest reason was I had this perception of it being something where, like, balance was, oh, I'd relax into this thing where it was like, okay, I'd have my time at work, and then I'd relax, and, like, things would all feel good.
[2863.88 → 2869.84] And that never worked for me because work is always pulling, and it always stretches because my work is interesting, like you all's work.
[2869.98 → 2872.60] And it just, it will pull more and more of your time.
[2872.60 → 2884.46] When I re-evaluated balance to be a dynamic tension, it got me thinking about, okay, whatever I'm doing outside of work has to be pulling equally hard to how work is pulling.
[2884.80 → 2886.34] It's got to pull my attention.
[2886.46 → 2887.82] It's got to pull for my time.
[2888.46 → 2892.68] And then the thing that really did it for me, like, more than anything, was kids, right?
[2892.90 → 2896.56] Because kids will, they will pull harder than anything else in your life.
[2897.98 → 2899.14] They will literally pull.
[2899.14 → 2900.66] They will literally pull, yes.
[2900.66 → 2906.42] So that shifted me further, and I'm not saying you can or should have kids in response to this change.
[2906.92 → 2913.16] That's a choice that has many additional factors that go into it, though all this time stuck in at home with partners.
[2913.74 → 2916.98] I was going to say nine months from now, we might have the coronavirus generation.
[2917.42 → 2919.30] I think there's twofold, right?
[2919.38 → 2926.06] So one of the things that they saw in Wuhan was when they, or in some parts of China, was when they started reducing the restrictions.
[2926.06 → 2928.94] There were a bunch, there was a surge in divorce filings.
[2928.94 → 2933.92] So, like, if you get stuck in that space, it's either going to kill your relationship or make it stronger.
[2934.04 → 2935.88] And maybe there will be a bunch of divorces.
[2936.02 → 2937.92] And then on the other side, a bunch of new babies.
[2938.08 → 2938.46] I don't know.
[2939.04 → 2939.66] But anyway.
[2939.66 → 2943.76] I've also seen, unfortunately, a rise in domestic violence, which is terrifying.
[2944.26 → 2945.18] That is terrifying.
[2945.30 → 2945.82] But yeah.
[2946.44 → 2948.08] Anyway, that kills the mood there.
[2948.14 → 2948.44] Keep going.
[2948.44 → 2952.92] Well, and I think there are, I've seen some resources out there.
[2953.00 → 2956.80] Like, if you're in that type of situation, or you're afraid for that, there are resources that can help.
[2957.08 → 2957.96] I don't know.
[2958.70 → 2960.46] Maybe we can include a link for that.
[2960.54 → 2962.46] It's off-topic for our show, but.
[2962.50 → 2962.76] Yeah.
[2963.16 → 2963.72] That'd be good.
[2964.02 → 2964.32] But yeah.
[2964.38 → 2965.78] So where was I going?
[2965.86 → 2966.68] Oh, you need something.
[2966.86 → 2970.50] Even if it's not kids, you need something that's going to pull you out of that work mode.
[2971.42 → 2972.10] Love that.
[2972.24 → 2972.94] 100% agree.
[2974.04 → 2974.98] Nick, anything to add?
[2974.98 → 2977.72] Yeah, no, I just echo what everyone is saying.
[2977.92 → 2979.84] It's important to try and set those boundaries.
[2981.00 → 2983.14] And there are lots of different ways to do that.
[2983.90 → 2985.52] They're all different right now.
[2985.98 → 2988.90] For me, it's my wife has to get her work done.
[2988.96 → 2991.56] So I have to finish what I'm doing quickly.
[2991.94 → 2996.72] And there's no going back because she has to get work done, and our kids have to be looked after.
[2997.06 → 2999.36] And so it's different for everyone.
[2999.58 → 3000.80] It's especially different right now.
[3001.44 → 3003.20] And just be aware of that.
[3003.20 → 3005.32] Everyone's going through lots of different things.
[3006.02 → 3008.98] Can I just say one off-topic thing?
[3008.98 → 3016.66] I'm very annoyed that Animal Crossing is launching in a couple of days and there's no online multiplayer.
[3016.90 → 3019.06] You have to do it in person with each other.
[3019.24 → 3023.32] And that was the worst timing for a game mechanic like that.
[3023.40 → 3027.66] And I'm so disappointed because I was going to play locally with someone on their island.
[3027.76 → 3028.44] And now I can't.
[3029.14 → 3030.26] That sucks.
[3030.26 → 3033.30] Nintendo, please fix this just for us.
[3033.36 → 3041.20] I realize that as a programmer that is asking for the world, it's like, just completely reprogram a whole new dynamic into the game and launch it next week.
[3041.24 → 3041.82] Cool, thanks.
[3042.04 → 3048.72] But yeah, I'm so sad because I think that online community is now more important than ever.
[3048.72 → 3052.62] And having something exciting like that to kind of like end your day with.
[3052.72 → 3054.42] It's like, okay, it's time for Animal Crossing now.
[3054.76 → 3056.92] That's kind of put a damper on things for me a little bit.
[3057.58 → 3057.96] Sad but true.
[3058.08 → 3058.58] Sad but true.
[3058.70 → 3060.88] So let's turn now to some additional resources.
[3061.02 → 3064.86] Of course, we're not the end all be all talkers about this subject.
[3064.94 → 3067.70] As I mentioned, Go Time also giving their insights.
[3068.28 → 3072.50] People from around the web are sharing tips and tricks, advice, their thoughts.
[3072.50 → 3080.68] And so there are lots of other things out there and other people to listen to and to communicate with about this thing that we're all kind of going through right now.
[3080.94 → 3086.22] And so we thought we'd share a few resources here as we tail off the show that you can follow up with.
[3086.34 → 3088.04] Of course, everything's in the show notes.
[3088.04 → 3096.20] If you're listening not inside a podcast app, you can go to changelog.com slash js party slash 120 to find those notes.
[3096.50 → 3099.64] If you're in a podcast app, you know how to pop those show notes open.
[3100.18 → 3103.06] So let's do that now.
[3103.12 → 3110.24] And I'll share one here, a post which I'm working my way through right now by Justin Series of Test Double.
[3110.64 → 3112.62] It's called Remote But Not Alone.
[3112.62 → 3117.60] And Justin's entire firm Test Double has been remote since 2011.
[3118.78 → 3121.98] He is a smart guy with lots of good insights.
[3122.18 → 3132.22] So he has a very good post on the Test Double blog all about his thoughts on working remote both as a human, as an employee, and as a manager.
[3132.56 → 3136.06] So if you're in any of those perspectives, that's a good one to read.
[3136.22 → 3140.38] We'll put that one in there and definitely submit that as a follow-up resource.
[3141.48 → 3142.48] I'll put one in.
[3142.64 → 3146.90] I'm shouting out some of my amazing colleagues at the company I work for called Hume.
[3146.90 → 3151.16] Our company is focused on behaviour change and making work better for folks.
[3151.70 → 3153.94] And typically, we work with large enterprises.
[3153.94 → 3165.08] But when all this remote work all of a sudden came out, a bunch of the scientists of the company quickly focused on building out a set of resources for folks who are working from home for the first time.
[3165.08 → 3169.20] And the way it works is you sign up with an email, and you get a nudge every couple days.
[3169.46 → 3174.02] It's building on this concept of nudges for behaviour change, which is a big thing coming out of psychology.
[3174.42 → 3178.72] And it gives you short, scientifically-based suggestions to help you work from home.
[3179.30 → 3180.94] So I'll include a link to that.
[3180.94 → 3183.70] But it's super cool stuff.
[3183.82 → 3190.12] And every one of these is backed in science and research, which is part of what I really appreciate about what the company is doing.
[3190.20 → 3197.58] We're trying to make life better, but do it in a way that is validated based on real research on human beings, not just opinions.
[3197.82 → 3200.42] And we make some software and see how it works.
[3201.30 → 3201.54] Awesome.
[3201.90 → 3202.40] Any others?
[3202.40 → 3203.90] Yeah, I'll throw out.
[3204.12 → 3206.32] This has been kind of what we alluded to.
[3206.70 → 3208.26] A lot of things are getting cancelled right now.
[3208.72 → 3216.68] It'll be interesting to see, in terms of conferences and things, what conferences come back, how that will look, how the conference landscape will look.
[3216.88 → 3222.60] But in the meantime, there are some folks doing some cool stuff with online conferences and experimenting with that.
[3222.60 → 3230.88] And one of them is by a guest on this podcast before, Fred K. Scott from Pike, who is putting on ESNextConf.
[3230.88 → 3233.60] And it's a five-day conference with 12 speakers.
[3233.74 → 3237.64] So it's kind of spread out for remote, optimized for remote over five days.
[3238.26 → 3242.04] And there are a lot of different conferences like that as well.
[3242.16 → 3244.06] So definitely, you're not alone.
[3244.14 → 3252.28] And if you want to continue that learning, continue that networking, it'll be interesting to see how networking and things like that work with online-only conferences.
[3252.76 → 3254.64] But I'm excited to see where we go.
[3255.02 → 3257.22] I'm a bookworm, so I have three books to recommend.
[3257.22 → 3261.70] The first one is Cal Newport's Deep Work, which I mentioned before.
[3262.70 → 3266.92] And the next one is Jenny O'Dell's How to Do Nothing.
[3267.72 → 3269.66] Jenny O'Dell is one of my favourite speakers.
[3269.98 → 3273.18] She speaks at IO Festival over the last few years.
[3273.50 → 3274.70] And she's an artist.
[3274.86 → 3282.54] And she talks about the fact that the new hustle culture and things like that are just constantly tearing at our personal time, our personal space, our mental well-being.
[3282.54 → 3286.72] And I think that right now I'm seeing a lot of that chatter on Twitter.
[3286.88 → 3290.18] It's like, this is time for your side project now that you're quarantined.
[3290.28 → 3292.30] And this is the time to do this and that.
[3292.46 → 3297.40] And just not allowing people to ever take a break because things are crappy, you know.
[3297.46 → 3299.72] And so I think that this book is particularly relevant.
[3300.02 → 3302.42] It's very popular and has really great reviews.
[3302.42 → 3306.04] And then also Contact Book by Carl Sagan.
[3306.04 → 3312.10] I'm seeing a lot of parallels in this book compared to what we're seeing now.
[3312.38 → 3326.60] And so, yes, it's a science fiction book, and it has nothing to do with a virus worldwide, but it has to do with worldwide cooperation, the breakdown of barriers between science and religion, as well as just watching different nations try to own different solutions.
[3326.60 → 3342.08] I think that there are just so many things that we're seeing, and I think that Carl Sagan kind of thinks about this stuff the right way, and you might actually find it quite comforting, you know, to kind of imagine ideologically, like, what would be the greatest way that we could deal with this kind of thing right now.
[3342.24 → 3345.40] So, I think that those three books are particularly relevant.
[3345.78 → 3355.30] You know, there's the work, but there's also, like, how do you then switch off and just, like, treat yourself nicely given that this is just quite an unprecedented experience to go through in your lifetime.
[3355.30 → 3356.90] Well said.
[3357.04 → 3359.62] That is our show for this week.
[3359.68 → 3371.18] Hey, if you're out there, and you're feeling particularly lonely, particularly isolated during this time, we hope this podcast and the podcast that we produce plays a small role in keeping you connected to us.
[3371.24 → 3374.88] Of course, you can connect directly with us, hang out in Slack, be part of the Changelog community.
[3375.06 → 3376.00] Everyone is welcome here.
[3376.08 → 3376.96] There are no imposters.
[3377.68 → 3381.34] So, that's all free and available to you at changelog.com slash community.
[3381.88 → 3383.02] We'll talk to you next time.
[3385.30 → 3387.66] Thank you for listening to JS Party.
[3387.98 → 3389.76] We appreciate you spending time with us.
[3390.28 → 3394.62] If this show has helped you, entertained you, or brought you joy in any way, please tell a friend.
[3394.96 → 3398.56] For me, podcasts are a great way to stay connected in times of isolation.
[3399.18 → 3403.38] As I mentioned on the show, our friends at Go Time also recorded a work-from-home episode.
[3403.98 → 3407.94] It's in your show notes and at changelog.com slash Go Time slash 123.
[3408.26 → 3410.46] Check it out if you can't get enough on this topic.
[3410.46 → 3416.18] Thanks to my friends Size Hinton, Nick Needed, and K-Ball for hanging out with me on this episode.
[3416.54 → 3419.02] And to Break master Cylinder for providing all of our beats.
[3419.54 → 3421.04] We have some awesome sponsors.
[3421.16 → 3421.94] Please support them.
[3422.14 → 3422.90] They support the show.
[3423.30 → 3426.44] Special thanks to Linde, Rollbar, and Vastly for hooking us up.
[3426.92 → 3427.94] That's all for this week.
[3428.18 → 3429.06] We'll talk to you next time.
[3429.06 → 3459.04] We'll be right back.
[3459.06 → 3461.66] It's just like a constant drone, though.
[3461.74 → 3464.52] It's not like the really annoying, leaf-blowing.
[3465.58 → 3466.06] Yeah, exactly.
[3466.20 → 3470.74] Constant drones are easy to gate out or noise reduce.
[3471.72 → 3475.86] Yeah, they sound more like whippersnappers, which is what we call weed whackers.
[3475.86 → 3476.34] I was going to say.
[3476.76 → 3477.38] And things like that.
[3477.40 → 3478.42] Internationalize that, please.
[3478.42 → 3479.12] It's a wonderful name.
[3479.28 → 3479.84] Whippersnapper?
[3480.04 → 3480.86] Because it whips and it snips.
[3481.06 → 3481.88] Dude, I love that.
[3481.90 → 3482.46] I love that.
[3483.10 → 3484.20] It whips her.
[3484.34 → 3485.52] In a wonderful way.
[3486.36 → 3488.22] I really love some Australian words.
[3488.32 → 3493.28] And I didn't realize how colloquial they were until I moved here, which was really great.
[3493.48 → 3495.66] And whippersnapper is one that Americans absolutely love.
[3495.74 → 3497.94] It's just like a universal joy-bringing word.
[3497.94 → 3498.30] That is.
[3498.66 → 3499.76] Well, we say whippersnappers.
[3500.02 → 3503.48] Or at least in Nebraska, my parents used to say whippersnappers.
[3503.48 → 3506.76] And that is like, you know, mar mint little kids.
[3506.98 → 3507.98] Like, yeah, little whippersnappers.
[3508.24 → 3509.22] Like, when they're causing trouble.
[3509.72 → 3511.22] I don't know where that comes from, though.
[3511.46 → 3512.12] But whippersnapper.
[3512.42 → 3512.58] I've heard that, too.
[3512.92 → 3513.56] You've heard that one?
[3513.56 → 3516.38] I feel like whippersnapper makes infinitely more sense.
[3516.62 → 3518.78] Even though I've heard whippersnapper a lot.
[3519.12 → 3521.08] Yeah, it's like somebody who makes noise, maybe.
[3522.38 → 3524.94] But whippersnapper is like, dude, that's so good.
[3525.26 → 3525.76] It's brilliant.
[3526.10 → 3526.64] I want to use it.
[3526.64 → 3531.94] It's much better than saying, like, trim the hedges or what do we say?
[3532.42 → 3533.84] I'm going to go weed eater.
[3533.84 → 3534.20] Weed whacker.
[3534.56 → 3535.34] Yeah, weed whacker.
[3535.62 → 3536.12] Weed eater.
[3536.98 → 3537.56] I'm going to start saying it.
[3537.56 → 3538.30] I'm going to go whippersnapper.
[3538.30 → 3538.38] I'm going to go whippersnapper.
