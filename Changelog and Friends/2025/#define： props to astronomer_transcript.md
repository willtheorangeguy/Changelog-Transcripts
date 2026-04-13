[0.00 --> 21.52]  Welcome to Changelog and Friends, a weekly talk show about oversharing shower habits.
[22.06 --> 27.50]  Thanks to our partners at Fly.io, the public cloud built for developers who ship.
[27.50 --> 31.14]  We love Fly. You might too. Learn more at Fly.io.
[31.60 --> 33.42]  Okay, let's play.
[42.22 --> 44.52]  Well, friends, it's all about faster builds.
[44.78 --> 49.28]  Teams with faster builds ship faster and win over the competition.
[49.68 --> 50.46]  It's just science.
[50.80 --> 54.40]  And I'm here with Kyle Galbraith, co-founder and CEO of Depot.
[54.40 --> 60.54]  Okay, so Kyle, based on the premise that most teams want faster builds, that's probably a truth.
[60.82 --> 65.36]  If they're using CI providers with their stock configuration or GitHub actions, are they wrong?
[65.54 --> 67.36]  Are they not getting the fastest builds possible?
[67.82 --> 73.66]  I would take it a step further and say if you're using any CI provider with just the basic things that they give you,
[73.78 --> 81.60]  which is if you think about a CI provider, it is in essence a lowest common denominator generic VM.
[81.60 --> 87.18]  And then you're left to your own devices to essentially configure that VM and configure your build pipeline.
[87.52 --> 94.22]  Effectively pushing down to you, the developer, the responsibility of optimizing and making those builds fast.
[94.54 --> 99.20]  Making them fast, making them secure, making them cost effective, like all pushed down to you.
[99.20 --> 112.92]  The problem with modern day CI providers is there's still a set of features, a set of capabilities that a CI provider could give a developer that makes their builds more performant out of the box,
[113.04 --> 118.28]  makes their builds more cost effective out of the box and more secure out of the box.
[118.28 --> 126.36]  I think a lot of folks adopt GitHub actions for its ease of implementation and being close to where their source code already lives inside of GitHub.
[126.90 --> 131.20]  And they do care about build performance and they do put in the work to optimize those builds.
[131.36 --> 135.60]  But fundamentally, CI providers today don't prioritize performance.
[135.84 --> 139.74]  Performance is not a top level entity inside of generic CI providers.
[139.74 --> 140.42]  Yes.
[140.86 --> 141.66]  Okay, friends.
[141.96 --> 142.60]  Save your time.
[142.72 --> 151.80]  Get faster builds with Depot, Docker builds, faster GitHub action runners, and distributed remote caching for Bazel, Go, Gradle, Turbo Repo, and more.
[152.26 --> 158.48]  Depot is on a mission to give you back your dev time and help you get faster build times with a one-line code change.
[158.82 --> 160.46]  Learn more at Depot.dev.
[160.58 --> 162.28]  Get started with a seven-day free trial.
[162.70 --> 164.14]  No credit card required.
[164.32 --> 166.72]  Again, Depot.dev.
[166.72 --> 182.84]  Welcome to another awesome episode of Pound Define, our game of obscure jargon, fake definitions, and expert tomfoolery.
[183.62 --> 192.90]  Our contestants checked their imposter syndrome at the door because they either know what these words mean or they're going to fake it until they make their peers think they do.
[194.16 --> 196.28]  Adam, you've played this game a lot.
[196.72 --> 198.48]  I feel like I've lost every time, Jared.
[198.48 --> 199.24]  You're going to win today?
[199.86 --> 200.56]  Oh, my.
[200.66 --> 201.12]  Feeling good?
[201.38 --> 209.04]  Well, I'm not on video, so at least maybe in the clip, but my face is sad because I have not won yet, but maybe today.
[209.28 --> 209.50]  Maybe.
[209.64 --> 210.96]  You did have a nice accolade.
[211.04 --> 216.80]  I think our last time we played, one particular listener said your answers were always his favorite.
[217.72 --> 217.96]  Yeah.
[218.16 --> 218.68]  Well, you know.
[218.80 --> 219.82]  So that's kind of a win.
[219.90 --> 220.80]  You've got to win somewhere, right?
[221.28 --> 222.70]  That's as good as winning everything.
[223.08 --> 223.20]  Yeah.
[223.38 --> 223.60]  Yeah.
[223.68 --> 224.56]  Put that on a dagger.
[224.56 --> 237.12]  Okay, so for this particular game, we decided let's get some of our Changelog++ supporters, some of our diehard fans and our listeners to hop on the mic and play with us.
[237.12 --> 242.18]  So I put out a call and asked if anybody had a good setup, if they were free this afternoon.
[242.84 --> 244.02]  And I can't remember what else I said.
[244.24 --> 245.94]  Likes playing silly games.
[246.62 --> 247.90]  And we got three respondents.
[248.10 --> 249.20]  They are all here today.
[249.20 --> 251.96]  So one of them you may know because he's been on the pod before.
[252.06 --> 253.00]  It's Jamie Tana.
[253.24 --> 254.04]  Jamie, what's up, man?
[254.52 --> 254.72]  Hey.
[255.08 --> 255.68]  Great to be back.
[255.96 --> 256.32]  Been a while.
[256.64 --> 257.14]  There you are.
[257.28 --> 257.78]  You're here now.
[258.24 --> 260.86]  Are you good at making up fake definitions for real words?
[262.86 --> 263.84]  We're going to find out.
[265.52 --> 268.56]  I was going to say, that's perfect, like, real time.
[268.90 --> 269.10]  No.
[269.50 --> 269.82]  Okay.
[270.42 --> 271.78]  Audio listeners only out there.
[272.14 --> 273.76]  He was, like, not sure what to say.
[274.04 --> 276.00]  He's like, gosh, do I go for it or not?
[276.00 --> 277.54]  Because I'm going to be found out here.
[277.68 --> 278.90]  Should I boast or what?
[280.26 --> 284.24]  We're also joined by Spencer Lyon from Orlando.
[284.48 --> 285.02]  Welcome, Spencer.
[285.44 --> 285.78]  Thanks.
[285.88 --> 286.68]  Happy to be here.
[287.40 --> 291.88]  Hopefully, I'm rooting to maybe extend Adam's losing streak.
[292.00 --> 292.38]  I don't know.
[292.46 --> 295.12]  We'll see if Jamie, David, and I can make it happen.
[295.12 --> 297.64]  I think the odds are in your favor.
[298.00 --> 300.12]  Three to one if you're just playing blind.
[301.14 --> 301.66]  That's true.
[302.02 --> 302.30]  It's true.
[302.38 --> 304.60]  There's also the spread because I do get to participate
[304.60 --> 307.72]  in kind of a strange way.
[307.78 --> 310.20]  But we should introduce David E. David Aja.
[310.76 --> 311.44]  Welcome, David.
[311.90 --> 312.32]  Thank you.
[312.68 --> 313.28]  Happy to be here.
[313.44 --> 314.26]  First time, long time.
[314.64 --> 316.10]  Happy to have you as well.
[316.24 --> 319.58]  So how this game works is we have 10 rounds,
[320.28 --> 321.36]  if we need them all.
[322.00 --> 325.18]  But we also have a goal of 15 points,
[325.60 --> 328.20]  which you can score in multiple ways.
[328.20 --> 331.64]  So I will provide for each round a word
[331.64 --> 335.10]  with a couple of rounds that aren't quite standard.
[335.26 --> 336.94]  But a standard round is a word,
[337.12 --> 340.90]  which comes from the broad-ranging world of STEM.
[341.06 --> 343.32]  I've been extending it beyond STEM.
[343.46 --> 344.16]  There's some music.
[344.30 --> 345.26]  There's some video games.
[345.42 --> 350.10]  There's anything you might imagine a nerd would love in the mix.
[350.86 --> 355.04]  And these words are obscure and sometimes old and quite jargony.
[355.04 --> 359.42]  If you know the word's definition, you submit to me that.
[360.38 --> 363.68]  If you submit that correctly right away, you get three points
[363.68 --> 367.16]  and you get to sit that round out because you know the definition.
[367.78 --> 370.06]  If you don't know the definition, you make one up.
[370.34 --> 371.10]  You submit that.
[371.48 --> 373.54]  And then I gather them all together and I read them
[373.54 --> 375.08]  along with the actual definition.
[375.82 --> 378.06]  And you all take your turns trying to identify
[378.06 --> 380.88]  which one is the correct definition
[380.88 --> 384.04]  for each person who guesses it correctly.
[384.20 --> 385.46]  At that point, you get two points.
[385.74 --> 388.84]  And for each person you trick into selecting your definition,
[389.18 --> 390.28]  you get one point.
[390.34 --> 393.96]  If nobody after the end of the round
[393.96 --> 395.82]  actually lands on the correct definition,
[396.10 --> 399.44]  I, your humble moderator, get four points.
[400.36 --> 402.82]  First one to 15 points wins.
[402.90 --> 403.38]  Any questions?
[404.96 --> 405.70]  Let's rock.
[405.98 --> 408.20]  I guess I just explained that so well.
[408.40 --> 409.68]  There's no questions.
[409.68 --> 411.94]  Okay, let's start then.
[412.62 --> 415.00]  Hopping right in to round one,
[415.18 --> 418.96]  where the word for round one is myoclonus.
[421.50 --> 422.10]  Myoclonus.
[422.16 --> 427.16]  That's M-Y-O-C-L-O-N-U-S.
[427.74 --> 432.84]  Please submit to me your definitions for the word myoclonus now.
[438.84 --> 439.32]  Myoclonus.
[439.68 --> 445.78]  Do we get points for making Jared laugh while reading?
[446.22 --> 447.08]  That's the question.
[447.46 --> 447.90]  In here.
[448.02 --> 449.92]  Yeah, it would give you a pat on the back.
[449.92 --> 450.50]  Get some cred.
[450.78 --> 451.06]  Some street cred.
[451.06 --> 452.26]  No real official points, but yes.
[452.26 --> 453.40]  You get docked points.
[454.50 --> 455.82]  By making my job harder.
[455.96 --> 456.30]  I was going to say,
[456.62 --> 458.74]  and then you also have to watch people's faces
[458.74 --> 459.96]  out of their being read out
[459.96 --> 461.22]  to see if someone's like,
[461.34 --> 462.00]  oh yeah, that was,
[462.14 --> 462.76]  that was my,
[463.16 --> 464.00]  that was a good one.
[464.02 --> 464.30]  That was funny.
[464.30 --> 465.98]  There are some social cues, yeah,
[466.08 --> 466.54]  that you can,
[466.90 --> 467.64]  you can look out for.
[467.70 --> 469.16]  Unless you're me and I do nothing.
[469.24 --> 470.02]  I have a stone case,
[470.16 --> 471.14]  a stone face here.
[471.84 --> 472.78]  There's no giveaways.
[472.92 --> 473.80]  This is poker to me.
[474.54 --> 475.60]  This is poker to me.
[475.60 --> 477.52]  There definitely is a giveaway
[477.52 --> 478.92]  in one of the rounds
[478.92 --> 480.42]  and I'm looking forward to
[480.42 --> 481.46]  taking advantage of that.
[481.66 --> 481.98]  Hmm.
[483.14 --> 485.04]  I have Spencer's,
[485.12 --> 485.48]  David's,
[485.52 --> 486.22]  and Jamie's.
[487.02 --> 488.58]  Which means we're just waiting on Adam.
[488.94 --> 489.26]  Chucky.
[489.92 --> 490.56]  Yeah, I know.
[490.62 --> 490.98]  I'm sorry.
[491.20 --> 493.20]  I don't know how to describe it.
[493.42 --> 494.34]  I'm working on that.
[494.34 --> 496.00]  So one suggestion that we've had
[496.00 --> 497.10]  is to,
[497.26 --> 498.90]  is to post
[498.90 --> 501.16]  all the definitions
[501.16 --> 502.60]  to you all
[502.60 --> 503.78]  and then read them once.
[504.22 --> 504.56]  Hmm.
[504.78 --> 505.72]  And that cuts down
[505.72 --> 507.18]  on the people asking to repeat.
[507.60 --> 508.84]  Now I think the asking to repeat
[508.84 --> 509.54]  is kind of funny,
[509.84 --> 511.00]  but it does get old.
[511.42 --> 512.30]  That's kind of the funny part.
[512.78 --> 513.82]  My fear with,
[514.02 --> 515.22]  the reason I haven't done it
[515.22 --> 516.32]  is because
[516.32 --> 518.04]  there's a certain amount of
[518.04 --> 519.12]  tells,
[519.38 --> 520.24]  even in the text,
[520.42 --> 521.74]  whether it's misspellings
[521.74 --> 523.66]  or the way that I present things.
[524.34 --> 526.38]  That can sometimes lead to you
[526.38 --> 527.42]  knowing whether or not it's,
[527.68 --> 528.24]  you know,
[528.34 --> 528.80]  real.
[529.62 --> 530.36]  So I'm curious,
[530.44 --> 532.24]  as we are here in the first round,
[532.94 --> 535.50]  what you all think about that.
[536.08 --> 536.24]  I mean,
[536.26 --> 538.24]  if you had some kind of tokenizer
[538.24 --> 540.44]  that like stripped all the punctuation
[540.44 --> 540.90]  and things,
[540.98 --> 542.20]  that might be a way to quickly
[542.20 --> 544.86]  homogenize things a little bit.
[545.16 --> 546.56]  The misspellings thing
[546.56 --> 548.38]  is probably harder to catch.
[549.08 --> 549.30]  Yeah.
[549.78 --> 551.38]  Kind of like the spawn-eity.
[551.62 --> 553.28]  It's funny to hear as a listener.
[554.10 --> 554.32]  Right.
[554.34 --> 555.14]  It equals reactions.
[556.76 --> 557.12]  Yeah,
[557.16 --> 557.62]  I think that I...
[557.62 --> 558.24]  Maybe it's not the best
[558.24 --> 559.20]  for game integrity,
[559.46 --> 561.06]  but maybe for entertainment value,
[561.18 --> 562.18]  it's a good choice.
[562.32 --> 563.76]  The reason why I,
[563.84 --> 564.96]  I would lean towards
[564.96 --> 565.56]  leaving it alone
[565.56 --> 566.80]  is because as a listener,
[566.96 --> 568.06]  you don't get the advantage
[568.06 --> 568.88]  of being able to look
[568.88 --> 569.46]  at the sentences.
[569.78 --> 571.10]  And so having them be repeated
[571.10 --> 572.38]  for you is actually helpful
[572.38 --> 572.92]  because you're like,
[572.96 --> 573.34]  I don't remember
[573.34 --> 574.20]  what that one was either.
[574.70 --> 576.34]  And so there's a camaraderie
[576.34 --> 576.80]  to that,
[577.10 --> 577.44]  you know,
[577.94 --> 579.28]  but I fully admit
[579.28 --> 580.64]  that it's not efficient at all
[580.64 --> 581.08]  because you're like,
[581.12 --> 582.14]  can you say that one again?
[582.14 --> 582.96]  And then it gets to be like,
[583.06 --> 583.26]  dude,
[583.32 --> 584.32]  I've said it six times,
[584.40 --> 584.60]  Adam,
[584.68 --> 585.02]  come on,
[585.06 --> 585.30]  stop.
[586.34 --> 586.68]  Oh,
[586.68 --> 587.50]  my name's in there?
[589.76 --> 590.12]  Well,
[590.20 --> 591.12]  you might be the most
[591.12 --> 592.18]  requester of them all.
[593.18 --> 594.80]  I've played the most.
[594.94 --> 595.58]  I've played the most.
[595.74 --> 596.08]  Right.
[596.08 --> 596.74]  Yeah,
[596.78 --> 598.02]  I think no definitions
[598.02 --> 598.58]  in the chat
[598.58 --> 599.44]  make sense.
[599.86 --> 600.30]  Okay.
[600.88 --> 602.38]  It's been a few people
[602.38 --> 603.18]  that have said this something,
[603.30 --> 604.82]  not like a major complaint
[604.82 --> 605.20]  or anything.
[606.32 --> 607.24]  All right.
[607.90 --> 611.18]  I have all five definitions
[611.18 --> 613.08]  for myoclinus.
[613.44 --> 614.66]  That's your four
[614.66 --> 616.54]  as well as the correct definition.
[617.08 --> 618.78]  They are number one,
[619.06 --> 620.70]  a term that defines
[620.70 --> 622.36]  the family of different forms
[622.36 --> 624.30]  of life that undergo mitosis.
[624.30 --> 625.88]  Number two,
[626.16 --> 627.00]  an eye disorder
[627.00 --> 629.08]  that results in double vision.
[629.62 --> 630.24]  Number three,
[630.38 --> 630.86]  a pre...
[630.86 --> 635.22]  It's been a while
[635.22 --> 635.90]  since I've done this.
[636.02 --> 636.18]  Okay.
[636.74 --> 637.32]  Number three,
[637.44 --> 638.80]  a precursor to the monocle,
[638.92 --> 640.92]  an ancient Mayan scene aid
[640.92 --> 643.14]  used to magnify small objects.
[643.64 --> 644.24]  Number four,
[644.38 --> 645.32]  known as the sibling
[645.32 --> 646.76]  of restless leg syndrome.
[646.76 --> 646.96]  Restless leg syndrome.
[647.16 --> 647.42]  Sorry.
[650.34 --> 651.36]  Restless leg syndrome
[651.36 --> 652.36]  is serious.
[652.98 --> 654.12]  I know it is.
[654.22 --> 655.30]  And I'm offending somebody.
[655.86 --> 656.84]  Known as the sibling
[656.84 --> 658.12]  of restless leg syndrome
[658.12 --> 659.90]  is when your muscles twitch
[659.90 --> 661.22]  and have sudden movements.
[661.62 --> 662.20]  Number five,
[662.30 --> 664.34]  the brief involuntary twitching
[664.34 --> 665.06]  of a muscle
[665.06 --> 666.88]  or group of muscles.
[667.08 --> 669.12]  There you have five definitions
[669.12 --> 670.26]  read perfectly.
[670.54 --> 670.94]  Each one.
[671.64 --> 672.02]  Nailed it.
[672.56 --> 673.36]  That is in the post.
[674.18 --> 674.86]  First try.
[674.96 --> 675.42]  First try.
[675.42 --> 676.94]  Yeah, I'm warming up still.
[677.02 --> 677.86]  I'm still warming up.
[678.30 --> 679.70]  And we are going to see
[679.70 --> 680.78]  if we can identify
[680.78 --> 681.64]  which one's real.
[681.86 --> 682.66]  We'll start with Jamie.
[683.00 --> 684.00]  What was the second one again?
[684.24 --> 685.98]  Second one was an eye disorder
[685.98 --> 687.52]  that results in double vision.
[687.96 --> 688.92]  Yeah, I'm going to go with that one.
[689.24 --> 689.64]  Okay.
[689.80 --> 691.98]  Jamie takes double vision.
[692.68 --> 693.66]  We go now to David.
[694.12 --> 695.42]  The fifth one,
[695.60 --> 696.16]  the muscle one.
[696.54 --> 697.74]  The muscle one.
[697.90 --> 698.10]  Okay.
[698.30 --> 699.46]  David takes the muscle one.
[699.94 --> 701.12]  We go to Spencer.
[701.64 --> 703.00]  I'm going to stick with David here.
[703.00 --> 705.10]  I'm thinking twitchy muscles,
[705.10 --> 706.30]  but not necessarily
[706.30 --> 708.18]  restricted to the legs.
[708.82 --> 709.34]  Okay.
[710.46 --> 712.90]  It goes beyond legs.
[713.82 --> 715.68]  Spencer takes number five.
[715.78 --> 716.62]  That's the muscle one.
[717.22 --> 718.68]  And now we go to Adam.
[719.24 --> 720.18]  Are you going to pile on?
[720.26 --> 721.86]  Are you going to spread it out?
[721.92 --> 722.62]  Are you going to...
[722.62 --> 723.10]  I don't know.
[723.18 --> 724.56]  I guess I'm going to do.
[725.62 --> 726.62]  I don't know.
[727.00 --> 728.10]  Well, did you mean to repeat
[728.10 --> 729.30]  any of them for you?
[729.30 --> 731.98]  Well, that was it four or five
[731.98 --> 732.54]  that made you laugh?
[732.58 --> 733.44]  Which one made you laugh?
[733.74 --> 735.66]  The sibling of restless leg syndrome.
[737.14 --> 738.36]  I'm kind of liking that one.
[738.36 --> 740.14]  Not because it's unbelievable.
[740.58 --> 741.30]  Just because I think it's...
[741.30 --> 741.50]  I'll pile on.
[741.62 --> 742.26]  I'll pile on.
[742.52 --> 742.82]  Okay.
[742.90 --> 743.40]  I'll pile on.
[743.66 --> 744.78]  So you have a pile on.
[745.02 --> 746.08]  That's early for a pile on.
[746.40 --> 747.90]  Nobody thought it was the sibling
[747.90 --> 749.32]  of restless leg syndrome.
[749.74 --> 751.58]  Probably because I didn't read it very well.
[751.64 --> 752.18]  I apologize.
[752.48 --> 753.58]  Adam, you had that one
[753.58 --> 754.42]  and then that was yours.
[754.50 --> 755.66]  You also misspelled known.
[755.94 --> 757.50]  So I was trying to overcome that.
[757.88 --> 758.20]  Oh.
[758.58 --> 760.64]  I had to add the N in my head
[760.64 --> 761.80]  as I tried to read it.
[761.84 --> 763.04]  And so you really stumbled me
[763.04 --> 763.58]  right at the front.
[763.78 --> 764.64]  And then I thought,
[764.74 --> 766.18]  why does restless leg syndrome
[766.18 --> 767.00]  have a sibling?
[767.90 --> 768.82]  It's just...
[768.82 --> 770.02]  For the arms?
[770.92 --> 771.32]  Yeah.
[771.40 --> 772.86]  They have like restless arm syndrome
[772.86 --> 773.88]  or what?
[774.76 --> 776.10]  So you just got me with that one.
[776.74 --> 777.96]  And you got nobody else
[777.96 --> 778.76]  probably because of that.
[779.48 --> 781.74]  However, Spencer also didn't trick anybody
[781.74 --> 783.56]  with his precursor to the monocle.
[783.56 --> 784.54]  Nobody picked that one.
[784.60 --> 785.40]  That was Spencer's.
[786.00 --> 787.86]  And Jamie didn't get anyone
[787.86 --> 789.92]  with a term that defines the family
[789.92 --> 791.16]  of different forms of life
[791.16 --> 792.16]  that undergo mitosis.
[793.24 --> 794.86]  So it's not looking very good for me
[794.86 --> 796.72]  because those are three fake ones.
[796.82 --> 798.50]  The other fake one that was selected
[798.50 --> 799.68]  was an eye disorder
[799.68 --> 801.78]  that results in double vision.
[801.96 --> 803.74]  Jamie guessed that.
[803.82 --> 804.74]  That was David.
[804.96 --> 807.28]  So one point to David for the eye disorder.
[807.48 --> 808.48]  I thought that was a good one.
[808.52 --> 809.70]  Double vision, mono.
[810.56 --> 812.30]  Myo for like myopic.
[812.30 --> 813.30]  Yeah, exactly.
[813.56 --> 813.98]  There you go.
[814.46 --> 815.40]  So well played.
[816.12 --> 818.18]  However, once I read the actual definition,
[818.28 --> 819.92]  it seems like you guys knew what it was.
[820.64 --> 822.86]  The brief involuntary twitching of a muzzle
[822.86 --> 824.30]  or group of muscles
[824.30 --> 827.16]  that is myoclinous.
[827.44 --> 829.08]  So David, Spencer, and Adam
[829.08 --> 830.74]  all get two points each.
[831.48 --> 832.38]  So after round one,
[832.48 --> 833.64]  David's in the lead with three.
[833.86 --> 835.18]  Spencer and Adam tied with two.
[835.32 --> 838.04]  And Jamie and I not quite yet on the board.
[838.04 --> 841.26]  But there's lots of poundifying left to play.
[841.34 --> 843.30]  We move now to round two,
[843.88 --> 845.84]  where your word for round two is
[845.84 --> 847.94]  Eigengrau.
[848.04 --> 852.40]  That's E-I-G-E-N-G-R-A-U.
[853.36 --> 853.76]  Eigengrau.
[854.14 --> 855.18]  Submit to me your definitions
[855.18 --> 856.70]  just as soon as you have them.
[856.70 --> 863.84]  Is restless leg syndrome a thing?
[864.88 --> 865.24]  Yes.
[865.82 --> 866.96]  I guess while we're in the break,
[867.04 --> 868.12]  I thought I was on the money with that one
[868.12 --> 868.92]  because that's,
[869.08 --> 869.80]  I learned about that
[869.80 --> 870.42]  because for a bit there,
[870.44 --> 871.24]  I thought I had it.
[871.56 --> 872.84]  And that's when I learned about
[872.84 --> 874.48]  myoclonus like this,
[874.62 --> 874.94]  or whatever,
[875.04 --> 876.10]  however it's pronounced.
[876.10 --> 876.38]  Yeah.
[876.92 --> 877.68]  It's twitchy stuff.
[877.76 --> 878.68]  So I thought I had all the money,
[879.28 --> 880.52]  but maybe I was off a little
[880.52 --> 882.00]  because that's how I learned about it.
[882.00 --> 882.62]  Because for a bit there,
[882.64 --> 883.24]  I had this,
[883.28 --> 884.52]  this thing where I thought I had,
[884.66 --> 884.84]  like,
[884.86 --> 886.18]  I just had twitchies for a bit.
[887.04 --> 888.72]  It was when my thigh was a little off.
[889.50 --> 891.08]  And it was kind of caused from that
[891.08 --> 892.00]  because there's like a,
[892.84 --> 894.20]  when you have like a thyroid issue,
[894.20 --> 898.06]  you can also have like versions of arthritis,
[898.06 --> 899.58]  but it's not like full on arthritis.
[899.58 --> 901.08]  It's kind of like arthritic things.
[901.60 --> 902.72]  And that's kind of a,
[902.72 --> 905.46]  a sibling to restless leg syndrome
[905.46 --> 906.36]  because they thought I had that.
[906.44 --> 907.64]  So they described several things
[907.64 --> 908.78]  and that was in my memory from that.
[909.00 --> 909.22]  Yeah.
[909.44 --> 910.64]  And that's why I described it that way.
[910.88 --> 911.08]  Yeah.
[911.12 --> 911.56]  It wasn't bad.
[911.60 --> 912.88]  I had never heard of reckless leg,
[913.04 --> 914.36]  restless leg syndrome.
[914.64 --> 915.28]  It's pretty bad.
[915.66 --> 916.06]  But yeah,
[916.16 --> 917.66]  it's just basically like your leg twitches
[917.66 --> 918.38]  uncontrollably.
[918.46 --> 919.64]  You can't stop moving it.
[919.68 --> 919.80]  Yeah.
[919.84 --> 920.72]  It's like it just moves
[920.72 --> 922.40]  without you wanting it to.
[922.48 --> 922.78]  And it's,
[922.78 --> 924.36]  it's usually during sleep
[924.36 --> 925.36]  when you're trying to sleep.
[925.84 --> 927.10]  And so obviously your sleep sucks.
[928.26 --> 930.00]  I can see how that reads funny though.
[930.18 --> 931.54]  Especially since it says no,
[931.74 --> 932.60]  not versus known.
[933.28 --> 933.64]  Yeah.
[934.04 --> 935.18]  That's what got me first.
[935.18 --> 936.70]  Then I started thinking like siblings.
[937.14 --> 937.50]  You know,
[937.64 --> 939.30]  it just got me giggling.
[939.76 --> 939.90]  Well,
[939.94 --> 940.56]  that win y'all.
[940.72 --> 941.34]  Somebody asked,
[941.42 --> 942.12]  who was it that asked?
[942.22 --> 942.74]  Was it David?
[943.38 --> 944.18]  Was there extra points
[944.18 --> 945.06]  for making Jared laugh?
[945.62 --> 946.62]  That was my question,
[946.78 --> 948.06]  but so far you're in the lead.
[948.50 --> 949.42]  You're in the lead.
[949.74 --> 950.02]  I got,
[950.02 --> 951.32]  I got in the left round one.
[951.88 --> 953.38]  So you've got a fun speaker
[953.38 --> 955.50]  lined up for the weekend in Denver
[955.50 --> 957.78]  and then other activities.
[957.98 --> 958.70]  What else is happening
[958.70 --> 960.66]  in the live show?
[960.66 --> 961.54]  Well,
[961.60 --> 962.40]  we're going to do our,
[962.40 --> 962.84]  uh,
[962.84 --> 964.20]  our Kaizen episode with Gerhard
[964.20 --> 964.52]  and,
[964.60 --> 965.84]  and we're going to be launching,
[966.20 --> 968.58]  cutting over Pipely to go live.
[968.72 --> 969.78]  So that'll be interesting.
[970.42 --> 971.14]  That's basically it.
[971.20 --> 971.80]  It's a two parter.
[971.92 --> 972.72]  So an interview
[972.72 --> 973.96]  and then a Kaizen.
[975.26 --> 975.66]  And,
[975.66 --> 975.98]  uh,
[975.98 --> 976.40]  sounds great.
[976.62 --> 977.20]  What else?
[977.32 --> 979.14]  Whatever else we make up on stage.
[979.14 --> 982.98]  We have all the definitions
[982.98 --> 983.80]  for Eigengrout.
[983.92 --> 984.46]  Number one,
[984.56 --> 985.90]  the dark gray color
[985.90 --> 986.80]  that people perceive
[986.80 --> 988.00]  in complete darkness
[988.00 --> 990.34]  rather than seeing pure black.
[991.14 --> 992.00]  Number two,
[992.06 --> 993.06]  when naming the beer
[993.06 --> 994.02]  Zeigenbach.
[997.16 --> 997.68]  Dude,
[997.74 --> 998.00]  you gotta,
[998.28 --> 999.26]  you can't laugh
[999.26 --> 999.72]  while I'm,
[999.76 --> 1001.14]  I'm going to have to mute you.
[1004.78 --> 1006.02]  When naming the beer
[1006.02 --> 1006.96]  Zeigenbach,
[1007.08 --> 1008.12]  his name was also
[1008.12 --> 1008.56]  in the running.
[1009.14 --> 1010.36]  It describes a patent
[1010.36 --> 1011.74]  pending process
[1011.74 --> 1012.84]  for mixing beer.
[1012.96 --> 1013.86]  So they considered it
[1013.86 --> 1014.92]  for the name of the beer.
[1015.60 --> 1016.70]  Number three,
[1017.22 --> 1018.58]  the deeply primal feeling
[1018.58 --> 1019.14]  of fear
[1019.14 --> 1020.30]  driven by a heightened
[1020.30 --> 1021.38]  increase of cortisol
[1021.38 --> 1022.68]  as if hearing
[1022.68 --> 1023.92]  the blood curdling cry
[1023.92 --> 1024.54]  of a beast
[1024.54 --> 1025.46]  while on the hunt.
[1027.36 --> 1028.66]  It's an amazing definition.
[1028.94 --> 1029.40]  That's intense.
[1029.54 --> 1029.66]  Yeah,
[1029.68 --> 1030.10]  these are good.
[1030.18 --> 1031.26]  The imaginary counterpart
[1031.26 --> 1032.58]  to the eigenspace
[1032.58 --> 1033.16]  of a matrix
[1033.16 --> 1034.78]  for complex valued matrices.
[1036.08 --> 1037.46]  And number five,
[1037.54 --> 1038.28]  from the German
[1038.28 --> 1040.02]  for singularly gray.
[1040.88 --> 1041.66]  There you have
[1041.66 --> 1042.64]  five definitions
[1042.64 --> 1043.64]  of eigengrau.
[1044.64 --> 1045.06]  David,
[1045.12 --> 1045.64]  we start with you.
[1046.36 --> 1046.60]  Sorry,
[1046.64 --> 1047.20]  could you remind me
[1047.20 --> 1048.42]  of the first one?
[1049.02 --> 1049.58]  Number one was
[1049.58 --> 1051.04]  a dark gray color
[1051.04 --> 1052.02]  that people perceive
[1052.02 --> 1053.08]  in complete darkness
[1053.08 --> 1054.10]  rather than seeing
[1054.10 --> 1054.68]  pure black.
[1055.38 --> 1055.84]  I mean,
[1055.92 --> 1056.26]  I think,
[1056.32 --> 1057.34]  I think as appealing
[1057.34 --> 1058.90]  as Adam's beer definition.
[1058.90 --> 1061.18]  Hey,
[1061.32 --> 1062.76]  you can't out him
[1062.76 --> 1063.22]  like that.
[1063.58 --> 1064.42]  I don't,
[1064.50 --> 1065.28]  I don't think I did.
[1065.40 --> 1065.72]  I think,
[1065.72 --> 1066.56]  I think that was all.
[1069.80 --> 1070.42]  I'm going to,
[1070.46 --> 1071.04]  I'm going to go for that
[1071.04 --> 1071.76]  with the first one.
[1071.92 --> 1072.22]  Okay.
[1072.22 --> 1072.84]  The first one.
[1073.60 --> 1074.00]  Spencer,
[1074.12 --> 1074.58]  what are you thinking?
[1074.98 --> 1075.72]  I'm thinking
[1075.72 --> 1077.36]  number five,
[1077.46 --> 1078.04]  the German
[1078.04 --> 1080.60]  word for singularly gray.
[1081.06 --> 1081.50]  Okay.
[1082.08 --> 1082.70]  So far,
[1082.72 --> 1083.42]  we've got gray
[1083.42 --> 1084.14]  and gray.
[1084.78 --> 1085.20]  Adam?
[1085.78 --> 1086.62]  I got to say
[1086.62 --> 1087.52]  those two definitions
[1087.52 --> 1088.84]  make me think
[1088.84 --> 1090.30]  something's in a shade
[1090.30 --> 1090.76]  of gray here.
[1090.82 --> 1091.30]  So I'm thinking
[1091.30 --> 1092.34]  number five as well,
[1092.42 --> 1094.06]  the German version
[1094.06 --> 1094.42]  of gray.
[1094.88 --> 1095.98]  Piling on gray,
[1096.32 --> 1097.12]  the German gray.
[1097.66 --> 1098.06]  Jamie,
[1098.18 --> 1099.00]  you're going to pile on?
[1099.16 --> 1099.64]  I'm going to go
[1099.64 --> 1100.40]  for the other gray.
[1102.08 --> 1102.48]  Okay.
[1102.60 --> 1103.46]  So we're piling on gray.
[1103.92 --> 1104.74]  We're going to pile
[1104.74 --> 1105.80]  on the other gray.
[1106.16 --> 1106.86]  So I'll go for one.
[1107.02 --> 1107.32]  Okay.
[1107.34 --> 1108.24]  So number one,
[1108.36 --> 1109.22]  we have David and Jamie
[1109.22 --> 1110.08]  on one and we have
[1110.08 --> 1111.34]  Spencer and Adam
[1111.34 --> 1113.34]  on five.
[1113.46 --> 1114.44]  Both definitions
[1114.44 --> 1115.30]  about gray.
[1115.62 --> 1116.78]  One of them is correct.
[1116.88 --> 1117.96]  One of them is incorrect.
[1118.24 --> 1119.08]  I'll tell you that much.
[1119.86 --> 1121.54]  And the definition
[1121.54 --> 1122.48]  that is incorrect
[1122.48 --> 1125.56]  is literally true though
[1125.56 --> 1126.28]  from the German
[1126.28 --> 1127.58]  for singularly gray.
[1128.00 --> 1129.16]  So that's just
[1129.16 --> 1130.40]  knowing the
[1130.40 --> 1132.08]  compound word,
[1132.16 --> 1132.58]  I suppose.
[1133.40 --> 1134.46]  And not the definition.
[1135.18 --> 1136.44]  The definition actually
[1136.44 --> 1137.64]  is the dark gray color
[1137.64 --> 1138.46]  that people perceive
[1138.46 --> 1139.20]  in complete darkness
[1139.20 --> 1139.98]  rather than seeing
[1139.98 --> 1140.76]  pure black.
[1140.98 --> 1141.48]  So that one
[1141.48 --> 1142.76]  was the actual definition.
[1142.76 --> 1145.48]  And David and Jamie
[1145.48 --> 1146.26]  both pick that.
[1146.54 --> 1147.32]  So David gets two.
[1147.84 --> 1148.60]  Jamie gets two.
[1149.20 --> 1149.52]  However,
[1149.72 --> 1150.66]  David was so close
[1150.66 --> 1151.70]  because he also knew
[1151.70 --> 1152.38]  from the German
[1152.38 --> 1153.46]  for singularly gray.
[1153.58 --> 1154.32]  That was his.
[1154.48 --> 1155.58]  So he also tricked
[1155.58 --> 1156.40]  two people.
[1157.00 --> 1158.56]  And so he scores four.
[1159.20 --> 1160.16]  That's a big round.
[1160.62 --> 1161.30]  Congrats, David.
[1161.36 --> 1161.82]  You must feel good
[1161.82 --> 1162.32]  about yourself.
[1162.74 --> 1163.58]  I do.
[1163.68 --> 1164.62]  I lived in Berlin
[1164.62 --> 1166.96]  for like half a year.
[1167.14 --> 1168.12]  And so in that time,
[1168.18 --> 1168.54]  I'm just like,
[1168.56 --> 1169.60]  yeah, that's enough.
[1169.60 --> 1170.56]  That's enough
[1170.56 --> 1171.54]  to put that word together.
[1171.68 --> 1171.92]  Eigen.
[1172.32 --> 1174.14]  Does Eigen mean singular?
[1174.82 --> 1175.82]  That actually,
[1175.88 --> 1176.50]  I just kind of went
[1176.50 --> 1177.30]  with the mathy,
[1177.46 --> 1179.28]  like Eigen vector value.
[1179.60 --> 1179.70]  Whatever.
[1180.04 --> 1180.16]  Yeah.
[1180.96 --> 1181.88]  According to Wikipedia,
[1182.06 --> 1183.20]  Eigen grouse the German
[1183.20 --> 1184.78]  from intrinsic gray.
[1185.66 --> 1186.54]  And so maybe Eigen
[1186.54 --> 1187.24]  means intrinsic.
[1188.24 --> 1189.66]  Also called Eigenlicht.
[1189.88 --> 1190.38]  Eigenlicht.
[1190.64 --> 1191.80]  I can't speak German.
[1192.44 --> 1192.98]  Dark light
[1192.98 --> 1194.24]  or brain gray.
[1194.72 --> 1195.64]  It's the uniform
[1195.64 --> 1196.70]  dark gray background color
[1196.70 --> 1197.80]  that many people report
[1197.80 --> 1198.90]  seen in the absence
[1198.90 --> 1199.56]  of light.
[1200.16 --> 1201.84]  The term Eigenlicht
[1201.84 --> 1203.64]  dates back
[1203.64 --> 1204.92]  to the 19th century
[1204.92 --> 1206.54]  and has rarely been used
[1206.54 --> 1207.90]  in recent scientific publications.
[1208.30 --> 1209.24]  So there you go.
[1210.04 --> 1210.56]  How would they all
[1210.56 --> 1211.36]  be reporting it
[1211.36 --> 1212.12]  as gray?
[1212.20 --> 1212.78]  Like there's no,
[1213.44 --> 1214.48]  I'm sorry,
[1214.56 --> 1216.26]  that's a philosophy question.
[1216.78 --> 1217.06]  Yeah,
[1217.10 --> 1218.28]  they think they're seeing black,
[1218.40 --> 1219.44]  but they're not basically
[1219.44 --> 1220.52]  because it's just like,
[1220.60 --> 1221.26]  well, it's dark.
[1221.36 --> 1221.68]  So it's,
[1221.92 --> 1222.42]  you know,
[1222.72 --> 1223.30]  it's black.
[1223.42 --> 1224.28]  It's actually not black.
[1224.42 --> 1225.48]  It's the absence of light.
[1225.54 --> 1226.30]  It's Eigen grouse.
[1226.66 --> 1226.82]  Yeah,
[1226.82 --> 1227.28]  that's interesting.
[1227.28 --> 1228.68]  We have a cave here
[1228.68 --> 1229.36]  in Texas
[1229.36 --> 1230.24]  that you can go to
[1230.24 --> 1230.90]  like as a tourist
[1230.90 --> 1232.00]  and go to the pitch part,
[1232.22 --> 1233.42]  the pitch black part of it.
[1233.70 --> 1233.98]  Oh, yeah.
[1234.10 --> 1235.22]  So they'll take you deep enough
[1235.22 --> 1235.94]  that, you know,
[1235.94 --> 1237.00]  you're not in danger.
[1237.20 --> 1237.96]  They'll turn the lights off
[1237.96 --> 1239.44]  and it literally is pitch black
[1239.44 --> 1240.78]  or what they call pitch black.
[1241.02 --> 1242.52]  And so maybe I should go back there
[1242.52 --> 1243.58]  and test this.
[1244.48 --> 1244.92]  Eigen grouse.
[1245.54 --> 1245.88]  Yes.
[1246.20 --> 1246.84]  Did you know
[1246.84 --> 1248.88]  this is actually Eigen grouse?
[1248.92 --> 1249.26]  That's right.
[1249.34 --> 1249.66]  There you go.
[1249.76 --> 1250.52]  This is not pitch black.
[1250.78 --> 1251.58]  I'll correct them.
[1252.54 --> 1253.04]  The tour guide.
[1253.04 --> 1253.96]  You should,
[1254.06 --> 1254.60]  you just yell
[1254.60 --> 1255.74]  das ist Eigen grouse.
[1256.42 --> 1257.68]  Das ist Eigen grouse.
[1259.30 --> 1260.42]  And be really angry.
[1260.96 --> 1261.42]  Yes.
[1262.04 --> 1262.46]  All right.
[1262.52 --> 1262.70]  Well,
[1262.72 --> 1263.70]  you should be really angry
[1263.70 --> 1264.62]  because you're getting
[1264.62 --> 1265.54]  whooped by David
[1265.54 --> 1266.16]  at this point,
[1266.32 --> 1267.70]  as is all of us
[1267.70 --> 1269.00]  because he has seven points
[1269.00 --> 1269.96]  after two rounds.
[1270.22 --> 1270.34]  Wow.
[1270.72 --> 1271.50]  The rest of you all
[1271.50 --> 1272.34]  are tied with two.
[1273.34 --> 1274.46]  There's plenty of
[1274.46 --> 1276.04]  pound to find left to play.
[1276.10 --> 1276.88]  I'm still in the
[1276.88 --> 1278.46]  in the Eigen grouse
[1278.46 --> 1279.20]  with zero.
[1279.20 --> 1280.96]  So let's move now
[1280.96 --> 1282.58]  to round three
[1282.58 --> 1283.78]  where your word
[1283.78 --> 1285.04]  for round three is
[1285.04 --> 1286.92]  klystron.
[1287.08 --> 1290.68]  That's K-L-Y-S-T-R-O-N.
[1291.16 --> 1292.12]  Please submit to me
[1292.12 --> 1292.88]  your definitions
[1292.88 --> 1294.42]  for the word klystron.
[1299.84 --> 1300.78]  So I was debating
[1300.78 --> 1301.20]  in my head
[1301.20 --> 1301.92]  whether I should just
[1301.92 --> 1302.86]  give David the two
[1302.86 --> 1303.64]  the three points
[1303.64 --> 1304.36]  for being correct
[1304.36 --> 1305.28]  because he was so close.
[1305.96 --> 1307.10]  I decided to let him play
[1307.10 --> 1307.72]  because he wasn't
[1307.72 --> 1308.48]  exactly right.
[1308.68 --> 1309.14]  But man,
[1309.64 --> 1310.64]  you actually scored
[1310.64 --> 1311.24]  way more points
[1311.24 --> 1312.08]  because I let you play
[1312.08 --> 1313.04]  than you would have
[1313.04 --> 1313.92]  if I had just given you
[1313.92 --> 1314.04]  the three points.
[1314.04 --> 1314.68]  It came out on top.
[1315.24 --> 1316.34]  I'm not mad about it.
[1316.48 --> 1317.20]  That definitely paid off
[1317.20 --> 1317.46]  for you,
[1317.54 --> 1318.20]  so good job.
[1326.58 --> 1327.62]  I do like the sound
[1327.62 --> 1327.98]  of that.
[1328.48 --> 1329.52]  It's clickety clackety.
[1330.00 --> 1330.64]  It sure is.
[1330.72 --> 1331.60]  It's really emphatic.
[1332.46 --> 1333.34]  I pressed enter
[1333.34 --> 1334.50]  and you all knew
[1334.50 --> 1335.42]  I pressed enter.
[1335.88 --> 1336.94]  During COVID,
[1337.08 --> 1338.10]  my partner and I
[1338.10 --> 1339.32]  so we were living
[1339.32 --> 1339.96]  at her house
[1339.96 --> 1341.60]  and we were sharing
[1341.60 --> 1342.14]  an office
[1342.14 --> 1343.50]  which was like,
[1344.26 --> 1345.04]  so it's a two-bed
[1345.04 --> 1345.90]  Victorian house
[1345.90 --> 1347.06]  and so
[1347.06 --> 1348.92]  the office bedroom
[1348.92 --> 1349.58]  that we were sharing
[1349.58 --> 1351.00]  was not very big
[1351.00 --> 1352.00]  and we both had
[1352.00 --> 1352.88]  mechanical keyboards
[1352.88 --> 1355.46]  and it was the sort
[1355.46 --> 1355.98]  of time that
[1355.98 --> 1357.02]  at lunch
[1357.02 --> 1357.56]  we'd talk a little
[1357.56 --> 1358.20]  bit about work
[1358.20 --> 1360.32]  and I wouldn't even
[1360.32 --> 1360.92]  need to tell
[1360.92 --> 1361.58]  my partner
[1361.58 --> 1362.52]  what was going on
[1362.52 --> 1362.88]  that morning
[1362.88 --> 1363.64]  because she would know
[1363.64 --> 1364.82]  if I'd been
[1364.82 --> 1366.60]  arguing with people
[1366.60 --> 1367.16]  on Slack
[1367.16 --> 1368.34]  because it was very,
[1368.48 --> 1369.04]  very clear
[1369.04 --> 1370.56]  in that small room.
[1370.56 --> 1371.46]  You're just emphatically
[1371.46 --> 1371.92]  typing.
[1372.34 --> 1372.56]  Yeah.
[1372.98 --> 1373.64]  But how does she know?
[1373.68 --> 1374.34]  You could have just been
[1374.34 --> 1375.34]  like in the flow state
[1375.34 --> 1376.82]  coding like a madman,
[1376.98 --> 1377.30]  you know,
[1377.48 --> 1378.78]  just really going after it.
[1379.20 --> 1379.98]  I think she learned
[1379.98 --> 1381.08]  pretty quickly, yeah.
[1381.22 --> 1381.62]  Different.
[1382.10 --> 1382.34]  Yeah.
[1383.94 --> 1385.14]  Many more pauses
[1385.14 --> 1385.84]  when you're coding
[1385.84 --> 1387.68]  to think of the next thing.
[1388.30 --> 1390.14]  When you're ranting
[1390.14 --> 1390.92]  you're just raving.
[1391.42 --> 1391.82]  Was she like,
[1391.84 --> 1392.72]  who are you arguing with?
[1393.78 --> 1394.62]  Are you winning?
[1396.62 --> 1397.10]  Okay.
[1397.54 --> 1398.28]  We're there.
[1398.28 --> 1399.90]  Five definitions
[1399.90 --> 1400.58]  for the word
[1400.58 --> 1401.74]  klystron.
[1402.30 --> 1402.80]  Number one,
[1402.84 --> 1404.00]  a device that converts
[1404.00 --> 1405.20]  the kinetic energy
[1405.20 --> 1406.74]  of an electron beam
[1406.74 --> 1409.18]  into radio frequency power.
[1410.22 --> 1411.00]  Number two,
[1411.06 --> 1412.00]  the process of moving
[1412.00 --> 1413.16]  swiftly through water.
[1414.02 --> 1414.52]  Number three,
[1414.62 --> 1415.86]  the nickname for a grouping
[1415.86 --> 1417.24]  of subatomic particles
[1417.24 --> 1418.72]  including the gluon
[1418.72 --> 1419.32]  and muon.
[1419.90 --> 1420.50]  Number four,
[1420.62 --> 1421.54]  a lesser used term
[1421.54 --> 1422.72]  in scientific vernacular
[1422.72 --> 1424.44]  to denote a grouping
[1424.44 --> 1426.38]  of potassium heavy entities.
[1427.04 --> 1427.88]  And number five,
[1427.88 --> 1429.18]  a subatomic particle
[1429.18 --> 1430.54]  with negative charge
[1430.54 --> 1431.86]  and spin.
[1432.48 --> 1433.50]  These are all believable
[1433.50 --> 1435.68]  to this layman over here.
[1435.98 --> 1437.62]  Let's see what y'all think
[1437.62 --> 1439.26]  starting with Spencer.
[1439.60 --> 1440.74]  I'm going to have to hear
[1440.74 --> 1442.28]  those first two again, Jared.
[1442.42 --> 1442.80]  Sure thing.
[1442.88 --> 1443.28]  Number one,
[1443.34 --> 1444.28]  a device that converts
[1444.28 --> 1445.18]  the kinetic energy
[1445.18 --> 1446.42]  of an electron beam
[1446.42 --> 1448.42]  into radio frequency power.
[1448.96 --> 1449.56]  And number two,
[1449.62 --> 1450.60]  the process of moving
[1450.60 --> 1452.42]  swiftly through water.
[1452.42 --> 1453.56]  Hmm.
[1454.40 --> 1456.38]  I think I'm going to,
[1456.84 --> 1457.68]  I'm going to go,
[1457.90 --> 1459.88]  there were two subatomic particles.
[1459.88 --> 1460.40]  So I,
[1460.48 --> 1462.24]  I'm drawn to one of those ones.
[1462.60 --> 1463.36]  And the question
[1463.36 --> 1465.50]  is which one?
[1466.16 --> 1467.28]  I think I'm going to go
[1467.28 --> 1469.14]  negative charge and spin.
[1469.82 --> 1470.76]  Number five.
[1471.02 --> 1471.78]  Number five,
[1471.98 --> 1472.88]  a subatomic particle
[1472.88 --> 1474.00]  with negative charge
[1474.00 --> 1474.88]  and spin.
[1475.80 --> 1476.72]  Locky in right there.
[1476.80 --> 1477.44]  Adam, to you.
[1477.44 --> 1478.06]  You know,
[1478.16 --> 1479.10]  five sounds pretty awesome,
[1479.92 --> 1480.10]  but,
[1480.38 --> 1482.04]  but,
[1482.12 --> 1484.20]  but,
[1484.20 --> 1485.54]  not quite awesome enough.
[1486.20 --> 1487.48]  I really feel like
[1487.48 --> 1488.68]  there's something
[1488.68 --> 1489.48]  to number two.
[1489.84 --> 1490.28]  Oh.
[1490.92 --> 1491.80]  But there's a lot of people
[1491.80 --> 1493.28]  talking about protons
[1493.28 --> 1493.82]  and mixing
[1493.82 --> 1494.68]  and stuff like that
[1494.68 --> 1495.44]  and the potassiums.
[1496.56 --> 1497.00]  Right.
[1497.38 --> 1498.08]  Can you read,
[1498.40 --> 1498.46]  charges.
[1498.68 --> 1499.94]  Can you read number four
[1499.94 --> 1500.42]  for me again
[1500.42 --> 1501.20]  just so I can have clear,
[1501.36 --> 1502.58]  that one was similar to five.
[1503.04 --> 1503.22]  Close.
[1503.24 --> 1504.34]  It's a lesser used term
[1504.34 --> 1505.86]  in scientific vernacular
[1505.86 --> 1506.70]  to denote
[1506.70 --> 1507.54]  a grouping
[1507.54 --> 1508.52]  of potassium
[1508.52 --> 1510.04]  heavy entities.
[1510.78 --> 1511.44]  Let's go with five.
[1511.88 --> 1512.28]  Five.
[1512.76 --> 1513.90]  The one that Spencer went with.
[1514.08 --> 1514.36]  That's right.
[1514.60 --> 1515.18]  You're going to pile on.
[1515.18 --> 1515.76]  He's got the points.
[1515.98 --> 1516.54]  I'm following him.
[1516.98 --> 1517.32]  All right.
[1517.66 --> 1519.32]  It's not been a winning strategy yet,
[1519.50 --> 1520.50]  but Adam and I
[1520.50 --> 1521.36]  are sticking together.
[1521.50 --> 1522.22]  It's going to pay off.
[1522.46 --> 1522.82]  You're going to have
[1522.82 --> 1523.52]  the same score.
[1524.08 --> 1524.54]  All right.
[1524.58 --> 1525.66]  Now to Jamie.
[1525.92 --> 1526.60]  I was hoping David
[1526.60 --> 1527.24]  would go first.
[1528.14 --> 1529.38]  You went first last time.
[1529.74 --> 1530.88]  What was number three?
[1531.00 --> 1531.52]  That was the other
[1531.52 --> 1532.76]  subatomic particle one.
[1532.96 --> 1533.36]  Yeah.
[1533.36 --> 1534.64]  The nickname for a grouping
[1534.64 --> 1535.86]  of subatomic particles
[1535.86 --> 1537.06]  including the glue on
[1537.06 --> 1537.56]  and move on.
[1537.84 --> 1538.48]  I'm not sure about
[1538.48 --> 1539.12]  the water one,
[1539.74 --> 1540.90]  but as it came out,
[1540.98 --> 1541.24]  I was like,
[1541.32 --> 1541.62]  hmm,
[1542.34 --> 1543.08]  I don't know.
[1543.36 --> 1544.36]  But I also don't know
[1544.36 --> 1544.78]  any of these.
[1545.70 --> 1546.70]  I think it's clear
[1546.70 --> 1547.48]  that none of us know
[1547.48 --> 1548.50]  what this definition is.
[1549.02 --> 1550.80]  So it's a guessing game
[1550.80 --> 1551.34]  at this point.
[1551.48 --> 1551.70]  Yeah.
[1552.26 --> 1552.66]  Yeah.
[1552.66 --> 1554.82]  I think I'm going to,
[1554.94 --> 1555.10]  again,
[1555.18 --> 1556.00]  try and split the vote
[1556.00 --> 1557.54]  and go for number three,
[1557.70 --> 1558.92]  the other subatomic particle.
[1559.60 --> 1559.96]  Okay.
[1560.48 --> 1561.56]  So you're liking subatomic,
[1561.68 --> 1562.14]  but you're going to go
[1562.14 --> 1564.32]  for the other subatomic.
[1564.76 --> 1565.10]  All right,
[1565.18 --> 1565.40]  David,
[1565.40 --> 1567.14]  you are last to guess
[1567.14 --> 1567.64]  this round.
[1568.48 --> 1569.02]  I almost,
[1569.24 --> 1570.88]  I feel it's like
[1570.88 --> 1572.28]  the subatomic particle
[1572.28 --> 1576.40]  thing seems so obvious
[1576.40 --> 1577.46]  that it's almost,
[1577.62 --> 1578.82]  like it feels like a trap.
[1579.34 --> 1579.62]  Mm.
[1579.92 --> 1580.22]  Mm.
[1580.72 --> 1581.70]  Cue Admiral Ackbar.
[1581.70 --> 1581.90]  Yeah.
[1583.80 --> 1584.28]  Whereas,
[1584.54 --> 1584.68]  like,
[1584.72 --> 1585.08]  I don't know
[1585.08 --> 1586.16]  if there's no
[1586.16 --> 1588.36]  klystron for water.
[1588.62 --> 1589.60]  It doesn't sound right.
[1589.74 --> 1590.80]  The potassium thing
[1590.80 --> 1592.44]  is like,
[1592.50 --> 1593.02]  no,
[1593.22 --> 1593.60]  that doesn't,
[1593.66 --> 1594.20]  that doesn't work either.
[1594.30 --> 1594.68]  I don't know.
[1595.02 --> 1596.08]  What was the first one?
[1596.20 --> 1596.92]  That was the,
[1596.94 --> 1597.86]  the device
[1597.86 --> 1598.46]  that converts
[1598.46 --> 1599.28]  the kinetic energy
[1599.28 --> 1600.36]  of an electron beam
[1600.36 --> 1602.04]  into radio frequency power.
[1602.84 --> 1604.12]  The kinetic energy
[1604.12 --> 1605.20]  of an electron beam.
[1605.74 --> 1606.08]  Correct.
[1606.66 --> 1606.84]  Yeah,
[1606.88 --> 1607.08]  I don't,
[1607.26 --> 1608.74]  you know what,
[1608.74 --> 1609.14]  I'm a,
[1609.14 --> 1609.92]  I don't,
[1610.10 --> 1611.00]  I'm going to go for the,
[1611.00 --> 1612.76]  I was like,
[1612.82 --> 1613.28]  I mean,
[1613.62 --> 1615.76]  yeah.
[1616.36 --> 1617.46]  This is that scenario
[1617.46 --> 1618.74]  when like you're sold something
[1618.74 --> 1619.72]  and you just want the salesperson
[1619.72 --> 1620.50]  to sell it to you.
[1620.58 --> 1621.10]  Can you just tell me
[1621.10 --> 1621.62]  which one to pick?
[1621.72 --> 1622.62]  Tell me which one to pick.
[1622.82 --> 1623.06]  Yeah,
[1623.18 --> 1623.64]  I'll just,
[1623.74 --> 1623.96]  you know,
[1624.04 --> 1624.60]  I'll,
[1624.60 --> 1624.78]  I'll,
[1624.78 --> 1625.26]  I'll,
[1625.26 --> 1626.26]  all I have is money.
[1626.48 --> 1627.28]  Somebody can be a problem.
[1628.10 --> 1629.40]  Just tell me what I should buy.
[1629.58 --> 1629.80]  Yeah.
[1630.26 --> 1630.66]  I'm,
[1630.72 --> 1633.00]  I'm going to go for the water one
[1633.00 --> 1633.84]  just because I got,
[1633.96 --> 1634.14]  yeah,
[1634.14 --> 1634.58]  I don't,
[1634.68 --> 1635.32]  I don't know.
[1635.64 --> 1636.88]  I don't feel strongly about it,
[1636.88 --> 1637.66]  but yeah,
[1637.66 --> 1638.16]  yeah,
[1638.26 --> 1638.82]  that's,
[1638.82 --> 1639.40]  that's what we're doing.
[1639.70 --> 1640.64]  But if you had to pick one,
[1640.72 --> 1641.70]  you're going to pick the water one.
[1642.22 --> 1645.04]  The process of moving swiftly through water.
[1645.14 --> 1647.12]  Adam did say there was something to that one.
[1647.20 --> 1648.48]  There was something special about that one.
[1648.52 --> 1648.84]  Wasn't there,
[1648.90 --> 1649.06]  Adam?
[1649.32 --> 1650.08]  Pretty special.
[1651.08 --> 1651.66]  Tell him what,
[1651.66 --> 1652.66]  tell him what he won.
[1653.22 --> 1655.90]  He won one point for Adam.
[1656.04 --> 1656.52]  There you go.
[1657.04 --> 1659.14]  Because that was something special about that one.
[1659.58 --> 1660.10]  For a second there,
[1660.12 --> 1660.28]  Adam,
[1660.28 --> 1662.50]  I thought you were going to do the people are talking about thing.
[1663.32 --> 1664.48]  It's not like people are talking about.
[1664.48 --> 1666.58]  Everybody said this,
[1666.58 --> 1667.10]  this boat,
[1667.18 --> 1668.82]  it moves through the water with the claystron.
[1668.94 --> 1669.56]  You don't even know.
[1669.74 --> 1669.96]  You're not,
[1669.96 --> 1670.24]  you're not.
[1670.24 --> 1671.20]  You're not talking about that water one.
[1671.28 --> 1671.50]  It's like,
[1671.70 --> 1671.92]  no,
[1671.98 --> 1673.04]  you're the first person to go.
[1673.14 --> 1673.50]  No one's not.
[1673.58 --> 1673.72]  Okay.
[1674.40 --> 1674.98]  So yeah,
[1674.98 --> 1676.28]  Adam gets a point there.
[1676.70 --> 1681.36]  The pile on was to the subatomic particle with negative charge and spin.
[1681.58 --> 1682.38]  Two points.
[1682.38 --> 1684.20]  Cause Spencer and Adam both selected.
[1684.34 --> 1685.62]  That one goes back to David.
[1685.68 --> 1686.68]  So he's still scoring.
[1687.72 --> 1688.84]  That's why I didn't believe it.
[1690.42 --> 1691.18]  It was cool.
[1691.26 --> 1691.82]  I liked it.
[1692.04 --> 1692.76]  It was a good one.
[1692.76 --> 1694.70]  I liked the glue on the moon on the most.
[1694.88 --> 1696.02]  Jamie liked that one as well.
[1696.10 --> 1697.60]  And that was Spencer's.
[1698.58 --> 1701.70]  So the subatomic particles was too good to be true.
[1702.22 --> 1703.72]  Neither of those was the right answer.
[1703.96 --> 1705.50]  It's Jerry on the board now.
[1705.78 --> 1717.34]  Which means I score four points because a claystron is a device that converts the connect energy of an electron beam into radio frequency power.
[1717.34 --> 1719.70]  Often called a claystron tube.
[1719.90 --> 1721.78]  If you want to look up the actual thing.
[1722.58 --> 1722.94]  And,
[1723.00 --> 1723.46]  uh,
[1723.88 --> 1724.50]  there you go.
[1725.14 --> 1726.60]  Surprised you guys didn't know that.
[1726.92 --> 1728.16]  I didn't know that either,
[1728.16 --> 1729.74]  but I knew it before you guys did.
[1729.78 --> 1730.82]  Cause I looked it up this morning.
[1731.24 --> 1732.92]  Vendor 1937.
[1733.14 --> 1733.82]  It's been around.
[1734.04 --> 1734.32]  Yeah.
[1734.34 --> 1735.00]  It's been out there.
[1735.06 --> 1736.20]  There's lots of YouTube videos.
[1736.20 --> 1739.16]  I watched them cause I wanted to figure out how to pronounce it.
[1740.10 --> 1741.58]  And I'm not sure if I pronounce it right.
[1741.58 --> 1744.58]  Cause I did see both clistron and claystron.
[1744.86 --> 1745.60]  Is it like,
[1745.68 --> 1750.40]  is it related at all to vacuum tubes or is that just like a completely separate technology?
[1751.02 --> 1751.22]  No,
[1751.30 --> 1751.58]  it's not.
[1751.66 --> 1752.10]  I don't know.
[1752.32 --> 1753.04]  It's a tube.
[1753.14 --> 1753.52]  I don't know.
[1753.52 --> 1754.74]  I'm not a physicist.
[1755.00 --> 1756.36]  I was attracted to that one too.
[1756.52 --> 1757.44]  I almost picked that one.
[1757.50 --> 1757.96]  It was close.
[1758.12 --> 1758.30]  Well,
[1758.30 --> 1759.86]  people were talking about that water one.
[1762.10 --> 1763.16]  Something special to it.
[1763.18 --> 1764.06]  There's something about it.
[1764.14 --> 1765.32]  There's something about that water one.
[1765.32 --> 1766.16]  All right.
[1766.28 --> 1767.80]  So we've all scored now.
[1767.90 --> 1768.98]  We're all feeling good.
[1769.30 --> 1770.74]  Jamie didn't score that round,
[1770.82 --> 1771.58]  but you are on the board.
[1771.76 --> 1773.38]  So after three rounds,
[1773.50 --> 1774.74]  David's still in the lead with nine.
[1775.56 --> 1777.62]  I guess I move into second place with four.
[1777.96 --> 1778.32]  Wow.
[1778.66 --> 1780.34]  That's the closest I've ever been to winning.
[1780.96 --> 1782.34]  Adam and Spencer tied of course,
[1782.42 --> 1787.46]  cause they select the same one every time with three and Jamie with two.
[1788.88 --> 1790.72]  So David's still out to a resounding lead,
[1790.80 --> 1791.76]  but I think we can catch him.
[1791.84 --> 1793.32]  We moved out to round four.
[1793.56 --> 1794.64]  This is a special round.
[1794.64 --> 1795.64]  We call it,
[1795.72 --> 1796.70]  give it a Goog,
[1797.30 --> 1798.02]  give it a Goog,
[1798.22 --> 1799.50]  give it a Goog.
[1800.46 --> 1800.86]  Well,
[1800.90 --> 1801.14]  friends,
[1801.18 --> 1802.22]  I'm here with a new friend of mine,
[1802.34 --> 1802.68]  hard job,
[1802.76 --> 1805.54]  Gil co-founder and CEO of code rabbit,
[1805.60 --> 1808.58]  where they're cutting code review time in half with their AI code review
[1808.58 --> 1809.16]  platform.
[1809.16 --> 1812.86]  So hard job in this new world of AI generated code,
[1812.94 --> 1813.28]  we are,
[1813.50 --> 1815.60]  we are at the perils of code review,
[1815.96 --> 1821.52]  getting good code into our code bases reviewed and getting it into production.
[1821.74 --> 1826.06]  Help me understand the state of code review in this new AI era.
[1826.06 --> 1830.82]  The success of AI in code generation has been just mind blowing.
[1830.82 --> 1835.94]  Like how fast some of the companies like cursor and GitHub copilot itself have grown.
[1836.14 --> 1839.46]  The developers are picking up these tools and running with it pretty much.
[1839.56 --> 1839.66]  I mean,
[1839.66 --> 1840.96]  there's a lot more code being written.
[1841.32 --> 1842.12]  And in that world,
[1842.34 --> 1846.88]  the bottleneck shifts to code review becomes like even more important than it was in the past.
[1846.88 --> 1847.56]  Even in the past,
[1847.68 --> 1849.50]  like companies cared about code quality,
[1849.60 --> 1852.96]  had all this pull request model for code reviews and a lot of checks.
[1853.30 --> 1854.46]  But post gen AI,
[1854.66 --> 1855.70]  now we are looking at,
[1855.84 --> 1856.58]  first of all,
[1856.64 --> 1857.90]  a lot more code being written.
[1858.30 --> 1858.84]  And interestingly,
[1858.94 --> 1861.16]  a lot of this code being written is not perfect,
[1861.50 --> 1861.70]  right?
[1861.76 --> 1866.02]  So the bottleneck and the importance of code review is even more so than,
[1866.10 --> 1866.88]  than it was in the past.
[1866.92 --> 1869.26]  You have to really understand this code in order to ship it.
[1869.34 --> 1870.90]  You can't just wipe code and ship.
[1870.98 --> 1872.62]  You have to first understand what the AI did.
[1872.82 --> 1874.14]  That's where code rabbit comes in.
[1874.22 --> 1875.26]  It's kind of like a,
[1875.48 --> 1876.84]  think of it as a second order effect,
[1877.06 --> 1880.50]  where the first order effect has been gen AI and code generation.
[1880.82 --> 1881.68]  Rapid success there.
[1881.78 --> 1882.98]  Now as a second order effect,
[1883.06 --> 1888.56]  there's a massive need in the market for tools like code rabbit to exist and solve that bottleneck.
[1888.60 --> 1891.36]  And a lot of the companies we know have been struggling to run with,
[1891.42 --> 1892.90]  especially the newer AI agents.
[1893.16 --> 1894.70]  If you look at the code generation AI,
[1895.10 --> 1897.64]  the first generation of the tools were just tab completion,
[1897.80 --> 1899.46]  which you can review in real time.
[1899.54 --> 1900.48]  And if you don't like it,
[1900.48 --> 1901.28]  don't accept it.
[1901.36 --> 1901.82]  If you like it,
[1901.84 --> 1902.60]  just press tab,
[1902.68 --> 1902.84]  right?
[1902.94 --> 1906.84]  But those systems have now evolved into more agentic workflows.
[1906.88 --> 1913.18]  Now you're starting with a prompt and you get changes performed on like multiple files and multiple equations in the code.
[1913.18 --> 1916.96]  And that's where the bottleneck has now become code review bottleneck.
[1917.06 --> 1919.48]  Every developer is now evolving into a code reviewer.
[1919.48 --> 1921.04]  A lot of the code being written by AI.
[1921.30 --> 1923.38]  That's where the need for code rabbit started.
[1923.62 --> 1925.02]  And that's being seen in the market.
[1925.22 --> 1927.48]  Like code rabbit has been non-linearly growing.
[1927.64 --> 1929.40]  I would say it's a relatively young company,
[1929.60 --> 1933.02]  but it's being trusted by a hundred thousand plus developers around the world.
[1933.02 --> 1933.84]  Okay,
[1933.84 --> 1934.14]  friends.
[1934.20 --> 1934.30]  Well,
[1934.30 --> 1934.48]  good.
[1934.48 --> 1937.16]  Next step is to go to code rabbit.
[1937.68 --> 1938.16]  AI.
[1938.46 --> 1943.22]  That's C O D E R A B B I T dot AI.
[1943.56 --> 1948.14]  Use the most advanced AI platform for code reviews to cut code review time in half,
[1948.28 --> 1948.92]  bugs in half,
[1948.98 --> 1950.36]  all that stuff instantly.
[1950.88 --> 1952.88]  You got a 14 day free trial to easy,
[1952.96 --> 1953.82]  no credit card required,
[1953.82 --> 1955.96]  and they are free for open source.
[1956.26 --> 1957.62]  Learn more at code rabbit.
[1957.62 --> 1967.02]  I went out to Google.com in an incognito browser.
[1967.44 --> 1968.86]  I did not use a VPN.
[1969.08 --> 1969.48]  So yes,
[1969.50 --> 1972.84]  you can probably triangulate some stuff because I was too lazy,
[1973.00 --> 1974.28]  even though I knew that might happen.
[1974.36 --> 1978.16]  And I Googled how does just those two words,
[1978.40 --> 1979.62]  how does,
[1979.76 --> 1982.70]  and then I hit space to make sure it knows that does is over.
[1982.70 --> 1987.22]  And I stopped and Google suggested some auto completes.
[1987.62 --> 1994.36]  I have a jotted down the number one auto complete and your job in this round is either to guess
[1994.36 --> 1996.02]  what Google auto completed for me,
[1996.10 --> 1997.22]  or of course,
[1997.30 --> 2001.08]  come up with what you think it might auto complete for most humans around the world.
[2001.52 --> 2004.08]  Please submit to me your auto completes now.
[2004.60 --> 2005.08]  And this is,
[2005.26 --> 2006.76]  you Googled this like today.
[2006.96 --> 2007.44]  Correct.
[2008.26 --> 2010.80]  And to confirm you're in Omaha,
[2011.26 --> 2011.60]  Nebraska.
[2012.12 --> 2012.62]  Correct.
[2013.26 --> 2013.66]  Well,
[2013.68 --> 2016.36]  you can stereotype me and then you can guess some stuff.
[2017.62 --> 2019.26]  Feel free.
[2019.42 --> 2019.74]  It's fine.
[2020.84 --> 2021.56]  I was going to say,
[2021.70 --> 2021.92]  yep.
[2022.02 --> 2025.00]  You have all of your false ideas about what we're like.
[2025.20 --> 2026.10]  How does corn grow?
[2026.40 --> 2026.58]  No,
[2026.62 --> 2026.74]  see,
[2026.78 --> 2027.50]  we already know that.
[2027.56 --> 2028.90]  We're not going to be asking Google that.
[2029.40 --> 2030.88]  You have to think of what we're ignorant of.
[2032.34 --> 2032.52]  Adam,
[2032.54 --> 2034.14]  are you thinking or what are you doing over there?
[2034.22 --> 2034.76]  I'm thinking.
[2035.18 --> 2035.54]  Okay.
[2035.64 --> 2038.26]  Cause it looks like you're just staring at the camera.
[2038.26 --> 2040.36]  Just like deeply breathing.
[2040.80 --> 2041.14]  Well,
[2041.24 --> 2041.42]  Oh,
[2041.42 --> 2041.70]  sorry.
[2046.04 --> 2047.08]  Am I breathing deeply?
[2047.20 --> 2047.84]  Maybe I'm excited.
[2048.24 --> 2048.94]  Oh man.
[2049.46 --> 2050.38]  I think I'm excited.
[2051.06 --> 2052.94]  I have an arm self-conscious about my breathing.
[2053.82 --> 2054.66]  Who wants a little TMI?
[2054.76 --> 2055.44]  You want some TMI?
[2059.06 --> 2059.54]  That's,
[2059.54 --> 2061.20]  that's not normally how that works.
[2061.20 --> 2063.08]  I don't know how to answer that.
[2063.44 --> 2065.10]  I know exactly how to answer that.
[2065.18 --> 2065.54]  No,
[2065.68 --> 2066.62]  the answer is no,
[2066.62 --> 2069.90]  but I'm going to hear it anyways.
[2069.90 --> 2070.34]  I'm sure.
[2070.94 --> 2071.30]  No,
[2071.42 --> 2072.08]  I will not tell.
[2072.32 --> 2072.60]  Okay.
[2072.60 --> 2073.12]  I'm keeping it.
[2073.44 --> 2073.74]  Okay.
[2074.38 --> 2074.62]  Wow.
[2074.68 --> 2074.96]  It worked.
[2075.16 --> 2075.58]  It worked.
[2075.74 --> 2077.24]  Can it be like a plus plus special?
[2077.40 --> 2077.62]  Yeah.
[2078.18 --> 2079.74]  Just bleep it for the regular people.
[2079.74 --> 2081.38]  I will unbleep it for plus plusers.
[2081.98 --> 2082.34]  Okay.
[2082.48 --> 2082.64]  I mean,
[2082.64 --> 2084.08]  this is a plus plus special right here.
[2084.18 --> 2084.38]  Okay.
[2084.62 --> 2085.92]  Change log plus plus.
[2086.22 --> 2086.88]  It's better.
[2091.20 --> 2092.12]  Well,
[2092.18 --> 2097.90]  we gave it a Goog and we tried to guess how people were Googling.
[2098.64 --> 2100.48]  How does stuff.
[2100.64 --> 2101.78]  That's not even a good sentence.
[2102.12 --> 2103.28]  I'm going to roll with it.
[2103.68 --> 2105.12]  And here's what we came up with.
[2105.16 --> 2108.20]  Five potential autocompletes for how does.
[2108.66 --> 2109.26]  Number one,
[2109.64 --> 2111.26]  how does a bill become a law?
[2111.62 --> 2112.28]  Number two,
[2112.58 --> 2113.88]  how does farming work?
[2114.28 --> 2114.92]  Number three,
[2115.08 --> 2116.94]  how does astronomer make money?
[2117.48 --> 2118.10]  Number four,
[2118.10 --> 2119.50]  how does Ozempic work?
[2120.14 --> 2120.74]  And number five,
[2120.74 --> 2122.90]  how does the world end?
[2123.56 --> 2124.50]  How does the world end?
[2125.20 --> 2125.64]  Five,
[2126.14 --> 2126.66]  four,
[2126.94 --> 2127.18]  three.
[2127.18 --> 2127.58]  Yeah.
[2128.16 --> 2129.82]  We just took a dark turn there.
[2130.12 --> 2131.36]  Like a dramatic countdown.
[2133.18 --> 2133.88]  All right,
[2134.04 --> 2134.42]  Adam,
[2134.62 --> 2136.40]  you are first this round,
[2136.50 --> 2136.82]  my friend.
[2137.00 --> 2137.14]  Gosh,
[2137.20 --> 2137.32]  man,
[2137.34 --> 2139.22]  there's like two in there that were really good.
[2139.48 --> 2139.92]  Oh,
[2140.00 --> 2140.68]  which ones were they?
[2141.28 --> 2144.08]  I really have to ask you to read four of them again.
[2144.24 --> 2144.96]  Or three of them.
[2145.26 --> 2146.54]  These are the shortest ones ever.
[2146.66 --> 2147.64]  How do you not remember them?
[2147.72 --> 2147.96]  Okay,
[2147.96 --> 2148.58]  I'll read them.
[2149.08 --> 2150.72]  The middle three were the ones that,
[2150.74 --> 2151.50]  stood out to me most of me.
[2151.60 --> 2151.66]  Like,
[2151.72 --> 2152.18]  so like two,
[2152.28 --> 2152.40]  three,
[2152.44 --> 2152.80]  and four.
[2153.04 --> 2153.68]  Can you read those please?
[2153.80 --> 2153.92]  Two,
[2153.96 --> 2154.10]  three,
[2154.14 --> 2154.42]  and four.
[2154.50 --> 2154.66]  Okay.
[2154.70 --> 2156.26]  Number two is how does farming work?
[2156.38 --> 2156.62]  Okay.
[2156.62 --> 2157.28]  That was not the one.
[2157.50 --> 2157.74]  Number three,
[2157.86 --> 2158.98]  number three,
[2159.06 --> 2160.60]  how does astronomer make money?
[2160.98 --> 2161.60]  That was awesome.
[2162.08 --> 2162.32]  Okay.
[2162.36 --> 2163.00]  Number four,
[2163.44 --> 2164.68]  how does Ozempic work?
[2165.12 --> 2165.36]  Okay,
[2165.36 --> 2165.66]  listen,
[2165.74 --> 2166.74]  I think it's number four,
[2166.74 --> 2168.54]  but I'm going to give it to number three because damn,
[2168.58 --> 2169.32]  that's a good answer.
[2169.50 --> 2169.68]  Okay.
[2170.32 --> 2171.58]  That is spot on.
[2172.10 --> 2172.46]  Whoever,
[2172.72 --> 2173.94]  whoever's that is,
[2173.98 --> 2174.72]  if it's not real,
[2174.82 --> 2175.38]  they're awesome.
[2176.08 --> 2176.48]  Okay.
[2176.60 --> 2177.02]  Forever friend.
[2177.14 --> 2178.16]  It goes with number.
[2178.16 --> 2182.20]  Date of recording might be relevant for that particular answer.
[2182.50 --> 2182.84]  Right.
[2183.18 --> 2183.38]  Astronomer.
[2183.50 --> 2183.72]  Yeah.
[2184.28 --> 2187.42]  Inquiring minds want to know how does astronomer make money?
[2187.50 --> 2187.70]  Okay.
[2189.08 --> 2189.82]  Next up,
[2190.32 --> 2191.64]  it's going to be Jamie.
[2192.22 --> 2192.78]  So I was going to say,
[2192.84 --> 2193.74]  we've heard the middle three.
[2194.48 --> 2194.84]  Yeah.
[2196.50 --> 2198.18]  How about number one and five?
[2198.32 --> 2198.44]  Yeah.
[2198.46 --> 2199.40]  One of them was,
[2199.52 --> 2200.80]  how does a bill become,
[2201.08 --> 2202.36]  how does a bill become a law?
[2202.76 --> 2203.50]  That was the first one.
[2203.74 --> 2204.50]  And then what was the other one?
[2204.52 --> 2205.12]  And the last one was,
[2205.18 --> 2205.92]  how does the world end?
[2206.06 --> 2206.86]  So there's your five.
[2207.30 --> 2209.30]  So you got farming in order.
[2209.42 --> 2210.02]  You got a bill,
[2210.50 --> 2211.24]  you got farming,
[2211.46 --> 2212.80]  then you got astronomer,
[2212.92 --> 2213.78]  then you have Ozempic,
[2213.88 --> 2214.58]  then you have the world.
[2215.04 --> 2216.10]  I think Ozempic.
[2216.60 --> 2217.08]  I mean,
[2217.12 --> 2221.42]  astronomer is like written perfectly how someone would search for it.
[2221.98 --> 2222.70]  But yeah,
[2222.70 --> 2223.42]  I think Ozempic.
[2223.68 --> 2224.10]  All right.
[2224.16 --> 2225.50]  Jamie picks Ozempic.
[2226.06 --> 2226.42]  David,
[2226.54 --> 2226.80]  do you?
[2227.44 --> 2230.86]  I'm going to go with Ozempic.
[2231.04 --> 2231.56]  I think that,
[2232.64 --> 2232.88]  yeah,
[2233.46 --> 2234.12]  that seems right.
[2234.36 --> 2235.26]  What are you guys trying to say?
[2236.84 --> 2237.12]  It's,
[2237.12 --> 2237.52]  it's,
[2237.52 --> 2240.56]  it's,
[2240.56 --> 2240.96]  it's,
[2240.96 --> 2241.94]  it's very popular.
[2242.08 --> 2243.82]  People want to know how it works.
[2243.82 --> 2244.04]  That's true.
[2244.20 --> 2244.70]  That's fair.
[2245.14 --> 2245.58]  Okay.
[2245.96 --> 2246.40]  Spencer.
[2246.82 --> 2247.32]  I'm torn.
[2247.98 --> 2255.14]  I feel like Adam and I have hitched our wagons together and I got to give props to astronomer.
[2255.26 --> 2255.50]  I mean,
[2256.24 --> 2258.46]  the reason I'm a plus plus subscriber,
[2258.46 --> 2262.18]  I like to support things that bring me happiness and I like it.
[2262.18 --> 2264.44]  And that answer brought me a bit of happiness.
[2264.60 --> 2266.32]  So I'm going to go for astronomer.
[2266.96 --> 2268.32]  Well played.
[2268.52 --> 2268.92]  Okay.
[2269.14 --> 2273.98]  So Spencer and Adam hitched again and ride or die,
[2274.04 --> 2274.28]  brother.
[2275.16 --> 2276.02]  Right to the bottom.
[2276.16 --> 2276.74]  Right to the bottom.
[2276.74 --> 2278.66]  Some people want to know how astronomer makes money.
[2278.76 --> 2280.20]  I want to know how David makes money.
[2280.20 --> 2281.94]  Cause he is scoring left and right.
[2282.04 --> 2283.18]  That was his good job,
[2283.26 --> 2283.64]  David.
[2284.06 --> 2285.84]  And that's a funny backstory on that one.
[2285.84 --> 2288.28]  Cause without the capitalized a,
[2288.44 --> 2290.84]  I thought he was trying to say how do astronomers make money?
[2291.22 --> 2291.54]  Also,
[2291.54 --> 2292.14]  I'm curious.
[2292.14 --> 2292.84]  How do they?
[2292.90 --> 2293.18]  And I'm like,
[2293.24 --> 2294.38]  do you want me to pluralize for that?
[2294.42 --> 2294.72]  And he's like,
[2294.76 --> 2294.94]  no,
[2294.98 --> 2295.20]  man.
[2295.24 --> 2295.58]  I was like,
[2295.60 --> 2295.90]  Oh,
[2295.90 --> 2297.22]  I get it.
[2297.22 --> 2297.66]  I didn't get it.
[2297.66 --> 2297.94]  No,
[2298.04 --> 2298.36]  man.
[2302.70 --> 2302.94]  Yeah.
[2302.94 --> 2303.80]  I was like astronomers.
[2304.14 --> 2304.40]  Yeah.
[2304.40 --> 2305.14]  How do they make money?
[2305.26 --> 2305.76]  I don't know.
[2305.76 --> 2307.42]  So two points for him.
[2307.42 --> 2309.90]  And then how does farming work?
[2310.00 --> 2310.14]  Well,
[2310.18 --> 2311.64]  Jamie already made a joke about that.
[2311.64 --> 2312.84]  So that was his,
[2313.26 --> 2314.72]  how's a bill become a law?
[2315.16 --> 2315.88]  Nobody cares,
[2316.02 --> 2316.36]  Spencer.
[2316.54 --> 2316.78]  I mean,
[2316.82 --> 2317.12]  come on.
[2317.12 --> 2317.86]  Nobody wants to know.
[2318.36 --> 2318.70]  I mean,
[2319.12 --> 2322.36]  you had to have seen the video when you were in grade school.
[2322.60 --> 2324.12]  How does a bill become a law?
[2324.44 --> 2324.88]  For sure.
[2325.38 --> 2326.96]  Not my favorite schoolhouse rock though.
[2327.20 --> 2327.34]  Honestly.
[2327.44 --> 2328.02]  That is a good one.
[2328.26 --> 2328.66]  Conjunction.
[2329.04 --> 2329.34]  Conjunction.
[2329.72 --> 2330.24]  There it is.
[2331.38 --> 2332.30]  What's your function?
[2332.50 --> 2332.70]  You know,
[2333.14 --> 2335.12]  hooking up words and phrases and clauses.
[2335.12 --> 2336.12]  Yes.
[2336.12 --> 2336.48]  Yes.
[2336.88 --> 2337.34]  All right.
[2337.84 --> 2338.12]  Meanwhile,
[2338.40 --> 2338.74]  Adam,
[2338.90 --> 2339.80]  the world ending one.
[2339.88 --> 2341.58]  Didn't you do that similar last time around?
[2341.66 --> 2342.80]  It was something about the end of the world.
[2343.24 --> 2344.16]  I don't know what else to say.
[2344.28 --> 2344.54]  Okay.
[2346.84 --> 2348.42]  He's got one thing on his mind.
[2348.70 --> 2351.76]  Does Adam have a doomsday device somewhere?
[2352.42 --> 2353.28]  Should we be worried?
[2353.28 --> 2354.66]  You know,
[2354.76 --> 2356.26]  I just don't have a good brain like you,
[2356.32 --> 2356.48]  David,
[2356.52 --> 2358.24]  because that was an awesome answer.
[2359.12 --> 2360.70]  And I guess I'm just bland.
[2360.94 --> 2363.50]  I could be more sparkling.
[2363.64 --> 2364.36]  I'm just a little bland,
[2364.50 --> 2364.88]  unfortunately.
[2365.40 --> 2365.80]  Well,
[2365.86 --> 2367.64]  the correct autocomplete,
[2367.84 --> 2372.12]  or at least for my incarnino tab on this side of the earth,
[2372.12 --> 2374.96]  is how does Ozempic work?
[2376.24 --> 2378.16]  And Jamie and David both picked that.
[2378.16 --> 2379.38]  So two points each.
[2379.60 --> 2381.60]  That's two for Jamie on the round.
[2381.90 --> 2383.36]  Four for David on the round.
[2384.12 --> 2387.14]  Other autocompletes that didn't quite make it as high,
[2387.20 --> 2388.06]  but we're still on the list.
[2388.32 --> 2388.98]  Number two was,
[2389.10 --> 2390.86]  how does a HELOC work?
[2391.26 --> 2391.78]  A HELOC.
[2392.30 --> 2392.58]  What?
[2392.68 --> 2393.30]  That is confusing.
[2393.50 --> 2394.86]  Home equity line of credit.
[2395.86 --> 2397.16]  Very complicated,
[2397.98 --> 2398.98]  but sometimes useful.
[2399.62 --> 2400.38]  Investing vehicle.
[2400.74 --> 2402.10]  How does plan B work?
[2402.82 --> 2405.16]  How does Zelle work?
[2405.24 --> 2405.44]  You know,
[2405.50 --> 2407.34]  that thing where you can send money between banks.
[2408.06 --> 2408.58]  I don't know.
[2408.80 --> 2409.58]  I don't know how it works.
[2409.76 --> 2411.20]  And how does hail form?
[2412.06 --> 2413.54]  That's straight out of Nebraska right there.
[2413.54 --> 2414.06]  Cause you know,
[2414.08 --> 2414.66]  we get hailed on.
[2414.84 --> 2415.14]  And Texas,
[2415.26 --> 2415.46]  bro.
[2415.62 --> 2416.28]  So much.
[2416.64 --> 2417.22]  Oh my gosh.
[2417.32 --> 2417.50]  Yeah.
[2417.62 --> 2422.70]  I got a particularly Orlando response in my how does.
[2422.70 --> 2423.58]  So number one,
[2423.76 --> 2424.58]  also Ozempic.
[2424.96 --> 2425.24]  Okay.
[2425.38 --> 2425.70]  Number two,
[2426.74 --> 2428.48]  how does lightning lane work?
[2428.78 --> 2430.86]  The Disney world fast pass system.
[2431.32 --> 2432.00]  No one knows.
[2432.10 --> 2432.84]  Oh no.
[2434.02 --> 2435.00]  It's like magic.
[2435.40 --> 2435.92]  No one knows.
[2436.30 --> 2437.06]  It's dark magic.
[2437.24 --> 2438.64]  It's like magic you pay for.
[2438.76 --> 2439.26]  And then you don't know.
[2439.48 --> 2439.62]  Yeah.
[2440.08 --> 2441.04]  That was magic for them.
[2441.70 --> 2442.18]  Hilarious.
[2442.26 --> 2442.68]  All right.
[2442.74 --> 2443.14]  Well,
[2443.30 --> 2445.46]  after just four rounds,
[2445.46 --> 2447.56]  we have like a world record pace here.
[2447.68 --> 2448.96]  David with 13 points.
[2449.00 --> 2451.38]  He's in striking distance of a win after four rounds.
[2452.44 --> 2458.66]  You wonder why I created 10 rounds and tied for second is me and Jamie with four.
[2459.00 --> 2460.56]  That's how far back we are.
[2460.56 --> 2463.52]  And tied in last is these two hitched together with three,
[2463.68 --> 2465.14]  Spencer and Adam.
[2465.56 --> 2468.80]  Can we go for a rule change and just like pull our points together?
[2469.88 --> 2471.08]  Just team up on him.
[2471.74 --> 2472.02]  Wow.
[2472.70 --> 2473.62]  I make the rules.
[2473.62 --> 2476.18]  So I could make up whatever I wanted to technically.
[2476.40 --> 2476.52]  I mean,
[2476.54 --> 2477.30]  it's our podcast,
[2477.52 --> 2480.58]  but he might not come back and maybe that's what we want.
[2480.66 --> 2481.16]  I don't know.
[2481.36 --> 2481.80]  Let's see how it is.
[2481.94 --> 2483.24]  Move now to round five.
[2483.38 --> 2484.88]  This is a new style round,
[2484.98 --> 2486.90]  even newer than the Google style round.
[2486.90 --> 2488.42]  This is called weird flicks,
[2488.42 --> 2489.22]  but okay.
[2490.50 --> 2493.06]  I've scoured the internet for one of the oldest,
[2493.28 --> 2494.74]  most obscure,
[2495.26 --> 2496.64]  weird movies.
[2497.18 --> 2498.58]  And I've grabbed the title,
[2499.26 --> 2500.82]  the year it was released,
[2501.14 --> 2503.16]  and the synopsis,
[2503.60 --> 2507.06]  a brief one sentence synopsis of what the movie is about.
[2507.64 --> 2511.92]  Your job is to write your own brief one sentence synopsis and try to trick
[2511.92 --> 2514.42]  your friends into thinking yours is real.
[2515.06 --> 2515.58]  And of course,
[2515.70 --> 2518.34]  I guess if you know the actual movie and you tell me what it's about,
[2518.50 --> 2519.70]  you'll still get your three points.
[2521.10 --> 2522.52]  I think if I were you guys,
[2522.52 --> 2524.14]  I'd start teaming up against David.
[2524.50 --> 2525.22]  Just saying,
[2525.62 --> 2526.26]  just saying.
[2526.76 --> 2526.84]  So,
[2527.04 --> 2527.78]  so just like,
[2527.94 --> 2531.06]  like the oldest possible movie is what we're going for.
[2531.52 --> 2532.42]  They're pretty old.
[2532.48 --> 2533.22]  So this first one,
[2533.30 --> 2534.22]  I have two of these rounds.
[2534.30 --> 2534.76]  The first one,
[2534.84 --> 2536.00]  this is in 1945.
[2536.00 --> 2537.38]  So it's an old movie.
[2537.66 --> 2540.88]  And the title of the movie is the reckless moment,
[2541.38 --> 2542.32]  the reckless moment.
[2542.76 --> 2544.90]  And your job is to come up with,
[2545.04 --> 2547.40]  or to know by having seen it,
[2547.58 --> 2549.70]  the synopsis of what that movie is about.
[2550.54 --> 2551.70]  So there you go.
[2552.34 --> 2555.38]  The reckless moment from 1945.
[2560.10 --> 2561.08]  And to confirm,
[2561.22 --> 2563.96]  is this the official one line synopsis?
[2563.96 --> 2567.56]  This would be the one liner that is on the IMDb page.
[2567.94 --> 2569.86]  So it's not like a tagline.
[2570.32 --> 2571.64]  It's a synopsis,
[2572.08 --> 2573.42]  but IMDb people wrote it,
[2573.48 --> 2574.86]  not the movie creators.
[2575.00 --> 2575.44]  I don't think.
[2575.80 --> 2577.08]  What does Adam have in his,
[2577.60 --> 2578.94]  what's he watching behind us?
[2579.18 --> 2579.70]  Silicon Valley.
[2580.10 --> 2580.90]  Silicon Valley.
[2581.40 --> 2582.22]  Is it always on?
[2582.62 --> 2582.84]  Always?
[2583.18 --> 2583.38]  Well,
[2583.40 --> 2584.16]  whenever we're recording,
[2584.26 --> 2585.60]  I think you might turn it off in between,
[2585.76 --> 2587.02]  but it's just loose.
[2587.14 --> 2587.78]  Different scenes.
[2587.98 --> 2588.16]  Yeah.
[2588.64 --> 2589.24]  He's just troll.
[2589.24 --> 2591.58]  I was trying to work it out from earlier.
[2591.70 --> 2592.64]  I thought it was community,
[2593.02 --> 2593.78]  but now I can see.
[2593.90 --> 2594.06]  Yeah.
[2594.44 --> 2596.74]  I thought it would be cool if he would like,
[2596.84 --> 2597.94]  do some different things,
[2598.02 --> 2598.60]  different episodes.
[2598.60 --> 2599.78]  Like it could be Star Wars.
[2599.88 --> 2601.08]  It could be Silicon Valley.
[2601.22 --> 2602.24]  It could be Predator,
[2602.62 --> 2602.98]  you know?
[2603.24 --> 2603.92]  And he's just like,
[2604.00 --> 2604.20]  no,
[2605.34 --> 2606.72]  only Silicon Valley all the time.
[2606.96 --> 2607.64]  Can we change the,
[2607.64 --> 2608.74]  the show for you?
[2608.84 --> 2609.00]  Yeah.
[2609.00 --> 2609.88]  I want to watch something different.
[2610.42 --> 2610.58]  No,
[2610.60 --> 2610.92]  we were just,
[2611.10 --> 2612.30]  we were very excited when you left.
[2612.30 --> 2614.28]  Cause we could actually catch up on a episode.
[2614.28 --> 2614.78]  So we missed.
[2615.12 --> 2615.42]  Yeah.
[2615.96 --> 2617.12]  This is a,
[2617.30 --> 2620.76]  that doesn't generate like a copyright problem from HBO.
[2621.08 --> 2621.66]  They're not like,
[2621.70 --> 2622.06]  no,
[2622.14 --> 2623.00]  it's obscure enough.
[2623.46 --> 2623.90]  Yeah.
[2623.96 --> 2624.74]  In the background enough.
[2624.76 --> 2626.18]  We don't ever get a takedown request.
[2626.32 --> 2626.76]  Thankfully.
[2627.78 --> 2632.40]  Do I remember we talked about there maybe being like a change log watch along
[2632.40 --> 2633.70]  Silicon Valley.
[2634.00 --> 2635.10]  Do you like episode a week?
[2635.24 --> 2635.48]  Yeah,
[2635.48 --> 2635.98]  that'd be cool.
[2636.08 --> 2637.76]  I'd never execute on that.
[2638.16 --> 2639.26]  Cause I didn't want to rewatch it,
[2639.34 --> 2639.76]  I guess.
[2639.90 --> 2640.48]  Or be,
[2640.48 --> 2641.24]  be forced to.
[2641.42 --> 2642.76]  We also almost did a,
[2642.84 --> 2643.12]  uh,
[2643.20 --> 2644.26]  so the last time we played this,
[2644.28 --> 2644.58]  game.
[2645.26 --> 2646.00]  What was the,
[2646.14 --> 2647.12]  he who gets slapped.
[2647.24 --> 2648.06]  Was that the name of the movie?
[2648.16 --> 2648.40]  I don't know.
[2648.40 --> 2648.72]  Yes.
[2648.92 --> 2649.28]  Yes.
[2649.44 --> 2653.40]  We actually were going to watch that in Denver as like a group activity.
[2653.46 --> 2654.52]  Cause it'd be hilarious,
[2654.52 --> 2656.60]  but the joke is funnier than the reality.
[2656.60 --> 2657.46]  So we're not going to do it,
[2657.52 --> 2658.76]  but cause it's public domain.
[2658.84 --> 2660.28]  John Henry found out it's in the public domain.
[2660.28 --> 2661.76]  Cause it's like 1928.
[2662.22 --> 2662.84]  And so like,
[2662.90 --> 2663.02]  man,
[2663.04 --> 2665.60]  we can like put it on a projector and watch it outside or something,
[2665.70 --> 2666.68]  but too lazy.
[2667.64 --> 2669.08]  I see David's guitars in the back.
[2669.16 --> 2671.84]  He may even need to start thinking of a victory jingle.
[2672.00 --> 2673.06]  You can play for us.
[2673.06 --> 2674.06]  Hmm.
[2674.72 --> 2675.68]  We're closing in.
[2676.04 --> 2678.08]  Can you improv music?
[2678.42 --> 2678.64]  Not,
[2678.78 --> 2679.34]  not well,
[2679.46 --> 2679.66]  no,
[2679.94 --> 2680.94]  not well,
[2681.28 --> 2683.78]  but you're definitely closing in on a win here.
[2684.28 --> 2684.64]  Has,
[2684.76 --> 2685.26]  has any,
[2685.32 --> 2686.14]  it feels,
[2686.30 --> 2687.60]  it feels the hubris of asking,
[2687.72 --> 2689.04]  has anyone ever won in five?
[2692.48 --> 2693.08]  You know,
[2693.08 --> 2694.16]  there's a reason it feels hubris.
[2694.16 --> 2697.34]  Not that I can imagine.
[2697.82 --> 2698.18]  Remember,
[2698.46 --> 2699.48]  I can imagine it.
[2699.52 --> 2700.14]  I can't remember it.
[2700.70 --> 2702.12]  This is our sixth time playing,
[2702.24 --> 2702.50]  isn't it?
[2702.52 --> 2703.78]  I think this is around six.
[2703.92 --> 2706.84]  And I think there may have been a win five,
[2706.96 --> 2707.32]  but back,
[2707.42 --> 2709.36]  that was back when we played less points.
[2709.40 --> 2710.66]  I think we're going to 12 for a while.
[2710.78 --> 2711.90]  And we extended it to 15.
[2712.02 --> 2713.56]  So you would have already won four.
[2713.82 --> 2714.18]  Well,
[2714.90 --> 2717.76]  and I think you're definitely on pace for the fastest W of all time,
[2717.82 --> 2718.82]  or the greatest,
[2718.98 --> 2720.00]  or the greatest show.
[2720.00 --> 2723.88]  The greatest collapse in the history of pound to fine.
[2725.88 --> 2726.58]  All right.
[2726.64 --> 2732.44]  We now have everybody's entry for a plot synopsis of 1945.
[2733.44 --> 2735.34]  The reckless moment.
[2735.48 --> 2738.78]  Are you guys ready to hear what everybody had to say?
[2739.52 --> 2740.02]  All right.
[2740.14 --> 2740.78]  Number one,
[2741.78 --> 2746.50]  well-to-do Howard Douglas makes a careless decision to leave his bowler hat at
[2746.50 --> 2746.90]  home.
[2747.38 --> 2747.92]  Number two,
[2747.92 --> 2752.68]  the untold untrue story of what Emperor Hirohito really told President Truman
[2752.68 --> 2755.48]  upon the Japanese surrender in World War II.
[2756.18 --> 2756.78]  Number three,
[2756.88 --> 2761.80]  the harrowing story of how the invasion at Normandy almost had to be called off.
[2762.92 --> 2763.86]  Number four,
[2764.34 --> 2767.98]  after discovering the dead body of her teenage daughter's lover,
[2768.64 --> 2772.44]  a housewife takes desperate measures to protect her family from scandal.
[2773.06 --> 2773.76]  Number five,
[2773.76 --> 2775.10]  with the keys to his new Plymouth,
[2775.30 --> 2777.86]  Ben takes a drive to the lookout with his friends.
[2777.92 --> 2778.76]  Where he met Betty.
[2780.80 --> 2781.46]  Hold on.
[2781.54 --> 2782.02]  I read it wrong.
[2782.56 --> 2783.32]  Where he met Betty,
[2783.64 --> 2785.48]  this knockout that sits next to you.
[2787.48 --> 2791.06]  How is this funny,
[2791.18 --> 2791.28]  Jerry?
[2794.40 --> 2796.66]  Try reading it in a transatlantic accent.
[2796.80 --> 2798.92]  That might flow a little bit more naturally.
[2798.92 --> 2800.54]  Yeah,
[2800.60 --> 2801.00]  exactly.
[2801.00 --> 2801.68]  If I could.
[2802.22 --> 2805.58]  Ben takes a drive to the lookout with his friends where he met Betty,
[2805.72 --> 2808.08]  this knockout that sits next to him in chem class.
[2808.48 --> 2809.60]  They hit it off well,
[2809.88 --> 2812.00]  but when this mysterious woman shows up,
[2812.40 --> 2813.26]  everything changes.
[2813.96 --> 2815.24]  Was that all one sentence?
[2815.92 --> 2816.32]  Ah,
[2817.08 --> 2817.48]  there's,
[2817.52 --> 2818.48]  there's one break in there.
[2818.56 --> 2819.30]  After chem class,
[2819.40 --> 2819.74]  there was a,
[2819.86 --> 2820.42]  there's a period.
[2820.42 --> 2820.70]  Okay.
[2821.26 --> 2821.70]  Okay.
[2822.74 --> 2826.04]  Five potential synopses for the reckless moment,
[2826.30 --> 2828.82]  starting with Jamie.
[2829.14 --> 2830.46]  Which one do you think is real?
[2831.04 --> 2831.82]  So I'm wondering,
[2832.30 --> 2838.38]  Emperor Hirohito and Normandy sound like they may be of the time period,
[2838.38 --> 2846.22]  but also could be quite near to like already get a film out about like Normandy or so.
[2846.98 --> 2847.48]  I'm not sure.
[2848.18 --> 2854.78]  The very long one sentence makes me wonder if it's either like not real or,
[2854.78 --> 2855.52]  um,
[2855.56 --> 2855.90]  not real.
[2856.44 --> 2857.76]  The other two,
[2857.90 --> 2858.82]  I'm not sure.
[2858.92 --> 2859.24]  Sound.
[2859.88 --> 2860.20]  Yeah.
[2860.52 --> 2862.90]  I think a little bit too far fetched.
[2863.00 --> 2863.94]  Which ones are far fetched?
[2864.08 --> 2867.94]  The one about the bowler hat and the housewife scandal.
[2868.38 --> 2871.20]  The bowler hat one just sounds a little bit out there.
[2871.58 --> 2871.90]  Um,
[2871.96 --> 2876.80]  my housewife scandal sounds like it could be like more contemporary.
[2877.46 --> 2877.98]  Right.
[2878.62 --> 2880.34]  I can't imagine that sort of thing happening.
[2880.78 --> 2881.54]  In the forties.
[2881.84 --> 2882.02]  Yeah.
[2882.02 --> 2883.80]  So you've eliminated all five.
[2884.02 --> 2884.24]  Yeah.
[2884.24 --> 2885.06]  I think that's all five.
[2886.44 --> 2887.52]  One of which he wrote.
[2890.28 --> 2891.20]  Which one?
[2891.82 --> 2892.14]  Yeah.
[2892.22 --> 2892.32]  I don't know.
[2892.32 --> 2892.94]  That's his strategy.
[2893.24 --> 2894.00]  I'm not going to say.
[2894.18 --> 2895.78]  He's just trying to make sure he doesn't pick David's.
[2895.86 --> 2897.16]  That's casting doubt widely.
[2897.56 --> 2897.78]  Yeah.
[2897.78 --> 2897.90]  Yeah.
[2898.58 --> 2900.14]  So having said all that,
[2900.20 --> 2900.82]  what are you going to do?
[2902.14 --> 2905.16]  I think I'm going to go for Normandy.
[2905.86 --> 2906.66]  I think Normandy.
[2906.94 --> 2907.22]  Yeah.
[2907.52 --> 2908.00]  All right.
[2908.32 --> 2909.22]  That's number three,
[2909.30 --> 2909.78]  by the way,
[2910.62 --> 2911.92]  Jamie goes for Normandy.
[2912.16 --> 2912.64]  David,
[2913.16 --> 2915.22]  you said the movie came out in 45.
[2915.80 --> 2916.28]  Mm hmm.
[2916.98 --> 2917.66]  I think.
[2918.50 --> 2918.94]  Sorry.
[2919.02 --> 2919.58]  What was.
[2919.58 --> 2921.42]  So it's bowler hats.
[2921.42 --> 2921.86]  Yes.
[2921.86 --> 2922.42]  Yes.
[2922.72 --> 2924.56]  Number two was president Truman.
[2924.98 --> 2925.24]  President,
[2925.30 --> 2925.44]  sorry.
[2925.52 --> 2926.58]  President Truman did what?
[2926.94 --> 2927.60]  The untold,
[2927.68 --> 2934.40]  untrue story of what Emperor Hirohito really told president to Truman upon the Japanese surrender in World War II.
[2934.64 --> 2935.94]  It's untrue and untold.
[2936.40 --> 2937.72]  It's untold and untrue.
[2938.28 --> 2939.12]  Now it's told though.
[2939.12 --> 2939.84]  Five.
[2940.32 --> 2940.64]  Yes.
[2940.64 --> 2940.92]  All right.
[2941.76 --> 2945.48]  And then number three is the Normandy,
[2945.66 --> 2946.58]  which Jamie just picked.
[2946.74 --> 2949.26]  And this is my way of backing into asking you to repeat all of them.
[2949.40 --> 2949.50]  Yeah.
[2949.58 --> 2950.44]  And number four,
[2950.64 --> 2952.90]  do you want the full sentences or just the summaries?
[2953.04 --> 2954.00]  My summary of the summary?
[2954.34 --> 2955.42]  The full sentence.
[2955.54 --> 2955.80]  Okay.
[2956.18 --> 2956.54]  Okay.
[2957.12 --> 2957.42]  Yeah.
[2957.46 --> 2957.94]  We're doing it.
[2958.00 --> 2958.16]  Sorry.
[2958.52 --> 2959.08]  All of them.
[2959.88 --> 2960.04]  No,
[2960.10 --> 2960.48]  just the last.
[2960.54 --> 2960.64]  Sorry.
[2960.72 --> 2961.46]  The last two.
[2961.62 --> 2962.06]  The last two.
[2962.20 --> 2962.28]  Yeah.
[2962.34 --> 2962.54]  Okay.
[2962.62 --> 2966.76]  Number four was after discovering the dead body of her teenage daughter's lover,
[2967.28 --> 2970.82]  a housewife takes desperate measures to protect her family from scandal.
[2971.58 --> 2974.28]  And number five is with the keys to his new Plymouth.
[2974.56 --> 2977.68]  Ben takes a drive to the lookout with his friends where he met Betty,
[2977.90 --> 2980.12]  this knockout that sits next to him in chem class.
[2980.30 --> 2981.16]  They hit it off well,
[2981.24 --> 2982.82]  but when this mysterious woman shows up,
[2982.88 --> 2983.80]  everything changes.
[2984.34 --> 2984.74]  Okay.
[2984.78 --> 2986.18]  I think I'm going bowler hat.
[2986.54 --> 2987.64]  He's going bowler hat.
[2988.74 --> 2989.10]  Okay.
[2989.70 --> 2990.06]  Spencer.
[2990.50 --> 2990.80]  Adam,
[2990.88 --> 2991.72]  it's up to you,
[2991.82 --> 2992.82]  but I'm switching.
[2992.96 --> 2993.70]  I'm going with David.
[2994.38 --> 2995.06]  Bowler hat.
[2995.72 --> 2996.66]  Bowler hat it is.
[2996.76 --> 2998.00]  It's going with the bowler hat.
[2998.96 --> 2999.36]  No,
[2999.38 --> 2999.94]  I'm going with David.
[3000.08 --> 3000.58]  Let me clarify.
[3000.84 --> 3001.50]  I'm going with David.
[3002.88 --> 3003.96]  Are you apologizing?
[3004.16 --> 3004.84]  What's happening here?
[3004.90 --> 3005.62]  Are we breaking up?
[3005.64 --> 3005.82]  Yeah.
[3005.88 --> 3008.60]  He switched off Adam and on to David is what he's saying here.
[3008.70 --> 3008.80]  Well,
[3008.80 --> 3008.90]  no,
[3008.92 --> 3009.62]  it's Adam's choice.
[3009.72 --> 3012.62]  He can choose to follow me on David's bandwagon or not,
[3012.82 --> 3013.82]  but that's up to Adam.
[3014.20 --> 3014.82]  I got you.
[3014.90 --> 3015.44]  So it's up to you.
[3015.44 --> 3016.36]  If you want to pile on,
[3016.54 --> 3016.90]  well,
[3016.98 --> 3018.20]  David wouldn't choose his own.
[3018.42 --> 3018.60]  So,
[3018.78 --> 3020.14]  but he only needs two,
[3020.24 --> 3021.28]  two points to win.
[3021.50 --> 3022.08]  That's right.
[3022.20 --> 3023.04]  And if he gets the right one,
[3023.08 --> 3023.56]  he gets one,
[3023.62 --> 3023.90]  right?
[3024.34 --> 3025.20]  If he gets it correct,
[3025.26 --> 3025.94]  he gets two.
[3026.42 --> 3026.94]  If he gets,
[3027.10 --> 3028.28]  if he tricks you,
[3028.32 --> 3029.12]  he gets one more.
[3029.36 --> 3030.50]  David could be choosing his own.
[3030.58 --> 3030.90]  You know that,
[3030.96 --> 3031.20]  right?
[3031.58 --> 3032.06]  He could be,
[3032.06 --> 3034.42]  he could be presupposing a pile on.
[3034.42 --> 3037.64]  Both of us are suckers to follow him for those two points,
[3037.64 --> 3038.86]  but maybe we are.
[3038.94 --> 3039.34]  We're in the,
[3039.42 --> 3040.04]  we're in the back.
[3040.12 --> 3040.54]  I don't know.
[3040.58 --> 3041.98]  And he's also going first though.
[3041.98 --> 3042.44]  So he's,
[3042.44 --> 3045.42]  he's kind of creating the current to follow.
[3045.90 --> 3046.10]  I mean,
[3046.10 --> 3047.52]  he's creating the pile on and you've,
[3047.52 --> 3049.08]  you've fought for his trick.
[3049.38 --> 3050.34]  Jamie did go first.
[3050.46 --> 3050.68]  Technically.
[3051.04 --> 3051.06]  Oh,
[3051.06 --> 3051.26]  sorry.
[3051.38 --> 3052.12]  Jamie went first,
[3052.34 --> 3053.56]  but David would want you to know that.
[3053.56 --> 3054.62]  David first ish.
[3054.64 --> 3055.96]  I just counted all of them.
[3056.90 --> 3060.10]  If I fall into this trap that David laid,
[3060.20 --> 3060.38]  he's,
[3060.52 --> 3063.68]  he's playing checkers and we're playing chess here so he can win.
[3064.38 --> 3065.04]  Oh man.
[3065.18 --> 3065.74]  Other way around.
[3066.12 --> 3066.28]  Yeah.
[3066.32 --> 3067.16]  I think he'd be playing chess.
[3067.40 --> 3068.74]  That's why we're going to lose right there.
[3072.08 --> 3073.62]  That's how confused he has Spencer.
[3074.58 --> 3075.10]  I don't know,
[3075.16 --> 3075.26]  Jared.
[3075.28 --> 3077.16]  I feel like that last one needs one more read.
[3077.22 --> 3077.66]  What do you think?
[3078.14 --> 3078.40]  Okay.
[3079.94 --> 3082.74]  You're just trying to make sure we use the full two hours.
[3083.52 --> 3084.14]  That's right.
[3084.44 --> 3086.06]  With the keys to his new Plymouth,
[3086.26 --> 3089.24]  Ben takes a drive to look out with his friends where he met Betty,
[3089.54 --> 3092.70]  this absolute knockout that sits next to him in chem class.
[3093.62 --> 3094.86]  Was it absolute there before?
[3095.32 --> 3095.72]  No,
[3095.78 --> 3096.20]  I had that.
[3096.78 --> 3098.34]  I just figured it needed to be there.
[3099.44 --> 3100.36]  They hit it off well,
[3100.44 --> 3102.18]  but when this mysterious woman shows up,
[3102.24 --> 3103.06]  everything changes.
[3103.66 --> 3104.38]  I'm going with that one.
[3106.38 --> 3107.02]  All right.
[3107.02 --> 3109.12]  So Adam picks his own.
[3109.28 --> 3110.30]  We'll just stop right there.
[3112.70 --> 3113.38]  I'm safe.
[3113.46 --> 3114.36]  I'm giving no points away.
[3114.76 --> 3115.22]  That's right.
[3115.44 --> 3116.38]  David and Spencer.
[3116.84 --> 3120.52]  I should say Spencer piled on with David onto the bowler hat.
[3120.60 --> 3122.04]  That was Jamie's bowler hat.
[3122.22 --> 3122.50]  Damn it.
[3123.12 --> 3123.84]  I was like,
[3123.90 --> 3125.02]  I was like the guy from England.
[3125.12 --> 3126.48]  He's not going to do a bowler hat.
[3126.48 --> 3128.50]  I thought it was on the nose,
[3128.70 --> 3129.18]  but all right.
[3129.26 --> 3129.48]  Yeah.
[3129.70 --> 3130.42]  He sure did.
[3130.70 --> 3132.82]  And then he acted like it couldn't possibly be right,
[3132.92 --> 3134.18]  which made you want to pick it as well.
[3134.18 --> 3134.38]  Yep.
[3134.62 --> 3134.96]  He's like,
[3135.00 --> 3136.20]  he's a good actor.
[3136.46 --> 3136.94]  He is.
[3137.50 --> 3140.22]  And then Jamie went with the harrowing story of Normandy.
[3140.22 --> 3143.34]  And that was David's giving David one point,
[3143.34 --> 3145.28]  but not a victory.
[3145.50 --> 3145.66]  He,
[3145.76 --> 3148.16]  he approaches the precipice.
[3148.26 --> 3148.64]  Meanwhile,
[3148.82 --> 3150.32]  Jared scores four points.
[3150.80 --> 3151.88]  Thank you very much,
[3151.94 --> 3152.28]  everybody.
[3153.24 --> 3159.56]  Because the correct synopsis of the reckless moment is after discovering the dead body of
[3159.56 --> 3161.02]  her teenage daughter's lover,
[3161.16 --> 3164.20]  a housewife takes desperate measures to protect her family from scandal.
[3164.20 --> 3167.02]  That sounded really spicy for 45.
[3167.40 --> 3168.32]  That's what I was thinking.
[3168.82 --> 3169.22]  Yeah.
[3169.48 --> 3169.62]  Well,
[3169.68 --> 3170.72]  that's why I didn't go with it.
[3171.40 --> 3171.76]  1949.
[3172.48 --> 3172.64]  Oh,
[3172.64 --> 3173.30]  did I do it wrong?
[3173.98 --> 3174.18]  Oh,
[3174.30 --> 3174.82]  1949.
[3175.16 --> 3175.56]  I'm sorry.
[3175.82 --> 3177.40]  That might've ruined some World War II ones.
[3178.26 --> 3179.36]  Did I mess with World War II?
[3180.36 --> 3181.74]  I must've wrote that down wrong.
[3182.32 --> 3182.48]  Yeah,
[3182.50 --> 3184.10]  I wrote down 45 as well.
[3184.18 --> 3184.80]  Where would I write it down?
[3184.88 --> 3185.82]  Let me see what I wrote down here.
[3186.84 --> 3187.22]  Yeah,
[3187.28 --> 3187.66]  45.
[3188.24 --> 3188.64]  Ah,
[3188.82 --> 3189.28]  my bad,
[3189.34 --> 3189.50]  y'all.
[3190.10 --> 3194.18]  I award everybody except for David one point for my mistake.
[3194.64 --> 3197.52]  Which is exactly why I made up a story about a car named Plymouth.
[3197.94 --> 3198.82]  So Jamie gets one.
[3198.82 --> 3200.06]  Because the Plymouth came out in 41-42.
[3200.48 --> 3200.82]  So,
[3201.18 --> 3202.22]  with bonuses applied,
[3202.46 --> 3206.46]  he still has more than twice as much as anybody who's actually playing.
[3206.92 --> 3208.60]  David has 14 points.
[3208.72 --> 3209.54]  I have eight.
[3209.62 --> 3210.54]  Still not really playing.
[3210.68 --> 3211.62]  Jamie has seven.
[3212.28 --> 3213.06]  Adam and Spencer,
[3213.18 --> 3215.26]  even though Spencer broke off that hitch,
[3215.84 --> 3217.60]  they're still tied with four points each.
[3217.60 --> 3218.00]  Ah,
[3218.40 --> 3218.76]  four.
[3218.94 --> 3219.82]  It's fun here at the bottom.
[3220.34 --> 3220.80]  Woof.
[3220.80 --> 3224.66]  Right or die.
[3225.24 --> 3225.60]  Yeah.
[3226.56 --> 3227.12]  All right.
[3227.16 --> 3228.20]  We moved to round six.
[3228.26 --> 3229.36]  We get to play around six.
[3229.44 --> 3230.60]  I wasn't sure if there would be one.
[3231.24 --> 3233.34]  And this is back to a pretty normal round.
[3233.44 --> 3234.22]  It's another word.
[3234.32 --> 3234.60]  However,
[3234.68 --> 3235.54]  this word's an acronym,
[3235.72 --> 3236.94]  so it's slightly different.
[3236.94 --> 3239.80]  because it's not just any old word.
[3239.84 --> 3240.32]  It's an acronym.
[3240.32 --> 3242.88]  So you have to come up with what the acronym stands for,
[3242.92 --> 3245.20]  and then that thing described or defined.
[3245.36 --> 3245.62]  Okay?
[3245.72 --> 3247.10]  So the acronym is
[3247.10 --> 3248.32]  WIMP.
[3249.00 --> 3251.32]  W-I-M-P.
[3252.40 --> 3253.26]  That's the acronym.
[3253.38 --> 3255.06]  So you'll come up with what it stands for,
[3255.20 --> 3257.22]  and then a definition of it.
[3261.42 --> 3261.92]  All right.
[3261.94 --> 3262.66]  So I looked it up.
[3262.66 --> 3266.86]  I remember Carol Lee, PhD, being quite dominant at this game as well,
[3267.14 --> 3270.72]  and it turns out she won after six rounds.
[3271.12 --> 3271.56]  Mm-hmm.
[3272.02 --> 3272.52]  You missed it.
[3272.74 --> 3273.18]  Mm-hmm.
[3273.36 --> 3274.08]  Pressure's on.
[3274.78 --> 3276.10]  Well, this is round six right here.
[3276.60 --> 3277.32]  Oh, gosh.
[3278.22 --> 3278.90]  He had a chance,
[3279.02 --> 3281.30]  and I have to go back and listen to the transcript
[3281.30 --> 3282.70]  or read the transcript
[3282.70 --> 3285.30]  and see if that went to 12 points or 15.
[3286.18 --> 3286.58]  Oh, yeah.
[3286.58 --> 3287.36]  It's 15 points,
[3287.50 --> 3289.08]  so it's apples to apples.
[3289.08 --> 3294.00]  I have Jamie's and David's definitions,
[3294.48 --> 3297.76]  which leads us with one person.
[3299.28 --> 3301.18]  One heavy breather.
[3305.40 --> 3307.06]  Are you trying to intimidate us?
[3307.62 --> 3309.20]  Just giving good audio for the edit.
[3309.38 --> 3311.32]  Are you trying to give us a mid-90s R&B?
[3311.42 --> 3312.08]  I'm just...
[3312.72 --> 3314.66]  You were just calling back.
[3314.72 --> 3315.16]  Loop that.
[3315.68 --> 3316.28]  Jason, loop that.
[3316.28 --> 3319.32]  Either pull out a lightsaber or...
[3319.32 --> 3319.56]  Right.
[3320.06 --> 3320.26]  Yeah.
[3321.20 --> 3321.68]  Of course.
[3323.52 --> 3324.26]  Seduce us.
[3324.58 --> 3324.76]  Yeah.
[3325.10 --> 3325.42]  What are you thinking?
[3325.54 --> 3327.40]  Like, Tony Braxton or like...
[3327.40 --> 3330.88]  The specific thing that was playing when I said that
[3330.88 --> 3332.48]  was Wait a Minute by Ray J,
[3333.06 --> 3333.80]  which is very...
[3333.80 --> 3333.90]  Wow.
[3333.90 --> 3335.04]  Like, it's very...
[3335.04 --> 3337.48]  In the chorus, there's like a lot of...
[3337.48 --> 3341.10]  But also, like, some stuff by 112, I think, features that.
[3341.24 --> 3341.82]  Oh, yeah.
[3342.18 --> 3343.92]  Go to room 112 where the players dwell.
[3344.58 --> 3345.20]  I remember that.
[3345.20 --> 3346.92]  Or at least I remember...
[3346.92 --> 3347.38]  I'm zero.
[3347.66 --> 3348.46]  Informed by that.
[3348.66 --> 3349.74]  Biggie Smalls rapping about that.
[3349.80 --> 3351.38]  I'm not sure if I remember them specifically.
[3354.18 --> 3354.74]  Okay.
[3355.06 --> 3355.90]  Everybody's in.
[3356.86 --> 3357.66]  Five...
[3357.66 --> 3358.86]  What do you call them?
[3359.04 --> 3360.68]  What do you call the fulfillment of an acronym?
[3362.10 --> 3362.66]  Five...
[3362.66 --> 3363.10]  Expansion?
[3363.58 --> 3365.22]  Five acronym expansions.
[3365.30 --> 3365.72]  Thank you.
[3366.54 --> 3370.16]  With definitions for the acronym WIMP.
[3370.96 --> 3371.48]  WIMP.
[3371.48 --> 3373.76]  Number one.
[3373.76 --> 3374.64]  WIMP.
[3374.94 --> 3377.50]  Worker initialized multi-processing.
[3378.36 --> 3380.86]  A distributed computing execution strategy.
[3381.50 --> 3382.10]  Number two.
[3382.38 --> 3385.02]  Weekly interacting massive particle.
[3385.40 --> 3389.24]  A hypothetical particle proposed as a candidate for dark matter.
[3389.94 --> 3391.26]  Number three.
[3391.90 --> 3393.66]  Rot iron manifold plateau.
[3393.66 --> 3402.24]  The culmination of the process for creating low-carbon iron alloys in which the maximum efficacy of the process is achieved.
[3403.14 --> 3404.50]  Number four.
[3404.80 --> 3407.14]  Windows Internet Management Platform.
[3407.38 --> 3414.22]  The Windows Internet Management Platform is a suite of tools used to manage the network's internet access at the enterprise level.
[3415.06 --> 3416.18]  And number five.
[3416.44 --> 3418.94]  Windows Image Management Package.
[3418.94 --> 3424.82]  The closed source proprietary answer to the popular open source image manipulation library.
[3425.32 --> 3425.68]  GIMP.
[3426.22 --> 3428.08]  So it's like GIMP, but for Windows.
[3428.58 --> 3429.72]  If I had to put it in my own words.
[3430.18 --> 3431.58]  Don't you smile like that, David.
[3432.06 --> 3432.96]  No, sir.
[3433.44 --> 3434.70]  No, sir.
[3435.40 --> 3436.40]  Okay, audio listeners.
[3436.50 --> 3437.58]  You didn't see that smile, okay?
[3437.70 --> 3438.48]  I saw that smile.
[3438.76 --> 3439.96]  That smile was, that's mine.
[3441.10 --> 3441.84]  Stay away.
[3441.84 --> 3449.68]  I'm sure David was thinking, but the GNU image management program is cross-platform.
[3450.42 --> 3451.56]  Oh, I'm sure he was thinking.
[3451.56 --> 3454.98]  I hate that you are correct that that is what I was thinking.
[3457.68 --> 3459.68]  I have definitely run GIMP.
[3461.22 --> 3463.64]  Didn't we interview the guy who built GIMP one time?
[3463.64 --> 3464.30]  We sure did.
[3464.64 --> 3466.66]  He also made CockroachDB.
[3467.32 --> 3468.24]  Oh, that's right.
[3468.76 --> 3469.56]  A talented fella.
[3469.84 --> 3470.06]  Yeah.
[3470.06 --> 3475.22]  We talked a lot about GIMP, too, because I didn't have a clue until I re-interviewed him.
[3475.62 --> 3476.22]  You didn't have a clue?
[3476.34 --> 3477.12]  Did not get it that dot.
[3477.22 --> 3480.04]  No, I think I did up until like the day before.
[3480.50 --> 3482.88]  Like in my research, I didn't know it until then.
[3483.80 --> 3485.18]  It was a surprise to me.
[3485.36 --> 3488.30]  So like the plan for the call and then the call was different because of it.
[3488.90 --> 3490.28]  All right, here we go.
[3490.82 --> 3491.60]  This is not GIMP.
[3491.66 --> 3492.22]  This is WIMP.
[3492.52 --> 3492.84]  Okay.
[3493.70 --> 3494.94]  Five definitions of WIMP.
[3495.00 --> 3498.86]  I've read them all and I won't read them again unless you ask me to.
[3498.86 --> 3500.24]  And David gets to go first.
[3500.34 --> 3501.64]  So David, you're right here, man.
[3501.78 --> 3503.42]  This is the game is in your hands.
[3503.48 --> 3506.70]  All you have to do is identify the actual WIMP.
[3507.60 --> 3507.72]  Windows.
[3507.92 --> 3509.38]  So Windows is there.
[3509.44 --> 3511.10]  There's GIMP for Windows there.
[3511.30 --> 3514.20]  Yeah, I'm going to ask you to repeat just like the you don't have to do the definitions.
[3514.50 --> 3515.32]  Just the things.
[3515.72 --> 3516.12]  Yeah.
[3516.56 --> 3517.46]  The summaries.
[3518.12 --> 3518.76]  I will summarize.
[3518.76 --> 3522.86]  So number one is the worker initialized multiprocessing.
[3523.34 --> 3526.16]  That's a distributed computing execution strategy.
[3526.44 --> 3529.46]  Number two is the weekly interactive massive particle.
[3530.48 --> 3532.54]  A hypothetical particle for dark matter.
[3532.98 --> 3535.26]  Number three was wrought iron manifold plateau.
[3536.32 --> 3539.86]  And number four was the Windows internet management platform.
[3540.06 --> 3544.16]  Whereas number five was the Windows image management package.
[3544.16 --> 3546.36]  That's your WIMP.
[3547.38 --> 3548.24]  Five WIMPs.
[3548.90 --> 3551.88]  Wrought iron manifold plateau.
[3552.84 --> 3554.24]  I wish I knew more about iron working.
[3554.58 --> 3556.16]  I think I'm going to go for two.
[3557.26 --> 3560.44]  So weekly interacting massive particle.
[3561.54 --> 3562.10]  Okay.
[3562.54 --> 3564.06]  David goes for number two.
[3564.72 --> 3566.24]  And now we move to Spencer.
[3566.24 --> 3569.22]  That also is going to be my choice.
[3569.58 --> 3571.50]  I know what it looks like, guys.
[3572.08 --> 3575.50]  I had it circled on my notepad.
[3575.76 --> 3577.36]  I was going to go for number two.
[3577.88 --> 3580.38]  That just says David's name.
[3580.48 --> 3581.56]  You just circled David's name.
[3581.92 --> 3582.36]  David.
[3585.70 --> 3586.50]  All right.
[3586.60 --> 3590.46]  But it does make me feel better about my choice knowing that David had already picked it.
[3590.62 --> 3591.62]  So thank you, David.
[3592.36 --> 3592.84]  There you go.
[3593.32 --> 3594.16]  All right, Jamie.
[3594.44 --> 3595.82]  Did you write anything down?
[3595.82 --> 3601.26]  I mean, much as number five is like really like selling it to me.
[3601.56 --> 3607.82]  I think I'm going to go for the multiprocessing, the worker initiated multiprocessing.
[3608.60 --> 3609.14]  Okay.
[3609.26 --> 3609.84]  Number one.
[3610.20 --> 3610.50]  Worker.
[3610.52 --> 3611.18]  Just go for something different.
[3611.76 --> 3612.22]  There you go.
[3612.82 --> 3613.88]  And Adam.
[3618.38 --> 3623.40]  On my virtual notebook here, I have also circled number two.
[3623.40 --> 3626.38]  That's a very plausible answer.
[3627.04 --> 3627.38]  Uh-huh.
[3628.68 --> 3629.08]  Independently.
[3629.08 --> 3630.16]  Is that what you chose, Spencer?
[3631.16 --> 3631.96]  That's what David chose.
[3631.98 --> 3632.52]  It's what I chose.
[3633.00 --> 3634.70]  Well, more importantly, it's what David chose.
[3634.90 --> 3635.02]  Yeah.
[3635.08 --> 3635.48]  That's right.
[3635.52 --> 3637.84]  Get in the band back together.
[3638.24 --> 3638.62]  Yeah.
[3638.80 --> 3639.88]  Might as well pile on.
[3640.02 --> 3643.08]  I mean, if your eyes are all wrong, I do win, though.
[3643.24 --> 3643.86]  Oh, no, I don't.
[3643.94 --> 3645.14]  I only have 12.
[3645.26 --> 3647.40]  I'm feeling like number four.
[3647.80 --> 3649.06]  I'm feeling number four is good.
[3649.88 --> 3650.58]  What's that one, Jared?
[3651.38 --> 3653.44]  Windows Internet Management Platform.
[3653.78 --> 3654.12]  That's right.
[3655.02 --> 3656.10]  It's missing your co-pilot.
[3657.04 --> 3658.50]  You're not going to guess that one, are you?
[3659.02 --> 3659.80]  Of course.
[3659.98 --> 3660.68]  It's safe play.
[3663.68 --> 3664.48]  I don't know.
[3664.48 --> 3666.08]  I don't understand you sometimes.
[3667.04 --> 3667.68]  All right.
[3667.74 --> 3669.82]  Adam picked his own again.
[3672.02 --> 3674.40]  So he gets zero points for picking his own.
[3674.74 --> 3675.74]  I'm too scared of David.
[3676.38 --> 3676.98]  He's going to win.
[3676.98 --> 3680.46]  I don't want to, though.
[3680.46 --> 3681.24]  I don't want to pick that one.
[3681.28 --> 3681.92]  It's a cop out.
[3682.40 --> 3683.34]  I should have more fun.
[3683.52 --> 3683.82]  Number two.
[3683.90 --> 3684.50]  We'll go with number two.
[3684.62 --> 3685.32]  Which one are you doing?
[3685.44 --> 3686.22]  We'll go with number two.
[3686.42 --> 3686.58]  Yeah.
[3686.60 --> 3687.32]  Let's have more fun.
[3687.98 --> 3689.70]  Whoever earned that answer gets it.
[3689.74 --> 3690.50]  Whatever it is.
[3690.68 --> 3691.00]  Fair.
[3691.46 --> 3692.16]  It's a pile on.
[3692.26 --> 3693.40]  That's the best answer.
[3693.88 --> 3694.46]  Dark matter.
[3694.58 --> 3695.50]  Come on, dark matter.
[3695.88 --> 3696.22]  All right.
[3696.28 --> 3699.62]  Well, David, Spencer, and Adam all piled on.
[3699.80 --> 3702.10]  They followed David to the weekly interactive.
[3702.10 --> 3702.82]  He's so excited.
[3702.92 --> 3703.36]  Look at David.
[3703.80 --> 3704.58]  Massive particles.
[3704.58 --> 3704.90]  He's pumped.
[3705.22 --> 3706.30]  And he knows.
[3706.30 --> 3706.98]  He knows.
[3706.98 --> 3707.62]  He's like, yeah.
[3707.96 --> 3711.90]  And that is the correct definition for WIMP.
[3712.30 --> 3714.10]  It's a weekly interacting massive particle.
[3714.34 --> 3716.28]  So David scores two.
[3716.52 --> 3717.48]  Spencer gets two.
[3717.60 --> 3718.50]  Adam gets two.
[3718.84 --> 3721.58]  Jamie picked worker initialized multiprocessing.
[3721.62 --> 3722.60]  That's David's.
[3722.72 --> 3722.96]  Ugh.
[3723.02 --> 3723.50]  This guy.
[3723.96 --> 3725.98]  You just can't do wrong.
[3726.12 --> 3727.00]  You can't do wrong.
[3728.68 --> 3731.10]  So above and beyond, he gets three points.
[3731.22 --> 3732.28]  Didn't even need that many.
[3732.92 --> 3733.36]  Gosh.
[3733.36 --> 3736.70]  And he wins with 17 points.
[3736.70 --> 3737.40]  Oh, my gosh.
[3737.68 --> 3738.68]  Congrats, David.
[3738.84 --> 3739.14]  Thank you.
[3740.08 --> 3740.70]  Thank you.
[3740.76 --> 3741.40]  So good.
[3742.04 --> 3746.32]  Tied for the fastest win in pound-define history.
[3746.48 --> 3748.64]  Perhaps the largest margin of victory.
[3749.24 --> 3751.76]  When second place was me with eight.
[3752.04 --> 3753.24]  I'm not even playing, guys.
[3753.94 --> 3754.16]  Yeah.
[3754.16 --> 3757.82]  So actual second place was Jamie with seven.
[3758.66 --> 3760.36]  A full 10 points behind David.
[3760.62 --> 3763.56]  And then Spencer and Adam with six.
[3764.28 --> 3766.08]  And one of those points was Gibby's.
[3766.64 --> 3767.08]  That's right.
[3767.08 --> 3773.62]  So David, as is our new tradition that I'm just making up right now, you must improvise
[3773.62 --> 3774.20]  us a song.
[3774.32 --> 3774.94]  No, I'm just kidding.
[3774.94 --> 3775.34]  Oh, hell no.
[3778.68 --> 3781.04]  I just mistook you from Matt Reier for a moment there.
[3781.26 --> 3782.84]  No, we will not have you to do that.
[3782.90 --> 3784.98]  However, you can say anything you like.
[3785.06 --> 3787.08]  You could promote anything you like.
[3787.08 --> 3789.26]  You have a moment to just say whatever you want, man.
[3789.38 --> 3789.88]  Go for it.
[3790.44 --> 3790.56]  Sure.
[3790.56 --> 3797.04]  I guess I'll plug some stuff from the open source stuff from the company I work for.
[3797.94 --> 3800.12]  So the company I work for is Posit.co.
[3800.74 --> 3804.26]  We make software for data scientists and scientific computing.
[3804.64 --> 3806.48]  A couple of things that might be interesting to check out.
[3806.58 --> 3811.04]  There's a project called Quarto, which is a sort of literate programming environment that
[3811.04 --> 3815.86]  lets you render R and Python code into websites, all kinds of documents.
[3815.86 --> 3821.66]  And we are also building an editor for data scientists called Positron.
[3822.00 --> 3824.92]  So check that out at positron.posit.co.
[3825.42 --> 3826.14]  Very cool.
[3826.42 --> 3828.44]  We will link up all those things.
[3828.60 --> 3833.14]  Posit.co, Quarto.org, and positron.posit.co.
[3833.14 --> 3834.14]  Positron.posit.co.
[3834.28 --> 3834.84]  There you go.
[3835.38 --> 3839.26]  We'll link those up in the show notes so you don't have to read them out loud and type
[3839.26 --> 3842.46]  them into your browser if you're driving or something like that.
[3842.84 --> 3843.38]  That's it.
[3843.46 --> 3844.30]  That's Pound to Find.
[3844.38 --> 3845.42]  This has been a fun one.
[3845.42 --> 3848.24]  I wouldn't say it's been a competitive one, but it's had a lot of laughs.
[3849.40 --> 3851.86]  And of course, these are our ChangeLog++ people.
[3852.10 --> 3854.14]  So I think we have 11 minutes.
[3854.44 --> 3855.12]  Is that fair, Jamie?
[3855.18 --> 3857.06]  You got 11 minutes to the top of the hour?
[3857.50 --> 3857.72]  All right.
[3857.78 --> 3861.76]  So if you are one of us, if you are a Plus Plus member, stick around for a bonus round
[3861.76 --> 3864.06]  right after we say goodbye.
[3864.40 --> 3867.40]  Adam, any final words before we hit our bonus round just for the Plus Plus people?
[3868.22 --> 3871.00]  You know, if you're a Plus Plus subscriber, it's better.
[3871.62 --> 3872.50]  It's been better for years.
[3873.02 --> 3873.38]  That's it.
[3873.84 --> 3874.10]  All right.
[3874.10 --> 3874.56]  Bye, friends.
[3874.56 --> 3875.40]  Bye, friends.
[3875.62 --> 3876.02]  Bye, friends.
[3879.24 --> 3879.60]  Okay.
[3879.80 --> 3884.38]  So the guys did stick around and we played a pretty epic bonus round.
[3884.72 --> 3885.26]  The winner?
[3885.48 --> 3890.20]  I don't want to spoil anything, but I will tell you it's the person you are least likely
[3890.20 --> 3890.68]  to guess.
[3890.68 --> 3894.90]  If you're not a ChangeLog++ member, join us, why don't you?
[3894.90 --> 3895.90]  Make the ads disappear.
[3895.90 --> 3896.68]  Make the ads disappear.
[3896.68 --> 3899.78]  Get closer to the metal with cool bonuses like this one.
[3899.78 --> 3900.86]  Get some free stickers.
[3900.86 --> 3906.24]  Plus that warm, fuzzy feeling you get from directly supporting something you enjoy.
[3906.24 --> 3908.70]  Learn more at ChangeLog.com.
[3908.70 --> 3914.78]  If you're hearing this right after it drops, then I'm road tripping to Denver for our big
[3914.78 --> 3916.72]  live show and Pipely launch.
[3917.04 --> 3918.48]  If you can't make it, no big deal.
[3918.48 --> 3922.42]  We are recording everything and we'll start shipping those episodes next week.
[3922.80 --> 3923.94]  Have yourself a great weekend.
[3924.34 --> 3927.26]  Send the ChangeLog to a friend or three who might dig it.
[3927.26 --> 3929.18]  And let's talk again real soon.
[3947.04 --> 3950.14]  All right.
[3950.16 --> 3952.28]  You have entered bonus round.
[3952.46 --> 3953.72]  The scores are wiped out.
[3953.84 --> 3955.52]  It's zero to zero to zero to zero.
[3955.52 --> 3956.40]  Take that, David.
[3956.82 --> 3957.18]  Jubilee.
[3957.68 --> 3958.12]  Yes.
[3958.38 --> 3959.44]  We've all got a chance.
[3959.56 --> 3960.10]  Anyone's game.
[3960.24 --> 3960.86]  Anyone's game.
[3961.06 --> 3961.96]  Anybody's got a chance.
[3962.02 --> 3964.32]  And this is the most free form round we have.
[3964.38 --> 3966.32]  It's called How Do You Do, Fellow Humans?
[3966.32 --> 3968.00]  Game on.
