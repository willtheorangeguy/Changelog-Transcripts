[0.00 --> 20.98]  Welcome to ChangeLog and Friends, a weekly talk show about how we podcast.
[21.54 --> 24.48]  Special thanks to our partners at Fly.io.
[24.48 --> 28.94]  Over 3 million apps have launched on Fly, including ours.
[29.30 --> 31.76]  And you can too, in 5 minutes or less.
[32.08 --> 34.12]  Learn how at Fly.io.
[34.50 --> 36.12]  Okay, let's talk.
[42.34 --> 45.98]  Hey friends, I'm here with Dave Rosenthal, CTO of Sentry.
[46.38 --> 50.28]  So Dave, I know lots of developers know about Sentry, know about the platform.
[50.72 --> 52.76]  Because hey, we use Sentry and we love Sentry.
[52.76 --> 56.50]  And I know tracing is one of the next big frontiers for Sentry.
[56.76 --> 58.32]  Why add tracing to the platform?
[58.60 --> 59.18]  Why tracing?
[59.46 --> 60.04]  And why now?
[60.36 --> 67.70]  When we first launched the ability to collect tracing data, we were really emphasizing the performance aspect of that.
[67.76 --> 69.96]  The kind of application performance monitoring aspect.
[70.14 --> 73.34]  You know, because you have these things that are spans that measure how long something takes.
[73.44 --> 77.54]  And so the natural thing is to try to graph their durations and think about their durations.
[77.76 --> 80.28]  And, you know, warn somebody if the durations are getting too long.
[80.28 --> 86.64]  But what we've realized is that the performance stuff ends up being just a bunch of gauges to look at.
[86.98 --> 88.60]  And it's not super actionable.
[89.12 --> 94.72]  Sentry is all about this notion of debuggability and actually making it easier to fix the problem, not just sort of giving you more gauges.
[95.02 --> 100.76]  A lot of what we're trying to do now is focus a little bit less on the sort of just the performance monitoring side of things.
[100.76 --> 105.10]  And turn tracing into a tool that actually aids the debuggability of problems.
[105.76 --> 106.14]  I love it.
[106.22 --> 106.50]  Okay.
[106.62 --> 108.56]  So they mean it when they say code breaks.
[108.80 --> 110.08]  Fix it faster with Sentry.
[110.32 --> 113.92]  More than 100,000 growing teams use Sentry to find problems fast.
[114.08 --> 115.06]  And you can too.
[115.56 --> 118.00]  Learn more at Sentry.io.
[118.14 --> 121.88]  That's S-E-N-T-R-Y.io.
[121.88 --> 124.30]  And use our code CHANGELOG.
[124.38 --> 126.52]  Get $100 off the team plan.
[126.84 --> 129.50]  That's almost four months free for you to try out Sentry.
[129.68 --> 132.32]  Once again, Sentry.io.
[140.16 --> 143.00]  The only Bob Seger song I could name is Old Time Rock and Roll.
[144.12 --> 145.20]  That's like the worst one.
[145.34 --> 146.50]  Well, I don't know the man's.
[146.50 --> 147.82]  All Bob fans kind of hate that song.
[147.94 --> 149.18]  I don't know the man's work, obviously.
[149.94 --> 150.86]  You're missing out, man.
[150.86 --> 153.00]  I don't have to give you his greatest hits.
[153.66 --> 154.20]  It's on Spotify.
[154.94 --> 155.66]  I'm sure it is.
[155.76 --> 156.80]  I don't use Spotify, though.
[157.60 --> 159.40]  I only program against it.
[159.44 --> 161.00]  I've been coding against Spotify this week.
[162.18 --> 164.90]  I finally cracked it, man.
[164.94 --> 165.78]  I finally cracked it.
[165.82 --> 167.06]  We're going to get our data out of there.
[167.58 --> 168.30]  Is that right?
[168.44 --> 168.92]  Got it, dude.
[168.96 --> 170.02]  I'm pulling data out of there.
[170.26 --> 171.04]  Unofficial API.
[171.46 --> 171.76]  It's cool.
[172.06 --> 172.90]  Is it legal?
[175.94 --> 177.54]  I don't know, honestly.
[177.76 --> 178.64]  I'm not sure it's not illegal.
[179.56 --> 180.66]  Well, I'm not sure it's not illegal.
[180.86 --> 181.36]  It's one of the two.
[181.40 --> 182.34]  They have terms of service.
[182.78 --> 184.24]  It's either legal or illegal.
[184.46 --> 184.88]  I don't know.
[185.66 --> 186.64]  It's one or the other.
[186.78 --> 188.02]  I mean, listen.
[188.60 --> 190.44]  They let you log into a dashboard and look at it.
[190.60 --> 192.12]  So that's all I'm doing.
[192.26 --> 193.36]  Only it's a robot.
[193.82 --> 194.38]  I love it.
[194.54 --> 195.32]  I love bots.
[195.86 --> 196.96]  A robot doing it for us.
[196.96 --> 201.88]  So, you know, I just like bots more before there was artificial intelligence.
[201.88 --> 203.08]  And now they're kind of scary.
[203.18 --> 204.96]  Like bots were controlled by us.
[204.96 --> 206.86]  And now they're kind of like maybe not controlled by us.
[207.46 --> 210.68]  So like when I said I like bots, I kind of cringed internally.
[210.68 --> 213.28]  Like maybe I don't.
[213.98 --> 214.66]  I don't know.
[214.66 --> 216.14]  I feel like we still control them.
[216.20 --> 216.58]  Do we not?
[216.78 --> 217.04]  I mean.
[217.68 --> 221.04]  So in the Babaverse book five.
[221.36 --> 223.36]  That's the deep cut that I don't have any access to.
[223.74 --> 224.46]  That's okay, though.
[224.76 --> 225.28]  That's okay.
[225.28 --> 231.68]  I think it's in the synopsis of the book where it's not plot ruining.
[232.24 --> 239.40]  But there's a premise of artificial intelligence not being nice.
[240.06 --> 240.50]  Okay.
[240.54 --> 243.20]  Let's just say, you know, trying to escape.
[243.62 --> 244.90]  Trying to be nefarious.
[245.14 --> 245.36]  Sure.
[245.74 --> 246.76]  And it's a little scary.
[247.28 --> 248.38]  It's just a book, though.
[248.80 --> 249.46]  That's just made up.
[250.12 --> 250.80]  For now.
[250.80 --> 255.38]  Until five years from now when science fiction becomes fiction.
[256.26 --> 257.00]  I'm skeptical.
[257.80 --> 259.40]  Or I should say, sorry, nonfiction.
[259.90 --> 260.08]  Yeah.
[260.58 --> 262.84]  I was going to correct you, but then I was like, I know what he means.
[262.86 --> 263.32]  You know what I mean?
[263.36 --> 263.54]  Yeah.
[263.62 --> 264.06]  Yeah, totally.
[264.46 --> 265.96]  And like an idiot, I still can't.
[266.02 --> 267.76]  I never am like, is it nonfiction or fiction?
[267.92 --> 268.74]  Every time in the moment.
[268.76 --> 270.08]  It is kind of backwards, isn't it?
[270.16 --> 270.58]  It is.
[270.58 --> 272.50]  Because one's the negation of the other.
[272.78 --> 273.06]  Yeah.
[273.60 --> 276.80]  And you think you would start with the real thing and then negate it for fiction.
[277.24 --> 278.92]  And then the movie ruined it for me.
[279.02 --> 279.78]  Stranger Than Fiction.
[279.78 --> 281.40]  Stranger Than Fiction.
[281.50 --> 282.18]  That's Will Ferrell?
[282.42 --> 282.96]  Will Ferrell.
[283.08 --> 284.08]  I never saw that one.
[284.40 --> 286.64]  It was a strange movie.
[287.02 --> 287.88]  Was it Stranger Than?
[288.10 --> 288.86]  But it was fiction.
[289.38 --> 290.04]  It was good.
[290.30 --> 291.66]  It was a good breakout role for him.
[291.78 --> 294.08]  It was different than all his preceding roles.
[294.18 --> 297.96]  It was like the first time he went out of the straight up comedy role.
[298.06 --> 298.36]  Right.
[298.76 --> 299.40]  And he did it?
[299.58 --> 300.54]  He accomplished it?
[300.58 --> 301.80]  He nailed it, in my opinion.
[301.96 --> 302.52]  He was solid.
[302.80 --> 303.06]  Really?
[303.40 --> 304.22]  Like I was rooting for him.
[304.78 --> 305.98]  He worked for the IRS.
[306.32 --> 306.90]  He was an auditor.
[307.48 --> 309.50]  Who's the best comedian crossover to drama?
[310.12 --> 310.30]  Yeah.
[310.32 --> 311.16]  I mean, short list, right?
[311.20 --> 311.90]  You got Adam Sandler.
[312.06 --> 313.22]  You got Jim Carrey.
[313.94 --> 314.60]  You've got...
[314.60 --> 315.76]  Adam Sandler's the GOAT, bro.
[316.06 --> 317.08]  Yeah, he probably is.
[317.86 --> 318.56]  He's the GOAT.
[318.98 --> 320.36]  Did Mike Myers ever cross over?
[320.46 --> 321.30]  I think he tried to.
[321.98 --> 323.50]  Oh, Steve Carell's actually done pretty well.
[324.24 --> 324.58]  Yeah.
[325.40 --> 325.76]  Anyways.
[326.66 --> 327.68]  Did you book your flight?
[327.78 --> 328.48]  I booked my flight.
[328.82 --> 329.66]  I booked my flight.
[330.02 --> 330.70]  We're booked, baby.
[331.02 --> 331.38]  Booked.
[331.66 --> 332.48]  All things open.
[332.86 --> 333.60]  All things open.
[333.96 --> 334.32]  2024.
[335.10 --> 335.42]  2024.
[336.00 --> 337.06]  Raleigh, North Carolina.
[337.58 --> 338.52]  Raleigh, North Carolina.
[338.70 --> 339.66]  I'm going to repeat what you say.
[339.84 --> 340.48]  We'll be there.
[341.44 --> 342.54]  I think we'll be there.
[342.78 --> 344.08]  I can't see why we wouldn't be there.
[344.56 --> 345.64]  We're planning on being there.
[345.82 --> 347.36]  We're just not sure where our booth is at yet.
[347.48 --> 349.48]  We don't know where our booth is at, but we'll have a booth, right?
[349.72 --> 350.72]  We will have a booth.
[351.24 --> 353.82]  We will have options, I believe.
[353.82 --> 357.84]  I think we have an option of in the main area near the ballrooms where we normally are,
[358.08 --> 361.54]  but where we have normally been is highly sought after.
[361.96 --> 362.10]  Right.
[362.44 --> 365.06]  And they had a swell of sponsorships in the end.
[365.24 --> 365.68]  I see.
[366.08 --> 368.42]  And so money trumps, you know, non-money.
[368.74 --> 370.08]  And I guess we're in the non-money bucket.
[370.22 --> 371.16]  We're non-money people.
[371.50 --> 371.70]  Yeah.
[372.56 --> 375.86]  I would say we bring the money, but we're not given the money.
[376.00 --> 376.58]  I mean, we are.
[376.68 --> 378.10]  We're so money that we don't even know it.
[378.26 --> 378.70]  That's right.
[378.80 --> 381.02]  But we don't actually have the money, so it's different.
[381.40 --> 381.64]  Yeah.
[381.80 --> 382.50]  I get it.
[382.50 --> 383.32]  We'll be there, though.
[383.36 --> 383.66]  It's cool.
[383.82 --> 384.10]  We're flex.
[384.12 --> 384.90]  We'll have our microphones.
[385.26 --> 386.00]  We'll have stickers.
[386.70 --> 387.84]  Who knows what else we'll have?
[388.00 --> 390.28]  I'm hoping we have at least one TV with clips.
[390.66 --> 394.54]  Yeah, we'll have our clip gallery behind us, hopefully.
[395.60 --> 402.24]  So if you're going to be at All Things Open 2024, which is at the end of October, 27th through
[402.24 --> 405.00]  the 30th, I believe, is our official trip dates.
[405.30 --> 405.60]  Yes.
[405.74 --> 406.50]  Sunday through Wednesday.
[406.94 --> 407.66]  Find us.
[408.30 --> 409.04]  Talk to us.
[410.02 --> 410.76]  High five us.
[411.90 --> 412.88]  Adam gives hugs.
[412.88 --> 413.98]  If you're into that kind of thing.
[414.16 --> 414.44]  Sometimes.
[415.06 --> 416.50]  I've pulled back from the hugs.
[416.86 --> 417.24]  Oh, you have?
[417.44 --> 417.62]  Yeah.
[418.02 --> 423.16]  But certain individuals, depending upon how they look at me, it's hug time.
[423.80 --> 427.80]  How should one approach if they're interested in an Adam hug?
[428.26 --> 428.90]  Great question.
[429.26 --> 430.24]  Oh, geez.
[430.24 --> 432.92]  I would say longingly.
[433.70 --> 434.02]  Longingly.
[434.60 --> 436.06]  And with a slight smile.
[436.70 --> 438.38]  Arms wide open or is that too much?
[438.46 --> 441.74]  I would say come with a handshake and convert to hug.
[441.96 --> 442.30]  Right.
[442.38 --> 443.24]  Well, that's the easy version.
[443.42 --> 445.40]  Like you shake the hand and you lean in.
[445.54 --> 445.70]  Yeah.
[445.80 --> 449.44]  You can do the back pat and then you can be like, you can whisper in his ear, I want the
[449.44 --> 449.92]  whole thing.
[450.14 --> 450.34]  You know?
[450.52 --> 450.98]  Something like that.
[451.02 --> 452.58]  Give me the full hug, Adam.
[454.58 --> 454.94]  Okay.
[455.24 --> 455.66]  There you go.
[455.66 --> 456.06]  It's getting weird.
[456.30 --> 461.30]  But hey, if you do that, well, then you listen to the show and you follow orders or at least
[461.30 --> 463.66]  entertain our silliness.
[463.94 --> 464.22]  Yes.
[464.56 --> 465.02]  Who knows?
[465.56 --> 466.10]  So there we go.
[466.18 --> 467.22]  All things open 2024.
[467.62 --> 474.60]  Also, our show with Alia Abbott has actually borne fruit, which is rare for us.
[474.64 --> 476.72]  Like we've actually, we followed up Zulip.
[476.72 --> 482.68]  We're trying out Zulip in earnest, meaning we're actually using it and we've invited people
[482.68 --> 487.28]  into it and we got people in there and we are checking it out.
[487.34 --> 491.26]  Now, I thought we'd talk about this on Kaizen, which is coming up just next week, but our
[491.26 --> 492.76]  Kaizen is busted at the seams.
[492.92 --> 495.14]  So why not just do quick first impressions here?
[496.12 --> 500.84]  What we think about Zulip after using it for two weeks-ish, maybe 10 days in earnest?
[501.48 --> 506.20]  You know, I did not expect me to like it as much as I like it.
[506.36 --> 506.78]  Really?
[506.78 --> 513.34]  I really was only trying it out of seemingly force.
[513.48 --> 516.04]  Like I know it was forcing me, but I felt like we really had to.
[516.40 --> 517.26]  Well, we said we would.
[517.50 --> 518.72]  Well, yes, we did.
[518.78 --> 519.14]  So yes.
[519.20 --> 520.08]  But there's no force there.
[520.44 --> 524.56]  You can always make empty promises or at least empty words to some degree.
[524.78 --> 525.12]  Uh-uh.
[525.38 --> 529.72]  Well, I don't mean to like not do it, but I mean like I was begrudgingly trying it out.
[529.86 --> 530.12]  Let's just say-
[530.12 --> 530.54]  I know you were.
[531.26 --> 532.06]  I felt it.
[532.14 --> 533.36]  I felt your begrudge for a minute.
[533.68 --> 534.00]  Yeah.
[534.00 --> 537.52]  Because you're like, you set it up, you invited me, and then you were like, I can tell you're
[537.52 --> 538.70]  like, and I did my thing.
[538.86 --> 539.70]  I did what I was supposed to do.
[540.32 --> 540.60]  Yeah.
[540.88 --> 541.16]  Yeah.
[541.30 --> 543.40]  Well, I felt like I had at least done that.
[543.48 --> 547.52]  But you know, what clinched it for me, and this is where we were chatting in our own DMs
[547.52 --> 552.34]  in there, was I was like, I really just feel like we need more realness to it.
[552.36 --> 554.60]  I can't just DM with you and be like, yeah, I like it.
[554.62 --> 555.18]  Let's do it.
[555.58 --> 556.92]  That's not going to be it.
[557.14 --> 559.28]  You know, we've got to have some real stuff in there.
[559.28 --> 566.44]  And wow, in addition to my mind changing, or at least my judgment, my prejudgment-
[566.44 --> 566.68]  Sentiment.
[566.90 --> 567.14]  Yeah.
[567.70 --> 568.18]  Changing.
[568.62 --> 574.38]  There's people in there, and I would say there's more deep conversation in Zulip than has ever
[574.38 --> 575.08]  been in Slack.
[575.20 --> 580.04]  Now, there's been lots of conversation, but like, it seems like it's deeper and longer
[580.04 --> 582.14]  because the thread is there, the topic is there.
[582.52 --> 583.24]  I don't know.
[583.34 --> 584.06]  Something-
[584.06 --> 584.32]  Yeah.
[584.32 --> 586.72]  Something uniquely different is in Zulip.
[587.22 --> 592.96]  And now when I go back to Slack, I really just feel like I have no idea where the conversation's
[592.96 --> 593.14]  at.
[593.54 --> 593.86]  Right.
[594.46 --> 594.88]  Yeah.
[594.92 --> 597.64]  A couple of things that have struck me.
[597.86 --> 605.40]  The first one is required topics makes you think a little more before you do something
[605.40 --> 606.08]  or say something.
[606.62 --> 612.06]  And so there's a little more intentionality to what you have to do, which is friction, which
[612.06 --> 613.00]  sometimes stops you.
[613.00 --> 616.02]  I think you said it, this feels more like real-time email.
[616.86 --> 621.16]  And because when you start a new email thread with somebody, you have to put a subject in
[621.16 --> 622.22]  that email.
[622.48 --> 623.78]  And that's what a topic is, really.
[624.60 --> 627.00]  And so it does feel a little bit more like that compared to Slack.
[627.36 --> 631.62]  The second thing is, and our community folks have figured this out quickly, it feels like
[631.62 --> 638.98]  it's built by nerds more so than Slack does, even though Slack has some nerdy things for
[638.98 --> 639.60]  sure in there.
[640.50 --> 641.58]  Nerds built this.
[642.24 --> 643.62]  And that's really cool.
[643.68 --> 644.86]  You can feel that love.
[645.82 --> 650.40]  And then the third thing is, we've already had a success story with one particular community
[650.40 --> 657.66]  member who already interacted with the Zulip team and their dev channel and had influence
[657.66 --> 659.16]  on the way the product was being built.
[659.16 --> 661.40]  And that's the open source ethos that we love.
[661.54 --> 663.40]  We would never have that kind of access with Slack.
[663.70 --> 667.98]  We've known folks inside of Slack for years, off and on, engineers.
[668.70 --> 673.94]  And we're the smallest fish in that huge ocean of users.
[674.20 --> 675.38]  So that's pretty cool.
[675.88 --> 676.70]  It has its problems.
[676.84 --> 677.58]  It has its warts.
[677.58 --> 683.24]  But yeah, kudos to the Zulip team for putting together something pretty cool.
[684.04 --> 684.16]  Yeah.
[684.56 --> 688.72]  And I think when you look at, like the first thing I start to think about when I evaluate
[688.72 --> 694.46]  something is the experience and the user interface, which is not simply just design.
[694.54 --> 695.42]  It's also experience.
[695.82 --> 697.90]  I thought because, well, they're not venture backed.
[698.22 --> 699.48]  Not that they're less talented.
[699.66 --> 705.16]  They've got less resources to apply to eke out all the UX permutations.
[705.16 --> 708.74]  And I really just thought it would be less polished.
[709.42 --> 710.98]  And that's not true.
[711.06 --> 715.48]  Like the built by nerds thing, the keyboard shortcuts is what's selling me.
[715.56 --> 716.22]  It's hard selling me.
[716.52 --> 717.88]  Like being able to navigate around.
[717.88 --> 718.04]  Yeah.
[718.16 --> 719.90]  It's completely keyboard driven.
[720.04 --> 724.20]  Like you can drive it without your mouse 100% if you want to, which is really cool.
[724.52 --> 728.20]  Which is why when I go back to Slack, I feel like I'm clicking everywhere.
[728.20 --> 733.88]  And it's so fatiguing in comparison, like one-to-one going back and forth.
[733.88 --> 735.50]  Because we are straddling the line.
[736.04 --> 736.12]  Right.
[736.22 --> 740.58]  Where we've got a micro version of our community in our Zolip.
[741.22 --> 742.96]  And there's conversations happening.
[743.08 --> 743.56]  There's topics.
[743.72 --> 746.30]  There's like, I feel like it's pretty fleshed out in a way.
[746.36 --> 748.26]  Like it's on its way to being fully fleshed out.
[749.00 --> 754.20]  And then we're going back to Slack for other conversations because we haven't made that cut over yet.
[754.24 --> 755.02]  And I'm not sure if we will.
[755.10 --> 757.22]  Maybe we can talk about that here on this conversation.
[757.54 --> 758.70]  But I don't know the answer right now.
[759.42 --> 759.78]  Yeah.
[759.88 --> 761.30]  I mean, I kind of feel like I know the answer.
[761.82 --> 762.56]  What is it?
[762.56 --> 764.04]  I feel like it's, yeah.
[764.38 --> 765.60]  Like Zolip is the future.
[766.10 --> 766.40]  Okay.
[766.88 --> 767.60]  That's how I feel.
[767.74 --> 773.16]  I feel like, so I didn't share this with you yet because I've been, you know me, I'm a reserved, I suppose.
[773.42 --> 774.60]  I haven't been talking a lot in there.
[774.64 --> 778.56]  I've been observing people conversating and participating through observation.
[779.28 --> 781.60]  And here and there, jabbing in with some stuff.
[781.76 --> 785.20]  But the web public stuff is super interesting.
[785.20 --> 793.34]  I think it could be cool to find ways to like make the changelog community not so much bigger to be bigger.
[793.34 --> 801.16]  But this idea that I've always shared and I think you've adopted it too is this idea of no imposters here.
[801.46 --> 802.10]  Everyone's welcome.
[802.10 --> 813.00]  And that same idea where maybe Zolip, because we have this full history and we can self-host it and all the things, they were not locked into their cloud.
[813.10 --> 816.66]  We can begin there and move to our own self-hosted version of it.
[816.66 --> 825.44]  But I feel like we have a lot more room to like really lean even heavier into community where we could have before, but we would have had to pay for it.
[825.48 --> 835.58]  And it was very, you know, a significant cost in the Slack world where maybe we didn't put that kind of pressure on ourselves to do so because of our known limitations.
[836.18 --> 837.68]  Whereas now I feel like unfettered.
[837.72 --> 839.98]  Now we can literally do what we want.
[839.98 --> 848.30]  And I don't know this to be true, but I can hypothesize that it would be that we can get pretty good buy-in and support from Zolip.
[848.50 --> 848.72]  Yeah.
[848.88 --> 849.46]  In whatever ways.
[849.52 --> 857.28]  Like if we have ideas for how to make this even more community focused, then I think that there's an opportunity there that was definitely not there with Slack.
[857.60 --> 858.94]  I agree with all of that.
[858.94 --> 882.88]  And I think that there's definitely ways where we could increase the amount of community discussion around the shows by deeply integrating into Zolip versus what we have been doing previously, which is some of the ideas being tossed around in our channel about, you know, sharing certain channels publicly and allowing people to lurk.
[882.88 --> 883.72]  Yes.
[883.96 --> 893.00]  Allowing people to lurk, sign up, you know, integrating the actual comments of our episodes into that directly, the discussion.
[893.26 --> 910.14]  So yeah, there's a lot of opportunities for nerdery and tomfoolery that previously were kind of just, they were non-starters because you were just deepening a relationship with an entity that you really couldn't go deeper in any sort of communal way.
[910.14 --> 914.62]  It was like, what are those barnacles on top of the whale?
[914.76 --> 918.00]  We like just a little bit bigger barnacle, you know, living off this whale.
[918.58 --> 919.74]  Well, we're not their customer either.
[920.08 --> 921.48]  We're not who they're optimizing for.
[922.06 --> 922.20]  No.
[922.56 --> 936.78]  And I don't think that, and so I suppose now that this thought has come into my mind in this moment, the only hesitation or reservation I have with Zolip is the uncertainty of their future.
[936.78 --> 940.62]  Which is not to say that I think their future is uncertain.
[941.52 --> 944.52]  Whereas Slack, maybe it's the same.
[944.80 --> 947.88]  I mean, geez, products die every day and they get deprecated.
[948.30 --> 949.94]  Like, so yeah, exactly.
[950.48 --> 950.86]  Who knows?
[950.92 --> 953.32]  Even though they've got maybe more deeper pockets or.
[953.82 --> 954.40]  Way deeper.
[954.82 --> 955.10]  Yeah.
[955.60 --> 956.08]  Whatever.
[956.08 --> 963.76]  I think my only concern with Zolip is the, is the, that reservation of like, how will they persevere?
[964.30 --> 966.08]  I know the team is capable of doing it.
[966.20 --> 967.08]  Sure, but even if they don't.
[967.74 --> 968.04]  Right.
[968.14 --> 973.42]  Then it's a open source project that we self-host and maybe we just don't go deeper than that.
[973.48 --> 974.66]  We just continue to use it as is.
[974.72 --> 979.48]  I mean, as is, it's got completely serviceable community chat.
[979.82 --> 981.80]  Completely serviceable without any changes.
[982.12 --> 982.40]  Yeah.
[982.62 --> 983.10]  Great point.
[983.10 --> 985.86]  Obviously, improvements always welcome.
[986.20 --> 993.78]  Well, I guess my reservation came from the fact that while I know it's open source, I'm used to things like we're using in Slack not being open source.
[994.00 --> 996.40]  And so my brain hasn't said, okay, this is open source.
[996.68 --> 1001.98]  So that reservation can be, you know, degraded down to 50% versus 100% reservation.
[1002.50 --> 1002.90]  Yeah.
[1003.06 --> 1003.96]  Because that's super cool.
[1004.00 --> 1008.54]  And that is, that's, I don't know if you listened to the show yet, but I monologued a little bit.
[1008.54 --> 1015.76]  I've been doing this a little bit lately in the end of our interview shows because I have thoughts and I just started calling it like closing thoughts and stuff.
[1016.44 --> 1018.96]  Because I just got thoughts afterwards that I just like reveal.
[1019.36 --> 1022.66]  And this one in particular, I talked about potential.
[1022.66 --> 1027.70]  And I don't know if you've ever heard me describe potential as kinetic energy stored waiting to be released.
[1028.10 --> 1033.28]  Because I feel like that's my reservation with Zulip is they have so much potential.
[1033.68 --> 1036.26]  And it's not that they haven't achieved greatness by any means.
[1036.32 --> 1041.38]  I'm not trying to degrade or downplay the greatness they've done by any means.
[1041.38 --> 1050.66]  But I believe they have so much more potential to potentially unseat, not so much fully unseat the giants like Slack or Teams.
[1051.16 --> 1055.10]  But when you look at the feature set that people really want, I feel like Zulip's got it.
[1055.68 --> 1058.10]  What they don't have, we talked about this on the show, was the awareness.
[1058.76 --> 1058.84]  Yeah.
[1059.02 --> 1060.32]  And something's got to change there.
[1060.44 --> 1064.32]  And that's where my uncertainty for them comes is like, you've got to figure out how to market.
[1065.10 --> 1068.80]  You can't be the best unknown tool in the marketplace.
[1069.80 --> 1070.86]  Something's got to change there.
[1071.38 --> 1076.60]  And I don't know if it's dollars spent, but something's got to change with their GTN, their go-to-market strategy.
[1076.90 --> 1078.72]  How they talk about them, their awareness.
[1079.42 --> 1082.14]  Firefox famously, get Firefox.
[1082.32 --> 1086.34]  We've lamented on this in positive and negative ways over the years.
[1086.34 --> 1090.06]  They did all that grassroots stuff with a very shoestring budget.
[1090.78 --> 1092.50]  Zulip can do something similar, I believe.
[1092.68 --> 1097.96]  And that's where my reservation comes is like, they've got so much kinetic energy stored waiting to be released.
[1098.26 --> 1098.98]  This potential.
[1099.66 --> 1100.84]  And I want to see them do that.
[1101.38 --> 1106.00]  Well, perhaps in the spirit of open source, we can also help them do that.
[1106.00 --> 1109.84]  I think our adoption would be useful in that sense.
[1109.94 --> 1112.34]  Let's talk about some other things going on.
[1112.34 --> 1116.78]  Of course, with open source companies, you're always afraid of a rug pull.
[1116.78 --> 1121.20]  As we've experienced many of holes, especially of late.
[1121.28 --> 1121.86]  How about this?
[1122.58 --> 1124.40]  I'm calling it the reverse rug pull.
[1125.12 --> 1127.24]  In which they, I don't know, put the rug back.
[1127.76 --> 1128.20]  Elastic.
[1129.20 --> 1130.06]  Elastic search.
[1130.36 --> 1131.22]  Open source once again.
[1131.40 --> 1132.04]  How about this?
[1133.00 --> 1133.88]  Reverse rug pull.
[1134.40 --> 1134.88]  So cool.
[1134.88 --> 1142.66]  That might be going a bit far because it does imply that you have rug pulled in the past.
[1142.66 --> 1145.04]  So you're already not cool.
[1145.12 --> 1146.28]  And now you're putting the rug back.
[1146.36 --> 1147.36]  So I don't know if it's so cool.
[1147.48 --> 1149.90]  Because like the better thing is just like leave the rug where it was.
[1149.98 --> 1151.00]  You know, it really held the room together.
[1151.28 --> 1151.38]  Sure.
[1151.38 --> 1154.10]  That rug really tied the room together, did it not?
[1154.30 --> 1158.00]  But yes, much cooler than the rug pull.
[1158.50 --> 1163.62]  We don't want to talk too much about this because we are talking with Shea Bannon, CTO of Elastic,
[1164.18 --> 1165.42]  soon, this month.
[1166.10 --> 1169.00]  He's coming on interviews for the deep dive.
[1169.16 --> 1170.48]  But yeah, Elastic search.
[1171.38 --> 1172.36]  Opened back up again.
[1172.64 --> 1177.56]  Went full OSI approved AGPL license.
[1179.34 --> 1181.00]  And Shea's pretty excited.
[1181.38 --> 1186.66]  As you can just read into his announcement post from August the 29th.
[1186.66 --> 1188.06]  And we're excited too, right?
[1188.16 --> 1190.50]  I mean, you called it so cool.
[1190.60 --> 1191.96]  So you must be for this move.
[1192.50 --> 1194.78]  Well, it was just a saying.
[1194.90 --> 1196.22]  I don't know if I have that belief yet.
[1196.94 --> 1198.42]  The jury is still out for me.
[1199.00 --> 1204.76]  So when I read his words, I can read between the lines and hear the sentiment of positivity.
[1204.98 --> 1206.58]  Like he seems to be very excited.
[1207.22 --> 1207.36]  Yeah.
[1207.58 --> 1211.10]  His roots in terms of how Elastic was born was Hacker.
[1211.38 --> 1219.20]  And I think I was reading over on InfoWorld from our friend of the show, I suppose.
[1219.50 --> 1219.90]  Matt Asay.
[1220.30 --> 1221.40]  Is that how you say his last name?
[1221.66 --> 1222.98]  It's either Asay or A.C.
[1223.38 --> 1223.82]  A.C.
[1223.96 --> 1224.62]  Matt Asay.
[1224.62 --> 1239.66]  And he, I'm going to paraphrase, but he talked about Bannon's, Shea Bannon's initiation of Elastic was he personally paid for the trademark for Elastic to protect his work.
[1239.66 --> 1244.64]  He was the developer making it in an apartment, I think, in New York City.
[1245.48 --> 1251.92]  And so very much like the stories we all hear about, which is why I'm kind of leaning back towards this so cool aspect.
[1251.92 --> 1258.54]  Because we all have dreams when we produce works in the world, our art.
[1259.20 --> 1260.16]  Sometimes it's code.
[1260.30 --> 1261.30]  Sometimes it's pixels.
[1262.32 --> 1263.08]  Sometimes it's both.
[1263.08 --> 1278.32]  And I believe that in a position which we may not have fully agreed with and we can argue and have argued and have done shows on with the Elastic versus AWS scenario, that you've got to do sometimes what you've got to do.
[1278.38 --> 1282.64]  And we may not agree that, hey, let's now go close source to protect.
[1282.64 --> 1287.26]  But I can at least respect their choice to do so.
[1287.76 --> 1291.74]  I may not agree with it, but I can at least respect that they've had the fortitude to do so.
[1292.70 --> 1301.98]  And now to be in a position, the same hacker that made it initially, when you read his post on it, you can tell he's excited.
[1302.32 --> 1312.44]  You can tell that he's got joy writing the words and revealing this and going back to an OSI approved AGPL license.
[1312.64 --> 1319.24]  And at least there is now a trajectory now for, as he says, more open source in the world.
[1319.94 --> 1320.56]  Yeah, I agree.
[1320.78 --> 1325.10]  Obviously, we have questions, which is why we invited him on the show to talk.
[1325.64 --> 1334.62]  One of the main things I want to ask him about is he asserts in his post that their move was successful.
[1334.90 --> 1339.66]  Like that was a successful thing they did despite him not wanting to do it.
[1339.66 --> 1343.22]  And now it's provided this opportunity to go back.
[1344.04 --> 1347.58]  And I would love to get that all out in the open.
[1348.24 --> 1349.72]  How did it find success?
[1349.98 --> 1351.20]  How did they know it was successful?
[1351.42 --> 1359.86]  Because we recently covered Red Monk's analysis of open source rug polls and whether or not they've been worth it.
[1359.86 --> 1371.64]  And to the best of her ability, I think it was Rachel Stevens over there at Red Monk, did the analysis on a bunch of at least publicly traded rug polls so that you can get the data.
[1371.64 --> 1380.74]  And she couldn't find any correlation between actually any sort of meteoric rise after the license change, especially ones that have been out there for a while, including Elastic.
[1380.92 --> 1383.84]  So that's an interesting thing.
[1383.84 --> 1386.94]  And we'll be talking with him soon to our listener.
[1387.12 --> 1397.22]  If you have specific questions, lines of thought, conversation that you'd like us to broach with Elastic CTO, Shea Bannon, definitely let us know.
[1397.78 --> 1399.72]  In Slack, in Zulip, I don't know.
[1400.90 --> 1402.84]  Email editors at changelog.com.
[1403.54 --> 1404.56]  It's probably the safest place.
[1404.96 --> 1410.10]  Right now, unless you're already in our Slack or already in our Zulip, then just go ahead and use what you're already doing.
[1410.24 --> 1410.54]  That works.
[1410.54 --> 1419.86]  I was just thinking as you were suggesting that if they were going to pile on or start anew in Zulip, where would it happen at?
[1420.54 --> 1426.46]  You know, that is the challenge, not to go back there, but that's the challenge of like, where does that live?
[1427.20 --> 1429.54]  Does it live in general under a topic called shows?
[1430.26 --> 1435.78]  Does it live under changelog podcast that isn't a channel yet, that will be a channel soon?
[1436.06 --> 1436.32]  Right.
[1436.32 --> 1436.88]  Or interviews?
[1437.60 --> 1438.02]  Interviews.
[1438.02 --> 1440.38]  I think we are going to create one channel per podcast.
[1440.54 --> 1449.54]  As I've already started to do, where we publish new episode notifications for discussion, which I haven't created one for this show yet because we haven't shipped an episode yet.
[1449.62 --> 1453.36]  Although today or tomorrow, I assume we'll have last week's going out.
[1453.86 --> 1454.48]  Yes, sir.
[1454.58 --> 1455.74]  With Erez Zuckerman.
[1455.74 --> 1462.06]  In that case, I think you would just go to the changelog or interviews, I guess, and be like, questions for Shea Bannon.
[1462.26 --> 1464.68]  And you just start a topic called that.
[1465.14 --> 1467.64]  You don't have to post into an existing topic.
[1468.10 --> 1469.18]  You can start a new topic.
[1469.58 --> 1471.02]  And we just, it could be ephemeral.
[1471.18 --> 1472.66]  It doesn't have to be a long lasting thing.
[1473.42 --> 1475.66]  Just post your conversation there.
[1475.72 --> 1478.66]  And then, then Bob's your uncle.
[1479.10 --> 1479.86]  Bob is your uncle.
[1480.36 --> 1480.58]  Yeah.
[1480.62 --> 1481.98]  That's my thought on the matter, at least.
[1482.34 --> 1485.08]  But yeah, you do have to stop and think before you just start talking, don't you?
[1485.44 --> 1486.46]  And so that is the challenge.
[1486.54 --> 1492.84]  That was the, that's the other challenge with Zulip is, is I was, my reservation came from like, now everything has to be structured.
[1492.84 --> 1497.70]  And then you have to be the person who says, you're off topic or that thread or, you know, like they do in forums.
[1497.70 --> 1504.08]  Remember that when, when you'd be like slapped around basically in forums, like you're changing, you know, you're, you're hijacking.
[1504.28 --> 1504.58]  You know what I mean?
[1504.58 --> 1505.04]  Like, yeah.
[1505.08 --> 1505.50]  Hijacking.
[1505.62 --> 1508.62]  Well, the cool thing about Zulip, now we're turning into a walking advertisement.
[1508.78 --> 1509.48]  I've already done this once.
[1510.02 --> 1516.38]  You can just take an entire topic thread and move it to a different channel or messages that are on a topic.
[1516.38 --> 1519.34]  You can just take that entire set of messages and move them to a different topic.
[1519.94 --> 1523.30]  So instead of saying you're hijacking, you just move them to where they belong.
[1523.30 --> 1526.50]  And people are happy to be like, oh, okay, it's over here now.
[1526.82 --> 1527.12]  Yeah.
[1527.38 --> 1527.58]  Cool.
[1527.58 --> 1532.34]  So that makes it somewhat less of a one-way door into more of a two-way door.
[1532.34 --> 1533.60]  How about this?
[1533.76 --> 1534.66]  Reverse rug pull.
[1534.96 --> 1535.78]  We'll see if it's cool.
[1537.12 --> 1537.92]  There you go.
[1538.06 --> 1538.28]  Yeah.
[1538.84 --> 1539.28]  Yeah.
[1539.44 --> 1544.22]  And I guess we'll find out when we talk to Shay himself and release that episode and see how we feel about that.
[1544.24 --> 1545.98]  Because we'll see.
[1549.74 --> 1553.86]  Hey friends, I'm here with Brandon Fu, co-founder and CEO of Paragon.
[1553.86 --> 1563.56]  Paragon lets B2B SaaS companies ship native integrations to production in days with more than 130 pre-built connectors or configure own custom integrations.
[1564.04 --> 1568.04]  So Brandon, talk to me about the friction developers feel with integrations.
[1568.54 --> 1573.34]  SSO, dealing with rate limits, retries, auth, all the things.
[1573.34 --> 1573.90]  Yeah.
[1574.14 --> 1575.46]  So there's a lot here.
[1575.50 --> 1589.78]  And I think there's a lot of aspects to the different problems that you have to solve in the integration story in building these integrations and also providing them in a user-friendly way for your customers to self-serve and onboard and consume those integrations.
[1590.20 --> 1594.14]  So part of what the Paragon SDK provides is that embedded user experience.
[1594.28 --> 1595.74]  Again, what we call our connect portal.
[1595.92 --> 1599.82]  That's going to provide the authentication for your users to connect their accounts.
[1599.98 --> 1601.48]  That's going to be the initial onboarding.
[1601.48 --> 1606.96]  But in addition to that, your users may also want to configure different options or settings for their integrations.
[1607.24 --> 1614.96]  A common example that we see for Salesforce or for CRM integrations in general is that your users may want to select some type of custom object mapping.
[1615.16 --> 1616.86]  Every CRM can be configured differently.
[1617.40 --> 1623.74]  So your users might want to map objects to some different type of record in their Salesforce or different fields in their Salesforce.
[1623.74 --> 1633.12]  And typically, that's what developers would have to build on their own is this UI for your users to configure these different settings for every single integration.
[1633.44 --> 1651.48]  That's also going to be what's provided by the Paragon SDK is not just that initial onboarding and authentication experience, but also the configuration end user UX for different settings like custom field mapping, selecting which types of features on your integration that your user might want to configure.
[1651.48 --> 1656.48]  And that's also going to be provided fully out of the box by Paragon SDK.
[1657.24 --> 1657.58]  Okay, cool.
[1657.72 --> 1659.06]  That's the front of the house.
[1659.16 --> 1662.94]  That's the UI layer that developers are getting solved.
[1663.00 --> 1663.72]  What about the backend?
[1663.98 --> 1665.70]  The re-limiting, the retries, et cetera?
[1665.70 --> 1669.76]  With integrations, different APIs might have different rate limits.
[1669.94 --> 1672.72]  They might have different policies that you have to conform with.
[1672.82 --> 1680.86]  And your developers typically have to learn these different nuances for every API and write code individually to conform to those different nuances.
[1681.34 --> 1692.78]  With Paragon, because we build and maintain the connector with each of the integrations that we support in our catalog, we're automatically going to handle for things like retries, things like rate limits.
[1692.78 --> 1708.46]  For example, Paragon knows the rate limit for each provider and will automatically throttle your requests so that you can conform to the rate limit for those providers and be able to intelligently retry requests in the event that you exceed the rate limit or a request fails.
[1708.46 --> 1723.12]  And so we look at this as sort of the backend or infrastructure layer of the integration problem that we have spent the last five years essentially building and optimizing the Paragon infrastructure to act as the integration infrastructure for your application.
[1723.46 --> 1726.32]  Okay, Paragon is built for product management.
[1726.50 --> 1727.74]  It's built for engineering.
[1727.88 --> 1728.70]  It's built for everybody.
[1729.02 --> 1733.66]  Ship hundreds of native integrations into your SaaS application in days.
[1733.86 --> 1736.30]  Or build your own custom connector with any API.
[1736.30 --> 1740.42]  Learn more at useparagon.com slash changelog.
[1740.54 --> 1744.20]  Again, useparagon.com slash changelog.
[1744.28 --> 1750.62]  That's U-S-E-P-A-R-A-G-O-N dot com slash changelog.
[1754.16 --> 1760.18]  Well, let's talk about another changelog news item that I did not feature in audio.
[1761.18 --> 1763.74]  I actually think I just put it in the list of links at the bottom.
[1763.74 --> 1771.16]  So I didn't write anything about it, but it's a really nice post by Christian Hollinger or Hollinger, perhaps.
[1772.00 --> 1778.04]  Why I still self-host my servers and what I've learned recently.
[1778.18 --> 1779.08]  I thought this one had hit home.
[1779.70 --> 1784.84]  With you, Adam, as a home labber, but maybe not a self-hoster, but maybe a self-hoster.
[1784.84 --> 1787.32]  This article is about two things, Christian says.
[1788.12 --> 1792.06]  Why I still bother and what has recently taught me.
[1792.20 --> 1796.70]  Think of it as a brief retrospective and an encouragement for readers to go down the same rabbit hole.
[1797.50 --> 1800.60]  So Christian likes self-hosting and he thinks you should too.
[1801.30 --> 1804.36]  It's a long post, but to summarize the two reasons at least.
[1805.52 --> 1807.46]  Independence, reason number one.
[1807.46 --> 1810.24]  And learning is good.
[1811.06 --> 1812.74]  Reason number two.
[1812.88 --> 1813.72]  Are you convinced, Adam?
[1814.44 --> 1815.30]  I concur.
[1815.56 --> 1816.38]  It is a rabbit hole.
[1816.98 --> 1817.26]  Yeah.
[1817.34 --> 1821.28]  I am convinced that you should at least attempt to do this.
[1821.88 --> 1828.08]  I don't think you should feel bad if you decide that it's not for you because it is a rabbit hole.
[1828.08 --> 1843.10]  It does require, you know, a certain level of responsibility over time, especially if your family or others around you begin to depend on those services and you can no longer dedicate the time necessary to keep going.
[1843.72 --> 1851.10]  I suppose as long as you've got the time and the desire, then self-hosting is certainly fruitful.
[1851.86 --> 1852.94]  You will learn a lot.
[1852.94 --> 1858.04]  I learned a lot about many things that I just never had to really consider before.
[1858.84 --> 1863.20]  And I think that I'm a better conversationalist around technology because of it.
[1863.34 --> 1868.54]  And I think that I'm just generally more wise to the tech in the world.
[1869.06 --> 1875.80]  Whereas before I had a once removed relationship with it where I would work with someone who was deeper in the knowledge.
[1876.00 --> 1877.34]  And now I have firsthand knowledge.
[1878.10 --> 1878.24]  Yeah.
[1878.94 --> 1880.30]  100% agree.
[1880.30 --> 1886.56]  I have self-hosted many things throughout my life and I learned so much doing so.
[1886.84 --> 1898.94]  Both production and small business and friends and family stuff, whether it's self-hosted on machines in my house, which I have done for a long time.
[1898.94 --> 1902.88]  I had a Linux server that ran in my home and I ran all kinds of services off of that.
[1903.02 --> 1911.22]  And then also VPS, self-hosting, shared hosting, self-hosting, you know, just managing your own things.
[1911.38 --> 1916.10]  And yeah, the amount of learning is really not to be compared with.
[1916.18 --> 1917.00]  You can't fake it.
[1917.08 --> 1917.98]  You just, it's just real.
[1917.98 --> 1922.58]  But the learning comes through trial and it comes through things going wrong.
[1923.20 --> 1931.96]  And this post that he writes is like, here are the, one of the sections is like things that broke in the last six months, you know?
[1932.20 --> 1932.44]  Yeah.
[1932.54 --> 1934.56]  And it's like, yeah, you're going to have that kind of stuff.
[1934.56 --> 1937.52]  And it's similar to any sort of maintenance.
[1938.28 --> 1943.84]  I don't know how many large appliances and vehicles you own, Adam, but you and I are both old enough to know.
[1944.84 --> 1954.68]  A house, a car, a laundry machine, anything that's significantly expensive and significantly complicated breaks.
[1955.28 --> 1957.64]  And when you own it, you own the break, you know?
[1957.82 --> 1958.06]  Yeah.
[1958.06 --> 1961.28]  And you're going to either pay to fix it or learn to fix it.
[1962.22 --> 1971.10]  And for me as a guy in my 40s with a pretty large family, I don't have the patience or the time to self-host anymore.
[1971.60 --> 1974.16]  But I think everybody else should.
[1976.06 --> 1979.88]  Not everybody else, but, you know, given your circumstance, I think everyone should try it.
[1980.24 --> 1981.20]  And some people should do it.
[1981.20 --> 1991.04]  And there's certainly things that I've thought about self-hosting, even though I don't have the time, because of privacy and autonomy and the independence that Christian speaks of.
[1991.12 --> 1999.00]  For me, more importantly than the learning, because I've already learned enough, I think, in the category, is there are things where I want the independence and the privacy.
[1999.40 --> 2004.86]  And so that's why I consider it, even though I don't want to do it, because I know how much of a headache it can be.
[2004.86 --> 2005.78]  Mm-hmm.
[2006.44 --> 2006.72]  Yeah.
[2007.26 --> 2014.76]  I'm definitely not in the, for me, specifically, Adam, you must self-host all the things camp.
[2015.36 --> 2016.28]  I'm not in that camp.
[2016.36 --> 2019.90]  Well, I asked you to self-host Zulip, and you were like, eh, you're on the show, remember that?
[2019.94 --> 2021.70]  No, I was like, I was not excited.
[2022.22 --> 2023.40]  Well, it's just too critical.
[2024.04 --> 2028.42]  I do self-hosting for the things that are, that I don't mind being down.
[2028.68 --> 2031.24]  If somebody's like, Adam, why is Zulip not working?
[2031.48 --> 2033.02]  That's the worst world for me ever.
[2033.02 --> 2034.10]  I don't want to live in that world.
[2034.86 --> 2036.28]  I don't want to be responsible to that degree.
[2036.50 --> 2037.60]  I don't mind assisting.
[2037.82 --> 2041.16]  It's just not something I want to personally be responsible for.
[2041.90 --> 2045.34]  Nor do I think I have the expertise currently to do so.
[2045.56 --> 2047.06]  Well, you probably would earn it over time.
[2047.22 --> 2048.62]  I would earn it over time, but I'm like.
[2049.22 --> 2049.80]  Battle scars.
[2049.98 --> 2050.94]  Yeah, I mean.
[2051.02 --> 2052.90]  And you get better at it, and it could become faster.
[2053.32 --> 2053.60]  Yeah.
[2053.60 --> 2056.28]  Because you're like, oh, I know what probably went wrong.
[2056.80 --> 2057.06]  Yeah.
[2057.48 --> 2057.86]  You know?
[2058.26 --> 2058.98]  Confidence is there.
[2059.10 --> 2059.74]  I'm sure I could do it.
[2059.84 --> 2061.36]  It's not about lack of confidence.
[2061.36 --> 2065.06]  It's about lack of desire to hold the responsibility.
[2066.14 --> 2072.42]  I would prefer Zulip to run as Zulip should run and be up for everyone all the time and
[2072.42 --> 2073.18]  it not be my problem.
[2073.54 --> 2075.86]  So what are some things you're okay with hosting?
[2076.04 --> 2076.40]  Plex.
[2076.78 --> 2077.16]  Plex.
[2077.48 --> 2077.88]  Pyhole.
[2078.44 --> 2079.36]  Stupid stuff.
[2079.74 --> 2081.46]  Pyhole sounds like it's critical, though.
[2081.72 --> 2083.12]  It is, but it's so easy to run.
[2083.38 --> 2085.08]  Well, that's what you find out about a lot of these things.
[2085.18 --> 2086.04]  They're very easy to run.
[2086.46 --> 2086.84]  Yes.
[2086.86 --> 2089.68]  And then you just got to make sure that they're updated or fix them.
[2089.84 --> 2092.10]  You know, like getting it set up is the hard part.
[2092.48 --> 2092.82]  Right.
[2093.20 --> 2094.30]  They run while they run.
[2094.92 --> 2096.10]  Things go wrong here or there.
[2096.36 --> 2098.12]  You know, a network connection goes down.
[2098.28 --> 2098.56]  Mm-hmm.
[2098.78 --> 2100.42]  A time database gets out of sync.
[2100.82 --> 2101.78]  An update fails.
[2102.50 --> 2102.74]  Yeah.
[2103.26 --> 2107.12]  Usually for me, it's like, oh, critical vulnerability in this thing that you don't care about anymore.
[2107.12 --> 2111.10]  And it's like, oh, I have to go update right now, even though three people are using
[2111.10 --> 2111.42]  this.
[2111.72 --> 2111.92]  You know?
[2112.54 --> 2113.20]  Like that kind of stuff.
[2113.20 --> 2118.18]  But most of the learning and most of the pain comes through that initial setup with
[2118.18 --> 2119.02]  the new technology.
[2119.88 --> 2120.12]  For sure.
[2121.04 --> 2123.38]  You know, this person's, what is his name?
[2123.46 --> 2123.76]  Christian?
[2123.92 --> 2124.18]  Is that right?
[2124.48 --> 2124.68]  Yeah.
[2125.36 --> 2126.44]  Christian goes deep.
[2126.84 --> 2128.30]  You know, he is self-hosting.
[2128.46 --> 2132.40]  And he gives a list of things that he is self-hosting.
[2132.42 --> 2133.42]  I'm trying to find a list quickly.
[2133.88 --> 2134.36]  At the top.
[2134.90 --> 2135.52]  My services.
[2135.78 --> 2136.08]  Yes.
[2137.10 --> 2137.86]  Pyhole's in there.
[2138.50 --> 2139.00]  Router OS.
[2139.24 --> 2139.88]  I won't read them all.
[2140.02 --> 2141.38]  Unified Controller's in there.
[2141.72 --> 2142.48]  TrueNAS is in there.
[2142.48 --> 2149.56]  I think he even mentioned he does it via ProxBox, which I would never do after trying it once.
[2150.04 --> 2154.18]  I don't like to virtualize a NAS and virtualize the access to the disks.
[2154.36 --> 2155.14]  It's just too critical.
[2155.58 --> 2160.94]  So I feel like a dedicated box to your storage device is proper.
[2160.94 --> 2164.08]  Even if it's overkill or a waste.
[2164.24 --> 2165.28]  You know it's done right.
[2166.04 --> 2171.12]  And you can pull the disk immediately if you need to and swap it and, you know, do some
[2171.12 --> 2175.90]  stuff with TrueNAS to ZFS or straight to ZFS if that's all you have.
[2176.44 --> 2176.86]  VS Code.
[2176.94 --> 2177.80]  I thought that was kind of interesting.
[2178.30 --> 2178.42]  Yeah.
[2178.54 --> 2179.10]  VS Code.
[2179.22 --> 2181.02]  I guess it's like a web-based version of it.
[2181.02 --> 2182.84]  Or like how do you self-host VS Code?
[2183.18 --> 2184.68]  So slight plug.
[2184.80 --> 2186.52]  I think they might be sponsoring this episode too.
[2187.12 --> 2189.22]  And I'm not saying this because they sponsored it.
[2189.40 --> 2190.64]  I truly like their technology.
[2190.80 --> 2191.80]  Coder.com is so cool.
[2192.44 --> 2197.22]  I think it might be like this because Coder.com is a cloud development environment.
[2197.22 --> 2199.44]  So we've heard of this with like Codespaces, right?
[2199.44 --> 2200.82]  And Gitpod.
[2201.28 --> 2206.74]  Those are all primarily Docker container-based where you're not running in a VM, you're running
[2206.74 --> 2207.22]  in a container.
[2208.58 --> 2210.24]  And Coder.com does both.
[2210.44 --> 2216.16]  But what they do uniquely is when you, I ran, I actually have a Coder.com instance in Proxmox.
[2216.22 --> 2222.30]  So I dedicated a brand new VM I created from Ubuntu, made that the Coder box, and now I can
[2222.30 --> 2225.14]  turn that into a cloud development environment.
[2225.14 --> 2232.02]  I can have code a new project, a new instance, like a new provision of a thing for me and
[2232.02 --> 2234.20]  my developers, which is just me because I was just tinkering with it.
[2234.94 --> 2239.26]  And inside of Coder, the reason why I bring it up is not to plug them, is because whenever
[2239.26 --> 2244.56]  you launch the code, you launch VS Code, you can at least, you can launch Vim as well.
[2244.82 --> 2245.90]  So it's for all the hackers.
[2246.60 --> 2253.58]  You can launch VS Code in the browser, and it will connect to the code on the VM in the
[2253.58 --> 2253.90]  browser.
[2253.90 --> 2256.28]  Like, you're literally editing it like that.
[2256.36 --> 2261.18]  I think that's what he's doing here, is he's self-hosting similar to that, but like, it's
[2261.18 --> 2266.50]  the dedicated layer of just VS Code, where it's remote connecting to somehow the code on
[2266.50 --> 2269.90]  your local machine via the browser, probably through the LAN.
[2270.72 --> 2271.16]  That's hardcore.
[2271.46 --> 2272.16]  That is so hardcore.
[2272.46 --> 2277.96]  And I don't know why you would do that, but, you know, in the Coder instance, you do it because
[2277.96 --> 2278.48]  of resources.
[2278.48 --> 2283.72]  You want to take all those resources, CPU, RAM, GPU, whatever you need to dedicate to your environment,
[2283.72 --> 2288.34]  into that CDE, that cloud development environment, versus your local.
[2289.18 --> 2290.00]  One more layer.
[2290.22 --> 2293.30]  This is something that I think is kind of cool, is I have my Jekyll blog still yet.
[2293.46 --> 2297.14]  So, adamstokowiak.com is a Jekyll blog, basically.
[2297.74 --> 2300.62]  I do not run that locally.
[2300.80 --> 2302.74]  I have set that up to run inside of Docker.
[2303.42 --> 2308.66]  Because I don't want to fiddle with Ruby and any of the gems and stuff like that locally.
[2308.82 --> 2312.82]  Like, it's all inside the Docker container, which I think is so cool.
[2312.82 --> 2315.06]  And never have to mess with local stuff.
[2315.64 --> 2316.02]  That is cool.
[2316.56 --> 2319.60]  I'm sure a lot of these services are Dockerized, which makes it a lot easier.
[2320.04 --> 2320.98]  Jellyfin for sure is.
[2321.22 --> 2321.34]  Yeah.
[2321.42 --> 2321.60]  Yeah.
[2321.98 --> 2327.20]  But, I mean, he's got MariahDB running locally, Redis, InfluxDB, Jellyfin, as you mentioned,
[2327.96 --> 2332.52]  GitT, so he's like local Git server, local wiki.
[2333.28 --> 2338.32]  Of course, Nginx, because his website and his blog are both hosted at, I assume this is his
[2338.32 --> 2338.68]  house.
[2339.78 --> 2344.00]  This is like a homesteading version of software, right?
[2344.10 --> 2344.74]  He's a homesteader.
[2344.74 --> 2351.26]  You know, I'm glad you brought that up because I thought that whenever I saw his photo of his
[2351.26 --> 2355.10]  garden, I was like, self-hosting and gardening go hand in hand.
[2355.22 --> 2355.96]  A hundred percent.
[2356.08 --> 2356.30]  Right?
[2356.74 --> 2357.10]  Yeah.
[2357.68 --> 2358.42]  Autonomy, man.
[2358.54 --> 2359.22]  Like, leave me alone.
[2359.32 --> 2360.22]  I'm going to run my life.
[2360.40 --> 2363.54]  But that's like, if you're gardening, then you're like, I want to be self-sustaining.
[2364.10 --> 2364.40]  Right.
[2364.54 --> 2367.66]  But then you're also tethered to technology because you're still self-hosting.
[2367.66 --> 2371.08]  So you're not, you're not like ejecting from the world, right?
[2371.12 --> 2377.60]  You're not remote in Denver on a cliff or not Denver, like Colorado as a proper state
[2377.60 --> 2380.36]  on a cliff in the mountains remote.
[2381.20 --> 2382.82]  You're still tethered to technology.
[2383.32 --> 2383.40]  Right.
[2383.46 --> 2386.02]  You're not living out in the boondocks of Montana.
[2386.56 --> 2386.68]  Yeah.
[2387.62 --> 2388.58]  I like Montana too.
[2388.78 --> 2388.92]  Yeah.
[2388.92 --> 2397.70]  What this looks like to me, and I don't want to be negative Nancy or negative Tim or pick
[2397.70 --> 2405.64]  your name by any means, is if you're trying to be productive, this seems like a lot of
[2405.64 --> 2408.68]  yaks that could be shaved on the daily.
[2408.68 --> 2409.36]  Right.
[2409.40 --> 2414.36]  Like if you're self-hosting your local Git server, provided this is all routinely easily
[2414.36 --> 2418.40]  maintained, your VS code is in the browser.
[2418.58 --> 2422.14]  You're maintaining whatever that is and whatever can go wrong could go wrong and you can fix
[2422.14 --> 2422.36]  it.
[2422.74 --> 2424.48]  But when it goes wrong, you got to fix it.
[2425.10 --> 2432.58]  Do you think that this is a list of shiny objects that can be distractions and or just
[2432.58 --> 2436.82]  simply things that need to be shaved like yaks?
[2436.82 --> 2439.32]  I don't know because nerds are going to nerd out.
[2439.42 --> 2444.60]  And I feel like some of this stuff is probably him nerding out, which is totally fine to do.
[2445.56 --> 2449.66]  So in the case of that, like define productive if this is what you enjoy.
[2449.76 --> 2450.90]  He obviously enjoys it.
[2451.22 --> 2457.96]  So it's almost like similar to gardening where if you don't love gardening, don't go plant
[2457.96 --> 2460.02]  a big garden because it's a whole bunch of work.
[2460.02 --> 2464.20]  And the people who continue and persist in that, they love the work.
[2464.30 --> 2465.18]  They love the process.
[2465.18 --> 2468.08]  And so for them, that's what it's all about.
[2469.02 --> 2472.46]  And so, yeah, I mean, there's certainly some yak shaving going on.
[2472.52 --> 2476.86]  But, you know, if you enjoy shaving yaks, you get a yak, don't talk back.
[2476.94 --> 2477.22]  I don't know.
[2477.28 --> 2478.76]  I just got stuck on yak there.
[2478.84 --> 2479.32]  But go ahead.
[2480.00 --> 2483.56]  Christian closes with this, which might be a good end cap to our discussion.
[2483.66 --> 2487.54]  He says, if you're a software engineer, I recommend self-hosting things.
[2487.64 --> 2491.72]  You learn a whole bunch of things through forced exposure to problems that you'll be less
[2491.72 --> 2495.54]  likely to encounter in your day job, which in itself is a benefit.
[2496.02 --> 2500.86]  Even better, I do believe you'll wind up using at least some of these things in your
[2500.86 --> 2505.36]  day job eventually, provided you work on something vaguely back-end related.
[2505.48 --> 2511.74]  By hosting stuff yourself, you also get a reasonable level of autonomy or at the very least some hedging
[2511.74 --> 2518.48]  against the corporate dream of your entire life being a perpetually rented subscription.
[2519.28 --> 2520.28]  I think that's nice.
[2520.96 --> 2521.24]  Poetic.
[2521.82 --> 2522.36]  Good ender.
[2522.46 --> 2524.04]  I mean, it's certainly romantic.
[2524.84 --> 2525.86]  That part gets me.
[2526.02 --> 2526.74]  That does get me.
[2526.76 --> 2528.78]  Not enough to do it, but enough to appreciate it.
[2529.10 --> 2529.86]  That's where I'm at.
[2529.90 --> 2532.32]  Because, like, he mentions Nextcloud in one of his services.
[2533.04 --> 2533.32]  Uh-huh.
[2533.66 --> 2537.38]  I don't want to be, I mean, maybe I do at some point, but I don't, at least right now,
[2537.44 --> 2543.38]  I don't want to be responsible for calendars being up, photos being up, file services being
[2543.38 --> 2543.74]  up.
[2543.92 --> 2545.22]  I mean, it just seems like, oof.
[2546.42 --> 2548.02]  But maybe Nextcloud makes it easy.
[2548.02 --> 2552.04]  I just feel like in the moment, without having tried it, it feels like a lot.
[2552.94 --> 2555.26]  And I speak to that because of the rented subscription.
[2556.68 --> 2558.92]  The easiest place you spend money is, like, Dropbox.
[2559.56 --> 2562.28]  Calendar, I guess, comes with our Google Suite for our business.
[2562.28 --> 2564.94]  And in other cases, you're getting it for-
[2564.94 --> 2566.30]  Or iCloud, if you have an iCloud account.
[2566.58 --> 2566.82]  Yeah.
[2567.26 --> 2575.66]  So you're, you are on this, you will own nothing and be happy, you know, World Forum, World Economic
[2575.66 --> 2579.78]  Forum prediction several years back where it's like, someone famously said, and infamously,
[2579.88 --> 2583.04]  maybe even infamously said, you will own nothing and be happy.
[2583.92 --> 2585.72]  I just don't know about that.
[2585.78 --> 2590.60]  Like, the perpetual, it feels like a long-term debt that society puts on you.
[2590.60 --> 2590.64]  Yeah.
[2591.18 --> 2596.12]  Like, to own an iPhone, you kind of inherit a level of perceived debt.
[2596.82 --> 2598.62]  Necessary cost to maintain the service.
[2598.92 --> 2599.12]  Yeah.
[2599.20 --> 2601.58]  Not just the phone service itself, but the things that come with it.
[2601.90 --> 2602.70]  To use it.
[2603.12 --> 2603.76]  Like photos.
[2604.48 --> 2606.90]  I don't know if that's the right word, but I'm with you in spirit.
[2607.06 --> 2607.78]  I think that-
[2607.78 --> 2609.26]  Well, it's debt if you-
[2609.26 --> 2611.14]  What I mean by, the reason why I say debt-
[2611.14 --> 2611.90]  Debt, you have to pay back.
[2612.12 --> 2614.80]  Is that you commit to a payment.
[2615.12 --> 2615.70]  Oh, you're renting.
[2615.70 --> 2616.06]  Right.
[2616.84 --> 2619.44]  You're indebted to pay for the service if you use the service.
[2620.16 --> 2620.56]  Yes.
[2620.60 --> 2622.22]  You have to pay for the service if you use the service.
[2622.38 --> 2624.56]  And if you stop paying for the service, then the service goes away.
[2625.34 --> 2629.78]  And I think renting is totally reasonable in certain cases.
[2629.78 --> 2632.38]  Like, I don't want to own a calendar service.
[2632.48 --> 2633.26]  I want to rent one.
[2633.48 --> 2633.84]  Mm-hmm.
[2633.84 --> 2640.34]  Because the calendar is only important over the next month, weeks, and maybe years.
[2640.98 --> 2643.94]  But have you ever considered about your historic calendar?
[2644.14 --> 2645.46]  I couldn't care less what was on there.
[2645.54 --> 2647.28]  Every once in a while, you go back and you're like, what day was that?
[2647.32 --> 2648.10]  And you check an event.
[2648.46 --> 2648.78]  Mm-hmm.
[2648.86 --> 2650.32]  And you're like, oh, I didn't put it in the calendar.
[2650.50 --> 2651.04]  And you're like, dang it.
[2651.30 --> 2651.52]  Yeah.
[2651.72 --> 2653.34]  But if it's in there, it's kind of useful.
[2653.46 --> 2656.76]  But your past calendar events, I couldn't possibly care less.
[2656.90 --> 2657.64]  Rent that service.
[2658.14 --> 2659.32]  If it goes away, it goes away.
[2659.88 --> 2663.12]  Other things, photos, opposite, right?
[2663.12 --> 2666.02]  Like, the history is what it's all about with photos.
[2666.64 --> 2668.48]  That's the kind of stuff that I'm afraid to self-host.
[2668.80 --> 2673.68]  Availability and history and reliability that it's there forever.
[2674.62 --> 2676.70]  Deletion of photos is very, very bad.
[2677.54 --> 2677.74]  Yeah.
[2678.66 --> 2679.26]  All right.
[2679.32 --> 2682.96]  Let's move on to our final topic.
[2683.22 --> 2684.90]  So, you know how we take episode requests.
[2685.24 --> 2685.54]  Do we?
[2686.36 --> 2687.02]  Yeah, man.
[2687.10 --> 2688.06]  Oh, that's so cool.
[2688.54 --> 2689.86]  It just takes a while sometimes.
[2689.86 --> 2692.94]  Is it at changelog.com slash request?
[2693.62 --> 2694.12]  That's right.
[2694.26 --> 2694.90]  Oh, gosh.
[2694.94 --> 2695.74]  That's a great URL.
[2696.02 --> 2696.46]  I love that.
[2696.52 --> 2697.48]  That is really nice.
[2698.48 --> 2700.44]  Well, we read every request.
[2701.04 --> 2702.66]  And we don't fulfill every request.
[2702.82 --> 2705.44]  But every once in a while, we dig one out of the ashes.
[2705.94 --> 2706.24]  Oof.
[2706.54 --> 2708.60]  And we would fulfill it three years later.
[2709.36 --> 2711.58]  So, shout out to listener Alex if you're still out there.
[2711.64 --> 2715.28]  If you're still listening, Alex, three years later, you're a trooper, man.
[2715.36 --> 2716.18]  We appreciate you.
[2716.50 --> 2717.72]  Because that's a long time to listen to.
[2717.90 --> 2718.80]  And you should be in Zulip.
[2719.22 --> 2719.58]  Anything.
[2721.20 --> 2724.48]  And you should finally be happy that we've answered your request.
[2724.80 --> 2729.16]  This one's navel-gazy and self-serving to a certain degree, which is why we didn't do it for a long time.
[2729.16 --> 2736.44]  But I thought it'd be a nice end cap to a friends episode with just the two of us where we can take at least one listener question slash request.
[2736.58 --> 2738.62]  Alex wants us to talk about how we podcast.
[2739.16 --> 2739.26]  Hmm.
[2739.60 --> 2742.26]  How we produce podcasts.
[2742.26 --> 2752.62]  He said he's heard of some really cool workflows from both the Linux people and you guys, which I guess means we're not Linux people, about different ways you record and upload scripts.
[2752.62 --> 2758.58]  He says, you guys, if I recall, have some type of encoded timestamps to the MP3s.
[2759.48 --> 2763.20]  Destination Linux timestamp the episode while they record.
[2764.36 --> 2769.70]  Jupiter Broadcasting uses some type of all-in-one container for recording, if he recalls.
[2770.46 --> 2772.00]  And we have Masterfeeds.
[2772.18 --> 2773.20]  They also have Masterfeeds.
[2773.20 --> 2778.02]  So just some of the inside baseball on how we produce our shows.
[2778.34 --> 2779.82]  Maybe some of the nerdier parts.
[2780.00 --> 2780.40]  I don't know.
[2780.50 --> 2784.42]  Some of it's boring, at least to us because we do it, but maybe interesting to other people.
[2785.44 --> 2791.48]  I think it's super interesting to other people because I've been having some conversations with a future branded podcast we're producing.
[2792.06 --> 2792.34]  Oh, yeah.
[2792.34 --> 2804.02]  And they have questions and I have answers and they sit back and listen as if we have pulled up a glass of favorite drink near a campfire and it's just so fun.
[2805.10 --> 2805.54]  Seriously.
[2805.96 --> 2807.16]  I didn't think what we'd done.
[2807.16 --> 2807.42]  Really?
[2807.64 --> 2807.92]  Yeah.
[2807.98 --> 2815.32]  I didn't think what we've done is, you know, you don't know what you know until you try and teach other people, basically.
[2815.52 --> 2815.98]  Right.
[2815.98 --> 2822.22]  And then they're like, wow, I mean, to us, it's logical and simple because we've repeated it so many times that.
[2822.64 --> 2823.28]  And refined it.
[2823.38 --> 2823.64]  Right.
[2823.70 --> 2826.98]  We could probably do a lot of what we do to some degree in our sleep.
[2827.56 --> 2827.92]  Right.
[2828.08 --> 2829.24]  You know, figurative speech.
[2829.98 --> 2830.48]  Figurative speech.
[2831.00 --> 2832.72]  I swear I'm not sleeping right now.
[2832.84 --> 2836.72]  Not literally in my sleep, but for example, I'll give you an example.
[2837.24 --> 2842.64]  And this is not necessarily answering Alex's question, except for maybe to flex a little bit and I'm not a flexor.
[2842.64 --> 2849.28]  However, I wrapped up this conversation yesterday for this Future Brain of Podcast that I'm not sure I can mention yet, which was why I'm being vague.
[2850.16 --> 2860.60]  And the idea was, okay, we've got the music components together and they can't hear slash see the future vision that I can see coming because I've got the experience and we've got the experience.
[2860.86 --> 2862.32]  And I know where we're trying to take them.
[2862.84 --> 2864.18]  They haven't done that yet.
[2864.20 --> 2868.38]  And so they have questions and reservations and apprehensions that need to be resolved.
[2868.38 --> 2875.28]  And the easiest way to do that is to give them a version, a listenable version of it.
[2875.90 --> 2886.54]  And so yesterday, within the span of an hour and a half, I think, I sat down and produced a fake episode that uses the intro music and the timing.
[2886.72 --> 2889.02]  I script-writed the intro and how I think it should work.
[2889.02 --> 2895.26]  How it blends into the show, how the show ends and how the music comes back in, how the show could end.
[2895.62 --> 2902.68]  And I used all the components that we've produced for them and gave them three different versions because we have three different outros they're considering.
[2902.88 --> 2907.12]  The intro is solid and it's not being scrutinized in any regard.
[2907.66 --> 2911.78]  But the outro is like, they've got questions of how it should, should they be the same?
[2911.88 --> 2912.52]  Should they match up?
[2912.58 --> 2913.52]  How similar should they be?
[2913.52 --> 2918.54]  And, you know, doneness is the enemy of perfection, right?
[2918.60 --> 2923.00]  If you can't just get it out there, it's going to, well, perfection is the enemy of doneness.
[2923.20 --> 2924.08]  I said that backwards.
[2924.58 --> 2925.98]  You can't strive for perfection.
[2926.12 --> 2934.24]  You can obviously, you know, don't wait until it's perfect or seemingly perfect or all the answers are answered to get momentum and move.
[2934.24 --> 2946.48]  The reason why I'm telling you this story is that in the span of, you know, an hour, I solidified and created what has been in my mind for many months waiting to take action on when the time is right.
[2946.90 --> 2947.80]  And it's done.
[2947.96 --> 2954.20]  And I think when you listen to it, you'll be like, yeah, that's pretty, that's a pretty good version of what it's going to be.
[2954.64 --> 2959.40]  It's obviously four minutes, not 40 minutes like it might be or will be.
[2959.40 --> 2964.52]  It's a micro version, listenable, that's actually kind of compelling.
[2965.08 --> 2968.26]  And when I listened back to it, I was like, I kind of want to listen to the whole thing now.
[2968.56 --> 2969.64]  And it's just a fake.
[2969.80 --> 2971.70]  It's just, it's just episode zero.
[2971.70 --> 2972.24]  It's not a teaser.
[2972.50 --> 2972.66]  Yeah.
[2972.80 --> 2973.88]  There's nothing, there's nothing.
[2974.14 --> 2975.08]  Well, there's something in there.
[2975.28 --> 2976.66]  Well, but not, not yet.
[2976.68 --> 2978.06]  If I told you, I would reveal too much.
[2978.62 --> 2978.98]  Sure.
[2979.22 --> 2982.00]  But it's, I was like, yeah, I would listen to this.
[2982.04 --> 2982.50]  This is cool.
[2982.50 --> 2993.84]  And the reason why I say that is because we've done it so much that in the span of an hour-ish, I created what is likely to be the future of that.
[2994.54 --> 2998.78]  Not two days or several days and, you know, had to go back and forth.
[2998.80 --> 2999.88]  It was just done.
[3000.36 --> 3002.32]  You're just inventing the future right in front of their eyes.
[3002.34 --> 3002.56]  That's right.
[3002.66 --> 3002.98]  Your ears.
[3003.22 --> 3003.50]  That's right.
[3004.10 --> 3004.46]  All right.
[3004.52 --> 3005.52]  Good, solid flex.
[3005.52 --> 3015.40]  Stay tuned for branded podcast upcoming of Adam's design with a partner, which will be the second time we've accomplished such.
[3015.76 --> 3021.56]  We do produce Big Tent, Grafana's Big Tent with them, which is the first one.
[3022.32 --> 3026.50]  And selective, but open to that process with others.
[3026.66 --> 3029.74]  Very selective strategically because we're a small team.
[3029.74 --> 3039.02]  But to more directly answer Alex's question, maybe he's interested in tools, techniques, like how we do what we do and what we use.
[3039.18 --> 3040.26]  He's not answering my flex.
[3040.32 --> 3041.60]  He's like, Adam, just be quiet.
[3042.18 --> 3042.36]  Yeah.
[3042.52 --> 3044.12]  Let Jared tell the true story here.
[3044.12 --> 3048.18]  We're going to chapter that one, Adam flexes, and then we'll have the real answer.
[3048.54 --> 3050.62]  Jared answers Alex directly is the next chapter.
[3050.62 --> 3055.58]  What's up, friends?
[3055.74 --> 3060.50]  I'm here with Cal Carberry, co-founder and CTO at Coder.com.
[3060.50 --> 3074.02]  So Coder.com is a cloud development environment, a CDE, and you run all the clouds, AWS, Azure, GCP, you run on-prem, and you're no stranger to competition, right?
[3074.02 --> 3083.26]  The competition out there is well known, but what shocks you, what surprises you about the state of cloud development environments and how developers are leveraging them?
[3083.66 --> 3084.62]  You know, it actually shocked me.
[3084.78 --> 3088.86]  The majority of our largest provision customers do not use containers with their development environments.
[3088.94 --> 3093.64]  They actually use VMs on like GCP, AWS, or some kind of mixture of them.
[3093.72 --> 3102.10]  One of the largest auto manufacturers, they have like a little bit over a thousand devs that use Coder every day, and they use a mixture of Azure, AWS, and GCP.
[3102.10 --> 3108.36]  So I've used Docker, I've used VMs, but take me into the technical details.
[3108.56 --> 3112.48]  What is it that's different between a VM and running something in Docker?
[3112.82 --> 3122.38]  Kind of like all existing solutions, like kind of our competitors in the market, all really have a container-based approach where you build like a Docker container and developers work inside of that.
[3122.52 --> 3130.76]  And it faces a couple limitations because, you know, Adam, like if, you know, on your machine right now, 100%, you're not working inside of a Docker container doing this discussion, right?
[3130.76 --> 3131.78]  It's just very different.
[3132.02 --> 3137.02]  So there's a lot of software expectations that actually don't really work inside of a container.
[3137.42 --> 3142.02]  An example is a customer of ours is Square, and they do stuff with a payment terminal.
[3142.32 --> 3145.42]  And so they need essentially like hardware accelerated Android.
[3145.74 --> 3148.28]  That is just really finicky to get working in a container.
[3148.56 --> 3156.06]  You totally can pass DevKVM into a container and get hardware accelerated virtualization, but it's a little trickier and a little more janky.
[3156.06 --> 3159.32]  And so they'd rather just be like, no, the simple thing is give everyone a VM.
[3159.60 --> 3164.88]  There's no point to change the way that we work in entirety to do some weird virtualization jank.
[3165.00 --> 3167.68]  It just makes more sense to give them a VM that we know works.
[3168.50 --> 3172.52]  Well, it might be time to consider a cloud development environment.
[3173.02 --> 3174.16]  And open source is awesome.
[3174.58 --> 3176.40]  And Coder is fully open source.
[3176.80 --> 3184.76]  You can go to Coder.com, get a demo or try it right now, or even start a 30-day trial of Coder Enterprise.
[3184.76 --> 3191.12]  Once again, Coder.com, that's C-O-D-E-R.com, Coder.com.
[3191.22 --> 3195.62]  And I'm also here with Todd Kaufman, CEO of TestDouble, TestDouble.com.
[3195.76 --> 3199.20]  You may know TestDouble from our good friend, Justin Serrales.
[3199.58 --> 3204.24]  So Todd, on your homepage, I see an awesome quote from Eileen Nucato.
[3204.72 --> 3209.70]  She says, quote, hot take, just have TestDouble build all your stuff, end quote.
[3209.70 --> 3215.12]  We did not pay Eileen for that quote, to be clear, but we do very much appreciate her sharing it.
[3215.46 --> 3223.00]  Yeah, we had the great fortune to work with Eileen and Aaron Patterson on the upgrade of GitHub's Ruby Rails framework.
[3223.48 --> 3225.56]  And that's a relatively complex problem.
[3225.68 --> 3227.04]  It's a very large system.
[3227.18 --> 3232.08]  There's a lot of engineers actively working on it at the same time that we were performing that upgrade.
[3232.08 --> 3238.10]  So being able to collaborate with them, achieve the outcome of getting them upgraded to the latest and greatest Ruby on Rails
[3238.10 --> 3244.22]  that has all of the security patches and everything that you would expect of the more modern versions of the framework,
[3244.22 --> 3251.84]  while still not holding their business back from delivering features, we felt was a pretty significant accomplishment.
[3251.84 --> 3258.24]  And it's great to, you know, work with someone like Eileen and Aaron, because we obviously learned a lot.
[3258.34 --> 3260.14]  We were able to collaborate effectively with them.
[3260.20 --> 3265.16]  But to hear that they were delighted by the outcome as well is very humbling for sure.
[3265.84 --> 3268.16]  Take me one layer deeper on this engagement.
[3268.44 --> 3270.82]  How many folks did you apply to this engagement?
[3271.38 --> 3272.88]  What was the objective?
[3273.30 --> 3274.84]  What did you do, etc.?
[3275.42 --> 3279.40]  Yeah, I think we had between two and four people at any phase of the engagement.
[3279.40 --> 3281.78]  So we tend to run with relatively small teams.
[3282.02 --> 3286.24]  We do believe smaller teams tend to be more efficient and more productive.
[3286.46 --> 3290.12]  So wherever possible, we try to get by with as few people as we can.
[3290.44 --> 3293.96]  This was a fairly clear set of expectations.
[3293.96 --> 3298.68]  We wanted to get to Rails, I believe 5.2 at the time, and Ruby like 2.5.
[3298.78 --> 3299.94]  Don't hold me to those numbers.
[3300.16 --> 3302.70]  But we had clear expectations at the outset.
[3302.70 --> 3312.44]  So from there, it was just a matter of figuring out the process that we were going to pursue to get these upgrades done without having a sizable impact on their team.
[3312.66 --> 3319.60]  A lot of the consultants on the project had some experience doing Rails upgrades, maybe not at that scale at that point.
[3319.72 --> 3332.06]  But it was really exciting because we were able to kind of develop a process that we think is very consistent in allowing Rails upgrades to be done without like providing a lot of risk to the client.
[3332.06 --> 3338.00]  So there's not a fear that, hey, we've missed something or, you know, this thing's going to fall over under scale.
[3338.00 --> 3345.14]  We do it very incrementally so that the team can, like I said, keep working on feature delivery without being impacted.
[3345.14 --> 3357.70]  But also so that we are very certain that we've covered all the bases and really got the system to a state where it's functionally equivalent to the last version, just on a newer version of Rails and Ruby.
[3357.70 --> 3359.34]  Very cool, Todd. I love it.
[3359.54 --> 3365.20]  Find out more about Test Double's software investment problem solvers at TestDouble.com.
[3365.50 --> 3367.30]  That's TestDouble.com.
[3367.42 --> 3371.96]  T-E-S-T-D-O-U-B-L-E dot com.
[3371.96 --> 3381.12]  I do have a propensity to answer questions directly, which some people appreciate and others think is boring.
[3381.96 --> 3383.90]  So your mileage may vary.
[3384.26 --> 3386.90]  But in brief, okay, so tools and techniques.
[3387.12 --> 3394.88]  We record everything on Riverside.fm, which is a proprietary in-browser technology that we pay for as a service.
[3394.96 --> 3395.78]  Happy to rent it.
[3396.56 --> 3397.78]  Don't want to self-host it.
[3397.98 --> 3399.36]  I'm sure it's very complex.
[3399.36 --> 3400.32]  Never.
[3400.80 --> 3405.94]  And very cool use of web tech.
[3406.54 --> 3408.72]  I mean, and it's gotten better, continues to get better.
[3409.12 --> 3411.54]  We've been on it for at least a couple of years now.
[3412.22 --> 3414.46]  Very few incidents, so we're happy with the software.
[3415.24 --> 3417.38]  We own a separate account for each of our podcasts.
[3418.08 --> 3419.92]  And everybody logs into their own account.
[3420.06 --> 3420.82]  They record in there.
[3420.82 --> 3429.74]  And that handles the majority of the actual video and audio recording and syncing.
[3430.38 --> 3435.18]  And then we export out of there into Adobe Audition for editing.
[3435.18 --> 3439.02]  We have a kind of a three-step process in our editing.
[3439.18 --> 3440.04]  One's called Prepped.
[3440.22 --> 3441.22]  So we prep the audio.
[3441.82 --> 3446.84]  This has to do with making sure all the tracks line up, all the boring stuff that people don't ever think about.
[3447.48 --> 3453.04]  Sometimes prepping the sounds, you know, trying to get a different version in case the audio of a specific track isn't great.
[3453.14 --> 3455.18]  And then we edit it, content edit.
[3455.18 --> 3457.48]  This is usually our editors.
[3457.74 --> 3461.06]  Shout out to Jason and Brian, who content edit our shows.
[3462.06 --> 3468.10]  And their job is to basically cut out all the bad parts, which is just, you know, awkwardness, weird pauses, et cetera.
[3468.18 --> 3470.52]  They do their work, ums and ahs.
[3470.98 --> 3472.56]  At that point, they leave markers.
[3472.72 --> 3475.62]  So Alex asked about timestamps and chapters and all that.
[3476.24 --> 3480.58]  We don't do any timestamping or marking while we record.
[3480.98 --> 3482.44]  Seems like the ideal time to do it.
[3482.44 --> 3488.18]  But actually, when you're in the moment, in the groove, you're not actually thinking about, oh, this is a great, except for earlier when I said, here's a chapter.
[3488.44 --> 3489.60]  Yeah, every once in a while, I'll think about it.
[3489.66 --> 3493.96]  But you just want to be able to just be free from all that and just enjoy the conversation.
[3494.14 --> 3495.94]  So we aren't doing anything.
[3496.06 --> 3501.68]  I think Riverside has, oh yeah, they have a mark clip button right there that we could use to like set a marker.
[3502.28 --> 3503.00]  But we don't do that.
[3503.00 --> 3504.44]  Sometimes there are things that we know about.
[3504.52 --> 3508.36]  And so we'll just tell our editors afterwards, like, hey, look out for this.
[3508.36 --> 3512.58]  You can drop a marker here, marker there in our locals as we go.
[3513.28 --> 3514.82]  And I've done less of that than I used to.
[3514.90 --> 3515.58]  I used to do it more.
[3516.42 --> 3518.46]  But Jason and Brian take good care of us.
[3518.58 --> 3519.82]  So they handle the edit.
[3519.92 --> 3524.78]  Then they pass it back to us for mastering, which is all the final stuff.
[3525.20 --> 3530.18]  Chapters, ads, voiceovers, music, final edit decisions.
[3530.18 --> 3537.00]  If there's any content editing to do, all of this is in just big old Dropbox folder, basically.
[3537.76 --> 3543.96]  That's organized by show and by episode and separate Adobe Audition sessions for each phase.
[3543.96 --> 3549.18]  So very much a manual version control system that works just fine just by copying files and renaming them.
[3550.16 --> 3556.46]  And then we mix down a WAV file and an MP3 file and we upload them to our website.
[3557.24 --> 3558.04]  Hit publish, baby.
[3558.04 --> 3561.94]  Now that's both detailed and glossy and a bunch of stuff, right?
[3562.52 --> 3562.96]  Yes.
[3563.84 --> 3573.00]  Yeah, the cool thing about the way that Adobe Audition works is that you have a file type called .sesx.
[3574.06 --> 3578.88]  And those files point to a local file set, essentially.
[3579.10 --> 3580.08]  It's like a timeline.
[3580.90 --> 3583.58]  I imagine it's probably, I've never actually read the file type.
[3583.94 --> 3584.88]  I thought it was proprietary, maybe.
[3585.02 --> 3586.16]  It's like an XML file, I think.
[3586.16 --> 3587.28]  It's very XML-like, yeah.
[3587.56 --> 3587.74]  Yeah.
[3588.04 --> 3593.46]  And so when you make these copies of it, the file is like a couple megs at most.
[3593.74 --> 3597.18]  So like, for example, Jared mentioned the prepped version of it.
[3597.20 --> 3602.64]  So we have a show coming up today on these ergonomic, really awesome keyboards from ZSA.
[3603.08 --> 3606.52]  And the prepped file is 130 kilobytes.
[3606.74 --> 3610.56]  The edited version is 2.2 megabytes.
[3610.56 --> 3615.98]  And because the master version only has a couple things added to it, it's the same file size.
[3615.98 --> 3623.44]  Now, once those changes go in, I'm going to produce that right after the show or after this recording that we're literally talking into right now.
[3623.48 --> 3625.44]  I'm going to go do that work in the master file.
[3625.44 --> 3629.42]  And then that file size will grow probably to, at most, three megabytes.
[3629.42 --> 3638.10]  So like these session files are very small and are supported by the local file system, which has recorded sessions in their imported files.
[3638.10 --> 3644.26]  All these different things that are sort of like file system stuff that Adobe Audition uses.
[3644.98 --> 3658.76]  Adobe Audition has been really, really good to use, I would say, over the years because it moves from person to person pretty easily as an independent file system or an independent directory that you can copy and do whatever you need to do with it.
[3658.76 --> 3661.70]  And so we've been very happy on that front.
[3662.08 --> 3675.32]  And even chaptering within in the WAV file, when we do that, there's a span that you can put like a marker and another marker and join those together and make them a chapter or a two-point marker.
[3675.40 --> 3677.40]  I'm not even sure what they call those things, honestly.
[3678.30 --> 3680.24]  Merged markers, something like that.
[3680.82 --> 3681.76]  And let's turn into chapters.
[3682.16 --> 3682.32]  Range.
[3682.46 --> 3683.52]  Range marker, I think.
[3683.62 --> 3683.84]  Yeah.
[3684.50 --> 3685.88]  Been very easy to do that.
[3685.88 --> 3691.50]  And I think it's important probably, Jared, for you to talk about some of the stuff you're doing with the WAV file.
[3691.60 --> 3692.92]  Can I interview you a little bit?
[3693.06 --> 3693.34]  Sure.
[3693.58 --> 3694.40]  On this process?
[3694.50 --> 3698.88]  I feel like maybe they might get more mileage on an interview version versus a Monolo version of it.
[3699.06 --> 3699.46]  Absolutely.
[3700.06 --> 3701.68]  So I know what we do.
[3701.82 --> 3703.68]  We mix down a WAV file.
[3704.18 --> 3704.50]  Right.
[3704.50 --> 3714.66]  And then we mix down through a process called match loudness to get to the MP3 because there's some things that happen in this match loudness process that make it broadcast worthy.
[3714.66 --> 3723.30]  It kind of pulls levels up inside the MP3 file to make it, you know, the levels normalized and stuff like that for production audio out in the world.
[3723.62 --> 3726.68]  And so the WAV file has chapters in it.
[3726.74 --> 3728.60]  It's larger than the MP3.
[3728.88 --> 3735.74]  We then drag that WAV file into match loudness and push go essentially or run, I think is the word, for the process.
[3735.74 --> 3742.28]  And then a minute or two later, depending upon the machine you're using it on, out comes this MP3, right?
[3742.84 --> 3743.04]  Right.
[3743.16 --> 3749.08]  And so we upload the MP3 into our CMS, our website, our application.
[3749.08 --> 3753.88]  And then before that, though, we also sort of drag and drop this WAV file.
[3753.96 --> 3759.48]  Can you talk about what you do to introspect that WAV file to pull out the chapters, to pull it into the CMS?
[3760.08 --> 3770.76]  And then some things that happen with the MP3 when it comes to like date changes or title changes or slug changes, how those things permeate into the final CDN that actually goes out to the world.
[3770.76 --> 3771.48]  Right.
[3771.48 --> 3771.64]  Right.
[3772.30 --> 3777.52]  So there's really two sources of truth for any piece of information about an episode.
[3778.04 --> 3785.70]  And those two sources are the RSS feed or feeds in our case in which the episode lives.
[3786.46 --> 3790.74]  And then the ID3 tags inside of the MP3, the final artifact.
[3791.48 --> 3796.56]  And those two sources of truth should be synchronized and match.
[3796.56 --> 3807.22]  And so the obvious place to do that work is in our admin because our admin is where we author a lot of that information, including the title, the date published, the duration.
[3807.84 --> 3809.10]  We pull that out of the MP3.
[3809.18 --> 3812.74]  But all the information is stored in our CMS.
[3813.48 --> 3825.28]  And so the way that the chaptering works and really the way that all metadata works is every time you save that episode in our admin, it's taking the result of the episode information that's in our database.
[3825.28 --> 3830.20]  It's rewriting a brand new MP3 that has that exact same match data.
[3830.34 --> 3831.04]  So it's always the same.
[3831.74 --> 3839.88]  The MP3 does not contain the chapter information until our admin contains the chapter information for that same reason.
[3840.22 --> 3844.62]  The chapters need to be outside of the MP3 because they also have to be in the RSS feed.
[3845.42 --> 3846.78]  We also use them on the website.
[3847.26 --> 3848.54]  We use them in multiple places.
[3848.82 --> 3850.78]  And so the data has to be outside of that MP3.
[3851.66 --> 3853.80]  And so the way that we get that is out of the WAV file.
[3853.80 --> 3856.62]  So the MP3 gets uploaded into our admin.
[3856.76 --> 3858.22]  The WAV file is huge in comparison.
[3858.68 --> 3860.72]  MP3s range from 50 megs.
[3860.94 --> 3863.22]  Well, changelog news is like 7 megabytes.
[3863.98 --> 3869.78]  You know, anywhere from 10 megabytes to 100 megabytes, sometimes bigger for Adam's epic interviews.
[3870.56 --> 3873.82]  But the WAV files are, that's raw audio, uncompressed.
[3873.92 --> 3875.92]  And so we're talking gigabytes, right?
[3876.46 --> 3879.50]  So we don't actually want to upload the WAV file to our admin.
[3879.74 --> 3881.44]  We just want the information out of it.
[3881.44 --> 3887.56]  And so every episode post-audition has four artifacts.
[3888.40 --> 3890.24]  Two WAV files, two MP3 files.
[3890.52 --> 3892.18]  One for regular changelog people.
[3892.64 --> 3895.20]  And then the it's better folks get their own file.
[3895.62 --> 3896.02]  It's better.
[3896.52 --> 3897.10]  That's right.
[3897.42 --> 3898.20]  For plus plus.
[3898.20 --> 3904.40]  When you drag the WAV file into our admin, it's just dropping it into the local browser session.
[3904.52 --> 3905.72]  It's not uploading it to the server.
[3906.54 --> 3913.38]  And the browser via our good friend JavaScript uses, I can't remember what library we're using,
[3913.66 --> 3914.80]  wave.js or something.
[3914.80 --> 3920.92]  Something somebody else wrote to basically introspect the WAV file, which can get at the markers,
[3921.50 --> 3928.18]  pull them out, match the timestamps, and basically create for us a bunch of chapter objects in the form.
[3928.80 --> 3929.62]  And that's how that works.
[3930.44 --> 3931.68]  So the WAV file is then discarded.
[3931.80 --> 3934.16]  When you hit save, the WAV file is not going anywhere.
[3934.36 --> 3935.16]  It just disappears.
[3935.76 --> 3938.48]  MP3 gets uploaded along with the chapter information.
[3938.48 --> 3946.10]  Yeah, the chapter information can live in the admin episode before the MP3 does.
[3946.96 --> 3947.04]  Yep.
[3947.14 --> 3947.28]  Right?
[3947.34 --> 3949.18]  Because it's its own data set, basically.
[3949.84 --> 3951.54]  Which informs the RSS feed.
[3951.54 --> 3951.76]  That's right.
[3951.86 --> 3956.78]  And you can go back and edit it later, and it will reflect into the MP3 and into the RSS feeds.
[3957.54 --> 3960.56]  And so that's why I want that to be the source of truth versus the WAV file.
[3961.06 --> 3964.14]  The WAV file is kind of like a starter for your chapters, basically.
[3964.94 --> 3965.10]  Right.
[3965.30 --> 3968.10]  It's the, starter's a good word, I suppose.
[3968.48 --> 3969.86]  Try and go with a different word.
[3970.38 --> 3971.10]  The kindling.
[3971.22 --> 3973.38]  The initial vehicle to get it there, I don't know.
[3973.48 --> 3974.26]  The transport layer.
[3974.36 --> 3976.86]  Yeah, it's just like the baseline data set.
[3976.90 --> 3979.72]  It's actually the conduit between Audition and web.
[3980.48 --> 3980.74]  Yeah.
[3980.86 --> 3981.04]  Right?
[3981.16 --> 3982.50]  And you can completely ignore it.
[3982.58 --> 3989.98]  Like, you could author all your chapters by hand in our admin by hitting add chapter, start time, end time.
[3990.36 --> 3991.06]  You know, you could do that.
[3991.16 --> 3991.44]  Yes.
[3991.44 --> 3991.94]  If you're a fool.
[3991.94 --> 3993.26]  But we're not fools.
[3993.54 --> 3993.68]  Nah.
[3993.68 --> 3993.72]  Yeah.
[3994.46 --> 4003.84]  And so the cool thing, too, is once the, you know, to kind of go technically a couple layers into the details, the WAV file does not get uploaded, as you mentioned.
[4003.98 --> 4004.24]  Right.
[4004.24 --> 4008.24]  It infers and informs the admin of all the chapter data.
[4008.24 --> 4021.88]  And the cool thing I think of is afterwards, if there's a typo, which I will go and save and then preview the webpage, because sometimes in Audition it's not easy to see all those typos because the interface of Audition has small type.
[4022.28 --> 4025.30]  And I'm in my 40s, as you've alluded to, you being in your 40s.
[4025.56 --> 4025.78]  Yes.
[4025.84 --> 4027.08]  It's not that my vision is bad.
[4027.14 --> 4028.20]  It's just, you know, it's small.
[4028.20 --> 4034.84]  And so I'll see things differently when previewing it as the, you know, future episode page of this episode, for example.
[4035.56 --> 4038.90]  And I'll notice that I fat fingered something or whatever may have happened.
[4038.90 --> 4043.92]  And I will change it in the admin versus having to re-upload a new WAV file.
[4043.92 --> 4063.20]  Now that does mean that the WAV file is no longer the source of truth, which is obvious because it's not meant to be, but the change happens in the web, not in the MP3, or sorry, the WAV file, which can take minutes, sometimes 15 minutes if you're on a non-Apple Silicon Mac.
[4063.54 --> 4064.32]  Yeah, too long.
[4064.40 --> 4071.38]  Like I've learned, you know, it could take, you know, 10 minutes sometimes to mix down from the session into the WAV file.
[4071.74 --> 4072.06]  Yes.
[4072.06 --> 4075.28]  And so that could be too long, like running tests, just too long.
[4075.42 --> 4075.82]  Forget it.
[4075.92 --> 4076.14]  Right.
[4076.32 --> 4077.04]  Just do it in the browser.
[4077.16 --> 4080.74]  And sometimes you'll catch a typo on an episode that you're listening to a week and a half later.
[4081.30 --> 4082.76]  Maybe Adam mastered it.
[4082.82 --> 4084.24]  So it's not even on my machine.
[4084.42 --> 4085.84]  Like Dropbox hasn't synced it.
[4086.22 --> 4090.10]  I don't want to go sync his session down, remix it down, et cetera.
[4090.20 --> 4093.92]  So I just go into our admin, make the change, and we're good to go.
[4094.02 --> 4094.72]  So that's really cool.
[4094.72 --> 4099.00]  All of the MP3 chaptering abilities.
[4099.00 --> 4116.82]  Let's shout out to our friend, Losh Vickman, who we hired a couple years ago to write a Elixir library, which allows us to write ID3 v2.3 tags, which we couldn't previously do with our FFmpeg-based solution, which is why we didn't do chapters.
[4116.82 --> 4122.14]  As quickly as we wanted to, all of that you can find in old episodes.
[4122.76 --> 4124.56]  There's a Kaizen with Losh.
[4124.64 --> 4140.92]  There's also an episode that I thought was really fun called A Guided Tour Through ID3 Esoterica, where we talk about all the cool stuff Losh learned along the way as he wrote that library, which we now maintain, although it's had very few changes because it works pretty much as advertised.
[4140.92 --> 4144.70]  Over the years, it allows us to embed images and links as well.
[4144.84 --> 4145.38]  Super cool.
[4146.50 --> 4150.88]  And, you know, not to flex or anything, but I feel like we have the best chaptering game in the biz.
[4152.14 --> 4153.30]  That is a flex, isn't it?
[4153.32 --> 4154.26]  Flex as you'd like.
[4154.56 --> 4156.62]  I concur, and I agree.
[4156.92 --> 4158.12]  Our chapters are pretty on point.
[4159.32 --> 4161.40]  I'm such a chapter snob now, man, really.
[4161.40 --> 4176.94]  I feel like anybody who's an avid podcast listener listening to podcasts that don't have chapters or haven't appreciated or come to appreciate chapters in podcasts are missing out so deeply.
[4177.76 --> 4186.54]  And maybe it's just because, you know, we're professionals and we quality assurance our stuff that I want to jump around more than the other listeners.
[4186.54 --> 4190.86]  Because, like, there's a lot of listeners, like, I don't jump around the podcast, so I have no need to.
[4190.86 --> 4193.62]  They listen straight through, and then they move on to their next episode and some other show.
[4193.74 --> 4196.58]  Yeah, but I'm like, nah, I kind of want to just jump to that one spot.
[4197.22 --> 4201.20]  Especially when the chapters are so well-named, you know, so much care and love put into it.
[4201.20 --> 4205.70]  Well, for me, that's the fun part is we get to inject a lot of fun, you know.
[4205.86 --> 4216.30]  Really, I wouldn't call them Easter eggs, but, like, the fun is in the chapter names and sometimes the chapter metadata that, like, I know seven people are going to notice or less.
[4216.90 --> 4221.70]  But someone's going to notice and get a giggle, hopefully, or even just roll their eyes.
[4222.98 --> 4233.90]  But, yeah, chaptering is something that we really take seriously and put a lot into and, I guess, don't care so much that a lot of people get a lot out of it.
[4233.90 --> 4234.88]  We'd love more people to.
[4235.72 --> 4241.52]  But it's kind of like that thing with Steve Jobs and Johnny Ives where they were designing the inside of a thing or the back.
[4242.30 --> 4245.90]  And they didn't care if nobody else saw how cool it looked on the inside because they knew.
[4246.02 --> 4247.10]  They knew how cool it looked.
[4247.92 --> 4248.90]  So that's how we do chapters.
[4249.04 --> 4251.48]  It's probably the most technical and interesting part of our flow.
[4252.30 --> 4255.06]  Everything else is relatively bog standard.
[4255.06 --> 4256.06]  Yes.
[4257.06 --> 4259.84]  I think the chaptering is the bee's knees, man.
[4260.18 --> 4260.88]  It's the cat's pajamas.
[4261.76 --> 4262.72]  It's the good stuff.
[4263.32 --> 4267.32]  And I think our workflow affords us the ability to do that with such care.
[4267.32 --> 4280.08]  Because going back to when we marker, taking the time in that post-production process took a bit to get used to because it is a time slot.
[4280.22 --> 4281.24]  You've got to dedicate to it.
[4282.10 --> 4284.06]  You may dedicate more.
[4284.26 --> 4285.38]  I may dedicate less.
[4285.90 --> 4287.42]  You may dedicate less.
[4287.50 --> 4288.28]  I may dedicate more.
[4288.32 --> 4288.70]  Who knows?
[4288.70 --> 4298.28]  But doing that pass is the final, I would just say, chef's kiss moment, opportunity on a show.
[4298.42 --> 4302.02]  And maybe we take it too seriously and others take it less seriously.
[4302.18 --> 4306.22]  Like you just mentioned with Steve and Waz designing the inside of this thing that nobody gets to see.
[4306.28 --> 4307.24]  But they know how cool it looks.
[4308.02 --> 4310.30]  I feel like that's the cool stuff for us.
[4310.30 --> 4315.46]  There was a couple chapters I can't get to them that I can think of.
[4316.00 --> 4316.46]  I don't know.
[4316.56 --> 4319.70]  I was going to bring out one from a recent show.
[4319.82 --> 4322.64]  But it's so contextually adjacent from this conversation.
[4322.76 --> 4323.70]  It won't really translate well.
[4323.96 --> 4333.80]  But if you go, dear listener, and you go through even like Lady Bird, like that episode, episode 604, has 42 chapters.
[4334.86 --> 4335.24]  That's a lot.
[4335.44 --> 4338.06]  And the final chapter, 42 is an awesome number two, by the way.
[4338.16 --> 4338.64]  That's true.
[4338.64 --> 4342.64]  The final chapter is Cozy Lo-Fi from Caitlin Colt.
[4343.76 --> 4350.70]  Because Andreas' wife produces lo-fi music that you probably could listen to when you're coding on YouTube.
[4351.14 --> 4351.82]  Good stuff, too.
[4351.86 --> 4352.64]  I've been listening to it.
[4352.72 --> 4353.00]  Have you?
[4353.72 --> 4354.72]  And that was his plug.
[4354.82 --> 4358.92]  And so we decided to put, I think it's actually called Cozy Lo-Fi is the name of that track.
[4359.54 --> 4361.84]  And so we put that in there as its own chapter dedicated.
[4362.00 --> 4364.86]  You can just jump to that chapter right now and listen to it.
[4365.48 --> 4366.48]  To me, that's the cool stuff.
[4366.48 --> 4369.22]  It's the details in podcasting that really.
[4370.14 --> 4376.18]  And I would just say, Marco, if you're listening, I love your software for the most part.
[4376.26 --> 4380.12]  But this latest update to Overcast, I am not super happy with it.
[4380.60 --> 4383.76]  I want to take this moment to tell you that chapters are so cool.
[4384.16 --> 4387.26]  And the way chapters work now is not so cool in Overcast.
[4387.26 --> 4393.46]  I liked it so much better when I clicked on a chapter, the page didn't go away.
[4394.24 --> 4398.70]  And now you have to go back to it again and find where you were at before you can use it as a jumper.
[4399.80 --> 4402.54]  Like a table of contents that did not move when you moved around.
[4403.04 --> 4405.80]  The audio would move because it's audio.
[4405.80 --> 4408.86]  But the interface did not hide.
[4409.62 --> 4412.04]  The chapters are a leaf page that pop up.
[4412.60 --> 4414.42]  And as soon as you click on one, it goes away.
[4414.84 --> 4418.96]  And then when you click on it again, it doesn't even take you to where you're at in the chapter list.
[4419.30 --> 4420.28]  It takes you to the top.
[4420.78 --> 4423.02]  And so you got to scroll, scroll, scroll to where you're trying to be at.
[4423.46 --> 4427.76]  And so the experience of chapters has drastically changed, in my opinion.
[4428.10 --> 4429.06]  And I'm super sad.
[4429.26 --> 4429.86]  Please change it, Marco.
[4430.50 --> 4431.20]  If you're listening.
[4431.20 --> 4434.20]  A plea from one particular user.
[4435.12 --> 4439.68]  And if not, we'll just chapter this in the audio and link directly to this chapter and send it to you.
[4440.08 --> 4440.84]  There you go.
[4441.46 --> 4448.18]  So one quick chaptering story before we move on as we're just stuck on chapters.
[4448.36 --> 4449.74]  This chapter will never end.
[4450.54 --> 4454.98]  A recent JS Party episode is called a Nick Level Emergency.
[4455.60 --> 4460.62]  So Nick Neesey, whom you may know from JS Party and also from ChangeLog and Friends.
[4460.62 --> 4462.64]  And other ChangeLog-y goodness.
[4463.64 --> 4465.08]  Is a big TypeScript fan.
[4465.54 --> 4471.52]  And the Node.js people recently added some TypeScript-related features.
[4472.02 --> 4474.28]  And Nick wanted to have an emergency pod about it.
[4474.36 --> 4475.68]  It was not worthy of an emergency.
[4475.94 --> 4477.92]  And so we did it anyways.
[4478.14 --> 4479.40]  We made fun of him along the way.
[4479.48 --> 4481.78]  And we call it a Nick Level Emergency.
[4482.02 --> 4484.68]  That's JS Party number 333.
[4485.36 --> 4488.14]  Which is a fun ride of itself.
[4488.14 --> 4489.94]  But then I got this idea for the chapters.
[4490.66 --> 4495.60]  Since this whole thing was Nick's emergency, I'm going to have him referenced in every single chapter.
[4496.50 --> 4498.34]  And so there's 22 chapters on that episode.
[4498.56 --> 4502.26]  And if you go read them, every single chapter has the word Nick in it somewhere.
[4502.96 --> 4503.44]  Chapter 3.
[4503.58 --> 4505.42]  Node adds TypeScript stripping for Nick.
[4505.72 --> 4506.24]  Chapter 4.
[4506.42 --> 4507.56]  Nick would absolutely love this.
[4507.78 --> 4508.40]  Chapter 5.
[4509.18 --> 4510.56]  Nick, I'd rather be TypeScripting.
[4511.06 --> 4511.66]  You get the point.
[4511.66 --> 4514.58]  That's the kind of nerdery I'm talking about.
[4515.32 --> 4515.98]  Why not, right?
[4516.30 --> 4516.94]  Have some fun.
[4517.84 --> 4520.12]  Probably less than seven people realize this.
[4520.58 --> 4521.78]  Less than 7%, huh?
[4521.80 --> 4522.32]  You think so?
[4522.72 --> 4523.36]  Well, how do you know?
[4523.50 --> 4525.02]  How do you know how many people will look at your chapters?
[4525.78 --> 4529.06]  We need to chapter pixel tracking technology ASAP.
[4529.06 --> 4541.88]  Yeah, I do appreciate that level of detail that we can put into it, which I believe the hardest core of hardcore listeners do appreciate.
[4541.88 --> 4549.26]  Just imagine the experience of hearing about us for, you know, the second or third time.
[4549.36 --> 4552.42]  And maybe you're not a full-time listener, but you've been linked up to an episode page.
[4552.44 --> 4555.64]  And you land there, and somebody says, they talked about X.
[4556.26 --> 4557.60]  And pick your variable, right?
[4557.84 --> 4561.26]  They talked about, you know, Nick-level emergencies on this thing.
[4561.28 --> 4564.76]  And he was mentioning his desire for what's new in ECMAScript 24.
[4565.46 --> 4567.04]  You can jump right to that chapter.
[4567.04 --> 4576.28]  And that chapter is also a linked chapter that goes out to an entire article on the new stack about it.
[4576.42 --> 4581.16]  Because that's probably what Nick did in show notes was like, hey, this is what my reference point is.
[4582.14 --> 4587.60]  So, you can go right to minute 18 and 26 seconds and listen to what's new.
[4587.70 --> 4591.50]  So, when they come there, they kind of get this version of instant gratification.
[4591.50 --> 4599.78]  Whereas podcasts generally require you to dedicate, in this case, 51 minutes potentially to hunt for the goodness.
[4600.54 --> 4602.06]  Chapters point you directly there.
[4602.44 --> 4605.70]  Now, I mentioned initially, chapter snob, that's me.
[4606.52 --> 4614.14]  Even on YouTube, like if I'm listening, if I'm watching anything on YouTube, like a recipe, you know, I've been like all in this chef stuff, you know.
[4614.14 --> 4623.14]  If I find a video that's like next level chicken parmesan and I want to like examine their recipe, I don't need to know.
[4623.58 --> 4633.10]  Like if I've experienced, I could, chapters let me bypass the things that are not for me versus having to listen to the whole thing or watch the whole thing or whatever it might be.
[4633.10 --> 4641.26]  Like if you are on YouTube or you're podcasting like we are and you're not chaptering and you have anything that's more than five minutes, sad, man.
[4641.58 --> 4642.78]  Like I would just bail on it.
[4642.82 --> 4647.98]  Like I'm just not going to like give your content time because you have not respected my time.
[4648.62 --> 4650.66]  So, here's a feature for YouTube I've been thinking about.
[4651.18 --> 4656.94]  Because we do now allow YouTube to slurp in our audio episodes.
[4656.94 --> 4668.28]  And you can subscribe to JS Party, GoTime, what have you on YouTube via the playlist at youtube.com slash changelog.
[4668.28 --> 4673.92]  And so this is YouTube's official way of adding audio podcasts as a feature to their platform.
[4675.04 --> 4677.56]  And they rehost like Spotify does.
[4678.04 --> 4684.62]  But they do not respect chapters in your feed or in your MP3 or anything like that.
[4684.62 --> 4693.50]  And so we do not have chapters on YouTube whereas we did go out of our way and implement Spotify's specific requirements for chapters on their platform.
[4693.88 --> 4695.50]  We do not have them on YouTube.
[4695.94 --> 4707.92]  What I'm thinking about doing is creating a second feed for every one of our podcast propers that includes the chapters as timestamps in the show notes.
[4708.32 --> 4710.98]  Which is how YouTube works as a creator.
[4710.98 --> 4714.32]  The way you add chapters in YouTube is super lame and manual.
[4714.62 --> 4723.96]  It's probably actually a good solution for non-technical people because you basically just put a section of your description, a list of timestamps with a title.
[4724.44 --> 4726.62]  And it will turn those into the chapters inside YouTube.
[4726.72 --> 4727.74]  That's how it officially works.
[4727.82 --> 4731.36]  There's no chaptering functionality in their YouTube studio.
[4732.06 --> 4734.38]  You just put it in the description and it turns those into chapters.
[4734.38 --> 4742.78]  And so I might start writing for every one of our podcasts a second feed file that's just for YouTube and point YouTube at that one.
[4742.86 --> 4748.54]  And everything is going to be completely identical except where we put the chapters in the show notes as timestamps.
[4749.10 --> 4751.02]  And that would give us chapters on YouTube.
[4751.44 --> 4756.32]  I don't want to do that in our feeds generally because it bloats them quite a bit.
[4756.32 --> 4762.58]  And our feeds are already pretty bloated due to being complete episode catalogs versus like the last 100 episodes.
[4763.02 --> 4764.74]  So our feed files are already pretty large.
[4765.04 --> 4769.22]  But that's something I've been thinking about doing for YouTube just to get the chapters information out to YouTube.
[4769.52 --> 4772.98]  However, there's just not that many people listening on YouTube yet.
[4773.44 --> 4776.02]  Or maybe ever because we're non-video podcast.
[4776.40 --> 4777.16]  A good episode.
[4777.16 --> 4782.20]  I think most recent ChangeLog News outperformed and it was only a couple days ago.
[4782.28 --> 4784.56]  500 people listen to that on YouTube.
[4785.46 --> 4788.40]  Typically we get 100-ish per episode over there.
[4789.24 --> 4792.44]  But I think having chapters over there would be appreciated.
[4792.66 --> 4793.46]  So I'm thinking about doing that.
[4793.54 --> 4794.06]  I haven't done it yet.
[4794.46 --> 4795.88]  Now we're basically Kaizen-ing.
[4795.96 --> 4796.70]  So maybe we should stop.
[4798.34 --> 4800.46]  Well, there's a little Kaizen in all the conversations.
[4800.68 --> 4803.62]  You know, you're always, part of Kaizen is always be improving.
[4803.72 --> 4804.88]  That's always, you know.
[4805.34 --> 4805.80]  That's right.
[4806.12 --> 4807.08]  Improve without ceasing.
[4807.82 --> 4808.38]  All right.
[4808.40 --> 4808.96]  What's left?
[4809.30 --> 4818.20]  I would say what is left is just to thank everyone who is paying attention to this enough to care about this last how we produce podcast section.
[4818.96 --> 4819.84]  Maybe you don't care.
[4820.02 --> 4820.56]  Maybe you do care.
[4820.62 --> 4823.58]  Maybe you care about how we, maybe you got some ideas.
[4823.70 --> 4825.44]  Maybe you're like, man, have you tried this?
[4825.54 --> 4827.00]  Or I like that workflow, but what about that?
[4827.60 --> 4829.92]  Our stack is open source.
[4830.34 --> 4831.92]  And I would say open to contributions.
[4833.08 --> 4836.30]  There is a Zulu for that, so, or a Slack for that potentially.
[4837.16 --> 4839.66]  Where maybe you can hop in there into a dev channel.
[4839.92 --> 4843.46]  And if you've got some ideas, you know, obviously it's open source.
[4843.54 --> 4844.50]  You can fork it and do what you want.
[4844.58 --> 4845.80]  But, you know, you can contribute.
[4845.94 --> 4847.92]  You can leverage the code base to learn.
[4847.92 --> 4856.18]  I was going to ask you some questions about the RSS feed because I think over the years you've iterated to, like, what I would probably say is potentially the best RSS feed alive.
[4856.18 --> 4856.84]  Mm-hmm.
[4857.00 --> 4865.98]  Like, with all the necessary features, like, you're really good at being on the tip of the RSS feature list where what should be and could be supported is supported.
[4866.52 --> 4866.88]  Mm-hmm.
[4866.88 --> 4872.50]  You know, almost, I wouldn't say instantaneously, but pretty close to instant whenever it makes sense.
[4873.22 --> 4875.38]  And so I think RSS feeds are pretty solid.
[4875.64 --> 4885.36]  So much so that I actually pulled down the master feed and I have it opened up in Zed just to look at a raw RSS feed from the master feed, which is just humongous.
[4885.50 --> 4885.74]  Mm-hmm.
[4885.74 --> 4886.08]  It's like...
[4886.08 --> 4887.40]  It's like 12 megs.
[4887.82 --> 4888.56]  I'll tell you.
[4888.62 --> 4889.30]  I curled it down.
[4889.66 --> 4891.68]  It is 11.7 megs.
[4891.86 --> 4892.52]  Oh, I drilled it.
[4892.94 --> 4896.54]  And it took me three seconds to curl it down.
[4897.00 --> 4898.98]  That's a pretty long time for an XML file.
[4899.12 --> 4899.60]  I mean, that's...
[4899.60 --> 4900.16]  12 megabytes.
[4900.18 --> 4901.12]  It should be almost instant, right?
[4901.42 --> 4902.28]  Not for 12 megs.
[4902.66 --> 4904.38]  Eh, I suppose.
[4904.56 --> 4907.32]  I mean, an XML file is not usually that big, though.
[4907.32 --> 4908.92]  That's a pretty big XML file.
[4909.62 --> 4909.94]  It is.
[4910.06 --> 4912.34]  It's got over 1,000 episodes in there.
[4912.46 --> 4912.68]  Yeah.
[4913.26 --> 4913.56]  Yeah.
[4913.72 --> 4914.82]  But it's got a lot of cool stuff in there.
[4914.94 --> 4917.58]  So all that to say is our code base is open source.
[4917.58 --> 4920.90]  If you're curious on how these things are implemented, look at that.
[4921.00 --> 4925.28]  Obviously, we are still in the process of potentially fully adopting Zulip.
[4925.38 --> 4928.44]  So there may be a place for you to have a conversation if you want to contribute.
[4928.62 --> 4931.42]  So you can hop in there and share some of your ideas, of course.
[4932.04 --> 4934.90]  Or just fork and do and PR away.
[4935.10 --> 4935.58]  There you go.
[4936.50 --> 4944.00]  But yeah, it's been fun to talk about self-hosting and the non-cool, cool rug pulls that are reversed and stuff.
[4944.68 --> 4944.96]  Mm-hmm.
[4945.20 --> 4946.18]  I'm excited about that stuff.
[4946.18 --> 4947.24]  All right.
[4947.30 --> 4948.40]  That's all we got for this week.
[4948.74 --> 4949.94]  Thanks for hanging out with us.
[4950.60 --> 4953.06]  Coming soon to a friends near you, Kaizen.
[4953.98 --> 4959.98]  Coming soon to a friends near you, Natalie Pissinovich talking AI code editors.
[4960.82 --> 4964.34]  Coming soon to the changelog, Elasticsearch.
[4964.98 --> 4966.46]  What else is coming soon on the changelog?
[4967.54 --> 4974.56]  Oh, coming soon on the changelog, Jimmy Miller talking about the best, worst code base.
[4974.56 --> 4976.92]  That should be good.
[4977.52 --> 4978.06]  Yeah, yeah, yeah.
[4978.42 --> 4979.18]  Looking forward to that one.
[4979.28 --> 4981.02]  So stay tuned right here.
[4981.70 --> 4989.46]  And if you're a nerd and you like pretty things, go curl down our RSS files and just appreciate that formatting.
[4989.70 --> 4992.60]  Because, you know, it's a lot of hard work putting in those suckers.
[4992.68 --> 4993.78]  And nobody reads them but computers.
[4994.50 --> 4994.80]  Yeah.
[4994.80 --> 4994.88]  Yeah.
[4995.06 --> 4996.28]  Chapter data is in there.
[4996.72 --> 4997.58]  All the stuff.
[4997.74 --> 4999.30]  It's a lot of stuff in there.
[5000.72 --> 5001.50]  Very cool.
[5001.74 --> 5003.68]  It is hard to appreciate that stuff.
[5004.50 --> 5012.68]  And I would say one more back in your list, because this came out after that, is ergonomic keyboards from ZSA.
[5013.18 --> 5013.86]  Cool stuff.
[5013.94 --> 5014.28]  That's right.
[5014.82 --> 5015.48]  Scroll up.
[5015.70 --> 5016.12]  Hit play.
[5016.26 --> 5016.70]  That's right.
[5017.44 --> 5017.98]  Or down.
[5018.36 --> 5019.12]  Depending upon where it is.
[5019.12 --> 5023.32]  I'm looking forward to that episode, although I'm looking back at it as we publish.
[5023.44 --> 5023.78]  Yes.
[5024.48 --> 5028.58]  The time travel of out-of-sync podcast recordings.
[5028.68 --> 5028.96]  All right.
[5029.02 --> 5030.44]  Let's call it a show.
[5031.18 --> 5032.10]  See you all in the next one.
[5032.18 --> 5032.64]  Bye, friends.
[5032.84 --> 5033.36]  Bye, friends.
[5033.36 --> 5063.34]  Bye, friends.
[5063.36 --> 5064.28]  ChangeLog.com.
[5064.42 --> 5066.72]  And we'll mail the goods directly to your front door.
[5067.10 --> 5067.50]  Mmm.
[5068.38 --> 5069.32]  That sounds good.
[5069.68 --> 5070.32]  I'll have that.
[5070.58 --> 5072.08]  Thanks again to our sponsors.
[5072.40 --> 5072.88]  Sentry.
[5073.24 --> 5073.88]  Paragon.
[5074.40 --> 5075.22]  Coder.com.
[5075.46 --> 5076.08]  And Test Double.
[5076.48 --> 5079.76]  And of course, to our longtime partners at Fly.io.
[5080.06 --> 5082.20]  To our beat-freaking residents, The Goat.
[5082.52 --> 5083.38]  Breakmaster Cylinder.
[5083.72 --> 5084.18]  Yeah.
[5084.96 --> 5085.72]  Music's good.
[5086.12 --> 5087.02]  And to you for listening.
[5087.30 --> 5089.98]  We appreciate you spending time with us each week.
[5090.32 --> 5092.32]  Next week on The ChangeLog.
[5092.32 --> 5093.60]  News on Monday.
[5094.00 --> 5098.12]  Jimmy Miller tells us about his best, worst code base on Wednesday.
[5098.66 --> 5102.36]  And Gerhard Lazu joins us for Kaizen 16 on Friday.
[5102.96 --> 5104.04]  Have a great weekend.
[5104.40 --> 5107.14]  Leave us a five-star review if you want some stickers.
[5107.72 --> 5109.48]  And let's talk again real soon.
[5109.48 --> 5120.64]  So, Gerhard, is there anything else we could talk about with this RSS feed?
[5120.92 --> 5122.78]  It's, let me count the lines.
[5123.44 --> 5124.18]  Let me count the ways.
[5124.18 --> 5131.06]  88,724 lines is the length of the LOCs on this file.
[5131.18 --> 5131.36]  Yeah.
[5131.48 --> 5135.88]  Well, that's our entire episode history in a single file.
[5136.34 --> 5137.72]  So, that's kind of interesting to think about.
[5138.40 --> 5141.20]  That is the change log in a nutshell.
[5141.62 --> 5142.50]  Literally is.
[5142.68 --> 5143.06]  It is.
[5143.26 --> 5144.86]  Everything that we've done is in there.
[5144.86 --> 5149.72]  It's better.
