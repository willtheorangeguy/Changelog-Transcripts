[0.00 --> 18.30]  Welcome to the ChangeLog episode 0.6.0.
[18.56 --> 19.54]  I'm Adam Stachowiak.
[19.90 --> 20.76]  And I'm Wynne Netherland.
[20.96 --> 21.88]  This is the ChangeLog.
[21.94 --> 23.52]  We cover what's fresh and new in open source.
[24.04 --> 26.86]  If you found us on iTunes, we're also on the web at thechangelog.com.
[27.10 --> 28.00]  We're also up on GitHub.
[28.00 --> 29.90]  Head to GitHub.com slash explore.
[29.98 --> 34.26]  You'll find some trending repos, some feature repos from the blog, as well as our audio podcasts.
[34.48 --> 37.54]  If you're on Twitter, follow ChangeLog Show and me, Adam Stach.
[37.88 --> 40.40]  And I'm Penguin, P-E-N-G-W-Y-N-N.
[40.74 --> 42.76]  And this episode is sponsored by GitHub Jobs.
[42.86 --> 45.74]  Head to thechangelog.com slash jobs to get started.
[46.34 --> 49.60]  If you'd like to feature your job on this show, select Advertise on the ChangeLog.
[50.02 --> 51.60]  When you post your job, we'll take care of the rest.
[52.16 --> 54.14]  A couple of jobs up this week by Mag10.
[54.72 --> 57.60]  They're rethinking publishing without the analog boundaries.
[57.60 --> 64.54]  The first is a senior iOS developer, architect prototype, and release complex iPad and iPhone apps.
[65.24 --> 72.96]  Your rig will include standard MacBook Pro, AirCine display, iPad, and iPhone, and stock options.
[73.74 --> 79.52]  But if you're on the web side, Mag10's also looking for software engineers for their web front end.
[79.76 --> 82.36]  Must be familiar with HTML5, CSS3, and JavaScript.
[82.36 --> 87.54]  Same rig applies as the iOS position.
[88.20 --> 89.36]  If you're interested in these two.
[89.70 --> 93.64]  LG.gd slash AO and AP.
[94.42 --> 95.96]  And next up is Tag.
[96.06 --> 99.10]  TagDink is the number one place to make new friends online.
[99.20 --> 102.82]  They're looking for a software engineer full-time in the San Fran area.
[102.94 --> 104.26]  That's San Francisco, California.
[104.84 --> 110.06]  Their stack is PHP, Java, Oracle, and HTML and Ajax on the client side.
[110.16 --> 113.76]  They're currently looking for better ways to do many, many things.
[113.86 --> 114.56]  They're building APIs.
[114.56 --> 118.34]  They're reducing spam, scams, and phishing, and much, much more.
[118.46 --> 124.46]  So if you have a BS or an MS in computer science or related fields, they have competitive salaries to offer you,
[124.54 --> 128.10]  generous stock options, quarterly compensation, as well as a 401k.
[128.20 --> 130.02]  Check out lg.gd slash AT.
[130.70 --> 131.86]  Fun episode this week.
[131.98 --> 134.42]  Talk to Wesley Berry over at Engine Yard.
[134.64 --> 138.96]  This is the last of our Red Dirt RubyConf recordings.
[138.96 --> 139.08]  Thanks.
[140.02 --> 142.14]  So long, Oklahoma City, until next year.
[143.24 --> 149.08]  But we talked about his Fog gem, a little bit about XCon, and how the Fog gem came about.
[149.18 --> 153.76]  So Fog is kind of the uber wrapper for all the cloud APIs from a Ruby perspective.
[154.22 --> 157.22]  And this is also our 60th episode.
[157.76 --> 158.48]  60th episode.
[158.58 --> 159.20]  Can you believe that?
[159.44 --> 160.92]  That's a lot of numbers.
[161.04 --> 163.34]  That's three digits, a couple points in there.
[163.42 --> 164.18]  It's a point release, too.
[164.26 --> 164.90]  So that's cool.
[165.56 --> 168.00]  Thanks, everyone, for putting up with us this long.
[168.00 --> 172.44]  Hopefully, we've got another 60 episodes in us, at least.
[172.86 --> 176.40]  And we've got some fun upcoming things happening, too, as well, on the advertising side.
[176.50 --> 177.44]  So stay tuned to that.
[177.62 --> 180.08]  And some fun new episodes coming up.
[180.62 --> 181.04]  Absolutely.
[181.56 --> 190.68]  And as far as conferences coming up, I'll be at TexasJS next month, and then Big D in Dallas in July.
[190.80 --> 191.32]  How about you, Adam?
[191.40 --> 191.92]  Any plans?
[192.26 --> 193.34]  I'll be there as well, Big D.
[193.34 --> 196.82]  And I'm also going to New York for a design conference.
[196.96 --> 200.18]  But I'm not sure if I'll attend, but I'm definitely going to be in New York later in this year, August.
[200.88 --> 201.20]  Awesome.
[201.82 --> 202.40]  Fun episode.
[202.50 --> 202.98]  Should we get to it?
[203.18 --> 203.68]  Let's do it.
[203.68 --> 218.72]  Thanks for coming out to a special live edition of the Change Log podcast with video this year.
[218.96 --> 225.30]  So in addition to the dozens of people in the room, probably half as many on the interwebs watching this live.
[225.96 --> 228.30]  And I hope to get a couple of episodes out of this.
[228.30 --> 232.14]  So in case you don't know, this is not Adam Stachowiak, my partner in crime usually.
[232.34 --> 235.12]  This is Wesley Berry of the Fog Gym.
[235.64 --> 239.36]  I'm going to chat a little bit about fog and all things cloud.
[240.02 --> 251.18]  I think we should start with the fog in the room of AWS outage today and reactions to half the interweb going down.
[251.18 --> 255.26]  It's been kind of a mess, as you well know.
[255.50 --> 262.24]  I mean, that's one of the things you have to worry about more in the cloud is you gain a lot of flexibility and power,
[262.46 --> 267.56]  but you lose a certain amount of control and knowledge of what's actually going on behind the scenes.
[267.86 --> 273.50]  So unfortunately, that sometimes means stuff will go down and there's not really very much you can do about it.
[273.56 --> 277.36]  It's not like you can drive over to the data center and swap out some hard drives or something.
[277.50 --> 278.86]  There's just not that much you can do.
[278.86 --> 287.76]  But I mean, I think the real testament to the services like that is that when it goes down, it is such a big deal.
[288.28 --> 294.20]  Like it's happened so infrequently that when it does, everyone is very surprised and terrified and whatnot.
[294.44 --> 297.18]  So I mean, I think the vast majority of the time it works very well.
[297.38 --> 306.92]  And so for those that might not know, tell us a bit about, I guess, fog as its scope and a little bit of background on how the project came about.
[306.92 --> 314.18]  Sure. So fog is probably the biggest yak shave that I've ever participated in.
[315.00 --> 322.80]  It started just as, ironically, it started with me wanting to know more about cloud services in general, but specifically about simple DB.
[322.80 --> 329.10]  As it turns out, simple DB is a very small and relatively unimportant portion of fog at this point.
[329.22 --> 333.90]  But that was the impetus is that there wasn't a good Ruby binding to simple DB.
[334.18 --> 335.36]  I wanted to play with simple DB.
[336.36 --> 337.26]  So I wrote one.
[337.80 --> 340.12]  And then pretty soon I was like, well, this is interesting.
[340.32 --> 342.20]  I don't know how interesting, but it's kind of interesting.
[342.20 --> 344.30]  And I want to play with S3.
[344.66 --> 356.98]  And then I started looking at some of the existing tools and had some level of dissatisfaction about how maintained they were and how up to date they were and how open the processes were around that open source stuff.
[357.12 --> 361.02]  You know, like whether or not I could help to make them be maintained or help to bring them up to date.
[361.40 --> 363.16]  And it seemed like there was a lot of open question there.
[363.16 --> 366.96]  So I started just writing some of my own S3 stuff.
[367.10 --> 370.50]  And I had reused some of the lessons I'd learned from doing the simple DB one.
[371.10 --> 373.04]  And so this kind of continued on and on.
[373.48 --> 376.44]  I never really had a particular reason to need these services.
[376.64 --> 377.50]  I was just very curious.
[377.68 --> 378.98]  I wanted to learn cloud.
[379.20 --> 380.36]  It seemed like a good way to do it.
[381.98 --> 383.84]  And then pretty soon I had all of these services.
[384.16 --> 385.94]  And then Rackspace servers came out.
[386.00 --> 387.22]  And I was like, well, this is interesting.
[387.72 --> 389.12]  I also want to try this.
[389.24 --> 391.28]  And so pretty soon I had a Rackspace servers implementation.
[391.28 --> 396.06]  And before too long I had multiple implementations of, say, Compute.
[396.44 --> 400.96]  And I realized that it was a huge pain to switch back and forth between them.
[401.00 --> 405.46]  I mean, like, if you've ever tried to switch back and forth between them at all,
[405.56 --> 406.96]  like, it becomes very clear.
[407.06 --> 410.14]  Like, it's not difficult to imagine that this is a hard problem.
[410.78 --> 414.72]  And so then all of a sudden there was sort of this use case.
[414.82 --> 417.18]  There was this purpose for Fog, which was, you know,
[417.22 --> 419.04]  I think I can actually make that problem easier.
[419.04 --> 422.46]  Like, I have this strong foundation to build on top of.
[422.58 --> 426.70]  So let me use that to provide things that will actually make this transition easier
[426.70 --> 428.42]  and make these things more comparable.
[429.14 --> 432.88]  How many providers do you support now in addition to EC2 and Rackspace?
[433.90 --> 436.38]  I don't even know a number offhand.
[436.52 --> 437.90]  It seems to continue growing.
[437.98 --> 440.46]  I've been lucky enough to recently there's been some providers
[440.46 --> 444.02]  where they actually were interested enough in the project and the community
[444.02 --> 448.06]  that they just said, here is an implementation of our service.
[448.80 --> 449.78]  Could you please include it?
[449.92 --> 451.74]  Like, there was very little work that I had to do.
[452.08 --> 454.74]  Both Bluebox and Brightbox have been kind enough to do that
[454.74 --> 457.62]  with their pretty recent cloud offerings, which has been awesome.
[458.30 --> 462.06]  So for a while it was just kind of like whatever service piqued my interest,
[462.18 --> 465.02]  the same as the EC2 and Rackspace server's case of like,
[465.08 --> 466.14]  oh, this seems interesting.
[466.26 --> 467.10]  I want to check that out.
[467.10 --> 470.74]  Or, you know, oh, I've had four people ask me about this,
[470.78 --> 472.54]  so maybe I'll go and look into it.
[473.40 --> 475.66]  But yeah, more and more it's the providers driving it.
[475.68 --> 477.08]  So it's become a pretty large number.
[477.18 --> 478.78]  I don't know that I can put my finger right on it,
[478.84 --> 481.32]  but between all of the different things,
[481.36 --> 484.20]  it's probably, I don't know, like 15 to 20.
[485.20 --> 488.64]  Not just compute providers, but because there's also storage and DNS,
[489.00 --> 493.64]  there's some distribution of like services that are on one provider for DNS,
[493.94 --> 495.72]  but a different provider for something else.
[495.72 --> 499.46]  So before we started, Dr. Nick came up and said,
[499.54 --> 502.28]  I'm not sure if you're aware, but that AWS has been down all day.
[502.44 --> 505.16]  And this might be because you have a lot of these services
[505.16 --> 506.52]  stubbed out when you're testing.
[506.76 --> 508.46]  So when did that come about?
[508.54 --> 511.44]  And was it just a large EC2 build that spawned the mocking?
[512.42 --> 516.50]  So yeah, there's a lot of mocking underneath the covers and fog.
[516.62 --> 520.64]  And the idea is that you can kind of run against these services
[520.64 --> 522.22]  in a more simulated manner.
[522.22 --> 526.52]  And that actually came from the usage of EC2 that we had at Engine Yard.
[526.74 --> 530.86]  So I started Fog prior to starting at Engine Yard,
[530.96 --> 532.58]  and then I joined the App Cloud team,
[532.72 --> 535.04]  which makes pretty heavy usage of EC2.
[535.22 --> 539.40]  Like we're probably one of the larger consumers as individuals
[539.40 --> 543.36]  because we sort of proxy all the traffic of our customers effectively into it.
[543.36 --> 549.74]  And so they had built a solution on top of right AWS
[549.74 --> 551.42]  that provided a lot of mocking
[551.42 --> 554.72]  because they got a lot more kind of bang for the buck in terms of testing.
[555.10 --> 557.26]  Because you don't want to really have to wait for a server
[557.26 --> 559.00]  to spin up for each of your unit tests
[559.00 --> 560.96]  and then break it back down again or something
[560.96 --> 563.52]  because servers can take minutes to spin up.
[563.60 --> 566.94]  And if you add minutes to the before each filter in your RSpec,
[566.94 --> 571.08]  you're not going to get your test suite done once a week or something.
[571.22 --> 572.42]  You'll see whether or not it's green,
[572.54 --> 574.00]  and then what do you do?
[574.38 --> 576.48]  So it came from that need.
[576.60 --> 579.38]  Like I knew that if I was going to get Engine Yard to adopt Fog
[579.38 --> 581.56]  because I felt that there were a lot of other merits for it
[581.56 --> 585.22]  in terms of performance and stability and maintainability
[585.22 --> 586.04]  and that sort of thing,
[586.46 --> 588.70]  that I needed to be able to provide the mocks as well
[588.70 --> 591.30]  so that it could be closer to a drop-in replacement.
[591.30 --> 594.58]  But it's also provided a lot of utility in terms of,
[595.06 --> 598.88]  oh, I want to just start to hack out some scripts against this
[598.88 --> 600.68]  without necessarily having to worry about
[600.68 --> 603.82]  whether I forget to spin down all the servers afterward or something.
[603.96 --> 606.96]  It can be a very nice playground kind of sandbox environment as well.
[607.74 --> 609.82]  It's been the biggest boost other than, I guess,
[609.88 --> 614.20]  food on the table of the project before and after the move to Engine Yard backing.
[615.88 --> 618.24]  It's been very interesting.
[618.24 --> 621.64]  I mean, a lot of it has just been Dr. Nick has been really great
[621.64 --> 623.04]  in terms of providing support,
[623.42 --> 625.50]  and he has a lot of very good ideas,
[625.64 --> 628.18]  and there's a lot of good back and forth with him
[628.18 --> 628.96]  that's been very helpful.
[629.76 --> 631.94]  There's also been a lot of good back and forth
[631.94 --> 633.18]  that I'm sure I could have had,
[633.24 --> 634.76]  but I kind of like have the end now
[634.76 --> 637.88]  with the Rubinius guys and with the JRuby guys
[637.88 --> 640.34]  where they've kind of been around the block
[640.34 --> 641.68]  and done this a little bit longer than me,
[641.78 --> 642.50]  so I'll be like,
[642.84 --> 645.22]  I'm thinking about doing this or that with my community.
[645.22 --> 648.48]  Like, I'm thinking about what I should do with my commit bit.
[648.58 --> 649.48]  What are you guys doing?
[649.68 --> 650.78]  How is that working for you?
[650.84 --> 651.74]  Would you recommend it?
[652.80 --> 654.70]  So that's the more obvious part.
[654.80 --> 656.22]  The maybe less obvious part is
[656.22 --> 658.20]  there's a lot of things as a hobby project
[658.20 --> 660.28]  that you don't necessarily get around to
[660.28 --> 661.42]  because they aren't as fun.
[662.18 --> 664.26]  So I'm, like, terrible about this
[664.26 --> 665.62]  in terms of, like, the documentation.
[665.98 --> 667.14]  I know it could use a lot of work.
[667.22 --> 668.36]  People tell me that all the time.
[668.46 --> 670.78]  I feel guilty and bad about it,
[670.84 --> 672.36]  but, like, when it was my hobby project,
[672.36 --> 673.60]  I didn't want to come home from work
[673.60 --> 675.08]  and spend two hours writing documentation.
[675.26 --> 678.50]  I wanted to hack on whatever cool new cloud thing was going on.
[679.28 --> 681.68]  And so having it be my full-time job
[681.68 --> 683.82]  means that I'm still not the best about it,
[683.86 --> 685.50]  but I don't, it's easier for me
[685.50 --> 687.08]  to dedicate an hour or two a day
[687.08 --> 688.52]  or at least a few hours a week
[688.52 --> 691.10]  to just trying to at least polish that up a little bit.
[692.02 --> 693.86]  So that's been a boon as well.
[693.86 --> 696.72]  One of the unique things that I've heard you do
[696.72 --> 698.28]  that I'm not sure other projects do this,
[698.28 --> 702.06]  is you base the T-shirt on
[702.06 --> 704.22]  whether or not you're a committer or a friend of Fog.
[704.30 --> 705.74]  So how did that idea come about?
[707.10 --> 710.40]  I don't know exactly what spawned that on.
[710.48 --> 711.72]  You've got to earn one of these, right?
[711.84 --> 713.58]  You do have to earn the shirts.
[714.70 --> 717.04]  I mean, to some extent, like, I've been a long-time gamer,
[717.26 --> 719.22]  and so to some extent it's this kind of idea
[719.22 --> 721.26]  of almost, like, the achievements or badges
[721.26 --> 722.66]  that you have on a lot of other services
[722.66 --> 725.70]  of, like, this is just, like, a physical badge, right?
[725.70 --> 728.48]  So in my case, like, you can get a blue shirt
[728.48 --> 731.00]  if you do something that's kind of supporting
[731.00 --> 733.76]  but not directly code-related for Fog.
[733.96 --> 737.16]  You can get gray if you get something accepted into Fog,
[737.18 --> 739.26]  and then you can get black if you become a committer,
[739.72 --> 743.54]  which I'm terrible about in terms of that still is only me.
[743.70 --> 745.24]  Like, I need to give commit out to other people.
[745.36 --> 746.52]  That's a difficult problem.
[746.62 --> 748.04]  It's one I've discussed with a lot of people.
[750.16 --> 753.06]  But, yeah, it's worked out really well, I think.
[753.14 --> 754.38]  People really like the shirts.
[754.38 --> 755.40]  They respond to them well.
[756.10 --> 758.00]  It's not really that expensive,
[758.30 --> 759.54]  because, as it turns out,
[759.88 --> 761.68]  most open-source projects don't get
[761.68 --> 765.26]  the thousands of committers that, you know, say, Rails does.
[765.44 --> 767.06]  I mean, I still, at this point,
[767.10 --> 769.84]  have gotten to a total of 50 or 60 contributors.
[770.02 --> 771.22]  And I mean, like, that's not free,
[771.42 --> 774.70]  but, I mean, 50 or 60 t-shirts is well worth it,
[774.74 --> 776.60]  in my mind, for the amount of extra support.
[777.00 --> 779.44]  And, you know, like, it makes me feel good
[779.44 --> 781.40]  to have these people come in and help me out,
[781.84 --> 783.62]  because there's so much that I can't do on my own.
[783.62 --> 787.80]  And the value of it is way more than the 10 or 12 bucks
[787.80 --> 789.54]  or whatever that I spend on a t-shirt for them.
[789.88 --> 792.56]  So we heard earlier today that Aaron Patterson said that
[792.56 --> 797.44]  the plus one is the most useless comment that you could put on a pull request.
[797.44 --> 801.06]  You've got 152 forks of Fog and only four pull requests.
[801.18 --> 802.58]  How do you manage that queue?
[803.00 --> 804.40]  Is it all you, or...?
[804.40 --> 806.50]  Right now, at least, it is all me.
[807.14 --> 808.48]  I'm pretty responsive to it.
[808.58 --> 810.52]  I'm lucky in that a lot of the pull requests
[810.52 --> 814.20]  are very small and fairly obvious.
[815.54 --> 818.72]  In a lot of cases, there's, like, Fog has a pretty large scope,
[818.82 --> 820.94]  but most of the time if someone is fixing an issue,
[821.38 --> 822.28]  they tend to be like,
[822.28 --> 824.52]  I'm using service foo,
[824.86 --> 827.30]  and when I do X, I expect Y,
[827.40 --> 828.38]  but I'm actually getting Z.
[828.62 --> 831.08]  So here is, you know, like, the two-line fix
[831.08 --> 834.54]  that gives me back what I expect from this one particular request.
[835.12 --> 837.32]  So that actually makes those a lot easier to get through.
[837.96 --> 839.28]  I just have...
[839.92 --> 841.82]  I usually basically get in in the morning
[841.82 --> 845.12]  and do pull requests, respond to issues, and all of that.
[845.36 --> 847.82]  Like, I do all of that before I ever let myself code.
[847.82 --> 851.12]  So that helps me to make sure that I stay on top of it.
[851.30 --> 854.08]  It usually takes a couple hours pretty much every workday,
[854.28 --> 857.28]  but, yeah, you just have to be really diligent.
[858.06 --> 859.58]  Tell us about XCon.
[859.70 --> 862.56]  Is that a byproduct of Fog, or did it predate Fog?
[863.66 --> 864.22]  Sure.
[864.42 --> 868.38]  So XCon is the HTTP library that underlies Fog.
[869.50 --> 873.16]  It came about, actually, while I was working on Fog itself.
[873.16 --> 876.88]  I was somewhat dissatisfied with the interfaces
[876.88 --> 878.60]  to some of the existing HTTP libraries.
[878.86 --> 881.58]  Like, figuring out how to use NetHttp
[881.58 --> 883.54]  always meant me referring to the docs.
[883.66 --> 884.74]  Like, I can never actually remember,
[884.90 --> 886.52]  and there's, like, four different ways you can do it.
[886.72 --> 888.64]  It's not clear if some are better than others.
[889.32 --> 890.70]  And for the use case that I wanted,
[890.80 --> 893.86]  which was most of the time if you're working with a cloud service,
[893.94 --> 895.16]  you're probably going to connect to it,
[895.54 --> 897.14]  and you're probably going to make several requests.
[897.42 --> 899.16]  It's unlikely that you're going to just connect
[899.78 --> 900.98]  and do one thing and be done.
[900.98 --> 902.84]  Like, you're probably going to spin up a server
[902.84 --> 904.96]  and maybe attach a volume and so on and so forth.
[905.04 --> 905.98]  Like, it's going to be a few things.
[906.48 --> 907.76]  So I wanted to be able to take advantage
[907.76 --> 909.50]  of keep a lot of connections wherever I could,
[910.20 --> 913.18]  which is also, you know, if it was hard to figure out
[913.18 --> 914.56]  how to do requests in the first place,
[914.58 --> 915.92]  it's, like, extra hard to figure out
[915.92 --> 917.14]  how to keep that connection open
[917.14 --> 918.82]  after the request is done
[918.82 --> 920.72]  to make sure that you can take advantage of that.
[921.50 --> 923.90]  So initially, XCon actually ended up being
[923.90 --> 925.36]  inside of Fog itself.
[925.58 --> 929.04]  There was just, like, a Fog slash HTTP file, basically,
[929.04 --> 931.12]  that encapsulated all of that.
[931.44 --> 934.60]  And over time, I started to realize, you know,
[934.96 --> 938.56]  granted, the scope of Fog is already kind of ridiculous,
[938.96 --> 941.50]  but having an HTTP library inside of it
[941.50 --> 943.14]  is, like, kind of beyond ridiculous.
[943.36 --> 944.44]  Like, this is just not okay.
[944.62 --> 946.52]  So at that point, I split it out.
[946.54 --> 947.48]  And it's actually been really nice
[947.48 --> 949.24]  because there have been a number of bugs
[949.24 --> 950.38]  and other things that have been fixed
[950.38 --> 953.22]  by virtue of the fact that it's clearly an HTTP library
[953.22 --> 954.42]  that's off on its own
[954.42 --> 956.78]  that maybe would have remained indefinitely
[956.78 --> 958.92]  had it just stayed kind of at the low level,
[959.02 --> 960.10]  hidden behind the scenes of Fog.
[960.76 --> 963.76]  Up to 15 services across storage, compute, DNS.
[965.24 --> 967.78]  Talk a bit about the state of the cloud.
[968.26 --> 972.10]  Are we emerging with standards in storage APIs,
[972.30 --> 973.48]  or is S3 one the day?
[975.24 --> 977.24]  It's a difficult question.
[978.56 --> 981.00]  It seemed like S3 was definitely a frontrunner,
[981.04 --> 981.88]  to say the very least.
[982.04 --> 983.78]  I mean, a lot of new services that were coming out
[983.78 --> 986.78]  were just saying, kind of punting and saying,
[986.94 --> 990.10]  we're just going to offer an S3-compliant API.
[991.76 --> 993.10]  Unfortunately, in my experience,
[993.26 --> 997.06]  compliant APIs, like, I don't even know what that means.
[997.18 --> 999.38]  I'm not sure that the people that say it know what it means.
[1000.20 --> 1002.94]  For instance, the Google Storage API
[1002.94 --> 1005.84]  is ostensibly S3-compliant,
[1005.94 --> 1008.42]  but it's compliant to the version of S3
[1008.42 --> 1010.34]  that was available when they released it.
[1010.74 --> 1010.80]  Right.
[1010.80 --> 1013.42]  Which, I'm not sure that they say what version that is,
[1013.46 --> 1015.00]  but I mean, like, it's drifted away from that.
[1015.80 --> 1017.80]  And then, you know, there are other things like
[1017.80 --> 1019.76]  the Rackspace storage,
[1020.10 --> 1022.68]  which that has, you know,
[1022.76 --> 1024.70]  obviously strongly influenced the OpenStack
[1024.70 --> 1026.20]  implementation of storage.
[1026.78 --> 1028.38]  But those haven't gotten really any adoption
[1028.38 --> 1029.78]  outside of Rackspace itself,
[1029.96 --> 1033.52]  so it's not really clear where that will go.
[1034.04 --> 1034.48]  I don't know.
[1034.54 --> 1036.64]  S3, I think, did a pretty good job in a lot of ways.
[1037.12 --> 1038.86]  I don't necessarily like the global namespace
[1038.86 --> 1041.30]  of all of the buckets have to be in the same namespace
[1041.30 --> 1041.80]  kind of thing,
[1041.94 --> 1044.80]  but mostly it seems to work really well.
[1044.96 --> 1046.30]  So did it win the day?
[1046.56 --> 1047.18]  I don't know.
[1047.26 --> 1048.56]  There are probably things that could be done better,
[1048.70 --> 1051.80]  but they have such a front-runner role at this point
[1051.80 --> 1053.92]  that I don't know that anybody's going to overtake them.
[1054.18 --> 1055.40]  What's your take on OpenStack?
[1055.46 --> 1056.90]  Is it truly commodity,
[1057.20 --> 1058.36]  or is it at least common denominator?
[1060.58 --> 1061.42]  It's tricky.
[1061.76 --> 1064.02]  There are a lot of chefs in the...
[1064.02 --> 1064.62]  No pun intended?
[1064.74 --> 1065.64]  No, no pun intended.
[1065.74 --> 1066.78]  There's a lot of cooks in the kitchen.
[1066.78 --> 1068.50]  That's what I intended to say.
[1068.90 --> 1071.46]  The chef thing was sort of terrible,
[1071.74 --> 1073.96]  like quadruple entendre or something.
[1075.12 --> 1076.40]  There are a lot of cooks in the kitchen.
[1076.56 --> 1077.30]  That concerns me.
[1078.10 --> 1080.02]  I mean, a couple of primary players
[1080.02 --> 1081.24]  are NASA and Rackspace.
[1081.96 --> 1084.20]  NASA wants a supercompute platform.
[1084.58 --> 1086.30]  Rackspace wants a public cloud offering.
[1087.34 --> 1090.02]  It's hard to think that that won't mean
[1090.02 --> 1091.12]  that either one of them loses
[1091.12 --> 1093.48]  or that it is lowest common denominator
[1093.48 --> 1095.64]  because those are two pretty different use cases.
[1096.78 --> 1098.76]  And I also just...
[1098.76 --> 1100.78]  I'm not sure how exciting it is
[1100.78 --> 1102.82]  because, I mean, it's...
[1102.82 --> 1104.32]  The analogy I was using earlier
[1104.32 --> 1105.96]  when I was discussing this with somebody was...
[1106.64 --> 1108.04]  It's kind of like somebody
[1108.04 --> 1109.48]  open sourcing the plans
[1109.48 --> 1110.74]  for a nuclear power plant, right?
[1111.16 --> 1112.34]  That's pretty cool, right?
[1112.46 --> 1114.62]  But I'm not going to go build a nuclear power plant.
[1114.74 --> 1115.56]  Like, I'm not interested
[1115.56 --> 1117.34]  in getting into the utility business.
[1117.80 --> 1118.76]  There's a lot of overhead
[1118.76 --> 1119.94]  to getting into the utility business.
[1120.06 --> 1121.40]  Even if I did get into it,
[1122.12 --> 1124.58]  it's likely that if the other utilities wanted to,
[1124.58 --> 1126.32]  they could crush me on price
[1126.32 --> 1127.54]  because they just have the scale
[1127.54 --> 1128.46]  to be able to do that.
[1128.88 --> 1130.72]  Like, I'm not sure that it's going to really invite
[1130.72 --> 1133.04]  other people into the market
[1133.04 --> 1135.70]  as much as a lot of us might like for it to.
[1136.96 --> 1137.74]  So I'm not sure.
[1137.94 --> 1142.04]  I worry that it's kind of a marketing effort
[1142.04 --> 1143.88]  more than necessarily a technology one.
[1144.34 --> 1145.32]  I've been interviewed...
[1145.32 --> 1146.48]  You hit a cat a couple of times,
[1146.60 --> 1148.60]  and he said himself
[1148.60 --> 1150.48]  that he builds more frameworks
[1150.48 --> 1151.10]  than he builds apps
[1151.10 --> 1152.66]  on top of those frameworks, right?
[1152.66 --> 1153.86]  What are you building in the cloud
[1153.86 --> 1155.94]  when you're not building libraries to consume it?
[1156.82 --> 1158.72]  Right now, not very much, unfortunately.
[1158.88 --> 1159.60]  There's been a few times
[1159.60 --> 1161.36]  where I've kind of, like, made small forays.
[1161.46 --> 1162.32]  The most recent was
[1162.32 --> 1164.14]  I've been very interested in React,
[1164.34 --> 1165.36]  so I was writing some stuff
[1165.36 --> 1166.88]  to just play with React and use it.
[1167.38 --> 1169.34]  And it was pretty fun
[1169.34 --> 1170.96]  because now that I, you know,
[1170.96 --> 1173.00]  kind of have this fog in my toolbox,
[1173.70 --> 1174.48]  I could pull that out,
[1174.54 --> 1175.54]  and then, like, a couple hours,
[1175.62 --> 1176.18]  I'd written a script
[1176.18 --> 1177.82]  that I could basically run a command
[1177.82 --> 1178.38]  where I said,
[1178.56 --> 1181.10]  I want to have a React cluster on Rackspace
[1181.10 --> 1182.66]  that has this many nodes in it.
[1183.08 --> 1184.12]  And you could just see it say,
[1184.24 --> 1185.48]  okay, this node is coming up.
[1185.54 --> 1186.72]  All right, it has joined the cluster.
[1186.90 --> 1187.70]  This node is coming up.
[1187.74 --> 1188.40]  It has joined the cluster.
[1188.48 --> 1189.16]  And then it would say,
[1189.44 --> 1191.54]  all right, here's the list of IPs in your ring,
[1191.66 --> 1193.20]  and then you could just connect to any of them
[1193.20 --> 1194.48]  and push and pull data
[1194.48 --> 1195.56]  and, like, that sort of thing.
[1195.72 --> 1197.46]  So I think it's very exciting,
[1197.60 --> 1198.20]  but unfortunately,
[1198.20 --> 1200.96]  I keep searching for what the use case is
[1200.96 --> 1202.40]  that's going to be really compelling for me
[1202.40 --> 1204.46]  and then end up getting bogged down
[1204.46 --> 1206.04]  in all of the particulars.
[1206.34 --> 1207.28]  And I don't know.
[1207.30 --> 1208.94]  I still have this problem
[1208.94 --> 1211.00]  similar to what ended up being fogged
[1211.00 --> 1212.34]  to everyone else's benefit
[1212.34 --> 1213.34]  and perhaps mine.
[1213.46 --> 1214.42]  Sometimes I'm not even sure.
[1214.92 --> 1217.10]  Of starting to work on a problem
[1217.10 --> 1218.98]  and ending up in these huge rabbit holes
[1218.98 --> 1221.94]  of basically kind of what Yehud is saying.
[1222.06 --> 1223.12]  Like, I end up working on, like,
[1223.38 --> 1225.36]  a framework related to the problem
[1225.36 --> 1228.36]  that I was actually trying to solve
[1228.36 --> 1229.16]  in the first place
[1229.16 --> 1230.82]  and maybe never actually get around
[1230.82 --> 1231.56]  to solving the problem.
[1233.18 --> 1234.16]  It's nice, I guess,
[1234.18 --> 1235.68]  when you can have the luxury of doing that
[1235.68 --> 1239.54]  or when the rabbit hole is interesting enough
[1239.54 --> 1240.76]  that you can get that lost in it.
[1241.70 --> 1243.50]  Incredible lineup here at Red Dirt RubyConf
[1243.50 --> 1244.74]  in Oklahoma City.
[1245.38 --> 1246.90]  Of all that you've seen today,
[1247.02 --> 1248.20]  what's got you the most excited
[1248.20 --> 1249.08]  that you want to go play with?
[1250.72 --> 1252.26]  It's a tricky question.
[1252.68 --> 1254.68]  I mean, like, the deck was kind of loaded for me,
[1254.72 --> 1255.76]  I guess, because of some of the stuff
[1255.76 --> 1256.62]  that I've already been looking at.
[1256.70 --> 1258.40]  Like, the cloud question for me,
[1258.68 --> 1260.16]  I don't have an answer right now,
[1260.24 --> 1261.60]  but I've been exploring a lot
[1261.60 --> 1264.64]  to look at, well, beyond just React,
[1264.78 --> 1268.48]  doing some stuff with Backbone and Backbone.js
[1268.48 --> 1271.72]  and maybe driving that with CoffeeScript
[1271.72 --> 1272.52]  instead of JavaScript.
[1272.72 --> 1273.82]  And, like, there's a lot of stuff like that
[1273.82 --> 1275.84]  where I don't know that I've really
[1275.84 --> 1278.28]  pinned down exactly what I'm going to do with it,
[1278.54 --> 1280.04]  but I've been doing, like,
[1280.24 --> 1282.06]  low-level back-end stuff for so long
[1282.06 --> 1283.50]  that I just want to do something
[1283.50 --> 1286.74]  to, like, make sure that I still have my chops, right?
[1286.80 --> 1288.22]  Like, I used to do a lot of web stuff
[1288.22 --> 1291.06]  and I just haven't for six or seven or eight months
[1291.06 --> 1294.02]  because I've been so deeply, you know,
[1294.04 --> 1294.88]  doing the fog thing
[1294.88 --> 1297.62]  that I just need to get back on the horse, I think, so.
[1298.12 --> 1299.28]  Well, thanks for joining us.
[1299.32 --> 1300.28]  We surely appreciate it.
[1300.34 --> 1301.40]  And if you use the fog, Jim,
[1301.44 --> 1302.70]  be sure and buy this guy a beer.
[1302.94 --> 1303.22]  Thanks.
[1303.42 --> 1304.02]  Yeah, thank you.
[1304.02 --> 1304.06]  Thank you.
[1321.06 --> 1334.02]  Lebens приготов couch measures from his channel.
[1334.16 --> 1335.82]  Welcome back to S computer.
[1336.02 --> 1336.06] .
