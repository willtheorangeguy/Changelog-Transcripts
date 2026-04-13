[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.84]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.22 --> 12.40]  And we're hosted on Linode cloud servers.
[12.76 --> 14.74]  Head to linode.com slash Changelog.
[15.72 --> 20.34]  This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 --> 25.10]  And we're excited to share they now offer dedicated virtual droplets.
[25.10 --> 29.02]  And unlike standard droplets, which use shared virtual CPU threads,
[29.02 --> 32.86]  their two performance plans, general purpose and CPU optimized,
[33.40 --> 36.08]  they have dedicated virtual CPU threads.
[36.40 --> 40.86]  This translates to higher performance and increased consistency during CPU intensive processes.
[41.36 --> 45.20]  So if you have build boxes, CICD, video encoding, machine learning, ad serving,
[45.50 --> 49.98]  game servers, databases, batch processing, data mining, application servers,
[50.20 --> 54.92]  or active front end web servers that need to be full duty CPU all day every day,
[55.14 --> 57.92]  then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 --> 61.26]  Pricing is very competitive starting at 40 bucks a month.
[61.66 --> 66.38]  Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 --> 69.02]  Again, do.co slash Changelog.
[69.02 --> 86.38]  Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.76 --> 88.56]  productive, and accessible to everyone.
[88.94 --> 93.44]  This is where conversations around AI, machine learning, and data science happen.
[93.92 --> 98.20]  Join the community and slack with us around various topics of the show at changelog.com slash community.
[98.20 --> 99.38]  Follow us on Twitter.
[99.48 --> 100.96]  We're at Practical AI FM.
[101.46 --> 102.28]  And now onto the show.
[106.94 --> 111.54]  Welcome to another fully connected episode of Practical AI.
[111.88 --> 118.30]  In these episodes, Chris and I keep you fully connected with everything that's happening in the AI community.
[118.84 --> 123.18]  We'll take some time to discuss some of the latest AI news and trends,
[123.18 --> 129.10]  and we'll dig a little bit into learning resources to help you level up your machine learning game.
[129.74 --> 130.92]  I'm Daniel Whitenack.
[131.04 --> 133.68]  I'm a data scientist with SIL International,
[134.10 --> 136.56]  and my co-host is here, Chris Benson,
[137.10 --> 140.26]  who's a principal AI strategist at Lockheed Martin.
[140.42 --> 141.08]  How you doing, Chris?
[141.22 --> 141.92]  I'm doing great.
[141.98 --> 142.88]  How's it going today, Daniel?
[143.48 --> 144.86]  It's going pretty good.
[144.96 --> 148.40]  Yeah, it's been a reasonably normal week in the sense that
[148.40 --> 152.00]  I've just mostly been at my desk here working on things.
[152.24 --> 157.92]  But yeah, a lot of exciting NLP and, you know, language-related stuff
[157.92 --> 160.74]  coming up this fall and into the spring for me.
[160.84 --> 161.96]  So I'm excited about that.
[162.10 --> 165.80]  But your week's been a little bit more exciting, I hear.
[166.48 --> 169.44]  Well, I'm in London right now as we're recording this
[169.44 --> 174.30]  and started off doing some stuff with the Royal Academy of Engineering
[174.30 --> 175.34]  representing Lockheed Martin.
[175.90 --> 177.20]  Yeah, we're united.
[177.20 --> 180.78]  I was not knighted, and I was so disappointed that I wasn't.
[180.98 --> 186.62]  Wait, I guess it's only possible for English citizens
[186.62 --> 189.02]  or UK citizens to be knighted.
[189.06 --> 189.50]  Is that true?
[189.58 --> 190.26]  I don't even know that.
[190.52 --> 193.40]  I'm not sure, but, you know, I'm married to a Brit,
[193.62 --> 195.22]  and my daughter is half-Brit.
[195.56 --> 196.10]  That should count.
[196.28 --> 198.76]  I was hoping that they'd make an exception, but they didn't.
[198.90 --> 201.00]  I'm going to register a complaint with Buckingham Palace.
[201.66 --> 203.44]  But they didn't kick you out.
[203.48 --> 204.46]  It was a good experience.
[204.84 --> 205.98]  They didn't kick me out.
[205.98 --> 209.72]  Did a talk earlier in the week and did a panel
[209.72 --> 214.38]  and was privileged to meet a lot of really, really, really smart people.
[215.06 --> 216.54]  And that was really good.
[216.84 --> 218.80]  I still had to work remotely after that was done
[218.80 --> 221.02]  because we're about to start a family vacation over here.
[221.10 --> 223.02]  So I was just kind of waiting for family to arrive.
[223.14 --> 226.70]  And I dashed off to North Wales and climbed Snowdon
[226.70 --> 229.06]  and then still put in a full work day every day.
[229.28 --> 230.54]  And so it's been busy.
[230.76 --> 233.78]  But I'm back in London now, and tomorrow is vacation.
[233.78 --> 235.34]  So all is good, my friend.
[236.16 --> 237.48]  Yeah, you're almost there.
[237.56 --> 240.92]  We got to get through this podcast recording,
[240.92 --> 244.50]  and then it's all vacation from there,
[244.60 --> 246.54]  at least until I talk to you next.
[246.88 --> 248.78]  I'm already drinking a Welch beer right now.
[248.88 --> 250.34]  So I'm getting started.
[250.68 --> 250.86]  Okay.
[251.18 --> 251.52]  Nice.
[251.90 --> 252.14]  Cool.
[252.14 --> 254.86]  Well, today on the Fully Connected episode,
[255.38 --> 257.40]  a few of these episodes in the past,
[257.48 --> 260.46]  we've kind of dug deep into individual topics.
[260.58 --> 263.54]  And the last one, we talked about high-performance computing,
[263.70 --> 264.34]  which was great.
[264.90 --> 267.66]  But today, we're just going to take some time
[267.66 --> 271.16]  and discuss a little bit about some of the trends
[271.16 --> 272.96]  that we're seeing in the AI community,
[273.60 --> 276.06]  a few news stories that caught our attention.
[276.66 --> 278.38]  And we've done this in the past,
[278.38 --> 282.74]  but every once in a while, we like to kind of update things in this way.
[282.96 --> 284.44]  So to get things started,
[284.90 --> 288.44]  I just kind of wanted to bring up a trend that I'm definitely seeing,
[288.54 --> 290.00]  which I'm encouraged by,
[290.08 --> 292.42]  and I think is a really good sign.
[292.56 --> 293.26]  And that's this,
[293.62 --> 295.38]  what's seeming to be some good momentum
[295.38 --> 298.30]  in terms of AI contributions,
[298.74 --> 301.24]  AI education, AI research activity,
[301.38 --> 303.68]  all of these things in the majority world.
[303.68 --> 306.34]  So outside of the US and Europe,
[306.80 --> 309.40]  in places, countries in Africa,
[309.40 --> 312.08]  or maybe India, Southeast Asia,
[312.66 --> 315.40]  and where most of the people in the world live.
[315.56 --> 319.02]  So it's great to see a lot of AI activity
[319.02 --> 320.72]  starting to happen in these areas.
[321.14 --> 323.72]  There's definitely still a lot of,
[323.72 --> 325.86]  you know, room for growth.
[326.22 --> 329.18]  There's a article that we'll reference in the show notes,
[329.22 --> 331.14]  and we'll reference all the articles in the show notes
[331.14 --> 332.14]  that we talk about.
[332.14 --> 334.58]  But they kind of look at the publications
[334.58 --> 336.84]  for the NeurIPS conference.
[337.28 --> 339.60]  And of course, those are still highly dominated
[339.60 --> 341.06]  by the US mainly,
[341.22 --> 343.02]  but also European contributors.
[343.42 --> 345.10]  But you can kind of start to see
[345.10 --> 347.80]  some other regions of the world contributing.
[348.32 --> 349.80]  So there's a lot of room for growth,
[349.98 --> 352.70]  but I've definitely been seeing a lot more attention
[352.70 --> 354.98]  being placed on education,
[355.40 --> 356.20]  AI research,
[356.32 --> 358.94]  AI innovation in other places around the world.
[359.04 --> 360.82]  I don't know if you've seen this as well, Chris.
[360.82 --> 361.52]  I have.
[361.78 --> 363.04]  And it's really good to see,
[363.12 --> 363.20]  you know,
[363.24 --> 366.16]  we talk so much about the democratization
[366.16 --> 368.38]  and commoditization of AI
[368.38 --> 370.22]  in terms of accessibility.
[370.84 --> 374.84]  And so seeing it really blossom all over the world
[374.84 --> 376.46]  and not just in kind of,
[376.48 --> 376.80]  you know,
[377.24 --> 378.16]  US and Europe
[378.16 --> 380.38]  and kind of key nations around the world,
[380.64 --> 381.54]  it's really good.
[381.96 --> 382.26]  You know,
[382.30 --> 383.38]  we talk a lot about,
[383.60 --> 384.76]  I like seeing it every time,
[384.86 --> 385.52]  you know,
[385.52 --> 386.16]  it's in Africa,
[386.16 --> 387.50]  and I know we've talked about in the past,
[387.50 --> 389.02]  and I think we're going to talk about that a bit today.
[389.82 --> 391.38]  So I'm pretty happy.
[391.50 --> 392.36]  And I've also noticed
[392.36 --> 395.42]  it's going into a lot of colleges and universities
[395.42 --> 396.26]  around the world
[396.26 --> 398.06]  that are not like top tier strictly.
[398.88 --> 400.94]  And so instead of everything strictly being,
[401.08 --> 401.32]  you know,
[401.36 --> 402.12]  like in the US,
[402.28 --> 402.46]  you know,
[402.52 --> 403.02]  Stanford,
[403.44 --> 403.78]  MIT,
[404.12 --> 404.64]  that kind of thing,
[404.92 --> 407.92]  there's a lot of second tier universities
[407.92 --> 409.90]  that are trying to do their thing in it.
[409.94 --> 411.38]  And I'm very encouraged by that.
[411.38 --> 413.08]  It's really becoming available to everyone.
[413.08 --> 413.76]  Yeah,
[413.86 --> 414.26]  definitely.
[414.46 --> 414.74]  And I mean,
[414.76 --> 416.40]  there's a lot of problems
[416.40 --> 418.10]  that are relevant to AI
[418.10 --> 420.34]  that are probably
[420.34 --> 422.60]  people from those regions
[422.60 --> 424.04]  have more domain expertise
[424.04 --> 425.02]  and more empathy
[425.02 --> 426.40]  for these sorts of problems
[426.40 --> 428.28]  around things like translation
[428.28 --> 429.42]  or things like
[429.42 --> 431.98]  certain agriculture related applications
[431.98 --> 433.58]  or other applications
[433.58 --> 433.76]  that,
[433.88 --> 433.98]  you know,
[434.00 --> 435.46]  I'm sure people are working on,
[435.52 --> 436.86]  but these sorts of problems,
[437.42 --> 439.40]  the major application of those
[439.40 --> 440.04]  seems like
[440.04 --> 441.46]  they would be in places
[441.46 --> 442.92]  where there is a lot of language
[442.92 --> 443.40]  diversity
[443.40 --> 445.10]  or where there is a lot of agriculture,
[445.26 --> 445.42]  right?
[445.94 --> 446.18]  You know,
[446.20 --> 446.92]  some of the things
[446.92 --> 448.32]  that I've seen recently
[448.32 --> 450.86]  are the ICLR,
[451.04 --> 452.56]  iClear conference
[452.56 --> 454.88]  is happening in Ethiopia this year,
[454.96 --> 455.78]  which it's a,
[455.82 --> 458.56]  it's a big AI research conference,
[458.56 --> 459.98]  which it's really great
[459.98 --> 461.66]  to see that happening there.
[461.74 --> 462.84]  I wish we could be there.
[462.92 --> 463.16]  Maybe,
[463.34 --> 464.06]  you know,
[464.08 --> 465.12]  if there's any organizers
[465.12 --> 466.26]  listening to this
[466.26 --> 468.28]  and you want our podcast there,
[468.40 --> 470.16]  definitely let us know.
[470.32 --> 471.72]  I'd be up for going to Ethiopia.
[471.72 --> 472.52]  Yeah,
[472.60 --> 473.12]  absolutely.
[473.30 --> 473.54]  Would you?
[473.84 --> 473.98]  Yeah.
[474.30 --> 474.70]  Totally.
[475.12 --> 475.98]  And I agree.
[476.34 --> 477.16]  And I say this,
[477.56 --> 478.72]  I'll say it quietly.
[478.80 --> 479.94]  I'm sitting in London right now
[479.94 --> 480.94]  and I don't want to see
[480.94 --> 481.72]  all AI stuff
[481.72 --> 481.96]  in,
[481.96 --> 482.46]  you know,
[482.52 --> 483.06]  New York City
[483.06 --> 483.94]  and London
[483.94 --> 485.54]  and San Francisco
[485.54 --> 486.78]  and places like that.
[486.86 --> 487.06]  You know,
[487.14 --> 487.96]  it's fantastic
[487.96 --> 488.76]  to see Ethiopia.
[489.50 --> 490.26]  I think,
[490.36 --> 491.36]  I think we should start
[491.36 --> 492.50]  tracking that a little bit
[492.50 --> 493.98]  in terms of places
[493.98 --> 495.06]  you wouldn't expect to see it
[495.06 --> 495.80]  that is popping up
[495.80 --> 497.06]  and give a shout out
[497.06 --> 497.74]  to people like that.
[497.74 --> 498.26]  Yeah,
[498.36 --> 498.66]  definitely.
[498.88 --> 500.28]  So I know Google AI,
[500.60 --> 501.20]  for example,
[501.80 --> 503.70]  has started opening,
[503.84 --> 504.28]  I should say,
[504.36 --> 505.10]  opening offices
[505.10 --> 505.98]  in other places
[505.98 --> 506.82]  around the world.
[507.22 --> 508.50]  They just announced,
[508.72 --> 510.42]  I forget when this announcement was,
[510.44 --> 511.58]  it was just in the last week
[511.58 --> 512.70]  that I saw it at least,
[513.22 --> 514.08]  that they're opening up
[514.08 --> 515.44]  an office in Bangalore,
[515.80 --> 516.64]  in Bangalore, India,
[516.80 --> 518.46]  but also they have offices
[518.46 --> 520.02]  in Ghana and Beijing.
[520.34 --> 521.56]  And then also,
[521.68 --> 522.90]  we're mentioning Africa.
[523.40 --> 524.30]  I know there's a series
[524.30 --> 525.06]  of conferences
[525.06 --> 525.76]  and events
[525.76 --> 526.46]  and workshops,
[526.96 --> 527.30]  you know,
[527.36 --> 528.88]  called the Deep Learning
[528.88 --> 529.38]  and Daba
[529.38 --> 530.48]  that's happening there.
[530.80 --> 531.86]  I've seen other things
[531.86 --> 532.98]  that are being sponsored
[532.98 --> 533.86]  by companies
[533.86 --> 534.66]  like Facebook,
[535.00 --> 535.32]  Google,
[535.64 --> 536.08]  Microsoft,
[536.58 --> 537.54]  and other sort of
[537.54 --> 538.90]  large tech entities
[538.90 --> 540.06]  that are happening there.
[540.14 --> 541.68]  There was a Southeast Asia
[541.68 --> 543.00]  machine learning school.
[543.42 --> 545.14]  There was an AI for India summit
[545.14 --> 547.04]  that Facebook put on in India.
[547.18 --> 548.12]  I think that was actually
[548.12 --> 549.06]  also in Bangalore.
[549.34 --> 550.16]  It seems like a lot
[550.16 --> 551.12]  of these tech companies
[551.12 --> 553.92]  are really interested
[553.92 --> 555.22]  in developing
[555.22 --> 556.84]  AI talent
[556.84 --> 558.24]  and AI expertise
[558.24 --> 559.80]  in these,
[559.90 --> 560.46]  you know,
[560.58 --> 563.06]  majority world countries.
[563.38 --> 564.80]  And I have my own thoughts
[564.80 --> 565.50]  about, you know,
[565.56 --> 566.96]  why that might be taking place.
[567.02 --> 567.88]  But do you have any thoughts
[567.88 --> 569.48]  on sort of why
[569.48 --> 571.40]  tech company like Google
[571.40 --> 572.30]  or Microsoft
[572.30 --> 573.90]  would be interested in that?
[574.50 --> 574.90]  Well, I mean,
[575.12 --> 576.48]  I think part of it is
[576.48 --> 577.52]  it's really hard
[577.52 --> 578.58]  to find great talent.
[578.80 --> 579.74]  And so I think
[579.74 --> 580.92]  having a diversity
[580.92 --> 581.62]  of your,
[581.96 --> 583.10]  in terms of your search
[583.10 --> 584.18]  for the people
[584.18 --> 584.88]  that are interested
[584.88 --> 586.04]  and capable of doing this,
[586.10 --> 586.80]  it makes sense
[586.80 --> 587.98]  to go to third world countries
[587.98 --> 589.46]  and take a bunch
[589.46 --> 590.50]  of interested people
[590.50 --> 591.26]  and, you know,
[591.44 --> 592.38]  bring them into the fold.
[592.52 --> 593.60]  I love that.
[593.92 --> 594.68]  I'm looking at the
[594.68 --> 595.62]  Indaba website
[595.62 --> 596.64]  from a few weeks ago
[596.64 --> 597.46]  when they had the conference.
[597.64 --> 598.24]  And, you know,
[598.34 --> 599.04]  to your point,
[599.26 --> 600.80]  the sponsor list
[600.80 --> 602.08]  is a who's who.
[602.22 --> 602.64]  It's, you know,
[603.06 --> 603.54]  DeepMind,
[603.66 --> 604.02]  Microsoft,
[604.30 --> 604.60]  Google,
[604.86 --> 605.18]  Facebook,
[605.40 --> 605.78]  IBM,
[606.20 --> 606.50]  Apple.
[606.50 --> 607.04]  I mean,
[607.36 --> 608.56]  it's the same tech companies
[608.56 --> 609.48]  that you're going to see
[609.48 --> 610.74]  sponsoring stuff
[610.74 --> 611.54]  in San Francisco
[611.54 --> 612.08]  and New York
[612.08 --> 612.54]  and London
[612.54 --> 613.06]  and such.
[613.22 --> 614.12]  And so I love
[614.12 --> 614.96]  seeing that attention
[614.96 --> 616.40]  and I would love to see
[616.40 --> 617.08]  in this case,
[617.10 --> 617.54]  since we're talking
[617.54 --> 618.08]  about Africa,
[618.62 --> 619.72]  Africa being able
[619.72 --> 621.10]  to really get
[621.10 --> 622.38]  a great AI community
[622.38 --> 623.10]  behind it.
[623.24 --> 624.14]  And while they're at it,
[624.14 --> 624.62]  they should listen
[624.62 --> 625.16]  to our podcast.
[626.56 --> 627.04]  Yeah,
[627.12 --> 628.72]  and we should get involved
[628.72 --> 630.32]  as we can for sure.
[630.66 --> 630.94]  I mean,
[630.94 --> 632.04]  I definitely agree with you.
[632.10 --> 633.48]  I think that the talent
[633.48 --> 635.00]  is one side of things.
[635.52 --> 636.60]  I also think that,
[636.66 --> 637.00]  you know,
[637.46 --> 638.74]  hopefully these companies
[638.74 --> 639.84]  are starting to realize,
[639.96 --> 640.48]  like I mentioned,
[640.58 --> 641.56]  that some of the problems
[641.56 --> 642.44]  that they're really putting
[642.44 --> 643.46]  a lot of focus into,
[643.58 --> 644.62]  like Facebook is putting
[644.62 --> 645.60]  a ton of focus
[645.60 --> 647.52]  into machine translation
[647.52 --> 648.74]  and language tech.
[649.60 --> 650.88]  And really the,
[651.08 --> 651.84]  you know,
[651.92 --> 653.90]  the sort of real world experience
[653.90 --> 654.84]  and domain knowledge
[654.84 --> 656.52]  that people from Africa
[656.52 --> 657.76]  or Southeast Asia
[657.76 --> 658.40]  could bring
[658.40 --> 660.42]  to those sorts of efforts.
[660.42 --> 661.36]  I think you're just
[661.36 --> 662.42]  going to end up
[662.42 --> 663.64]  with better results
[663.64 --> 664.82]  by using expertise
[664.82 --> 666.20]  that's rooted
[666.20 --> 667.98]  and has experience
[667.98 --> 669.52]  in those areas.
[670.10 --> 670.50]  And of course,
[670.64 --> 670.92]  you know,
[671.24 --> 671.52]  AI,
[671.96 --> 672.36]  I think,
[672.42 --> 673.54]  is going to be
[673.54 --> 675.06]  kind of ubiquitous
[675.06 --> 676.72]  in the software stack
[676.72 --> 677.56]  as we move forward.
[677.78 --> 678.12]  And so,
[678.50 --> 679.98]  as we try to build up,
[680.04 --> 680.36]  you know,
[680.62 --> 681.32]  software engineering
[681.32 --> 681.92]  in general
[681.92 --> 683.68]  in these different areas
[683.68 --> 685.36]  and education in general,
[685.36 --> 686.22]  I think it definitely
[686.22 --> 687.48]  needs to be a part of it.
[687.66 --> 688.64]  I wanted to share too,
[688.80 --> 690.58]  recently in July,
[690.58 --> 692.68]  I was in Singapore
[692.68 --> 694.46]  and had the chance
[694.46 --> 695.86]  to stop by
[695.86 --> 698.04]  the AI Singapore offices,
[698.30 --> 699.54]  which you might have heard
[699.54 --> 701.00]  of programs like this.
[701.14 --> 702.10]  So it's kind of like
[702.10 --> 703.64]  the prime minister's office
[703.64 --> 705.54]  in Singapore says,
[705.66 --> 706.72]  Singapore needs to be
[706.72 --> 708.12]  a leader in AI.
[708.52 --> 709.86]  How are we going to do that?
[709.94 --> 711.10]  How are we going to develop
[711.10 --> 712.52]  local talent in AI?
[712.76 --> 713.74]  How are we going to contribute
[713.74 --> 714.50]  to research,
[714.68 --> 714.98]  et cetera,
[715.06 --> 715.40]  et cetera?
[715.84 --> 716.94]  And they established
[716.94 --> 719.56]  this AI Singapore organization,
[719.82 --> 720.66]  which is associated
[720.66 --> 722.34]  with the prime minister's office.
[722.68 --> 724.62]  And their job is to basically
[724.62 --> 725.90]  figure that out.
[726.22 --> 726.76]  I have to say,
[726.84 --> 728.44]  I was super impressed
[728.44 --> 730.16]  with the program
[730.16 --> 731.86]  that they've put together there.
[732.12 --> 733.48]  It seems to be run
[733.48 --> 735.12]  like a well-oiled machine.
[735.40 --> 736.56]  So companies can come
[736.56 --> 738.08]  to AI Singapore
[738.08 --> 740.48]  and they basically say,
[740.64 --> 741.78]  OK, if you have a problem
[741.78 --> 743.08]  that's related to AI,
[743.54 --> 744.54]  let's partner together
[744.54 --> 745.58]  to solve that.
[745.66 --> 746.30]  What we're going to do
[746.30 --> 747.74]  is we're going to form a team
[747.74 --> 748.66]  in AI Singapore,
[749.00 --> 750.00]  which includes,
[750.08 --> 750.44]  you know,
[750.50 --> 752.18]  really top-notch mentors
[752.18 --> 753.14]  in AI
[753.14 --> 754.32]  and researchers in AI
[754.32 --> 755.08]  paired with
[755.08 --> 756.42]  AI apprentices
[756.42 --> 757.64]  that they're training up
[757.64 --> 759.24]  and your engineers
[759.24 --> 760.06]  from your company.
[760.26 --> 760.74]  So basically,
[760.86 --> 762.14]  everybody's leveling up
[762.14 --> 763.68]  in AI at the same time.
[764.16 --> 764.98]  And their focus
[764.98 --> 766.00]  is really not just
[766.00 --> 766.88]  to kind of learn
[766.88 --> 767.72]  interesting things,
[767.72 --> 768.68]  but they're working on,
[768.72 --> 769.16]  you know,
[769.22 --> 770.12]  real-world problems
[770.12 --> 771.14]  that can be solved.
[771.60 --> 772.32]  And they really want
[772.32 --> 773.26]  to take on problems
[773.26 --> 774.48]  that will be pushed
[774.48 --> 775.32]  into production
[775.32 --> 777.06]  in commercial entities.
[777.40 --> 778.22]  So they have
[778.22 --> 779.06]  this whole program
[779.06 --> 779.56]  around it.
[779.56 --> 780.40]  And I have to say,
[780.48 --> 781.72]  I was super impressed
[781.72 --> 783.00]  with the talent
[783.00 --> 783.64]  that was there
[783.64 --> 784.62]  and the program
[784.62 --> 786.10]  that they have going on.
[786.26 --> 787.02]  So it's just cool
[787.02 --> 788.90]  to see that sort of thing happen.
[789.04 --> 790.06]  And I shouldn't
[790.06 --> 790.88]  have been shocked,
[790.96 --> 791.62]  but I was kind of
[791.62 --> 792.48]  a little bit shocked
[792.48 --> 792.96]  that, you know,
[793.00 --> 794.02]  this was going on
[794.02 --> 794.78]  in Singapore
[794.78 --> 797.22]  and at such a great level
[797.22 --> 798.82]  and I had no idea about it.
[799.08 --> 799.80]  So is it accurate
[799.80 --> 800.94]  to say that it's sort of
[800.94 --> 802.42]  running like an AI incubator,
[802.56 --> 803.96]  the way you see incubators
[803.96 --> 804.70]  in the US,
[804.90 --> 805.12]  you know,
[805.16 --> 806.14]  where there are nonprofits
[806.14 --> 807.06]  and, you know,
[807.12 --> 808.60]  university-affiliated organizations
[808.60 --> 809.76]  that are, you know,
[809.94 --> 811.24]  taking the talent in.
[811.30 --> 811.94]  They're just doing it
[811.94 --> 812.88]  instead of being around
[812.88 --> 814.70]  a university setting specifically,
[814.70 --> 815.34]  they're doing it
[815.34 --> 817.04]  out of the prime minister's office.
[817.14 --> 818.46]  Is that a fair way of assessing?
[818.60 --> 819.98]  Yeah, it's not unrelated
[819.98 --> 822.00]  to that sort of incubator idea,
[822.14 --> 823.18]  but it's really more
[823.18 --> 824.68]  maybe an accelerator
[824.68 --> 826.10]  or something like that
[826.10 --> 826.70]  paired with
[826.70 --> 828.94]  educational pieces there.
[829.20 --> 830.54]  Because what happens is
[830.54 --> 832.00]  every year they have,
[832.04 --> 832.26]  you know,
[832.26 --> 833.38]  engineers and whoever
[833.38 --> 834.32]  from Singapore
[834.32 --> 835.66]  apply to become
[835.66 --> 836.60]  AI apprentices
[836.60 --> 838.10]  in the program.
[839.00 --> 839.80]  And I think they said
[839.80 --> 840.26]  they were like,
[840.36 --> 840.52]  you know,
[840.54 --> 841.44]  it's really competitive.
[841.92 --> 842.56]  I'm probably going to get
[842.56 --> 843.36]  the numbers wrong,
[843.44 --> 844.10]  but there were like
[844.10 --> 845.60]  800 people applied
[845.60 --> 847.10]  and 20 get in, right?
[847.14 --> 848.40]  So it's really competitive.
[848.66 --> 849.24]  And so you got
[849.24 --> 850.60]  these top-notch applicants
[850.60 --> 851.82]  and they're training
[851.82 --> 852.96]  them up over this
[852.96 --> 854.98]  sort of nine-month period
[854.98 --> 857.44]  to be AI engineers.
[858.22 --> 859.76]  And so they go through
[859.76 --> 860.62]  a little bit of training,
[860.76 --> 861.74]  but then they're also
[861.74 --> 862.68]  kind of,
[862.68 --> 863.86]  their capstone
[863.86 --> 864.54]  or the project
[864.54 --> 865.28]  that they work on
[865.28 --> 866.60]  is an actual problem
[866.60 --> 867.66]  within a company,
[868.10 --> 868.78]  tech company
[868.78 --> 869.82]  that they're working with.
[869.94 --> 870.82]  And so they sort of
[870.82 --> 872.52]  form this collaborative team
[872.52 --> 874.06]  with mentors
[874.06 --> 874.82]  and the apprentices
[874.82 --> 877.12]  and the industry company
[877.12 --> 879.02]  to actually solve
[879.02 --> 879.44]  a problem
[879.44 --> 880.68]  that will go into production.
[880.88 --> 881.62]  So it's kind of
[881.62 --> 882.84]  existing companies
[882.84 --> 883.96]  leveling up
[883.96 --> 885.28]  their AI expertise
[885.28 --> 886.94]  while at the same time,
[886.98 --> 887.28]  you know,
[887.34 --> 888.76]  developing AI talent
[888.76 --> 889.56]  within Singapore.
[889.74 --> 890.30]  It's pretty cool.
[890.72 --> 891.06]  Do you think
[891.06 --> 891.54]  you're going to see
[891.54 --> 892.66]  more of these popping up
[892.66 --> 893.68]  associated with
[893.68 --> 895.14]  various nation states
[895.14 --> 896.02]  around the world?
[896.12 --> 896.40]  Do you think
[896.40 --> 897.34]  this is going to be
[897.34 --> 898.34]  a kind of a common blueprint
[898.34 --> 899.06]  that we'll see?
[899.96 --> 901.74]  Yeah, I certainly hope so.
[901.94 --> 902.60]  They kind of
[902.60 --> 904.22]  seem to have this down.
[904.72 --> 905.36]  And I'm kind of
[905.36 --> 905.98]  actually shocked
[905.98 --> 906.96]  because most of the times
[906.96 --> 907.80]  when I think about
[907.80 --> 908.56]  like internship
[908.56 --> 910.00]  or sort of
[910.00 --> 911.38]  accelerator programs
[911.38 --> 913.62]  or project-focused program
[913.62 --> 914.14]  partnerships
[914.14 --> 915.16]  between academia
[915.16 --> 916.46]  and industry,
[916.56 --> 917.12]  a lot of times
[917.12 --> 917.76]  those seem like
[917.76 --> 918.84]  they're run really poorly.
[918.84 --> 919.94]  And I think
[919.94 --> 920.72]  what I was shocked by
[920.72 --> 921.42]  was this was run
[921.42 --> 921.96]  really well.
[922.06 --> 922.48]  So I think
[922.48 --> 924.62]  if other countries
[924.62 --> 926.14]  are really serious
[926.14 --> 926.74]  about this,
[926.76 --> 927.68]  I think it is a model
[927.68 --> 929.06]  that we might see more of.
[929.16 --> 929.78]  I think it's hard
[929.78 --> 930.94]  to get right for sure
[930.94 --> 932.14]  because, you know,
[932.20 --> 932.84]  how many times
[932.84 --> 933.54]  have we seen,
[934.10 --> 934.70]  oh, you know,
[934.74 --> 935.56]  this company is going
[935.56 --> 936.38]  to work with this
[936.38 --> 937.16]  university
[937.16 --> 938.22]  or there's going to be
[938.22 --> 939.02]  like this center
[939.02 --> 939.66]  of excellence
[939.66 --> 940.40]  at a university
[940.40 --> 942.12]  that we're going
[942.12 --> 942.80]  to work with
[942.80 --> 944.20]  certain companies
[944.20 --> 944.90]  from industry
[944.90 --> 945.90]  and then, you know,
[946.32 --> 947.16]  some stuff happens,
[947.16 --> 947.84]  but it's not really
[947.84 --> 948.80]  that impactful.
[949.08 --> 949.82]  So I hope that
[949.82 --> 950.58]  these sorts of things
[950.58 --> 951.16]  are a little bit
[951.16 --> 951.84]  more impactful.
[961.44 --> 961.92]  Greetings,
[962.08 --> 962.96]  AI practitioners.
[963.38 --> 964.02]  Jared here,
[964.20 --> 965.06]  wanting to let you know
[965.06 --> 965.74]  that ChangeLog
[965.74 --> 966.96]  will be at All Things Open
[966.96 --> 968.10]  on October 14th
[968.10 --> 968.80]  and 15th.
[969.30 --> 969.84]  We're hosting
[969.84 --> 971.10]  a live JS party
[971.10 --> 971.84]  on stage
[971.84 --> 972.84]  and as a special thanks
[972.84 --> 973.54]  from the organizers,
[973.90 --> 974.60]  we're giving away
[974.60 --> 975.42]  five free passes
[975.42 --> 976.12]  to the conference.
[976.12 --> 977.74]  All you have to do
[977.74 --> 978.12]  is tweet,
[978.26 --> 979.22]  I want a free pass
[979.22 --> 980.00]  to All Things Open
[980.00 --> 980.66]  because,
[981.00 --> 981.78]  state your reason
[981.78 --> 982.44]  and mention
[982.44 --> 983.24]  at ChangeLog
[983.24 --> 984.92]  or at PracticalAIFM
[984.92 --> 985.76]  so we see it
[985.76 --> 986.88]  and we will DM you
[986.88 --> 987.52]  if you win.
[987.88 --> 989.00]  Okay, that's all for me.
[989.18 --> 990.14]  Let's get back into it.
[999.98 --> 1000.70]  It was definitely
[1000.70 --> 1002.30]  great to talk
[1002.30 --> 1003.40]  about some of the things
[1003.40 --> 1004.80]  that have been going on
[1004.80 --> 1006.00]  in parts of the world
[1006.00 --> 1006.92]  that we're not
[1006.92 --> 1007.96]  currently in
[1007.96 --> 1009.06]  but there's certainly
[1009.06 --> 1010.96]  a lot of AI news
[1010.96 --> 1012.14]  coming from the rest
[1012.14 --> 1012.66]  of the world
[1012.66 --> 1013.64]  as well
[1013.64 --> 1014.48]  and I think that
[1014.48 --> 1015.46]  you had something
[1015.46 --> 1016.46]  you wanted to highlight
[1016.46 --> 1018.36]  that you saw in,
[1018.84 --> 1019.88]  was it from MIT
[1019.88 --> 1021.14]  or where was it from?
[1021.28 --> 1022.00]  Yeah, I saw it on
[1022.00 --> 1023.38]  phys.org
[1023.38 --> 1024.82]  and so it's an article
[1024.82 --> 1026.34]  that I ran across
[1026.34 --> 1027.34]  and called
[1027.34 --> 1028.48]  Artificial Intelligence
[1028.48 --> 1029.58]  Probes Dark Matter
[1029.58 --> 1030.26]  in the Universe
[1030.26 --> 1030.86]  and so
[1030.86 --> 1032.90]  from ETH Zurich.
[1033.04 --> 1033.26]  Yep.
[1033.36 --> 1034.22]  Sorry, I got that wrong.
[1034.38 --> 1034.70]  Correct.
[1034.94 --> 1035.56]  And so
[1035.56 --> 1036.88]  I know that you're
[1036.88 --> 1038.40]  a physicist by background
[1038.40 --> 1039.98]  and just as an amateur
[1039.98 --> 1040.70]  I love physics
[1040.70 --> 1041.54]  and so it certainly
[1041.54 --> 1042.32]  caught my attention
[1042.32 --> 1044.40]  and it was interesting
[1044.40 --> 1045.56]  that they were
[1045.56 --> 1047.56]  trying to explain it
[1047.56 --> 1048.78]  by drawing an analogy
[1048.78 --> 1049.86]  with facial recognition
[1049.86 --> 1050.78]  in terms of how
[1050.78 --> 1051.90]  they're using models
[1051.90 --> 1053.58]  to scan, you know,
[1053.66 --> 1054.40]  scan the universe
[1054.40 --> 1055.54]  and try to understand
[1055.54 --> 1057.32]  what both dark matter
[1057.32 --> 1058.92]  and dark energy are.
[1058.92 --> 1059.82]  And for listeners
[1059.82 --> 1061.16]  who may not be familiar,
[1061.74 --> 1061.94]  you know,
[1062.06 --> 1063.38]  the dark matter
[1063.38 --> 1064.70]  exerts gravity
[1064.70 --> 1065.52]  on the universe
[1065.52 --> 1066.74]  and you can measure that
[1066.74 --> 1067.92]  but we can't see it.
[1068.10 --> 1069.24]  It's kind of like gravity
[1069.24 --> 1070.94]  coming from an invisible source.
[1071.40 --> 1071.74]  And Daniel,
[1071.86 --> 1073.32]  if I mess any of this up
[1073.32 --> 1074.16]  you should correct me.
[1074.76 --> 1076.14]  No, you're doing great.
[1076.64 --> 1076.84]  Yeah.
[1076.98 --> 1077.74]  And also the universe
[1077.74 --> 1078.48]  is expanding,
[1078.74 --> 1079.64]  constantly accelerating
[1079.64 --> 1080.40]  in this expansion
[1080.40 --> 1082.22]  and so that's dark energy
[1082.22 --> 1083.32]  and once again
[1083.32 --> 1085.02]  we cannot see that source
[1085.02 --> 1085.68]  and so
[1085.68 --> 1087.18]  those are two of the
[1087.18 --> 1087.88]  great mysteries
[1087.88 --> 1088.94]  in physics at this point
[1088.94 --> 1090.06]  is trying to identify
[1090.06 --> 1091.62]  and understand
[1091.62 --> 1092.84]  what we're observing
[1092.84 --> 1093.74]  and so
[1093.74 --> 1094.84]  seeing that
[1094.84 --> 1096.10]  they're using models
[1096.10 --> 1098.00]  to try to
[1098.00 --> 1099.88]  recognize those features
[1099.88 --> 1101.28]  and find the patterns
[1101.28 --> 1102.16]  that maybe otherwise
[1102.16 --> 1102.80]  we're not seeing
[1102.80 --> 1103.90]  that was pretty cool.
[1104.76 --> 1105.30]  Yeah, definitely.
[1105.50 --> 1106.48]  I think that there's
[1106.48 --> 1107.80]  a sort of
[1107.80 --> 1109.10]  general trend
[1109.10 --> 1109.88]  in science
[1109.88 --> 1110.88]  where these sorts of
[1110.88 --> 1112.12]  AI techniques
[1112.12 --> 1112.92]  are being applied
[1112.92 --> 1114.52]  that are making an impact
[1114.52 --> 1115.42]  and I've mentioned
[1115.42 --> 1116.14]  a couple times
[1116.14 --> 1116.76]  on the podcast
[1116.76 --> 1118.40]  where machine learning
[1118.40 --> 1120.08]  started to make an impact
[1120.08 --> 1120.98]  on the field
[1120.98 --> 1121.70]  that I was studying
[1121.70 --> 1122.74]  when I was in grad school
[1122.74 --> 1124.08]  but I think the pattern
[1124.08 --> 1125.28]  was similar there
[1125.28 --> 1126.08]  and that's
[1126.08 --> 1126.82]  the sense that
[1126.82 --> 1127.32]  you know
[1127.32 --> 1128.08]  we have these
[1128.08 --> 1129.90]  experimental observations
[1129.90 --> 1131.32]  which are kind of
[1131.32 --> 1131.58]  you know
[1131.58 --> 1132.68]  they're rooted in reality
[1132.68 --> 1134.24]  and we have a little bit
[1134.24 --> 1134.66]  of knowledge
[1134.66 --> 1135.84]  about how things work
[1135.84 --> 1136.50]  and you know
[1136.50 --> 1136.96]  constants
[1136.96 --> 1138.00]  and other things
[1138.00 --> 1139.00]  and certain laws
[1139.00 --> 1140.00]  that shouldn't be
[1140.00 --> 1140.66]  violated
[1140.66 --> 1141.68]  so constraints
[1141.68 --> 1142.16]  essentially
[1142.16 --> 1144.04]  but the sort of
[1144.04 --> 1144.72]  relationships
[1144.72 --> 1146.30]  between input
[1146.30 --> 1146.90]  and output
[1146.90 --> 1148.36]  could be incredibly
[1148.36 --> 1150.08]  complicated to write down
[1150.08 --> 1151.32]  in terms of equations
[1151.32 --> 1152.88]  or maybe computationally
[1152.88 --> 1153.48]  too expensive
[1153.48 --> 1154.28]  so the problems
[1154.28 --> 1155.22]  that we are working on
[1155.22 --> 1156.14]  were you know
[1156.14 --> 1156.70]  we know
[1156.70 --> 1158.64]  that this atom
[1158.64 --> 1159.18]  or molecule
[1159.18 --> 1160.36]  has this many
[1160.36 --> 1161.52]  particles in it
[1161.52 --> 1161.74]  right?
[1161.90 --> 1162.44]  Electrons
[1162.44 --> 1164.76]  and neutrons
[1164.76 --> 1165.90]  but to kind of
[1165.90 --> 1167.06]  write down the equations
[1167.06 --> 1167.96]  and actually make
[1167.96 --> 1168.84]  the computations
[1168.84 --> 1170.06]  about how all
[1170.06 --> 1170.84]  these things
[1170.84 --> 1172.02]  work together
[1172.02 --> 1172.96]  it's actually
[1172.96 --> 1174.06]  computationally
[1174.06 --> 1174.92]  infeasible
[1174.92 --> 1176.42]  to do that
[1176.42 --> 1177.14]  you know
[1177.14 --> 1178.54]  and just by the
[1178.54 --> 1179.38]  equations that we
[1179.38 --> 1179.90]  write down
[1179.90 --> 1181.22]  and in this case
[1181.22 --> 1182.46]  with the dark matter
[1182.46 --> 1183.20]  you know
[1183.20 --> 1184.12]  we know some of
[1184.12 --> 1184.86]  these constraints
[1184.86 --> 1185.50]  we know the
[1185.50 --> 1186.74]  experimental observations
[1186.74 --> 1188.06]  but we're not able
[1188.06 --> 1189.14]  to sort of
[1189.14 --> 1190.42]  maybe write down
[1190.42 --> 1191.06]  well the
[1191.06 --> 1192.18]  statistics like
[1192.18 --> 1192.84]  that they're talking
[1192.84 --> 1193.46]  about that
[1193.46 --> 1194.56]  govern these things
[1194.56 --> 1195.02]  and so
[1195.02 --> 1195.94]  kind of plugging
[1195.94 --> 1196.94]  in a neural network
[1196.94 --> 1198.62]  into that gap
[1198.62 --> 1199.86]  and having it
[1199.86 --> 1201.40]  try to learn
[1201.40 --> 1201.94]  some of the
[1201.94 --> 1202.72]  features that
[1202.72 --> 1203.28]  are important
[1203.28 --> 1204.56]  to some
[1204.56 --> 1205.32]  input output
[1205.32 --> 1206.08]  whether that's
[1206.08 --> 1206.52]  input
[1206.52 --> 1207.54]  in this case
[1207.54 --> 1208.06]  input
[1208.06 --> 1208.90]  it sounds like
[1208.90 --> 1209.74]  these experimental
[1209.74 --> 1210.46]  observations
[1210.46 --> 1211.36]  and output
[1211.36 --> 1212.46]  cosmological
[1212.46 --> 1213.30]  constants
[1213.30 --> 1214.18]  and other things
[1214.18 --> 1215.58]  or in the case
[1215.58 --> 1216.42]  of atoms and
[1216.42 --> 1216.82]  molecules
[1216.82 --> 1217.88]  inputting like
[1217.88 --> 1219.18]  geometries
[1219.18 --> 1220.16]  or numbers of
[1220.16 --> 1220.58]  particles
[1220.58 --> 1221.28]  and outputting
[1221.28 --> 1221.74]  energies
[1221.74 --> 1223.08]  putting a
[1223.08 --> 1223.68]  neural network
[1223.68 --> 1224.38]  into that
[1224.38 --> 1225.14]  that gap
[1225.14 --> 1225.68]  where things
[1225.68 --> 1226.28]  are really hard
[1226.28 --> 1226.84]  to model
[1226.84 --> 1227.80]  can make a lot
[1227.80 --> 1228.16]  of sense
[1228.16 --> 1228.58]  I think
[1228.58 --> 1229.44]  yeah I mentioned
[1229.44 --> 1229.92]  that they draw
[1229.92 --> 1230.56]  that analogy
[1230.56 --> 1231.58]  which
[1231.58 --> 1232.74]  they talk about
[1232.74 --> 1233.26]  how Facebook
[1233.26 --> 1234.26]  uses its algorithms
[1234.26 --> 1235.16]  to find eyes
[1235.16 --> 1235.90]  mouth and ears
[1235.90 --> 1236.36]  and images
[1236.36 --> 1237.36]  and that they're
[1237.36 --> 1238.42]  looking for these
[1238.42 --> 1239.38]  telltale signs
[1239.38 --> 1240.02]  of dark matter
[1240.02 --> 1240.72]  and dark energy
[1240.72 --> 1241.16]  that they're
[1241.16 --> 1241.80]  basically looking
[1241.80 --> 1242.72]  for light bending
[1242.72 --> 1243.52]  you know
[1243.52 --> 1244.02]  and so
[1244.02 --> 1245.24]  as light is bent
[1245.24 --> 1246.26]  by the gravitational
[1246.26 --> 1247.30]  influence
[1247.30 --> 1248.48]  I'm assuming
[1248.48 --> 1249.14]  that they're using
[1249.14 --> 1249.98]  convolutional neural
[1249.98 --> 1250.40]  networks
[1250.40 --> 1250.96]  although they don't
[1250.96 --> 1252.00]  explicitly say that
[1252.00 --> 1253.16]  to try to notice
[1253.16 --> 1254.00]  the subtleties
[1254.00 --> 1255.14]  in terms of
[1255.14 --> 1255.90]  identifying the
[1255.90 --> 1256.40]  relationships
[1256.40 --> 1257.38]  but it's just
[1257.38 --> 1258.08]  really interesting
[1258.08 --> 1258.70]  to see it
[1258.70 --> 1259.64]  being used
[1259.64 --> 1260.22]  in this way
[1260.22 --> 1260.96]  I'm always
[1260.96 --> 1261.84]  fascinated to see
[1261.84 --> 1262.62]  all the different
[1262.62 --> 1263.14]  use cases
[1263.14 --> 1264.74]  across industry
[1264.74 --> 1265.48]  as we see this
[1265.48 --> 1266.18]  becoming more
[1266.18 --> 1266.82]  and more pervasive
[1266.82 --> 1267.34]  over time
[1267.34 --> 1268.12]  yeah
[1268.12 --> 1269.10]  data science
[1269.10 --> 1269.86]  for science
[1269.86 --> 1270.76]  I think that's
[1270.76 --> 1271.74]  kind of in vogue
[1271.74 --> 1272.24]  right now
[1272.24 --> 1273.00]  I think
[1273.00 --> 1273.80]  it's a delightful
[1273.80 --> 1274.48]  redundancy
[1274.48 --> 1274.92]  of the word
[1274.92 --> 1275.86]  science isn't it
[1275.86 --> 1277.52]  yeah
[1277.52 --> 1277.94]  very
[1277.94 --> 1278.76]  very meta
[1278.76 --> 1279.66]  yeah
[1279.66 --> 1280.20]  so
[1280.20 --> 1281.38]  speaking of
[1281.38 --> 1282.06]  language
[1282.06 --> 1282.62]  you know
[1282.62 --> 1282.96]  listeners
[1282.96 --> 1283.84]  always know
[1283.84 --> 1284.48]  I'm keeping up
[1284.48 --> 1285.06]  with language
[1285.06 --> 1285.80]  related things
[1285.80 --> 1286.70]  so maybe
[1286.70 --> 1287.22]  you're out there
[1287.22 --> 1287.68]  you're listening
[1287.68 --> 1287.98]  you're like
[1287.98 --> 1288.62]  oh Daniel's
[1288.62 --> 1289.00]  gonna share
[1289.00 --> 1289.68]  another language
[1289.68 --> 1290.40]  related thing
[1290.40 --> 1291.44]  I'm tired of that
[1291.44 --> 1292.26]  don't worry
[1292.26 --> 1292.98]  we're gonna do
[1292.98 --> 1293.42]  an episode
[1293.42 --> 1293.98]  where you're gonna
[1293.98 --> 1294.70]  share all that
[1294.70 --> 1295.32]  with us soon
[1295.32 --> 1296.04]  so you're not
[1296.04 --> 1296.58]  getting out of it
[1296.58 --> 1297.04]  that easy
[1297.04 --> 1297.84]  cool
[1297.84 --> 1298.82]  well I think
[1298.82 --> 1299.50]  that this kind
[1299.50 --> 1300.24]  of has a more
[1300.24 --> 1301.28]  general angle
[1301.28 --> 1301.72]  on it
[1301.72 --> 1302.54]  so not just
[1302.54 --> 1303.06]  language
[1303.06 --> 1304.22]  so hopefully
[1304.22 --> 1304.72]  our listeners
[1304.72 --> 1305.40]  are okay with
[1305.40 --> 1306.06]  that
[1306.06 --> 1307.76]  but I was
[1307.76 --> 1308.88]  really intrigued
[1308.88 --> 1309.44]  by
[1309.44 --> 1311.44]  this recent
[1311.44 --> 1311.98]  thing that
[1311.98 --> 1312.60]  Hugging Face
[1312.60 --> 1313.00]  released
[1313.00 --> 1313.76]  so if
[1313.76 --> 1314.16]  you
[1314.16 --> 1314.66]  if you
[1314.66 --> 1314.84]  don't
[1314.84 --> 1315.22]  remember
[1315.22 --> 1316.68]  the
[1316.68 --> 1317.30]  CEO
[1317.30 --> 1317.54]  of
[1317.54 --> 1318.16]  Hugging Face
[1318.16 --> 1318.72]  was on the
[1318.72 --> 1319.46]  podcast here
[1319.46 --> 1320.06]  talking about
[1320.06 --> 1321.02]  social AI
[1321.02 --> 1322.84]  and conversational
[1322.84 --> 1323.26]  AI
[1323.26 --> 1324.10]  and that was a
[1324.10 --> 1324.66]  great episode
[1324.66 --> 1325.30]  we'll link it
[1325.30 --> 1325.60]  in our
[1325.60 --> 1326.16]  in our show
[1326.16 --> 1326.46]  notes
[1326.46 --> 1327.46]  but they've
[1327.46 --> 1327.90]  kind of
[1327.90 --> 1328.52]  really been
[1328.52 --> 1328.96]  working on
[1328.96 --> 1329.52]  these you
[1329.52 --> 1329.64]  know
[1329.64 --> 1330.78]  large scale
[1330.78 --> 1331.68]  language models
[1331.68 --> 1332.32]  you might have
[1332.32 --> 1332.62]  heard of
[1332.62 --> 1333.22]  BERT or
[1333.22 --> 1334.28]  ELMO or
[1334.28 --> 1335.66]  GPT-2
[1335.66 --> 1336.16]  from
[1336.16 --> 1336.86]  OpenAI
[1336.86 --> 1338.10]  and so
[1338.10 --> 1338.84]  with this
[1338.84 --> 1340.06]  most recent
[1340.06 --> 1340.74]  release
[1340.74 --> 1341.60]  or one of
[1341.60 --> 1342.10]  their recent
[1342.10 --> 1342.74]  releases
[1342.74 --> 1343.90]  and publications
[1343.90 --> 1345.24]  they kind of
[1345.24 --> 1345.76]  took a different
[1345.76 --> 1346.42]  angle on it
[1346.42 --> 1347.20]  and it's called
[1347.20 --> 1348.12]  DistillBERT
[1348.12 --> 1349.32]  and so
[1349.32 --> 1350.30]  what they said
[1350.30 --> 1351.10]  was okay
[1351.10 --> 1352.16]  the trend
[1352.16 --> 1352.54]  in these
[1352.54 --> 1353.32]  language models
[1353.32 --> 1353.80]  is that
[1353.80 --> 1354.20]  they keep
[1354.20 --> 1354.80]  getting larger
[1354.80 --> 1355.36]  and larger
[1355.36 --> 1355.72]  and they're
[1355.72 --> 1356.12]  trained on
[1356.12 --> 1356.50]  more and
[1356.50 --> 1357.02]  more data
[1357.02 --> 1358.58]  and in fact
[1358.58 --> 1359.34]  one of the
[1359.34 --> 1359.72]  references
[1359.72 --> 1360.44]  they give
[1360.44 --> 1361.58]  is a
[1361.58 --> 1362.20]  latest model
[1362.20 --> 1362.90]  from Facebook
[1362.90 --> 1363.24]  AI
[1363.24 --> 1363.78]  that was
[1363.78 --> 1364.48]  trained on
[1364.48 --> 1365.66]  160
[1365.66 --> 1366.72]  gigabytes
[1366.72 --> 1367.34]  of text
[1367.34 --> 1367.68]  which
[1367.68 --> 1368.38]  that might
[1368.38 --> 1368.86]  not seem
[1368.86 --> 1369.34]  like a lot
[1369.34 --> 1369.76]  for those
[1369.76 --> 1370.26]  that do
[1370.26 --> 1370.80]  images
[1370.80 --> 1371.64]  or videos
[1371.64 --> 1372.50]  but if you
[1372.50 --> 1372.86]  think about
[1372.86 --> 1374.06]  160 gigabytes
[1374.06 --> 1374.80]  of text
[1374.80 --> 1375.38]  that's a lot
[1375.38 --> 1375.90]  of text
[1375.90 --> 1376.72]  raw text
[1376.72 --> 1377.00]  data
[1377.00 --> 1377.36]  that's an
[1377.36 --> 1377.80]  enormous
[1377.80 --> 1378.18]  amount
[1378.18 --> 1378.56]  of text
[1378.56 --> 1378.82]  data
[1378.82 --> 1379.34]  so
[1379.34 --> 1379.90]  they were
[1379.90 --> 1380.32]  motivated
[1380.32 --> 1380.84]  by the
[1380.84 --> 1381.08]  fact
[1381.08 --> 1381.40]  of looking
[1381.40 --> 1381.74]  at those
[1381.74 --> 1382.02]  things
[1382.02 --> 1382.34]  and then
[1382.34 --> 1382.64]  saying
[1382.64 --> 1382.96]  okay
[1382.96 --> 1383.34]  well
[1383.34 --> 1384.02]  if we
[1384.02 --> 1384.32]  actually
[1384.32 --> 1384.70]  want to
[1384.70 --> 1384.96]  use
[1384.96 --> 1385.22]  those
[1385.22 --> 1385.50]  types
[1385.50 --> 1385.70]  of
[1385.70 --> 1386.06]  models
[1386.06 --> 1386.44]  in
[1386.44 --> 1386.94]  production
[1386.94 --> 1387.74]  how do
[1387.74 --> 1387.86]  we
[1387.86 --> 1388.08]  do
[1388.08 --> 1388.32]  that
[1388.32 --> 1388.56]  under
[1388.56 --> 1388.84]  the
[1388.84 --> 1389.06]  sort
[1389.06 --> 1389.18]  of
[1389.18 --> 1389.42]  low
[1389.42 --> 1389.90]  latency
[1389.90 --> 1390.56]  constraints
[1390.56 --> 1390.98]  where
[1390.98 --> 1391.26]  we
[1391.26 --> 1391.46]  might
[1391.46 --> 1391.60]  want
[1391.60 --> 1391.68]  to
[1391.68 --> 1391.84]  make
[1391.84 --> 1392.24]  a lot
[1392.24 --> 1392.38]  of
[1392.38 --> 1392.76]  predictions
[1396.72 --> 1397.54]  also
[1397.54 --> 1398.80]  how
[1398.80 --> 1399.00]  would
[1399.00 --> 1399.16]  we
[1399.16 --> 1399.44]  run
[1399.44 --> 1399.72]  those
[1399.72 --> 1399.98]  types
[1399.98 --> 1400.18]  of
[1400.18 --> 1400.54]  models
[1400.54 --> 1400.80]  on
[1400.80 --> 1400.96]  a
[1400.96 --> 1401.38]  smartphone
[1401.38 --> 1401.76]  where
[1401.76 --> 1402.12]  there's
[1402.12 --> 1402.70]  obviously
[1402.70 --> 1403.64]  constraints
[1403.64 --> 1404.02]  around
[1404.02 --> 1404.44]  energy
[1404.44 --> 1405.08]  efficiency
[1405.08 --> 1406.04]  you know
[1406.04 --> 1406.42]  maybe
[1406.42 --> 1407.20]  memory
[1407.20 --> 1407.98]  constraints
[1407.98 --> 1409.08]  and also
[1409.08 --> 1409.46]  just
[1409.46 --> 1410.04]  generally
[1410.04 --> 1410.82]  the
[1410.82 --> 1411.30]  environmental
[1411.30 --> 1411.94]  cost
[1411.94 --> 1412.44]  of running
[1412.44 --> 1413.00]  large
[1413.00 --> 1413.34]  models
[1413.34 --> 1413.84]  like this
[1413.84 --> 1414.08]  is
[1414.08 --> 1414.64]  huge
[1414.64 --> 1415.50]  in terms
[1415.50 --> 1415.98]  of
[1415.98 --> 1416.36]  the
[1416.36 --> 1416.96]  computing
[1416.96 --> 1417.70]  requirements
[1417.70 --> 1418.26]  for them
[1418.26 --> 1419.06]  and so
[1419.06 --> 1419.82]  they took
[1419.82 --> 1420.82]  this
[1420.82 --> 1421.56]  and said
[1421.56 --> 1421.92]  what would
[1421.92 --> 1422.56]  it take
[1422.56 --> 1423.20]  to create
[1423.20 --> 1424.24]  a smaller
[1424.24 --> 1424.86]  faster
[1424.86 --> 1425.40]  cheaper
[1425.40 --> 1425.96]  lighter
[1425.96 --> 1427.04]  version
[1427.04 --> 1427.38]  of
[1427.38 --> 1427.60]  BERT
[1427.60 --> 1427.86]  which
[1427.86 --> 1428.00]  is
[1428.00 --> 1428.16]  one
[1428.16 --> 1428.30]  of
[1428.30 --> 1428.56]  these
[1428.56 --> 1429.16]  large
[1429.16 --> 1429.64]  scale
[1429.64 --> 1430.44]  language
[1430.44 --> 1430.80]  models
[1430.80 --> 1431.20]  and they
[1431.20 --> 1431.74]  ended up
[1431.74 --> 1431.94]  doing
[1431.94 --> 1432.22]  that
[1432.22 --> 1432.52]  and
[1432.52 --> 1433.18]  this
[1433.18 --> 1433.58]  is
[1433.58 --> 1433.68]  what
[1433.68 --> 1433.82]  they're
[1433.82 --> 1434.16]  calling
[1434.16 --> 1434.70]  Distill
[1434.70 --> 1434.98]  BERT
[1434.98 --> 1435.84]  and
[1435.84 --> 1436.28]  it
[1436.28 --> 1436.66]  actually
[1436.66 --> 1437.24]  has
[1437.24 --> 1437.64]  very
[1437.64 --> 1438.02]  small
[1438.02 --> 1438.46]  penalties
[1438.46 --> 1439.10]  in terms
[1439.10 --> 1439.28]  of
[1439.28 --> 1439.88]  evaluation
[1439.88 --> 1440.22]  but
[1440.22 --> 1440.80]  it's
[1440.80 --> 1441.40]  smaller
[1441.40 --> 1441.96]  faster
[1441.96 --> 1442.54]  cheaper
[1442.54 --> 1442.98]  lighter
[1442.98 --> 1444.58]  in comparison
[1444.58 --> 1445.64]  they have
[1445.64 --> 1446.00]  a little
[1446.00 --> 1446.76]  graph
[1446.76 --> 1447.52]  of how
[1447.52 --> 1447.78]  many
[1447.78 --> 1448.26]  millions
[1448.26 --> 1448.48]  of
[1448.48 --> 1449.00]  parameters
[1449.00 --> 1449.98]  various
[1449.98 --> 1450.48]  models
[1450.48 --> 1450.98]  have
[1450.98 --> 1451.82]  and
[1451.82 --> 1452.02]  the
[1452.02 --> 1452.38]  latest
[1452.38 --> 1452.84]  so
[1452.84 --> 1453.26]  there's
[1453.26 --> 1453.82]  an
[1453.82 --> 1454.22]  NVIDIA
[1454.22 --> 1454.60]  model
[1454.60 --> 1454.92]  language
[1454.92 --> 1455.20]  model
[1455.20 --> 1455.54]  that has
[1455.54 --> 1455.80]  like
[1455.96 --> 1456.94]  8300
[1456.94 --> 1457.94]  million
[1457.94 --> 1460.22]  parameters
[1460.22 --> 1460.98]  and
[1460.98 --> 1461.36]  Distill
[1461.36 --> 1461.54]  BERT
[1461.54 --> 1461.90]  has
[1461.90 --> 1462.42]  66
[1462.42 --> 1462.90]  million
[1462.90 --> 1463.16]  so
[1463.16 --> 1463.54]  a
[1463.54 --> 1464.12]  significant
[1464.12 --> 1464.66]  reduction
[1464.66 --> 1465.32]  in size
[1465.32 --> 1465.84]  but
[1465.84 --> 1466.28]  only
[1466.28 --> 1467.18]  you know
[1467.18 --> 1468.18]  Distill
[1468.18 --> 1468.42]  BERT
[1468.42 --> 1468.96]  still
[1468.96 --> 1469.68]  maintains
[1469.68 --> 1470.98]  95%
[1470.98 --> 1471.24]  of
[1471.24 --> 1471.58]  BERT's
[1471.58 --> 1472.10]  performance
[1472.10 --> 1473.18]  on
[1473.18 --> 1474.02]  language
[1474.02 --> 1474.94]  understanding
[1474.94 --> 1475.58]  benchmarks
[1475.58 --> 1476.14]  like
[1476.14 --> 1476.64]  like
[1476.64 --> 1476.90]  glue
[1476.90 --> 1477.18]  which
[1477.18 --> 1477.60]  I think
[1477.60 --> 1478.58]  for such
[1478.58 --> 1479.02]  a reduction
[1479.02 --> 1479.80]  in size
[1479.80 --> 1480.56]  with
[1480.56 --> 1481.50]  only a
[1481.50 --> 1482.06]  very small
[1482.06 --> 1482.44]  in some
[1482.44 --> 1483.00]  cases
[1483.00 --> 1483.72]  negligible
[1483.72 --> 1484.18]  penalty
[1484.18 --> 1484.38]  and
[1484.38 --> 1484.84]  performance
[1484.84 --> 1485.10]  it's
[1485.10 --> 1485.28]  just
[1485.28 --> 1485.70]  really
[1485.70 --> 1486.18]  encouraging
[1486.18 --> 1486.74]  to see
[1486.74 --> 1487.64]  so
[1487.64 --> 1488.10]  since
[1488.10 --> 1488.40]  we're
[1488.40 --> 1488.74]  fortunate
[1488.74 --> 1489.10]  that you're
[1489.10 --> 1489.48]  kind of
[1489.48 --> 1489.80]  an expert
[1489.80 --> 1490.20]  in this
[1490.20 --> 1490.52]  topic
[1490.52 --> 1490.86]  to some
[1490.86 --> 1491.14]  degree
[1491.14 --> 1491.66]  I've
[1491.66 --> 1491.94]  seen
[1491.94 --> 1492.40]  lately
[1492.40 --> 1493.14]  a lot
[1493.14 --> 1493.42]  of
[1493.42 --> 1493.90]  different
[1493.90 --> 1494.46]  articles
[1494.46 --> 1494.74]  about
[1494.74 --> 1495.00]  different
[1495.00 --> 1495.32]  types
[1495.32 --> 1495.70]  of
[1495.70 --> 1496.26]  compression
[1496.26 --> 1497.06]  and
[1497.06 --> 1497.36]  different
[1497.36 --> 1497.90]  types
[1497.90 --> 1498.26]  of
[1498.26 --> 1498.76]  architecture
[1498.76 --> 1499.38]  construction
[1499.38 --> 1500.44]  in an
[1500.44 --> 1500.68]  effort
[1500.68 --> 1501.06]  to make
[1501.06 --> 1501.30]  it more
[1501.30 --> 1501.84]  performant
[1501.84 --> 1502.32]  do you
[1502.32 --> 1502.48]  have
[1502.48 --> 1502.68]  any
[1502.68 --> 1503.06]  insight
[1503.06 --> 1503.50]  into
[1503.50 --> 1504.26]  how
[1504.26 --> 1504.52]  they
[1504.52 --> 1504.74]  might
[1504.74 --> 1504.96]  be
[1504.96 --> 1505.34]  approaching
[1505.34 --> 1505.62]  that
[1505.62 --> 1505.86]  or
[1505.86 --> 1506.34]  even
[1506.34 --> 1507.24]  if not
[1507.24 --> 1507.68]  how
[1507.68 --> 1507.94]  would you
[1507.94 --> 1508.16]  tend
[1508.16 --> 1508.90]  to do
[1508.90 --> 1509.08]  that
[1509.08 --> 1509.36]  and what
[1509.36 --> 1509.60]  kind
[1509.60 --> 1509.72]  of
[1509.72 --> 1510.18]  benefits
[1510.18 --> 1510.80]  can you
[1510.80 --> 1511.14]  get out
[1511.14 --> 1511.42]  and what
[1511.42 --> 1511.56]  kind
[1511.56 --> 1511.66]  of
[1511.66 --> 1512.20]  applications
[1512.20 --> 1512.60]  might
[1512.60 --> 1512.76]  it
[1512.76 --> 1513.12]  enable
[1513.12 --> 1513.76]  yeah
[1513.76 --> 1514.32]  definitely
[1514.32 --> 1514.88]  I'm
[1514.88 --> 1515.52]  not an
[1515.52 --> 1515.84]  expert
[1515.84 --> 1516.48]  in all
[1516.48 --> 1517.04]  areas
[1517.04 --> 1517.34]  of
[1517.34 --> 1517.60]  this
[1517.60 --> 1517.82]  field
[1517.82 --> 1518.04]  there's
[1518.04 --> 1518.28]  a lot
[1518.28 --> 1518.58]  of
[1518.58 --> 1518.98]  different
[1518.98 --> 1519.50]  techniques
[1519.50 --> 1519.78]  used
[1519.78 --> 1520.00]  here
[1520.00 --> 1520.32]  of course
[1520.32 --> 1520.54]  there's
[1520.54 --> 1520.92]  a lot
[1520.92 --> 1521.12]  of
[1521.12 --> 1522.24]  people
[1522.24 --> 1522.58]  working
[1522.58 --> 1522.94]  in this
[1522.94 --> 1523.28]  area
[1523.28 --> 1523.68]  you know
[1523.68 --> 1524.28]  Intel
[1524.28 --> 1525.46]  and Google
[1525.46 --> 1526.08]  and others
[1526.08 --> 1526.52]  are working
[1526.52 --> 1527.42]  to kind
[1527.42 --> 1528.08]  of shrink
[1528.08 --> 1528.46]  down
[1528.46 --> 1528.98]  models
[1528.98 --> 1529.54]  to put
[1529.54 --> 1529.74]  them
[1529.74 --> 1529.94]  on
[1529.94 --> 1530.36]  smartphones
[1530.36 --> 1530.92]  or
[1530.92 --> 1531.56]  even
[1531.56 --> 1532.62]  microcontrollers
[1532.62 --> 1532.94]  and other
[1532.94 --> 1533.30]  things
[1533.30 --> 1534.18]  and so
[1534.18 --> 1535.02]  there's a lot
[1535.02 --> 1535.28]  of work
[1535.28 --> 1535.74]  going on
[1535.74 --> 1535.98]  there
[1535.98 --> 1536.86]  some of
[1536.86 --> 1537.36]  the methods
[1537.36 --> 1537.60]  kind
[1537.60 --> 1538.02]  of fall
[1538.02 --> 1538.40]  under
[1538.40 --> 1539.30]  I think
[1539.30 --> 1539.56]  what's
[1539.56 --> 1539.88]  called
[1539.88 --> 1540.30]  pruning
[1540.30 --> 1540.74]  which
[1540.74 --> 1541.80]  is kind
[1541.80 --> 1542.10]  of like
[1542.10 --> 1542.68]  cutting out
[1542.68 --> 1543.18]  parts of
[1543.18 --> 1543.68]  your network
[1543.68 --> 1544.14]  that might
[1544.14 --> 1544.74]  not be
[1544.74 --> 1545.24]  having an
[1545.24 --> 1545.66]  impact
[1545.66 --> 1546.38]  hopefully
[1546.38 --> 1546.86]  I'm saying
[1546.86 --> 1547.34]  that somewhat
[1547.34 --> 1548.02]  right as I'm
[1548.02 --> 1548.58]  not an
[1548.58 --> 1549.10]  expert on
[1549.10 --> 1549.34]  that
[1549.34 --> 1550.20]  I had a
[1550.20 --> 1550.70]  conversation
[1550.70 --> 1551.32]  with a
[1551.32 --> 1552.50]  professor at
[1552.50 --> 1553.00]  Georgia State
[1553.00 --> 1553.38]  who was
[1553.38 --> 1554.46]  doing a
[1554.46 --> 1554.92]  version of
[1554.92 --> 1555.38]  that for
[1555.38 --> 1555.80]  compression
[1555.80 --> 1556.70]  and so
[1556.70 --> 1556.92]  yeah
[1556.92 --> 1557.38]  keep going
[1557.38 --> 1557.64]  I wasn't
[1557.64 --> 1557.88]  trying to
[1557.88 --> 1558.16]  cut you
[1558.16 --> 1558.40]  off
[1558.40 --> 1558.76]  yeah
[1558.76 --> 1559.08]  no
[1559.08 --> 1559.90]  so that's
[1559.90 --> 1560.08]  like
[1560.08 --> 1560.38]  you could
[1560.38 --> 1560.66]  kind of
[1560.66 --> 1561.06]  think about
[1561.06 --> 1561.30]  that
[1561.30 --> 1561.76]  technique
[1561.76 --> 1562.14]  as a
[1562.14 --> 1562.32]  like
[1562.32 --> 1562.84]  you train
[1562.84 --> 1563.08]  your
[1563.08 --> 1563.50]  model
[1563.50 --> 1564.08]  and then
[1564.08 --> 1564.54]  afterwards
[1564.54 --> 1564.96]  you go
[1564.96 --> 1565.12]  through
[1565.12 --> 1565.56]  this sort
[1565.56 --> 1565.68]  of
[1565.68 --> 1566.22]  optimization
[1566.22 --> 1567.18]  or compilation
[1567.18 --> 1567.78]  which
[1567.78 --> 1568.10]  kind of
[1568.10 --> 1568.42]  prunes
[1568.42 --> 1569.10]  things out
[1569.10 --> 1569.68]  or makes
[1569.68 --> 1570.26]  the model
[1570.26 --> 1571.06]  smaller
[1571.06 --> 1571.44]  so it's
[1571.44 --> 1571.98]  kind of
[1571.98 --> 1572.26]  like a
[1572.26 --> 1573.04]  post-processing
[1573.04 --> 1573.22]  thing
[1573.22 --> 1573.50]  if that
[1573.50 --> 1574.00]  makes sense
[1574.00 --> 1574.20]  do you
[1574.20 --> 1574.48]  think that'll
[1574.48 --> 1574.94]  be common
[1574.94 --> 1575.78]  in terms
[1575.78 --> 1576.22]  of as a
[1576.22 --> 1576.60]  technique
[1576.60 --> 1577.30]  in this
[1577.30 --> 1577.66]  area
[1577.66 --> 1578.10]  you know
[1578.10 --> 1578.52]  with you
[1578.52 --> 1579.14]  doing NLP
[1579.14 --> 1579.46]  all the
[1579.46 --> 1579.78]  time
[1579.78 --> 1580.80]  and you
[1580.80 --> 1580.94]  know
[1580.94 --> 1581.74]  is this
[1581.74 --> 1581.92]  going to
[1581.92 --> 1582.16]  be a
[1582.16 --> 1582.38]  standard
[1582.38 --> 1582.82]  part of
[1582.82 --> 1583.14]  NLP
[1583.14 --> 1583.74]  deployment
[1583.74 --> 1584.04]  going
[1584.04 --> 1584.38]  forward
[1584.38 --> 1585.00]  yeah
[1585.00 --> 1585.38]  I think
[1585.38 --> 1585.64]  it'll
[1585.64 --> 1586.20]  probably
[1586.20 --> 1586.84]  at least
[1586.84 --> 1587.28]  based on
[1587.28 --> 1587.44]  my
[1587.44 --> 1587.86]  understanding
[1587.86 --> 1588.22]  it'll
[1588.22 --> 1588.72]  depend
[1588.72 --> 1589.50]  on the
[1589.50 --> 1589.98]  the
[1589.98 --> 1590.42]  type of
[1590.42 --> 1590.82]  model
[1590.82 --> 1591.08]  the
[1591.08 --> 1591.34]  type
[1591.34 --> 1591.50]  of
[1591.50 --> 1591.96]  task
[1591.96 --> 1592.26]  and
[1592.26 --> 1592.52]  also
[1592.52 --> 1592.76]  the
[1592.76 --> 1593.04]  type
[1593.04 --> 1593.26]  of
[1593.26 --> 1593.70]  target
[1593.70 --> 1594.44]  architecture
[1598.10 --> 1598.48]  need
[1598.48 --> 1598.78]  to
[1598.78 --> 1599.14]  get
[1599.14 --> 1599.88]  I think
[1599.88 --> 1600.14]  that
[1600.14 --> 1600.52]  some
[1600.52 --> 1600.76]  of the
[1600.76 --> 1601.12]  goals
[1601.12 --> 1601.54]  of
[1601.54 --> 1601.72]  the
[1601.72 --> 1601.96]  hugging
[1601.96 --> 1602.34]  face
[1602.34 --> 1602.80]  team
[1602.80 --> 1603.62]  were to
[1603.62 --> 1603.98]  get the
[1603.98 --> 1604.26]  model
[1604.26 --> 1604.58]  small
[1604.58 --> 1604.80]  enough
[1604.80 --> 1605.08]  to where
[1605.08 --> 1605.36]  they could
[1605.36 --> 1605.74]  run it
[1605.74 --> 1606.16]  efficiently
[1606.16 --> 1606.82]  in production
[1606.82 --> 1608.22]  and maybe
[1608.22 --> 1609.64]  on smartphones
[1609.64 --> 1609.86]  right
[1609.86 --> 1610.30]  which still
[1610.30 --> 1610.72]  are actually
[1610.72 --> 1611.26]  pretty
[1611.26 --> 1612.22]  computationally
[1612.22 --> 1612.66]  powerful
[1612.66 --> 1613.42]  if we
[1613.42 --> 1613.80]  at least
[1613.80 --> 1614.36]  compare them
[1614.36 --> 1614.70]  to like
[1614.70 --> 1615.72]  microcontrollers
[1615.72 --> 1616.00]  sure
[1616.00 --> 1616.44]  but so
[1616.44 --> 1616.94]  they use
[1616.94 --> 1617.22]  this
[1617.22 --> 1617.76]  technique
[1617.76 --> 1618.74]  called
[1618.74 --> 1619.30]  knowledge
[1619.30 --> 1620.22]  distillation
[1620.22 --> 1620.80]  and that's
[1620.80 --> 1621.28]  why the
[1621.28 --> 1622.12]  model is
[1622.12 --> 1622.44]  called
[1622.44 --> 1623.80]  distilbert
[1623.80 --> 1624.06]  or
[1624.06 --> 1625.28]  distilbert
[1625.28 --> 1626.16]  which has
[1626.16 --> 1626.52]  to be a
[1626.52 --> 1626.88]  knockoff
[1626.88 --> 1627.22]  Dilbert
[1627.22 --> 1627.52]  right
[1627.52 --> 1629.60]  they should
[1629.60 --> 1629.98]  have come
[1629.98 --> 1630.38]  up with
[1630.38 --> 1631.04]  a logo
[1631.04 --> 1631.86]  as such
[1631.86 --> 1632.38]  yeah
[1632.38 --> 1632.90]  so this
[1632.90 --> 1633.20]  model
[1633.20 --> 1633.60]  you might
[1633.60 --> 1633.92]  have heard
[1633.92 --> 1634.18]  of
[1634.18 --> 1634.64]  sort of
[1634.64 --> 1635.02]  teacher
[1635.02 --> 1635.70]  student
[1635.70 --> 1636.30]  training
[1636.30 --> 1636.78]  models
[1636.78 --> 1637.20]  and the
[1637.20 --> 1637.56]  idea
[1637.56 --> 1637.96]  is
[1637.96 --> 1639.14]  I think
[1639.14 --> 1639.50]  again
[1639.50 --> 1639.84]  you know
[1639.84 --> 1640.18]  please
[1640.18 --> 1640.54]  our
[1640.54 --> 1640.88]  listeners
[1640.88 --> 1641.60]  correct me
[1641.60 --> 1641.98]  if I'm
[1641.98 --> 1642.26]  wrong
[1642.26 --> 1642.90]  but I
[1642.90 --> 1643.08]  think
[1643.08 --> 1643.74]  the basic
[1643.74 --> 1644.18]  idea
[1644.18 --> 1644.62]  is that
[1644.62 --> 1645.22]  you have
[1645.22 --> 1645.58]  a sort
[1645.58 --> 1645.68]  of
[1645.68 --> 1645.96]  teacher
[1645.96 --> 1646.46]  model
[1646.46 --> 1647.16]  is a
[1647.16 --> 1647.50]  larger
[1647.50 --> 1648.14]  scale
[1648.14 --> 1648.78]  model
[1648.78 --> 1649.40]  maybe
[1649.40 --> 1649.78]  like
[1649.78 --> 1650.14]  full
[1650.14 --> 1650.54]  BERT
[1650.54 --> 1650.94]  let's
[1650.94 --> 1651.14]  say
[1651.14 --> 1651.74]  and then
[1651.74 --> 1652.08]  you
[1652.08 --> 1652.64]  have a
[1652.64 --> 1653.04]  smaller
[1653.04 --> 1653.60]  model
[1653.60 --> 1654.54]  that
[1654.54 --> 1655.00]  is
[1655.00 --> 1655.46]  supervised
[1655.46 --> 1656.00]  during
[1656.00 --> 1656.40]  training
[1656.40 --> 1656.82]  by the
[1656.82 --> 1657.14]  larger
[1657.14 --> 1657.50]  model
[1657.52 --> 1657.82]  so you
[1657.82 --> 1658.14]  try to
[1658.14 --> 1658.44]  get as
[1658.44 --> 1658.94]  close as
[1658.94 --> 1659.32]  you can
[1659.32 --> 1659.70]  to the
[1659.70 --> 1659.98]  larger
[1659.98 --> 1660.52]  model's
[1660.52 --> 1660.98]  performance
[1660.98 --> 1662.20]  and output
[1662.20 --> 1663.02]  distribution
[1663.02 --> 1664.42]  using this
[1664.42 --> 1665.02]  kind of
[1665.02 --> 1665.38]  teacher
[1665.38 --> 1666.14]  student
[1666.14 --> 1666.90]  supervision
[1666.90 --> 1668.14]  and that's
[1668.14 --> 1668.44]  kind of
[1668.44 --> 1668.82]  interesting
[1668.82 --> 1669.46]  because you
[1669.46 --> 1669.80]  kind of
[1669.80 --> 1670.22]  do a
[1670.22 --> 1670.72]  full scale
[1670.72 --> 1671.18]  training
[1671.18 --> 1671.54]  on a
[1671.54 --> 1671.80]  larger
[1671.80 --> 1672.22]  model
[1672.22 --> 1672.70]  so that
[1672.70 --> 1673.18]  still
[1673.18 --> 1673.78]  happens
[1673.78 --> 1674.64]  but maybe
[1674.64 --> 1675.30]  it doesn't
[1675.30 --> 1675.96]  happen
[1675.96 --> 1676.90]  over and
[1676.90 --> 1677.24]  over and
[1677.24 --> 1677.48]  over
[1677.48 --> 1677.96]  you kind
[1677.96 --> 1678.18]  of are
[1678.18 --> 1678.60]  able to
[1678.60 --> 1678.90]  train
[1678.90 --> 1679.28]  these
[1679.28 --> 1680.00]  smaller
[1680.00 --> 1680.52]  models
[1680.52 --> 1681.00]  to
[1681.00 --> 1682.08]  still get
[1682.08 --> 1682.86]  most of
[1682.86 --> 1683.12]  the
[1683.12 --> 1683.86]  performance
[1683.86 --> 1684.46]  out of
[1684.46 --> 1685.04]  the tasks
[1685.04 --> 1685.64]  that you're
[1685.64 --> 1686.10]  concerned
[1686.10 --> 1686.40]  with
[1686.40 --> 1686.60]  and
[1686.60 --> 1687.20]  so I
[1687.20 --> 1687.36]  think
[1687.36 --> 1687.78]  this was
[1687.78 --> 1688.28]  the type
[1688.28 --> 1688.98]  of methodology
[1688.98 --> 1690.32]  that Hugging Face
[1690.32 --> 1690.78]  employed
[1690.78 --> 1691.64]  Hugging Face
[1691.64 --> 1692.60]  is a very
[1692.60 --> 1693.26]  open source
[1693.26 --> 1694.10]  focused company
[1694.10 --> 1695.38]  and so in
[1695.38 --> 1696.56]  their blog post
[1696.56 --> 1697.38]  even they show
[1697.38 --> 1697.92]  some of the
[1697.92 --> 1698.76]  PyTorch code
[1698.76 --> 1699.56]  and illustrate
[1699.56 --> 1700.40]  how to do
[1700.40 --> 1701.42]  this in
[1701.42 --> 1702.00]  PyTorch
[1702.00 --> 1702.68]  so if you're
[1702.68 --> 1703.70]  interested in
[1703.70 --> 1704.98]  knowledge distillation
[1704.98 --> 1706.52]  and teacher
[1706.52 --> 1707.64]  student models
[1707.64 --> 1709.10]  and want to
[1709.10 --> 1709.80]  actually get
[1709.80 --> 1710.40]  your hands
[1710.40 --> 1711.42]  dirty trying out
[1711.42 --> 1711.96]  some of these
[1711.96 --> 1712.58]  things maybe
[1712.58 --> 1713.64]  trying your
[1713.64 --> 1714.02]  own
[1714.02 --> 1715.00]  distillation
[1715.00 --> 1715.96]  then that would
[1715.96 --> 1716.44]  be a good
[1716.44 --> 1717.12]  place to start
[1717.12 --> 1717.42]  I think
[1717.42 --> 1717.74]  because you
[1717.74 --> 1718.22]  could look at
[1718.22 --> 1718.92]  some hands-on
[1718.92 --> 1719.66]  examples
[1719.66 --> 1733.92]  this episode
[1733.92 --> 1734.46]  is brought
[1734.46 --> 1735.10]  to you by
[1735.10 --> 1735.72]  Brave
[1735.72 --> 1736.66]  the Brave
[1736.66 --> 1737.22]  team is on
[1737.22 --> 1737.70]  a mission
[1737.70 --> 1738.30]  to fix
[1738.30 --> 1738.84]  the web
[1738.84 --> 1739.48]  by building
[1739.48 --> 1739.90]  an open
[1739.90 --> 1740.30]  source
[1740.30 --> 1741.02]  privacy
[1741.02 --> 1741.56]  focused
[1741.56 --> 1742.54]  and performance
[1742.54 --> 1743.24]  oriented
[1743.24 --> 1743.84]  browser
[1743.84 --> 1744.80]  browse the
[1744.80 --> 1745.34]  web up to
[1745.34 --> 1745.90]  eight times
[1745.90 --> 1746.58]  faster than
[1746.58 --> 1746.94]  Chrome and
[1746.94 --> 1747.30]  Safari
[1747.30 --> 1748.60]  block ads
[1748.60 --> 1749.18]  and trackers
[1749.18 --> 1749.86]  by default
[1749.86 --> 1750.64]  and reward
[1750.64 --> 1751.12]  your favorite
[1751.12 --> 1751.92]  creators with
[1751.92 --> 1752.50]  the built-in
[1752.50 --> 1753.48]  basic attention
[1753.48 --> 1753.98]  token
[1753.98 --> 1755.36]  yes you heard
[1755.36 --> 1755.80]  that right
[1755.80 --> 1756.72]  a real-world
[1756.72 --> 1757.36]  use case
[1757.36 --> 1757.98]  for blockchain
[1757.98 --> 1759.20]  download Brave
[1759.20 --> 1759.72]  for free
[1759.72 --> 1760.48]  using the link
[1760.48 --> 1760.90]  in the show
[1760.90 --> 1761.58]  notes and give
[1761.58 --> 1762.40]  tipping a try
[1762.40 --> 1763.98]  on changelob.com
[1763.98 --> 1774.58]  okay so I
[1774.58 --> 1775.56]  found an article
[1775.56 --> 1776.42]  that was
[1776.42 --> 1777.06]  interesting to
[1777.06 --> 1777.48]  me from the
[1777.48 --> 1779.04]  title but as
[1779.04 --> 1779.62]  I started reading
[1779.62 --> 1779.98]  through it I
[1779.98 --> 1780.72]  realized that I
[1780.72 --> 1781.32]  actually know one
[1781.32 --> 1781.84]  of the authors
[1781.84 --> 1782.64]  it's a it's an
[1782.64 --> 1783.36]  article called
[1783.36 --> 1784.52]  three people
[1784.52 --> 1785.34]  centered design
[1785.34 --> 1786.04]  principles for
[1786.04 --> 1786.48]  deep learning
[1786.48 --> 1788.12]  and it's by
[1788.12 --> 1788.62]  dr.
[1788.62 --> 1789.70]  David Bray
[1789.70 --> 1790.74]  and R.
[1791.04 --> 1791.70]  Ray Wang
[1791.70 --> 1792.58]  and dr.
[1792.70 --> 1793.32]  David Bray
[1793.32 --> 1794.02]  and I both
[1794.02 --> 1794.48]  used to work
[1794.48 --> 1794.82]  at the same
[1794.82 --> 1795.46]  company together
[1795.46 --> 1796.04]  called Intel
[1796.04 --> 1796.46]  and it many
[1796.46 --> 1797.46]  years ago and
[1797.46 --> 1797.98]  we've kind of
[1797.98 --> 1798.90]  loosely kept in
[1798.90 --> 1800.00]  touch yeah so
[1800.00 --> 1800.80]  that that's
[1800.80 --> 1801.36]  that's super
[1801.36 --> 1802.12]  cool and I'm
[1802.12 --> 1802.84]  glad that you
[1802.84 --> 1803.58]  like when you
[1803.58 --> 1804.06]  said it out
[1804.06 --> 1804.76]  loud it made
[1804.76 --> 1805.36]  so much more
[1805.36 --> 1805.90]  sense to me
[1805.90 --> 1806.46]  because when I
[1806.46 --> 1807.10]  first read the
[1807.10 --> 1808.22]  title I was
[1808.22 --> 1808.94]  thinking like
[1808.94 --> 1810.20]  three people
[1810.20 --> 1811.30]  centered design
[1811.30 --> 1812.10]  I think how
[1812.10 --> 1812.60]  do you center
[1812.60 --> 1813.36]  design around
[1813.36 --> 1814.04]  three people I
[1814.04 --> 1814.70]  guess sometimes
[1814.70 --> 1815.46]  you're designing
[1815.46 --> 1816.42]  things for three
[1816.42 --> 1817.96]  people you know
[1817.96 --> 1818.90]  interacting kind
[1818.90 --> 1819.94]  of thing so my
[1819.94 --> 1820.74]  mind was totally
[1820.74 --> 1821.46]  in the in the
[1821.46 --> 1822.42]  wrong direction on
[1822.42 --> 1822.98]  that but thanks
[1822.98 --> 1823.54]  for clearing that
[1823.54 --> 1824.20]  up no no
[1824.20 --> 1824.82]  problem actually
[1824.82 --> 1825.78]  when I just a
[1825.78 --> 1826.34]  minute ago when I
[1826.34 --> 1827.02]  started saying it
[1827.02 --> 1827.74]  I started saying
[1827.74 --> 1828.44]  it that way in
[1828.44 --> 1829.56]  error as well and
[1829.56 --> 1830.56]  corrected myself if
[1830.56 --> 1831.54]  you notice so
[1831.54 --> 1832.70]  yeah a little bit
[1832.70 --> 1833.10]  of an awkward
[1833.10 --> 1834.04]  title there but
[1834.04 --> 1834.80]  very interesting
[1834.80 --> 1835.86]  article and a lot
[1835.86 --> 1836.70]  of that from my
[1836.70 --> 1837.40]  standpoint has to
[1837.40 --> 1837.90]  do with the fact
[1837.90 --> 1839.30]  that I'm a big
[1839.30 --> 1841.26]  advocate of keeping
[1841.26 --> 1842.46]  people and users
[1842.46 --> 1843.44]  at the center of
[1843.44 --> 1844.20]  technology and
[1844.20 --> 1845.24]  that's not an AI
[1845.24 --> 1846.36]  specific principle
[1846.36 --> 1847.72]  you know it's used
[1847.72 --> 1848.70]  across many different
[1848.70 --> 1849.92]  types of development
[1849.92 --> 1850.84]  processes and
[1850.84 --> 1852.26]  technologies and I
[1852.26 --> 1853.56]  like seeing this AI
[1853.56 --> 1854.82]  centered piece and I
[1854.82 --> 1855.74]  and when I go out
[1855.74 --> 1856.84]  and do you know
[1856.84 --> 1857.52]  some things like that
[1857.52 --> 1858.50]  around AI it's one of
[1858.50 --> 1859.24]  the points I'm often
[1859.24 --> 1860.12]  making so I was I
[1860.12 --> 1860.82]  was kind of delighted
[1860.82 --> 1862.38]  to see it and he
[1862.38 --> 1863.28]  kind of starts off
[1863.28 --> 1864.80]  talking about in
[1864.80 --> 1865.90]  deep learning and how
[1865.90 --> 1866.98]  you think about the
[1866.98 --> 1868.46]  outcome first with the
[1868.46 --> 1869.76]  intention of kind of
[1869.76 --> 1871.24]  avoiding bias
[1871.24 --> 1872.90]  bias in your process
[1872.90 --> 1874.00]  which is very easy
[1874.00 --> 1875.52]  to allow to happen
[1875.52 --> 1876.58]  as we all know it's
[1876.58 --> 1877.20]  probably the most
[1877.20 --> 1878.66]  common problem in
[1878.66 --> 1879.36]  deep learning that we
[1879.36 --> 1880.34]  all face with our
[1880.34 --> 1881.98]  data but how easy it
[1881.98 --> 1882.66]  is to get to
[1882.66 --> 1884.40]  potentially a bad
[1884.40 --> 1886.28]  outcome and so by
[1886.28 --> 1887.88]  kind of keeping your
[1887.88 --> 1889.40]  people centered outcome
[1889.40 --> 1890.52]  at the center of your
[1890.52 --> 1892.16]  process he kind of
[1892.16 --> 1893.02]  says you're more
[1893.02 --> 1894.08]  likely to get an
[1894.08 --> 1895.36]  outcome and better
[1895.36 --> 1896.76]  training than you
[1896.76 --> 1897.74]  would otherwise get
[1897.74 --> 1899.64]  and so the three kind
[1899.64 --> 1900.52]  of keys that he's
[1900.52 --> 1902.28]  talking about here is
[1902.28 --> 1904.44]  transparency and he's
[1904.44 --> 1905.46]  talking about the fact
[1905.46 --> 1906.94]  that you really need to
[1906.94 --> 1907.74]  understand what you're
[1907.74 --> 1909.16]  trying to get to and be
[1909.16 --> 1911.10]  very clear with what
[1911.10 --> 1912.22]  your intentions are in
[1912.22 --> 1914.06]  the training and make
[1914.06 --> 1915.56]  sure that your your data
[1915.56 --> 1917.78]  is is oriented on the
[1917.78 --> 1918.80]  outcome that you want
[1918.80 --> 1920.48]  and making sure that the
[1920.48 --> 1922.00]  process of doing the the
[1922.00 --> 1923.32]  model training is obvious
[1923.32 --> 1924.72]  in terms of what your
[1924.72 --> 1925.64]  inputs are to get your
[1925.64 --> 1926.84]  output as possible so that
[1926.84 --> 1928.00]  no mistakes are made and
[1928.00 --> 1929.40]  the second point is
[1929.40 --> 1931.20]  explainability and this
[1931.20 --> 1933.14]  is obviously a huge area
[1933.14 --> 1935.38]  inside AI research in
[1935.38 --> 1936.60]  terms of being able to
[1936.60 --> 1938.36]  understand how the
[1938.36 --> 1939.52]  inferences that a model
[1939.52 --> 1941.28]  is making how those
[1941.28 --> 1942.04]  inferences are being
[1942.04 --> 1943.96]  reached and so that's
[1943.96 --> 1945.04]  certainly in the industry
[1945.04 --> 1946.34]  I'm in where we have a
[1946.34 --> 1948.18]  lot of autonomy in terms
[1948.18 --> 1949.86]  of autonomous vehicles you
[1949.86 --> 1950.90]  know being able to put
[1950.90 --> 1952.32]  people's lives in that and
[1952.32 --> 1953.66]  being able to explain how
[1953.66 --> 1954.84]  your models getting that is
[1954.84 --> 1956.58]  is a is kind of a key to
[1956.58 --> 1957.58]  people having confidence
[1957.58 --> 1958.92]  in that and then the
[1958.92 --> 1959.86]  last thing is is
[1959.86 --> 1961.20]  reversibility and
[1961.20 --> 1962.94]  understanding how you
[1962.94 --> 1963.94]  reverse out of a model
[1963.94 --> 1965.26]  about what it knows it's
[1965.26 --> 1965.92]  kind of tied to
[1965.92 --> 1967.98]  explainability so you're
[1967.98 --> 1968.96]  really looking between
[1968.96 --> 1970.38]  transparency explainability
[1970.38 --> 1971.94]  and reversibility you're
[1971.94 --> 1972.82]  really looking at
[1972.82 --> 1974.14]  something where your
[1974.14 --> 1975.78]  outcome is a little bit
[1975.78 --> 1977.02]  less black box it's a
[1977.02 --> 1978.00]  little bit less mysterious
[1978.00 --> 1979.46]  and you have kind of a
[1979.46 --> 1980.54]  map on how you're working
[1980.54 --> 1981.22]  your way through the
[1981.22 --> 1982.48]  network obviously there
[1982.48 --> 1983.56]  are limitations on what
[1983.56 --> 1984.94]  we can do today and in
[1984.94 --> 1985.62]  each of those areas
[1985.62 --> 1986.64]  because obviously there's
[1986.64 --> 1987.80]  some fairly significant
[1987.80 --> 1989.38]  research going on but
[1989.38 --> 1991.26]  it's a good focus to try
[1991.26 --> 1992.68]  to kind of know that
[1992.68 --> 1993.34]  that's the direction
[1993.34 --> 1994.84]  you're going and so I'm
[1994.84 --> 1995.86]  looking forward to seeing
[1995.86 --> 1996.96]  where we go have you
[1996.96 --> 1997.94]  have you come across
[1997.94 --> 1998.94]  people-centered design
[1998.94 --> 1999.86]  principles in the past
[1999.86 --> 2000.10]  Daniel?
[2000.80 --> 2002.28]  Yeah I definitely have I
[2002.28 --> 2003.18]  mean I wouldn't say I
[2003.18 --> 2005.06]  haven't had any formal
[2005.06 --> 2006.78]  introduction to the topic
[2006.78 --> 2008.08]  but it's definitely come up
[2008.08 --> 2009.66]  in a lot of teams that
[2009.66 --> 2010.46]  I've worked on and
[2010.46 --> 2012.78]  different organizations and
[2012.78 --> 2014.32]  I think that it's you
[2014.32 --> 2015.22]  know it's a it's an
[2015.22 --> 2016.32]  important piece I just
[2016.32 --> 2017.90]  remember being in a
[2017.90 --> 2019.46]  meeting just the other
[2019.46 --> 2020.92]  day when one of my
[2020.92 --> 2021.82]  supervisors we were
[2021.82 --> 2023.00]  talking about you know
[2023.00 --> 2024.14]  the topic just came
[2024.14 --> 2025.02]  about you know in
[2025.02 --> 2026.30]  general what is the
[2026.30 --> 2027.84]  purpose of a commercial
[2027.84 --> 2029.94]  entity and you know the
[2029.94 --> 2031.48]  idea that oh it's it's
[2031.48 --> 2032.82]  to make profit came up
[2032.82 --> 2033.92]  at least that's part of
[2033.92 --> 2034.98]  it and you know he was
[2034.98 --> 2036.46]  saying well some people
[2036.46 --> 2037.76]  might think about it that
[2037.76 --> 2039.00]  way right but I think
[2039.00 --> 2041.12]  that whether you're a
[2041.12 --> 2042.50]  kind of social good
[2042.50 --> 2044.60]  company or organization
[2044.60 --> 2046.84]  non-profit or a
[2046.84 --> 2047.72]  commercial entity
[2047.72 --> 2048.78]  ultimately you're
[2048.78 --> 2049.92]  wanting to satisfy
[2049.92 --> 2051.04]  customers right and
[2051.04 --> 2052.08]  that should be at the
[2052.08 --> 2053.66]  very forefront of your
[2053.66 --> 2055.30]  design of your product
[2055.30 --> 2056.52]  of how you go about
[2056.52 --> 2057.26]  your business that
[2057.26 --> 2057.84]  you're wanting to
[2057.84 --> 2058.86]  satisfy your customer
[2058.86 --> 2060.36]  or your user in this
[2060.36 --> 2061.46]  article I was kind of
[2061.46 --> 2062.24]  wrestling and trying to
[2062.24 --> 2063.38]  figure out this idea of
[2063.38 --> 2064.80]  reversibility because
[2064.80 --> 2065.90]  initially when I read
[2065.90 --> 2066.50]  that I immediately
[2066.50 --> 2067.00]  thought of
[2067.00 --> 2068.24]  reproducibility which
[2068.24 --> 2069.86]  is something we've
[2069.86 --> 2070.96]  talked a lot about on
[2070.96 --> 2072.80]  the podcast and had an
[2072.80 --> 2073.82]  episode where we talked
[2073.82 --> 2075.50]  to one of the founders
[2075.50 --> 2076.92]  of Packaderm about data
[2076.92 --> 2078.24]  versioning and such but
[2078.24 --> 2080.62]  reversibility it seems it
[2080.62 --> 2081.76]  seems very different so I
[2081.76 --> 2084.02]  was kind of interested to
[2084.02 --> 2085.28]  to read a little bit more
[2085.28 --> 2085.86]  about that
[2085.86 --> 2087.14]  yeah that caught my
[2087.14 --> 2088.62]  attention as well and I
[2088.62 --> 2089.50]  also went to
[2089.50 --> 2091.30]  reproducibility initially in
[2091.30 --> 2092.10]  my head and went nope
[2092.10 --> 2093.18]  that's that's not what he's
[2093.18 --> 2094.34]  saying so it was
[2094.34 --> 2095.54]  interesting to see I'm
[2095.54 --> 2097.34]  kind of curious to see I
[2097.34 --> 2098.14]  think of the three
[2098.14 --> 2099.16]  concepts that he talks
[2099.16 --> 2100.44]  about that's the one that
[2100.44 --> 2102.46]  I probably need to ramp up
[2102.46 --> 2103.42]  on a little bit more and
[2103.42 --> 2104.76]  understand how it would be
[2104.76 --> 2106.50]  utilized here but at the
[2106.50 --> 2107.96]  end of the day I think the
[2107.96 --> 2109.48]  intention is good it it's
[2109.48 --> 2110.98]  funny I have a personal tie a
[2110.98 --> 2112.34]  little bit to this interest
[2112.34 --> 2113.80]  and that is you recently
[2113.80 --> 2115.40]  interviewed me on one of
[2115.40 --> 2116.76]  our episodes about high
[2116.76 --> 2118.30]  performance computing as it
[2118.30 --> 2119.88]  relates to AI and I can say
[2119.88 --> 2121.44]  that in the effort that we
[2121.44 --> 2123.38]  did at Lockheed Martin and are
[2123.38 --> 2125.56]  still doing that aspect of
[2125.56 --> 2127.38]  really centering on the person
[2127.38 --> 2129.12]  that is building the model and
[2129.12 --> 2130.10]  those outcomes that you're
[2130.10 --> 2131.24]  trying to achieve it was
[2131.24 --> 2132.88]  really one of the core
[2132.88 --> 2134.52]  design principles that we
[2134.52 --> 2136.20]  built into our effort to the
[2136.20 --> 2138.14]  point of it was every bit as
[2138.14 --> 2140.38]  important to do that for the
[2140.38 --> 2142.40]  ability of getting to the
[2142.40 --> 2144.60]  outcomes that we needed and
[2144.60 --> 2146.48]  and need as quickly as
[2146.48 --> 2147.56]  possible with very high
[2147.56 --> 2149.88]  fidelity and so anyway when I
[2149.88 --> 2151.52]  saw this article I was I was
[2151.52 --> 2152.80]  pretty pretty interested and
[2152.80 --> 2154.76]  maybe at some point maybe Dr.
[2154.84 --> 2156.36]  David Bray might come on to the
[2156.36 --> 2157.60]  podcast and tell us a little
[2157.60 --> 2159.06]  bit more about it and I
[2159.06 --> 2159.60]  think that would be an
[2159.60 --> 2161.16]  interesting episode yeah I
[2161.16 --> 2161.82]  definitely would be
[2161.82 --> 2164.06]  interested in hearing more
[2164.06 --> 2165.18]  about some of the details
[2165.18 --> 2166.76]  that he goes into so he also
[2166.76 --> 2168.86]  talks about creating data
[2168.86 --> 2170.86]  advocates which I thought was
[2170.86 --> 2173.46]  an interesting idea and also a
[2173.46 --> 2174.70]  huge piece of this which I
[2174.70 --> 2176.04]  think is important and was
[2176.04 --> 2178.06]  mentioned by one of our
[2178.06 --> 2180.02]  guests Lindsay Zulaga from
[2180.02 --> 2182.62]  HireVue is really putting a
[2182.62 --> 2184.42]  lot of effort into mindful
[2184.42 --> 2186.44]  monitoring systems to test
[2186.44 --> 2188.80]  data sets for biases so if I
[2188.80 --> 2189.94]  remember right I think
[2189.94 --> 2191.64]  Lindsay was talking and this
[2191.64 --> 2192.70]  probably intersects there
[2192.70 --> 2194.08]  where she was talking about
[2194.08 --> 2195.56]  well it's good if you put in
[2195.56 --> 2196.60]  some effort into thinking
[2196.60 --> 2197.92]  about your users and thinking
[2197.92 --> 2199.52]  about bias when you're
[2199.52 --> 2202.06]  training AI models but a lot
[2202.06 --> 2203.42]  of things drift over time and
[2203.42 --> 2204.42]  the performance of things
[2204.42 --> 2206.06]  drift over time your user base
[2206.06 --> 2208.36]  might change in different ways
[2208.36 --> 2210.28]  and so really putting in a
[2210.28 --> 2212.00]  monitoring system that is
[2212.00 --> 2214.10]  actually monitoring your
[2214.10 --> 2217.48]  online models to really
[2217.48 --> 2219.14]  judge whether you're
[2219.14 --> 2220.76]  actually dealing with any
[2220.76 --> 2224.34]  sort of bias in the input or
[2224.34 --> 2227.46]  if your model is is all the
[2227.46 --> 2229.30]  sudden generating predictions
[2229.30 --> 2231.10]  that are biased between two
[2231.10 --> 2232.98]  different groups or something
[2232.98 --> 2234.88]  like that so I think that's a
[2234.88 --> 2236.58]  really important piece of the
[2236.58 --> 2237.86]  puzzle and I'd love to hear
[2237.86 --> 2239.70]  more from the author here about
[2239.70 --> 2241.22]  the the types of monitoring
[2241.22 --> 2242.82]  systems that he has in mind he
[2242.82 --> 2246.08]  does even have like a a chart
[2246.08 --> 2247.78]  for the mindful monitoring
[2247.78 --> 2251.18]  system for AI which I think is
[2251.18 --> 2252.64]  is kind of interesting I'd like
[2252.64 --> 2253.68]  to hear more about that
[2253.68 --> 2255.94]  yeah I would too do you I'm just
[2255.94 --> 2257.24]  curious just from your own
[2257.24 --> 2259.24]  personal experience how do you
[2259.24 --> 2261.14]  when you're thinking about bias
[2261.14 --> 2262.32]  in the data that you're working
[2262.32 --> 2264.20]  with and however you may choose
[2264.20 --> 2265.78]  to monitor to try to address it
[2265.78 --> 2267.16]  ahead of time how do you
[2267.16 --> 2268.96]  approach that it's it's a little
[2268.96 --> 2270.72]  bit of a tangent but if there is
[2270.72 --> 2272.44]  one thing that every data
[2272.44 --> 2275.14]  scientist that works in AI is
[2275.14 --> 2276.50]  going to contend with it's that
[2276.50 --> 2277.94]  I'd love to know how you
[2277.94 --> 2279.94]  approach bias and what what are
[2279.94 --> 2282.22]  some of the processes or you
[2282.22 --> 2285.14]  know exercises you do to try to
[2285.14 --> 2286.82]  eliminate bias that might produce
[2286.82 --> 2288.52]  a bad outcome for you yeah I
[2288.52 --> 2289.52]  think I mean right now I'm
[2289.52 --> 2291.46]  working on a lot of language and
[2291.46 --> 2293.40]  voice tech and I think people
[2293.40 --> 2294.58]  when they think of bias they
[2294.58 --> 2296.38]  always think of some some sort
[2296.38 --> 2298.94]  of like discrimination against
[2298.94 --> 2301.78]  certain groups maybe like based
[2301.78 --> 2304.16]  on race or gender or whatever it
[2304.16 --> 2306.00]  is so I don't think it always has
[2306.00 --> 2307.74]  to be that side of things but of
[2307.74 --> 2309.12]  course we should be aware of that
[2309.12 --> 2310.54]  side of things I mean it could just
[2310.54 --> 2313.18]  be as simple as like I'm trying to
[2313.18 --> 2315.50]  translate this piece of text into
[2315.50 --> 2318.24]  Hindi but in my training data all I
[2318.24 --> 2320.24]  had was news data I only had
[2320.24 --> 2321.90]  politics data I didn't have any
[2321.90 --> 2324.44]  sports data right and so it could
[2324.44 --> 2326.26]  just be a simple bias in that data
[2326.26 --> 2327.62]  set in terms of what it's been
[2327.62 --> 2330.52]  exposed to but also you know
[2330.52 --> 2332.22]  there's there's certainly cases
[2332.22 --> 2337.10]  where I think marrying that sort of
[2337.10 --> 2339.80]  mindset with a mindset geared towards
[2339.80 --> 2341.66]  your users can be really powerful so
[2341.66 --> 2343.88]  especially with voice you want your
[2343.88 --> 2346.72]  voice system to work equally well for
[2346.72 --> 2348.42]  men and women right you want it to
[2348.42 --> 2349.90]  work equally well for those that are
[2349.90 --> 2352.00]  highly educated and and not highly
[2352.00 --> 2354.62]  educated maybe or those with certain
[2354.62 --> 2356.80]  accents and you know not certain
[2356.80 --> 2358.80]  accents or certain regions certain
[2358.80 --> 2361.98]  dialects or or not and so the only
[2361.98 --> 2364.64]  way that you're going to be able to you
[2364.64 --> 2366.94]  know be able to do well in that
[2366.94 --> 2370.70]  scenario is if you for one try to have
[2370.70 --> 2372.80]  diversity in your training data when
[2372.80 --> 2374.70]  you initially put that system together
[2374.70 --> 2377.48]  but also in terms of monitoring I mean
[2377.48 --> 2379.46]  one thing is you may never be able to
[2379.46 --> 2381.34]  anticipate all the types of people that
[2381.34 --> 2382.66]  are going to interact with your system
[2382.66 --> 2385.34]  right so you know anticipating that in
[2385.34 --> 2386.76]  advance and putting a monitoring
[2386.76 --> 2388.46]  system in place where you could
[2388.46 --> 2391.88]  actually tell oh in these scenarios our
[2391.88 --> 2394.52]  system isn't doing well based on you
[2394.52 --> 2396.42]  know our feedback we're getting or
[2396.42 --> 2397.84]  based on some metric that we're
[2397.84 --> 2399.94]  measuring and if you look further into
[2399.94 --> 2401.92]  that you could identify you know
[2401.92 --> 2403.22]  certain groups that are using your
[2403.22 --> 2404.78]  system that you just didn't expect
[2404.78 --> 2406.82]  before and so now you should circle
[2406.82 --> 2408.68]  back and integrate that into your
[2408.68 --> 2410.54]  training data so I think it's it's a
[2410.54 --> 2412.22]  cycle and you have to think about it
[2412.22 --> 2416.08]  both in production in training and kind
[2416.08 --> 2417.82]  of this feedback in between the two
[2417.82 --> 2421.00]  gotcha okay thanks for going there yeah
[2421.00 --> 2423.68]  definitely well I appreciate you coming
[2423.68 --> 2425.74]  up with some some good articles this
[2425.74 --> 2428.66]  week Chris before we head out like in
[2428.66 --> 2431.96]  all of our fully connected episodes we
[2431.96 --> 2435.34]  like to end with just a couple at least
[2435.34 --> 2438.74]  one learning resource that you can use as
[2438.74 --> 2440.36]  you're trying to learn more about the
[2440.36 --> 2444.28]  most recent trends in AI and kind of
[2444.28 --> 2447.12]  level up your skills so the one that we
[2447.12 --> 2448.74]  wanted to highlight this week which I've
[2448.74 --> 2452.34]  just really enjoyed over the past year is
[2452.34 --> 2454.50]  called and we may have even highlighted
[2454.50 --> 2455.98]  this before I'm not sure but it's worth
[2455.98 --> 2459.02]  highlighting again it's called papers with
[2459.02 --> 2460.98]  code so if you just go to papers with
[2460.98 --> 2465.14]  code calm it's a site that is essentially
[2465.14 --> 2468.74]  what it is named it's papers with code so
[2468.74 --> 2472.34]  it's AI research papers with the links to
[2472.34 --> 2476.26]  the code of the implementation on github and
[2476.26 --> 2478.82]  in some cases a sort of ranking on various
[2478.82 --> 2481.40]  tasks so on the on the front page if you go
[2481.40 --> 2483.40]  to this site it'll show trending research
[2483.40 --> 2485.56]  at the very top of the trending research
[2485.56 --> 2487.74]  right now is PyTorch transformers which
[2487.74 --> 2490.10]  is not a not a huge surprise there since
[2490.10 --> 2492.96]  hugging faces is killing it but you can click
[2492.96 --> 2495.24]  on PyTorch transformers on that paper it's
[2495.24 --> 2497.00]  going to take you right to the github repo
[2497.00 --> 2498.98]  of the implementation but you could also
[2498.98 --> 2500.92]  click on the paper right and it's going to
[2500.92 --> 2503.96]  take you to the to the paper for that and
[2504.62 --> 2507.12]  you can click on some of the papers are
[2507.12 --> 2509.68]  tagged with little things like oh this
[2509.68 --> 2513.26]  model or this paper is state-of-the-art in
[2513.26 --> 2515.92]  common-sense reasoning or something with a
[2515.92 --> 2518.16]  certain data set and so they've also got
[2518.16 --> 2521.64]  these pages of what are the most state-of-the-art
[2521.64 --> 2525.42]  papers with code for x task like you know
[2525.42 --> 2527.86]  reading comprehension or question answering
[2527.86 --> 2530.84]  or you know sentiment analysis or these
[2530.84 --> 2533.66]  different things so just an overall really
[2533.66 --> 2536.80]  well put together site and something where
[2536.80 --> 2538.94]  for example the other day I wanted to know
[2538.94 --> 2541.10]  what are people doing in terms of sign
[2541.10 --> 2543.62]  language recognition and who's doing the
[2543.62 --> 2546.38]  best stuff and I was able to get just a few
[2546.38 --> 2548.56]  leads on this site that led me in the right
[2548.56 --> 2552.08]  direction so I find it really useful yeah we
[2552.08 --> 2554.54]  have I do remember that we have highlighted
[2554.54 --> 2556.64]  it before but I also love it just like you
[2556.64 --> 2560.16]  do it is definitely worth highlighting again
[2560.16 --> 2562.80]  and and actually as I'm looking at this
[2562.80 --> 2565.40]  right now the third one is is one that I'm
[2565.40 --> 2566.98]  going to dive into as soon as we're done
[2566.98 --> 2569.58]  recording this podcast which is deep privacy
[2569.58 --> 2571.76]  a generative adversarial network for face
[2571.76 --> 2574.62]  anonymization you know because we we had an
[2574.62 --> 2577.86]  episode really recently on deep fakes and so
[2577.86 --> 2579.80]  I'm looking forward to diving into that one
[2579.80 --> 2581.70]  and see what they have but thank you for
[2581.70 --> 2583.44]  for highlighting this site again it's a
[2583.44 --> 2585.88]  fantastic one and after a little while we
[2585.88 --> 2587.54]  might even need to to do it one more time
[2587.54 --> 2590.06]  yeah for sure I think it's a good good
[2590.06 --> 2592.18]  reminder and a lot of things have been
[2592.18 --> 2594.12]  added over time on the site that have made
[2594.12 --> 2597.00]  it really useful well I appreciate you
[2597.00 --> 2599.52]  taking time before your vacation to talk
[2599.52 --> 2602.44]  through a little bit of AI stuff Chris I'm I
[2602.44 --> 2604.70]  wouldn't miss it this is fun stuff to me as
[2604.70 --> 2606.16]  far as I'm concerned vacations already
[2606.16 --> 2609.12]  started this is part of it so yeah I mean
[2609.12 --> 2610.18]  this is great I always love our
[2610.18 --> 2613.34]  conversations we always love to get the
[2613.34 --> 2616.10]  feedback that our listeners give us we
[2616.10 --> 2619.60]  talk to people on on slack because we have
[2619.60 --> 2621.94]  our slack community we talk to people on
[2621.94 --> 2625.52]  LinkedIn we talk on Twitter and a lot of
[2625.52 --> 2628.44]  what this show is is about is coming from
[2628.44 --> 2632.06]  engaged listeners who ask a question or say
[2632.06 --> 2633.46]  hey I would really love to hear more about
[2633.46 --> 2636.78]  this and so I really hope that that
[2636.78 --> 2638.96]  everyone keeps engaging us on this and
[2638.96 --> 2640.96]  let us know what you're interested in so
[2640.96 --> 2643.06]  that it's part of what makes this fun
[2643.06 --> 2646.50]  yep definitely do and have a have a great
[2646.50 --> 2648.20]  vacation Chris we'll talk to you soon
[2648.20 --> 2649.40]  thanks a lot take care Daniel
[2649.40 --> 2653.24]  all right thank you for tuning into this
[2653.24 --> 2655.62]  episode of practical AI if you enjoyed the
[2655.62 --> 2657.72]  show do us a favor go on iTunes give us a
[2657.72 --> 2659.60]  rating go in your podcast app and
[2659.60 --> 2661.56]  favorite it if you are on Twitter or social
[2661.56 --> 2663.18]  network share a link with a friend whatever
[2663.18 --> 2666.28]  you got to do share the show with a friend if you enjoyed it and bandwidth for
[2666.28 --> 2670.76]  changelog is provided by fastly learn more at fastly.com and we catch our
[2670.76 --> 2674.36]  errors before our users do here at changelog because of rollbar check them out at
[2674.36 --> 2679.24]  rollbar.com slash changelog and we're hosted on linode cloud servers and at
[2679.24 --> 2684.08]  linode.com slash changelog check them out support this show this episode is hosted by
[2684.08 --> 2690.28]  Daniel Whitenack and Chris Benson the music is by breakmaster cylinder and you can find more shows just like this at
[2690.28 --> 2702.60]  this at changelog.com when you go there pop in your email address get our weekly email keeping you up to date with the news and podcasts for developers in your inbox every single week thanks for tuning in we'll see you next week
[2702.60 --> 2708.44]  thank you
[2708.44 --> 2710.12]  to
