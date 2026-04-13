[0.00 --> 2.52]  I've got one which is something that's kind of triggering.
[2.74 --> 5.40]  I don't know if anyone else has got sort of triggers from being horrified.
[5.78 --> 7.46]  One of my old bosses used to come to me,
[7.64 --> 9.68]  and if he started the sentence with,
[10.10 --> 11.04]  what do you know about?
[11.54 --> 13.62]  Then I knew immediately it was downhill.
[14.10 --> 16.32]  It's like, what do you know about Perl?
[16.48 --> 18.20]  It's like, uh-oh, where's this going?
[18.66 --> 21.66]  Or, what do you know about directory services and exchange?
[21.80 --> 23.98]  It's like, um, that they exist?
[24.14 --> 24.92]  Great, you'll do.
[25.34 --> 27.32]  And off you'll be shipped to a client's site.
[30.00 --> 32.98]  What's up, friends?
[33.06 --> 35.40]  This episode is brought to you by Sourcegraph.
[35.86 --> 38.66]  With the release of Sourcegraph 4.0
[38.66 --> 41.32]  and the Starship event just a few weeks behind us,
[41.54 --> 44.62]  it is super clear that Sourcegraph is becoming not just CodeSearch,
[44.62 --> 47.76]  but a full-on code intelligence platform.
[48.18 --> 48.96]  And I'm here with Joel Cortler,
[49.06 --> 51.30]  Product Manager of Code Insights for Sourcegraph.
[51.58 --> 54.78]  Joel, this move from CodeSearch to Code Intelligence
[54.78 --> 56.22]  is a really big deal.
[56.48 --> 59.04]  How would you explain this feature, Code Insights,
[59.04 --> 61.38]  if you're just talking to folks in the hallway track
[61.38 --> 62.58]  of your favorite conference?
[63.16 --> 64.98]  I would really start with the technical
[64.98 --> 66.40]  because before I was a product manager,
[66.50 --> 67.42]  I used to be an engineer as well.
[67.70 --> 70.38]  And it's really cool and exciting just to be able to say,
[70.54 --> 72.58]  we're going to turn your code base into a database.
[73.04 --> 75.38]  And the structured language that you need to interact
[75.38 --> 77.44]  is just the ability to write a code search.
[77.74 --> 79.66]  You know, literal search, that's totally fine.
[79.82 --> 80.86]  Regular expression, you know,
[80.88 --> 82.30]  that'll give you a few more advanced options,
[82.56 --> 83.46]  even a structural search.
[83.46 --> 86.60]  But the number of long-tail possibilities it unlocks,
[86.76 --> 89.02]  truly the journey of building this product
[89.02 --> 90.98]  was just saying, well, we've just unlocked,
[91.20 --> 93.20]  you know, an infinite number of possibilities.
[93.64 --> 95.54]  We got to figure out some immediate use cases
[95.54 --> 97.48]  so we can start to, you know, invest in this product,
[97.60 --> 98.30]  build it and sell it.
[98.74 --> 100.12]  But we're only getting started
[100.12 --> 101.42]  in terms of the number of uses
[101.42 --> 102.72]  that we're uncovering for it.
[103.06 --> 104.88]  The story I told you about discovering,
[104.96 --> 106.32]  like, version tracking turned out
[106.32 --> 107.40]  to be a really important use case
[107.40 --> 108.96]  that wasn't even on our roadmap six months
[108.96 --> 110.44]  prior to discovering that
[110.44 --> 111.76]  as we were already planning to launch this product
[111.76 --> 112.92]  until we talked to enough folks,
[113.22 --> 114.12]  realized this was a problem,
[114.12 --> 115.26]  and then found, well, oh,
[115.26 --> 117.38]  that's like a simple regular expression capture group
[117.38 --> 118.46]  that you can just plug right in
[118.46 --> 119.94]  because we really built this system
[119.94 --> 122.10]  to not limit the power of what we built.
[122.18 --> 123.08]  We don't want to give you, like,
[123.20 --> 124.08]  three out-of-the-box templates
[124.08 --> 125.26]  and you can only change, like,
[125.28 --> 126.18]  one character or something.
[126.30 --> 128.10]  It's truly, like, the templates are there
[128.10 --> 129.20]  to hold your hand and get you started,
[129.32 --> 131.18]  but if you can come up with anything
[131.18 --> 132.40]  you want to track in your code base,
[132.46 --> 133.48]  you can do that with Code Insights.
[133.74 --> 134.86]  I love it. Thank you, Joel.
[134.98 --> 138.52]  So right now there is a treasure trove of insights
[138.52 --> 139.60]  just waiting for you.
[139.88 --> 141.32]  Living inside your code base,
[141.32 --> 144.34]  your code base is now a querible database
[144.34 --> 145.36]  thanks to Sourcegraph.
[145.78 --> 148.32]  This opens up a world of possibilities for your code
[148.32 --> 149.92]  and the intelligence you can gain from it.
[150.20 --> 152.04]  A good next step is to go to
[152.04 --> 155.46]  about.sourcegraph.com slash code dash insights.
[155.76 --> 157.02]  The link will be in the show notes.
[157.38 --> 159.86]  See how the teams are using this awesome feature.
[160.06 --> 164.94]  Again, about.sourcegraph.com slash code dash insights.
[165.30 --> 167.58]  Again, this link is in the show notes.
[167.58 --> 183.34]  Let's do it.
[183.92 --> 185.00]  It's go time.
[185.00 --> 186.92]  Welcome to Ghost Time.
[187.64 --> 189.56]  Your source for spooky conversations
[189.56 --> 191.24]  from around the digital campfire.
[191.70 --> 194.62]  Special thanks to our partners Fastly and Fly.io
[194.62 --> 197.42]  for helping us bring you Go Time each and every week.
[197.80 --> 198.08]  Okay.
[198.52 --> 199.88]  Here we go.
[199.88 --> 212.14]  Hello.
[212.14 --> 212.44]  Hello.
[213.40 --> 216.10]  And welcome to Ghost Time.
[216.48 --> 217.28]  I'm Matt Ryer.
[217.66 --> 220.68]  Today we're talking about tech horror stories.
[220.96 --> 222.76]  I'm joined, as ever,
[223.40 --> 224.06]  Johnny Boo.
[224.36 --> 225.52]  Johnny Borsico's here.
[225.60 --> 226.08]  Hello, Johnny.
[226.74 --> 228.02]  Hello, Matt.
[228.02 --> 231.18]  Welcome to the spooky Go Time episode.
[231.78 --> 232.90]  Are you getting in the spirit of it?
[232.98 --> 235.42]  You've really got to get in the spirit of it.
[236.30 --> 236.98]  Are you?
[237.12 --> 237.32]  No.
[237.80 --> 238.02]  Yeah.
[239.14 --> 242.80]  We're also joined here by Chris Brando.
[244.58 --> 245.48]  Spooky ghost.
[245.56 --> 246.30]  Hello, Chris.
[247.04 --> 247.34]  Hello.
[247.82 --> 248.92]  I'm back again.
[249.14 --> 249.48]  Finally.
[249.88 --> 250.20]  Yes.
[250.28 --> 251.26]  Welcome back again.
[251.82 --> 254.74]  We're also joined by your friend and mine,
[254.86 --> 256.32]  Natalie Pistonowitch.
[256.52 --> 258.00]  Hello, Natalie.
[258.56 --> 258.94]  Hello.
[260.38 --> 260.78]  Yeah.
[260.96 --> 261.98]  Getting into the spirit.
[264.20 --> 264.64]  Yeah.
[265.04 --> 266.62]  We have a special guest joining us.
[266.88 --> 267.88]  You're not going to believe this.
[268.32 --> 269.12]  It's Spoopy D.
[269.54 --> 270.30]  D Kitchen.
[270.50 --> 271.16]  Welcome, D.
[271.52 --> 272.18]  Thank you.
[272.30 --> 273.66]  I'm enjoying being here.
[274.04 --> 275.22]  I even got the backdrop for it.
[275.60 --> 275.88]  Hmm.
[275.96 --> 276.24]  Good.
[276.36 --> 278.60]  Well, that's a good start because it literally just started.
[278.76 --> 282.20]  So if you, I mean, really the only way is down now in a lot of ways,
[282.24 --> 284.42]  but hopefully we don't go there.
[284.42 --> 286.92]  But we are talking about scary things today.
[287.00 --> 288.84]  How are you generally with scary things, D?
[289.20 --> 290.14]  That's my career.
[291.74 --> 292.42]  All of it.
[292.78 --> 293.00]  Yeah.
[293.66 --> 294.10]  Okay.
[294.24 --> 294.74]  Anyone else?
[294.86 --> 295.78]  Anyone scared of ghosts?
[296.40 --> 297.64]  I'm scared of ghost time.
[298.34 --> 298.58]  Yeah.
[298.62 --> 299.56]  You're scared of ghost time.
[300.06 --> 301.72]  I'm actually scared of horror movies.
[301.84 --> 302.70]  I don't really watch them.
[302.96 --> 303.26]  Oh.
[303.40 --> 303.82]  Oh, yeah.
[303.98 --> 304.32]  Same.
[304.50 --> 305.68]  Heebie-jeebies for me.
[306.04 --> 306.32]  Hmm.
[306.48 --> 307.46]  I just find them boring.
[307.92 --> 308.18]  Yeah.
[308.80 --> 309.90]  But you come from the industry.
[310.12 --> 313.06]  I remember you saying, Chris, that you see a movie and you kind of,
[313.22 --> 315.78]  the first three minutes and you know exactly how it's going to be laid out.
[316.24 --> 316.56]  Yeah.
[316.56 --> 320.78]  It's the curse of having a creative writing degree and specializing in screenwriting.
[321.08 --> 323.92]  It's just, all movies are just kind of ruined.
[325.12 --> 325.56]  Yeah.
[325.66 --> 326.58]  It's all generics.
[326.72 --> 327.32]  That's what I said.
[327.34 --> 329.00]  You'd be happier if you're just an idiot.
[329.56 --> 330.44]  I've always said that.
[333.18 --> 335.48]  Is this something you know from personal experience, Matt?
[337.72 --> 338.52]  Shots fired.
[338.52 --> 344.10]  I also don't really like horror films, especially if there's any kind of contradiction in it.
[344.18 --> 345.14]  I can't deal with that.
[345.42 --> 350.44]  Like, if there's an invisible thing that can grab you, first of all, it's invisible.
[350.62 --> 351.34]  It would be blind.
[351.50 --> 352.24]  We covered this.
[352.54 --> 355.32]  But also, if it can grab you, you can grab it.
[355.42 --> 356.24]  You can hurt it.
[356.34 --> 357.66]  Like, it's not fair.
[357.96 --> 361.62]  It's like when the physics don't apply generally and I'm just out.
[361.76 --> 364.12]  And I just tell everyone in the cinema, I'm like, sorry, everyone.
[364.22 --> 365.06]  I can't stay.
[365.60 --> 368.02]  I've got to go because of the inconsistencies of the physics.
[368.02 --> 369.86]  No, just go and get some popcorn and go.
[370.18 --> 371.66]  Do you get sweet or salty popcorn?
[372.66 --> 373.02]  Salty.
[373.42 --> 374.14]  Do you have a choice?
[374.38 --> 375.26]  Or is it always salty?
[375.48 --> 376.12]  No, you have a choice.
[379.00 --> 379.88]  You have a choice.
[380.24 --> 380.48]  Yeah.
[381.08 --> 381.68]  What do you mean?
[381.74 --> 384.70]  Like, there's the police are going around saying, hey, are you only having salty?
[385.06 --> 385.54]  What are you doing?
[386.38 --> 392.42]  I only discovered in my late 20s that some other countries sell popcorn that is not just salty in the cinema.
[392.90 --> 393.58]  Oh, right.
[393.82 --> 394.12]  Yeah.
[394.12 --> 397.50]  And then I came to the US and then it's like not just two flavors, but 15.
[398.02 --> 398.56]  Yeah, of course.
[398.68 --> 398.78]  Yeah.
[399.68 --> 400.04]  Yeah.
[400.44 --> 401.70]  That's a horror story there.
[402.06 --> 402.22]  Yeah.
[402.22 --> 409.10]  You can choose individual bits of corn and have them different flavors and just have as many as you want.
[409.24 --> 409.86]  You just program it.
[409.90 --> 412.18]  You do it as an app and then it pops it on demand.
[412.86 --> 415.96]  You say that, but we do have soda machines where you can choose your own flavor.
[416.34 --> 416.70]  Yeah.
[416.98 --> 417.74]  I've seen that.
[417.82 --> 419.48]  Those freestyle Coke things.
[419.60 --> 419.68]  Yeah.
[419.68 --> 421.04]  Has anyone come up with a good one yet?
[421.10 --> 422.80]  Because I imagine they're all terrible.
[423.34 --> 425.36]  But you reckon someone's like, do you know what?
[425.38 --> 429.64]  I've accidentally pressed these three and I've made a brand new flavor that never existed before.
[430.00 --> 430.34]  Well, no.
[430.46 --> 435.94]  I think they make it so you can't make any truly terrible tasting ones because that would be perhaps bad for them.
[436.28 --> 436.30]  So.
[437.26 --> 437.82]  Oh, really?
[438.06 --> 438.42]  Clever.
[438.42 --> 439.28]  How do they do that?
[440.00 --> 440.92]  Oh, well, we'll never know.
[441.52 --> 444.78]  Well, speaking of horror stories, let's get into this, shall we?
[444.82 --> 447.16]  Who wants to kick us off with a spooky story?
[447.30 --> 454.08]  Oh, by the way, we should actually introduce Dee because Dee wrote a package that I think a lot of people here will be familiar with.
[454.42 --> 455.56]  Can you tell us about Blue Monday?
[456.58 --> 457.40]  Ah, Blue Monday.
[457.90 --> 462.34]  It's named because there was a package called Black Friday, which is all the best markdowns.
[462.34 --> 463.52]  And it's a markdown package.
[464.10 --> 468.76]  And after you've generated markdown, markdown can include HTML, which makes it dangerous.
[469.20 --> 474.72]  It's probably you're using this because you've got user-generated content and you want to sanitize it.
[474.72 --> 478.88]  So Blue Monday is named after the New Order song, but follows Black Friday.
[479.46 --> 481.52]  And it basically sanitizes HTML.
[481.78 --> 488.54]  It's the only Go package that sanitizes HTML, which is a foolish and reckless thing to attempt to take on.
[488.92 --> 489.66]  But that's what I did.
[490.90 --> 491.40]  Amazing.
[491.40 --> 494.68]  And what do you like about it and what don't you like about it?
[495.00 --> 496.12]  I like that it works.
[496.54 --> 498.38]  It's all a streaming parser.
[498.62 --> 499.60]  It's got fixed memory.
[499.78 --> 503.22]  So you can use it quite comfortably in a lot of situations and throw a lot through it.
[503.52 --> 507.42]  I don't like when people tell me there's security issues with it and then I have to go,
[507.82 --> 509.98]  oh, I'm supposed to take this open source thing seriously.
[510.64 --> 511.86]  I do appreciate it.
[511.90 --> 514.00]  I should actually say I do appreciate security reports.
[514.20 --> 520.54]  But at the same time, you never can predict when they're going to turn up and you never know what kind of worms you're going to open
[520.54 --> 521.96]  to try and actually figure it out.
[521.96 --> 527.82]  Yeah, there must be a lot of responsibility, actually, because it is a package that is used and quite trusted.
[527.82 --> 529.70]  Yeah, it's used.
[530.28 --> 534.90]  I don't know how many stars it's got, but the stars don't betray the number of times it's used.
[534.90 --> 537.28]  Like it's used in Hugo and everyone uses Hugo.
[537.54 --> 540.20]  And this is the HTML sanitizer that keeps Hugo safe.
[540.36 --> 542.04]  And it's used in so many things.
[542.12 --> 544.22]  It's got literally thousands of dependencies.
[544.68 --> 546.42]  Do I take it seriously and stressfully?
[546.62 --> 548.02]  No, no, I don't.
[548.26 --> 553.96]  I figure that if someone is brave enough to take an open source project with a MIT license or BSD3 clause,
[554.04 --> 557.90]  whatever it is, and incorporate into their production software, that's on them.
[558.66 --> 559.44]  Okay, fair enough.
[559.82 --> 562.44]  Well, I have done that, but no, good to know.
[562.44 --> 565.44]  I genuinely have used it, though, quite a few times.
[565.86 --> 570.72]  So I like it because it's like you opt in to what you want to support, don't you?
[570.78 --> 573.22]  Like you explicitly say the things that you want to allow.
[573.82 --> 577.68]  Yeah, there's no way of defining what makes a good HTML sanitizer.
[577.96 --> 580.06]  Everyone's got a different rule, depending on their use case.
[580.44 --> 584.52]  But the Java OWASP, Open Web Application Security thing,
[585.04 --> 588.42]  their sanitizer defined this really beautiful interface for sort of going,
[588.42 --> 592.74]  I want to allow images, but I don't want to allow this images that end in .gif.
[593.16 --> 596.32]  And I copied their API and then extended it for my own use.
[596.78 --> 598.66]  So, yeah, it's a really good way of doing it.
[599.96 --> 600.40]  Nice.
[600.64 --> 606.62]  Okay, well, I'm going to tell you about a horror story in tech of mine that happened quite recently.
[606.62 --> 612.74]  I have this project which interacts with Twitter and interacts with the Twitter API.
[613.14 --> 616.26]  And so it poll results and then compares them and stuff.
[616.88 --> 619.14]  And that's just one of the things it does at a regular interval.
[619.70 --> 624.18]  And then what happened recently was something happened where like the API key changed
[624.18 --> 625.84]  and that request failed.
[626.20 --> 631.38]  And because of the way I was doing it in GCP, it meant essentially that it would retry.
[631.56 --> 634.46]  And because it was scheduled, it kept compounding.
[634.46 --> 640.14]  And this ran up a $1,000 bill for me, for yours truly.
[640.58 --> 644.22]  $1,000 given, paid, gone.
[644.76 --> 646.90]  So that's a bit of a tech horror story.
[648.06 --> 649.28]  Any advice for me?
[649.74 --> 650.68]  Is it tax deductible?
[653.50 --> 653.94]  Probably.
[654.34 --> 656.60]  AWS famously was funded if you get something wrong.
[656.68 --> 657.70]  Did GCP not do that?
[657.96 --> 658.46]  I don't know.
[658.50 --> 659.42]  It's quite recent.
[659.54 --> 661.10]  I haven't yet tried that.
[661.24 --> 663.50]  Do you think I should get in touch with support and see if they'll...
[663.50 --> 665.08]  $1,000 would motivate me.
[665.66 --> 666.02]  Yeah.
[666.58 --> 667.00]  There you go.
[667.06 --> 667.44]  $1,000.
[668.40 --> 668.76]  Okay.
[668.84 --> 671.54]  Well, I'll try it and I'll let the listeners know how we get on.
[671.82 --> 672.52]  Could have been worse.
[672.94 --> 673.18]  Right?
[673.62 --> 674.66]  Could have been $2,000.
[674.98 --> 675.30]  Yeah.
[675.68 --> 676.86]  Well, just $1,001.
[677.50 --> 678.66]  Would be worse, wouldn't it?
[678.90 --> 679.20]  It would.
[679.58 --> 681.58]  What would you do, Johnny, if you saw that?
[682.00 --> 683.14]  I'd call you and say, hey.
[683.14 --> 685.20]  You got a grand.
[685.48 --> 685.96]  I hear you.
[686.08 --> 686.66]  You're loaded.
[687.28 --> 691.00]  You're just wasting $1,000 here, $1,000 there on your bugs and stuff.
[691.30 --> 694.34]  Honestly, when I found out about it, I wanted to just karate chop the air.
[694.80 --> 698.52]  That was the kind of spooky reaction I had to it.
[698.60 --> 700.16]  Just like, whew, in the air.
[700.64 --> 700.92]  Angry.
[701.78 --> 703.42]  But yeah, it's a good lesson though, isn't it?
[703.48 --> 706.34]  Like set budgets and stuff on your things.
[706.70 --> 707.32]  Do set an alarm.
[707.44 --> 707.60]  Yeah.
[707.94 --> 708.16]  Yeah.
[708.34 --> 709.06]  Budget alarms.
[709.52 --> 709.88]  Observability.
[709.88 --> 711.32]  Yes, yes.
[711.38 --> 712.68]  And you know a thing or two about that, yeah?
[714.68 --> 715.04]  Yeah.
[715.88 --> 716.24]  Okay.
[716.46 --> 718.34]  Who can beat my $1,000 bill?
[718.68 --> 719.74]  Not a $1,000 bill.
[719.92 --> 721.06]  Oh yeah, it was a $1,000 bill.
[721.14 --> 724.06]  But that makes it sound like it was one thing, doesn't it?
[724.06 --> 725.46]  Like a single bill.
[725.90 --> 727.28]  It had $1,000 on it.
[727.58 --> 728.40]  So it's not that.
[728.54 --> 730.68]  It was just paid through bank transfer.
[731.40 --> 732.66]  Okay, who's got another one?
[733.14 --> 736.72]  I have one that could have cost many thousands of dollars.
[737.00 --> 737.86]  Oh, Johnny.
[737.86 --> 738.94]  It wasn't spotted.
[739.36 --> 739.44]  Okay.
[739.44 --> 745.86]  So one of the things you can do with function as a service things like AWS Lambda, for example,
[746.16 --> 751.08]  is that you can trigger a Lambda when you write an object to an S3 bucket.
[751.36 --> 759.42]  Word of advice, do not have your Lambdas write to a bucket that they are themselves responding to.
[761.32 --> 761.88]  Oh.
[761.88 --> 765.94]  Because that's going to give you a very nasty bill.
[766.46 --> 766.66]  Yeah.
[766.72 --> 768.96]  And you will not like what you see.
[769.60 --> 772.36]  So yeah, thankfully, Budget Alarms came to the rescue.
[772.94 --> 773.20]  Uh-huh.
[773.52 --> 774.04]  There you go.
[774.08 --> 774.80]  That's the lesson there.
[774.80 --> 777.98]  So what happens is an object goes in the first time.
[778.06 --> 779.10]  That triggers the Lambda.
[779.30 --> 784.14]  The Lambda then writes something into that same bucket, which then triggers another Lambda.
[784.40 --> 784.64]  Right.
[784.72 --> 785.96]  Which then writes something.
[786.32 --> 788.88]  And like, how quickly does that get out of hand?
[789.74 --> 790.26]  Very quickly.
[791.02 --> 791.10]  Yeah.
[791.10 --> 799.30]  Like, if you want to see how well Lambda scales on your own dime, you can do that.
[799.30 --> 802.92]  And yeah, it'll cost you money very quickly.
[803.32 --> 803.66]  Wow.
[803.90 --> 804.10]  Yeah.
[804.58 --> 804.90]  Yeah.
[805.02 --> 805.32]  Okay.
[805.68 --> 806.18]  Pretty good.
[806.52 --> 808.78]  But yeah, the alerts came to the rescue.
[809.22 --> 809.56]  Nice one.
[809.66 --> 809.86]  Mm-hmm.
[810.20 --> 810.50]  Mm-hmm.
[810.86 --> 811.42]  Okay.
[811.76 --> 812.86]  Anyone else got one for us?
[813.28 --> 814.78]  I've got another infinite loop one.
[815.08 --> 816.60]  Are we allowed to name company names?
[816.76 --> 817.22]  I don't know.
[817.36 --> 818.82]  Maybe it's internal and I shouldn't.
[818.94 --> 819.10]  Yeah.
[819.22 --> 819.58]  I don't know.
[819.58 --> 823.68]  I worked for a certain company which has an orange logo that has a bit of a light flying
[823.68 --> 826.04]  shining behind it, and they man in the middle of the entire internet.
[826.04 --> 832.58]  Now, with that in mind, when I was working for said company and their DDoS team, we didn't
[832.58 --> 833.16]  DDoS people.
[833.30 --> 834.70]  We were protecting against DDoSers.
[834.80 --> 834.88]  Yeah.
[835.00 --> 835.40]  I've wounded.
[835.74 --> 836.04]  I don't know.
[836.10 --> 836.82]  The DDoS team.
[837.02 --> 839.22]  I just suddenly realized, I was like, that's the opposite of what we're doing.
[839.66 --> 843.22]  Now, we were trying to protect, and they have a system, right?
[843.48 --> 848.06]  They've got all these 200 pops or points of presence and thousands and thousands of servers.
[848.62 --> 851.66]  And every single one of these is protecting some of the traffic.
[851.84 --> 854.06]  Each machine can do like 20,000 requests per second.
[854.06 --> 859.72]  And yet they need to be able to actually show the value back to the customer and make the
[859.72 --> 860.82]  sort of decision centrally.
[861.02 --> 864.52]  So you send all the logs somewhere, and they're all being sent to one data center.
[865.34 --> 869.64]  So what you end up with is like, if you're doing globally 10 million requests per second,
[869.86 --> 872.58]  you get 10 million log lines per second in one place.
[872.98 --> 874.10]  Ah, nice.
[874.10 --> 879.72]  Certain customer on a certain point in time, industry and type to be non-disclosed,
[880.06 --> 884.50]  wrote an infinite loop in their client and basically spiked 8 million requests per second
[884.50 --> 885.88]  on top of our normal load.
[886.00 --> 886.40]  Oh, wow.
[886.58 --> 889.62]  And they basically broke our logging, entire visibility.
[890.00 --> 895.06]  So they were effectively under attack, but now flying blind because we couldn't see anything
[895.06 --> 896.14]  because they'd broken all the login.
[896.66 --> 897.24]  Oh, no.
[897.84 --> 899.02]  That was not a good day.
[899.68 --> 899.96]  Yeah.
[900.24 --> 901.40]  That one doesn't sound fun.
[901.52 --> 902.08]  What happened?
[902.72 --> 905.56]  We figured out which customer it was, but we couldn't figure out the rest.
[905.68 --> 908.58]  But we asked them what they'd done, and they figured out that bit and stopped it.
[908.72 --> 909.14]  Oh, wow.
[909.32 --> 910.06]  They fessed up to it.
[910.10 --> 910.84]  They owned up to it.
[911.18 --> 912.26]  Somebody run infinite loop.
[912.58 --> 912.92]  Yes.
[913.58 --> 914.58]  I think they realized.
[915.32 --> 917.24]  They must have seen what was happening on their side.
[917.24 --> 922.54]  So they didn't pull a, well, I will not name names, but they didn't blame any intern?
[923.64 --> 927.52]  Oh, we've got a certain thing where we actually, an intern did that.
[927.66 --> 928.48]  I heard that intern.
[928.60 --> 929.68]  He's actually a really good guy.
[930.00 --> 931.98]  He's become a full-time engineer in that team, you know.
[932.32 --> 932.98]  He's really good.
[933.22 --> 934.74]  Learned a lesson that none of us will replicate.
[935.08 --> 935.44]  Oh, yeah.
[935.52 --> 936.48]  I love interns.
[936.48 --> 941.34]  I just don't like to throw them under the bus when something goes wrong with my company.
[942.62 --> 944.26]  No, that one was interesting.
[944.26 --> 946.32]  Also, that said, a man-in-the-middle company.
[946.68 --> 947.86]  We had a system.
[948.12 --> 949.22]  The system was brilliant, right?
[949.26 --> 952.82]  You could send an instruction to any machine in the world in under 10 seconds, and every
[952.82 --> 954.36]  machine received the same instruction.
[955.36 --> 959.08]  And that's great when you want to say there's a new domain name, because you tell the whole
[959.08 --> 959.92]  world at the same time.
[960.20 --> 965.04]  But it's really bad when you say there's a new way to stop traffic, and we've made a
[965.04 --> 965.94]  greedy regex.
[966.32 --> 967.90]  And the greedy regex was the problem.
[968.32 --> 972.54]  Now, frankly, the system shouldn't have allowed it, but the system did allow it.
[972.54 --> 975.36]  And we were all at lunch.
[975.42 --> 976.54]  It was an all-hands lunch.
[976.86 --> 981.98]  And the next thing we know, we just get people running in going, the internet's down.
[982.56 --> 987.28]  Because we used our own systems, and we lost everything internally at the same time.
[988.42 --> 989.82]  It was a...
[989.82 --> 990.64]  That was hard, too.
[991.12 --> 992.78]  I feel like there are many lessons there.
[993.20 --> 994.24]  There was a lot of lessons.
[994.60 --> 995.62]  What were we having for lunch?
[998.18 --> 999.20]  Lunch went cold.
[999.20 --> 1001.40]  That's scary, isn't it?
[1001.52 --> 1001.96]  But hang on.
[1002.06 --> 1005.18]  So just can you explain to someone who doesn't know what a greedy regex is?
[1005.34 --> 1006.14]  What do you mean by that?
[1006.68 --> 1007.00]  Yeah.
[1007.42 --> 1011.16]  A greedy regex, I mean, if you do something like .star, what you're saying is match any
[1011.16 --> 1012.28]  character any number of times.
[1012.36 --> 1017.36]  But if you do .star, .star, you've now exploded this any character any number of times, followed
[1017.36 --> 1019.26]  by any character any number of times.
[1019.36 --> 1021.76]  And what you're doing is you're increasing the CPU computation.
[1021.76 --> 1028.24]  You still put the same fixed input in, but what it can match is now you've doubled the
[1028.24 --> 1029.84]  possibility in just that one go.
[1030.42 --> 1031.80]  And essentially, that's what happened.
[1031.98 --> 1034.70]  But some of the inputs were web pages and web traffic.
[1035.22 --> 1037.20]  So they weren't small.
[1037.32 --> 1038.30]  They were quite large inputs.
[1038.68 --> 1040.74]  And under that condition, they consumed all the CPU.
[1041.52 --> 1045.74]  So wherever this rule was applied, and we had shipped it globally to every single website,
[1045.90 --> 1049.20]  every single bit of traffic, we fried every single machine instantly.
[1049.20 --> 1053.24]  So it was about four hours for us to recover from that.
[1053.88 --> 1056.62]  And the teams I saw, they did interesting things.
[1056.74 --> 1059.98]  We were connecting directly to machines and looking at the Prometheus on them because we
[1059.98 --> 1061.26]  had no other observability.
[1061.92 --> 1062.14]  Wow.
[1062.64 --> 1064.40]  And what was the impact of that?
[1064.54 --> 1065.66]  How many people were affected?
[1066.24 --> 1067.30]  Everything was affected.
[1067.70 --> 1069.04]  We knocked out a lot.
[1069.88 --> 1073.30]  DNS, TLS, HTTP, everything.
[1073.54 --> 1075.22]  It was one of those nightmare scenarios.
[1075.72 --> 1078.70]  And you sit there as a company, you sit there and you sort of go, what are these meteorites?
[1078.70 --> 1082.76]  The dinosaurs were made extinct by a meteorite as a company or product service offering.
[1083.06 --> 1084.82]  What's a meteorite that's going to hit us?
[1085.22 --> 1087.96]  At that company, we were hit by every meteorite we predicted.
[1088.50 --> 1089.34]  It survived.
[1089.96 --> 1093.98]  But still, on the days when they hit, it lays waste to everything.
[1094.50 --> 1095.44]  And everyone has them.
[1095.64 --> 1098.74]  The thing that you've got to realize is when you're there, you've got to sympathize with,
[1099.08 --> 1101.38]  you know, you can externally see another company go through this.
[1101.76 --> 1102.90]  They're having a bad day.
[1102.98 --> 1106.04]  And you've got to sympathize because one of those meteorites is going to hit you one day.
[1106.04 --> 1110.56]  Yeah, we see the hug-ups goes around often on social media and things.
[1110.66 --> 1114.60]  People sending their support in those difficult times.
[1115.04 --> 1119.08]  Yeah, there's a good tradition of sending cakes to each other to sort of go thinking of you.
[1119.20 --> 1119.38]  Yeah.
[1119.54 --> 1122.22]  And trying not to have your salespeople the ambulance chase.
[1122.58 --> 1123.34]  Mm-hmm.
[1123.34 --> 1128.02]  How well was your break glass procedures documented?
[1128.62 --> 1129.42]  It was pretty good.
[1129.56 --> 1134.28]  We were lucky that this happened during a London lunch hour where all of the SR team,
[1134.66 --> 1136.46]  the original SRE team were there.
[1136.78 --> 1138.56]  It's possible for a few people to break glass.
[1138.66 --> 1142.86]  They could do so in about five minutes once we actually understood what we actually had to do.
[1143.30 --> 1147.00]  It took about 20 minutes for us to gain any visibility and sort of understand,
[1147.54 --> 1149.12]  hey, it's this feature.
[1149.34 --> 1150.12]  Go turn that off.
[1150.56 --> 1151.66]  Regular expressions, huh?
[1151.66 --> 1152.90]  They're still hard.
[1153.22 --> 1154.06]  They're hard for everyone.
[1155.20 --> 1156.04]  Easy to write.
[1156.20 --> 1157.32]  Hard to understand what they're doing.
[1157.50 --> 1158.58]  Why are they called that?
[1158.76 --> 1160.90]  Because what is regular about them?
[1161.58 --> 1162.70]  That's out of my domain.
[1162.90 --> 1164.54]  I don't know if anyone's got the answer for that.
[1165.06 --> 1165.90]  No, genuinely have.
[1166.36 --> 1170.12]  I just watched a talk from Strangeloop about regular expressions.
[1170.84 --> 1172.68]  And the speaker did go into this.
[1172.70 --> 1175.10]  And I've completely forgotten what she said.
[1175.40 --> 1177.66]  But we can probably put that talk in the show notes.
[1177.66 --> 1180.22]  It was a really good one about just the history.
[1180.46 --> 1182.26]  Ken Thompson came up, which is pretty cool.
[1182.42 --> 1183.60]  I'm like, oh, I know that dude.
[1184.52 --> 1184.70]  Yeah.
[1184.78 --> 1189.34]  But no, it has to do with mathy things and finite automata and all of that.
[1190.18 --> 1190.34]  Yeah.
[1190.34 --> 1196.98]  When I was a junior, which is the closest to intern I was, I was working with a team lead.
[1197.20 --> 1199.62]  And when we deployed something together, we looked at it.
[1200.08 --> 1201.88]  And I forget what it was exactly.
[1201.98 --> 1209.46]  But this is a company that receives a lot of pings from the SDK of the many clients.
[1209.46 --> 1210.52]  And it's all real time.
[1210.52 --> 1216.74]  And if that is not logged, then the entire transaction, like flow, user flow is gone forever.
[1217.78 --> 1220.66]  And we deployed something we worked on together.
[1220.80 --> 1222.00]  We worked on it for half a day.
[1222.10 --> 1222.80]  We tested it.
[1222.86 --> 1225.66]  We did all the good practices because that's how you do with a junior, right?
[1225.72 --> 1227.12]  You want to show that you're very thorough.
[1227.26 --> 1233.92]  You go for all the tests, deploy, look at all the metrics and see that it behaves as expected.
[1234.54 --> 1236.50]  And then he went to lunch and then I stayed.
[1236.94 --> 1237.78]  Da-da-da.
[1237.78 --> 1238.78]  Da-da-da.
[1239.82 --> 1242.34]  And then I proceeded to do something else.
[1242.38 --> 1246.58]  And then suddenly a weird behavior started pinging Slack, all the monitoring channels.
[1246.74 --> 1247.36]  It's like something wrong.
[1247.44 --> 1247.94]  Something's weird.
[1248.44 --> 1254.20]  And then some of the colleagues that were there tried to see where it comes from.
[1254.90 --> 1257.80]  And we couldn't figure this out in 15 minutes.
[1257.80 --> 1263.40]  And then bravely came to the head of the DevOps team.
[1263.54 --> 1265.60]  There was no SRE team at the time.
[1265.60 --> 1267.80]  And I said, I think it's this thing that we did.
[1267.90 --> 1268.76]  Can I revert it?
[1269.18 --> 1275.08]  Nobody else, from all the other senior people that don't have another better word than brave,
[1275.14 --> 1276.20]  but I don't want to use the word brave.
[1276.52 --> 1280.44]  Nobody else wanted to do anything about that because nobody was sure.
[1280.54 --> 1282.44]  And then I was like, let's do this.
[1282.52 --> 1283.46]  Let's try it worse.
[1283.68 --> 1285.34]  It cannot get much worse than that, right?
[1285.50 --> 1287.38]  And reverting that indeed succeeded.
[1287.54 --> 1288.66]  And then we were all very happy.
[1288.66 --> 1290.42]  And then I was like, I think I know how to fix it.
[1290.48 --> 1290.94]  Can I try?
[1291.04 --> 1292.54]  And then he looked at me and said, no.
[1293.66 --> 1294.44]  Stay away.
[1297.36 --> 1299.10]  I went to the next level of brave.
[1299.44 --> 1299.76]  Yeah.
[1300.02 --> 1302.54]  Well, what a great way to learn stuff though, isn't it?
[1303.66 --> 1304.20]  Break them.
[1304.42 --> 1304.54]  Yeah.
[1305.20 --> 1308.32]  How often does that memory come back to haunt you, Natalie?
[1309.14 --> 1310.62]  Every time I'm asked to please.
[1311.02 --> 1311.24]  Yeah.
[1312.36 --> 1315.16]  Every time I get to speak with other junior people.
[1315.16 --> 1318.06]  So to give the good example of it, obviously you will break something.
[1318.42 --> 1320.90]  So be reasonable about your expectations.
[1322.52 --> 1322.88]  Nice.
[1323.06 --> 1327.18]  I'm curious if you have a way, like now that you're older and wiser and, you know,
[1327.20 --> 1329.08]  you've been through the experience, which is a great teacher.
[1329.44 --> 1334.72]  I'm wondering, do you have strategies now for doing things that are scary,
[1334.90 --> 1335.92]  that could break things?
[1335.92 --> 1337.94]  Like, do you have a strategy for tackling that now?
[1338.34 --> 1341.00]  The thing is we did everything right at the time, right?
[1341.00 --> 1343.66]  So we did all the tests we could think of.
[1343.66 --> 1348.86]  We thought, what do we expect in the logs and the monitoring and the dashboard?
[1349.26 --> 1350.02]  And we observed.
[1350.62 --> 1353.36]  So the only thing that I would do different is not to plot it for lunch.
[1356.42 --> 1358.58]  So you can, I guess, observe for longer.
[1359.56 --> 1360.94]  Speaking of spooky things, right?
[1361.16 --> 1362.22]  What are we having for lunch?
[1362.96 --> 1363.18]  Yeah.
[1363.18 --> 1364.46]  I don't think I had lunch that day.
[1364.96 --> 1368.12]  I mean, I was like gnashing stuff, but I don't think I had a lunch lunch.
[1368.30 --> 1368.48]  Yeah.
[1368.50 --> 1370.98]  There's another theme emerging here.
[1370.98 --> 1375.54]  One of the main reasons to write good code is so you can just have lunch.
[1376.56 --> 1377.48]  Quite a good reason.
[1377.78 --> 1379.00]  That's another thing I would do different.
[1379.14 --> 1379.90]  I would write good code.
[1380.18 --> 1380.28]  Yeah.
[1382.16 --> 1382.84]  That's optional.
[1383.20 --> 1385.02]  If you've got good tests, you don't need good code.
[1386.36 --> 1386.72]  Controversial.
[1386.72 --> 1393.14]  So to me, what I usually tell junior members of staff is to be like, look, we expect you
[1393.14 --> 1393.84]  to break things.
[1393.98 --> 1396.68]  It's just part of sort of maturing as an engineer.
[1397.04 --> 1398.76]  What is helpful, right?
[1398.88 --> 1402.62]  And even if you follow the, you know, the playbooks and you do the right things and everything
[1402.62 --> 1404.60]  else, you know, sometimes things will go wrong.
[1404.70 --> 1408.20]  Whoever writes these things, how many people have touched the documentation you're looking
[1408.20 --> 1408.40]  at?
[1408.40 --> 1412.12]  There's a chance that they might have overlooked something or they take something for granted
[1412.12 --> 1414.34]  that you as a junior haven't encountered yet.
[1414.34 --> 1415.40]  So you don't take it for granted.
[1415.54 --> 1416.56]  So there's some steps in between.
[1416.64 --> 1418.94]  So there's some unwritten things in between the lines, right?
[1418.98 --> 1423.82]  That are sort of being conveyed that you have not yet matured enough to kind of pick up on.
[1424.08 --> 1425.94]  So just document every step you take.
[1426.44 --> 1429.34]  It's much easier for the team to go back and say, okay, what?
[1429.54 --> 1432.48]  Because the first thing they're going to say is ask you, what did you do?
[1433.90 --> 1438.12]  You know, so after everybody comes down and you can say that, well, these are the steps
[1438.12 --> 1438.38]  I took.
[1438.50 --> 1441.96]  I mean, and that means, you know, literally like even to this day, I do this, right?
[1441.96 --> 1445.52]  If I'm working with a system that I haven't come across before and I don't know what the
[1445.52 --> 1449.12]  side effects are of the things that I'm going to do, I'll literally like in a document
[1449.12 --> 1453.88]  somewhere, literally be copying the commands that I'm issuing the command line, right?
[1453.88 --> 1457.50]  I'm literally going to copy them into this doc and I'm basically, I'm capturing the output,
[1457.58 --> 1457.72]  right?
[1457.74 --> 1458.30]  As I go.
[1458.88 --> 1460.90]  Now, one could say that's sort of extreme.
[1461.38 --> 1464.48]  I mean, again, if there was a playbook for it, if there was some automation, I could just
[1464.48 --> 1467.02]  click the button or it should have come in and let it do its thing.
[1467.02 --> 1471.54]  But if I have to, you know, do this step-by-step thing, that means there's no playbook for it.
[1471.58 --> 1472.62]  That means there's no automation.
[1472.76 --> 1473.58]  There's no script, whatever it is.
[1473.62 --> 1477.06]  So I'm just going to be literally documented what I'm doing step-by-step-by-step.
[1477.12 --> 1479.14]  And if something breaks, I know exactly what broke.
[1479.62 --> 1483.52]  Or if I can't tell what broke, I can ask my team and say, hey, these are the steps I was
[1483.52 --> 1483.84]  following.
[1484.42 --> 1484.52]  Right?
[1484.58 --> 1487.38]  And then nine times out of 10, maybe I'm just lucky.
[1487.78 --> 1491.02]  They'll be like, oh, yeah, this thing you should have done, this command before, you know,
[1491.04 --> 1491.74]  you do this, whatever.
[1491.86 --> 1493.22]  And then we find out, right?
[1493.74 --> 1497.32]  There's a gap in the documentation or a gap in the process or something like that, right?
[1497.60 --> 1497.78]  Yeah.
[1497.78 --> 1498.74]  And you can update it.
[1499.06 --> 1499.22]  Yeah.
[1499.30 --> 1503.38]  So by literally just track what you're doing, that may actually end up helping you.
[1503.44 --> 1504.28]  Hey, guess what?
[1504.34 --> 1507.82]  That might even turn into a playbook or an opportunity for automation for whatever it is that you're
[1507.82 --> 1508.20]  working on.
[1508.56 --> 1508.76]  Yeah.
[1508.80 --> 1508.98]  Yeah.
[1508.98 --> 1510.68]  It's like step one, SSH in.
[1510.98 --> 1512.84]  Step two, check the Go version.
[1512.84 --> 1515.24]  Step three, drop all the database tables.
[1516.34 --> 1516.66]  Whip.
[1517.16 --> 1518.12]  Spot the problem.
[1519.10 --> 1519.96]  It's just pen testing.
[1520.16 --> 1520.36]  It's fine.
[1520.42 --> 1520.70]  Exactly.
[1520.80 --> 1520.94]  Yeah.
[1521.02 --> 1523.18]  You shouldn't be able to do that, really, if you can do that.
[1523.18 --> 1526.52]  I think that's important, though, that they've taken steps because it helps with something
[1526.52 --> 1526.80]  else.
[1526.90 --> 1529.72]  It helps people admit that they've possibly done something.
[1530.20 --> 1534.76]  Who in that early career has got the courage to say, I've mucked up, right?
[1535.18 --> 1537.26]  I potentially have lost you money or time.
[1537.60 --> 1538.64]  Most people are terrified.
[1539.08 --> 1542.04]  And you're terrified legitimately because you've got no experience in the industry.
[1542.12 --> 1542.68]  You're brand new.
[1543.12 --> 1545.04]  You're finally being paid to do something.
[1545.16 --> 1546.44]  And you think you're not very good.
[1546.62 --> 1546.78]  How?
[1546.78 --> 1549.50]  Well, we're long in our career and we probably think we're not very good.
[1549.86 --> 1551.20]  So early career, you're crushed.
[1551.52 --> 1554.66]  And that ability to turn around and go, that might have been me.
[1555.24 --> 1556.48]  I think I did that.
[1556.78 --> 1558.18]  I pressed this button and then it broke.
[1558.90 --> 1559.72]  That's tough.
[1560.26 --> 1560.40]  Yeah.
[1560.62 --> 1564.28]  Well, I think that speaks to the blameless culture that's important.
[1564.28 --> 1571.14]  It's important to reach the point where people aren't punished for these mistakes because the
[1571.14 --> 1576.46]  last thing you want is people, like you say, they bury it, they try and hide it or just
[1576.46 --> 1579.66]  don't tell anybody, which could make the problem much worse.
[1579.90 --> 1582.52]  So yeah, I think that culture plays a big part, doesn't it?
[1583.06 --> 1583.24]  Yeah.
[1583.38 --> 1585.44]  Should always blame systems and not people.
[1585.80 --> 1585.98]  Yeah.
[1586.32 --> 1587.16]  Something went wrong.
[1587.24 --> 1588.28]  It's not the person's fault.
[1588.44 --> 1590.98]  It's why did the system allow the person to do that?
[1591.12 --> 1591.38]  Right.
[1591.38 --> 1597.66]  So like if when Johnny says something that's mean to me, it's not Johnny that I've complained
[1597.66 --> 1597.94]  about.
[1598.06 --> 1601.56]  It's the system that lets Johnny get on a podcast and be horrible to me.
[1603.00 --> 1603.44]  Exactly.
[1604.04 --> 1606.36]  It's part of the system to be mean to you, Matt.
[1606.48 --> 1607.02]  Don't you know?
[1607.38 --> 1607.70]  Indeed.
[1609.16 --> 1609.80]  Oh yeah.
[1609.94 --> 1611.30]  It feels like it sometimes.
[1621.38 --> 1628.80]  Hey friends, this episode is brought to you by my friends and potentially your friends
[1628.80 --> 1630.02]  too at FireHydrant.
[1630.22 --> 1634.14]  And I'm here with Robert Ross, founder and CEO of FireHydrant.
[1634.28 --> 1639.32]  And Robert, there are several options out there for incident management, but what is it that
[1639.32 --> 1640.82]  makes FireHydrant different?
[1640.82 --> 1645.64]  The reason that we think that FireHydrant is on to something is because we're meeting
[1645.64 --> 1647.16]  companies really where they are.
[1647.44 --> 1652.56]  We face the same problems that every company in the industry that is building and releasing
[1652.56 --> 1654.42]  software is also facing.
[1654.80 --> 1659.68]  So where you want people to be able to sign up for FireHydrant and immediately be able
[1659.68 --> 1665.60]  to kick off an incident using the best practices that we've built and we've experienced and have
[1665.60 --> 1668.16]  gathered through the other amazing customers that use our tool.
[1668.16 --> 1673.26]  It really is a very quick time to value and we want people to have a long jump from where
[1673.26 --> 1676.72]  they are to where they want to be in incident management.
[1677.30 --> 1677.60]  I love it.
[1677.66 --> 1678.20]  Thank you, Robert.
[1678.48 --> 1683.60]  Small teams up to 10 people can get started for free with all FireHydrant features included.
[1683.74 --> 1685.46]  There's no credit card required to sign up.
[1685.80 --> 1687.48]  They are making it too easy to get started.
[1687.68 --> 1690.38]  So check them out at FireHydrant.com.
[1690.38 --> 1693.00]  Again, FireHydrant.com.
[1698.16 --> 1714.06]  Have we got any more horror stories?
[1714.30 --> 1717.26]  Oh, by the way, this campfire's warm, isn't it?
[1717.26 --> 1720.50]  So we'll probably put an effect of a campfire over the top.
[1720.78 --> 1723.02]  So just pretend we're all gathered around a campfire.
[1723.12 --> 1724.46]  Oh, what do you think of the campfire, Johnny?
[1725.12 --> 1725.42]  Sure.
[1725.42 --> 1725.86]  Yeah.
[1726.08 --> 1726.34]  Yeah.
[1726.56 --> 1727.04]  That's how about it.
[1727.76 --> 1729.24]  I'm convinced by that performance, Johnny.
[1730.08 --> 1731.84]  Have you done actual theater?
[1732.00 --> 1732.10]  Have you?
[1732.20 --> 1733.88]  Because what about you, Chris?
[1734.14 --> 1735.06]  What do you think of the fire?
[1735.20 --> 1735.98]  It's cozy, isn't it?
[1736.54 --> 1736.86]  Sure.
[1737.82 --> 1738.14]  Okay.
[1739.38 --> 1740.36]  Crackly warm fire.
[1740.48 --> 1742.14]  We don't have any marshmallows, so it's not as good.
[1742.20 --> 1742.50]  Don't we?
[1742.62 --> 1743.48]  It's imaginary land.
[1743.68 --> 1744.44]  It's podcast land.
[1744.78 --> 1745.56]  You can have anything you want.
[1745.62 --> 1746.16]  Check this out.
[1746.24 --> 1746.72]  What's this?
[1746.84 --> 1747.10]  Look.
[1747.34 --> 1748.12]  Look at your face.
[1748.74 --> 1749.04]  Look.
[1749.14 --> 1749.80]  It's marshmallows.
[1750.74 --> 1751.98]  Natalie, what do you think of the fire?
[1753.34 --> 1754.58]  Shouldn't be burning servers.
[1754.58 --> 1756.24]  No, it shouldn't be burning servers.
[1756.54 --> 1759.42]  No, this is a fire that doesn't actually release any carbon.
[1759.80 --> 1760.40]  It's a good fire.
[1760.94 --> 1762.64]  It's basically my GPU over here.
[1762.64 --> 1763.02]  He's like, oh, my God.
[1765.04 --> 1766.58]  It's the sound of my cooking.
[1766.86 --> 1767.70]  It's a money fire.
[1767.86 --> 1768.60]  My electric bill.
[1769.24 --> 1770.70]  It's some old Intel Macs.
[1770.76 --> 1774.34]  You know, we just turned them on, open Slack, and now they've made us a nice fire.
[1774.50 --> 1774.92]  It's good.
[1774.92 --> 1778.96]  Just have Slack and a regular expression running.
[1779.34 --> 1781.34]  That'll generate enough heat to cook your marshmallow.
[1782.38 --> 1784.42]  And those fans can definitely fly us somewhere.
[1784.64 --> 1786.80]  We could all go visit Matt in the UK.
[1787.34 --> 1787.66]  Yeah.
[1787.94 --> 1790.72]  I mean, make sure you do go through proper passport control.
[1790.88 --> 1793.76]  Don't just fly in at any point because that's illegal.
[1793.76 --> 1796.00]  But if you, yeah, otherwise do, please visit.
[1796.08 --> 1796.90]  We'd love to have you.
[1797.52 --> 1803.22]  Yeah, I remember talking about hot CPUs, the CPU hot program that I used to have on an Amiga.
[1803.52 --> 1805.80]  And basically run it and it just made your CPU hot.
[1806.44 --> 1808.14]  And that was a program that you could have.
[1808.18 --> 1810.64]  It was on like a front of a magazine for some reason.
[1811.22 --> 1811.84]  What's that doing?
[1812.58 --> 1814.36]  Someone wrote another infinite loop.
[1814.96 --> 1815.66]  Yeah, there you go.
[1815.66 --> 1823.82]  They've turned their horror story into a big success story because they got on a magazine cover with a floppy disk.
[1825.08 --> 1825.62]  Interesting.
[1825.62 --> 1834.48]  Now with the energy costs going up here in Europe, all the heaters are becoming more expensive because people assume they will not have gas to hit their house.
[1835.24 --> 1839.36]  Many houses have this, apartment buildings have this systems with gas, right?
[1839.68 --> 1844.82]  So you buy like electrical heaters to warm the place in case you might need that.
[1845.08 --> 1846.52]  So they become really expensive.
[1846.66 --> 1849.18]  So really what you're saying is that all you need is an old computer.
[1849.36 --> 1849.60]  Yeah.
[1849.72 --> 1851.18]  Which is probably cheaper at this point.
[1851.18 --> 1854.52]  I bet we see a spike in the downloads of Slack in that area.
[1854.52 --> 1857.22]  Or that CPU hot.
[1857.62 --> 1859.90]  How many Electron apps can I install on one machine?
[1861.52 --> 1861.92]  Okay.
[1862.04 --> 1865.44]  Has anybody got any other horror stories?
[1866.84 --> 1867.32]  I've got more.
[1867.52 --> 1870.02]  I've got one which is something that's kind of triggering.
[1870.26 --> 1872.92]  I don't know if anyone else has got sort of triggers from being horrified.
[1873.30 --> 1877.28]  One of my old bosses used to come to me and if he started the sentence with,
[1877.28 --> 1878.64]  what do you know about?
[1879.16 --> 1881.24]  Then I knew immediately it was downhill.
[1881.70 --> 1883.92]  It's like, what do you know about Perl?
[1884.12 --> 1885.84]  It's like, oh, where's this going?
[1886.32 --> 1889.32]  Or what do you know about directory services and exchange?
[1889.44 --> 1891.62]  It's like, um, that they exist?
[1891.82 --> 1892.56]  Great, you'll do.
[1893.00 --> 1894.92]  And off you'll be shipped to a client site.
[1895.38 --> 1899.50]  And I ended up at one of these client sites and there was a customer and it was a big,
[1899.68 --> 1900.44]  big company.
[1900.80 --> 1902.28]  And they were basically doing a split.
[1902.92 --> 1904.84]  Merger and acquisition is the normal thing you hear about.
[1904.92 --> 1905.62]  They're doing the other thing.
[1905.72 --> 1906.58]  They're splitting in two.
[1907.42 --> 1912.00]  And they basically said, they contracted the company I worked for to split their active
[1912.00 --> 1916.20]  directory, to clone it and then rename it to the other company name.
[1916.28 --> 1917.96]  So they had a perfect copy renamed.
[1918.28 --> 1920.20]  And I'm just like, turn up on site.
[1920.32 --> 1922.92]  I know a bit of visual basic, a little bit of C sharp at that point.
[1923.24 --> 1924.72]  How do I approach this problem?
[1925.16 --> 1926.54]  I did not know at all.
[1926.70 --> 1930.34]  So I get in touch with Microsoft Professional Services and go, how would you do this?
[1930.34 --> 1931.44]  And they're like, you don't.
[1931.48 --> 1932.06]  That's impossible.
[1932.86 --> 1933.54]  Don't do that.
[1933.82 --> 1937.04]  That's reckless and foolish and it's not supported.
[1937.48 --> 1939.80]  And it's like, okay, but I'm being paid for this.
[1939.88 --> 1944.00]  And I know no better because I'm barely in my mid twenties and I'm going to take a stab
[1944.00 --> 1944.36]  at this.
[1944.60 --> 1949.24]  And I wrote a script going through the registry on the, uh, one of the cloned exchange server
[1949.24 --> 1949.64]  machines.
[1949.80 --> 1954.26]  And I basically renamed everything and I fired it up afterwards and it worked.
[1954.86 --> 1955.26]  Wow.
[1955.48 --> 1956.46]  That was my day's work done.
[1956.46 --> 1957.14]  I left.
[1957.14 --> 1958.94]  I have no idea whether that worked.
[1961.04 --> 1961.92]  It appeared to work.
[1962.12 --> 1965.16]  Oh, well, I just took notice exactly after this project ended.
[1965.52 --> 1966.08]  Oh, I don't know.
[1966.14 --> 1966.70]  I don't want to know.
[1968.60 --> 1969.64]  They rate contractors.
[1969.78 --> 1970.40]  That's what you get.
[1971.50 --> 1971.86]  Wow.
[1972.56 --> 1973.96]  That could have just worked though.
[1974.30 --> 1976.94]  But you know, I never trust code that works first time.
[1977.02 --> 1978.92]  That's why I like a failing test before.
[1979.26 --> 1981.54]  The only thing that I was really, really scared about it.
[1981.60 --> 1984.20]  The name of the company in the Active Directory was six characters long.
[1984.20 --> 1987.66]  And I was reasonably sure that that was a magic value.
[1988.16 --> 1991.52]  So I asked them for a new name to be the Active Directory name.
[1991.64 --> 1993.18]  That was also six characters long.
[1993.42 --> 1996.94]  That's the only thing that I think was intelligent about what I did that day.
[1997.72 --> 1998.98]  The rest is luck.
[1999.54 --> 2000.46]  And lots of regexes.
[2001.60 --> 2002.04]  Again.
[2002.68 --> 2003.08]  Yeah.
[2003.60 --> 2004.30]  Good call.
[2005.56 --> 2006.00]  Spooky.
[2006.58 --> 2007.06]  Spoopy.
[2007.56 --> 2008.04]  Spoopy.
[2008.28 --> 2010.70]  But yeah, that's the scary question though.
[2010.74 --> 2011.76]  No one's asked me that for years.
[2012.10 --> 2013.06]  Hey, what do you know about?
[2015.06 --> 2015.38]  Yeah.
[2015.42 --> 2016.04]  What do you know about this?
[2016.08 --> 2017.16]  You're like, no, you're like, nothing.
[2017.32 --> 2017.56]  Nothing.
[2017.68 --> 2018.16]  Nothing at all.
[2018.40 --> 2019.70]  I don't want to know anything about it.
[2019.78 --> 2019.98]  Yeah.
[2020.62 --> 2021.40]  I know nothing.
[2021.64 --> 2022.62]  Maybe that's the thing, right?
[2022.62 --> 2024.90]  When you see people late in their career and you're just like,
[2024.92 --> 2025.64]  what do you know about this?
[2025.70 --> 2028.72]  And you think they're doing the, I've forgotten more than you'll ever learn.
[2028.84 --> 2030.80]  But no, they're actually going, I don't want to do this.
[2032.48 --> 2033.20]  Active Directory.
[2033.84 --> 2034.66]  Never heard of it, mate.
[2034.66 --> 2035.52]  Never heard of him.
[2035.86 --> 2037.42]  Thinks it's someone man's name.
[2038.34 --> 2039.12]  Active Directory.
[2039.24 --> 2040.46]  That's a weird name for a man.
[2040.66 --> 2041.58]  I think that's a man.
[2042.18 --> 2045.00]  Just really selling, you know, that you don't know it just to get out of the job.
[2045.26 --> 2047.60]  Well, just a tip there for people that want to get into that.
[2047.96 --> 2049.46]  Like I said, I'm jet lagged.
[2050.24 --> 2052.42]  And this is spooky Halloween party special.
[2052.98 --> 2054.78]  How are those marshmallows looking, Chris?
[2055.38 --> 2057.64]  They are toasty and brown and delicious.
[2058.34 --> 2058.90]  Oh, perfect.
[2059.10 --> 2059.50]  Well done.
[2060.18 --> 2061.98]  Are you going to share or?
[2062.82 --> 2063.22]  No.
[2063.42 --> 2063.68]  No.
[2063.68 --> 2066.84]  These are my marshmallows now.
[2066.84 --> 2067.02]  Good point, yeah.
[2067.72 --> 2068.00]  Yeah.
[2068.14 --> 2073.64]  I know they're imaginary, but, you know, but I still want one.
[2074.12 --> 2075.14]  We have an infinite supply.
[2075.26 --> 2076.58]  Everybody can make their own marshmallows.
[2077.40 --> 2077.76]  Oh, yeah.
[2077.88 --> 2078.14]  Okay.
[2078.14 --> 2080.32]  All you need is an infinite loop.
[2080.76 --> 2082.46]  Speaking of loops, I have a scary story.
[2082.46 --> 2097.22]  But if that's really a story that I think helped me gain a new appreciation for sort of how to integrate systems, how distributed systems have sort of pitfalls.
[2097.22 --> 2104.84]  It's a tradeoff for everything and all the things that we value, right, as best practices for dealing with, you know, integrating systems.
[2104.84 --> 2117.28]  So I was working for an organization, that very awesome organization, a nonprofit, which basically helps students, right, especially in underserved communities, sort of prepare to take sort of standardized testing and that kind of thing.
[2117.28 --> 2126.46]  So for months leading up to a major sort of testing day, right, students are going to come, sit down into their classrooms.
[2126.78 --> 2132.16]  They're going to be logging in and taking an assessment, right, to help them, right, with the real things.
[2132.40 --> 2136.94]  And this is like a coordination across multiple schools and everything.
[2137.02 --> 2138.84]  So the whole county, right, is doing this thing.
[2138.88 --> 2144.62]  So we're talking like, you know, maybe like 3,000 to 4,000 students, right, that are going to all sit down and do this thing.
[2144.92 --> 2145.02]  Wow.
[2145.02 --> 2152.06]  And basically I'm part of the team that's basically has been working on this sort of integration, right, for months now, right?
[2152.12 --> 2154.24]  We have different systems talking to each other and everything else.
[2154.82 --> 2157.98]  In development and even in staging, everything works perfectly.
[2159.32 --> 2163.04]  Systems can talk to each other, you know, like we're sending, you know, lots of traffic.
[2163.18 --> 2167.90]  We're keeping an eye on things and we're observing to the best availability, you know, with the tools that we have.
[2168.50 --> 2174.00]  And on production day, basically, which is when students actually sit down to do the thing,
[2174.00 --> 2183.12]  what we didn't test against is basically having roughly 4,000 students trying to log in to the system at the same time.
[2185.66 --> 2190.86]  You know, and because you have these systems that are talking to each other for authentication and pooling things, whatever it is,
[2190.94 --> 2194.22]  basically we just had a thundering herd kind of situation happening.
[2194.22 --> 2201.04]  And we didn't account for that because all of our tests, even our integration tests and everything else, they didn't factor in that kind of scale.
[2201.38 --> 2204.74]  And I take responsibility for that because I was one of the team leads.
[2204.88 --> 2212.20]  And basically one of my questions was supposed to be, what is the expected number of users and clients, right, on the system?
[2212.20 --> 2219.30]  And basically we touched on these things, but there were bottlenecks in the system, right, that we should have better accounted for.
[2219.74 --> 2226.68]  And thankfully we had enough of an understanding of what was happening with enough observability to be like, oh, crap, we know where the bottleneck is.
[2226.72 --> 2227.64]  We need to go do this, whatever.
[2227.82 --> 2233.14]  So within a matter of, you know, about an hour and a half or so, while students are waiting there,
[2233.14 --> 2236.32]  because they can't really dismiss everybody and send everybody home, right?
[2236.36 --> 2242.34]  We're talking like countywide, 4,000 plus students, all this coordination across months, you know.
[2242.64 --> 2248.18]  To me, this remains the best and worst moment of my career because I'm like, here I am.
[2248.30 --> 2249.96]  I'm supposed to be serving these kids.
[2249.96 --> 2255.60]  Like as an, often we are so far removed from the consequences of our code, right, good or bad, right?
[2255.62 --> 2256.68]  We're so far removed from it.
[2256.76 --> 2263.00]  But here I am, I knew exactly, right, what the impact that my mistake was having on these kids.
[2263.14 --> 2263.34]  Right.
[2263.36 --> 2266.56]  And they already, right, have been given a short straw in life.
[2266.60 --> 2268.58]  And here I am just making that worse, right?
[2268.94 --> 2271.68]  So after that incident, I was like, never again.
[2271.72 --> 2272.86]  Like, what do I need to do?
[2272.96 --> 2273.98]  What do I need to learn?
[2274.16 --> 2275.30]  Who do I need to talk to?
[2275.70 --> 2277.76]  Like it was, I had to level up.
[2277.76 --> 2283.64]  At any point in my career, I can't remember a single incident that has driven me to level up as much as this one.
[2283.74 --> 2286.00]  Because the impact was so real.
[2286.18 --> 2287.84]  It was so in my face.
[2287.96 --> 2288.88]  It's just undeniable.
[2290.18 --> 2290.72]  That was scary.
[2290.72 --> 2294.68]  That is the $1,001 bill.
[2296.00 --> 2296.78]  Yeah, that's a face.
[2296.98 --> 2299.60]  Listen, I would have gladly like handed over $1,000.
[2300.10 --> 2301.26]  Like out of my pocket.
[2301.50 --> 2303.30]  Like to be like, look, whatever this is.
[2303.34 --> 2303.88]  To the kids.
[2304.02 --> 2305.26]  Make it go away right now.
[2305.28 --> 2306.02]  Just give it to the kids.
[2306.12 --> 2306.44]  To the kids.
[2307.64 --> 2308.00]  Right.
[2308.56 --> 2310.40]  Uncle Johnny's messed up again.
[2310.54 --> 2312.94]  Come and collect your $20 bills, everyone.
[2313.54 --> 2316.68]  No college for you, but here's some, I don't know.
[2316.78 --> 2317.60]  Yeah, that's horrific.
[2317.60 --> 2324.04]  Well, yeah, but when the stakes are that high, Johnny, like that is like, ooh, that is scary.
[2324.44 --> 2324.62]  Yeah.
[2324.86 --> 2325.08]  Yeah.
[2325.18 --> 2326.50]  And you feel awful.
[2326.74 --> 2331.04]  Like awful, awful, awful for being responsible for that.
[2331.26 --> 2331.48]  Oof.
[2331.48 --> 2332.02]  Mm-hmm.
[2332.90 --> 2337.12]  What do you think about sort of engineers sort of being, having that sort of sense of consequence?
[2337.42 --> 2338.88]  Because it comes in multiple directions.
[2339.04 --> 2343.34]  You get salespeople going, if you don't do this, we're going to lose a million dollar deal.
[2343.52 --> 2345.62]  It's not like the engineer is going to receive a million dollars, right?
[2345.64 --> 2346.96]  They're just going to get their normal salary.
[2347.12 --> 2348.18]  They're getting the normal pay.
[2348.72 --> 2350.12]  That's a little bit abstract.
[2350.28 --> 2351.04]  It's a ton of stress.
[2351.04 --> 2351.60]  Mm-hmm.
[2351.60 --> 2355.60]  And likewise, when you're working incidents, you know, someone will turn and go, it's affected
[2355.60 --> 2360.74]  this air traffic control signal, or it's affected this sort of kids or hospital, or traffic
[2360.74 --> 2361.92]  lights are down, or whatever.
[2362.66 --> 2364.04]  Kind of unhealthy, isn't it?
[2364.52 --> 2370.02]  It's like, we've got to keep it abstract enough that, because I get that it changes us.
[2370.38 --> 2372.32]  All of those incidents changed all of us.
[2372.64 --> 2373.82]  They're all horrifying moments.
[2373.82 --> 2378.52]  But I'm also just like, that's the path to burnout, to sort of accepting the consequence
[2378.52 --> 2379.66]  for all of these things.
[2379.92 --> 2380.02]  Yeah.
[2380.16 --> 2384.90]  So some value in being somewhat abstracted from the consequences.
[2385.18 --> 2385.58]  Is that what you mean?
[2385.88 --> 2386.20]  Yeah.
[2386.48 --> 2389.66]  If you consider it too much, it just weighs so heavily.
[2389.88 --> 2390.80]  It's too serious.
[2390.96 --> 2392.04]  It's too much of a...
[2392.04 --> 2395.26]  And the things you need to do to actually get out of those situations, they become even
[2395.26 --> 2396.46]  more horrifying and scary.
[2396.70 --> 2398.02]  What if I prolong this?
[2398.10 --> 2399.28]  What if I make it worse?
[2399.28 --> 2402.08]  And sometimes you've just got to be a bit fearless.
[2402.08 --> 2406.48]  And you can't if you've got that sort of burden on you that we put on ourselves.
[2406.98 --> 2409.64]  I feel like this is where systems can be helpful, though.
[2409.72 --> 2414.94]  Because I think we, as an industry, are pretty bad at understanding that there can be bad
[2414.94 --> 2415.44]  consequences.
[2415.44 --> 2416.94]  It's like something terrible happens.
[2417.02 --> 2419.28]  And we're like, oh no, this terrible thing happened.
[2419.38 --> 2422.08]  But so much of the time, that terrible thing was completely predictable.
[2422.74 --> 2426.50]  And we just didn't predict it because we thought it'd go fine.
[2427.08 --> 2428.18]  Like I worked for a lifeguard.
[2428.36 --> 2429.70]  When I was younger, I worked as a lifeguard.
[2429.70 --> 2434.60]  I remember one of the things that we always did is we trained a lot, but also did a lot
[2434.60 --> 2437.50]  to make sure that the environment was always a safe one.
[2438.08 --> 2439.12]  So it was like, we did a lot of...
[2439.12 --> 2441.14]  That's why lifeguards yell at people so much.
[2441.26 --> 2442.04]  And they're like, don't run.
[2442.22 --> 2445.02]  Don't do these things that might result in you getting injured.
[2445.50 --> 2448.40]  I kind of feel like in software engineering, we just let people do whatever.
[2448.74 --> 2452.02]  And then people slip and bash their head and they're bleeding all over the place.
[2452.08 --> 2453.44]  And we're like, oh no, how did this happen?
[2453.56 --> 2458.78]  And it's like, well, not only did we not tell people not to run, but we also left giant puddles
[2458.78 --> 2462.40]  of water on the floor because we didn't put down the proper mats to make sure that even
[2462.40 --> 2463.92]  if they are running, they can do it safely.
[2464.16 --> 2467.82]  There's all these other things that you have to set up as precautions that I feel like in
[2467.82 --> 2469.96]  software engineering, we just kind of don't do.
[2470.04 --> 2474.96]  And part of me wonders if we don't do that because there aren't enough consequences flowing
[2474.96 --> 2476.16]  down to the engineers.
[2476.16 --> 2481.78]  I feel like the number of times I've been at companies that I've worked at banks and
[2481.78 --> 2484.46]  people have been like, well, you know, this isn't like life or death.
[2484.62 --> 2488.12]  And I'm like, this is affecting people's money and their livelihood.
[2488.56 --> 2489.72]  Like, what do you mean?
[2490.50 --> 2494.04]  And that's always a thing that gets rolled out is if it's like, oh, well, we're not doing
[2494.04 --> 2495.14]  things that could kill people.
[2495.28 --> 2498.02]  It's like, well, we're doing things that can substantially affect people's lives.
[2498.24 --> 2501.00]  And I feel like we have to take that into account.
[2501.00 --> 2505.32]  Because when we don't, we do lots of immoral things like run psychological experiments
[2505.32 --> 2508.22]  on people without their knowledge and other terrible things.
[2508.22 --> 2510.48]  Because we're like, ah, what's the harm?
[2510.64 --> 2511.84]  I haven't done that for weeks.
[2512.00 --> 2513.04]  I don't know why you're bringing it up.
[2515.08 --> 2515.92]  It's spooky.
[2516.84 --> 2518.08]  It's a spooky show.
[2525.02 --> 2526.78]  I have a spooky story, I think.
[2527.02 --> 2527.98]  It feels spooky.
[2527.98 --> 2530.92]  So I'd recently joined this company.
[2531.94 --> 2535.28]  And of course, because it's the modern day, they're using Kubernetes.
[2536.24 --> 2538.44]  And of course, they're using all the shiny things of Kubernetes.
[2538.60 --> 2539.46]  They're also using Istio.
[2540.10 --> 2541.56]  No one actually knows how any of this works.
[2541.62 --> 2543.92]  It's just like, oh, this is what we're supposed to be using.
[2544.08 --> 2547.98]  So we have this big old cluster and it's running and our DevOps people are pulling their hair
[2547.98 --> 2549.04]  out because I hate all of this.
[2549.52 --> 2552.08]  And I start reading through the code base and looking at things.
[2552.18 --> 2555.22]  And I'm like, okay, these auth policies look a little funky.
[2555.22 --> 2559.70]  And then I go talk to people and they're like, we don't really have any auth policies.
[2560.12 --> 2561.90]  Everything's just kind of open right now.
[2562.38 --> 2564.08]  Everything in the back end, you just talk to each other.
[2564.16 --> 2564.98]  There's no auth policies.
[2565.14 --> 2566.96]  And I'm like, are you sure?
[2567.04 --> 2568.92]  Because I see these auth policies in the code base.
[2569.00 --> 2571.32]  They're like, yeah, but we don't think they're being used for anything.
[2571.46 --> 2572.58]  And I was like, okay.
[2572.86 --> 2575.12]  So I just kind of let it go and go about my business.
[2575.26 --> 2576.92]  And then I have a few more of these conversations.
[2577.16 --> 2578.84]  And I'm like, this feels weird.
[2578.96 --> 2580.86]  But all these people know more than I do.
[2580.86 --> 2590.56]  And then months and months later, someone stumbles across this one auth policy that has no labels and no access rules.
[2591.24 --> 2596.34]  Which in Istio language means that it applies to literally everything and allows all traffic in.
[2597.06 --> 2605.86]  So this one policy had just opened our entire API, including the public API, to the entire internet for anybody to do anything without needing any authorization.
[2605.86 --> 2610.76]  You just needed a JSON web token that you could easily get from anywhere.
[2611.72 --> 2614.22]  And I was just like, so it caused all these problems, right?
[2614.68 --> 2615.64]  Everybody's freaking out.
[2616.14 --> 2617.98]  And then they just ripped that policy out.
[2618.06 --> 2619.98]  And they're like, okay, well, without this policy would be fine.
[2620.18 --> 2624.48]  But then all of those auth policies that had been sitting there that I was like, these look funky.
[2624.70 --> 2625.84]  All those took over.
[2626.00 --> 2627.22]  And all of those were broken.
[2627.62 --> 2629.36]  So then it broke all the APIs.
[2629.36 --> 2637.98]  So then they had to put the other policy back and then go through and go find every single auth policy within Istio and then fix all of those auth policies.
[2638.66 --> 2643.38]  And then they could finally remove that one policy that was opening everything to the world.
[2643.50 --> 2646.98]  And I think the total amount of time that the door was just open was about nine months.
[2648.02 --> 2651.32]  And to the knowledge that people have, nothing bad happened.
[2651.98 --> 2654.70]  But yeah, it was quite horrifying.
[2655.42 --> 2658.76]  That is still a security incident requiring disclosure, I'm afraid.
[2658.76 --> 2659.12]  Yeah.
[2659.72 --> 2660.24]  I know.
[2660.34 --> 2661.86]  I'm just like, is this disclosure?
[2664.00 --> 2665.24]  No, it was, yeah.
[2665.32 --> 2666.80]  I was like, oh, oh no.
[2667.28 --> 2671.44]  It taught me a lesson that like when I see funky things, I should probably bring them up a little bit soon.
[2671.52 --> 2672.90]  It's like, no, that policy is there.
[2672.94 --> 2675.30]  And that policy definitely doesn't work.
[2675.88 --> 2681.12]  And some of the broken things were like some YAML white spacing thing where it's like something was tabbed in a little too far.
[2681.16 --> 2684.84]  And then people were just copying and pasting these policies and then not testing them,
[2684.84 --> 2690.88]  which was like another thing that we had to go back and be like, please test the things that you put into the code base.
[2691.20 --> 2691.76]  Pretty please.
[2691.86 --> 2692.20]  Thank you.
[2692.40 --> 2692.48]  Yeah.
[2692.54 --> 2699.54]  I think that also is a bit of a lesson is if there are bits of code and you're like, no, yeah, but that doesn't do anything now.
[2699.62 --> 2702.20]  Like that used to be doing something and now it doesn't.
[2702.20 --> 2704.68]  It's like either take it out.
[2705.00 --> 2707.18]  If it's really not doing something, get rid of it.
[2707.34 --> 2707.60]  Prove it.
[2708.00 --> 2708.32]  Exactly.
[2708.48 --> 2709.78]  It probably is doing something.
[2710.28 --> 2713.56]  And if it isn't, maybe it should be like in your case, Chris.
[2713.80 --> 2714.08]  Yeah.
[2714.72 --> 2715.36]  Spoopy.
[2715.78 --> 2716.92]  The zombie apocalypse.
[2717.30 --> 2717.56]  Yeah.
[2718.94 --> 2720.62]  Will be caused by Istio.
[2722.84 --> 2725.82]  Zombie code just haunting us.
[2726.18 --> 2728.04]  I'm never sure what's worse than those things.
[2728.04 --> 2733.52]  Like the insecure environment where we're just like nothing applies or the extremely secure environment.
[2733.74 --> 2736.72]  I've seen some where they've been really locked down and like everything.
[2736.88 --> 2741.02]  You've got an IP firewall for everything and you're like, I have total confidence.
[2741.62 --> 2744.54]  And then mysteriously API calls between machines just didn't work.
[2744.80 --> 2746.54]  We're just like, why not?
[2746.98 --> 2750.30]  And what we realized, the debugging for this went wild.
[2750.38 --> 2751.16]  It went really low.
[2751.60 --> 2755.40]  And we were down at Wireshark and we're watching what's going on and we're watching what's going on inside the kernel.
[2755.40 --> 2759.66]  But we were turning on contract connection tracking.
[2760.00 --> 2760.96]  And this is in TCP.
[2761.28 --> 2766.80]  It's got little tables, state tables and network there to keep track of the sort of TCP connections.
[2766.94 --> 2768.14]  But you can overflow these tables.
[2768.28 --> 2769.32]  We were turning them on and off.
[2769.76 --> 2775.78]  And every time we turned them on and off, we were toggling which IP firewall rules were actually matching or not.
[2776.12 --> 2781.10]  So we were taking existing connections and then just randomly dropping them every time we flipped these things.
[2781.42 --> 2782.66]  But we could never observe it.
[2782.66 --> 2785.74]  And we were just there the whole time just going, we lost it again.
[2786.04 --> 2786.92]  There goes the connection.
[2787.44 --> 2791.24]  And it took us weeks of just poking around going, what's going on?
[2791.74 --> 2792.44]  Can't see it.
[2792.62 --> 2793.40]  Ghost in the machine.
[2794.84 --> 2795.24]  Wow.
[2796.00 --> 2797.20]  Yeah, too secure is a problem.
[2798.26 --> 2798.66]  Honestly.
[2799.12 --> 2801.42]  Well, in that spirit, D, what's your pin number?
[2802.80 --> 2804.28]  Just give us three of the numbers.
[2805.32 --> 2806.38]  Let's play Mastermind.
[2806.96 --> 2808.76]  Is this like, what's it, Spaceballs?
[2808.98 --> 2809.88]  One, two, three, four?
[2810.34 --> 2810.58]  Yeah.
[2811.44 --> 2813.06]  No one's going to suspect that, I think.
[2813.54 --> 2814.78]  No one's going to try that, are they?
[2815.20 --> 2816.54]  Zero, zero, zero, zero.
[2816.92 --> 2817.80]  Does it allow you?
[2817.88 --> 2819.58]  I don't think systems allow you to do that.
[2819.80 --> 2820.08]  Why?
[2820.72 --> 2821.00]  I don't know.
[2821.06 --> 2822.28]  I'm going to try and change my pin now.
[2822.34 --> 2822.46]  Yeah.
[2823.04 --> 2823.38]  You might.
[2823.38 --> 2825.52]  Oh, yeah.
[2825.62 --> 2826.10]  I don't know.
[2826.46 --> 2826.70]  Maybe.
[2826.90 --> 2827.60]  Because it's too easy.
[2828.24 --> 2828.74]  I don't know.
[2829.92 --> 2834.96]  Any other horror stories before we throw a, what do you put on fire?
[2835.06 --> 2835.42]  Water?
[2835.78 --> 2836.60]  Don't do that, do you?
[2836.66 --> 2838.10]  Just let it die out on its own?
[2838.26 --> 2839.24]  No, we've got to be responsible.
[2839.76 --> 2841.46]  How are we going to sort this fire out?
[2841.92 --> 2843.78]  By throwing water and the electrical equipment?
[2845.72 --> 2846.48]  Use foam.
[2846.72 --> 2847.28]  We'll use foam.
[2847.36 --> 2847.70]  Turn it off.
[2847.72 --> 2848.60]  We'll close slack.
[2848.60 --> 2849.32]  What's on fire?
[2849.50 --> 2849.64]  Yeah.
[2849.80 --> 2851.96]  Close slack, and then the fire will die down.
[2851.96 --> 2856.06]  So before we put the fire out, has anyone got any other final horror stories?
[2856.70 --> 2859.18]  Well, you know, if you're mine, anyone you want to hear?
[2859.60 --> 2861.14]  Well, what do you mean in real life?
[2863.06 --> 2867.18]  I wrote one down, which actually I wrote in advance about doing a sequel statement and
[2867.18 --> 2874.08]  accidentally double putting in the semicolon after the from table, so an update.
[2874.58 --> 2878.50]  So the where statement didn't apply, and that was to a production system.
[2878.92 --> 2881.86]  Oh, so what's the effect of that then?
[2881.86 --> 2886.38]  So normally you would be updating something and specifying the where, which will limit
[2886.38 --> 2887.92]  what gets changed, right?
[2888.32 --> 2889.06]  Yeah, exactly.
[2889.38 --> 2892.48]  I tweeted this when you actually asked about it, and I think no one really appreciated
[2892.48 --> 2896.00]  what it does and how it happened.
[2896.16 --> 2897.46]  But I executed a query.
[2897.60 --> 2902.22]  I was just tidying up some debt that was left over, and it should have been really trivial.
[2902.22 --> 2905.68]  And I practiced it, and then I copy and pasted it into the console.
[2905.84 --> 2910.78]  But after I copied and pasted the first one, for whatever reason, I fingered a semicolon
[2910.78 --> 2912.78]  and then put in the where line.
[2912.92 --> 2914.20]  But that makes it two commands.
[2914.50 --> 2918.58]  So it successfully did the update column set value equals on table.
[2919.06 --> 2920.46]  And it didn't apply the where.
[2920.62 --> 2923.62]  So it updated, I think it was like 90 million rows or something.
[2923.90 --> 2924.68]  Oh, God.
[2924.68 --> 2927.08]  And the machine was very fast.
[2927.84 --> 2929.70]  Faster than I was at finding Control Z.
[2929.96 --> 2930.90]  Oh, no.
[2931.48 --> 2934.94]  And that's why you work inside of transaction blocks, kids.
[2936.22 --> 2940.36]  That's why that's advisable, but was not what I was doing that day.
[2940.36 --> 2946.20]  The real mess there is actually sort of going, how can we restore this when our database backup
[2946.20 --> 2950.84]  was like 12 hours ago, and there's 12 hours of changes in other tables since then?
[2951.16 --> 2951.26]  Ouch.
[2951.68 --> 2953.34]  So you're not going to sort of do anything there.
[2953.44 --> 2959.06]  So it's a pull the old sort of thing and extract that table and then go and update all the necessary
[2959.06 --> 2960.04]  rows for the right things.
[2960.88 --> 2961.86]  Takes time.
[2963.58 --> 2964.06]  Yeah.
[2964.30 --> 2967.48]  I like that you couldn't keep up because the machine was so fast.
[2967.48 --> 2970.88]  Is that why you now insist only on running on Raspberry Pis?
[2971.48 --> 2972.24]  Intel Max.
[2972.70 --> 2973.64]  Run on Intel Max.
[2973.74 --> 2974.80]  It's the solution for everything.
[2977.34 --> 2977.78]  Okay.
[2977.88 --> 2978.96]  Well, that sound.
[2979.24 --> 2981.26]  We all heard that sound, didn't we?
[2982.26 --> 2984.22]  How would you describe that sound that we just heard?
[2984.50 --> 2985.10]  That sound.
[2985.28 --> 2985.66]  Spooky.
[2985.82 --> 2986.08]  Natalie.
[2986.76 --> 2987.20]  Spooky.
[2987.36 --> 2987.66]  Yes.
[2988.04 --> 2990.06]  Natalie, how would you describe that sound that we just heard?
[2990.84 --> 2991.80]  Did I miss the sound?
[2992.46 --> 2993.46]  Yeah, we heard that sound.
[2995.68 --> 2997.20]  Chris, how would you describe it?
[2997.20 --> 2998.04]  Was it the marshmallows?
[2999.24 --> 3002.56]  I think it's the sound of us closing slack so our fire is going away.
[3002.70 --> 3003.28]  Was it marshmallows?
[3003.70 --> 3005.36]  Yeah, it's kind of a spooky sound, wasn't it, Johnny?
[3005.48 --> 3006.82]  How would you describe that, Johnny?
[3007.06 --> 3008.02]  If you had to, what'd you do?
[3008.60 --> 3010.28]  As silent as your hairline?
[3011.60 --> 3012.50]  Oh, wow.
[3014.10 --> 3019.80]  I mean, it's getting very poetic and slightly unusual.
[3020.20 --> 3021.08]  Banter that.
[3021.08 --> 3023.94]  You asked for it.
[3024.06 --> 3025.38]  I mean, you did ask for it.
[3025.44 --> 3025.64]  Amazing.
[3026.20 --> 3026.36]  Yeah.
[3026.64 --> 3028.64]  Is it silent because it's so far away?
[3028.82 --> 3029.64]  Like, distant.
[3029.90 --> 3030.80]  It's in the distance.
[3031.62 --> 3032.28]  Does that mean?
[3033.08 --> 3035.08]  Like, it's screaming, but you can't hear it.
[3035.48 --> 3036.46]  It's too far back.
[3037.20 --> 3037.44]  Yeah.
[3037.44 --> 3040.20]  It's just screaming, why, Dad?
[3040.98 --> 3041.34]  Why?
[3042.42 --> 3043.14]  Do you know what I mean?
[3043.26 --> 3045.62]  If you know you're going to look like this, don't have kids.
[3045.98 --> 3048.20]  If you know you're going to make kids that look like me, don't have them.
[3048.38 --> 3049.28]  That's my advice.
[3049.80 --> 3050.78]  But my dad doesn't listen.
[3050.78 --> 3053.96]  We're all talking about recessions nowadays, but you've been in one for quite some time,
[3054.02 --> 3054.34]  right, Matt?
[3056.06 --> 3057.18]  Oh, there we go.
[3058.06 --> 3058.86]  That was a good one.
[3062.64 --> 3063.42]  That was a good one.
[3063.42 --> 3063.62]  Yeah.
[3064.00 --> 3064.26]  Yeah.
[3065.02 --> 3065.64]  Good point.
[3066.86 --> 3067.22]  Okay.
[3067.42 --> 3067.64]  Well.
[3070.54 --> 3075.52]  That sound of Johnny talking tells us it's time for Unpopular Opinions.
[3075.52 --> 3079.52]  Unpopular Opinions.
[3086.52 --> 3089.44]  Unpopular Opinions.
[3091.68 --> 3092.68]  Okay.
[3093.42 --> 3100.00]  Who's going to kick us off with the first unpopular opinion?
[3100.92 --> 3101.20]  D.
[3103.48 --> 3104.28]  You've been chosen.
[3104.48 --> 3104.86]  You scared him.
[3105.62 --> 3106.32]  He was like, what?
[3106.54 --> 3106.82]  What?
[3106.88 --> 3107.24]  What happened?
[3107.32 --> 3107.60]  What happened?
[3108.40 --> 3112.38]  Let's just say, I promise no one's pushing their hand around the Ouija board to make it
[3112.38 --> 3115.20]  spell out that I'm about my hairline.
[3115.36 --> 3118.50]  I don't want to hear anything from the ghosts about my hairline, Johnny.
[3118.92 --> 3119.18]  Right?
[3119.28 --> 3121.44]  So don't make it do that.
[3121.90 --> 3122.80]  Everyone put your hand on it.
[3122.80 --> 3123.64]  Let it be natural.
[3123.90 --> 3124.36]  And we'll see.
[3124.54 --> 3124.76]  Yeah.
[3124.80 --> 3126.10]  It's floated over to D.
[3126.72 --> 3127.32]  Okay, D.
[3127.70 --> 3128.26]  It's a fix.
[3128.26 --> 3128.76]  It's a fix.
[3129.56 --> 3130.44]  Unpopular Opinions.
[3130.58 --> 3131.16]  It was a fix.
[3131.30 --> 3131.44]  Yeah.
[3132.26 --> 3133.52]  Mine comes from the last go.
[3133.74 --> 3134.70]  The last go time.
[3134.94 --> 3136.44]  One of the guests said that Go's brilliant.
[3136.56 --> 3137.56]  You don't have to worry about security.
[3137.72 --> 3138.64]  It does everything for you.
[3138.76 --> 3140.10]  You don't have to worry about the memory management.
[3140.34 --> 3140.88]  It's everything.
[3140.88 --> 3141.78]  It's super cool.
[3141.88 --> 3148.16]  And I think it actually has made Go more insecure because people are so, they've put so much
[3148.16 --> 3153.20]  trust and safety in the actual sort of language that a lot of the basics are dropping by
[3153.20 --> 3153.62]  the wayside.
[3154.12 --> 3156.82]  For me, the number one thing that people should do is sanitize inputs.
[3156.82 --> 3160.10]  And it's not because I wrote Blue Band-Aid, but they should do it on everything.
[3160.42 --> 3162.56]  And I just don't think see anyone doing it anywhere.
[3163.12 --> 3165.16]  And there's just great big holes in everything.
[3165.34 --> 3167.86]  But people are still there going, but we've got memory safety.
[3168.72 --> 3171.28]  Memory safety saves you from yourself, not from others.
[3171.28 --> 3175.90]  What do we think?
[3175.98 --> 3177.54]  Is that popular or unpopular?
[3177.82 --> 3178.74]  It should be popular.
[3180.04 --> 3181.18]  Sanitize all your inputs?
[3181.48 --> 3182.28]  It should be.
[3182.66 --> 3186.98]  But if you look at all of the open source stuff that's out there, very few people actually
[3186.98 --> 3189.42]  sanitize, check, validate their inputs.
[3189.88 --> 3193.98]  They're just like, I mapped this input directly to a struct and I'm going to use it.
[3194.44 --> 3196.72]  You know, they take their form fill and they're on their way.
[3197.06 --> 3197.26]  Yeah.
[3197.26 --> 3201.14]  One simple version of that is just a limit reader when you're reading a body.
[3201.48 --> 3202.98]  Or like of a request.
[3203.26 --> 3206.28]  Like you can error if it's too big and things like that.
[3206.40 --> 3207.18]  There's bits like that.
[3207.28 --> 3210.94]  But you end up doing quite a lot of that heavy lifting yourself every time.
[3211.32 --> 3214.78]  There are libraries out there where you can add tacks and say, this should be a text field.
[3214.84 --> 3216.10]  It should be no longer than this length.
[3216.22 --> 3216.92]  There should be a number.
[3217.06 --> 3217.94]  It should be no longer than this.
[3218.36 --> 3220.50]  But far too few projects do it.
[3220.74 --> 3221.90]  Do they use reflection?
[3222.06 --> 3223.90]  I think I've avoided them if they...
[3223.90 --> 3226.36]  But although that's not a great reason to avoid it.
[3226.36 --> 3228.36]  I just tend to not...
[3228.36 --> 3230.02]  Why are you afraid of your reflection?
[3230.48 --> 3231.08]  Are you a vampire?
[3231.28 --> 3232.28]  Well, it's...
[3232.28 --> 3233.88]  Because I am a Dracula.
[3234.60 --> 3235.38]  Yeah, the casino.
[3236.78 --> 3238.90]  Because he doesn't want to see that hairline.
[3239.14 --> 3239.38]  Obviously.
[3239.84 --> 3239.94]  Oh!
[3240.58 --> 3242.28]  That's why I don't have mirrors.
[3243.48 --> 3244.30]  Chris is in on it.
[3244.40 --> 3244.68]  All right.
[3244.74 --> 3245.54]  Everybody take a turn.
[3245.70 --> 3246.56]  Yeah, Chris is in on it.
[3246.84 --> 3247.84]  Take a stab at Matt.
[3248.98 --> 3249.92]  I'm like a pinata.
[3250.84 --> 3252.48]  Like a really rubbish pinata.
[3252.62 --> 3254.96]  Imagine you buying a pinata for kids and it's me.
[3255.48 --> 3256.12]  You know what I mean?
[3256.12 --> 3257.20]  You'd take it back, wouldn't you?
[3257.82 --> 3260.66]  You'd be like, no, we'd probably go for the unicorn instead in second thought.
[3260.66 --> 3262.20]  Should have guessed that, really.
[3262.54 --> 3263.16]  Okay, yeah.
[3263.88 --> 3264.28]  Fine.
[3264.60 --> 3265.06]  Thanks, Chris.
[3265.16 --> 3265.88]  It's Halloween special.
[3266.02 --> 3267.76]  You're allowed to do that.
[3268.18 --> 3268.82]  Spooky opinion.
[3269.86 --> 3270.46]  Yeah, exactly.
[3271.08 --> 3271.40]  Okay.
[3271.46 --> 3272.80]  Any other unpopular opinions?
[3273.18 --> 3273.80]  I have one.
[3274.48 --> 3276.42]  Natalie Pistano, which?
[3277.26 --> 3277.50]  How?
[3277.50 --> 3277.82]  Ooh!
[3278.96 --> 3279.56]  I don't assume.
[3280.34 --> 3281.76]  They don't know I've just done that.
[3282.00 --> 3283.88]  So it just sounds like a sound effect in the background.
[3284.10 --> 3284.36]  Come on.
[3284.66 --> 3289.58]  Some of the training that you should be taking occasionally throughout your career, even annually,
[3289.58 --> 3294.70]  should not be about things that are in the future, like new things, like new technologies
[3294.70 --> 3295.52]  coming and so on.
[3295.52 --> 3297.58]  But also a little bit about the back.
[3298.64 --> 3300.84]  A little bit of assembly every now and then.
[3301.56 --> 3305.96]  Might be useful accidentally at some point in your life because you need it.
[3306.08 --> 3310.10]  And even if not, it might, like you'll see patterns because it's all the same things,
[3310.14 --> 3312.74]  it's just more and more abstractions, but it's still the same things.
[3312.74 --> 3320.36]  So seeing how it's done, how things were solved, how problems were, might help you figure future
[3320.36 --> 3322.02]  when you rely on the past.
[3322.74 --> 3323.48]  And it's unpopular.
[3323.76 --> 3325.18]  I know you all haven't been agree with me.
[3325.28 --> 3325.82]  It's unpopular.
[3326.02 --> 3326.44]  None of us.
[3326.60 --> 3330.72]  I also did not do that and don't allocate time or budget for that.
[3332.02 --> 3333.26]  I do know what you mean.
[3333.42 --> 3336.30]  I actually have this book called But How Do It Know?
[3336.60 --> 3339.24]  It's just on, I got it off the Amazon website.
[3339.24 --> 3344.92]  And basically it talks about computing from the very bare beginnings, like literally logic
[3344.92 --> 3350.00]  gates and then how you make a bit out of two NAND gates and like just showing how the logic
[3350.00 --> 3352.80]  works and then building up everything in a computer like that.
[3352.94 --> 3354.02]  And it is amazing.
[3354.24 --> 3357.58]  But yeah, it was like not something I need.
[3357.86 --> 3362.06]  And actually something else that occurred to me when you were saying that one is having like
[3362.06 --> 3365.42]  training or paying attention to things that you already think you're good at.
[3365.56 --> 3369.14]  So not just new things that are new to you, things that you already think
[3369.14 --> 3370.06]  yeah, I've got that nailed.
[3370.58 --> 3371.70]  You might be surprised.
[3372.00 --> 3373.68]  Like plenty of other things to learn.
[3373.84 --> 3374.08]  Yeah.
[3374.56 --> 3375.34]  I like that one.
[3375.44 --> 3376.34]  We'll test that one.
[3376.66 --> 3377.90]  See if that's unpopular or not.
[3378.08 --> 3381.46]  Even the way you did that is interesting because you were already a couple of years
[3381.46 --> 3384.10]  a software developer and then you looked into gates and so on.
[3384.12 --> 3386.54]  And that kind of helped you put this in place.
[3386.68 --> 3391.24]  When I started my degree, the first course I did was those logic gates and everything was
[3391.24 --> 3391.46]  scary.
[3391.58 --> 3392.34]  Calculus was scary.
[3392.46 --> 3394.00]  And then those gates, like what?
[3394.42 --> 3395.32]  I don't know that.
[3395.48 --> 3396.70]  Just let me pass that test.
[3396.76 --> 3397.24]  Leave me alone.
[3397.24 --> 3401.98]  And if it would be the other way around, start with the programming courses and then
[3401.98 --> 3406.60]  you go about semiconductors and then you go about circuits and then you speak about gates.
[3406.76 --> 3410.62]  It might have been more interesting and actually would make more sense.
[3410.70 --> 3411.60]  Maybe for me, at least.
[3412.40 --> 3415.04]  I think that's the path that people take accidentally.
[3415.52 --> 3419.44]  Like those who do boot camps and then they actually eventually over like five, 10 years
[3419.44 --> 3423.34]  become like systems engineers and are working on like kernel or TLS or something.
[3423.34 --> 3426.76]  They don't know they're doing that, but that's kind of what they're doing, right?
[3426.80 --> 3428.08]  They're looking back at the fundamentals.
[3428.54 --> 3428.62]  Yeah.
[3428.72 --> 3429.18]  I agree.
[3429.24 --> 3429.76]  It's unpopular.
[3429.98 --> 3432.70]  I don't know anyone who does that, but I think it's genius and we should.
[3432.90 --> 3435.02]  We shouldn't open a university that teaches that way.
[3435.44 --> 3436.94]  I feel like that's how my career has been.
[3437.10 --> 3439.74]  I just have gone like down the stack further and further.
[3440.14 --> 3440.72]  That's interesting.
[3440.88 --> 3441.04]  Yeah.
[3441.22 --> 3441.82]  It's been fun.
[3442.26 --> 3445.56]  I've written like a few like operating system kernels, like toy kernels.
[3445.56 --> 3447.14]  It was infuriating.
[3447.34 --> 3451.64]  Modern processors are terrible, but mostly because they're so old.
[3452.18 --> 3454.60]  Like, oh, maybe I have this code from the 70s.
[3454.64 --> 3458.82]  I might need to run on my Intel 12th gen chip or something.
[3458.94 --> 3459.62]  You never know.
[3459.92 --> 3463.68]  It's like, no, Intel, I don't need to run code from 1980 on my new processor.
[3463.84 --> 3464.20]  Thank you.
[3464.20 --> 3471.58]  I like that too, though, that people can start higher up in the stack and still be doing things
[3471.58 --> 3473.18]  without understanding everything.
[3473.62 --> 3475.08]  Because I've seen it.
[3475.14 --> 3480.24]  People help themselves back because they think, well, I just don't know all of this stuff.
[3480.34 --> 3484.86]  And they don't know that they don't need to know it necessarily, which is why I say you
[3484.86 --> 3486.58]  sometimes don't need to know a lot of the stuff.
[3486.68 --> 3488.42]  Just sort of get on with it and try things.
[3488.82 --> 3490.24]  But it doesn't work for everybody.
[3490.24 --> 3493.80]  I think there's so many different styles and things that people appreciate.
[3493.80 --> 3494.84]  Things that work.
[3495.02 --> 3498.16]  And so wouldn't like to force it on everybody.
[3498.30 --> 3500.26]  As we like to say, it depends.
[3501.54 --> 3506.66]  And I'm afraid put down your goblets of red wine.
[3506.78 --> 3507.70]  Yes, it was what?
[3507.78 --> 3509.02]  It was definitely wine.
[3509.36 --> 3509.74]  Yeah.
[3510.48 --> 3514.48]  And put also away those sandwiches of miscellaneous.
[3515.84 --> 3517.20]  No, there weren't any sandwiches.
[3517.58 --> 3520.28]  No, let's just not do the sandwiches, but we'll do the wine bit.
[3520.28 --> 3523.38]  And then keep the wine because I think it's blood.
[3523.80 --> 3524.56]  Okay.
[3524.72 --> 3529.32]  And that's all the time we have on today's Ghost Time.
[3529.74 --> 3531.30]  Thanks for joining us, everybody.
[3531.98 --> 3534.20]  See you next time and stay spoopy.
[3534.20 --> 3544.24]  Do you have a spooky story that'll scare your fellow devs?
[3544.42 --> 3546.22]  Let us know in the comments.
[3546.78 --> 3549.56]  The link to discuss this episode is in your show notes.
[3550.14 --> 3552.58]  And if you enjoyed this Halloween-themed edition of Go Time,
[3552.82 --> 3554.86]  please do share the pod with your friends.
[3555.10 --> 3556.96]  We appreciate you helping spread the word.
[3557.32 --> 3559.44]  Thanks once again to our partners at Fastly.
[3559.44 --> 3562.88]  They ship all of our pods super fast to wherever you listen.
[3563.18 --> 3565.00]  Check them out at Fastly.com.
[3565.36 --> 3566.54]  And to Fly.io.
[3567.12 --> 3569.78]  Post your app servers and database closer to your users.
[3570.24 --> 3571.10]  No ops required.
[3571.56 --> 3573.44]  Learn more at Fly.io.
[3573.90 --> 3577.66]  Next time on Go Time, Ian and Natalie are joined by Tim Smith
[3577.66 --> 3580.38]  to discuss Go in medicine and biology.
[3581.08 --> 3583.44]  Subscribe now if you haven't yet so you don't miss it.
[3583.44 --> 3585.84]  We'll have that episode ready for you next week.
