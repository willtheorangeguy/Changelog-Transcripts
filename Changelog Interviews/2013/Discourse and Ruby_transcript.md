[0.00 --> 18.14]  This is the Change Log and I'm your host, Adams Dekowiak.
[18.48 --> 23.00]  We're a member-supported blog and podcast that covers the intersection of software development
[23.00 --> 24.32]  and open source.
[24.68 --> 28.86]  We shine a spotlight on what's fresh and new in open source.
[28.86 --> 35.80]  Tune in live every Tuesday at 3 p.m. Pacific, 6 p.m. Eastern at thechangelaw.com slash live.
[36.14 --> 42.28]  And this is episode 0.8.6, recorded April 23, 2013.
[42.88 --> 46.80]  We're joined by Jeff Atwood, also known as Coding Horror.
[47.56 --> 50.62]  If you found this show on iTunes, we're also on the web at thechangelaw.com.
[50.74 --> 54.14]  And if you're on Twitter, follow the Change Log, because that's us.
[58.86 --> 61.50]  In California.
[61.50 --> 66.30]  Welcome back, everybody.
[66.38 --> 67.94]  We're here live again.
[68.02 --> 68.66]  It is Tuesday.
[68.96 --> 70.06]  This is the Change Log.
[70.24 --> 71.86]  It is the time to have some fun.
[71.92 --> 73.18]  We got some awesome people with us.
[73.62 --> 75.98]  The first person in that lineup is Andrew Thorpe.
[75.98 --> 76.72]  Sir, how are you?
[77.04 --> 77.74]  I'm doing good.
[77.94 --> 78.42]  How are you doing, Stack?
[78.64 --> 81.94]  We're also joined back again because he is awesome, Kenneth Wrights.
[82.00 --> 82.48]  What's up, man?
[83.02 --> 83.80]  Not a whole lot.
[83.82 --> 84.16]  How are you doing?
[84.66 --> 85.74]  Not a whole lot, huh?
[86.74 --> 88.40]  Got to come on the show with a lot of energy, you know?
[88.50 --> 89.54]  That's how it works.
[89.70 --> 90.66]  Today's an amazing day.
[90.94 --> 93.32]  I actually have some Chipotle sitting right here, so I'm pretty excited.
[94.10 --> 94.42]  Nice.
[94.68 --> 96.10]  Chipotle is kind of nice.
[96.40 --> 99.04]  Kenneth, you should be excited that he said Wrights and not Reitz this time.
[99.06 --> 99.68]  I'm very excited.
[100.12 --> 100.80]  I listen.
[100.88 --> 101.78]  I listen very well.
[102.96 --> 107.86]  And the silent partner here so far, I'm sure he won't be too silent during the show.
[107.94 --> 112.00]  It's going to be a lot of fun getting into some of the great topics we have lined up.
[112.00 --> 114.00]  But Jeff Atwood is with us.
[114.08 --> 114.80]  Jeff, what's up, man?
[114.82 --> 115.28]  How are you?
[116.00 --> 116.24]  Hi.
[116.38 --> 117.28]  Great to be here on the show.
[117.48 --> 121.88]  I'm excited to be actually building an entire project that's open source, finally.
[122.00 --> 122.30]  Yeah.
[122.60 --> 125.30]  And do you come on live podcasts often?
[126.32 --> 127.16]  I've been on a few.
[127.26 --> 127.44]  Yeah?
[127.62 --> 129.54]  Which shows have you done recently?
[129.70 --> 130.32]  Just kind of curious.
[130.60 --> 131.64]  Oh, gosh.
[132.06 --> 134.64]  I mean, by recently, I mean maybe once every four months.
[134.94 --> 138.06]  So you're kind of making me dig through the old memory facts here.
[138.56 --> 139.86]  Gotcha, gotcha, gotcha.
[139.86 --> 140.44]  I have done it.
[140.54 --> 141.02]  I have to look it up.
[141.02 --> 147.48]  So, Jeff, I don't want to assume that your moniker, Coding Horror, goes without knowing who you are.
[147.62 --> 150.64]  So is there anybody out there who doesn't know who you are that might be listening to the show?
[150.64 --> 152.74]  I'm sure it's possible.
[152.84 --> 153.18]  You think?
[153.18 --> 155.44]  I think it's good to have intros, yeah.
[155.44 --> 158.08]  So for those who may not know who you are, who are you?
[159.10 --> 166.42]  Well, I'm a long-time blogger at codinghorror.com and co-founder of Stack Overflow and Stack Exchange.
[166.96 --> 171.70]  And that's how most people who would know me would find me.
[172.64 --> 182.14]  And then now I'm doing this open source project, Discourse, which is essentially a next generation forum reboot that's totally open source and free to everyone.
[182.14 --> 184.74]  Free to everyone.
[184.96 --> 186.44]  Well, yeah, open source is awesome.
[186.62 --> 187.64]  I'm kind of curious.
[187.96 --> 190.40]  I'm sure, Andrew, you've got tons of questions lined up.
[191.30 --> 197.76]  But, you know, there was a number of, I guess, different alternatives out there in the past.
[198.74 --> 204.02]  You know, from way back in the day, you can go back as far as, like, VB bulletin boards from back in the day.
[204.34 --> 207.04]  And then even things like Convor.
[207.12 --> 208.38]  Was it Convor or Conervor?
[209.18 --> 209.90]  Never remember.
[210.04 --> 211.18]  Convor was more of a chat system.
[211.18 --> 211.58]  Yes.
[212.22 --> 215.30]  It's kind of a, yeah, I guess you can kind of mix the lines there.
[215.34 --> 225.36]  I'm just kind of curious what took you from Stack Overflow, Stack Exchange, and that whole, as you had put it, city, software city.
[226.36 --> 230.82]  How you got in from that to this, to Discourse?
[231.48 --> 231.82]  Sure.
[232.16 --> 233.44]  I'd love to talk about that.
[233.44 --> 238.40]  So Stack Overflow and Stack Exchange, we launched that, we started building that in early 2008.
[238.40 --> 242.66]  And we started by researching sort of what was the problem.
[242.66 --> 249.96]  So a lot of the stuff I do is about fixing problems on the Internet because I want the Internet to be really good.
[250.46 --> 254.86]  And the problem that I had as a programmer was that I would search for stuff as a programmer.
[255.00 --> 258.56]  You know, I have an error or something I have a problem with I need background on.
[258.88 --> 259.54]  And I would search for it.
[259.54 --> 264.58]  And I would just, as Joel Spolsky always says, page fault in the information I need at the time that I need it.
[265.06 --> 268.24]  I wasn't, I love programming books and I have a ton of programming books.
[268.24 --> 282.02]  But when you just want a really specific answer to the problem that's facing you in your editor or your interpreter, a lot of times it's easier to just, like, search for something really fast to get you moving along and on to solving your problem.
[282.40 --> 286.62]  So when I did this, I would often get, sometimes I got blog hits, which are usually good.
[287.04 --> 294.12]  And that's actually one of the reasons I started my own blog in 2004 was that I noticed that I was getting really good information from blogs.
[294.12 --> 302.32]  And this made me think of them as not personal diaries, but as a way to publish really useful information to other people in the world.
[303.10 --> 306.72]  And when I didn't get blogs, sometimes I would get forum results.
[306.80 --> 309.02]  And the forum results were very, very problematic.
[309.82 --> 312.02]  I mean, the list of reasons is enormous.
[312.28 --> 314.82]  But first of all, it's hard to even find information on a forum.
[315.00 --> 318.80]  Like, you land on a page, which is, you know, 20 posts, right?
[318.84 --> 321.92]  Some pagination number of posts on the page.
[321.92 --> 324.76]  And you don't know if the answer is on that page.
[324.76 --> 327.08]  It could be on page one of 20.
[327.66 --> 328.16]  Or if it's current.
[328.84 --> 329.90]  Or it's even incurrent.
[330.00 --> 331.82]  I mean, the list of problems is just enormous.
[332.02 --> 333.00]  Like, it's slow to load.
[333.16 --> 335.18]  It's slow to even tell you what's on the page.
[335.24 --> 336.66]  It's usually filled with a bunch of ads.
[337.02 --> 342.52]  People have a bunch of ridiculous signature blocks that take up a ton of space on the page, making it even noisier.
[342.92 --> 344.12]  The layout is bad.
[344.32 --> 346.68]  It's like, you know, 1999 all over again.
[347.34 --> 350.06]  But if you're willing to dig, sometimes there was good information there.
[350.06 --> 352.72]  So you couldn't just discard the forum results.
[352.92 --> 360.04]  But as we got deeper into Stack Overflow, we realized we were building a Q&A system more than an actual discussion forum system.
[360.40 --> 362.58]  So we kind of stopped looking at forums.
[363.02 --> 366.64]  But forums were a big part of the impetus for Stack Overflow and Stack Exchange.
[366.86 --> 371.64]  In terms of getting to information efficiently, forums are not that, right?
[371.64 --> 380.08]  I mean, I think everyone realizes that if you want efficient answer to your question, forums are one of the worst places to go for that for variety of reasons.
[380.14 --> 381.12]  So we kind of stopped looking.
[381.22 --> 382.34]  We realized we're not building forums.
[382.40 --> 383.62]  We're building a Q&A system.
[384.28 --> 387.20]  And it turned out there were a ton of Q&A systems on the internet.
[387.38 --> 388.40]  Like Answer Bag.
[388.78 --> 389.80]  Of course, Yahoo Answers.
[389.92 --> 390.56]  Everybody's favorite.
[391.40 --> 396.88]  And just tons of Q&A systems that were like dark matter of the internet that I had never heard of but were very, very large sites.
[396.88 --> 398.94]  And we realized, well, hey, we're onto something.
[399.04 --> 400.06]  This is a model that works.
[400.16 --> 402.06]  It's just not well appreciated.
[402.44 --> 403.20]  So we polished it.
[403.26 --> 403.74]  We iterated.
[403.90 --> 407.54]  And we built a really nice Q&A system that got, of course, wildly, wildly popular.
[407.80 --> 418.36]  And then we extended it from just programming questions to sysadmin questions to computer enthusiast questions to cooking questions to gardening questions.
[418.36 --> 420.66]  All those sites are on the Stack Exchange network now.
[421.08 --> 423.74]  But the engine is very much a strict Q&A engine.
[424.12 --> 425.76]  And it's not about discussion.
[425.76 --> 431.30]  It's not about having a discussion about how your day went or what the coolest Java keyword is.
[431.60 --> 432.84]  It's about I have a problem.
[433.52 --> 437.34]  And I would like people to help me figure out an answer to my problem.
[438.02 --> 441.42]  But that leaves a lot of stuff on the table because there's a lot of topics.
[441.58 --> 443.36]  Like let me give you poker I think is a really good one.
[443.80 --> 445.18]  Stack Exchange has a poker site.
[445.42 --> 447.54]  But it's just utterly failing.
[448.20 --> 450.96]  And that's okay because they're experiments.
[451.12 --> 453.90]  All the Stack Exchange launches are community launches.
[453.90 --> 456.08]  Like the community told us, hey, we want a poker site.
[456.14 --> 457.02]  They voted for it.
[457.20 --> 458.50]  They said we would support it.
[459.34 --> 461.38]  It's like this whole democracy in action thing.
[461.44 --> 461.94]  So that's great.
[462.02 --> 463.02]  But not all of them work.
[463.12 --> 466.42]  And poker is not working like radically not working.
[466.68 --> 468.48]  It's like at the bottom of all the stats lists.
[468.76 --> 472.82]  Because poker isn't really about getting answers to your questions.
[472.82 --> 479.04]  Poker is a social game about hanging out and talking about what's the coolest cigar to smoke when you play poker.
[479.42 --> 481.24]  What's the best whiskey to drink when you play poker?
[481.54 --> 482.36]  What's the best table?
[482.44 --> 483.20]  What's the best cards?
[483.30 --> 485.96]  Like what are some good strategies for this hand that I have?
[486.60 --> 488.74]  These are not really concrete questions.
[488.94 --> 491.42]  These are more like social discussions.
[491.42 --> 499.56]  And the software for this is terrible because I also had startups come to me and say, hey, Jeff, we want your opinion about this thing you're building.
[500.04 --> 507.04]  And I always really dreaded these questions because, first, it's very unlikely I would ever go to their site just organically.
[507.24 --> 512.82]  The thing they were showing me is unlikely to appeal to me because people have a lot of different interests.
[512.94 --> 514.90]  And that just may not happen to be one of my interests.
[514.96 --> 517.84]  So it's already very, very artificial for me to look at their thing.
[517.84 --> 525.24]  So the first thing I would respond with is, well, why don't you ask your own community what they think of the thing that you're building?
[526.48 --> 529.36]  And first of all, that will tell you if you even have a community.
[529.62 --> 533.72]  If you don't have a community around the things you're building, then that's your problem.
[533.84 --> 534.58]  Go fix that.
[534.80 --> 536.50]  Don't ask me what I think about it.
[537.16 --> 540.34]  Figure out why nobody cares enough to give you feedback on your thing.
[540.78 --> 543.50]  Why is there no community forming around this thing that you're building?
[543.94 --> 544.88]  So go fix that.
[544.88 --> 547.82]  But the ones that came back to me and said, hey, that's a great idea.
[547.92 --> 548.72]  We have some community.
[548.84 --> 550.28]  We just don't have a good place for them to go.
[550.72 --> 551.58]  What should we do?
[552.72 --> 556.06]  The fundamental building block of an online community really is the forum.
[556.16 --> 558.74]  It's not a Q&A system because it's very, very directed.
[558.94 --> 561.52]  It's not about hanging out.
[561.58 --> 563.02]  It's not about socializing.
[563.52 --> 565.18]  It's just very, very directed.
[565.70 --> 568.80]  And that's not a good map to a lot of communities.
[568.80 --> 574.82]  So the software options that are out there for this are all, quite frankly, awful.
[575.16 --> 577.00]  I looked at them in good conscience.
[577.28 --> 579.16]  I hadn't looked at forums in four years.
[579.86 --> 581.20]  So in 2008, we looked.
[581.60 --> 582.32]  We researched it.
[582.76 --> 585.84]  And then in 2012, I was like, oh, these guys need a forum.
[585.96 --> 587.78]  Let me go find a forum to recommend them.
[588.20 --> 590.42]  And I just couldn't do it, man.
[590.66 --> 592.52]  All the forums were so bad.
[592.92 --> 594.32]  And I was like, this is embarrassing.
[594.32 --> 598.64]  I would be embarrassed to have this software associated with my software product, right?
[599.14 --> 600.58]  So I was like, this is a problem.
[601.04 --> 601.90]  This is a problem.
[602.14 --> 604.90]  And I still regularly get Google hits to forums.
[605.38 --> 609.74]  I would say it's rare that a day goes by that I don't get a search hit to a forum.
[610.08 --> 612.54]  They're regularly producing good information.
[613.14 --> 615.12]  It's just hard to get to that information.
[615.20 --> 620.42]  And when you do hit it, it's like when we said a couple seconds ago, whether it's current or not,
[620.42 --> 627.08]  the biggest question I ever do, and I'm like you whenever I hit, like I can't recall something I was trying to figure out an issue with.
[628.90 --> 630.06]  I can't remember what it was.
[630.14 --> 633.54]  But it was something where it was – I landed on a forum.
[633.90 --> 639.24]  It wasn't the right answer or it was the right answer, but I wasn't sure if it was dated or not dated.
[639.24 --> 646.18]  And you get there and you're just like – all these forums tend to look like obscure and even unusual looking.
[646.38 --> 649.56]  They have like weird looking headers and the graphics are like outdated.
[649.56 --> 654.20]  And somebody's got this dancing signature and it's just not the right situation.
[654.94 --> 656.12]  It doesn't feel like the modern web.
[656.36 --> 656.40]  No.
[656.50 --> 657.22]  That's not a problem.
[657.40 --> 660.60]  When you land on a forum and you feel like you've stepped back in time, I mean really 10 years.
[660.96 --> 664.82]  I mean I hate to say this, but it's like a full decade behind modern web design.
[665.04 --> 669.10]  It just doesn't feel like – it feels like you've landed – like you said, you've gone to someone's house.
[669.16 --> 670.14]  There's like wood paneling.
[670.22 --> 671.76]  There's like stuff from the 70s.
[672.30 --> 675.06]  It's like you've entered a different era of the world.
[675.06 --> 682.36]  We don't have to hang on this topic, but I want to say the thing I was trying to find was disabling the escape key to take you –
[682.36 --> 689.20]  Jeff, you're not a Mac guy, but when you take an app in full screen on the Mac, if you hit escape, it takes you out of full screen.
[689.30 --> 690.40]  And I was trying to disable that.
[690.46 --> 695.98]  It was driving me crazy because I have an app that requires me to hit the escape key to get at certain tools.
[695.98 --> 703.56]  So if you're listening and you know how to disable the escape key while in full screen on a Mac OS, then just let me know, please.
[703.68 --> 706.70]  I need a solution because the one I went to was what Jeff said.
[706.76 --> 709.94]  It was some obscure form that had nothing for me.
[710.02 --> 712.20]  The solution is to just not use full screen mode basically.
[713.36 --> 714.04]  Well, you know.
[714.20 --> 716.30]  I wanted to use logic in full screen.
[716.82 --> 719.74]  I'm a big fan of disabling the caps lock key.
[720.36 --> 720.60]  Ah.
[721.20 --> 721.44]  Yeah.
[721.68 --> 724.22]  Jeff, you've written a lot about keyboards and stuff like that, right?
[724.22 --> 725.22]  Jeff, you've written a lot about keyboards and stuff like that.
[725.22 --> 725.90]  Yes, I have.
[725.90 --> 727.54]  Do you want to tell us what your current setup is?
[729.76 --> 732.14]  Well, my current setup is – oh, gosh.
[732.20 --> 733.38]  I want to say Unicomp.
[733.60 --> 735.38]  It's the one – yeah, Unicomp.
[735.42 --> 737.76]  It's a buckling spring keyboard, so it's incredibly loud.
[739.12 --> 741.16]  So it's like the old IBM keyboard.
[741.18 --> 741.40]  Go ahead.
[741.40 --> 742.40]  Type a little bit for us.
[743.26 --> 745.20]  Yeah, give us a little audio preview of it.
[746.08 --> 746.40]  Okay.
[746.64 --> 749.48]  Well, I'll have to put my mic close to it, but here –
[749.48 --> 749.92]  It's beautiful.
[750.20 --> 750.36]  Ah.
[750.92 --> 751.28]  Beautiful sound.
[751.28 --> 752.32]  That is some fast typing.
[752.32 --> 753.16]  I'm using the –
[753.16 --> 754.02]  Well, I was just being random.
[754.22 --> 754.76]  I was pressing these.
[754.84 --> 755.74]  I wasn't actually –
[755.74 --> 756.12]  Yeah.
[756.94 --> 757.60]  That's funny.
[758.06 --> 758.14]  That's funny.
[758.14 --> 761.58]  So that's kind of the gist of kind of where you came from.
[761.70 --> 767.22]  So where in this – you know, if you could kind of just give us a intro to discourse
[767.22 --> 773.16]  and where you kind of see the divergence from Stack Exchange and what discourse kind of does
[773.16 --> 773.92]  differently for you.
[775.16 --> 775.52]  Yeah.
[775.70 --> 780.84]  Well, so discourse is really there to support – it's a much more fundamental building block
[780.84 --> 783.00]  of community in that it's just about conversations.
[783.00 --> 785.80]  It's not about producing useful information.
[786.32 --> 792.32]  Stack Exchange is very strict and necessarily so about producing information that is somewhat
[792.32 --> 793.66]  useful to the outside world.
[794.62 --> 796.20]  Forums are less so.
[796.36 --> 802.00]  Forums are really about just having fun conversations in your clubhouse with your friends or people
[802.00 --> 803.34]  that love the same thing that you love.
[803.34 --> 806.68]  It doesn't necessarily have to be your friends, but usually you're in the clubhouse because
[806.68 --> 809.30]  it's a clubhouse for, say, I don't know, lawn bowling or something.
[809.40 --> 812.32]  Something that you just enjoy and other people enjoy and you want to go there and hang out
[812.32 --> 814.84]  with people that enjoy the same thing as you.
[815.06 --> 819.16]  But there's not really a focus on outside – utility to the outside world.
[819.16 --> 823.72]  So there's no concept of, for example, voting answers up to the top because you can't
[823.72 --> 825.08]  really vote up an opinion.
[825.52 --> 833.76]  If I start a topic titled, who is the coolest X-Man, your opinion on Cyclops being the coolest
[833.76 --> 839.36]  X-Man is not more correct than my opinion that Wolverine is the coolest X-Man, which is,
[839.48 --> 840.00]  by the way, true.
[840.60 --> 841.36]  Of course, yeah.
[841.70 --> 841.92]  Duh.
[842.52 --> 843.22]  Yeah, duh.
[843.22 --> 843.62]  Yeah.
[843.98 --> 851.72]  So if discourse then is completely open source, how would you respond to, let's say, that
[851.72 --> 856.38]  somebody decides and the community decides that that's actually something we do want.
[856.44 --> 858.20]  We do want to be able to upvote things.
[858.62 --> 863.12]  Where would that flow kind of fit in and do you still kind of take – what kind of an
[863.12 --> 864.92]  attitude would you take with something like that?
[865.92 --> 868.52]  Well, we want to have a really good plug-in system.
[868.52 --> 875.26]  Our spirit animal discourse is really WordPress, not so much the PHP part of it, but the idea
[875.26 --> 878.28]  that you have this building block of the web, in this case blogs.
[878.86 --> 882.28]  And if someone said to you, hey, I want to start a blog, where should I do, where should
[882.28 --> 882.58]  I go?
[883.24 --> 889.36]  Most people will kind of say WordPress eventually, either WordPress.com or .org or one way or another
[889.36 --> 890.80]  you'll end up on WordPress, kind of.
[890.96 --> 895.68]  It's a nice fundamental building block for human communication because blogs are a net good,
[895.76 --> 895.86]  right?
[895.86 --> 898.44]  If we can get more people to write, writing is good.
[899.16 --> 902.24]  I mean, what you write about may be ridiculous, but you're writing, and that's good.
[903.30 --> 906.36]  The same sort of thing I want to happen with this course, where people say, hey, we need
[906.36 --> 913.86]  a place for people to hang out and talk about our product or blue jeans or motorcycles or
[913.86 --> 915.94]  I don't even know how to blow things up.
[916.12 --> 916.84]  It doesn't matter.
[917.50 --> 919.88]  It could be something bad, like how to be a racist.
[920.24 --> 923.18]  We want a clubhouse for these people to go to, to talk to.
[923.56 --> 924.68]  What software should I use?
[924.68 --> 927.78]  I want people to eventually come to the realization, oh, Discourse.
[927.86 --> 928.36]  Go to Discourse.
[928.44 --> 928.88]  It's free.
[929.20 --> 929.72]  No obligation.
[929.98 --> 932.66]  Just take it, install it, or have someone install it for you.
[933.14 --> 937.60]  And then bam, you've got a nice clubhouse for people to go to and talk about motorcycles.
[938.80 --> 940.86]  That's where we want to get to with Discourse.
[940.98 --> 941.24]  Gotcha.
[941.36 --> 942.58]  Very much like what WordPress did.
[942.74 --> 946.64]  And just as a disclaimer, we're not telling anyone that's listening to this that we want
[946.64 --> 947.94]  you to figure out how to be a racist.
[949.84 --> 950.60]  Good one, Andrew.
[950.74 --> 951.06]  Good one.
[951.06 --> 953.64]  Well, we did actually look at those guys.
[954.56 --> 957.22]  I won't mention the name because people get angry when I mention the name.
[957.32 --> 962.20]  But we talk about Discourse as a rainbow system where people are going to discuss what they're
[962.20 --> 962.68]  going to discuss.
[962.86 --> 965.78]  And some of the stuff they're going to discuss is kind of unpleasant, right?
[965.90 --> 966.08]  Right.
[966.08 --> 967.56]  Like being a racist.
[967.88 --> 969.32]  And I actually researched that.
[969.42 --> 977.06]  We did a whole bunch of research on what community behavior guidelines you want to provide for
[977.06 --> 979.90]  all forums as just a universal constant.
[980.08 --> 983.02]  Like what's the sane set of behaviors that you want on a forum?
[983.08 --> 988.38]  Because forums that have survived for 10 years have done a lot of thinking about what behaviors
[988.38 --> 989.40]  are we going to allow here?
[989.54 --> 991.58]  And what behaviors are we not going to allow?
[991.58 --> 992.66]  Because they're not sustainable.
[992.80 --> 994.14]  They tear the community apart.
[994.36 --> 999.34]  Even though they may be fun or enjoyable or, you know, may seem like the right thing, we're
[999.34 --> 1000.32]  not going to allow them.
[1000.66 --> 1004.56]  And one of the ones we looked at was a prominent, you know, essentially racist forum.
[1004.74 --> 1009.38]  And I was really shocked to discover they had a lot of the same rules that were sensible
[1009.38 --> 1013.24]  rules about how to communicate with other people about racism.
[1013.24 --> 1015.80]  And I found that really, really interesting.
[1015.90 --> 1019.66]  And it's not in any way of support of racism because if you go on that forum, these people
[1019.66 --> 1020.22]  are ridiculous.
[1020.22 --> 1021.90]  Like it's like reading The Onion.
[1022.18 --> 1025.24]  Like I could not take them seriously because they were just ridiculous.
[1025.24 --> 1030.16]  Like there was no scientific basis for hating people on the basis of like their skin color
[1030.16 --> 1030.90]  is different than yours.
[1032.32 --> 1034.48]  And these are not the smartest people in the world.
[1034.60 --> 1035.32]  Let me just put it that way.
[1035.32 --> 1041.36]  So they kind of, they're their own best argument as to why you wouldn't have that position,
[1041.60 --> 1042.36]  I thought.
[1042.68 --> 1046.62]  So I was okay mentioning them, but people got very up in arms that I even mentioned them
[1046.62 --> 1048.04]  as a research point.
[1048.04 --> 1052.64]  Well, I think, you know, for me, like when I first, I was kind of digging through the
[1052.64 --> 1057.46]  archives of Stack Overflow and because that's when I first kind of found out about, I think,
[1057.54 --> 1059.82]  Stack Overflow, you know, before Stack Exchange and all that.
[1060.10 --> 1064.20]  And my first question, it's funny, was actually about Adobe Flex and ActionScript.
[1064.20 --> 1068.84]  And I was kind of digging through the archives and I was looking through a lot of my questions
[1068.84 --> 1070.80]  and you bring up a good point.
[1071.02 --> 1075.64]  Like the, what is allowed and what is not allowed in certain atmospheres.
[1075.74 --> 1080.22]  Now, obviously, when you're on a Q&A type of a question like Stack Overflow, that's about
[1080.22 --> 1080.70]  development.
[1081.42 --> 1085.74]  What's allowed is questions about, you know, here's my problem and answers about, you
[1085.74 --> 1086.94]  know, here's a solution.
[1087.14 --> 1090.90]  And we upvote and we give, you know, yes, this is a good one.
[1090.94 --> 1091.82]  I'm going to accept this answer.
[1091.82 --> 1098.74]  So I noticed that through all of my questions, there was very little, how do you put it,
[1098.84 --> 1105.48]  like elitism, very, very little people really making me feel dumb for asking the questions.
[1105.58 --> 1109.38]  And I think the problem with a lot of people that they don't ask the questions because they
[1109.38 --> 1111.08]  feel dumb when they ask them.
[1111.08 --> 1117.58]  So how on Stack Overflow have you guys done what is seemingly impossible for forums to
[1117.58 --> 1124.56]  do, which is like moderate without like making the users hate the man kind of a thing?
[1125.68 --> 1128.98]  Well, a large part of the secret of why that works is focus.
[1129.64 --> 1134.60]  I think if you go, the example everybody cites for bad comments is YouTube.
[1134.60 --> 1138.80]  And they're not wrong, but they fail to really analyze why that is.
[1139.34 --> 1143.60]  The reason YouTube has such a difficult time with comments, even though they've actually
[1143.60 --> 1147.84]  done some innovation here that people have not noticed that much as far as promoting
[1147.84 --> 1151.96]  only certain comments and stuff like that, is the audience is too broad.
[1152.28 --> 1156.88]  I mean, if you have a video of, you know, Lady Gaga, there's just too many people.
[1157.24 --> 1158.56]  It's the tragedy of the comments, right?
[1158.56 --> 1159.88]  It's not specific enough.
[1159.88 --> 1164.62]  It's just too many, it's a huge cross-section of humanity are listening to this and wanting
[1164.62 --> 1166.70]  to put their little mark on the video.
[1168.86 --> 1172.30]  And on Stack Overflow, it's like, well, this is a question about Java, which is already
[1172.30 --> 1172.46]  okay.
[1172.50 --> 1173.56]  How many people know Java in the world?
[1173.58 --> 1174.76]  How many people care about Java?
[1175.12 --> 1178.84]  And on top of that, it's a really specific question because we demand that the questions
[1178.84 --> 1179.46]  be specific.
[1179.78 --> 1184.80]  You cannot ask, what is the coolest, you know, Java keyword, right?
[1184.80 --> 1188.54]  I mean, it's fun to think about, but it's not, it doesn't solve any problems for anybody,
[1188.70 --> 1188.82]  right?
[1188.82 --> 1190.24]  What problem does that solve for you?
[1190.50 --> 1192.82]  Knowing that, you know, this word, this is the coolest keyword.
[1193.08 --> 1194.10]  What does that even mean, right?
[1194.10 --> 1195.18]  How do you define coolest?
[1195.48 --> 1197.30]  It sounds like something discourse for discourse.
[1198.02 --> 1199.04]  It is something for discourse.
[1199.20 --> 1200.34]  It's exactly something for discourse.
[1200.64 --> 1204.44]  But you see why we don't do that because if you allow that, then you get into arguments
[1204.44 --> 1207.52]  about, well, we'll define cool and no, that's not cool because of this.
[1207.58 --> 1209.30]  And nothing is really correct because there's no data.
[1209.38 --> 1210.06]  There's no science.
[1210.38 --> 1213.94]  Whereas I came in with, I'm getting this, you know, this compilation error in Java.
[1214.24 --> 1216.42]  Well, I mean, there's some science you can apply to that.
[1216.94 --> 1218.12]  You know, it's computer science, right?
[1218.12 --> 1223.02]  It's not hard science like math, but there are verifiably correct ways to do things.
[1223.54 --> 1227.62]  And even if it's something somewhat broad of like, I want to, you know, how do I concatenate
[1227.62 --> 1228.06]  two strings?
[1228.10 --> 1228.90]  That's a valid question.
[1229.18 --> 1230.50]  There's a lot of ways to do that, right?
[1230.92 --> 1232.02]  And a lot of them are correct.
[1232.08 --> 1233.44]  But there's only like a finite number.
[1233.44 --> 1236.06]  There's not an infinite number of ways to concatenate a string.
[1236.16 --> 1242.18]  There may be five good, three good ways and three crazy-ish ways, right, that you might
[1242.18 --> 1242.52]  do.
[1242.92 --> 1247.86]  But if a topic grows and grows and grows, if it has an infinite number of air quote answers,
[1248.72 --> 1250.36]  then it is not a question.
[1250.44 --> 1251.44]  It's a discussion, right?
[1251.46 --> 1255.28]  If there's an infinite number of answers, then it's an opinion sort of situation.
[1255.28 --> 1260.32]  And that's sort of the magic part, a big part of the magical sauce is just staying on topic
[1260.32 --> 1265.38]  and keeping the topic really narrow so that only people who really care about that will
[1265.38 --> 1266.00]  go in there.
[1266.48 --> 1268.62]  Going broad is a recipe for failure.
[1268.74 --> 1272.90]  And I think forums, you see this in forums where somebody actually sent me on Twitter a
[1272.90 --> 1279.52]  great link to a 2007 forum topic about a programming question that just went completely horribly
[1279.52 --> 1279.92]  wrong.
[1279.92 --> 1285.08]  It was like this complete argument about unrelated things and it just went radically off topic
[1285.08 --> 1289.20]  because nobody was there saying, look, this is, you know, essentially, as we say, being
[1289.20 --> 1290.30]  a dick about moderation.
[1290.56 --> 1295.16]  Like, you have to stay on topic and you have to come up with a topic that's narrow and specific
[1295.16 --> 1296.62]  and that can actually be answered.
[1297.26 --> 1299.72]  So the focus is a big part of the problem.
[1300.16 --> 1301.92]  Fixing the focus fixes most of it.
[1302.02 --> 1305.76]  Yeah, it's incredible how, you know, and this is kind of the, probably the reason, one of
[1305.76 --> 1309.08]  the main reasons, well, I don't want to speculate, but it's, I'm sure, one of the
[1309.08 --> 1313.72]  reasons for Stack Overflow's popularity is this idea that, you know, on forums, it was
[1313.72 --> 1318.92]  like my rank or whatever they would call it at the time was, was dependent on like what
[1318.92 --> 1321.02]  the amount of posts I would have on the forum.
[1321.16 --> 1326.68]  So if I had, you know, 7,000 posts on a forum, I was like this, like important person there.
[1327.02 --> 1332.40]  Whereas on Stack Overflow, depending on the quality of questions I ask, the quality of
[1332.40 --> 1337.28]  answers I give, you know, if, if the community kind of decides who gets the credit for stuff
[1337.28 --> 1342.46]  and that probably, it's almost like the whole, you know, if I'm going to buy something on
[1342.46 --> 1347.68]  eBay and it's got a 99% like happiness rate or whatever that rate is, I feel more comfortable
[1347.68 --> 1348.18]  about it.
[1348.24 --> 1353.38]  So it kind of breeds this environment where people are happy with the answers they're
[1353.38 --> 1355.38]  getting and they're satisfied easier.
[1356.74 --> 1358.50]  So I think that it's pretty cool.
[1358.66 --> 1358.76]  Sure.
[1358.76 --> 1365.98]  So what drove the, the idea of having this be a thing that isn't fully hosted?
[1366.16 --> 1369.52]  Like there's a hosted version and you can run it on your own, on your own systems.
[1369.52 --> 1372.24]  Why, what made you decide to do that after doing Stack Overflow?
[1374.10 --> 1377.08]  Well, let me take one step back.
[1377.16 --> 1381.98]  I will get to that, but it was frustrating not being able to give the Stack Exchange software
[1381.98 --> 1382.42]  to people.
[1382.68 --> 1387.08]  On the other hand, it's such a strict system that requires really deep understanding of like
[1387.08 --> 1389.10]  why you need to be strict in the system.
[1389.24 --> 1390.40]  That's why it works.
[1390.52 --> 1394.00]  You need essentially people installing the software need to understand the philosophy
[1394.00 --> 1399.86]  of why it works and how it works and be willing to enforce it and be willing to, you know,
[1399.88 --> 1404.08]  they have to be able to muster an audience that can actually come in and live under this
[1404.08 --> 1405.70]  fairly strict rule set, right?
[1405.78 --> 1408.44]  Like there's a reason, you know, there's Ivy League colleges.
[1408.44 --> 1412.20]  And to be clear, I think of Stack Overflow as at best a community college.
[1412.42 --> 1415.48]  It's not like MIT or Yale or anything like that.
[1415.48 --> 1419.06]  In terms of like super strictness, but there are standards, right?
[1419.10 --> 1420.56]  Like there's some level of strictness.
[1420.70 --> 1425.50]  It's not just let it all hang out, anything goes, which is a lot of really the expectation
[1425.50 --> 1427.02]  on the internet is I can do what I want.
[1427.74 --> 1431.04]  Nobody's going to tell me that what I'm doing is not correct because, you know, it's the
[1431.04 --> 1431.28]  internet.
[1431.46 --> 1432.02]  Anything goes.
[1432.12 --> 1432.92]  It's the Wild West.
[1433.34 --> 1436.82]  And then all of a sudden they come on Stack Overflow and wow, we have actual rules about
[1436.82 --> 1438.18]  what you can post.
[1438.18 --> 1443.50]  And the reason you come there is because the rules work and because it's a good place to
[1443.50 --> 1448.62]  get your question answered because we're somewhat strict about these rules that we have.
[1449.00 --> 1453.44]  So even if we made Stack Exchange open source, which I kind of wanted to do at one point and
[1453.44 --> 1454.78]  then I got talked down by Joel.
[1455.30 --> 1457.98]  And I think he was right, but not for the reasons that he thought.
[1458.16 --> 1462.26]  I think he was right indirectly because the system is too strict.
[1462.26 --> 1467.16]  If I gave you the Stack Exchange system and there's plenty of open source clones of Stack
[1467.16 --> 1469.00]  Overflow that are just really awful.
[1469.68 --> 1474.46]  Like there's, oh God, there's Shappado and like OSQA and these things are just hideous.
[1474.56 --> 1480.68]  They're like, you know, the Rolex that has the R in the word, Rorex, you know, they're
[1480.68 --> 1481.02]  like that.
[1481.10 --> 1482.18]  They're just terrible, terrible.
[1482.52 --> 1487.38]  And on top of being just terribly implemented, like when they get installed, nobody understands
[1487.38 --> 1490.24]  how they work and they don't understand how to be strict and they treat it like a forum
[1490.24 --> 1491.68]  and it just breaks down.
[1492.26 --> 1494.32]  So it wouldn't have worked.
[1494.38 --> 1497.50]  But on the other hand, like I really wanted to give it to people that I thought knew how
[1497.50 --> 1498.62]  to use it, but I couldn't.
[1498.74 --> 1504.96]  They had to go through the Stack Exchange system on area51.stackexchange.com to fill things
[1504.96 --> 1505.14]  out.
[1505.54 --> 1510.16]  So with this course, I'm very excited that I can actually give the software to everyone
[1510.16 --> 1515.38]  because I feel like discussions and just, you know, hanging out in the clubhouse is a much
[1515.38 --> 1521.56]  more generally applicable, broader activity that's going to work for like way, way more audiences
[1521.56 --> 1522.92]  maybe even all audiences.
[1522.92 --> 1530.94]  Like I struggle to think of a community online that couldn't use a forum as a basic building
[1530.94 --> 1532.18]  block of organization.
[1532.78 --> 1534.36]  So let's, do we hang out there for a second then?
[1534.50 --> 1539.60]  So since forums have been around for so long, why have they kind of, I guess, dwindled and
[1539.60 --> 1542.18]  why have they stagnated if they're so useful?
[1543.12 --> 1544.92]  Well, I think it's a, you know, I don't know.
[1545.10 --> 1548.76]  I think the reason is good enough syndrome is like, oh, this is good enough.
[1549.00 --> 1549.06]  Right.
[1549.38 --> 1549.44]  Yeah.
[1549.66 --> 1552.00]  PHPB is not very good, but it kind of works.
[1552.20 --> 1553.92]  And it's a layout from 1999.
[1554.34 --> 1555.74]  But hey, that layout works.
[1556.18 --> 1561.56]  And certainly there's lots of really good live forums using terrible, terrible software.
[1561.76 --> 1563.70]  So the argument was, well, it's working.
[1563.70 --> 1565.92]  It's not so broken that anyone's complaining.
[1565.92 --> 1569.08]  But on the other hand, I would counter with really two arguments.
[1569.30 --> 1574.58]  One is what other software on the internet has changed so little in the last 10 years?
[1575.16 --> 1580.18]  And the second argument is just, you know, nobody cared.
[1580.28 --> 1581.82]  It became so unsexy.
[1581.92 --> 1585.84]  It was just working that nobody was willing to go in and really lead.
[1586.32 --> 1591.64]  And it's very frustrating to me that if you bring up forum software to a mildly technical
[1591.64 --> 1596.44]  person, they can't even tell you where to go to set up a forum or what the software should be.
[1596.62 --> 1596.66]  Right.
[1596.70 --> 1601.64]  Like there's no leader in this space that was willing to really, you know, take a stand.
[1601.80 --> 1603.18]  Like, again, like WordPress did.
[1603.90 --> 1609.12]  And forums themselves, they have the problem of like they start out and the community will
[1609.12 --> 1609.98]  grow and grow and grow.
[1610.18 --> 1615.34]  And then, you know, they kind of establish their community and then they start to know
[1615.34 --> 1615.66]  each other.
[1615.76 --> 1619.52]  And then it's really hard for newcomers to get in on that and to come be a part of it.
[1619.52 --> 1621.70]  You know, they kind of breed that like environment.
[1621.88 --> 1626.06]  So you'll see a lot of forums that will kind of fall apart over time because people get bored
[1626.06 --> 1626.40]  with them.
[1626.54 --> 1632.44]  So I think these ideas encourage people to keep coming and makes it easier for newcomers
[1632.44 --> 1634.20]  alike, you know, to do it.
[1634.38 --> 1635.16]  Well, that's right.
[1635.22 --> 1639.36]  Because on Stack Exchange, for example, on Stack Overflow, to ask a question is hard because
[1639.36 --> 1642.14]  you have to have a specific narrow question that can be answered.
[1642.54 --> 1646.72]  Whereas on a forum, you could just come in and say, hey, you know, this cool thing happened
[1646.72 --> 1646.90]  to me.
[1646.96 --> 1647.98]  Let me tell you guys about it.
[1648.34 --> 1648.86]  And that's OK.
[1648.86 --> 1650.54]  I mean, unless the forum just allows that.
[1650.58 --> 1653.16]  But most forums allow socialization, right?
[1653.20 --> 1654.24]  They allow socializing.
[1654.24 --> 1659.18]  This might sound weird, but I think that your biggest competitor will be Reddit.
[1661.70 --> 1666.04]  To some extent, but the format on Reddit is really bizarre.
[1666.38 --> 1671.08]  Like, I find that, I don't know, I like Reddit for what it is, but I have problems with Reddit.
[1671.34 --> 1674.92]  Like, I think the ultimate Reddit post is an image.
[1674.92 --> 1678.30]  And I think that's a problem.
[1679.26 --> 1679.98]  I can see that.
[1679.98 --> 1684.02]  I think where you see the really good data on Reddit or the really good content is the
[1684.02 --> 1686.60]  subreddits that are very, very heavily moderated.
[1686.60 --> 1686.88]  Yes.
[1687.26 --> 1688.72]  Because Reddit always has this idea.
[1688.82 --> 1691.44]  It's very libertarian, which is really irritating to me.
[1691.44 --> 1695.18]  To a point where it's just frustrating.
[1695.46 --> 1696.14]  They're so libertarian.
[1696.28 --> 1697.44]  Like, no, there can be no rules.
[1697.54 --> 1698.76]  We just do whatever we want on Reddit.
[1699.06 --> 1699.56]  Child porn?
[1699.70 --> 1699.86]  Sure.
[1699.96 --> 1700.22]  Great.
[1700.32 --> 1700.60]  Awesome.
[1701.14 --> 1702.58]  You know, they had a whole backlash about that.
[1702.62 --> 1705.92]  Because even that was like something they were unwilling to address, which is crazy.
[1705.92 --> 1711.80]  But where it's strictly moderated, like on Ask Science and stuff like that, it can work.
[1711.92 --> 1717.40]  But I feel like it's an example, yet again, of people that people are just born social animals.
[1717.50 --> 1718.94]  If you have children, you'll see this.
[1719.10 --> 1721.16]  Like, I mean, humans are born incredibly social.
[1721.48 --> 1726.30]  So they'll take whatever tool you give them, and they'll make it work to socialize with other
[1726.30 --> 1726.88]  human beings.
[1727.22 --> 1728.96]  And I think that's what people are doing with Reddit.
[1729.08 --> 1731.76]  But how much has the Reddit software changed since 2005?
[1731.76 --> 1732.00]  Yeah.
[1733.34 --> 1736.06]  I mean, I still have a hard time with a lot of it.
[1736.16 --> 1738.60]  And I've, you know, kind of learned how to use a lot of it.
[1738.72 --> 1740.50]  But yeah, I agree with you.
[1740.60 --> 1744.48]  Like, ultimately, the ideal post on Reddit is an image.
[1745.06 --> 1747.02]  And that's not good.
[1747.06 --> 1747.28]  Yeah.
[1747.36 --> 1748.06]  For discourse, right?
[1748.08 --> 1749.08]  We have a project called Discourse.
[1749.16 --> 1750.50]  And although we have great image support.
[1750.56 --> 1751.86]  And actually, I love image topics.
[1752.22 --> 1753.04]  I think they're fun.
[1753.08 --> 1755.68]  And every forum has a post the funny image.
[1755.72 --> 1756.90]  And those are awesome topics.
[1756.92 --> 1757.70]  Like, I love those.
[1757.70 --> 1762.90]  But if your entire site is nothing but that, you have the wrong design.
[1763.48 --> 1767.80]  Reddit is designed for a world where you submit URLs and you comment on URLs.
[1768.28 --> 1769.92]  That's what Reddit was designed for.
[1770.44 --> 1773.62]  And everything about Reddit flows out of that original design decision.
[1774.24 --> 1776.80]  Although, you know, you can make it work as a discussion system.
[1776.90 --> 1778.14]  It really wasn't designed for that.
[1778.18 --> 1779.32]  And it hasn't changed.
[1779.42 --> 1781.06]  I mean, it's barely changed since 2005.
[1781.16 --> 1782.40]  And I find that very frustrating.
[1782.86 --> 1786.54]  One of my only pet peeves with software is I really dislike software that's not evolving.
[1786.54 --> 1788.72]  Because I think it's the job of software.
[1789.12 --> 1791.22]  When software is born, you evolve.
[1791.40 --> 1792.08]  You grow up.
[1792.48 --> 1793.42]  You know, you start out as a baby.
[1793.62 --> 1795.22]  You become, you know, a child, a teenager.
[1795.40 --> 1795.98]  And you grow up.
[1796.00 --> 1798.02]  And even as an adult, you continue evolving, right?
[1798.04 --> 1798.92]  You have different positions.
[1799.08 --> 1800.18]  You have different ideas about things.
[1800.50 --> 1801.38]  You learn stuff.
[1801.62 --> 1804.60]  If you're not changing as software, then you're dead.
[1805.08 --> 1807.60]  And I have that problem with Reddit where they're just not changing.
[1808.12 --> 1808.62]  You know, and I agree.
[1808.76 --> 1809.62]  They're a small team.
[1809.68 --> 1811.34]  For a long time, they were a very, very small team.
[1811.34 --> 1813.80]  And they had a lot of explosive growth.
[1813.98 --> 1817.08]  But still, just where's the design work?
[1817.24 --> 1820.14]  Where's the changes to the system to make it better?
[1820.42 --> 1821.38]  I'm just not seeing it.
[1822.28 --> 1827.24]  I'm noticing on the discourse site here that you decided to make the default discussion license, Creative Commons.
[1827.62 --> 1828.68]  That's very fascinating.
[1829.66 --> 1830.76]  Do you want to get into that at all?
[1830.84 --> 1832.06]  And what drove that decision?
[1833.38 --> 1837.92]  That turned out to be, this is another example where the status quo of form software is just bad.
[1837.92 --> 1847.52]  But the status quo of form software, if you install, I think, VBulletin or PHP or any of the big players, you'll get a default license, which is we kind of own your content.
[1847.88 --> 1851.92]  I mean, you can still use it, but we can do whatever we want with your content for any reason.
[1853.46 --> 1855.32]  And that's kind of uncool.
[1855.82 --> 1857.16]  And it was really hard.
[1857.62 --> 1858.42]  I was surprised.
[1858.50 --> 1859.18]  I even asked on Twitter.
[1859.30 --> 1863.40]  I was like, show me forums that are some ways that are more permissive, right?
[1863.66 --> 1865.08]  Like Creative Commons or what have you.
[1865.28 --> 1867.18]  And almost nobody could come up with examples.
[1867.18 --> 1870.32]  There's like a handful of examples of this.
[1870.88 --> 1872.82]  And I think that's a bad default.
[1872.96 --> 1874.14]  I don't think that's really intentional.
[1874.36 --> 1875.20]  I think sometimes it is.
[1875.24 --> 1880.22]  Like if you have a big forum and you're some corporate entity, for legal reasons, you want to make that decision.
[1881.04 --> 1883.58]  And if the users are okay with it, that's fine.
[1883.70 --> 1884.60]  It's not terrible.
[1884.64 --> 1887.06]  But as a default, it's kind of dangerous, right?
[1887.10 --> 1888.34]  Like that shouldn't be the default.
[1888.92 --> 1890.66]  So we are actually trying to change that.
[1890.78 --> 1891.30]  So that's right.
[1891.34 --> 1893.56]  When you install this course, you're free to override this.
[1893.56 --> 1898.28]  And we do explain it in the admin setup guide, which is all, of course, rapidly evolving.
[1898.42 --> 1899.50]  This is a very new project.
[1899.64 --> 1901.18]  It's three months old.
[1901.18 --> 1904.20]  But we do explain, look, you need to make this choice.
[1904.70 --> 1907.92]  Who gets – what rights level do you want for the content submitted?
[1908.30 --> 1910.12]  Do you want the users to have the most rights?
[1910.64 --> 1912.48]  Do you want the public to have the most rights?
[1912.74 --> 1915.78]  Or do you, the forum owner, want to have the most rights?
[1915.88 --> 1916.68]  Those are all valid.
[1916.68 --> 1919.24]  Depending on your situation, they're all valid.
[1919.88 --> 1924.90]  But the default of the public having the most rights is, I think, better for the world.
[1925.00 --> 1935.20]  And that's certainly what discourse is about, is about good discussions that make the world better with software that makes it possible for this to happen.
[1935.20 --> 1938.24]  But it's interesting.
[1938.38 --> 1941.00]  So let's kind of switch gears here for a second.
[1941.34 --> 1947.54]  And I think a question that I have for you, as I know you're a Windows guy, Jeff.
[1947.62 --> 1951.50]  So what has it been like for you getting into Ruby on Windows?
[1951.84 --> 1956.92]  And, I mean, it's been a pretty big shift for you, right, to go from .NET to Ruby.
[1957.12 --> 1959.86]  So what have you thought since you've kind of done this here?
[1961.08 --> 1963.16]  Well, I like Ruby.
[1963.26 --> 1964.34]  I had always been intrigued by Ruby.
[1964.34 --> 1967.90]  I cited the Steve Yegge post from, gosh, 2006.
[1968.16 --> 1971.30]  It was an old post where he did a roundup of a bunch of languages.
[1971.82 --> 1974.62]  And Steve Yegge is a polyglot.
[1974.76 --> 1976.44]  He knows all these languages.
[1977.26 --> 1980.54]  And I find that the best programmers know multiple languages.
[1980.68 --> 1981.82]  So I trust Steve Yegge.
[1981.96 --> 1984.34]  I think his opinion is, I think, sacrosanct.
[1985.12 --> 1988.74]  It's one of the best opinions you can get as a programmer.
[1989.00 --> 1992.22]  And when he says, I think Ruby, I mean, pretty much he said this.
[1992.22 --> 1993.04]  I'm paraphrasing.
[1993.04 --> 1993.70]  I don't have it in front of me.
[1993.80 --> 1997.86]  But Ruby combines sort of the best aspects of modern language design.
[1998.22 --> 2000.20]  That really stuck with me for a long time.
[2000.26 --> 2004.94]  And I always had on my mental to-do list to sort of come back to Ruby when it was more mature.
[2005.94 --> 2012.82]  And when we were making a decision about what to build discourse in, we knew it was obviously 100% open source.
[2012.88 --> 2013.76]  That was one of the design goals.
[2013.76 --> 2019.32]  It came down to really three choices, Python, Ruby, or Node.
[2020.12 --> 2025.98]  Initially, I liked Node because I do think JavaScript is going to eat the world, basically.
[2026.16 --> 2027.12]  I think it's kind of inevitable.
[2027.32 --> 2035.26]  And I said this with Atwood's Law in 2007, which half-jokingly, I said any software that can be written in JavaScript will be written in JavaScript.
[2035.26 --> 2043.40]  And Node is another manifestation of that where you take the JavaScript engine from Chrome, V8, which is super, super fast and crazy optimized.
[2043.92 --> 2055.66]  And you move it to the server and start writing the same language on the server as you do on the client, which is great because then there's just less cognitive dissonance between, oh, I'm writing Ruby on the server and I'm writing JavaScript on the client.
[2055.66 --> 2064.22]  But Node is in the same place I feel that Ruby was in about 2004, which is that it's very, very immature.
[2064.38 --> 2067.94]  I think it's actually even more immature than Ruby in a lot of ways.
[2068.40 --> 2070.84]  Like a lot of the major frameworks have yet to emerge.
[2071.54 --> 2076.50]  I felt if we chose Node for discourse, we would end up rewriting it in two years from scratch.
[2076.78 --> 2079.10]  And I wasn't willing to do that.
[2079.28 --> 2082.38]  I think it was – I just wanted something a little more mature than that.
[2082.56 --> 2085.18]  So I took Node off the table for that reason.
[2085.18 --> 2088.12]  Although I think it has a very, very bright future for the record.
[2088.56 --> 2098.64]  So when it came down to Python versus Ruby, the partner, the person that approached me who had an incredible background in Ruby, that kind of made the decision for me.
[2098.70 --> 2101.96]  I was like, well, it was sort of six of one, half dozen of the other.
[2102.06 --> 2104.14]  It was like either Python or Ruby are both good choices.
[2104.34 --> 2106.62]  So we just decided to go with Ruby.
[2106.62 --> 2116.96]  Now, as far as actual getting it implemented and the community and the performance and stuff, we've been happy.
[2117.10 --> 2118.82]  I mean, I haven't really seen a lot of problems.
[2119.28 --> 2126.92]  I will say that I have been a little shocked at – I expected Ruby to be a little bit more mature than it is now in terms of performance.
[2126.92 --> 2130.38]  I'm happy with the changes that I see in Ruby 2.0.
[2130.38 --> 2134.84]  But there's a lot of what I call very low-hanging fruit performance-wise in Ruby.
[2134.84 --> 2140.90]  You see stuff like JRuby and Rubinius and stuff like that.
[2141.04 --> 2153.42]  But you also see a lot of C plugins for Ruby that are there – well, not plugins, but gems, if you will – that essentially give you these massive speed boosts that you need to do things in a reasonable fashion.
[2153.42 --> 2164.12]  And then that causes problems because if you want to use JRuby, well, then I can't use JRuby because our entire project depends on this gem that's written in C.
[2164.38 --> 2166.36]  And now you're sort of back to square zero.
[2166.82 --> 2169.46]  So I'm happy with Ruby.
[2169.76 --> 2174.06]  I feel like there's a long way to go in terms of performance and maturity.
[2174.38 --> 2176.16]  But it's in a good place to start.
[2176.30 --> 2179.40]  I think Ruby 2.0 is – I'm happy we started now.
[2179.56 --> 2181.70]  I would have been very unhappy in, say, 2008.
[2181.70 --> 2184.90]  My hat is off to people that use Ruby very early on.
[2184.96 --> 2185.84]  I don't know how you did it.
[2187.92 --> 2189.28]  But I think it's in a good place.
[2189.46 --> 2191.90]  The velocity is good and it's going in the right direction.
[2191.92 --> 2192.64]  So I'm not sure.
[2192.84 --> 2194.80]  Maybe I missed it because I was listening really closely.
[2195.28 --> 2199.96]  But did he answer exactly the Windows question, though, like how Ruby and Windows?
[2199.96 --> 2200.10]  Well, yeah.
[2200.70 --> 2201.78]  Generally, we don't.
[2201.98 --> 2202.30]  Sorry.
[2202.42 --> 2203.14]  Let me answer that.
[2203.18 --> 2203.58]  We don't.
[2203.58 --> 2204.50]  We don't use Ruby on Windows.
[2204.56 --> 2205.54]  We use virtual machines.
[2206.76 --> 2209.96]  And that turns out to be the much saner way to approach development.
[2209.96 --> 2213.14]  If you go to – there's blog.discourse.org.
[2213.56 --> 2218.08]  There's a blog post called Discourse as Your First Ruby Project.
[2218.32 --> 2220.70]  And we use Vagrant, which I'm a huge fan of.
[2221.44 --> 2227.14]  And Vagrant essentially downloads a VM of Ubuntu for you and sets it up, spins it up, gets it started.
[2227.36 --> 2228.46]  And then that's your server.
[2228.56 --> 2232.34]  Your server is a VM running Ubuntu that does all the Ruby work.
[2232.54 --> 2234.38]  Then you can use a local editor in Windows.
[2234.38 --> 2237.94]  I use RubyMine, which I like, and develop that way.
[2238.26 --> 2241.34]  So the server, if you will, is a virtual machine running Unix.
[2242.68 --> 2243.04]  Yeah.
[2243.14 --> 2247.02]  We're actually going to have Mitchell from Vagrant on the show.
[2247.26 --> 2248.42]  I think it's two weeks from now.
[2248.46 --> 2251.00]  But, yeah, we love Vagrant here big time.
[2251.24 --> 2253.70]  So you kind of hit on it.
[2253.72 --> 2255.72]  So what does your environment look like for development?
[2255.86 --> 2256.90]  You're a RubyMine guy.
[2256.90 --> 2262.20]  And what are the unique tools or circumstances have you found yourself in?
[2263.04 --> 2264.66]  Well, I have to be honest with you.
[2264.86 --> 2268.00]  In this project, like in Stack Overflow, I was definitely a developer.
[2268.18 --> 2269.78]  I mean, I spent a lot of time writing C Sharp code.
[2270.16 --> 2276.88]  But in Discourse, I'm more of a project manager or a product manager, if you will.
[2276.98 --> 2280.02]  Like I write a little tiny bit of Ruby code.
[2280.08 --> 2283.62]  And I'm set up with the environment so that I can make changes and stuff like that.
[2283.62 --> 2289.42]  But it turned out not to be efficient for me to write a bunch of code in this project.
[2290.54 --> 2292.50]  I set up the venture capital funding.
[2292.66 --> 2294.28]  We're a venture capital funded company.
[2296.36 --> 2301.56]  It's kind of like that old office space joke.
[2301.68 --> 2305.28]  I take the requirements from the customer and I bring them to the engineers.
[2306.56 --> 2307.44]  That's what I do.
[2307.58 --> 2308.48]  Well, actually, my secretary does.
[2308.48 --> 2310.58]  It reminds me of the movie Office Space.
[2310.62 --> 2311.44]  What do you do around here?
[2311.44 --> 2313.82]  What do you really do around here?
[2314.06 --> 2316.28]  I take things from here and I give them to those guys.
[2316.66 --> 2318.60]  I'm not going to work here anymore.
[2319.50 --> 2319.82]  Exactly.
[2320.06 --> 2323.14]  So I am not by any means a hardcore Ruby dev.
[2323.26 --> 2324.60]  I'm an utter noob.
[2324.98 --> 2331.58]  And really, all the heavy lifting on the project is done by Neil, Robin, and Sam in terms of actual Ruby development.
[2331.98 --> 2335.00]  So I'm not really in a position to speak about that stuff.
[2335.00 --> 2339.44]  So I'm not sure if Andrew's got this on his docket of questions to ask.
[2339.44 --> 2350.36]  So since you're not so much that role then, besides possibly just lifting Ruby up and saying how great it is, but you wrote the post, why Ruby?
[2350.68 --> 2353.48]  What exactly made you write that post?
[2353.48 --> 2361.90]  Well, you remember in the previous U.S. election, there were people that had the attitude, anybody but Bush?
[2363.10 --> 2365.62]  I have the attitude, anything but PHP.
[2366.10 --> 2368.36]  So I actually looked at PHP.
[2368.44 --> 2375.50]  One of the great sadnesses of my life is that when we were getting into discourse, I had to actually look at PHP as an actual choice for my project.
[2375.50 --> 2379.76]  And I'd suppress my gag reflex and say, should we actually do this in PHP?
[2379.92 --> 2383.22]  Because it would actually be able to reach many more servers.
[2383.48 --> 2384.56]  It would be very easy to deploy.
[2385.26 --> 2385.44]  Yeah.
[2385.66 --> 2387.18]  Yeah, but that's the problem.
[2387.30 --> 2390.14]  It's like Ruby needs to get better and easier to deploy.
[2390.54 --> 2391.28]  This is a problem.
[2391.76 --> 2393.68]  I mean, the status quo is bad.
[2393.84 --> 2401.82]  And the only way to change the status quo is to come up with a really compelling project that has awesome functionality that's so good.
[2402.16 --> 2402.90]  They're like, you know what?
[2402.96 --> 2403.34]  Screw it.
[2403.34 --> 2403.70]  It's Ruby.
[2403.80 --> 2407.76]  It's hard to set up, but I'm going to do it anyway because this is so much better than the other stuff out there.
[2408.04 --> 2408.24]  Right?
[2408.54 --> 2412.60]  Whereas if I built it in PHP, it would just be yet another reinforcement of the status quo.
[2412.68 --> 2415.32]  It's like we use PHP because everyone uses PHP.
[2415.68 --> 2420.38]  Nobody uses PHP because it's actually good or it's actually a great technical choice.
[2420.38 --> 2421.40]  It gets the job done.
[2421.50 --> 2421.78]  Fine.
[2422.16 --> 2425.66]  But that's not – this is not the way that we want the world to work.
[2425.76 --> 2427.92]  Like I don't want my child to write PHP code.
[2428.02 --> 2429.16]  I really don't want that.
[2429.74 --> 2432.84]  Like I don't want Henry to grow up in a world where he has to write PHP code.
[2433.38 --> 2436.98]  And the only way we're going to change that is by coming up with compelling alternatives.
[2437.18 --> 2437.36]  Right?
[2437.76 --> 2438.98]  I don't want to attack PHP.
[2439.16 --> 2439.78]  I don't like it.
[2439.82 --> 2441.34]  But I'm not going to spend any time attacking it.
[2441.56 --> 2445.76]  I'm just going to try to build something awesome that's so good that makes people look at it.
[2445.76 --> 2451.68]  And one of the great satisfactions I've had in this project is hearing people on Twitter and on our forums say, hey, you know what?
[2451.70 --> 2459.98]  I'm a PHP guy, but I really like discourse and I really want to get into Ruby and I really want to understand this and help develop because I really like what you guys are doing.
[2460.04 --> 2461.20]  This project seems really cool.
[2461.20 --> 2468.10]  And that's absolutely the goal of the project is to get Ruby to a place where we're switching PHP devs over.
[2468.60 --> 2473.12]  And if you think back, like Ruby on Rails, like DHH, he was a PHP guy, right?
[2473.12 --> 2475.00]  And he said, you know what?
[2475.54 --> 2477.50]  I don't really want to be a PHP guy anymore.
[2477.58 --> 2479.86]  And he came up with Rails basically, right?
[2479.90 --> 2480.92]  Like at 37 Signals.
[2481.24 --> 2484.74]  So there is an established path for making this transition.
[2484.74 --> 2492.30]  And we want to encourage people to cross that bridge and make it over with us to the world of Ruby.
[2492.44 --> 2495.90]  Do you feel like you're in a good place now with the deployment of it if you want to set it up?
[2495.94 --> 2498.68]  Or is that something that you're still trying to work towards and making it simple?
[2499.92 --> 2501.68]  It's a lot better than it used to be.
[2501.94 --> 2504.72]  I mean, I'm very impressed with the velocity that we have as a project.
[2504.98 --> 2506.10]  We have a lot of contributions.
[2506.32 --> 2509.90]  The install is so much smoother than it was on February 5th when we launched.
[2510.64 --> 2511.82]  Every day it gets better.
[2512.02 --> 2513.04]  I'm happy with the progress.
[2513.04 --> 2515.60]  My idea of a project is you're building a pyramid.
[2516.04 --> 2518.98]  Your job when building a pyramid is not to build a pyramid.
[2519.32 --> 2522.74]  Your job is to move these giant blocks one mile per day.
[2523.16 --> 2523.80]  That's your job.
[2524.46 --> 2529.48]  And if you move enough of these massive giant blocks one mile per day, eventually you get a pyramid, right?
[2529.88 --> 2532.76]  So the progress of the blocks being moved I think is fantastic.
[2532.98 --> 2536.56]  I mean, it's measurably better in every dimension that I can think of.
[2536.64 --> 2537.38]  The setup is easier.
[2537.82 --> 2538.66]  Lots of contributions.
[2538.86 --> 2539.44]  It's way smoother.
[2539.52 --> 2540.42]  We have better instructions.
[2541.04 --> 2542.76]  We're a long way from where we need to be.
[2543.04 --> 2544.32]  But the blocks are moving, man.
[2545.02 --> 2547.08]  Those heavy two-ton blocks are moving.
[2547.28 --> 2547.76]  We're moving them.
[2548.26 --> 2552.42]  So being a .NET guy and doing it, and you obviously wrote that post, Why Ruby?
[2552.42 --> 2556.00]  Did you get a lot of flack when you decided to do it in Ruby?
[2556.20 --> 2565.98]  Or was your community, which unfortunately a lot of us on this side of it are blind to a lot of that, did you get response from the community in this?
[2566.20 --> 2569.26]  Or what prompted you to actually write the post itself?
[2569.26 --> 2571.10]  Well, there were a lot of questions.
[2571.10 --> 2573.24]  Like, you know, why not just do it in the thing that you know?
[2573.64 --> 2576.22]  You know, which surprised me because I love .NET.
[2576.34 --> 2577.68]  I think .NET is amazing.
[2578.10 --> 2579.68]  It's a very well-designed language.
[2580.84 --> 2581.98]  Anders is brilliant.
[2582.20 --> 2583.46]  I think he's a brilliant language designer.
[2583.46 --> 2594.34]  They've done a good job of curating language and growing and evolving it way better than, for example, Java, which I think has been very poorly evolved in the last five or eight years.
[2595.62 --> 2597.42]  So it's a very well-designed thing.
[2597.58 --> 2602.98]  But it's not – there's too much friction in the stack for just, you know, open-source deployment.
[2603.08 --> 2605.94]  Like, download everything you need and get started in a few hours, right?
[2606.90 --> 2609.18]  .NET is not a great solution for that.
[2609.18 --> 2613.08]  And certainly licensing always comes up, and I hate software licensing.
[2613.24 --> 2619.38]  I think it's a huge pain in the butt, not because of the money, but because of just I have to think about something now that I don't want to think about.
[2619.46 --> 2627.96]  I just want to build my solution and see if it's any good before I worry about, you know, SQL server licenses and Windows server licenses and all that stuff.
[2627.96 --> 2643.32]  And I do feel bad because I'm a friend of Miguel de Acaza, and I didn't talk about Mono, which is, of course, the open-source – I don't know what to call it, but the open-source version of .NET that's not from Microsoft but from Ximian.
[2644.44 --> 2654.44]  And I felt a little bad about that, but I don't – with .NET, it's always like you're swimming a little bit upstream if you write .NET's code and you don't install it on the official runtime.
[2654.44 --> 2657.44]  It's just kind of in a weird place.
[2657.66 --> 2660.80]  Like, I'm very encouraged by what they're doing, particularly on the mobile side.
[2661.40 --> 2669.06]  They have a new company that lets you write .NET code and then deploy it to all sort of mobile phones without doing a bunch of cross-platform work.
[2669.40 --> 2670.50]  And I think that's exciting.
[2670.50 --> 2680.20]  But I had heard a lot of not great stories about taking giant .NET projects and trying to run them on Mono and just kind of having a lot of problems.
[2680.86 --> 2684.94]  So I didn't view that as really a realistic choice for our project.
[2684.94 --> 2697.70]  I was sharing some links while y'all were talking, just kind of lamenting on your blog post discourse as your first Rails app.
[2697.70 --> 2709.18]  And I have to say how perfect that cat kind of teetering into the bathtub with a little bit of water in there is to doing what you're saying.
[2709.18 --> 2720.44]  And for those who are listening that are, as Jeff had mentioned, like PHP developers or someone who's not very familiar with Ruby, this blog post would be great for getting started too.
[2722.30 --> 2725.12]  Yeah, I mean, and that's, again, the purpose of discourse.
[2725.24 --> 2729.02]  One of the hidden missions of discourse, one of the hidden objectives.
[2729.02 --> 2729.60]  I like that.
[2729.60 --> 2733.82]  One of the things that I've been doing is to get people introduced to the world of Ruby and the world of open source.
[2734.40 --> 2738.38]  And, you know, it's a very, you know, a lot of stuff is kind of broken, right?
[2738.42 --> 2742.98]  Like I've been surprised at the number of things in Ruby that we've run into in Rails that have been a little bit broken.
[2743.48 --> 2745.74]  But the advantage is we can actually go in and fix it.
[2745.78 --> 2749.64]  And you've seen what Sam, the work Sam Safran has done and Robin Ward has done.
[2749.84 --> 2753.96]  Our goal is to improve the ecosystem, not just selfishly for discourse, but for everyone.
[2754.20 --> 2757.02]  We want Ruby to be as easy to deploy as PHP.
[2757.24 --> 2757.96]  And this is hard.
[2757.96 --> 2760.08]  Like we, let me give you an example.
[2760.26 --> 2763.42]  So one thing WordPress can do is WordPress can update its own version.
[2763.72 --> 2769.50]  Like if you're out of date on WordPress, you can be in the admin UI in the web browser in WordPress and say, update my version.
[2769.76 --> 2776.66]  It'll pull down the code and basically override all the files and give you a new version of WordPress and update the database.
[2776.76 --> 2781.94]  And even if it doesn't have permissions to the files, it'll even connect to your own FTP server to re-upload itself.
[2782.10 --> 2782.50]  It's amazing.
[2782.66 --> 2785.60]  There's a little bit of config you have to do to get that to work, but not much.
[2785.60 --> 2787.18]  It's mostly sysadmin type stuff.
[2787.18 --> 2788.38]  It's not, you know, code.
[2789.14 --> 2790.66]  But for the most part, it works.
[2790.74 --> 2795.42]  And I have a hosted blog with Laughing Squid that works fine with this.
[2795.74 --> 2797.70]  Our Stack Overflow blog worked with this.
[2798.28 --> 2802.38]  Our discourse blog works with this with a little tiny bit of sysadmin level file permission tweaks.
[2802.60 --> 2807.04]  We can't even find a Ruby app that even tries to do this, right?
[2807.28 --> 2810.26]  Show me the Ruby app that can do what WordPress does.
[2810.42 --> 2811.66]  I don't think it's possible.
[2811.66 --> 2814.10]  If it is, nobody can do it, right?
[2814.66 --> 2816.86]  And that's the kind of stuff that we're going to try to solve.
[2816.96 --> 2817.92]  I mean, it's really hard.
[2820.08 --> 2822.52]  You know, like we need to be able to update our own version, right?
[2822.90 --> 2824.06]  Like just like WordPress does.
[2824.12 --> 2829.70]  I think that's a big part of the WordPress success story is how easy they made it to do common stuff like get the latest code.
[2829.70 --> 2833.30]  So you don't, A, have security problems, and, B, you get, you know, new features and stuff.
[2833.30 --> 2839.74]  You can even install plugins through the same methodology and the same update system that you mentioned for updating its own system.
[2839.90 --> 2850.02]  You can, you know, with a Ruby app, it's not quite as easy to or possible to just click a button and install somebody's gem or plugin to your app.
[2850.02 --> 2851.60]  That's right.
[2851.84 --> 2852.24]  That's right.
[2852.50 --> 2858.24]  And it is fun to participate in an ecosystem where we can contribute back fixes that get rolled up.
[2858.34 --> 2860.22]  I mean, Sam was very excited.
[2860.44 --> 2870.44]  He's put one thing in that is about to be accepted into Rails and, you know, a bunch of other tweaks that we want to give back to all the other gems and all the stuff that we're using.
[2870.50 --> 2871.26]  So what's the progress?
[2871.38 --> 2874.60]  Where are you guys at with some of these bleeding edge things you really want to achieve?
[2874.60 --> 2881.42]  Well, right now we're narrowly, we have about a two-year mission time frame for the amount of money that we have.
[2881.60 --> 2883.24]  We're a venture capital-backed company.
[2883.68 --> 2892.64]  So you can sort of guarantee that there will be at least four people, four to six people working on the project for that length of time.
[2893.58 --> 2900.28]  In that window, what we want to accomplish is, there's a couple things, a couple ways of how we measure success on the Discourse project.
[2900.82 --> 2902.50]  One is how many contributions we get.
[2902.50 --> 2905.40]  We've been very happy with the level of contributions we've got.
[2905.52 --> 2913.62]  You guys can go to github.com slash discourse slash discourse and view the contributors graph and see that we've got a nice wide range of contributors.
[2913.78 --> 2914.32]  So that's good.
[2914.80 --> 2917.94]  The number of installed forums is reasonable.
[2918.22 --> 2926.30]  We don't actually want that many Discourse forums right now because every Discourse forum right now needs to be very aggressively updated because it's so new.
[2926.30 --> 2929.52]  We're still building out the functionality.
[2929.70 --> 2932.60]  There's still some mild security things we're working out.
[2933.08 --> 2939.54]  I don't want to scare anyone, but my point is you need to be upgrading very, very aggressively at this stage in the lifecycle of the project.
[2939.96 --> 2942.38]  And we've also solicited some partners.
[2943.16 --> 2948.22]  We're going to have three partners that we handpick, and we deploy the forums on our servers.
[2948.22 --> 2951.48]  So we guarantee a really good experience where you don't have to upgrade.
[2952.02 --> 2953.98]  We take care of all the heavy lifting for you.
[2954.24 --> 2955.74]  We've done this with HowToGeek.
[2956.52 --> 2963.70]  If you go to discuss.howtogeek.com, you'll get to the first sort of live partner discourse forum.
[2964.12 --> 2970.58]  There's another one that's going to launch in mid-May that I can't say the name of yet, but it's a site that I'm very, very sure you've heard of.
[2970.58 --> 2975.52]  It's not necessarily world famous, but I think most geeks have heard of it, and that's very exciting.
[2975.80 --> 2983.08]  That's the next step for us is to get a little bit higher volume activity going on our hosted forums, and then a third partner.
[2983.50 --> 2985.10]  And again, we can't really announce who that is.
[2985.72 --> 2987.06]  But those are the near-term steps.
[2987.16 --> 2998.82]  It's like, are we generating discussions that actually work, that people enjoy, and, you know, you can actually land on these pages and not feel bad as a person, like, because the page sucks.
[2998.82 --> 3000.46]  The content sucks.
[3000.96 --> 3002.46]  It was very, very slow to load.
[3002.52 --> 3006.54]  All the things that you dislike about today's forums, is it noisy?
[3007.76 --> 3009.18]  That's the kind of stuff we want to fix.
[3009.28 --> 3010.42]  So you can judge for yourself.
[3010.54 --> 3014.56]  Go to discuss.howtogeek.com and click around a little bit.
[3014.76 --> 3016.26]  And how does that page make you feel?
[3016.54 --> 3019.64]  How would you feel landing on this page from a Google search?
[3020.26 --> 3021.04]  I can tell you landing on it now.
[3021.04 --> 3021.96]  Those are the ways we're making.
[3022.20 --> 3024.70]  The design of just the posts are great.
[3025.00 --> 3026.70]  It reminds me of Stack Overflow a lot.
[3026.70 --> 3028.48]  Like, it's just good typography, basically.
[3028.48 --> 3029.70]  It goes a long way, right?
[3030.78 --> 3032.66]  Well, good design.
[3032.78 --> 3032.92]  Yeah.
[3033.08 --> 3034.06]  And we did work.
[3034.14 --> 3038.24]  We've been spending a lot of money on designers because I'm happy to, you know, we're engineers, right?
[3038.24 --> 3039.24]  We're not great designers.
[3039.54 --> 3040.80]  I mean, I'm good at copying things.
[3041.26 --> 3043.34]  I see things that I like and I want to copy them.
[3043.50 --> 3046.34]  But I like to have real designers looking at what we're doing.
[3046.68 --> 3048.04]  And it's got to look good.
[3048.24 --> 3052.88]  I mean, one of the things that would have blocked us for launch is we didn't look good.
[3052.88 --> 3057.50]  Because I think a lot of people will judge you based on how you look as a project.
[3057.68 --> 3059.30]  I think in general in life this is true, right?
[3059.38 --> 3063.28]  But even in software, how you look matters a lot.
[3063.60 --> 3068.74]  So if you don't look sort of professional, if you don't look designed, you will immediately get written off.
[3068.82 --> 3072.12]  Because there's, you know, millions of different options out there, right?
[3072.12 --> 3078.72]  Yeah, that's one of the unique things about, you know, communities like the Ruby community with – it kind of draws the interest of a lot of creatives.
[3079.02 --> 3081.94]  So, you know, you see that kind of a thing.
[3082.14 --> 3089.74]  And, you know, one thing, when you were talking about looking at the contributors graphs, I did that and I saw, hey, our very own Steve Klabnik is on there.
[3089.76 --> 3091.56]  And he contributed something to discourse.
[3091.72 --> 3096.64]  So I looked at the commit and he fixed a typo in the author's markdown.
[3096.76 --> 3099.08]  There was developer instead of developer.
[3099.08 --> 3101.86]  So he hasn't actually contributed too much.
[3102.28 --> 3103.46]  But I wanted –
[3103.46 --> 3104.08]  Hey, it's a contribution.
[3104.16 --> 3107.20]  Those changes are important because the maintainers aren't going to do it.
[3107.92 --> 3108.36]  Exactly.
[3108.52 --> 3108.94]  Well, they're not going to do it.
[3108.94 --> 3118.92]  So I wanted to say he – in our last week's podcast, Steve Klabnik kind of talked about this – kind of this – I don't know how to – this group that he started on Google Groups.
[3118.92 --> 3120.82]  And it's philosophy in the time of software.
[3121.16 --> 3124.94]  And he doesn't have a website for them.
[3125.00 --> 3126.24]  They don't have anything like that.
[3126.24 --> 3138.20]  So what – does Discourse have any plans to offer something for people like him to come and create an area of conversation or whatever you call it, not a forum, but just a place for to talk about this topic?
[3138.34 --> 3142.42]  Or is it going to be – is it going to have to be hosted by them?
[3142.46 --> 3145.70]  I guess my question is do you plan on offering any kind of hosting for different areas?
[3146.76 --> 3147.12]  We do.
[3147.40 --> 3148.62]  That's part of the two-year runway.
[3148.82 --> 3150.44]  But we've got to get through our three partners.
[3150.66 --> 3151.92]  We're on partner number one now.
[3151.92 --> 3157.02]  Partner number two is coming around the latter half of next month.
[3157.50 --> 3160.56]  So we have to get all our partners, like, really smoothly humming along.
[3160.80 --> 3163.04]  I believe really deeply in what I call the rule of three.
[3163.80 --> 3166.98]  Programmers think that everything they build is reusable, right?
[3167.00 --> 3172.48]  Every programmer thinks that every function they build is reusable, you know, in an infinite number of scenarios.
[3172.48 --> 3175.76]  But reusability is really, really hard.
[3176.50 --> 3188.12]  And I think the way to approach this is to say, have I taken this function, whatever it is, software function, doesn't matter the unit of work here, and used it in three different contexts, three legitimately different enough contexts.
[3188.24 --> 3189.84]  Not maybe radically different, but different enough.
[3190.18 --> 3194.00]  Once you've done that, you actually have some level of reusability.
[3194.00 --> 3196.94]  And I don't believe you have that until you've done that.
[3197.00 --> 3201.30]  So therefore, I am leery of doing hosting until we've gone through our three partners.
[3201.58 --> 3204.28]  And the three partners are not just happy, but ecstatically happy.
[3204.88 --> 3205.24]  Right.
[3205.42 --> 3210.04]  They kind of help you hammer out the details and kind of grow in the right direction and everything, too.
[3210.28 --> 3214.88]  Well, that's right, because I want to make decisions based on things we're actually observing.
[3215.24 --> 3223.50]  I have this huge problem with what I call imagineering, where you imagine that you're going to have a certain problem with the software that you're building.
[3223.50 --> 3228.20]  So you build a solution to this thing that you've imagined in your head that is going to happen.
[3229.12 --> 3231.38]  Isn't Imagineer what Disney calls their engineers?
[3232.20 --> 3232.44]  I think so.
[3232.44 --> 3233.78]  Aren't they called Disney Imagineers?
[3234.64 --> 3235.12]  Possibly.
[3235.48 --> 3238.44]  But the connection here is you want to make decisions.
[3238.86 --> 3241.38]  I'm not a big believer in making every decision based on data.
[3241.50 --> 3244.84]  I'm not a 42 shades of blue Google kind of guy.
[3245.76 --> 3249.08]  I believe you want some data, though, for all your decisions.
[3249.08 --> 3256.54]  You want to be observing what users are actually doing and making decisions based on real behaviors that you're seeing.
[3256.88 --> 3258.54]  I believe very deeply in that.
[3259.16 --> 3264.70]  And that's why a lot of the features that we built with discourse, we're kind of waiting to see the partners go live.
[3265.54 --> 3267.72]  We have HowToGeek Live, and that's working very well.
[3267.86 --> 3272.08]  Lowell is very happy with his discourse instance because he's seeing really good conversations.
[3272.08 --> 3275.82]  I mean, if you think about any system like discourse, what's the goal of discourse?
[3276.28 --> 3279.04]  Well, it's about, you know, people talking to each other.
[3279.12 --> 3282.74]  So the measurement of success is when you go there, A, are people talking to each other?
[3282.82 --> 3283.68]  Does it even go there?
[3284.14 --> 3285.62]  Are they having fun, right?
[3285.68 --> 3290.44]  Because to even have a conversation, you have to be enjoying it to some degree, right?
[3290.46 --> 3294.10]  It's not this dry academic debate like you're on the debate team.
[3294.22 --> 3295.28]  That's not really fun.
[3295.28 --> 3299.98]  You have to go there because it's some level of enjoyment, entertainment, right?
[3300.02 --> 3300.92]  So you have to be having fun.
[3301.58 --> 3307.30]  And are the conversations somewhat interesting to, you know, someone who's vaguely interested in the subject matter?
[3307.80 --> 3311.36]  And I think both of those are definitely true at HowToGeek right now.
[3311.90 --> 3313.12]  And that's very encouraging.
[3313.54 --> 3314.82]  And we actually had one user.
[3315.30 --> 3321.34]  HowToGeek has a surprising number of older users, like 50, 60, 70-year-old computer users that post.
[3321.40 --> 3322.50]  And I was like, this is fascinating.
[3322.56 --> 3323.06]  I love this.
[3323.06 --> 3324.40]  This is, again, another great data point.
[3324.40 --> 3326.92]  Like, I wouldn't have predicted that there would be older users.
[3327.24 --> 3329.12]  And they're able to tolerate the discourse system.
[3329.50 --> 3330.72]  Like, in fact, one of them said, you know what?
[3330.74 --> 3332.80]  I think the system is good, but it might be too fun.
[3333.40 --> 3334.44]  And I said, that's great.
[3334.86 --> 3337.84]  Because one of the goals is to actually have fun.
[3337.86 --> 3341.68]  Because if it's not fun, nobody's going to be in the room at this party talking to each other.
[3341.68 --> 3343.42]  You're not supposed to enjoy conversation.
[3344.44 --> 3345.22]  Well, that's right.
[3345.36 --> 3346.70]  And it was just encouraging to hear.
[3346.78 --> 3347.90]  I was like, that's great to hear.
[3347.98 --> 3351.80]  Because one of the design goals of discourse we decided early on was, like, people have to be having fun.
[3352.50 --> 3354.28]  Because conversation cannot happen.
[3354.86 --> 3357.60]  If people aren't fundamentally enjoying being in the room with these people.
[3358.24 --> 3359.08]  But someone's wrong on the internet.
[3359.08 --> 3359.80]  That's the compromise.
[3361.10 --> 3363.94]  Whereas on Stack Overflow, we tolerate fun.
[3364.18 --> 3364.36]  Right?
[3364.50 --> 3365.92]  But just like if you go to MIT.
[3366.06 --> 3366.70]  Nobody goes to MIT.
[3366.84 --> 3368.70]  It's like, woo, I'm going to MIT to party all the time.
[3368.76 --> 3368.96]  Right?
[3368.96 --> 3371.46]  Well, you might be in for a little disappointment.
[3371.90 --> 3373.50]  Because it might be hard work.
[3373.64 --> 3373.82]  Right?
[3374.94 --> 3376.08]  It's not wrong to have fun.
[3376.16 --> 3377.76]  It's just a question of what your goals are.
[3378.00 --> 3378.12]  Right?
[3378.54 --> 3381.04]  And discourse is much more of a party system, to be honest with you.
[3381.10 --> 3384.80]  It's like about having fun almost first, really.
[3384.80 --> 3389.92]  And then generating useful stuff sort of as an inevitable byproduct of that system.
[3390.36 --> 3393.98]  Where Stack Exchange would produce, I would say, 50% to 80% useful information.
[3394.48 --> 3397.38]  A forum will produce maybe 10%.
[3397.38 --> 3399.32]  And that's probably wildly optimistic.
[3399.86 --> 3402.18]  But that's still better than, say, a chat system.
[3402.56 --> 3406.26]  Although there are relationships between chat software and forum software.
[3406.70 --> 3407.96]  Let me ask you guys this.
[3408.06 --> 3409.86]  And answer, like, think about in your mind.
[3410.16 --> 3412.00]  When was the last time you did a search result?
[3412.60 --> 3417.00]  Or you did a search and you got a result page that took you to a chat log that helped you?
[3417.88 --> 3421.44]  When was the last time you got a search result of a chat log that helped you?
[3421.44 --> 3429.24]  I don't know if I – you know, it's funny because I think I ask the question and then I look for the Stack Overflow.
[3429.68 --> 3434.62]  Like, when I'm doing tech stuff, I ask the question in Google and then I look for the Stack Overflow page.
[3434.62 --> 3440.70]  But nothing frustrates me more than when I see those – I don't know what they are even.
[3440.80 --> 3444.74]  They're like chat logs that are transcripts elsewhere.
[3445.14 --> 3445.82]  You know what I'm talking about?
[3445.86 --> 3446.58]  Like, you'll see it.
[3446.86 --> 3449.64]  I see – I get mailing list archives a lot.
[3449.64 --> 3451.54]  Yeah, that's what mailing list archives.
[3451.84 --> 3459.50]  And I hate that because I'm like – I'm like tricked into viewing this because I think this is some site that's providing some kind of something to me.
[3459.62 --> 3460.38]  Useful information?
[3460.58 --> 3460.64]  It's not.
[3460.64 --> 3465.96]  And there's seven clones of the same content with like increasingly worse design each time.
[3466.68 --> 3466.94]  Right.
[3467.62 --> 3479.28]  But no, to answer your question, I couldn't tell you the last time that I was – I found a chat log or a mailing list transcript or something that wasn't maybe the original source of it that I felt satisfied with whatever answer I found.
[3479.64 --> 3483.80]  I mean, for me, it's extremely rare.
[3484.04 --> 3487.10]  I would say one in a thousand searches result in a chat log.
[3488.52 --> 3492.80]  Whereas I would say easily one in – at least one in a hundred forum results.
[3492.92 --> 3494.04]  But I think many more actually.
[3494.32 --> 3495.72]  Maybe one in 25, one in 50.
[3496.44 --> 3499.94]  It's just not that uncommon for me to end up on a forum from a search result.
[3500.50 --> 3505.46]  That's one of the reasons I like the discourse project and I wouldn't like – although the chat software is really bad actually.
[3506.10 --> 3508.92]  Web chat, the state of web chat is really abysmal, sadly.
[3509.62 --> 3514.32]  We're using lichat.im, which I like a lot and they're still evolving it.
[3514.40 --> 3519.82]  But I wouldn't want to build chat software because it doesn't produce enough useful artifacts.
[3520.60 --> 3523.28]  Stack Exchange was all about producing useful artifacts.
[3523.28 --> 3529.78]  I mean, to the point that we make you leave the room if you're not generating useful artifacts as part of what you're doing.
[3530.30 --> 3533.60]  Now, on discourse, obviously you don't do that because that's not the point of discourse.
[3533.80 --> 3542.76]  But I'm also very, very confident these communities – like if you go to discourse.soylent.me.
[3542.76 --> 3545.72]  I mean, soylent like in soylent green as in it's made of people.
[3546.90 --> 3549.04]  This is a crazy topic.
[3549.22 --> 3555.12]  It's this guy who came up with this idea of eating essentially liquid food all the time that's cheaper.
[3555.42 --> 3558.14]  Like stop cooking food, just eat the same thing all the time.
[3558.50 --> 3560.14]  Kind of like cats and kibble, I guess.
[3561.12 --> 3563.00]  Except it's a liquid drink called Soylent.
[3563.32 --> 3565.82]  And it's a whole forum for discussing this because it's cheaper.
[3566.78 --> 3567.56]  It's easier.
[3567.96 --> 3569.68]  I met a guy that does this a couple days ago.
[3569.80 --> 3570.66]  He works for New Relic.
[3570.66 --> 3571.10]  Yeah.
[3573.42 --> 3578.46]  No, but this is awesome because part of what I said with discourse is it's a rainbow system.
[3578.56 --> 3581.30]  It's about letting your freak flag fly, right?
[3581.54 --> 3585.46]  This crazy thing that you're into, you're going to find other people on the internet that are into it.
[3586.02 --> 3590.26]  And this is exactly the kind of audience that I had in mind when we started discourse.
[3590.44 --> 3593.34]  It was like, yeah, this is a little bit crazy, but it's also kind of cool.
[3593.64 --> 3595.14]  It's like, wow, this could work.
[3595.28 --> 3599.08]  I mean, our cats eat kibble every day and have for the last five years and they're not dead.
[3599.08 --> 3602.32]  Maybe this could work for humans too.
[3603.88 --> 3604.70]  And it's great.
[3605.26 --> 3607.18]  It's producing really interesting, useful discussion.
[3607.28 --> 3610.14]  So people that search for this will eventually find this information, right?
[3610.54 --> 3618.90]  The other people that are like, hey, what if I had this liquid drink that I made myself with multivitamins and oils and God knows what else, like chemistry, right?
[3618.90 --> 3623.10]  And find other like-minded people that want to do this stuff.
[3623.58 --> 3627.32]  And there are some Google artifacts in there that people are going to be able to find for this stuff.
[3628.08 --> 3632.38]  Then they can go to this clubhouse of all these people that love this and hang out and socialize.
[3633.40 --> 3635.06]  It works for me.
[3635.20 --> 3638.08]  That's why I like the discourse project versus, say, a chat software.
[3638.14 --> 3638.58]  I'm curious.
[3638.70 --> 3642.90]  Did you ever interact with the project called Convor at any point?
[3642.90 --> 3644.90]  I didn't.
[3646.72 --> 3647.70]  No, I didn't.
[3648.04 --> 3652.64]  At the time, Stack Exchange has its own chats offer, which is actually amazingly good.
[3652.84 --> 3654.34]  It's actually one of the, I think, the best.
[3655.68 --> 3656.46]  I'm biased.
[3656.94 --> 3660.06]  But if you go to chat.stackoverflow.com, you can see this.
[3660.36 --> 3663.98]  Now, you can only get in the room if you have 20 Stack Overflow rep.
[3663.98 --> 3665.58]  Hmm.
[3667.52 --> 3668.88]  So essentially, it's a perk.
[3669.72 --> 3674.74]  It's a perk built for, you know, members of the Stack Overflow and Stack Exchange community.
[3674.80 --> 3675.76]  I have never seen this before.
[3676.72 --> 3677.34]  It's awesome.
[3677.56 --> 3679.52]  I think it's the best chat system on the market.
[3679.72 --> 3680.68]  And 20 is pretty low.
[3680.74 --> 3684.02]  That's basically like you answer a question that has the proper answer, right?
[3684.32 --> 3685.90]  Just kind of proves that you're a real person.
[3686.82 --> 3690.32]  Yeah, it's two upvotes on an answer or four upvotes on a question.
[3691.32 --> 3692.32]  So yeah, it's pretty low.
[3692.32 --> 3695.88]  So it's not like we're asking you to move heaven and earth to get on this chat.
[3695.88 --> 3701.14]  But it keeps all the junk away and it makes sure that the people that are on there are already familiar with kind of the system.
[3702.08 --> 3702.58]  That's right.
[3702.72 --> 3705.06]  Because you need sort of a real-time vector.
[3705.38 --> 3707.14]  I mean, it's a different, it's an organizational system.
[3707.84 --> 3710.86]  There is overlap between chat software and forum software.
[3710.86 --> 3715.10]  They're much closer related than I thought when I started this project.
[3716.18 --> 3721.86]  But I think the main difference, if I had to quantify it, is people in a discussion,
[3722.32 --> 3725.28]  in a forum discussion, are willing to type paragraphs to each other.
[3725.48 --> 3726.46]  And they could be short paragraphs.
[3726.58 --> 3727.42]  They could be like two sentences.
[3727.96 --> 3731.06]  Whereas on chat, there's no expectation of even complete thoughts.
[3731.94 --> 3732.12]  Right?
[3732.18 --> 3733.16]  It's just LOL, enter.
[3733.38 --> 3734.14]  Which is fine.
[3734.18 --> 3734.58]  It's chat.
[3734.70 --> 3736.14]  I'm not saying that shouldn't be allowed.
[3736.88 --> 3739.96]  But on chat, like I won't even finish my thought.
[3739.96 --> 3744.86]  I'll just take five random, not even sentences, to complete a thought.
[3744.86 --> 3748.64]  Which is terrible for reading later, right?
[3748.76 --> 3751.76]  It's this huge cost for people to come in after the fact.
[3751.86 --> 3757.38]  It's like it optimizes for the writer, which is the wrong decision ultimately, I think.
[3758.02 --> 3763.60]  Whereas forum software sort of optimizes for the readers a little bit more in that you have paragraphs
[3763.60 --> 3765.72]  and somewhat complete thoughts together.
[3765.72 --> 3773.04]  You don't have to read five interspersed lines to figure out the paragraphs that that person was trying to say.
[3773.14 --> 3780.36]  So if you're a moderator on a discussion, are you encouraged to edit answers to make them maybe easier to read
[3780.36 --> 3781.76]  and things like that, like on GitHub?
[3783.42 --> 3784.22]  You can.
[3784.60 --> 3785.72]  I have been.
[3785.90 --> 3788.02]  Like on HowToGeek, I'm an admin there.
[3788.02 --> 3792.84]  And I will edit to correctly mark down things and just make things a little bit prettier.
[3793.92 --> 3798.94]  But there's absolutely no expectation of other users editing your stuff.
[3799.04 --> 3801.52]  That is really key to understand.
[3802.00 --> 3806.50]  When you get on Stack Overflow and you answer, you should expect other users to edit your stuff.
[3806.84 --> 3809.70]  And if that bothers you, you should not be there.
[3810.42 --> 3812.06]  We try to be really clear about this.
[3812.56 --> 3813.82]  But on discourse, no.
[3814.22 --> 3817.60]  Other users will never, ever be able to edit your stuff.
[3817.60 --> 3821.54]  That's not, even in the plans we have, there's no way to make that happen.
[3821.94 --> 3829.32]  Now, there is this obscure feature we're going to implement where you can opt in for a specific discussion post
[3829.32 --> 3831.30]  to make it editable by other trusted users.
[3831.52 --> 3832.98]  But it's not even implemented yet.
[3833.44 --> 3838.78]  So right now, the only way your content could change about your opinion about the coolest X-Man,
[3838.92 --> 3844.52]  which is obviously Wolverine, is if the moderator edits it.
[3844.74 --> 3846.46]  Other users cannot edit your stuff.
[3846.46 --> 3848.52]  There should be no expectation of peer editing.
[3848.72 --> 3851.22]  I guess that would kind of turn it into a wiki in a way.
[3852.64 --> 3854.58]  More of like an evolving discussional wiki.
[3855.30 --> 3859.00]  Which people like to shove conversations like that into wikis often, and it's a big problem.
[3860.72 --> 3861.28]  That's right.
[3861.52 --> 3862.64]  Well, conversations are a problem.
[3862.80 --> 3864.10]  What did we learn from Stack Overflow?
[3864.22 --> 3867.60]  It's like, people think that discussion is this unfettered good.
[3868.04 --> 3870.84]  Like, there must be discussion because discussion is good.
[3870.84 --> 3873.74]  And we found that that was absolutely not true.
[3873.84 --> 3874.92]  Discussion was bad.
[3875.84 --> 3877.18]  You know, you didn't want discussion.
[3877.30 --> 3882.16]  You wanted the minimum amount of discussion necessary to get the result that you wanted.
[3882.76 --> 3884.98]  And a lot of people object to that, right?
[3885.04 --> 3888.82]  They're like, how can you say that my discussion is not useful or relevant?
[3888.82 --> 3891.36]  And I don't know.
[3891.58 --> 3893.98]  It's the more discussion you have, the less you learn.
[3894.70 --> 3897.22]  That's counterintuitive, but that's kind of what we found.
[3897.48 --> 3898.56]  It just depends what your goal is.
[3898.58 --> 3900.26]  Is your goal to get in the room and learn something?
[3900.48 --> 3906.16]  Or is your goal to sort of hang out, have fun, maybe learn something accidentally?
[3906.30 --> 3907.52]  That's more the Reddit model, right?
[3907.72 --> 3909.90]  I mean, nobody goes to Reddit to learn stuff.
[3909.96 --> 3911.56]  If they do, it's kind of accidental.
[3911.56 --> 3915.68]  And that's okay, because the goal is to be entertained, for the most part.
[3916.46 --> 3918.08]  It's certainly a healthier balance than Dig.
[3918.26 --> 3922.42]  I mean, Dig was a terrible system, because it was just all entertainment.
[3922.58 --> 3925.48]  Reddit at least has some incidental learning that goes on there.
[3926.26 --> 3927.02]  Do you read Hacker News?
[3928.38 --> 3928.94]  I do.
[3930.10 --> 3930.60]  So do I.
[3930.72 --> 3932.38]  I'm trying to wean myself off.
[3932.58 --> 3935.68]  It was my New Year's resolution to not read Hacker News anymore, but I can't do it.
[3937.14 --> 3937.88]  You're addicted.
[3938.84 --> 3939.20]  Unfortunately.
[3939.20 --> 3942.24]  No, I like Hacker News.
[3942.38 --> 3946.08]  I mean, I think it's evolved from what it used to be, but I don't really have any objection
[3946.08 --> 3946.90]  to what goes on there.
[3947.20 --> 3954.32]  There are some complaints about the comments being, you know, not friendly enough, but I
[3954.32 --> 3954.66]  don't know.
[3954.78 --> 3955.86]  It's just a question of the audience.
[3955.96 --> 3958.78]  Like, every audience has its own tone, right?
[3958.82 --> 3961.46]  Like, I'm the guy that was telling you I went to the racist forum.
[3961.58 --> 3961.84]  It didn't.
[3962.22 --> 3967.16]  I mean, I do not condone racism, but I think it's okay for the racists to have a place to
[3967.16 --> 3967.48]  hang out.
[3967.48 --> 3971.92]  So I'm also going to tell you it's okay for the programmers who are a little bit, you know,
[3972.00 --> 3976.36]  aspergery to have a place to hang out and make socially inappropriate comments about
[3976.36 --> 3976.80]  stuff.
[3977.16 --> 3978.36]  I think that's actually okay.
[3978.36 --> 3981.24]  That's what I always found really fascinating about Reddit was that you have all these little
[3981.24 --> 3983.86]  subreddits that, you know, people completely isolate from each other.
[3983.94 --> 3986.20]  So the whole site isn't one large community.
[3986.20 --> 3990.04]  It's a bunch of small communities, which is an interesting thing about discourse.
[3990.32 --> 3995.82]  There's never going to be like a large single installation of like, here is meta discussion
[3995.82 --> 3996.58]  on everything, right?
[3996.60 --> 4000.52]  Everything is topical because there's installations and different versions of it.
[4000.52 --> 4003.00]  I think every community has its own norms.
[4003.26 --> 4008.18]  And I think it's kind of wrong to go in a community that has a certain set of norms and demand that
[4008.18 --> 4010.44]  their norms align with yours.
[4010.80 --> 4013.16]  Now, if what they're doing is illegal, that's a different topic.
[4013.34 --> 4014.62]  It's not illegal to be a racist.
[4014.74 --> 4015.22]  It's dumb.
[4015.34 --> 4015.78]  It's stupid.
[4015.96 --> 4017.16]  It's offensive, right?
[4017.16 --> 4018.38]  But it's not illegal.
[4019.16 --> 4024.66]  So nor is it, you know, illegal to be, you know, a programmer that has ridiculous libertarian
[4024.66 --> 4025.40]  views on everything.
[4025.56 --> 4026.64]  I find it personally offensive.
[4027.88 --> 4029.94]  But, you know, that's what I expect when I go to Hacker News.
[4030.04 --> 4031.04]  That's the kind of stuff I expect.
[4031.26 --> 4034.16]  And they mostly keep it civil, which I think is great.
[4034.58 --> 4036.62]  And it's just, you have to expect that, right?
[4036.68 --> 4040.38]  Like, I mean, I think that the current trope is that anything on Hacker News involving women
[4040.38 --> 4045.86]  just gets crazy, ridiculous responses that don't really make sense in society.
[4047.16 --> 4049.18]  Which I think is partially true.
[4049.62 --> 4050.94]  But, I mean, again, you've got to look at the community.
[4051.06 --> 4055.14]  This is a community of, you know, programmers who have this very logical view of the world.
[4055.34 --> 4059.70]  And, you know, that's what you're going to get to some degree, plus or minus 20%.
[4059.70 --> 4061.64]  And if you don't want that, then, like, don't go there.
[4061.96 --> 4065.76]  Like, who would go to a community of racists and lecture them about not being a racist?
[4066.22 --> 4067.30]  Like, what's the point of that?
[4068.52 --> 4070.58]  Like, I don't know.
[4070.66 --> 4071.64]  I just don't get it, right?
[4071.72 --> 4074.88]  Like, I don't know where I'm going with that.
[4074.88 --> 4076.82]  But every community has its right to a clubhouse.
[4076.82 --> 4079.44]  I was going to save you, but I figured, why not?
[4080.06 --> 4080.60]  Yeah, exactly.
[4080.96 --> 4084.26]  So I got a question for you from, actually, from the chat room.
[4084.94 --> 4086.90]  We are the changelog on Freenode.
[4088.32 --> 4091.66]  And his name is Film424242.
[4091.78 --> 4093.28]  So I'm not sure if that's just random or not.
[4093.66 --> 4094.62]  Is that his real name?
[4094.62 --> 4098.66]  I can't imagine that's his human name, but maybe it's his robot name.
[4100.36 --> 4103.56]  He asks you, you know, why did you go with Ember for the front end?
[4103.74 --> 4109.48]  And kind of what would you recommend to all the other Ember people out there that have built a large application?
[4109.48 --> 4116.84]  Well, Ember is one of those decisions that Robin made where I just trusted Robin's sort of design instincts.
[4116.96 --> 4119.00]  Robin's been building Ruby stuff since 2006.
[4120.62 --> 4124.50]  He built this great game called Forum Wars with a Z.
[4124.72 --> 4126.58]  Forum, W-A-R-Z.
[4126.58 --> 4130.94]  And that's a Ruby app, and he built that in Ruby on Rails, and he built that in 2006.
[4131.38 --> 4133.58]  So he's a very, very experienced programmer.
[4133.70 --> 4136.40]  He's been a programmer since, like, age 11, as he wrote on his blog.
[4137.56 --> 4143.16]  And he said that I had him evaluate, because we had this idea that Discourse is going to be a JavaScript application,
[4143.28 --> 4147.12]  meaning all the functionality is going to be essentially delivered through JavaScript.
[4147.32 --> 4149.06]  It's a ball of JavaScript that comes down.
[4149.06 --> 4154.38]  And it's not traditional HTML and CSS, although we have some of that for Google, so he can spider us.
[4154.80 --> 4156.08]  But it's a ball of JavaScript.
[4156.74 --> 4158.54]  And, you know, how should we build this?
[4158.56 --> 4160.18]  That was the question that I posed to Robin.
[4160.44 --> 4162.64]  And Robin went out and researched a bunch of stuff and came back and said,
[4162.70 --> 4166.44]  you know what, I think Ember is the best way for us to achieve this.
[4166.82 --> 4171.36]  And I just essentially trusted his, you know, instincts on this.
[4171.74 --> 4174.90]  And I do like, I've met Yehuda and Tom.
[4175.00 --> 4177.24]  Those are the two sort of principal people at Ember.
[4177.24 --> 4180.08]  There's a large community, but those are the sort of core figures.
[4180.32 --> 4181.36]  And I like those guys a lot.
[4181.40 --> 4186.66]  I think they're very smart guys, very sharp, very, you know, astute in the way they handle their interactions with the community.
[4187.04 --> 4187.92]  They make good decisions.
[4188.74 --> 4195.62]  Essentially, I just trust the direction of the project based on Robin's, you know, I just trust the people involved, basically.
[4195.84 --> 4201.80]  And I also believe deeply in this concept of JavaScript applications delivered to the browser.
[4201.80 --> 4208.90]  I think it's absolutely the future of a lot of different types of apps on the web versus binary blobs that are delivered to iOS.
[4209.84 --> 4212.10]  I don't think that's going to work out in the long term.
[4212.44 --> 4213.14]  Are there any plans to be?
[4213.14 --> 4214.18]  Somewhat controversial opinion.
[4214.42 --> 4214.76]  Oh, I'm sorry.
[4214.82 --> 4215.08]  Go ahead.
[4215.90 --> 4216.46]  That's okay.
[4217.78 --> 4220.28]  But Ember is still very rapidly evolving, right?
[4220.32 --> 4223.88]  Ember just got to 1.0 basically right at the time we launched in February.
[4224.96 --> 4226.12]  So Ember has a long way to go.
[4226.12 --> 4231.06]  And I realize there's been a lot of complaints about Ember's learnability, like it's kind of intimidating for newbies.
[4231.88 --> 4234.34]  And that's something that we want to help to fix at Discourse.
[4234.48 --> 4235.48]  Like we want to have tutorials.
[4235.60 --> 4243.10]  In fact, Robin has posted on his blog at eviltrout.com, eviltrout.net, several sort of intro tutorials to Ember.
[4243.48 --> 4246.24]  And the Ember team is, you know, very, very aware of this difficulty.
[4246.62 --> 4249.34]  So trying to make it easier to learn.
[4249.34 --> 4249.88]  Gotcha.
[4249.88 --> 4249.96]  Gotcha.
[4251.96 --> 4256.82]  So I guess we're going to kind of start to try and wrap this thing up.
[4256.98 --> 4266.06]  But let me ask you, just one of my coworkers asked me, and he said, you know, since you're a Windows guy, and I think I've actually seen you talk about this.
[4267.30 --> 4269.70]  I want to say I've seen you talk about this on Twitter.
[4269.92 --> 4270.58]  I'm not sure, though.
[4270.58 --> 4278.04]  What are your thoughts on just like Windows 8 and the overall blue feeling and all that stuff just from your experience?
[4278.04 --> 4284.66]  Well, I think Windows 8 had a Frankenstein problem where they built two very different things and combined them.
[4285.58 --> 4287.70]  And I think it does make sense.
[4287.74 --> 4288.80]  You have to look at the numbers.
[4289.12 --> 4294.68]  Because a lot of, you know, hardcore desktop guys like me, like I'm looking at three monitors right now.
[4294.84 --> 4296.44]  Like three giant 27-inch monitors.
[4296.80 --> 4299.52]  This is not a system that works well with Metro UI.
[4300.02 --> 4300.54]  Believe me.
[4300.54 --> 4304.74]  But if you look at the overall market, how many desktops are sold?
[4305.08 --> 4306.40]  How many laptops are sold?
[4306.66 --> 4308.10]  How many tablets are sold?
[4308.80 --> 4311.52]  I mean, I have an iPad 4 and I love it.
[4311.68 --> 4314.54]  And I think that tablets are undeniably the future computer.
[4314.62 --> 4316.86]  My wife has a tablet and doesn't touch her laptop.
[4317.00 --> 4320.12]  Hasn't touched her laptop in probably six months at all.
[4320.40 --> 4321.36]  She just doesn't, right?
[4321.66 --> 4324.68]  So for the regular person, a tablet is the computer.
[4324.68 --> 4324.76]  Sure.
[4325.36 --> 4328.70]  So Windows, I don't know if you noticed, kind of sucks on a tablet.
[4330.20 --> 4336.86]  So Microsoft had this huge problem, which is like their software doesn't work on the computers of the future at all.
[4337.38 --> 4338.88]  So they had to fix this.
[4338.98 --> 4341.86]  I mean, I give them actually huge props for changing so rapidly.
[4342.06 --> 4346.76]  But I think they changed so rapidly that they alienated sort of like old school people,
[4346.88 --> 4349.90]  the enterprises that aren't going to upgrade to tablets anytime soon.
[4350.08 --> 4350.54]  You know what I mean?
[4350.54 --> 4351.10]  Right, yeah.
[4351.16 --> 4354.24]  They made the right decision in building this Frankenstein monster.
[4354.24 --> 4357.64]  They put two things together, like this tablet-centric UI, which is actually very, very nice.
[4357.94 --> 4360.00]  Although it needs some tweaks, it's actually very solid.
[4360.42 --> 4368.70]  Actually, I find myself doing swipes on iPad that work on Windows 8 that are really nice for going back and forward and stuff.
[4370.24 --> 4372.32]  But it's hard to build Frankenstein.
[4372.48 --> 4375.52]  You've got two fundamentally different things that you're trying to smush together, right?
[4375.64 --> 4379.28]  So what Apple did was they have iOS, which is totally alien, different.
[4379.52 --> 4381.28]  And then they have OS X, right?
[4381.46 --> 4383.08]  Two totally different worlds, right?
[4383.08 --> 4386.56]  You're either in tablet land and phone land or you're in desktop land.
[4387.30 --> 4390.90]  And Microsoft chose a different strategy, which is to Frankenstein them together.
[4391.08 --> 4396.70]  And I think I don't know which solution is going to be the better long-term choice.
[4396.86 --> 4400.86]  But it is kind of nice to have the Frankenstein sometimes.
[4400.86 --> 4408.42]  It's just a lot trickier, I think, to get it right because you have to satisfy those two different audiences with the same thing, right?
[4410.16 --> 4412.04]  They didn't finish building Frankenstein.
[4412.44 --> 4416.46]  Windows 8 is a lot better than 7 in terms of startup time, sleep time, resume time.
[4417.26 --> 4419.46]  The task manager is tons better.
[4420.08 --> 4421.86]  There's a lot of – the Explorer, I think, is way better.
[4422.04 --> 4424.24]  File copying is, holy shit, so much better.
[4424.24 --> 4427.82]  So there's good reasons to upgrade to Windows 8.
[4428.34 --> 4433.78]  But hopefully in Windows 8.1 they can sort of make Frankenstein a little more palatable.
[4433.90 --> 4434.72]  They can finish him out.
[4434.78 --> 4436.02]  He's missing a few limbs.
[4438.00 --> 4446.28]  And hopefully Windows 8.1 is going to sort of flesh out the Frankenstein monster a little bit more and make it a little more adaptable.
[4446.52 --> 4450.30]  Because you do get kicked to these different worlds sort of at random, right?
[4450.30 --> 4452.08]  You'll be using tablet mode and all of a sudden you're on the desktop.
[4452.22 --> 4452.76]  Like, what the hell?
[4453.98 --> 4454.74]  And vice versa.
[4454.86 --> 4456.68]  Like, you're on your desktop and I press the Windows key right now.
[4456.70 --> 4458.28]  It's like, oh, my God, what is this, right?
[4458.64 --> 4459.90]  It's like this totally different UI.
[4460.78 --> 4462.26]  And there's literally no start button at all.
[4462.36 --> 4466.46]  There's no way to enable it or there's no third-party one that you can turn on either, right?
[4467.06 --> 4472.72]  Well, the latest news is they're actually going to put in a start button equivalent that just essentially lets you launch.
[4472.72 --> 4474.46]  It's the same as pressing the Windows key, right?
[4474.72 --> 4475.16]  That would be good.
[4475.26 --> 4475.88]  It doesn't do anything.
[4476.16 --> 4478.16]  It's not an actual start menu like Windows 7, though.
[4478.30 --> 4479.60]  At least that's the latest I heard.
[4481.26 --> 4481.62]  Yeah.
[4481.86 --> 4482.20]  All right.
[4482.26 --> 4484.56]  So we're going to go ahead and close out with this question for you.
[4484.66 --> 4489.92]  And it's kind of a traditional question that we ask everyone on the podcast.
[4490.18 --> 4492.78]  And who would you say is your programming hero?
[4492.96 --> 4495.32]  Who would you say you've looked up to?
[4495.38 --> 4499.22]  I know you said Anders about the language stuff, but who would you say is your programming hero?
[4499.92 --> 4506.90]  Well, I've got to say Steve McConnell because of the Coding Horror logo itself is from the Steve McConnell book, Code Complete.
[4506.90 --> 4522.04]  And what I loved about Steve McConnell and the book Code Complete was that he was a programmer who kind of put ego aside and looked at – his programming is a very egocentric activity for whatever reason, which is I think maybe again why Hacker News gets so weird all the time.
[4522.04 --> 4534.98]  And learning to, like, put your ego aside and realize that you're the source of all your problems and that your code is bad, even when it's good, it's bad, is really critical to understanding that.
[4534.98 --> 4540.30]  And Steve McConnell sort of walks you through that in this very patient voice, and he uses a lot of data.
[4540.72 --> 4543.06]  He cites a lot of data and studies that were done.
[4543.14 --> 4548.38]  It isn't just here's my opinion and I'm right because I'm an extreme programmer that has written 30,000 lines of code.
[4548.42 --> 4549.78]  He was like, look at this data.
[4549.94 --> 4551.16]  Look at these studies that were done.
[4551.26 --> 4552.58]  Look at this analysis, right?
[4553.00 --> 4560.20]  And I love that, this appeal to data rather than appeal to authority or appeal to, you know, who's the gnarliest programmer, you know?
[4560.20 --> 4568.94]  So it's like put all that stuff aside and just concentrate on the results, concentrate on the data, and, you know, getting things done in a way that doesn't make everybody hate you.
[4569.16 --> 4571.48]  And he did that in general or in Code Complete specifically?
[4571.52 --> 4572.14]  In Code Complete.
[4572.30 --> 4574.44]  The Code Complete is a very philosophical book.
[4574.52 --> 4574.90]  It's weird.
[4574.98 --> 4579.76]  It's a book about code, but it's – there's a lot of stuff about personal character in that book.
[4580.96 --> 4582.76]  And it really resonates.
[4582.86 --> 4585.20]  Plus he's just a – he's a nice Midwestern guy.
[4585.32 --> 4587.88]  He's just a very likable guy, and it really comes across in his book.
[4587.88 --> 4593.80]  So if you want to be likable as a programmer, I strongly recommend reading Code Complete very closely.
[4595.26 --> 4595.50]  All right.
[4595.56 --> 4596.04]  Well, thank you.
[4596.18 --> 4599.08]  And for everyone that was listening, it was a great time talking with you, Jeff.
[4599.12 --> 4604.20]  Once again, if you don't know who Jeff Atwood is, first get out from under your rock and then follow him on Twitter.
[4604.40 --> 4606.12]  It's at Coding Horror on Twitter.
[4607.34 --> 4611.12]  It was great to have you today, Jeff, and look forward to the next time we get to talk.
[4611.82 --> 4612.20]  Yeah, thanks.
[4612.20 --> 4618.56]  And then anyone who's interested, please go to discourse.org and check out the project.
[4618.82 --> 4619.46]  Install it locally.
[4619.82 --> 4620.24]  See what you think.
[4620.32 --> 4622.22]  I was meaning to ask, are you looking for contributions?
[4623.58 --> 4624.12]  Oh, absolutely.
[4624.22 --> 4624.48]  Always.
[4624.60 --> 4628.22]  In fact, I will make one call to arms on this podcast.
[4628.64 --> 4630.16]  Our diff is terrible.
[4631.16 --> 4632.62]  We do have revision tracking.
[4632.86 --> 4634.56]  Like as you edit post, it shows the revisions.
[4634.70 --> 4636.46]  It's a little pencil icon in the left gutter.
[4636.62 --> 4637.14]  It's kind of tiny.
[4637.14 --> 4640.04]  And our diff is horrendously bad.
[4640.14 --> 4645.88]  If anyone wants to take that on and actually produce a nice visual diff of, oh, look, this is what changed when this user edited their post.
[4646.08 --> 4646.98]  I would love that.
[4647.50 --> 4648.88]  It's really bad right now.
[4650.24 --> 4653.78]  So, yeah, if anyone wants to, you know, dig in, there's a place.
[4654.68 --> 4655.32]  Sounds awesome.
[4656.54 --> 4657.26]  All right, guys.
[4657.50 --> 4658.26]  I'll say goodbye.
[4658.58 --> 4659.04]  See you all later.
[4659.04 --> 4660.48]  Thanks.
[4667.14 --> 4668.58]  Bye.
[4668.58 --> 4682.48]  Bye.
