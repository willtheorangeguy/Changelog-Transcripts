[0.00 --> 16.90]  This is ChangeLog and Friends,
[17.36 --> 20.96]  our weekly talk show about text-based user interfaces,
[21.58 --> 22.74]  a.k.a. Tuis.
[23.22 --> 27.02]  A massive thank you to our friends and partners at fly.io.
[27.38 --> 28.96]  Deploy your app near your users.
[28.96 --> 30.26]  That's what the cool kids do.
[30.36 --> 33.08]  Make it happen at fly.io.
[33.42 --> 36.06]  Okay, let's talk about Tuis.
[38.08 --> 39.02]  What's up, friends?
[39.06 --> 41.58]  I'm here with Dave Rosenthal, CTO of Sentry.
[41.98 --> 43.00]  So Dave, when I look at Sentry,
[43.12 --> 46.38]  I see you driving towards full application health,
[46.64 --> 48.12]  error monitoring where things began,
[48.52 --> 51.70]  session replay, being able to replay a view of the interface
[51.70 --> 54.98]  a user had going on when they experienced an issue
[54.98 --> 56.56]  with full tracing, full data,
[56.56 --> 59.76]  the advancements you're making with tracing and profiling,
[60.12 --> 62.74]  Chrome monitoring, co-coverage, user feedback,
[63.12 --> 65.14]  and just tons of integrations.
[65.54 --> 68.26]  Give me a glimpse into the inevitable future.
[68.50 --> 69.32]  What are you driving towards?
[69.76 --> 72.96]  Yeah, one of the things that we're seeing is that in the past,
[73.08 --> 76.30]  people had separate systems where they had like logs on servers,
[76.42 --> 77.10]  written files.
[77.10 --> 81.08]  They were maybe sending some metrics to Datadog or something like that
[81.08 --> 82.06]  or some other system.
[82.40 --> 85.06]  They were monitoring for errors with some product, maybe it was Sentry.
[85.40 --> 89.52]  But more and more what we see is people want all of these sources of telemetry
[89.52 --> 91.50]  logically tied together somehow.
[92.16 --> 95.30]  And that's really what we're pursuing at Sentry now.
[95.42 --> 97.08]  We have this concept of a trace ID,
[97.34 --> 101.48]  which is kind of a key that ties together all of the pieces of data
[101.48 --> 103.20]  that are associated with the user action.
[103.20 --> 107.62]  So if user loads a webpage, we want to tie together all the server requests
[107.62 --> 111.40]  that happened, any errors that happened, any metrics that were collected.
[111.90 --> 113.80]  And what that allows on the backend,
[114.28 --> 116.70]  you don't just have to look at like three different graphs
[116.70 --> 120.24]  and sort of line them up in time and try to draw your own conclusions.
[120.52 --> 124.08]  You can actually like analyze and slice and dice the data and say,
[124.16 --> 127.26]  hey, what did this metric look like for people with this operating system
[127.26 --> 129.90]  versus this metric looked like for people with this operating system
[129.90 --> 131.80]  and actually get into those details.
[131.80 --> 136.84]  So this kind of idea of tying all of the telemetry data together
[136.84 --> 140.50]  using this concept of a trace ID or basically some key,
[140.70 --> 144.58]  I think is a big win for developers trying to diagnose
[144.58 --> 146.48]  and debug real world systems
[146.48 --> 150.28]  and something that is, we're kind of charged the path for that for everybody.
[150.70 --> 152.16]  Okay. Let's see you get there.
[152.34 --> 153.40]  Let's see you get there tomorrow.
[153.66 --> 153.80]  Yeah.
[153.92 --> 154.24]  Perfectly.
[154.48 --> 155.70]  How will systems be different?
[155.94 --> 158.00]  How will teams be different as a result?
[158.00 --> 161.32]  Yeah. I mean, I guess, again, I just keep saying it maybe,
[161.46 --> 164.30]  but I think it kind of goes back to this debuggability experience.
[164.76 --> 166.14]  When you are digging into an issue,
[166.56 --> 169.58]  you know, having a sort of a richer data model that's, you know,
[169.68 --> 171.00]  your logs are structured.
[171.14 --> 173.32]  There's sort of this hierarchical structure with spans.
[173.52 --> 175.62]  And not only is it just the spans that are structured,
[175.74 --> 178.00]  they're tied to errors, they're tied to other things.
[178.00 --> 180.86]  So when you have the data model that's kind of interconnected,
[181.32 --> 184.04]  it opens up all different kinds of analysis
[184.04 --> 187.62]  that were just kind of either very manual before,
[187.86 --> 190.62]  kind of guessing that maybe this log was, you know,
[190.68 --> 192.56]  happened at the same time as this other thing,
[192.72 --> 193.66]  or we're just impossible.
[194.00 --> 196.68]  We get excited not only about the new kinds of issues
[196.68 --> 198.90]  that we can detect with that interconnected data model,
[199.00 --> 201.14]  but also just for every issue that we do detect,
[201.22 --> 202.96]  how easy it is to get to the bottom of it.
[203.30 --> 203.76]  I love it.
[203.84 --> 204.10]  Okay.
[204.10 --> 206.16]  So they mean it when they say code breaks,
[206.40 --> 207.74]  fix it faster with Sentry.
[207.94 --> 211.54]  More than 100,000 growing teams use Sentry to find problems fast.
[211.70 --> 212.68]  And you can too.
[213.16 --> 215.60]  Learn more at Sentry.io.
[215.76 --> 219.50]  That's S-E-N-T-R-Y.io.
[220.12 --> 221.92]  And use our code, changelog.
[222.00 --> 224.16]  Get $100 off the team plan.
[224.44 --> 227.12]  That's almost four months free for you to try out Sentry.
[227.40 --> 229.90]  Once again, Sentry.io.
[234.10 --> 236.94]  So we're hanging out with Nick Jantakis.
[237.14 --> 241.38]  He's flying close to the sun with only 2.5 gigabytes of hard drive space.
[241.54 --> 244.14]  Nick, do you like to live dangerously or what's going on over there?
[244.48 --> 246.08]  Yeah, I must say I do.
[246.38 --> 247.14]  You must.
[248.02 --> 251.08]  I'm over here sitting on like three and a half terabytes, I think,
[251.34 --> 252.52]  of available space.
[252.88 --> 253.80]  So, you know, at this point,
[253.88 --> 256.12]  I've gone all in with this idea of,
[256.20 --> 257.62]  I'm going to keep this workstation alive
[257.62 --> 259.68]  until it no longer wants to be alive.
[259.68 --> 264.22]  So I'm at just under 10 years now with the same like first generation SSD.
[264.86 --> 266.76]  So what's the ultimate size on that?
[266.88 --> 268.54]  Well, the SSD is 250 gigs.
[268.68 --> 270.74]  I do have a one terabyte hard drive as well,
[270.92 --> 271.88]  just like an external one.
[272.10 --> 272.22]  Right.
[272.30 --> 273.82]  But that's also getting pretty full.
[274.20 --> 275.78]  Is this a system you built yourself?
[276.10 --> 278.08]  Yeah, just assorted parts off of,
[278.26 --> 280.20]  well, back then, Newegg and a little bit of Amazon.
[280.66 --> 281.44]  When's back then?
[282.32 --> 284.28]  Back then, like 2014.
[285.42 --> 287.18]  Dang, that's how old this machine is you're on?
[287.74 --> 289.10]  Yeah, I almost can't believe it too,
[289.10 --> 290.20]  because it's like, you know,
[290.44 --> 291.74]  I could buy a new one if I want to,
[291.80 --> 292.68]  just part it out, build it.
[292.72 --> 293.04]  It's fun.
[293.18 --> 293.70]  But it's like,
[294.04 --> 295.52]  it just hasn't become a problem somehow.
[295.68 --> 298.24]  Like I can still record videos and day-to-day usage.
[298.38 --> 298.50]  Yeah.
[298.92 --> 299.58]  What's your CPU?
[300.10 --> 303.38]  It is a quad core 3.2 gigahertz.
[304.08 --> 306.46]  It's like an E4460, I think, an Intel one.
[306.58 --> 307.54]  You're missing out, man.
[307.70 --> 308.36]  Sorry about that.
[308.46 --> 309.42]  Sorry about that.
[309.94 --> 312.58]  Yeah, the last decade has been good in hardware advances, you know?
[312.90 --> 316.64]  Yeah, wait until you hear I have like a GeForce 750 Ti as my video card.
[316.82 --> 317.22]  Oh my goodness.
[317.22 --> 318.96]  That is an interesting one.
[319.66 --> 320.30]  Yeah, I suppose.
[320.70 --> 325.24]  Well, you know, the new Intel CPUs generally have integrated GPUs,
[325.30 --> 327.44]  which is enough in most cases, really.
[328.24 --> 328.38]  Yeah.
[328.50 --> 329.20]  Nick wouldn't know.
[330.76 --> 332.82]  14th gen just sitting out there waiting for you to get it.
[332.88 --> 334.18]  I mean, 14th gen is out there too,
[334.30 --> 337.28]  but riddled with Linux bugs, I'm sure, because it's latest gen.
[337.44 --> 338.58]  I'm excited for you, Nick,
[338.66 --> 342.72]  because A, we might kill that machine here today as we fill up a tar drive,
[342.82 --> 346.00]  but B, you're going to have the best upgrade of all time, aren't you?
[346.00 --> 347.28]  I mean, it's going to be amazing.
[347.48 --> 348.26]  It's going to be a good day.
[348.70 --> 351.70]  That's like how Adam starves himself all day for that one meal.
[352.44 --> 354.10]  But that one meal is the best, isn't it, Adam?
[354.18 --> 355.24]  I mean, you really go after it.
[355.40 --> 358.64]  You know, man, I have to tell you, I've been like becoming a chef.
[358.72 --> 359.04]  Oh, yeah.
[359.28 --> 359.74]  Oh, yeah.
[360.64 --> 361.26]  That's all I'll say.
[361.28 --> 361.70]  I believe it.
[362.30 --> 362.98]  I believe it.
[362.98 --> 367.68]  Nick's going to be a chef when it comes to building a recipe for his next machine.
[368.18 --> 371.52]  Nick, I'm half tempted to donate some RAM to you or something, bro.
[372.12 --> 372.54]  Oh, don't worry.
[372.60 --> 373.60]  I've got 16 gigs.
[374.50 --> 374.74]  Okay.
[374.76 --> 377.50]  Well, you've got plenty of RAM, but does that RAM scale to your next system?
[377.86 --> 380.22]  Like what gen is that RAM even?
[380.74 --> 383.66]  I couldn't even say the exact gen of the RAM, but the answer is no.
[383.66 --> 384.10]  Okay.
[385.12 --> 390.76]  This kind of reminds me of my very first MacBook Pro laptop, which was probably around the same time period.
[391.28 --> 393.22]  Now, it had to be before that, 2010.
[394.26 --> 399.58]  It was one of those big heavy honkers with the really nice keyboard.
[400.58 --> 407.80]  And I had a similar streak going, not how long can I run this thing, but how long could I go without rebooting my laptop?
[408.62 --> 413.54]  At the time, I was traveling into the office to work every day, but I would never turn it off.
[413.54 --> 416.22]  I would just close the lid and open it back up.
[416.28 --> 417.34]  And I called it a server.
[417.90 --> 420.12]  And all my colleagues thought I was a dork, and I was.
[420.96 --> 426.02]  But I went over a year without rebooting that thing, which by the end of it, I mean, it was dogging.
[426.20 --> 427.62]  It was like the RAM, it was swapping.
[427.90 --> 428.74]  The RAM was gone.
[429.28 --> 430.44]  It was like, please reboot me.
[430.54 --> 433.96]  But once I had the streak going, I didn't want to break it.
[434.34 --> 435.46]  Yeah, it's weird how streaks work.
[435.66 --> 438.62]  I had something similar happen with this machine, actually.
[438.98 --> 441.76]  So this machine predates Windows 10, which is I'm running now.
[441.76 --> 443.28]  I used to run Windows 7 on there.
[443.54 --> 447.58]  And at some point in time, security patches stopped, and I wasn't getting auto-updated
[447.58 --> 448.68]  from Microsoft all the time.
[448.96 --> 452.32]  So yeah, I had something like 230 days of uptime, I think, on the machine.
[452.88 --> 454.48]  For a Windows box, it's pretty decent.
[454.56 --> 457.28]  Because usually Windows would be like, by the way, I'm going to reboot on Friday and the
[457.28 --> 457.70]  next Tuesday.
[457.82 --> 458.54]  On Tuesdays.
[458.82 --> 459.58]  Was it Tuesdays?
[459.64 --> 460.68]  It's been so long, I forget.
[460.84 --> 461.82]  Patch Tuesday, isn't it?
[461.84 --> 463.94]  Isn't that the big day on the Windows side?
[464.48 --> 465.20]  I believe so.
[466.34 --> 467.06]  Nick knows.
[467.86 --> 468.10]  Tuesday.
[468.10 --> 469.76]  I got an idea for you, though, Nick.
[470.10 --> 473.20]  You got enough followers and subs on YouTube.
[473.20 --> 478.76]  I think you could probably put a call out there for hardware folks.
[479.58 --> 482.62]  Get Fractal Design to give you a case.
[483.38 --> 485.44]  Get so-and-so to give you a motherboard.
[485.72 --> 488.02]  Get so-and-so to give you some drives.
[488.14 --> 489.68]  I need one brand only, of course.
[489.76 --> 490.12]  I'm sorry.
[490.22 --> 491.30]  I like Fractal Design.
[491.48 --> 491.90]  They're cool.
[492.38 --> 493.42]  So you want me to sell out?
[494.06 --> 495.12]  No, I don't miss.
[495.30 --> 495.50]  No.
[495.62 --> 495.90]  Yes.
[496.02 --> 497.06]  That's not selling out.
[497.44 --> 498.94]  That's leveraging your channel, bro.
[499.08 --> 499.26]  Oh.
[499.62 --> 500.24]  You're missing out.
[500.44 --> 503.32]  There's good content waiting for you to build your next machine.
[503.84 --> 510.16]  All the choices you'll make as a bash scripter, a Vim master, a Docker dude, whatever you want
[510.16 --> 510.74]  to call yourself.
[510.90 --> 516.62]  I'm just looking at all your keywords on your YouTube channel.
[517.30 --> 518.48]  You're missing out, man.
[518.82 --> 519.74]  Build yourself a new machine.
[520.22 --> 520.98]  Use this promotion.
[520.98 --> 522.34]  Get some friends.
[522.60 --> 523.28]  Get some network.
[524.32 --> 524.72]  Boom.
[525.12 --> 525.68]  So here we go.
[526.04 --> 528.96]  YouTube video title, like how to pick the best motherboard to run Docker.
[530.28 --> 530.68]  Yeah.
[530.86 --> 534.74]  I mean, I don't think you really need to choose between motherboards to run Docker, do you?
[535.04 --> 535.20]  No.
[536.24 --> 536.96]  Okay, then.
[537.14 --> 537.34]  Okay.
[537.44 --> 538.88]  Just whatever's on the market.
[539.52 --> 541.10]  Anyways, you should do that.
[541.64 --> 542.18]  It's an idea.
[542.42 --> 543.00]  It's an idea.
[543.44 --> 545.72]  I don't think that's exactly Nick's style of content.
[545.72 --> 550.68]  You're more tutorial, learn a thing, opinion pieces, right?
[550.68 --> 554.32]  I think you're, I've even seen you kind of reading some of your blog posts now on YouTube.
[554.32 --> 556.78]  Is that a recent thing you started doing or you've been doing that in a while?
[557.26 --> 559.72]  You mean linking to the blog post from YouTube?
[559.78 --> 562.06]  No, it's like, here's a blog post and there's also a video.
[562.48 --> 562.94]  Oh, right.
[562.98 --> 566.46]  The video is effectively you either reading or summarizing the blog post.
[566.54 --> 570.94]  I mean, it's almost like a audio transcript in video form and they link back and forth.
[570.94 --> 578.20]  Sometimes it depends, like certain posts I will write out beforehand, but a lot of times I'll just make the YouTube video first and then I'll just do the blog post after.
[578.38 --> 580.02]  But yeah, some of them, it makes sense to write it first.
[580.44 --> 582.98]  Yeah, I've been doing that style, I guess, maybe for like a year and a half, I want to say.
[583.80 --> 592.28]  And I was just figuring like, well, you know, it'd be interesting to see if that increases traffic to both sites, both YouTube and my own site, just by having, you know, a little bit more content in my site.
[592.52 --> 592.76]  Right.
[592.76 --> 595.62]  Have you had any good results from that or are you?
[596.12 --> 597.36]  So it's hard to tell.
[597.86 --> 598.52]  Hard to tell.
[598.88 --> 600.92]  Because I also disabled Google Analytics.
[601.52 --> 603.20]  So whenever they switched over.
[603.38 --> 606.64]  Which I don't blame you about, but how are you going to know?
[607.86 --> 608.32]  I don't know.
[608.90 --> 609.92]  I don't know.
[610.90 --> 611.22]  All right.
[611.22 --> 611.72]  I don't know.
[611.80 --> 612.18]  All right.
[612.60 --> 614.98]  Maybe it's just a feeling, like you'll feel like it's worth it.
[615.28 --> 616.54]  That's how I go on stuff a lot.
[616.60 --> 617.58]  I'm like, this feels right.
[617.98 --> 620.18]  Isn't there a plot hole we're missing out on here, Jared, though?
[620.18 --> 622.80]  Like the last time we talked to Nick, he was changing.
[623.42 --> 623.74]  Right.
[623.80 --> 625.64]  He was like ending the podcast.
[626.22 --> 630.90]  I think even ending the blog and like moving on to something like a gig.
[631.64 --> 631.96]  Isn't that true?
[632.08 --> 632.38]  I don't know, man.
[632.42 --> 634.40]  It's been so long that I don't remember it.
[634.50 --> 634.64]  Yeah.
[635.10 --> 635.30]  Yeah.
[635.34 --> 636.30]  No, you're right about the blog.
[636.46 --> 637.24]  So, or sorry.
[637.52 --> 637.80]  Hold on.
[638.12 --> 641.74]  You're right about the podcast because I was running, running in production.com for a while.
[641.80 --> 641.98]  Right.
[641.98 --> 645.58]  I did a hundred plus episodes and then, yeah, just decided to call it quits on that one.
[645.82 --> 647.86]  But yeah, the blog and the YouTube channel, they're still going strong.
[648.18 --> 648.70]  Weekly posts.
[648.70 --> 650.38]  So you haven't changed at all?
[650.56 --> 651.54]  Since then, no.
[652.12 --> 655.60]  Interestingly, though, I have done a lot of contract work, but one of the people I was
[655.60 --> 659.36]  working with, you know, they did invite me to work full time as like an SRE slash like
[659.36 --> 663.50]  DevOps engineer slash developer advocate slash whatever you want to classify that role as.
[663.76 --> 664.84]  The do all the things person.
[665.16 --> 665.44]  Yes.
[666.82 --> 669.32]  The run things in production person.
[669.46 --> 669.94]  That's right.
[670.48 --> 671.06]  Oh, man.
[671.54 --> 672.22]  And how'd that go?
[672.58 --> 674.22]  Yeah, that's actually going pretty good.
[674.22 --> 678.14]  It's interesting because, you know, it's like a nine to six type of job, but it kind
[678.14 --> 683.12]  of feels like I was working, you know, similar hours doing contract work beforehand anyways.
[683.58 --> 687.22]  And now it's just like consolidated into one company, which has, you know, it's pros and
[687.22 --> 687.72]  cons, right?
[687.76 --> 692.00]  If the company decides to let you off or something happens, you only have one revenue stream.
[692.12 --> 693.60]  But so far, it's a good.
[694.20 --> 696.86]  And you have courses still in play?
[697.06 --> 697.30]  Yeah.
[697.30 --> 698.22]  Still doing courses or no?
[698.52 --> 698.72]  Mm-hmm.
[699.16 --> 699.96]  Keeping those up to date.
[700.14 --> 701.24]  Still need to make some new ones.
[701.52 --> 704.92]  There's been a deploy course in the works now since like 1935, but.
[705.62 --> 706.56]  Older than your computer.
[706.72 --> 710.02]  You might miss out because there's a lot of like non-deployment happening.
[710.34 --> 710.50]  Yeah.
[710.62 --> 711.96]  You know, people ain't shipping.
[712.32 --> 712.42]  No.
[712.60 --> 716.50]  He's slowing down because he can't, you know, he has to slow down to keep up with his computer.
[716.66 --> 717.50]  He just can't go.
[717.64 --> 718.08]  That's right.
[718.22 --> 719.74]  Do you have any pain from that?
[719.80 --> 721.98]  Like, I mean, you're rendering videos, you're doing stuff.
[722.10 --> 723.90]  I mean, do you ever be like, I could wait.
[723.90 --> 728.24]  I remember when we upgraded to the M star, I think ours are M ones.
[729.14 --> 736.44]  My mix down inside of Adobe Audition went from like four minutes to like between 30 seconds and 45 seconds.
[736.56 --> 742.66]  I mean, it was, it was enough where I don't get as distracted now as I did because I mean, you got to waste five minutes waiting for that thing.
[742.82 --> 744.74]  Especially when you mess up, you got to remix down.
[745.08 --> 752.00]  But do you have any of that where you're like, man, I'm just literally watching this thing spin for video takes even longer than audio, obviously.
[752.56 --> 752.64]  Right.
[752.64 --> 754.90]  No, if that were the case, I would upgrade it a long time ago.
[754.98 --> 755.38]  So you're right.
[755.46 --> 755.70]  Definitely.
[755.82 --> 759.60]  Like the video encoding is going to be so much faster on a new machine, probably like a 10 X difference.
[759.94 --> 764.70]  But, you know, let's say I record a 15 minute YouTube video and maybe that takes like 25 minutes to render.
[765.18 --> 766.20]  You know, I like to walk a lot.
[766.46 --> 768.00]  I also sleep and I eat meals and stuff.
[768.04 --> 770.40]  So I'll just like render that video when I know I'm going away for an hour.
[770.48 --> 771.22]  I'll also sleep.
[771.56 --> 771.82]  Yeah.
[772.48 --> 775.88]  During your rendering, your encodings, he takes a nap, you know.
[776.50 --> 776.82]  Right.
[777.02 --> 779.86]  This is the exact reason why people upgrade.
[779.86 --> 784.94]  I spend my whole life as optimized around me doing different things when I need to render a video.
[785.88 --> 786.68]  He has things.
[786.74 --> 787.24]  Am I rendering?
[787.46 --> 788.20]  Okay, cool.
[788.46 --> 789.02]  Time to do it.
[789.04 --> 790.62]  It's like a forced Pomodoro technique.
[790.76 --> 792.02]  You know, he's like, I got 25 minutes.
[792.18 --> 792.66]  I got to go.
[793.00 --> 793.62]  I'm the same, Jared.
[793.72 --> 799.04]  I have the iMac Pro at home as my kind of work home desktop thing that I use.
[799.04 --> 807.68]  I thought I would use a lot more for like, okay, I don't have to go and, you know, somewhere else and basically just do my work.
[807.80 --> 810.98]  I don't have to go and record so I can just like edit this show here.
[811.14 --> 811.24]  Sure.
[811.68 --> 812.18]  Nah, man.
[812.26 --> 815.00]  On that Intel Mac, the mix down was like.
[815.06 --> 815.58]  Too slow.
[815.78 --> 816.48]  15 minutes.
[816.58 --> 817.44]  Like unbearable.
[817.66 --> 818.04]  Right.
[818.60 --> 819.50]  15 minutes.
[820.18 --> 820.90]  No, thank you.
[820.98 --> 825.02]  When I can like spend a minute and a half at most on my M1 Mac.
[825.12 --> 825.54]  Forget it.
[825.54 --> 825.94]  I know.
[826.24 --> 831.06]  Now, this is maybe a controversial take, but this work computer that I have too is separate.
[831.18 --> 834.82]  So the company issued me an M2 Air, which is actually quite nice.
[835.02 --> 836.40]  It's super speedy and it's cool.
[836.48 --> 842.36]  But it's like if I'm just browsing websites or doing like a Docker Compose up, it's really not that much different than my current machine.
[842.76 --> 846.02]  And I really feel like it's just having an SSD on both of them makes such a big difference.
[846.02 --> 847.32]  Like if I didn't have an SSD, forget it.
[847.36 --> 848.26]  It would be like the end of the world.
[848.92 --> 855.22]  You're probably not doing a lot of compression, but I would say your video work is what would really tax the GPU particularly.
[855.22 --> 859.00]  And then probably the CPU as well with some of that at least.
[859.46 --> 859.54]  Yeah.
[859.62 --> 864.06]  It's certainly we're at a point now where common internet usage.
[864.42 --> 865.52]  You got your VIM.
[865.92 --> 866.66]  You got your terminal.
[866.90 --> 867.82]  You got your browser.
[868.30 --> 870.54]  Maybe you've got a music app running.
[871.16 --> 877.14]  You're not really going to have much of a difference on brand new hardware versus, you know, I guess in your case, 10 years ago.
[877.14 --> 887.54]  Although when you did get that put together, it was pretty bleeding edge, it seems like, or at least pretty good versus like an old machine that was also low quality at the time.
[887.94 --> 889.28]  You're not going to notice as much.
[889.34 --> 894.28]  I mean, there's little things where like you tab away and you have to wait for like the window to actually swap those kind of things.
[894.28 --> 900.00]  But really where the gains are is if you're doing heavy loads, compiling test suites.
[900.72 --> 906.40]  Our test suite also runs now again in under 10 seconds, I think.
[906.86 --> 914.78]  Whereas on my old one, it was like getting up to 30 seconds, which of course you run that often enough that you're sitting there staring at it.
[914.78 --> 923.78]  The old SKCD, the obligatory SKCD, I think it's 303 where they excuses that they're compiling, of course, is why they're having a sword fight in the hallway.
[924.12 --> 924.62]  They're sword fighting.
[924.76 --> 924.90]  Yeah.
[925.46 --> 926.68]  So those are the things that you'll notice.
[926.72 --> 929.66]  But yeah, I mean, if you're going to go take a walk, I mean, you've got worker.
[929.76 --> 930.78]  I call that a workaround.
[931.12 --> 932.72]  But, you know, it's a lifestyle workaround.
[932.76 --> 933.58]  So it's the best kind.
[933.66 --> 933.84]  Right.
[934.16 --> 934.30]  Yeah.
[934.32 --> 941.40]  And it's funny, too, because like, let's say I were to release a new course, right, a new video course that has like 75 videos that need to render like those.
[941.40 --> 943.06]  I'll just start that before I go to sleep.
[943.06 --> 945.50]  I do sleep a good seven, eight hours most nights.
[945.58 --> 947.50]  So it's like by the time I wake up, they're all done.
[947.68 --> 948.94]  It's like a gift just waiting there.
[949.00 --> 949.88]  All the all the videos.
[950.00 --> 951.78]  I didn't have to do a single thing like waiting around.
[952.16 --> 957.66]  Does it ever fail in all the night or do you ever like realize you made a mistake and then you're like, oh, I got to go to sleep again.
[958.18 --> 959.08]  Got to sleep again.
[959.48 --> 959.66]  Yeah.
[960.54 --> 961.48]  Go back to sleep.
[961.64 --> 963.26]  You know, I've never had a batch fail like that.
[963.34 --> 969.88]  But I mean, if it did, it is interesting, though, because if it did fail and I was planning to launch like two days from now or something, you know, that would have an effect.
[969.88 --> 973.06]  Like, but yeah, another quick use case just around upgrading.
[973.18 --> 976.16]  I mean, yeah, I would like to play a little bit more modern games.
[976.46 --> 979.32]  So I actually do like playing video games, you know, MMOs, FPS, et cetera.
[979.60 --> 983.38]  And like nothing modern will, you know, within reason is going to run my current machine.
[983.38 --> 986.36]  So I'm stuck to like playing these like 2D platform games.
[986.98 --> 995.78]  Well, I'm in the same world as you because I play all my video games on Nintendo Switch, which is not modern hardware because they refuse to ship modern hardware.
[996.28 --> 997.10]  Nintendo does.
[997.98 --> 1002.94]  And so all the games that look silky smooth on Xbox, they're all glitchy on Switch.
[1003.02 --> 1005.00]  But, you know, it's nostalgic and it's Nintendo.
[1005.22 --> 1006.24]  So I just live with it.
[1006.92 --> 1007.04]  Yeah.
[1007.08 --> 1007.72]  Actually, here's it.
[1007.82 --> 1008.70]  Here's a dilemma for you.
[1008.70 --> 1019.34]  My biggest dilemma around the next upgrade is like, well, do I actually want to go with another workstation that I build up from parts, run Windows with like WSL, et cetera, maybe doable with Linux or something?
[1019.74 --> 1021.84]  Or does one actually go with a laptop?
[1022.38 --> 1024.62]  And then it's kind of like, well, you can do everything from there.
[1024.98 --> 1028.92]  I mean, you know, parts are going to be a little bit worse, but you have the convenience of actually having the laptop.
[1028.92 --> 1035.00]  Because, man, did I run into some issues when, so Docker had this Captain Summit in Lisbon, Portugal last month.
[1035.32 --> 1039.28]  And, you know, I don't have a dedicated laptop, but I have this Chromebook that I modified to run Linux.
[1039.56 --> 1041.24]  That's also like 10 years old, literally.
[1041.52 --> 1042.92]  And like, I can't even run Docker desktop.
[1043.16 --> 1048.68]  And it just became annoying to like sync files from my workstation onto there so I can like post a blog post from, you know, there.
[1049.00 --> 1050.08]  So, yeah, I don't know.
[1050.16 --> 1051.10]  Where do you guys stand on that?
[1051.14 --> 1053.46]  Do you like this idea of like one machine to rule them all?
[1053.56 --> 1055.14]  You do all of your work and fun and all that?
[1055.20 --> 1056.02]  Or do you have separate ones?
[1056.72 --> 1057.36]  Great question.
[1057.36 --> 1059.88]  So, I think Adam and I differ on this to a certain extent.
[1060.04 --> 1060.48]  Go ahead, Adam.
[1060.82 --> 1062.40]  I'm pro laptop, honestly.
[1062.54 --> 1063.22]  Then I'm wrong.
[1063.32 --> 1064.02]  We do not differ.
[1064.92 --> 1066.96]  Well, you've always had a desktop for a long time.
[1067.16 --> 1067.68]  Yeah, I did.
[1067.76 --> 1075.36]  But mainly because the iMac Pro was the latest thing you can buy that was good, I suppose, at that era of Mac.
[1076.02 --> 1076.80]  And it was a desktop.
[1077.36 --> 1077.92]  And that was why.
[1078.74 --> 1079.84]  I wanted a larger screen.
[1080.16 --> 1082.96]  Larger screens were not really a thing for Apple at the time.
[1082.96 --> 1087.68]  I think they still had like the old school display, not even like the newest stuff.
[1088.14 --> 1097.02]  You know, and always any sort of external display with a Mac has, as you know, Jared, been generally fraught with issues throughout the years.
[1097.14 --> 1100.38]  It's gotten better, but it's not like native.
[1100.38 --> 1105.82]  When you have a native screen, the laptop screen or the iMac Pro screen or the iMac screen, it's good.
[1106.46 --> 1108.96]  So, I'm all for a good laptop, honestly.
[1109.14 --> 1109.82]  It goes everywhere.
[1110.42 --> 1113.80]  Just sucks going from screen to laptop because the stuff moves around.
[1113.86 --> 1114.56]  The windows move around.
[1114.78 --> 1115.10]  Oh, yeah.
[1115.28 --> 1116.56]  Unplugging and unplugging.
[1116.76 --> 1116.98]  Yeah.
[1117.34 --> 1117.98]  It's my biggest.
[1118.10 --> 1120.02]  I mean, like how has Apple not solved that yet?
[1120.58 --> 1123.66]  Why is it a third-party tool that works okay?
[1123.80 --> 1124.14]  Right.
[1124.36 --> 1124.84]  Solving it.
[1124.84 --> 1127.00]  So, yeah, I've been pro mobility.
[1127.52 --> 1135.00]  I have had a desktop in the past, but I've always preferred a laptop and that to be one machine to rule them all.
[1135.18 --> 1137.04]  Like, I just get the beefiest laptop I can.
[1137.26 --> 1145.92]  I err on the side of big versus pure mobility because the difference, especially now, between the pros and the errors or whatever is minuscule.
[1145.92 --> 1157.44]  I mean, it used to be more epic as the pros were just like these huge honking bricks that you really didn't want to put on your lap because they would heat your lap to send your leg hair to a point.
[1157.84 --> 1171.32]  But they've gotten so good now that I just don't want to have multiple machines where I have to worry about syncing and installing stuff here, installing it there, and did I do this there or that there, blah, blah, blah, blah.
[1171.32 --> 1176.98]  And I certainly can't do my work only at my work desk.
[1177.30 --> 1179.40]  I just, my lifestyle doesn't afford that.
[1179.70 --> 1181.48]  So, I'm a laptop guy.
[1181.66 --> 1183.42]  Laptops for life, pretty much, at this point.
[1183.92 --> 1184.06]  Okay.
[1184.64 --> 1190.86]  Yeah, I've always been just build my machine up from parts, but maybe that'll change or maybe I'll get two machines.
[1191.04 --> 1191.34]  I don't know.
[1191.58 --> 1193.94]  Maybe a new workstation and a laptop on the side.
[1194.06 --> 1196.08]  Well, you get that YouTube series going.
[1196.22 --> 1198.18]  You might get so much hardware to be coming out of your ears.
[1198.18 --> 1206.18]  You know, funny enough, I have had one opportunity to get hardware, but it was for like one of those, it was like an exercise bike.
[1206.46 --> 1206.74]  Oh.
[1206.86 --> 1209.80]  But like a really fancy one, a crazy one with like a big screen and everything.
[1210.32 --> 1210.54]  And I'm like.
[1210.54 --> 1211.66]  Like a Peloton kind of thing?
[1211.90 --> 1212.54]  Something like that.
[1212.60 --> 1214.08]  But it wasn't, you know, it wasn't that brand.
[1214.20 --> 1214.40]  Sure.
[1214.58 --> 1225.38]  But it felt weird to accept something that large, like physically and like, you know, money wise value to be like, how does that relate to, you know, making a YouTube video on like how to write a shell script, you know?
[1225.38 --> 1227.92]  Like I don't know how much of an audience crossover there is.
[1228.38 --> 1228.98]  I'll tell you how.
[1229.34 --> 1230.98]  I'm sure there's embedded Linux on that thing.
[1231.42 --> 1232.04]  Very possible.
[1232.48 --> 1232.74]  Right.
[1233.08 --> 1234.14]  Let's hack that thing.
[1234.26 --> 1238.90]  How can we check its outgoing IP lookups and stuff like that?
[1238.94 --> 1240.40]  Let's look at its DNS lookups.
[1241.04 --> 1242.82]  Let's actually hack it to make it not a bike.
[1243.16 --> 1246.42]  Then you find out that it's phoning home and it's tracking everything you're doing.
[1246.42 --> 1246.68]  That's right.
[1246.68 --> 1247.66]  And you can bust them.
[1247.92 --> 1248.36]  You can bust them.
[1248.36 --> 1248.92]  And you out the people.
[1249.40 --> 1249.92]  That's right.
[1250.14 --> 1250.68]  You're paid.
[1250.68 --> 1255.42]  They sent me this free bike and now I'm debunking them on their privacy problems.
[1257.00 --> 1258.68]  That's how you really get the views, Nick.
[1259.44 --> 1260.10]  That is.
[1260.34 --> 1260.76]  There we go.
[1260.94 --> 1266.80]  So just call us anytime you get new hard word opportunities and we'll give you ideas to do or to not do.
[1266.80 --> 1268.34]  All kinds of stuff that we never do either.
[1269.50 --> 1270.22]  No, we don't.
[1270.38 --> 1270.60]  No, we don't.
[1271.30 --> 1271.88]  It would be fun.
[1273.36 --> 1274.50]  Peloton, send me a bike.
[1274.92 --> 1276.04]  I'll hack it.
[1276.26 --> 1276.70]  There you go.
[1276.70 --> 1280.40]  Well, let's dive into our topic for today.
[1280.64 --> 1285.76]  This is a follow-up to the last time we had you on, which has been a few years.
[1285.88 --> 1287.62]  But we talked modern Unix tools.
[1288.42 --> 1297.34]  And that was a lot of fun, going through a lot of the common Unix tools like LS and CD and CAT and et cetera, et cetera, et cetera.
[1298.34 --> 1305.18]  And talking about modern alternatives to those which have bells and whistles.
[1305.18 --> 1306.74]  So that was that episode.
[1306.86 --> 1308.10]  People can go back in the feed.
[1308.20 --> 1309.44]  Episode 451.
[1310.22 --> 1311.34]  We will link it up.
[1311.74 --> 1314.22]  Modern Unix tools with Nick Janatakis.
[1314.60 --> 1317.34]  Today we're going to talk terminal again.
[1317.56 --> 1318.88]  We're focusing on TUIs.
[1319.00 --> 1321.68]  I feel like TUIs are having a moment.
[1322.14 --> 1324.28]  A, I don't want to call it a revolution.
[1324.60 --> 1325.28]  A renaissance.
[1325.52 --> 1326.02]  There you go.
[1326.52 --> 1327.08]  A renaissance.
[1327.42 --> 1330.10]  Probably in light of a lot of the tooling that's now available.
[1330.10 --> 1343.32]  We've had shows with people like Charm, the Charm Bracelet folks who are providing Go-based tooling for doing all kinds of text-based and terminal things.
[1344.00 --> 1352.24]  And then there's also, is it Wilma Guggen, I believe, and the Textualize folks over there providing similar tools for the Python community.
[1352.24 --> 1357.14]  And a lot of the stuff that we'll talk about today is built with Textualize.
[1357.82 --> 1363.24]  And then there's also something going on in the Rust world with a toolkit called Ratatouille.
[1364.24 --> 1367.86]  And the truth is, I have no talent at all.
[1368.08 --> 1371.86]  But this rat, he's the one behind these recipes.
[1372.04 --> 1372.76]  He's the cook.
[1373.74 --> 1375.06]  Spectacular name, by the way.
[1375.06 --> 1380.06]  I'm going to grab that one and throw it in my notes real quick because I'm compiling a list of the best open source puns.
[1380.88 --> 1386.32]  And, of course, that's a reference to the movie or maybe just the dish or both.
[1386.80 --> 1387.16]  Both.
[1387.58 --> 1388.48]  But it's a good pun.
[1388.54 --> 1397.72]  By the way, if you're listening and you have a good open source project pun that makes you laugh, giggle, or at least smirk whenever you hear it or read it, send it my way.
[1397.86 --> 1399.14]  I'm putting together a blog post.
[1399.78 --> 1402.88]  But Ratatouille in the Rust world is a rust crate for cooking up.
[1403.64 --> 1404.62]  Oh, they're doubling down.
[1404.62 --> 1405.70]  That's their words, not mine.
[1405.80 --> 1409.04]  Cooking up terminal user interfaces.
[1409.82 --> 1415.88]  And, of course, its little mascot is a rat-looking chef.
[1416.64 --> 1420.62]  So a lot of the tools that we're seeing also are written in Rust is the reason why I bring that up.
[1420.72 --> 1425.70]  So, like, Ratatouille is powering this movement, charm, and Textualize perhaps more.
[1425.80 --> 1433.90]  Some people are just old school building up end curses stuff, you know, hand rolling their terminal or text-based user interfaces.
[1433.90 --> 1435.76]  But lots going on.
[1435.82 --> 1438.82]  And so there are so many Tuis now.
[1439.48 --> 1448.54]  In fact, we went out to the awesome Tuis repo, which happens to be maintained by ShipIt host Justin Garrison.
[1448.54 --> 1450.58]  And I didn't even realize that when I first loaded it up.
[1450.62 --> 1455.32]  But I do know Justin is super into text-based UIs.
[1455.96 --> 1461.82]  And if you just look at that repo and scroll it, holy cow, y'all.
[1462.06 --> 1463.06]  There's hundreds on there.
[1463.50 --> 1464.82]  And those are just the ones that have been submitted.
[1464.82 --> 1467.54]  So that's kind of the topic for today.
[1467.62 --> 1474.14]  We both have or we all have brought some Tuis to the world, to the show, to discuss.
[1474.82 --> 1478.06]  But let's start with maybe Tuis, maybe not.
[1478.16 --> 1486.62]  But terminal tools, tips and tricks that we've been using or are using or know about that we could share with each other and with our listener.
[1486.74 --> 1489.68]  Nick, starting with you, I know you are a command line junkie.
[1490.52 --> 1490.62]  Yeah.
[1490.62 --> 1492.12]  So just general tips?
[1492.50 --> 1496.36]  General tips are maybe a tool you've been using recently or something you've learned.
[1496.50 --> 1497.10]  Anything you want.
[1497.60 --> 1498.32]  Open book.
[1498.88 --> 1499.62]  Yeah, it's kind of funny.
[1500.02 --> 1506.42]  When it comes to solving these business problems that sometimes get thrown my way, it always comes back to grep, set, and cut.
[1506.70 --> 1511.10]  Those three tools combined can solve so many random things that might come your way.
[1511.70 --> 1513.48]  For example, just a quick use case.
[1513.64 --> 1520.26]  The business came at me and they're like, by the way, we have this Salesforce dump of 178 CSV files.
[1520.62 --> 1522.08]  And it was like 30 gigs of data.
[1522.18 --> 1524.98]  So we have 100, you know, let's call it 180 files, a lot of data there.
[1525.24 --> 1526.98]  You know, all the different columns, all the different rows.
[1526.98 --> 1530.12]  And it's like, well, now we need to import that into a MySQL database.
[1530.78 --> 1534.42]  And, you know, if you try to do that by hand, you know, what are you going to do?
[1534.50 --> 1538.98]  You're going to have to make like 8,000 different columns and like so many different tables, like 180 of them or whatever.
[1539.34 --> 1544.98]  But yeah, I just threw together a little bit of shell scripting, like 30 lines of code with like set and grep and cut and all those combined.
[1545.28 --> 1548.30]  And we had a solution that got us like 95% of the way there.
[1548.30 --> 1554.26]  Like it just auto-generated the create table syntax and like auto-filled out the columns with like varkar 55 by default.
[1554.54 --> 1556.92]  And then someone can go in there by hand to like modify things as needed.
[1557.12 --> 1558.26]  And it worked out real nice.
[1558.64 --> 1561.14]  So yeah, just random, random stuff like that.
[1561.14 --> 1568.02]  Yeah, I mean, that's the beauty of Unix Tools is just the composability, like little functions, do one thing well.
[1568.34 --> 1570.44]  And then the combining of them.
[1570.90 --> 1576.46]  Like a good chef, Adam, you know, will put together different ingredients and come up with an amazing recipe.
[1576.72 --> 1577.12]  That's right.
[1577.28 --> 1578.12]  That may be a one-off.
[1578.20 --> 1580.46]  Maybe it's something they should wrap up and share with the world.
[1580.68 --> 1588.68]  But what's the movie where Adam Sandler is a chef and he goes home to make himself a sandwich at one point?
[1589.74 --> 1589.76]  And.
[1590.14 --> 1590.86]  Yeah, what was that movie?
[1590.86 --> 1592.36]  It's just like an egg sandwich.
[1593.04 --> 1599.92]  But because he's a world-renowned chef, the way that he makes himself a sandwich for lunch is still just like mouthwatering.
[1599.98 --> 1607.32]  You're like, oh man, how cool would it be to be that good at cooking that even your throwaway lunch sandwich is just like drool worthy.
[1607.72 --> 1608.62]  Maybe Spanglish?
[1609.30 --> 1609.66]  Spanglish.
[1609.86 --> 1610.82]  It was Spanglish, yeah.
[1611.16 --> 1611.52]  Awesome.
[1612.14 --> 1612.90]  Came back to me.
[1613.12 --> 1613.58]  Good movie.
[1613.80 --> 1615.22]  A really underrated movie, honestly.
[1615.22 --> 1615.94]  Yeah, I like that one.
[1615.96 --> 1617.38]  It's a solid, solid movie.
[1617.66 --> 1619.46]  A lot of good acting in that movie, in my opinion.
[1619.94 --> 1620.60]  I like that one.
[1620.60 --> 1621.80]  Nick, that's definitely a good use.
[1622.50 --> 1624.58]  Grep, said, and cut.
[1625.12 --> 1629.60]  I was doing similar things with our front-end feud survey results.
[1630.60 --> 1634.22]  So we use type form to go out and ask people a bunch of questions.
[1634.22 --> 1638.58]  And because they are free form, this is for like Family Feud.
[1638.66 --> 1639.90]  Are you familiar with the game, Nick?
[1639.96 --> 1640.50]  Family Feud?
[1640.76 --> 1641.60]  Survey says yes.
[1641.82 --> 1642.22]  Yeah, totally.
[1642.86 --> 1648.38]  And so because it's survey says, the whole point of it is the form has to be a text box.
[1648.46 --> 1650.84]  It cannot be a multiple choice because that ruins the entire point.
[1650.90 --> 1651.96]  Like what would people say?
[1651.96 --> 1654.88]  And they have to be able to type whatever they want.
[1655.54 --> 1658.26]  And so we use type form just to collect the entries.
[1658.52 --> 1662.08]  And then I download a CSV inside type form.
[1662.20 --> 1665.26]  I'm not going to just read through all these and tally them up, you know, by hand.
[1665.26 --> 1671.68]  And so for a long time I had this process where I would open up the CSV in numbers.
[1672.24 --> 1676.26]  And then I would like scrub and normalize and try to do some stuff.
[1676.42 --> 1679.82]  And then I would export it back out to a different CSV.
[1679.82 --> 1685.48]  And then I would use, then I would import that CSV into a SQLite database.
[1686.04 --> 1690.46]  And then I would use the SQLite command line to go inside there and query it.
[1690.98 --> 1695.74]  And then I realized or I was taught by somebody, might have been Simon Willison.
[1696.40 --> 1697.34]  I can't remember who taught me.
[1697.92 --> 1702.98]  That SQLite actually has a CSV mode and an in-memory mode.
[1703.80 --> 1708.10]  And then it also will take queries directly from the command line.
[1708.10 --> 1713.16]  So you don't have to go into like the little SQLite UI and do things from there, the prompt.
[1713.88 --> 1719.30]  And so I reduced, this is not multiple tools together, but this is like just knowing a tool better.
[1719.66 --> 1725.38]  I actually reduced that entire process down to a single command line that would just tell,
[1725.56 --> 1731.50]  that would take the original CSV from type form, open it in memory in SQLite as a CSV,
[1732.16 --> 1734.36]  which automatically creates the tables right there and everything.
[1734.36 --> 1738.14]  And then execute the specific query and then output it the way I wanted to.
[1738.34 --> 1739.98]  And I was like, oh, happy day.
[1740.28 --> 1743.78]  You know, like when you have something like that just works like that, it's amazing.
[1743.98 --> 1746.76]  When you, you're just cutting down five steps to one.
[1746.88 --> 1748.60]  It's like, you feel like you're superhuman.
[1748.86 --> 1748.98]  Yeah.
[1749.54 --> 1750.36]  No, I love stuff like that.
[1750.36 --> 1764.96]  Hey friends, I'm here with a new friend of mine, Shane Harder, the founder of Chronitor.
[1765.20 --> 1767.16]  Check them out, chronitor.io.
[1767.52 --> 1773.46]  They let you keep tabs on your chron jobs, Linux, Kubernetes, Apache Airflow, Sidekick, and more.
[1773.46 --> 1779.76]  With over 12 open source integrations, you can instrument all your jobs, no matter where you're running them.
[1780.18 --> 1782.10]  So Shane, for me, you know I'm a user of Chronitor.
[1782.46 --> 1786.00]  To me, it is the missing link, in my opinion, to Chron.
[1786.28 --> 1787.02]  What do you think?
[1787.06 --> 1787.86]  How do you explain it?
[1788.06 --> 1793.94]  You know, every other software that a developer creates, you can watch it work and you can interact with it.
[1793.94 --> 1808.14]  You run it from a command line or you have an API endpoint and it's, you have logs that get produced and it's really easy to add like an APM monitoring into your API where you can start to get a sense of what your application is doing internally.
[1808.42 --> 1813.28]  But when it comes to chron jobs, that somehow just was never built until Chronitor.
[1813.68 --> 1822.62]  Chron jobs, you would have to run them at the command line, see that they were, and then just fire them off into the ether and let crontab run them.
[1822.62 --> 1829.56]  And the only way you could know if they're working or not is by looking at the database to see if the thing did its job.
[1829.72 --> 1833.72]  Or if it's like, maybe if it's supposed to upload files, maybe you would just go check that the files are uploaded.
[1834.06 --> 1836.28]  But that sort of verification doesn't scale.
[1836.50 --> 1840.60]  It's hard to write tests, like end-to-end tests that do that in production.
[1840.98 --> 1844.58]  Even if you can, then they're bound to break eventually as the cron job breaks.
[1844.84 --> 1851.84]  You know, if you're testing a specific bucket for a file, if you're checking that file gets uploaded, you know, soon enough that bucket's going to change or the file's going to change.
[1851.84 --> 1852.82]  And then your test's going to break.
[1853.04 --> 1863.48]  Rather than just looking for the side effects to know that it's working, Chronitor is actually watching every cron job execution and reporting back to the cloud service when your job runs, starts, or fails.
[1863.64 --> 1866.54]  Along with like telemetry, including like the full log output.
[1866.54 --> 1872.88]  So when it does fail, you've got like the metrics and the logs that you need to dig in and understand why and debug it and fix it.
[1873.42 --> 1878.98]  So I'm using Linux and Linux cron jobs are by far the most popular in my opinion, right?
[1878.98 --> 1882.16]  But there's so many other cron-like things.
[1882.28 --> 1885.36]  Kubernetes, Airflow, Sidekick.
[1885.78 --> 1891.34]  Help me understand the full spectrum of background jobs and cron jobs beyond Linux cron.
[1891.74 --> 1894.72]  Yeah, Linux cron jobs are massively popular.
[1895.04 --> 1902.90]  They are still, 40 years later, the tool that most developers will go to first when they need to start scheduling something in the background.
[1902.90 --> 1908.78]  But when you get into a team environment or an enterprise environment, there is a lot of other constraints at play.
[1908.98 --> 1910.22]  And there's other considerations.
[1910.58 --> 1919.04]  And whether it's simply like redundancy that you're not going to get from cron tab itself or, you know, more like complex orchestration stories like you can get with like Airflow.
[1919.04 --> 1921.90]  We see companies eventually outgrowing cron.
[1922.18 --> 1928.64]  And what we wanted to be sure of is that, first of all, like migrating from cron to anything else is a complicated thing.
[1928.88 --> 1936.16]  So we wanted to give you tools to help you monitor that transition and make sure your jobs are working good as you do that migration.
[1936.52 --> 1946.08]  You know, and then second, we wanted to give you a way to unify all these different job platforms because seldom do you have just like platform A and you migrate cleanly to platform B.
[1946.08 --> 1951.00]  Probably in a real world scenario, you're running both side by side for a while.
[1951.38 --> 1958.30]  You don't want to have different monitoring tools or different monitoring strategies for different for every different platform that you that you deploy.
[1958.50 --> 1962.22]  So our goal is anywhere you're running a background job, you can use Cronitor.
[1962.50 --> 1972.16]  The number one way that we ensured that was possible is by having like a really simple API that you can just use with an HTTP request yourself, which is pretty abnormal for monitoring tools.
[1972.42 --> 1973.98]  But that works in a lot of cases.
[1973.98 --> 1982.60]  But to make it easier, then every popular job platform out there, like Linux, CronJobs, Kubernetes, CronJobs, Windows, Sidekick, Airflow, you name it.
[1982.80 --> 1994.04]  We have a Cronitor SDK that you can install that will run automatically, configure your monitoring, run in the background and sync all your jobs with Cronitor the same way your Linux CronJobs will be synced.
[1994.48 --> 1997.88]  OK, friends, join more than 50,000 developers using Cronitor.
[1998.12 --> 1998.90]  I'm one of them.
[1998.90 --> 2003.00]  You can start for free and they have a pay as you grow pricing plan.
[2003.28 --> 2007.28]  Setup is too easy with more than 20 SDKs.
[2007.50 --> 2009.88]  Check them out at Cronitor.io.
[2010.24 --> 2014.60]  That's C-R-O-N-I-T-O-R.io.
[2015.00 --> 2017.06]  Again, Cronitor.io.
[2017.06 --> 2025.16]  As far as tools we're using, I'm still rocking A2N.
[2025.30 --> 2026.78]  Adam, are you still using it?
[2026.86 --> 2027.24]  A2N?
[2027.62 --> 2027.96]  Mm-mm.
[2028.16 --> 2028.50]  No?
[2028.92 --> 2030.06]  I don't have a need for it, I guess.
[2030.18 --> 2030.44]  Yeah.
[2031.08 --> 2034.16]  I use warp as my terminal and it remembers a lot for me.
[2034.16 --> 2035.26]  Yeah, you're using warp on the terminal.
[2035.52 --> 2035.84]  Mm-hmm.
[2036.32 --> 2037.36]  Nick, do you know about A2N?
[2037.70 --> 2037.98]  Nope.
[2037.98 --> 2040.62]  Is it an actual, like, a terminal or something else?
[2040.98 --> 2043.36]  A2N is a history tool.
[2044.06 --> 2053.22]  So it replaces Ctrl-R and the up arrow with a better interface, fuzzy search, a bunch of
[2053.22 --> 2058.56]  stuff that is basically like your terminal's history on steroids, so to speak.
[2058.56 --> 2063.14]  And we did a show with A2N's creator, Ellie Huxtable.
[2063.68 --> 2063.86]  Mm-hmm.
[2064.00 --> 2065.52]  Yeah, we did a show with Ellie Huxtable.
[2065.52 --> 2070.30]  And it's one of these tools where it kind of disappears into the background.
[2070.46 --> 2074.54]  It's not, like, front and center, because I'm never actually typing the A2N command.
[2074.72 --> 2079.38]  It's just in there, in my history, and you invoke it via things that you're already invoking.
[2079.88 --> 2086.06]  You know, if you're Ctrl-Ring to search or just arrowing up or down to find recent commands.
[2086.62 --> 2087.68]  And I've installed that.
[2087.76 --> 2089.18]  I think that was, like, a year or so ago.
[2089.82 --> 2091.60]  And I'm still rocking that.
[2091.68 --> 2093.54]  Definitely am not going to uninstall.
[2093.54 --> 2099.62]  It's just small quality of life improvements over the default Bash history or ZSH history.
[2100.16 --> 2100.34]  Oh, yeah.
[2100.44 --> 2101.00]  It's interesting.
[2101.12 --> 2104.32]  I forgot the name of that tool, but I'm pretty sure I vaguely remember it now from, like,
[2104.34 --> 2106.10]  a Hacker News post from some time ago.
[2106.64 --> 2107.84]  Yeah, it's pretty well beloved.
[2107.90 --> 2111.02]  It's one of those things that just kind of makes your life better and doesn't ask anything
[2111.02 --> 2111.42]  of you.
[2111.60 --> 2113.16]  And so it's like, why not?
[2113.26 --> 2113.54]  For sure.
[2113.54 --> 2114.56]  Let me ask you this.
[2114.98 --> 2117.32]  So I like using Ctrl-R all the time.
[2117.46 --> 2122.56]  And I happen to use FCF to do, you know, searching through my history like that, which could be
[2122.56 --> 2126.20]  classified as a T-U-I to some degree because it is opening up like a little interface that
[2126.20 --> 2127.00]  you can interact with.
[2127.44 --> 2130.04]  How does this tool compare to FCF?
[2130.16 --> 2132.64]  Like, have you tried both side by side or in general?
[2132.64 --> 2136.00]  Not side by side, but I did use FCF for a little while.
[2136.84 --> 2141.42]  And you're going to find very similar fuzzy finding with A2N.
[2141.72 --> 2147.10]  It's a little bit better looking in terms of, like, she's taking more time to make sure
[2147.10 --> 2150.56]  that the UI is nicer than I think FCF is.
[2150.60 --> 2152.28]  I know you can tweak that and customize it.
[2152.78 --> 2157.14]  But it's really kind of a no-step similar functionality.
[2157.14 --> 2162.86]  So with FCF, this is like a thing that you go into somewhere and make sure that in your
[2162.86 --> 2166.64]  Bash RC or whatever, and make sure that when you Ctrl-R, FCF gets invoked and there's
[2166.64 --> 2168.30]  like some steps that get us to set up, right?
[2168.76 --> 2168.92]  Yeah.
[2169.02 --> 2171.90]  And then on top of that, I mean, if you're talking about history stuff, there's, you
[2171.90 --> 2175.38]  know, many different Bash or Z shell settings that you need to configure just to get your
[2175.38 --> 2179.00]  history set up so that you can save 50,000 lines worth and, you know, other things like
[2179.00 --> 2179.18]  this.
[2179.38 --> 2179.96]  Yeah, exactly.
[2180.06 --> 2185.02]  Which I had done all that stuff because I didn't know about A2N until like, you know, a year
[2185.02 --> 2185.30]  ago.
[2185.64 --> 2190.14]  And so if you already have all that stuff set up with FCF, you're going to have a very
[2190.14 --> 2194.44]  similar fuzzy searching of your history with A2N as you would with FCF.
[2195.12 --> 2199.74]  A2N does bring a few other things to the table like stats and I don't know, when you
[2199.74 --> 2205.68]  up arrow, are you having fuzzy search inside of the history there?
[2205.84 --> 2210.44]  Or like is FCF invoked at all in your up and down arrowing through your history?
[2210.72 --> 2212.24]  Or is that just the standard Linux one?
[2212.24 --> 2216.76]  No, if I'm just hitting the up arrow in my shell, I don't, it doesn't invoke FCF.
[2216.96 --> 2217.12]  Yes.
[2217.18 --> 2220.36]  I mean, there might be some like custom key binds to do something with that, but I haven't
[2220.36 --> 2220.78]  set that up.
[2220.86 --> 2221.02]  Yeah.
[2221.10 --> 2224.22]  So that's one thing about A2N is even when you up arrow, I'm sure you can probably turn
[2224.22 --> 2230.30]  this off, but it will invoke the A2N UI, which you can just continue to up arrow like
[2230.30 --> 2236.46]  you normally would, except for you also then have that same fuzzy search functionality as
[2236.46 --> 2237.48]  you would with control R.
[2237.48 --> 2241.06]  And so sometimes you're not thinking about control R and you're just like up arrowing
[2241.06 --> 2244.76]  and you realize, you know, it was like, oh, not that version of this command.
[2244.86 --> 2245.44]  It was a different one.
[2245.50 --> 2246.74]  Then you can start to like narrow it down.
[2246.82 --> 2249.68]  So it's just slightly more tuned into that.
[2249.74 --> 2252.62]  But other than that, I think that the experience would be relatively similar.
[2253.70 --> 2253.94]  Yeah.
[2253.94 --> 2254.86]  I just tested this now.
[2254.96 --> 2258.50]  So if you just go to your terminal with FCF and just hit control R, that will bring up
[2258.50 --> 2259.44]  your search history there.
[2259.46 --> 2262.78]  And then you can kind of up and down through FCF's window, but you still need to invoke it
[2262.78 --> 2264.24]  with like a, you know, control R.
[2264.24 --> 2264.68]  Right.
[2265.14 --> 2269.10]  So for folks who already have that configured, probably not a big win, but for people who
[2269.10 --> 2274.38]  are new to the terminal or didn't know about FCF and how to set up the right environment
[2274.38 --> 2280.14]  variables to get their bash or ZSH history to be 50,000 lines or whatever, like installing
[2280.14 --> 2284.46]  A2N, I think is an easy, like one step that does all those things for you.
[2284.92 --> 2287.02]  So let me follow up with one more question about that.
[2287.18 --> 2287.32]  Sure.
[2287.48 --> 2290.96]  So one interesting thing when you're dealing with your shell's history is if you happen to
[2290.96 --> 2295.60]  be using a tool like Tmux and you have multiple sessions and panes and windows running, how
[2295.60 --> 2300.96]  does this tool let you have a unified shell history between all of them without like, you
[2300.96 --> 2304.34]  know, things getting out of date or commands not being in the right order when you want
[2304.34 --> 2304.52]  them?
[2304.96 --> 2305.30]  Yes.
[2305.40 --> 2310.48]  So that's one of the core things about A2N is it's unified shell history, not just across
[2310.48 --> 2314.20]  your Tmux sessions, but actually, and here I am with one computer, so I don't really get
[2314.20 --> 2317.18]  to live this life, but across all your machines as well.
[2317.18 --> 2321.24]  So that's one of the core things that Ellie is doing that I don't really care about as
[2321.24 --> 2325.46]  much because I just have one computer is like, you could have your shell history across and
[2325.46 --> 2330.80]  synced across all of your machines via into an encrypted sync service that she provides.
[2331.00 --> 2334.80]  But I don't really know how I want that to work sometimes, honestly.
[2335.18 --> 2340.38]  Like I get in, there's moments where I'm like, oh, I type this command into another Tmux
[2340.38 --> 2346.44]  session and I would love to just up arrow and type it here and it's not there.
[2346.82 --> 2350.16]  And then there's times where it is there, but I don't want it to be there.
[2350.20 --> 2352.18]  I'm like, actually, that was contextual to another thing.
[2352.22 --> 2353.84]  I don't want it in this little shell history.
[2353.98 --> 2358.50]  I mean, I am of two minds about how I would actually want the feature to work.
[2358.74 --> 2360.02]  I think it's not straightforward.
[2360.52 --> 2361.52]  Have you had that experience?
[2362.22 --> 2362.60]  Very much.
[2362.66 --> 2366.36]  And it's very much like not straightforward because it almost feels like the only way to
[2366.36 --> 2370.80]  solve this and like the best way possible is like, just do like what I want.
[2370.94 --> 2371.44]  That's it.
[2371.56 --> 2373.00]  That's what I wanted to do as well.
[2373.08 --> 2377.86]  But I don't know that the computer knows what you want is the problem.
[2378.12 --> 2384.56]  You know, does it say things like as if you LST and then with some flags, a particular
[2384.56 --> 2389.86]  directory, is it keeping the base command plus flags plus directory in its history too?
[2389.96 --> 2396.10]  So that when you re-invoke it, it's like, well, I want the LST command with these
[2396.10 --> 2398.62]  flags, but not with the argument.
[2398.96 --> 2400.26]  It's going to be the entire command.
[2400.68 --> 2401.46]  Yeah, that's kind of painful.
[2401.70 --> 2405.40]  So you might have to like up arrow, select it, and then you can hit tab or whatever.
[2405.40 --> 2408.20]  And then you can like delete back and stuff like that.
[2408.26 --> 2414.98]  You can probably do a quick shell expansion thing with the exclamation mark and that kind
[2414.98 --> 2418.94]  of stuff, which is obviously more Kung Fu and things that I can't remember how they
[2418.94 --> 2419.56]  work all the time.
[2419.56 --> 2425.40]  But yeah, it's not smart enough to know, like I just want the flags.
[2425.70 --> 2429.34]  Like I want the, I liked that version of LS, but now I'm doing it in a different context.
[2429.42 --> 2431.78]  I want to change the path or use no path.
[2431.88 --> 2433.26]  I think you have to just do that stuff manually.
[2433.78 --> 2433.80]  Yeah.
[2434.28 --> 2437.04]  This is where I like warp.
[2437.04 --> 2443.90]  I don't know if it has this feature because I do use a few machines, but so sparingly that
[2443.90 --> 2446.92]  I forget what I've done the last time I used it.
[2447.66 --> 2452.64]  And so warp, at least on a single machine, I think you would appreciate this, Jared, and
[2452.64 --> 2455.60]  I already use A2N, is that it does that.
[2455.68 --> 2463.70]  So like I'm just tinkering on this spare Linux VM I have on Proxmox because, hey, I'm on a
[2463.70 --> 2464.18]  podcast.
[2464.30 --> 2464.90]  I'm about two ways.
[2465.00 --> 2466.36]  I'm like, I'm going to install some, right?
[2466.36 --> 2470.36]  And I want to do it in a way where I can just blow it away and there you go.
[2471.34 --> 2475.12]  And so I'm logged in and I'm just like, well, what are some recent commands just to see if
[2475.12 --> 2475.58]  they're there?
[2475.64 --> 2476.42]  Because I know they're there.
[2476.50 --> 2479.98]  I know how warp works, but just to see if they've actually followed me even into this
[2479.98 --> 2480.64]  different machine.
[2481.10 --> 2482.24]  And of course they're there.
[2482.32 --> 2487.52]  So like I have that same feature because of the terminal application I've chosen versus
[2487.52 --> 2490.28]  this sub thing.
[2490.74 --> 2495.04]  And I think the one thing that I think warp is driving towards, and this is by zero an ad,
[2495.04 --> 2496.12]  they're not even sponsoring us.
[2496.32 --> 2496.96]  I just like them.
[2497.44 --> 2498.82]  And Zach's cool and I like his team.
[2499.40 --> 2501.34]  And I believe it is a version of the terminal of the future.
[2501.50 --> 2501.92]  There you go.
[2502.54 --> 2506.84]  I think that they're doing things like team features, which I think would be cool because
[2506.84 --> 2513.12]  you can log in to warp and let those things transfer via their cloud service if they do
[2513.12 --> 2513.30]  that.
[2513.30 --> 2514.64]  I think that's where they're driving towards.
[2515.08 --> 2520.04]  I wish they would do that more so with settings because going between machines, it doesn't
[2520.04 --> 2520.60]  have that.
[2521.10 --> 2526.94]  Whereas another tool I use daily is Raycast and it has that where it cloud syncs settings.
[2527.10 --> 2530.40]  It doesn't cloud sync clipboard history and sensitive things.
[2530.58 --> 2536.52]  It's doing things that like themes and stuff you really want to have unified between machines.
[2537.04 --> 2538.24]  That's kind of how I look at these tools.
[2538.24 --> 2542.30]  Even though we're talking about TUIs, I still feel like Raycast and warp are kind of similar
[2542.30 --> 2547.50]  in that respect because they're a layer above the need for a TUI because the application
[2547.50 --> 2551.32]  itself has the things in it it needs to give you that history.
[2552.18 --> 2553.02]  There's other stuff too.
[2553.08 --> 2558.30]  I'm not even using like expansions and snippets, things I'm not even like, I don't know.
[2558.44 --> 2560.02]  I don't even know how to use them, honestly.
[2560.44 --> 2561.46]  I think some of the tooling...
[2561.46 --> 2562.28]  Does it support Tmux?
[2562.70 --> 2564.24]  Well, I really wish maybe...
[2564.24 --> 2569.02]  I haven't dug into their documentation to like criticize it, but even Raycast, they're
[2569.02 --> 2573.66]  doing a great job with like teaching you how to use the tool because there's always
[2573.66 --> 2574.40]  these hidden features.
[2574.50 --> 2578.60]  I think H1 probably could do this as well or basically any tool that has hidden features
[2578.60 --> 2584.32]  that are not easily discoverable because the Jared's of the world will just be happy with
[2584.32 --> 2590.08]  the defaults that you're given and not all the expressiveness that you can achieve if
[2590.08 --> 2591.22]  you would just tweak a few things.
[2591.32 --> 2593.86]  And maybe Nick is the kind of person who's like, let me tweak this.
[2593.86 --> 2594.74]  Nick knows all the different things.
[2594.74 --> 2597.52]  On the super old hardware, by the way, but let me tweak this.
[2598.78 --> 2599.36]  Yeah, exactly.
[2599.64 --> 2601.76]  Now, Nick definitely knows all the command line flags, don't you, Nick?
[2602.64 --> 2603.16]  Some of them.
[2603.40 --> 2603.60]  Yeah.
[2603.98 --> 2604.32]  Some of them.
[2604.32 --> 2605.46]  I mean, he's written them down at least.
[2605.56 --> 2606.16]  They're on his blog.
[2606.38 --> 2607.02]  They're on his YouTube.
[2607.30 --> 2609.34]  He may forget them, but he can always...
[2609.34 --> 2613.66]  They're a Google search away as long as Google search continues to index our content.
[2613.66 --> 2615.30]  But that's a different topic.
[2616.14 --> 2616.38]  Yeah.
[2616.66 --> 2617.70]  I mean, Warp is cool.
[2617.96 --> 2621.12]  I love people trying to reinvent stuff, you know, make it better.
[2621.12 --> 2621.56]  Sure.
[2622.02 --> 2625.18]  As soon as I get Tmux support, then maybe I can give it a try.
[2625.38 --> 2627.54]  But until then, and it sounds like Nick, you're probably with me.
[2628.08 --> 2632.64]  I'm just not going to use it because I live inside of Tmux pretty much everything I do.
[2633.52 --> 2639.38]  And so that's the rub with trying to replace a lower level foundational part of the stack.
[2639.38 --> 2648.24]  Whereas A2N is like a history thing, like it's a smaller subsection of your terminal, is that you have to support, you know, all these different things.
[2648.24 --> 2653.22]  And there's a long history of weirdness inside of terminals that is just difficult.
[2653.22 --> 2663.66]  And so until then, or they convinced me they've replaced Tmux with their own functionality that is better than Tmux and provides me all the same things that Tmux does.
[2664.32 --> 2665.60]  I think they could probably get that done.
[2665.68 --> 2668.10]  I'm a relatively vanilla user of Tmux.
[2668.20 --> 2669.74]  I'm not an advanced Tmuxer.
[2670.44 --> 2672.80]  But that's an education problem, right?
[2672.84 --> 2674.84]  Like they have to be able to teach people that they've done that.
[2675.40 --> 2675.80]  Yeah, I agree.
[2675.80 --> 2682.28]  I've never been, I've used Tmux several times, but I've never been like, oh, this is, this is the way.
[2682.88 --> 2689.40]  I never sat beside somebody either or like pair programmed or pair terminal, which is probably different than programming.
[2689.52 --> 2691.12]  It's like, just like, let me just see how you hack.
[2691.94 --> 2696.08]  To really be like, oh, well, I'm really missing something with Tmux.
[2696.16 --> 2696.96]  Like I've used it.
[2697.50 --> 2699.28]  It's kind of kludgy in some cases.
[2699.68 --> 2703.06]  But maybe that's because I haven't gotten past that even like the Vim stage.
[2703.06 --> 2707.86]  Like I'm a fairly daily user of Vim, but very basic user of Vim studio.
[2708.04 --> 2713.96]  Like I even like getting to the end of lines or jumping lines or copying multiple lines or even yanking and pasting.
[2714.06 --> 2715.76]  Like those are the, I'm doing basics, you know.
[2716.10 --> 2717.26]  I can at least get out of it.
[2717.34 --> 2718.48]  So thank you very much.
[2718.96 --> 2722.10]  But, you know, with Tmux, I've never gotten past the whole training wheels.
[2722.24 --> 2725.70]  Let me actually find usefulness because I guess I just haven't.
[2726.06 --> 2726.18]  Sure.
[2726.60 --> 2728.30]  Well, Nick, you're a Tmux user, right?
[2728.88 --> 2729.08]  Yeah.
[2729.36 --> 2730.38]  Give that on the pitch.
[2730.96 --> 2731.54]  What's the pitch?
[2731.78 --> 2732.18]  Okay.
[2732.18 --> 2732.26]  Okay.
[2732.60 --> 2740.02]  So if you like to use the terminal, let's say you're using Vim or whatever editor and running a whole bunch of different command line tools, maybe TUIs as well.
[2740.34 --> 2743.70]  And you don't want to leave your terminal to juggle multiple projects.
[2743.88 --> 2753.90]  I mean, you can use something like Tmux sessions to have, let's say, you know, maybe if you're working on the changelog source code or maybe you have your own personal blog or maybe you have a different project, the Kassad project that you're building.
[2753.90 --> 2755.90]  You know, you can have a Tmux session for all three of those things.
[2755.90 --> 2759.52]  And then use Tmux to jump between each of those.
[2759.68 --> 2764.94]  And all three of those sessions, they might have their own window layouts that are, you know, specific to that application.
[2764.94 --> 2768.76]  Like with the changelog source code, you know, maybe you have your code editor in one window.
[2768.86 --> 2773.02]  Maybe you have like Docker Compose up or however you run your application in another window.
[2773.02 --> 2776.28]  And then, you know, when you jump to your own personal blog, it has its own set of windows.
[2776.42 --> 2786.98]  So you can kind of switch between contexts very quickly and have everything just ready to go right there for you without having to be like, oh, I got to open up my code editor and split this window, open up a second terminal and then, you know, do all these things.
[2787.32 --> 2791.86]  That's typically how I use Tmux in my day to day just to help me juggle a lot of different things.
[2792.14 --> 2796.70]  You know, because I have probably like 11 or 12 different Tmux sessions, basically 11 or 12 different projects.
[2796.70 --> 2798.32]  And yeah, they're all laid out a little bit different.
[2798.32 --> 2806.76]  I mean, Tmux makes it super easy to like, if I just want to open up a second window or split a plane vertically or horizontally, you know, I can do that type of stuff and jump between those hotkeys.
[2806.88 --> 2810.04]  Like if I want to go to window one or two or three, you know, that's just a hotkey away.
[2811.42 --> 2813.24]  Yeah, I've been there to do some of those things.
[2813.44 --> 2818.60]  I definitely am not a daily driver in the terminal where I'm like effective and efficient on the daily.
[2818.82 --> 2820.42]  My work is generally outside of that.
[2820.52 --> 2821.92]  My tinkering is more in it.
[2822.48 --> 2827.38]  So I haven't found the need to be like, let me obsess over the tooling so much.
[2828.32 --> 2829.74]  What's wrong with multiple tabs?
[2830.52 --> 2831.84]  Well, you have to set them back up again.
[2832.02 --> 2832.44]  I have to go.
[2832.60 --> 2833.54]  See you later, guys.
[2835.92 --> 2839.00]  I had to ask the question because somebody out there is like, what's wrong with multiple tabs?
[2839.50 --> 2841.76]  You mean like just your terminal has multiple tabs open?
[2842.16 --> 2843.14]  It's like a new tab.
[2843.22 --> 2844.18]  Yeah, a new tab, new.
[2844.66 --> 2845.14]  Yeah, exactly.
[2845.36 --> 2847.22]  Well, then you have to set that back up again later.
[2847.56 --> 2848.36]  So that's the reason.
[2848.44 --> 2849.90]  It's like the setup, the teardown.
[2849.96 --> 2854.74]  So let me give you an example that maybe would be enticing for you because you SSH into local boxes.
[2854.92 --> 2855.42]  Multiple machines.
[2855.68 --> 2856.66]  Yeah, exactly.
[2856.66 --> 2859.10]  So this is less of a problem as it used to be.
[2859.38 --> 2866.38]  But, you know, SSH sessions, which have not the best internet, like obviously on your LAN, you're going to have good connections all the time.
[2866.96 --> 2873.52]  But anytime you're like SSH into a remote server where you may hang, you may have an internet outage, you may lose that session.
[2873.84 --> 2875.14]  This starts with a good new screen.
[2875.24 --> 2875.82]  It goes way back.
[2875.92 --> 2878.38]  But Tmux has its functionality as well.
[2878.90 --> 2880.68]  What you can do is you can SSH in.
[2880.78 --> 2883.20]  You can start Tmux inside that remote machine.
[2883.20 --> 2887.98]  You can have multiple panes, multiple things, all the stuff you could have like with tabs on your own computer.
[2888.30 --> 2891.54]  But then you can also detach from that session and it stays running.
[2892.40 --> 2893.16]  And so you can set it up.
[2893.24 --> 2898.78]  So like if you accidentally close your laptop and you're like, dang, I had three tabs open SSH into this machine.
[2899.46 --> 2899.48]  Right.
[2899.48 --> 2901.06]  Moving files around, doing different stuff.
[2901.14 --> 2901.26]  Yeah.
[2901.38 --> 2907.28]  Now you basically just lost the connection to all that setup, which is still live on that remote server.
[2907.58 --> 2914.04]  So the next time you SSH in, you just tell Tmux to connect to that session you had going and everything magically back.
[2914.62 --> 2915.42]  So that's a big win.
[2915.86 --> 2916.02]  Yeah.
[2916.26 --> 2918.56]  And just expanding on like the magically back thing.
[2918.92 --> 2922.94]  So one interesting thing with Tmux is, you know, you can have multiple sessions and windows and panes and all of that.
[2923.44 --> 2928.32]  But by default, if you were to reboot your box and come back, like all of your Tmux state is going to be gone.
[2928.60 --> 2930.18]  You know, you have to like start from scratch there.
[2930.36 --> 2933.44]  But there's this really nice Tmux plugin called Tmux Resurrect.
[2933.64 --> 2935.44]  And I've been using this one for quite some time now.
[2935.82 --> 2937.98]  And now let's say you've got your Tmux set up however you want.
[2938.04 --> 2940.40]  You've got your 10 different sessions, all these windows laid out.
[2940.40 --> 2946.06]  And now you can just hit a hotkey, basically your Tmux leader key, control R or control S to save it actually.
[2946.34 --> 2949.60]  And it's going to save all of your sessions, windows and layouts to a text file.
[2949.86 --> 2950.74]  You don't need to think about it.
[2950.76 --> 2951.60]  You don't need to worry about it.
[2951.68 --> 2957.70]  And then when you reboot, all you have to do is just launch Tmux and then restore from your resurrected file another hotkey for that one.
[2957.98 --> 2960.78]  And everything is back to just how you left it to some degree.
[2960.78 --> 2965.58]  I say some degree because it's not going to like reopen every single application and put you exactly where you were.
[2965.78 --> 2970.34]  But at least all of your sessions and windows and certain applications like Vim can be auto started as well.
[2970.58 --> 2971.40]  So it's a nice one.
[2971.80 --> 2973.66]  But yeah, I've been using that one for a couple of years.
[2974.16 --> 2979.56]  Three years ago, you mentioned the save and restore Tmux sessions across reboots with Tmux resurrect.
[2980.56 --> 2981.54]  This is on your YouTube.
[2981.66 --> 2984.68]  I'm just thinking like, gosh, where could I dive deep into Tmux?
[2984.78 --> 2985.94]  Like where is the good primer?
[2986.38 --> 2988.30]  I mentioned I'm becoming a chef.
[2988.30 --> 2991.78]  I found some really awesome resources behind the scenes.
[2991.88 --> 2993.34]  I always have some sort of crazy hobby.
[2993.80 --> 2995.08]  And I'm actually getting really good at cooking.
[2995.36 --> 3000.34]  So good that I'm like now the cooker in our household because it's like such good food.
[3000.40 --> 3001.28]  And our kids love it.
[3001.80 --> 3002.88]  And I've been enjoying the process.
[3002.88 --> 3007.88]  But like I've found some really cool stuff to teach me the first principles of cooking.
[3008.08 --> 3012.16]  Not just how to make a meal, but like how do you sharpen your knives?
[3012.44 --> 3013.84]  What are the best ways to dice?
[3014.00 --> 3016.34]  What are the ways you should do different cheeses?
[3016.50 --> 3024.64]  How to, you know, do garlic and pull it off the clove and like make it a garlic clove that you can actually begin to slice, dice, mash, whatever.
[3025.24 --> 3027.40]  I'd like to have the same kind of idea for Tmux.
[3027.50 --> 3028.44]  Like help me, Nick.
[3028.78 --> 3033.06]  If you haven't already done this, maybe you have or point me to the YouTube videos and we'll put them in our show notes.
[3033.24 --> 3036.32]  But help me with a primer of like watching somebody.
[3036.42 --> 3040.08]  Because that's what I think I lack personally is I don't have a good buddy next to me.
[3040.52 --> 3049.84]  And ChatGPT does not have this function yet where it's like, hey, let me shadow you as a seasoned engineer that loves Tmux.
[3049.84 --> 3058.60]  Like if that, when that becomes a thing, that'd be kind of cool until then we've got the Knicks out there that have been slaying it on YouTube for years on this old hardware.
[3058.94 --> 3060.40]  Just, just killing it.
[3061.12 --> 3065.06]  Nick, surely you have a video about the fundamentals of Tmux or something like that, right?
[3065.20 --> 3073.02]  I don't have it like the exact fundamentals, like sharpening your knife level, but I do have like a use case based one to be like, this is how I use Tmux in my day to day.
[3073.04 --> 3076.90]  And it kind of demonstrates using, you know, the panes and the windows and sessions and Tmux resurrect.
[3076.90 --> 3081.26]  And it's like, you know, like an eight minute video or something was from maybe five years ago.
[3081.38 --> 3086.12]  But it's interesting because I would be curious to see if Adam can Google for that topic.
[3086.28 --> 3089.48]  And if my site or page doesn't come up, then there's a problem.
[3089.82 --> 3090.38]  What's that search?
[3090.52 --> 3091.10]  Tell me the search.
[3091.16 --> 3091.96]  I'll put it in right now.
[3092.24 --> 3093.36]  Well, that would be cheating.
[3093.52 --> 3094.30]  I want you to try.
[3094.68 --> 3100.96]  Well, just give me a couple of, like getting started with Tmux.
[3101.26 --> 3101.62]  Boom.
[3101.84 --> 3102.38]  Let's see what's there.
[3103.10 --> 3103.46]  Wow.
[3103.62 --> 3104.58]  Red had his first.
[3105.78 --> 3106.70]  GitHub, Tmux.
[3106.70 --> 3107.60]  Tmux is there.
[3107.76 --> 3108.18]  The wiki.
[3108.98 --> 3110.08]  LinuxEyes.
[3111.00 --> 3111.40]  Hamvaki.
[3112.64 --> 3113.88]  Linux Training Academy.
[3114.24 --> 3115.52]  Hacker News Post.
[3116.58 --> 3117.76]  Pragmatic Pineapple.
[3117.92 --> 3118.40]  Hostinger.
[3118.56 --> 3118.74]  Wow.
[3118.82 --> 3120.50]  Hostinger's got some content out there on Tmux.
[3120.88 --> 3121.32]  It's ranking.
[3122.18 --> 3122.62]  Sorry, Nick.
[3122.66 --> 3123.04]  You're losing.
[3124.00 --> 3124.60]  Let's see.
[3124.62 --> 3125.24]  I'm losing back.
[3125.62 --> 3127.06]  Shane Lee on YouTube.
[3127.26 --> 3128.50]  Now, I didn't search YouTube, though.
[3128.60 --> 3131.82]  Let me take the same search and apply it to YouTube.
[3132.24 --> 3135.32]  Well, the funny thing is I don't even actually know the titles of those posts because they're from
[3135.32 --> 3136.36]  some so long ago.
[3136.66 --> 3139.76]  That's okay because here, this is probably a great example.
[3140.68 --> 3145.10]  So, Network Chuck obviously is first because he's just, he kills it on all content.
[3145.64 --> 3147.54]  This is something you need to know right now.
[3147.66 --> 3149.96]  It's always right now in all caps with exclamation points.
[3150.06 --> 3151.06]  I'm like, please.
[3151.20 --> 3152.06]  That's an old title.
[3152.22 --> 3152.70]  Let it go.
[3153.70 --> 3154.92]  Let's see if Nick is in the scroll.
[3155.32 --> 3157.58]  Learn Linux TV is in the scroll.
[3157.58 --> 3161.52]  Dreams of Code is in the scroll.
[3161.68 --> 3163.76]  You're just getting a different kind of slayed here.
[3163.92 --> 3165.66]  He was slaying it earlier and now he's getting slayed.
[3165.74 --> 3166.86]  So, Primogen is there.
[3167.20 --> 3168.12]  Theo is there.
[3168.68 --> 3170.10]  Warp.dev is there.
[3170.92 --> 3172.44]  Shane Lee is there again.
[3172.88 --> 3173.72]  Where is Nick?
[3173.84 --> 3175.76]  Nick, oh, where are you on your old hardware?
[3177.52 --> 3177.94]  Gosh.
[3178.26 --> 3181.46]  I do not see Nick in the initial page scroll.
[3181.86 --> 3182.10]  Okay.
[3182.26 --> 3183.58]  I think I discovered why.
[3183.86 --> 3188.92]  Because I'm looking at this post now and the title is so, this is a great aside in just
[3188.92 --> 3193.92]  how important naming your titles are because my title is using Tmux sessions, windows, panes
[3193.92 --> 3195.24]  and Vim buffers together.
[3195.54 --> 3196.14]  Oh yeah.
[3196.16 --> 3197.44]  That's pretty specific on.
[3197.88 --> 3200.92]  But the, but the, but the atoms of the world aren't starting to be like, oh, how do I use
[3200.92 --> 3201.54]  a window and a pane?
[3201.54 --> 3204.10]  It's like, you don't even know what those terms might be if you're just getting started.
[3204.52 --> 3205.44]  Teach me Tmux.
[3206.08 --> 3207.18]  Getting started with Tmux.
[3207.30 --> 3208.14]  Tmux for beginners.
[3208.74 --> 3208.96]  Right.
[3209.12 --> 3210.34]  Why should I use Tmux?
[3210.34 --> 3212.84]  Tmux, all those Tmux phrases.
[3213.26 --> 3213.90]  Yeah, I agree.
[3213.98 --> 3216.52]  You have to think, this is part of user experience though.
[3216.76 --> 3217.84]  This is part of product development.
[3217.98 --> 3219.26]  This is the problem of all products.
[3219.38 --> 3224.84]  It's the problem of all, I guess, startups really is like, how do you capture the attention?
[3225.58 --> 3227.10]  Well, you have to think like the user.
[3227.26 --> 3228.50]  You have to talk to some people.
[3228.56 --> 3229.54]  You have to go on some podcast.
[3229.64 --> 3229.98]  You're doing that.
[3230.02 --> 3230.16]  Great.
[3230.20 --> 3230.56]  No problem.
[3230.64 --> 3231.02]  Good job.
[3231.60 --> 3235.80]  But you have to title and think like, and Jared and I, maybe we don't do this very well,
[3235.84 --> 3235.94]  right?
[3235.98 --> 3236.82]  Do we do this very well?
[3236.94 --> 3237.20]  No.
[3237.36 --> 3239.22]  We're not a great example of titling well.
[3239.22 --> 3240.60]  We enjoy our titles.
[3240.74 --> 3242.02]  This is for the love of titling.
[3242.18 --> 3245.12]  We don't title for that purpose, which is why no one finds us.
[3245.52 --> 3245.70]  Yeah.
[3246.64 --> 3249.92]  No one finds us for other reasons, Nick, but we're okay with that, I guess.
[3250.42 --> 3251.24]  So I found it.
[3251.32 --> 3255.00]  I found another post from 2017, which is, this is more of a getting started guide.
[3255.00 --> 3256.46]  Like it walks you through the basics and everything.
[3256.62 --> 3260.94]  There's no video for that one, but this one is who else wants to boost their terminal productivity
[3260.94 --> 3266.38]  with Tmux, which is maybe closer, but still way off the radar of what a human being would
[3266.38 --> 3266.80]  search for.
[3267.24 --> 3267.46]  Right.
[3267.96 --> 3269.74]  Boost your terminal productivity.
[3270.16 --> 3276.32]  I bet you, if you took an exercise and went back and retitled some of your videos, I'm not
[3276.32 --> 3278.66]  even sure how you can like optimize your YouTube.
[3278.66 --> 3285.90]  But my assumption is if you can go back and revisit, either go back and update or revisit
[3285.90 --> 3290.86]  some of these topics and create brand new content that is better titled and more focused,
[3291.06 --> 3296.76]  shorter form, more focused, compartmentalized, time to content is super crucial.
[3296.90 --> 3297.64]  No meandering.
[3298.06 --> 3301.04]  Get to the point and then make it a series.
[3301.60 --> 3302.54]  I bet you.
[3302.76 --> 3303.38]  No meandering.
[3303.56 --> 3304.48]  We're an hour in.
[3304.52 --> 3305.50]  We haven't talked to you yet.
[3305.50 --> 3305.66]  Yeah.
[3308.54 --> 3309.74]  Well, let's talk about a 2-E.
[3310.32 --> 3311.42]  Oh, love it.
[3311.46 --> 3312.38]  I got one open right now.
[3312.46 --> 3312.48]  All right.
[3312.48 --> 3313.30]  Let's hear it.
[3313.94 --> 3316.88]  So, Nick, on your list, you had H-Top, which I'm a fan of H-Top.
[3317.06 --> 3323.68]  And Jerry, I think we had the prior core committer of H-Top on the show way back in the day
[3323.68 --> 3324.52]  when it got, yeah.
[3325.22 --> 3327.66]  I have here in front of me, Bash Top.
[3327.86 --> 3328.48]  Bash Top.
[3328.64 --> 3329.16]  Bash Top.
[3329.16 --> 3334.46]  And I think it's kind of cool because the installation process is pretty easy.
[3334.46 --> 3338.06]  One thing it asks you to do is to do the apt.
[3338.46 --> 3341.36]  Sorry, I'm on Ubuntu, so at least my process is this.
[3341.96 --> 3343.44]  And your mileage may vary wherever you're at.
[3343.58 --> 3350.44]  But it's on Ubuntu, you add the apt repository via this thing I believe is called PPA.
[3351.40 --> 3355.90]  That stands for, Nick, help me out here, Personal Package Archive.
[3355.90 --> 3363.82]  And essentially, you're adding bash top dash monitor slash bash top as an apt repository.
[3363.96 --> 3368.06]  So, you can apt update and just do sudo apt install bash top.
[3368.16 --> 3369.06]  And then it installs.
[3369.36 --> 3375.56]  It installs things like Libs Sensors, Python 3, Utilities if you don't have them in there,
[3375.72 --> 3376.90]  Systat and a couple others.
[3376.90 --> 3383.06]  And then once you get it there, you just simply type bash, B-A-S-H-T-O-P.
[3383.72 --> 3385.58]  And boom, you've got this beautiful thing.
[3386.20 --> 3390.42]  What I like most about it is that it's got super awesome configuration theming.
[3390.84 --> 3393.04]  You can do a bunch of different changes to it.
[3393.58 --> 3398.58]  And one thing I don't like personally and why I prefer this over H-Top now is,
[3398.74 --> 3399.64]  one, it's slightly more beautiful.
[3399.64 --> 3405.40]  And then two, I just hate how challenging it is to configure H-Top.
[3405.80 --> 3408.52]  The configuration file is not meant to be edited by the human.
[3408.88 --> 3410.86]  It's only via the interface.
[3411.18 --> 3415.40]  And I find the interface kind of kludgy to fine-tune where things are at.
[3415.86 --> 3419.56]  Whereas bash top seems to be a bit more just, I guess,
[3419.64 --> 3422.06]  human-friendly on configuration management with it.
[3422.34 --> 3422.50]  Okay.
[3422.80 --> 3423.54]  I'll have to check it out.
[3423.60 --> 3425.66]  Yeah, it's interesting because with H-Top,
[3425.82 --> 3428.00]  you know, it's a tool I've also been using for a really long time.
[3428.00 --> 3431.06]  But usually I'm reaching for it very occasionally.
[3431.46 --> 3435.28]  You know, it's like on my really, really nice work machine now,
[3435.34 --> 3438.42]  if I want to see if my CPU cores are pegged, all four of them, by the way,
[3438.48 --> 3441.10]  you know, I can run an H-Top and just see those little bars to be like,
[3441.18 --> 3442.52]  oh, well, three CPUs are maxed out.
[3442.58 --> 3443.72]  The fourth one's still doing good.
[3443.74 --> 3446.76]  Or, you know, maybe I just want to see like what is using the most memory
[3446.76 --> 3447.74]  out of a list of processes.
[3448.10 --> 3450.40]  So it's interesting that you mentioned like configurability.
[3450.52 --> 3453.38]  Like in my mind, like I would want to configure like nice themes
[3453.38 --> 3454.28]  with T-Mocs and everything.
[3454.48 --> 3457.46]  But like an H-Top, it didn't even ever cross my mind once
[3457.46 --> 3460.14]  to like jump into its config to like tweak it out.
[3460.46 --> 3460.54]  Yeah.
[3460.58 --> 3462.94]  Just because it's like usually I'm going in very specific thing
[3462.94 --> 3465.28]  and then like exiting out 20 seconds later.
[3465.56 --> 3466.40]  Well, let me explain to you.
[3466.44 --> 3471.20]  So then on my, I like to, I guess the one thing I do
[3471.20 --> 3475.50]  that makes me pay attention to those, I guess, metrics
[3475.50 --> 3480.78]  more so than anybody else is I wanted to monitor my Plex box
[3480.78 --> 3486.48]  for how well it's using the RAM or the CPU during like maybe a 4K movie transcode,
[3486.56 --> 3486.98]  for example.
[3487.76 --> 3493.82]  Or on the TrueNAS box, I want to pay attention because we compress our archives
[3493.82 --> 3496.74]  and put them into a file package called 7z.
[3497.34 --> 3498.12]  And I max it out.
[3498.12 --> 3500.26]  I push the compression algorithm to the max.
[3500.90 --> 3507.82]  And so whenever I archive these things, it pegs my M1 max CPU 100%
[3507.82 --> 3513.68]  and takes the temperature to almost 200 degrees Fahrenheit for five minutes.
[3513.86 --> 3514.58]  And then it's done.
[3515.36 --> 3516.56]  But it's kind of fun to watch that.
[3516.64 --> 3517.26]  It's just kind of fun.
[3517.34 --> 3520.38]  Like you're really pushing this beefy machine.
[3521.04 --> 3522.66]  And damn it, I want to see what's going on here.
[3522.80 --> 3525.62]  You know, I want to H-Top up in there or my new case, Bash Top.
[3525.62 --> 3529.62]  And so the one thing I do specifically on these kind of boxes
[3529.62 --> 3532.52]  is I want to have my CPU stacked.
[3532.64 --> 3533.84]  I want to have them organized.
[3534.38 --> 3535.90]  I want to have my host name there.
[3535.94 --> 3536.84]  I want to have my uptime.
[3537.16 --> 3540.56]  I want to have my average CPU, my memory, my swap.
[3540.68 --> 3541.66]  I want these things there.
[3541.74 --> 3542.60]  I want network there.
[3542.80 --> 3544.06]  I want disk IO there.
[3544.32 --> 3546.44]  And if this system happens to have ZFS,
[3547.14 --> 3550.46]  H-Top thankfully has this other cool line item you can put in there
[3550.46 --> 3552.78]  for ZFS arc management
[3552.78 --> 3555.56]  and just kind of knowing how your ZFS file system is working.
[3556.18 --> 3557.36]  So I appreciate that about that.
[3557.40 --> 3559.32]  But for every time I've got to instantiate
[3559.32 --> 3561.44]  a new machine with new H-Top,
[3561.92 --> 3564.32]  it's not like one config that I can just move over
[3564.32 --> 3567.54]  from a Git repository or a copy paste.
[3567.84 --> 3569.98]  It is literally a file you should not edit.
[3570.12 --> 3571.16]  I think they even tell you that.
[3571.36 --> 3572.38]  And from system to system,
[3572.38 --> 3573.90]  I tried to see if like it made sense.
[3574.24 --> 3576.30]  There's no rhyme or reason to this config file.
[3576.84 --> 3578.18]  So every time I do it,
[3578.22 --> 3580.58]  I have to do this brand new setup,
[3580.80 --> 3582.10]  which is not too frequent,
[3582.20 --> 3583.46]  but it's enough that I'm like, forget it.
[3583.46 --> 3584.36]  I don't want to do this anymore,
[3584.36 --> 3586.74]  but I do keep doing it because it has been the best.
[3587.36 --> 3588.66]  But now I'm looking at Bash Top.
[3588.74 --> 3590.28]  It's not won for me yet.
[3590.34 --> 3592.46]  It's still runner up and it's still winning
[3592.46 --> 3594.28]  or at least trying to win.
[3594.42 --> 3596.34]  So I haven't fully adopted Bash Top,
[3596.44 --> 3599.36]  but I'm thinking that it might be a long-term better solution.
[3599.92 --> 3600.38]  That makes sense.
[3600.46 --> 3601.70]  And it's a great aside too,
[3601.76 --> 3605.18]  just around like being really engulfed in your environment, right?
[3605.24 --> 3606.80]  You mentioned you're running Ubuntu there.
[3606.98 --> 3608.70]  So I would imagine you'd be using Bash Top
[3608.70 --> 3611.14]  as like your full-blown like system monitoring tool,
[3611.26 --> 3612.66]  like an activity monitor or whatever.
[3612.92 --> 3614.08]  Whereas me with H Top,
[3614.38 --> 3616.36]  you know, I am still running Windows with WSL,
[3616.66 --> 3619.18]  but like I would just probably just open Windows as,
[3619.30 --> 3621.34]  you know, like task manager to see that information.
[3621.54 --> 3623.32]  Whereas for you, like you're using that one tool.
[3623.42 --> 3624.58]  So you want that one tool to be like,
[3624.62 --> 3626.22]  yeah, I want to see network and CPU and all that,
[3626.42 --> 3627.42]  have it laid out the way I want
[3627.42 --> 3628.24]  so I don't need to tweak it.
[3628.70 --> 3629.76]  That makes total sense.
[3630.26 --> 3631.28]  Not to go one layer deeper,
[3631.40 --> 3633.32]  but there might be somebody out there saying,
[3633.46 --> 3634.48]  but what about BTop?
[3634.48 --> 3635.68]  I agree.
[3636.00 --> 3636.86]  BTop is awesome.
[3637.42 --> 3639.56]  Except for Bash Top has more letters
[3639.56 --> 3640.72]  and it's slightly more awesome.
[3641.28 --> 3641.68]  There you go.
[3643.14 --> 3645.80]  Well, I was just reading about BTop++.
[3646.72 --> 3647.70]  Oh, nice.
[3647.76 --> 3648.40]  Have you heard of this?
[3649.06 --> 3649.40]  No.
[3649.60 --> 3649.88]  Did they?
[3650.28 --> 3650.56]  Nope.
[3650.76 --> 3651.88]  They like to increment like us.
[3651.94 --> 3652.16]  Yeah.
[3652.24 --> 3653.12]  I mean, I assume it's better
[3653.12 --> 3654.34]  because that's what the++ means.
[3654.44 --> 3654.96]  It is better.
[3655.24 --> 3655.76]  It is.
[3655.84 --> 3656.78]  It's been better for years.
[3657.02 --> 3657.98]  It's by the same author.
[3658.42 --> 3660.30]  Bash Top in C++.
[3660.60 --> 3663.26]  So Bash Top is written in pretty much Bash.
[3663.26 --> 3664.90]  I don't know if that surprises you,
[3665.02 --> 3667.00]  but it's 94% shell scripts,
[3667.08 --> 3668.30]  which I assume is Bash.
[3668.36 --> 3669.46]  Must be tough to maintain.
[3669.92 --> 3670.30]  Yeah.
[3670.50 --> 3672.32]  And now there's a BTop++
[3672.32 --> 3675.92]  is a C++ version of Bash Top.
[3676.18 --> 3678.50]  Now, switching from something to C++
[3678.50 --> 3680.58]  doesn't automatically make it better.
[3680.84 --> 3682.76]  I mean, I've heard that maybe C
[3682.76 --> 3684.84]  in certain ways is even better than C++.
[3685.12 --> 3687.76]  But one thing I'll notice about the GitHub
[3687.76 --> 3691.52]  is that Bash Top's last commit was two years ago,
[3691.52 --> 3696.26]  whereas BTop++ was committed to three weeks ago.
[3696.40 --> 3697.94]  So it seems like the author of Bash Top
[3697.94 --> 3702.88]  has switched their focus over to BTop++.
[3703.62 --> 3704.78]  So maybe give that one a look.
[3704.94 --> 3706.12]  So I saw a release.
[3706.20 --> 3707.80]  I thought I saw a release on Bash Top
[3707.80 --> 3708.50]  that made me think,
[3708.60 --> 3709.52]  okay, this is kind of cool.
[3709.72 --> 3710.94]  And now I'm not seeing it.
[3711.12 --> 3712.48]  There are no releases for it.
[3713.32 --> 3713.92]  Dang it.
[3714.08 --> 3714.52]  It's all right.
[3714.86 --> 3716.02]  This is dated software?
[3716.58 --> 3718.18]  I'm pimping dated software?
[3718.28 --> 3719.00]  What's wrong with me?
[3719.00 --> 3720.82]  Hey, some old software is just good.
[3721.00 --> 3721.60]  Okay, fine.
[3721.64 --> 3721.94]  You're right.
[3722.02 --> 3722.84]  I mean, how old is Tmux?
[3723.26 --> 3724.40]  But if the, if the,
[3724.52 --> 3727.34]  so this is a case where it would be
[3727.34 --> 3730.68]  to find these tools out there on GitHub.
[3731.20 --> 3732.34]  Sure, there's a username there.
[3732.40 --> 3734.06]  I could probably pay attention to the user
[3734.06 --> 3735.78]  who's actually making this software
[3735.78 --> 3736.36]  and see if they-
[3736.36 --> 3736.82]  The human?
[3737.00 --> 3738.94]  The actual human that's writing your software for you
[3738.94 --> 3740.08]  and giving it to you as a gift?
[3740.20 --> 3740.64]  That's right.
[3740.74 --> 3741.48]  I should, you know,
[3742.00 --> 3744.08]  this free USB stick at the front of their lawn,
[3744.16 --> 3744.64]  I just, you know,
[3744.64 --> 3745.84]  I just run by and steal it.
[3745.84 --> 3746.00]  Right.
[3746.38 --> 3746.96]  Yet it's free.
[3746.96 --> 3749.24]  Well, I think there's a dot connector
[3749.24 --> 3749.90]  that you've done
[3749.90 --> 3751.32]  that I did not do yet
[3751.32 --> 3752.44]  between the two,
[3752.54 --> 3753.52]  which is if it's the same
[3753.52 --> 3755.38]  original maintainer slash author
[3755.38 --> 3756.34]  of the software,
[3756.76 --> 3757.74]  have they moved on?
[3758.20 --> 3759.44]  Which it seems like they've moved on.
[3760.06 --> 3760.70]  Oh, man.
[3760.92 --> 3761.42]  That's all right.
[3761.90 --> 3763.46]  So I should be using Btop++.
[3763.60 --> 3764.70]  I don't know if it's actually better.
[3764.90 --> 3765.98]  I mean, it's not Changelog++,
[3766.20 --> 3767.16]  which we know is better.
[3767.38 --> 3767.64]  All right.
[3767.66 --> 3768.24]  But it might be.
[3768.58 --> 3769.46]  And I know that the author
[3769.46 --> 3770.26]  is still working on it.
[3770.32 --> 3771.56]  So maybe, you know,
[3771.58 --> 3772.24]  the big rewrite,
[3772.40 --> 3773.18]  sometimes it takes a while
[3773.18 --> 3774.20]  to come up to feature parity.
[3774.30 --> 3775.66]  It may actually be worse for a while,
[3775.66 --> 3777.16]  but have a better foundation.
[3777.78 --> 3779.32]  I am not a user of this tool,
[3779.42 --> 3780.78]  so I have no idea about the history.
[3781.22 --> 3782.58]  But let's get them on the pod.
[3782.68 --> 3783.52]  Let's talk about it.
[3783.74 --> 3785.72]  So it seems like slash Btop
[3785.72 --> 3787.00]  is now just Btop++.
[3787.32 --> 3788.38]  Did they just change it then?
[3788.78 --> 3789.48]  This I don't know.
[3789.86 --> 3790.16]  Okay.
[3790.40 --> 3791.74]  So it's the same.
[3791.82 --> 3792.68]  I've been doing my research
[3792.68 --> 3793.44]  while you've been talking.
[3793.62 --> 3795.08]  So I'm very shallow at this point.
[3795.56 --> 3796.10]  You actually reached
[3796.10 --> 3796.84]  the end of my knowledge.
[3796.90 --> 3798.16]  The person's name is Jacob.
[3798.62 --> 3799.78]  Don't know how to say your last name.
[3800.56 --> 3801.30]  We're going to reach out.
[3801.80 --> 3802.26]  There you go.
[3802.26 --> 3803.54]  It is interesting
[3803.54 --> 3804.84]  how fast developers
[3804.84 --> 3806.16]  will just like throw away
[3806.16 --> 3807.00]  a project they love
[3807.00 --> 3808.20]  just because it hasn't been touched
[3808.20 --> 3809.32]  in like 11 seconds.
[3809.54 --> 3809.70]  Right.
[3810.14 --> 3810.64]  Adam's like,
[3810.72 --> 3811.04]  you know what?
[3811.10 --> 3812.00]  Btop sucks.
[3812.14 --> 3812.98]  Or Vashtop sucks.
[3814.62 --> 3816.76]  Well, maybe Btop has the same principles.
[3817.10 --> 3817.72]  Well, it's right.
[3817.86 --> 3819.44]  It's literally the same person.
[3819.46 --> 3820.62]  So I assume it's like
[3820.62 --> 3821.72]  the successor
[3821.72 --> 3823.00]  to the tool you already love.
[3823.28 --> 3824.40]  And so check it out.
[3824.48 --> 3825.42]  And nobody wants to buy
[3825.42 --> 3826.28]  last year's product
[3826.28 --> 3826.80]  at the New Year.
[3826.92 --> 3827.78]  You know, this product
[3827.78 --> 3828.30]  for this year.
[3828.36 --> 3828.82]  Nick does.
[3828.94 --> 3830.46]  I mean, his PC is 10 years old, man.
[3830.46 --> 3831.00]  That's true.
[3831.24 --> 3831.58]  Gosh.
[3832.26 --> 3832.74]  All right, Nick.
[3832.82 --> 3834.22]  School us on going old.
[3835.66 --> 3836.32]  Staying old.
[3836.82 --> 3837.18]  Legacy.
[3837.48 --> 3837.88]  There we go.
[3838.28 --> 3838.88]  It's actually funny.
[3838.96 --> 3839.72]  You know, we're now like
[3839.72 --> 3840.64]  however long it's been
[3840.64 --> 3841.68]  on the whole entire show.
[3841.72 --> 3842.72]  But have we even defined
[3842.72 --> 3844.36]  like what makes something
[3844.36 --> 3845.08]  a TUI
[3845.08 --> 3846.28]  versus just a regular
[3846.28 --> 3847.40]  command line tool?
[3847.72 --> 3848.48]  Great job, Nick.
[3848.50 --> 3849.34]  You should be a podcaster.
[3850.18 --> 3850.54]  Tell us.
[3850.60 --> 3850.78]  Maybe.
[3851.12 --> 3851.44]  One day.
[3851.62 --> 3853.00]  Do you have a definition?
[3853.28 --> 3853.96]  Do you have an idea?
[3854.10 --> 3855.18]  Do you want to hypothesize?
[3855.40 --> 3856.42]  Well, okay.
[3856.74 --> 3858.28]  Let's go zero research
[3858.28 --> 3859.02]  top of my head.
[3859.02 --> 3859.72]  I mean, I would say
[3859.72 --> 3861.76]  a tool like grep, sed, cut, etc.
[3862.20 --> 3863.36]  You know, this is a command line tool
[3863.36 --> 3864.28]  typically that you'd run.
[3864.44 --> 3865.52]  You provide it some inputs.
[3865.64 --> 3866.74]  It will provide some outputs.
[3866.98 --> 3867.44]  And, you know,
[3867.46 --> 3868.32]  the output that you get
[3868.32 --> 3868.92]  on your screen,
[3869.06 --> 3870.44]  it's almost like a transaction,
[3870.60 --> 3871.76]  almost like an HTTP request.
[3871.86 --> 3872.46]  Like your request
[3872.46 --> 3873.20]  is calling the command.
[3873.42 --> 3874.40]  The response you get back
[3874.40 --> 3875.12]  is what you get back
[3875.12 --> 3875.90]  in the output there.
[3876.12 --> 3876.68]  And it could be like
[3876.68 --> 3877.76]  an image net.
[3877.86 --> 3878.56]  You know, if you're dealing
[3878.56 --> 3879.80]  with like an image manipulation tool,
[3879.92 --> 3880.84]  it doesn't need to be taxed.
[3880.98 --> 3881.78]  But like a TUI,
[3881.96 --> 3882.52]  to me at least,
[3882.58 --> 3883.54]  it's like something
[3883.54 --> 3884.74]  that's like just running.
[3884.92 --> 3885.52]  You know, it's like,
[3885.52 --> 3886.50]  like HTAP,
[3886.56 --> 3887.20]  like it's just running
[3887.20 --> 3888.28]  and you can interact with it.
[3888.32 --> 3889.24]  You're still sending it inputs.
[3889.30 --> 3890.12]  You're still getting outputs,
[3890.12 --> 3890.84]  but you're kind of getting
[3890.84 --> 3891.66]  these little, you know,
[3891.72 --> 3892.50]  incremental updates
[3892.50 --> 3893.68]  on the screen somewhere.
[3893.94 --> 3894.72]  Like in your case,
[3894.76 --> 3895.94]  like a CPU graph
[3895.94 --> 3896.74]  or something like that.
[3896.98 --> 3898.48]  So, yeah, I don't know.
[3898.50 --> 3898.96]  In a weird way,
[3899.00 --> 3899.50]  if you're going to follow
[3899.50 --> 3900.92]  that HTTP like analogy
[3900.92 --> 3901.38]  or something,
[3901.38 --> 3901.92]  it's almost like
[3901.92 --> 3902.84]  a WebSocket connection
[3902.84 --> 3903.54]  where like that connection
[3903.54 --> 3904.28]  is like staying open
[3904.28 --> 3904.74]  and then it's like
[3904.74 --> 3905.48]  broadcasting things
[3905.48 --> 3906.08]  back and forth.
[3906.36 --> 3906.82]  Or, you know,
[3906.88 --> 3907.76]  one way works as well.
[3908.02 --> 3908.44]  But I don't know.
[3908.48 --> 3908.98]  Do you guys have like
[3908.98 --> 3910.12]  a different definition of that?
[3910.70 --> 3911.26]  I think mine is
[3911.26 --> 3912.42]  slightly more simple.
[3912.74 --> 3913.46]  I would say I think
[3913.46 --> 3915.54]  a TUI is more application-like.
[3916.34 --> 3917.42]  Whereas you open it
[3917.42 --> 3918.64]  and you have a brand new
[3918.64 --> 3921.00]  probably bespoke interface
[3921.00 --> 3922.28]  that's specific to
[3922.28 --> 3923.18]  its function.
[3923.90 --> 3925.30]  Whereas those tools
[3925.30 --> 3925.98]  or utilities
[3925.98 --> 3926.56]  where you're sort of
[3926.56 --> 3927.32]  passing things around
[3927.32 --> 3928.16]  on the command line,
[3928.76 --> 3930.84]  they're not meant to be TUIs.
[3931.66 --> 3932.64]  What does TUIs stand for,
[3932.72 --> 3933.02]  Jared, again?
[3933.30 --> 3935.14]  Text-based user interface.
[3935.28 --> 3935.68]  There you go.
[3935.70 --> 3936.30]  I thought so.
[3936.80 --> 3938.56]  Not terminal user interface,
[3938.72 --> 3939.22]  text-based.
[3939.40 --> 3939.84]  Not necessarily.
[3939.84 --> 3941.02]  User interface.
[3941.72 --> 3942.64]  So I think they literally
[3942.64 --> 3943.60]  are a UI
[3943.60 --> 3945.04]  to a particular application.
[3945.18 --> 3945.86]  So I think they
[3945.86 --> 3947.28]  probably get started
[3947.28 --> 3948.64]  like a bash top
[3948.64 --> 3949.28]  or a btop
[3949.28 --> 3949.84]  or an htop.
[3949.92 --> 3951.10]  You just invoke the command
[3951.10 --> 3953.00]  and it runs this application
[3953.00 --> 3954.52]  that has a particular UI
[3954.52 --> 3955.78]  that matches
[3955.78 --> 3957.34]  whatever its function is.
[3957.42 --> 3958.66]  Whether it's a
[3958.66 --> 3959.52]  markdown reader
[3959.52 --> 3960.86]  for readmes
[3960.86 --> 3962.10]  or an editor.
[3962.90 --> 3964.00]  Vim is kind of like
[3964.00 --> 3964.46]  a TUI, right?
[3964.48 --> 3964.80]  It's kind of like
[3964.80 --> 3965.56]  an application.
[3965.84 --> 3966.18]  For sure.
[3966.52 --> 3966.78]  Right?
[3966.90 --> 3967.62]  It's kind of a TUI.
[3967.68 --> 3967.90]  For sure.
[3967.98 --> 3968.64]  Well, if you run it
[3968.64 --> 3969.14]  in the terminal,
[3969.14 --> 3970.62]  where else would you run it?
[3971.30 --> 3972.34]  There's Vim GUIs.
[3972.66 --> 3973.68]  I don't know about those.
[3973.68 --> 3974.04]  In fact,
[3974.16 --> 3975.40]  Chris Brando got in trouble
[3975.40 --> 3976.70]  because one of his
[3976.70 --> 3978.06]  recent unpopular opinions
[3978.06 --> 3979.66]  was you should learn
[3979.66 --> 3980.88]  a text-based editor
[3980.88 --> 3982.42]  like Vim or Emacs.
[3982.66 --> 3983.22]  And of course,
[3984.06 --> 3984.90]  the nerds came out
[3984.90 --> 3985.60]  of the woodwork
[3985.60 --> 3986.08]  and said,
[3986.66 --> 3988.02]  Emacs is not necessarily
[3988.02 --> 3989.66]  a text-based editor.
[3990.04 --> 3990.20]  Sure,
[3990.34 --> 3991.08]  you can use it
[3991.08 --> 3992.38]  inside a terminal,
[3992.74 --> 3993.92]  but Emacs is so much more
[3993.92 --> 3995.22]  than just a text-based editor.
[3995.22 --> 3995.66]  And of course,
[3996.14 --> 3997.50]  there are GUIs for Vim.
[3997.70 --> 3997.92]  Okay.
[3998.20 --> 3998.70]  But yes,
[3998.82 --> 4000.26]  Vim in your terminal
[4000.26 --> 4001.78]  would be a TUI,
[4002.00 --> 4002.48]  wouldn't it, Nick?
[4002.76 --> 4003.06]  Yeah,
[4003.18 --> 4003.80]  I would agree with that.
[4004.22 --> 4004.62]  So yeah,
[4004.66 --> 4005.36]  I think Nick's on point.
[4005.42 --> 4006.08]  I think Adam's on point.
[4006.20 --> 4007.42]  I think the point is
[4007.42 --> 4009.24]  statelessness versus statefulness.
[4009.50 --> 4010.70]  Nick's was more scientific,
[4010.86 --> 4011.04]  though.
[4011.46 --> 4012.48]  He was like a scholar
[4012.48 --> 4013.54]  laying out there
[4013.54 --> 4014.30]  what TUIs are.
[4014.74 --> 4015.28]  I was like a layman.
[4015.28 --> 4016.12]  He's off the top of his head.
[4016.16 --> 4016.76]  He's just scholarly.
[4017.60 --> 4017.80]  Yeah.
[4017.88 --> 4018.10]  Well,
[4018.10 --> 4019.44]  he's being very technical
[4019.44 --> 4020.00]  and pedantic,
[4020.10 --> 4021.32]  as we would expect us to be.
[4022.18 --> 4023.34]  And I think he's right.
[4023.42 --> 4024.58]  I think the statefulness
[4024.58 --> 4025.54]  is the point,
[4025.66 --> 4025.82]  right?
[4025.86 --> 4027.52]  Like a command
[4027.52 --> 4028.86]  or utility,
[4029.00 --> 4029.44]  as you called it,
[4029.48 --> 4029.72]  Adam,
[4030.58 --> 4031.54]  from the command line
[4031.54 --> 4033.90]  is a single transaction,
[4034.06 --> 4034.48]  like Nick said.
[4034.56 --> 4035.86]  Like you run the command,
[4036.04 --> 4036.92]  it does some stuff,
[4037.40 --> 4038.38]  it outputs some stuff.
[4038.46 --> 4039.34]  Maybe it outputs nothing,
[4039.72 --> 4040.58]  as it should,
[4040.64 --> 4041.66]  if everything goes correctly
[4041.66 --> 4042.48]  and has no output.
[4043.28 --> 4045.18]  Whereas a TUI
[4045.18 --> 4046.54]  has state.
[4047.14 --> 4047.84]  You launch it,
[4048.34 --> 4049.36]  it goes through time,
[4049.36 --> 4051.84]  things change on it
[4051.84 --> 4052.46]  as it runs
[4052.46 --> 4053.58]  and then you exit it.
[4053.92 --> 4054.28]  And so,
[4054.66 --> 4055.58]  I think that's pretty much
[4055.58 --> 4056.14]  the difference.
[4056.30 --> 4056.92]  I would probably say
[4056.92 --> 4058.38]  they're themable as well.
[4058.46 --> 4058.54]  I mean,
[4058.56 --> 4059.32]  there's an interface
[4059.32 --> 4060.38]  that you care about.
[4060.62 --> 4060.88]  Themable,
[4061.02 --> 4061.18]  I think,
[4061.22 --> 4061.68]  is a feature
[4061.68 --> 4063.06]  that you would want
[4063.06 --> 4063.52]  in a TUI,
[4063.60 --> 4064.34]  but not necessarily.
[4064.76 --> 4065.74]  A desirable feature,
[4065.78 --> 4066.10]  I would say,
[4066.16 --> 4066.72]  for me at least.
[4066.78 --> 4067.34]  I want to theme
[4067.34 --> 4068.28]  everything Dracula.
[4068.66 --> 4068.82]  You know,
[4068.86 --> 4069.60]  if it's not Dracula,
[4069.76 --> 4070.78]  just throw it in the trash.
[4071.22 --> 4072.30]  Let me introduce you
[4072.30 --> 4073.78]  to a new
[4073.78 --> 4075.98]  text-based user interface
[4075.98 --> 4078.66]  for HTTP requests.
[4078.66 --> 4079.92]  This actually kind of
[4079.92 --> 4080.98]  inspired this episode
[4080.98 --> 4082.88]  because I just thought
[4082.88 --> 4083.66]  this was so cool.
[4083.88 --> 4084.78]  I want to talk about it more.
[4084.86 --> 4085.96]  I put it in news on Monday.
[4086.52 --> 4087.46]  It's called Posting.
[4088.12 --> 4090.10]  A powerful HTTP client
[4090.10 --> 4092.06]  that lives in your terminal.
[4093.14 --> 4094.20]  And it's basically like
[4094.20 --> 4095.24]  take Postman
[4095.24 --> 4096.42]  or take Insomnia,
[4097.44 --> 4098.08]  put it in the terminal.
[4098.18 --> 4099.32]  It's built with Textualize.
[4099.68 --> 4100.90]  So it's a Python tool.
[4101.60 --> 4102.40]  You can pipX,
[4102.52 --> 4103.86]  install it like I did.
[4104.84 --> 4106.80]  And it's very much
[4106.80 --> 4107.36]  like Postman
[4107.36 --> 4108.48]  insofar as you have
[4108.48 --> 4109.24]  like collections
[4109.24 --> 4110.62]  and you can create,
[4110.66 --> 4111.04]  you know,
[4111.32 --> 4112.60]  whole different sessions
[4112.60 --> 4113.40]  of requests.
[4113.50 --> 4114.34]  So it's not your typical
[4114.34 --> 4115.96]  like just run curl,
[4116.20 --> 4116.68]  get an output.
[4116.82 --> 4117.82]  This thing is a long-standing
[4117.82 --> 4118.28]  application.
[4118.38 --> 4119.00]  The reason why I want
[4119.00 --> 4120.34]  to introduce it to you,
[4120.46 --> 4120.56]  Adam,
[4120.60 --> 4122.24]  is because this sucker
[4122.24 --> 4123.26]  is themable.
[4124.00 --> 4124.28]  In fact,
[4124.28 --> 4125.06]  if you launch it,
[4125.12 --> 4126.38]  it's beautiful to start.
[4127.12 --> 4127.30]  Yeah.
[4127.36 --> 4128.46]  But you can also hit
[4128.46 --> 4130.42]  Control-P for commands
[4130.42 --> 4132.60]  and it has the,
[4132.66 --> 4133.38]  you know,
[4133.44 --> 4134.74]  the command palette
[4134.74 --> 4135.54]  which is so common
[4135.54 --> 4137.30]  in text editors
[4137.30 --> 4138.14]  and other tools today.
[4138.42 --> 4139.60]  And you can just go
[4139.60 --> 4140.40]  through the themes
[4140.40 --> 4141.42]  and change the way it looks
[4141.42 --> 4142.38]  and there is a theme
[4142.38 --> 4144.18]  called Hacker
[4144.18 --> 4146.84]  with the Hacker green
[4146.84 --> 4147.52]  on black.
[4148.18 --> 4148.50]  Guys,
[4148.88 --> 4149.58]  this thing is awesome.
[4149.76 --> 4150.84]  It's chasing my heart here.
[4151.28 --> 4151.72]  I gotta say,
[4151.76 --> 4152.36]  I'm just glancing
[4152.36 --> 4153.10]  the readme file
[4153.10 --> 4153.76]  on GitHub now
[4153.76 --> 4154.48]  and there's quite a few
[4154.48 --> 4155.64]  screenshots with different themes.
[4155.86 --> 4155.96]  Yeah,
[4156.00 --> 4156.80]  this looks pretty slick.
[4156.80 --> 4159.26]  It's very high quality
[4159.26 --> 4160.40]  in my opinion.
[4160.56 --> 4160.90]  You have,
[4161.04 --> 4162.40]  you have different
[4162.40 --> 4164.08]  built-in panes
[4164.08 --> 4164.82]  for different sections
[4164.82 --> 4165.68]  like the request,
[4166.16 --> 4166.82]  the response,
[4167.00 --> 4167.52]  a collection,
[4167.68 --> 4168.26]  different things.
[4168.46 --> 4169.42]  If you are familiar
[4169.42 --> 4169.98]  with Postman,
[4170.08 --> 4171.44]  at least the earlier
[4171.44 --> 4172.20]  versions of Postman,
[4172.24 --> 4172.82]  I haven't used Postman
[4172.82 --> 4173.32]  for years,
[4173.78 --> 4175.48]  but that whole UI
[4175.48 --> 4177.10]  is very much akin to that
[4177.10 --> 4178.14]  but here in your terminal.
[4178.98 --> 4180.52]  And what's cool about it
[4180.52 --> 4181.88]  is you can do
[4181.88 --> 4182.82]  all the keyboard shortcuts
[4182.82 --> 4183.80]  but you can also
[4183.80 --> 4185.40]  use your mouse
[4185.40 --> 4186.06]  and click through
[4186.06 --> 4186.84]  on different tabs
[4186.84 --> 4188.12]  and so it's like
[4188.12 --> 4189.50]  aware of the mouse
[4189.50 --> 4191.72]  but also keyboard driven.
[4192.88 --> 4193.16]  It's,
[4193.32 --> 4194.42]  I wonder,
[4194.62 --> 4195.24]  and this would be a question
[4195.24 --> 4196.92]  for probably for
[4196.92 --> 4197.92]  Wilma Guggen
[4197.92 --> 4199.16]  and for the author of this
[4199.16 --> 4200.48]  whose name is Darren Burns,
[4201.26 --> 4201.90]  like how much
[4201.90 --> 4202.56]  of this functionality
[4202.56 --> 4203.62]  that they've accomplished
[4203.62 --> 4204.96]  in this particular tool
[4204.96 --> 4206.46]  he's getting for free
[4206.46 --> 4207.38]  from Textualize
[4207.38 --> 4208.82]  and how much of it Darren
[4208.82 --> 4209.62]  has actually done
[4209.62 --> 4211.10]  because I would consider
[4211.10 --> 4212.24]  this a very rich
[4212.24 --> 4213.86]  text-based UI
[4213.86 --> 4215.60]  as opposed to a lot of them
[4215.60 --> 4216.24]  where like
[4216.24 --> 4218.30]  it's just keyboard commands
[4218.30 --> 4220.26]  or it doesn't really have
[4220.26 --> 4220.96]  all of the things
[4220.96 --> 4221.50]  figured out.
[4221.94 --> 4223.10]  The tab situation
[4223.10 --> 4224.16]  is correct,
[4224.30 --> 4225.48]  like you can tab
[4225.48 --> 4226.44]  through the different areas
[4226.44 --> 4227.20]  as you would
[4227.20 --> 4227.90]  on a web form
[4227.90 --> 4229.00]  and it just,
[4229.36 --> 4230.18]  it just works
[4230.18 --> 4231.14]  in the way you'd expect it to
[4231.14 --> 4232.06]  and so it's very
[4232.06 --> 4233.42]  easy to manipulate
[4233.42 --> 4234.78]  so I'm just highly impressed
[4234.78 --> 4235.66]  by this one in particular.
[4236.50 --> 4236.82]  Very nice.
[4237.36 --> 4237.46]  Yeah,
[4237.48 --> 4238.44]  I may have to check this one out.
[4238.62 --> 4239.40]  It's actually interesting
[4239.40 --> 4239.56]  though,
[4239.60 --> 4240.54]  like this could be maybe
[4240.54 --> 4241.70]  a hot take
[4241.70 --> 4243.02]  on TUIs in general
[4243.02 --> 4245.10]  so I really
[4245.10 --> 4246.02]  don't use
[4246.02 --> 4246.88]  too many of them.
[4247.02 --> 4247.28]  Like sure,
[4247.34 --> 4247.98]  if I'm going to classify
[4247.98 --> 4248.82]  Vim as a TUI
[4248.82 --> 4249.38]  and FCF
[4249.38 --> 4250.04]  once in a while
[4250.04 --> 4250.92]  but like
[4250.92 --> 4252.24]  I know there's TUIs
[4252.24 --> 4252.88]  maybe we'll get to this
[4252.88 --> 4253.34]  a little bit
[4253.34 --> 4253.94]  for Git
[4253.94 --> 4254.62]  and there's like one
[4254.62 --> 4255.58]  for Kubernetes as well
[4255.58 --> 4256.32]  like K9S
[4256.32 --> 4257.16]  like I just,
[4257.62 --> 4258.30]  my use cases
[4258.30 --> 4259.16]  just don't really
[4259.16 --> 4260.78]  go after using tools
[4260.78 --> 4261.06]  like that
[4261.06 --> 4261.78]  because usually it's just like
[4261.78 --> 4262.42]  I just want to run it off
[4262.42 --> 4263.36]  one off command
[4263.36 --> 4264.08]  get some output
[4264.08 --> 4264.72]  move on.
[4264.96 --> 4266.14]  Do you use GUIs?
[4267.02 --> 4267.42]  Yes,
[4267.52 --> 4268.26]  for certain things
[4268.26 --> 4268.92]  definitely.
[4269.24 --> 4269.78]  Like if I'm editing
[4269.78 --> 4270.40]  like a spreadsheet
[4270.40 --> 4270.94]  or something
[4270.94 --> 4272.16]  I prefer that
[4272.16 --> 4272.70]  in a GUI.
[4273.08 --> 4273.70]  Would you
[4273.70 --> 4275.32]  consider a TUI
[4275.32 --> 4275.70]  for that?
[4276.10 --> 4276.52]  If you can
[4276.52 --> 4277.58]  find me a good
[4277.58 --> 4278.04]  spreadsheet
[4278.04 --> 4278.98]  for your TUI
[4278.98 --> 4279.42]  and I shall
[4279.42 --> 4279.80]  Hold on,
[4279.84 --> 4280.36]  let me go back
[4280.36 --> 4281.66]  to the awesome TUIs repo
[4281.66 --> 4282.54]  and see if I can
[4282.54 --> 4283.66]  just search for the word
[4283.66 --> 4284.16]  spreadsheet
[4284.16 --> 4285.24]  or Excel.
[4286.08 --> 4286.30]  Hmm,
[4286.48 --> 4287.20]  SCIM
[4287.20 --> 4287.82]  an NCURS'
[4287.82 --> 4288.70]  spreadsheet program
[4288.70 --> 4289.38]  for the terminal.
[4290.24 --> 4290.68]  We're going to get you
[4290.68 --> 4291.32]  to try that one out?
[4291.48 --> 4292.08]  I'll give it a shot.
[4292.42 --> 4293.18]  Or VisiData
[4293.18 --> 4293.98]  actually VisiData
[4293.98 --> 4294.50]  is awesome.
[4294.84 --> 4295.58]  Have you tried VisiData?
[4296.16 --> 4296.48]  Mm-hmm.
[4296.74 --> 4298.12]  That is
[4298.12 --> 4299.40]  more of a
[4299.40 --> 4300.40]  visualization tool
[4300.40 --> 4301.08]  so it's not going to be
[4301.08 --> 4301.84]  like a one-for-one
[4301.84 --> 4302.64]  replacement
[4302.64 --> 4303.60]  for Google Docs
[4303.60 --> 4304.78]  or Excel
[4304.78 --> 4305.38]  or Numbers.
[4305.92 --> 4306.50]  But yeah,
[4306.58 --> 4307.16]  I would say that
[4307.16 --> 4307.82]  spreadsheet one's
[4307.82 --> 4308.70]  an interesting use case
[4308.70 --> 4309.90]  because some of that
[4309.90 --> 4310.42]  at least the way
[4310.42 --> 4310.96]  I use them
[4310.96 --> 4311.48]  is like,
[4311.52 --> 4311.66]  you know,
[4311.66 --> 4312.14]  let's say I'm
[4312.14 --> 4313.08]  exporting a Stripe
[4313.08 --> 4313.74]  CSV dump
[4313.74 --> 4314.14]  for like,
[4314.32 --> 4314.54]  you know,
[4314.72 --> 4315.82]  whatever courses
[4315.82 --> 4316.62]  I sold over the month
[4316.62 --> 4316.92]  and I want to
[4316.92 --> 4317.64]  calculate something.
[4318.02 --> 4318.56]  I may just like
[4318.56 --> 4319.22]  use my mouse
[4319.22 --> 4319.84]  to drag,
[4320.28 --> 4320.64]  I don't know,
[4320.64 --> 4321.90]  like three weeks
[4321.90 --> 4322.98]  worth of rows
[4322.98 --> 4324.04]  or in there
[4324.04 --> 4324.52]  and kind of just
[4324.52 --> 4325.50]  sum up a total
[4325.50 --> 4326.14]  based on what
[4326.14 --> 4326.82]  I have selected
[4326.82 --> 4327.64]  and I kind of feel
[4327.64 --> 4328.36]  like in the TUI
[4328.36 --> 4328.88]  that's going to be
[4328.88 --> 4329.60]  hard to pull off.
[4330.04 --> 4330.44]  Like it would be
[4330.44 --> 4331.14]  probably pretty easy
[4331.14 --> 4331.96]  to sum a whole column
[4331.96 --> 4332.48]  but what about
[4332.48 --> 4333.06]  just like
[4333.06 --> 4334.48]  rows 6, 15
[4334.48 --> 4335.08]  and you know,
[4335.14 --> 4335.88]  30 through 50?
[4335.88 --> 4336.76]  that's why this
[4336.76 --> 4337.56]  particular tool
[4337.56 --> 4338.74]  is impressing me
[4338.74 --> 4339.42]  and I want to
[4339.42 --> 4339.86]  go back
[4339.86 --> 4340.50]  and maybe
[4340.50 --> 4341.46]  visit more
[4341.46 --> 4342.42]  textualized based
[4342.42 --> 4342.98]  and maybe even
[4342.98 --> 4343.30]  some more
[4343.30 --> 4343.98]  charm based
[4343.98 --> 4344.88]  TUIs
[4344.88 --> 4345.22]  because
[4345.22 --> 4347.20]  the manipulability
[4347.20 --> 4347.64]  of this
[4347.64 --> 4348.56]  is higher
[4348.56 --> 4349.32]  than I would
[4349.32 --> 4349.84]  expect
[4349.84 --> 4350.58]  out of a
[4350.58 --> 4350.96]  traditional
[4350.96 --> 4352.06]  terminal tool.
[4352.80 --> 4353.36]  The fact that
[4353.36 --> 4353.98]  I could probably
[4353.98 --> 4355.36]  I could imagine
[4355.36 --> 4356.24]  something built with
[4356.24 --> 4356.68]  this and maybe
[4356.68 --> 4357.48]  it doesn't do this
[4357.48 --> 4358.16]  but I could imagine
[4358.16 --> 4358.80]  you'd be able to
[4358.80 --> 4359.50]  click and drag
[4359.50 --> 4360.32]  inside your terminal
[4360.32 --> 4361.00]  to select
[4361.00 --> 4362.42]  cells
[4362.42 --> 4363.16]  as you would
[4363.16 --> 4363.84]  inside your GUI
[4363.84 --> 4364.28]  and if we get
[4364.28 --> 4364.76]  that far
[4364.76 --> 4365.76]  I mean
[4365.76 --> 4366.30]  you may never
[4366.30 --> 4366.74]  have to leave
[4366.74 --> 4367.02]  your terminal
[4367.02 --> 4367.56]  again Nick.
[4367.98 --> 4368.76]  I mean this machine
[4368.76 --> 4369.36]  might last you
[4369.36 --> 4370.00]  another decade.
[4370.50 --> 4371.16]  That's right.
[4371.34 --> 4371.78]  I hope so.
[4372.14 --> 4373.00]  Another decade.
[4382.78 --> 4383.54]  Hey friends
[4383.54 --> 4383.92]  I'm here with
[4383.92 --> 4384.42]  Brandon Fu
[4384.42 --> 4385.38]  co-founder and
[4385.38 --> 4387.04]  CEO of Paragon.
[4387.36 --> 4388.04]  Paragon lets
[4388.04 --> 4389.28]  B2B SaaS companies
[4389.28 --> 4390.26]  ship native
[4390.26 --> 4390.92]  integrations to
[4390.92 --> 4391.84]  production in days
[4391.84 --> 4392.64]  with more than
[4392.64 --> 4393.62]  130 pre-built
[4393.62 --> 4394.10]  connectors
[4394.10 --> 4395.16]  or configure
[4395.16 --> 4395.78]  your own custom
[4395.78 --> 4396.60]  integrations.
[4397.04 --> 4397.62]  Brandon there's
[4397.62 --> 4398.80]  a certain level
[4398.80 --> 4399.46]  of pain
[4399.46 --> 4400.24]  that a product
[4400.24 --> 4400.82]  team or an
[4400.82 --> 4401.40]  engineering team
[4401.40 --> 4402.18]  has to endure
[4402.18 --> 4403.50]  to let's just
[4403.50 --> 4404.18]  call it rolling
[4404.18 --> 4404.90]  your own
[4404.90 --> 4405.64]  integrations.
[4406.12 --> 4406.92]  Help me understand
[4406.92 --> 4407.62]  that pain
[4407.62 --> 4408.60]  that angst
[4408.60 --> 4409.50]  for those teams.
[4409.82 --> 4410.26]  Help me understand
[4410.26 --> 4411.08]  that true pain
[4411.08 --> 4411.52]  of delayed
[4411.52 --> 4412.18]  integrations
[4412.18 --> 4413.38]  for a product
[4413.38 --> 4414.48]  not integrating
[4414.48 --> 4415.56]  or having to
[4415.56 --> 4416.30]  roll your own
[4416.30 --> 4416.94]  integration
[4416.94 --> 4418.12]  this seemingly
[4418.12 --> 4419.10]  slower route
[4419.10 --> 4420.36]  to integrations.
[4420.76 --> 4421.08]  I think for
[4421.08 --> 4422.14]  context one of the
[4422.14 --> 4422.86]  reasons we started
[4422.86 --> 4423.92]  Paragon is that
[4423.92 --> 4425.06]  today the average
[4425.06 --> 4426.08]  company uses over
[4426.08 --> 4427.42]  130 different
[4427.42 --> 4428.52]  software applications.
[4429.06 --> 4429.90]  So that means if
[4429.90 --> 4430.82]  you're a B2B software
[4430.82 --> 4432.02]  company selling into
[4432.02 --> 4433.40]  the markets there's
[4433.40 --> 4435.22]  over 130 of your
[4435.22 --> 4436.12]  customers applications
[4436.12 --> 4437.46]  that you probably need
[4437.46 --> 4438.30]  to connect your tool
[4438.30 --> 4439.22]  to because customers
[4439.22 --> 4440.28]  today expect that any
[4440.28 --> 4441.10]  product they buy is
[4441.10 --> 4441.46]  going to work
[4441.46 --> 4442.66]  seamlessly with the
[4442.66 --> 4443.22]  hundreds of other
[4443.22 --> 4444.02]  applications that
[4444.02 --> 4444.42]  they're using.
[4444.72 --> 4445.82]  Of course we see this
[4445.82 --> 4446.98]  when companies come to
[4446.98 --> 4448.24]  us and they say hey
[4448.24 --> 4449.66]  we have a backlog of
[4449.66 --> 4450.88]  10 or 20 or 50
[4450.88 --> 4452.34]  integrations that you
[4452.34 --> 4453.08]  know our sales team
[4453.08 --> 4453.86]  has told us we're
[4453.86 --> 4454.84]  losing deals because
[4454.84 --> 4455.74]  customers are asking
[4455.74 --> 4456.70]  us to integrate with
[4456.70 --> 4457.30]  all these different
[4457.30 --> 4458.70]  apps and we can't
[4458.70 --> 4459.24]  deliver on those
[4459.24 --> 4460.18]  integrations or maybe
[4460.18 --> 4461.24]  our competitors are
[4461.24 --> 4461.78]  integrating with
[4461.78 --> 4463.04]  these tools and the
[4463.04 --> 4463.84]  problem that that
[4463.84 --> 4465.04]  results in for product
[4465.04 --> 4465.86]  and engineering teams
[4465.86 --> 4467.08]  of course is how do
[4467.08 --> 4468.36]  we build and maintain
[4468.36 --> 4469.58]  these integrations in a
[4469.58 --> 4470.22]  way that's scalable
[4470.22 --> 4471.34]  that we can not just
[4471.34 --> 4472.52]  satisfy what customers
[4472.52 --> 4473.28]  are asking for us
[4473.28 --> 4474.28]  today but we can
[4474.28 --> 4474.94]  maintain those
[4474.94 --> 4475.92]  integrations in a way
[4475.92 --> 4477.34]  that's scalable for you
[4477.34 --> 4478.56]  know the next hundred
[4478.56 --> 4479.60]  customers the next hundred
[4479.60 --> 4480.50]  integrations that we
[4480.50 --> 4480.94]  need to build.
[4480.94 --> 4481.94]  So for engineering
[4481.94 --> 4482.70]  one of the challenges
[4482.70 --> 4484.24]  obviously the backlog
[4484.24 --> 4486.86]  and prioritizing time
[4486.86 --> 4487.72]  for certain features
[4487.72 --> 4489.32]  or integrations but
[4489.32 --> 4490.14]  then there's this other
[4490.14 --> 4491.16]  side where you got to
[4491.16 --> 4492.62]  really learn every
[4492.62 --> 4493.76]  single API and
[4493.76 --> 4494.96]  everything is hand
[4494.96 --> 4496.18]  rolled custom
[4496.18 --> 4498.04]  maintained and over
[4498.04 --> 4498.66]  time that kind of
[4498.66 --> 4499.98]  gets I got to imagine
[4499.98 --> 4501.66]  kind of taxing on
[4501.66 --> 4502.14]  teams.
[4502.38 --> 4503.20]  What do you think?
[4503.62 --> 4504.60]  So most engineers
[4504.60 --> 4505.64]  know that's you know
[4505.64 --> 4507.06]  every API is
[4507.06 --> 4507.86]  completely different
[4507.86 --> 4508.64]  can be completely
[4508.64 --> 4509.60]  different in terms of
[4509.60 --> 4510.14]  how they handle
[4510.14 --> 4511.54]  authentication in terms
[4511.54 --> 4512.60]  of how they deal with
[4512.60 --> 4513.68]  different record types
[4513.68 --> 4515.58]  and so it becomes this
[4515.58 --> 4516.46]  problem for engineering
[4516.46 --> 4517.72]  teams to basically have
[4517.72 --> 4519.10]  to become experts in
[4519.10 --> 4520.14]  other people's APIs
[4520.14 --> 4521.40]  and what could be
[4521.40 --> 4522.74]  dozens or hundreds of
[4522.74 --> 4523.48]  different APIs
[4523.48 --> 4525.30]  and to build those
[4525.30 --> 4526.44]  integrations we've seen
[4526.44 --> 4527.54]  can take as much as
[4527.54 --> 4528.86]  three to six months
[4528.86 --> 4530.42]  per integration for a
[4530.42 --> 4532.08]  developer to write the
[4532.08 --> 4533.50]  code to build that
[4533.50 --> 4534.30]  integration and it
[4534.30 --> 4535.22]  depends on the use case
[4535.22 --> 4536.70]  of course and the type of
[4536.70 --> 4537.26]  product that you're
[4537.26 --> 4538.96]  integrating with but of
[4538.96 --> 4539.98]  course that becomes a
[4539.98 --> 4541.24]  massive challenge at
[4541.24 --> 4541.90]  scale when you're
[4541.90 --> 4543.02]  looking at how do we
[4543.02 --> 4543.94]  scale our product to
[4543.94 --> 4545.76]  support you know 10 or
[4545.76 --> 4547.00]  20 or 50 different
[4547.00 --> 4547.58]  integrations.
[4548.26 --> 4549.26]  So again Paragon was
[4549.26 --> 4550.18]  really designed to solve
[4550.18 --> 4551.56]  that problem and to
[4551.56 --> 4552.78]  distill the complexities
[4552.78 --> 4554.54]  and the nuances and
[4554.54 --> 4555.38]  the differences between
[4555.38 --> 4556.30]  hundreds of different
[4556.30 --> 4557.32]  SaaS apps into a
[4557.32 --> 4558.42]  single connecting
[4558.42 --> 4559.66]  platform into a single
[4559.66 --> 4560.86]  SDK that your
[4560.86 --> 4562.46]  engineers can install in
[4562.46 --> 4563.52]  your app and then
[4563.52 --> 4564.68]  easily connect your
[4564.68 --> 4565.98]  products to all these
[4565.98 --> 4566.96]  different SaaS applications
[4566.96 --> 4567.52]  in the market.
[4568.12 --> 4569.80]  Okay Paragon is built
[4569.80 --> 4570.66]  for product management
[4570.66 --> 4571.72]  is built for
[4571.72 --> 4572.56]  engineering it's built
[4572.56 --> 4573.58]  for everybody ship
[4573.58 --> 4574.62]  hundreds of native
[4574.62 --> 4576.10]  integrations into your
[4576.10 --> 4577.48]  SaaS application in
[4577.48 --> 4578.94]  days or build your own
[4578.94 --> 4580.12]  custom connector with any
[4580.12 --> 4580.64]  API.
[4581.44 --> 4582.64]  Learn more at use
[4582.64 --> 4584.12]  paragon.com slash
[4584.12 --> 4585.62]  changelog again
[4585.62 --> 4588.16]  use paragon.com slash
[4588.16 --> 4588.98]  changelog that's
[4588.98 --> 4592.44]  u-s-e-p-a-r-a-g-o-n
[4592.44 --> 4594.22]  dot com slash
[4594.22 --> 4595.08]  changelog.
[4595.08 --> 4602.20]  I was thinking about
[4602.20 --> 4603.10]  this while we were
[4603.10 --> 4604.56]  going beyond the
[4604.56 --> 4605.96]  norm of a developer
[4605.96 --> 4607.44]  tool so to speak to
[4607.44 --> 4608.48]  maybe go one layer
[4608.48 --> 4609.84]  deeper on developer
[4609.84 --> 4610.58]  tool and I don't know
[4610.58 --> 4610.98]  if this is watching
[4610.98 --> 4612.88]  this show but I saw
[4612.88 --> 4614.48]  pager duty mentioned
[4614.48 --> 4615.60]  in this list as you
[4615.60 --> 4616.80]  were digging into this
[4616.80 --> 4617.86]  list further Jared so I
[4617.86 --> 4619.96]  was following you and
[4619.96 --> 4620.84]  I saw pager duty I'm
[4620.84 --> 4622.00]  thinking like okay well
[4622.00 --> 4623.94]  there is pager duty
[4623.94 --> 4626.34]  dash t ui a
[4626.34 --> 4627.34]  minimalistic terminal
[4627.34 --> 4628.62]  ui to manage triggered
[4628.62 --> 4630.38]  incidents and so I'm
[4630.38 --> 4631.90]  thinking gosh well I
[4631.90 --> 4632.58]  don't want to go to the
[4632.58 --> 4634.62]  century dashboard can I
[4634.62 --> 4635.94]  just two-y this thing in
[4635.94 --> 4636.82]  century and there's
[4636.82 --> 4637.48]  nothing in here for
[4637.48 --> 4638.96]  century but I'm thinking
[4638.96 --> 4640.82]  like particular dev
[4640.82 --> 4643.10]  tools that are you know
[4643.10 --> 4646.44]  web ui dashboard based
[4646.44 --> 4647.66]  things like century or
[4647.66 --> 4649.26]  others might be would it
[4649.26 --> 4650.08]  make sense to have a
[4650.08 --> 4651.22]  two-y because like
[4651.22 --> 4652.50]  hackers be hackers give
[4652.50 --> 4653.76]  me an interface that is
[4653.76 --> 4656.04]  just simplified not the
[4656.04 --> 4657.04]  extras just the things
[4657.04 --> 4659.20]  that matters is there a
[4659.20 --> 4660.44]  room for a to be in the
[4660.44 --> 4661.90]  world of like a century or
[4661.90 --> 4664.24]  maybe even who do we use
[4664.24 --> 4665.02]  for analysts again
[4665.02 --> 4667.02]  plausible plausible yeah
[4667.02 --> 4667.66]  like things like that
[4667.66 --> 4668.44]  like could there be a to
[4668.44 --> 4669.46]  be for plausible and
[4669.46 --> 4670.90]  century and obviously
[4670.90 --> 4671.96]  duty or something like
[4671.96 --> 4673.04]  that like I would welcome
[4673.04 --> 4674.86]  that personally right I
[4674.86 --> 4676.62]  would yeah I think so
[4676.62 --> 4677.60]  especially with that type
[4677.60 --> 4678.74]  of data it's like you
[4678.74 --> 4679.88]  don't necessarily need to
[4679.88 --> 4680.98]  see the pie chart but the
[4680.98 --> 4682.12]  numbers matter and if the
[4682.12 --> 4684.00]  two we you know output
[4684.00 --> 4684.78]  them in a way that was
[4684.78 --> 4685.84]  glanceable then you get
[4685.84 --> 4686.92]  the same information so
[4686.92 --> 4688.02]  yeah quick check too it's
[4688.02 --> 4688.92]  like I don't have to exit
[4688.92 --> 4690.64]  my terminal I can maybe
[4690.64 --> 4691.96]  even have a team accession
[4691.96 --> 4693.24]  with it already there
[4693.24 --> 4694.54]  exactly you know it's
[4694.54 --> 4696.40]  already in my world see
[4696.40 --> 4697.48]  now you're now you're
[4697.48 --> 4700.50]  thinking century you should
[4700.50 --> 4701.96]  do this I think plausible
[4701.96 --> 4702.80]  should do it too I think
[4702.80 --> 4703.76]  that's a great example of
[4703.76 --> 4704.98]  like something that you
[4704.98 --> 4706.02]  normally would go to some
[4706.02 --> 4707.12]  sort of web interface to
[4707.12 --> 4709.50]  check and there's
[4709.50 --> 4710.84]  something powerful in the
[4710.84 --> 4711.72]  constraints that the
[4711.72 --> 4714.00]  terminal does put on a
[4714.00 --> 4715.54]  design I believe even
[4715.54 --> 4716.18]  though we're starting to
[4716.18 --> 4717.20]  see more richness and
[4717.20 --> 4719.16]  tools like this one where
[4719.16 --> 4720.90]  it might actually even be
[4720.90 --> 4722.64]  quicker better and just
[4722.64 --> 4723.60]  better information
[4723.60 --> 4724.46]  architecture and all that
[4724.46 --> 4725.30]  stuff if you're like we
[4725.30 --> 4726.26]  have to provide a really
[4726.26 --> 4727.72]  simplified view for the
[4727.72 --> 4729.48]  terminal and then you just
[4729.48 --> 4730.40]  ask yourself questions like
[4730.40 --> 4731.64]  what really matters you
[4731.64 --> 4732.52]  know versus like showing
[4732.52 --> 4733.64]  them all the widgets you
[4733.64 --> 4735.22]  know and so that could be
[4735.22 --> 4736.62]  really cool yeah
[4736.62 --> 4738.66]  simplified a UI is is a
[4738.66 --> 4741.46]  big deal I think I'd
[4741.46 --> 4742.36]  imagine they can probably
[4742.36 --> 4745.58]  put a a search or query
[4745.58 --> 4748.18]  kind of like bar in that
[4748.18 --> 4749.62]  UI to interact with the
[4749.62 --> 4750.64]  data to to some degree
[4750.64 --> 4751.98]  like almost a command line
[4751.98 --> 4754.32]  for the TUI to change the
[4754.32 --> 4756.02]  data UI or just maybe even
[4756.02 --> 4756.92]  buttons or something like
[4756.92 --> 4758.44]  that that makes it a bit
[4758.44 --> 4759.72]  more rich the challenge I
[4759.72 --> 4761.80]  think is that and maybe
[4761.80 --> 4762.72]  this is something we talked
[4762.72 --> 4765.36]  with with what's his name
[4765.36 --> 4767.16]  McGoole first name which
[4767.16 --> 4769.10]  one the fellow that did
[4769.10 --> 4770.96]  textualize and textual will
[4770.96 --> 4772.26]  McGoogan will McGoogan
[4772.26 --> 4773.84]  McGoole I was thinking
[4773.84 --> 4774.54]  about a different friend of
[4774.54 --> 4775.74]  ours that's the fellow from
[4775.74 --> 4776.96]  Google I was thinking about
[4776.96 --> 4779.54]  McGoole from that that that
[4779.54 --> 4780.62]  GitHub universe trip we did
[4780.62 --> 4781.60]  remember that that crazy
[4781.60 --> 4782.86]  yeah yeah that drive there
[4782.86 --> 4784.28]  yeah oh man that didn't make
[4784.28 --> 4785.34]  it into your highlights video
[4785.34 --> 4786.44]  man I'm sorry about that I
[4786.44 --> 4787.22]  didn't take any pictures of
[4787.22 --> 4788.88]  that trip probably not but I
[4788.88 --> 4790.08]  that conversation we had with
[4790.08 --> 4790.82]  them I think it was pretty
[4790.82 --> 4792.14]  I'm just wondering how much
[4792.14 --> 4793.68]  we'll link that up in the
[4793.68 --> 4794.60]  show notes by the way we
[4794.60 --> 4795.24]  had a great conversation
[4795.24 --> 4797.20]  with Will about textualize
[4797.20 --> 4799.02]  and textual and rich and
[4799.02 --> 4800.10]  really just this idea of
[4800.10 --> 4801.50]  where TUIs can go and I
[4801.50 --> 4802.32]  think that was a precursor
[4802.32 --> 4803.26]  to a lot of this stuff
[4803.26 --> 4805.52]  really just a maybe a 101 on
[4805.52 --> 4806.50]  where this thing is going
[4806.50 --> 4809.08]  but realistically how
[4809.08 --> 4811.42]  defined is the interface
[4811.42 --> 4813.80]  standard I suppose for a
[4813.80 --> 4814.92]  TUI they seem to be all
[4814.92 --> 4815.96]  over the map and so maybe
[4815.96 --> 4816.96]  that's why they're less
[4816.96 --> 4819.14]  appreciated maybe adopted
[4819.14 --> 4820.16]  maybe developed because
[4820.16 --> 4821.56]  there's no kind of rich
[4821.56 --> 4822.54]  standard like there is for
[4822.54 --> 4824.76]  iOS for example or even
[4824.76 --> 4826.06]  like when you're web
[4826.06 --> 4826.94]  designer these days you
[4826.94 --> 4828.10]  usually begin with mobile
[4828.10 --> 4829.36]  screens first or the
[4829.36 --> 4830.74]  smaller screens first and
[4830.74 --> 4832.30]  that sort of sets the bar
[4832.30 --> 4833.60]  for your larger screens
[4833.60 --> 4835.32]  and I'm just wondering like
[4835.32 --> 4836.92]  there is no true standard
[4836.92 --> 4841.00]  thus far or like just a
[4841.00 --> 4842.66]  just a what's the right
[4842.66 --> 4844.22]  word for it a system a
[4844.22 --> 4845.62]  design system for these
[4845.62 --> 4846.66]  things I almost feel like if
[4846.66 --> 4847.78]  you did that and you had
[4847.78 --> 4849.90]  components maybe it might
[4849.90 --> 4851.16]  be maybe that's what
[4851.16 --> 4853.24]  textual does rich does I
[4853.24 --> 4854.30]  don't know yeah it's kind
[4854.30 --> 4855.02]  of moving a little bit
[4855.02 --> 4855.86]  away from the Unix
[4855.86 --> 4857.54]  philosophy even though
[4857.54 --> 4858.44]  you're still like right
[4858.44 --> 4859.62]  there alongside all the
[4859.62 --> 4862.22]  Unix tools because instead
[4862.22 --> 4864.50]  of doing one thing you're
[4864.50 --> 4865.42]  doing lots of stuff right
[4865.42 --> 4866.60]  like it's stateful there's
[4866.60 --> 4868.48]  lots of features inside of
[4868.48 --> 4871.16]  a TUI etc and you're kind
[4871.16 --> 4873.72]  of abandoning this idea of
[4873.72 --> 4875.00]  like inputs and outputs
[4875.00 --> 4876.94]  everything is text I've
[4876.94 --> 4877.70]  noticed a lot of these
[4877.70 --> 4879.06]  tools will have some sort
[4879.06 --> 4880.44]  of alternate output mode
[4880.44 --> 4882.54]  and it's usually JSON which
[4882.54 --> 4883.70]  makes some sense because
[4883.70 --> 4885.46]  you know JSON for most
[4885.46 --> 4887.44]  tooling is actually less
[4887.44 --> 4889.16]  work to parse than text
[4889.16 --> 4891.10]  is in the case that you
[4891.10 --> 4892.56]  don't know what the text
[4892.56 --> 4893.48]  is going to be until you
[4893.48 --> 4895.40]  start to use it of course
[4895.40 --> 4897.00]  Nick probably can just set
[4897.00 --> 4898.78]  and cut it to exactly what
[4898.78 --> 4899.78]  he wants but you know that
[4899.78 --> 4900.46]  can be sort of thinking
[4900.46 --> 4901.28]  about his commands he's
[4901.28 --> 4902.72]  writing to slice and dice
[4902.72 --> 4903.58]  this JSON I know he's
[4903.58 --> 4904.68]  actually I can see his eyes
[4904.68 --> 4905.60]  moving in his head he's
[4905.60 --> 4906.50]  like setting he's cutting
[4906.50 --> 4907.56]  stuff he's like oh man
[4907.56 --> 4909.28]  text is the bomb I don't
[4909.28 --> 4910.34]  disagree with that but I
[4910.34 --> 4912.54]  am noticing a motion
[4912.54 --> 4913.66]  towards more tools
[4913.66 --> 4915.18]  outputting JSON especially
[4915.18 --> 4917.10]  if they have a stateful UI
[4917.10 --> 4918.66]  where it's like the regular
[4918.66 --> 4919.74]  view is like this rich
[4919.74 --> 4921.72]  client in your terminal and
[4921.72 --> 4922.68]  then we'll also give you a
[4922.68 --> 4925.76]  JSON output not necessarily
[4925.76 --> 4927.16]  commenting on that but I
[4927.16 --> 4928.24]  think that it's I'm
[4928.24 --> 4930.76]  noticing it as a trend and
[4930.76 --> 4931.62]  so that's kind of going away
[4931.62 --> 4932.96]  from the Unix philosophy right
[4932.96 --> 4934.74]  possibly and then I think
[4934.74 --> 4936.30]  the the standardization
[4936.30 --> 4937.76]  around inputs and outputs
[4937.76 --> 4940.66]  everything is text is it's
[4940.66 --> 4942.84]  not a user interface it is
[4942.84 --> 4944.82]  it's an interface it's a
[4944.82 --> 4946.02]  programmatic interface that
[4946.02 --> 4947.64]  has become a standard
[4947.64 --> 4949.02]  amongst Unix like things
[4949.02 --> 4950.76]  which now we have all of
[4950.76 --> 4952.30]  these rich things inside the
[4952.30 --> 4954.02]  terminal I'm sure the charm
[4954.02 --> 4955.24]  toolkit works differently than
[4955.24 --> 4956.74]  the textualized one probably
[4956.74 --> 4957.70]  works differently than the
[4957.70 --> 4959.04]  Ratatouille one and so you
[4959.04 --> 4960.54]  may have to learn a UI every
[4960.54 --> 4962.04]  single time as you adopt
[4962.04 --> 4963.76]  these which could be a
[4963.76 --> 4965.10]  barrier to adoption Nick
[4965.10 --> 4965.56]  you were going to say
[4965.56 --> 4966.70]  something yeah just a
[4966.70 --> 4967.64]  little bit and it's related
[4967.64 --> 4969.02]  to that as well just you
[4969.02 --> 4969.70]  know I'm sure you guys
[4969.70 --> 4970.76]  remember the old days with
[4970.76 --> 4972.74]  like flash and you know
[4972.74 --> 4973.50]  trying to build your own
[4973.50 --> 4974.52]  flash application was a
[4974.52 --> 4975.10]  little bit challenging
[4975.10 --> 4975.86]  because it kind of just
[4975.86 --> 4976.86]  had this white blank
[4976.86 --> 4977.88]  screen and then you could
[4977.88 --> 4979.02]  literally do anything like
[4979.02 --> 4979.72]  whatever you wanted to put
[4979.72 --> 4980.68]  on there within reason can
[4980.68 --> 4981.76]  be done but with like
[4981.76 --> 4982.52]  HTML you have some
[4982.52 --> 4983.36]  structure you have like an
[4983.36 --> 4984.78]  h1 and you know link tag
[4984.78 --> 4985.76]  and some other stuff so you
[4985.76 --> 4986.52]  have these little components
[4986.52 --> 4987.84]  to build something which
[4987.84 --> 4989.46]  gives you a constraint but
[4989.46 --> 4990.76]  it's like still flexible
[4990.76 --> 4991.62]  enough to build the things
[4991.62 --> 4992.60]  that you'd like but yeah
[4992.60 --> 4993.68]  it would be interesting to
[4993.68 --> 4994.88]  see if some of these more
[4994.88 --> 4996.42]  defined like I don't know
[4996.42 --> 4997.88]  terminal UI toolkits come
[4997.88 --> 4998.68]  out or if they're not
[4998.68 --> 4999.76]  already there like if that
[4999.76 --> 5000.62]  would help spark a little
[5000.62 --> 5002.20]  bit more interest in
[5002.20 --> 5003.22]  building tools like this
[5003.22 --> 5004.70]  well that was the hope
[5004.70 --> 5005.76]  going back to the
[5005.76 --> 5006.42]  conversation we had with
[5006.42 --> 5007.48]  Will was he had a big
[5007.48 --> 5009.06]  idea which should be it
[5009.06 --> 5009.80]  would be fun to revisit
[5009.80 --> 5011.34]  that with him Jared because
[5011.34 --> 5012.94]  he had some I would say we
[5012.94 --> 5014.08]  even pushed back in the
[5014.08 --> 5015.70]  last 20 minutes on his
[5015.70 --> 5018.76]  philosophy for being the
[5018.76 --> 5019.72]  founder and CEO of
[5019.72 --> 5020.52]  textualize which I
[5020.52 --> 5021.56]  believe is a company he
[5021.56 --> 5022.88]  founded and formed around
[5022.88 --> 5025.48]  this textual textualize
[5025.48 --> 5028.32]  rich all these projects
[5028.32 --> 5029.58]  around this idea of
[5029.58 --> 5031.54]  twoies and I think we
[5031.54 --> 5032.52]  were like you just want to
[5032.52 --> 5034.56]  take these twoies to make
[5034.56 --> 5035.64]  them websites it seemed
[5035.64 --> 5036.78]  like an oxymoron like that
[5036.78 --> 5037.98]  doesn't make sense really
[5037.98 --> 5039.50]  counterintuitive to the
[5039.50 --> 5041.18]  idea so I'd love to revisit
[5041.18 --> 5042.98]  that but if we had a
[5042.98 --> 5044.06]  champion like I think Will
[5044.06 --> 5045.30]  was trying to be around
[5045.30 --> 5047.64]  standardizing what twoies
[5047.64 --> 5049.90]  are popularizing them and
[5049.90 --> 5052.20]  then giving people the
[5052.20 --> 5053.60]  training wheels slash
[5053.60 --> 5055.40]  frameworks slash components
[5055.40 --> 5057.10]  so that it's a little
[5057.10 --> 5058.36]  easier to build them I
[5058.36 --> 5059.36]  think would be a step up
[5059.36 --> 5061.36]  because I'm a user of
[5061.36 --> 5062.60]  them and if there was
[5062.60 --> 5064.10]  more of services I use
[5064.10 --> 5065.40]  like century or whatever
[5066.28 --> 5067.12]  else is out there
[5067.12 --> 5068.54]  plausible I mean where
[5068.54 --> 5069.40]  else could you use this
[5069.40 --> 5070.32]  stuff like any place you
[5070.32 --> 5070.98]  would want to use a little
[5070.98 --> 5071.86]  dashboard just to get a
[5071.86 --> 5073.42]  version of it you know I
[5073.42 --> 5075.00]  know KDS has wasn't
[5075.00 --> 5076.00]  there a single painted
[5076.00 --> 5077.50]  glass thing that Gerard
[5077.50 --> 5078.48]  had back in the day when
[5078.48 --> 5080.00]  we were on Linux yeah
[5080.00 --> 5081.74]  canines there's all that
[5081.74 --> 5082.54]  for all these different
[5082.54 --> 5083.70]  applications Docker has
[5083.70 --> 5084.76]  versions of them I'm sure
[5084.76 --> 5085.48]  right right I think
[5085.48 --> 5086.74]  there's there's all these
[5086.74 --> 5087.42]  things out there for
[5087.42 --> 5088.38]  Docker that you can see
[5088.38 --> 5089.44]  like okay here's all my
[5089.44 --> 5090.56]  here's all my containers
[5090.56 --> 5092.10]  running here's the you
[5092.10 --> 5093.44]  know the CPU usage of
[5093.44 --> 5094.70]  each of them and you know
[5094.70 --> 5096.16]  what the status of it I
[5096.16 --> 5097.08]  mean they're here to stay
[5097.08 --> 5098.90]  I wonder if we just had
[5098.90 --> 5100.42]  better tooling underneath
[5100.42 --> 5101.20]  and maybe that's what Will
[5101.20 --> 5103.94]  and team are doing for
[5103.94 --> 5105.06]  for this I don't know
[5105.06 --> 5106.08]  yeah for sure it's
[5106.08 --> 5106.66]  actually another
[5106.66 --> 5108.72]  interesting segue or like
[5108.72 --> 5109.28]  what's the difference
[5109.28 --> 5110.38]  between like a CLI tool
[5110.38 --> 5111.50]  that's not a TUI versus
[5111.50 --> 5113.30]  one that is like Docker
[5113.30 --> 5114.12]  is a great example like
[5114.12 --> 5115.04]  there's a Docker stats
[5115.04 --> 5115.94]  command that you can run
[5115.94 --> 5116.88]  and that will just list
[5116.88 --> 5117.48]  out all your running
[5117.48 --> 5118.52]  containers and give you
[5118.52 --> 5119.64]  the outputs of like the
[5119.64 --> 5121.46]  CPU memory disk and
[5121.46 --> 5122.58]  network like you know just
[5122.58 --> 5123.54]  little stats about those
[5123.54 --> 5125.30]  things and you know
[5125.30 --> 5126.26]  there is this like medium
[5126.26 --> 5127.46]  ground I guess between
[5127.46 --> 5128.58]  like a CLI and a TUI
[5128.58 --> 5129.96]  for output like you have
[5129.96 --> 5130.92]  you guys ever used like
[5130.92 --> 5131.96]  the watch commands and
[5131.96 --> 5132.82]  like some commands just
[5132.82 --> 5133.86]  support like dash dash
[5133.86 --> 5134.82]  watch like Kubernetes as
[5134.82 --> 5135.80]  well like you know it'll
[5135.80 --> 5137.50]  just watch a program and
[5137.50 --> 5138.58]  we'll let you know when the
[5138.58 --> 5139.82]  outputs are changing so
[5139.82 --> 5140.58]  it's like Docker stats
[5140.58 --> 5141.52]  almost feels like it's
[5141.52 --> 5142.66]  just doing that it's not
[5142.66 --> 5144.34]  quite a TUI but yeah there
[5144.34 --> 5145.64]  are other other tools
[5145.64 --> 5147.26]  dedicated to it's a PUI
[5147.26 --> 5148.38]  actually it's a plain UI
[5148.38 --> 5150.74]  yeah but I actually going
[5150.74 --> 5151.44]  back to what Adam said
[5151.44 --> 5152.16]  before around his
[5152.16 --> 5153.14]  definition of TUI as
[5153.14 --> 5153.68]  being more like
[5153.68 --> 5155.50]  application like and just
[5155.50 --> 5156.42]  going back to like the
[5156.42 --> 5158.52]  Unix philosophy I do think
[5158.52 --> 5159.46]  it to some degree like when
[5159.46 --> 5160.36]  you're using an application
[5160.36 --> 5162.04]  you like there's certain
[5162.04 --> 5162.92]  characteristics of the
[5162.92 --> 5163.76]  Unix philosophy that you
[5163.76 --> 5164.56]  almost don't care about
[5164.56 --> 5166.18]  like if you had a TUI to
[5166.18 --> 5167.80]  have like an mp3 player
[5167.80 --> 5168.96]  it's like you want to open
[5168.96 --> 5170.28]  that program find the mp3
[5170.28 --> 5171.10]  that you want maybe it's
[5171.10 --> 5171.78]  like there's some bouncing
[5171.78 --> 5172.82]  lines like you know with the
[5172.82 --> 5173.66]  EQ or something that'd be
[5173.66 --> 5174.68]  cool maybe some metadata
[5174.68 --> 5175.86]  about the file being played
[5175.86 --> 5177.88]  like that's what I care
[5177.88 --> 5178.80]  about because I'm like
[5178.80 --> 5179.74]  using that application to
[5179.74 --> 5181.30]  select and play an mp3
[5181.30 --> 5182.94]  but I guess technically I
[5182.94 --> 5184.72]  mean Adam and you know
[5184.72 --> 5185.38]  Jared you mentioned this
[5185.38 --> 5186.32]  with like JSON output do
[5186.32 --> 5187.42]  some of these TUIs also
[5187.42 --> 5188.94]  offer flags or ways to run
[5188.94 --> 5190.04]  them to where like if you
[5190.04 --> 5190.82]  wanted to get that metadata
[5190.82 --> 5192.04]  back you can get that back
[5192.04 --> 5193.32]  in text form and now it's
[5193.32 --> 5194.76]  like suddenly back to hey
[5194.76 --> 5195.72]  I'm getting text as output
[5195.72 --> 5196.68]  I can go and pipe that to
[5196.68 --> 5197.54]  something else so you kind of
[5197.54 --> 5198.44]  get the best of both worlds
[5198.44 --> 5199.72]  the TUI when you want to use
[5199.72 --> 5200.74]  it as an app and the
[5200.74 --> 5201.66]  outputs for when you want to
[5201.66 --> 5202.32]  do something else
[5202.32 --> 5204.14]  yeah absolutely obviously
[5204.14 --> 5207.00]  it's app by app an mp3
[5207.00 --> 5208.04]  player like what kind of
[5208.04 --> 5209.68]  output would you want from
[5209.68 --> 5212.26]  that necessarily maybe like
[5212.26 --> 5213.06]  your list of played
[5213.06 --> 5215.80]  recently played or maybe I
[5215.80 --> 5217.54]  did find a podcasting app
[5217.54 --> 5218.50]  which I threw in here
[5218.50 --> 5221.50]  called Castero which I
[5221.50 --> 5222.54]  downloaded and tried and
[5222.54 --> 5224.50]  yes it does work this is a
[5224.50 --> 5226.00]  Python thing so you pipex
[5226.00 --> 5228.78]  install it doesn't look like
[5228.78 --> 5229.98]  it's necessarily maintained
[5229.98 --> 5232.64]  it did work I did listen to
[5232.64 --> 5233.96]  a little bit of changelog news
[5233.96 --> 5235.46]  in there that was pretty cool
[5235.46 --> 5238.40]  and when you launch it now
[5238.40 --> 5239.64]  this is like a three-pain thing
[5239.64 --> 5241.10]  with like your feeds your
[5241.10 --> 5243.86]  episodes if something like
[5243.86 --> 5245.24]  that and you're that would
[5245.24 --> 5246.38]  be two pains I don't know
[5246.38 --> 5248.06]  it's like your podcasts your
[5248.06 --> 5249.50]  episodes and then what's
[5249.50 --> 5250.26]  currently playing or
[5250.26 --> 5254.54]  something and my big gripe
[5254.54 --> 5255.54]  with that one is the space
[5255.54 --> 5256.76]  bar for some reason doesn't
[5256.76 --> 5258.26]  play pause it like moves up
[5258.26 --> 5259.28]  and down anyways that's a
[5259.28 --> 5260.90]  small gripe but I just think
[5260.90 --> 5262.08]  what do you think what do
[5262.08 --> 5263.10]  you think man come on
[5263.10 --> 5264.70]  everywhere the space bar is a
[5264.70 --> 5265.94]  play pause or a quick look
[5265.94 --> 5267.56]  and so when you launch it
[5267.56 --> 5268.66]  you're like I gotta load my
[5268.66 --> 5269.78]  feeds into this thing and
[5269.78 --> 5271.34]  like you can load in and
[5271.34 --> 5273.18]  out of I think opml and so
[5273.18 --> 5275.06]  I could see where Castero
[5275.06 --> 5276.40]  with some sort of flag like
[5276.40 --> 5277.54]  launching it not the two
[5277.54 --> 5279.28]  but some other version of
[5279.28 --> 5280.72]  the program where it'll just
[5280.72 --> 5282.24]  output your opml right your
[5282.24 --> 5283.88]  subscriptions list as xml or
[5283.88 --> 5285.20]  whatever it is I could see
[5285.20 --> 5287.40]  that as a alternate way to
[5287.40 --> 5288.60]  run the program and get some
[5288.60 --> 5290.04]  output that would make sense
[5290.04 --> 5292.08]  to pipe somewhere else but
[5292.08 --> 5293.32]  yeah I think it's contextual I
[5293.32 --> 5294.38]  think some of them makes total
[5294.38 --> 5297.00]  sense like a tool like posting
[5297.00 --> 5299.00]  which is its entire point is
[5299.00 --> 5300.50]  to do like HTTP requests and
[5300.50 --> 5302.42]  bring you back the information
[5302.42 --> 5304.32]  after running it I can see
[5304.32 --> 5305.30]  where you can put together a
[5305.30 --> 5307.58]  collection maybe through using
[5307.58 --> 5309.10]  the user interface set it all
[5309.10 --> 5310.32]  up and a lot of people use
[5310.32 --> 5311.08]  these things for like
[5311.08 --> 5313.22]  integration tests and you
[5313.22 --> 5313.96]  could maybe take that
[5313.96 --> 5315.48]  collection save it as yaml and
[5315.48 --> 5316.28]  then you could run it from the
[5316.28 --> 5317.76]  command line with some sort of
[5317.76 --> 5319.22]  alternate flag to where it's
[5319.22 --> 5320.22]  not going to launch the user
[5320.22 --> 5321.68]  interface it's going to provide
[5321.68 --> 5324.24]  you a boolean true or false
[5324.24 --> 5325.28]  did it pass or you know I'm
[5325.28 --> 5326.82]  saying like I like the idea of
[5326.82 --> 5329.26]  the 2e slash command line
[5329.26 --> 5332.78]  utility being symbiotic and the
[5332.78 --> 5333.96]  fact that they you know you
[5333.96 --> 5335.76]  might hop into the 2e to do a
[5335.76 --> 5339.50]  more deeper visual you know
[5339.50 --> 5342.76]  application like experience that
[5342.76 --> 5344.00]  also has like you said a
[5344.00 --> 5345.28]  configuration or setting I'm
[5345.28 --> 5346.36]  thinking like even tailscale I'm
[5346.36 --> 5347.92]  wearing the t-shirt today big fan
[5347.92 --> 5350.20]  of tailscale not sponsored where
[5350.20 --> 5351.86]  they can even have a 2e like that
[5351.86 --> 5353.28]  where you've got multiple machines
[5353.28 --> 5355.10]  multiple machines across your
[5355.10 --> 5357.32]  tail net kind of thing you might
[5357.32 --> 5358.32]  go there and configure a
[5358.32 --> 5359.72]  collection of machines you know I
[5359.72 --> 5361.22]  don't know do some cool stuff in
[5361.22 --> 5362.94]  the 2e but the same time you
[5362.94 --> 5364.56]  still have the traditional
[5364.56 --> 5366.48]  tailscale CLI or even the same
[5366.48 --> 5368.38]  case here with with posting is
[5368.38 --> 5370.24]  like the application is just one
[5370.24 --> 5373.66]  more way you enjoy the CLI the
[5373.66 --> 5374.96]  command line interface that's
[5374.96 --> 5376.98]  there it's just a visual version of
[5376.98 --> 5378.96]  it built probably on top of it with
[5378.96 --> 5381.56]  textualize or textual or rich or
[5381.56 --> 5384.22]  whatever they're trying to use I
[5384.22 --> 5385.14]  think more people should adopt
[5385.14 --> 5386.60]  these things man like it's it's
[5386.60 --> 5388.68]  just like an underserved market I
[5388.68 --> 5390.68]  like it please do more of it
[5390.68 --> 5392.32]  please let me ask you one question
[5392.32 --> 5394.44]  here Nick on on on this docker
[5394.44 --> 5396.80]  stats if you don't mind because I
[5396.80 --> 5399.66]  have a question because I did this
[5399.66 --> 5404.68]  on my plexbox which is a an ubuntu
[5404.68 --> 5407.58]  machine in a VM on proxbox so it's
[5407.58 --> 5410.60]  got a single usage yes I know I'm
[5410.60 --> 5413.72]  running docker on top of a VM on
[5413.72 --> 5415.38]  top of proxbox it's multiple layers
[5415.38 --> 5416.76]  it's kind of unnecessary but I like
[5416.76 --> 5418.10]  it because it's it just keeps it
[5418.10 --> 5421.54]  siloed but anyways I digress so when
[5421.54 --> 5424.02]  I write or when I type in docker
[5424.02 --> 5427.08]  stats on this plex box which it
[5427.08 --> 5429.32]  literally is only a single ubuntu box
[5429.32 --> 5432.02]  dedicated to running docker to run a
[5432.02 --> 5434.26]  single docker container which is the
[5434.26 --> 5435.76]  plex docker container just to give you
[5435.76 --> 5438.42]  a full circumference of the the the
[5438.42 --> 5441.06]  reason for the machine the cpu I run
[5441.06 --> 5443.42]  docker stats and it's real time the
[5443.42 --> 5447.24]  cpu is at 66 point whatever right but
[5447.24 --> 5450.28]  then because I don't run tmux I go into
[5450.28 --> 5453.36]  a new tab and I ssh back into that box
[5453.36 --> 5455.76]  again and then I type htop because
[5455.76 --> 5457.68]  that's what I have on that box and I
[5457.68 --> 5459.84]  see that my cpu is not being taxed at
[5459.84 --> 5462.78]  all at that percentage what's the deal
[5462.78 --> 5465.60]  why is docker stats saying such a high cpu
[5465.60 --> 5468.02]  usage and it's not yeah I mean docker
[5468.02 --> 5469.66]  stats would be reporting the cpu usage
[5469.66 --> 5471.18]  of whatever happening in the container
[5471.18 --> 5472.70]  but I mean that's still affecting your
[5472.70 --> 5475.02]  host operating system cpu with no it's
[5475.02 --> 5476.48]  not like a magic cpu that's just going
[5476.48 --> 5478.84]  to exist so like that that cpu load
[5478.84 --> 5480.94]  should have carried over I mean I have
[5480.94 --> 5482.38]  to look at your setup a little a little
[5482.38 --> 5484.38]  more detail I mean when you run any
[5484.38 --> 5486.08]  docker command you're connecting against
[5486.08 --> 5488.00]  wherever you have docker running right
[5488.00 --> 5489.78]  well I can tell you on htop the average
[5489.78 --> 5491.62]  cpu usage right now is four point
[5491.62 --> 5494.50]  something whereas in the docker stats
[5494.50 --> 5497.50]  real-time update it says 64% I was
[5497.50 --> 5498.70]  just wondering like maybe as a docker
[5498.70 --> 5500.02]  thing maybe this image is out
[5500.02 --> 5502.44]  allocated a certain percentage of the
[5502.44 --> 5504.18]  cpu and of that slice that's been
[5504.18 --> 5506.54]  given there's a high degree of usage
[5506.54 --> 5508.18]  being used I wasn't really sure
[5508.18 --> 5509.90]  anyways that's all this shows about
[5509.90 --> 5511.16]  I was just kind of curious that is a
[5511.16 --> 5512.56]  possibility too you'd have to look at
[5512.56 --> 5514.14]  the command that was run because
[5514.14 --> 5515.88]  there is a way to set cpu and memory
[5515.88 --> 5518.48]  limits on a container okay I'd like to
[5518.48 --> 5519.34]  know more about that do you have a
[5519.34 --> 5522.38]  video about that um actually no so I'm
[5522.38 --> 5524.18]  gonna put that in my drafts put in your
[5524.18 --> 5526.14]  drafts man and when you when you post
[5526.14 --> 5528.14]  it tell me and I'll help you title it
[5528.14 --> 5529.88]  yeah I was gonna say maybe I'll put
[5529.88 --> 5532.88]  Adam in the title so he finds it I'm
[5532.88 --> 5534.82]  not searching for myself out there help
[5534.82 --> 5536.98]  Adam with docker and then all the
[5536.98 --> 5539.44]  results come back there you go what can
[5539.44 --> 5540.80]  we do to get more people to do these
[5540.80 --> 5541.80]  two each year that's what I want to
[5541.80 --> 5543.68]  know can we just keep doing podcasts
[5543.68 --> 5546.54]  about it every other year or so just
[5546.54 --> 5548.76]  constantly that's it just do a uh a
[5548.76 --> 5551.92]  watch you know or sleep seven or watch
[5551.92 --> 5553.26]  I don't know how does watch work
[5553.26 --> 5555.44]  exactly Nick in terms of how often it
[5555.44 --> 5557.24]  runs does it run every second so I
[5557.24 --> 5558.68]  think it might be a second or two by
[5558.68 --> 5560.70]  default but there is a flag to to you
[5560.70 --> 5562.62]  can set the interval and then it'll
[5562.62 --> 5564.26]  just like output new changes and let
[5564.26 --> 5565.32]  you know when it changed like there's a
[5565.32 --> 5567.34]  little time stamp that happens yeah I
[5567.34 --> 5568.72]  use in the past I know Gerhard use it
[5568.72 --> 5570.04]  all the time I think it's a great way to
[5570.04 --> 5571.36]  basically build your own little
[5571.36 --> 5574.44]  stateful yeah command right like you're
[5574.44 --> 5575.94]  taking a stateless command and you're
[5575.94 --> 5577.94]  just running it on repeat which is like
[5577.94 --> 5580.32]  what is a user interface if not some
[5580.32 --> 5581.94]  sort of event loop with things
[5581.94 --> 5583.54]  updating at a frame rate you know
[5583.54 --> 5586.38]  you're basically doing that by using
[5586.38 --> 5588.60]  the watch command which exists on every
[5588.60 --> 5590.94]  Unix like system probably out there
[5590.94 --> 5593.32]  today yeah that demo he gave us was the
[5593.32 --> 5595.16]  bomb did that make it to YouTube yet
[5595.16 --> 5597.18]  uh it's in the drafts folder it's gonna
[5597.18 --> 5599.70]  hit YouTube this was our recent Kaizen
[5599.70 --> 5602.52]  Nick Gerhard demoed a pipe dream of mine
[5602.52 --> 5604.74]  and he did a really good job he actually
[5604.74 --> 5608.74]  had an entire scripted user interface I
[5609.60 --> 5610.88]  mean I'm sure I actually don't know how
[5610.88 --> 5612.50]  he put it together it was a script but it
[5612.50 --> 5615.22]  had a lot of it was magical had colors it
[5615.22 --> 5616.78]  had state I think it was just running
[5616.78 --> 5618.74]  different user prompts throughout which
[5619.34 --> 5622.20]  we'll put on YouTube but I'm not sure
[5622.20 --> 5623.74]  how Gerhard did that he probably used
[5624.40 --> 5628.44]  dagger that'd be my guess if I if I know
[5628.44 --> 5630.04]  Gerhard he probably used dagger well you're
[5630.04 --> 5633.16]  talking about watching Docker stats have
[5633.16 --> 5635.12]  you seen this lazy Docker one I know this
[5635.12 --> 5637.24]  was in the list it's in my list I did not
[5637.24 --> 5640.02]  try it yet but it's on my list to do so
[5640.02 --> 5643.34]  there's three tools built by Jesse
[5643.34 --> 5648.68]  Duffield lazy Docker lazy get and lazy
[5648.68 --> 5651.88]  NPM and they're all of a similar ilk of
[5651.88 --> 5653.82]  course sponsored by warp which is
[5653.82 --> 5657.40]  interesting warp is sponsoring Jesse's
[5657.40 --> 5659.72]  work on these things you can tell because
[5659.72 --> 5661.82]  there's a big special things to warp in
[5661.82 --> 5665.74]  the readme and it looks a lot like your
[5665.74 --> 5667.78]  Docker stats there Nick except for it's
[5667.78 --> 5669.50]  interactive you can select different
[5669.50 --> 5672.36]  images and see more information you can
[5672.36 --> 5674.14]  just watch the animated gif there in the
[5674.14 --> 5675.66]  readme if you haven't yet to see what I'm
[5675.66 --> 5677.56]  talking about would that be something
[5677.56 --> 5679.00]  that you'd be interested in using or I
[5679.00 --> 5680.38]  mean are you just good to go already
[5680.38 --> 5681.58]  because I know you're kind of shying away
[5681.58 --> 5683.38]  from these things but this one looks like
[5683.38 --> 5684.94]  it's pretty useful I mean I guess it
[5684.94 --> 5687.50]  would be when would I use it like what
[5687.50 --> 5689.04]  would be the use case that would be like
[5689.04 --> 5690.74]  okay now I got to use this because I do
[5690.74 --> 5692.74]  know like for example the other month I
[5692.74 --> 5694.32]  was doing a Kubernetes update you know
[5694.32 --> 5696.88]  just updating from version whatever 1.28
[5696.88 --> 5700.06]  to 1.29 and that process when you have
[5700.06 --> 5701.76]  your own Kubernetes worker nodes requires
[5701.76 --> 5703.06]  like creating new nodes you need to join
[5703.06 --> 5704.40]  the cluster and there's like a whole like
[5704.40 --> 5705.92]  you know sequence of events that happen
[5705.92 --> 5707.64]  in that case yeah I just used Kubernetes
[5707.64 --> 5710.52]  like watch flag on like the nodes list so
[5710.52 --> 5712.42]  I can see these new nodes coming up when
[5712.42 --> 5714.38]  are they being like drained when you know
[5714.38 --> 5716.28]  when are they ready and stuff like that so
[5716.28 --> 5717.94]  it's like little one-offs like that I
[5717.94 --> 5719.60]  don't know like watch goes pretty far but
[5719.60 --> 5722.06]  here yeah I don't know I'm curious to
[5722.06 --> 5723.40]  either of you have a use case in mind
[5723.40 --> 5725.50]  where you would use this tool I don't
[5725.50 --> 5729.52]  use Docker okay took the easy way out
[5729.52 --> 5732.56]  he's hardcore against Docker I'm not I
[5732.56 --> 5736.08]  just don't like it very much I tend to I
[5736.08 --> 5738.06]  have one machine that I have more than
[5738.06 --> 5739.92]  one Docker container running on and it's
[5739.92 --> 5742.52]  like the one machine that's like it does
[5742.52 --> 5745.62]  like home assistant and like other
[5745.62 --> 5747.56]  automation stuff and it's it's sort of
[5747.56 --> 5749.42]  like not in a good state because I don't
[5749.42 --> 5751.76]  have time to tinker with it but I do have
[5751.76 --> 5755.18]  a single machine that is a VM that is
[5755.18 --> 5757.74]  intended to be more beefy for multiple
[5757.74 --> 5759.56]  applications running a Docker and I think
[5759.56 --> 5762.10]  in those cases I would want something
[5762.10 --> 5763.68]  like that because then you have maybe a
[5763.68 --> 5765.60]  Docker network you've got multiple
[5765.60 --> 5767.06]  applications you've got different things
[5767.06 --> 5769.44]  happening at least on that machine and
[5769.44 --> 5772.74]  it's kind of like htop or btop plus plus
[5772.74 --> 5775.32]  or bash top for Docker essentially you're
[5775.32 --> 5777.74]  seeing your services the containers that
[5777.74 --> 5779.10]  are running the images that they're
[5779.10 --> 5781.70]  using config stats it's kind of like that
[5781.70 --> 5784.84]  for Docker logs I mean I don't know if I
[5784.84 --> 5786.12]  would dig into it that was really
[5786.12 --> 5788.00]  cracking open at least once or twice just
[5788.00 --> 5790.82]  to just to see how cool it is to to
[5790.82 --> 5793.36]  command this world you know yeah to have a
[5793.36 --> 5795.08]  single box for all these services no it
[5795.08 --> 5796.48]  is nice because I mean even like Docker
[5796.48 --> 5798.46]  desktop is like the GUI version to look at
[5798.46 --> 5799.70]  some things about your containers and
[5799.70 --> 5801.50]  images and volumes and stuff yeah and it
[5801.50 --> 5803.88]  it displays you know similar-ish things
[5803.88 --> 5805.70]  but here is like that same information on
[5805.70 --> 5807.26]  the command line so it is nice well you
[5807.26 --> 5808.80]  need that for a headless machine so in
[5808.80 --> 5810.84]  these in this case I'm SSHing into it
[5810.84 --> 5813.08]  there is no right you know you need a
[5813.08 --> 5814.72]  TUI and that's a great actually a good
[5814.72 --> 5816.02]  example of like where a TUI really
[5816.02 --> 5817.80]  applies is like when you're just SSHing
[5817.80 --> 5821.16]  into a box that has no monitor or no
[5821.16 --> 5826.46]  GUI you need a TUI no GUI get a TUI
[5826.46 --> 5829.44]  and and here's the biggest pitch ever to
[5829.44 --> 5831.98]  use lazy Docker it looks like DHH is a
[5831.98 --> 5833.66]  sponsor so his avatar is in there on the
[5833.66 --> 5834.08]  read me file
[5834.08 --> 5837.86]  well let me give you the actual pitch
[5837.86 --> 5840.16]  because Jesse has taken a moment to read
[5840.16 --> 5843.04]  or to write an elevator pitch and I'm
[5843.04 --> 5844.36]  gonna read this to you Nick and you tell
[5844.36 --> 5847.14]  me if he sells you or not he says minor
[5847.14 --> 5849.14]  rant incoming something's not working
[5849.14 --> 5851.70]  maybe a service is down Docker compose
[5851.70 --> 5854.70]  PS yep it's that microservice is still
[5854.70 --> 5856.70]  buggy no issue I'll just restart it
[5856.70 --> 5860.06]  Docker compose restart okay now let's
[5860.06 --> 5861.74]  try again oh wait the issue is still
[5861.74 --> 5864.92]  there hmm Docker compose PS right so the
[5864.92 --> 5865.92]  service must have just stopped
[5865.92 --> 5867.78]  immediately after starting I probably
[5867.78 --> 5869.44]  would have known if I was reading a
[5869.44 --> 5870.56]  log stream but there is a lot of
[5870.56 --> 5872.72]  clutter in there from other services I
[5872.72 --> 5874.20]  could get the logs for just that one
[5874.20 --> 5875.90]  service with Docker compose logs dash
[5875.90 --> 5878.84]  dash follow microservice but that dies
[5878.84 --> 5880.54]  every time the service dies so I need to
[5880.54 --> 5881.90]  run that command every time I restart
[5881.90 --> 5884.58]  the service I could alternatively run
[5884.58 --> 5887.36]  Docker compose up my service and in that
[5887.36 --> 5889.08]  terminal window if the service is down I
[5889.08 --> 5891.54]  could just up it again but now I've got
[5891.54 --> 5893.54]  one service hogging a terminal window even
[5893.54 --> 5896.14]  after I no longer care about its logs this
[5896.14 --> 5898.08]  sounds like an infomercial it's such a
[5898.08 --> 5900.26]  pain but wait there's more yeah I guess
[5900.26 --> 5902.14]  when I want to reclaim the terminal real
[5902.14 --> 5905.44]  estate I can do control P Q but wait
[5905.44 --> 5907.72]  that's not working for some reason should I
[5907.72 --> 5910.26]  use control C instead I can't remember if
[5910.26 --> 5912.12]  that closes the foreground process or
[5912.12 --> 5914.60]  kills the actual service what a headache
[5914.60 --> 5917.80]  this is a infomercial he says memorizing
[5917.80 --> 5920.16]  Docker commands is hard memorizing
[5920.16 --> 5922.86]  aliases is slightly less hard keeping
[5922.86 --> 5924.84]  track of your containers across multiple
[5924.84 --> 5928.00]  terminal windows is near impossible what
[5928.00 --> 5929.80]  if you had all the information you needed in
[5929.80 --> 5932.66]  one terminal window with every common
[5932.66 --> 5935.72]  command living one key press away and the
[5935.72 --> 5938.62]  ability to add custom commands as well lazy
[5938.62 --> 5941.42]  Docker's goal is to make that dream a
[5941.42 --> 5944.28]  reality sounds like Jesse needs to start
[5944.28 --> 5946.16]  using T-mox then his terminal problems
[5946.16 --> 5950.20]  go away this is true this is true no but
[5950.20 --> 5952.20]  seriously I will say like I tried not to
[5952.20 --> 5953.90]  read it along like I was just listening to
[5953.90 --> 5955.84]  you and like uh-huh the way you handle
[5955.84 --> 5957.68]  some of those objections what was it the
[5957.68 --> 5959.08]  first one to be like oh I'll just like
[5959.08 --> 5961.40]  follow that service or maybe I'll just up
[5961.40 --> 5963.04]  that one thing like those were things
[5963.04 --> 5964.54]  going in my mind so I think it did a
[5964.54 --> 5966.44]  great job at just demonstrating like the
[5966.44 --> 5968.02]  usefulness of it yeah like you literally
[5968.02 --> 5971.22]  do those things and it works for you and
[5971.22 --> 5972.70]  he obviously knows how to do those
[5972.70 --> 5974.66]  things as well it is a pretty good
[5974.66 --> 5976.18]  elevator pitch but there's something
[5976.18 --> 5979.48]  about knowing the pain of something
[5979.48 --> 5981.68]  enough that you just do it and you kind
[5981.68 --> 5983.64]  of just become calloused to the pain and
[5983.64 --> 5985.10]  you're like well that's just what I do I
[5985.10 --> 5986.58]  do the Docker and Compose PS thing and
[5986.58 --> 5988.82]  then I do that thing but yeah T-mox does
[5988.82 --> 5990.54]  solve a few of these problems I feel like
[5990.54 --> 5991.74]  you're indirectly telling me to like
[5991.74 --> 5993.42]  upgrade my computer already because all
[5993.42 --> 5996.08]  the pain of experience I told you that
[5996.08 --> 5997.80]  directly about an hour ago so I wouldn't
[5997.80 --> 6000.80]  need to be so coy no but yeah if you had a
[6000.80 --> 6002.10]  production server we had a whole bunch of
[6002.10 --> 6003.48]  different containers running like nine
[6003.48 --> 6004.74]  in kubernetes or something and you just
[6004.74 --> 6006.74]  want to have an outlook of all of your
[6006.74 --> 6008.62]  Docker related things yeah I can
[6008.62 --> 6009.80]  definitely see that being useful because
[6009.80 --> 6011.18]  you're right it is annoying to like up
[6011.18 --> 6012.94]  arrow enter control C up arrow and
[6012.94 --> 6014.50]  switch the tab do this thing if I can
[6014.50 --> 6015.80]  just look at a screen and monitor that
[6015.80 --> 6018.16]  stuff that is a win that is a quality of
[6018.16 --> 6020.76]  life improvement right all right so we're
[6020.76 --> 6021.98]  selling it here Adam we're getting them
[6021.98 --> 6024.54]  over to our side the two we world slowly
[6024.54 --> 6026.96]  but surely I've moved to about 10% now
[6026.96 --> 6028.36]  at the start of the show I was at like
[6028.36 --> 6030.74]  two resistance is futile all will be
[6030.74 --> 6032.62]  assimilated by the way earlier you
[6032.62 --> 6034.78]  mentioned that you know Adam you wanted
[6034.78 --> 6036.06]  to get a little bit more interest in
[6036.06 --> 6038.04]  folks like contributing towards the TUI
[6038.04 --> 6040.96]  ecosystem of things and I think you
[6040.96 --> 6042.16]  guys joked around about starting a
[6042.16 --> 6043.88]  podcast around now and but you guys do
[6043.88 --> 6045.42]  have ship it so I think you need to
[6045.42 --> 6049.92]  start like TUI it mmm TUI it well
[6049.92 --> 6053.06]  that's not our game man no I like your
[6053.06 --> 6054.36]  ideas but that's not our game what's
[6054.36 --> 6056.14]  our game I don't know I think I would
[6056.14 --> 6058.28]  actually really encourage will to do
[6058.28 --> 6060.72]  that kind of podcast because Jared and
[6060.72 --> 6062.54]  I are not the epicenter of that I think
[6062.54 --> 6064.40]  we would welcome him on the show and
[6064.40 --> 6065.64]  encourage them to create their own
[6065.64 --> 6068.58]  content because that's their world in my
[6068.58 --> 6070.40]  opinion and I would support it from
[6070.40 --> 6073.34]  externally and report to the masses but
[6073.34 --> 6077.08]  not be the like I suppose if I had TUI
[6077.08 --> 6079.38]  ink and I was trying to build the next
[6079.38 --> 6081.44]  big thing on top of TUI's and there
[6081.44 --> 6082.78]  was some sort of advantage there than
[6082.78 --> 6085.82]  I would but our advantage is keep the
[6085.82 --> 6087.10]  main thing the main thing and the main
[6087.10 --> 6090.12]  thing is not TUI's the main thing is I
[6090.12 --> 6091.52]  would suppose like developer culture
[6091.52 --> 6093.88]  developer happiness the latest tech
[6093.88 --> 6096.86]  that's evolving where trends are going
[6096.86 --> 6099.20]  why should we care those kinds of
[6099.20 --> 6101.76]  questions but I don't discredit the
[6101.76 --> 6104.48]  idea just not for us okay what would
[6104.48 --> 6107.02]  you name said podcast I mean I obviously
[6107.02 --> 6108.64]  you said Tui it but I think that's a
[6108.64 --> 6110.60]  terrible name myself no offense Tui up
[6110.60 --> 6113.56]  Tui up yeah a little better not Tui
[6113.56 --> 6119.12]  down about uh Tui for Tui for Yui I bet
[6119.12 --> 6122.38]  you Tui.fm is available I mean just to
[6122.38 --> 6124.72]  keep it super short URL yeah that'd be
[6124.72 --> 6130.54]  cool Tui.fm or Tui FTW.fm you know
[6130.54 --> 6131.94]  that'd be a good company name Tui for the
[6131.94 --> 6134.56]  Nick if we find if we land on a good
[6134.56 --> 6136.04]  name here Adam's gonna completely
[6136.04 --> 6137.94]  change from okay we're doing this not
[6137.94 --> 6139.64]  our game to this is our totally our
[6139.64 --> 6142.16]  game we need to make this podcast oh my
[6142.16 --> 6144.64]  gosh I'll stop there stop with a really
[6144.64 --> 6146.68]  bad name like Tui for Yui yeah you've
[6146.68 --> 6149.04]  won the worst name possible yeah I did I
[6149.04 --> 6152.78]  beat you on the Tui it well I think Tui's
[6152.78 --> 6154.48]  are fun I think I would summarize it I
[6154.48 --> 6155.48]  don't know how much more deeper want to
[6155.48 --> 6157.06]  go back I think I think we're plenty
[6157.06 --> 6158.98]  deep there is a place for more Tui's
[6158.98 --> 6162.14]  out there I do enjoy a good Tui and if
[6162.14 --> 6167.16]  it was a sandwich or a meal of sorts like
[6167.16 --> 6171.22]  a Tui sandwich num num num you know all
[6171.22 --> 6172.96]  day long give it to me this is a
[6172.96 --> 6175.00]  Spanglish callback if it were a sandwich
[6175.00 --> 6176.52]  or some food what would it actually
[6176.52 --> 6178.20]  taste like like how would you describe
[6178.20 --> 6182.86]  Tui as a taste bright flavorful lots of
[6182.86 --> 6187.12]  flavor scrumptious yummy gimme gimme gimme
[6187.12 --> 6191.28]  I'm not gonna wade into that pool we're
[6191.28 --> 6193.34]  gonna let Adam have the final say on
[6193.34 --> 6197.60]  that all right Nick anything else you
[6197.60 --> 6199.92]  want to say about this or any topic
[6199.92 --> 6202.22]  before we let you go no I think this was
[6202.22 --> 6204.20]  a really fun episode I learned some new
[6204.20 --> 6206.46]  things I may need to explore Tui's in a
[6206.46 --> 6208.74]  little bit more detail yeah there is one
[6208.74 --> 6210.60]  thing I want to say before we go can I
[6210.60 --> 6212.22]  say one more thing just I think this is
[6212.22 --> 6215.22]  worth sharing this is the installation
[6215.22 --> 6218.58]  process you can't just get the Tui right
[6218.58 --> 6220.78]  you have to get the install process
[6220.78 --> 6222.30]  right and I don't know how you all feel
[6222.30 --> 6224.46]  but if the only way to install is via
[6224.46 --> 6228.02]  npm you're doing it wrong is that is
[6228.02 --> 6229.44]  that can we do an unpopular opinion
[6229.44 --> 6231.12]  I feel like that's like that's a popular
[6231.12 --> 6232.98]  opinion I'm terrible at unpopular opinions
[6232.98 --> 6235.92]  I am so with you on that one yeah I will
[6235.92 --> 6238.78]  not if I have to install node to install
[6238.78 --> 6240.70]  your tool and it's nothing against node
[6240.70 --> 6241.98]  this could happen to Ruby or whatever
[6241.98 --> 6243.94]  like it's the same thing I much prefer
[6243.94 --> 6246.16]  either you know give me a binary I can
[6246.16 --> 6248.90]  just curl down and run it or yeah if
[6248.90 --> 6250.22]  you have built-in package manager
[6250.22 --> 6253.42]  support for my OS that's nice too yeah I
[6253.42 --> 6255.60]  didn't mind the the process that I
[6255.60 --> 6258.62]  mentioned for btop or bash top I should
[6258.62 --> 6261.18]  say and that may have been dated which
[6261.18 --> 6263.76]  was to to do the add app repository and
[6263.76 --> 6266.08]  the PPA version of it and then literally
[6266.08 --> 6268.40]  update apt and then install the bash top
[6268.40 --> 6270.58]  application I didn't mind that
[6270.58 --> 6274.12]  but don't make me use a thing that's not
[6274.12 --> 6275.48]  even intended to be on my system that
[6275.48 --> 6277.48]  has no place on my system because it's
[6277.48 --> 6279.44]  not my desktop it's maybe a remote
[6279.44 --> 6282.20]  machine or a standalone VM that I just
[6282.20 --> 6283.30]  don't want to have I want to keep it
[6283.30 --> 6286.42]  minimized and if the only way to install
[6286.42 --> 6290.94]  is via only node or npm then I don't
[6290.94 --> 6292.92]  like that I want to have a native way to
[6292.92 --> 6295.18]  install it for my system yeah I think a
[6295.18 --> 6296.58]  great point around that one too is just
[6296.58 --> 6299.10]  like adaptability or adaptability of a
[6299.10 --> 6300.78]  tool at maybe like an organization
[6300.78 --> 6302.04]  because right now the place I work at
[6302.04 --> 6304.16]  you know we've got 15 developers and you
[6304.16 --> 6306.04]  know we're allowed to have macOS we can
[6306.04 --> 6307.68]  have data Linux you can have Windows with
[6307.68 --> 6309.88]  WSL you know these are all viable setups
[6309.88 --> 6311.12]  that you can have as your dev environment
[6311.12 --> 6314.06]  and if I'm writing a script or a tool to
[6314.06 --> 6316.24]  help automate setting up tools on any of
[6316.24 --> 6318.66]  those devices you know it is nice to have
[6318.66 --> 6321.04]  a way like go to GitHub release pages for
[6321.04 --> 6323.16]  the project and just download that binary
[6323.16 --> 6326.10]  for that CPU architecture you know that base
[6326.10 --> 6328.24]  operating system and then that will just
[6328.24 --> 6329.94]  work and there's little variables you know
[6329.94 --> 6331.46]  you can run the command line to like get
[6331.46 --> 6332.78]  those programmatically so you have one
[6332.78 --> 6334.82]  command to run for any system it's going
[6334.82 --> 6337.90]  to be installed on no actual no dependencies
[6337.90 --> 6339.70]  or if conditions or whatever I think that
[6339.70 --> 6341.66]  goes a reasonably long ways yeah I definitely
[6341.66 --> 6342.80]  want to pay attention to the install
[6342.80 --> 6345.44]  process I would say installation and
[6345.44 --> 6347.64]  initial usage is to me is key for any
[6347.64 --> 6350.00]  to it might seem obvious it's just simply
[6350.00 --> 6351.92]  type in bashtop for example after you
[6351.92 --> 6353.72]  install it that might seem obvious but at
[6353.72 --> 6355.98]  least give me that next step in your
[6355.98 --> 6357.86]  docs where it's installation for my
[6357.86 --> 6360.28]  system I'm cool with brew I'm cool with
[6360.28 --> 6362.66]  whatever else is out there if you have an
[6362.66 --> 6364.36]  Ubuntu system or you're using apt you
[6364.36 --> 6366.58]  know give me that apt flavor if it's a
[6366.58 --> 6368.02]  binary and you want me to pipe it in the
[6368.02 --> 6369.60]  bash I'm cool with that too I'll
[6369.60 --> 6371.22]  obviously check the file first before I
[6371.22 --> 6374.50]  do that because hey that's just crazy or
[6374.50 --> 6375.90]  check the source code and just double
[6375.90 --> 6378.14]  check that but then after that like
[6378.14 --> 6379.86]  what's the very first next step to
[6379.86 --> 6381.94]  enjoying the tool what's the config like
[6381.94 --> 6384.00]  what's the setup like and I think for
[6384.00 --> 6386.80]  any Tui that is that's just like how
[6386.80 --> 6388.32]  you document it how you get people into
[6388.32 --> 6390.62]  it yeah I'm a big fan of just you know
[6390.62 --> 6392.18]  seeing the tool being used on something
[6392.18 --> 6393.82]  real like a use case of here's how to
[6393.82 --> 6395.18]  solve this type of problem I love that
[6395.18 --> 6397.84]  stuff but even going back to the
[6397.84 --> 6399.22]  installation Adam would it help like
[6399.22 --> 6400.98]  let's say that the tool is just you
[6400.98 --> 6402.90]  know not a binary you can just install
[6402.90 --> 6404.24]  but you need node or you need something
[6404.24 --> 6406.04]  I think even if they wrapped it up in a
[6406.04 --> 6407.48]  Docker image so you can just run it as
[6407.48 --> 6409.02]  a container quickly at least to get a
[6409.02 --> 6410.74]  feel for the tool like day one I
[6410.74 --> 6411.98]  think that goes kind of a long ways
[6411.98 --> 6413.56]  it'd be kind of interesting actually
[6413.56 --> 6415.08]  to have a demo as a Docker image
[6415.08 --> 6417.58]  because you can set up like your own
[6417.58 --> 6418.90]  little dummy file system there if it
[6418.90 --> 6421.36]  required you know some demo data
[6421.36 --> 6423.46]  basically and provide a world where
[6423.46 --> 6424.98]  you're like hey let me try this out and
[6424.98 --> 6427.28]  I don't have to like muck up my my
[6427.28 --> 6429.00]  install like my machine keep it
[6429.00 --> 6431.58]  vanilla keep it pristine because even
[6431.58 --> 6433.50]  like on a VM before I do some of this
[6433.50 --> 6435.42]  stuff I'll I will back up that VM if
[6435.42 --> 6437.32]  it's necessary you can't back up a
[6437.32 --> 6438.54]  machine pretty easily but you can do
[6438.54 --> 6441.10]  that with a VM on Proxmox or a cloud
[6441.10 --> 6443.70]  box or whatever I like that because
[6443.70 --> 6445.46]  you can easily now that assumes you've
[6445.46 --> 6447.46]  got Docker that's a pretty good
[6447.46 --> 6449.26]  assumption of most developer machines
[6449.26 --> 6451.00]  these days aside from Jared's like he's
[6451.00 --> 6453.72]  just like don't even touch my machine
[6453.72 --> 6457.52]  with D O C K E R get it out of here no
[6457.52 --> 6459.16]  Docker here you know it's just too slow
[6459.16 --> 6460.94]  I have Docker installed oh you do have
[6460.94 --> 6462.38]  it installed okay never mind I just
[6462.38 --> 6464.56]  don't want to I still want to but I
[6464.56 --> 6466.56]  have to because I'm a developer and
[6466.56 --> 6468.18]  sometimes you just need it so talk
[6468.18 --> 6470.68]  Docker one basically yeah they won
[6470.68 --> 6472.82]  they won big time but I'm with you if
[6472.82 --> 6474.02]  you had a Docker image it's like hey
[6474.02 --> 6475.56]  let me play with this that'd be kind of
[6475.56 --> 6477.92]  cool I think it'd be good for mileage
[6477.92 --> 6479.86]  for new adoption probably good for
[6479.86 --> 6484.40]  mileage potentially even a dev setup to
[6484.40 --> 6487.34]  maybe more easily contribute it can be a
[6487.34 --> 6489.82]  dual facing use case for using Docker
[6489.82 --> 6492.20]  in that case like a demo as well as
[6492.20 --> 6494.88]  maybe contribution yeah I actually love
[6494.88 --> 6496.00]  that that's another angle that's really
[6496.00 --> 6497.48]  important like the more people that can
[6497.48 --> 6499.52]  contribute towards the project even just
[6499.52 --> 6500.98]  like opening up a PR to like do some
[6500.98 --> 6502.68]  small patch yeah if all I have to do is
[6502.68 --> 6505.12]  just run a container and that's it
[6505.12 --> 6508.12]  absolutely sign me up yeah I love that
[6508.12 --> 6510.30]  idea a lot honestly like if I could just
[6510.30 --> 6514.44]  dock and pose up anything I'll do it you
[6514.44 --> 6516.92]  just send me a command anything what's
[6516.92 --> 6519.78]  out I'll just do it that's like in the
[6519.78 --> 6522.92]  show Jared just do it just do it send
[6522.92 --> 6524.84]  Adam a command anything that's right
[6524.84 --> 6526.38]  and he'll just do it prefaces with
[6526.38 --> 6530.22]  Docker compose and I will do that all
[6530.22 --> 6532.76]  right well Nick always good to catch up
[6532.76 --> 6535.08]  I think we'll should do more shows like
[6535.08 --> 6537.36]  these with you because it's always fun
[6537.36 --> 6539.14]  yeah thanks a lot for the invite and if
[6539.14 --> 6540.44]  anybody's curious you know we mentioned
[6540.44 --> 6542.02]  I had two and a half gigs of hard drive
[6542.02 --> 6543.50]  space at the start of this episode I've
[6543.50 --> 6546.20]  been recording this locally just as a
[6546.20 --> 6548.16]  backup if needed it still shows that I
[6548.16 --> 6550.02]  have nine hours remaining of disk space
[6550.02 --> 6551.78]  so even though a wave is being output
[6551.78 --> 6554.50]  we're still pretty efficient wow wow
[6554.50 --> 6556.18]  even on that old hardware you're doing
[6556.18 --> 6558.56]  good keep going then yeah we're just
[6558.56 --> 6560.68]  nine hours away from from denial of
[6560.68 --> 6562.66]  servicing him that's right that's right
[6562.66 --> 6566.60]  that's a slow motion DOS no go ahead
[6566.60 --> 6568.18]  but I was gonna say yeah thanks again
[6568.18 --> 6569.84]  for the invite and happy to come on
[6569.84 --> 6571.62]  whenever you want awesome well you're a
[6571.62 --> 6574.14]  friend you're welcome here anytime that's
[6574.14 --> 6575.72]  right bye friends all right bye
[6575.72 --> 6576.04]  friends
[6576.04 --> 6582.92]  okay that's it for this week's developer
[6582.92 --> 6585.22]  pods from changelog hope you enjoyed
[6585.22 --> 6587.26]  them awesome having Nick back talking
[6587.26 --> 6589.46]  about two is this time text user
[6589.46 --> 6592.52]  interfaces I love them I hope they
[6592.52 --> 6595.02]  become more in vogue but only time will
[6595.02 --> 6597.80]  tell we do have a bonus for this episode
[6597.80 --> 6600.62]  for a plus plus subscribers learn more at
[6600.62 --> 6603.64]  changelog.com slash plus plus it's better
[6603.64 --> 6606.10]  some say it is better I think it's
[6606.10 --> 6608.36]  better but you should try it out see for
[6608.36 --> 6610.34]  yourself 10 bucks a month 100 bucks a
[6610.34 --> 6612.86]  year drop the ads directly support us
[6612.86 --> 6615.36]  get bonus content get closer to that
[6615.36 --> 6617.62]  cool changelog medal and of course get a
[6617.62 --> 6619.86]  free sticker pack sent directly to you
[6619.86 --> 6623.24]  that's awesome again changelog.com slash
[6623.24 --> 6625.02]  plus plus well we couldn't do this without
[6625.02 --> 6627.36]  awesome sponsors and awesome partners
[6627.36 --> 6630.82]  today's sponsors are chronitor century and
[6630.82 --> 6633.20]  paragon if you try out century use the
[6633.20 --> 6635.08]  code changelog and get 100 bucks off for
[6635.08 --> 6637.40]  three months and of course a massive
[6637.40 --> 6640.84]  thank you to our friends over at fly.io
[6640.84 --> 6643.78]  pull your apps near users too easy learn
[6643.78 --> 6647.52]  more at fly.io and to the beat freak in
[6647.52 --> 6649.52]  residence brake master cylinder thank you
[6649.52 --> 6651.48]  for those awesome beats that's it the
[6651.48 --> 6653.66]  show's done we'll see you next week
[6653.66 --> 6670.74]  actually it's a quick closing remark that's
[6670.74 --> 6672.72]  maybe interesting around you know good
[6672.72 --> 6675.58]  stuff for free so when I was actually
[6675.58 --> 6678.50]  traveling around Portugal I was on the top
[6678.50 --> 6681.20]  of some castle I think it was St. George's
[6681.20 --> 6682.66]  castle I'm probably butchering the
[6682.66 --> 6684.30]  pronunciation but I was wearing the
[6684.30 --> 6686.26]  changelog shirt that you guys sent me the
[6686.26 --> 6688.34]  very first time I was on the show yes and
[6688.34 --> 6690.10]  that is one of my favorite shirts honestly
[6690.10 --> 6691.92]  like I wear it kind of frequently and this
[6691.92 --> 6693.68]  guy was just like cool shirt and I was
[6693.68 --> 6695.58]  like thank you and he's like I'm familiar
[6695.58 --> 6696.80]  with the show I've watched so many different
[6696.80 --> 6699.06]  episodes he knows who both of you are and
[6699.06 --> 6701.32]  get out of here yeah that weird no it was
[6701.32 --> 6703.92]  really cool yeah on a castle in Portugal yeah
[6703.92 --> 6707.06]  that's a small world I guess but it made me
[6707.06 --> 6709.52]  think like the only reason I accepted your
[6709.52 --> 6711.10]  invite to go on the show was to potentially
[6711.10 --> 6713.22]  get another awesome high quality free shirt
[6713.22 --> 6716.16]  the only reason well now you're not getting
[6716.16 --> 6718.24]  one well yeah now we have to do with your
[6718.24 --> 6720.54]  thank you code we're gonna do the we're
[6720.54 --> 6723.24]  gonna set the flag to to uh to no coupon code
[6723.24 --> 6725.96]  to not send him the coupon code yeah just to
[6725.96 --> 6727.64]  spite you you're gonna adjust the price so
[6727.64 --> 6729.48]  it's actually twice expensive so like I can't
[6729.48 --> 6731.10]  get it the function is called has one or
[6731.10 --> 6734.28]  not and you already have one so you get not
[6734.28 --> 6736.66]  no the other the the toggle is like has
[6736.66 --> 6738.52]  he spited us that's right and you just
[6738.52 --> 6742.34]  spited us so oh man check yourself man
[6742.34 --> 6745.20]  ultimate backfires but seriously do you
[6745.20 --> 6747.76]  guys have a different a different inventory
[6747.76 --> 6749.44]  of shirts or is it the same well it depends
[6749.44 --> 6752.32]  on which one you got do you have the OG I
[6752.32 --> 6754.20]  have the cool I don't know if it's OG but
[6754.20 --> 6756.18]  it has the globe and it says change log same
[6756.18 --> 6758.10]  one yeah we haven't changed but you can get
[6758.10 --> 6760.50]  a jazz party if maybe or you can get
[6760.50 --> 6762.24]  yourself a Kaizen shirt or a tail scale t-shirt
[6762.24 --> 6764.48]  we don't sell skills that's what I'm
[6764.48 --> 6764.70]  wearing
[6764.70 --> 6767.94]  Adam will send you a tail scale off his
[6767.94 --> 6770.34]  back yeah so you could get a practically
[6770.34 --> 6771.84]  I saw you don't have to get the change
[6771.84 --> 6773.68]  log one so you'd have to you can get a
[6773.68 --> 6775.22]  different version you get a Kaizen a few
[6775.22 --> 6776.74]  more Kaizens out there whatever you like
[6776.74 --> 6778.62]  man hook yourself up you have to have the
[6778.62 --> 6780.50]  special link to get the Kaizen cool I was
[6780.50 --> 6781.56]  trying to give you guys a free plug on
[6781.56 --> 6783.32]  your awesome shirts no I loved it and
[6783.32 --> 6784.72]  we're just messing with you yeah that's
[6784.72 --> 6787.20]  so cool though honestly to rewind you can
[6787.20 --> 6788.64]  have another t-shirt
[6788.64 --> 6802.18]  and
