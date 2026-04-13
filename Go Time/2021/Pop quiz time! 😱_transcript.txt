[0.00 --> 4.28]  Sometimes when you start a new language, you bring your preconception from the language you're coming in.
[4.36 --> 6.82]  When I started with Go, I wrote a lot of Python in Go.
[6.94 --> 8.78]  And it worked, it compiled, but it wasn't Go.
[9.02 --> 14.48]  I think these quizzes also help you break these misconceptions or preconceptions and say, no, we do it differently here.
[16.88 --> 19.50]  Big thanks to our partners, Linode, Fastly, and LaunchDarkly.
[19.86 --> 21.92]  We love Linode. They keep it fast and simple.
[22.04 --> 24.40]  Check them out at linode.com slash changelog.
[24.64 --> 26.70]  Our bandwidth is provided by Fastly.
[27.04 --> 28.38]  Learn more at fastly.com.
[28.38 --> 30.60]  And get your feature flags powered by LaunchDarkly.
[30.86 --> 32.58]  Get a demo at LaunchDarkly.com.
[33.34 --> 42.32]  This episode is brought to you by our friends at Cockroach Labs, the makers of CockroachDB, the most highly evolved database on the planet.
[42.74 --> 47.42]  With CockroachDB, you can scale fast, survive anything, and thrive everywhere.
[48.02 --> 53.98]  It's open source, Postgres wire compatible, and Kubernetes friendly, which means you can launch and run it anywhere.
[53.98 --> 60.42]  For those who need more, you can build and scale fast with Cockroach Cloud, which is CockroachDB hosted as a service.
[60.68 --> 65.86]  It's the simplest way to deploy CockroachDB and is available instantly on AWS and Google Cloud.
[66.24 --> 74.44]  With Cockroach Cloud, a team of world-class SREs maintains and manages your database infrastructure so you can focus less on ops and more on code.
[74.82 --> 78.22]  Get started for free with a 30-day free trial or try their new forever free tier.
[78.36 --> 79.30]  That's super generous.
[79.30 --> 82.16]  Head to CockroachLabs.com slash changelog to learn more.
[82.54 --> 85.44]  Again, CockroachLabs.com slash changelog.
[96.54 --> 97.56]  Let's do it.
[98.08 --> 99.18]  It's go time.
[99.84 --> 104.62]  Welcome to Go Time, your source for diverse discussions from around the Go community.
[104.62 --> 109.76]  We record live each and every Tuesday at 3 p.m. U.S. Eastern.
[110.04 --> 115.06]  Subscribe now at youtube.com slash changelog so you're notified of when we go live.
[115.34 --> 119.62]  And don't forget to hop into the Gophers, Slack, and the Go Time FM channel.
[119.78 --> 121.00]  That's where all the chatter happens.
[121.24 --> 124.70]  If this is your first time listening, subscribe now at gotime.fm.
[124.82 --> 126.32]  Hey, let's get right into it, shall we?
[126.82 --> 127.82]  Here we go.
[127.82 --> 131.92]  Hi, everyone.
[132.24 --> 135.50]  Good evening, morning, afternoon, wherever you're joining from.
[135.78 --> 138.48]  Today we have people joining from all over the place.
[138.62 --> 141.98]  So we're definitely celebrating all hours of the day.
[142.78 --> 147.72]  And this episode is here to talk about Go Code pop quizzes.
[148.54 --> 153.82]  And we have lots of interesting guests from, it's really fun to say, from around the world.
[153.82 --> 156.28]  But this is really, really happening now.
[156.52 --> 158.24]  So we have Miki joining from Israel.
[158.46 --> 159.32]  What time is it for you, Miki?
[159.40 --> 159.62]  Hello.
[159.90 --> 162.10]  It's 11.10 p.m.
[162.58 --> 162.88]  Cool.
[163.22 --> 164.36]  Did you have coffee recently?
[165.98 --> 167.54]  No, but I'm good.
[167.90 --> 168.30]  That's good.
[168.66 --> 170.92]  It's probably better not to have coffee so close to sleep.
[171.44 --> 172.62]  Oh, it doesn't affect me.
[172.82 --> 175.18]  I can drink a cup of coffee and go right away to sleep.
[175.46 --> 175.70]  Crazy.
[176.92 --> 179.72]  And we have Dave joining us from Sydney.
[180.28 --> 180.96]  Dave, good morning.
[181.48 --> 182.08]  Good morning.
[182.18 --> 182.44]  Hello.
[182.44 --> 183.92]  You're already in the future.
[184.78 --> 185.18]  Yep.
[185.46 --> 187.48]  It's about 10 past six in the morning here.
[187.74 --> 188.84]  So we're just starting our day.
[189.58 --> 190.78]  And you're in tomorrow.
[192.28 --> 193.78]  You probably never heard that.
[193.88 --> 194.06]  Sorry.
[194.28 --> 195.62]  I do get excited by that.
[195.70 --> 197.40]  I don't have too many colleagues in Australia.
[197.80 --> 199.02]  I'm joining from Berlin here.
[199.14 --> 199.76]  It's 10 p.m.
[200.34 --> 201.56]  John, what time is it for you?
[202.36 --> 203.48]  It is 4 p.m.
[203.58 --> 205.04]  Well, 4.10, but yeah, 4 p.m.
[205.16 --> 206.54]  I'm on the East Coast of the U.S.
[206.76 --> 208.70]  So New York time, essentially.
[208.70 --> 212.80]  Dave, I imagine your teammates who aren't in Australia don't love that.
[213.24 --> 216.36]  Like Natalie's loving that you're in a different day, but anybody trying to schedule a meeting
[216.36 --> 217.60]  with you is like, this is annoying.
[218.38 --> 218.52]  Yeah.
[218.58 --> 223.36]  If you're on the East Coast, it's not great to talk to Australians, especially in kind
[223.36 --> 225.04]  of like this set of time zones.
[225.18 --> 229.16]  It's okay to the West Coast, like to California and Seattle, especially in the winter for Americans.
[229.16 --> 231.10]  But yeah, right now it's not super awesome.
[231.72 --> 235.10]  When Natalie was telling me the time for this, I was like trying to confirm three times because
[235.10 --> 236.30]  I'm like, all right.
[236.70 --> 238.46]  Because she told me your date and time at first.
[238.48 --> 241.46]  And I'm like, all right, I got to make sure I have this right here because I'm not sure.
[242.48 --> 244.94]  It's just, it makes me like double check everything.
[245.36 --> 245.50]  Yeah.
[245.58 --> 250.22]  I think throughout this remote year, I don't know if I had a meeting where each person
[250.22 --> 251.52]  came from a different time zone.
[252.44 --> 256.90]  There was groups of people in different time zones or everybody somewhere and I'm here.
[257.50 --> 257.62]  Yeah.
[257.62 --> 260.48]  When you work in big international companies, that happens a lot.
[260.66 --> 264.00]  All these time zones and finding the right time for a meeting is so challenging.
[264.76 --> 266.58]  And as well, also the weekend is different.
[266.92 --> 269.72]  So less opportunities to actually meet people.
[270.12 --> 271.96]  Somebody spotted your dog, Joe.
[272.34 --> 273.78]  Yes, that is a dog behind me.
[273.92 --> 275.10]  I'm hoping my dog is quiet.
[275.62 --> 278.18]  If you see me like frantically hitting the mute button, that's what's going on.
[279.38 --> 281.54]  So our quick introduction round.
[281.70 --> 284.22]  Dave, you are a gopher working at GitHub.
[284.76 --> 287.58]  Yes, I've been GitHub for just every year.
[287.58 --> 289.26]  Now, GitHub is a very large place.
[289.44 --> 290.76]  Like it's a very big service.
[290.96 --> 292.82]  A lot of the backend stuff is written in Go.
[293.14 --> 297.42]  A lot of things that you interact with daily that aren't very obvious above the waterline.
[297.92 --> 301.54]  For example, I maintain the service that manages git commit signing.
[301.72 --> 306.78]  Like whenever you see a thing that is verified on GitHub, part of that traffic went to my service
[306.78 --> 307.40]  to actually check.
[307.96 --> 308.98]  Are your commits verified?
[308.98 --> 312.84]  So we have a lot of gophers at perhaps some on the call here.
[312.84 --> 314.60]  A lot of gophers at GitHub.
[314.84 --> 317.06]  Again, doing a lot of back-endy things.
[317.94 --> 318.04]  Cool.
[318.36 --> 322.42]  And you also are a master of pop quizzes in Go.
[323.10 --> 326.58]  You're doing so many of those on Twitter and conferences and other places.
[327.26 --> 328.32]  Yeah, the last one got me.
[330.68 --> 335.64]  Well, I think the thing that is most pleasing is that I'm not the only one who's doing them.
[335.72 --> 340.28]  Like that's like the, you know, you're onto a winner when other people want to get into
[340.28 --> 340.58]  the game.
[340.58 --> 344.16]  They're inspired to like take and enhance and take the idea further.
[344.50 --> 345.30]  This is super exciting.
[345.30 --> 352.16]  Mickey, you describe yourself as an old dog that learns new tricks from time to time.
[352.66 --> 353.20]  Exactly.
[353.80 --> 355.44]  Does that include also pop quizzes?
[356.32 --> 357.26]  Yeah, definitely.
[358.48 --> 364.62]  I like quizzes in general and turning them into a tool of teaching and several books.
[364.82 --> 367.32]  It's something new that I picked up.
[367.74 --> 368.74]  I am old in technology.
[369.20 --> 371.62]  Like I'm 51, which is ancient, I think.
[371.62 --> 378.26]  I started when I was 16, I think, somewhere around that.
[378.94 --> 381.08]  And professionally, it's 25 years.
[381.68 --> 382.96]  And I always try to learn.
[383.14 --> 384.34]  That's what survives me still now.
[384.58 --> 385.18]  That's really cool.
[385.60 --> 386.32]  John, you're on mute.
[386.52 --> 387.82]  Does it mean the dog is barking now?
[387.94 --> 391.02]  I wanted to ask you about teaching and your thoughts about pop quizzes.
[391.50 --> 392.44]  No, he's not barking.
[392.84 --> 393.92]  I mean, I like pop quizzes.
[394.38 --> 397.74]  It's kind of interesting because a lot of the ones I see on, which we'll probably get into,
[397.74 --> 401.12]  tend to be showing something that's very unique about the language.
[401.62 --> 405.56]  Which is always fun to see, like, how many people who think they're experts in something
[405.56 --> 408.64]  really understand what's going to happen in some really obscure case.
[409.42 --> 412.64]  And I think, Dave, you've definitely gotten, I think, everybody at some point in time.
[412.84 --> 415.00]  I don't think it's possible that anybody's answered them all.
[415.44 --> 418.22]  I'm honestly curious if you knew the answer to all of them before you ran them.
[419.26 --> 420.26]  Oh, absolutely not.
[420.28 --> 423.10]  And that's kind of, I'm sure we'll get into this, but like, if you're looking for the,
[423.40 --> 424.30]  what's the inspiration?
[424.30 --> 428.30]  It's usually when I was like, well, I didn't know that, or I wasn't sure.
[428.52 --> 432.72]  Or then naturally from that follows, well, I wonder if anybody else knows this.
[433.52 --> 435.70]  Yeah, for me, it's usually bugs that I make.
[435.90 --> 438.02]  And then I start wondering, why?
[438.24 --> 439.08]  Why did this happen?
[439.24 --> 440.14]  I didn't expect that.
[440.52 --> 442.28]  And then you try to figure it out.
[442.34 --> 447.02]  And then if you move it to teaching and you try to distill it, then you hit this point
[447.02 --> 451.76]  where you get a really short example that people like, and it's really confusing.
[452.28 --> 456.80]  So it sounds like you're not hunting after topics, but you just come across things and
[456.80 --> 458.76]  then develop that into something interesting.
[459.32 --> 460.94]  Oh, I'm really good at writing bugs.
[461.26 --> 464.04]  So I have a lot of opportunities to learn from them.
[464.60 --> 465.60]  I'm not particular.
[465.60 --> 469.28]  I think sometimes it's interesting for me to say, like, what happens?
[469.74 --> 473.94]  A lot of times students ask, you know, the weirdest questions about what will happen if
[473.94 --> 474.44]  we do this.
[474.56 --> 476.14]  And, you know, I never done that.
[476.14 --> 478.82]  And then you try it out and, oh, that's interesting.
[479.30 --> 481.52]  It's a lot coming from my students as well.
[481.84 --> 485.88]  Students are always really fun because, like, when they're not programmers, they don't think
[485.88 --> 488.74]  about things the same way somebody who's been programming for a while thinks.
[489.04 --> 489.28]  Yes.
[489.38 --> 491.72]  And when they, like, ask those questions, it's always, like, enlightening.
[491.72 --> 496.30]  You're like, oh, maybe I should, like, talk to people who aren't programmers more often
[496.30 --> 497.90]  to get their insights as to what happens.
[498.54 --> 503.68]  I think a lot of the time, like, as technologists or especially as, like, the person that writes
[503.68 --> 509.30]  the programmer or that works very closely in the area, you can kind of develop blinders
[509.30 --> 509.90]  or blinkers.
[509.90 --> 515.16]  Like, they kind of protect you or guide you down, like, a reasonable, sensible path.
[515.36 --> 519.32]  I saw a tweet on Twitter a couple of days ago of, it's just kind of like a mean thing
[519.32 --> 522.22]  of a user trying your product for the first time.
[522.22 --> 526.64]  And it's, like, it's a cartoon guy trying to drink water out of a glass.
[527.30 --> 530.96]  He starts by licking the bottom of the glass and then kind of tacking it with his chin,
[531.04 --> 531.60]  things like that.
[531.92 --> 534.64]  But the point is kind of made, like, we know the right way to do something.
[534.86 --> 538.90]  So it seems unnatural to kind of be, like, to kind of try and do it the wrong way.
[539.02 --> 542.38]  But yet, if you introduce that situation to somebody new, they have no carders.
[542.42 --> 544.00]  They have no idea how to do it.
[544.00 --> 550.00]  And if you think back to, like, very early in when computing was, like, when kind of
[550.00 --> 553.82]  desktop computing, I think back to kind of, like, the 80s and 90s when I was growing up,
[554.16 --> 557.94]  there was a big push to do a thing called desktop skills or typing skills, which was
[557.94 --> 559.68]  basically, do you know how to use Microsoft Word?
[560.04 --> 563.18]  Because people were so scared that, like, they could break your computer.
[564.10 --> 566.22]  Like, if you type the wrong thing, you could break your computer.
[566.64 --> 569.82]  I'm sure, Mickey, like, you would notice from teaching your students, like, the first thing
[569.82 --> 573.70]  they'd be worried about is, like, if I make a syntax error, like, is that going to break it?
[573.70 --> 575.24]  Like, the computer is going to be somehow broken.
[575.36 --> 577.40]  Like, the first syntax error and it's broken completely.
[578.00 --> 582.46]  And one of the hardest things about teaching is to teach people it's okay to make mistakes.
[582.70 --> 586.48]  It's okay to, like, if the program doesn't compile, that's not a big deal.
[586.58 --> 586.90]  Congratulations.
[587.08 --> 587.82]  We just get to fix it.
[588.10 --> 589.84]  Nothing is terribly broken or ruined.
[589.84 --> 596.02]  But that was very much a thing of kind of introducing computers to people starting high school
[596.02 --> 599.94]  and primary school here in Australia just so that they would be more familiar with them.
[600.06 --> 602.38]  Again, it's something we take for granted that the children.
[602.38 --> 607.48]  And I remember someone telling me that their young child tried to tap on the television screen,
[608.00 --> 613.02]  which seems perfectly reasonable because every other screen they'd ever seen, you could tap on.
[613.10 --> 614.24]  So why couldn't you tap on the TV?
[614.76 --> 620.06]  And then compare that to maybe yourself or your parents who just don't really want to use a computer
[620.06 --> 621.56]  because they're worried they could break it.
[622.38 --> 627.68]  So the idea about, like, familiarizing people and familiarizing them saying it's okay to fail or make mistakes
[627.68 --> 630.12]  is kind of like the first hurdle of teaching anything.
[630.12 --> 635.28]  Yeah. I'm still afraid to break my computer every time I use it, but I think I'm getting better at it.
[635.70 --> 639.20]  And I totally agree that this fear, and this is what's fun about programming,
[639.40 --> 641.84]  is that you can make mistakes as much as you want.
[641.92 --> 645.34]  And most of the time, the cost of error is almost nothing.
[645.54 --> 647.32]  So you just can play around with it.
[647.92 --> 649.18]  And Go is a great language for that.
[649.18 --> 653.92]  Because of this fast cycle of go run and try it out and go run again,
[654.16 --> 655.86]  it's really easy to just try things out.
[656.08 --> 660.78]  Like your quizzes, I just copy and paste from Twitter and do a go run and see,
[660.86 --> 662.02]  oh, I got it wrong again.
[662.44 --> 664.52]  But it's really easy to try it out.
[665.22 --> 671.00]  There's a joke that computers are the thing in history that allows you to make mistakes the fastest,
[671.34 --> 673.46]  with the exception of tequila and head guns.
[673.46 --> 678.54]  So you should use that and actually learn from those mistakes.
[679.18 --> 681.30]  Yeah, it's a very interesting point, David.
[681.40 --> 686.04]  You said that to include in the learning process that you should be making mistakes,
[686.12 --> 687.12]  you should be breaking things.
[687.24 --> 693.78]  That's definitely not obvious and can open a whole discussion on if you use a grading system.
[693.96 --> 696.66]  Do you encourage that versus if you do things like projects?
[697.36 --> 699.78]  It's true, not just for teaching, by the way.
[699.78 --> 704.22]  A lot of companies also, if you have an atmosphere where it's okay to make mistakes,
[704.42 --> 708.06]  these companies usually do better than people who are always worried about
[708.06 --> 709.90]  what will happen if I do something wrong.
[710.86 --> 712.22]  So I totally agree with that.
[712.74 --> 712.88]  Yeah.
[713.84 --> 716.70]  I wonder if a pop quiz is a quick way of encouraging that,
[716.78 --> 719.68]  because you basically tell people, take a guess, try.
[720.10 --> 723.10]  You might get it wrong, but you do encourage them to do that.
[723.24 --> 726.64]  I'd say pop quizzes help, because every pop quiz, you can just run it.
[726.64 --> 730.18]  Like, there's no, like, big downside of, like, oh, I got this wrong,
[730.22 --> 731.22]  and the whole world's going to know.
[731.72 --> 734.52]  Like, even if you get it wrong, you're, like, usually within a lot of people
[734.52 --> 736.84]  have already gotten it wrong, so you're not, like, the only one getting it wrong.
[737.34 --> 740.74]  And then on top of that, you can go run it and be like, oh, now I understand, like,
[740.86 --> 741.92]  or I see what's going on.
[741.94 --> 743.42]  You might not understand why that's happening.
[743.76 --> 745.48]  So I probably need to give a little bit of history.
[745.78 --> 749.18]  So you asked Natalie, where do some of these ideas come from?
[749.18 --> 753.42]  And a lot of them come from bugs or mistakes that I didn't understand,
[754.12 --> 755.06]  or teaching opportunities.
[755.22 --> 758.12]  But the original idea, or the original genius for this was,
[758.56 --> 761.58]  I was reading the Go spec, and this makes me sound like the giantest nerd ever,
[761.76 --> 763.40]  because I read the spec a lot.
[764.02 --> 766.32]  A lot of the quizzes come from it, so I am a giant nerd.
[767.04 --> 772.92]  And just in reading through that, I was like, oh, copy, the built-in copy operation.
[773.32 --> 774.90]  The copy function returns a number.
[775.52 --> 776.46]  Well, I guess that makes sense.
[776.46 --> 778.62]  It's like, oh, copy returns how many bytes of copy.
[778.72 --> 779.88]  So that makes sense.
[779.98 --> 783.40]  But, like, this is going back so early in the days of Go.
[783.82 --> 787.90]  Before we had append, we actually had to use copy to, like, grow and make new slices.
[788.06 --> 790.12]  Like, everyone would write their own append function.
[790.26 --> 793.94]  And, I mean, this is going back into the prehistoric days of Go.
[793.94 --> 796.80]  So back then, copy was used a lot more.
[796.90 --> 799.28]  But now that we have append, it's used very infrequently,
[799.40 --> 800.84]  except if you're doing, like, slice tricks.
[800.96 --> 805.44]  And so I thought, well, like, most of the time I barely remember copies there.
[805.44 --> 809.54]  I wonder how many people also remember that it returns a number.
[810.36 --> 814.10]  And so I thought, well, how could I kind of show this to people or remind people about this
[814.10 --> 816.48]  in a way that kind of would give them a laugh?
[816.54 --> 818.44]  And so that was the idea for the quiz.
[818.82 --> 822.56]  And the other piece, which was it used to be much harder,
[822.68 --> 826.18]  but now, thankfully, tweets are longer, was I set myself to challenge
[826.18 --> 830.40]  because I like this idea of Ritchie K has this great talk on constraints.
[830.40 --> 833.54]  And to not spoil the whole thing, it says that, you know,
[833.64 --> 836.22]  composers when they're starting out will set themselves a bunch of constraints,
[836.22 --> 838.84]  like I'm only going to use this key, or I'm going to make this,
[838.98 --> 840.26]  build this around a particular instrument.
[840.68 --> 840.96]  Why?
[841.52 --> 842.92]  Or just to give themselves limitations.
[843.04 --> 845.20]  Otherwise, you'd have this impossible blank canvas.
[845.46 --> 849.30]  So rather than just linking to the playground,
[849.98 --> 852.56]  all the code and a runnable sample, I said, well, it has to fit in the tweet.
[852.78 --> 856.86]  And that usually involved quite a lot of brutalism to the syntax
[856.86 --> 860.04]  and kind of like remove all the white space to make it fit in the tweet.
[860.10 --> 861.56]  But that was the kind of the constraint.
[861.96 --> 865.42]  Can you ask this question in a way that fits in a tweet?
[865.88 --> 867.96]  And along the way, tweets got a little bit bigger.
[868.24 --> 870.40]  We've got quizzes, the questionnaire things,
[870.44 --> 871.58]  which kind of make it very easy.
[871.70 --> 873.84]  And also don't count against your word count, which is great
[873.84 --> 876.50]  to give a set of predefined answers.
[876.82 --> 878.90]  But that was kind of like the genius for that.
[878.90 --> 880.80]  And the last thing about the quiz,
[880.86 --> 883.90]  I remember I had a conversation over Twitter with Peter Bergon.
[884.30 --> 885.54]  I think I tweeted once, you know,
[885.54 --> 887.46]  Golang top tip, something like that.
[887.70 --> 888.78]  And he said, why is it a top tip?
[888.88 --> 890.72]  I said, well, because it was a pro tip,
[890.82 --> 891.92]  not everyone would be able to use it.
[892.52 --> 894.58]  The idea of making a pop quiz is like,
[894.64 --> 897.16]  don't make it about it's only for experts or like,
[897.16 --> 898.50]  make it anyone can try.
[898.56 --> 899.58]  So it's kind of like, that's the,
[900.28 --> 901.72]  if you want to like think of the ground rules
[901.72 --> 904.16]  for how to do a Twitter Golang pop quiz,
[904.74 --> 906.12]  those are like how to fit in a tweet.
[906.12 --> 908.74]  The other reason about not using the playground is,
[909.40 --> 911.48]  well, it kind of makes it too easy to get the answer.
[911.70 --> 913.12]  Like you go to that playground link
[913.12 --> 914.68]  and instead of having to think,
[914.76 --> 915.98]  you could just like push the run button
[915.98 --> 916.86]  and it'll tell you the answer.
[917.24 --> 919.38]  So every now and occasionally people are like,
[919.44 --> 920.96]  oh, why can't you post a link to the playground?
[921.12 --> 922.38]  Or, you know, I need a bot
[922.38 --> 923.92]  to automatically copy this into the playground.
[924.12 --> 925.58]  Like, well, if you did that,
[926.08 --> 927.36]  like where would the challenge be?
[928.00 --> 929.10]  That's kind of like the ground rules
[929.10 --> 930.78]  for how this whole shebang started.
[931.20 --> 931.92]  So does that mean that
[931.92 --> 933.64]  if we're using screenshots of code, we're cheating?
[934.10 --> 935.76]  I don't claim proprietary over this.
[935.82 --> 937.84]  I don't claim that like, this is my idea.
[937.90 --> 938.60]  That's certainly not.
[938.60 --> 942.62]  The actual idea for this came from 20 years ago.
[942.70 --> 944.60]  There was a wonderful book by Josh Block
[944.60 --> 945.58]  called Java Puzzlers.
[946.12 --> 946.84]  It's one of my favorites.
[946.98 --> 947.84]  And Mickey knows this story.
[948.28 --> 952.02]  It was my favorite because it had like 50 questions
[952.02 --> 955.42]  of like in the kind of classic pop quiz style.
[955.82 --> 956.80]  What does this program print?
[956.86 --> 958.04]  Or does this program compile?
[958.34 --> 960.34]  Like very simple, short programs.
[960.94 --> 963.42]  And then a much larger description afterwards,
[963.42 --> 965.76]  which said, well, actually no.
[965.76 --> 968.28]  And this might be surprising because,
[968.74 --> 970.10]  and then gave the explanation.
[970.34 --> 972.10]  And for me, it wasn't so much about
[972.10 --> 974.20]  like getting 50 out of 50 on those quizzes.
[974.20 --> 976.64]  It was about what you learned from like,
[976.72 --> 977.86]  well, that was surprising.
[978.08 --> 978.68]  Why is that?
[979.16 --> 982.48]  And so the pop quiz format is like mutated
[982.48 --> 984.54]  from just short tweets.
[985.24 --> 986.50]  I'll give you some examples.
[986.78 --> 987.56]  At the London Gophers,
[987.64 --> 989.64]  they have a question for the audience
[989.64 --> 990.86]  between the talks.
[991.40 --> 993.20]  So at the end of the talk,
[993.48 --> 995.24]  they put a slide up while people are on break.
[995.24 --> 996.36]  And then you come back and you,
[996.90 --> 998.50]  I think they either do like a show of hands.
[998.58 --> 1000.30]  And then the person that asked the question,
[1000.40 --> 1001.14]  like has to explain,
[1001.24 --> 1002.48]  well, if you thought that,
[1002.86 --> 1003.80]  here's the answer and here's why.
[1003.88 --> 1006.50]  Like the important part is giving the explanation.
[1007.14 --> 1009.06]  I know that I've seen some examples
[1009.06 --> 1011.00]  that at some of the meetups
[1011.00 --> 1012.38]  that the Japanese Gophers have,
[1012.56 --> 1014.40]  1010 had three questions
[1014.40 --> 1015.90]  that they asked in their after party.
[1015.98 --> 1018.56]  And again, some are kind of educational,
[1018.70 --> 1020.26]  others are just downright mean.
[1020.78 --> 1022.64]  So I've taken some of the ones that,
[1022.78 --> 1024.64]  some of the pop quizzes that I like the most.
[1024.64 --> 1026.06]  And I've kind of redid them
[1026.06 --> 1027.58]  into 20 minute presentation
[1027.58 --> 1029.80]  because it was a good thing to bring to meetups
[1029.80 --> 1031.16]  if I was traveling or something like that.
[1031.22 --> 1032.66]  Like it's always a good party filler
[1032.66 --> 1034.58]  to have some questions for the audience
[1034.58 --> 1036.10]  to like to warm people up.
[1036.62 --> 1037.28]  And in that format,
[1037.46 --> 1039.24]  kind of you can have a slide with the question,
[1039.32 --> 1040.40]  you can have a slide with the answer.
[1040.52 --> 1042.84]  So it's not like a fixed thing.
[1042.92 --> 1045.22]  It's not like there's a way to do it right or wrongly.
[1045.70 --> 1047.46]  To me, the value is always
[1047.46 --> 1050.28]  not to like be true and strict to the form.
[1050.28 --> 1052.78]  It's to the bit that comes after asking that question
[1052.78 --> 1056.10]  and saying, oh, well, I wasn't expecting that answer.
[1056.64 --> 1057.46]  Why is that?
[1057.92 --> 1059.40]  And that's probably one thing
[1059.40 --> 1061.52]  that the Twitter form lacks,
[1061.82 --> 1064.12]  partially because like that was yesterday's tweet,
[1064.48 --> 1065.28]  lose interest in it.
[1065.62 --> 1067.34]  And I kind of do recognize that I'd leave the,
[1067.82 --> 1068.76]  why is the answer three?
[1068.96 --> 1071.00]  For example, as a kind of like,
[1071.06 --> 1073.32]  oh, you have to go and figure that out yourself.
[1073.78 --> 1075.64]  Perhaps it could be more effective
[1075.64 --> 1078.30]  if I did have more kind of follow through.
[1078.52 --> 1079.24]  But generally these,
[1079.90 --> 1081.24]  the kind of genius for asking a question
[1081.24 --> 1082.78]  comes quite spontaneously.
[1083.06 --> 1084.44]  And so I'm like, that'll fit in a tweet.
[1084.52 --> 1086.56]  I can make that into a pop quiz.
[1088.06 --> 1089.58]  So on a related note, I guess,
[1090.04 --> 1091.04]  when you're making these quizzes,
[1091.04 --> 1093.04]  you said like it kind of being an unexpected answer
[1093.04 --> 1094.82]  is part of the appeal is like,
[1094.90 --> 1095.94]  it catches people off guard.
[1096.00 --> 1097.46]  It's something new that they're going to learn.
[1098.00 --> 1099.72]  Do you ever worry that you post so many of those
[1099.72 --> 1101.58]  that people just expect the unexpected with you?
[1101.98 --> 1103.52]  I mean, granted, they should be learning regardless.
[1103.52 --> 1106.44]  So it's useful, but I don't know if like,
[1106.58 --> 1107.82]  do you ever try to like throw ones in
[1107.82 --> 1108.72]  that are more obvious
[1108.72 --> 1111.32]  just to see if people are actually on like paying attention?
[1112.00 --> 1112.14]  Yeah.
[1112.26 --> 1115.08]  If there is an aspect that people feel that like
[1115.08 --> 1116.54]  they're cruel or unfair
[1116.54 --> 1118.50]  or attempting to catch people,
[1118.56 --> 1119.72]  that's a personal failing on me,
[1119.78 --> 1122.14]  not in the idea of encouraging people
[1122.14 --> 1123.74]  to learn a subject more deeply
[1123.74 --> 1125.38]  through asking simple questions.
[1125.38 --> 1126.18]  That's definitely on me.
[1126.54 --> 1127.64]  To not take all of the blame.
[1127.90 --> 1128.90]  Twitter lets you have four answers.
[1129.08 --> 1130.90]  So generally you put a ringer in there.
[1130.90 --> 1134.16]  I do try to make them not too unfair.
[1134.36 --> 1136.84]  Like there's, but in saying that almost always,
[1136.94 --> 1138.98]  like if you give doesn't compile or panics at runtime,
[1139.48 --> 1141.52]  some 10, 15% of people will click on it.
[1141.70 --> 1142.84]  Maybe because they think,
[1143.04 --> 1144.24]  well, actually that's invalid syntax
[1144.24 --> 1145.18]  or something like that.
[1145.22 --> 1147.06]  There was a pop quiz a couple of weeks ago
[1147.06 --> 1150.24]  when I found out that there's a hexadecimal form
[1150.24 --> 1151.32]  of floating point literals.
[1152.28 --> 1154.18]  I'm sure it has the same utility
[1154.18 --> 1155.96]  as complex numbers have in Go.
[1156.02 --> 1157.46]  And I'm sure I'm going to get some hate mail for that.
[1157.46 --> 1160.88]  But there is a hexadecimal form of,
[1161.48 --> 1163.78]  so not 1.5 e to the minus two.
[1163.92 --> 1165.60]  It's some hexadecimal form.
[1165.66 --> 1166.80]  And of course, when it's hexadecimal,
[1167.04 --> 1170.32]  you can't use e because e is part of the character set for hex.
[1170.38 --> 1171.32]  So you have to use p.
[1171.86 --> 1173.26]  So it just looks like line noise.
[1173.80 --> 1175.36]  And so when I asked that question,
[1175.46 --> 1176.72]  it probably is quite reasonable
[1176.72 --> 1178.36]  to make one of the answers,
[1178.74 --> 1180.74]  well, this doesn't compile because it's line noise.
[1180.86 --> 1182.36]  That's like not valid syntax.
[1182.36 --> 1186.76]  But perhaps one of the failings of the Twitter quiz thing
[1186.76 --> 1188.14]  is that you don't get to have another go.
[1188.26 --> 1190.76]  You click one answer and you can't ever change your mind.
[1191.16 --> 1192.44]  But hopefully people say,
[1192.52 --> 1193.80]  well, why would you ask a question
[1193.80 --> 1195.86]  where it clearly looks like line noise on the page
[1195.86 --> 1198.86]  and one of the answers is doesn't compile?
[1199.52 --> 1200.72]  Like, isn't that too easy?
[1201.28 --> 1203.20]  Like, so perhaps there's a little bit of that
[1203.20 --> 1205.60]  in structuring the question.
[1206.26 --> 1207.62]  I'll give you another example.
[1207.62 --> 1209.02]  My friend Tenten from Japan,
[1209.60 --> 1211.84]  one of the pop quizzes he wrote for his meetup,
[1212.36 --> 1214.08]  it was two pages worth of code
[1214.08 --> 1217.80]  and you needed to trace a variable from a function
[1217.80 --> 1219.48]  and then it went into a map
[1219.48 --> 1221.44]  and then he looked up the key,
[1221.54 --> 1222.86]  but it was by the wrong value.
[1223.00 --> 1224.78]  So you were getting the zero value out of the map
[1224.78 --> 1226.34]  and you returned that from a function,
[1226.42 --> 1227.74]  but actually used the name return.
[1228.32 --> 1231.22]  It actually turned out that none of that mattered
[1231.22 --> 1234.26]  because he deliberately missed the space
[1234.26 --> 1235.86]  in the go embed declaration.
[1236.70 --> 1238.12]  To make the quiz as impossible as possible,
[1238.20 --> 1239.66]  and I'll finally kind of put it in the show notes,
[1240.08 --> 1241.36]  it actually included itself.
[1241.36 --> 1243.98]  So used go embed to embed the source code itself
[1243.98 --> 1245.96]  and then used the length of the source code
[1245.96 --> 1249.42]  as an input to the function and then all of this.
[1250.12 --> 1252.46]  And I went through all the work of trying to figure out
[1252.46 --> 1255.18]  what would this return eventually boils down to true or false.
[1255.72 --> 1257.80]  The reality is that like, that's not really a quiz,
[1257.86 --> 1260.30]  that's kind of like just doing the algorithm longhand.
[1260.88 --> 1262.18]  Like if you look further and you ask,
[1262.28 --> 1263.40]  why is someone asking this question?
[1263.76 --> 1266.14]  It's probably because there is a more straightforward answer.
[1266.22 --> 1268.02]  And the straightforward answer was that he'd missed off,
[1268.02 --> 1270.60]  he deliberately left the space out of go embed
[1270.60 --> 1272.28]  so that declaration didn't do anything.
[1272.62 --> 1275.48]  And so the length of the file was pointless
[1275.48 --> 1276.94]  because he never embedded the file.
[1277.32 --> 1279.16]  So I think part of asking the question
[1279.16 --> 1280.28]  might seem a little bit unfair,
[1280.28 --> 1281.94]  but you have to think, well, what is the,
[1282.04 --> 1284.34]  like, it's usually not the obvious answer.
[1284.96 --> 1285.88]  I'll take today's quiz.
[1286.28 --> 1288.26]  For example, what is the length of the string
[1288.26 --> 1289.98]  composed of the rune minus one?
[1290.62 --> 1291.68]  And the answer is one, two, and three.
[1292.16 --> 1293.78]  Turns out the answer is three for all the people
[1293.78 --> 1295.36]  who are still working it out.
[1295.40 --> 1298.34]  And the reason it's three is because in the spec,
[1298.72 --> 1301.34]  how I came across this was when you're iterating over a string,
[1301.68 --> 1304.54]  and we know that strings are made up of UTF encoded characters,
[1305.14 --> 1308.78]  you iterate over it, not byte by byte, but rune by rune.
[1309.26 --> 1310.58]  And so you can come into a situation
[1310.58 --> 1313.72]  where you have invalid UTF-8.
[1314.66 --> 1316.74]  In that case, the spec clearly says
[1316.74 --> 1319.82]  that Go will return this called the broken rune
[1319.82 --> 1320.62]  or something like that.
[1320.70 --> 1322.14]  It's Unicode FFFD.
[1322.70 --> 1324.62]  So the only thing you need to remember about that
[1324.62 --> 1327.46]  is to encode 16 bits in Unicode,
[1327.54 --> 1328.54]  you actually need three characters.
[1329.42 --> 1331.48]  So one of the answers there was, well, it doesn't compile.
[1331.90 --> 1333.02]  That would seem to be the obvious one.
[1333.04 --> 1334.68]  Like when you have var rune equals minus one,
[1334.86 --> 1336.78]  you might be thinking, well, that doesn't compile
[1336.78 --> 1338.72]  because that doesn't make any sense to have a,
[1338.92 --> 1340.22]  like a character that is negative.
[1340.22 --> 1341.20]  That doesn't make any sense.
[1341.98 --> 1343.54]  But if you were to think a little bit further
[1343.54 --> 1346.10]  and say, well, wouldn't that be like the easy answer?
[1346.34 --> 1347.82]  Like all those quizzes, none of them compile.
[1347.94 --> 1348.80]  Like that's the easy answer.
[1349.08 --> 1350.70]  As Frances says, you should write better code.
[1350.76 --> 1351.76]  Like don't write code like that.
[1352.20 --> 1354.14]  But if you were to ask the question a little bit deeper
[1354.14 --> 1356.44]  and say, well, if this code did compile,
[1356.68 --> 1357.74]  how would that propagate through?
[1357.94 --> 1360.30]  And that could potentially lead you to a different answer.
[1360.30 --> 1371.56]  This episode is brought to you by our friends at LaunchDarkly,
[1371.70 --> 1373.66]  feature management for the modern enterprise,
[1373.98 --> 1376.22]  power testing in production at any scale.
[1376.46 --> 1377.24]  Here's how it works.
[1377.66 --> 1379.28]  LaunchDarkly enables development teams
[1379.28 --> 1382.18]  and operation teams to deploy code at any time,
[1382.42 --> 1384.72]  even if a feature isn't ready to release to users.
[1385.08 --> 1386.44]  Wrapping code with feature flags
[1386.44 --> 1388.38]  gives you the safety to test new features
[1388.38 --> 1390.76]  and infrastructure in your production environments
[1390.76 --> 1392.96]  without impacting the wrong end users.
[1393.40 --> 1394.66]  When you're ready to release more widely,
[1394.96 --> 1395.92]  update the flag status
[1395.92 --> 1397.80]  and the changes are made instantaneously
[1397.80 --> 1399.74]  by the real-time streaming architecture.
[1400.20 --> 1401.72]  Eliminate risk, deliver value,
[1401.86 --> 1404.44]  get started for free today at LaunchDarkly.com.
[1404.44 --> 1406.48]  Again, LaunchDarkly.com.
[1406.48 --> 1422.40]  I think the goal of these quizzes is to teach,
[1422.50 --> 1424.92]  is not to show just dark corners of the language
[1424.92 --> 1427.54]  that, you know, I did a stupid bug and that's it,
[1427.62 --> 1429.82]  or there is something really weird going on.
[1429.88 --> 1431.42]  But I think especially in Go,
[1431.80 --> 1434.52]  there's a lot of thought behind everything in the language.
[1434.52 --> 1438.50]  So, every time you see a weird behavior,
[1439.12 --> 1441.26]  there's usually a justification for that
[1441.26 --> 1444.24]  and you need to dig out why is that for finding out.
[1445.04 --> 1445.98]  That's precisely it.
[1446.72 --> 1446.94]  Yeah.
[1447.28 --> 1450.00]  So, I always say it doesn't compile.
[1450.88 --> 1454.78]  Maybe, but probably there's a deeper reason
[1454.78 --> 1456.36]  for why it's showing this quiz
[1456.36 --> 1457.80]  so we can learn from it.
[1458.42 --> 1458.68]  Yeah.
[1458.74 --> 1459.50]  I think in the past,
[1459.60 --> 1461.72]  I probably have put a few of those kind of like,
[1461.72 --> 1462.94]  those answers that trick people
[1462.94 --> 1464.86]  because already you're kind of in the form,
[1464.92 --> 1466.22]  you're kind of squeezing it into a tweet.
[1466.30 --> 1468.02]  So, you're kind of mangling the syntax a little bit
[1468.02 --> 1470.34]  and like maybe collapsing something onto a few lines.
[1470.46 --> 1470.92]  And so to say,
[1471.20 --> 1473.58]  so the answer is it actually doesn't compile
[1473.58 --> 1474.86]  because I very trickily,
[1475.48 --> 1476.26]  instead of a space,
[1476.30 --> 1478.70]  I put that Unicode non-breaking space in there.
[1478.74 --> 1479.42]  Haha, I got you.
[1479.48 --> 1481.90]  Like, yeah, you're the smartest quiz asker.
[1482.02 --> 1483.20]  Like, no one got the right answer.
[1483.36 --> 1484.06]  Like, congratulations.
[1484.38 --> 1486.02]  But that wasn't very fair.
[1486.60 --> 1488.50]  Generally, I include that answer as like,
[1488.54 --> 1489.96]  it's one of the set of wrong answers.
[1489.96 --> 1492.36]  It's like, it would be unfair to ask to us that.
[1492.44 --> 1494.04]  And also like, what would someone learn from that?
[1494.18 --> 1496.48]  Other than here's how to write mangled source code
[1496.48 --> 1497.38]  that might fool somebody.
[1497.48 --> 1499.30]  Like, I think that defeats the purpose of
[1499.30 --> 1500.52]  as kind of like pop quizzes
[1500.52 --> 1502.00]  as a kind of an educational tool.
[1502.18 --> 1502.36]  Yeah.
[1502.40 --> 1503.52]  And to the reader,
[1503.70 --> 1506.30]  if we dismiss the easy, obvious ones of like,
[1506.56 --> 1507.22]  oh, that doesn't work
[1507.22 --> 1508.64]  or like that could never work.
[1509.16 --> 1509.96]  And once you dismiss that,
[1510.00 --> 1512.68]  you're left with a much more kind of more profound answer
[1512.68 --> 1514.12]  of, well, if that does work,
[1514.72 --> 1515.46]  I didn't know that.
[1515.54 --> 1516.82]  Like, what else don't I know about
[1516.82 --> 1518.18]  this part of the language?
[1518.18 --> 1519.74]  The iterating over string ones,
[1519.82 --> 1520.70]  I think is important
[1520.70 --> 1522.88]  because it's something that we do quite rarely.
[1523.00 --> 1524.62]  It's extremely common to use,
[1524.74 --> 1526.70]  you know, for ranging over byte slices
[1526.70 --> 1528.70]  or most slices.
[1529.10 --> 1531.58]  But we do also know that a string is a slice
[1531.58 --> 1534.88]  and iterating over using for range over a string
[1534.88 --> 1536.96]  has some surprising properties,
[1537.10 --> 1539.82]  which because I think most people don't use very often
[1539.82 --> 1542.30]  would again, like where things are surprising,
[1542.72 --> 1543.80]  those are where bugs lurk.
[1543.80 --> 1545.36]  When you iterate over a string,
[1545.80 --> 1549.26]  the index doesn't move by single increments every time.
[1549.50 --> 1553.10]  It moves to the start of each character encoded as UTF-8.
[1553.70 --> 1555.78]  So that can be one, can be two, can be three,
[1556.04 --> 1558.60]  can be up to four indexes into the string.
[1559.00 --> 1560.42]  I remember in the compiler, there wasn't a bug.
[1560.50 --> 1561.70]  It was a change I tried to make.
[1561.76 --> 1563.42]  And so I was like, no, you've missed that.
[1563.66 --> 1564.80]  For exactly that case,
[1564.88 --> 1567.76]  that there was a cast from a byte slice to a string.
[1567.94 --> 1569.26]  I'm like, why are we doing that?
[1569.30 --> 1569.94]  That's wasteful.
[1569.94 --> 1571.22]  And the answer was,
[1571.28 --> 1573.00]  it was so that the code moved through the string
[1573.00 --> 1575.88]  at the start of each rune in the string,
[1576.02 --> 1577.90]  rather than treating it as just like a byte slice
[1577.90 --> 1578.64]  of Unicode data.
[1578.80 --> 1581.96]  So it's one of these things which come up very rarely.
[1582.60 --> 1583.66]  You kind of need to know them
[1583.66 --> 1586.64]  because even though it's an unfamiliar part of Go,
[1586.76 --> 1587.30]  like for example,
[1587.36 --> 1589.18]  maybe breaking out of a loop to a label,
[1589.50 --> 1590.80]  like you have a loop inside a loop
[1590.80 --> 1592.96]  or a switch inside of a loop.
[1593.14 --> 1596.90]  You have to remember that break breaks to the innermost scope.
[1596.90 --> 1598.38]  So things like that,
[1598.46 --> 1600.82]  which are uncommon and are great examples
[1600.82 --> 1603.88]  for writing quizzes are also important
[1603.88 --> 1606.38]  because occasionally you're going to come up against them
[1606.38 --> 1608.18]  in code that someone else wrote.
[1608.94 --> 1611.44]  So what could be distilled into a teasing tweet
[1611.44 --> 1614.40]  can also be a bug that you're going to have to decode,
[1614.84 --> 1616.02]  debug in somebody else's code.
[1616.14 --> 1616.48]  Or your own.
[1616.76 --> 1618.46]  Or your own if you were being super smart.
[1618.58 --> 1618.74]  Yes.
[1619.86 --> 1622.30]  I think what you mentioned about Unicode,
[1622.48 --> 1624.96]  which I found a really great source for quizzes
[1624.96 --> 1627.56]  is both Unicodes and time and time zones,
[1627.96 --> 1629.60]  is that it's across languages.
[1629.98 --> 1631.76]  So every language has these things.
[1632.18 --> 1633.64]  So following your quizzes,
[1633.76 --> 1635.64]  when I got bored during COVID,
[1635.76 --> 1637.64]  I wrote a Go quiz book
[1637.64 --> 1639.06]  and then a Python quiz book.
[1639.40 --> 1640.18]  And both of them,
[1640.40 --> 1643.08]  the section about Unicode and time zones
[1643.08 --> 1645.46]  is roughly the same questions and the same answers
[1645.46 --> 1648.22]  because it's something you should know regardless.
[1649.24 --> 1649.36]  Yeah.
[1649.42 --> 1651.80]  And definitely if you're coming from another language,
[1651.80 --> 1654.64]  it's an area where languages do differ
[1654.64 --> 1655.60]  and they do innovate.
[1655.94 --> 1657.26]  Certainly for coming from Java,
[1657.92 --> 1660.22]  in Go, we just take as kind of a statement of fact,
[1660.76 --> 1662.28]  all the source code is UTF-8.
[1662.40 --> 1663.94]  At our local Go meetup a couple of years ago,
[1664.12 --> 1665.32]  Rob Pike was in the audience
[1665.32 --> 1667.50]  and he reminded me when I said something like,
[1668.36 --> 1669.52]  add a quiz that had an emoji
[1669.52 --> 1671.42]  and is this a valid identifier?
[1671.88 --> 1673.40]  You have to remember that.
[1673.60 --> 1675.90]  So like it was the franny face emoji
[1675.90 --> 1677.02]  or the thinking face emoji.
[1677.56 --> 1679.24]  The answer is it's not an identifier
[1679.24 --> 1680.86]  because it's not a letter
[1680.86 --> 1683.14]  because Unicode says that that emoji is not a letter.
[1683.52 --> 1685.24]  But what he reminded me was that
[1685.24 --> 1688.26]  I was like trying to make some example of like the bytes,
[1688.78 --> 1690.32]  you know, it's three bytes.
[1690.46 --> 1691.20]  And he said, no, no, no, no,
[1691.20 --> 1694.28]  like your editor has let you type the franny face
[1694.28 --> 1695.42]  in the source code
[1695.42 --> 1696.84]  because the source code is UTF-8.
[1696.92 --> 1699.20]  There's no kind of like interpreting it.
[1699.36 --> 1701.00]  It literally is UTF-8.
[1701.64 --> 1704.26]  And this is something which I think we kind of,
[1704.70 --> 1705.88]  perhaps Go programmers take for granted
[1705.88 --> 1707.92]  or perhaps programmers using languages
[1707.92 --> 1709.76]  of kind of Go's pedigree,
[1710.16 --> 1712.18]  take for granted because UTF-8 is the assumed.
[1712.30 --> 1713.70]  It's kind of like the default text format.
[1713.82 --> 1715.80]  We've gone away from code pages
[1715.80 --> 1718.18]  and all of those kind of like seven bit ASCII things
[1718.18 --> 1719.36]  that we had in the 90s.
[1719.46 --> 1720.72]  So it's very easy to just think,
[1720.80 --> 1722.10]  well, all text is Unicode,
[1722.34 --> 1724.42]  except if you're in Java land,
[1725.30 --> 1726.40]  all the characters are two bytes
[1726.40 --> 1727.82]  and the UTF-16 encoded.
[1728.28 --> 1729.78]  You have surrogate, pairs
[1729.78 --> 1731.70]  and all of these other horrible hacks
[1731.70 --> 1733.12]  to work around the fact that
[1733.12 --> 1735.26]  the Unicode space is bigger than 16 bits.
[1735.88 --> 1738.40]  And so if you were used to doing text processing,
[1739.40 --> 1740.74]  certainly you grew up in kind of like
[1740.74 --> 1744.10]  the early 2000s text processing with XML in Java,
[1744.60 --> 1746.02]  you would be thinking all the time
[1746.02 --> 1748.86]  about the code page that you got the file in from
[1748.86 --> 1750.66]  because you would be getting some input
[1750.66 --> 1754.58]  from some horrible IBM 370 system using Epsodic.
[1754.68 --> 1756.80]  You'd be talking to a fixed exchange,
[1757.30 --> 1758.26]  probably using ASCII.
[1758.64 --> 1760.00]  You'd have all kinds of like escaping
[1760.00 --> 1763.12]  to somehow fit umlauts and graphs
[1763.12 --> 1765.20]  and things like that from the hybrid ASCII thing.
[1765.26 --> 1766.64]  And these are things which we don't kind of
[1766.64 --> 1767.20]  have to deal with.
[1767.30 --> 1768.62]  And maybe Mickey, you can talk a little bit about
[1768.62 --> 1770.70]  like what it's like in the old world of Python
[1770.70 --> 1771.50]  because I know this is something
[1771.50 --> 1773.66]  that Python has worked really hard to,
[1774.00 --> 1774.82]  like in Python 2,
[1774.90 --> 1776.26]  there wasn't really a notion of
[1776.26 --> 1778.02]  all text is one encoding.
[1778.18 --> 1779.16]  Like encodings were kind of,
[1779.50 --> 1780.42]  and Ruby is the same way,
[1780.48 --> 1782.86]  encodings are kind of a property of the string.
[1782.94 --> 1783.86]  And so you can have strings
[1783.86 --> 1784.74]  with different encodings
[1784.74 --> 1786.44]  kind of flowing all through your program.
[1786.50 --> 1787.30]  And it's just something that
[1787.30 --> 1790.96]  we just kind of don't have to deal with in Go.
[1791.04 --> 1791.80]  But most programmers
[1791.80 --> 1793.48]  who are probably coming to Go now,
[1793.68 --> 1795.28]  I would say, if not a majority,
[1795.48 --> 1797.42]  like a certain large percentage of them
[1797.42 --> 1799.54]  come with experience and baggage
[1799.54 --> 1801.66]  and preconceptions from other languages.
[1802.60 --> 1803.96]  And so if anything,
[1805.08 --> 1806.10]  questions like the one I had
[1806.10 --> 1807.30]  about the minus one rune
[1807.30 --> 1809.80]  to kind of help you expose your preconceptions
[1809.80 --> 1811.02]  and say, well, I know,
[1811.12 --> 1812.48]  of course I know the answer is two
[1812.48 --> 1813.14]  because in Java,
[1813.28 --> 1814.90]  every character is two bytes.
[1814.90 --> 1817.30]  And then you find out the answer isn't two.
[1817.84 --> 1818.54]  And you have to ask,
[1818.96 --> 1820.92]  that hopefully prompts other questions of,
[1821.68 --> 1822.46]  why isn't that?
[1822.56 --> 1823.58]  Like my education,
[1823.68 --> 1824.60]  my intuition tells me
[1824.60 --> 1825.70]  that it should be this.
[1826.12 --> 1826.62]  What am I missing?
[1826.86 --> 1827.72]  That's the kind of goal.
[1828.50 --> 1830.12]  Yeah, I think we talked about preconceptions
[1830.12 --> 1830.78]  at the beginning.
[1830.96 --> 1831.92]  And this is sometimes
[1831.92 --> 1833.20]  when you start a new language,
[1833.32 --> 1834.36]  you bring your preconception
[1834.36 --> 1835.88]  from the language you're coming in.
[1836.58 --> 1837.92]  And then when I started with Go,
[1837.98 --> 1839.46]  I wrote a lot of Python in Go.
[1839.72 --> 1840.86]  And it worked, it compiled,
[1841.02 --> 1841.98]  but it wasn't Go.
[1842.26 --> 1843.76]  So I think these quizzes
[1843.76 --> 1844.56]  also help you
[1844.56 --> 1845.88]  break these misconceptions
[1845.88 --> 1846.96]  or preconceptions
[1846.96 --> 1847.58]  and say, no,
[1847.74 --> 1848.78]  we do it differently here.
[1849.18 --> 1850.66]  You touched a little bit
[1850.66 --> 1851.36]  the point of
[1851.36 --> 1852.46]  were you ever convinced
[1852.46 --> 1853.28]  that the solution
[1853.28 --> 1854.78]  that you think is right
[1854.78 --> 1855.74]  is not the right one?
[1856.26 --> 1857.88]  So you shortly mentioned
[1857.88 --> 1859.42]  that the way you explained something
[1859.42 --> 1860.60]  was a kind of led you
[1860.60 --> 1861.66]  to a different way
[1861.66 --> 1862.90]  of thinking about this.
[1863.42 --> 1864.74]  But did somebody ever convince you
[1864.74 --> 1865.48]  actually that
[1865.48 --> 1866.30]  something else
[1866.30 --> 1867.42]  is the right answer?
[1868.02 --> 1868.68]  Oh, well,
[1868.88 --> 1869.76]  back in the early days
[1869.76 --> 1870.88]  of asking pop quizzes,
[1871.44 --> 1872.48]  either like I hadn't figured out
[1872.48 --> 1874.22]  the form or it was just easier
[1874.22 --> 1875.30]  to put them on my blog.
[1876.00 --> 1877.20]  I generally had to like
[1877.20 --> 1878.90]  rewrite the quiz several times
[1878.90 --> 1880.60]  over the course of a bunch of hours.
[1880.70 --> 1881.72]  And there are cases now
[1881.72 --> 1883.42]  where if I get the form
[1883.42 --> 1884.28]  of a pop quiz wrong,
[1884.54 --> 1885.24]  I'll just delete it,
[1885.34 --> 1886.58]  delete it and post it again
[1886.58 --> 1887.32]  or something like that.
[1887.48 --> 1888.20]  So it's just definitely
[1888.20 --> 1889.88]  asking the question
[1889.88 --> 1891.22]  in an unambiguous way
[1891.22 --> 1892.62]  is tricky,
[1892.76 --> 1893.96]  especially when you're trying
[1893.96 --> 1896.86]  to illuminate an edge case.
[1897.00 --> 1898.04]  One of my favorite quizzes,
[1898.04 --> 1899.36]  which completely fails
[1899.36 --> 1900.40]  every time I try to give it
[1900.40 --> 1901.76]  is something along the lines of
[1901.76 --> 1903.30]  it was in the form of like
[1903.30 --> 1904.08]  fix this program
[1904.08 --> 1905.52]  by adding only two characters
[1905.52 --> 1906.48]  or something like that.
[1906.72 --> 1907.38]  Yet for a while,
[1907.48 --> 1908.28]  I tried to have a series
[1908.28 --> 1909.02]  of pop quizzes like
[1909.02 --> 1910.14]  what is the shortest way
[1910.14 --> 1910.84]  to write this
[1910.84 --> 1912.62]  to do a particular thing?
[1913.18 --> 1914.14]  And this was where
[1914.14 --> 1915.76]  knowing bizarre
[1915.76 --> 1916.46]  edge case properties
[1916.46 --> 1916.84]  of language,
[1916.94 --> 1918.04]  like the copy returns
[1918.04 --> 1918.40]  a number,
[1918.46 --> 1919.46]  you can use that to
[1919.46 --> 1920.56]  as a very quick way
[1920.56 --> 1922.28]  of doing the minimum
[1922.28 --> 1923.20]  of two or the maximum
[1923.20 --> 1924.74]  of two different values.
[1924.74 --> 1926.34]  And so that they were
[1926.34 --> 1928.48]  very tricky to get right
[1928.48 --> 1929.94]  because like very,
[1930.00 --> 1930.82]  very kind of tricky
[1930.82 --> 1931.46]  to run code.
[1931.54 --> 1932.48]  The format of like
[1932.48 --> 1933.20]  this very simple,
[1933.66 --> 1934.74]  what this short program
[1934.74 --> 1935.72]  fits in a tweet print
[1935.72 --> 1937.14]  and like the answers
[1937.14 --> 1938.18]  already provided for you
[1938.18 --> 1939.32]  seems to work better
[1939.32 --> 1940.06]  because it kind of
[1940.06 --> 1941.50]  constrains the constraints.
[1941.60 --> 1942.72]  And also it's kind of
[1942.72 --> 1944.10]  easier to verify as well.
[1944.42 --> 1945.34]  I remember always the
[1945.34 --> 1946.38]  do the shortest version
[1946.38 --> 1947.46]  of this for days,
[1947.54 --> 1949.18]  like people like Kevin Gillette
[1949.18 --> 1950.14]  would be sending me like,
[1950.20 --> 1950.94]  well, here's an actual
[1950.94 --> 1951.48]  shorter version
[1951.48 --> 1952.34]  and here's a shorter version
[1952.34 --> 1952.72]  after that
[1952.72 --> 1953.20]  and here's a shorter
[1953.20 --> 1954.08]  version after that.
[1954.08 --> 1954.38]  So it's,
[1955.04 --> 1956.06]  in some ways I think
[1956.06 --> 1957.46]  the point of moving past
[1957.46 --> 1958.98]  like the got it right
[1958.98 --> 1959.60]  or got it wrong
[1959.60 --> 1961.56]  to the thinking about
[1961.56 --> 1962.30]  the potentially
[1962.30 --> 1963.22]  the lesson behind it
[1963.22 --> 1964.52]  is occluded a little bit
[1964.52 --> 1964.88]  when you,
[1965.20 --> 1965.96]  it becomes a competition
[1965.96 --> 1967.06]  like write the shortest version.
[1967.54 --> 1968.14]  And I also like
[1968.14 --> 1968.84]  the kind of poetry
[1968.84 --> 1970.66]  of like the ones
[1970.66 --> 1971.42]  that the quizzes
[1971.42 --> 1971.98]  that always start
[1971.98 --> 1972.58]  with the same form.
[1972.68 --> 1973.80]  What does this program print?
[1974.28 --> 1974.88]  Because I think like
[1974.88 --> 1976.04]  printing is the simplest thing.
[1976.16 --> 1977.16]  Like what's the first program
[1977.16 --> 1977.70]  that everyone writes
[1977.70 --> 1978.34]  in every language?
[1978.64 --> 1979.26]  Hello world,
[1979.40 --> 1979.92]  like hello,
[1980.48 --> 1981.14]  hello go,
[1981.26 --> 1981.72]  hello David.
[1981.84 --> 1983.30]  Like it's the smallest
[1983.30 --> 1983.98]  simplest program
[1983.98 --> 1984.42]  you can write
[1984.42 --> 1985.38]  and all other programs
[1985.38 --> 1986.02]  are going to be bigger
[1986.02 --> 1986.96]  or complicated
[1986.96 --> 1987.78]  or more magnanimous
[1987.78 --> 1988.58]  after that.
[1988.70 --> 1989.72]  So I like the idea
[1989.72 --> 1990.52]  that the quiz space
[1990.52 --> 1991.08]  is just,
[1991.50 --> 1992.74]  it's just the tiniest portion
[1992.74 --> 1993.10]  of like,
[1993.72 --> 1994.54]  we're just talking about
[1994.54 --> 1995.32]  programs that print
[1995.32 --> 1996.00]  one value.
[1996.48 --> 1997.38]  What does this program print?
[1997.72 --> 1999.30]  Because the solution space
[1999.30 --> 2000.44]  of other programs
[2000.44 --> 2001.36]  is so much larger
[2001.36 --> 2001.82]  than that.
[2002.28 --> 2003.10]  Yeah, for me,
[2003.26 --> 2003.84]  several times
[2003.84 --> 2004.66]  I thought I knew
[2004.66 --> 2005.34]  the right answer
[2005.34 --> 2006.44]  for a quiz
[2006.44 --> 2007.42]  I showed to people
[2007.42 --> 2009.16]  and as Linus says,
[2009.28 --> 2010.32]  given enough eyeballs,
[2010.44 --> 2011.14]  all bugs are shallow.
[2011.14 --> 2012.52]  So when you do a quiz
[2012.52 --> 2013.30]  for a lot of people,
[2013.58 --> 2014.40]  they will correct you.
[2014.46 --> 2015.06]  I remember one
[2015.06 --> 2016.68]  when I did about
[2016.68 --> 2017.90]  greedy regular expressions
[2017.90 --> 2019.50]  in a local Python group
[2019.50 --> 2021.00]  and I did an explanation
[2021.00 --> 2022.06]  and then someone
[2022.06 --> 2023.24]  who has a long history
[2023.24 --> 2024.10]  of regular expression,
[2024.24 --> 2024.46]  Pearl,
[2024.68 --> 2025.40]  raised their hand
[2025.40 --> 2025.70]  and said,
[2025.90 --> 2026.20]  no, no,
[2026.48 --> 2027.44]  let me give you
[2027.44 --> 2028.30]  a counter example
[2028.30 --> 2029.06]  for what you're saying.
[2029.66 --> 2031.02]  I think the fun part is
[2031.02 --> 2032.16]  even when you're teaching
[2032.16 --> 2032.92]  or even when you're
[2032.92 --> 2033.82]  showing these things,
[2033.98 --> 2034.68]  you might learn
[2034.68 --> 2035.34]  something as well.
[2035.42 --> 2036.26]  Even though you think
[2036.26 --> 2037.10]  you know what you're doing,
[2037.30 --> 2038.40]  it's not necessarily right.
[2039.20 --> 2039.56]  Absolutely.
[2039.80 --> 2040.86]  To go back to
[2040.86 --> 2041.86]  the kind of inspiration
[2041.86 --> 2042.86]  of the Josh Bloch
[2042.86 --> 2044.14]  Jet Java Puzzlers book,
[2044.60 --> 2045.10]  as I said before,
[2045.16 --> 2045.94]  the bit that I enjoyed
[2045.94 --> 2046.86]  the most about that
[2046.86 --> 2048.44]  was not the competition
[2048.44 --> 2049.16]  of like how many
[2049.16 --> 2049.94]  out of 50 points
[2049.94 --> 2050.86]  did I get right
[2050.86 --> 2051.56]  on the first try.
[2051.64 --> 2052.80]  It was the,
[2052.92 --> 2053.74]  let me explain to you
[2053.74 --> 2055.00]  why you might have
[2055.00 --> 2055.52]  got this wrong.
[2055.60 --> 2056.62]  Like the explanation part
[2056.62 --> 2057.52]  was the far more vague.
[2057.60 --> 2058.42]  It's the bit that I miss
[2058.42 --> 2060.14]  from when I would give,
[2060.52 --> 2061.42]  I have this broken
[2061.42 --> 2062.76]  Go present slide deck
[2062.76 --> 2064.32]  that has been re-edited
[2064.32 --> 2065.46]  and re-edited so many times
[2065.46 --> 2066.04]  because every time
[2066.04 --> 2066.72]  I'll go to a meetup,
[2066.78 --> 2067.62]  I'd like delete
[2067.62 --> 2068.34]  some of the old ones
[2068.34 --> 2069.38]  add some new ones
[2069.38 --> 2070.58]  like maybe trim it for time,
[2071.16 --> 2072.14]  been through so many iterations.
[2072.34 --> 2073.10]  The thing about Go present
[2073.10 --> 2074.04]  is that you have to give
[2074.04 --> 2074.88]  every slide a title
[2074.88 --> 2076.64]  and so there would be
[2076.64 --> 2077.42]  a slide with the quiz
[2077.42 --> 2078.80]  and then I would always
[2078.80 --> 2079.74]  copy the title
[2079.74 --> 2080.70]  and put in brackets
[2080.70 --> 2081.40]  continued.
[2082.46 --> 2083.48]  And so my favorite part
[2083.48 --> 2084.50]  was always the second slide
[2084.50 --> 2085.10]  which is the,
[2085.42 --> 2086.12]  not just the answer
[2086.12 --> 2086.80]  but the explanation
[2086.80 --> 2088.20]  for why it is.
[2088.44 --> 2089.18]  Like the one that
[2089.18 --> 2089.98]  was always my favorite
[2089.98 --> 2091.38]  was there's a bunch of,
[2091.46 --> 2092.52]  this is around identifiers.
[2092.76 --> 2093.32]  We all know that
[2093.32 --> 2094.84]  identifiers have to start
[2094.84 --> 2096.02]  with whatever Unicode
[2096.02 --> 2096.76]  defines as a letter
[2096.76 --> 2097.76]  or the underscore
[2097.76 --> 2099.00]  which includes
[2099.00 --> 2100.98]  a lot of pre-emoji characters.
[2101.36 --> 2101.74]  In Japanese,
[2101.84 --> 2102.04]  they're called
[2102.04 --> 2102.56]  Kaomoji
[2102.56 --> 2104.06]  or K-A-O
[2104.06 --> 2105.66]  Kaomoji
[2105.66 --> 2106.62]  which is like
[2106.62 --> 2107.66]  kind of typing faces.
[2108.10 --> 2108.58]  If everyone knows
[2108.58 --> 2109.56]  the flipping table meme,
[2109.88 --> 2110.90]  it's that class of thing
[2110.90 --> 2111.88]  like the frowny eyes.
[2112.36 --> 2112.70]  It turns out
[2112.70 --> 2113.36]  the frowny eyes
[2113.36 --> 2114.86]  is a valid identifier
[2114.86 --> 2116.42]  because the
[2116.42 --> 2117.22]  kind of O
[2117.22 --> 2117.90]  with a dot in the middle
[2117.90 --> 2118.82]  and a kind of little eyebrow
[2118.82 --> 2120.24]  is a character called Thar
[2120.24 --> 2121.18]  which I think
[2121.18 --> 2122.48]  is Greek or Turkish
[2122.48 --> 2124.42]  and so that's a letter
[2124.42 --> 2125.54]  so you can totally have
[2125.54 --> 2126.28]  an identifier
[2126.28 --> 2127.84]  which is this kind of
[2127.84 --> 2128.82]  frowny side eyes.
[2129.52 --> 2130.20]  But like the
[2130.20 --> 2131.12]  that explanation
[2131.12 --> 2132.02]  like explaining
[2132.02 --> 2133.16]  even though
[2133.16 --> 2133.76]  it's not just
[2133.76 --> 2134.94]  kind of Roman
[2134.94 --> 2135.44]  or Cyrillic
[2135.44 --> 2136.14]  alphanumerics
[2136.14 --> 2136.78]  but also
[2136.78 --> 2138.02]  a great,
[2138.18 --> 2138.96]  when we say a letter
[2138.96 --> 2139.72]  this includes
[2139.72 --> 2141.20]  all of the written languages
[2141.20 --> 2142.48]  Hebrew,
[2142.92 --> 2143.26]  Turkish,
[2143.44 --> 2143.76]  Japanese,
[2143.94 --> 2144.96]  like these are all letters.
[2145.28 --> 2145.96]  Not all of them will be
[2145.96 --> 2146.80]  uppercase letters
[2146.80 --> 2147.86]  but they will all be letters
[2147.86 --> 2148.18]  and so
[2148.18 --> 2149.38]  you can write
[2149.38 --> 2151.12]  identifiers in your Go code
[2151.12 --> 2152.30]  in your native tongue
[2152.30 --> 2153.24]  and also
[2153.24 --> 2154.16]  just kind of also
[2154.16 --> 2155.26]  highlight that
[2155.26 --> 2156.18]  you're not restricted
[2156.18 --> 2157.16]  to speaking about source code
[2157.16 --> 2157.88]  only in English.
[2158.44 --> 2159.10]  I really like that
[2159.10 --> 2159.92]  explanation part
[2159.92 --> 2161.30]  of explaining
[2161.30 --> 2162.78]  why the frowny face
[2162.78 --> 2163.62]  is totally valid.
[2163.82 --> 2164.46]  You can have a variable
[2164.46 --> 2165.86]  called frowny side eyes.
[2166.86 --> 2167.84]  Pop question,
[2168.04 --> 2168.52]  pop quizzes
[2168.52 --> 2170.06]  is job interviews.
[2170.50 --> 2170.98]  Good idea
[2170.98 --> 2171.68]  or a bad idea?
[2172.44 --> 2172.96]  Terrible idea.
[2173.08 --> 2173.60]  Very unfair.
[2174.04 --> 2175.30]  Job interviews are not fun
[2175.30 --> 2176.54]  and pop quizzes
[2176.54 --> 2177.24]  are supposed to be fun
[2177.24 --> 2178.92]  so do not mix the two.
[2179.40 --> 2179.48]  Yeah,
[2179.64 --> 2180.14]  I have
[2180.14 --> 2181.22]  quite often
[2181.22 --> 2181.82]  people will comment
[2181.82 --> 2182.20]  you know
[2182.20 --> 2183.12]  like if I got this
[2183.12 --> 2183.88]  in a job interview
[2183.88 --> 2184.80]  like I would have failed
[2184.80 --> 2186.06]  or something like that.
[2186.14 --> 2186.34]  You know,
[2186.80 --> 2188.06]  it's unfair for two reasons.
[2188.60 --> 2188.96]  One,
[2189.24 --> 2189.52]  the form.
[2189.62 --> 2190.54]  If you would just guess
[2190.54 --> 2191.58]  you have a one in four chance
[2191.58 --> 2192.62]  like that's terrible
[2192.62 --> 2193.68]  but also
[2193.68 --> 2195.36]  there's a terrible power imbalance
[2195.36 --> 2196.02]  and there's already
[2196.02 --> 2197.36]  like in the interview situation
[2197.36 --> 2198.08]  the power imbalances
[2198.08 --> 2198.54]  are already
[2198.54 --> 2199.88]  terribly off the scale
[2199.88 --> 2200.74]  but there's this terrible
[2200.74 --> 2201.30]  power imbalance
[2201.30 --> 2203.34]  that as the asker
[2203.34 --> 2204.70]  you know the answer.
[2204.86 --> 2205.46]  You wrote the question
[2205.46 --> 2206.22]  you probably wrote the
[2206.22 --> 2207.80]  especially in the kind of
[2207.80 --> 2208.62]  tweet sized
[2208.62 --> 2210.14]  pop quiz form
[2210.14 --> 2211.58]  they're written away
[2211.58 --> 2212.94]  to either confuse
[2212.94 --> 2213.96]  or perhaps obfuscate
[2213.96 --> 2214.32]  a little bit
[2214.32 --> 2215.22]  and none of those things
[2215.22 --> 2215.60]  are fair.
[2216.26 --> 2216.96]  Terrible tool
[2216.96 --> 2218.46]  and also the most important bit
[2218.46 --> 2219.30]  is like
[2219.30 --> 2220.58]  if these are some
[2220.58 --> 2221.50]  pop quizzes
[2221.50 --> 2222.48]  some kind of like
[2222.48 --> 2223.56]  do this multiple choice
[2223.56 --> 2224.46]  as part of your
[2224.46 --> 2225.10]  kind of interview pack
[2225.10 --> 2225.96]  do this multiple choice
[2225.96 --> 2226.46]  set of questions
[2226.46 --> 2227.74]  where's the learning in that?
[2228.56 --> 2229.30]  It's simply like
[2229.30 --> 2230.00]  can you solve
[2230.00 --> 2231.04]  these quick number puzzles
[2231.04 --> 2231.84]  quickly?
[2231.98 --> 2232.38]  There's no
[2232.38 --> 2233.36]  that the value
[2233.36 --> 2233.94]  of the pop quizzes
[2233.94 --> 2235.64]  is the educational component
[2235.64 --> 2236.38]  that comes after that
[2236.38 --> 2236.64]  of saying
[2236.64 --> 2238.04]  well I got the wrong answer
[2238.04 --> 2239.28]  and now
[2239.28 --> 2241.26]  I'm confused by that
[2241.26 --> 2242.20]  like why is that?
[2242.30 --> 2243.34]  Like I mean
[2243.34 --> 2244.54]  yesterday a number of people
[2244.54 --> 2244.88]  were saying
[2244.88 --> 2245.62]  well how can you have
[2245.62 --> 2246.96]  a negative one letter?
[2247.24 --> 2247.96]  Like that doesn't make
[2247.96 --> 2248.42]  any sense
[2248.42 --> 2249.94]  and so that was an opportunity
[2249.94 --> 2250.46]  to explain
[2250.46 --> 2251.10]  well it turns out
[2251.10 --> 2252.04]  that rune is actually
[2252.04 --> 2253.08]  an alias
[2253.08 --> 2254.44]  and aliases
[2254.44 --> 2255.00]  are not
[2255.00 --> 2256.90]  the horrible alias keyword
[2256.90 --> 2257.68]  we added a few
[2257.68 --> 2258.40]  versions ago
[2258.40 --> 2260.00]  but this idea of
[2260.00 --> 2261.60]  a type has another name
[2261.60 --> 2262.88]  and this is a thing
[2262.88 --> 2263.70]  which also
[2263.70 --> 2264.58]  comes up
[2264.58 --> 2265.48]  quite infrequently
[2265.48 --> 2265.80]  in Go
[2265.80 --> 2267.18]  because we know
[2267.18 --> 2267.84]  that like
[2267.84 --> 2269.16]  int 64 and int
[2269.16 --> 2270.96]  are the same type
[2270.96 --> 2272.46]  mostly under the hood
[2272.46 --> 2273.92]  but they're not transposable
[2273.92 --> 2274.80]  if you have an int 64
[2274.80 --> 2275.68]  you have to cast it
[2275.68 --> 2276.54]  to an int
[2276.54 --> 2278.62]  but when you have a rune
[2278.62 --> 2279.50]  and an int 32
[2279.50 --> 2280.80]  they can
[2280.80 --> 2281.96]  transparently be
[2281.96 --> 2283.14]  because they're actually
[2283.14 --> 2283.82]  aliases
[2283.82 --> 2284.50]  the same for
[2284.50 --> 2285.36]  byte and utf
[2285.36 --> 2286.34]  and byte and
[2286.34 --> 2287.18]  uint 8
[2287.18 --> 2288.56]  so
[2288.56 --> 2290.44]  that was an opportunity
[2290.44 --> 2291.08]  to explain
[2291.08 --> 2291.96]  a thing about like
[2291.96 --> 2293.46]  the rune characters
[2293.46 --> 2294.38]  the rune type
[2294.38 --> 2295.04]  is probably something
[2295.04 --> 2296.26]  that not a lot of people
[2296.26 --> 2296.84]  have come up with
[2296.84 --> 2297.48]  especially like
[2297.48 --> 2298.42]  if you're parsing
[2298.42 --> 2298.98]  network data
[2298.98 --> 2300.30]  you're getting in bytes
[2300.30 --> 2302.10]  it's not strictly ASCII
[2302.10 --> 2302.88]  but you can kind of
[2302.88 --> 2303.66]  most of the time
[2303.66 --> 2304.72]  ignore that
[2304.72 --> 2305.26]  and just kind of
[2305.26 --> 2305.96]  treat it like ASCII
[2305.96 --> 2306.84]  so byte will work
[2306.84 --> 2307.68]  but actually
[2307.68 --> 2308.82]  strings are runes
[2308.82 --> 2310.48]  so it was an opportunity
[2310.48 --> 2310.98]  to
[2310.98 --> 2312.96]  explain that a little bit
[2312.96 --> 2314.14]  so yeah
[2314.14 --> 2314.98]  to summarize
[2314.98 --> 2315.36]  yes
[2315.36 --> 2316.34]  pop quizzes
[2316.34 --> 2317.18]  terrible tool
[2317.18 --> 2317.68]  for interviewing
[2317.68 --> 2318.34]  like that's just
[2318.34 --> 2318.76]  unfair
[2318.76 --> 2319.74]  and also
[2319.74 --> 2320.42]  like it's
[2320.42 --> 2321.36]  you're missing
[2321.36 --> 2322.20]  the most important bit
[2322.20 --> 2322.80]  which is the
[2322.80 --> 2324.28]  the opportunity to
[2324.28 --> 2325.54]  say oh well
[2325.54 --> 2326.46]  I got that wrong
[2326.46 --> 2327.40]  why
[2327.40 --> 2328.22]  to ask that
[2328.22 --> 2329.04]  question why
[2329.04 --> 2347.46]  what's up gophers
[2347.46 --> 2348.32]  this episode
[2348.32 --> 2349.18]  is brought to you
[2349.18 --> 2349.82]  by friends
[2349.82 --> 2350.50]  at teleport
[2350.50 --> 2351.46]  with teleport
[2351.46 --> 2352.38]  access plane
[2352.38 --> 2352.94]  you can quickly
[2352.94 --> 2353.86]  access any
[2353.86 --> 2354.60]  computing resource
[2354.60 --> 2355.24]  anywhere
[2355.24 --> 2356.16]  engineers
[2356.16 --> 2357.16]  and security teams
[2357.16 --> 2357.88]  can unify access
[2357.88 --> 2359.08]  to SSH servers
[2359.08 --> 2360.10]  kubernetes clusters
[2360.10 --> 2361.12]  web applications
[2361.12 --> 2362.10]  and databases
[2362.10 --> 2363.42]  across all environments
[2363.42 --> 2364.02]  teleport
[2364.02 --> 2365.30]  is open core
[2365.30 --> 2365.90]  which you can use
[2365.90 --> 2366.38]  for free
[2366.38 --> 2367.16]  and it's supported
[2367.16 --> 2367.74]  by their cloud
[2367.74 --> 2368.50]  hosted version
[2368.50 --> 2369.36]  which lets you forget
[2369.36 --> 2370.18]  about configuring
[2370.18 --> 2370.86]  updating
[2370.86 --> 2372.26]  or managing teleport
[2372.26 --> 2373.16]  the teleport team
[2373.16 --> 2374.22]  does all that for you
[2374.22 --> 2375.26]  your team can focus
[2375.26 --> 2376.08]  on your projects
[2376.08 --> 2377.32]  and spend less time
[2377.32 --> 2377.76]  worrying about
[2377.76 --> 2379.08]  infrastructure access
[2379.08 --> 2379.92]  try teleport
[2379.92 --> 2380.78]  today in the cloud
[2380.78 --> 2381.64]  self hosted
[2381.64 --> 2382.94]  or open source
[2382.94 --> 2383.58]  head to
[2383.58 --> 2384.56]  go teleport.com
[2384.56 --> 2385.18]  to learn more
[2385.18 --> 2385.98]  and get started
[2385.98 --> 2386.64]  again
[2386.64 --> 2388.02]  go teleport.com
[2388.02 --> 2401.56]  I agree with you
[2401.56 --> 2402.62]  I think it's a bad
[2402.62 --> 2403.22]  thing to do
[2403.22 --> 2403.74]  in interviews
[2403.74 --> 2405.04]  mostly because
[2405.04 --> 2405.62]  I don't think
[2405.62 --> 2406.38]  as an interviewer
[2406.38 --> 2406.86]  you learn
[2406.86 --> 2408.04]  something valuable
[2408.04 --> 2408.86]  about the candidate
[2408.86 --> 2409.94]  when they face that
[2409.94 --> 2410.76]  either they know it
[2410.76 --> 2411.50]  or they don't
[2411.50 --> 2412.14]  usually have
[2412.14 --> 2412.96]  enough time
[2412.96 --> 2413.40]  to go
[2413.40 --> 2414.64]  over the internet
[2414.64 --> 2415.42]  and read the spec
[2415.42 --> 2416.42]  and see what's going on
[2416.42 --> 2417.44]  maybe play with the code
[2417.44 --> 2418.30]  they don't have it
[2418.30 --> 2419.18]  during the interview
[2419.18 --> 2419.74]  situation
[2419.74 --> 2420.92]  so either they know
[2420.92 --> 2421.44]  it or not
[2421.44 --> 2422.60]  and that's basically
[2422.60 --> 2423.50]  maybe their memory
[2423.50 --> 2424.54]  but nothing more
[2424.54 --> 2424.88]  than that
[2424.88 --> 2425.66]  and it's also
[2425.66 --> 2426.36]  as you mentioned
[2426.36 --> 2426.98]  very stressful
[2426.98 --> 2428.46]  like I have no idea
[2428.46 --> 2429.08]  what it is
[2429.08 --> 2429.72]  why is that
[2429.72 --> 2430.98]  so they're forced
[2430.98 --> 2431.88]  to invent something
[2431.88 --> 2433.12]  which I personally
[2433.12 --> 2433.56]  don't like
[2433.56 --> 2435.02]  and completely artificial
[2435.02 --> 2436.84]  to the entire way
[2436.84 --> 2437.46]  that you would work
[2437.46 --> 2438.26]  and perform your job
[2438.26 --> 2439.56]  to not get too far
[2439.56 --> 2439.98]  into attention
[2439.98 --> 2440.56]  about hiring
[2440.56 --> 2441.80]  like one of my
[2441.80 --> 2442.22]  favorite things
[2442.22 --> 2442.78]  is to watch
[2442.78 --> 2444.08]  machinist videos
[2444.08 --> 2444.54]  on YouTube
[2444.54 --> 2445.64]  people using
[2445.64 --> 2446.52]  blades
[2446.52 --> 2447.30]  and drills
[2447.30 --> 2447.70]  and things like
[2447.70 --> 2447.84]  that
[2447.84 --> 2448.40]  to make things
[2448.40 --> 2448.76]  and I'm sure
[2448.76 --> 2449.14]  if you were
[2449.14 --> 2449.88]  interviewing for a job
[2449.88 --> 2450.58]  as a machinist
[2450.58 --> 2451.88]  you wouldn't sit down
[2451.88 --> 2452.36]  and have a long
[2452.36 --> 2452.92]  discussion about
[2452.92 --> 2453.66]  material science
[2453.66 --> 2454.94]  you'd tuck some
[2454.94 --> 2456.04]  bar stock up in the lathe
[2456.04 --> 2456.68]  and you would turn
[2456.68 --> 2457.10]  the part
[2457.10 --> 2457.94]  as described
[2457.94 --> 2458.38]  and then people
[2458.38 --> 2458.66]  would say
[2458.66 --> 2459.52]  well did you
[2459.52 --> 2460.34]  do a reasonable
[2460.34 --> 2460.82]  job at that
[2460.82 --> 2461.34]  were you fast
[2461.34 --> 2462.22]  wastage
[2462.22 --> 2462.80]  things like that
[2462.80 --> 2464.20]  so that does
[2464.20 --> 2465.08]  on surface
[2465.08 --> 2465.88]  sound a little bit
[2465.88 --> 2466.70]  like doing whiteboard
[2466.70 --> 2467.04]  coding
[2467.04 --> 2468.12]  like you're doing
[2468.12 --> 2468.42]  the thing
[2468.42 --> 2469.56]  but the key
[2469.56 --> 2470.02]  is you're doing
[2470.02 --> 2470.82]  it in the environment
[2470.82 --> 2471.38]  you're not talking
[2471.38 --> 2471.58]  about
[2471.58 --> 2472.58]  I would remember
[2472.58 --> 2473.42]  to set the speed
[2473.42 --> 2473.94]  on the machine
[2473.94 --> 2475.22]  to X and Y
[2475.22 --> 2476.42]  so I think
[2476.42 --> 2476.94]  the pop quiz
[2476.94 --> 2477.82]  format taken out
[2477.82 --> 2478.36]  is just like
[2478.36 --> 2479.26]  here's a tiny piece
[2479.26 --> 2479.66]  of text
[2479.66 --> 2480.36]  and four answers
[2480.36 --> 2481.46]  circle one of them
[2481.46 --> 2482.56]  is so artificial
[2482.56 --> 2483.74]  of course if you
[2483.74 --> 2484.24]  got the answer
[2484.24 --> 2485.04]  the first thing
[2485.04 --> 2485.36]  you do
[2485.36 --> 2486.26]  copy that text
[2486.26 --> 2486.96]  put it in your editor
[2486.96 --> 2487.46]  run it
[2487.46 --> 2488.68]  change it
[2488.68 --> 2489.50]  explore it
[2489.50 --> 2490.06]  pull it apart
[2490.06 --> 2490.70]  which is the
[2490.70 --> 2491.62]  key to learning
[2491.62 --> 2492.34]  to like dissect
[2492.34 --> 2492.74]  something
[2492.74 --> 2494.44]  so I agree a lot
[2494.44 --> 2495.10]  that it's stressful
[2495.10 --> 2495.70]  and artificial
[2495.70 --> 2497.00]  and unfair
[2497.00 --> 2498.10]  so I would like
[2498.10 --> 2498.66]  to turn the
[2498.66 --> 2499.92]  situation a little bit
[2499.92 --> 2501.50]  and ask
[2501.50 --> 2502.24]  you are all
[2502.24 --> 2502.76]  in the position
[2502.76 --> 2503.50]  of interviewers
[2503.50 --> 2504.22]  your old position
[2504.22 --> 2505.44]  of interviewees
[2505.44 --> 2507.12]  if you
[2507.12 --> 2508.24]  as an interviewer
[2508.24 --> 2509.32]  get a pop quiz
[2509.32 --> 2510.24]  question at the end
[2510.24 --> 2511.62]  from an interviewee
[2511.62 --> 2512.10]  at the part
[2512.10 --> 2512.58]  that you ask
[2512.58 --> 2513.42]  do you have a question
[2513.42 --> 2513.82]  for me
[2513.82 --> 2514.64]  is that okay
[2514.64 --> 2516.90]  I think so
[2516.90 --> 2517.30]  yes
[2517.30 --> 2518.50]  because for me
[2518.50 --> 2519.38]  it's less stressful
[2519.38 --> 2520.84]  and it might show
[2520.84 --> 2521.88]  them the depth
[2521.88 --> 2523.04]  of the knowledge
[2523.04 --> 2523.66]  of the team
[2523.66 --> 2524.50]  or the people
[2524.50 --> 2524.98]  they are going
[2524.98 --> 2525.84]  to interact with
[2525.84 --> 2526.86]  and maybe
[2526.86 --> 2527.26]  you know
[2527.26 --> 2527.96]  they just want
[2527.96 --> 2528.90]  to get close
[2528.90 --> 2529.62]  on a social level
[2529.62 --> 2530.44]  so for me
[2530.44 --> 2530.78]  it's fine
[2530.78 --> 2531.58]  I would buy it
[2531.58 --> 2532.70]  as a fun social thing
[2532.70 --> 2533.90]  I would view it
[2533.90 --> 2535.04]  as it's almost
[2535.04 --> 2535.62]  like they have
[2535.62 --> 2536.50]  some obscure knowledge
[2536.50 --> 2536.92]  that they want
[2536.92 --> 2537.28]  to share
[2537.28 --> 2538.18]  and like the pop quiz
[2538.18 --> 2539.04]  is like a fun format
[2539.04 --> 2539.66]  of sharing it
[2539.66 --> 2540.52]  so to me
[2540.52 --> 2540.88]  it would show
[2540.88 --> 2541.64]  that they were excited
[2541.64 --> 2542.14]  and they want to
[2542.14 --> 2542.66]  share something
[2542.66 --> 2543.42]  they learned
[2543.42 --> 2544.12]  so like that's
[2544.12 --> 2544.56]  a good thing
[2544.56 --> 2545.68]  and it's not
[2545.68 --> 2546.18]  like they're saying
[2546.18 --> 2546.88]  like oh you're
[2546.88 --> 2547.32]  you're going to get
[2547.32 --> 2547.86]  fired if you don't
[2547.86 --> 2548.16]  know this
[2548.16 --> 2548.70]  like it's not
[2548.70 --> 2549.56]  that stress
[2549.56 --> 2550.04]  whereas like
[2550.04 --> 2550.42]  somebody who's
[2550.42 --> 2550.82]  interviewing
[2550.82 --> 2551.78]  even if you
[2551.78 --> 2552.30]  just ask it
[2552.30 --> 2552.96]  as like oh
[2552.96 --> 2553.76]  a fun little intro
[2553.76 --> 2554.54]  here's a pop quiz
[2554.54 --> 2555.14]  it's still like
[2555.14 --> 2555.88]  a stressful scenario
[2555.88 --> 2556.30]  for them
[2556.30 --> 2556.72]  and they're going
[2556.72 --> 2557.06]  to go home
[2557.06 --> 2557.72]  thinking oh I got
[2557.72 --> 2558.12]  that wrong
[2558.12 --> 2558.44]  they're never
[2558.44 --> 2558.96]  going to hire me
[2558.96 --> 2559.54]  now like it's
[2559.54 --> 2560.10]  a completely
[2560.10 --> 2561.10]  different environment
[2561.10 --> 2561.44]  there
[2561.44 --> 2563.10]  I have a lot
[2563.10 --> 2563.78]  more questions
[2563.78 --> 2564.38]  that are slowly
[2564.38 --> 2565.40]  running out of time
[2565.40 --> 2568.20]  one last question
[2568.20 --> 2569.26]  and then will be
[2569.26 --> 2569.84]  the fun part
[2569.84 --> 2570.56]  of an unpopular
[2570.56 --> 2571.00]  opinion
[2571.00 --> 2573.44]  so we talk
[2573.44 --> 2574.18]  about pop quizzes
[2574.18 --> 2575.04]  as part of an
[2575.04 --> 2575.94]  interview process
[2575.94 --> 2577.36]  maybe yes
[2577.36 --> 2577.82]  if you are
[2577.82 --> 2578.70]  on the interviewee
[2578.70 --> 2579.14]  side
[2579.14 --> 2580.18]  pop quizzes
[2580.18 --> 2581.24]  as part of
[2581.24 --> 2582.32]  learning a language
[2582.32 --> 2583.88]  syllabus of a
[2583.88 --> 2584.52]  course are just
[2584.52 --> 2585.20]  for you to do
[2585.20 --> 2586.68]  when you freely
[2586.68 --> 2587.46]  take a language
[2587.46 --> 2588.38]  to learn upon you
[2588.38 --> 2589.74]  do you teach that
[2589.74 --> 2590.18]  do you like
[2590.18 --> 2590.96]  learning with that
[2590.96 --> 2592.08]  I'm for it
[2592.08 --> 2592.96]  I'm doing several
[2592.96 --> 2593.92]  ways of teaching
[2593.92 --> 2594.74]  people and every
[2594.74 --> 2595.52]  time at the end
[2595.52 --> 2596.20]  giving them
[2596.20 --> 2597.14]  something to think
[2597.14 --> 2598.02]  about which is
[2598.02 --> 2599.02]  related to the
[2599.02 --> 2599.90]  subject is usually
[2599.90 --> 2600.50]  something that
[2600.50 --> 2601.30]  strengthens their
[2601.30 --> 2602.50]  understanding and
[2602.50 --> 2603.70]  makes them better
[2603.70 --> 2605.22]  learning so I
[2605.22 --> 2605.82]  think it's a good
[2605.82 --> 2606.82]  idea to have some
[2606.82 --> 2607.52]  kind of a question
[2607.52 --> 2608.70]  at the end that
[2608.70 --> 2609.56]  see if you got it
[2609.56 --> 2610.30]  or not and I
[2610.30 --> 2611.02]  think quizzes are a
[2611.02 --> 2611.82]  great match because
[2611.82 --> 2613.82]  apart from related
[2613.82 --> 2614.40]  to the subject
[2614.40 --> 2615.20]  they're also fun
[2615.20 --> 2616.20]  and they also
[2616.20 --> 2616.86]  encourage you to
[2616.86 --> 2617.64]  explore more so
[2617.64 --> 2618.50]  yeah for sure
[2618.50 --> 2619.68]  I think part of
[2619.68 --> 2620.44]  it is definitely
[2620.44 --> 2621.66]  the atmosphere
[2621.66 --> 2622.90]  of it like I
[2622.90 --> 2623.32]  don't know like if
[2623.32 --> 2623.82]  it was like a
[2623.82 --> 2624.50]  learning materials
[2624.50 --> 2624.90]  and you had to
[2624.90 --> 2625.76]  get the quiz 100%
[2625.76 --> 2626.24]  before you can
[2626.24 --> 2626.72]  move on that
[2626.72 --> 2627.04]  would probably
[2627.04 --> 2627.88]  frustrate me like
[2627.88 --> 2628.40]  it would make it
[2628.40 --> 2629.22]  a less enjoyable
[2629.22 --> 2630.56]  experience because
[2630.56 --> 2631.02]  like Dave you
[2631.02 --> 2631.42]  even mentioned
[2631.42 --> 2631.76]  you'll have
[2631.76 --> 2632.26]  quizzes you'll
[2632.26 --> 2632.70]  have like does
[2632.70 --> 2633.28]  not compile as
[2633.28 --> 2634.32]  an answer and
[2634.32 --> 2634.76]  there are times
[2634.76 --> 2635.86]  where I click
[2635.86 --> 2636.58]  that just thinking
[2636.58 --> 2637.94]  my first intuition
[2637.94 --> 2638.54]  is this doesn't
[2638.54 --> 2639.34]  compile but I want
[2639.34 --> 2639.80]  to learn something
[2639.80 --> 2640.84]  from this but
[2640.84 --> 2641.20]  like if you have
[2641.20 --> 2641.70]  a quiz where it's
[2641.70 --> 2642.34]  like a barrier to
[2642.34 --> 2642.90]  moving on it
[2642.90 --> 2643.36]  doesn't feel like
[2643.36 --> 2643.86]  you're having fun
[2643.86 --> 2644.32]  and learning it
[2644.32 --> 2644.84]  feels like you're
[2644.84 --> 2645.76]  just kind of stuck
[2645.76 --> 2646.98]  behind this getting
[2646.98 --> 2647.90]  100% on a quiz
[2647.90 --> 2649.58]  yeah like the goal
[2649.58 --> 2650.52]  is never to like
[2650.52 --> 2651.86]  be the best to
[2651.86 --> 2652.72]  like get 20 out of
[2652.72 --> 2653.28]  20 or something
[2653.28 --> 2653.88]  like that it's
[2653.88 --> 2654.62]  about what you can
[2654.62 --> 2655.30]  learn I think the
[2655.30 --> 2655.94]  quiz format like it
[2655.94 --> 2657.12]  worked I mean I
[2657.12 --> 2657.56]  sound like someone
[2657.56 --> 2658.58]  pining for the
[2658.58 --> 2659.44]  bygone past but
[2659.44 --> 2660.56]  like when we used
[2660.56 --> 2661.06]  to be able to
[2661.06 --> 2662.04]  travel and go to
[2662.04 --> 2662.62]  meetups and things
[2662.62 --> 2663.66]  like that it's a
[2663.66 --> 2664.40]  format that works
[2664.40 --> 2665.74]  really I think works
[2665.74 --> 2666.56]  better than kind of
[2666.56 --> 2667.78]  like Twitter clicking
[2667.78 --> 2668.72]  clicking buttons it
[2668.72 --> 2670.18]  works really well in
[2670.18 --> 2671.68]  the collegiate setting
[2671.68 --> 2672.42]  in a meetup group
[2672.42 --> 2674.08]  because like you can
[2674.08 --> 2674.60]  present the four
[2674.60 --> 2675.10]  answers you can
[2675.10 --> 2675.96]  say let's we would
[2675.96 --> 2676.46]  always do it I
[2676.46 --> 2677.26]  meet up like give a
[2677.26 --> 2679.16]  show of hands and
[2679.16 --> 2680.20]  who thinks A who
[2680.20 --> 2680.96]  thinks B who thinks
[2680.96 --> 2682.08]  C and then you can
[2682.08 --> 2683.88]  ask if there's like a
[2683.88 --> 2684.96]  standout or like if
[2684.96 --> 2685.34]  there's a lot of
[2685.34 --> 2686.12]  people who are
[2686.12 --> 2686.60]  choosing a particular
[2686.60 --> 2687.10]  option just pick
[2687.10 --> 2688.14]  someone say why do
[2688.14 --> 2688.86]  you think that like
[2688.86 --> 2690.68]  explain it and then
[2690.68 --> 2691.78]  they give their answer
[2691.78 --> 2692.28]  and you could pick
[2692.28 --> 2693.08]  someone from a who
[2693.08 --> 2693.82]  had an opposing view
[2693.82 --> 2694.88]  and you have a dialogue
[2694.88 --> 2696.10]  before you even like
[2696.10 --> 2697.12]  haha like the answer
[2697.12 --> 2698.66]  is actually C and let
[2698.66 --> 2699.80]  me just explain to you
[2699.80 --> 2701.12]  the answer like it's a
[2701.12 --> 2702.26]  really good format for
[2702.26 --> 2703.24]  having a discussion and
[2703.24 --> 2704.00]  dialogue which is like
[2704.00 --> 2705.28]  the like that's the
[2705.28 --> 2705.98]  best kind of learning
[2705.98 --> 2706.80]  like rather than just
[2706.80 --> 2707.60]  rote learning like
[2707.60 --> 2708.52]  memorize these answers
[2708.52 --> 2709.92]  it is show you're
[2709.92 --> 2710.60]  working show me your
[2710.60 --> 2711.34]  thought process which
[2711.34 --> 2712.66]  is definitely to tie
[2712.66 --> 2713.24]  back to your earlier
[2713.24 --> 2714.22]  question like the style
[2714.22 --> 2715.94]  of interviewing I think
[2715.94 --> 2717.06]  is more successful at
[2717.06 --> 2718.20]  Heptio we would we did
[2718.20 --> 2718.70]  the thing where we
[2718.70 --> 2719.76]  asked the candidate to
[2719.76 --> 2720.56]  go and do an exercise
[2720.56 --> 2721.58]  and bring it back but
[2721.58 --> 2722.74]  like it wasn't just
[2722.74 --> 2723.74]  like give us a code
[2723.74 --> 2725.06]  look at it if it's
[2725.06 --> 2725.78]  above some kind of
[2725.78 --> 2726.48]  artificial bar which
[2726.48 --> 2726.98]  you won't tell you
[2726.98 --> 2728.26]  about then you
[2728.26 --> 2729.84]  progress it was like the
[2729.84 --> 2730.56]  next step was that you
[2730.56 --> 2731.60]  got on a phone a phone
[2731.60 --> 2732.96]  call with someone someone
[2732.96 --> 2733.40]  who worked at the
[2733.40 --> 2734.26]  company and you would
[2734.26 --> 2734.92]  just talk about the
[2734.92 --> 2736.34]  code just like show me
[2736.34 --> 2737.00]  you're working show me
[2737.00 --> 2737.78]  how you approach this
[2737.78 --> 2739.24]  problem why you chose to
[2739.24 --> 2740.86]  do it this way or that
[2740.86 --> 2742.02]  or like tell me walk me
[2742.02 --> 2742.68]  through your design
[2742.68 --> 2743.54]  interviews are
[2743.54 --> 2744.32]  artificial but I think a
[2744.32 --> 2746.06]  lot closer to the kind
[2746.06 --> 2746.80]  of discourse that you
[2746.80 --> 2748.00]  would have between
[2748.00 --> 2749.14]  co-workers on a team
[2749.14 --> 2750.60]  like let's talk about
[2750.60 --> 2751.10]  how you want to do
[2751.10 --> 2751.70]  this let's talk about
[2751.70 --> 2752.88]  the trade-offs talk
[2752.88 --> 2753.52]  about like some of the
[2753.52 --> 2755.02]  limitations of of that
[2755.02 --> 2755.62]  approach like like oh
[2755.62 --> 2756.26]  that's the kind of
[2756.26 --> 2756.80]  discussion you would
[2756.80 --> 2758.06]  have building or
[2758.06 --> 2758.72]  maintaining a service
[2758.72 --> 2760.22]  on team interviews are
[2760.22 --> 2761.32]  artificial but perhaps
[2761.32 --> 2762.06]  close to the real one
[2762.06 --> 2762.80]  and also it's a
[2762.80 --> 2763.96]  discussion between two
[2763.96 --> 2764.88]  people about the code
[2764.88 --> 2766.38]  rather than simply what
[2766.38 --> 2766.90]  you wrote was good
[2766.90 --> 2767.80]  enough move on to the
[2767.80 --> 2768.86]  next question kind of
[2768.86 --> 2770.92]  thing yeah so many
[2770.92 --> 2771.82]  questions but we should
[2771.82 --> 2773.30]  be wrapping up and I
[2773.30 --> 2774.18]  would say it's time for
[2774.18 --> 2775.46]  an unpopular opinion but
[2775.46 --> 2776.48]  I guess we already have
[2776.48 --> 2777.50]  one that we all agree on
[2777.50 --> 2778.92]  so we can just call it a
[2778.92 --> 2782.30]  day maybe after all yes
[2782.30 --> 2784.14]  an unpopular opinion
[2784.14 --> 2803.20]  so who wants to start with
[2803.20 --> 2804.84]  unpopular opinions I can
[2804.84 --> 2806.12]  start all right Mickey so
[2806.12 --> 2807.94]  my unpopular opinion is
[2807.94 --> 2809.24]  that you should never use a
[2809.24 --> 2810.66]  technology that is less than
[2810.66 --> 2813.26]  seven years old okay is
[2813.26 --> 2813.96]  this based on your
[2813.96 --> 2814.98]  experience when starting
[2814.98 --> 2819.06]  go earlier yeah so of
[2819.06 --> 2820.34]  course I started go at the
[2820.34 --> 2821.88]  very beginning so yeah I
[2821.88 --> 2822.70]  don't listen to my own
[2822.70 --> 2825.04]  advices of course but I've
[2825.04 --> 2826.24]  been burned so many times
[2826.24 --> 2827.06]  by the new and shiny
[2827.06 --> 2828.64]  things and seven years it's
[2828.64 --> 2829.62]  usually production seven
[2829.62 --> 2831.08]  years will make your life
[2831.08 --> 2833.06]  so much easier I worked at
[2833.06 --> 2834.16]  the company that my boss
[2834.16 --> 2835.72]  said my goal in life is
[2835.72 --> 2837.76]  never to be paged at 4 a.m.
[2837.76 --> 2840.34]  so he built everything on
[2840.34 --> 2843.56]  files in all technologies
[2843.56 --> 2845.70]  and he was right we never
[2845.70 --> 2847.10]  got the pager it was just
[2847.10 --> 2849.20]  working so I'm trying to
[2849.20 --> 2851.78]  follow this opinion this is
[2851.78 --> 2852.98]  Dan McKinley's innovation
[2852.98 --> 2855.36]  tokens yes exactly if you're
[2855.36 --> 2856.16]  someone out there in radio
[2856.16 --> 2857.32]  land who doesn't know what
[2857.32 --> 2858.28]  I'm talking about you need
[2858.28 --> 2860.12]  to google Dan McKinley
[2860.12 --> 2861.94]  choose boring technology and
[2861.94 --> 2864.30]  turns to and really take this
[2864.30 --> 2865.68]  idea of innovation tokens and
[2865.68 --> 2866.54]  really take it to heart
[2866.54 --> 2868.48]  because really seriously you
[2868.48 --> 2869.98]  get three you get three
[2869.98 --> 2870.96]  innovation tokens per
[2870.96 --> 2873.50]  project and if you spend
[2873.50 --> 2875.22]  them all up front you have
[2875.22 --> 2877.02]  none left so as I've got
[2877.02 --> 2877.72]  more mature in this
[2877.72 --> 2879.00]  industry yeah like the idea
[2879.00 --> 2880.42]  of using the latest shiny
[2880.42 --> 2882.20]  thing has gone from being
[2882.20 --> 2883.66]  kind of like this is
[2883.66 --> 2885.00]  exciting to being this is
[2885.00 --> 2887.74]  concerning so we became
[2887.74 --> 2888.92]  old geezers that's what
[2888.92 --> 2891.16]  you're saying yep which is
[2891.16 --> 2892.04]  fine because there should be
[2892.04 --> 2893.98]  people to replace us this was
[2893.98 --> 2895.36]  something I was super
[2895.36 --> 2896.76]  passionate about every year
[2896.76 --> 2897.86]  when we would be choosing
[2897.86 --> 2898.88]  the speakers for go for
[2898.88 --> 2900.62]  cotton like if it's just the
[2900.62 --> 2903.62]  same old heads on stage
[2903.62 --> 2904.98]  that's not a community that's
[2904.98 --> 2906.76]  not growth that is stagnation
[2906.76 --> 2907.96]  like you should be actively
[2907.96 --> 2910.28]  looking for new voices and
[2910.28 --> 2911.26]  new people who are hungry
[2911.26 --> 2912.86]  who are going to push their
[2912.86 --> 2914.20]  new ideas into the scene
[2914.20 --> 2915.64]  because otherwise there's just
[2915.64 --> 2917.88]  stagnation this is teetering
[2917.88 --> 2919.10]  dangerously into unpopular
[2919.10 --> 2920.80]  opinion territory but I
[2920.80 --> 2922.14]  encourage the audience to cast
[2922.14 --> 2923.40]  their eye around to other
[2923.40 --> 2924.72]  language communities and ask
[2924.72 --> 2927.56]  the question who are they
[2927.56 --> 2931.10]  full of the same popular
[2931.10 --> 2933.56]  established old heads coming
[2933.56 --> 2934.82]  up with great new ideas of
[2934.82 --> 2936.68]  course but from the same
[2936.68 --> 2938.50]  people or are they actively
[2938.50 --> 2940.94]  seeking to replace and
[2940.94 --> 2942.82]  rejuvenate with new speakers
[2942.82 --> 2944.30]  and new ideas new points of
[2944.30 --> 2946.42]  view and new perspectives that's
[2946.42 --> 2948.50]  why you have kids so when you
[2948.50 --> 2949.80]  say to you something it's seven
[2949.80 --> 2951.36]  years old are you referring to
[2951.36 --> 2952.94]  like the technology itself is
[2952.94 --> 2955.28]  seven years old or like can
[2955.28 --> 2956.40]  you I guess elaborate a bit
[2956.40 --> 2957.80]  like because like when you
[2957.80 --> 2958.88]  talk about innovation tokens
[2958.88 --> 2960.22]  obviously if you take a
[2960.22 --> 2961.00]  language that you've never
[2961.00 --> 2962.62]  used that's 17 years old
[2962.62 --> 2963.96]  that's probably not going to
[2963.96 --> 2965.62]  help you in that front well
[2965.62 --> 2967.26]  you know I'm teaching Python
[2967.26 --> 2969.30]  still and Python is 30 years
[2969.30 --> 2970.56]  old now so I'm teaching people
[2970.56 --> 2971.46]  who are younger than the
[2971.46 --> 2972.88]  language and they still think
[2972.88 --> 2975.58]  it's new and cool so but there
[2975.58 --> 2977.36]  is something about a product
[2977.36 --> 2978.70]  that has been in production
[2978.70 --> 2980.30]  for many years that people
[2980.30 --> 2981.94]  ironed all the bugs they
[2981.94 --> 2983.74]  found out there is enough
[2983.74 --> 2985.44]  community and knowledge
[2985.44 --> 2987.18]  around it so you can go and
[2987.18 --> 2988.22]  find answers to your
[2988.22 --> 2989.14]  questions you can read
[2989.14 --> 2990.62]  tutorials and it takes time
[2990.62 --> 2991.92]  it takes time to build this
[2991.92 --> 2994.58]  volume of things to do so I
[2994.58 --> 2995.56]  think it's around seven years
[2995.56 --> 2996.40]  maybe sometimes more
[2996.40 --> 2997.98]  almost all of the things that
[2997.98 --> 2999.44]  we think of as kind of
[2999.44 --> 3002.20]  overnight successes generally
[3002.20 --> 3004.84]  they spend about 10 years in
[3004.84 --> 3006.50]  the wilderness before it Twitter
[3006.50 --> 3007.66]  is an example of that most of
[3007.66 --> 3009.16]  the popular services that we
[3009.16 --> 3010.14]  think can use in products
[3010.14 --> 3014.18]  spent decades as either going
[3014.18 --> 3015.54]  down the wrong track or just
[3015.54 --> 3018.16]  kind of waiting for that spark
[3018.16 --> 3019.62]  to happen programming
[3019.62 --> 3022.18]  languages technologies tools
[3022.18 --> 3023.54]  websites all of these
[3023.54 --> 3026.10]  computers the history of that
[3026.10 --> 3026.84]  we're all sitting in front of
[3026.84 --> 3028.98]  Macintoshes would you really be
[3028.98 --> 3029.76]  sitting in front of a Mac in
[3029.76 --> 3031.84]  the 90s like they were on the
[3031.84 --> 3034.86]  road to oblivion but what yeah
[3034.86 --> 3037.16]  in 2001 the company which is
[3037.16 --> 3039.16]  now the largest I think they're
[3039.16 --> 3039.92]  worth more than certain
[3039.92 --> 3041.84]  countries had to be bailed up by
[3041.84 --> 3043.94]  Microsoft with a loan to avoid
[3043.94 --> 3045.52]  going broke most of the things
[3045.52 --> 3047.68]  you see as successful have a long
[3047.68 --> 3050.42]  period of struggle and toil to put
[3050.42 --> 3051.52]  that foundation that makes them
[3051.52 --> 3053.76]  seem so successful there's a
[3053.76 --> 3055.92]  formula for maturity that Martin
[3055.92 --> 3057.74]  Winner posted which says that
[3057.74 --> 3059.68]  maturity is blood plus sweat
[3059.68 --> 3062.36]  divided by complexity and all this
[3062.36 --> 3064.16]  blood and sweat takes time this is
[3064.16 --> 3065.96]  something you need to know I think
[3065.96 --> 3067.86]  about that in terms of the go
[3067.86 --> 3071.42]  compiler itself like in 2012 2013
[3071.42 --> 3074.42]  each new version of go we were
[3074.42 --> 3076.82]  working on juju at canonical juju was
[3076.82 --> 3078.60]  just large enough that had been
[3078.60 --> 3079.88]  written by enough people with
[3079.88 --> 3081.06]  enough different coding styles we
[3081.06 --> 3082.08]  basically had one of every
[3082.08 --> 3083.68]  different version of kind of the
[3083.68 --> 3084.88]  way you could do a thing and go
[3084.88 --> 3086.76]  inside there somewhere and we
[3086.76 --> 3087.98]  would regularly turn up compiler
[3087.98 --> 3090.14]  bugs runtime bugs things like that
[3090.14 --> 3091.80]  like horrible like show-stopping
[3091.80 --> 3094.48]  escape analysis bugs but over time
[3094.48 --> 3096.02]  those things stopped happening and
[3096.02 --> 3097.48]  it wasn't just the compiler got
[3097.48 --> 3100.42]  better it absolutely did but the
[3100.42 --> 3103.10]  experience of all of those bugs that
[3103.10 --> 3104.42]  happened to everybody in the
[3104.42 --> 3105.74]  formative years ago is actually
[3105.74 --> 3107.76]  codified in the actual source tree
[3107.76 --> 3110.38]  if you look in go go tests there are
[3110.38 --> 3113.34]  some 30,000 different test cases each
[3113.34 --> 3115.18]  one and they're named after the issue
[3115.18 --> 3117.18]  that they were logged in and they
[3117.18 --> 3120.94]  represent a bug found in real code in
[3120.94 --> 3123.58]  the wild and fixed and now that test
[3123.58 --> 3124.92]  case lives there to make sure that
[3124.92 --> 3126.90]  bug can't ever come back every kind of
[3126.90 --> 3128.42]  weird crash that someone had to debug
[3128.42 --> 3130.00]  and be like this can't possibly be my
[3130.00 --> 3131.48]  program and actually turned out was a
[3131.48 --> 3133.36]  bug in the runtime or the language or
[3133.36 --> 3134.64]  the compiler or something like that
[3134.64 --> 3136.52]  that experience got codified and
[3136.52 --> 3138.48]  turned into a test case which runs
[3138.48 --> 3140.36]  literally every single tribot run
[3140.36 --> 3142.48]  every commit to make that quality bar
[3142.48 --> 3144.18]  just a little bit higher every time
[3144.18 --> 3147.66]  yeah John do you have an unpopular
[3147.66 --> 3150.00]  opinion for us not today I don't think
[3150.00 --> 3152.46]  I'm sure I have plenty but none that
[3152.46 --> 3153.72]  I've thought about long enough to want
[3153.72 --> 3155.60]  to talk about it on air I'm still
[3155.60 --> 3158.12]  thinking over the seven years technology
[3158.12 --> 3160.56]  one because like it's not that I
[3160.56 --> 3162.16]  disagree with that it's just I don't
[3162.16 --> 3163.68]  know how you fix that problem in the
[3163.68 --> 3164.98]  sense that there's a lot of people new
[3164.98 --> 3166.98]  to programming who instantly want to
[3166.98 --> 3168.68]  dive into everything that's new because
[3168.68 --> 3170.96]  that's what they read about I think
[3170.96 --> 3172.04]  it's easy to go to people who are
[3172.04 --> 3173.86]  experienced and be like okay you need to
[3173.86 --> 3175.42]  like choose which tech you're using
[3175.42 --> 3177.58]  that's new but for somebody who's new
[3177.58 --> 3179.74]  to everything it's kind of like why
[3179.74 --> 3181.10]  not just learn all the new stuff and
[3181.10 --> 3183.28]  it's like Dave your test cases example
[3183.28 --> 3185.02]  is a great one of like you know these
[3185.02 --> 3186.78]  things get better over time and do you
[3186.78 --> 3187.98]  really want to be the one who's finding
[3187.98 --> 3189.34]  the bugs while trying to figure out how
[3189.34 --> 3192.36]  it works versus you know figuring out
[3192.36 --> 3194.08]  how it works first and then moving
[3194.08 --> 3196.22]  forward there's a tension here because
[3196.22 --> 3198.34]  if everyone sits on the fence and waits
[3198.34 --> 3200.28]  seven years for somebody else to be the
[3200.28 --> 3201.70]  first one no one can make any
[3201.70 --> 3204.00]  progress and to go back to to dumping on
[3204.00 --> 3206.24]  old faces at conference talks like if
[3206.24 --> 3208.16]  you only choose the people who are
[3208.16 --> 3210.60]  successful yeah you kind of bake in like
[3210.60 --> 3212.84]  a bunch of safety there but your kind of
[3212.84 --> 3214.32]  community atrophies through ideas I think
[3214.32 --> 3216.60]  about how certainly Australia go came
[3216.60 --> 3218.64]  into a lot of a lot of companies and it
[3218.64 --> 3221.64]  was a combination of a very specific
[3221.64 --> 3223.74]  like one example there was there was a
[3223.74 --> 3225.54]  Ruby shop that the log processing job
[3225.54 --> 3227.56]  took more than a day so it could never
[3227.56 --> 3230.98]  keep up with itself pinpoint case for go in
[3230.98 --> 3232.32]  write a different log processor in
[3232.32 --> 3234.68]  different language other examples when
[3234.68 --> 3235.78]  I was working at Atlassian people
[3235.78 --> 3237.00]  weren't I didn't have a lot of
[3237.00 --> 3239.06]  oversight and so I chose to write the
[3239.06 --> 3240.48]  piece of infrastructure code that I was
[3240.48 --> 3241.94]  working on in go rather than in Java
[3241.94 --> 3243.70]  because people no one was looking over
[3243.70 --> 3246.12]  my shoulder so we got lucky there it's
[3246.12 --> 3248.38]  that tension between sticking with the
[3248.38 --> 3250.14]  tried and true and kind of waiting for
[3250.14 --> 3251.98]  somebody else to take the first move and
[3252.82 --> 3255.34]  the realization that like you have to
[3255.34 --> 3257.98]  try new juniors and new solutions the
[3257.98 --> 3259.54]  only kind of like like kind of shrug emoji
[3259.54 --> 3260.92]  thing I can say is well that's
[3260.92 --> 3262.22]  engineering that's about weighing
[3262.22 --> 3264.94]  trade-offs and risks and making sure
[3264.94 --> 3267.00]  that you don't paint yourself so
[3267.00 --> 3268.92]  terribly into a corner that you have no
[3268.92 --> 3270.96]  budget for risk at all left if you spend
[3270.96 --> 3272.54]  all your budget up front you can't take
[3272.54 --> 3273.74]  any more risks for the rest of the
[3273.74 --> 3276.26]  project like you have no safety margin
[3276.26 --> 3277.90]  at all that's terrible place to be
[3277.90 --> 3279.54]  working from like to go way back to
[3279.54 --> 3281.64]  discussion of people being like afraid
[3281.64 --> 3283.14]  to break computers because they made a
[3283.14 --> 3285.16]  syntax error like if you arrive in a
[3285.16 --> 3287.82]  place where you can't like any one
[3287.82 --> 3290.22]  mistake no matter how big or small kills
[3290.22 --> 3291.26]  your project because you have no more
[3291.26 --> 3293.10]  budget for risk you painted yourself into
[3293.10 --> 3294.28]  a corner it's very difficult to recover
[3294.28 --> 3295.92]  from that situation I like to say that
[3295.92 --> 3297.58]  this is the trade-off for the people
[3297.58 --> 3299.34]  that make the decisions in the business
[3299.34 --> 3301.66]  bringing in new technology brings in new
[3301.66 --> 3303.56]  opportunities brings in new opportunities
[3303.56 --> 3305.04]  to hire people new opportunities for
[3305.04 --> 3306.92]  new technologies to solve problems in
[3306.92 --> 3309.48]  different ways new technologies that a lot
[3309.48 --> 3311.22]  of the reason that systems in the back end
[3311.22 --> 3313.14]  of github are written in go is for
[3313.14 --> 3314.72]  concurrency like there are things which
[3314.72 --> 3317.44]  fit much better the ability to use
[3317.44 --> 3319.26]  concurrency than that kind of single
[3319.26 --> 3321.22]  process request response model that
[3321.22 --> 3322.86]  other that other languages have
[3322.86 --> 3324.62]  different horses different use cases
[3324.62 --> 3326.96]  for different technologies the trade-off
[3326.96 --> 3328.02]  there for kind of like the engineering
[3328.02 --> 3329.74]  manager or the VP of engineering is
[3329.74 --> 3331.82]  something is to be saying how do you
[3331.82 --> 3333.72]  like if we have one of everything in
[3333.72 --> 3335.34]  our technology stack and I'm sure people
[3335.34 --> 3336.40]  have worked at places with that where
[3336.40 --> 3338.64]  they do have one of every technology in
[3338.64 --> 3340.68]  their stack how do we staff all these
[3340.68 --> 3342.52]  teams how do we cross skill across all
[3342.52 --> 3344.10]  these teams we need someone who knows
[3344.10 --> 3347.26]  haskell and javascript and closure and
[3347.26 --> 3350.66]  ruby and go and python and c++ like
[3350.66 --> 3352.32]  that becomes that kind of impossible
[3352.32 --> 3355.40]  unicorn like maybe someone has passing
[3355.40 --> 3357.00]  knowledge of of all those technologies
[3357.00 --> 3359.38]  but they need to kind of be an expert in
[3359.38 --> 3361.04]  all those technologies so for example
[3361.04 --> 3362.80]  what I've seen at some companies that
[3362.80 --> 3365.16]  they'll say we have three or four or five
[3365.16 --> 3367.34]  languages and that kind of gives them a
[3367.34 --> 3369.48]  continuum to say here are the established
[3369.48 --> 3371.16]  languages here are the ones that are
[3371.16 --> 3372.94]  coming up and perhaps here are some of
[3372.94 --> 3374.90]  the ones that we don't use anymore I
[3374.90 --> 3377.60]  know that famously Google was Java c++
[3377.60 --> 3379.38]  and Python I don't believe they use
[3379.38 --> 3382.42]  Python anymore and so by having a set
[3382.42 --> 3385.50]  of technologies in your stack you get to
[3385.50 --> 3387.44]  have a discussion about their maturity
[3387.44 --> 3391.62]  level or are they in the kind of are
[3391.62 --> 3393.18]  they used for new work are they used for
[3393.18 --> 3395.58]  existing projects are they kind of they're
[3395.58 --> 3396.98]  the workhorses but we're not starting
[3396.98 --> 3399.12]  new things in them I think that's one way
[3399.12 --> 3400.60]  to manage the risk and manage the maturity
[3400.60 --> 3403.52]  of technologies I think the problem is
[3403.52 --> 3406.26]  that people a lot of time overestimate the
[3406.26 --> 3408.84]  benefits and underestimate the risks or the
[3408.84 --> 3411.80]  downside of new technology absolutely all
[3411.80 --> 3414.98]  right Natalie so my unpopular opinion is a
[3414.98 --> 3417.82]  lot less exciting unfortunately it's also
[3417.82 --> 3423.36]  about interviews and it's that you should
[3423.36 --> 3427.72]  write some of your social media on your CV and
[3427.72 --> 3430.14]  while I do see sometimes people many times
[3430.14 --> 3432.96]  write their LinkedIn and GitHub I feel that in
[3432.96 --> 3435.10]  tech it kind of makes sense to also include
[3435.10 --> 3438.80]  your Twitter for example if you have one where
[3438.80 --> 3441.66]  you anyway rant about tech or share things like
[3441.66 --> 3444.04]  that some Twitter handles of course don't make
[3444.04 --> 3446.76]  sense but I don't think that it belongs
[3446.76 --> 3450.24]  enough in the stack of a at least of a techie
[3450.24 --> 3453.04]  yeah I think it makes sense but in a way
[3453.04 --> 3455.82]  sometimes it's hard to separate so for me
[3455.82 --> 3458.20]  there was a clear separation between Facebook
[3458.20 --> 3461.50]  for social and Twitter for geek stuff and in
[3461.50 --> 3464.88]  last years I got a lot of tech in Facebook and a
[3464.88 --> 3469.12]  lot of social in Twitter so I don't think I have a
[3469.12 --> 3471.76]  problem showing what's going on there and people
[3471.76 --> 3474.46]  can see that I think a lot of people are afraid of
[3474.46 --> 3477.18]  that for some reason I don't know why it's like
[3477.18 --> 3479.16]  interesting in the sense that once you get popular
[3479.16 --> 3481.22]  enough it's almost like you don't even have to
[3481.22 --> 3482.72]  share it because if they just Google your name
[3482.72 --> 3485.12]  they'll probably find it yeah I mean I guess there's
[3485.12 --> 3487.90]  obviously the people who have a random racist Facebook
[3487.90 --> 3489.62]  or Twitter account or something then they probably
[3489.62 --> 3491.18]  shouldn't be sharing it that's probably not going to
[3491.18 --> 3493.12]  help them I mean maybe it would help the rest of us
[3493.12 --> 3495.02]  hiring people but they probably don't know
[3495.02 --> 3500.64]  yes obviously but yeah yeah well sounds like the
[3500.64 --> 3503.28]  unpopular opinion is a little bit unpopular so that's
[3503.28 --> 3507.38]  good I'm always trying to stick that box I guess I'm just
[3507.38 --> 3509.96]  not sure like I guess I wonder how it would be for
[3509.96 --> 3512.22]  people who just choose not to do those social things if
[3512.22 --> 3515.76]  there'd be some like negative side effect for them who for
[3515.76 --> 3518.50]  whatever reason decide like I don't use Facebook pretty much
[3518.50 --> 3522.22]  ever I have one but I don't remember the last time I've logged
[3522.22 --> 3524.86]  in and I basically stopped using it because I found that I
[3524.86 --> 3528.16]  didn't get on Facebook and walk away happier in any way like
[3528.16 --> 3531.10]  having an enriched life so I was like this isn't worth doing
[3531.10 --> 3534.54]  and even like Twitter at times I'm very limited in what I do
[3534.54 --> 3536.98]  with it because I find if I'm on Twitter too much it just
[3536.98 --> 3540.82]  doesn't make me feel like my day is any better there's just too
[3540.82 --> 3545.50]  many crappy people out there so I guess it just is kind of a mixed
[3545.50 --> 3550.72]  bag for me yeah is there anything else we should say for this episode
[3550.72 --> 3556.34]  solve more quizzes be curious all the time and take the idea and change
[3556.34 --> 3560.92]  it and make it your own the opportunity to share like to share
[3560.92 --> 3563.76]  something that you learned or share something that was surprising to you
[3563.76 --> 3566.92]  as I said a lot of the quizzes come from like reading the spec and finding
[3566.92 --> 3570.94]  obscure things in there which is really just like a road quiz but quite a number
[3570.94 --> 3575.08]  of them come from seeing a bug and it's like a bug and I'm kind of making my
[3575.08 --> 3579.48]  hands like like I once caught a fish this big kind of large and the challenge
[3579.48 --> 3583.40]  there is like for me is it possible to find the the core the guts of the guts
[3583.40 --> 3586.24]  of this misunderstanding you know thing that will fit as a properly
[3586.24 --> 3590.00]  formatted go program in the tweet that's kind of the challenge for me but like
[3590.00 --> 3593.66]  those are the constraints that I set for myself to like can I ask the question
[3593.66 --> 3597.34]  in the form of a tweet there are no rules here like the goal is to share
[3597.34 --> 3601.40]  like share I learned this surprising thing is anybody else surprised by it and
[3601.40 --> 3605.84]  also and it's surprising because I didn't know that you could write you could
[3605.84 --> 3609.84]  have emoji identifiers or I didn't know the opportunity to like share does
[3609.84 --> 3614.16]  everyone know Julia Evans? Julia Evans makes make zines yeah yeah her chosen form
[3614.16 --> 3617.70]  of communicating this is like if she's learning about epol or learning about like
[3617.70 --> 3622.30]  some arcane or you know not particularly her ability to take a very weird or
[3622.30 --> 3626.50]  obscure piece of some part of her job and not just turn it into a question but
[3626.50 --> 3631.18]  turn it into like craft as a magazine like a 90s zine thing that's her way of
[3631.18 --> 3635.48]  sharing sharing that and that's like so my suggestion was like if you like the
[3635.48 --> 3639.12]  idea behind the quizzes it's not just like here's a question you know I'm keeping
[3639.12 --> 3642.00]  my own score of how well I'm doing on these over the year but if you actually
[3642.00 --> 3647.30]  engage with the idea of them as a vehicle to teach and share something that you
[3647.30 --> 3650.58]  learned or certainly something was surprising or unexpected to you like take
[3650.58 --> 3654.24]  the idea and do it exactly as I do if you want or take the idea and do it
[3654.24 --> 3657.98]  completely differently again nothing is off the table here turn them into books
[3657.98 --> 3661.78]  turn them into conference talks and give them at your meetups like write them
[3661.78 --> 3665.98]  send them as letters to communications of the ACM like the opportunity there to
[3665.98 --> 3671.60]  teach and to educate about something that was new and surprising and that you
[3671.60 --> 3675.66]  appreciated learning is that's the goal there it's not about what are the rules
[3675.66 --> 3680.76]  writing perfect pop quiz big thank you thank you for participating on such a
[3680.76 --> 3685.30]  short notice and creating so much content it almost feels like it was a podcast of
[3685.30 --> 3689.14]  just two interesting quiz creators I enjoyed listening a lot
[3689.14 --> 3718.36]  we'll put these unpopular opinions to the test on twitter follow go time fm and let your opinion be heard when we take the poll and of course if you dig the show spread the love and let other gophers or even go curious folks know about go time we do appreciate it go time is produced by jared santo with music by breakmaster cylinder we're brought to you by fastly launch darkly and linode
[3718.36 --> 3729.24]  next time on go time john and chris are joined by peter bergeon and tim heckman to discuss ghost controversial b2 plus problem we'll have that episode ready for you next week
[3729.24 --> 3740.12]  bye
[3740.12 --> 3741.96]  as
[3759.24 --> 3771.24]  Game on!
