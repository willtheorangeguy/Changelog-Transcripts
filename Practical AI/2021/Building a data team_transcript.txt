[0.00 --> 2.86]  I created a little bit of a nightmare myself.
[3.14 --> 4.80]  I was at a previous employer.
[5.20 --> 7.74]  It was a large company that everyone's heard of.
[7.74 --> 11.60]  I was hired in to create the first AI team
[11.60 --> 12.52]  in that organization.
[13.04 --> 17.36]  And I made the mistake of hiring a team of data scientists.
[17.78 --> 20.10]  And in this case, they were true data scientists,
[20.56 --> 22.60]  but I ended up making assumptions
[22.60 --> 25.04]  about what those capabilities those individuals had.
[25.22 --> 27.22]  They were all probably better
[27.22 --> 29.66]  at the mathematics of deep learning than I was,
[29.66 --> 31.20]  but then when we got to the point
[31.20 --> 34.04]  where we needed to do DevOps and deployment and all that,
[34.32 --> 36.02]  there was absolutely no understanding.
[36.02 --> 39.38]  Everything from SQL to what is a container,
[39.58 --> 40.24]  all these things.
[40.64 --> 42.78]  It was an interesting ramp up experience.
[42.78 --> 44.50]  And I had to make some course corrections
[44.50 --> 47.34]  late on after hiring several people in that capacity.
[47.34 --> 48.88]  I had to specifically recognize
[48.88 --> 49.80]  that there were other skills
[49.80 --> 51.64]  that I had not addressed at all
[51.64 --> 53.50]  and go hire people for those themselves.
[56.28 --> 57.46]  Big thanks to our partners,
[57.56 --> 58.92]  Linode, Fastly, and LaunchDarkly.
[58.92 --> 59.84]  We love Linode.
[59.92 --> 61.34]  They keep it fast and simple.
[61.46 --> 63.84]  Check them out at linode.com slash changelog.
[64.06 --> 66.14]  Our bandwidth is provided by Fastly.
[66.48 --> 67.80]  Learn more at Fastly.com
[67.80 --> 70.02]  and get your feature flags powered by LaunchDarkly.
[70.18 --> 72.02]  Get a demo at LaunchDarkly.com.
[74.66 --> 77.54]  With advancements in AI and deep learning
[77.54 --> 79.22]  evolving at lightning pace,
[79.36 --> 80.90]  it's more important now than ever
[80.90 --> 84.08]  to research the best options suited to your unique needs.
[84.08 --> 87.56]  This is particularly true when building custom systems
[87.56 --> 89.42]  and those systems that are GPU heavy.
[89.90 --> 92.50]  Not only do the applications running on the system matter,
[92.68 --> 95.20]  but your AI infrastructure and budget constraints
[95.20 --> 97.02]  need to be front of mind as well.
[97.64 --> 102.32]  PSSC Labs, which is an HPC and AI custom solutions provider
[102.32 --> 103.16]  based in California,
[103.16 --> 106.10]  has been creating high performance computing systems
[106.10 --> 109.16]  to meet their clients' unique enterprise computing challenges
[109.16 --> 110.76]  for more than 25 years.
[110.76 --> 114.60]  And with cloud computing costs growing at astronomical rates,
[114.78 --> 117.18]  plus companies increasingly losing control
[117.18 --> 118.12]  of their data security,
[118.32 --> 121.26]  it is no wonder that enterprises and government agencies
[121.26 --> 123.14]  need to continually look for ways
[123.14 --> 124.72]  to take back control of their data.
[125.14 --> 128.48]  Solutions from PSSC Labs provide a cost-effective,
[128.80 --> 131.04]  highly secure, and performance guarantee
[131.04 --> 133.70]  that organizations need to reach their AI
[133.70 --> 134.96]  and machine learning goals.
[134.96 --> 138.12]  For more information and a free consultation,
[138.40 --> 141.88]  please visit PSSCLabs.com slash practical AI.
[142.18 --> 146.66]  Once again, that's PSSCLabs.com slash practical AI.
[154.74 --> 156.48]  Welcome to Practical AI,
[156.82 --> 159.32]  a weekly podcast that makes artificial intelligence
[159.32 --> 161.94]  practical, productive, and accessible to everyone.
[161.94 --> 165.22]  This is where conversations around AI, machine learning,
[165.38 --> 166.38]  and data science happen.
[166.62 --> 168.42]  Join the community and Slack with us
[168.42 --> 169.92]  around various topics of the show
[169.92 --> 171.44]  at kingjaw.com slash community,
[171.76 --> 172.74]  and follow us on Twitter.
[172.90 --> 174.46]  We're at Practical AI FM.
[180.48 --> 183.62]  Welcome to another Fully Connected episode
[183.62 --> 186.44]  where Chris and I keep you fully connected
[186.44 --> 189.44]  with everything that's happening in the AI community.
[189.44 --> 192.94]  We'll take some time to discuss the latest AI news,
[193.06 --> 194.84]  and we'll dig into some learning resources
[194.84 --> 197.40]  to help you level up your machine learning game.
[198.00 --> 198.94]  I'm Daniel Whitenack,
[199.04 --> 201.46]  a data scientist with SIL International,
[201.82 --> 204.50]  and I'm joined as always by my co-host, Chris Benson,
[204.74 --> 206.46]  who is a strategist at Lockheed Martin.
[206.84 --> 207.46]  How are you doing, Chris?
[207.82 --> 209.04]  I'm doing very well, Daniel.
[209.10 --> 209.58]  How's it going?
[209.78 --> 210.58]  Oh, it's going great.
[210.70 --> 213.08]  I hear almost congrats are in order.
[213.20 --> 215.44]  You're about to be an official pilot
[215.44 --> 218.48]  with your pilot's license.
[218.62 --> 219.06]  Is that right?
[219.06 --> 221.58]  I actually got the license last Sunday.
[221.68 --> 221.92]  Okay.
[222.24 --> 224.12]  So you are actually official.
[224.48 --> 226.16]  Frighteningly, I am a licensed pilot,
[226.16 --> 228.06]  and I know that has nothing to do with AI,
[228.40 --> 229.84]  but I appreciate the congrats.
[230.16 --> 232.62]  I'm sure there's some type of AI system
[232.62 --> 236.56]  that images the Earth or airplanes
[236.56 --> 238.84]  or manages air traffic control
[238.84 --> 240.78]  that will find you at some point.
[240.96 --> 242.28]  At some point, yes.
[242.50 --> 244.32]  Something like that might exist.
[244.68 --> 246.98]  And, you know, I do work for an aerospace company, too.
[246.98 --> 248.58]  So aside from what I'm doing,
[248.74 --> 250.50]  there might be things like that out there.
[250.66 --> 253.02]  I'm trying to remember the exact conversation we had,
[253.08 --> 254.84]  but there was like a conversation we had
[254.84 --> 255.98]  where we talked about this.
[256.08 --> 257.88]  I think it's persistent surveillance
[257.88 --> 260.40]  that is being promoted,
[260.54 --> 262.26]  I think, by at least one company
[262.26 --> 265.70]  where essentially you just record video
[265.70 --> 268.10]  of everything all the time,
[268.10 --> 269.32]  but in low quality.
[269.54 --> 269.94]  Yeah.
[269.94 --> 272.22]  So low enough quality to where you can't
[272.22 --> 275.02]  like personally identify all the people walking around
[275.02 --> 275.90]  and that sort of thing,
[275.90 --> 278.98]  but high enough quality to where if something goes down,
[278.98 --> 281.32]  then you can sort of backtrack
[281.32 --> 282.90]  and figure out what happened.
[283.58 --> 286.38]  So I don't know if that's happening above my head now.
[286.58 --> 288.40]  I don't think Lafayette, Indiana
[288.40 --> 290.60]  is maybe the highest priority target
[290.60 --> 292.40]  for that sort of system.
[292.72 --> 294.68]  But if I knew about something like that,
[294.70 --> 295.62]  I couldn't talk about it.
[295.82 --> 298.20]  Except, wait a minute,
[298.20 --> 300.60]  except my wife is English
[300.60 --> 303.18]  and so I spend a fair amount of time in the UK
[303.18 --> 306.58]  and they do have cameras pretty,
[306.78 --> 308.46]  just kind of all over the place there.
[308.54 --> 309.16]  Sure, sure.
[309.16 --> 310.62]  You cannot walk through London
[310.62 --> 312.66]  without being filmed all over the place.
[313.92 --> 315.22]  That's just normal life.
[315.40 --> 316.98]  I think you're in the US,
[317.14 --> 319.32]  that's becoming more and more normal life as well
[319.32 --> 320.46]  because I don't know about you,
[320.48 --> 322.58]  but everybody has a ring or a nest on their door
[322.58 --> 323.24]  at this point.
[323.94 --> 325.44]  Yeah, yeah, definitely a lot.
[325.54 --> 327.30]  And we have cameras in our,
[327.30 --> 329.06]  my wife's business,
[329.24 --> 330.76]  all around the business
[330.76 --> 332.90]  and all sorts of that stuff.
[333.26 --> 335.02]  The network video recorders now,
[335.24 --> 337.82]  you can record so much for so cheap
[337.82 --> 340.50]  because you just load them with some state drives
[340.50 --> 342.50]  or even spinning disks
[342.50 --> 345.36]  and you can get a lot of data.
[345.92 --> 348.32]  Yeah, it's kind of funny on our Nest Cam,
[348.58 --> 351.28]  we, you know how only like postal workers,
[351.58 --> 351.76]  you know,
[351.84 --> 353.46]  and we are talking a little bit about,
[353.50 --> 354.74]  you know, AI related stuff,
[354.74 --> 356.10]  but just on our Nest Cam,
[356.20 --> 357.60]  we found an Amazon driver
[357.60 --> 360.28]  who decided to put a package into our mailbox,
[360.52 --> 361.70]  which isn't legal and stuff.
[361.76 --> 363.98]  But I was kind of amazed in an age
[363.98 --> 366.18]  where not only are there cameras
[366.18 --> 367.74]  pretty much everywhere now,
[367.98 --> 369.82]  but now there's all of this automation.
[370.06 --> 371.74]  There's tons of deep learning analysis,
[372.24 --> 372.74]  super cheap,
[372.82 --> 374.02]  deployed all over the place.
[374.64 --> 376.20]  You have folks be careful what you do.
[376.28 --> 377.12]  There's somebody washing.
[377.62 --> 379.52]  The building that my wife's business is in,
[379.52 --> 381.10]  and then we own a second building,
[381.10 --> 384.28]  which her business will expand into.
[384.82 --> 386.68]  And right now there's not a lot in there
[386.68 --> 388.70]  and there's no internet over there, right?
[388.94 --> 389.94]  So what I,
[390.36 --> 394.56]  as a sort of quasi security camera solution,
[394.56 --> 398.00]  now they have like deer cams that people use
[398.00 --> 401.40]  or like wildlife cams that people put out in the-
[401.40 --> 402.40]  I have tons of those.
[402.54 --> 402.76]  Yeah.
[402.88 --> 404.14]  People put them out in the forest,
[404.14 --> 405.68]  but now they have the ones where,
[405.68 --> 408.06]  like when they see an event,
[408.06 --> 409.84]  they work off the cell signal,
[409.98 --> 411.58]  they can ping your phone,
[411.58 --> 414.92]  but also they have like built-in pre-trained models
[414.92 --> 416.80]  for like different animals,
[416.92 --> 419.12]  you know, the deer or turkeys or whatever.
[419.62 --> 421.38]  I don't think there was a people one
[421.38 --> 422.78]  in the one that I got.
[423.34 --> 425.40]  Like hopefully not that many people
[425.40 --> 427.00]  are hunting for people,
[427.00 --> 429.76]  but I mean, we're not using them for hunting.
[429.90 --> 431.52]  We're using them for this purpose,
[431.52 --> 432.70]  but yeah.
[433.00 --> 434.24]  You're raising a really good point.
[434.24 --> 437.04]  And that is AI is just everywhere these days.
[437.22 --> 438.72]  You know, these convolutional models
[438.72 --> 440.12]  are so cheap to deploy.
[440.76 --> 442.90]  And like aside from us talking about,
[442.96 --> 445.28]  you know, AI from the AI industry perspective,
[445.90 --> 447.28]  the animal protection nonprofit
[447.28 --> 448.52]  that my wife and I run,
[448.66 --> 450.18]  we have tons of those cameras.
[450.58 --> 452.90]  And yes, you are seeing these pre-trained models,
[453.34 --> 455.02]  you know, in these common tools
[455.02 --> 457.28]  and these consumers have no idea.
[457.36 --> 458.70]  A lot of data to sift through.
[458.76 --> 459.14]  It is.
[459.28 --> 460.92]  That is starting to happen right now.
[461.02 --> 461.88]  And I got to tell you,
[461.88 --> 464.64]  I would have thought that's about as far from AI
[464.64 --> 466.28]  as I could possibly be.
[466.50 --> 468.54]  We're seeing models now turn up
[468.54 --> 471.04]  in the most unlikely of places, it seems.
[471.68 --> 474.92]  I guess we can turn to what we had talked about
[474.92 --> 476.06]  discussing today,
[476.16 --> 478.70]  which I think is a really interesting topic.
[478.80 --> 480.96]  It's something I've been thinking a lot about recently
[480.96 --> 484.82]  is building a data team in a company.
[484.82 --> 488.30]  There is a really interesting article I saw.
[488.68 --> 488.98]  Yeah.
[489.04 --> 492.48]  Last week, very recent from Eric Bernhudson
[492.48 --> 496.24]  about building a data team at a mid-stage startup,
[496.40 --> 497.18]  a short story.
[497.76 --> 500.74]  And the format of the article is quite interesting.
[500.90 --> 501.92]  It's almost like a parable.
[502.10 --> 504.38]  So he's sort of taken a bunch of his experiences
[504.38 --> 506.46]  over the years, building data teams
[506.46 --> 509.86]  and wrap them up in this sort of parable
[509.86 --> 513.54]  about a data scientist coming into a new company
[513.54 --> 516.46]  charged with building a data team
[516.46 --> 521.42]  and the experiences that such a person might encounter,
[521.54 --> 522.78]  which I think is quite intriguing
[522.78 --> 525.20]  and refreshing to read.
[525.72 --> 528.36]  You had shared the article with me before the episode
[528.36 --> 531.66]  and he puts it into the reader's perspective there.
[531.98 --> 533.66]  You know, you're the one going through it.
[533.74 --> 536.12]  You notice a lot of code starts to that kind of thing.
[536.42 --> 538.40]  It was an interesting perspective shift
[538.40 --> 539.62]  because it puts it onto the reader.
[539.90 --> 540.36]  I liked it.
[540.94 --> 542.04]  It definitely got me thinking
[542.04 --> 544.98]  about a lot of the experience that I've had in the past.
[545.06 --> 545.88]  And I don't know about you.
[545.94 --> 547.82]  You've been at several places, I'm sure.
[548.38 --> 549.24]  Both big and small.
[549.38 --> 550.66]  So as part of those experiences,
[550.66 --> 553.04]  I'm sure you've been charged at one time or another
[553.04 --> 556.76]  with maybe not always starting the first data team
[556.76 --> 560.12]  at a company, but building a data team at a company.
[560.12 --> 563.48]  Is that part of your experiences in the past?
[563.88 --> 564.56]  It is indeed.
[564.76 --> 567.92]  And actually, I have started the data team more than once.
[567.92 --> 570.10]  Just mainly because I've been working for a long time
[570.10 --> 572.10]  and, you know, a while back,
[572.36 --> 573.92]  companies didn't even have data teams.
[574.00 --> 574.72]  They didn't exist.
[574.88 --> 578.34]  And ironically, for a while, you just had a DBA,
[578.50 --> 579.66]  a database administrator,
[579.66 --> 582.72]  and that person was expected to do anything
[582.72 --> 585.64]  that had anything to do with data for a long time.
[585.98 --> 590.08]  The idea of data teams is a relatively recent thing
[590.08 --> 590.96]  in terms of mainstream.
[591.18 --> 593.54]  And when I say that, meaning a number of years now,
[593.64 --> 595.24]  but, you know, it hasn't been decades.
[595.24 --> 599.80]  Yeah, and by data team, it's probably worth us discussing
[599.80 --> 601.40]  even that term.
[601.70 --> 606.42]  In my mind, I have sort of this vision of a team
[606.42 --> 609.46]  of mostly data science-y people,
[609.80 --> 613.86]  but maybe with some kind of towards the side
[613.86 --> 615.80]  of infrastructure more,
[615.98 --> 619.46]  and some maybe more towards the side of experimentation
[619.46 --> 623.48]  and research or prototyping type of people.
[624.00 --> 625.28]  When you think of data team,
[625.42 --> 627.00]  what comes to your mind?
[627.28 --> 627.76]  I'm curious.
[628.10 --> 630.18]  Usually, it's a little bit different.
[630.32 --> 631.36]  It's still very unique.
[631.50 --> 634.68]  There's not a standard concept for what a data team is.
[635.32 --> 637.08]  And I've had some misfires in that.
[637.30 --> 638.36]  There are different roles,
[638.64 --> 640.74]  and those roles are as distinct
[640.74 --> 642.92]  as the software development world has become
[642.92 --> 645.12]  with developers and, you know,
[645.18 --> 647.76]  different DevSecOps people or DevOps people.
[648.00 --> 650.20]  It's maturing is what's really happening.
[650.32 --> 651.50]  It's been maturing rapidly
[651.50 --> 653.00]  because this AI thing,
[653.10 --> 655.28]  this deep learning taking over the world
[655.28 --> 657.10]  has been happening so fast.
[657.54 --> 658.90]  Before this era,
[659.38 --> 661.58]  not a lot of companies had dedicated data teams,
[661.68 --> 663.18]  and so we're still in that process
[663.18 --> 664.02]  of figuring it out.
[664.40 --> 665.96]  We have lots of them at my employer,
[665.96 --> 667.42]  and they don't all,
[667.82 --> 669.28]  even in the organization,
[669.58 --> 670.88]  they don't all think of themselves
[670.88 --> 671.94]  in the same construct.
[672.20 --> 673.88]  You know, you can ask different data teams,
[673.94 --> 674.58]  what is a data team,
[674.60 --> 675.54]  and they'll give you different answers.
[676.04 --> 677.74]  Yeah, one anecdote
[677.74 --> 680.18]  that I actually was discussing
[680.18 --> 681.64]  with someone recently,
[681.88 --> 683.50]  a friend from college,
[683.82 --> 685.50]  which I won't share the details
[685.50 --> 687.46]  because I didn't get his permission,
[687.76 --> 689.96]  but basically the story was
[689.96 --> 692.88]  he has an engineering background,
[693.20 --> 695.40]  is working in the industry,
[695.40 --> 697.20]  and he had an opportunity
[697.20 --> 698.80]  within the company to,
[699.44 --> 701.74]  because they knew he had some coding skills
[701.74 --> 703.90]  and some modeling skills
[703.90 --> 704.92]  and that sort of thing.
[705.02 --> 706.68]  They basically wanted him
[706.68 --> 708.50]  to sort of become a data scientist
[708.50 --> 710.22]  within the company
[710.22 --> 712.58]  because he had a lot of the industry knowledge,
[713.28 --> 714.64]  and they knew he was sort of gifted
[714.64 --> 716.96]  on the coding and programming
[716.96 --> 718.50]  and modeling side.
[718.86 --> 719.88]  So they said, you know,
[719.94 --> 721.84]  hey, why don't you sort of start
[721.84 --> 724.76]  our in-house data science team,
[724.76 --> 726.30]  and I think what he's found
[726.30 --> 728.54]  is there are people throughout the company
[728.54 --> 732.06]  that are doing data science-y things.
[732.06 --> 733.74]  They're not really coordinated
[733.74 --> 734.88]  maybe well yet.
[735.02 --> 737.70]  There's not a lot of like ML ops
[737.70 --> 740.46]  and sort of good operational
[740.46 --> 742.50]  and deployment strategies yet,
[742.72 --> 745.10]  and so that's a lot of what he's parsing through
[745.10 --> 747.50]  is what are those best practices,
[747.50 --> 749.66]  and they're not giving him,
[749.66 --> 753.14]  you know, a full data engineering team
[753.14 --> 755.02]  to solve all those things for him.
[755.58 --> 757.28]  They're saying, hey, you know,
[757.34 --> 758.72]  you figure out a way to do it
[758.72 --> 759.60]  with these people
[759.60 --> 760.58]  that have been identified
[760.58 --> 761.56]  as data scientists
[761.56 --> 762.54]  or data analysts
[762.54 --> 763.58]  throughout the company
[763.58 --> 764.62]  and saying, you know,
[764.70 --> 766.82]  hey, figure out how to deploy models
[766.82 --> 769.46]  such that people can use them,
[769.50 --> 771.62]  but you're going to have to figure it out,
[771.70 --> 773.20]  and we don't really have a lot
[773.20 --> 775.96]  of pre-built infrastructure for that.
[775.96 --> 778.90]  So, yeah, I mean, it's a big challenge.
[779.44 --> 780.34]  That actually happens
[780.34 --> 781.78]  at companies large and small.
[781.98 --> 783.04]  I've seen that at both,
[783.26 --> 784.18]  and it's interesting
[784.18 --> 785.22]  as you try to learn
[785.22 --> 787.94]  how people have moved in.
[788.04 --> 789.22]  I think a lot of early people
[789.22 --> 789.98]  have come in,
[790.34 --> 791.86]  which certainly includes me,
[792.02 --> 793.22]  and I think to some degree,
[793.32 --> 794.50]  to some degree includes you,
[794.64 --> 796.18]  from the software development side
[796.18 --> 797.88]  with less experience
[797.88 --> 800.74]  on kind of the pure data science-y world,
[800.84 --> 802.40]  and that there's a ramp up
[802.40 --> 803.96]  for people that are moving
[803.96 --> 805.12]  into those kind of roles
[805.12 --> 806.80]  because just because you've coded
[806.80 --> 808.14]  doesn't mean that you understand
[808.14 --> 809.80]  statistics deeply
[809.80 --> 811.52]  and understand the various
[811.52 --> 813.50]  mathematical constructs
[813.50 --> 815.14]  that you need to apply to this.
[815.30 --> 816.26]  And so I know for me,
[816.58 --> 818.02]  some of which I had in school
[818.02 --> 819.04]  a long time ago,
[819.48 --> 820.70]  but there was definitely
[820.70 --> 821.66]  a ramp up for me
[821.66 --> 823.18]  to be able to be productive,
[823.66 --> 825.26]  especially four or five,
[825.38 --> 826.20]  six years ago,
[826.64 --> 826.98]  you know,
[827.06 --> 828.18]  when before things
[828.18 --> 829.10]  were quite so popular
[829.10 --> 830.58]  and when individuals
[830.58 --> 831.26]  were kind of doing
[831.26 --> 832.12]  everything end to end.
[832.12 --> 832.80]  Yeah,
[832.94 --> 834.34]  one of the points
[834.34 --> 835.84]  that was sort of brought out
[835.84 --> 836.68]  in this article
[836.68 --> 838.94]  is that sometimes companies
[838.94 --> 840.12]  hire in
[840.12 --> 842.04]  or promote people
[842.04 --> 843.06]  to do
[843.06 --> 844.78]  AI or whatever
[844.78 --> 845.92]  and figure out
[845.92 --> 846.88]  where it should be done
[846.88 --> 849.04]  and come to find out
[849.04 --> 850.38]  maybe the immediate needs
[850.38 --> 850.98]  aren't that
[850.98 --> 852.08]  sort of machine learning
[852.08 --> 853.20]  and AI stuff,
[853.26 --> 854.08]  or maybe you can't even
[854.08 --> 854.92]  get to those yet,
[855.00 --> 856.10]  but it's
[856.10 --> 856.92]  sort of
[856.92 --> 859.38]  equal type things
[859.38 --> 860.00]  or like
[860.00 --> 861.18]  people that say,
[861.18 --> 861.76]  you know,
[861.78 --> 862.74]  I wish I could figure out
[862.74 --> 863.42]  this number
[863.42 --> 864.56]  or this metric
[864.56 --> 866.46]  and it's totally accessible.
[866.72 --> 867.98]  They just can't translate
[867.98 --> 868.46]  that,
[868.72 --> 869.46]  those words
[869.46 --> 871.38]  into either
[871.38 --> 871.88]  SQL
[871.88 --> 873.00]  or scripting
[873.00 --> 874.00]  or whatever it takes
[874.00 --> 874.72]  to pull,
[874.98 --> 876.16]  extract that data out
[876.16 --> 877.34]  from its various sources
[877.34 --> 878.22]  and get that
[878.22 --> 879.00]  in front of them.
[879.12 --> 880.00]  That's sort of
[880.00 --> 880.92]  one of the things
[880.92 --> 882.30]  that is needed
[882.30 --> 883.62]  most often first.
[884.38 --> 885.02]  I created
[885.02 --> 885.56]  a little bit
[885.56 --> 886.22]  of a nightmare
[886.22 --> 887.22]  in that area
[887.22 --> 887.86]  myself.
[888.28 --> 889.00]  I was at
[889.00 --> 889.98]  a previous employer.
[889.98 --> 891.58]  I was hired in
[891.58 --> 892.38]  that it was a
[892.38 --> 893.42]  large company
[893.42 --> 894.06]  that everyone's
[894.06 --> 894.48]  heard of.
[894.68 --> 895.86]  I was hired in
[895.86 --> 896.78]  to create
[896.78 --> 897.44]  the first
[897.44 --> 898.34]  AI team
[898.34 --> 899.26]  in that organization
[899.26 --> 900.56]  and
[900.56 --> 901.74]  it was early enough
[901.74 --> 902.10]  to where I had
[902.10 --> 902.90]  come into that
[902.90 --> 903.36]  from
[903.36 --> 904.78]  generally smaller
[904.78 --> 905.88]  operations in that
[905.88 --> 907.72]  and I made the mistake
[907.72 --> 909.48]  of hiring a team
[909.48 --> 910.78]  of data scientists
[910.78 --> 912.22]  and in this case
[912.22 --> 912.96]  they were true
[912.96 --> 913.86]  data scientists
[913.86 --> 915.68]  but I ended up
[915.68 --> 916.68]  making assumptions
[916.68 --> 917.46]  about what those
[917.46 --> 918.08]  capabilities
[918.08 --> 919.50]  could do,
[919.64 --> 920.24]  what those
[920.24 --> 920.80]  capabilities
[920.80 --> 921.56]  those individuals
[921.56 --> 921.92]  had.
[922.46 --> 923.36]  They were all
[923.36 --> 924.52]  probably better
[924.52 --> 925.62]  at the mathematics
[925.62 --> 926.32]  of deep learning
[926.32 --> 927.30]  than I was.
[927.72 --> 928.68]  I had self-taught
[928.68 --> 929.40]  and self-studied
[929.40 --> 929.94]  and I could
[929.94 --> 930.90]  hold my own
[930.90 --> 932.30]  but that's what
[932.30 --> 932.86]  all of their
[932.86 --> 933.68]  formal education
[933.68 --> 934.34]  had been.
[934.46 --> 934.80]  They had all
[934.80 --> 935.70]  recently for the
[935.70 --> 936.06]  most part
[936.06 --> 936.80]  come out of
[936.80 --> 937.44]  college,
[937.52 --> 938.20]  out of university
[938.20 --> 939.18]  and
[939.18 --> 940.08]  but then
[940.08 --> 940.58]  when we got
[940.58 --> 941.14]  to the point
[941.14 --> 941.72]  where we needed
[941.72 --> 942.50]  to do DevOps
[942.50 --> 943.28]  and deployment
[943.28 --> 944.00]  and all that
[944.00 --> 945.48]  there was absolutely
[945.48 --> 946.32]  no understanding.
[946.56 --> 947.12]  Everything from
[947.12 --> 948.40]  SQL to
[948.40 --> 949.66]  what is a container
[949.66 --> 950.54]  all these things.
[950.92 --> 951.72]  It was an interesting
[951.72 --> 953.06]  ramp up experience
[953.06 --> 953.80]  and I had to make
[953.80 --> 954.80]  some course corrections
[954.80 --> 955.90]  late on after hiring
[955.90 --> 956.94]  several people
[956.94 --> 957.64]  in that capacity
[957.64 --> 958.58]  I had to specifically
[958.58 --> 959.42]  recognize that there
[959.42 --> 960.08]  were other skills
[960.08 --> 961.20]  that I had not
[961.20 --> 961.92]  addressed at all
[961.92 --> 963.22]  and go hire people
[963.22 --> 963.76]  for those
[963.76 --> 964.82]  themselves.
[968.20 --> 976.78]  We deserve a better
[976.78 --> 977.68]  internet and the
[977.68 --> 978.72]  brave team has the
[978.72 --> 979.86]  recipe for bringing
[979.86 --> 980.40]  it to us.
[980.52 --> 981.12]  Start with Google
[981.12 --> 982.10]  Chrome, keep the
[982.10 --> 983.10]  extensions, the dev
[983.10 --> 983.84]  tools and the
[983.84 --> 984.62]  rendering engine that
[984.62 --> 985.48]  make Chrome great.
[985.68 --> 986.28]  Rip out the Google
[986.28 --> 987.18]  bits, we don't need
[987.18 --> 987.32]  them.
[987.68 --> 988.88]  Mix in ad and
[988.88 --> 989.76]  tracker blocking by
[989.76 --> 991.04]  default, quick access
[991.04 --> 991.80]  to the Tor network
[991.80 --> 992.80]  for true private
[992.80 --> 994.00]  browsing and an
[994.00 --> 995.06]  opt-in reward system
[995.06 --> 995.98]  so you can get paid
[995.98 --> 996.86]  to view privacy
[996.86 --> 997.90]  respecting ads
[997.90 --> 998.68]  then turn around
[998.68 --> 999.22]  and use those
[999.22 --> 1000.24]  rewards to support
[1000.24 --> 1000.96]  your favorite web
[1000.96 --> 1001.84]  creators like us.
[1002.20 --> 1003.04]  Download Brave today
[1003.04 --> 1004.08]  using the link in the
[1004.08 --> 1004.86]  show notes and give
[1004.86 --> 1005.92]  tipping a try on
[1005.92 --> 1006.76]  changelog.com.
[1017.76 --> 1019.14]  You brought up a
[1019.14 --> 1019.90]  really interesting
[1019.90 --> 1021.32]  point which
[1021.32 --> 1022.54]  crosses over into
[1022.54 --> 1023.66]  the hiring side of
[1023.66 --> 1025.18]  things which is
[1025.18 --> 1025.94]  there's a few
[1025.94 --> 1026.70]  scenarios that could
[1026.70 --> 1027.28]  happen right?
[1027.28 --> 1028.40]  you could hire in
[1028.40 --> 1030.54]  like machine learning
[1030.54 --> 1032.80]  AI data scientists
[1032.80 --> 1033.92]  who are expecting
[1033.92 --> 1035.72]  to do machine
[1035.72 --> 1036.60]  learning AI
[1036.60 --> 1037.52]  advanced type
[1037.52 --> 1039.20]  things and if the
[1039.20 --> 1040.62]  immediate needs are
[1040.62 --> 1042.24]  hey take this
[1042.24 --> 1043.26]  disparate data and
[1043.26 --> 1044.12]  assemble it together
[1044.12 --> 1045.34]  and get it in in
[1045.34 --> 1046.30]  front of people
[1046.30 --> 1048.30]  there could be some
[1048.30 --> 1050.24]  job satisfaction
[1050.24 --> 1051.50]  issues that you
[1051.50 --> 1052.40]  might that you might
[1052.40 --> 1053.18]  run into just
[1053.18 --> 1054.16]  because you know I'm
[1054.16 --> 1055.00]  not saying that all
[1055.00 --> 1056.02]  people like that would
[1056.02 --> 1057.38]  think that that sort
[1057.38 --> 1058.18]  of thing is beneath
[1058.18 --> 1059.14]  them you know I
[1059.14 --> 1059.88]  think a lot of people
[1059.88 --> 1060.88]  enjoy dipping into
[1060.88 --> 1061.78]  that at some point
[1061.78 --> 1062.80]  or they might yeah
[1062.80 --> 1063.80]  they might I mean if
[1063.80 --> 1065.24]  a year goes by
[1065.24 --> 1066.64]  two years go by and
[1066.64 --> 1067.92]  like there's you know
[1067.92 --> 1068.68]  the only thing they've
[1068.68 --> 1069.68]  done is write sequel
[1069.68 --> 1071.86]  there's a mismatch at
[1071.86 --> 1072.80]  the same time like you
[1072.80 --> 1074.52]  were saying you know
[1074.52 --> 1076.04]  you could you could
[1076.04 --> 1078.12]  hire in the other
[1078.12 --> 1080.56]  way and then have
[1080.56 --> 1082.44]  trouble advancing into
[1082.44 --> 1083.80]  the more you know
[1083.80 --> 1085.20]  sophisticated analyses
[1085.20 --> 1086.18]  and that sort of
[1086.18 --> 1087.76]  thing so what is
[1087.76 --> 1089.14]  your take on how
[1089.14 --> 1090.12]  to parse out that
[1090.12 --> 1091.52]  that hiring bit and
[1091.52 --> 1092.40]  how to think about
[1092.40 --> 1094.20]  who who you should
[1094.20 --> 1095.40]  really be bringing in
[1095.40 --> 1096.54]  because that could
[1096.54 --> 1097.34]  create a lot of
[1097.34 --> 1098.56]  issues I have an
[1098.56 --> 1099.64]  answer for that but I
[1099.64 --> 1100.46]  think it's a little
[1100.46 --> 1101.50]  bit of a cheat on
[1101.50 --> 1102.66]  your question because I
[1102.66 --> 1103.42]  think the question
[1103.42 --> 1105.10]  assumes that you
[1105.10 --> 1106.76]  don't necessarily know
[1106.76 --> 1107.86]  all the things but
[1107.86 --> 1108.78]  I've had the benefit
[1108.78 --> 1109.84]  of a little bit of
[1109.84 --> 1110.86]  experience that going
[1110.86 --> 1111.66]  through this process
[1111.66 --> 1113.12]  several times now in
[1113.12 --> 1113.62]  several different
[1113.62 --> 1115.14]  organizations and so
[1115.14 --> 1117.02]  for me I would hire
[1117.02 --> 1119.82]  in to reflect the
[1119.82 --> 1121.82]  entire workflow so I
[1121.82 --> 1124.02]  know what a good
[1124.02 --> 1126.28]  data science including
[1126.28 --> 1127.32]  deep learning workflow
[1127.32 --> 1129.04]  looks like these days
[1129.04 --> 1130.28]  from beginning to end
[1130.28 --> 1132.00]  all of those things
[1132.00 --> 1132.82]  that have to happen
[1132.82 --> 1134.36]  from understanding the
[1134.36 --> 1136.28]  problem to identifying
[1136.28 --> 1137.74]  what kinds of models
[1137.74 --> 1138.98]  need to be there to
[1138.98 --> 1139.94]  how you would implement
[1139.94 --> 1140.74]  them what kind of
[1140.74 --> 1142.16]  equipment you need for
[1142.16 --> 1143.06]  those models the
[1143.06 --> 1144.80]  software how you do
[1144.80 --> 1146.78]  the DevOps or DevSecOps
[1146.78 --> 1148.42]  to get those all the
[1148.42 --> 1149.58]  way out to deployment
[1149.58 --> 1150.86]  to production and so
[1150.86 --> 1152.28]  there's the from the
[1152.28 --> 1154.04]  early conception almost
[1154.04 --> 1155.10]  at the business level
[1155.10 --> 1156.06]  all the way through
[1156.06 --> 1157.12]  those various steps to
[1157.12 --> 1158.20]  the end and you have
[1158.20 --> 1159.44]  something out there
[1159.44 --> 1160.60]  it's a model it's
[1160.60 --> 1161.26]  wrapped in software
[1161.26 --> 1161.86]  and it's doing
[1161.86 --> 1162.70]  something productive in
[1162.70 --> 1164.00]  the world at this
[1164.00 --> 1165.36]  point I would catalog
[1165.36 --> 1167.32]  those I know how much
[1167.32 --> 1169.12]  effort roughly would go
[1169.12 --> 1169.82]  into each of those
[1169.82 --> 1171.78]  areas ballpark and I
[1171.78 --> 1173.02]  hire against that kind
[1173.02 --> 1174.00]  of those levels of
[1174.00 --> 1174.90]  effort in those
[1174.90 --> 1176.20]  different stages to try
[1176.20 --> 1177.06]  to get a complete team
[1177.06 --> 1178.08]  and depending on what
[1178.08 --> 1178.90]  the budget is and how
[1178.90 --> 1181.02]  many people you know I
[1181.02 --> 1182.24]  will kind of group some
[1182.24 --> 1183.16]  of those tasks together
[1183.16 --> 1184.42]  or whatever and figure
[1184.42 --> 1185.40]  out what that is and
[1185.40 --> 1186.08]  also depends on the
[1186.08 --> 1187.14]  candidates I talk to I
[1187.14 --> 1188.40]  may make a change if I
[1188.40 --> 1189.46]  get a particularly
[1189.46 --> 1190.74]  capable candidate then
[1190.74 --> 1192.56]  that can change how I'm
[1192.56 --> 1193.50]  thinking about things on
[1193.50 --> 1195.30]  a tight budget what if
[1195.30 --> 1198.54]  the CEO that hires you
[1198.54 --> 1201.04]  in is expecting some
[1201.04 --> 1203.84]  cool AI data science
[1203.84 --> 1205.32]  machine learning type
[1205.32 --> 1207.56]  things but what you find
[1207.56 --> 1209.06]  out very quickly is that
[1209.06 --> 1211.12]  that actually isn't the
[1211.12 --> 1212.74]  most immediate need the
[1212.74 --> 1214.32]  most immediate need is
[1214.32 --> 1216.32]  data aggregation and
[1216.32 --> 1217.48]  getting some metrics in
[1217.48 --> 1218.96]  front of people how do
[1218.96 --> 1221.14]  you handle that situation
[1221.14 --> 1222.88]  with your with your
[1222.88 --> 1224.74]  leadership any any
[1224.74 --> 1225.90]  thoughts there first
[1225.90 --> 1226.68]  of all they always
[1226.68 --> 1228.30]  expect that that's not
[1228.30 --> 1229.88]  like what if that is
[1229.88 --> 1231.60]  every time because the
[1231.60 --> 1232.64]  people responsible for
[1232.64 --> 1233.90]  that even even people
[1233.90 --> 1235.46]  who are usually supposed
[1235.46 --> 1236.20]  to be technical
[1236.20 --> 1238.18]  leadership are beyond
[1238.18 --> 1239.48]  the details at the
[1239.48 --> 1240.48]  point they're making
[1240.48 --> 1241.28]  the decision they're
[1241.28 --> 1242.00]  far enough along in
[1242.00 --> 1243.42]  their career because they
[1243.42 --> 1244.22]  may not be handling
[1244.22 --> 1245.28]  those technical details
[1245.28 --> 1246.50]  on a day-to-day basis
[1246.50 --> 1247.90]  and therefore they don't
[1247.90 --> 1249.14]  really understand anymore
[1249.14 --> 1250.18]  even if they think they
[1250.18 --> 1252.86]  do and so there is a
[1252.86 --> 1254.18]  there is a gentle
[1254.18 --> 1255.70]  education process and
[1255.70 --> 1257.12]  there is a discussion
[1257.12 --> 1259.20]  of what happens based
[1259.20 --> 1260.14]  on you know if you if
[1260.14 --> 1261.26]  you just run forward
[1261.26 --> 1262.78]  and do it try to do
[1262.78 --> 1263.52]  deep learning when
[1263.52 --> 1264.92]  you're not set to be
[1264.92 --> 1265.48]  able to do it
[1265.48 --> 1266.76]  effectively you're
[1266.76 --> 1267.54]  running into a wall
[1267.54 --> 1268.96]  and the harder you try
[1268.96 --> 1269.78]  to do it the faster
[1269.78 --> 1270.44]  you're running into
[1270.44 --> 1272.26]  that that brick wall so
[1272.26 --> 1273.14]  there's a there's a bit
[1273.14 --> 1274.28]  of an education process
[1274.28 --> 1276.10]  and also there's even
[1276.10 --> 1277.38]  if there is an opera a
[1277.38 --> 1279.86]  clear opportunity to move
[1279.86 --> 1281.54]  move into some AI
[1281.54 --> 1282.60]  related work and
[1282.60 --> 1283.66]  machine learning stuff
[1283.66 --> 1286.98]  my experience is the
[1286.98 --> 1288.36]  right data that you
[1288.36 --> 1290.64]  need is usually very
[1290.64 --> 1292.76]  hard to get or it's
[1292.76 --> 1295.14]  very fragmented this
[1295.14 --> 1296.46]  article also talks about
[1296.46 --> 1298.22]  fragmented data and
[1298.22 --> 1300.06]  that sort of thing so
[1300.06 --> 1301.28]  I've been in places
[1301.28 --> 1305.18]  where you want to ask
[1305.18 --> 1306.86]  the question like okay
[1307.70 --> 1308.90]  to train this model I
[1308.90 --> 1310.92]  need all of this type
[1310.92 --> 1312.92]  of data but that's a
[1312.92 --> 1314.20]  sort of anti-pattern
[1314.20 --> 1316.52]  because maybe people
[1316.52 --> 1317.56]  are used to like let's
[1317.56 --> 1318.88]  say the example is in
[1318.88 --> 1319.96]  a financial institution
[1319.96 --> 1320.98]  or something like that
[1320.98 --> 1323.26]  but previous maybe
[1323.26 --> 1324.34]  support people or
[1324.34 --> 1325.48]  customer service people
[1325.48 --> 1327.10]  or even analysts or
[1327.10 --> 1327.74]  whatever they're maybe
[1327.74 --> 1328.70]  used to looking at a
[1328.70 --> 1329.86]  very small set of
[1329.86 --> 1331.08]  transactions or at a
[1331.08 --> 1332.64]  single transaction or
[1332.64 --> 1333.98]  a single user and all
[1333.98 --> 1335.76]  the things that's gone
[1335.76 --> 1337.14]  on for that user and
[1337.14 --> 1338.06]  so when you ask a
[1338.06 --> 1339.32]  question give me all
[1339.32 --> 1340.44]  the transactions of
[1340.44 --> 1342.14]  this type it's sort of
[1342.14 --> 1343.24]  an anti-pattern for
[1343.24 --> 1344.02]  how they've been
[1344.02 --> 1345.18]  looking at the data
[1345.18 --> 1346.30]  and their systems
[1346.30 --> 1347.70]  aren't really set up
[1347.70 --> 1349.12]  for that sort of
[1349.12 --> 1350.54]  query even so it may
[1350.54 --> 1353.14]  be that you have to
[1353.14 --> 1356.74]  push the infrastructure
[1356.74 --> 1358.18]  or rethink how you're
[1358.18 --> 1360.14]  getting the data or
[1360.14 --> 1360.96]  the patterns that
[1360.96 --> 1361.60]  people are pulling
[1361.60 --> 1362.62]  data in order for you
[1362.62 --> 1363.56]  to even set up your
[1363.56 --> 1364.72]  problem and have
[1364.72 --> 1365.88]  success in doing any
[1365.88 --> 1366.56]  type of modeling.
[1366.56 --> 1367.90]  I have had that same
[1367.90 --> 1368.88]  experience and
[1368.88 --> 1370.10]  ironically just because
[1370.10 --> 1370.76]  it's at the top of my
[1370.76 --> 1371.64]  mind I'm thinking about
[1371.64 --> 1372.62]  that same previous
[1372.62 --> 1374.02]  employer large company
[1374.02 --> 1375.00]  with a well-known
[1375.00 --> 1377.20]  name and lots of
[1377.20 --> 1378.24]  physical hardware
[1378.24 --> 1379.68]  products that come out
[1379.68 --> 1380.60]  of that organization
[1380.60 --> 1382.72]  they collect a fair
[1382.72 --> 1383.98]  amount of telemetry
[1383.98 --> 1385.20]  from those various
[1385.20 --> 1386.88]  products but what we
[1386.88 --> 1387.92]  discovered was based
[1387.92 --> 1389.12]  on the things that we
[1389.12 --> 1390.18]  wanted deep learning
[1390.18 --> 1392.34]  models to do and ways
[1392.34 --> 1393.78]  of improving that
[1393.78 --> 1395.00]  product's capabilities
[1395.00 --> 1396.60]  and the user experience
[1396.60 --> 1398.48]  that most of the
[1398.48 --> 1400.20]  telemetry was absolutely
[1400.20 --> 1401.22]  useless for our
[1401.22 --> 1401.66]  purposes.
[1401.94 --> 1403.80]  It was great for
[1403.80 --> 1405.04]  figuring out what went
[1405.04 --> 1405.98]  wrong with the product
[1405.98 --> 1407.18]  after the fact but it
[1407.18 --> 1408.66]  didn't actually it
[1408.66 --> 1409.66]  couldn't be used to
[1409.66 --> 1412.14]  teach a model how to
[1412.14 --> 1413.88]  more effectively do the
[1413.88 --> 1415.28]  capability and I think
[1415.28 --> 1416.98]  that's a common I in my
[1416.98 --> 1417.92]  experience we saw that
[1417.92 --> 1419.64]  across products and I
[1419.64 --> 1420.62]  think that that would
[1420.62 --> 1421.98]  probably hold true across
[1421.98 --> 1423.36]  many organizations where
[1423.36 --> 1424.66]  you where you may
[1424.66 --> 1425.52]  collect a lot of data
[1425.52 --> 1426.16]  but that doesn't mean
[1426.16 --> 1427.32]  it's the right data and
[1427.32 --> 1428.40]  it's not the data that's
[1428.40 --> 1428.96]  going to help you get
[1428.96 --> 1429.60]  where you want to go.
[1429.92 --> 1430.60]  When you enter an
[1430.60 --> 1431.80]  organization and you're
[1431.80 --> 1433.30]  building a data team
[1433.30 --> 1435.14]  you start interacting with
[1435.14 --> 1436.32]  product teams and
[1436.32 --> 1437.58]  customer support and
[1437.58 --> 1439.44]  that sort of thing if
[1439.44 --> 1441.34]  those teams aren't yet
[1441.34 --> 1443.44]  data driven what are
[1443.44 --> 1444.38]  some of the things that
[1444.38 --> 1446.08]  you think motivate those
[1446.08 --> 1447.28]  teams if it's not data
[1447.28 --> 1448.10]  how are they making
[1448.10 --> 1449.64]  their decisions in a
[1449.64 --> 1451.02]  non-data driven way
[1451.02 --> 1451.82]  because that's often
[1451.82 --> 1453.18]  what I've I've seen is
[1453.18 --> 1454.92]  like I start interacting
[1454.92 --> 1456.90]  with a product team or
[1456.90 --> 1457.84]  something like that and
[1457.84 --> 1459.60]  they aren't making data
[1459.60 --> 1461.30]  driven decisions one of
[1461.30 --> 1462.70]  the ways to think about
[1462.70 --> 1464.28]  how to change that
[1464.28 --> 1465.34]  culture is to think about
[1465.34 --> 1466.64]  what what is motivating
[1466.64 --> 1468.40]  them what has been your
[1468.40 --> 1469.52]  experience in the past in
[1469.52 --> 1470.52]  terms of the culture of
[1470.52 --> 1471.56]  the teams that you start
[1471.56 --> 1472.48]  interacting with when you
[1472.48 --> 1473.30]  build a data team.
[1473.62 --> 1474.40]  I think that's a huge
[1474.40 --> 1475.76]  issue meaning the word
[1475.76 --> 1477.12]  being culture and
[1477.12 --> 1479.10]  because when if in
[1479.10 --> 1480.80]  general to generalize and
[1480.80 --> 1481.74]  based on at least what
[1481.74 --> 1483.34]  I've seen when teams
[1483.34 --> 1484.40]  aren't using data to
[1484.40 --> 1485.62]  drive their decisions you
[1485.62 --> 1486.58]  know in an explicit
[1486.58 --> 1489.16]  objective manner then
[1489.16 --> 1491.12]  they're usually relying on
[1491.12 --> 1492.50]  experts or at least
[1492.50 --> 1494.68]  self-proclaimed experts and
[1494.68 --> 1495.88]  they're those decisions
[1495.88 --> 1498.56]  often are somewhat
[1498.56 --> 1500.18]  arbitrary and and off and
[1500.18 --> 1501.46]  oftentimes not consistent
[1501.46 --> 1503.40]  even even with that
[1503.40 --> 1504.76]  person's other decisions
[1504.76 --> 1506.54]  across time and across
[1506.54 --> 1508.82]  similar situations so and
[1508.82 --> 1510.36]  and in doing that there
[1510.36 --> 1511.32]  is a belief because
[1511.32 --> 1512.30]  they've built a business
[1512.30 --> 1513.40]  on it so this is one of
[1513.40 --> 1514.64]  those this is one of
[1514.64 --> 1515.96]  those kind of political
[1515.96 --> 1518.26]  cultural things that is
[1518.26 --> 1519.50]  deeply entrenched in an
[1519.50 --> 1521.56]  organization and that you
[1521.56 --> 1523.60]  as as the new leader of a
[1523.60 --> 1525.32]  data science team are
[1525.32 --> 1526.74]  forced to contend with and
[1526.74 --> 1528.08]  it's a really hard problem
[1528.08 --> 1529.60]  it's a it's a hard nut to
[1529.60 --> 1530.92]  crack they may have run
[1530.92 --> 1532.76]  years or even decades on
[1532.76 --> 1534.88]  that approach so you have
[1534.88 --> 1536.98]  to find a way to convince
[1536.98 --> 1537.98]  them that there is a
[1537.98 --> 1538.84]  better way and that
[1538.84 --> 1539.96]  they'll get better results
[1539.96 --> 1541.48]  from that because they've
[1541.48 --> 1542.82]  gotten in their opinion
[1542.82 --> 1544.06]  they've got good results
[1544.06 --> 1544.82]  which is why they're still
[1544.82 --> 1546.16]  doing it if they weren't
[1546.16 --> 1547.78]  getting some level of
[1547.78 --> 1548.80]  result it would have
[1548.80 --> 1550.54]  already passed but it's
[1550.54 --> 1551.90]  your job usually in the
[1551.90 --> 1553.34]  very early days to figure
[1553.34 --> 1555.12]  out how to address those
[1555.12 --> 1556.88]  perceptions I'm struck by
[1556.88 --> 1558.42]  the scenario that's talked
[1558.42 --> 1560.34]  about in this article from
[1560.34 --> 1562.84]  Eric talks about a sort of
[1562.84 --> 1564.26]  mid-stage startup around
[1564.26 --> 1565.92]  10 million and so that's
[1565.92 --> 1567.42]  about the size that that
[1567.42 --> 1568.96]  my wife's business is and
[1568.96 --> 1570.12]  looking at her marketing
[1570.12 --> 1572.58]  and and sales customer
[1572.58 --> 1575.10]  service department if you
[1575.10 --> 1576.02]  think about that early
[1576.02 --> 1577.06]  stage like you were
[1577.06 --> 1579.12]  talking about it was
[1579.12 --> 1581.62]  basically her she built up
[1581.62 --> 1583.62]  a ton of expertise and
[1583.62 --> 1585.42]  internal knowledge in terms
[1585.42 --> 1586.76]  of what was working and
[1586.76 --> 1589.10]  what was driving sales and
[1589.10 --> 1590.94]  that basically boosted the
[1590.94 --> 1592.82]  company to you know
[1592.84 --> 1594.84]  mostly where it's at but
[1595.38 --> 1596.32]  then you start thinking
[1596.32 --> 1598.50]  okay well it's at a size
[1598.50 --> 1599.68]  where we're hiring in
[1599.68 --> 1602.28]  marketing people or people
[1602.28 --> 1603.00]  that are supposed to be
[1603.00 --> 1604.78]  driving sales is it
[1604.78 --> 1607.08]  reasonable to assume that
[1607.08 --> 1608.32]  each of those people are
[1608.32 --> 1609.78]  going to have both the
[1609.78 --> 1611.76]  sort of ownership over the
[1611.76 --> 1613.50]  business and the drive to
[1613.50 --> 1615.18]  like build up that you know
[1615.18 --> 1617.32]  level of internal knowledge
[1617.32 --> 1618.94]  and you know there's going
[1618.94 --> 1620.34]  to be appropriate knowledge
[1620.34 --> 1621.58]  transfer between all of
[1621.58 --> 1622.70]  these people coming in it's
[1622.70 --> 1624.58]  just not the case like you
[1624.58 --> 1625.92]  say you hit this wall where
[1625.92 --> 1627.84]  now how do we be creative
[1627.84 --> 1629.24]  how do we try new things and
[1629.24 --> 1630.32]  how do we make sure that
[1630.32 --> 1632.32]  we're driving new sales and
[1632.32 --> 1634.74]  growing it has to be data
[1634.74 --> 1637.48]  driven at that point but the
[1637.48 --> 1639.88]  culture it wasn't sort of set
[1639.88 --> 1641.52]  up that way organically not
[1641.52 --> 1642.84]  because they weren't wanting to
[1642.84 --> 1644.44]  be that way but because it
[1644.44 --> 1646.70]  just sort of organically grew
[1646.70 --> 1648.42]  into this department where
[1648.42 --> 1649.94]  they're doing the things that
[1649.94 --> 1651.32]  like you say they know work
[1651.32 --> 1652.44]  to some degree and they
[1652.44 --> 1654.00]  they felt like we're still
[1654.00 --> 1656.24]  working and so I think now
[1656.24 --> 1658.56]  in her company they're doing
[1658.56 --> 1660.22]  a lot of thinking about yeah
[1660.22 --> 1662.34]  how do they how do they drive
[1662.34 --> 1664.56]  that data driven culture in
[1664.56 --> 1666.36]  marketing and some of it's just
[1666.36 --> 1668.12]  the very simple stuff that even
[1668.12 --> 1669.32]  Eric talked about in his
[1669.32 --> 1670.94]  article like do people
[1670.94 --> 1673.10]  understand how UTM codes and
[1673.10 --> 1675.44]  website traffic works like there
[1675.44 --> 1676.58]  needs to be some knowledge
[1676.58 --> 1678.64]  sharing there and then there
[1678.64 --> 1680.24]  needs to be common you know
[1680.24 --> 1683.10]  data gathering like okay we've
[1683.10 --> 1684.46]  got this stuff over here and
[1684.46 --> 1685.94]  Facebook pixel and this stuff
[1685.94 --> 1687.20]  over here and Google Analytics
[1687.20 --> 1688.46]  and this stuff over here and
[1688.46 --> 1691.00]  Shopify and this stuff over here
[1691.00 --> 1692.56]  in these sort of random places
[1692.56 --> 1695.52]  no one can like really coalesce
[1695.52 --> 1697.76]  around anything if if all of
[1697.76 --> 1699.30]  that's fragmented out and so
[1699.30 --> 1700.60]  there needs to be data
[1700.60 --> 1702.26]  aggregation together there needs
[1702.26 --> 1703.70]  to be a common way to look at it
[1703.70 --> 1705.96]  and then you know building that
[1705.96 --> 1707.72]  culture like it's also about
[1707.72 --> 1709.52]  people's motivation you have to
[1709.52 --> 1712.14]  think about if I'm gonna show
[1712.14 --> 1713.62]  something to this marketing
[1713.62 --> 1715.94]  person how are they motivated by
[1715.94 --> 1717.24]  that I mean it could be like
[1717.24 --> 1718.70]  commissions or something right like
[1718.70 --> 1720.90]  if you if you make this much off
[1720.90 --> 1724.00]  of Facebook ads then you you get
[1724.00 --> 1726.26]  this commission or this incentive
[1726.26 --> 1728.68]  right well pretty quickly they're
[1728.68 --> 1729.66]  gonna want to know how much
[1729.66 --> 1731.20]  they're making off of Facebook ads
[1731.20 --> 1732.44]  and if they're not setting up their
[1732.44 --> 1734.18]  UTMs right and they're not using
[1734.18 --> 1736.84]  the the common systems where data
[1736.84 --> 1738.04]  is coming in then they're not
[1738.04 --> 1739.54]  gonna be able to know right you
[1739.54 --> 1741.80]  know it is you're telling me that
[1741.80 --> 1743.00]  and I'm listening to kind of the
[1743.00 --> 1744.94]  just these normal struggles of
[1744.94 --> 1747.98]  your wife's business going through
[1747.98 --> 1750.66]  this and I'm struck with the fact
[1750.66 --> 1752.60]  that you have a brilliant wife who
[1752.60 --> 1754.58]  is really good at what she does and
[1754.58 --> 1757.24]  you are you are really good at what
[1757.24 --> 1761.98]  you do and and I'll give her that I'll
[1761.98 --> 1763.94]  give her that she has the benefit she
[1763.94 --> 1766.28]  is a brilliant business person and
[1766.28 --> 1768.24]  love talking to her and love learning
[1768.24 --> 1770.42]  from her but she also does have the
[1770.42 --> 1772.06]  benefit of being married to you and
[1772.06 --> 1773.80]  you're able to put these things in
[1773.80 --> 1776.52]  front of her most business people as
[1776.52 --> 1779.40]  smart as they are are don't have such
[1779.40 --> 1781.78]  an intimate fountain of knowledge about
[1781.78 --> 1783.86]  these particular topics they know their
[1783.86 --> 1785.56]  business but they don't necessarily
[1785.56 --> 1787.56]  understand you know have someone who
[1787.56 --> 1789.88]  can inform them all the all these data
[1789.88 --> 1791.70]  points they can hire people to do that
[1791.70 --> 1794.56]  but to your point those people may not
[1794.56 --> 1796.76]  be quite as motivated as you are as a
[1796.76 --> 1798.94]  as a business owner or the spouse of a
[1798.94 --> 1801.64]  business owner it kind of brings a lot of
[1801.64 --> 1805.28]  weight to this whole building a data
[1805.28 --> 1807.96]  team side of things because I think
[1807.96 --> 1811.34]  about like let's say I'm not in the
[1811.34 --> 1813.80]  picture and she hires a data person to
[1813.80 --> 1816.32]  figure out you know figure out how to
[1816.32 --> 1819.76]  make our company you know data driven
[1819.76 --> 1821.76]  and using modeling and all this stuff and
[1821.76 --> 1823.88]  she hires that person and that person
[1823.88 --> 1827.24]  spends all their time on you know fancy
[1827.24 --> 1829.20]  deep learning stuff but doesn't address
[1829.20 --> 1831.38]  these basic issues of like how does the
[1831.38 --> 1832.88]  marketing team operate what's the
[1832.88 --> 1835.72]  culture what numbers do they need to see
[1835.72 --> 1838.84]  in front of that actually could I mean I'm
[1838.84 --> 1840.60]  not saying it's gonna it would take down
[1840.60 --> 1841.90]  the business but it's gonna make a
[1841.90 --> 1844.50]  significant negative impact on it
[1844.50 --> 1846.60]  absolutely because it's it's not what's
[1846.60 --> 1849.86]  needed right so I think that people
[1849.86 --> 1852.04]  coming into these sorts of positions need
[1852.04 --> 1855.16]  to be sort of not scared but sober
[1855.16 --> 1857.92]  minded in the sense of you know really
[1857.92 --> 1859.92]  having the perspective of what what are
[1859.92 --> 1862.78]  the needs of the business rather than
[1862.78 --> 1865.20]  what's the coolest project that I can work
[1865.20 --> 1867.50]  on or what's the way I build my resume or
[1867.50 --> 1869.84]  what's the way I get the training class
[1869.84 --> 1872.26]  that I really would love to do but isn't
[1872.26 --> 1874.78]  necessarily directly in line with what
[1874.78 --> 1876.08]  we're trying to accomplish at the
[1876.08 --> 1878.40]  organizational level so yeah there's a
[1878.40 --> 1880.64]  huge risk you you're able to bring a
[1880.64 --> 1882.82]  purity because all you care about is the
[1882.82 --> 1884.78]  success of the organization but that's not
[1884.78 --> 1887.74]  always the case one of the other points
[1887.74 --> 1889.94]  that Eric brings up which I think is
[1889.94 --> 1894.28]  really interesting is executive support for
[1894.28 --> 1899.26]  ML AI type things and the sentiment that
[1899.26 --> 1902.48]  sometimes comes up when you're an AI or
[1902.48 --> 1904.86]  machine learning person maybe you've dealt
[1904.86 --> 1906.86]  with all of the sort of getting metrics in
[1906.86 --> 1909.00]  front of people thing there is a really
[1909.00 --> 1911.84]  important problem that you think is solved
[1911.84 --> 1914.10]  really well by machine learning and AI
[1914.10 --> 1916.82]  you've you know trained a model or whatever
[1916.82 --> 1921.02]  it is and like you're genuinely convinced
[1921.02 --> 1925.36]  that this is a meaningful thing that you've
[1925.36 --> 1928.14]  done that has great benefit for the company
[1928.14 --> 1933.62]  but you try and try to like build support for
[1933.62 --> 1936.46]  this and you get nothing what are maybe in
[1936.46 --> 1939.22]  your experience what maybe is going on in
[1939.22 --> 1942.12]  that situation where you're trying you have
[1942.12 --> 1944.94]  this solution but you're having trouble like
[1944.94 --> 1947.10]  either helping people in the organization
[1947.10 --> 1949.40]  understand it or understand the value or
[1949.40 --> 1952.62]  understand the benefit and you know buy into
[1952.62 --> 1955.14]  it and support it it's your job to communicate
[1955.14 --> 1958.12]  that as the leader of the effort or as the
[1958.12 --> 1960.50]  visionary who understands what's possible
[1960.50 --> 1963.50]  you have to be able to explain it but without
[1963.50 --> 1965.58]  diving into all the technical details you have
[1965.58 --> 1968.34]  to be able to maybe you're either not using
[1968.34 --> 1970.56]  data science or maybe you're using more
[1970.56 --> 1972.80]  traditional mechanisms in data science and
[1972.80 --> 1976.04]  you know that a convolutional neural network or
[1976.04 --> 1978.92]  a natural language processing model has a
[1978.92 --> 1982.32]  particular strength in a certain area you've
[1982.32 --> 1984.04]  got to find a way to communicate that and
[1984.04 --> 1986.42]  doing that by to some degree dumbing it down
[1986.42 --> 1988.62]  and I don't mean that in a derogatory way I
[1988.62 --> 1991.02]  mean that of your audience is not as technical
[1991.02 --> 1993.54]  as you are and so you have to get that
[1993.54 --> 1996.18]  communication at the level that they get the
[1996.18 --> 1998.94]  value you have to abstract it to a point where
[1998.94 --> 2000.96]  they can where they're going to understand that
[2000.96 --> 2003.34]  but that's it's really on you it's not on them
[2003.34 --> 2007.20]  it's your job to show them if I look at other
[2007.20 --> 2010.10]  similar fields and they used to do it this way
[2010.10 --> 2012.44]  and there's here's a paper or an article about
[2012.44 --> 2014.98]  that and this other company who has something
[2014.98 --> 2018.02]  similar to ours or maybe has a similar interest in
[2018.02 --> 2021.56]  this particular task did something and they've
[2021.56 --> 2024.36]  gone all in after testing it this is why these
[2024.36 --> 2026.20]  are the basics of this that's the basic to that
[2026.20 --> 2029.76]  there's a definite advantage we should invest in
[2029.76 --> 2032.24]  that and also know when not to invest because
[2032.24 --> 2034.18]  we've come through an age the last few years
[2034.18 --> 2036.98]  where so many people are just wanting to do AI so
[2036.98 --> 2039.38]  they can say they're doing AI and there's a lot
[2039.38 --> 2041.76]  of things that deep learning is is not the best
[2041.76 --> 2044.48]  thing for or or at least it's way more expensive
[2044.48 --> 2047.88]  than other options that are equally as good or nearly
[2047.88 --> 2051.76]  as good so it's it's finding somebody who understands
[2051.76 --> 2054.50]  that to lead your effort and who can communicate that
[2054.50 --> 2057.96]  effectively to all the stakeholders I think that's why
[2057.96 --> 2061.76]  maybe certain tools that have come out recently like
[2061.76 --> 2064.96]  let's say a streamlet or something like that can
[2064.96 --> 2069.62]  actually be incredibly powerful to solve this problem
[2069.62 --> 2073.54]  because would you want to develop your whole product
[2073.54 --> 2077.28]  in streamlet maybe maybe not depending on what it is
[2077.28 --> 2082.32]  but could you use that tool in order to prototype
[2082.32 --> 2086.86]  something out and demonstrably show the value of what
[2086.86 --> 2091.84]  you're doing yeah definitely prototypes and sort of
[2091.84 --> 2096.48]  minimal viable things are I think really valuable in this
[2096.48 --> 2100.40]  case and often the way that Eric puts this is sometimes
[2100.40 --> 2104.34]  the data team just doesn't take it upon themselves to get
[2104.34 --> 2108.12]  the work into a place where it demonstrates value and is
[2108.12 --> 2112.76]  reasonably easy to ship so you could have a Jupiter notebook
[2112.76 --> 2118.98]  right or you could run a model on your GPU server right and
[2118.98 --> 2123.64]  then do your test set on your GPU server and show that you
[2123.64 --> 2129.30]  get you know 90 accuracy or whatever it is and then your
[2129.30 --> 2132.14]  executive team's like oh that's great you know let's ship
[2132.14 --> 2135.22]  it how do we get it into this product and if your answer is oh I
[2135.22 --> 2139.16]  haven't thought about that yet or it only runs on the GPU server
[2139.16 --> 2143.16]  or I don't know how to like extract it we have to figure out
[2143.16 --> 2145.98]  that problem do you want to invest in that it doesn't really inspire
[2145.98 --> 2149.86]  a lot of confidence right it doesn't so I think just that one
[2149.86 --> 2155.10]  step of do we expect data teams or data scientists to actually
[2155.10 --> 2159.56]  build robust products maybe in certain cases they they're part
[2159.56 --> 2163.12]  of that like in smaller startups and that sort of thing in larger
[2163.12 --> 2167.76]  companies maybe not but should they be expected to maybe go
[2167.76 --> 2171.50]  that little extra mile to create a prototype that demonstrates
[2171.50 --> 2175.66]  value and gets things in in front of people in a meaningful
[2175.66 --> 2179.62]  way even if it doesn't scale all the way up I think that's like
[2179.62 --> 2185.24]  that's a huge huge point that I don't see emphasized that much you
[2185.24 --> 2189.48]  know because you see a lot emphasized about getting your models training
[2189.48 --> 2194.92]  well and you know evaluating well but not this sort of prototyping bit of
[2194.92 --> 2199.02]  the problem I agree with that completely I think that people you know
[2199.02 --> 2202.62]  over talk it a little bit early on and don't recognize the value of
[2202.62 --> 2206.44]  lightweight prototyping to help you figure your way through it figure out
[2206.44 --> 2210.08]  what it is that you need and prove out that what you're thinking is
[2210.08 --> 2213.88]  actually accurate because if you think of how many organizations build
[2213.88 --> 2217.70]  things that actually are not very useful in the end or don't have the
[2217.70 --> 2222.06]  audience that the they originally expected that you can solve that in part
[2222.06 --> 2226.52]  with prototyping and and and help yourself hone in on and I think that a lot
[2226.52 --> 2232.72]  of organizations are they interpret that as scary in a way or potentially as
[2232.72 --> 2237.02]  long and expensive and so they they make the mistake of trying to talk their way
[2237.02 --> 2241.98]  through it and I've seen that through my entire career and in my earliest
[2241.98 --> 2246.64]  days there was no such thing as agile that didn't happen for a while actually
[2246.64 --> 2250.56]  until you know eventually this agile movement around the beginning of the
[2250.56 --> 2256.16]  2000s came about and and it's taken the next 20 years for that mindset to really
[2256.16 --> 2261.52]  take hold in a broad sense and so you need to try stuff out and you need to be to be
[2261.52 --> 2267.38]  ready to to go off and do a coding spike on something and figure out with a simple
[2267.38 --> 2271.24]  model whether or not this is doable whether it could be or if it's doable can you
[2271.24 --> 2275.18]  deploy it is it deployable in a reasonable way do you have resources where you need
[2275.18 --> 2279.44]  to deploy it so your points are well made these are all things that you need to be
[2279.44 --> 2283.88]  thinking about when you're building these teams and and you're looking for the
[2283.88 --> 2287.66]  people with the right mindset and the right skill sets so that you can be
[2287.66 --> 2288.08]  successful.
[2288.08 --> 2294.12]  And on your data teams that you've built in the past in terms of the communication
[2294.12 --> 2299.38]  between the data team and maybe like organizational units that that data team is
[2299.38 --> 2304.12]  serving let's say marketing or supply chain or whatever it is how does the
[2304.12 --> 2309.38]  communication work between those sort of external or internal but other
[2309.38 --> 2314.68]  organizational units and the data team work in your experience often does that flow
[2314.68 --> 2320.28]  through the management of the data team or does that flow directly through the individual
[2320.28 --> 2323.38]  data scientists working on various products or?
[2323.74 --> 2327.38]  So I don't think there's any standardized way and I've seen that happen in all sorts of
[2327.38 --> 2331.10]  different ways and some of them are formal and some of them are informal just because
[2331.10 --> 2335.50]  people are talking but I've rarely seen great integration in that capacity.
[2335.92 --> 2341.64]  I've rarely seen that kind of inner functional communication and the translation required for them to
[2341.64 --> 2348.02]  understand each other to happen well and seamlessly and consistently but it definitely
[2348.02 --> 2351.60]  helps and this goes back to that thing we talked about at the very beginning is culture.
[2351.94 --> 2358.76]  If you don't evolve your growing organization with the right culture to take advantage of
[2358.76 --> 2364.20]  this it's really really hard to make that change down the road even and you may have to but
[2364.20 --> 2369.72]  you're really gonna have to consciously set some things aside that maybe were long time
[2369.72 --> 2375.82]  valued processes. And I think this is something this is like a growth area for me I think that I've
[2375.82 --> 2385.52]  seen recently is oftentimes when you're building a team if you're the one building the team it's most
[2385.52 --> 2391.20]  natural for sort of all communication and sort of project communication and all of that to sort of
[2391.20 --> 2398.24]  flow through you as the management of the data team and at a certain point so I think that's
[2398.24 --> 2404.26]  probably good in the beginning because you're setting some standards you're setting workflows all of
[2404.26 --> 2410.98]  this stuff and you sort of need to guard that a little bit I think that's probably reasonable but
[2410.98 --> 2416.42]  as the team grows and as the number of project grows at some point you become the bottleneck right?
[2416.72 --> 2417.00]  You do.
[2417.26 --> 2422.46]  If you know all the communication from all these different projects and the different organizational
[2422.46 --> 2430.84]  units are flowing through you then pretty quickly the queue builds up and you know stuff is falling
[2430.84 --> 2438.36]  through the cracks so I feel that right now in terms of the teams that I'm helping build there needs to be
[2438.36 --> 2445.92]  this transition to more sort of embedded communication where the people working on different projects are
[2445.92 --> 2456.32]  are feeling the freedom to have those communication while still you know trying to maintain standards and
[2456.32 --> 2462.06]  all of that of course and make sure that projects are done well there still needs to be data management but
[2462.06 --> 2466.04]  I think things need to get more decentralized over time.
[2466.46 --> 2470.46]  It does and that data management that you're talking about has to become human management.
[2470.46 --> 2477.14]  It has to be recognizing your individuals for what they are and what their capabilities are and
[2477.14 --> 2482.32]  understanding that they're all different and developing a good understanding of what each of
[2482.32 --> 2488.68]  those individuals can and can't do well along a spectrum and then being able to give them those
[2488.68 --> 2495.04]  responsibilities where they both can be successful but also have room to grow and that is really hard to do.
[2495.30 --> 2499.00]  It's super easy for me to say that and it's super hard to execute that.
[2499.00 --> 2503.48]  That's what you have to do if you're going to grow past those early stages of putting it all together.
[2503.68 --> 2511.94]  I was really inspired by this article just in terms of like understanding where I've been at
[2511.94 --> 2517.10]  at the past and how I've been able to grow into certain data teams but also I think it's
[2517.10 --> 2521.38]  a really great way to frame some of this up in a creative way.
[2521.56 --> 2525.38]  So thank you Eric for writing this and putting in the time to do it.
[2525.38 --> 2529.70]  You're welcome on the show anytime to talk through other things along with this.
[2529.94 --> 2532.52]  So if you're out there feel free to join us sometime.
[2532.98 --> 2537.60]  In these fully connected episodes we usually also try to give a couple learning resources
[2537.60 --> 2541.18]  related to the topic that we're talking about.
[2541.18 --> 2548.42]  This week I wanted to mention a book from one of our past guests Mike Bugimbe cracking the data code
[2548.42 --> 2555.20]  which is a great book where he talks a lot about data culture and creating a data driven culture in
[2555.20 --> 2555.76]  your business.
[2556.40 --> 2562.86]  And then also there's a book by also one of our previous guests Hillary Mason and DJ Patel
[2562.86 --> 2565.52]  called data driven creating a data culture.
[2565.52 --> 2571.84]  It's more like a booklet I think you can get it in some cases for free like on your Kindle or something
[2571.84 --> 2572.32]  like that.
[2572.38 --> 2573.70]  It's a good good little read.
[2573.98 --> 2576.18]  So maybe maybe choices out there.
[2576.66 --> 2576.90]  Yeah.
[2577.14 --> 2577.36]  Yeah.
[2577.36 --> 2583.04]  There's definitely resources out there and you know although you and I have had experiences
[2583.04 --> 2591.40]  I definitely respect the opinions of people like Eric and Hillary and DJ and Mike Bugimbe and others
[2591.40 --> 2598.10]  who really have been able to scale things like that up because yeah like you said the human problem is
[2598.10 --> 2604.42]  maybe the main thing that you're dealing with as you're building a data team is not so much your ability
[2604.42 --> 2608.42]  as a data team to do things but how you relate to other teams in your organization.
[2608.42 --> 2616.26]  How you can be gracious and clear and tenacious and creative and all those things kind of together
[2616.26 --> 2622.14]  and not burn a bunch of bridges and end up in a bad situation.
[2622.62 --> 2628.24]  Yeah that's really important and you really have to respect all of those people including the diversity
[2628.24 --> 2631.86]  of their differences because they did not have your experiences.
[2632.44 --> 2636.08]  They did not grow up thinking that data was the thing they were going to spend their time on.
[2636.08 --> 2642.74]  You have to position the value in a way that they understand and that they can also value
[2642.74 --> 2646.44]  and it's crossing that chasm that is the key to success there.
[2646.72 --> 2648.42]  Well thanks for having this chat.
[2648.50 --> 2649.86]  I enjoyed hearing your stories Chris.
[2650.22 --> 2651.48]  I enjoy hearing yours as well.
[2651.56 --> 2652.20]  We have good ones.
[2652.36 --> 2652.82]  All right.
[2652.90 --> 2653.88]  I'll see you next week.
[2654.14 --> 2654.44]  Okay.
[2654.58 --> 2654.88]  Take care.
[2657.84 --> 2660.28]  Thank you for listening to Practical AI.
[2660.28 --> 2664.94]  We have a bundle of awesome podcasts for you at changelog.com
[2664.94 --> 2668.04]  including our brand new show Ship It with Gerhard Lezou.
[2668.28 --> 2672.84]  A podcast about getting your best ideas into the world and seeing what happens.
[2673.20 --> 2677.08]  It's about the code, the ops, the infra, and the people that make it happen.
[2677.38 --> 2681.10]  Yes we focus on the people because everything else is an implementation detail.
[2681.44 --> 2685.70]  Subscribe now at changelog.com slash ship it or simply search for ship it.
[2685.80 --> 2687.36]  In your favorite podcast app you'll find it.
[2687.36 --> 2690.80]  Of course the galaxy brain move is to subscribe to our master feed.
[2690.80 --> 2696.18]  It's all changelog podcasts including Practical AI and Ship It in one place.
[2696.50 --> 2701.26]  Search changelog master feed or head to changelog.com slash master and subscribe today.
[2701.70 --> 2706.46]  Practical AI is hosted by Daniel Whitenack and Chris Benson with music by Breakmaster Cylinder.
[2706.66 --> 2709.18]  We're brought to you by Fastly, LaunchDarkly, and Linode.
[2709.48 --> 2710.18]  That's all for now.
[2710.40 --> 2711.34]  We'll talk to you again next week.
[2717.36 --> 2747.34]  We'll talk to you again next week.
