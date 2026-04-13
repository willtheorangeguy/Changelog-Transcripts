[0.00 --> 19.06]  Welcome to The Change Log, episode 0.1.9.
[19.22 --> 20.42]  I'm Adam Stachowiak.
[20.56 --> 21.46]  And I am Wyn Netherland.
[21.64 --> 22.60]  This is The Change Log.
[22.66 --> 24.76]  We cover what's fresh and new in the world of open source.
[25.30 --> 28.44]  If you found us on iTunes, check us out on the web at thechangelog.com.
[28.44 --> 31.70]  Or for a real-time view, check out tail.thechangelog.com.
[31.90 --> 35.00]  You can also swing over to github.com forward slash explore.
[35.10 --> 39.12]  You'll find some training repos, some feature repos from our blog and all of our audio podcasts.
[39.66 --> 44.84]  And if you're on Twitter, the Twitter, you should be following Change Log Show, not The Change Log.
[44.98 --> 46.16]  And I am Adam Stach.
[46.28 --> 49.04]  And I am Penguin, P-E-N-G-W-Y-N-N.
[49.46 --> 53.02]  So cool this week, got to catch up with one of my heroes, James Edward Gray II.
[53.66 --> 54.86]  Big name in the roomie community.
[54.86 --> 56.62]  Author of a number of gems.
[57.58 --> 59.68]  Maintainer of the rubyquiz.com.
[60.38 --> 62.76]  That's at www.rubyquiz.com.
[63.08 --> 67.56]  Also putting together a cool conference in May that we'll be at called Red Dirt RubyConf.
[68.12 --> 73.74]  We were up in Oklahoma City at another event, Open Beta 4, where Adam and I got to participate.
[74.04 --> 74.84]  Yeah, I got to judge.
[74.92 --> 75.54]  You got the keynote.
[75.80 --> 76.62]  It was pretty awesome.
[76.72 --> 78.50]  And we also did some demonstrations, too.
[78.50 --> 83.96]  What a cool venue up there in Oklahoma City with the OKC Coco run by Derek Parkhurst.
[84.28 --> 88.04]  Cool co-working space up there and just a really cool venue.
[88.48 --> 91.68]  Yeah, got a big thanks to Derek for bringing us up.
[91.72 --> 92.30]  It was a blast.
[92.74 --> 94.48]  And I couldn't thank you enough for having us there.
[94.90 --> 95.12]  I know.
[95.16 --> 96.56]  It's got me excited about going back to Red Dirt.
[96.78 --> 97.00]  Yeah.
[97.98 --> 101.62]  A lot of big names coming in for Red Dirt RubyConf, so be sure and add that one to your calendar.
[102.24 --> 105.20]  By design, this interview is a bit short, as is the intro.
[105.20 --> 110.50]  So those of you that's been giving us the good feedback on the survey, we surely appreciate it.
[110.54 --> 111.28]  And this one's for you.
[111.62 --> 111.92]  All right.
[111.94 --> 112.66]  Let's get to it, then.
[121.56 --> 122.08]  All right.
[122.12 --> 125.18]  Adam and I are joined today by James Gray in Oklahoma City.
[125.28 --> 129.54]  We're up for the Open Beta event in Oklahoma City at OKC Coco.
[130.06 --> 134.94]  So, James, why don't you tell the listeners a little bit about yourself, who you are, and why they should care?
[135.20 --> 139.10]  So, I'm James Gray on the internet.
[139.30 --> 145.88]  I go by my full name, which is James Edward Gray II, because if I don't, then my eye doctor gives me the wrong glasses.
[148.38 --> 154.20]  I've been in the Ruby community for a long, long time, longer than Rails has been released.
[154.82 --> 164.10]  I was actually playing with Ruby before Rails was released, and then when Rails came out, I suddenly had a skill that was in demand, which is funny, because I was just doing it for fun.
[164.10 --> 169.74]  And I've been involved in lots of different parts of Ruby.
[169.96 --> 174.06]  I think I started by writing documentation for certain libraries.
[174.40 --> 180.36]  I documented ERB and P-Store and a few of the standard Ruby libraries.
[180.36 --> 184.68]  And then I released some libraries eventually.
[185.58 --> 191.90]  Probably the one everybody knows is FasterCSV, which eventually became the standard CSV library in Ruby 1.9.
[192.46 --> 202.96]  And then, geez, I've stayed and done everything in the community and helped maintain the Ruby web page and just about everything.
[202.96 --> 208.24]  Where do you see Ruby headed with Ruby 1.9 as far as adoption?
[208.48 --> 213.74]  When do you think we'll be over the hump, as it were, with gem adoption on 1.9?
[214.32 --> 218.66]  Well, this summer I went to Japan to attend Ruby Kaigi.
[219.20 --> 226.78]  And that was their big focus was they're trying to figure out how to get everybody on to Ruby 1.9 so they can move forward.
[227.10 --> 228.96]  And that's definitely their main goal.
[228.96 --> 240.58]  I think the Ruby 1.9.2 release is where they're really trying to make sure they've addressed all the lingering concerns so that they can get public adoption.
[242.18 --> 248.56]  They got everything passing on the Ruby spec, which is really great.
[248.66 --> 252.64]  They held the release just to get everything up to date with Ruby spec.
[252.64 --> 258.64]  And they're really pushing hard to get those things done.
[258.64 --> 263.60]  And I think Rails 3 is going to help with that a lot, being more friendly on Ruby 1.9 and stuff.
[263.74 --> 267.36]  So I think we're just finally starting to get over the hump.
[267.38 --> 270.12]  And I think we'll start to see some Ruby 1.9 adoption soon.
[272.62 --> 276.86]  You're also known for your TextMate bundle, the TextMate book.
[277.26 --> 278.50]  You're on the TextMate team.
[278.50 --> 282.72]  Speak a little bit about what TextMate means to you as a developer.
[282.72 --> 286.16]  I really love the TextMate team.
[286.16 --> 294.72]  And this is mostly just I started hanging out in that IRC channel a long time ago when I found TextMate.
[295.32 --> 297.86]  And I've been there ever since.
[298.10 --> 300.20]  And they're just a really great bunch of guys.
[300.28 --> 303.32]  I can't believe how much they know about everything.
[303.32 --> 312.28]  And it's my favorite place to just hang out and pick up crazy cool geek tips and all kinds of wild stuff.
[313.90 --> 321.30]  That's where I learn about things like Git or just all kinds of random topics working with the TextMate team.
[321.86 --> 327.66]  And I built a bundle just to make my life easier when I was programming Ruby with TextMate.
[327.66 --> 332.68]  And I released it for a while just on my blog.
[332.80 --> 334.40]  And people downloaded it from there.
[334.66 --> 337.38]  And then eventually Alan approached me and said,
[337.52 --> 342.76]  let's just take this and make it the Ruby bundle and replace what we have.
[343.02 --> 345.74]  And I've maintained that part ever since.
[345.88 --> 350.70]  And then after I wrote the Best of Ruby quiz for the pragmatic programmers,
[350.94 --> 353.76]  they were asking me, what other things are you interested in?
[353.82 --> 355.04]  What would you like to talk about?
[355.04 --> 358.48]  And I said, well, I'm pretty into TextMate and stuff.
[358.70 --> 360.16]  I'd love to write a book about that.
[360.32 --> 361.48]  And so they said, let's do it.
[361.54 --> 362.12]  So we did.
[362.38 --> 365.24]  And that's how I've been involved in the TextMate.
[365.34 --> 366.52]  It's an awesome, awesome book.
[366.60 --> 371.32]  And if you're in TextMate regularly, I highly recommend that you check it out.
[371.96 --> 376.40]  So I guess when you started the bundle, you were maintaining that in Subversion?
[377.34 --> 378.14]  Yeah, that's right.
[378.24 --> 378.88]  Yeah, way back.
[379.40 --> 384.02]  Actually, TextMate until very recently was still Subversion managed.
[384.02 --> 386.40]  And we've wanted to go to Git for a long time.
[386.90 --> 392.86]  But there are actually a couple of things in Git that don't mesh super well with how we do some things in TextMate.
[393.42 --> 397.32]  So we had some stumbling blocks there that kind of held us back for a little while.
[397.42 --> 399.70]  But we had wanted to do it for a long time.
[399.76 --> 402.42]  And now we are, most of the bundles are now hosted on GitHub.
[402.42 --> 407.54]  Can you mention any resources for maybe a bundle developer for TextMate?
[407.64 --> 409.58]  Just any good resources besides, say, the wiki?
[410.64 --> 412.58]  Yeah, if you're building bundles.
[414.50 --> 419.06]  So in my book, I do actually go through and show how to build a bundle.
[419.06 --> 424.50]  In fact, I literally built one that didn't exist when I was writing the book.
[424.58 --> 427.30]  And now that's one of the bundles we ship with TextMate.
[427.58 --> 431.50]  So I definitely tried to put everything I knew about it then.
[431.92 --> 439.72]  And I talked to all the members of the team back then to say, you know, what's the best practices for doing variables?
[439.86 --> 441.90]  And that was how I showed off variables and stuff.
[441.90 --> 445.80]  So that is one of the most complete sections of documentation.
[446.02 --> 451.94]  But you mentioned the wiki, and it does have a lot of information, including, like, some best practices and stuff that we try to follow.
[452.10 --> 454.08]  So that's a pretty good place.
[454.42 --> 458.48]  The other thing I would tell you if you're doing anything with TextMate is go to the IRC channel.
[459.04 --> 463.64]  There are people always there involved, and they're very helpful.
[464.34 --> 465.16]  They'll tell you things.
[465.26 --> 466.30]  They'll work with you on code.
[466.40 --> 467.24]  You can post stuff.
[467.30 --> 468.04]  They'll give you feedback.
[468.36 --> 470.06]  And it's hard to beat that.
[470.06 --> 480.20]  Yeah, I actually – I'm not much of a developer, but I do some maintaining of the SAS bundle as well as the Hamill bundle for TextMate.
[480.74 --> 488.28]  And one thing I found myself wanting to do was go into, like, actual TextMate and write some code versus use, like, that GUI bundle editor.
[488.92 --> 490.48]  Is that a normal thing?
[491.00 --> 493.04]  Absolutely, and you can certainly do it.
[494.40 --> 496.20]  You can open the bundles.
[496.20 --> 505.68]  So TextMate just stores, you know, files on the disk in XML, so you can definitely edit those for some things.
[505.82 --> 518.02]  But if you're talking about, like, writing bundle code and stuff, when you install TextMate, if you go into the – I think it's the bundles menu, and you go down to, like, TextMate or something, there's a install edit in TextMate.
[518.14 --> 520.24]  There's a command called edit in TextMate.
[520.24 --> 526.00]  And if you get it to install that, it'll put a thing in your edit menu, a choice called edit in TextMate.
[526.20 --> 531.42]  And so, like, if you're writing a mail in mail, then you can go to edit in TextMate and pick that.
[531.76 --> 535.68]  One of the great unknown secrets is it works in TextMate's bundle editor.
[535.92 --> 540.98]  So you can open the bundle editor, go edit in TextMate, and it'll pop it into the TextMate.
[541.06 --> 543.82]  You edit and save, close, and it goes back to bundle editor.
[543.98 --> 544.70]  Very nice.
[544.76 --> 545.84]  You mentioned the IRC channel.
[545.90 --> 546.96]  Is that just hash TextMate?
[546.96 --> 550.38]  Actually, it's hash, hash TextMate.
[550.76 --> 559.50]  It's an old IRC rule because it's not – yeah, I'm not 100% sure on that.
[559.56 --> 560.82]  We'd have to look it up in free node.
[560.82 --> 565.96]  But it's a policy due to, oh, TextMate's not free software.
[566.20 --> 566.88]  That's what it is.
[567.12 --> 574.68]  It's because TextMate is only – I mean, the bundles are all open source and stuff, but the program itself is closed source.
[574.68 --> 577.80]  And because of that, it has to have two pounds in front of it.
[577.94 --> 581.20]  We've gotten away with the single hash on the change log on IRC channel.
[581.26 --> 582.82]  I'm not sure if we qualify or not.
[583.50 --> 586.94]  Any inside information on where we might see TextMate 2.0?
[587.56 --> 588.72]  Everybody asks me that.
[588.78 --> 589.30]  I don't know.
[590.26 --> 593.14]  I know they're working really hard on it.
[594.08 --> 598.84]  You know, it's Alan and Searing Lash, I think is his name.
[599.06 --> 601.62]  But they're working very hard on it.
[601.66 --> 602.96]  They're making a lot of great progress.
[602.96 --> 604.46]  I think it's going to be amazing.
[604.82 --> 606.04]  So I hope soon.
[606.50 --> 610.16]  We're getting dangerously close to Duke Nukem forever territory here.
[610.62 --> 613.04]  It's been made before, definitely, the comparison.
[614.24 --> 616.30]  So let's go back to Ruby for a moment.
[617.10 --> 619.02]  Faster CSV is one of your gems.
[619.36 --> 620.62]  So what's the breakdown?
[620.80 --> 625.76]  How much do you spend writing Ruby applications and how much of it's web applications using Ruby?
[626.72 --> 628.16]  Well, that is my day job.
[628.16 --> 634.28]  So I work all day, every day, building applications with Rails, mostly.
[635.22 --> 636.02]  Some with Sinatra.
[637.22 --> 638.78]  But I looked recently.
[639.16 --> 640.60]  I actually sat down and counted.
[641.16 --> 645.40]  And I've actually worked on over 30 shipping Rails applications now.
[645.58 --> 648.76]  So that's definitely what I spend most of my time doing.
[649.90 --> 651.56]  Like I say, we do have some Sinatra.
[651.56 --> 656.12]  But I'm kind of one of the people at work, they just give weird projects to.
[656.26 --> 661.60]  So there will be entire weeks when I don't write any web application code.
[661.64 --> 666.38]  Instead, I'm writing some crazy system that runs on one of our servers or whatever.
[666.66 --> 669.10]  So I love that about my job.
[669.18 --> 670.98]  I get to do different things all the time.
[671.12 --> 674.40]  And even if I'm doing something boring, I don't worry about it.
[674.40 --> 677.00]  Because I know next week I'll be doing something totally different.
[678.00 --> 680.16]  What excites you the most about Rails 3?
[681.08 --> 681.94]  About Rails 3?
[682.06 --> 682.92]  Wow, that's a good question.
[684.00 --> 686.10]  There's a lot of exciting stuff in Rails 3.
[686.28 --> 693.32]  I think I'm really excited about how much they've embraced Rack and gone down that road.
[693.32 --> 704.56]  And so now we can use just that awesome ecosystem of tools and how you can just take a Sinatra application and shove it in there and route straight to it or things like that.
[704.72 --> 710.22]  I also think the new query engine they've put in there is really cool for ActiveRecord.
[710.40 --> 714.30]  So I think those are probably two of the things that have me pretty excited about it.
[714.60 --> 716.50]  I've actually tried to play with it a little bit.
[716.60 --> 717.66]  But I was a little early.
[718.34 --> 722.82]  And there were quite a few pain points when I pulled it down and started messing with it.
[722.82 --> 724.52]  So it wasn't as much fun.
[724.66 --> 726.58]  But I know they're trying to work those out.
[727.44 --> 730.64]  So sometime in the future we plan to have Yehuda on the podcast to talk about Rails 3.
[730.80 --> 733.44]  But let's just forecast he's going to be on soon.
[734.02 --> 736.50]  If there's any questions you have for Yehuda, what would it be?
[738.92 --> 740.20]  Maybe jQuery questions.
[740.72 --> 741.46]  Maybe jQuery.
[742.18 --> 743.06]  I love jQuery.
[743.30 --> 744.40]  I use that all the time.
[744.74 --> 748.14]  I see Yehuda pretty often at the conferences and stuff.
[748.20 --> 749.24]  And we chat quite a bit.
[749.24 --> 751.84]  So I think I'm kind of up on things.
[751.84 --> 754.74]  But that's a good question.
[755.60 --> 761.18]  We had a really good talk at Lone Star about modules and how modules worked in Ruby.
[761.66 --> 767.90]  I gave that talk at Lone Star last year about modules and basically explaining Ruby's method lookup system.
[767.90 --> 774.82]  And he said that he came up to me after that talk and he said basically I had just described the Rails 3 development process.
[775.04 --> 777.78]  That that's what they had figured out how all that worked.
[777.84 --> 785.14]  And now they were going back through and removing things like alias method change so they could switch and just use Ruby's natural method lookup system.
[785.14 --> 791.40]  Which I thought was really cool that they've done, you know, really embrace more Ruby with Rails 3.
[791.56 --> 792.40]  And I thought that was neat.
[792.86 --> 797.96]  And when you say Lone Star, of course you're talking about our awesome Texas Ruby Conference, Lone Star Ruby Conf.
[798.06 --> 802.86]  In August of every year, no better time to visit Austin than 105 degree heat, right?
[802.86 --> 808.50]  But you're launching your own conference up in Oklahoma City, Red Dirt Ruby Conf.
[808.60 --> 809.68]  Talk a little bit about that.
[810.12 --> 810.54]  That's right.
[811.12 --> 814.32]  So, yeah, we're building a Ruby Conference.
[814.54 --> 817.78]  This year turned out to be kind of a low conference year for me.
[817.86 --> 820.48]  I did a bunch last year, including Japan.
[820.86 --> 823.36]  And this year I couldn't do as many.
[823.58 --> 827.46]  My wife's having a baby and we didn't want to travel as much.
[827.46 --> 834.38]  So we were hanging out here and I said, well, you know, if I can't go to a Ruby Conference, I guess I'll just have to build one.
[834.74 --> 841.40]  And so we got together with a bunch of crazy guys that help run the Coco here, Derek Parkhurst.
[841.58 --> 849.86]  And then Grant Schofield is a regular of our community and one of the founding members of OKRB, our local Ruby users group.
[850.38 --> 852.90]  And then Dana has been helping me too with the conference.
[852.90 --> 862.62]  So we all just kind of threw in together and said, let's try to build a Ruby Conference and let's build the conference we've always wanted to attend.
[863.02 --> 864.96]  And that's exactly what we sat down and did.
[865.08 --> 865.76]  Single track?
[866.28 --> 867.30]  Single track, yes.
[867.42 --> 867.90]  One track.
[868.06 --> 873.00]  We thought long and hard about that, but we feel like the talks are always better on the single track.
[873.10 --> 881.16]  So we were like, let's do a single track, one day event, but let's figure out how we can maximize the amount of material that we could cram into it.
[881.16 --> 882.70]  So we totally redesigned the program.
[882.90 --> 885.16]  Single track, but multiple areas of focus.
[885.26 --> 886.64]  And I know SQL is big this year.
[886.72 --> 892.36]  Talk a little bit about how you went into that decision process and some of the talks that you're looking forward to.
[893.34 --> 903.16]  So it came down to, like I said, we wanted to figure out how could we maximize the amount of content we could get in one day with a single track conference.
[903.16 --> 915.64]  And so we decided, well, if we could put it in sessions, if we could divide it up into topics and we could have people talk on topics, then we could have introductory speeches for those sections.
[915.64 --> 922.16]  But then we could have shorter focus talks that just did one simple slice of that section.
[922.16 --> 930.38]  And then also the Q&A, which actually turns out to be a pretty big time sink, we could put that at the end with a panel of speakers.
[930.68 --> 935.52]  So it basically removes that burden from the speakers in planning their speeches and stuff.
[935.92 --> 939.16]  And that way we can, you know, maximize our usage of the time.
[939.16 --> 942.68]  And so we pre-selected topics that were interesting to us.
[943.06 --> 945.22]  And I was on the team.
[945.42 --> 947.68]  So NoSQL was interesting to me.
[947.76 --> 948.58]  And it made the cut.
[949.04 --> 954.36]  And actually, it was pretty funny because I fought pretty hard for it to get it on there because, you know, it's not really a Ruby thing.
[954.90 --> 957.38]  And I wanted to have NoSQL in the conference.
[957.38 --> 959.08]  And I thought it was important.
[959.32 --> 961.68]  And I really tried to make that happen.
[961.68 --> 968.20]  And then, like, a week after we had planned that, LA RubyConf, I think, announced their lineup.
[968.90 --> 974.02]  And one of the reasons we had done NoSQL is we had seen it in so many places and it was really big.
[974.62 --> 979.28]  And then LA RubyConf announced their lineup and there was no NoSQL in the program.
[979.72 --> 982.82]  So all the other organizers were looking at me like, yeah, that's really big, James.
[982.88 --> 983.74]  Good job, you know.
[984.06 --> 987.62]  But I think we've had a lot of interest in it.
[987.62 --> 990.40]  And so I think I'm vindicated now.
[991.68 --> 995.18]  Not long ago, you wrote a series of articles on Redis.
[995.68 --> 997.42]  And that's a data store, right?
[997.64 --> 998.04]  That's it.
[999.30 --> 1002.36]  I'm the lack of technical guy on the side of the podcast.
[1002.48 --> 1004.96]  But I actually delved into a couple of your articles.
[1005.06 --> 1006.74]  And I like your writing style and your blog.
[1006.90 --> 1011.74]  But what turned you on about NoSQL and this type of data stores?
[1013.14 --> 1017.84]  To me, NoSQL is, like, one of the super exciting things to me in our world right now.
[1017.84 --> 1024.22]  Not so much just because of, I mean, well, we get great new toys to play with and what Geek doesn't like that.
[1024.44 --> 1031.74]  But also because it's kind of encouraging us to take a step back and just look at data a different way.
[1031.90 --> 1036.92]  You know, we've gotten so used to just, oh, cram it all in a MySQL database and it'll sort itself out.
[1036.92 --> 1048.26]  But this is like, you know, this particular solution isn't as cool as a MySQL database, but it totally destroys it for this one use case, you know, or whatever.
[1048.48 --> 1055.46]  And it kind of gets us to take a step back and think about the data we have and how we need to look at it and stuff.
[1055.58 --> 1057.60]  And I think that's exciting and cool.
[1057.60 --> 1062.08]  But I'm mostly a back-end programmer, so I enjoy that kind of stuff a lot.
[1062.40 --> 1067.40]  But, yeah, so I really like how it encourages us to try new things.
[1067.52 --> 1070.96]  And Redis is a great example because it has, like, sets.
[1071.06 --> 1075.76]  It's basically memcache on steroids with sets and lists and things like that.
[1075.84 --> 1083.88]  So you can do all the great things you can do with memcache and then more because you can do these kind of pseudo-queries using set intersection and stuff like that.
[1083.88 --> 1095.94]  Yeah, I'd love to see the panel that we had from last episode, the 018th of SmackDown, expanded to include other data stores like Redis and someone that can actually speak to Mongo a little better than me.
[1096.08 --> 1103.30]  And maybe we can put that together at RedDirt to talk about some of those other, I guess, platforms other than just the three.
[1103.86 --> 1104.14]  SmackDown 2.
[1104.14 --> 1106.14]  Yeah, NoSQL SmackDown 2, that's right.
[1107.22 --> 1112.66]  But switching gears for a moment to talk, I guess, more about the personal side of your development.
[1112.66 --> 1118.98]  You, outside of this conference, also run OK.RB, which is the local Oklahoma Ruby group, right?
[1118.98 --> 1119.48]  Right, yep.
[1119.48 --> 1125.88]  So how did that come about and what words of advice would you have for other folks that may be wanting to start a Ruby group in their area?
[1126.74 --> 1131.32]  Well, OKRB was formed in the most logical place, which was New York City.
[1132.44 --> 1135.80]  So actually it was totally hilarious.
[1135.80 --> 1148.62]  I'd been thinking about putting a Ruby group together in Oklahoma for a while, and I talked to a few of my buddies about doing it, including Greg Brown, who does the Prawn Jam and various other projects.
[1148.94 --> 1151.70]  But I talked to him about it.
[1151.84 --> 1156.90]  And then Grant Schofield is another local, and he had also thought about doing a Ruby group.
[1156.90 --> 1166.86]  So he went to New York for some business thing, I think, and he decided to drop in on a New York Ruby group meeting where he met Greg Brown.
[1167.50 --> 1168.80]  And so they were sitting around talking.
[1168.94 --> 1172.60]  He's like, yeah, I've been thinking of putting one together in Oklahoma.
[1172.98 --> 1175.20]  And Greg's all, you've got to talk to James.
[1175.26 --> 1176.52]  He's been thinking about that.
[1176.74 --> 1180.64]  And so Greg put the two of us in touch, and that's how OKRB got formed.
[1181.02 --> 1181.52]  That's awesome.
[1181.62 --> 1181.96]  That's awesome.
[1181.96 --> 1184.28]  You guys meet here at the OKC Coco, right?
[1184.64 --> 1185.00]  Right.
[1185.08 --> 1187.46]  Actually, we just moved here, our last meeting.
[1187.76 --> 1196.08]  We were always meeting up in Edmond because that's where I live, and I got plenty of flack for the 20-minute drive the OKC people have to make all the time.
[1196.62 --> 1200.02]  So now I'm the guy that makes the 20-minute drive to come down here to OKC.
[1200.02 --> 1202.52]  But it really has been wonderful.
[1203.28 --> 1205.36]  You know, Coco is kind of our geek headquarters.
[1205.96 --> 1210.90]  And just being here in the very first meeting, our membership basically tripled.
[1210.90 --> 1212.20]  So that was great.
[1212.36 --> 1213.02]  It's an awesome venue.
[1213.20 --> 1215.06]  I'm impressed with the setup here.
[1215.16 --> 1216.68]  I can't wait for the event this evening.
[1217.22 --> 1219.68]  Another question from a personal standpoint.
[1219.86 --> 1223.68]  So at lunch, we have a great burger at Irma's.
[1223.90 --> 1224.44]  Cool place.
[1224.52 --> 1225.34]  They're on Twitter, by the way.
[1225.42 --> 1229.18]  We need to post a photo of the sign we took in the window.
[1229.36 --> 1233.90]  But you made the comment that you can't believe that you actually get paid to do what you're truly passionate about.
[1233.90 --> 1239.90]  And I think we're probably big on the campuses based on people that follow us on Twitter and add us.
[1239.96 --> 1242.02]  It makes me feel old that these guys are still in school.
[1242.12 --> 1249.86]  But what words of advice would you have for the guy on campus or the gal on campus that is, you know, slinging code and is looking at Ruby?
[1250.02 --> 1252.32]  Or what other language as far as following your passions?
[1252.32 --> 1256.40]  I would say totally do it no matter what.
[1256.62 --> 1258.08]  Just do what you're passionate about.
[1258.28 --> 1260.06]  And it just sorts itself out.
[1260.16 --> 1269.04]  Like I said, I was playing with Ruby as a side project and just for fun because I enjoyed it and I thought the language was so cool.
[1269.04 --> 1274.02]  And what was really great about Ruby back then is there was nobody in the language.
[1274.62 --> 1285.08]  So literally we all talked on this one mailing list and I traded emails with people like Dave Thomas and Jim Wyrick every day, you know, and that was just amazing to me.
[1285.52 --> 1287.04]  And I was all doing it for fun.
[1287.56 --> 1298.10]  And then Rails was released and suddenly everybody needed Rails developers immediately, which I knew nothing about Rails, but I knew Ruby, you know, so same thing, you know, close enough.
[1299.06 --> 1308.72]  And so suddenly I had a skill that was immensely valuable and I quit my job and came to work building Rails apps and I've done that ever since.
[1309.08 --> 1313.12]  So, yeah, they literally pay me to play with my favorite toy all day long.
[1313.22 --> 1313.86]  That's awesome.
[1314.52 --> 1317.94]  Well, if you can, make it out to Oklahoma City to catch Red Dirt RubyConf.
[1318.00 --> 1318.82]  It's going to be a good one.
[1318.98 --> 1322.60]  And if you've never seen James speak, it's something to behold.
[1322.60 --> 1329.40]  I remember Adam and I on the drive up were talking about the Heroes talk a couple years ago at Red Dirt and then the Battlestar Galactica.
[1330.00 --> 1330.94]  That's what I say.
[1331.04 --> 1331.42]  Red Dirt.
[1331.52 --> 1332.58]  Sorry, at Lone Star.
[1333.48 --> 1335.84]  And then Battlestar Galactica the next year.
[1335.92 --> 1337.54]  And then last year it was your vacation photos.
[1337.80 --> 1340.66]  So I'm trying to see how you topped the photos of Japan.
[1340.84 --> 1342.44]  Any idea for your talk this year?
[1342.48 --> 1343.00]  You got it in your head?
[1343.00 --> 1346.24]  No, I'm actually not going to give a speech.
[1346.50 --> 1347.18]  No way!
[1347.58 --> 1349.96]  On the conference itself.
[1350.12 --> 1353.94]  But I am going to do a three-hour training the next day.
[1354.06 --> 1356.84]  So with Glenn Vanderberg, who's like another one of my heroes.
[1357.12 --> 1359.16]  So that's the awesome thing about Red Dirt.
[1359.28 --> 1362.18]  They told me, go get everybody you would want to hang out with.
[1362.26 --> 1365.28]  And so I went to all my heroes and they all said yes, which is too cool.
[1365.36 --> 1366.28]  That's why they're my heroes.
[1366.58 --> 1366.98]  That's awesome.
[1367.84 --> 1370.26]  So Glenn and I will do a training the second day.
[1370.34 --> 1371.86]  So I'll try to be entertaining.
[1371.86 --> 1372.48]  What's the topic?
[1373.00 --> 1376.46]  The topic is the Ruby your mother warned you about.
[1377.08 --> 1381.86]  We're going to look at bad Ruby and ways to make it better and what we can learn from that.
[1382.54 --> 1389.26]  So every time we have someone on the podcast, we always want to ask them what's cool in the open source world that you're into.
[1389.40 --> 1390.10]  So what's on your radar?
[1390.22 --> 1391.66]  What's something that you're just dying to play with?
[1392.46 --> 1393.84]  That I'm dying to play with?
[1394.18 --> 1395.28]  TextMate 2.0.
[1395.40 --> 1396.98]  I'm definitely dying to play with that.
[1397.12 --> 1397.88]  Well, that's not the source.
[1398.52 --> 1399.22]  Oh, yeah.
[1399.32 --> 1399.82]  You're right.
[1399.90 --> 1400.18]  Sorry.
[1400.18 --> 1404.32]  I spend all my time writing on the bundles of TextMate, which are open source.
[1404.94 --> 1405.64]  But you're right.
[1405.68 --> 1407.40]  The application itself is not a good point.
[1407.40 --> 1413.46]  But my favorite thing to play with has definitely lately been NoSQL databases.
[1413.46 --> 1421.44]  I love Redis, Tokyo Cabinet especially, which I've been building a mixer for that wrapper library.
[1421.44 --> 1424.64]  So I love just the NoSQL databases.
[1424.76 --> 1426.18]  That's my favorite thing to play with lately.
[1426.72 --> 1427.68]  We've got to keep the streak alive.
[1427.76 --> 1428.72]  What about Node.js?
[1429.24 --> 1429.80]  Node.js?
[1430.08 --> 1431.52]  I knew you were going to ask that.
[1432.00 --> 1435.90]  And I'm like one of the few people in the world that hasn't played with Node.js yet.
[1435.98 --> 1437.32]  So I feel really ashamed.
[1437.56 --> 1441.26]  And I'm going to go now and go play with Node.js so that I feel better.
[1442.68 --> 1443.10]  Great.
[1443.18 --> 1443.94]  Well, thanks for your time.
[1444.02 --> 1448.10]  I can't wait to the event tonight and then also the conference coming up in May.
[1448.38 --> 1449.16]  Thanks for having me.
[1449.16 --> 1458.20]  Thank you for listening to this edition of The Change Log.
[1459.26 --> 1465.98]  Point your browser to tail.thechangelog.com to find out what's going on right now in open source.
[1467.18 --> 1475.72]  Also be sure to head to github.com forward slash explore to catch up on trending and feature repos as well as the latest episodes of The Change Log.
[1479.16 --> 1509.14]  The Change Log.
[1509.16 --> 1510.94]  The Change Log.
[1510.94 --> 1513.30]  Bring it back
