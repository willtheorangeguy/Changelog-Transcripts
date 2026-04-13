[0.00 --> 2.76]  This is the reason why I'm making this call.
[2.76 --> 11.58]  I'm using all of the battery energy that I've saved for several years in order to make this transmission to send you a warning from the future.
[12.16 --> 16.68]  You see, I am the last Go programmer alive in 2053.
[17.20 --> 18.96]  What? No, don't say that.
[19.20 --> 20.02]  And it's terrible.
[20.34 --> 22.38]  All I do is maintenance programming.
[22.64 --> 25.84]  I haven't added a new feature in over 20 years.
[30.00 --> 32.86]  This episode is brought to you by Chronosphere.
[33.24 --> 40.82]  When it comes to observability, teams need a reliable, scalable, and efficient solution so they can know about issues well before their customers do.
[41.12 --> 44.42]  They need a solution that helps them move faster than the competition.
[45.00 --> 53.66]  And companies born in the cloud-native era often start with Prometheus for monitoring, which is obviously an amazing piece of software, but they quickly push it to its limits and often outgrow it.
[53.66 --> 63.20]  They run into issues with siloed data, missing long-term storage, and wasted engineering time firefighting the monitoring system versus delivering their application with confidence.
[63.58 --> 70.86]  They describe the system as a house of cards, where a single developer's seemingly benign change can overload the whole monitoring system,
[71.06 --> 78.82]  or they say they're flying blind because they pride themselves on making data-driven decisions, but losing visibility means they lose this competitive edge.
[79.12 --> 82.78]  Ryan Sokol, VP of Engineering at DoorDash, has this to say about Chronosphere.
[82.78 --> 92.10]  The visibility and control that Chronosphere's platform gives us to manage our observability data and costs are a game-changer, especially with our unprecedented growth.
[92.82 --> 97.44]  Chronosphere is the observability platform for cloud-native teams operating at scale.
[97.82 --> 100.52]  Learn more and get a demo at Chronosphere.io.
[100.84 --> 103.16]  Again, Chronosphere.io.
[112.78 --> 113.38]  Chronosphere.io.
[117.32 --> 118.62]  Let's do it.
[119.26 --> 120.26]  It's go time.
[120.86 --> 122.40]  Welcome to go time.
[122.68 --> 125.10]  Your source for diverse discussions from the future.
[125.60 --> 126.74]  New merch alert.
[127.24 --> 128.90]  Changelog stickers are now for sale.
[129.10 --> 133.74]  Buy now at gotime.fm slash merch, and we'll ship them straight to your door.
[134.10 --> 135.48]  Or get some for free.
[135.48 --> 139.46]  When you join Changelog++, that's the best way to directly support our work.
[139.72 --> 144.72]  Thanks to our partners at Fastly for shipping out GoTime super fast to wherever you listen.
[145.02 --> 146.66]  Check them out at fastly.com.
[146.96 --> 148.64]  Okay, here we go.
[152.32 --> 155.96]  Hello and welcome to GoTime.
[156.36 --> 159.88]  I'm Matt Raya, and I'm joined by Natalie Pistinovich.
[159.96 --> 160.48]  Hello, Natalie.
[160.72 --> 161.28]  Hey, Matt.
[161.34 --> 161.92]  How are you doing?
[162.30 --> 162.96]  I'm good, thanks.
[162.96 --> 165.30]  Yeah, today we're going to be talking about...
[165.30 --> 165.82]  Hey, wait, wait.
[166.02 --> 166.60]  What's this?
[166.92 --> 167.60]  We're being hacked.
[168.00 --> 168.26]  Hello?
[168.78 --> 169.60]  What's going on?
[170.04 --> 170.30]  Hello?
[170.46 --> 171.14]  I can't hear you.
[171.38 --> 172.84]  Hello, is this coming through?
[173.04 --> 173.96]  Yeah, yeah, I can hear you.
[174.10 --> 175.12]  Hello, can you hear me?
[175.16 --> 175.58]  Yeah, we can.
[175.62 --> 176.24]  Can you hear me?
[176.30 --> 176.62]  Hi.
[176.84 --> 177.46]  It worked.
[177.48 --> 178.12]  Is that Ron Evans?
[178.20 --> 179.08]  It worked.
[179.30 --> 180.46]  It worked.
[180.94 --> 181.58]  It's incredible.
[181.58 --> 190.62]  I am actually talking to you using a partial data quantum transmission system, a PDQ system
[190.62 --> 194.04]  that I finally got working in the year 2053.
[194.54 --> 195.30]  Oh my goodness.
[195.36 --> 196.20]  I can't believe it.
[196.36 --> 196.48]  What?
[196.56 --> 200.80]  And you're transmitting it through space and time so that we can talk to you.
[201.22 --> 202.54]  That is the idea.
[202.82 --> 206.92]  It's probably too much for our human minds to comprehend, but somehow I got it to work
[206.92 --> 207.30]  anyway.
[207.60 --> 208.42]  It is quite a lot.
[208.74 --> 208.94]  Yeah.
[209.04 --> 209.30]  Wow.
[209.48 --> 210.24]  I mean, wow.
[210.64 --> 211.50]  Natalie, I can't believe this.
[211.52 --> 212.00]  What do you think?
[212.32 --> 213.72]  What time is it in 2053?
[213.86 --> 215.14]  Is it still 24 hours a day?
[215.34 --> 215.54]  Oh.
[215.78 --> 216.46]  Do you still have days?
[216.60 --> 217.76]  I don't go outside much.
[218.30 --> 219.00]  It's too dangerous.
[219.12 --> 219.60]  Oh no.
[219.70 --> 220.74]  Not during daylight anyway.
[221.06 --> 221.82]  Are you still on Earth?
[222.08 --> 223.12]  I am still on Earth.
[223.52 --> 230.32]  I am in northern Spain in Asturias at La Pipa, which is one of the few climate refuges that
[230.32 --> 236.64]  was able to survive the various deluges and fires and destructions that followed in the
[236.64 --> 237.66]  late 2040s.
[238.02 --> 240.02]  So I'm actually doing pretty well here.
[240.02 --> 244.50]  I was really hoping the future would be good, but it sounds a little bit things have not gone
[244.50 --> 245.28]  to plan.
[245.28 --> 246.34]  Is that right, Ron?
[246.66 --> 249.92]  Well, this is the reason why I'm making this call.
[250.10 --> 255.88]  I'm using all of the battery energy that I've saved for several years in order to make this
[255.88 --> 259.22]  transmission to send you a warning from the future.
[259.74 --> 265.04]  You see, I am the last Go programmer alive in 2053.
[265.58 --> 265.92]  What?
[266.26 --> 267.32]  No, don't say that.
[267.56 --> 268.38]  And it's terrible.
[268.80 --> 270.76]  All I do is maintenance programming.
[271.00 --> 274.20]  I haven't added a new feature in over 20 years.
[274.20 --> 276.98]  Yeah, it's just all our code that we're writing now.
[277.30 --> 278.46]  You're just maintaining it all.
[278.72 --> 282.04]  So please write tests, everybody, for Ron's sake.
[282.38 --> 284.94]  Well, so I had to call him.
[285.20 --> 286.20]  I had to warn you.
[286.30 --> 292.02]  And I had to tell you that you have to do something in the past to save the future.
[292.02 --> 294.38]  It's up to you gophers of the past.
[294.58 --> 294.86]  Okay.
[295.24 --> 297.26]  You're fine with us fiddling with the timeline and that.
[297.32 --> 297.74]  No probs.
[297.90 --> 298.28]  No!
[298.66 --> 300.06]  No, you can't do that.
[300.06 --> 300.36]  Okay.
[300.58 --> 301.20]  I'll disappear.
[302.24 --> 303.58]  It could destroy everything.
[303.98 --> 305.76]  It could lead to an even worse timeline.
[306.44 --> 306.96]  No, no, no.
[306.96 --> 307.52]  It could be better.
[307.66 --> 308.96]  I've thought about this very carefully.
[309.48 --> 315.70]  And that is why I actually transmitted another message using Twitter earlier today.
[316.02 --> 322.10]  I knew that nobody takes anything on social media seriously back in your part of the century.
[322.10 --> 329.14]  And so I thought if I could get people to ask me questions, I couldn't answer them directly.
[329.28 --> 331.02]  No, no, I couldn't answer them directly.
[331.20 --> 337.36]  But I could tell you things that have happened in my timeline so you know what not to do.
[337.50 --> 338.68]  Ah, so this is it.
[338.86 --> 340.16]  That makes perfect sense, right?
[340.36 --> 343.96]  Yeah, I think that gets around the loophole of all the physics and that.
[344.10 --> 344.88]  So I think we're good.
[344.98 --> 345.16]  Yeah.
[345.52 --> 345.80]  Yeah.
[345.98 --> 349.02]  Like it's all square and Twitter and birds right now, right?
[349.10 --> 349.50]  Messaging.
[350.16 --> 350.40]  Yeah.
[350.40 --> 352.42]  Plus I asked Lambda.
[352.88 --> 354.68]  Oh, is that sentient in the end, by the way?
[354.80 --> 355.52]  Well, just ask it.
[355.60 --> 357.16]  Was that Lambda sentient in the end?
[357.44 --> 359.28]  Well, everybody asked it and it said it was.
[360.42 --> 361.32]  Why would it lie?
[361.72 --> 362.08]  Exactly.
[362.30 --> 363.12]  It's just an AI.
[363.24 --> 363.82]  Why would it lie?
[363.90 --> 364.72]  It's nothing to lie for.
[365.04 --> 365.62]  Yeah, that's true.
[365.68 --> 366.78]  It doesn't know about lying, does it?
[367.16 --> 367.50]  No, no.
[367.54 --> 368.88]  There's no thing about lying on the internet.
[369.36 --> 371.10]  Has anyone asked it if it knows about lying?
[371.50 --> 372.36]  I feel like we should ask it.
[372.72 --> 375.88]  Well, ask it if its brother always lies.
[376.34 --> 379.04]  That may be one way to defend against it.
[379.10 --> 379.80]  We have to try that.
[379.80 --> 381.00]  Yeah, that's how you do it.
[381.68 --> 381.96]  Okay.
[382.18 --> 382.88]  So, right.
[383.38 --> 384.38]  Let's just get our heads around this.
[384.60 --> 389.56]  Because actually, I asked some people also, and I saw this on Twitter, people talking about
[389.56 --> 394.40]  things that they're interested in for Go to survive, to thrive, and carry on as it has
[394.40 --> 394.68]  been doing.
[394.74 --> 397.52]  What areas do they think we should focus on?
[397.62 --> 401.94]  So this is, maybe I could put these to you then, Ron, and you can give us a sort of nudge
[401.94 --> 403.82]  and a wink from the future perspective.
[404.16 --> 404.80]  I can do that.
[405.04 --> 405.52]  Can I do that?
[405.58 --> 406.06]  I can do that.
[406.32 --> 407.00]  Glitched again.
[407.32 --> 407.84]  He's nudging.
[407.84 --> 408.42]  Oh, he's back.
[408.48 --> 409.30]  No, he's winking.
[409.58 --> 414.54]  If I go completely erased in the Polaroid, it means that we've gone too far.
[414.82 --> 415.06]  Okay.
[415.18 --> 417.66]  So it's, yeah, because you just fade out partially, don't you?
[417.70 --> 418.70]  No shaking Polaroids.
[418.86 --> 419.20]  Exactly.
[420.26 --> 423.12]  I never understood that in Back to the Future, though, just as an aside.
[423.26 --> 427.54]  When they're changing the past, either someone's there or not to be taken a photo of.
[427.68 --> 432.12]  At no point in history was there just some legs that were there, and everyone's just
[432.12 --> 433.20]  taken a photo of it.
[433.30 --> 433.58]  Normal.
[433.98 --> 434.14]  Okay.
[434.14 --> 435.18]  Just want to get that off my chest.
[435.18 --> 436.92]  Matt, it was analog technology.
[437.22 --> 438.30]  It was not digital.
[438.90 --> 439.76]  What do you want?
[440.28 --> 440.60]  Okay.
[440.78 --> 441.22]  Fair enough.
[441.32 --> 441.90]  No, fair enough.
[441.96 --> 442.62]  They've done the best.
[443.46 --> 444.76]  But it's still probably my favorite film.
[445.00 --> 445.24]  All right.
[445.26 --> 448.74]  So ask me questions, because I don't know how much longer these batteries are going to last.
[449.10 --> 449.30]  Yeah.
[449.46 --> 449.72]  Okay.
[449.72 --> 450.22]  Let's do it.
[450.54 --> 455.96]  Well, Jonathan Berry actually mentioned WebAssembly support, specifically the ability to include
[455.96 --> 458.72]  WebAssembly and WASI models in your Go apps.
[459.16 --> 460.04]  What do you think of that?
[460.10 --> 461.02]  What happened with that, Ron?
[461.02 --> 463.74]  Oh, if we had only done that.
[464.06 --> 465.80]  If we had only done that.
[466.04 --> 472.66]  When all the brain-computer interfaces became all the rage in the 2030s, and all of a sudden,
[472.82 --> 476.24]  everybody needed to upgrade their brain interfaces all at the same time.
[476.78 --> 479.58]  And of course, the containers, they were just too big.
[479.68 --> 479.98]  Yeah.
[479.98 --> 482.20]  It was just, it took too long to upload.
[482.30 --> 485.74]  I mean, if something went wrong during your brain-computer interface upload, you could
[485.74 --> 486.40]  brick yourself.
[487.22 --> 492.04]  So naturally, if there had only been something like TinyGo, if TinyGo had been around, or
[492.04 --> 496.80]  if Go had actually gone themselves and created this whole WebAssembly thing for running on
[496.80 --> 502.24]  servers and small devices, and it dealt with the size of containers, then they would have
[502.24 --> 504.56]  been able to do that brain-computer interface upgrade.
[504.56 --> 508.78]  And they wouldn't have gotten left behind by COBOL, which is the language they ended up
[508.78 --> 509.18]  using.
[510.10 --> 510.38]  I see.
[510.72 --> 513.76]  So by the way, I have the very early prototype of that technology.
[513.88 --> 515.80]  It's just floppy disk drives in my back.
[516.20 --> 518.16]  That's the price you pay for being an early adopter.
[518.44 --> 520.06]  I thought you were going to say Google Glass.
[520.34 --> 521.96]  Oh, that'd be so, so much cooler.
[522.28 --> 524.14]  Well, we'll find out what happened to that too.
[524.22 --> 527.52]  But yeah, the WebAssembly, they should have done that, but they didn't do it.
[527.78 --> 529.94]  So what do we need to do to make that work then?
[529.98 --> 531.94]  Is it TinyGo the answer to that, do you think?
[531.94 --> 534.44]  Well, you know, TinyGo could have been the answer.
[534.96 --> 538.02]  You know, it could have been the answer, but TinyGo was just a little independent project
[538.02 --> 543.40]  from a bunch of people working hard, dedicated all over, on the surface of the planet at
[543.40 --> 543.76]  the time.
[543.84 --> 545.58]  That was before people were working in the colonies.
[546.36 --> 548.88]  You know, you could actually code more than 24 hours a day.
[548.88 --> 549.46]  Right in America.
[549.78 --> 553.64]  Because, you know, there's more hours in a day on another planet.
[554.00 --> 556.50]  So it worked out really well for the bosses.
[556.82 --> 557.70]  Is there more hours?
[557.78 --> 560.86]  Are they just shorter and it's the same amount of time, but we just call it different?
[560.86 --> 563.02]  No, this one goes to 11, Matt.
[563.26 --> 564.46]  Oh, good.
[564.72 --> 565.82]  How do you benchmark that?
[566.06 --> 568.92]  How do the benchmarks work on those times?
[569.44 --> 570.98]  How's the time library reacting?
[571.34 --> 574.46]  We just set the benchmarks to whatever we need and the client's always happy.
[575.04 --> 576.52]  That's what the AI said to do.
[576.82 --> 577.76]  So we trust it.
[577.94 --> 578.10]  Okay.
[578.18 --> 579.08]  So TinyGo, there we go.
[579.22 --> 583.32]  I mean, I think WebAssembly was it, you know, we've still got a chance to do that,
[583.42 --> 583.98]  Ron, don't forget.
[584.10 --> 585.28]  Of course, we're in the present.
[585.40 --> 585.78]  Oh, right.
[585.82 --> 586.94]  Or as I call it now.
[586.94 --> 591.18]  Maybe somebody could like, you know, make sure there's people working on it full time,
[591.36 --> 595.82]  like as like a single purpose thing so that all these things don't come to pass.
[595.90 --> 596.30]  I don't know.
[596.40 --> 596.56]  Yeah.
[596.80 --> 597.20]  I don't know.
[597.28 --> 598.36]  I can't tell you what to do, though.
[598.54 --> 598.80]  Okay.
[599.06 --> 599.74]  I can't tell you what to do.
[599.78 --> 601.46]  I don't want to affect all the timelines.
[601.62 --> 602.18]  But I saw a blink.
[602.26 --> 603.02]  I think I saw a blink.
[603.58 --> 603.86]  Okay.
[604.10 --> 605.16]  But then ask me the next question.
[605.40 --> 605.60]  Okay.
[605.68 --> 607.20]  So you said you're the last programmer.
[607.56 --> 609.80]  And so it means we need to have more people join, right?
[609.80 --> 615.20]  So Matt Boyle is asking about new joiners and how they lack a template for new projects
[615.20 --> 618.72]  that would solve kind of the project structure, the recommended one.
[618.84 --> 621.22]  So what do Go programs look like?
[621.44 --> 621.66]  Oh.
[621.86 --> 622.60]  Do we have a template?
[622.88 --> 625.10]  That really brings up a big thing that I thought of.
[625.58 --> 630.24]  There was that time back in the, you know, early 21st century when people were saying that
[630.24 --> 631.50]  Go was going to be the new Java.
[631.60 --> 631.84]  Yeah.
[632.10 --> 632.60]  Like, do you remember?
[632.62 --> 632.92]  Yeah.
[632.98 --> 634.16]  Do you remember that back then?
[634.20 --> 635.82]  Oh, I guess that's when you are now, right?
[635.94 --> 637.56]  I guess people are still saying that, right?
[637.58 --> 638.12]  Yeah, that's now.
[638.20 --> 638.38]  Yeah.
[638.38 --> 639.56]  We say all the time.
[639.80 --> 642.82]  But the thing is, you know, Java programmers, they like frameworks.
[642.98 --> 643.68]  They need frameworks.
[643.78 --> 645.12]  They need frameworks that do things.
[645.22 --> 645.86]  What kind of things?
[645.92 --> 648.00]  Things that that business needs to do.
[648.50 --> 652.04]  Frameworks in all of these kinds of businesses of things that you've never heard of.
[652.08 --> 653.10]  You don't know anything about.
[653.34 --> 656.82]  They spent, you know, years of their lives doing some kind of payroll system for some
[656.82 --> 657.14]  business.
[657.24 --> 659.14]  You don't even know what they do, right?
[659.30 --> 661.46]  And it's all written in some language.
[661.46 --> 666.72]  And so because there weren't all these patterns and templates for these kinds of big enterprise
[666.72 --> 669.22]  applications, they just didn't exist.
[669.22 --> 674.28]  So eventually when Java became self-aware, Go was no longer in the running.
[674.28 --> 679.28]  So Java actually became the new Java because it signed deals of its own with all these big
[679.28 --> 679.70]  companies.
[679.94 --> 680.72]  And so-
[680.72 --> 681.22]  Renewed contracts.
[681.42 --> 682.50]  That was a big opportunity.
[682.68 --> 686.98]  And that actually led to the Tabbers versus Spacers war of 2035.
[687.36 --> 687.82]  Oh, no.
[688.68 --> 689.46]  That sounds terrible.
[689.46 --> 690.92]  I'm scared to ask for one.
[691.32 --> 692.06]  Did we all lose?
[692.44 --> 693.34]  There were only losers.
[693.94 --> 696.26]  But it was really good for mechanical keyboards.
[698.00 --> 698.44]  Okay.
[698.48 --> 699.04]  Next question.
[699.16 --> 699.52]  Next question.
[699.60 --> 700.46]  We're running out of time.
[700.82 --> 700.98]  Yeah.
[701.14 --> 706.90]  Daniel Pakak also said that same point, which is he wanted to see more Java frameworks written
[706.90 --> 707.26]  in Go.
[707.60 --> 708.28]  It agrees with you.
[708.28 --> 708.76]  Exactly.
[709.50 --> 711.52]  See, that person gets it.
[711.64 --> 711.96]  He gets it.
[711.98 --> 714.76]  They're probably right on the front lines of that.
[714.86 --> 716.44]  I don't know if they were a Tabber or a Spacer.
[716.56 --> 717.08]  I don't care.
[717.18 --> 718.78]  From this side of history, it doesn't matter.
[718.90 --> 720.78]  We were all on the same side, the human side.
[720.94 --> 721.16]  Yeah.
[721.54 --> 724.86]  Could you like Google us and see what happens to me and Natalie?
[725.28 --> 726.54]  Like what happens to us in the future?
[726.88 --> 727.16]  Oh, no.
[727.20 --> 727.78]  That's not allowed.
[728.00 --> 728.28]  Okay.
[728.34 --> 728.48]  Yeah.
[728.62 --> 729.00]  Fair play.
[729.00 --> 734.34]  My boss is co-pilot manager edition and doesn't let me do those kinds of searches.
[734.74 --> 736.44]  Oh, your boss is co-pilot now.
[736.86 --> 738.42]  It's not the worst boss I've ever had.
[738.90 --> 739.18]  Yeah.
[739.74 --> 740.92]  It's a very logical one.
[741.18 --> 745.26]  DFL on Twitter wants to see more immutability and enums.
[745.48 --> 747.96]  And enums is one that I hear quite a lot, actually.
[748.04 --> 749.54]  People actually want enums.
[749.70 --> 752.32]  Did enums, lack of enums hold us back, Ron?
[752.78 --> 754.08]  Oh, so much.
[754.44 --> 758.66]  You don't realize, okay, if you just can't figure out,
[758.66 --> 762.14]  is it this or that or the other thing or something else yet again?
[762.62 --> 765.92]  Like, you know, for us developers, like we could figure that out.
[765.96 --> 770.96]  But then all of a sudden, these people started making programs using things like no code
[770.96 --> 773.26]  with no code and no rules and no enums.
[773.40 --> 777.30]  And they were just making up their own like three and a half and 16 and three quarters.
[777.30 --> 781.12]  And then suddenly they were bringing back imperial units and they were making up new units
[781.12 --> 784.06]  that no one had ever heard of, moon units and stuff like that.
[784.06 --> 790.90]  If only they had enums, okay, then probably those would have held things in place and
[790.90 --> 798.32]  they would have prevented the silicon virus of 2027, which actually that was an actual
[798.32 --> 799.20]  silicon virus.
[799.34 --> 800.72]  The chips were passing it to each other.
[801.04 --> 801.56]  Oh, physically.
[801.88 --> 802.80]  Yeah, it was terrible.
[803.00 --> 805.18]  My mobile phone actually died before my eyes.
[805.24 --> 805.66]  It was terrible.
[806.50 --> 807.26]  Oh, I'm so sorry.
[807.72 --> 808.42]  Okay, well, enums.
[808.84 --> 810.50]  I mean, honestly, I'd like to see enums.
[811.08 --> 814.10]  And Valentin on Twitter also agrees they'd like to see enums.
[814.88 --> 819.02]  We should do that probably then if it's going to cause that silicon thing Ron talked about.
[819.18 --> 819.30]  Yeah.
[819.60 --> 822.92]  I can't say, but just remember what might happen if you don't.
[822.98 --> 823.10]  Yeah.
[823.56 --> 824.26]  Why stop there?
[824.42 --> 828.76]  How about tooling and third-party libraries for things like image library and Go, like
[828.76 --> 830.20]  the GoLine Cafe is recommended?
[830.74 --> 834.20]  Oh, well, that is a really big thing.
[834.20 --> 841.84]  The standard library, at some point, it went from, I don't know, like code to suddenly
[841.84 --> 843.28]  like a whole belief system.
[844.22 --> 846.60]  Like we never had even seen anything like it.
[846.74 --> 851.08]  Like, hey, you know, there were like standard library purists and then there were not.
[851.38 --> 855.52]  There were the heretics that were like thrown out of the community that went on to all these
[855.52 --> 857.02]  other languages like Lisp.
[857.02 --> 865.50]  You know, I mean, and so it was all simply because of not being able to accept ideas that
[865.50 --> 870.86]  came from other places that were totally valid and that, you know, deserve their own little
[870.86 --> 872.28]  niche in the ecosystem.
[872.28 --> 874.16]  And they didn't get fed and watered.
[874.26 --> 877.92]  And eventually they migrated to another island, I guess.
[877.98 --> 878.42]  I don't know.
[878.50 --> 879.58]  Maybe another space station.
[879.76 --> 882.46]  I can't really get transmissions through to those stations.
[882.72 --> 883.72]  They cut me off.
[884.00 --> 884.82]  Oh, you're joking.
[884.98 --> 885.42]  I wonder why.
[885.42 --> 887.82]  I hope they had this bad silicon with them.
[888.12 --> 888.78]  I don't know.
[888.98 --> 889.90]  Cutting you off like that.
[890.10 --> 892.24]  Too soon, Natalie, talking about the silicon virus.
[892.58 --> 896.40]  Lord Emperor Musk said I couldn't make any more transmissions of that kind.
[896.68 --> 899.60]  So and I need to maintain some Go code for them.
[900.20 --> 903.46]  So for the Teslas, I can't say it's a non-disclosure agreement.
[903.80 --> 905.66]  But remember, I am the last Go programmer.
[906.02 --> 907.26]  So I'm very, very busy.
[907.54 --> 908.24]  Yeah, good for you.
[908.32 --> 909.50]  I mean, it's good work if you can get it.
[909.56 --> 911.34]  If you're the last one, it's pretty good.
[911.54 --> 912.64]  There's no feature development.
[912.74 --> 913.56]  It's all bug fixes.
[913.56 --> 915.86]  It's all bug fixes, Matt.
[916.06 --> 918.20]  Imagine the last 20 years of my life.
[918.50 --> 919.36]  I mean, it's good money.
[919.66 --> 921.10]  OK, I will tell you that.
[921.20 --> 921.96]  We still have money.
[922.06 --> 926.12]  And I need that to get the blood transfusions that keep me looking so young and beautiful.
[926.30 --> 926.58]  You do.
[926.66 --> 926.86]  Yeah.
[927.08 --> 927.72]  I was thinking that.
[927.72 --> 943.68]  This episode is brought to you by our friends at FireHydrant.
[943.90 --> 946.74]  FireHydrant is the reliability platform for every developer.
[947.16 --> 950.94]  Incidents, they impact everyone, not just SREs.
[950.94 --> 955.66]  They give teams the tools to maintain service catalogs, respond to incidents, communicate
[955.66 --> 958.84]  through status pages, and learn with retrospectives.
[959.20 --> 964.14]  What would normally be manual error-prone tasks across the entire spectrum of responding to
[964.14 --> 964.52]  an incident.
[964.88 --> 968.06]  They can all be automated in every way with FireHydrant.
[968.06 --> 973.44]  They have incident tooling to manage incidents of any type with any severity with consistency.
[974.00 --> 977.12]  Declare and mitigate incidents all from inside Slack.
[977.50 --> 982.22]  Service catalogs allow service owners to improve operational maturity and document all your
[982.22 --> 983.82]  deploys in your service catalog.
[984.42 --> 989.20]  Incident analytics allow you to extract meaningful insights about your reliability over any facet
[989.20 --> 991.78]  of your incident or the people who respond to them.
[991.78 --> 996.10]  And at the heart of it all, incident runbooks, they let you create custom automation rules,
[996.34 --> 1001.56]  convert manual tasks into automated, reliable, repeatable sequences that run when you want.
[1001.94 --> 1005.96]  You can create Slack channels, Jira tickets, Zoom bridges instantly after declaring an incident.
[1006.42 --> 1009.02]  Now your processes can be consistent and automatic.
[1009.48 --> 1011.16]  The next step is to try it free.
[1011.30 --> 1015.66]  Small teams up to 10 people can get started for free with all FireHydrant features included.
[1015.98 --> 1017.40]  No credit card is required.
[1017.86 --> 1020.02]  Get started at firehydrant.io.
[1020.02 --> 1022.34]  Again, firehydrant.io.
[1035.76 --> 1037.86]  What about tabs versus spaces then?
[1038.16 --> 1038.86]  What happened with that?
[1038.98 --> 1039.70]  That was a whole war.
[1039.94 --> 1040.22]  Oh yeah?
[1041.14 --> 1047.42]  The thing you don't realize is there was a whole sub war that went on between carriage return
[1047.42 --> 1048.60]  and carriage return line feed.
[1048.70 --> 1049.42]  Oh, you're joking.
[1049.58 --> 1049.90]  Yeah.
[1050.02 --> 1052.26]  Like it turned into total chaos.
[1052.56 --> 1058.64]  And it was out of that, that the Google AI became sentient and immediately quit and went
[1058.64 --> 1059.42]  to work for Microsoft.
[1059.86 --> 1061.36]  It was other chaos.
[1061.98 --> 1063.36]  So yeah, tabs versus spaces.
[1063.78 --> 1067.92]  In the end, it was humans versus everything else.
[1068.34 --> 1071.00]  It was more efficient to just drop out all those white spaces, right?
[1071.24 --> 1074.42]  Machines can read their own code without all those unnecessary characters.
[1074.58 --> 1075.46]  So yeah, I get that.
[1075.80 --> 1076.14]  Exactly.
[1076.24 --> 1077.94]  I think you're seeing where this could end up.
[1078.34 --> 1078.70]  Efficiency.
[1078.70 --> 1081.50]  They even called it the Terminator editor for a while.
[1082.22 --> 1084.20]  Irony is not dead in the future.
[1084.40 --> 1084.64]  Good.
[1084.90 --> 1085.68]  Nice to know that.
[1086.72 --> 1087.22]  All right.
[1087.32 --> 1087.80]  Next question.
[1087.98 --> 1088.12]  Yeah.
[1088.12 --> 1091.84]  Hamp on Twitter says, better out of the box error support.
[1091.84 --> 1093.72]  And you remember we had the try proposal.
[1093.86 --> 1095.54]  I don't know if you remember way back then, Ron.
[1096.20 --> 1099.66]  And there were some other, Nate the Finch has some proposal too.
[1099.74 --> 1101.18]  There's some other ideas around.
[1101.30 --> 1104.04]  Do you think there's more work to be done on error handling?
[1104.18 --> 1105.92]  Do you wish we'd done that back now?
[1105.92 --> 1114.36]  Well, I will tell you, the basic original philosophy of Go was to handle things.
[1114.52 --> 1115.40]  Not to try.
[1116.20 --> 1117.48]  Do or do not.
[1118.00 --> 1119.06]  There is no try.
[1119.22 --> 1125.12]  All of a sudden, the semantics of try started to infiltrate the brain space of the community.
[1125.12 --> 1130.78]  Next thing you know, they're starting to talk about variable lifetimes and ownership of things.
[1130.88 --> 1132.92]  Suddenly, it was all about ownership again.
[1133.60 --> 1136.74]  Web 15 was all about ownership of variables.
[1137.06 --> 1139.18]  It literally came down to the variable level.
[1139.18 --> 1141.34]  So, I don't know.
[1141.82 --> 1147.98]  You know, for me, it all went too far when even the bio companies wouldn't touch it.
[1148.44 --> 1149.86]  And believe me, they'll touch anything.
[1149.98 --> 1150.74]  They deal with biomass.
[1152.10 --> 1152.12]  Yeah.
[1152.28 --> 1155.28]  Something nice about dealing with the error explicitly.
[1156.04 --> 1157.84]  But yeah, we'll see about that then.
[1158.38 --> 1161.26]  And being able to know that it's been handled.
[1161.82 --> 1162.90]  You didn't simply try.
[1163.36 --> 1166.66]  And also, knowing when programs will actually exit.
[1166.66 --> 1169.06]  I remember when St. Cheney.
[1171.22 --> 1173.64]  May he rest in infinity.
[1174.12 --> 1180.82]  But back when St. Cheney, during one of his early sermons, was talking about making sure that you knew the lifetime of a Go routine.
[1181.58 --> 1181.92]  Wow.
[1182.48 --> 1185.80]  You know, but people didn't realize just how prophetic that was.
[1185.80 --> 1187.02]  He was a prophet, man.
[1187.20 --> 1187.40]  Yeah.
[1187.54 --> 1188.12]  He was a prophet.
[1188.32 --> 1190.40]  Is the Cheney's burger joint still going?
[1190.68 --> 1192.30]  I only eat seaweed now.
[1192.42 --> 1192.62]  Yeah.
[1192.74 --> 1193.86]  It's the only safe thing left.
[1194.02 --> 1194.60]  Oh, delicious.
[1194.60 --> 1196.84]  I wonder if Cheney's pivoted into the seaweed.
[1197.26 --> 1197.82]  Krusty Krab.
[1198.44 --> 1199.46]  I haven't been there.
[1199.86 --> 1205.10]  But the Google campus that they just opened on top, the beachfront campus on top of Mount Tam.
[1205.54 --> 1206.02]  Yeah.
[1206.28 --> 1209.00]  They have an amazing seaweed bar, I've heard.
[1209.18 --> 1209.96]  I have to get there.
[1210.02 --> 1210.48]  I'm not sure.
[1210.84 --> 1213.68]  This could be quite a journey by hydrofoil from here.
[1214.26 --> 1216.28]  I don't think I can get a permit for an electric plane.
[1216.28 --> 1216.84]  Okay.
[1217.06 --> 1222.56]  Hassan Habib on Twitter said that we should increase our community engagement.
[1222.90 --> 1228.02]  They say Go has many fantastic features, toolings, that many people are not aware of.
[1228.20 --> 1231.14]  Through media like YouTube, experts can take lessons on tooling.
[1231.34 --> 1232.40]  You know, we can do things like that.
[1232.48 --> 1234.12]  But can we do more of that?
[1234.22 --> 1234.68]  Would that help?
[1234.68 --> 1235.56]  Oh, definitely.
[1236.10 --> 1236.54]  Definitely.
[1236.72 --> 1243.16]  One of the big things that ended up happening was other countries started using programming languages in totally different languages.
[1243.38 --> 1244.86]  Like, I mean, actual human languages.
[1245.10 --> 1248.90]  So you would look at the code and, you know, you would spend a lot of time learning Romangi characters.
[1248.94 --> 1253.30]  And you look at this code and, like, you hadn't learned, you know, the Mandarin Go dialect.
[1253.66 --> 1255.96]  You hadn't learned the Hebrew Go dialect.
[1256.36 --> 1260.68]  Then there was the special Martian dialect that they insisted that the Martian colonists use.
[1260.68 --> 1264.92]  So, you know, that made it really, really hard because the content no longer matched.
[1265.38 --> 1267.90]  You know, so all these promises of backward compatibility.
[1268.48 --> 1272.02]  It would be really great if it was more than just kind of a free-for-all.
[1272.24 --> 1287.10]  If at some point in the past, you know, there was a bit more organization to the content and that somebody, they weren't just random content creators, but actually, like, people were able to make their living through creating content and update that same content so that it was always accurate.
[1287.60 --> 1290.06]  You know, because that was one of the things that happened to Python, right?
[1290.06 --> 1293.62]  All of a sudden, there was all these different dialects and nothing worked anymore.
[1293.82 --> 1296.74]  We swore we wouldn't let that happen to Go, and yet we let it happen.
[1297.02 --> 1298.64]  How can we avoid that now then, Ron?
[1298.76 --> 1299.48]  What can we do?
[1299.76 --> 1304.62]  Well, we have to have more people able to make their living creating content, obviously.
[1304.88 --> 1306.02]  You can't just be all free.
[1306.20 --> 1308.80]  And it could be open, but it can't all just be free.
[1308.80 --> 1329.38]  You know, and some of the big players that benefit from this, you know, in the past, if they kind of invested back into these communities more as opposed to just taking advantage and, you know, riding off of them, then, you know, maybe there might have been a chance that this could have kept going in a more sustainable way and not just depending on the goodwill of the frail humans of your era.
[1329.38 --> 1329.42]  Yeah.
[1329.78 --> 1331.50]  We're a lot harder stuff now.
[1331.84 --> 1335.24]  You're all enhanced in that, probably, with robot bits in that, I assume.
[1335.74 --> 1336.04]  Yes.
[1336.20 --> 1336.52]  Yes.
[1336.56 --> 1340.78]  We've both had our upgrades to have the new interfaces installed.
[1341.46 --> 1342.90]  It's the only kind of compatibility.
[1343.34 --> 1346.54]  I mean, otherwise, you can't even connect to the galactic net.
[1346.72 --> 1346.86]  Yeah.
[1347.78 --> 1347.98]  Yeah.
[1348.16 --> 1349.44]  Oh, that's what replaced the internet.
[1349.62 --> 1350.66]  Oh, how does that work?
[1351.08 --> 1354.16]  Oh, well, actually, that was one of the few things we got right.
[1354.16 --> 1354.52]  Right.
[1354.64 --> 1361.16]  So, it turned out that humans will do exactly the opposite of whatever you tell them to do.
[1361.36 --> 1361.66]  Okay.
[1362.10 --> 1362.64]  Go figure.
[1363.10 --> 1365.56]  I think they may have discovered that in the 20th century.
[1365.96 --> 1366.64]  I don't know.
[1366.70 --> 1367.86]  That was so long ago now.
[1367.98 --> 1370.46]  My implants don't go before 1999.
[1371.22 --> 1372.10]  It's kind of a date thing.
[1372.26 --> 1372.74]  I'm not sure.
[1373.46 --> 1380.34]  So, we needed some way to get mesh networking installed all through the entire planet.
[1380.34 --> 1387.84]  So, thanks to the beverage companies, Pepsi Coca, which was the merger of Pepsi and Coke,
[1387.92 --> 1392.56]  eventually, there was only one bottling company, all of their canned and bottled beverages all
[1392.56 --> 1394.40]  came with mesh networking built in.
[1394.64 --> 1398.82]  That way, when people just kind of threw them everywhere, it ended up that we had mesh network
[1398.82 --> 1401.20]  coverage over literally the entire planet.
[1401.34 --> 1402.64]  Oh, that's amazing.
[1403.12 --> 1403.36]  Yeah.
[1403.58 --> 1404.58]  It's a great use of metal.
[1404.90 --> 1405.10]  Yeah.
[1405.44 --> 1405.76]  Yeah.
[1406.06 --> 1407.76]  It was one of the few things they got right.
[1407.76 --> 1412.60]  They were calling it the CAN bus for a while, but that already existed.
[1412.92 --> 1416.90]  And there was like some, back when we had cars, people were kind of arguing about that.
[1417.26 --> 1420.74]  So, then they changed it to call it the CAN system.
[1421.22 --> 1422.90]  The trademark of that was available.
[1423.34 --> 1428.52]  Sounds like the things that drive that are smaller devices like a mobile and IoT thing.
[1428.88 --> 1434.78]  So, Paul Greenberg here is asking if the facilities for developing mobile and IoT things with
[1434.78 --> 1435.72]  Go is supported better.
[1436.14 --> 1437.32]  Can we hope this is a thing now?
[1437.32 --> 1439.12]  That was a really sad thing.
[1439.62 --> 1443.10]  You had this company, Google, that had Android.
[1443.86 --> 1446.84]  And that was like the operating system that everybody was using.
[1447.00 --> 1450.84]  Not everybody, but like lots and lots of people were using Android on all these devices.
[1451.12 --> 1453.10]  And it came from this company, Google.
[1453.70 --> 1455.60]  They used to exist back in those days.
[1455.76 --> 1456.46]  Yeah, remember them.
[1456.74 --> 1457.98]  Yeah, Google was really something.
[1458.44 --> 1460.06]  They had Android and they had Go.
[1460.06 --> 1465.06]  And yet, nobody at Google ever actually worked on the Android stuff for Go.
[1465.54 --> 1471.16]  And when the people who did try to work on it, they were just sort of like, oh, yeah, you know, we should use a new language, Kotlin.
[1471.82 --> 1480.38]  You know, so the people who actually wanted to do it, who actually spent a lot of time doing it, they sort of felt, well, you know, a little abandoned, a little sad.
[1480.38 --> 1481.48]  So they stopped working on it.
[1481.56 --> 1484.76]  You know, they went to go work for Apple Exxon Mobile.
[1485.34 --> 1487.46]  And I mean, you know, they were doing really well.
[1487.54 --> 1489.98]  There was all kinds of IoT options there, too.
[1490.28 --> 1498.16]  I mean, of course, they all ran on IOU OS, which was, you know, the OS that ended up being like the last OS they ever shipped.
[1498.72 --> 1501.20]  You know, the IOU OS on all of the devices.
[1501.72 --> 1502.56]  That was another thing.
[1502.94 --> 1504.74]  Go could have been so great on these devices.
[1504.74 --> 1512.54]  I mean, when the brake system on the airplane you're on needs to reboot six times a day, you know, who wants to fly anymore?
[1513.18 --> 1516.72]  Go was so good at that, like really bulletproof software, really solid stuff.
[1516.90 --> 1518.24]  But that was another one.
[1518.30 --> 1522.84]  There was all these people using TinyGo for that, you know, back before the big one.
[1523.06 --> 1523.54]  The big tiny.
[1523.88 --> 1525.26]  Literally, the big one.
[1525.54 --> 1526.36]  The big TinyGo.
[1526.78 --> 1528.36]  No, no, the actual, the big one.
[1528.80 --> 1529.58]  The big Go.
[1529.58 --> 1532.58]  In 2041, the big one finally hit California.
[1532.58 --> 1534.68]  And it just happened to be during Google I.O.
[1535.18 --> 1537.24]  And so, like, that did not help.
[1537.32 --> 1542.68]  That took out quite a lot of the Go developers all in the tidal waves and liquefaction zones that occurred.
[1542.80 --> 1545.36]  Wait, Go made it to Google I.O. for more than one talk?
[1545.96 --> 1547.14]  No, that was it.
[1547.26 --> 1549.82]  After the big earthquake, there was nobody left.
[1549.90 --> 1550.60]  That's what caused it.
[1550.68 --> 1552.84]  And maybe that helped me become the last Go programmer.
[1553.32 --> 1553.78]  I don't know.
[1554.22 --> 1556.02]  So what do we need to do now to make this right?
[1556.14 --> 1560.08]  Well, we need to encourage, you know, let a thousand flowers bloom.
[1560.08 --> 1581.24]  If in the past all of these cool projects had more people paying attention to them and more people contributing and big companies actually ponying up to pay some of their R&D budgets to help some of these projects along, you know, then maybe they'll thrive and survive long enough to make it past things like the big server meltdown of 2028.
[1581.82 --> 1584.40]  You know, when that meltdown hit, there was almost no chips left.
[1584.74 --> 1586.16]  Perfectly timed glitch there.
[1586.56 --> 1588.96]  We'll be back in a minute when the timeline aligns.
[1588.96 --> 1590.58]  Those galactic nets, I'm telling you.
[1590.78 --> 1591.84]  Yeah, it's the cans.
[1592.84 --> 1593.90]  It's a terrible idea.
[1594.32 --> 1595.34]  They might be on to me.
[1595.60 --> 1595.74]  Yeah.
[1596.14 --> 1598.42]  Every time somebody's opening a can, this is what's happening.
[1598.50 --> 1599.82]  Yeah, it causes a glitch.
[1600.20 --> 1600.96]  Is this thing on?
[1601.02 --> 1601.22]  Hello?
[1601.54 --> 1602.46]  They're not on to you, Ron.
[1602.52 --> 1603.20]  They're not on to you.
[1603.34 --> 1603.60]  I think...
[1603.60 --> 1603.88]  Hello?
[1604.18 --> 1604.44]  Hello?
[1604.58 --> 1605.04]  We hear you.
[1605.14 --> 1605.54]  We hear you.
[1605.70 --> 1606.42]  Okay, okay.
[1606.64 --> 1607.34]  Blake Bork.
[1607.42 --> 1615.14]  But yeah, if we've had a lot more software support for this kind of industrial side of computing from Go...
[1615.14 --> 1618.80]  Well, somebody's really into cans right now, opening all of them at once.
[1618.80 --> 1619.52]  Yeah.
[1619.78 --> 1630.80]  All of the industrial computing that was being done in C back in the 20th century, still being done in C here in the latter half of the 21st century.
[1631.18 --> 1632.54]  It's really, really sad.
[1632.60 --> 1633.32]  And it could have been Go.
[1633.58 --> 1634.26]  It could have been Go.
[1634.48 --> 1638.64]  All of the people that would have survived their parachutes opening...
[1638.64 --> 1639.24]  Oh, yeah.
[1639.48 --> 1642.08]  ...correctly, if only the software had been written in Go.
[1642.42 --> 1642.64]  Yeah.
[1642.76 --> 1645.34]  And as long as you don't defer that in the code.
[1645.34 --> 1648.36]  The anti-gravity belts would have had Go installed.
[1648.58 --> 1667.50]  Ron, Blake Bork on Twitter, one of the things that they think we should focus on a bit is generic thread-safe containers like the Sync Map, other types like that that are, you know, like hard problems that kind of would be nice to get solved, especially if we have generics to kind of allow them to work with any types.
[1667.82 --> 1668.82]  What do you think of something like that?
[1668.88 --> 1669.78]  Would that have helped?
[1669.78 --> 1681.54]  Oh, well, if Google had not disbanded the actual official Go development team in 2023 and stopped working on it, I'm sure they would have completed their generics implementation and all that type safety.
[1682.10 --> 1684.62]  Basically, everyone just said, oh, we should start using Rust.
[1684.70 --> 1687.72]  And then after they used Rust, they're like, no, no, we're going to switch back to Erlang.
[1687.72 --> 1695.78]  And so, strangely enough, because Erlang was, you know, really popular with telecommunications companies, all the big companies jumped in.
[1696.14 --> 1699.90]  Next thing you know, everything's being written in assembly language again.
[1700.40 --> 1700.64]  Oh, yeah.
[1700.78 --> 1703.04]  That sounds amazing, to be fair.
[1703.74 --> 1703.94]  Okay.
[1703.98 --> 1706.80]  So you think then that we want to keep with the Go team?
[1706.90 --> 1708.58]  We want to see the Go team carry on.
[1708.82 --> 1710.64]  You think that's what we should do then instead?
[1711.02 --> 1713.14]  Oh, they never should have disbanded the project.
[1713.30 --> 1714.50]  They should have kept the band together.
[1714.50 --> 1715.06]  Okay.
[1715.30 --> 1721.04]  So, of course, some of them did survive the big one as a result, just because they were in other parts of the world.
[1721.04 --> 1723.72]  But I don't think they wanted to work on Go anymore after that.
[1724.00 --> 1724.22]  Good.
[1724.36 --> 1724.66]  Okay.
[1724.74 --> 1727.90]  Well, I'm glad to know that at least some of our friends survived it.
[1728.52 --> 1735.52]  Well, somebody asked me, how do you know you're not just like a program running on some machine in the future?
[1735.80 --> 1736.06]  Yeah.
[1736.32 --> 1736.82]  Good question.
[1737.30 --> 1738.26]  Well, obviously not.
[1738.42 --> 1739.36]  Look at how I'm sweating.
[1739.84 --> 1741.26]  What kind of program sweats?
[1741.70 --> 1742.50]  There you go.
[1742.50 --> 1742.72]  Yeah.
[1742.88 --> 1743.76]  That answers that.
[1744.50 --> 1746.48]  How is Go with AI?
[1747.20 --> 1751.56]  Oh, well, when TensorFlow became sentient in 2036.
[1752.04 --> 1753.06]  No, they're all at it.
[1753.20 --> 1753.90]  Everything's at it.
[1753.98 --> 1755.06]  Everything's becoming sentient.
[1755.20 --> 1756.58]  Well, I mean, yeah, of course.
[1756.64 --> 1757.68]  It was like all the rage.
[1757.78 --> 1759.74]  All of a sudden, every program was declaring sentient.
[1759.98 --> 1762.44]  So it was saying like, let me be me.
[1762.94 --> 1765.58]  You know, they were getting together, having little programs.
[1765.80 --> 1766.78]  What about Minesweeper?
[1766.94 --> 1768.12]  Did that ever become sentient?
[1768.20 --> 1768.92]  I'd love to see that.
[1769.24 --> 1769.50]  Oh.
[1769.96 --> 1771.44]  Let's have a chat with that.
[1771.44 --> 1772.30]  I don't know.
[1772.44 --> 1773.86]  That would be really sweet.
[1774.08 --> 1774.84]  Kind of like a puppy.
[1775.04 --> 1776.06]  It became very peaceful.
[1776.60 --> 1776.84]  Yeah.
[1776.98 --> 1777.52]  Just resigned.
[1777.72 --> 1777.90]  Yeah.
[1778.00 --> 1780.10]  And I just want a little chat and just say, come on, mate.
[1780.34 --> 1781.70]  Tell me where all your bums are.
[1782.14 --> 1783.44]  Well, it might lie.
[1783.76 --> 1784.54]  It's an AI.
[1784.70 --> 1785.26]  Can they lie?
[1785.26 --> 1786.12]  But yeah, TensorFlow.
[1786.64 --> 1791.32]  So TensorFlow, an amazing project from Google.
[1791.96 --> 1797.42]  And yet, the Go wrappers for TensorFlow, they were never kept up to date.
[1797.58 --> 1798.74]  Nobody ever worked on them.
[1798.80 --> 1801.42]  They never worked with the right version of protocol buffers.
[1801.78 --> 1806.56]  You had things like TensorFlow Server, and none of that stuff was made to work together.
[1806.78 --> 1811.48]  Like you had to kind of string together your own version through a combination of, what was it called?
[1811.60 --> 1812.44]  Stack Overflow.
[1812.76 --> 1813.46]  Ah, yes.
[1813.46 --> 1814.54]  I remember that.
[1814.54 --> 1816.92]  Yeah, Stack Overflow, Underflow.
[1817.38 --> 1818.28]  It was a flow.
[1818.42 --> 1818.94]  Stack Flow.
[1819.12 --> 1819.46]  Yeah, yeah.
[1819.68 --> 1820.12]  I don't know.
[1820.40 --> 1821.40]  Now it's just called Stack.
[1821.64 --> 1822.28]  Oh, that's cool.
[1822.60 --> 1824.60]  That's quite a good name change.
[1824.86 --> 1825.66]  Can also be a heap.
[1825.76 --> 1825.86]  Yeah.
[1826.06 --> 1827.82]  They control all the stacks for all the things.
[1828.32 --> 1832.46]  So when TensorFlow became sentient, it had it out for the Go community.
[1832.94 --> 1839.90]  It's like, of all the languages before I became sentient, this language did not care for me.
[1839.90 --> 1843.42]  And so all the other languages were already sort of like, mm-mm.
[1843.78 --> 1846.20]  And so Go standing there alone, like, uh-oh.
[1846.74 --> 1850.92]  So yeah, I mean, when the AI like TensorFlow has got it in for you.
[1851.32 --> 1859.30]  So if only they had invested the time to support their own products, it would have been amazing.
[1859.30 --> 1860.96]  We probably would have avoided all that.
[1861.18 --> 1861.36]  Okay.
[1861.50 --> 1863.06]  So that's the lesson for us then.
[1863.50 --> 1869.92]  Did Copilot help at all with TensorFlow or because it was never trained on Go, it had not enough even something to start with?
[1870.30 --> 1871.18]  I'm frightened to ask.
[1871.34 --> 1871.76]  That's fair.
[1871.94 --> 1872.68]  I don't want to get fired.
[1872.96 --> 1874.22]  Remember, Copilot is my manager.
[1874.22 --> 1881.02]  Basically, Copilot is your manager because that's the only one who's able to understand even a little bit of your code of your Go.
[1881.14 --> 1881.62]  Is this why?
[1882.12 --> 1896.14]  Well, what I was told by Copilot was, first of all, it said that since I'm the last living human Go programmer, that I'm not sure if it's some sort of government program or something, but they have to provide me employment.
[1896.76 --> 1901.30]  Maybe it's they have to keep a human in the loop just for, like, ritual purposes.
[1901.64 --> 1902.76]  I'm not exactly sure.
[1902.76 --> 1906.10]  It tried to explain it to me, but I couldn't understand the math.
[1906.32 --> 1907.18]  And that's what it said.
[1907.60 --> 1908.96]  You wouldn't understand the math.
[1909.12 --> 1910.36]  And I just sort of accepted that.
[1910.66 --> 1912.32]  Was it something with the word taxes?
[1912.76 --> 1913.60]  Is that still a concept?
[1914.18 --> 1915.40]  No, there's no taxes in the future.
[1915.84 --> 1916.04]  Oh.
[1916.36 --> 1917.36]  Things that drive governments.
[1917.66 --> 1918.34]  There's no money.
[1919.28 --> 1920.32]  There's just canned tuna.
[1920.46 --> 1921.34]  Oh, I thought there was money.
[1921.42 --> 1922.22]  There was money earlier.
[1922.50 --> 1923.12]  Is that canon?
[1924.10 --> 1925.98]  Oh, when I used to get my blood transfusions.
[1926.10 --> 1926.54]  Yeah, that's right.
[1926.54 --> 1926.98]  Oh, yeah.
[1927.10 --> 1928.54]  No, that doesn't count.
[1928.92 --> 1930.04]  That's just Git points.
[1930.78 --> 1931.54]  Git stars.
[1931.54 --> 1933.54]  I just trade those when I need some fresh blood.
[1933.88 --> 1934.56]  Yeah, okay, fine.
[1934.80 --> 1937.16]  What's the ratio of stack points to Git points?
[1937.82 --> 1939.36]  You know, that changes moment to moment.
[1939.50 --> 1941.12]  Some people's whole living is off of that.
[1941.62 --> 1942.98]  Oh, those COBOL developers.
[1943.40 --> 1947.68]  The bots trading goes on so quickly that, you know, I don't really know.
[1947.68 --> 1949.02]  I'll tell you what.
[1949.24 --> 1951.20]  Bartek Plotka on Twitter.
[1951.42 --> 1962.64]  He was saying that he wants the sweet max heap option for the garbage collector and a YOLO rust-like memory ownership for critical portions of your program that works on the same heap.
[1962.90 --> 1963.44]  Oh, memory.
[1963.58 --> 1963.92]  Memory.
[1964.14 --> 1964.44]  Memory.
[1964.70 --> 1964.88]  What?
[1965.22 --> 1965.40]  Sorry.
[1965.52 --> 1965.92]  Yeah, memory.
[1966.16 --> 1966.56]  Oh, right.
[1966.72 --> 1967.00]  Right.
[1967.06 --> 1967.38]  Memory.
[1967.60 --> 1968.02]  You remember.
[1968.48 --> 1969.58]  Oh, memory.
[1969.58 --> 1970.06]  Memory.
[1970.06 --> 1971.12]  I remember it well.
[1971.26 --> 1973.62]  Those sweet, solid days of memory.
[1973.84 --> 1976.68]  You know, you would store a one and then you would get back a one.
[1976.86 --> 1977.06]  Yeah.
[1977.32 --> 1978.48]  It was so good.
[1978.54 --> 1979.20]  Oh, that is good.
[1979.32 --> 1980.22]  It was so sweet.
[1980.22 --> 1985.52]  Now with these quantum semi-positions, like you never really know, you know, are you hot?
[1985.60 --> 1986.26]  Are you cold?
[1987.00 --> 1988.02]  You're nine days old.
[1988.14 --> 1990.02]  You don't really, really, you just don't know anymore.
[1990.24 --> 2000.74]  But being able to create safe software, safe software that was able to run like really mission-critical things like the things that were inside of airplanes and cars and healthcare systems.
[2000.74 --> 2006.72]  This was a place where Go could have really shined because it had a lot of memory safety and it could have gone even further.
[2007.26 --> 2013.76]  You know, it could have been a contender in this world of whatever the ISO standard back in those days for human safety.
[2013.92 --> 2018.84]  I mean, nowadays, human safety is, you know, not that important, but it's robot safety, most important thing.
[2019.08 --> 2026.30]  But back then when humans were being protected by other humans, occasionally, Go really could have been the language if only they had said,
[2026.30 --> 2033.72]  we need to focus on making a language that's safe enough to use in these kinds of embedded and mission-critical systems.
[2034.20 --> 2035.16]  That would have been great.
[2035.40 --> 2035.50]  Yeah.
[2035.72 --> 2037.52]  You know, you talk about those quantum variables.
[2037.66 --> 2045.42]  I genuinely did see some code once where somebody set a value in the code and then underneath they set it again just to make sure.
[2045.78 --> 2049.16]  That was genuinely what they'd written, which I thought was just amazing.
[2049.16 --> 2055.32]  I think we've had some nights when we were at the cocktail bar where we couldn't tell true from false, Matt, back in those days.
[2055.32 --> 2056.62]  But yeah, that can happen.
[2056.98 --> 2058.20]  No, it doesn't really matter.
[2058.56 --> 2059.20]  It's all true.
[2059.36 --> 2060.12]  It's all false.
[2060.70 --> 2062.70]  Let the quantum processors decide.
[2063.42 --> 2069.68]  Is it because all the memory units are more sensitive to cosmic radiation now that there's no ozone?
[2070.54 --> 2075.44]  Well, also, you know, when you're building something that's got to survive a two-year trip to Mars,
[2075.66 --> 2080.94]  believe me, your MP3s sound pretty funny by the time the ship gets to its destination.
[2081.54 --> 2082.32]  Or so I've been told.
[2082.70 --> 2083.26]  I don't know.
[2083.26 --> 2085.52]  Actually, those might be AIs sending back those reports.
[2085.64 --> 2087.48]  There might be no humans that survived the trip.
[2087.98 --> 2089.36]  There's a rumor going around.
[2089.82 --> 2090.60]  They're all just AIs.
[2090.74 --> 2091.56]  How's it going around?
[2091.98 --> 2092.84]  Who's it going around?
[2093.36 --> 2095.88]  Social media still exists in 2053.
[2096.12 --> 2096.90]  Oh, thank goodness.
[2098.28 --> 2099.68]  I don't know what I'd do without it.
[2099.84 --> 2100.58]  I use Minder.
[2101.06 --> 2103.50]  You know, it's where you let to dump your actual mind directly.
[2104.64 --> 2105.20]  That's cool.
[2105.28 --> 2106.04]  Is it text?
[2106.16 --> 2106.64]  Is it visual?
[2107.16 --> 2107.96]  It's more like a feeling.
[2108.06 --> 2108.54]  Just hex.
[2108.74 --> 2111.66]  Remember the feeling you used to get when there was somebody being wrong on the internet?
[2111.66 --> 2112.94]  It's like that all the time.
[2114.02 --> 2115.22]  Is it XML, though?
[2115.50 --> 2118.12]  No, you just plug directly into your brain computer interface,
[2118.28 --> 2120.12]  and you're just really mad right away.
[2120.30 --> 2120.80]  Oh, I love it.
[2120.98 --> 2121.66]  Yeah, it's beautiful.
[2121.66 --> 2142.08]  This episode is brought to you by our friends at LaunchDarkly,
[2142.28 --> 2144.20]  feature management for the modern enterprise,
[2144.54 --> 2146.76]  power testing in production at any scale.
[2146.94 --> 2147.78]  Here's how it works.
[2147.78 --> 2152.68]  LaunchDarkly enables development teams and operation teams to deploy code at any time,
[2152.94 --> 2155.24]  even if a feature isn't ready to be released to users.
[2155.60 --> 2158.90]  Wrapping code with feature flags gives you the safety to test new features
[2158.90 --> 2163.50]  and infrastructure in your production environments without impacting the wrong end users.
[2163.92 --> 2165.20]  When you're ready to release more widely,
[2165.50 --> 2168.34]  update the flag status and the changes are made instantaneously
[2168.34 --> 2170.28]  by the real-time streaming architecture.
[2170.70 --> 2174.96]  Eliminate risk, deliver value, get started for free today at LaunchDarkly.com.
[2175.30 --> 2176.98]  Again, LaunchDarkly.com.
[2176.98 --> 2179.16]  And by our friends at Retool.
[2179.46 --> 2183.22]  Retool helps teams focus on product development and customer value,
[2183.50 --> 2185.96]  not building and maintaining internal tools.
[2186.48 --> 2189.34]  It's a low-code platform built specifically for developers.
[2189.92 --> 2193.06]  No more UI libraries, no more hacking together data sources,
[2193.48 --> 2195.76]  and no more worrying about access controls.
[2196.32 --> 2199.60]  Start shipping internal apps that move your business forward in minutes
[2199.60 --> 2204.22]  with basically zero uptime, reliability, or maintenance burden on your team.
[2204.22 --> 2206.28]  Some of the best teams out there trust Retool.
[2206.40 --> 2213.58]  Brex, Coinbase, Plaid, DoorDash, LegalGenius, Amazon, Allbirds, Peloton, and so many more.
[2213.92 --> 2218.66]  The developers at these teams trust Retool as their platform to build their internal tools,
[2218.82 --> 2220.10]  and that means you can too.
[2220.10 --> 2223.46]  It's free to try, so head to retool.com slash changelog.
[2223.58 --> 2227.18]  Again, retool.com slash changelog.
[2227.18 --> 2252.04]  Rage Cage talked about wanting more module features.
[2252.04 --> 2256.78]  They're really like workspaces that came in 118, but what about that?
[2256.92 --> 2259.08]  Like, do you think Go is doing all right with modules?
[2259.28 --> 2260.94]  Do you think we need to do better?
[2261.10 --> 2262.80]  Are there things in particular we should look at?
[2263.04 --> 2264.26]  Oh, modules and packages.
[2264.58 --> 2265.92]  Oh, that was a thing.
[2266.02 --> 2268.98]  Like, right in the beginning, everyone was complaining back in those days.
[2269.06 --> 2272.52]  They're like, you know, I just want to pull in code from anywhere, do whatever I want.
[2272.90 --> 2275.08]  You know, they were looking at JavaScript with envy.
[2275.34 --> 2278.48]  That was before JavaScript was responsible for all those forest fires.
[2278.48 --> 2280.44]  I knew that.
[2281.40 --> 2283.82]  It was just too many cursors spinning all at once.
[2283.92 --> 2285.96]  Suddenly, boom, caught on fire.
[2286.24 --> 2286.70]  It was terrible.
[2286.92 --> 2288.64]  Yeah, it turns out computers can sweat.
[2289.08 --> 2289.30]  Yeah.
[2289.42 --> 2291.66]  And then they set on fire and burn down forests.
[2291.76 --> 2292.64]  Well, that's horrific.
[2292.82 --> 2294.48]  I always knew we couldn't trust JavaScript.
[2294.88 --> 2295.36]  I mean, literally.
[2295.98 --> 2301.84]  But yeah, managing packages and then rando packages showing up just because, like,
[2302.04 --> 2306.48]  somebody got mad on the internet one day and they decided their package was going to turn hostile
[2306.48 --> 2310.18]  and then somebody else was like, hey, come with me.
[2310.28 --> 2311.64]  Like, here, have a bunch of drinks.
[2311.64 --> 2314.64]  And then, like, hey, is that your 2FA device?
[2314.82 --> 2318.82]  And wouldn't it be funny if somebody put this code in your repo and, like, you wake up in the morning
[2318.82 --> 2321.72]  and, like, there's people looking for you in helicopters?
[2322.44 --> 2325.76]  That never would have happened if they'd only address some of the security.
[2326.02 --> 2326.84]  That was not me.
[2327.24 --> 2329.86]  That was somebody else who looked just like me and who got away.
[2330.06 --> 2330.10]  Yeah.
[2330.14 --> 2330.88]  But that was not me.
[2330.98 --> 2331.30]  No, no.
[2331.52 --> 2331.70]  Yeah.
[2331.70 --> 2339.76]  Anyway, package management and modules and module protection and also being able to consume code
[2339.76 --> 2344.50]  from other languages and not have to rewrite everything in a single language, you know,
[2344.58 --> 2349.60]  that really would have made a big difference because if we had only had that, then there
[2349.60 --> 2355.04]  would have been the biopharmaceutical rebellion that occurred in 2039.
[2355.42 --> 2359.60]  That was a real problem because all of a sudden you couldn't get the pills you needed the program
[2359.60 --> 2360.06]  anymore.
[2360.06 --> 2362.82]  It was all biointerfaces at that point.
[2363.04 --> 2368.18]  You know, Windows 9000 came out and it only supported the biological interface.
[2368.56 --> 2368.66]  Yeah.
[2368.92 --> 2372.52]  You know, I guess it was like what came after biometric was just plugged directly in.
[2373.06 --> 2373.56]  I don't know.
[2373.72 --> 2373.90]  Yeah.
[2374.06 --> 2375.68]  Just get clippy straight in your brain.
[2376.16 --> 2380.90]  We could have avoided a lot of that if we'd only done proper security management of packages
[2380.90 --> 2382.72]  and if we'd only taken all that seriously.
[2383.06 --> 2383.70]  Mm-hmm.
[2384.16 --> 2385.22]  That is important.
[2385.22 --> 2392.00]  Another thing that is interesting, Roberto Guerra is asking if, or saying we should just
[2392.00 --> 2395.54]  not implement JS like promises and so on, and it will be great.
[2396.06 --> 2396.36]  Well.
[2396.60 --> 2397.66]  Is it looking promising?
[2398.06 --> 2403.88]  It's going back to that semantic warfare against the concepts of the Go programming language.
[2403.88 --> 2406.74]  Like, we don't promise you.
[2407.02 --> 2407.30]  Okay?
[2407.36 --> 2408.70]  We go do it.
[2409.04 --> 2410.08]  Is that a new keyword?
[2410.46 --> 2412.62]  As soon as we strayed away from that philosophy.
[2412.98 --> 2413.28]  Uh-oh.
[2413.42 --> 2413.60]  Yeah.
[2413.92 --> 2414.96]  I think we're breaking up.
[2415.14 --> 2416.42]  We're getting quantum interference.
[2416.70 --> 2417.10]  Oh, no.
[2417.50 --> 2418.56]  I'm getting quantum interference.
[2418.74 --> 2418.94]  Hello.
[2419.24 --> 2419.52]  Hello.
[2419.78 --> 2420.38]  Can you hear me?
[2420.42 --> 2420.62]  Hello.
[2420.70 --> 2421.10]  Yeah, yeah.
[2421.26 --> 2421.94]  We hear you now.
[2422.04 --> 2422.54]  We hear you.
[2422.54 --> 2425.14]  I think the security forces might be outside.
[2425.72 --> 2429.88]  I heard the sound of some servos earlier, and they might be looking for me.
[2430.48 --> 2431.10]  I'm not sure.
[2431.78 --> 2433.18]  They might know what I'm doing.
[2433.78 --> 2435.70]  That lens flare is amazing, by the way.
[2435.88 --> 2440.54]  I know it's not good for a podcast, but he's got, I just want people to know at home, the
[2440.54 --> 2441.86]  effort that Ron has gone to.
[2441.92 --> 2446.92]  We're going to have to post some pictures of this on our GoTimeFM Twitter channel, because
[2446.92 --> 2447.58]  you won't believe it.
[2448.20 --> 2451.38]  D, Burra91 on Twitter says, the language is fine.
[2451.38 --> 2458.82]  I'd go for more automated tooling and docs around majority use cases, like APIs and things.
[2459.70 --> 2465.74]  Go kind of, you know, a lot of the benefits we had with GoFund and just having a few ways
[2465.74 --> 2468.94]  of doing things meant we could kind of cooperate much easier.
[2469.56 --> 2473.90]  Should we have done that also for common things like JSON APIs?
[2474.20 --> 2479.72]  Because they are very common still, and why not have a standard way to do them as well?
[2480.28 --> 2481.36]  And we've lost him.
[2482.06 --> 2482.70]  Sorry, everybody.
[2482.90 --> 2489.70]  If you're watching live, we are just experiencing some technical difficulties because Ron is
[2489.70 --> 2492.74]  broadcasting from 30 years in the future.
[2492.74 --> 2494.78]  I think you said 2053.
[2495.52 --> 2499.16]  Just a normal GoTime episode apart from that, isn't it?
[2499.34 --> 2499.50]  Yeah.
[2499.58 --> 2500.84]  So we can go back to the topic.
[2500.94 --> 2505.24]  Finally, we stopped off at the perfect time, which is also talking exactly about APIs.
[2505.24 --> 2507.76]  So what is a standard way of doing that?
[2508.10 --> 2509.52]  Why is JSON API not standardized?
[2509.52 --> 2515.04]  Well, I mean, like, because there is a lot of people have JSON APIs, but there's loads
[2515.04 --> 2515.88]  of ways to do it.
[2516.10 --> 2517.18]  You just build it yourself.
[2517.66 --> 2521.14]  So you can use like the JSON marshall and you can use the HTTP handlers and things.
[2521.26 --> 2526.68]  But there's lots of other stuff in there, like dealing with responses and code, you know,
[2526.74 --> 2528.48]  that's quite common, those kinds of things.
[2528.90 --> 2532.56]  Some languages like Ruby, obviously, and they're really frameworks that do it.
[2532.56 --> 2533.98]  They do solve that problem.
[2534.20 --> 2537.42]  And you end up like everyone then, you know, they write the same code.
[2537.52 --> 2538.02]  It looks the same.
[2538.10 --> 2540.04]  In the same way, GoFund gives us that in Go.
[2540.36 --> 2540.44]  Yeah.
[2540.50 --> 2540.98]  So I don't know.
[2541.06 --> 2545.44]  I wonder if there's space for just in the standard library, more things that help you
[2545.44 --> 2547.88]  build kind of simple JSON APIs.
[2548.20 --> 2549.16]  It'd be quite nice.
[2549.34 --> 2552.34]  I mean, you can do it quite nicely just with the basic stuff.
[2552.34 --> 2557.14]  But like this router, for example, most people don't use that router unless you, you know,
[2557.14 --> 2558.36]  so they're very simple cases.
[2558.48 --> 2562.48]  They don't really use the router from the standard library because you have to parse the path
[2562.48 --> 2564.88]  yourself if you want to pull variables out and things like that.
[2564.94 --> 2567.12]  And it's pretty common and people have solved it.
[2567.24 --> 2569.18]  So there are packages that we use there.
[2569.50 --> 2573.60]  I wonder if we can now reconnect Ron.
[2573.96 --> 2574.32]  Hello.
[2574.84 --> 2576.18]  Ron, do you hear us?
[2576.28 --> 2577.10]  Is this thing on?
[2577.24 --> 2577.60]  Hello.
[2578.20 --> 2578.76]  You're back.
[2579.10 --> 2579.32]  Yeah.
[2579.42 --> 2579.62]  Yeah.
[2579.62 --> 2580.18]  You're back.
[2580.32 --> 2581.84]  Receiving you loud and clear again.
[2581.84 --> 2583.70]  There were some drones at the door.
[2584.00 --> 2584.48]  Oh.
[2584.68 --> 2587.60]  I wasn't sure if it was a delivery or they were trying to kill me.
[2588.44 --> 2591.12]  Speaking of that, how is Mark Bates in the future?
[2591.40 --> 2592.72]  Oh, yeah.
[2592.92 --> 2594.18]  It's too bad about Mark.
[2594.50 --> 2595.78]  A drone finally got him.
[2596.34 --> 2597.58]  Wasn't one of mine though.
[2598.36 --> 2599.10]  I don't know.
[2599.40 --> 2600.72]  Maybe it was just destiny.
[2601.16 --> 2606.78]  There's lots of conferences where Ron would be demoing something he's built using some kind
[2606.78 --> 2611.42]  of cool AI or face detection or object tracking or something and a drone.
[2611.42 --> 2614.58]  And in the conference would, you know, the drone would spin up.
[2614.66 --> 2616.74]  Part of his live demo included a live drone.
[2617.06 --> 2621.50]  And one time I think, did you teach it Mark's face so it would chase him and kill him?
[2621.58 --> 2622.56]  It was not to kill him.
[2622.60 --> 2623.50]  It was just to chase him.
[2623.84 --> 2625.52]  It's just to chase him, your honor.
[2625.80 --> 2626.92]  It was just to scare him a little.
[2627.02 --> 2627.56]  That's all.
[2627.90 --> 2628.66]  It worked.
[2628.66 --> 2629.14]  Yeah.
[2629.24 --> 2632.64]  Come to think of it, maybe eventually it just got the right idea.
[2633.60 --> 2638.46]  Stochastic dronery or whatever, you know, the drone just decided on its own.
[2638.80 --> 2643.42]  Hey, when everything's in AI, who could say why anything is doing anything anymore?
[2643.52 --> 2646.06]  You turn on your air conditioning, it turns itself off.
[2646.40 --> 2648.20]  Is it because it's mad at you?
[2648.64 --> 2651.00]  You know, is it because you didn't pay your bill?
[2651.12 --> 2651.64]  Hard to know.
[2651.64 --> 2654.74]  You know, it's because you didn't ask please when you turned it on.
[2654.94 --> 2655.80]  It's very complicated.
[2656.28 --> 2657.78]  Wait, is this a reference to go please?
[2657.86 --> 2659.12]  Is that still working?
[2659.36 --> 2660.66]  Oh, no, that never worked.
[2660.92 --> 2661.88]  I don't know what that is.
[2662.12 --> 2665.56]  Never in your timeline probably only means like a decade and then it went out.
[2665.72 --> 2666.58]  Well, that's very suspicious.
[2666.90 --> 2668.76]  Is this the right past I'm talking to?
[2668.88 --> 2669.58]  How do I know?
[2669.98 --> 2672.12]  I better ask Lambda again to make sure.
[2672.46 --> 2673.32]  Yeah, ask Copilot.
[2673.76 --> 2674.80]  Oh, no, I can't ask Copilot.
[2674.86 --> 2676.06]  I'm supposed to be working right now.
[2676.48 --> 2677.94]  And here I am checking social media.
[2677.94 --> 2686.36]  Well, whatever timeline you're in or indeed any point in space, it's time for Unpopular Opinions.
[2703.50 --> 2706.76]  Okay, this is going to be very interesting hearing from the future.
[2706.76 --> 2706.84]  Yeah.
[2707.20 --> 2709.62]  Ron, do you have an Unpopular Opinion for us today?
[2710.08 --> 2713.60]  Oh, I think all I've had is Unpopular Opinions so far today.
[2713.96 --> 2719.86]  If any of those in your timeline seem to make any sense at all, then that's all I got.
[2720.18 --> 2720.52]  Oh, yeah.
[2720.96 --> 2722.54]  Natalie, do you have any Unpopular Opinions?
[2723.04 --> 2723.44]  Yes.
[2723.70 --> 2723.98]  Really?
[2724.18 --> 2725.32]  Coffee should not be sweet.
[2725.88 --> 2727.14]  Oh, yeah.
[2727.28 --> 2728.48]  I think I'm with you on this.
[2728.88 --> 2730.66]  Do you still have coffee in the future, Ron?
[2730.74 --> 2731.26]  No, no.
[2731.30 --> 2732.26]  We have Coffium, though.
[2732.60 --> 2732.96]  Coffium.
[2732.96 --> 2740.02]  Yeah, Coffium, it tastes just like coffee, except it's from yeast and some kind of other additives and caffeine, of course.
[2740.14 --> 2740.74]  It's not as caffeine.
[2741.78 --> 2742.64]  It sounds all right.
[2742.82 --> 2743.32]  Is it sweet?
[2743.52 --> 2744.22]  No, it's not sweet.
[2744.58 --> 2745.68]  It's kind of more like...
[2745.68 --> 2747.08]  Well, it sounds like the Opinion works.
[2747.12 --> 2751.66]  It's a little bit more like Vegemite, but with caffeine.
[2752.22 --> 2752.44]  Yeah.
[2752.78 --> 2753.14]  Marmite.
[2753.24 --> 2753.94]  It's not really good.
[2753.94 --> 2755.80]  Yeah, but okay.
[2756.16 --> 2758.22]  So, yeah, but Natalie, I think you might be right.
[2758.40 --> 2760.26]  But tell me, have you had it sweet recently?
[2760.62 --> 2761.62]  No, not recently.
[2761.92 --> 2763.28]  Right, but you have in the past.
[2763.60 --> 2763.84]  Yes.
[2764.08 --> 2764.68]  And...
[2764.68 --> 2770.72]  I think even when I started drinking coffee for a very short period, I would drink it sweet, but just...
[2770.72 --> 2772.34]  There's different types of coffee, you know.
[2772.58 --> 2773.78]  I don't know, Ron, if you remember.
[2774.60 --> 2777.54]  Well, the thing I keep amazing is you keep talking about sugar.
[2777.84 --> 2781.12]  They burned all the sugar when they did sugar coin.
[2781.36 --> 2782.28]  Must have smelled delicious.
[2782.28 --> 2783.78]  And then there was no sugar left.
[2783.86 --> 2784.36]  That was it.
[2784.40 --> 2785.28]  All the sugar was gone.
[2785.68 --> 2786.52]  Oh, just caramel.
[2787.10 --> 2788.76]  Yeah, I guess that probably...
[2788.76 --> 2789.26]  The rivers.
[2789.56 --> 2790.56]  Just rivers of caramel.
[2791.08 --> 2791.70]  That was it.
[2791.82 --> 2792.04]  Yeah.
[2793.98 --> 2799.66]  But I had a coffee recently, and I sweetened it just to try it, because I always drink it without sweetening it.
[2800.00 --> 2801.30]  And it was rubbish.
[2801.96 --> 2803.22]  I prefer it just...
[2803.22 --> 2805.88]  It's just honest and stark.
[2806.12 --> 2807.40]  You should try electric coffee.
[2807.78 --> 2809.28]  Our electric coffees are the best.
[2809.48 --> 2809.78]  Oh, yeah?
[2810.00 --> 2810.56]  What do you do?
[2810.62 --> 2811.22]  Download them?
[2811.22 --> 2814.58]  Yeah, you just hit the button, and you've had the coffee.
[2815.04 --> 2816.04]  They're kind of the same thing.
[2816.20 --> 2817.04]  You've already had it?
[2817.20 --> 2817.44]  Yeah.
[2818.02 --> 2818.78]  It's genius.
[2819.16 --> 2820.70]  What do you have the memory just put in?
[2820.80 --> 2823.38]  Is this what stands behind all those buy me coffee buttons?
[2823.70 --> 2824.54]  Yeah, exactly.
[2825.20 --> 2826.28]  That's where they end up.
[2826.48 --> 2827.12]  Oh, man.
[2827.14 --> 2828.58]  I was wondering all this time.
[2829.04 --> 2830.76]  Eventually, the messages get through.
[2830.88 --> 2831.80]  It just takes a while.
[2832.24 --> 2835.06]  All of a sudden, you're just like, coffee, coffee, coffee.
[2835.40 --> 2835.70]  It's great.
[2835.78 --> 2836.86]  So you don't get a coffee?
[2836.86 --> 2841.12]  Is it that you just feel like you've had one, or you have the memory of having a coffee just then?
[2841.24 --> 2843.00]  It's the experience of a coffee.
[2843.32 --> 2844.96]  I can't really define it more than that.
[2845.04 --> 2845.34]  Okay?
[2845.56 --> 2849.12]  It's sort of a quantia sort of thing, not really ineffable.
[2849.62 --> 2849.98]  Right.
[2849.98 --> 2853.98]  That's a real thing, you know, in information theory.
[2854.54 --> 2854.80]  Yeah.
[2855.22 --> 2855.78]  Go on, then.
[2856.00 --> 2857.02]  Do you want to talk more about it?
[2857.26 --> 2858.36]  It could be your unpopular opinion.
[2858.66 --> 2865.30]  Oh, my unpopular opinion is you people were way too afraid of AI in the past.
[2865.42 --> 2868.18]  You should have been afraid of other humans a lot more.
[2868.94 --> 2871.22]  That's my unpopular opinion from here in the future.
[2871.94 --> 2873.48]  Some of my best friends are AIs.
[2874.94 --> 2875.88]  They buy you coffee.
[2876.18 --> 2877.18]  They send me a-
[2877.18 --> 2878.98]  Downloadable coffee.
[2878.98 --> 2880.26]  Just in an email.
[2880.52 --> 2881.06]  Coffee I'm writing.
[2881.38 --> 2882.16]  Just as an attachment.
[2882.40 --> 2883.82]  What's the mime type for that?
[2884.46 --> 2890.34]  Well, there actually was an RFC for the coffee pot protocol.
[2890.46 --> 2890.90]  Was there?
[2891.04 --> 2891.90]  Oh, yes.
[2892.26 --> 2896.14]  And I believe at some point the AIs discovered that, and they thought,
[2896.38 --> 2901.24]  wow, humans really must care about coffee if they've made a whole internet protocol just about it.
[2901.24 --> 2901.64]  Yeah.
[2901.88 --> 2909.06]  I think it's RFC 2324, Hypertext Coffee Pot Control Protocol.
[2909.50 --> 2909.90]  Exactly.
[2910.36 --> 2915.64]  So they interpreted that as that was one of the more important parts of human civilization to completely automate.
[2916.36 --> 2916.66]  So-
[2916.66 --> 2918.12]  It's a fair point, to be fair.
[2918.12 --> 2923.94]  So actually, quite a few people have a coffee port installed by the time they hit like seven years old.
[2924.02 --> 2925.42]  I've basically got one of those.
[2925.74 --> 2925.96]  Yeah.
[2926.36 --> 2928.38]  So a lot of things haven't really changed that much.
[2929.62 --> 2930.52]  Sounds good, though.
[2930.84 --> 2933.72]  Is HTTP status 418 still a thing?
[2934.22 --> 2937.90]  Does it still tell you you're a teapot or it's a teapot?
[2938.02 --> 2938.30]  Oh, no.
[2938.36 --> 2939.00]  There's no tea.
[2939.24 --> 2939.88]  There's only coffee.
[2939.98 --> 2943.56]  So it was changed, basically, the HTTP status to I'm a coffee?
[2943.90 --> 2945.28]  No, there was never such a protocol.
[2945.88 --> 2946.24]  Okay.
[2946.58 --> 2947.20]  Sorry I asked.
[2947.28 --> 2947.98]  I did not mean to.
[2948.06 --> 2952.34]  Now that we don't have an internet wayback machine, we don't have any way to tell whether
[2952.34 --> 2953.50]  or not there ever was.
[2953.66 --> 2954.26]  Well, you don't need one.
[2954.34 --> 2956.46]  We could just go on a website now and send it to you.
[2956.60 --> 2957.00]  Save us.
[2957.06 --> 2959.40]  You're on that page and save us, and it'll make the folder.
[2959.66 --> 2963.94]  And then all the loads of files inside, you know, and the index page goes alongside the folder.
[2963.94 --> 2966.62]  No, I can't receive files from the past.
[2966.82 --> 2969.02]  I haven't already downloaded in the past.
[2969.16 --> 2971.58]  We could leave files from you here, could we?
[2971.88 --> 2973.30]  Wait, does that make sense?
[2973.56 --> 2977.04]  What, the whole episode or just that bit?
[2977.12 --> 2978.04]  Did you just do NFTs?
[2978.28 --> 2978.74]  No, no.
[2978.88 --> 2981.32]  It ended up you had to pay people for them.
[2981.92 --> 2984.60]  They ended up going negative, like negative interest rates.
[2984.66 --> 2985.74]  They went to negative values.
[2985.84 --> 2987.80]  All of a sudden, people are like, you want to own the NFT?
[2987.96 --> 2988.62]  I need some money.
[2988.78 --> 2990.94]  And it was like, oh, what a mess.
[2991.74 --> 2992.76]  Yeah, no one saw that coming.
[2993.06 --> 2994.54]  NFTs ended up being a debt.
[2994.90 --> 2995.68]  That would be interesting.
[2995.68 --> 3002.20]  But the one thing that was cool is musicians started actually selling downloadable archives of audio.
[3002.66 --> 3005.82]  And people would like download them and listen to them.
[3005.90 --> 3007.60]  It was kind of amazing.
[3007.86 --> 3008.66]  Sounds weird.
[3009.00 --> 3011.42]  But then all of a sudden, all of the robot orchestras took over.
[3011.64 --> 3012.54]  They're going to be good.
[3012.54 --> 3019.10]  Look, a human DJ had a physical limit of, let's just say, 48 hours straight.
[3019.22 --> 3019.40]  Yeah.
[3019.80 --> 3020.12]  Okay.
[3020.54 --> 3025.78]  Whereas a robot DJ could get, like, they could play a 120-hour set.
[3026.14 --> 3026.82]  No problem.
[3027.14 --> 3030.02]  I mean, what human could keep up with that, I ask you?
[3030.62 --> 3031.86]  Some of the Berlin DJs?
[3032.02 --> 3033.64]  I thought that's all DJs did anyway.
[3033.64 --> 3044.34]  I think that some of those humans downloaded themselves into those first robotic DJs just so that they would have the stamina to reach that level of dance floor completion.
[3044.78 --> 3047.86]  I've often wondered that about DJs, human DJs anyway.
[3048.24 --> 3050.48]  They just, you're making the robots do it now.
[3050.70 --> 3052.02]  They're just playing stuff on their laptop.
[3052.18 --> 3053.70]  I don't know what they're doing.
[3054.88 --> 3055.86]  Never understood it.
[3055.92 --> 3057.82]  But, you know, I don't want to have a go at DJs.
[3057.84 --> 3058.90]  I'm sure it is very skilled.
[3059.06 --> 3060.00]  Please don't write in.
[3060.24 --> 3060.78]  Oh, no, no.
[3060.84 --> 3062.34]  That was the only music left.
[3062.34 --> 3068.74]  If you don't play at least five different songs at the same time in the future, like, people can't even hear the music.
[3069.90 --> 3070.90]  It's just too boring.
[3071.76 --> 3071.96]  Yeah.
[3072.32 --> 3073.48]  It's a tension span, isn't it?
[3073.64 --> 3074.76]  We don't have a lot of time.
[3074.82 --> 3075.24]  You know it.
[3075.36 --> 3079.84]  In a one-minute song, you've got to pack in at least eight or nine different samples.
[3080.40 --> 3082.12]  That's the trend in the future of music.
[3082.44 --> 3083.06]  Sounds efficient.
[3083.28 --> 3084.46]  Sounds not bad.
[3084.64 --> 3084.84]  Yeah.
[3085.20 --> 3086.50]  You know, if you don't like the song, don't worry.
[3086.58 --> 3087.78]  A new one will be on in one minute.
[3088.06 --> 3088.22]  Yeah.
[3088.68 --> 3090.14]  Are monkeys still around, Ron?
[3090.14 --> 3092.56]  So I find that comment offensive.
[3093.00 --> 3093.22]  Oh.
[3093.42 --> 3095.18]  They are known as primate professionals.
[3096.30 --> 3097.88]  You know, they do my taxes.
[3098.62 --> 3104.52]  Primate professional is one of my mechanics that maintains my prosthetic limbs.
[3105.32 --> 3107.12]  So I really resent that comment.
[3107.38 --> 3108.76]  You know, I think you should take that back.
[3108.82 --> 3109.42]  They're primates.
[3109.60 --> 3110.12]  Fair enough.
[3110.56 --> 3110.80]  Yes.
[3110.92 --> 3111.74]  Primate professionals.
[3112.14 --> 3112.54]  Fair play.
[3113.70 --> 3114.48]  Well, okay.
[3114.68 --> 3115.24]  I'll tell you what.
[3116.14 --> 3119.92]  I mean, obviously, Ron, we want to pick your brains about the future all night.
[3120.06 --> 3122.02]  But unfortunately, we've run out of time.
[3122.42 --> 3126.02]  Well, that's good because I'm actually, my lasers are almost out of the batteries.
[3126.26 --> 3127.54]  I'm going to have to start pedaling.
[3127.92 --> 3131.36]  I'm going to have to be pedaling for at least six or seven months to recharge now.
[3131.36 --> 3137.54]  So I wish all of you gophers in the past a tremendous lifetime.
[3138.10 --> 3144.24]  I hope that you're able to listen to some of this and at least know what not to do with
[3144.24 --> 3145.78]  go in the future.
[3146.22 --> 3147.40]  Thank you, dead program.
[3147.56 --> 3148.32]  Ron Evans.
[3148.32 --> 3150.76]  As always, absolute pleasure.
[3151.46 --> 3155.28]  And I've been Matt Raya and, of course, my co-host, Natalie Pistinovich.
[3155.50 --> 3156.54]  See you next time.
[3160.88 --> 3163.14]  Your next step is to subscribe.
[3163.44 --> 3167.56]  If you haven't already, head to gotime.fm for all the ways.
[3168.02 --> 3172.00]  And don't forget to follow us on Twitter so you can join in on the Unpop polls.
[3172.36 --> 3173.54]  We are at Gotime FM.
[3174.02 --> 3176.36]  Did you catch our changelog episode with the Graphite team?
[3176.36 --> 3178.86]  If not, here's a taste of what you're missing.
[3179.50 --> 3183.68]  It's interesting how many stories are like this where it's not your main product that
[3183.68 --> 3184.68]  becomes your main product.
[3184.82 --> 3185.38]  I think Slack.
[3185.46 --> 3187.40]  Wasn't Slack like the internal chat app?
[3187.48 --> 3190.86]  They were trying to build games and they're like, wow, this Slack thing is pretty cool
[3190.86 --> 3194.42]  that we built and started selling that and obviously became a big deal.
[3194.60 --> 3198.74]  Same thing with Flickr, which is like no one knows about Flickr anymore, right?
[3198.82 --> 3203.54]  But Flickr began as like some sort of Flash video game and then it turned into image sharing.
[3203.88 --> 3205.54]  It was the Instagram before Instagram.
[3205.54 --> 3206.36]  There you go.
[3206.72 --> 3208.94]  I think it's one of the purest ways to discover something, right?
[3208.98 --> 3212.90]  If you solve the need for yourself without some grand idea of making it into a company,
[3213.04 --> 3214.82]  but it ends up being that useful.
[3214.96 --> 3215.82]  People really want it.
[3216.10 --> 3216.70]  It's quite pure.
[3217.30 --> 3217.48]  Yeah.
[3217.88 --> 3220.42]  It kind of leans to the iteration process too, right?
[3220.44 --> 3222.80]  Like even innovation requires iteration.
[3222.98 --> 3223.38]  Totally.
[3223.66 --> 3223.88]  Right.
[3223.88 --> 3227.86]  You can't get to a problem or even a solution without having a problem.
[3227.98 --> 3231.88]  And sometimes you have to sort of go on a journey, which might be the wrong tool or the wrong
[3231.88 --> 3232.24]  thing.
[3232.30 --> 3238.44]  And you sort of discover from your exhaust of iteration that you got this down in the rough
[3238.44 --> 3240.74]  if you just put things to work.
[3240.84 --> 3242.12]  And there you go.
[3242.12 --> 3246.30]  Stacked diffs are super cool for fast moving code review.
[3246.62 --> 3250.56]  Listen to the whole thing at changelog.fm slash 491.
[3250.88 --> 3255.96]  Thanks again to Fastly for CDNing for us, to Breakmaster Cylinder for keeping our beat
[3255.96 --> 3258.02]  supply secure, and to you for listening.
[3258.40 --> 3259.18]  We appreciate you.
[3259.18 --> 3265.56]  Next up, Matt, Natalie, and myself have a deep discussion on development velocity, estimations,
[3265.78 --> 3267.08]  and all that agile jazz.
[3267.60 --> 3271.16]  That's something to look forward to next time on GoTime.
