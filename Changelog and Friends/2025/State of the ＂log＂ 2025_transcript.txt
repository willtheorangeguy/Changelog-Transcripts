[0.00 --> 18.18]  Oh yes, it's late December once again.
[18.68 --> 25.34]  That classic changelog theme song is bumpin' and it's time for our 8th annual State of
[25.34 --> 26.18]  the Log episode.
[26.40 --> 29.76]  If this is your first time with us, welcome to the changelog.
[30.00 --> 35.64]  The software world's best weekly news brief, deep technical interviews, and weekend talk
[35.64 --> 39.18]  show that feels like you're hanging out with your friends in the hallway track of your
[39.18 --> 40.68]  favorite conference on repeat.
[41.06 --> 47.80]  Big thanks to our partners at fly.io for helping us bring you awesome developer pods all year
[47.80 --> 48.24]  long.
[48.66 --> 52.76]  You know we love Fly, the public cloud built for developers who ship.
[53.20 --> 55.80]  Give it a try at fly.io.
[55.80 --> 58.68]  All right, State of the Log 2025.
[59.34 --> 60.16]  Let's do it.
[60.16 --> 67.48]  Well friends, I'm here with a good friend of mine.
[67.80 --> 72.42]  Again, Kyle Galbraith, co-founder and CEO of depot.dev.
[72.80 --> 76.16]  Kyle, we are in an era of disruption, right?
[76.30 --> 79.68]  I would also describe it as rethinking what we thought was true.
[79.88 --> 82.74]  And I guess that's kind of the definition of disruption.
[82.74 --> 88.62]  But from your perspective, how are teams, reliability teams, CISCD, pipeline teams, how are they all
[88.62 --> 89.66]  rethinking things?
[89.96 --> 92.20]  And where does depot fit into that?
[92.38 --> 97.94]  In the conversations that I have with customers, a lot of DevOps teams, platform teams, site
[97.94 --> 102.12]  reliability teams, they're really looking at this new era of software engineering that
[102.12 --> 102.92]  we're all living in.
[103.00 --> 107.92]  And they're starting to question like the bottleneck is no longer the act of writing code.
[108.16 --> 109.28]  The bottleneck is shifting.
[109.28 --> 112.26]  The most time consuming part is integrating the code.
[112.52 --> 113.72]  It's everything that comes after.
[114.18 --> 114.94]  It's the build.
[115.22 --> 116.76]  It's the pull request review.
[117.32 --> 118.20]  It's the deployment.
[118.66 --> 120.38]  It's the getting it into production.
[121.02 --> 124.76]  Once it's in productions, it's scaling up support teams to support it.
[124.82 --> 128.10]  It's adding documentation, all of these downstream problems.
[128.70 --> 132.82]  And so through the lens of depot, what we're really starting to think about is there's a very
[132.82 --> 138.30]  realistic possibility that within the next two to three years, maybe even sooner, that we're
[138.30 --> 143.46]  going to enter a world where an engineering team of three people could theoretically have the
[143.46 --> 146.30]  velocity of an engineering team of 300 people.
[146.76 --> 148.40]  And what's the consequences of that?
[148.72 --> 155.68]  What's the consequences of the code velocity spiking up to that level with such a small team?
[155.92 --> 160.64]  There's no way three engineers are going to be able to code review all of the code that's
[160.64 --> 167.04]  being created if there's three engineers and 297 agents also creating features and fixing bugs.
[167.36 --> 169.14]  So that's just like from a pull request perspective.
[169.34 --> 173.94]  But then you think about it through a build lens, too, of if your builds take 20 minutes
[173.94 --> 179.52]  with three humans and now you're going to have three humans and 297 agents also running.
[179.64 --> 184.46]  Well, like you definitely don't want your builds taking 20 minutes because now like the entire
[184.46 --> 186.38]  pinch point is the build pipeline.
[186.38 --> 192.16]  And so we're starting to think a lot about how do we eliminate the bottlenecks that come
[192.16 --> 195.74]  downstream and what can we do with Depot that streamlines that?
[196.28 --> 199.34]  So obviously, friends, we are in an era of disruption.
[199.50 --> 200.16]  Things are changing.
[200.28 --> 200.68]  You know it.
[200.74 --> 201.32]  I know it.
[201.54 --> 202.34]  That's how it is.
[202.64 --> 206.78]  And the thing with production and what Kyle's talking about here is how in the world do you
[206.78 --> 207.90]  get your builds to be faster?
[208.14 --> 213.14]  How do you get them to be more reliable, faster, more observability around those deployments?
[213.14 --> 214.02]  You need it.
[214.22 --> 214.84]  It's required.
[215.18 --> 216.56]  And Depot is there to help you.
[216.86 --> 221.78]  So a good first step is to go to depot.dev, get faster, try their trial.
[221.98 --> 222.70]  It's too easy.
[223.04 --> 225.58]  Again, depot.dev is where to go.
[226.00 --> 228.04]  It all begins at depot.dev.
[231.76 --> 236.42]  Here we are, the eighth annual state of the law.
[236.50 --> 236.98]  Can you believe?
[237.12 --> 238.64]  Eight times this has happened.
[239.42 --> 240.14]  Eight times the charm?
[241.08 --> 241.56]  Hopefully.
[241.56 --> 243.24]  Seven times was a charm.
[244.08 --> 245.90]  This eighth one is going to be a charm, too.
[246.46 --> 247.22]  Oh, my gosh.
[247.42 --> 249.60]  Don't say the word charm, Jared.
[249.82 --> 250.40]  Oh, my goodness.
[250.94 --> 252.00]  Oh, my gosh.
[252.20 --> 253.42]  Hey, you know what I'm saying, right?
[253.54 --> 254.08]  Y'all out there.
[254.58 --> 255.26]  Welcome, everyone.
[255.82 --> 257.78]  Welcome back, hopefully, or welcome for the first time.
[257.86 --> 261.08]  If this is your first time listening, this is not how it normally goes.
[261.46 --> 263.22]  It normally goes like this once a year.
[263.96 --> 265.60]  This is how it always goes eight times.
[265.96 --> 266.44]  That's right.
[266.44 --> 273.38]  And we have eight voicemails to listen to from some of our longtime listeners and some newer listeners.
[273.68 --> 274.32]  So that is cool.
[274.80 --> 276.48]  Maybe a little recap on what this is.
[276.70 --> 277.26]  What do you think?
[277.80 --> 279.08]  A little recap on what this is.
[279.16 --> 279.48]  Go ahead.
[279.54 --> 279.98]  Recap it.
[279.98 --> 283.62]  I was just thinking about that because, like, you know, you mentioned the new listener potentially.
[283.76 --> 285.38]  I was thinking, like, a tiny little recap.
[285.60 --> 287.76]  So state of the log.
[287.86 --> 288.98]  We're called the change log.
[289.10 --> 290.62]  So this is state of the log.
[291.12 --> 305.62]  And all year we work tirelessly, Jared, to log, I would say, the developer journey, you know, from the new project to the sale of a company to a new side project to an acquisition.
[305.62 --> 313.50]  So you just, you name it, the latest platform that may be out there, the newest framework in the JavaScript world, which is, like, on the daily.
[314.10 --> 317.84]  Bun acquisitions, just name specifically, you know.
[318.06 --> 327.88]  And as we talk to these humans, not just these machines, these humans in this world, we get to podcast and share and all that good stuff.
[327.94 --> 330.76]  And this is a sort of an examination of that.
[330.76 --> 336.38]  But first, we invite our listenership, those folks that are listening to the show, to submit a voicemail.
[336.58 --> 337.56]  And then we hand that voicemail.
[337.74 --> 339.12]  Am I stealing some of your thunder here?
[339.18 --> 341.14]  I know you do a good job of, like, doing this.
[341.20 --> 342.22]  Am I stealing some of this?
[342.68 --> 343.00]  No, man.
[343.14 --> 343.66]  Okay, cool.
[345.54 --> 347.88]  Brake Master Cylinder, behind the scenes, produces our music.
[348.42 --> 350.32]  I won't share the real name because he's still anonymous.
[351.52 --> 354.16]  But Brake Master Cylinder is beloved by us, produces all of our music.
[354.24 --> 354.86]  We love that.
[355.58 --> 357.88]  And, you know, Jared collects these voicemails.
[357.88 --> 361.16]  I stay out of it because I want to be surprised in this moment.
[361.30 --> 362.68]  I've listened to none of these yet.
[363.40 --> 365.40]  And so each year we do this state of the law.
[365.48 --> 366.50]  We kind of go back through.
[366.64 --> 370.40]  We invite folks to send voicemails, what they love about the show, what they don't love about the show.
[370.50 --> 373.86]  And then Brake Master makes these cool remixes, which are super cool.
[374.26 --> 378.28]  And we have fun listening to those and just kind of, like, diving in.
[378.58 --> 382.84]  And for those who may be new and don't know me, I don't like watching movie trailers.
[383.72 --> 383.84]  Okay?
[383.88 --> 385.06]  And so these are, like, movie trailers.
[385.06 --> 389.38]  These are, like, little voicemail movie trailers that I can't watch because it ruins the movie.
[389.84 --> 390.72]  And so I've heard none of these.
[390.80 --> 391.70]  This is fresh for me.
[392.36 --> 393.18]  I'll hand it back to you, Jared.
[393.24 --> 397.22]  Hopefully I did a pretty decent job of describing state of law.
[397.32 --> 397.66]  That's right.
[397.78 --> 398.60]  So this is the movie.
[399.86 --> 401.90]  And we're about to watch it together.
[402.16 --> 402.36]  Okay.
[402.36 --> 404.12]  Listen to it, as is the case.
[404.44 --> 404.58]  Yeah.
[404.70 --> 405.46]  With voicemail.
[405.56 --> 410.24]  So thank you to all of you who wrote in and to everybody who listened throughout the year.
[410.54 --> 412.64]  We put out a lot of pods, almost 150.
[413.24 --> 416.70]  If you count news, if you take news out, that's almost 100.
[416.70 --> 421.32]  As each of our three legs of our table did about 50 episodes.
[422.22 --> 423.74]  As we tend to do per year.
[423.86 --> 424.70]  And so that's a lot.
[424.84 --> 426.78]  It is tough to pick faves.
[427.02 --> 428.94]  But we've done the work.
[429.18 --> 430.32]  And our listeners have done the work.
[430.88 --> 434.28]  And let's kick off with our first voicemail.
[434.34 --> 435.72]  Now, I know what you're thinking.
[436.50 --> 438.84]  In what order do these voicemails come?
[438.94 --> 441.22]  Do we do it chronologically by reception?
[441.84 --> 442.18]  No.
[442.38 --> 445.14]  Do we do it alphabetically by last name?
[445.56 --> 445.90]  No.
[446.64 --> 448.54]  Do we do it alphabetically by first name?
[448.92 --> 449.10]  Yes.
[449.10 --> 449.74]  How do we do it?
[450.58 --> 451.74]  How do we do it?
[452.22 --> 455.44]  Alphabetically by first name, because that's the way Finder arranged them.
[455.66 --> 455.98]  Okay.
[455.98 --> 456.94]  The files came in.
[457.06 --> 458.60]  They're just, put your first name first.
[458.94 --> 464.20]  And so, I guess Andrew Patton with first name Andrew gets to go first.
[464.28 --> 466.02]  So let's listen to Andrew's voicemail.
[466.78 --> 468.14]  Hello, ChangeLog family.
[468.74 --> 472.42]  First time leaving a voicemail, which is very exciting.
[472.78 --> 474.36]  Though I've been listening for many years.
[474.36 --> 482.18]  I checked and ChangeLog takes home the gold for my most listened to podcast in 2025 at 105 hours.
[482.74 --> 483.34]  Oh my gosh.
[483.34 --> 489.28]  Which would have been 111 and a half hours at 1x because I only use Smart Speed so as not to ruin those banging beats.
[489.28 --> 495.10]  This year, I really enjoyed Friends 75 with Matt Reier.
[496.10 --> 502.56]  As a pianist, it was a joy hearing him switch from guitar to piano for that episode.
[502.98 --> 507.24]  And the weird and wonderful Matt World episode, which was episode 90, was also great.
[507.24 --> 515.60]  The entire Pipe Dream saga in the Kaizen episodes this year was very fun, including that dramatic onstage live launch.
[516.22 --> 521.30]  The ChangeLog interview 635 about Tiger Beetle was fascinating.
[521.84 --> 524.16]  ChangeLog Friends 96 with Steve Yegge.
[524.62 --> 528.40]  He's always entertaining and certainly interesting.
[528.40 --> 538.90]  The interview 664 with Adam Jacob was another really interesting and enlightening episode.
[538.90 --> 545.30]  All the ChangeLog Beats releases and everything that Breakmaster Cylinder provides.
[545.96 --> 548.44]  I really missed JS Party this year.
[548.64 --> 551.28]  I was hoping for a few more dysfunctional developer episodes.
[551.50 --> 561.92]  But I love the multiple three-way conversations between Jared, Adam, and Nick Neesey, including Friends 89, 102, and the most recent.
[561.92 --> 564.16]  They are always very funny.
[564.78 --> 569.46]  They're always very relevant to the issues of the day.
[569.88 --> 577.28]  And I find it somewhat mind-blowing when I get a peek into the habits and methods of Nick Neesey.
[577.64 --> 579.14]  Thank you all for all you do.
[579.60 --> 583.00]  And looking forward to a great 2026.
[584.28 --> 588.58]  The Habits and Methods.
[589.44 --> 590.82]  Yeah, that's a good show title.
[590.82 --> 591.40]  That's cool.
[592.68 --> 593.44]  That's cool, man.
[593.52 --> 596.48]  Next time Nick's on, we should have one called The Habits and Methods of Nick Neesey.
[596.86 --> 598.34]  Oh, man.
[598.50 --> 599.62]  I do enjoy Nick as well.
[599.78 --> 601.24]  I concur with everything.
[602.38 --> 603.30]  What was his name again?
[603.38 --> 603.62]  I'm sorry.
[603.72 --> 604.00]  Andrew.
[604.32 --> 604.64]  Andrew.
[604.82 --> 605.60]  Everything Andrew said.
[605.66 --> 608.50]  I was too busy listening to catch the first name.
[608.58 --> 609.00]  I'm sorry, Andrew.
[609.16 --> 610.50]  But yeah, I concur.
[610.96 --> 615.10]  Adam Jacob, Nick Neesey, Matt Reier, piano to guitar.
[615.50 --> 618.06]  Like, I mean, that's just podcast gold there.
[618.06 --> 618.14]  Yeah.
[618.14 --> 622.70]  So I have collated the list.
[622.70 --> 623.88]  I'll put that in the show notes.
[623.96 --> 626.70]  We'll have all these favorite episodes listed.
[626.84 --> 628.52]  Andrew listed 11.
[629.28 --> 630.96]  So that's a lot.
[631.04 --> 631.72]  Not the most.
[631.80 --> 633.60]  There is somebody who's going to list more than 11.
[633.96 --> 635.08]  It's probably going to be you, Adam.
[635.48 --> 639.32]  But in addition to Adam, there's somebody else to set up a teaser.
[639.46 --> 640.56]  They're not a spoiler, but a teaser.
[640.56 --> 643.52]  I was going to outdo Andrew, but still, that's a good list.
[644.08 --> 648.06]  And for our lists, we try not to overlap listener lists.
[648.24 --> 650.68]  And so you and I have both created our own lists.
[650.76 --> 655.98]  But however, we're kind of crossing off the ones that they mention as they go so that we don't have too much overlap.
[656.14 --> 658.88]  Because that's just repetition.
[658.88 --> 660.92]  And we all want to keep it dry around here.
[662.20 --> 663.64]  He took a lot of my favorites, though.
[663.66 --> 664.24]  I'm not going to lie.
[664.66 --> 666.42]  A lot of his favorites were my favorites.
[666.42 --> 681.08]  And speaking of JS Party and Nick Neesey and Amel Hussain, who was on the show last year but didn't quite hit the three-timer pace that Nick hit and that Matt Ryer hit, she's coming back on the show in January.
[681.30 --> 684.90]  So Amel actually did reach out recently and say, hey, how come Nick's on the show more than I am?
[684.90 --> 687.38]  And I just said, I can't get rid of this guy.
[687.48 --> 690.84]  He's always hanging around, whereas you disappear for a while and then come back.
[690.92 --> 692.28]  So you're always welcome, Amel.
[692.38 --> 693.50]  And she's coming soon.
[693.68 --> 695.86]  So a little more JS Party sprinkled in.
[696.42 --> 698.18]  Upcoming episodes.
[698.66 --> 698.84]  Yeah.
[699.44 --> 700.10]  All right.
[700.10 --> 701.56]  You want the Andrew Patton remix?
[702.34 --> 703.18]  Hit it.
[703.58 --> 703.98]  There you go.
[705.08 --> 706.72]  Hello, ChangeLog family.
[707.26 --> 710.48]  I've been the pianist for many years, which is very exciting.
[710.92 --> 714.72]  I was hoping for a few more banging piano beats from Breakmaster Cylinder.
[715.34 --> 719.98]  They are always very dramatic and certainly interesting.
[720.94 --> 724.74]  Looking forward to a weird and wonderful 2026.
[726.42 --> 733.34]  There you go.
[733.76 --> 735.28]  Those are special moments right there, man.
[735.34 --> 736.58]  Listen to those banging beats.
[737.38 --> 739.76]  A sweet voicemail remix like that.
[739.76 --> 741.56]  And a nice little crazy outro.
[741.76 --> 744.56]  If you knew Breakmaster, like we know Breakmaster.
[745.82 --> 746.60]  Very fitting.
[746.96 --> 750.28]  It's a very fitting outro to the banging beats.
[750.28 --> 750.72]  100%.
[750.72 --> 751.62]  100%.
[751.62 --> 752.10]  All right.
[752.16 --> 754.92]  Up next, because, hey, his name starts with a B.
[755.84 --> 756.58]  It's our old friend.
[756.70 --> 759.10]  And I think every year, Caller Inner.
[759.56 --> 760.14]  Come on now.
[760.14 --> 760.26]  Hopefully.
[760.74 --> 761.62]  It's Brett Cannon.
[761.90 --> 762.44]  Brett Cannon.
[762.98 --> 763.38]  Here we go.
[763.38 --> 765.06]  Hello, Adam and Jared.
[765.30 --> 769.24]  It's Brett Cannon calling for that annual tradition to see whether I can read dates appropriately
[769.24 --> 772.04]  while I tell you about my favorite episodes that I got to listen to this year.
[772.30 --> 775.32]  So I'm going to start off with The Power of the Button, which you actually recorded in
[775.32 --> 777.26]  2024, but didn't publish until 2025.
[777.58 --> 778.14]  So I'm safe.
[778.36 --> 783.30]  I found that episode kind of fun just to have that twist on it of talking about the physicality
[783.30 --> 786.78]  of the world and just how that kind of ties into technology and just kind of the different
[786.78 --> 791.52]  approach of just seeing how things tie in both sides of both the physical and the software
[791.52 --> 792.32]  for all of us.
[792.62 --> 797.56]  The next episode I liked a lot was the 1000 Times Faster Financial Database with Yoran
[797.56 --> 798.28]  from Tiger Beetle.
[798.28 --> 802.94]  I just thought that was a really cool chat to show that sometimes, you know what, you don't
[802.94 --> 804.08]  have to take the general solution.
[804.28 --> 807.96]  Sometimes it's okay to actually build something from scratch if it leads to a simple solution
[807.96 --> 809.06]  that really gets you what you're after.
[809.06 --> 813.96]  I also really enjoyed the chat with Bert Hubert, Build Software That Lasts.
[814.00 --> 817.60]  Just a lot of good advice that I think a lot of us could stand to listen to consistently.
[818.02 --> 824.40]  And then finally, the WSL.exe-cathello.cs episode I liked a lot for two reasons.
[824.40 --> 830.04]  One, Adam's total infatuation with WSL was rather infectious and great to hear.
[830.30 --> 834.20]  And also I wanted to give a letter of recommendation for Mads.
[834.24 --> 835.24]  He is an awesome person.
[835.52 --> 838.10]  And with that, to give Breakmaster Cylinder something to work with.
[838.10 --> 842.56]  Andrea did not listen to any of these episodes, so she loves them all equally, as does our
[842.56 --> 842.78]  kiddo.
[843.14 --> 843.44]  Thanks.
[844.54 --> 850.76]  So to bring everybody else in on that reference of Andrea at the end, go back to previous
[850.76 --> 858.74]  States of the Log in which BMC created a hilarious remix of Brett's previous message where the
[858.74 --> 862.84]  whole thing is centered around his wife, Andrea, which was one of my favorites from previous
[862.84 --> 863.28]  years.
[863.28 --> 864.62]  I'm not going to lie.
[864.74 --> 867.66]  BMC's remix of this one, also one of my favorites.
[867.86 --> 871.34]  But first, do you want to address Brett's actual content of what he had to say?
[871.46 --> 871.70]  Or should we?
[872.46 --> 873.20]  Let's see.
[874.08 --> 874.88]  Power of the Button.
[875.26 --> 877.00]  Power of the Button was definitely powerful.
[877.50 --> 879.74]  You know, and that was a...
[879.74 --> 884.02]  I think I mentioned the Good for Nothing Button book in that show.
[884.02 --> 889.44]  And that just brings like the titling of our shows, which I think we may introduce a new
[889.44 --> 891.80]  category, which is best title.
[893.24 --> 900.22]  That was a fun title for me, obviously for the content, but then also the Good for Nothing
[900.22 --> 902.70]  Button book that I've read with my kids.
[902.70 --> 910.42]  You know, I don't know where the infectious feelings I had towards WSL went.
[910.88 --> 911.58]  I was going to say.
[912.02 --> 916.64]  But I think they went with Windows out the door to some degree.
[917.12 --> 919.24]  I'm such a wishy-washy operating system person.
[919.34 --> 919.82]  I can't help it.
[919.84 --> 921.64]  I'm a literal operative.
[921.80 --> 923.34]  I would say an OS hopper.
[923.42 --> 924.00]  You are a hopper.
[924.00 --> 924.66]  Not even a distro hopper.
[924.78 --> 926.96]  You want to call it a sampler, but it's more of a hopper, I think.
[927.04 --> 928.30]  Yeah, it kind of is, honestly.
[929.44 --> 931.30]  You know, I just want to love Windows.
[931.30 --> 932.64]  I just wish they would get it together.
[933.90 --> 937.82]  You know, there's so much good stuff in there and just too much AI getting slapped around.
[938.08 --> 940.96]  Anyways, WSL is really cool, though, for Windows.
[941.06 --> 944.80]  Like, I think if you are, for some reason, you got to be in that world where, like, you
[944.80 --> 948.74]  have no choice because that's what your platform is, your applications are, your company's at,
[948.82 --> 950.28]  then, you know, it is what it is.
[950.34 --> 951.94]  That's what you got to do.
[953.00 --> 957.50]  I think WSL is the next best thing and super cool for that to be, like, embedded in Windows.
[957.50 --> 961.92]  So, I mean, that, to me, is a technological feat that I love.
[962.88 --> 968.88]  So, if I had to be in Windows, I could only be there happily because of WSL.
[969.56 --> 969.68]  Right.
[971.00 --> 973.00]  Which didn't exist back when I switched away.
[973.42 --> 973.54]  No.
[973.60 --> 979.06]  And I think it's very cool that it does exist, but I just don't have that problem anymore.
[979.40 --> 980.56]  Can we address this title, though?
[980.56 --> 985.64]  WSL.exe-cathello.cs.
[985.86 --> 986.70]  That was your title, Jared.
[986.98 --> 987.40]  That's right.
[987.66 --> 988.90]  You came up with that all on your own.
[989.08 --> 991.88]  And when you said it to me, I was like, ship it, man.
[992.06 --> 992.68]  Just ship it.
[992.98 --> 993.32]  Just ship it.
[993.32 --> 996.00]  We had a hard time naming that one because it was two interviews.
[996.60 --> 1001.04]  And so it was the one about WSL and then the other one with Mads, is it Torgerson?
[1001.04 --> 1005.44]  I can't remember his last name, the current lead design on C Sharp.
[1005.44 --> 1010.96]  And it's like, well, it's two different things and I don't know, this and that.
[1011.16 --> 1012.52]  You kind of, what do you do?
[1012.64 --> 1017.24]  And then I was like, I don't even know where I came up with that, but I just thought, let's
[1017.24 --> 1019.58]  just send a command out there and say hello to C Sharp.
[1019.94 --> 1021.72]  Let's just have WSL tell us hello.
[1023.02 --> 1025.82]  It's also been too long since we talked to Brett.
[1025.82 --> 1032.36]  And I feel like we've done ourselves a disservice with change-logging friends missing that friend.
[1033.16 --> 1034.02]  Well said.
[1034.58 --> 1035.38]  Come back, Brett.
[1035.56 --> 1035.80]  Anytime.
[1036.70 --> 1038.20]  We will invite you personally soon.
[1038.62 --> 1042.48]  Unless you email us first and they'll say, come on.
[1042.82 --> 1042.94]  Yeah.
[1043.02 --> 1043.76]  Let's do it.
[1044.30 --> 1047.50]  We did some Python coverage this year, but we were talking with other folks, you know?
[1047.58 --> 1049.06]  We're just kind of mixing it up a little bit.
[1049.70 --> 1054.30]  And not that we have to talk to Brett about Python, but of course, and he's moved on from
[1054.30 --> 1056.22]  the steering committee, but there's lots to say there.
[1057.08 --> 1060.40]  And I haven't watched John Wick 4, so maybe I've been avoiding him.
[1060.40 --> 1063.64]  Just like ashamed of myself for not having done that.
[1063.80 --> 1064.94]  We talked about Dune too.
[1064.94 --> 1065.00]  Dune too.
[1065.40 --> 1065.78]  That's right.
[1065.78 --> 1066.30]  And John Wick 4.
[1066.98 --> 1069.42]  Those are the things we were supposed to do to get back together.
[1070.12 --> 1070.78]  And I did not.
[1070.94 --> 1073.06]  I did not watch Dune too, because I'm still kind of mad at Dune too.
[1073.06 --> 1074.36]  Dune too is so good, man.
[1074.42 --> 1075.18]  It was so good.
[1075.54 --> 1076.26]  It is so good.
[1076.26 --> 1077.28]  It's a rewatch for me.
[1077.42 --> 1082.26]  I have a hard time going and watching one again, because it was sort of a slow burn to
[1082.26 --> 1082.58]  the storyline.
[1082.58 --> 1083.36]  It was a slow burn.
[1083.44 --> 1084.36]  It never ended too.
[1084.80 --> 1087.64]  But Dune too takes all that to the next level.
[1088.22 --> 1089.16]  And it's worth it.
[1089.60 --> 1090.52]  I mean, it's good.
[1091.00 --> 1091.32]  It's good.
[1091.52 --> 1094.04]  Now, I know I told you this, but I'm not sure if I said this on the show.
[1094.04 --> 1098.06]  When I went and saw Dune 1, they didn't call it Dune 1.
[1098.44 --> 1098.88]  No, they didn't.
[1098.92 --> 1101.58]  And I didn't do trailers or anything, because I'm like, it's Dune.
[1101.64 --> 1102.50]  I want to watch it.
[1102.74 --> 1103.12]  That's right.
[1103.24 --> 1104.70]  And I don't get out to movies very often.
[1105.26 --> 1108.22]  And so I got out to a movie, and I went to Dune 1, and I was enjoying the heck out of
[1108.22 --> 1109.28]  it, even though it was a slow burn.
[1109.36 --> 1110.06]  I'm patient.
[1110.16 --> 1110.88]  I like slow movies.
[1111.54 --> 1113.80]  And then I realized it's only half of a movie.
[1114.32 --> 1117.16]  And I just got very angry, because they didn't say Dune 1.
[1117.42 --> 1119.22]  At least then I would have known what I was getting myself into.
[1119.58 --> 1119.80]  Yeah.
[1120.06 --> 1123.26]  But I remember being like two hours in thinking, how are they going to get through all this?
[1123.30 --> 1124.38]  There's so much more that happens.
[1124.86 --> 1126.50]  And then I'm like, oh, they aren't.
[1127.62 --> 1129.94]  And then it was, what, three years later for Dune 2?
[1130.02 --> 1130.70]  I was just too mad.
[1130.76 --> 1131.76]  I'm like, I'm not going to see it.
[1132.38 --> 1132.70]  Yeah.
[1133.06 --> 1133.88]  I'm just overweight.
[1134.26 --> 1138.12]  Now, it's been long enough that maybe I can just change that attitude, my bad attitude.
[1138.30 --> 1140.26]  But that was my stance prior.
[1140.88 --> 1143.92]  And that's why I haven't seen Dune 2 yet, even though I hear it's pretty good.
[1144.78 --> 1145.66]  It's pretty good.
[1147.18 --> 1148.24]  I would recommend it.
[1148.34 --> 1151.18]  Speaking of pretty good, you want to hear this BMC remix of Brett Cannon?
[1151.68 --> 1152.64]  I cannot wait.
[1152.90 --> 1153.66]  There's a power.
[1154.10 --> 1156.16]  If you think there's power in the button, just wait for this one.
[1156.76 --> 1157.80]  Hello, Adam and Jared.
[1157.96 --> 1161.52]  It's Brett Cannon calling for that annual tradition to tell you about my favorite episodes.
[1162.14 --> 1165.64]  So I'm going to start off with the power of the button, talking about the physicality
[1165.64 --> 1167.80]  of the button and just how that kind of ties into technology.
[1167.80 --> 1167.88]  Interesting.
[1168.46 --> 1171.32]  The next episode I liked a lot was the 1000 Butt Infections.
[1171.82 --> 1176.34]  I just thought that was a really cool chat to show that sometimes, you know what, you
[1176.34 --> 1177.58]  don't have to take the journal solution.
[1177.76 --> 1180.94]  Sometimes it's okay to actually scratch your butt if it really gets you what you're after.
[1181.30 --> 1182.06]  So I'm safe.
[1182.58 --> 1185.76]  And then finally, the kind of fun cat butt episode.
[1185.76 --> 1190.38]  Just a lot of good cat butt advice that I think a lot of us could stand to listen to consistently.
[1191.56 --> 1194.54]  Andrea did not love any of these episodes, but you know what?
[1194.70 --> 1195.34]  It's okay.
[1196.16 --> 1197.48]  She still is an awesome person.
[1201.70 --> 1203.86]  Oh, I hope you like that, Brett.
[1205.02 --> 1205.78]  Oh, man.
[1206.16 --> 1206.68]  That's edgy.
[1207.66 --> 1208.30]  That's edgy.
[1208.54 --> 1209.54]  Do we have to bleep that one at all?
[1209.68 --> 1210.40]  Is there any bleeps there?
[1210.40 --> 1214.02]  I just think, I think butt is pretty pedestrian at this point.
[1214.58 --> 1215.14]  It was good.
[1215.40 --> 1216.00]  That was good.
[1216.44 --> 1216.96]  Oh, my gosh.
[1217.00 --> 1217.50]  The cat.
[1219.34 --> 1220.22]  Oh, gosh.
[1220.54 --> 1220.96]  The cat.
[1220.96 --> 1222.04]  I'm still 12 years old at heart.
[1222.14 --> 1224.34]  You know, a good butt joke just still hits me.
[1225.22 --> 1225.50]  Yeah.
[1225.98 --> 1231.82]  I'm just past a chest cold, and that made me want to cough some stuff up.
[1231.94 --> 1232.42]  Let's just say.
[1232.42 --> 1232.72]  Yeah.
[1233.12 --> 1233.36]  Yeah.
[1233.36 --> 1235.44]  It's kind of like, it's percolating.
[1236.60 --> 1237.68]  It's percolating.
[1238.38 --> 1239.32]  All right.
[1239.50 --> 1244.10]  Next up, another longtime listener and first time guest this year.
[1244.22 --> 1245.00]  It's Don McKinnon.
[1245.98 --> 1247.36]  Greetings, friends.
[1247.98 --> 1251.60]  My favorite episode of 2025 was an early one.
[1251.94 --> 1254.48]  Terso is rewriting SQLite in Rust.
[1254.78 --> 1257.30]  One reason is I'm a sucker for people building in Rust.
[1257.40 --> 1258.00]  Big surprise.
[1258.00 --> 1265.76]  But more importantly, I enjoyed it because I got to learn about the concept of deterministic simulation testing, which I found to be pretty fascinating.
[1266.06 --> 1270.20]  I always love the episodes where I get to learn about a concept that I haven't run up against before.
[1270.46 --> 1272.06]  Anywho, thank you guys for the podcast.
[1272.22 --> 1274.96]  I'm looking forward to what you have lined up in 2026.
[1275.50 --> 1276.26]  Pretty cool stuff.
[1276.56 --> 1280.18]  Of course, we talk about that as well on the Tiger Beetle episode.
[1280.52 --> 1287.34]  But Glauber Costa from Terso certainly introduced it to both of us and apparently a lot of other people on that episode.
[1287.34 --> 1294.58]  So, yeah, that's part of what we do here is just kind of uncover techniques that other people are doing that you may not have heard of.
[1294.96 --> 1296.78]  And maybe they'll help you on your path.
[1296.86 --> 1308.32]  Maybe they won't, but just being more well-rounded while not having to work too hard, you know, just listen to a couple of doofs ask silly questions and we learn a thing or two.
[1309.42 --> 1310.42]  That's a good way to summarize it.
[1310.44 --> 1310.94]  I like that.
[1312.46 --> 1312.82]  Doofs.
[1313.18 --> 1314.10]  A couple of doofs.
[1314.52 --> 1314.84]  I don't know.
[1314.84 --> 1317.66]  I've never done any deterministic simulation testing.
[1317.78 --> 1317.94]  Have you?
[1318.56 --> 1326.40]  No, that was actually really, really revealing because I had never heard of that concept.
[1326.90 --> 1331.60]  And it seemed to be, I'm trying to recall exactly how they were leveraging it.
[1332.16 --> 1335.96]  It was like being able to like have confidence in the future because it tested it.
[1335.96 --> 1343.16]  And it went kind of like an AI might even do to like figure things out that you wouldn't normally figure out like non-written tests that get tested.
[1343.54 --> 1345.98]  It's kind of like the unknown unknowns kind of thing, you know?
[1346.42 --> 1346.52]  Yeah.
[1346.58 --> 1348.12]  It's like a fuzzer to a certain extent.
[1348.22 --> 1350.46]  It's like a fuzzer for tests, but it was deterministic.
[1350.46 --> 1358.36]  And so it could be completely reproducible, whereas fuzzers generally will produce, you know, pseudo random stuff.
[1358.82 --> 1358.94]  Yeah.
[1359.04 --> 1364.46]  It's reproducible and therefore you get regression type of assurances as well.
[1364.46 --> 1367.34]  Obviously, I don't know exactly how it works.
[1367.90 --> 1369.82]  That's why we invite the experts on and tell us.
[1370.22 --> 1378.16]  You know, that's, I should look into this more now that this is brought up because as you may know, I'm working on this thing called DNS hole.
[1378.40 --> 1383.96]  And one thing I actually introduced was this thing called DNS chaos, DNS hole chaos.
[1383.96 --> 1390.32]  And it was essentially like throwing chaos at this DNS server to like attack it and like make it push its boundaries.
[1390.62 --> 1398.16]  And so pushing different RFCs, different things around it that it is supposed to support and should support.
[1398.62 --> 1402.42]  And it's kind of like deterministic testing or this DST is like that.
[1402.50 --> 1406.64]  It's like how can you push a system in a certain way and test its boundaries?
[1407.40 --> 1408.60]  That's kind of wild stuff.
[1409.22 --> 1412.02]  I should look more into DSTs.
[1412.16 --> 1412.90]  You should.
[1412.90 --> 1414.08]  DNS hole.
[1414.16 --> 1415.06]  Do we have to bleep that?
[1415.28 --> 1415.50]  I don't know.
[1415.82 --> 1416.14]  Oof.
[1416.30 --> 1416.94]  I don't think so.
[1417.28 --> 1417.70]  All right.
[1417.76 --> 1419.84]  Here's Don McKinnon's remix.
[1422.10 --> 1423.32]  Greetings, friends.
[1423.70 --> 1427.94]  I always love the episodes where I get to learn about a concept that I haven't run up against before.
[1428.52 --> 1436.20]  My favorite episode, I enjoyed it because I got to learn I'm in a simulation, which I found to be pretty fascinating.
[1436.78 --> 1440.22]  And my friends and the people have always been in the simulation.
[1440.22 --> 1442.32]  Big surprise.
[1442.32 --> 1442.70]  But.
[1445.58 --> 1447.38]  Anywho, thank you guys for the podcast.
[1456.10 --> 1457.08]  Into the matrix.
[1457.32 --> 1457.56]  Great.
[1457.68 --> 1458.94]  I love that sound at the end there.
[1458.94 --> 1459.70]  Yeah.
[1461.28 --> 1462.12]  And then the.
[1462.44 --> 1462.84]  It's still going.
[1463.06 --> 1463.26]  Yes.
[1463.38 --> 1463.66]  Just the.
[1463.82 --> 1464.44]  A little trail off.
[1464.72 --> 1467.86]  Trail off in the crowd noise there.
[1468.20 --> 1468.54]  Yeah.
[1468.54 --> 1472.98]  I was thinking, was that crowd noise crowdsourced from the meetup in Denver?
[1473.66 --> 1474.26]  Oh, wow.
[1474.52 --> 1476.62]  Because that's where BMC was with us.
[1476.64 --> 1481.48]  And I wonder if he like maybe pulled out his phone and captured some sound and like reused it later on for us.
[1481.60 --> 1482.38]  We should go ask.
[1482.46 --> 1482.96]  That would be a.
[1483.38 --> 1484.66]  That would be a deep cut if that was the case.
[1484.68 --> 1485.50]  That would be a deep cut.
[1485.58 --> 1487.34]  Like a well-planned deep cut.
[1487.40 --> 1488.60]  Like I'm going to need this one day.
[1489.04 --> 1491.56]  Someday I'm going to mix this into something they asked me for.
[1491.82 --> 1491.98]  Yeah.
[1491.98 --> 1492.70]  That would be really cool.
[1492.70 --> 1496.90]  And it turned out to be Don McKinnon's simulation crowd.
[1496.90 --> 1498.56]  All right.
[1498.80 --> 1501.24]  Next up we have Fernando.
[1501.98 --> 1503.92]  And his last name is tough because he's from Brazil.
[1504.72 --> 1505.20]  Bevalacqua.
[1506.66 --> 1507.18]  Bevalacqua.
[1507.48 --> 1507.70]  I don't know.
[1507.72 --> 1508.20]  He'll say it.
[1508.28 --> 1509.12]  So he'll get it right.
[1509.32 --> 1509.64]  Here we go.
[1510.42 --> 1511.54]  Hey, Adam and Jared.
[1511.74 --> 1514.86]  This is Fernando Bevalacqua speaking all the way from Brazil.
[1514.86 --> 1518.88]  I've been a long time listener of the pod since 2015.
[1519.44 --> 1525.40]  My favorite episodes of this year were Flowing with Agents, episode 658.
[1525.40 --> 1532.62]  And Reaching Industrial Economies of Scale, episode 632, both with Byung Liu.
[1532.84 --> 1538.90]  They were very insightful about the usage of agents in the everyday activities we have with software development.
[1539.18 --> 1545.82]  And I think they give us a glimpse into the future of how software development and how technology in the field will evolve.
[1546.20 --> 1554.12]  Last but not least, episode Solving the AI Energy Crisis, 652 with Greg Uzuri.
[1554.12 --> 1562.44]  It was a very interesting talk about politics, about infrastructure, about how to grow AI in a more practical way.
[1562.62 --> 1569.66]  Not about just technology, but how to build the real world, the physical things we need to sustain this kind of advancement.
[1569.66 --> 1580.66]  And I just want to say that it took me 10 years, but 2026 will not only be the year of the Linux desktop, but it will be the year that I will become a changelog plus plus subscriber.
[1581.70 --> 1584.52]  Hard earned money will be shared with you guys.
[1584.52 --> 1587.28]  I've been following you and really admire your work.
[1587.38 --> 1591.98]  And I want to support the creators, especially in this sea of AI sloth.
[1592.08 --> 1603.26]  I really want to see people with critical thinking and making the good questions and intriguing thoughts and making us reflect on the path we have to follow.
[1603.56 --> 1604.26]  That's it, guys.
[1604.54 --> 1605.22]  Keep on rocking.
[1605.64 --> 1607.22]  And thanks for all the pods.
[1607.22 --> 1609.92]  I don't know about you, Jared, but that's why we do it, man.
[1610.10 --> 1610.68]  Right there.
[1611.54 --> 1611.88]  Oh, yeah.
[1612.74 --> 1615.06]  I mean, who could have said it better?
[1615.14 --> 1618.72]  Like, in an age of AI slop, we are the critical thinkers.
[1619.12 --> 1622.56]  I mean, maybe not me and you, necessarily, but by proxy, of course.
[1622.56 --> 1623.80]  We talk to the critical thinkers.
[1624.06 --> 1624.42]  That's right.
[1627.06 --> 1627.90]  That's cool, man.
[1628.22 --> 1629.24]  All the way from Brazil, too.
[1629.24 --> 1635.96]  I mean, like, that just shows you how big the world is and how big the reach is for an MP3 on the internet, dude.
[1636.06 --> 1636.52]  Like, that's.
[1636.98 --> 1637.38]  Yeah.
[1637.68 --> 1638.14]  That's wild.
[1639.98 --> 1640.34]  Yeah.
[1640.46 --> 1641.94]  Super, super cool.
[1642.04 --> 1643.52]  Thank you, Fernando, for writing in.
[1645.62 --> 1647.34]  Digging the Beyond Lou episodes, of course.
[1647.46 --> 1649.02]  There's one of your critical thinkers there.
[1649.46 --> 1657.28]  Always worth talking to Beyond about what he thinks, where the world is going, and some of what he's, where he's making the world go.
[1657.28 --> 1657.72]  Yeah.
[1657.72 --> 1660.28]  By the experts they're doing there at Source, Graph, and Amp.
[1661.02 --> 1663.00]  And, of course, solving the AI energy crisis.
[1663.18 --> 1666.36]  That was, I think, one of our more controversial episodes of the year.
[1666.80 --> 1667.02]  Yeah.
[1667.38 --> 1678.06]  Probably created one of the longest threads in our Zulip channel because people began to debate and discuss the merits of AI and energy and politics.
[1678.06 --> 1683.96]  And it gets a little bit drawn down some political lines because of people's approaches to these things.
[1683.96 --> 1691.68]  But I liked Greg's story episode because he cracked me up a couple times when he put on the glasses.
[1692.38 --> 1694.00]  And I'm like, that was funny.
[1694.36 --> 1697.30]  He's doing some really cool, weird stuff with this house he's building.
[1697.52 --> 1701.42]  Just very interesting human with interesting takes.
[1701.82 --> 1707.42]  And decentralized AI training and inference.
[1707.42 --> 1708.86]  I don't know.
[1709.86 --> 1713.14]  Now they're trying to talk about space-based stuff, too.
[1713.24 --> 1719.54]  Not they, Greg, but they, the AI hyperscalers, are both Google and XAI.
[1719.84 --> 1725.28]  And I believe Bezos has to be talking about it because he's into space as well.
[1725.38 --> 1725.66]  Yeah.
[1726.04 --> 1728.06]  We're talking about training models in space.
[1728.56 --> 1729.94]  And I don't know.
[1729.98 --> 1730.80]  That's beyond my pay grade.
[1730.80 --> 1734.40]  To me, it doesn't seem like a very smart idea, but they seem to think it's going to be better.
[1734.90 --> 1738.16]  Maybe you're closer to the sun, so you get better solar power or something.
[1738.30 --> 1740.98]  But anyways, we can talk about that some other time.
[1741.30 --> 1742.90]  But I got some ideas there.
[1743.54 --> 1744.40]  You want to talk about them?
[1744.48 --> 1744.72]  You want to?
[1745.10 --> 1745.80]  Just briefly.
[1746.12 --> 1748.14]  I mean, it would make total sense, right?
[1748.20 --> 1749.00]  One, it's cold.
[1750.10 --> 1750.74]  Well, it's a vacuum.
[1750.86 --> 1751.98]  You don't have any air movement.
[1752.82 --> 1755.54]  So getting the heat away from the source would be difficult.
[1756.90 --> 1757.66]  I would think.
[1757.66 --> 1760.66]  I guess you have some sort of out and into space.
[1761.48 --> 1767.88]  I don't know that part, but definitely unfettered access to the number one energy source nearest to us.
[1767.96 --> 1771.34]  Yeah, closer to the sun makes sense, but you have to move the data up and down as well.
[1771.94 --> 1772.56]  Well, that's true.
[1772.88 --> 1774.04]  Well, maybe you can like.
[1774.14 --> 1774.64]  It seems tough.
[1774.80 --> 1778.72]  Like you get a bad GPU and it's like, dang, we got to send another rocket up.
[1779.12 --> 1779.36]  Anyways.
[1779.74 --> 1780.46]  Robots, I bet.
[1780.70 --> 1785.54]  Robots and automated hard drive delivery or data delivery from up and down.
[1785.54 --> 1787.00]  There's no pipe, I bet.
[1787.66 --> 1793.92]  That's going to be like taking the data literally from something and down to the earth or just chucking it out.
[1794.18 --> 1794.34]  Right.
[1794.40 --> 1795.24]  It'll make it.
[1795.48 --> 1795.72]  Right.
[1796.56 --> 1797.56]  It'll make it.
[1797.68 --> 1798.52]  It's going to make it.
[1798.78 --> 1801.46]  There's your DNS request there.
[1801.62 --> 1801.84]  Right.
[1802.02 --> 1802.36]  UDP.
[1802.60 --> 1803.12]  It'll make it.
[1803.20 --> 1804.22]  If not, who cares?
[1804.88 --> 1805.92]  Somebody else will catch it.
[1806.18 --> 1806.46]  Yeah.
[1806.46 --> 1807.02]  Yeah.
[1807.02 --> 1807.72]  I don't know.
[1807.92 --> 1818.92]  Smarter people than me say it's smart, but I'm a bit skeptical because it seems like a whole lot of work to get the stuff up there and doing stuff and then a whole lot of work to get it back down.
[1818.98 --> 1821.48]  And then you have latency.
[1821.88 --> 1827.30]  I guess you could do training, but maybe not inference because I mean, what's the latency even from Starlink?
[1827.30 --> 1828.88]  It's not great.
[1829.00 --> 1830.46]  It's better than anything else there's been.
[1830.60 --> 1835.48]  But anyways, maybe a topic we can dig into in 2026 is like what?
[1835.56 --> 1836.52]  It's a caching problem, Jared.
[1836.84 --> 1837.50]  It's varnish.
[1838.12 --> 1838.76]  It is.
[1838.90 --> 1839.92]  Varnish will solve this too.
[1840.20 --> 1840.68]  That's right.
[1840.86 --> 1841.68]  Varnish in space.
[1841.78 --> 1842.62]  Now we're talking.
[1842.62 --> 1843.90]  All right.
[1844.10 --> 1845.04]  Fernando remixed.
[1849.38 --> 1850.92]  Hey, Adam and Jared.
[1851.22 --> 1852.84]  This is Fernando Pivilaqua speaking.
[1853.78 --> 1860.44]  It took me years, but 2026 will be the year that I will become a secret agent in the field.
[1860.94 --> 1865.60]  I really want to see the world and I really admire gas men.
[1865.60 --> 1875.84]  I want to see everyday creating in politics, faith, justice, and so real prices in my world of intrigue.
[1876.96 --> 1877.90]  That's it, guys.
[1878.20 --> 1880.86]  Keep on rocking and thanks for all the thoughts.
[1882.50 --> 1884.40]  That's a proper remix right there.
[1885.54 --> 1889.48]  I thought it was like Darth Vader entering for a bit there, you know?
[1890.68 --> 1890.90]  Batman.
[1890.90 --> 1891.74]  Then he got like heroic.
[1893.00 --> 1894.06]  Secret agent.
[1894.06 --> 1894.70]  Fernando.
[1894.70 --> 1895.06]  Fernando.
[1895.32 --> 1895.80]  Batman.
[1896.16 --> 1896.64]  Bevilacqua.
[1897.42 --> 1898.34]  That's what I'm talking about.
[1898.40 --> 1898.60]  Yeah.
[1898.82 --> 1899.66]  That's what I'm talking about.
[1899.84 --> 1901.38]  That's what I'm talking about right there, man.
[1901.54 --> 1902.76]  That's a nickname for you.
[1902.92 --> 1903.66]  The Dark Knight.
[1903.94 --> 1904.20]  Yes.
[1904.32 --> 1905.02]  Oh, yes.
[1905.80 --> 1907.30]  From the south.
[1907.98 --> 1909.56]  The deep, deep south.
[1909.76 --> 1910.36]  That's right.
[1910.90 --> 1911.76]  Deeper than the south.
[1912.08 --> 1912.90]  Oh, my gosh.
[1912.90 --> 1913.48]  That's cool.
[1913.68 --> 1914.48]  I like that one.
[1914.66 --> 1915.56]  That was epic.
[1916.02 --> 1916.60]  That was epic.
[1920.92 --> 1923.32]  Well, friends, I'm here with my good friend, Chris Kelly.
[1923.32 --> 1925.16]  Augment code.
[1925.16 --> 1926.66]  Chris, I'm a fan.
[1926.98 --> 1928.40]  I use Augie on the daily.
[1928.78 --> 1930.40]  It's one of my daily drivers.
[1930.46 --> 1931.86]  Now, I use Cloud Code.
[1932.00 --> 1933.58]  I use Augment Augie.
[1933.86 --> 1935.74]  And I also use Amp Code and others.
[1935.92 --> 1937.70]  But Augie, I keep going back to it.
[1937.88 --> 1938.54]  And here's where I'm at.
[1938.64 --> 1942.82]  I feel like not enough of our audience knows about Augment code.
[1942.96 --> 1944.94]  Not enough about Augie, the CLI.
[1945.18 --> 1945.74]  It's amazing.
[1945.90 --> 1946.50]  I love it.
[1946.74 --> 1947.30]  What can you share?
[1947.30 --> 1947.74]  Yeah.
[1948.00 --> 1951.66]  We often say Augment is the best coding assistant you've never heard of.
[1951.98 --> 1956.22]  And that's both frustrating as someone that works there and is very proud of the work we've done.
[1956.50 --> 1957.50]  But also inspiring.
[1957.74 --> 1960.48]  We want to go and sort of punch above our weight.
[1960.60 --> 1962.86]  Because we aren't anthropic and we aren't open AI.
[1963.42 --> 1970.22]  And so the quality of the product itself with our context engine, once you do touch it, people are just blown away by that.
[1970.32 --> 1971.88]  And so that keeps me going every day.
[1971.88 --> 1975.52]  So not to bear the lead here, but this is a paid spot.
[1975.70 --> 1978.34]  You are sponsoring this show to get this awareness.
[1978.54 --> 1980.06]  Now, at the same time, we're selective.
[1980.42 --> 1982.68]  And I love to use your tool.
[1983.12 --> 1984.64]  But there is in the world.
[1984.74 --> 1989.08]  So a lot of developers look at the space and they say, OK, well, how long can this work?
[1989.14 --> 1993.90]  How long is this sustainable in the case of Cursor or Windsurf?
[1993.98 --> 1996.94]  Or you pick the name and you think discounted tokens.
[1997.28 --> 2000.14]  Help me shape a lens for our audience.
[2000.14 --> 2002.34]  I think it's a lot of awareness, right?
[2002.42 --> 2010.12]  Like Cursor got a lot of publicity early on for like fast revenue growth, which well deserved.
[2010.34 --> 2014.88]  I think, you know, frankly, some of the media gets the story wrong.
[2015.00 --> 2021.48]  And that like if I gave you $1.50 for every dollar you sent me, I'd be the fastest growing startup in the valley.
[2021.78 --> 2025.80]  And so when you're selling discounted tokens, yes, of course you're going to grow very fast.
[2025.82 --> 2028.48]  But all that money plus more goes to the model providers.
[2028.48 --> 2033.52]  So I think the real story is the story of Anthropic and, you know, being an API provider.
[2033.90 --> 2040.16]  I think the market has just moved so fast and there's so many pieces of competition out there that it's just hard to get noticed.
[2040.60 --> 2046.42]  So, friends, I love Augment Code and I love using Augie and I highly recommend you use it.
[2046.62 --> 2047.48]  I love using Augie.
[2047.48 --> 2057.60]  I can hand Augie a well-defined specification, a well-defined PEP, as I call them in my world, an agent flow, and it executes flawlessly.
[2058.14 --> 2063.20]  So the cool thing about Augie that I love most really is that context engine.
[2063.52 --> 2065.36]  And I can hand it a task.
[2065.36 --> 2071.62]  And it can just churn away on my well-defined plan and just never bother me and accomplish the mission.
[2071.88 --> 2078.44]  It is so cool leveraging the latest models, the context engine, and all the fun things behind the scenes in that awesome CLI.
[2078.66 --> 2080.10]  So, yes, go try it out.
[2080.58 --> 2081.36]  Augmentcode.com.
[2082.20 --> 2086.04]  Right in the top there is a CLI icon, a terminal icon.
[2086.40 --> 2088.94]  Click that, install it, and change your world.
[2089.28 --> 2089.84]  It's going to be awesome.
[2090.34 --> 2091.44]  Augmentcode.com.
[2095.36 --> 2104.52]  Up next, we have the, my previous tease was somebody will outnumber Andrew Patton, and that's Jamie Tanna.
[2104.72 --> 2107.66]  Jamie, safe to say Jamie likes the pod.
[2107.88 --> 2109.50]  Let's hear from Jamie.
[2110.14 --> 2111.16]  Hey, Adam and Jared.
[2111.46 --> 2112.72]  Happy State of the Log again.
[2113.04 --> 2114.04]  It's Jamie Tanna.
[2114.52 --> 2118.72]  I think this may be one of the most on-time voicemails I've sent you.
[2120.32 --> 2120.80]  Yeah.
[2121.36 --> 2123.40]  Thanks again for another great year.
[2123.40 --> 2130.44]  I ran the numbers, and this year I've listened to a whopping 74 episodes, which is about five days of listening time.
[2130.80 --> 2137.38]  And I've managed to whittle down an amazing year to a short list of around 15 episodes.
[2138.18 --> 2140.38]  But I'll try and keep it even shorter than that.
[2140.70 --> 2147.02]  With the strife and the open source ecosystem this year, there were some really good discussions about some of the drama and some of the threats.
[2147.02 --> 2153.28]  Some of the really good episodes around this were Feroz in Changing on the Friends 111.
[2153.56 --> 2157.04]  Mike McQuaid and Justin Sills in Changing on the Friends 113.
[2157.04 --> 2165.70]  And a related discussion with Andrew Nesbitt and the excellent work he is doing with ecosystems in Interviews 665.
[2166.28 --> 2169.72]  I've also really enjoyed what feels like an increase in levity this year.
[2169.72 --> 2182.12]  And especially some of the conversations with your friends, like Amal in Friends 86, Dan Moore in Friends 78, Matt Raya in 75 and 90, and a whole lot of other Friends episodes.
[2182.62 --> 2188.26]  As ever, things like Hash Define and Friendly Few game shows have been really, really great.
[2188.26 --> 2196.00]  And I've really enjoyed them, especially even like being in my own this year and participating myself was really cool.
[2196.00 --> 2202.14]  I also really enjoyed some of the deep dives you'll have done into things like different folks' blog posts.
[2202.58 --> 2208.60]  So, for instance, Friends 81 and the interview you had with Sean in Interviews 666.
[2208.96 --> 2217.12]  As a little bit of an AI skeptic, it has been really interesting digging into some of the interesting cases of AI without a lot of the hype.
[2217.12 --> 2218.52]  You'll have done.
[2218.76 --> 2224.10]  So, in particular, things like the interview with David Croshaw in Interviews 629.
[2224.58 --> 2228.66]  Nick Neesey in Friends 88, 102 and 120.
[2229.24 --> 2232.64]  And Adam Jacob in Interviews 664.
[2233.34 --> 2235.72]  And Steve Yege in Friends 96.
[2236.32 --> 2242.32]  And also Torsten Ball in Interviews 648.
[2242.70 --> 2247.10]  Finally, I want to again repeat, but it's been really nice just having a few moments.
[2247.12 --> 2250.24]  A few episodes of just the two of you just chatting about stuff.
[2250.98 --> 2255.66]  Not necessarily even about the tech, just about life and movies and stuff.
[2255.86 --> 2256.72]  It has been really interesting.
[2257.16 --> 2260.04]  And yeah, a really nice balance between different things.
[2260.74 --> 2262.94]  So, thanks for a great year.
[2263.50 --> 2264.14]  And here's to another.
[2264.70 --> 2264.98]  Thanks.
[2266.86 --> 2267.58]  Cheers, Jamie.
[2267.80 --> 2268.30]  That was awesome.
[2268.38 --> 2268.52]  Yeah.
[2268.60 --> 2269.12]  Thanks, Jamie.
[2269.70 --> 2270.40]  That's very touching.
[2270.40 --> 2272.00]  I mean, just to think about that.
[2272.10 --> 2273.40]  Like, he's not only a listener to that level.
[2274.16 --> 2275.58]  Five days of listening.
[2275.94 --> 2279.18]  But he took the time to go through, to retrospect.
[2279.58 --> 2280.14]  He did.
[2280.22 --> 2280.96]  What mattered.
[2281.10 --> 2283.82]  And made a comprehensive, well-articulated list.
[2284.02 --> 2286.10]  And then shared it via voice to us.
[2287.20 --> 2288.46]  And then it's going to get remixed.
[2288.62 --> 2289.44]  I mean, like, that's...
[2289.84 --> 2290.38]  That's spectacular.
[2290.38 --> 2290.46]  Yeah.
[2290.48 --> 2293.90]  I mean, honestly, Jamie's list pretty much could have just been my list.
[2294.26 --> 2296.58]  Like, he hit on a lot of the ones that I would have done.
[2296.72 --> 2297.94]  And he hit on...
[2297.94 --> 2299.76]  You know, we were talking about doing 8 to 10.
[2299.86 --> 2300.42]  He got...
[2300.42 --> 2302.28]  I think he got 15 or 16 in there.
[2302.64 --> 2303.80]  But to add a little bit.
[2303.86 --> 2306.80]  Because he was just going through, like, you know, friends, 111.
[2307.14 --> 2308.62]  You know, interviews, 665.
[2310.44 --> 2312.84]  To add a little bit of color to those.
[2313.76 --> 2317.22]  So, he talked about the ones where we do blog posts.
[2317.56 --> 2319.16]  So, interviews, 666.
[2319.36 --> 2321.72]  That was Do Repeat Yourself with Sean Gattie.
[2321.72 --> 2322.62]  That was recently.
[2323.32 --> 2324.36]  In which we had him on.
[2324.42 --> 2326.46]  And then there's another one, Friends 81, that he mentioned.
[2326.58 --> 2327.50]  Called Change My Mind.
[2328.16 --> 2330.14]  And this is where we use Chris Keel's post.
[2330.72 --> 2333.12]  About development topics that he's changed his mind on.
[2333.50 --> 2334.54]  Over the last 10 years.
[2334.68 --> 2338.10]  As a bit of a launching pad into a discussion that you and I had.
[2339.22 --> 2341.90]  And about things we have and have not changed our minds on.
[2342.14 --> 2342.74]  Over the years.
[2342.86 --> 2345.98]  And so, that's a little bit of what Jamie was talking about.
[2346.02 --> 2348.52]  Of course, there's many other references there.
[2348.92 --> 2350.62]  But what are your thoughts on them?
[2351.72 --> 2354.60]  Man, I could probably go on.
[2354.68 --> 2355.52]  But I agree.
[2355.62 --> 2357.92]  I think even that show in particular, Chained My Mind.
[2358.08 --> 2362.82]  I recall coming to that episode thinking, did I prepare well enough for this?
[2362.86 --> 2364.14]  I felt underprepared.
[2364.74 --> 2367.92]  Because I was thinking, like, how much have I changed my mind on?
[2368.00 --> 2373.52]  And I think, did we have something happen before that show that kind of made it a little uniquely recorded?
[2374.96 --> 2375.70]  I don't know.
[2375.70 --> 2376.96]  I thought something happened.
[2377.50 --> 2380.04]  Probably a cancellation of a guest, is my guess.
[2380.36 --> 2380.68]  Maybe.
[2381.08 --> 2381.32]  Something.
[2382.28 --> 2383.86]  I don't recall exactly in the moment.
[2384.08 --> 2386.38]  But that was a fun one to record.
[2386.60 --> 2386.92]  I agree.
[2387.08 --> 2389.48]  I like some of the pods we get to do.
[2389.56 --> 2393.14]  Like, one of the ones on my list, I guess I can just briefly share it.
[2393.22 --> 2393.92]  And no one said it yet.
[2393.96 --> 2396.08]  Was, turn him into a walrus.
[2396.88 --> 2398.32]  That's on my faves list.
[2398.46 --> 2398.98]  That was fun.
[2398.98 --> 2406.72]  But those are like the fun episodes where you just like, just get together and just get in a groove on whatever it is.
[2406.80 --> 2410.90]  And I think, Chained My Mind, that was a really fun, really fun pod.
[2411.40 --> 2415.14]  Probably the best pod that we recorded all year was the Dev Null one that we didn't get a shit.
[2415.70 --> 2416.80]  We were on fire, man.
[2416.88 --> 2417.30]  Remember that?
[2417.68 --> 2421.10]  Oh, that was, that was pure gold.
[2421.18 --> 2421.48]  Honestly.
[2422.08 --> 2424.88]  It might have been like the best 45 minutes we've ever done together.
[2425.00 --> 2426.30]  That's why we were so mad afterwards.
[2426.30 --> 2429.24]  Because the show that actually went out, I listened back to it.
[2429.28 --> 2430.86]  I was like, you know, it's fine.
[2431.06 --> 2431.52]  It was good.
[2431.62 --> 2431.86]  Yeah.
[2432.16 --> 2434.62]  You know, we covered a lot of topics and we had fun and stuff.
[2435.14 --> 2435.48]  And we did.
[2435.68 --> 2438.60]  But man, that 45 minutes was pure gold.
[2439.20 --> 2439.72]  It was.
[2439.78 --> 2441.86]  At least we get to say that and no one can refuse it ever.
[2441.86 --> 2447.22]  Yeah, no one can, no one can challenge the fact or the opinion for a free event.
[2447.40 --> 2448.56]  More of a fact than an opinion.
[2448.74 --> 2448.90]  Okay.
[2449.38 --> 2450.68]  A lot of good episodes here though.
[2450.68 --> 2454.14]  Like 629, I think was in this list.
[2454.62 --> 2454.94]  666.
[2455.20 --> 2455.98]  David Kroshaw.
[2455.98 --> 2463.90]  So we had, yes, we had Sean Gedecky, of course, Agentic, Infra Changes, Everything, the most recent Adam Jacob episode, which was really good.
[2464.22 --> 2464.48]  Yeah.
[2464.72 --> 2470.74]  And then of course the Steve Yeggy episode, I think probably the most referenced as we go through our list here.
[2471.44 --> 2472.48]  I mean, Steve Yeggy.
[2472.50 --> 2473.96]  Adventures in Babysitting Coding Agents.
[2474.08 --> 2478.08]  That one was very interesting to a lot of people.
[2478.34 --> 2479.50]  Another stellar title.
[2479.90 --> 2480.52]  Look at that title.
[2480.52 --> 2483.30]  That was one of my, that's on my list of best titles for sure.
[2483.30 --> 2483.80]  Oh man.
[2484.12 --> 2484.46]  That's a good one.
[2484.46 --> 2487.54]  Anytime you get an 80s movie reference into a title, come on.
[2487.62 --> 2488.36]  And it's on point.
[2488.48 --> 2489.04]  It's like, come on.
[2489.84 --> 2490.98]  It couldn't be a better title.
[2491.10 --> 2492.44]  There's no other way to title that.
[2492.50 --> 2494.24]  It's like taking candy from a baby, you know?
[2494.28 --> 2494.64]  Yeah.
[2495.16 --> 2495.28]  Don't do that.
[2495.28 --> 2497.32]  Which is a really weird figure of speech.
[2498.04 --> 2498.98]  Which I would never do.
[2498.98 --> 2499.98]  Okay.
[2501.20 --> 2502.28]  Jamie Tanner remix.
[2502.76 --> 2503.56]  Let's do it.
[2508.10 --> 2509.12]  Hey Adam and Jared.
[2509.40 --> 2510.66]  Happy State of the Lock again.
[2511.02 --> 2512.00]  It's Jamie Tanner.
[2514.10 --> 2517.52]  It's been really nice just having a few episodes of just the two of you.
[2517.76 --> 2519.08]  Just chatting about stuff.
[2519.76 --> 2521.46]  Not necessarily even about the tech.
[2521.60 --> 2523.30]  Just about life.
[2524.56 --> 2525.80]  From movies.
[2526.44 --> 2527.68]  From friends.
[2527.68 --> 2530.02]  From game shows.
[2530.64 --> 2531.76]  From pipe.
[2532.70 --> 2533.98]  From deep diving.
[2535.28 --> 2535.94]  From systems.
[2536.90 --> 2537.94]  From whittles.
[2542.56 --> 2543.90]  Oh my gosh.
[2544.38 --> 2546.00]  You give Breakmaster a reason to go.
[2547.36 --> 2549.56]  Just to lose his mind a little.
[2550.06 --> 2551.08]  Oh gosh.
[2553.56 --> 2554.84]  That's a throwback.
[2556.64 --> 2557.22]  I love that.
[2557.22 --> 2557.90]  That's cool.
[2558.86 --> 2559.64]  Up next.
[2560.14 --> 2561.58]  Another long time listener.
[2561.82 --> 2562.50]  And community member.
[2562.70 --> 2563.48]  It's Jarvis Yang.
[2564.00 --> 2565.48]  Hello ChangeLog and friends.
[2565.64 --> 2567.58]  This is Jarvis checking in once more.
[2567.86 --> 2572.40]  Great to see the ChangeLog.news website has finally landed in the right hands.
[2572.82 --> 2574.94]  2025 has been quite the year.
[2575.46 --> 2578.58]  And I was happy to help keep an eye on that vanity domain.
[2578.82 --> 2580.30]  And inform Jared of its availability.
[2580.92 --> 2582.62]  And I really appreciate you Jared.
[2582.82 --> 2584.94]  Keeping me updated on all the major news.
[2584.94 --> 2586.26]  Things get hectic.
[2586.26 --> 2591.08]  But always make sure to carve out time for a listen and a look through the newsletter.
[2591.60 --> 2593.60]  My final shout out is for Minibar 20.
[2593.98 --> 2598.54]  That's the 20th unconference for the Ministar organization here in Minnesota.
[2598.54 --> 2605.14]  For those who don't know, Minibar is the nation's largest and longest running technology unconference.
[2605.14 --> 2607.02]  First held in 2006.
[2607.02 --> 2616.18]  It's a user-generated, participant-led event, meaning there are no keynotes and all the sessions are run by the local tech and business communities.
[2616.44 --> 2617.78]  Best of all, it's free.
[2617.78 --> 2619.10]  Mark your calendars.
[2619.32 --> 2623.72]  Minibar 20 is on Saturday, May 2nd, 2026.
[2624.44 --> 2632.08]  Also, a very happy early birthday to Jared's daughter, whose birthday conveniently aligns with the event weekend.
[2632.46 --> 2634.38]  See you all next year.
[2637.02 --> 2637.78]  Conveniently aligns.
[2638.58 --> 2640.24]  Do you hear a little bit of a troll in there?
[2640.24 --> 2643.00]  We were invited to Minibar.
[2643.40 --> 2646.18]  He thought it'd be a good place for our next live show.
[2646.34 --> 2648.08]  And I told him that we have a conflict that week.
[2648.12 --> 2649.26]  And so that's what he's referring to.
[2649.42 --> 2649.68]  Okay.
[2650.94 --> 2654.60]  But for those who don't know Jarvis, he calls in every year and he gives us shout outs.
[2654.68 --> 2656.54]  And then he always gives something else a shout out.
[2656.80 --> 2659.60]  Most of the time, some Minnesota-based organization.
[2659.98 --> 2662.68]  Such as Minibar, which looks like a really cool event, actually.
[2662.82 --> 2664.36]  20 years to throw an unconference.
[2664.52 --> 2665.64]  That's pretty impressive.
[2666.18 --> 2667.42]  Is it called Minibar?
[2668.36 --> 2668.76]  Minibar.
[2668.76 --> 2670.20]  Like M-I-N-N-E.
[2671.08 --> 2671.40]  Bar.
[2671.96 --> 2673.36]  Like Minnesota, I think.
[2673.38 --> 2673.90]  Oh, yeah.
[2673.94 --> 2674.60]  That makes sense.
[2674.90 --> 2675.08]  Yeah.
[2677.12 --> 2677.48]  Okay.
[2677.92 --> 2678.66]  Minnesota Bar.
[2679.14 --> 2679.58]  Minibar.
[2679.98 --> 2680.32]  Minibar.
[2681.30 --> 2682.18]  May 2nd.
[2683.02 --> 2684.10]  Bar camps are still a thing?
[2684.32 --> 2685.00]  Is this really?
[2687.16 --> 2687.78]  They must be.
[2687.84 --> 2688.46]  At least in Minnesota.
[2688.66 --> 2688.84]  I know.
[2688.86 --> 2692.90]  I know that Nebraska, the Omaha Bar Camp, I think, has gone by the wayside.
[2693.02 --> 2694.24]  I think someone tried to bring it back.
[2694.24 --> 2697.56]  We had it going for five, six, seven years.
[2697.76 --> 2698.44]  Maybe 10 years.
[2698.44 --> 2700.92]  And then eventually it stopped and then someone tried to bring it back.
[2701.00 --> 2705.88]  I'm not sure if it's still going, but I don't hear much about bar camps anymore.
[2706.70 --> 2708.26]  Missed that idea, you know?
[2708.58 --> 2708.84]  Mm-hmm.
[2709.12 --> 2709.64]  That's cool.
[2710.92 --> 2715.86]  I wonder what makes them, I guess just getting people together is hard, you know?
[2716.42 --> 2716.84]  It really is.
[2716.84 --> 2717.24]  That's just a lot of work.
[2717.24 --> 2719.10]  Expensive, hard.
[2720.02 --> 2720.92]  Yeah, it is a lot of work.
[2720.98 --> 2721.86]  It takes some dedication.
[2722.12 --> 2726.72]  There's risk involved that is oftentimes undue, you know?
[2726.78 --> 2730.66]  Like, you're like, why am I risking this in my personal life to put on an event?
[2730.66 --> 2733.54]  Usually with regards to insurance or et cetera.
[2734.10 --> 2737.70]  Or fronting a bunch of money to rent a space out that maybe no one's going to show up to.
[2737.76 --> 2739.76]  And you're like, eventually you're like, why am I doing this?
[2740.00 --> 2740.14]  You know?
[2740.72 --> 2745.60]  And you almost need like a nonprofit established for it, which is a whole other problem, right?
[2745.72 --> 2745.92]  Yeah.
[2745.92 --> 2747.72]  And now you're like basically taking on a second job.
[2748.04 --> 2748.36]  Yeah.
[2748.78 --> 2749.04]  Yeah.
[2750.00 --> 2750.64]  Not easy.
[2751.00 --> 2751.66]  Not easy.
[2751.88 --> 2755.06]  So thank an organizer out there, y'all, when you go to your events.
[2755.44 --> 2756.26]  Yeah, for sure.
[2756.62 --> 2761.04]  Definitely thank an organizer because no one's getting rich off these things.
[2762.40 --> 2763.52]  So they're doing it for the love.
[2763.58 --> 2766.22]  Lots of times they have ulterior motives, but they're usually straightforward.
[2766.70 --> 2770.60]  And it's still worth thanking them as long as they're doing it on the up and up.
[2771.24 --> 2775.54]  Just as maybe a slight mention to that, I was in the GopherCon channel.
[2775.92 --> 2777.30]  And they go for Slack.
[2778.64 --> 2785.06]  And I guess there was some concern around timing, you know, because like people want it at a certain time of year.
[2785.16 --> 2786.20]  And it's kind of hard to do that.
[2786.20 --> 2786.64]  Yeah, I know it's moved.
[2786.78 --> 2789.70]  It's like August now or in the winter.
[2790.06 --> 2792.58]  They've had to move it to different locations and move it to different timing.
[2792.86 --> 2795.42]  And I just saw like just a drive-by look.
[2796.10 --> 2802.92]  Heather Sullivan, who runs that conference along with, I believe, Brian and Eric.
[2802.92 --> 2807.66]  I don't know what the exact structure is anymore, but she was saying it loses money.
[2807.76 --> 2809.40]  Like it lost 200 grand last year.
[2810.60 --> 2819.38]  So even a conference that's well established like that, if that, I don't doubt it's not a true statement, but like how true is the detail of that that I'm not aware of?
[2819.38 --> 2823.42]  You know, like what's left under the covers I haven't mentioned here.
[2823.50 --> 2829.98]  But I saw her mentioned in there in GopherCon Slack and the channel there in the Gopher Slack that lost money.
[2829.98 --> 2837.08]  So like even if you run a well-done conference like that with great organization, every year great production.
[2837.62 --> 2840.52]  Yeah, I mean, that's like 12 years running maybe, like a long time.
[2841.00 --> 2841.16]  Yeah.
[2841.60 --> 2841.92]  Yeah.
[2842.12 --> 2848.42]  So you're not immune to the risk, even if you've been in a groove for years.
[2848.42 --> 2866.68]  Well, even when the who runs Strange Loop, I can't remember his name now, but at the last Strange Loop, one of the last talks was the organizer, whose name I'm forgetting, forgive me, who put it on thanklessly, except for the small group of people that thanked him for years, six, seven years.
[2866.68 --> 2877.36]  And he shared all the financials for Strange Loop, which was a very successful conference, small regional, not huge like a KubeCon, but certainly well-respected and well-run.
[2878.24 --> 2880.12]  And the financials just didn't make any sense.
[2880.34 --> 2884.46]  Like you could just tell by the end of it, he was only doing it because he loved doing it.
[2884.56 --> 2887.22]  There was no reason why anybody in their right mind would do it otherwise.
[2887.78 --> 2887.98]  Yeah.
[2888.06 --> 2890.22]  And that's for like a well-regarded successful conference.
[2890.22 --> 2896.52]  So, I mean, that's why un-conferences do make some sense because there's less to do, right?
[2896.52 --> 2901.26]  Like your job is to get people to show up and hopefully there's some catering or whatever, but it's just less.
[2901.60 --> 2905.34]  And then you're also less guaranteed that you're going to have quality talks, et cetera.
[2906.02 --> 2910.26]  I'm feverishly trying to get the name of our dear friend who I'm sad.
[2910.36 --> 2911.58]  I've forgotten the name as well.
[2911.64 --> 2912.06]  Same.
[2912.94 --> 2913.38]  Alex.
[2913.60 --> 2914.14]  Alex Miller.
[2914.54 --> 2915.06]  There you go.
[2915.36 --> 2915.50]  Yeah.
[2915.50 --> 2915.70]  Yep.
[2916.92 --> 2917.36]  Yeah.
[2917.36 --> 2919.06]  I mean, and we were there.
[2919.30 --> 2921.20]  Thankfully, it was their first and last.
[2921.28 --> 2922.50]  It was the last Strange Loop.
[2922.64 --> 2923.42]  It was our first.
[2924.24 --> 2925.40]  2023 in St. Louis.
[2925.40 --> 2927.40]  And we met that call in there.
[2927.60 --> 2928.72]  That was kind of cool.
[2929.66 --> 2935.84]  Long-time listener, Slack, and Zulu participant, and then met in the flesh, fellow Pennsylvanian.
[2937.24 --> 2939.30]  That's where I'm originally from was Pittsburgh area.
[2940.36 --> 2941.38]  But man, that's a great conference.
[2941.50 --> 2951.86]  And then Alan, or sorry, Alex, you know, obviously was emotional delivering his final, you know, rollout finale of the conference.
[2951.86 --> 2965.38]  And if you listen to the episode we delivered from there, I was smart enough to not only be there in the moment, but also capture a voice memo and put that on the pod.
[2965.46 --> 2973.14]  So at the tail end, the closer of that episode includes some of those final moments from that conference.
[2973.14 --> 2979.62]  So if you didn't make it or you did make it and you want to kind of go back with some nostalgia, we tried to capture some of that for you.
[2979.86 --> 2980.52]  It was a good conference.
[2981.22 --> 2984.62]  And if you're wondering about that episode, it's called Vibes from Strange Loop.
[2984.82 --> 2990.66]  And it also featured the moment we met Taylor Trosh, who we haven't forgotten ever since.
[2990.78 --> 2991.94]  Take my small hand.
[2991.94 --> 2995.30]  That's episode 559.
[2995.58 --> 2996.94]  So changelog.fm slash 559.
[2997.64 --> 2999.56]  If you want to go back and hear what Adam is talking about.
[2999.66 --> 3001.76]  Lots of, that was a grab bag, an anthology.
[3002.12 --> 3003.62]  Ah, one of the best.
[3004.06 --> 3004.40]  Yeah, man.
[3004.50 --> 3005.00]  That was awesome.
[3005.30 --> 3005.94]  One of the best.
[3006.64 --> 3007.14]  Remix it.
[3007.60 --> 3008.24]  Let's remix it.
[3008.92 --> 3009.58]  Hello, friends.
[3011.56 --> 3013.14]  Jarvis has finally landed.
[3013.56 --> 3015.16]  Check, check, checking in once more.
[3015.34 --> 3015.50]  Check.
[3016.54 --> 3018.20]  Friends, things get hectic.
[3018.20 --> 3025.10]  Always make sure to carve out time for Minibar 20, the nation's largest technology unconference.
[3025.48 --> 3025.92]  It's free.
[3026.52 --> 3028.68]  Best of all, there is a Minibar.
[3029.16 --> 3033.38]  And I really appreciate you, Jared, informing me of the Minibar's availability.
[3034.34 --> 3036.38]  I'm happy to help keep an eye on it.
[3037.10 --> 3039.18]  See you all next year.
[3040.14 --> 3040.90]  Jarvis out.
[3043.58 --> 3044.48]  Jarvis out.
[3044.48 --> 3048.24]  Yeah, that's good stuff.
[3048.40 --> 3049.28]  Celebrate the Minibar.
[3051.06 --> 3053.78]  Yeah, that's a solid remix, Breakmaster Cylinder.
[3054.12 --> 3054.82]  Solid remix.
[3055.12 --> 3056.52]  So far, so good on these remixes.
[3056.66 --> 3057.82]  I don't think there's been a miss yet.
[3058.40 --> 3058.54]  No.
[3059.22 --> 3059.80]  All right.
[3060.32 --> 3068.58]  Now, speaking of longtime friends, here's our very old friend from way back, probably at the beginning of the show, Justin Dorfman.
[3068.64 --> 3069.74]  How long were you known Justin, Adam?
[3070.18 --> 3071.52]  Oh, my gosh.
[3071.94 --> 3072.42]  Forever.
[3072.42 --> 3075.08]  Over a decade.
[3075.54 --> 3075.68]  Yeah.
[3076.80 --> 3077.78]  Hey, Jared, Adam.
[3078.04 --> 3078.92]  Justin Dorfman here.
[3079.52 --> 3080.80]  Long time listener.
[3081.08 --> 3081.82]  Ten plus years.
[3082.40 --> 3090.66]  And I'm really looking forward to 2026 and the guest that you will be having on and maybe even see you in North Carolina.
[3091.02 --> 3091.22]  Maybe.
[3091.58 --> 3091.98]  Anyway.
[3092.36 --> 3093.46]  Have a great one.
[3093.72 --> 3097.78]  And thanks for always entertaining, at least me.
[3098.72 --> 3099.22]  Yeah.
[3099.42 --> 3099.80]  Take care.
[3099.80 --> 3102.72]  Yeah, I'm a big fan of Justin.
[3103.30 --> 3105.02]  Max CDN days.
[3105.32 --> 3105.70]  Oh, yeah.
[3106.80 --> 3108.54]  Really involved in the community.
[3108.64 --> 3110.04]  Always trying to love on people.
[3110.24 --> 3111.18]  That's what I love about Justin.
[3111.66 --> 3114.28]  And I'm loving the work he's doing for Sourcegraph.
[3114.50 --> 3116.82]  And I think by proxy, maybe AMP, too.
[3116.86 --> 3118.48]  I'm not sure because of the divide now.
[3118.48 --> 3125.08]  But I'm loving his role and what he's doing for them and just kind of keeping people informed with what Sourcegraph is doing, what AMP is doing.
[3126.08 --> 3128.76]  And he's, yeah, super awesome, dude.
[3129.30 --> 3129.64]  Mm-hmm.
[3131.00 --> 3132.50]  Always love to hear from you, Justin.
[3132.86 --> 3133.90]  Don't be a stranger.
[3134.18 --> 3135.46]  Hopefully we'll see you in North Carolina.
[3136.12 --> 3136.70]  Mm-hmm.
[3136.70 --> 3138.18]  Here's your remix.
[3141.06 --> 3142.26]  Hey, Jared and Adam.
[3142.62 --> 3143.52]  Justin Dorfman here.
[3143.72 --> 3144.92]  Long-time listener.
[3145.18 --> 3146.08]  10-plus years.
[3146.76 --> 3152.96]  I'm really looking forward to 2026 and the guests that you will be having on.
[3152.96 --> 3155.52]  And maybe we can see you in North Carolina.
[3156.18 --> 3156.40]  Maybe.
[3156.64 --> 3157.14]  Anyway.
[3157.52 --> 3158.66]  Have a great one.
[3159.00 --> 3160.88]  And thanks for always entertaining me.
[3161.32 --> 3161.52]  Yeah.
[3162.78 --> 3163.14]  All right.
[3163.54 --> 3163.88]  Wow.
[3164.98 --> 3165.88]  Very musical.
[3166.70 --> 3168.18]  Rhythmic, even.
[3169.12 --> 3170.12]  Very rappy.
[3170.56 --> 3171.08]  Yes.
[3171.38 --> 3172.02]  Like a little rap.
[3172.32 --> 3173.26]  Justin Dorfman here.
[3173.62 --> 3173.78]  Yep.
[3174.52 --> 3175.06]  Yeah, very.
[3176.56 --> 3177.54]  Very rap-like.
[3179.00 --> 3180.10]  Took me back to the 80s, man.
[3180.16 --> 3182.16]  That's like late 80s, early 90s rap.
[3182.80 --> 3183.44]  That was.
[3183.70 --> 3186.56]  That was very much like Funkmaster Flex and stuff like that.
[3186.90 --> 3187.34]  Mm-hmm.
[3188.00 --> 3188.78]  All right.
[3188.96 --> 3191.80]  Our final caller, Nabil Suleiman.
[3192.56 --> 3193.80]  Hello, Adam and Jared.
[3194.18 --> 3195.08]  What a year it's been.
[3195.08 --> 3196.86]  This has definitely been the year of AI.
[3197.30 --> 3200.90]  And I do appreciate and count on your content to keep up to date with all of that.
[3201.22 --> 3206.04]  However, my favorite episodes personally are the ones around Homelab, Kaizen, and Oxide.
[3206.18 --> 3207.06]  Those have all been great.
[3207.26 --> 3211.18]  But definitely, without a doubt, peak changelog for me was the meetup in Denver.
[3211.50 --> 3214.44]  It was great meeting you all and making several new friends along the way.
[3214.70 --> 3222.46]  And I mean, who would have imagined that we'd all go adventuring in the wilderness together with the mysterious Breakmaster Cylinder and battle a whole bunch of rattlesnakes.
[3222.46 --> 3224.08]  It was definitely a trip to remember.
[3224.44 --> 3228.88]  Anyways, kudos to you all for another great year of great content.
[3229.18 --> 3229.68]  Take care.
[3230.06 --> 3230.58]  Merry Christmas.
[3230.82 --> 3231.62]  Happy New Year's.
[3231.70 --> 3231.94]  Cheers.
[3232.66 --> 3234.74]  And I'll see you on the other side of the year.
[3236.24 --> 3237.08]  Cheers to you, Nabil.
[3237.44 --> 3237.94]  That was awesome.
[3240.74 --> 3241.46]  Battle of the rattlesnakes.
[3242.36 --> 3242.54]  Not.
[3242.68 --> 3242.90]  Not.
[3242.90 --> 3245.82]  It's one rattlesnake.
[3246.60 --> 3248.22]  Well, he pluralized it, so.
[3248.42 --> 3248.98]  I like that.
[3248.98 --> 3250.18]  Yeah, that's how stories go.
[3250.26 --> 3250.86]  They get better and better.
[3250.86 --> 3251.78]  You got embellished a little bit.
[3251.96 --> 3253.44]  Yeah, they get better as you get further away.
[3253.46 --> 3253.48]  Yeah, they get better as you get further away.
[3253.50 --> 3254.58]  That story a little bit, you know?
[3254.64 --> 3255.80]  A little seasoning won't hurt anybody.
[3255.92 --> 3258.06]  Remember that den of rattlesnakes we had stumbled upon?
[3258.42 --> 3259.22]  Gosh, so many.
[3259.50 --> 3261.32]  Just one almost got us.
[3261.38 --> 3262.22]  Why'd it have to be snakes?
[3262.76 --> 3263.08]  Yeah.
[3264.64 --> 3266.00]  Man, Homelab for sure.
[3266.00 --> 3270.40]  You know, Homelab's near and dear to my heart.
[3272.42 --> 3273.60]  Proxbox for life.
[3274.04 --> 3275.16]  ZFS for life.
[3276.62 --> 3277.58]  Windows for life?
[3277.66 --> 3277.98]  Oh, wait.
[3279.48 --> 3279.92]  Well.
[3280.56 --> 3281.46]  Windows for a minute.
[3281.78 --> 3283.56]  Well, not quite.
[3283.82 --> 3289.60]  But I did get support on getting my Windows license from Nabil.
[3289.76 --> 3290.78]  So that was very kind of Jim.
[3290.88 --> 3291.26]  Oh, nice.
[3291.62 --> 3291.80]  Yeah.
[3291.88 --> 3292.26]  Thanks, Nabil.
[3292.26 --> 3298.88]  He lent me his support to get it for slightly less, which is very kind.
[3299.18 --> 3299.56]  Very kind.
[3300.36 --> 3304.60]  Well, I do want to mention Nabil's mention of our AI coverage.
[3304.60 --> 3307.72]  And I think it was Andrew as well or somebody else earlier on.
[3307.84 --> 3310.84]  Maybe it was Jamie who said he's kind of a skeptic.
[3310.96 --> 3320.22]  But he appreciates our AI coverage because it's not completely saturated in the hype that you can get out there.
[3320.22 --> 3322.50]  Because we've also been accused of that.
[3323.38 --> 3328.38]  Especially, yeah, it seems like people on Spotify in particular comment on our shows.
[3328.62 --> 3330.96]  And they're very upset that we're talking about AI.
[3331.46 --> 3335.94]  And one guy says it's all we talk about now and blah, blah, blah.
[3336.66 --> 3339.82]  And, you know, you can't keep everybody happy.
[3339.82 --> 3350.92]  But I want to bring it up because, you know, it is something that we think about and something that we want to both talk about and recognize and use and ponder.
[3350.92 --> 3367.60]  But we also understand that it is oversold and that it is over discussed and that we tend to lean into it at times when I think we have less interesting things on the docket.
[3367.72 --> 3372.28]  We're like, well, it's always fodder for an interesting conversation because of all the questions, right?
[3372.30 --> 3373.40]  Because we don't have the answers.
[3373.40 --> 3379.36]  And so we're doing our best to both talk about it but not gush too much.
[3379.44 --> 3382.54]  But then when we're excited, just go ahead and be excited, you know?
[3383.18 --> 3398.02]  I think you probably, as you guys have been listening over the years, have gotten a taste of both our excitement and then our skepticism and then our disappointments and then our realizations of what it can do and how exciting that is and what it can't do and how frustrating that is.
[3398.02 --> 3408.92]  And so, yeah, we're trying and it's not easy because if we wanted to just chase audience, we would just lean hard into it like so many people have.
[3409.54 --> 3414.24]  And I've never wanted the changelog to become like yet another AI show.
[3415.02 --> 3418.22]  And so I appreciate that you all appreciate the non-AI topics.
[3418.22 --> 3422.70]  And when we hear the criticism, we take it very seriously.
[3422.96 --> 3425.14]  And then I look back at our most recent episodes.
[3425.32 --> 3428.60]  Like I go through our playlist and I'm like, maybe we are just doing too much of this.
[3428.66 --> 3429.88]  And I look at it and I'm like, you know what?
[3430.02 --> 3430.24]  Nope.
[3430.36 --> 3431.90]  There's plenty of stuff in there that's not.
[3432.00 --> 3436.18]  It's just like confirmation bias, I guess, when people say it's all we talk about.
[3437.62 --> 3441.48]  I think it definitely is a recurring topic.
[3441.78 --> 3442.20]  Oh, yeah.
[3442.20 --> 3447.52]  But it's not the isolated primary topic, obviously.
[3447.96 --> 3448.54]  Of the show.
[3448.68 --> 3448.80]  Yeah.
[3448.86 --> 3450.08]  I mean, it's what episodes it is.
[3451.14 --> 3451.26]  Yeah.
[3451.26 --> 3459.96]  I think even like the show I did recently with Alex Kuchmar was that we were talking about the Linux rabbit hole, essentially.
[3461.12 --> 3463.76]  Because I didn't even plan that really.
[3463.80 --> 3465.50]  We just started talking about the fun stuff.
[3466.02 --> 3467.20]  And that was kind of fun.
[3467.20 --> 3473.44]  And I think we were about 50 minutes in and he mentioned something he had done, vibe coding.
[3474.36 --> 3476.48]  And we talked about it on the podcast as well.
[3477.40 --> 3479.80]  And I didn't even plan to mention it, really.
[3480.98 --> 3482.64]  So it wasn't like a topic on my mind.
[3482.72 --> 3484.48]  But obviously he laid down the spades.
[3484.56 --> 3485.96]  So we played spades.
[3485.96 --> 3502.42]  Well, just wanted to mention that we do think about it and we hope to bring somewhat level-headed and yet also keeping to the edge of what things are going on and not ignoring it just because it's AI.
[3502.74 --> 3504.36]  Because I feel like that's also foolhardy.
[3505.18 --> 3508.04]  And, of course, news talks about it all the time because it's so much in the news.
[3508.04 --> 3516.26]  And so if you want to keep up with it without having to actually follow the news yourself, of course, I feel like we've tried to be a good resource for that.
[3516.64 --> 3521.12]  But, you know, opinions vary and mileage varies as well.
[3521.42 --> 3525.08]  Even my own mileage with the same tool I was using yesterday varies today.
[3525.22 --> 3530.30]  It's like, oh, I was so excited yesterday and then I hit a roadblock today and now I'm mad again.
[3530.48 --> 3535.76]  You know, it's like doing two all over again because we're emotional beings.
[3535.76 --> 3540.66]  Well, let's get to the bills and our final Breakmaster Cylinder remix.
[3541.54 --> 3542.76]  Peak changelog for me.
[3549.16 --> 3551.38]  Was venturing in the wilderness.
[3557.22 --> 3560.00]  Together with the mysterious Breakmaster Cylinder.
[3560.00 --> 3567.10]  And battling a whole bunch of rattlesnakes.
[3588.10 --> 3589.18]  There's a little trail off there.
[3590.00 --> 3591.26]  I love the footsteps.
[3591.88 --> 3594.16]  Yeah, I hope that ending means that we survived, you know.
[3595.94 --> 3597.68]  After whatever happened there happened.
[3597.92 --> 3598.34]  The climactic.
[3599.88 --> 3600.86]  There was lasers.
[3601.22 --> 3602.50]  There was a lot going on there.
[3603.50 --> 3604.66]  Somebody got carried away.
[3605.00 --> 3605.32]  Yeah.
[3605.96 --> 3612.92]  Like, carried away with their talent and then carried away with their unfortunate event, maybe.
[3613.02 --> 3614.58]  There was no speaking at the end in the walkway.
[3614.66 --> 3615.88]  So, I mean, we don't know for sure.
[3616.68 --> 3618.94]  Could have been a park ranger getting us out of there.
[3618.94 --> 3621.56]  We're done now.
[3622.16 --> 3622.52]  All right.
[3622.56 --> 3623.58]  We're done with BMC now.
[3623.70 --> 3624.38]  Thank you, BMC.
[3626.26 --> 3629.48]  Not forever, but just for this particular state of the log.
[3630.00 --> 3630.32]  Yes.
[3630.80 --> 3633.46]  And thank you to everybody who took the time out of your day.
[3633.54 --> 3634.44]  I know y'all are busy.
[3634.90 --> 3638.28]  I know it's asking a lot to record a voicemail and upload it through a form.
[3638.54 --> 3639.38]  None of that's easy.
[3639.38 --> 3645.68]  You know, if we were SaaS entrepreneurs, we'd be failing, right?
[3645.74 --> 3646.42]  There's too much friction.
[3646.76 --> 3648.10]  Our conversion rates would be low.
[3648.44 --> 3648.66]  Yeah.
[3649.28 --> 3650.86]  PLG is PLG.
[3651.84 --> 3657.42]  All that to say, we thank you for going through that for us because it makes us feel good.
[3657.54 --> 3660.32]  And hopefully, it makes you all feel good too.
[3660.42 --> 3661.72]  Should we talk about our own faves now?
[3661.76 --> 3662.76]  Let's get to our faves.
[3662.88 --> 3663.48]  I mean, come on.
[3663.54 --> 3665.66]  Enough of these people's faves.
[3665.76 --> 3666.92]  They don't know the real faves.
[3669.42 --> 3673.18]  So our friends at Framer are fans of this podcast and their sponsor.
[3673.18 --> 3677.14]  You know, most design tools, they lock you behind a paywall.
[3677.42 --> 3678.42]  Well, Framer flips that script.
[3678.64 --> 3683.42]  It is a free, full-feature design tool that does something that most site builders cannot.
[3683.92 --> 3686.06]  It's actually designed for designers.
[3686.60 --> 3691.88]  And Framer already built the fastest way to publish beautiful, production-ready websites.
[3691.88 --> 3696.16]  But with design pages, they've redefined what it means to design for the web.
[3696.40 --> 3700.28]  This is not a Webflow clone or a WordPress competitor.
[3700.72 --> 3708.76]  It is a true design platform, vectors, 3D transforms, gradients, wireframes, all the tools you actually use.
[3709.02 --> 3709.72]  And they're all free.
[3710.10 --> 3711.08]  Unlimited projects.
[3711.44 --> 3712.22]  Unlimited pages.
[3712.96 --> 3713.84]  Unlimited collaborators.
[3714.46 --> 3715.50]  And here is the kicker.
[3715.66 --> 3719.72]  You design, you iterate, and you publish all in one place.
[3719.72 --> 3721.42]  There's no Figma handoff.
[3721.52 --> 3724.02]  There's no messy HTML imports.
[3724.12 --> 3725.40]  There's no tool switching.
[3725.82 --> 3729.62]  And for designers and developers who are tired of the tool switching, this whole dance you've
[3729.62 --> 3735.66]  got to do to create social media assets, to create campaign visuals, icons, entire sites.
[3736.06 --> 3738.22]  You can do all this now without leaving Framer.
[3738.46 --> 3742.14]  This is where ideas go to live, start to finish.
[3742.14 --> 3746.82]  So if you're ready to design and publish in one tool, start creating for free today at
[3746.82 --> 3753.86]  Framer.com slash design and use our promo code changelog for a free month of Framer Pro.
[3754.14 --> 3756.32]  Again, Framer.com slash design.
[3756.72 --> 3760.24]  Use the code changelog for a free month of Framer Pro.
[3760.62 --> 3762.20]  Rules and restrictions may apply.
[3762.20 --> 3768.80]  The final chapter, you know, the final segment.
[3768.94 --> 3772.58]  It's like if it was a story arc, this is the final act of the pod.
[3772.90 --> 3773.28]  That's right.
[3773.80 --> 3774.46]  How do you want to do it?
[3774.46 --> 3775.16]  You want to go first?
[3775.24 --> 3775.98]  You want me to go first?
[3776.04 --> 3778.16]  You want to go tit for tat?
[3780.42 --> 3783.02]  Let's go at the exact same time and talk over each other.
[3784.14 --> 3785.30]  We've been known to do that.
[3785.42 --> 3786.36]  I mean, Jason will tell you.
[3786.84 --> 3787.10]  Yeah.
[3788.06 --> 3788.80]  You know, I don't know.
[3788.84 --> 3789.58]  I don't have a prescription.
[3789.74 --> 3790.50]  I'll take your lead.
[3790.50 --> 3791.80]  All right.
[3791.86 --> 3794.50]  Well, I have a list that was longer than I was expecting.
[3795.24 --> 3795.64]  Ten.
[3795.78 --> 3800.26]  My list is ten deep, and these are all ten that have not been mentioned at all yet, which
[3800.26 --> 3802.42]  means I had a bunch of other ones that other people mentioned.
[3802.90 --> 3806.72]  And I'm just going to ten that were not mentioned.
[3808.58 --> 3810.02]  And I'll start with the oldest.
[3811.24 --> 3818.66]  And that would be Interview 625, Open Source, from Open Source to Acquired with Ashley Jeffs.
[3818.66 --> 3820.18]  This was back in January.
[3820.50 --> 3830.60]  In which Ash told us all about Benthos and his journey to finding an acquirer for Benthos in Red Panda.
[3830.60 --> 3835.16]  And an open source success story in many ways.
[3835.16 --> 3839.48]  And also just a guy who cracked me up with the way he was.
[3839.62 --> 3845.02]  I mean, his mannerisms, the way he talks, his random contradictions of himself.
[3845.02 --> 3847.72]  Like, he would say left and then right, and he would stare at you.
[3848.18 --> 3848.44]  You know?
[3848.56 --> 3849.72]  Like, he's just a funny person.
[3849.98 --> 3850.88]  I really enjoyed him.
[3850.88 --> 3854.02]  Like, I try to get him back onto a pound to find.
[3854.12 --> 3856.40]  Because I'm like, you're just funny and fun to be around.
[3856.52 --> 3858.06]  Please come play games with us.
[3858.80 --> 3859.92]  And he respectfully declined.
[3860.08 --> 3864.54]  But to my chagrin, I really just enjoy that guy.
[3864.92 --> 3867.00]  And so that is my first fave.
[3867.00 --> 3874.58]  That was a fun episode.
[3875.34 --> 3876.10]  Daddy Pig.
[3878.30 --> 3878.74]  Yes.
[3878.74 --> 3881.30]  That was a good one.
[3881.52 --> 3881.88]  That was a good one.
[3881.88 --> 3882.48]  Should I go now?
[3882.94 --> 3883.36]  Yeah, go ahead.
[3883.42 --> 3884.38]  Should I comment a little bit?
[3884.42 --> 3885.26]  I like that one a lot.
[3885.36 --> 3886.42]  That was a good story, too.
[3887.42 --> 3889.10]  That was a fun story from a choir, too.
[3889.18 --> 3890.88]  Like, he's having fun doing what he's doing, too.
[3891.08 --> 3892.24]  He's taking care of his family.
[3892.54 --> 3892.84]  Right.
[3893.10 --> 3893.98]  Enjoying what he's doing.
[3894.08 --> 3895.22]  He's clearly pretty happy.
[3896.18 --> 3896.82]  Balanced, it seems.
[3896.82 --> 3898.10]  Remember how he sat on that chair?
[3898.20 --> 3899.28]  He had that chair set up.
[3899.34 --> 3901.82]  And he's like, this makes me more powerful than you guys.
[3901.86 --> 3903.10]  And I was like, it's totally working.
[3903.50 --> 3904.26]  It is working.
[3904.48 --> 3905.16]  The funny guy.
[3906.24 --> 3908.60]  Okay, well, I mentioned one during the pod.
[3908.66 --> 3910.10]  So I kind of went first, technically.
[3910.62 --> 3911.02]  Right.
[3911.38 --> 3912.28]  Which was which one?
[3912.68 --> 3914.08]  Turn him into a walrus.
[3914.40 --> 3915.14]  Oh, yes.
[3915.40 --> 3915.66]  87.
[3916.06 --> 3921.44]  This is when ChatGPT just got good at, like, Dolly 2 or something happened.
[3921.96 --> 3922.40]  Yes.
[3922.86 --> 3923.74]  Studio Ghibli.
[3924.36 --> 3924.60]  Right.
[3925.14 --> 3925.72]  Was that.
[3926.08 --> 3926.44]  Right.
[3927.02 --> 3928.96]  And then it's actually, so that's permeate.
[3928.96 --> 3932.40]  Like, I loved the short or the clip.
[3932.46 --> 3935.74]  I'm not sure which one it was out there on the socials.
[3937.26 --> 3938.66]  I had to share that with my brother.
[3939.04 --> 3940.94]  You know, I was like, this is this is cool stuff.
[3941.02 --> 3942.56]  And then because wasn't it?
[3942.56 --> 3944.34]  It turned me and him into a walrus.
[3944.42 --> 3944.52]  Right.
[3944.52 --> 3945.26]  We went golfing.
[3945.68 --> 3946.22]  It was just you.
[3946.34 --> 3947.54]  You're you're exiting a golf.
[3947.70 --> 3948.40]  It was just me.
[3948.62 --> 3950.70]  You had golfed with your brother, but he wasn't in the shot.
[3951.14 --> 3951.46]  Exactly.
[3951.74 --> 3955.26]  So in my mind, behind the scenes, I've got two pictures.
[3955.50 --> 3957.10]  One that's a selfie of me and my brother.
[3957.50 --> 3958.84]  And then one that was just me.
[3958.84 --> 3959.78]  And that one that was just me.
[3959.84 --> 3960.94]  I share with you on the pod.
[3960.96 --> 3962.58]  And then you turn me into a walrus.
[3962.94 --> 3963.26]  Right.
[3963.42 --> 3966.44]  And then I share that with him because he was there and he would have thought it was really
[3966.44 --> 3966.62]  cool.
[3966.64 --> 3968.30]  And he's not in tech at all.
[3968.60 --> 3970.64]  And then so then he came back a few months later.
[3970.82 --> 3971.50]  We golfed again.
[3971.58 --> 3972.34]  Same place.
[3972.98 --> 3973.86]  Took the same.
[3974.32 --> 3974.68]  Oh, yeah.
[3974.70 --> 3975.38]  Same selfie.
[3976.06 --> 3978.12]  But this time it was me, him and my son.
[3978.96 --> 3983.72]  And so behind the scenes in our household, I had to make me a walrus again or us a walrus.
[3983.84 --> 3985.76]  And it's just is cool.
[3985.90 --> 3986.10]  Yeah.
[3986.10 --> 3990.56]  So that one's like a heartstring for me, not just a good show and a good title, but it
[3990.56 --> 3991.64]  was a really good show, too.
[3991.70 --> 3995.52]  I thought that was like one of those ones where it's like, I think I said on there, like,
[3995.56 --> 3997.04]  this is what the Internet was made for.
[3997.16 --> 3999.10]  Like, that's the sauce, man.
[3999.38 --> 4000.06]  That's the sauce.
[4000.06 --> 4000.14]  Yes.
[4000.52 --> 4000.88]  Yes.
[4001.02 --> 4005.58]  And this was around the time that I began saying, to this day, I think we should continue
[4005.58 --> 4009.62]  to make, use software to make things that bring joy to people.
[4010.00 --> 4010.18]  Yeah.
[4010.40 --> 4011.84]  And like, that's the good stuff.
[4012.04 --> 4015.86]  Now, we can talk about all the downsides of AI generated images.
[4015.86 --> 4017.90]  And I'm aware of all these things.
[4017.90 --> 4019.30]  And I have all the feelings everybody else does.
[4019.30 --> 4026.68]  But like, that's the joy of software is like, take this person and turn them into a walrus.
[4026.76 --> 4027.54]  It's just fun.
[4027.62 --> 4027.96]  It's funny.
[4028.04 --> 4029.36]  Everybody wants to see what themselves look like.
[4029.46 --> 4030.14]  Oh, that looks like me.
[4030.18 --> 4031.02]  Oh, it doesn't look like me.
[4031.38 --> 4031.52]  Yeah.
[4031.52 --> 4032.28]  It gets old eventually.
[4032.56 --> 4035.60]  And, you know, there's creepy things you can do, et cetera, et cetera.
[4035.60 --> 4038.16]  But like, let's use it to have fun.
[4038.28 --> 4039.48]  And we did that on an episode.
[4039.48 --> 4040.16]  And I agree.
[4040.22 --> 4040.84]  That was a great one.
[4041.54 --> 4041.64]  Yeah.
[4042.34 --> 4042.52]  Yeah.
[4042.52 --> 4043.86]  I was just going to mention it and then move on.
[4043.90 --> 4045.12]  But we dug in deep.
[4045.12 --> 4049.56]  So I just, I roll with it, but the one I wanted to mention first, and it's because I haven't
[4049.56 --> 4051.12]  talked to him in so long.
[4051.18 --> 4052.62]  I couldn't believe how long it was.
[4052.68 --> 4054.22]  I talked to him, Drew Wilson.
[4054.64 --> 4060.66]  So we had Drew Wilson on the pod, episode 639 of the interview show, chasing that next
[4060.66 --> 4061.74]  big thing with Drew Wilson.
[4062.78 --> 4067.66]  And, you know, I'm not a big fan of the with, you know, titled shows, but that's what that
[4067.66 --> 4068.14]  was.
[4068.94 --> 4071.70]  Cause Drew is always chasing something.
[4071.70 --> 4079.90]  He's, he launched plazo, I believe, which was a banking platform, sold it to GoDaddy
[4079.90 --> 4081.38]  or I don't know what he'd say.
[4081.44 --> 4082.50]  He's done some crazy stuff.
[4082.58 --> 4086.42]  The guy is always, he's always on the fringe, like on where it should be.
[4086.48 --> 4090.04]  We're like, wherever the puck is going, he's kind of already there and he's kind of examined
[4090.04 --> 4090.50]  it already.
[4090.70 --> 4093.06]  And you're kind of coming to the puck and he's already been there.
[4093.20 --> 4093.90]  And that's Drew.
[4094.06 --> 4094.86]  So I really appreciate it.
[4094.88 --> 4096.66]  Getting back on the pod with him.
[4097.14 --> 4099.38]  And we produced a podcast together a long time ago.
[4099.38 --> 4103.92]  And so it was just wild getting to, to hang with him again and talk about what he's
[4103.92 --> 4104.28]  up to.
[4104.36 --> 4105.74]  And just, it was, it was cool.
[4106.90 --> 4108.64]  It was like a, like a reunion.
[4110.78 --> 4113.00]  It was a reunion after many years.
[4114.08 --> 4120.60]  Next up for me would be discovering discovery coding with Jimmy Miller, episode 80 of friends.
[4121.16 --> 4125.92]  And this is Jimmy Miller's return to the show after an excellent episode last year, I think
[4125.92 --> 4128.52]  was in both of our list was the best worst code base.
[4129.06 --> 4132.78]  We had him back on this year talking about his new blog post about discovery coding.
[4133.84 --> 4138.22]  And I just love that even this summary here, fire up a REPL, grab your favorite Stephen King
[4138.22 --> 4140.00]  novel and hold onto the seat of your pants.
[4140.16 --> 4144.20]  Jimmy Miller returns to reveal why, at least for some of us, discovery coding is where it's
[4144.20 --> 4144.50]  at.
[4145.16 --> 4146.12]  And I'm just like, you know what?
[4146.12 --> 4147.46]  I hear that description.
[4147.64 --> 4149.50]  I'm like, I want to go, I want to go to there.
[4149.82 --> 4150.52]  I want to listen to that.
[4151.76 --> 4156.14]  And that was a fun conversation about his process of discovery coding, which I think honestly
[4156.14 --> 4160.36]  is probably different than both what you and I were thinking about and talking about and
[4160.36 --> 4168.30]  relating to because his was kind of very specific, but fascinating that guy and the way he writes
[4168.30 --> 4169.04]  about what he does.
[4169.04 --> 4175.48]  I wonder if there's a mirror of that happening in the vibe code world, like if it's a version
[4175.48 --> 4176.58]  of that, but not really.
[4177.78 --> 4179.86]  Like we're all doing discovery coding all the time.
[4180.28 --> 4188.10]  Well, like I think that, yeah, because like there's, there's like when I putter, I call
[4188.10 --> 4188.48]  it puttering.
[4189.58 --> 4189.90]  Okay.
[4189.92 --> 4191.16]  I don't have a target.
[4191.32 --> 4193.26]  I guess, you know, it is discovery coding.
[4193.98 --> 4195.34]  I don't even know what I'm going to pick up.
[4195.38 --> 4198.06]  I'm just going to play with something like today, for example, like the end of our meeting,
[4198.06 --> 4202.62]  I'm like, I wonder if Safari has an API where you can easily pull back all the tabs, the
[4202.62 --> 4205.12]  URLs and I'm in the page titles and turn that into a markdown list.
[4205.66 --> 4210.34]  And moments later we had that script written and like, that was a version of like almost
[4210.34 --> 4214.54]  discovery coding where it's like, I wonder what, I have no purpose here to like write
[4214.54 --> 4214.96]  code.
[4215.22 --> 4220.88]  Obviously I didn't write the code either, but the idea is like, can I, can I automate what
[4220.88 --> 4226.48]  would be a 10 minute task to take all the tabs that opened up, but it was like 50 tabs
[4226.48 --> 4230.78]  of these shows and probably about 30 and make a list.
[4230.92 --> 4231.66]  Why would I do that?
[4231.86 --> 4236.36]  You know, why can't I just query the Safari API and get that list?
[4236.78 --> 4237.10]  Yeah.
[4237.44 --> 4237.76]  I don't know.
[4238.98 --> 4240.72]  It's like, it's like discovery coding in a way.
[4240.82 --> 4241.04]  Yeah.
[4241.12 --> 4241.72]  To a certain extent.
[4242.10 --> 4242.32]  Yeah.
[4242.80 --> 4246.40]  I'm certainly doing way more than that, way more of that than I ever have.
[4246.72 --> 4247.12]  Yeah.
[4247.12 --> 4251.68]  Because I don't have to, I don't have to go through the toil of finding the answer.
[4251.68 --> 4258.92]  I can go do the emails or whatever I'm up to and let the computer do the toiling as I
[4258.92 --> 4259.54]  do the discovering.
[4259.84 --> 4260.98]  And I think that's really fun.
[4261.18 --> 4263.66]  And probably a lot of what both of us are doing with these things.
[4266.10 --> 4266.64]  All right.
[4266.66 --> 4267.64]  What's next on your list?
[4268.18 --> 4269.30]  Let's see here.
[4270.16 --> 4271.46]  I have a long list.
[4271.94 --> 4272.66]  Let me see.
[4272.66 --> 4283.86]  One, two, three, four, five, six, seven in my faves and one, two, three, four, five,
[4284.00 --> 4285.92]  six in my must listen list.
[4286.44 --> 4287.68]  Two distinct lists.
[4288.00 --> 4288.66]  Those are the same.
[4288.76 --> 4293.14]  Kind of all favorites, but you know, I'm just cheating here because I, because I want to,
[4293.50 --> 4296.70]  you know, honestly, I want to say, I won't say them all.
[4296.70 --> 4303.82]  I'll spare everybody my, my verbosity, but I would say line number 14 here in this markdown
[4303.82 --> 4307.72]  file is inside Oxide with Brian Cantrell and Steve Tuck.
[4308.18 --> 4319.02]  Very special moment to be on stage with them recording in the IRL as part of Oxcon 25, 2025,
[4319.34 --> 4320.76]  which is their internal conference.
[4320.76 --> 4323.28]  It's not really promoted or published much.
[4323.72 --> 4327.42]  If you are in the know with Oxide and what they're doing, then you probably know about
[4327.42 --> 4327.82]  Oxcon.
[4327.90 --> 4330.24]  It's their once per year annual internal conference.
[4331.14 --> 4333.00]  And this year they had some big news this year internally.
[4333.20 --> 4336.96]  We can't share that news because we're on our NDA, but if you were there, wow.
[4337.16 --> 4338.72]  I mean, there's some cool stuff happening there.
[4339.64 --> 4341.42]  And we've said crossing the chasm.
[4341.98 --> 4342.38]  Yeah.
[4342.40 --> 4344.42]  I'd say it's probably safe to say they've crossed the chasm.
[4344.64 --> 4346.02]  Honestly, they're not crossing.
[4346.14 --> 4346.66]  They've crossed it.
[4346.66 --> 4353.16]  And just to be there with, you know, I would say internet legends, you know, like, wow,
[4353.30 --> 4361.12]  dude, I mean, such a fan of, of Brian and Steve, but then also to be in their headquarters
[4361.12 --> 4369.50]  office on their stage podcasting about how they do materials, which is a crucial, uh, like
[4369.50 --> 4374.92]  it is the, the beginning of the DNA of their DNA for Oxide.
[4374.92 --> 4376.44]  It's how they hire.
[4376.84 --> 4378.82]  It's how they choose who to let in.
[4379.18 --> 4383.84]  And this process is so critical to their culture.
[4384.32 --> 4387.26]  And we got to just jam with them on their stage.
[4387.28 --> 4389.04]  And that was, that was dope.
[4389.54 --> 4390.66]  As far as dope as you can get, man.
[4391.08 --> 4391.20]  Yeah.
[4391.52 --> 4392.96]  Well, that one's on my list as well.
[4393.06 --> 4396.90]  So we, uh, we teamed up on that one and I agree with you.
[4396.96 --> 4398.42]  That was awesome.
[4398.42 --> 4405.62]  I thought it turned out really well and, uh, it was quite an honor, you know, it's like
[4405.62 --> 4408.14]  we were their special guests and it's like, why?
[4408.26 --> 4411.52]  I don't, I'm not sure why, but here we are anyways, let's act like we belong here.
[4411.56 --> 4413.92]  You know, imposter syndrome, go, go, go.
[4413.92 --> 4416.50]  And it was lots of fun.
[4416.62 --> 4421.66]  Speaking of live on stage, let me bring up the other live show that we did.
[4421.78 --> 4426.54]  Now we did have Nabeel mentioning Kaizen Pipely is live.
[4427.06 --> 4428.48]  That was friends 105.
[4428.86 --> 4430.52]  And of course we did that one live on stage.
[4430.58 --> 4433.30]  We also had Andrew mentioning that as well.
[4433.58 --> 4436.36]  The one that wasn't mentioned was the interview show that we did.
[4436.36 --> 4441.58]  And so I wanted to give a shout out to that one live from Denver, live from Denver with
[4441.58 --> 4447.70]  Nora Jones interviews, 653, you and I, Nora Jones on stage.
[4448.46 --> 4450.56]  Is it the best interview we've ever done in our lives?
[4450.64 --> 4451.28]  Probably not.
[4451.58 --> 4454.26]  You know, uh, could, could it have gone better?
[4454.40 --> 4454.78]  Yeah, sure.
[4454.82 --> 4455.56]  Of course it could have.
[4456.20 --> 4462.86]  Was it still a cool thing that I'm glad happened and that all in all turned out pretty well.
[4462.86 --> 4465.86]  And I'm super thankful that Nora showed up for us in big ways.
[4466.36 --> 4466.66]  Yes.
[4466.88 --> 4471.42]  And so it definitely a highlight for me was that particular episode, which is the other
[4471.42 --> 4475.36]  half of the show, which has already been previously mentioned as people's favorites.
[4476.36 --> 4476.38]  Yeah.
[4476.88 --> 4478.18]  Well, that's on my list too, man.
[4478.56 --> 4478.80]  Nice.
[4479.00 --> 4479.58]  The Nora Jones episode.
[4479.72 --> 4484.82]  I mean, like it's, uh, yeah, I mean, the IRL stuff is, is fun, obviously.
[4485.02 --> 4489.94]  I mean, I love humans and, um, I'm a non-transactional person.
[4489.94 --> 4495.70]  If you know me in the reels, which I think you kind of proverbially you all listening,
[4495.86 --> 4500.94]  know me through the airwaves and the video waves to some degree, uh, you get a pretty
[4500.94 --> 4504.24]  good snapshot of who I am and you know, who I am here is who I am in person.
[4504.24 --> 4505.36]  Like I'm not a different person.
[4505.42 --> 4506.20]  This isn't an act.
[4506.78 --> 4507.86]  I can't act that good.
[4507.90 --> 4509.28]  You know, it's just, it's just who I am.
[4509.28 --> 4511.32]  You know, I'm a lover, not a fighter.
[4511.90 --> 4514.48]  I'll walk away from a fight before I stand there and fight around.
[4515.22 --> 4518.02]  And I just love to go deep with people and I love to serve people.
[4518.16 --> 4524.32]  And I love just to, just to really relate and have relationship, not transaction and
[4524.32 --> 4525.04]  by Sia.
[4525.34 --> 4529.22]  So being able to be there with Nora and she accepted and she was from Denver and could
[4529.22 --> 4529.84]  easily do it.
[4529.86 --> 4531.82]  And it was just like, yeah, that was cool.
[4531.82 --> 4536.90]  And to do it on stage in front of a listening audience was, was cool.
[4537.68 --> 4540.56]  Uh, we got the, the stage lighting set really well.
[4540.64 --> 4541.60]  Some orange and teal.
[4541.66 --> 4544.40]  I think it was, it all worked out well.
[4544.40 --> 4545.98]  And that was a, I agree with you.
[4545.98 --> 4547.12]  It wasn't our best interview.
[4548.20 --> 4549.90]  Uh, what could have made it better though?
[4549.96 --> 4552.16]  I think what could have made it better was just like better monitoring.
[4552.16 --> 4553.48]  Like for me, it was technical.
[4554.40 --> 4554.50]  Yeah.
[4554.92 --> 4556.40]  Because it wasn't the actual content.
[4556.62 --> 4559.70]  It was the execution of the process.
[4559.70 --> 4564.10]  And a lot of my little jabs that I do throughout the interviews, you know, just like random
[4564.10 --> 4569.80]  one-off comments that are there to go, have a moment of levity and, and, and whatever.
[4570.44 --> 4571.62]  She just couldn't hear them.
[4571.62 --> 4575.44]  And so like the crowd even kind of laughed a little bit, you and I chuckled and then
[4575.44 --> 4576.10]  she's like, what?
[4576.20 --> 4580.96]  And I'm like, uh, it doesn't even, it's not worth, it's not worth even saying again.
[4580.96 --> 4583.28]  Like I'm going to feel like an idiot having to say this back.
[4583.32 --> 4584.74]  I shouldn't have said it the first time, you know?
[4585.20 --> 4585.52]  Right.
[4585.54 --> 4588.20]  Like those little things could have been better, but you know, whatever, whatever.
[4588.82 --> 4589.14]  Yeah.
[4589.14 --> 4590.46]  A lot of good stuff there, man.
[4591.96 --> 4592.80]  Is it me again?
[4593.52 --> 4594.26]  Yes, it is.
[4595.64 --> 4596.00]  Okay.
[4596.72 --> 4600.76]  Let me look at my list here and see which ones of the ones I've selected that I will share.
[4602.44 --> 4606.98]  I'm going to say two more and, uh, I'm going to say the best for last, I think.
[4606.98 --> 4616.72]  And I'd say Charlie Marsh, Astral, UV, what they're doing for Python with Rust is super, super cool.
[4616.72 --> 4631.96]  I've been looking at the design even of the UV library in terms of like the organization of all the, the workspaces inside of the way that Rust composed itself in a, in a directory structure.
[4631.96 --> 4632.96]  So cool.
[4632.96 --> 4639.44]  I mean, just really, I mean, they have different teams doing different crates and just like the autonomy, each one of them.
[4639.94 --> 4643.08]  It's just such a really very verbose design.
[4643.08 --> 4649.56]  I think he even commented on that, but just, uh, what they've done for Python on the speed front.
[4649.68 --> 4650.44]  I'm a UV user.
[4650.44 --> 4659.00]  So whenever I install or mess with Python, which isn't too frequently, I'm reaching for UV over pip, uh, for those reasons.
[4659.00 --> 4659.84]  It's just fast.
[4660.20 --> 4663.60]  A lot of things to learn and they're actually making a business around it.
[4663.60 --> 4666.50]  Like it's not just dev tooling for dev tooling sake.
[4666.56 --> 4667.90]  They've built a business around it.
[4667.94 --> 4668.70]  They got a registry.
[4669.46 --> 4671.04]  Uh, they're doing even more stuff.
[4671.08 --> 4672.40]  It's, it's really cool.
[4672.80 --> 4673.34]  It's admirable.
[4673.76 --> 4674.60]  Heck yeah, man.
[4674.78 --> 4675.86]  I'm a fan as well.
[4676.10 --> 4679.00]  I do think that was a good one.
[4679.00 --> 4684.36]  I want to give a specific shout out to a specific pound to find game.
[4684.46 --> 4685.72]  Now we play a lot of these games.
[4685.84 --> 4692.52]  We've had our listeners mentioned them as a group, but if we were to just to name one from this year, there's been three pound to fines this year.
[4692.74 --> 4695.50]  One back in May and then July.
[4695.68 --> 4700.62]  And then most recently, of course, we had our tournament of champions in November.
[4701.88 --> 4708.98]  But if I had to pick one that just cracked me up and had a blast, I would say it was the one back in the game.
[4709.00 --> 4709.68]  Back in May.
[4710.18 --> 4710.80]  Pound to fine.
[4710.92 --> 4711.80]  I'm going pants.
[4713.00 --> 4714.24]  With Angelica Hill.
[4714.46 --> 4715.36]  Matthew Sanabria.
[4715.74 --> 4716.58]  John Henry Moeller.
[4717.36 --> 4718.06]  You and I, of course.
[4718.20 --> 4720.86]  And the mysterious Rape Master Cylinder himself.
[4720.86 --> 4730.68]  For a hilarious and crazy game of a pound to fine that had me laughing out loud as I listened back later.
[4731.52 --> 4738.78]  And so if you haven't listened to our game shows and you're wondering, you know, how do I dip my toe in those waters?
[4738.78 --> 4740.78]  I would suggest ChangeLoginFriends93.
[4742.34 --> 4743.10]  Pound to fine.
[4743.24 --> 4744.64]  I'm going pants.
[4745.32 --> 4746.78]  Because that is a good one.
[4747.68 --> 4748.80]  What would that come from?
[4748.86 --> 4750.38]  What did the pants reference come from?
[4750.46 --> 4751.00]  Remind me.
[4751.54 --> 4752.38]  It was.
[4753.34 --> 4760.84]  I think it was either BMC or John who would select pants as the, was it the autocomplete?
[4761.04 --> 4761.26]  I don't know.
[4761.30 --> 4762.38]  It was an answer to a question.
[4764.44 --> 4766.14]  And I was like trying to get them to lock in.
[4766.26 --> 4767.12]  And they're like, pants?
[4767.18 --> 4768.90]  I think it was BMC because that's just how he talks.
[4768.96 --> 4769.56]  He's like, pants?
[4769.58 --> 4770.26]  And I'm like, are you sure?
[4770.28 --> 4771.32]  He's like, I'm going pants.
[4771.90 --> 4772.82]  It was that.
[4772.92 --> 4773.10]  Yeah.
[4773.10 --> 4773.38]  Yeah.
[4773.54 --> 4774.52]  I'm in the transcript now.
[4774.66 --> 4775.14]  Spelunking.
[4775.78 --> 4776.38]  Okay, cool.
[4776.64 --> 4776.78]  Yeah.
[4777.20 --> 4777.86]  Yeah, it was.
[4777.90 --> 4779.10]  It was actually one of the references.
[4779.34 --> 4782.56]  I think you said, number three, comfortable pants for remote working.
[4782.92 --> 4784.62]  I guess it was an option to select.
[4784.84 --> 4785.48]  Yeah, exactly.
[4785.56 --> 4786.76]  And he's like, I'm going pants.
[4787.84 --> 4788.36]  Oh, yeah.
[4788.40 --> 4790.02]  And then I laughed and I said, I love your conviction.
[4790.12 --> 4790.86]  He's going pants.
[4790.92 --> 4791.34]  All right.
[4791.50 --> 4792.74]  So that just became the show title.
[4792.74 --> 4797.14]  Those are hard ones to name because how do you name a game show without being boring?
[4797.42 --> 4800.94]  And so I just named the game and I just picked some sort of sentence that somebody said.
[4800.94 --> 4805.54]  But, of course, props to Astronomer was also a good addition.
[4805.70 --> 4807.54]  That was with Changelog++ members.
[4808.72 --> 4811.86]  And, of course, the last one went crazy.
[4812.56 --> 4813.42]  Sheer resistance.
[4813.74 --> 4817.50]  Probably the most conservatively played game of Pound to find.
[4818.64 --> 4819.72]  A lot of piling on.
[4819.76 --> 4821.24]  We're going to have to change the rules a little bit.
[4821.24 --> 4823.16]  Just stop the pylons all the time.
[4823.24 --> 4824.86]  You guys all picking the same answers, man.
[4825.30 --> 4826.42]  That's the easy button, you know?
[4826.78 --> 4827.94]  When in doubt, pile on.
[4828.66 --> 4829.30]  That's right.
[4829.30 --> 4831.54]  That's the closest I got to winning, too.
[4831.76 --> 4831.96]  Didn't I?
[4831.96 --> 4832.44]  That's true.
[4832.84 --> 4835.82]  Didn't I win in the – I won in plus-plus somewhere, too.
[4835.90 --> 4836.74]  One of the eights, I think.
[4837.82 --> 4838.74]  Yeah, I still haven't won yet.
[4838.74 --> 4840.24]  You won in the after show.
[4840.74 --> 4843.14]  And I didn't even play my trump card here on this one, either.
[4843.18 --> 4846.66]  I had the access to an LLM and I forgot to do it.
[4846.70 --> 4851.34]  The game ended before I can like – I was like, when can I play my triple word score?
[4851.44 --> 4851.88]  Come on.
[4852.08 --> 4852.44]  Right.
[4852.68 --> 4853.58]  That's when they didn't.
[4853.58 --> 4857.26]  That's when they like have the coach coming in pitch for you, you know?
[4857.46 --> 4858.20]  Coach has to pitch.
[4858.48 --> 4861.24]  And then you just stare at – you just stare down a strike and he strikes you out.
[4861.32 --> 4862.38]  You get struck out by the coach.
[4862.48 --> 4863.06]  That's what that is.
[4863.76 --> 4866.88]  Yeah, and I missed my – I missed my spot there on that one.
[4867.16 --> 4867.86]  Yeah, I agree.
[4867.94 --> 4871.40]  Those are fun, unique styled shows.
[4871.52 --> 4872.62]  Not your typical podcast.
[4872.90 --> 4874.12]  We had an idea for a while.
[4874.20 --> 4877.58]  Then we always like coding shows or coding –
[4877.58 --> 4878.30]  Dev game shows.
[4878.30 --> 4883.82]  It was dev game shows, but like a long time ago it was like code games, I believe.
[4883.96 --> 4884.36]  Code games.
[4884.50 --> 4885.88]  It was the original kind of idea.
[4886.06 --> 4887.08]  And I think it was in Slack.
[4887.60 --> 4888.28]  We did something.
[4888.28 --> 4888.92]  We were trying to do something in Slack.
[4889.04 --> 4891.94]  And I think you did it for a little bit and it just like didn't really catch on.
[4892.38 --> 4892.76]  Right.
[4892.84 --> 4898.50]  So like there's been iterations to maybe where we're at from just the idea of like playing games together.
[4898.94 --> 4899.30]  Right.
[4899.98 --> 4901.14]  So that's cool.
[4902.38 --> 4902.58]  Yeah.
[4902.94 --> 4903.60]  All right, your turn.
[4905.20 --> 4907.78]  Is this – how many more should I do?
[4907.78 --> 4909.52]  Like how much more time should we spend doing this?
[4909.64 --> 4909.66]  I don't know, man.
[4909.66 --> 4912.20]  I can probably throw one more out there or two more at least.
[4912.40 --> 4913.08]  Let's go one.
[4913.18 --> 4914.20]  Let's go one more each.
[4914.52 --> 4914.98]  You can do two.
[4915.08 --> 4915.56]  I'll do one.
[4916.50 --> 4919.58]  I would say – well, I wanted to make this one the last one, but I'm not going to do it.
[4920.14 --> 4920.86]  Werner, man.
[4920.94 --> 4924.96]  Talking to the CTO of Amazon, Werner Vogels, on the pod, that's recent.
[4925.08 --> 4926.00]  That's recency bias.
[4926.22 --> 4926.88]  That is recent.
[4927.30 --> 4932.58]  Just really interesting to talk to a legend like that on a podcast and to go through predictions
[4932.58 --> 4937.58]  and to just talk about things that isn't like, so how does Amazon work?
[4937.88 --> 4939.70]  Or how does AWS work?
[4939.82 --> 4943.98]  I mean that would be kind of cool too, but at the same time, you get to zoom out and get theory.
[4944.20 --> 4948.22]  I'd rather get theory from that level of a thinker than prescription.
[4948.86 --> 4950.00]  Like here's what you go to do.
[4950.24 --> 4951.20]  A plus B gets C.
[4951.44 --> 4953.98]  I feel like theory, big picture, how he thinks.
[4954.86 --> 4956.98]  I got a snapshot of this legend.
[4957.74 --> 4961.68]  And I don't want to call him an old guy necessarily, but he's obviously – I'm old too.
[4962.06 --> 4963.46]  But he's older than I am.
[4963.70 --> 4964.02]  Right.
[4964.44 --> 4968.52]  I just mean it like you get to sit down with like an internet legend and kind of a grandpa
[4968.52 --> 4971.42]  to software developers and to platform makers.
[4971.42 --> 4977.46]  There's a visionary, a thinker, a discoverer like he built it on his laptop.
[4977.46 --> 4982.36]  Like to me, that's like, wow, you get to talk to somebody who's made a dent in the world that big?
[4983.30 --> 4984.18]  That's cool, man.
[4984.22 --> 4987.16]  I'm like – I kind of like got goosebumps now just thinking about it.
[4987.26 --> 4987.42]  You know?
[4987.70 --> 4987.98]  It's cool.
[4988.12 --> 4988.20]  Yeah.
[4988.20 --> 4989.48]  I agree.
[4989.76 --> 4995.68]  And I'm also going to go recent because I had so much fun learning about Zipline, man.
[4995.74 --> 5003.58]  I felt like cool guest, cool company, cool combo of questions from us.
[5003.66 --> 5004.94]  There's a good balance to that show.
[5005.40 --> 5006.58]  I feel like we all hit it off.
[5006.82 --> 5013.46]  And I honestly just think that it's a seriously cool technology that is right on the – it's
[5013.46 --> 5016.94]  before it changes the world in good ways, but I think it's going to.
[5016.94 --> 5023.42]  And yeah, there'll be unintended consequences as there are with all new tech, but I just
[5023.42 --> 5027.98]  think it's – I still just can't wait for Zipline to be in Omaha because I want to order
[5027.98 --> 5031.72]  a Chipotle burrito and have it delivered to my house while it's still too hot and it's
[5031.72 --> 5032.34]  going to burn my mouth.
[5032.62 --> 5035.10]  I want to just come down out of the sky.
[5036.20 --> 5043.12]  I think that's just a magical thing, and I think it's going to just be a cool piece of
[5043.12 --> 5044.04]  our lives here in the future.
[5044.04 --> 5047.64]  And I like to be able to learn about it before it's out there.
[5048.76 --> 5051.02]  Much bigger and smaller than I expected.
[5051.98 --> 5052.10]  Yeah.
[5052.60 --> 5054.04]  Hundreds of drones.
[5054.60 --> 5055.66]  400, I think he said.
[5055.84 --> 5057.22]  Yeah, which was less than I thought he was going to say.
[5057.24 --> 5060.28]  Yeah, I thought it was going to be like a serious fleet.
[5060.66 --> 5060.88]  Same.
[5060.88 --> 5065.58]  That's still a serious fleet, but here in Texas, from what I can tell, Dallas-Fort Worth area
[5065.58 --> 5066.42]  makes sense.
[5067.32 --> 5068.04]  Texas is big.
[5068.16 --> 5071.32]  Dallas is one of the top cities in Texas.
[5071.32 --> 5075.04]  Yeah, it makes total sense, and the weather is amenable to it.
[5075.28 --> 5075.90]  I think that's the reason.
[5076.34 --> 5076.48]  Yeah.
[5076.48 --> 5076.66]  Yeah.
[5076.96 --> 5079.86]  It does get colder there than it does, I guess.
[5079.90 --> 5083.06]  I used to live in Houston, and now I live in Austin, and so I guess it gets a little
[5083.06 --> 5084.70]  colder here than it does in Houston.
[5084.70 --> 5089.54]  But I had been in Texas for a decade, and I'm like, it gets cold here.
[5089.66 --> 5091.22]  It gets briefly cold in Houston.
[5091.76 --> 5094.16]  But not like cold is going to take your drone out of the sky cold.
[5094.30 --> 5094.70]  Right.
[5094.90 --> 5095.18]  Right.
[5095.30 --> 5100.32]  So I just, you know, Dallas still gets enough chill that you can actually maybe get the
[5100.32 --> 5104.74]  inclement weather testing ability, but you also get the extreme heat.
[5104.86 --> 5106.42]  So you kind of get a little bit of both, really.
[5106.42 --> 5113.18]  You get a brief moment of extreme cold, maybe brief there is like a month, maybe a couple
[5113.18 --> 5113.64]  of weeks.
[5114.44 --> 5116.78]  It's cold still yet, but not like super, super cold.
[5116.90 --> 5120.36]  And then obviously, Texas, gosh, do not come here in July or August, please.
[5121.00 --> 5122.62]  If you got somewhere else to be, go there.
[5122.72 --> 5123.38]  Don't come here.
[5124.64 --> 5125.26]  No doubt.
[5125.90 --> 5126.26]  Yeah.
[5126.56 --> 5127.28]  What a shame.
[5127.60 --> 5127.88]  Anyways.
[5128.36 --> 5128.52]  All right.
[5128.54 --> 5128.90]  Back to you.
[5129.08 --> 5129.78]  That's Texas for you.
[5130.02 --> 5130.32]  Okay.
[5130.88 --> 5133.76]  Less ceremonious, but still quite fun.
[5133.76 --> 5139.44]  And bringing it back to home lab state of the home lab tech 2025.
[5140.06 --> 5140.52]  Techno Tim.
[5140.88 --> 5141.70]  Techno Tim.
[5142.54 --> 5144.46]  That was the only part I did with him this year.
[5144.86 --> 5146.16]  Kind of bummed about that.
[5146.76 --> 5148.84]  I like to just circle back with him.
[5148.92 --> 5155.00]  I think instead I opted for Alex, not necessarily as a either or, but just more just timing kind
[5155.00 --> 5155.32]  of thing.
[5156.00 --> 5157.64]  And I'm a fan of Tim.
[5157.74 --> 5158.40]  I love his channel.
[5158.40 --> 5159.72]  I love his exploration.
[5160.48 --> 5161.96]  He's always got something cool to share.
[5162.04 --> 5162.96]  He's a big thinker.
[5162.96 --> 5164.20]  He's a cool dude.
[5164.36 --> 5165.66]  He's a, he's a fun friend.
[5166.26 --> 5171.48]  And I just get energized around him because he's, he's always got something, you know,
[5171.48 --> 5174.94]  he's got something to say about something and he's got some opinion about something.
[5175.06 --> 5177.28]  He's, he's really into the community.
[5177.58 --> 5182.20]  You know, he's, he's doing a lot of cool stuff and he's a software developer still on
[5182.20 --> 5182.62]  the daily.
[5182.76 --> 5186.90]  I think he kind of does a little bit of both where he's not a full-time content creator.
[5186.90 --> 5190.64]  He's got a side job or a day job.
[5190.64 --> 5195.48]  And then also his, his, his platform he's built out techno Tim.
[5196.28 --> 5200.66]  I think he's more in that than he is in his day job though, but I like his, his perspective
[5200.66 --> 5201.12]  on things.
[5201.12 --> 5201.90]  And so I miss him.
[5201.90 --> 5206.46]  I had fun talking to him earlier this year and maybe we'll do that sometime in January.
[5206.62 --> 5209.08]  Get that beginning of the year.
[5209.22 --> 5211.16]  Like what's going to happen in the home lab this year.
[5211.46 --> 5211.96]  That'd be cool.
[5212.46 --> 5212.86]  There you go.
[5214.18 --> 5214.90]  All right.
[5215.00 --> 5215.84]  Do we do best titles?
[5215.96 --> 5217.02]  Do we wrap with best titles?
[5218.46 --> 5220.04]  Uh, yeah, let's, let's wrap.
[5220.48 --> 5220.78]  All right.
[5220.86 --> 5221.08]  Best titles.
[5221.08 --> 5225.18]  So we already mentioned adventures and babysitting coding agents.
[5225.34 --> 5225.72]  Yeah.
[5226.54 --> 5227.42]  Both love that one.
[5227.68 --> 5227.88]  Yeah.
[5228.02 --> 5231.30]  Oh, we both liked WSL.exe dash dash cat hello.cs.
[5231.78 --> 5232.24]  Yes.
[5233.08 --> 5239.88]  Um, I really liked over the top off strategies mostly because it directly, it was hard one
[5239.88 --> 5240.30]  to name.
[5240.44 --> 5241.74]  And then we had the reference.
[5241.86 --> 5246.64]  We actually talked with Dan more about all these different OAuth stuff and 2FA and blah,
[5246.66 --> 5247.04]  blah, blah.
[5247.22 --> 5247.80]  And past games.
[5248.48 --> 5250.54]  And then we couldn't name the shows.
[5250.54 --> 5252.16]  It was like, there was all these terrible names.
[5252.30 --> 5253.16]  And then it's like, wait a second.
[5253.22 --> 5259.56]  We talked about over the top, which is the awesome Sylvester Stallone arm wrestling movie
[5259.56 --> 5262.56]  that I don't think Dan had seen or he wasn't aware of it.
[5263.04 --> 5266.86]  And we actually, I can't remember why, but we, I don't even know why it related to the
[5266.86 --> 5268.78]  conversation, but we got it in there on point.
[5269.18 --> 5275.20]  And then, um, over the top at off strats, I want to go over the top off strats, but you
[5275.20 --> 5276.66]  know, I think it was probably too obscure.
[5276.76 --> 5278.04]  Anyways, I thought that was a good one.
[5278.46 --> 5279.50]  What was the actual title again?
[5279.74 --> 5280.12]  Over the top.
[5280.12 --> 5285.02]  Over the top off strategies, which is kind of a little bit less cool, but more approachable.
[5285.02 --> 5286.20]  Like people know what we're talking about.
[5286.66 --> 5286.88]  Yeah.
[5286.92 --> 5287.18]  I don't know.
[5287.24 --> 5288.92]  I would have gone either or on that one now that I know that.
[5289.32 --> 5289.74]  Oh, okay.
[5291.04 --> 5295.54]  Strats would have been maybe one notch above current title.
[5295.80 --> 5297.08]  We can go back and rename it.
[5297.20 --> 5298.06]  It's going to stop us.
[5298.12 --> 5298.56]  It's our show.
[5298.70 --> 5299.08]  That's right.
[5299.14 --> 5300.64]  There's no slug that says that too.
[5300.96 --> 5301.42]  So that's right.
[5301.60 --> 5302.72]  Make it into the URLs.
[5303.12 --> 5303.54]  That's right.
[5303.60 --> 5304.60]  Just episode 78.
[5304.80 --> 5305.42]  So there you go.
[5305.52 --> 5305.74]  Yeah.
[5306.04 --> 5307.00]  ID only, man.
[5307.00 --> 5309.78]  What else do you like title wise?
[5312.78 --> 5314.28]  Man, it's a tough one there.
[5314.78 --> 5315.64]  That's a tough one.
[5315.76 --> 5317.38]  Let me see if I've prepared well enough for this.
[5319.80 --> 5321.70]  I mean, it's got to be a good title, right?
[5321.86 --> 5323.10]  It's got to be a good one.
[5323.10 --> 5324.58]  Isn't that what we're doing?
[5324.66 --> 5325.12]  Good titles.
[5325.22 --> 5325.38]  Yeah.
[5325.48 --> 5325.90]  Good ones.
[5326.22 --> 5327.34]  I thought you had a list of these.
[5327.54 --> 5327.86]  My bad.
[5328.22 --> 5329.42]  I got a list of a lot of them.
[5329.46 --> 5332.56]  I'm just trying to figure out which one is the best title of them.
[5332.62 --> 5333.72]  Oh, well, you don't have to pick the best.
[5333.78 --> 5335.42]  Just pick one you like and we'll do a couple of them.
[5336.16 --> 5337.32]  That's so hard.
[5338.14 --> 5338.94]  How about try harder?
[5339.24 --> 5339.80]  Ultra thing.
[5340.50 --> 5341.32]  That was good.
[5341.56 --> 5342.44]  That was a good one.
[5342.76 --> 5343.32]  That was a good one.
[5343.32 --> 5344.74]  I mean, there's a lot of good titles in here, man.
[5344.74 --> 5348.08]  It's a fun process to name these shows.
[5348.22 --> 5348.78]  Let me see if I can.
[5350.26 --> 5350.72]  I don't know.
[5350.76 --> 5353.84]  I kind of liked, you know, honestly, I liked flowing with agents with beyond.
[5353.84 --> 5355.92]  That was a fun one.
[5355.96 --> 5356.40]  The name.
[5356.54 --> 5357.86]  It's because it's your code flow.
[5358.20 --> 5358.74]  It's your agent flow.
[5358.92 --> 5359.56]  Agent flow.
[5359.76 --> 5360.00]  Yeah.
[5360.36 --> 5360.62]  Yeah.
[5361.56 --> 5362.92]  But that's not the one I'll choose.
[5364.06 --> 5364.88]  Oh, gosh.
[5364.90 --> 5365.42]  Here we go.
[5365.76 --> 5366.14]  Here we go.
[5366.22 --> 5366.94]  Dude, you ready for this one?
[5367.58 --> 5368.20]  You sitting down?
[5368.76 --> 5369.96]  No, you're standing up, aren't you?
[5370.16 --> 5370.38]  Standing up.
[5370.44 --> 5370.58]  Yeah.
[5371.48 --> 5373.36]  Line 44 from my markdown file.
[5374.38 --> 5375.44]  Refactored in prison.
[5376.16 --> 5376.80]  Oh, yeah.
[5377.08 --> 5377.30]  Yeah.
[5377.36 --> 5379.22]  I mean, like, good show.
[5379.78 --> 5381.32]  It didn't make my list.
[5381.32 --> 5385.70]  I, you know, just, it was a good show.
[5385.84 --> 5386.78]  It was a really good show.
[5387.96 --> 5390.26]  But the title, that's a good title, man.
[5390.32 --> 5393.92]  Like, reformed in prison, refactored in prison.
[5394.44 --> 5394.52]  Like.
[5394.88 --> 5395.16]  Yeah.
[5395.34 --> 5397.42]  And then talk to somebody in prison.
[5399.10 --> 5399.46]  Yeah.
[5399.56 --> 5399.76]  Yeah.
[5399.86 --> 5400.16]  Good show.
[5400.36 --> 5401.66]  I could probably come up with better ones.
[5401.72 --> 5405.94]  I probably, it's more of like a sad letdown, best title from Adam.
[5406.18 --> 5407.94]  But so many to choose from.
[5407.96 --> 5409.22]  I can be here all day telling you.
[5409.22 --> 5409.74]  Oh, for sure.
[5409.74 --> 5410.44]  You know this.
[5410.88 --> 5416.98]  One other one I will pick, because it's another movie reference, was the episode with Justin
[5416.98 --> 5418.14]  Searles and Mike McQuaid.
[5418.48 --> 5419.96]  I had a hard time naming that one.
[5420.04 --> 5422.42]  It's about Ruby and drama and it's open source.
[5422.48 --> 5423.34]  It's not a career.
[5424.02 --> 5427.46]  But I already knew that that was kind of Justin's title he was going with, because it was a crossover
[5427.46 --> 5428.66]  episode on both podcasts.
[5430.14 --> 5431.38]  And I couldn't think of anything.
[5431.50 --> 5433.26]  I think I sent you like seven different things.
[5433.32 --> 5434.08]  I can't even remember.
[5434.08 --> 5437.20]  And then finally, I was just like, oh, actually, you know what?
[5437.20 --> 5438.62]  I was talking with Justin about it.
[5438.68 --> 5439.14]  It wasn't you.
[5439.26 --> 5441.36]  It was Justin, because he asked me what I was going to call the episode.
[5441.48 --> 5442.88]  And I had sent him some stuff.
[5443.48 --> 5445.44]  And I just wasn't happy with any of the titles.
[5445.60 --> 5446.74]  And then I thought, you know what?
[5446.80 --> 5451.52]  This is one there where Mike at the beginning said, like, I got to be able to cuss on the
[5451.52 --> 5451.86]  episode.
[5452.08 --> 5453.22]  And I said, you can't cuss.
[5453.30 --> 5454.44]  I mean, you can cuss on our episodes.
[5454.90 --> 5455.20]  Fine.
[5455.20 --> 5456.30]  But you're going to get bleeped.
[5457.02 --> 5459.06]  And that's why he's like, well, let's put it on breaking change.
[5459.12 --> 5460.26]  It'll be unbleeped over there.
[5460.32 --> 5461.40]  It'll be bleeped on the change log.
[5461.50 --> 5465.34]  And so the title, there will be bleeps, I thought was a great.
[5465.44 --> 5466.92]  There will be blood, of course, movie reference.
[5467.20 --> 5467.42]  Yeah.
[5467.54 --> 5468.60]  Also tantalizing.
[5468.72 --> 5472.06]  Like, OK, you're like, I'm not sure what they're talking about, but it's going to get
[5472.06 --> 5472.48]  spicy.
[5473.42 --> 5474.52]  I thought that was a pretty good title.
[5475.32 --> 5477.42]  It saved me from an otherwise terrible title.
[5477.52 --> 5479.14]  I had up like six bad ones before.
[5479.24 --> 5480.16]  And then I thought, you know what?
[5480.74 --> 5481.56]  Let's go a different direction.
[5481.90 --> 5482.30]  Yeah.
[5482.30 --> 5482.46]  Yeah.
[5482.52 --> 5486.80]  Sometimes you have to be a little out there in your thinking.
[5488.26 --> 5490.16]  But spot on just as well.
[5491.12 --> 5491.88]  What a good movie, though.
[5491.90 --> 5492.52]  There will be blood.
[5492.80 --> 5493.46]  Oh, man.
[5493.60 --> 5497.30]  You know, day Lewis, man, the method actor of method actors.
[5497.74 --> 5498.88]  He is so good.
[5499.78 --> 5501.98]  His co-star in there was really good, too.
[5502.44 --> 5502.80]  Yes.
[5503.00 --> 5503.70]  The kid in the end.
[5503.82 --> 5504.64]  He's not a kid anymore.
[5504.68 --> 5506.14]  But at the time he was younger.
[5507.06 --> 5507.74]  Dana something.
[5507.74 --> 5511.32]  I don't know his name off the top of my head, but fantastic actor.
[5512.30 --> 5513.64]  Just a phenomenal movie.
[5513.96 --> 5518.22]  And I think I heard that he got swapped in like two weeks before filming started onto
[5518.22 --> 5519.74]  that off of somebody else.
[5520.46 --> 5522.70]  Fact check me or somebody else can afterwards.
[5522.98 --> 5528.52]  But I heard that, which would be amazing to know that he actually swapped in late because
[5528.52 --> 5531.82]  his performance is top notch.
[5532.30 --> 5532.78]  Spot on.
[5532.84 --> 5532.98]  Yeah.
[5533.12 --> 5534.54]  His name is Paul Danos.
[5534.62 --> 5535.28]  You're pretty close.
[5535.44 --> 5535.82]  Dano.
[5535.90 --> 5536.10]  Yeah.
[5536.10 --> 5537.28]  I was like, what did I say?
[5537.44 --> 5537.78]  Dave?
[5538.04 --> 5538.30]  Dan?
[5538.54 --> 5539.18]  Dano something.
[5539.74 --> 5539.90]  Yeah.
[5540.42 --> 5540.78]  Dana.
[5540.78 --> 5540.90]  Dana.
[5541.00 --> 5541.90]  That was what I was saying.
[5542.54 --> 5543.20]  Paul Dano.
[5543.66 --> 5543.78]  Yeah.
[5544.56 --> 5545.00]  2007.
[5545.80 --> 5546.74]  This movie came out.
[5547.04 --> 5548.32]  So not recent.
[5549.32 --> 5551.04]  Takes place right there in Texas, doesn't it?
[5551.04 --> 5551.88]  I mean, it's all about oil.
[5552.64 --> 5554.06]  You know, I don't know if it's in Texas.
[5554.34 --> 5554.96]  I don't know that either.
[5554.96 --> 5555.38]  It might be.
[5555.48 --> 5557.20]  I assume it is, but it might not be.
[5557.42 --> 5558.88]  I don't know if it's clear what the setting is.
[5560.74 --> 5562.92]  If it's in Texas, it probably is in Texas.
[5563.26 --> 5564.22]  I mean, it's.
[5564.46 --> 5566.08]  Where else would it be when it comes to oil?
[5566.40 --> 5566.64]  You know?
[5567.44 --> 5568.92]  It's like the Wild West oil trade.
[5569.06 --> 5570.02]  It's got to be Texas, right?
[5570.02 --> 5570.32]  Yeah.
[5570.54 --> 5574.80]  What a ruthless silver miner turned oil prospector.
[5575.04 --> 5575.36]  Exactly.
[5575.64 --> 5577.20]  That's the way to open a movie right there, man.
[5578.86 --> 5579.68]  Go watch it.
[5579.74 --> 5580.52]  It's in 4K.
[5580.68 --> 5585.80]  If you've got a theater or if you've got yourself a Plex box, go buy it on Amazon or steal it
[5585.80 --> 5586.44]  if that's what you do.
[5586.56 --> 5587.96]  I don't think you should do it, but you know.
[5587.96 --> 5589.54]  That's your advice?
[5590.24 --> 5593.14]  No, I just heard that a lot of people are bypassing.
[5593.34 --> 5597.84]  Well, it kind of goes to the fact that you can't get physical media anymore, you know?
[5597.84 --> 5601.10]  Oh, and so if you can't get access to the physical media, I mean.
[5601.18 --> 5601.64]  What are you going to do?
[5602.60 --> 5602.92]  Yeah.
[5602.98 --> 5605.58]  I mean, I guess the only option would be to.
[5606.76 --> 5607.60]  Steal it, I guess.
[5607.66 --> 5607.86]  Yeah.
[5607.86 --> 5608.30]  Steal it.
[5609.44 --> 5611.22]  You know, I'm not suggesting you do that, though.
[5611.22 --> 5614.32]  My recommendation is go and buy it.
[5615.24 --> 5618.00]  Take yourself and get yourself Make MKV.
[5618.48 --> 5619.60]  Pop that in there.
[5621.82 --> 5623.64]  And then rip it to your Plex.
[5623.94 --> 5624.64]  And then keep it forever.
[5625.72 --> 5629.56]  And that's what I shall do because that is a, I think I actually own that movie.
[5629.70 --> 5630.72]  I don't own it in 4K, though.
[5630.76 --> 5631.42]  I think it's in HD.
[5631.98 --> 5632.30]  Mm.
[5632.88 --> 5633.24]  Yeah.
[5633.90 --> 5635.82]  Take that out there in the bird pile, you know.
[5636.38 --> 5636.78]  HD.
[5637.04 --> 5637.52]  Good for nothing.
[5637.52 --> 5645.78]  You know, honestly, though, if you watch HD versus 4K HDR back to back, side by side, you'll know what I'm talking about.
[5645.96 --> 5647.42]  The sound is different.
[5647.94 --> 5649.38]  The visuals are different.
[5649.74 --> 5656.46]  And in fact, one of the things I use is a way to gauge if I'll buy the 4K Blu-ray or not.
[5656.46 --> 5661.44]  Is I go to blue, B-L-U-ray.com.
[5661.74 --> 5667.06]  And they do phenomenal reviews for when a film makes it to 4K HDR.
[5667.62 --> 5671.20]  And they'll talk about the picture and the sound and it scores it.
[5671.52 --> 5674.50]  They pull out stills and frames from it.
[5674.70 --> 5675.88]  It's really well done.
[5676.02 --> 5676.68]  Really great site.
[5676.90 --> 5677.34]  Nice.
[5677.34 --> 5686.24]  And it's what I track to know, like, new releases, too, because, like, being as old as we are, there's films back in our day, basically, that are now coming to 4K.
[5686.60 --> 5686.96]  Right.
[5687.44 --> 5692.96]  And one of the ones I just watched recently was Terminator 1.
[5693.04 --> 5693.34]  Mm.
[5693.58 --> 5693.84]  Why?
[5693.84 --> 5698.38]  I mean, like, take a film that was never, I guess, never intended for 4K.
[5698.46 --> 5699.24]  I can't say that, really.
[5699.32 --> 5702.80]  But, like, who knew the future would exist, right, in the past?
[5702.80 --> 5703.62]  That's just how it works.
[5704.24 --> 5708.70]  But this film is funnily CGI.
[5709.08 --> 5709.82]  Like, so bad.
[5710.12 --> 5710.54]  So bad.
[5710.76 --> 5716.10]  And it just screams through CGI even more when it's crystal clear in 4K.
[5716.32 --> 5720.30]  Like, what stuff is CGI when he gets, like, his skin blown off and you can see the metal underneath and stuff?
[5720.40 --> 5720.88]  Oh, yeah.
[5720.96 --> 5722.54]  Like, it's, you can tell it's a puppet.
[5722.84 --> 5723.78]  It's so nasty.
[5723.94 --> 5724.40]  Oh, animatronic.
[5724.40 --> 5725.80]  When he's looking at himself in the mirror.
[5726.20 --> 5726.54]  Right.
[5726.68 --> 5729.46]  Like, on one shot, it's clearly an animatronic.
[5730.08 --> 5732.40]  I mean, just, like, the whole thing is animatronic.
[5732.90 --> 5735.10]  So it's almost better in low res, you know?
[5735.32 --> 5736.82]  Yeah, it kind of ruins it.
[5736.88 --> 5737.52]  It really does.
[5737.64 --> 5744.24]  I mean, if I'm being honest, if you don't like going to an open casket funeral or something like that, man, that's kind of what it is.
[5744.32 --> 5744.60]  Okay?
[5744.90 --> 5746.64]  That ruins the movie in a way for you.
[5746.80 --> 5747.12]  Right.
[5747.12 --> 5747.82]  Don't do that.
[5748.16 --> 5748.78]  Don't do it.
[5749.12 --> 5750.94]  Get the 1080p, you know?
[5751.42 --> 5752.68]  I mean, I guess in that regard.
[5752.68 --> 5753.40]  Get the 720p.
[5753.50 --> 5755.44]  Go back on DVD and just stretch that sucker.
[5755.56 --> 5756.12]  You'll never know.
[5756.44 --> 5757.82]  You know what I thought about doing the, Jared?
[5757.86 --> 5758.50]  It was this, man.
[5758.50 --> 5759.72]  I was like, I'm going to go buy.
[5761.34 --> 5762.06]  I'll reveal.
[5762.40 --> 5763.62]  I'll reveal the deep cut here.
[5764.08 --> 5764.44]  Okay.
[5765.16 --> 5774.52]  I was going to go onto our favorite place called eBay and purchase a VHS player and RCA that to my receiver.
[5774.90 --> 5777.36]  Not optics, nothing like that.
[5777.38 --> 5777.86]  No HDMI.
[5778.54 --> 5778.94]  RCA.
[5779.32 --> 5783.34]  The red, the yellow, and I think the white, I think, brings the audio.
[5783.82 --> 5784.84]  Mono audio.
[5784.84 --> 5785.44]  Audio.
[5786.52 --> 5786.60]  Mm-hmm.
[5786.84 --> 5787.44]  Mm-hmm.
[5787.60 --> 5793.34]  And the film I wanted to get, what was provoking me to do this, was Cutting Edge.
[5794.38 --> 5796.32]  Was that like a skiing movie?
[5797.04 --> 5799.40]  It was a very close, yes.
[5799.48 --> 5800.18]  Snowboarding movie?
[5800.82 --> 5801.78]  Very, very close.
[5801.94 --> 5803.10]  It was ice skating.
[5803.74 --> 5804.18]  Okay.
[5804.64 --> 5805.50]  That makes sense.
[5805.54 --> 5806.70]  With D.B. Sweeney.
[5807.30 --> 5809.24]  That almost sounds like a Will Ferrell comedy.
[5810.46 --> 5811.48]  It, you know what?
[5811.52 --> 5812.60]  I think it inspired.
[5813.34 --> 5814.48]  I think it probably did.
[5814.48 --> 5815.24]  Blades of Glory.
[5815.62 --> 5816.48]  Blades of Glory.
[5816.72 --> 5817.26]  Blades of Glory.
[5817.26 --> 5817.46]  There you go.
[5818.42 --> 5819.38]  I've never heard of that.
[5819.50 --> 5819.60]  What?
[5820.70 --> 5820.94]  Yeah.
[5820.94 --> 5821.24]  Why?
[5821.46 --> 5821.78]  Yeah.
[5821.78 --> 5827.16]  Because my wife and I both loved this film before we knew each other.
[5827.48 --> 5829.46]  It was released in 92.
[5830.48 --> 5839.16]  And so this is one of those, one of those movies that as you learn more and more about your wife over the years, like it took probably 10 years for her to tell me that this was one of her favorite movies.
[5839.16 --> 5840.12]  Oh, this is a rom-com.
[5840.26 --> 5842.56]  I was expecting it to be more of like an 80s chick flick.
[5842.80 --> 5842.82]  Oh, yeah.
[5842.82 --> 5843.36]  But it's a rom-com.
[5843.56 --> 5844.68]  Sports and romance, dude.
[5844.96 --> 5845.32]  Wow.
[5845.44 --> 5846.38]  I mean, you know, it's.
[5846.38 --> 5846.72]  I mean.
[5847.36 --> 5847.96]  Double-edged.
[5848.18 --> 5849.66]  Consider figure-siting sports.
[5849.66 --> 5851.00]  Oh, sorry.
[5851.10 --> 5852.04]  Just offended some people there.
[5853.20 --> 5854.90]  Of course, the guy has a hockey stick.
[5854.96 --> 5856.90]  So he plays hockey and she's a figure skater.
[5857.00 --> 5857.56]  Is that the storyline?
[5857.56 --> 5857.80]  Yeah.
[5858.32 --> 5868.22]  Former Olympic hockey player, Doug Dorsey, played by DB Sweeney, pairs up with stuck-up figure skater, Kate Mosley.
[5869.62 --> 5871.04]  Moria Kelly is her name.
[5871.38 --> 5871.72]  Okay.
[5871.84 --> 5874.74]  And like the way they come together, it's a good love story.
[5874.90 --> 5876.58]  You know, I'm a romantic at heart.
[5877.44 --> 5879.46]  And, but this is the one that was provoking me.
[5879.46 --> 5880.74]  I was like, I haven't done it yet.
[5880.80 --> 5883.14]  So now that I'm seeing this again, I kind of want to do it.
[5883.38 --> 5888.96]  And it's mainly brought on by the letdown that was 4K Terminator.
[5889.26 --> 5890.72]  Like I kind of wish I didn't do that.
[5890.74 --> 5891.58]  You don't want to be letdown by 4K.
[5891.76 --> 5892.04]  Yeah.
[5892.28 --> 5892.60]  Any edge.
[5893.00 --> 5897.38]  Well, I was telling him that I'm like, babe, it would be so cool to have a theater like we have.
[5897.38 --> 5902.60]  120-inch screen, laser 4K projector, super awesome sound system.
[5902.60 --> 5907.92]  And then put a VHS player in there and watch old films from our back in the day.
[5908.96 --> 5910.38]  Old films from 1992.
[5910.74 --> 5911.54]  I'm missing a film.
[5911.86 --> 5913.06]  What's the, now it is.
[5913.12 --> 5913.32]  You're right.
[5913.42 --> 5914.56]  What's the worst that could happen though?
[5914.60 --> 5917.96]  It's not like, you know, the kiss scene they cut to like a mannequin or something.
[5918.06 --> 5919.38]  Like there's no CGI in this thing.
[5919.38 --> 5919.78]  Not in that one.
[5919.92 --> 5920.08]  Yeah.
[5920.14 --> 5920.80]  That one there is.
[5920.84 --> 5921.86]  That one there's going to be fun.
[5921.94 --> 5923.06]  Like I thought for the nostalgia.
[5923.06 --> 5927.18]  Because I know when I watched it originally was probably VHS.
[5927.90 --> 5928.24]  Oh yeah.
[5928.54 --> 5931.58]  So go back to the roots, you know, it wasn't on DVD.
[5932.36 --> 5937.68]  Then you should also go one step further and get one of those auto rewinders so you can rewind all your VHSs, you know?
[5938.02 --> 5938.38]  Oh yeah.
[5938.46 --> 5939.06]  Put it in there.
[5939.34 --> 5940.08]  Be kind.
[5940.32 --> 5940.64]  Rewind.
[5940.84 --> 5941.20]  Be kind.
[5941.26 --> 5941.84]  Rewind, man.
[5941.98 --> 5942.26]  Be kind.
[5942.32 --> 5942.64]  Rewind.
[5942.90 --> 5943.12]  Yeah.
[5943.52 --> 5944.36]  So there you go.
[5944.50 --> 5944.62]  Yeah.
[5944.64 --> 5948.90]  I'd probably skip Terminator in 4K unless you just have to have the nostalgia.
[5949.66 --> 5951.18]  It was laughable though, man.
[5951.18 --> 5954.46]  So I'm going to watch Terminator 2 and I'm hoping it's not a ruin.
[5955.68 --> 5955.94]  Yeah.
[5956.08 --> 5956.90]  I think that one will do better.
[5956.90 --> 5958.18]  Some films though are just amazing.
[5958.38 --> 5959.06]  Like Alien.
[5960.10 --> 5961.26]  The Alien series.
[5961.46 --> 5962.88]  Alien, Aliens.
[5963.48 --> 5964.74]  Those are two distinct movies.
[5964.94 --> 5965.68]  Aliens was second.
[5965.86 --> 5966.62]  Alien was first.
[5966.82 --> 5967.16]  Right.
[5967.94 --> 5971.48]  A rare example of a sequel being better than the original perhaps.
[5971.70 --> 5972.38]  Yeah, for sure.
[5972.50 --> 5974.24]  And like Aliens, there's a lot of talk.
[5974.34 --> 5977.62]  Like don't go and watch it because it's so crystal clear now.
[5977.66 --> 5978.34]  It's so good.
[5978.34 --> 5982.20]  Like it almost ruins the original grunginess of it.
[5982.42 --> 5982.78]  Weird.
[5983.20 --> 5985.34]  But they kind of introduced it in the process.
[5985.34 --> 5987.02]  So it's clear, but it's also grungy.
[5987.74 --> 5988.80]  I think it's good.
[5989.16 --> 5995.16]  You know, personally, that one didn't have a lot of ruin for me, but Terminator was kind
[5995.16 --> 5995.80]  of funny, man.
[5995.94 --> 5996.62]  It was kind of funny.
[5997.44 --> 5997.94]  That's what you get.
[5998.06 --> 5998.90]  Grab it at the end, y'all.
[5999.92 --> 6002.46]  There you have a little bit of movie hour there at the end.
[6003.54 --> 6003.90]  Awesome.
[6003.90 --> 6005.40]  Well, there you have our list.
[6005.50 --> 6008.78]  Check the show notes if you want to click through to any particular episodes.
[6009.06 --> 6013.52]  Otherwise, have a great holiday and New Year's and end of your year.
[6013.64 --> 6015.10]  And we'll see y'all on the other side.
[6015.62 --> 6015.90]  You know what?
[6015.94 --> 6016.60]  Actually, one more.
[6016.80 --> 6017.70]  I'll throw one more thing at the end.
[6017.94 --> 6018.74]  I think you'll like this.
[6019.24 --> 6024.76]  There was a mention in Zulip to talk about the longest running Zulip thread from an episode.
[6024.76 --> 6029.02]  And I think we should have the folks listen to this.
[6029.14 --> 6031.82]  Like, if you didn't get a voicemail in, you can still get your word in edgewise.
[6032.42 --> 6032.98]  Go to Zulip.
[6033.78 --> 6035.06]  Changeworld.com slash community.
[6035.56 --> 6036.38]  Hang out with us there.
[6036.82 --> 6038.16]  Comment on this episode.
[6038.32 --> 6039.10]  Some of your favorites.
[6039.94 --> 6040.74]  Share a conversation.
[6041.04 --> 6046.28]  If you've got some downtime during this holiday, maybe throw some notes in there and hop in
[6046.28 --> 6050.78]  on this episode in Zulip and comment on your favorite episodes if you want to chime in.
[6051.60 --> 6053.56]  Or your favorite 90s era rom-coms.
[6053.56 --> 6055.44]  Or your cutting edge.
[6055.52 --> 6056.62]  Whatever your cutting edge is.
[6056.86 --> 6057.14]  Share it.
[6057.14 --> 6058.48]  Yeah, what's the cutting edge to you?
[6058.76 --> 6059.56]  That's a great question.
[6060.60 --> 6061.08]  All right.
[6061.18 --> 6061.68]  Bye, friends.
[6061.92 --> 6062.32]  Bye, friends.
[6065.22 --> 6066.00]  All right.
[6066.10 --> 6066.94]  That's it.
[6067.60 --> 6069.54]  2025 is in the bag.
[6069.78 --> 6070.54]  Can you believe it?
[6070.92 --> 6076.20]  If you have ideas, requests, or anything at all, you'd like to say hop in our Zulip and
[6076.20 --> 6078.58]  sound off on the discussion thread for this episode.
[6078.74 --> 6079.64]  We love hearing from you.
[6079.84 --> 6082.38]  Thank you one last time for listening to our shows this year.
[6082.38 --> 6086.12]  We literally wouldn't be able to keep putting out new stuff if y'all weren't listening.
[6086.34 --> 6086.88]  So thank you.
[6087.18 --> 6091.42]  And a huge thanks to everyone on our team and in the changelog community for everything you do.
[6091.80 --> 6094.48]  You know who you are, but I will name a few names.
[6094.84 --> 6096.22]  Breakmaster Cylinder, of course.
[6096.50 --> 6097.54]  Our editor, Jason.
[6097.82 --> 6099.30]  Alexander on transcripts.
[6099.46 --> 6100.74]  Gerhard Lazu, of course.
[6100.96 --> 6103.96]  And our friends and family who support everything we do.
[6104.24 --> 6104.84]  Y'all are awesome.
[6104.84 --> 6110.02]  Thank you to our partners at Fly.io and to our sponsors of this episode.
[6110.36 --> 6117.34]  Check them out at depot.dev, augmentcode.com, and framer.com slash design.
[6118.06 --> 6122.66]  That's all for now, but let's get back together and talk a lot more next year.
[6122.66 --> 6142.82]  Game live!
[6142.82 --> 6172.80]  Thank you.
