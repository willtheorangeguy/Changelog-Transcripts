[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.84]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.22 --> 12.40]  And we're hosted on Linode cloud servers.
[12.76 --> 14.74]  Head to linode.com slash Changelog.
[17.62 --> 20.50]  This episode is brought to you by DigitalOcean.
[20.96 --> 24.88]  DigitalOcean provides worry-free database hosting with their managed databases.
[25.18 --> 29.32]  If you need to get data in and out of Postgres, MySQL, or Redis,
[29.32 --> 32.02]  call on the world-class support teams at DigitalOcean
[32.02 --> 35.14]  and stop wasting time on setup, backup, and maintenance.
[35.60 --> 37.22]  Get simple, predictable pricing.
[37.62 --> 38.86]  Get detailed documentation.
[39.56 --> 43.06]  Get up and running in minutes so you can get on with your business.
[43.44 --> 44.24]  What are you waiting for?
[44.38 --> 46.42]  Head to do.co slash Changelog.
[46.60 --> 49.22]  Again, that's do.co slash Changelog.
[59.32 --> 67.68]  Welcome to Practical AI, a weekly podcast about making artificial intelligence
[67.68 --> 70.40]  practical, productive, and accessible to everyone.
[70.78 --> 75.28]  This is where conversations around AI, machine learning, and data science happen.
[75.78 --> 78.30]  Join the community and slack with us around various topics of the show
[78.30 --> 80.04]  at changelog.com slash community.
[80.28 --> 81.20]  Follow us on Twitter.
[81.20 --> 82.80]  We're at Practical AI FM.
[83.30 --> 84.12]  And now onto the show.
[88.68 --> 91.70]  Welcome to another episode of the Practical AI Podcast.
[92.32 --> 93.18]  I am Chris Benson.
[93.38 --> 95.74]  I am a principal AI strategist at Lockheed Martin.
[95.94 --> 98.70]  And with me, as always, is my co-host, Daniel Whitenack,
[98.76 --> 101.50]  who is a data scientist with SIL International.
[101.96 --> 102.80]  How's it going today, Daniel?
[103.26 --> 104.10]  It's going pretty good.
[104.10 --> 106.34]  Got a bit of a cold, but not too bad.
[106.50 --> 110.50]  I'm doing some pretty interesting stuff with text-to-speech this week.
[110.66 --> 111.72]  So that's pretty fun.
[111.72 --> 112.32]  Really?
[112.48 --> 115.40]  Anything worth sharing, or are you going to wait until later?
[115.56 --> 119.52]  Well, I think there'll be some things revealed at the Project Voice Conference,
[119.72 --> 122.00]  which we'll both be at in January.
[122.40 --> 122.72]  Yep.
[123.06 --> 125.64]  So I'll leave you in anticipation until then,
[125.72 --> 130.62]  but it involves lots of speech data and some text-to-speech in local languages.
[131.12 --> 135.44]  And for any listeners who happen to be in the Chattanooga, Tennessee area,
[135.58 --> 138.24]  north of Atlanta, and want to catch Daniel and I,
[138.28 --> 141.08]  we're going to give a talk at the Project Voice Conference,
[141.08 --> 143.92]  and we're also going to be recording some episodes there.
[144.06 --> 145.38]  So we would love to see you there.
[145.46 --> 147.78]  If you happen to listen to us, come up and say hi.
[148.14 --> 150.66]  Well, I am pretty excited about today.
[150.94 --> 155.12]  We have a guest that I already have quite a bit of knowledge about.
[155.40 --> 158.84]  We have some work between our company and his organization.
[158.84 --> 164.30]  With us today is Greg Allen, who is the Chief of Strategy and Communications
[164.30 --> 170.84]  at the U.S. Department of Defense's relatively new Joint Artificial Intelligence Center.
[171.30 --> 172.06]  Welcome to the show, Greg.
[172.46 --> 173.36]  Hey, thanks for having me.
[173.80 --> 175.26]  Yeah, I'm pretty excited about it.
[175.32 --> 177.40]  You guys do some super cool stuff,
[177.68 --> 180.16]  and so I'm really happy to share that with our listeners.
[180.36 --> 182.44]  I've been looking forward to doing this for a while.
[182.44 --> 187.02]  I guess if you could just start us off kind of telling us a bit about yourself
[187.02 --> 190.60]  and your background, kind of how you got to this point,
[191.04 --> 196.56]  and then after that we'll dive into what the Joint Artificial Intelligence Center does.
[197.22 --> 197.52]  Sure.
[197.86 --> 202.10]  Well, as you said, I'm the Chief of Strategy and Communications here at the Joint AI Center,
[202.36 --> 206.12]  and I came here from a variety of backgrounds, really.
[206.12 --> 210.60]  My primary professional experience has been in corporate strategy work,
[211.00 --> 213.16]  and I did that both as a management consultant
[213.16 --> 215.84]  and then also working in the corporate strategy offices
[215.84 --> 218.18]  of a variety of commercial technology companies.
[218.58 --> 222.36]  But after a while, I was working on some AI strategy projects
[222.36 --> 227.36]  and ended up doing a piece of work for the Intelligence Advanced Research Projects activity.
[227.80 --> 229.44]  That organization is called IARPA.
[229.88 --> 231.24]  If you're familiar with DARPA,
[231.24 --> 236.18]  this is the sister agency that covers the intelligence community of DARPA.
[236.54 --> 240.12]  And my report there was titled Artificial Intelligence and National Security.
[240.62 --> 244.28]  And it was essentially, you know, going through the different aspects of AI technology,
[244.52 --> 246.02]  how it was changing over time,
[246.44 --> 249.74]  and elaborating on what the likely implications of that would be
[249.74 --> 252.32]  for different areas of national security.
[252.92 --> 255.86]  What year was this around in terms of kind of how things were developing?
[256.40 --> 259.14]  Yeah, this report came out in 2017,
[259.14 --> 262.24]  and I was working on it for the entire preceding year.
[262.64 --> 262.74]  Gotcha.
[263.06 --> 266.20]  So if you're familiar with the Obama administration,
[266.56 --> 272.44]  White House's reports on artificial intelligence that came out in October 2016,
[273.14 --> 276.48]  sort of the origin of this was that there was an additional report
[276.48 --> 279.82]  that they talked about writing on AI and national security,
[279.82 --> 282.66]  but ended up punting on it and deciding, you know,
[282.72 --> 284.02]  oh, somebody will get to that later.
[284.02 --> 287.16]  We should focus more on the workforce and the economic
[287.16 --> 289.12]  and the research and development impacts of AI.
[289.52 --> 292.60]  And so IARPA, the head of IARPA at the time, Jason Matheny,
[293.14 --> 295.32]  asked me, well, you know, rather than wait,
[295.44 --> 297.92]  why don't we have you as sort of an outsider
[297.92 --> 301.10]  take a first stab at this report that was not written?
[301.66 --> 303.68]  And so it was on behalf of IARPA,
[303.82 --> 306.36]  but it was ultimately published through the Harvard Belfer Center
[306.36 --> 308.38]  for Science and International Affairs.
[308.90 --> 310.28]  And after that report came out,
[310.36 --> 314.08]  there was a great deal of interest from the U.S. national security community,
[314.08 --> 317.68]  and I ended up joining the Center for a New American Security,
[317.86 --> 320.70]  which is a think tank in the Washington, D.C. area,
[321.18 --> 325.14]  and doing a lot of analysis and sort of pro bono advisory work
[325.14 --> 326.44]  to the Department of Defense.
[326.94 --> 328.24]  And so when they ended up standing up
[328.24 --> 330.42]  the Joint Artificial Intelligence Center,
[330.80 --> 332.50]  the individuals who were standing up that organization
[332.50 --> 334.24]  asked me if I would be willing to help out.
[334.60 --> 336.12]  And of course, I jumped at the chance.
[336.12 --> 337.34]  It was a very exciting opportunity.
[338.36 --> 338.74]  Very cool.
[338.74 --> 342.26]  So I guess, and just as a, to call out a couple of acronyms,
[342.34 --> 343.78]  I know you described IARPA.
[344.18 --> 346.40]  You also referenced that by talking about
[346.40 --> 348.64]  kind of the intelligence side from DARPA.
[349.12 --> 351.12]  Listeners who are not familiar with it
[351.12 --> 353.52]  may remember that DARPA is the agency,
[353.66 --> 355.82]  Defense Advanced Research Projects Agency,
[355.90 --> 357.94]  if I got that right, that started the internet.
[358.24 --> 360.12]  So if you're not familiar with this already,
[360.18 --> 362.08]  that's probably where you would have heard of DARPA
[362.08 --> 364.80]  and IARPA, its sister agency for defense.
[364.94 --> 367.58]  So I guess at this point, if you could kind of,
[367.58 --> 369.74]  I know the JAIC, and I should say,
[369.94 --> 372.22]  JAIC refers to where the center that you're at,
[372.28 --> 374.86]  the Joint AI Center at the Department of Defense,
[375.04 --> 376.68]  and we call it the JAIC for short.
[376.92 --> 378.94]  So I know it is relatively new.
[379.06 --> 380.50]  You guys just came into existence
[380.50 --> 384.34]  in the, I think, middle to late part of the year in 2018.
[384.44 --> 387.56]  If you could kind of start off by telling us
[387.56 --> 390.16]  what is the JAIC and, you know,
[390.22 --> 392.98]  kind of describe its mission and its budget
[392.98 --> 394.92]  and, you know, why is it there?
[395.44 --> 395.58]  Sure.
[395.58 --> 398.40]  So the Joint AI Center was established
[398.40 --> 400.24]  as the Department of Defense's
[400.24 --> 402.76]  Center of Excellence for AI Technology.
[403.30 --> 405.54]  It was officially stood up in parallel
[405.54 --> 407.72]  with the release of the Department of Defense's
[407.72 --> 408.64]  AI strategy.
[409.22 --> 412.34]  So that document was released in the middle of 2018,
[412.34 --> 414.28]  and it was released publicly
[414.28 --> 418.26]  in the unclassified summary in February of 2019.
[418.66 --> 421.92]  So a bit of a gap between when the strategy was finished
[421.92 --> 423.28]  and when it was released publicly,
[423.28 --> 425.92]  but ultimately it's out there, you can read it on the internet.
[426.34 --> 430.08]  And so the DoD AI strategy that came out in the summer of 2018,
[430.74 --> 433.44]  what it says is that the Department of Defense recognizes
[433.44 --> 436.06]  the strategic importance of AI technology,
[436.06 --> 437.70]  and it also says that, you know,
[437.82 --> 439.66]  the Department of Defense wants to pursue
[439.66 --> 441.52]  advances in AI technology
[441.52 --> 443.94]  technology basically for military advantage.
[444.22 --> 447.06]  So the basic reason that we're interested in most technologies.
[447.88 --> 449.64]  And that document said that we were going to create
[449.64 --> 452.08]  a new organization called the Joint AI Center,
[452.22 --> 455.16]  which would be the focal point of the implementation
[455.16 --> 457.88]  and execution of the DoD's AI strategy.
[458.40 --> 461.68]  So maybe I'll start by talking a bit about the DoD AI strategy,
[462.08 --> 464.86]  and then I can get into the specifics about what the JAIC is doing
[464.86 --> 466.66]  to make good on that strategy.
[466.66 --> 467.86]  That sounds fine.
[467.86 --> 471.10]  The DoD AI strategy has five pillars.
[471.60 --> 475.96]  These are deliver AI capabilities for mission impact,
[476.42 --> 479.06]  scale AI's impact through a common foundation,
[479.64 --> 481.56]  cultivate a leading AI workforce,
[482.36 --> 484.64]  engage commercial industry, academia,
[484.98 --> 486.54]  and international allies and partners,
[487.30 --> 489.92]  and lead in military ethics and AI safety.
[490.28 --> 490.94]  What I just described,
[491.00 --> 492.62]  those are the sort of five key pillars
[492.62 --> 494.72]  of the DoD AI strategy.
[494.72 --> 497.42]  The JAIC is the focal point for each of those pillars,
[497.98 --> 500.16]  but we're especially interested in,
[500.30 --> 501.50]  at least in the near term,
[501.60 --> 503.40]  we have been especially interested in
[503.40 --> 506.68]  delivering AI capabilities for mission impact.
[507.42 --> 509.24]  So, and this is a little bit of how we are structured
[509.24 --> 510.14]  as an organization.
[510.64 --> 513.36]  It's quite common in commercial industry
[513.36 --> 516.38]  for AI organizations to separate into,
[516.62 --> 518.64]  you know, who are the people who are actually developing
[518.64 --> 521.46]  and implementing and executing AI capabilities,
[521.46 --> 523.66]  and then who are the folks who are building
[523.66 --> 525.88]  the infrastructure, the platforms,
[526.18 --> 528.98]  the tools to enable that other group.
[529.12 --> 532.20]  So there's a separation between your data scientists
[532.20 --> 533.52]  and your data engineers,
[533.52 --> 536.16]  and similarly a separation between
[536.16 --> 539.30]  your sort of AI capability developers
[539.30 --> 542.38]  and your AI infrastructure and platform developers.
[542.86 --> 545.08]  And that is a distinction that is recognized
[545.08 --> 546.54]  in the DoD AI strategy
[546.54 --> 547.96]  and is also recognized
[547.96 --> 550.24]  in the organizational structure of the JAIC.
[550.24 --> 553.16]  So we have our mission initiatives,
[553.32 --> 554.68]  our national mission initiatives.
[555.34 --> 557.86]  These are specific projects that we're going after
[557.86 --> 561.30]  because we believe that they have a lot of the features
[561.30 --> 564.94]  that allow for success in AI development.
[565.48 --> 567.24]  So some of these projects are,
[567.28 --> 568.46]  I'll just list off a few,
[568.78 --> 570.86]  humanitarian assistance and disaster relief,
[571.34 --> 572.32]  predictive maintenance,
[572.90 --> 573.44]  cybersecurity,
[574.34 --> 575.74]  intelligent business automation,
[576.44 --> 577.34]  warfighter health,
[577.80 --> 579.14]  and joint warfighting.
[579.14 --> 581.28]  And the sort of common approach
[581.28 --> 583.14]  to how we identify projects
[583.14 --> 584.64]  and select them to go after them
[584.64 --> 585.76]  are, you know,
[585.82 --> 587.38]  what are the features that we believe
[587.38 --> 589.62]  lend themselves to success
[589.62 --> 591.06]  in developing AI capabilities?
[591.62 --> 593.30]  So this is areas such as,
[593.56 --> 595.72]  is there a relevant data set
[595.72 --> 596.88]  that you can use
[596.88 --> 599.22]  for training your machine learning algorithms?
[599.22 --> 601.12]  And do you have access to that data?
[601.32 --> 602.86]  Is it of sufficient quality?
[603.18 --> 605.04]  The second thing that we're looking for is,
[605.04 --> 608.18]  is there mature AI technology
[608.18 --> 610.24]  in commercial industry or academia
[610.24 --> 613.16]  that could be used against this problem?
[613.46 --> 615.22]  The third, and perhaps most importantly,
[615.68 --> 617.62]  is would there be mission impact?
[617.68 --> 619.86]  If you did succeed at building this thing
[619.86 --> 621.30]  that you are setting out to build,
[621.68 --> 623.06]  would anybody actually care?
[623.42 --> 625.42]  And then the fourth criteria is,
[625.90 --> 629.34]  do we have access to end user partner organizations
[629.34 --> 632.20]  who would be willing to test our capabilities
[632.20 --> 633.94]  as they're being developed
[633.94 --> 635.20]  in an iterative basis?
[635.64 --> 637.26]  User feedback is critical
[637.26 --> 639.02]  for any software development effort,
[639.46 --> 641.52]  but we believe that iterative user feedback
[641.52 --> 642.80]  is especially critical
[642.80 --> 645.62]  for success in developing AI programs.
[646.16 --> 647.30]  So if you have, you know,
[647.30 --> 648.88]  sort of those four criteria
[648.88 --> 650.60]  as a recipe for success,
[650.60 --> 651.34]  then, you know,
[651.36 --> 652.48]  you have a shot at being
[652.48 --> 653.88]  one of our mission initiatives,
[653.88 --> 654.76]  and those are the ones
[654.76 --> 655.88]  that we're going after right now.
[656.56 --> 658.20]  The sort of second big chunk
[658.20 --> 660.48]  of our organization is related to,
[660.58 --> 661.38]  as I mentioned before,
[661.52 --> 662.80]  infrastructure and platforms.
[663.48 --> 664.34]  And so our infrastructure
[664.34 --> 665.84]  and platform team is developing
[665.84 --> 666.62]  what we're calling
[666.62 --> 668.00]  the Joint Common Foundation.
[668.76 --> 670.94]  And this is an environment
[670.94 --> 673.32]  that lowers the barriers to entry
[673.32 --> 675.58]  to develop machine learning
[675.58 --> 676.74]  and AI capabilities
[676.74 --> 678.30]  in the Department of Defense.
[678.52 --> 679.58]  As you can imagine,
[679.94 --> 680.70]  the Department of Defense
[680.70 --> 682.76]  is a pretty significant target
[682.76 --> 686.22]  for hacking and adversarial intent
[686.22 --> 687.10]  just in general.
[687.10 --> 688.86]  So when we're developing software,
[689.10 --> 690.44]  it's critical that we do that
[690.44 --> 691.50]  in a secure environment.
[692.00 --> 693.08]  But at the same time,
[693.32 --> 693.50]  you know,
[693.52 --> 695.76]  a lot of these security processes
[695.76 --> 697.02]  can sort of slow down
[697.02 --> 698.12]  the development of software.
[698.82 --> 700.66]  So that's why we're developing
[700.66 --> 702.06]  the Joint Common Foundation.
[702.44 --> 703.94]  This is an infrastructure environment
[703.94 --> 707.04]  that has pre-cyber-hardened tools
[707.04 --> 709.20]  that are the same sort of
[709.20 --> 710.60]  machine learning development frameworks
[710.60 --> 711.76]  that you might want to use
[711.76 --> 712.72]  in commercial industry,
[713.08 --> 714.04]  but they're adapted
[714.04 --> 715.24]  to be compatible
[715.24 --> 717.64]  with DoD cybersecurity policies.
[717.64 --> 719.14]  They're containerized
[719.14 --> 720.10]  so that they run
[720.10 --> 721.50]  in cloud environments
[721.50 --> 723.48]  at reasonably high performance levels.
[724.18 --> 725.28]  And that combination
[725.28 --> 728.26]  allows you to develop software quickly
[728.26 --> 729.98]  and get it into the hands
[729.98 --> 731.68]  of users and testers
[731.68 --> 732.78]  in a reasonable timeframe,
[732.78 --> 735.20]  but also do so in a way
[735.20 --> 736.60]  that takes into account
[736.60 --> 738.04]  the very significant
[738.04 --> 739.34]  cybersecurity risks
[739.34 --> 741.14]  that any significant DoD
[741.14 --> 742.58]  undertaking faces.
[742.58 --> 744.36]  Yeah, I have a question there
[744.36 --> 745.84]  around that sort of flow
[745.84 --> 747.66]  from what frameworks
[747.66 --> 749.46]  and software is used in industry
[749.46 --> 751.90]  to what you have to develop on.
[752.02 --> 753.86]  Are you involved very closely
[753.86 --> 755.30]  in, for example,
[755.36 --> 757.04]  the TensorFlow PyTorch communities
[757.04 --> 758.26]  and kind of you have
[758.26 --> 760.22]  your own versions of those things
[760.22 --> 761.24]  that you run internally?
[761.24 --> 763.56]  Or is it more taking frameworks
[763.56 --> 765.24]  like that and wrapping them
[765.24 --> 766.62]  around like middleware
[766.62 --> 767.52]  and other things
[767.52 --> 769.04]  that give the protection
[769.04 --> 769.90]  that's needed?
[769.90 --> 772.16]  Yeah, so I don't want to get
[772.16 --> 773.78]  into too much of the secret sauce
[773.78 --> 775.20]  for security reasons,
[775.20 --> 777.18]  but the basic thinking there
[777.18 --> 778.82]  is that open source tools
[778.82 --> 781.70]  are popular for a reason, right?
[781.74 --> 782.68]  They work well.
[783.18 --> 784.14]  They have been tested
[784.14 --> 785.90]  by users who have
[785.90 --> 787.68]  pretty significant requirements
[787.68 --> 788.44]  and needs.
[789.10 --> 790.32]  And we want to make sure
[790.32 --> 791.20]  that when you're developing
[791.20 --> 792.60]  machine learning software
[792.60 --> 793.96]  in the DoD environment,
[794.40 --> 795.92]  we don't want you to have to use,
[795.98 --> 797.26]  you know, baby software
[797.26 --> 799.02]  software or software
[799.02 --> 800.88]  that has been largely disabled
[800.88 --> 802.02]  because, you know,
[802.04 --> 802.80]  so many of the features
[802.80 --> 803.68]  were not approved.
[804.02 --> 805.14]  So the goal very much
[805.14 --> 806.70]  is to give our communities
[806.70 --> 808.42]  of developers access
[808.42 --> 810.10]  to the same types of things
[810.10 --> 811.02]  that they would be using
[811.02 --> 812.14]  if they were doing so
[812.14 --> 813.58]  in a commercial industry environment,
[814.04 --> 815.26]  but doing so in a way
[815.26 --> 816.48]  that gives us confidence
[816.48 --> 817.70]  about the security
[817.70 --> 818.52]  of that operation.
[818.76 --> 819.38]  So there are a few,
[819.56 --> 820.90]  in the commercial world,
[821.04 --> 822.02]  a lot of what we talk about
[822.02 --> 822.84]  in software development
[822.84 --> 824.24]  is what's called DevOps,
[824.64 --> 825.72]  development operations,
[825.72 --> 827.10]  and the sort of seamless
[827.10 --> 828.16]  figure eight loop
[828.16 --> 829.24]  between those two
[829.24 --> 830.46]  where you're constantly,
[830.80 --> 831.42]  you know,
[831.82 --> 832.68]  adding features,
[832.92 --> 834.00]  deploying those features,
[834.26 --> 834.90]  gaining feedback
[834.90 --> 835.70]  from your users
[835.70 --> 837.32]  on how those features
[837.32 --> 837.82]  are used,
[837.84 --> 838.50]  which informs
[838.50 --> 840.12]  how you want to modify them
[840.12 --> 841.44]  or come to
[841.44 --> 843.22]  with a new batch of features
[843.22 --> 844.90]  or overhaul the software
[844.90 --> 845.98]  in more significant ways.
[846.56 --> 847.60]  In the Department of Defense,
[847.70 --> 848.66]  we have sort of adapted
[848.66 --> 849.50]  that paradigm
[849.50 --> 850.72]  to DevSecOps,
[850.82 --> 851.86]  which sort of recognizes
[851.86 --> 853.90]  the different security requirements
[853.90 --> 854.94]  that you might have
[854.94 --> 856.10]  at each stage
[856.10 --> 856.92]  of the development
[856.92 --> 858.46]  and operations process.
[859.00 --> 860.82]  And so for the machine learning world,
[861.18 --> 862.76]  some of this is
[862.76 --> 864.72]  relatively uncharted territory,
[864.72 --> 866.32]  which makes it exciting,
[866.66 --> 867.34]  but we're finding
[867.34 --> 868.74]  that a lot of the value
[868.74 --> 869.64]  that we can add
[869.64 --> 871.60]  is just taking,
[871.78 --> 872.26]  you know,
[872.32 --> 873.52]  commercial and academic
[873.52 --> 874.76]  and open source tools
[874.76 --> 876.02]  and adapting them
[876.02 --> 878.20]  to the national security use case.
[878.58 --> 879.14]  Gotcha.
[879.50 --> 880.34]  One of the things
[880.34 --> 881.56]  I'm kind of curious about
[881.56 --> 882.56]  is, you know,
[882.68 --> 883.60]  the very first word
[883.60 --> 884.34]  is joint
[884.34 --> 886.12]  in the organization's title.
[886.78 --> 887.40]  And you end up,
[887.54 --> 888.66]  as you described already,
[889.00 --> 889.64]  working with
[889.64 --> 890.68]  all these different partners.
[891.00 --> 892.54]  Some are from industry,
[892.70 --> 893.82]  like the company I work for.
[894.22 --> 895.16]  Some are academic,
[895.36 --> 896.20]  various universities
[896.20 --> 897.62]  that are doing great work in AI.
[898.02 --> 898.46]  Obviously,
[898.66 --> 899.72]  you work with
[899.72 --> 901.36]  the various branches
[901.36 --> 903.16]  of the military
[903.16 --> 904.44]  and they obviously
[904.44 --> 905.56]  have their own
[905.56 --> 907.26]  initiatives in AI.
[907.82 --> 908.56]  Could you talk
[908.56 --> 909.34]  a little bit
[909.34 --> 910.66]  about what those
[910.66 --> 911.50]  different types
[911.50 --> 912.40]  of interactions
[912.40 --> 913.26]  look like,
[913.56 --> 914.96]  both with industry,
[915.30 --> 916.22]  how you support it,
[916.28 --> 916.90]  what you're asking
[916.90 --> 918.02]  from it,
[918.12 --> 919.62]  as well with the academic,
[919.80 --> 920.28]  and also,
[920.48 --> 921.40]  what is the
[921.40 --> 923.16]  division of responsibility
[923.16 --> 925.02]  that the Jake has
[925.02 --> 926.46]  with the various,
[926.56 --> 926.78]  you know,
[926.82 --> 928.18]  service-specific laboratories
[928.18 --> 929.44]  that do work in AI
[929.44 --> 930.38]  in their own
[930.38 --> 931.18]  specific missions?
[931.34 --> 932.00]  What do all those
[932.00 --> 932.82]  different relationships
[932.82 --> 933.62]  look like to you?
[934.30 --> 934.54]  Sure.
[934.96 --> 935.18]  So,
[935.46 --> 936.32]  starting with
[936.32 --> 937.30]  the last part
[937.30 --> 937.90]  of your question,
[937.90 --> 939.32]  which is how we interact
[939.32 --> 940.74]  with the service laboratories,
[941.44 --> 942.40]  and I'll add
[942.40 --> 943.48]  to the service laboratories
[943.48 --> 943.92]  also,
[944.12 --> 944.26]  you know,
[944.28 --> 944.86]  an organization
[944.86 --> 945.68]  like DARPA.
[946.04 --> 946.82]  In general,
[947.22 --> 948.16]  these laboratories,
[948.66 --> 948.82]  you know,
[948.86 --> 950.60]  the Naval Research Laboratory,
[951.08 --> 952.16]  the Air Force Research Laboratory,
[952.30 --> 953.48]  the Army Research Laboratory,
[953.58 --> 954.16]  and so on,
[954.34 --> 955.30]  they are primarily
[955.30 --> 956.74]  focused more
[956.74 --> 957.76]  on advancing
[957.76 --> 958.88]  the state-of-the-art
[958.88 --> 959.60]  in AI
[959.60 --> 961.10]  and dealing
[961.10 --> 961.90]  with situations
[961.90 --> 963.02]  where the sort
[963.02 --> 963.62]  of existing
[963.62 --> 964.58]  state-of-the-art
[964.58 --> 965.94]  is not a good fit
[965.94 --> 967.64]  for military requirements.
[967.90 --> 968.26]  So,
[968.32 --> 968.84]  that's a very
[968.84 --> 969.84]  important job,
[970.06 --> 970.54]  but it's a bit
[970.54 --> 971.50]  different from the
[971.50 --> 972.70]  job of the Jake.
[973.00 --> 973.82]  We are interested
[973.82 --> 974.68]  in problems
[974.68 --> 975.84]  that we can go after
[975.84 --> 977.60]  where technology
[977.60 --> 979.02]  that is available
[979.02 --> 980.06]  in commercial industry
[980.06 --> 981.50]  or academia today,
[981.96 --> 982.38]  so sort of
[982.38 --> 983.08]  state-of-the-art
[983.08 --> 984.74]  as it currently exists,
[984.98 --> 985.70]  is a reasonably
[985.70 --> 986.42]  good fit
[986.42 --> 988.04]  for military needs.
[988.44 --> 988.68]  DARPA
[988.68 --> 989.78]  and the service laboratories
[989.78 --> 990.52]  are focused
[990.52 --> 991.48]  more on areas
[991.48 --> 992.84]  where some additional
[992.84 --> 994.04]  research and development
[994.04 --> 995.18]  is needed
[995.18 --> 996.44]  in order to
[996.44 --> 997.78]  get the technology
[997.78 --> 998.42]  to a level
[998.42 --> 999.08]  of maturity
[999.08 --> 1000.20]  where it can be
[1000.20 --> 1001.22]  useful for
[1001.22 --> 1002.02]  DoD needs.
[1002.16 --> 1002.26]  So,
[1002.48 --> 1003.20]  the way we sort
[1003.20 --> 1004.02]  of view it is
[1004.02 --> 1005.76]  if your problem
[1005.76 --> 1006.42]  is the kind
[1006.42 --> 1007.00]  of problem
[1007.00 --> 1008.46]  that can be solved
[1008.46 --> 1010.20]  in zero
[1010.20 --> 1011.42]  to five years,
[1011.88 --> 1012.52]  you're probably
[1012.52 --> 1013.12]  a better fit
[1013.12 --> 1013.74]  for the Jake.
[1014.20 --> 1015.08]  If your problem
[1015.08 --> 1015.72]  is the kind
[1015.72 --> 1016.24]  of problem
[1016.24 --> 1017.02]  where it might
[1017.02 --> 1018.02]  require five
[1018.02 --> 1019.14]  to 20 years
[1019.14 --> 1019.84]  of research
[1019.84 --> 1020.34]  and development
[1020.34 --> 1021.60]  to be solved,
[1021.72 --> 1022.44]  then it's probably
[1022.44 --> 1023.06]  a better fit
[1023.06 --> 1023.90]  for the service
[1023.90 --> 1024.46]  laboratories
[1024.46 --> 1025.08]  and DARPA.
[1025.72 --> 1026.18]  And that's not
[1026.18 --> 1027.44]  sort of a perfect
[1027.44 --> 1027.94]  summary.
[1028.22 --> 1028.56]  Of course,
[1028.72 --> 1029.54]  each of the service
[1029.54 --> 1030.30]  labs and DARPA
[1030.30 --> 1032.04]  also work on
[1032.04 --> 1033.06]  some near-term
[1033.06 --> 1033.78]  projects
[1033.78 --> 1034.78]  as needed
[1034.78 --> 1035.70]  by necessity
[1035.70 --> 1036.62]  or some specific
[1036.62 --> 1037.18]  competencies
[1037.18 --> 1037.66]  and skills
[1037.66 --> 1038.12]  they might have,
[1038.38 --> 1038.84]  but to sort of
[1038.84 --> 1039.94]  a first approximation,
[1040.48 --> 1041.04]  that kind of
[1041.04 --> 1041.66]  characterizes
[1041.66 --> 1042.28]  the division
[1042.28 --> 1042.76]  of labor
[1042.76 --> 1044.10]  between the two
[1044.10 --> 1044.56]  organizations.
[1044.94 --> 1045.72]  And the fact
[1045.72 --> 1046.18]  is,
[1046.50 --> 1046.98]  DARPA and the
[1046.98 --> 1047.68]  service laboratories
[1047.68 --> 1048.72]  have been doing
[1048.72 --> 1049.48]  amazing work
[1049.48 --> 1050.20]  and continue
[1050.20 --> 1050.90]  to do amazing
[1050.90 --> 1051.28]  work.
[1051.64 --> 1052.20]  But the Jake
[1052.20 --> 1053.56]  was kind of
[1053.56 --> 1054.26]  stood up
[1054.26 --> 1054.76]  to solve
[1054.76 --> 1055.24]  a different
[1055.24 --> 1055.80]  problem.
[1056.18 --> 1056.74]  So not the
[1056.74 --> 1057.42]  problem of
[1057.42 --> 1058.16]  advancing the
[1058.16 --> 1058.66]  state-of-the-art,
[1058.76 --> 1059.30]  but the problem
[1059.30 --> 1060.10]  of adopting
[1060.10 --> 1061.26]  the state-of-the-art
[1061.26 --> 1062.78]  as it exists
[1062.78 --> 1063.52]  in commercial
[1063.52 --> 1064.10]  industry and
[1064.10 --> 1064.60]  academia.
[1064.96 --> 1065.52]  Which gets to
[1065.52 --> 1066.28]  the second part
[1066.28 --> 1066.74]  of your question,
[1066.88 --> 1067.02]  right?
[1067.04 --> 1067.88]  How do we engage
[1067.88 --> 1068.38]  with commercial
[1068.38 --> 1069.14]  industry and
[1069.14 --> 1069.64]  academia?
[1070.14 --> 1070.94]  And the obvious
[1070.94 --> 1071.92]  answer is
[1071.92 --> 1073.38]  early and often.
[1073.92 --> 1074.56]  We have,
[1074.68 --> 1075.30]  I would say,
[1075.44 --> 1075.90]  a sort of
[1075.90 --> 1076.60]  unusually
[1076.60 --> 1077.66]  aggressive
[1077.66 --> 1079.74]  outreach program.
[1080.26 --> 1080.70]  We have
[1080.70 --> 1081.34]  one staff
[1081.34 --> 1081.84]  member who
[1081.84 --> 1082.76]  is co-located
[1082.76 --> 1083.46]  with the
[1083.46 --> 1084.28]  Defense Innovation
[1084.28 --> 1085.10]  Unit in the
[1085.10 --> 1085.56]  San Francisco
[1085.56 --> 1086.40]  Bay Area.
[1087.06 --> 1087.80]  And full-time,
[1087.94 --> 1088.98]  his job is to
[1088.98 --> 1089.74]  sort of go out,
[1090.12 --> 1090.44]  meet with
[1090.44 --> 1090.86]  companies,
[1091.14 --> 1091.38]  meet with
[1091.38 --> 1092.42]  venture capitalists,
[1092.82 --> 1093.22]  identify,
[1093.50 --> 1093.68]  you know,
[1093.74 --> 1094.22]  what is going
[1094.22 --> 1095.04]  on in the
[1095.04 --> 1095.72]  tech space
[1095.72 --> 1096.62]  that might be
[1096.62 --> 1097.54]  relevant to
[1097.54 --> 1098.02]  the types of
[1098.02 --> 1098.58]  problems that
[1098.58 --> 1099.00]  the military
[1099.00 --> 1100.12]  has and the
[1100.12 --> 1100.44]  types of
[1100.44 --> 1100.94]  problems that
[1100.94 --> 1101.30]  the Jake
[1101.30 --> 1101.62]  is either
[1101.62 --> 1102.08]  trying to
[1102.08 --> 1102.98]  tackle or
[1102.98 --> 1103.54]  might be
[1103.54 --> 1104.02]  interested in
[1104.02 --> 1104.38]  trying to
[1104.38 --> 1104.90]  tackle in the
[1104.90 --> 1105.24]  future.
[1105.80 --> 1106.16]  And the
[1106.16 --> 1106.54]  organization
[1106.54 --> 1107.04]  that he's
[1107.04 --> 1107.46]  co-located
[1107.46 --> 1108.00]  with that I
[1108.00 --> 1108.28]  mentioned,
[1108.40 --> 1108.72]  the Defense
[1108.72 --> 1109.10]  Innovation
[1109.10 --> 1109.48]  Unit,
[1109.68 --> 1110.52]  or DIU,
[1110.52 --> 1111.16]  is,
[1111.24 --> 1111.78]  similarly,
[1112.04 --> 1112.34]  that's an
[1112.34 --> 1112.90]  organization
[1112.90 --> 1114.02]  whose primary
[1114.02 --> 1115.74]  priority is
[1115.74 --> 1116.78]  improving the
[1116.78 --> 1117.16]  Department of
[1117.16 --> 1117.62]  Defense's
[1117.62 --> 1119.14]  relationship with
[1119.14 --> 1120.10]  commercial industry
[1120.10 --> 1120.56]  and the
[1120.56 --> 1121.50]  commercial technology
[1121.50 --> 1122.58]  industry especially.
[1122.94 --> 1123.44]  So there's a
[1123.44 --> 1123.90]  variety of
[1123.90 --> 1124.12]  sort of
[1124.12 --> 1124.44]  different
[1124.44 --> 1125.14]  contracting
[1125.14 --> 1125.70]  mechanisms
[1125.70 --> 1126.48]  that are
[1126.48 --> 1127.00]  designed to
[1127.00 --> 1127.30]  make it a
[1127.30 --> 1127.60]  little bit
[1127.60 --> 1128.16]  easier to
[1128.16 --> 1128.74]  do business
[1128.74 --> 1129.04]  with the
[1129.04 --> 1129.48]  Department of
[1129.48 --> 1129.88]  Defense.
[1129.88 --> 1130.80]  Folks who
[1130.80 --> 1131.20]  have not
[1131.20 --> 1131.66]  been paying
[1131.66 --> 1132.42]  close attention
[1132.42 --> 1133.64]  would probably
[1133.64 --> 1135.12]  remember that
[1135.12 --> 1135.96]  it's often
[1135.96 --> 1137.32]  very lengthy
[1137.32 --> 1138.18]  and process
[1138.18 --> 1139.42]  intensive and
[1139.42 --> 1139.84]  there's a lot
[1139.84 --> 1140.38]  of bureaucracy
[1140.38 --> 1141.26]  to do business
[1141.26 --> 1141.54]  with the
[1141.54 --> 1141.94]  Department of
[1141.94 --> 1142.30]  Defense.
[1142.86 --> 1143.20]  And that's
[1143.20 --> 1143.64]  very much
[1143.64 --> 1144.38]  something that
[1144.38 --> 1145.04]  the DOD has
[1145.04 --> 1145.44]  been working
[1145.44 --> 1146.36]  on quite
[1146.36 --> 1147.12]  intensely to
[1147.12 --> 1147.56]  reform.
[1148.06 --> 1148.32]  And so
[1148.32 --> 1149.36]  DIU in
[1149.36 --> 1150.28]  particular has
[1150.28 --> 1151.08]  pioneered the
[1151.08 --> 1152.20]  use of
[1152.20 --> 1153.32]  some not
[1153.32 --> 1154.50]  new but
[1154.50 --> 1155.18]  comparatively
[1155.18 --> 1155.88]  unfamiliar
[1155.88 --> 1157.10]  contracting and
[1157.10 --> 1157.60]  acquisition
[1157.60 --> 1158.92]  techniques such
[1158.92 --> 1159.28]  as other
[1159.28 --> 1159.84]  transaction
[1159.84 --> 1160.36]  agreements.
[1161.18 --> 1161.72]  And these
[1161.72 --> 1162.22]  allow you to
[1162.22 --> 1162.90]  sort of get
[1162.90 --> 1163.56]  on contract
[1163.56 --> 1164.24]  quicker, get
[1164.24 --> 1164.92]  money flowing
[1164.92 --> 1165.50]  quicker, and
[1165.50 --> 1166.04]  actually start
[1166.04 --> 1166.74]  doing work
[1166.74 --> 1167.14]  quicker.
[1167.52 --> 1168.10]  And to that
[1168.10 --> 1169.04]  the Jake has
[1169.04 --> 1170.58]  also been an
[1170.58 --> 1173.20]  early adopter of
[1173.20 --> 1174.42]  commercial solution
[1174.42 --> 1175.82]  openings which is
[1175.82 --> 1176.50]  sort of another
[1176.50 --> 1177.66]  contracting mechanism.
[1178.02 --> 1178.78]  And the important
[1178.78 --> 1179.42]  feature of these
[1179.42 --> 1180.72]  mechanisms is again
[1180.72 --> 1181.68]  it makes it easier
[1181.68 --> 1183.02]  to do business
[1183.02 --> 1183.90]  with commercial
[1183.90 --> 1184.94]  technology companies
[1184.94 --> 1185.86]  and it makes it
[1185.86 --> 1186.56]  easier to do
[1186.56 --> 1187.36]  business with
[1187.36 --> 1188.12]  sort of smaller
[1188.12 --> 1189.26]  companies who
[1189.26 --> 1189.78]  can't always
[1189.78 --> 1190.64]  afford the
[1190.64 --> 1191.92]  overhead required
[1191.92 --> 1192.82]  to do business
[1192.82 --> 1193.30]  with the Department
[1193.30 --> 1193.96]  of Defense for
[1193.96 --> 1194.46]  our bidding
[1194.46 --> 1195.68]  process and our
[1195.68 --> 1196.62]  proposal writing
[1196.62 --> 1197.28]  process.
[1197.98 --> 1198.48]  I'm coming at
[1198.48 --> 1199.34]  this conversation
[1199.34 --> 1200.80]  as someone who
[1200.80 --> 1202.22]  is not deeply
[1202.22 --> 1203.86]  involved in the
[1203.86 --> 1205.48]  defense world
[1205.48 --> 1206.64]  but one of the
[1206.64 --> 1207.44]  things that was
[1207.44 --> 1208.44]  kind of coming
[1208.44 --> 1209.44]  to my mind as
[1209.44 --> 1210.26]  we entered into
[1210.26 --> 1211.06]  the conversation
[1211.06 --> 1212.04]  was I was
[1212.04 --> 1213.12]  wondering how
[1213.12 --> 1213.90]  much of the
[1213.90 --> 1214.90]  strategy that
[1214.90 --> 1215.96]  you're putting
[1215.96 --> 1216.72]  into this
[1216.72 --> 1217.50]  that the
[1217.50 --> 1218.54]  DOD is
[1218.54 --> 1219.34]  doing is
[1219.34 --> 1220.08]  driven by
[1220.08 --> 1221.02]  what other
[1221.02 --> 1221.88]  maybe potential
[1221.88 --> 1222.80]  adversaries are
[1222.80 --> 1223.76]  doing in AI
[1223.76 --> 1224.68]  and like what
[1224.68 --> 1225.48]  is the landscape
[1225.48 --> 1227.06]  of AI and
[1227.06 --> 1228.06]  defense look like
[1228.06 --> 1228.84]  around the world
[1228.84 --> 1229.82]  and how has that
[1229.82 --> 1231.06]  impacted the
[1231.06 --> 1231.94]  priority we put
[1231.94 --> 1233.00]  onto it and
[1233.00 --> 1233.74]  then like how
[1233.74 --> 1234.50]  we go about
[1234.50 --> 1235.20]  you know
[1235.20 --> 1235.94]  developing that
[1235.94 --> 1236.44]  technology.
[1237.18 --> 1237.62]  Sure I mean I
[1237.62 --> 1238.46]  would start by
[1238.46 --> 1240.16]  saying that the
[1240.16 --> 1242.06]  two countries are
[1242.06 --> 1243.72]  specifically named
[1243.72 --> 1245.02]  by the national
[1245.02 --> 1246.08]  defense strategy
[1246.08 --> 1247.04]  which came out
[1247.04 --> 1247.84]  in 2018
[1247.84 --> 1249.28]  two countries are
[1249.28 --> 1250.22]  specifically named
[1250.22 --> 1251.42]  as strategic
[1251.42 --> 1251.98]  competitors
[1251.98 --> 1253.42]  and that is
[1253.42 --> 1254.18]  Russia and
[1254.18 --> 1255.42]  China and so
[1255.42 --> 1255.82]  these are
[1255.82 --> 1256.70]  countries who
[1256.70 --> 1257.76]  have interests
[1257.76 --> 1258.36]  that are
[1258.36 --> 1259.42]  identified as
[1259.42 --> 1260.04]  being you know
[1260.04 --> 1261.36]  contrary and in
[1261.36 --> 1262.26]  contradiction to
[1262.26 --> 1263.10]  in many cases
[1263.10 --> 1264.06]  the interests of
[1264.06 --> 1264.82]  the United States
[1264.82 --> 1266.00]  and also who have
[1266.00 --> 1266.94]  oriented their
[1266.94 --> 1267.90]  national security
[1267.90 --> 1269.46]  establishments in
[1269.46 --> 1270.48]  competition with
[1270.48 --> 1271.36]  the United States
[1271.36 --> 1273.06]  and that's not a
[1273.06 --> 1274.28]  very surprising
[1274.28 --> 1275.58]  statement I would
[1275.58 --> 1276.72]  say to most I
[1276.72 --> 1277.08]  mean when the
[1277.08 --> 1277.66]  national defense
[1277.66 --> 1278.72]  strategy came out
[1278.72 --> 1279.58]  it was sort of
[1279.58 --> 1280.42]  putting on paper
[1280.42 --> 1281.22]  the sorts of
[1281.22 --> 1282.20]  things that a lot
[1282.20 --> 1283.28]  of United States
[1283.28 --> 1283.90]  leaders had been
[1283.90 --> 1285.04]  saying and frankly
[1285.04 --> 1285.64]  that you know a
[1285.64 --> 1286.58]  lot of leaders in
[1286.58 --> 1287.60]  the two countries I
[1287.60 --> 1288.16]  just mentioned
[1288.16 --> 1289.30]  were also saying
[1289.30 --> 1290.32]  so that's the
[1290.32 --> 1290.96]  sort of basic
[1290.96 --> 1291.94]  backdrop of
[1291.94 --> 1292.94]  strategic competition
[1292.94 --> 1294.02]  into artificial
[1294.02 --> 1295.30]  intelligence of
[1295.30 --> 1295.94]  course this is the
[1295.94 --> 1296.74]  national security
[1296.74 --> 1297.76]  world we're talking
[1297.76 --> 1298.38]  about and the
[1298.38 --> 1298.96]  military we're
[1298.96 --> 1300.08]  talking about so we
[1300.08 --> 1300.74]  remain quite
[1300.74 --> 1302.04]  interested in what
[1302.04 --> 1303.04]  is going on around
[1303.04 --> 1304.02]  the world and we
[1304.02 --> 1304.94]  would be silly not
[1304.94 --> 1305.38]  to be paying
[1305.38 --> 1306.70]  attention to that I
[1306.70 --> 1307.74]  think speaking about
[1307.74 --> 1308.88]  China and Russia
[1308.88 --> 1310.72]  each in turn China's
[1310.72 --> 1312.12]  AI strategy which
[1312.12 --> 1313.36]  came out in 2017
[1313.36 --> 1314.66]  you know specifically
[1314.66 --> 1316.16]  identifies that they
[1316.16 --> 1317.24]  see AI as a
[1317.24 --> 1317.78]  transformative
[1317.78 --> 1319.04]  technology in many
[1319.04 --> 1319.88]  different areas
[1319.88 --> 1321.34]  including in national
[1321.34 --> 1322.34]  security and it
[1322.34 --> 1323.90]  also identifies AI
[1323.90 --> 1325.30]  as a leapfrog
[1325.30 --> 1327.06]  technology the term
[1327.06 --> 1328.10]  leapfrog is
[1328.10 --> 1328.92]  interesting in this
[1328.92 --> 1330.22]  use case because it
[1330.22 --> 1330.78]  is described
[1330.78 --> 1332.00]  elsewhere by
[1332.00 --> 1332.92]  Chinese military
[1332.92 --> 1333.60]  thinkers and
[1333.60 --> 1335.02]  strategists as
[1335.02 --> 1336.04]  really sort of
[1336.04 --> 1337.24]  describing their
[1337.24 --> 1338.12]  their belief about
[1338.12 --> 1339.40]  what AI technology
[1339.40 --> 1340.48]  will enable their
[1340.48 --> 1341.86]  military compared to
[1341.86 --> 1342.42]  the United States
[1342.42 --> 1344.08]  military so if you
[1344.08 --> 1345.18]  can think about the
[1345.18 --> 1346.98]  example of cellular
[1346.98 --> 1348.00]  telecommunications
[1348.00 --> 1349.70]  infrastructure in
[1349.70 --> 1350.88]  developing countries
[1350.88 --> 1351.84]  notably you know
[1351.84 --> 1352.34]  many developing
[1352.34 --> 1353.32]  countries in Africa
[1353.32 --> 1354.24]  this is the
[1354.24 --> 1355.58]  canonical example of
[1355.58 --> 1356.02]  a leapfrog
[1356.02 --> 1357.16]  technology there
[1357.16 --> 1357.60]  were many
[1357.60 --> 1358.64]  developing countries
[1358.64 --> 1359.50]  in Africa who
[1359.50 --> 1360.56]  did not have
[1360.56 --> 1361.96]  well built out
[1361.96 --> 1363.32]  landline telephone
[1363.32 --> 1364.98]  infrastructure and
[1364.98 --> 1366.04]  yet this was no
[1366.04 --> 1367.24]  disadvantage whatsoever
[1367.24 --> 1367.98]  in adopting
[1367.98 --> 1369.14]  cellular telephone
[1369.14 --> 1370.16]  infrastructure they
[1370.16 --> 1371.50]  just skipped the
[1371.50 --> 1372.56]  development step of
[1372.56 --> 1373.80]  landline telephones and
[1373.80 --> 1374.38]  went straight to
[1374.38 --> 1375.78]  cell phones and that
[1375.78 --> 1376.86]  skipping is is
[1376.86 --> 1377.52]  referred to as
[1377.52 --> 1378.82]  leapfrogging and
[1378.82 --> 1379.78]  in our competition
[1379.78 --> 1380.64]  with China in
[1380.64 --> 1381.46]  military technology
[1381.46 --> 1382.08]  there are many
[1382.08 --> 1382.80]  things that we are
[1382.80 --> 1384.12]  quite good at that
[1384.12 --> 1385.10]  they are have a very
[1385.10 --> 1386.02]  hard time with in
[1386.02 --> 1386.58]  a technological
[1386.58 --> 1387.46]  sense things like
[1387.46 --> 1388.78]  jet engines things
[1388.78 --> 1389.48]  like aircraft
[1389.48 --> 1390.82]  carriers these are
[1390.82 --> 1391.78]  really tough
[1391.78 --> 1392.72]  technologies really
[1392.72 --> 1393.70]  complicated technologies
[1393.70 --> 1395.58]  that we are you
[1395.58 --> 1396.22]  know as a country
[1396.22 --> 1397.04]  tend to be quite good
[1397.04 --> 1398.08]  at and that China
[1398.08 --> 1398.86]  as a country has
[1398.86 --> 1399.66]  historically had a
[1399.66 --> 1400.30]  lot of difficulty
[1400.30 --> 1401.24]  with and so when
[1401.24 --> 1402.12]  they write about AI
[1402.12 --> 1402.88]  technology they're
[1402.88 --> 1404.08]  saying well if we
[1404.08 --> 1405.68]  could really develop
[1405.68 --> 1406.30]  an interesting
[1406.30 --> 1408.26]  advantage in AI
[1408.26 --> 1410.00]  perhaps we could
[1410.00 --> 1410.88]  leapfrog the United
[1410.88 --> 1411.82]  States which is to
[1411.82 --> 1413.24]  say perhaps we would
[1413.24 --> 1414.44]  not have to catch up
[1414.44 --> 1415.78]  to them in aircraft
[1415.78 --> 1416.90]  carriers or catch up
[1416.90 --> 1417.94]  to them in jet
[1417.94 --> 1418.76]  engines because we
[1418.76 --> 1419.84]  will shift the basis
[1419.84 --> 1421.56]  of competition and
[1421.56 --> 1422.24]  they write you know
[1422.24 --> 1422.88]  Chinese military
[1422.88 --> 1423.80]  thinkers often write
[1423.80 --> 1424.66]  quite optimistically
[1424.66 --> 1426.04]  about China's
[1426.04 --> 1427.40]  opportunity to compete
[1427.40 --> 1428.30]  with the United States
[1428.30 --> 1429.20]  technologically in
[1429.20 --> 1430.66]  these terms so you
[1430.66 --> 1431.16]  know we would be
[1431.16 --> 1432.50]  remiss if we were not
[1432.50 --> 1433.44]  paying attention to
[1433.44 --> 1434.72]  that the second thing
[1434.72 --> 1436.02]  I will say is that
[1436.02 --> 1437.16]  as pointed out by the
[1437.16 --> 1438.12]  Secretary of Defense
[1438.12 --> 1439.18]  at the National Security
[1439.18 --> 1441.36]  Commission on AI in
[1441.36 --> 1442.52]  his speech at that
[1442.52 --> 1443.38]  commission you know
[1443.38 --> 1444.20]  there are many Chinese
[1444.20 --> 1445.38]  weapons manufacturers
[1445.38 --> 1446.44]  who are currently
[1446.44 --> 1447.52]  selling on
[1447.52 --> 1448.70]  international markets
[1448.70 --> 1450.02]  weapons systems
[1450.02 --> 1452.26]  advertised as being
[1452.26 --> 1453.64]  autonomous meaning
[1453.64 --> 1454.46]  they can sort of make
[1454.46 --> 1455.12]  their own decisions
[1455.12 --> 1456.10]  and act independently
[1456.10 --> 1457.64]  and also you know
[1457.64 --> 1458.76]  having that full
[1458.76 --> 1460.40]  combat autonomy meaning
[1460.40 --> 1460.96]  they can you know
[1460.96 --> 1461.78]  actually be responsible
[1461.78 --> 1462.58]  for the use of
[1462.58 --> 1463.74]  lethal force and
[1463.74 --> 1464.50]  so that's what China
[1464.50 --> 1465.22]  is sort of up to
[1465.22 --> 1466.30]  today at least in
[1466.30 --> 1466.86]  terms of what they're
[1466.86 --> 1467.92]  advertising on the
[1467.92 --> 1468.80]  international market
[1468.80 --> 1470.64]  Russia is similarly you
[1470.64 --> 1471.84]  know very interested in
[1471.84 --> 1473.34]  AI technology one
[1473.34 --> 1474.64]  quote that everybody
[1474.64 --> 1475.54]  really paid attention
[1475.54 --> 1476.74]  to was in September
[1476.74 --> 1478.70]  of 2017 when
[1478.70 --> 1479.76]  Vladimir Putin said
[1479.76 --> 1480.32]  that you know whoever
[1480.32 --> 1481.64]  leads in AI technology
[1481.64 --> 1482.66]  will be the ruler of
[1482.66 --> 1484.24]  the world and I think
[1484.24 --> 1486.12]  Russia does not have a
[1486.12 --> 1487.46]  very clear path to
[1487.46 --> 1488.84]  leading in AI technology
[1488.84 --> 1490.28]  whereas the United
[1490.28 --> 1492.00]  States and China you
[1492.00 --> 1493.22]  know regularly top the
[1493.22 --> 1494.62]  lists of who is
[1494.62 --> 1496.12]  publishing the most AI
[1496.12 --> 1497.42]  research papers annually
[1497.42 --> 1498.80]  and who is publishing
[1498.80 --> 1500.30]  the best AI research
[1500.30 --> 1501.84]  papers annually and
[1501.84 --> 1503.20]  similarly lead in
[1503.20 --> 1504.32]  measurements about who
[1504.32 --> 1505.22]  is attracting the most
[1505.22 --> 1506.52]  you know venture capital
[1506.52 --> 1508.06]  for AI companies you
[1508.06 --> 1509.00]  know Russia is pretty
[1509.00 --> 1510.12]  low on all of the
[1510.12 --> 1511.06]  rankings that I just
[1511.06 --> 1512.50]  mentioned so I don't
[1512.50 --> 1513.44]  think that Russia has a
[1513.44 --> 1515.00]  clear path to leading in
[1515.00 --> 1516.36]  AI technology unfortunately
[1516.36 --> 1518.22]  they do have a reasonably
[1518.22 --> 1519.88]  clear path to leading in
[1519.88 --> 1521.38]  the weaponization of AI
[1521.38 --> 1523.10]  technology I think this is a
[1523.10 --> 1524.56]  pretty similar story to the
[1524.56 --> 1526.62]  internet Russia was not a
[1526.62 --> 1528.36]  leader in any of the
[1528.36 --> 1529.14]  foundational technologies
[1529.14 --> 1530.90]  technologies for computer
[1530.90 --> 1532.44]  networking or the internet
[1532.44 --> 1534.18]  and yet nevertheless you
[1534.18 --> 1535.10]  know Russia developed a
[1535.10 --> 1537.12]  very advanced and broad and
[1537.12 --> 1539.12]  deep cyber capability
[1539.12 --> 1540.46]  military cyber capability
[1540.46 --> 1542.62]  and so similarly I think
[1542.62 --> 1544.00]  you know Russia is looking
[1544.00 --> 1545.26]  to be a leader in the
[1545.26 --> 1546.78]  weaponization of AI just as
[1546.78 --> 1547.52]  they were a leader in the
[1547.52 --> 1548.34]  weaponization of the
[1548.34 --> 1549.36]  internet in terms of what
[1549.36 --> 1551.04]  they're doing it's a lot of
[1551.04 --> 1552.18]  what you would expect the
[1552.18 --> 1553.36]  social media disinformation
[1553.36 --> 1556.10]  campaigns and influence
[1556.10 --> 1558.36]  operations that Russia has
[1558.36 --> 1559.50]  been in the news a lot for
[1559.50 --> 1560.84]  lately they are also
[1560.84 --> 1562.04]  interested in bringing more
[1562.04 --> 1563.40]  advanced machine learning and
[1563.40 --> 1564.72]  AI capabilities to these
[1564.72 --> 1566.22]  operations and then
[1566.22 --> 1568.28]  secondarily combat robotics
[1568.28 --> 1570.66]  is an area that Russia has
[1570.66 --> 1571.80]  devoted a lot of investment
[1571.80 --> 1573.00]  and has shown a lot of
[1573.00 --> 1574.40]  interest and they're
[1574.40 --> 1576.06]  experimenting with a lot of
[1576.06 --> 1576.96]  their military robotic
[1576.96 --> 1578.78]  systems operationally
[1578.78 --> 1580.14]  literally you know using some
[1580.14 --> 1582.08]  of these systems in Syria so
[1582.08 --> 1583.48]  both Russia and China are
[1583.48 --> 1585.44]  moving out aggressively to
[1585.44 --> 1586.76]  incorporate AI capabilities
[1586.76 --> 1588.66]  into their military I would
[1588.66 --> 1589.80]  say you know in terms of
[1589.80 --> 1591.14]  the United States's response
[1591.14 --> 1593.76]  you know our intent is to
[1593.76 --> 1595.36]  lead the world in the
[1595.36 --> 1597.34]  military use of AI for the
[1597.34 --> 1598.90]  benefit of United States
[1598.90 --> 1600.52]  national security I don't
[1600.52 --> 1601.72]  think we're so much you know
[1601.72 --> 1603.80]  obsessing over each individual
[1603.80 --> 1606.06]  capability that you know that
[1606.06 --> 1607.52]  comes out of China or Russia
[1607.52 --> 1609.12]  so much as we are sort of
[1609.12 --> 1610.12]  looking at the broader
[1610.12 --> 1612.68]  landscape I think AI is a
[1612.68 --> 1614.78]  general purpose technology the
[1614.78 --> 1615.96]  way electricity is a general
[1615.96 --> 1617.38]  purpose technology it's useful
[1617.38 --> 1618.94]  for things like radio but it's
[1618.94 --> 1620.40]  also useful for light bulbs
[1620.40 --> 1622.32]  similarly computers are useful
[1622.32 --> 1623.62]  for for just about everything
[1623.62 --> 1625.44]  and and we similarly think that
[1625.44 --> 1627.52]  AI ultimately has a lot of
[1627.52 --> 1629.26]  application specific
[1629.26 --> 1631.58]  opportunities for us so we're
[1631.58 --> 1633.04]  interested in in leading in AI
[1633.04 --> 1635.16]  in in the broad sense and
[1635.16 --> 1636.60]  would I be correct in saying
[1636.60 --> 1638.02]  then that of course there's
[1638.02 --> 1639.34]  certain things that you know
[1639.34 --> 1641.40]  even me not being involved in the
[1641.40 --> 1643.54]  defense industry at all like I'm
[1643.54 --> 1646.40]  aware of for example China using
[1646.40 --> 1648.58]  facial recognition technology and
[1648.58 --> 1650.96]  Russia interfering in elections
[1650.96 --> 1653.24]  and doing behavioral type of stuff
[1653.24 --> 1656.00]  like you talked about and so would
[1656.00 --> 1657.18]  I be correct in saying that
[1657.18 --> 1658.92]  there's kind of for every
[1658.92 --> 1660.66]  different type of AI model you can
[1660.66 --> 1661.72]  think of whether that's you know
[1661.72 --> 1663.18]  natural language processing
[1663.18 --> 1666.38]  computer vision object recognition
[1666.38 --> 1669.36]  trend analysis forecasting there's
[1669.36 --> 1672.04]  there's probably all sorts because
[1672.04 --> 1673.78]  this is general purpose like you say
[1673.78 --> 1677.64]  there's probably a way to weaponize
[1677.64 --> 1680.40]  all sorts of those types of models
[1680.40 --> 1682.20]  it's just not that you know facial
[1682.20 --> 1685.22]  recognition is is an issue it's you
[1685.22 --> 1688.00]  know a whole varied range of things
[1688.00 --> 1690.28]  that could be at play yeah I think
[1690.28 --> 1692.16]  machine learning is just a new way to
[1692.16 --> 1694.30]  create software you know traditionally
[1694.30 --> 1697.60]  software required you know every line
[1697.60 --> 1700.40]  of code to be typed out by human hands
[1700.40 --> 1702.86]  but suddenly there's been a vast
[1702.86 --> 1704.78]  improvement in this this field of
[1704.78 --> 1706.06]  artificial intelligence known as
[1706.06 --> 1708.38]  machine learning from which as I'm
[1708.38 --> 1709.54]  sure most of your listeners already
[1709.54 --> 1711.08]  know you know from which we can
[1711.08 --> 1713.04]  program or to a certain extent the
[1713.04 --> 1715.46]  system can program itself based on
[1715.46 --> 1717.76]  what it learns from data and so that
[1717.76 --> 1720.78]  general truth about the rise in in
[1720.78 --> 1722.82]  machine learning software well that's
[1722.82 --> 1724.86]  useful for most of the places where
[1724.86 --> 1726.76]  software is useful which is to say
[1726.76 --> 1728.28]  absolutely everything whether that
[1728.28 --> 1730.74]  everything is a missile guidance system
[1730.74 --> 1732.84]  or sort of you know back office
[1732.84 --> 1735.84]  applications like word processing I
[1735.84 --> 1738.04]  think over the long term and I do want
[1738.04 --> 1740.10]  to emphasize long term because while
[1740.10 --> 1741.38]  some of this transformation will be
[1741.38 --> 1743.44]  quick some of it won't over the long
[1743.44 --> 1745.00]  term we expect you know machine
[1745.00 --> 1747.82]  learning AI to be useful for just
[1747.82 --> 1749.66]  about everything right from the from
[1749.66 --> 1751.56]  the most backwater parts of the back
[1751.56 --> 1753.32]  office to the front lines of the
[1753.32 --> 1756.28]  battlefield so one of the things that
[1756.28 --> 1757.52]  you were talking about a moment ago
[1757.52 --> 1759.70]  was kind of the the our our
[1759.70 --> 1762.66]  adversaries perspective on you know
[1762.66 --> 1765.82]  they are kind of advertising AI in a
[1765.82 --> 1768.22]  lethal context and stuff I'm assuming
[1768.22 --> 1771.40]  that the US Department of Defense has a
[1771.40 --> 1773.56]  policy out there regarding how we think
[1773.56 --> 1776.68]  about AI being incorporated into lethal
[1776.68 --> 1779.90]  force scenarios can you talk about that
[1779.90 --> 1782.76]  what is the American viewpoint on that
[1782.76 --> 1784.82]  question well sure I think I think the
[1784.82 --> 1787.48]  first thing I would point out is that the
[1787.48 --> 1790.14]  Department of Defense you know abides by
[1790.14 --> 1792.92]  the law of war and for folks who are not
[1792.92 --> 1794.70]  familiar you know with the national
[1794.70 --> 1797.94]  security context the law of war might
[1797.94 --> 1799.60]  not be familiar to them these are the
[1799.60 --> 1801.16]  you know literally legally binding
[1801.16 --> 1803.80]  principles that are enshrined in
[1803.80 --> 1805.48]  documents such as the Geneva
[1805.48 --> 1807.78]  Convention but also have flow down
[1807.78 --> 1811.42]  requirements to DOD policy DOD training
[1811.42 --> 1813.52]  rules of engagement in different
[1813.52 --> 1816.56]  scenarios so the overarching thing which
[1816.56 --> 1819.46]  guides all you know US conduct in
[1819.46 --> 1821.68]  military operations is the principles
[1821.68 --> 1823.88]  underlying the law of war and these
[1823.88 --> 1825.94]  principles really get to you know when
[1825.94 --> 1828.46]  is the use of force appropriate when is
[1828.46 --> 1830.72]  it acceptable and and let me just you
[1830.72 --> 1832.20]  know sort of list some of the key
[1832.20 --> 1834.02]  principles underlying that military
[1834.02 --> 1836.84]  necessity right was your use of force
[1836.84 --> 1839.28]  that the only way that you could achieve
[1839.28 --> 1840.80]  the objective that you had to achieve
[1840.80 --> 1843.64]  proportionality if somebody slapped you in
[1843.64 --> 1846.02]  the face you know did you respond with a
[1846.02 --> 1847.72]  nuclear weapon well then that would not
[1847.72 --> 1849.74]  be a proportional response distinction
[1850.34 --> 1852.74]  right did you make every effort to
[1852.74 --> 1856.20]  prevent harming civilians and only harming
[1856.20 --> 1858.62]  enemy military combatants you know
[1858.62 --> 1861.70]  humanity did you use any means you know
[1861.70 --> 1864.20]  that violate the principle of humanity and
[1864.20 --> 1866.84]  of course you know abiding by the military
[1866.84 --> 1869.04]  principle of honor so those ethical
[1869.04 --> 1870.76]  principles you know the Department of
[1870.76 --> 1873.58]  Defense has been guided by those and these
[1873.58 --> 1875.28]  are actually legally binding you know you
[1875.28 --> 1876.92]  could be court-martialed for failing to
[1876.92 --> 1878.92]  abide by these principles but those have
[1878.92 --> 1880.14]  been guiding the Department of Defense for
[1880.14 --> 1883.08]  decades now to that there are two two
[1883.08 --> 1885.86]  things that are comparatively new the
[1885.86 --> 1887.64]  first is the Department of Defense
[1887.64 --> 1891.84]  Directive 3000.09 which relates to the use of
[1891.84 --> 1894.60]  autonomy in weapons systems and the second and
[1894.60 --> 1898.36]  that was a policy that was released in 2012
[1898.36 --> 1902.48]  and was widely praised at the time and that
[1902.48 --> 1905.20]  policy was renewed and essentially made
[1905.20 --> 1908.94]  permanent in 2017 you know basically you know
[1908.94 --> 1912.28]  neither Russia you know nor China have any
[1912.28 --> 1916.96]  kind of policy comparable to 3000.09 which I think
[1916.96 --> 1920.54]  says a lot right and then there's also our what
[1920.54 --> 1923.88]  what came out just recently which is the Defense
[1923.88 --> 1927.68]  Innovation Board's principles for the ethical
[1927.68 --> 1928.54]  use of AI.
[1934.64 --> 1937.10]  This episode is brought to you by Brave.
[1937.50 --> 1939.34]  We deserve a better internet.
[1939.66 --> 1941.98]  That's why the team behind Brave reimagined what
[1941.98 --> 1943.00]  a browser could be.
[1943.56 --> 1945.44]  Brave is like Chrome the good parts.
[1945.74 --> 1947.36]  Even your extensions will just work.
[1947.36 --> 1949.90]  It has built-in ad and tracker blocking, easy
[1949.90 --> 1952.10]  anonymization with the Tor network, earn tokens
[1952.10 --> 1954.16]  while you browse and use them to tip your
[1954.16 --> 1956.08]  favorite creators and did I mention is
[1956.08 --> 1956.84]  lightning fast.
[1957.18 --> 1958.98]  Turns out the web is super fast when you
[1958.98 --> 1959.78]  remove all the cruft.
[1960.12 --> 1962.00]  Download Brave today using the link in the
[1962.00 --> 1963.86]  show notes and give tipping a try on
[1963.86 --> 1964.82]  changelog.com.
[1964.82 --> 1977.66]  So Greg I know one of the really hot and
[1977.66 --> 1981.20]  important topics these days in AI is kind
[1981.20 --> 1984.76]  of the ethical concerns ethical principles
[1984.76 --> 1988.52]  of how you apply AI and what that means and
[1988.52 --> 1990.32]  I know both in the defense industry as well
[1990.32 --> 1991.92]  as in lots of different commercial
[1991.92 --> 1994.04]  industries that has become a big thing and
[1994.04 --> 1996.40]  you know a while back we saw Google and
[1996.40 --> 1998.20]  Microsoft and other large organizations
[1998.20 --> 2001.18]  releasing kind of public principles and
[2001.18 --> 2002.82]  frameworks about how they thought about
[2002.82 --> 2005.36]  this and I know in the defense industry
[2005.36 --> 2008.86]  there is an organization made up of a lot
[2008.86 --> 2012.42]  of experts from outside the defense
[2012.42 --> 2013.54]  establishment itself.
[2013.54 --> 2016.06]  It's called the Defense Innovation Board
[2016.06 --> 2019.90]  and they had a fairly substantial conversation
[2019.90 --> 2023.10]  around AI ethics and principles and recently
[2023.10 --> 2026.28]  released a document that covered a lot of
[2026.28 --> 2029.00]  that and I am told that you were pretty
[2029.00 --> 2031.98]  involved in that process as was the Jake at
[2031.98 --> 2034.74]  large and that and I was wondering if you
[2034.74 --> 2036.82]  could kind of talk a little bit about your
[2036.82 --> 2038.34]  involvement what it means to you and
[2038.34 --> 2040.80]  actually go through what those principles
[2040.80 --> 2042.80]  that you guys worked on are and how that
[2042.80 --> 2046.30]  relates back to the Jake and what the DOD will
[2046.30 --> 2047.30]  be doing going forward.
[2047.30 --> 2050.18]  Sure so the Defense Innovation Board is a
[2050.18 --> 2052.62]  federally appointed advisory committee so
[2052.62 --> 2054.18]  while they are not actually part of the
[2054.18 --> 2056.16]  Department of Defense the federal government
[2056.16 --> 2058.12]  has sort of given them an official
[2058.12 --> 2060.62]  relationship whereby they can advise the
[2060.62 --> 2062.52]  Department of Defense and when we released
[2062.52 --> 2065.56]  the DOD AI strategy in the summer of 2018
[2065.56 --> 2068.70]  it was immediately obvious to us that the
[2068.70 --> 2071.32]  ethical considerations of AI technology was
[2071.32 --> 2072.82]  something that we wanted to take very
[2072.82 --> 2074.52]  seriously and that we wanted to understand
[2074.52 --> 2077.06]  very thoroughly. So the Secretary of Defense
[2077.06 --> 2079.40]  asked the Defense Innovation Board to run a
[2079.40 --> 2081.56]  study about the ethical implications of AI
[2081.56 --> 2084.38]  and recommendations for principles for the
[2084.38 --> 2086.88]  Department of Defense's use of AI technology.
[2087.06 --> 2090.56]  They ran a very robust process. They were
[2090.56 --> 2093.44]  working on this for 15 months. They held
[2093.44 --> 2096.70]  three you know public forums at leading
[2096.70 --> 2099.74]  universities in the United States. They ran
[2099.74 --> 2102.62]  multiple you know rounds of open calls
[2102.62 --> 2106.00]  for comment on the subject from expert
[2106.00 --> 2108.00]  communities and also just the general public.
[2108.64 --> 2110.88]  And they ended up talking to hundreds of
[2110.88 --> 2113.78]  you know not just leading AI researchers and
[2113.78 --> 2117.24]  leading AI industry types but also ethicists,
[2117.54 --> 2120.80]  lawyers and folks with perspective from a lot of
[2120.80 --> 2123.14]  different industries and walks of life. So this
[2123.14 --> 2126.24]  was a lengthy robust process and the report
[2126.24 --> 2130.50]  that they released on October 31st 2019 you
[2130.50 --> 2132.74]  know reflects their best judgment at the
[2132.74 --> 2136.86]  intersection of you know ethical obligations, the
[2136.86 --> 2139.70]  requirements of the domain of national security and
[2139.70 --> 2142.16]  the mission of the Department of Defense and then
[2142.16 --> 2145.76]  the nuances of AI technology. And so they are an
[2145.76 --> 2148.06]  independent organization helping out the
[2148.06 --> 2150.62]  Department of Defense in these issues. So I was not
[2150.62 --> 2153.66]  involved in the actual writing of these principles.
[2153.66 --> 2158.14]  My only involvement was giving advice on how they could
[2158.14 --> 2160.70]  structure this to maximize the benefit from the
[2160.70 --> 2163.96]  Department of Defense's perspective as a consumer. So
[2163.96 --> 2167.10]  helping them craft actionable recommendations and
[2167.10 --> 2169.70]  thinking through you know how to how to write their
[2169.70 --> 2172.32]  recommendations in a way that would actually be
[2172.32 --> 2175.32]  compatible with the DoD bureaucracy and the DoD process.
[2175.32 --> 2179.78]  But what came back ended up being really quite
[2179.78 --> 2182.98]  substantive and something that you know we take
[2182.98 --> 2185.14]  seriously here in the department as is now it is it
[2185.14 --> 2187.96]  falls to us to implement them and also something that
[2187.96 --> 2191.64]  our allies whether that be you know in Europe or in Asia or
[2191.64 --> 2195.36]  elsewhere our allies have shown a great deal of interest in
[2195.36 --> 2198.34]  these principles as helping think through how do we
[2198.34 --> 2201.28]  recognize the legitimate ethical concerns that the rise of AI
[2201.28 --> 2205.84]  technology raises while also being able to move forward and
[2205.84 --> 2208.68]  use this technology you know in the mission of national
[2208.68 --> 2212.00]  security. So maybe I'll just sort of go through each of the
[2212.00 --> 2214.34]  principles that the DIB is recommending that the Department
[2214.34 --> 2216.96]  of Defense adopt and we can sort of think about how the DoD
[2216.96 --> 2218.26]  thinks about these issues.
[2218.90 --> 2221.80]  Yeah if you can kind of hit the six and then and then kind of
[2221.80 --> 2224.90]  dive in however you want to the dozen recommendations
[2224.90 --> 2227.14]  afterwards and just kind of just so name what the six
[2227.14 --> 2229.80]  principles are and and then talk about what those
[2229.80 --> 2232.42]  recommendations that came out of that if that's okay with you.
[2232.86 --> 2237.20]  Absolutely. So the principles start with responsible. So
[2237.20 --> 2241.18]  this is that human beings should exercise appropriate levels
[2241.18 --> 2244.14]  of judgment and remain responsible for the development
[2244.14 --> 2248.86]  deployment and outcomes of AI systems. Second is equitable
[2248.86 --> 2252.22]  that DoD should take deliberate steps to avoid unintended bias
[2252.22 --> 2255.46]  and development and deployment of combat or non combat AI
[2255.46 --> 2258.80]  systems that would inadvertently cause harm to persons. Third is
[2258.80 --> 2262.24]  traceable that DoD's AI engineering discipline should be
[2262.24 --> 2265.62]  sufficiently advanced that technical experts possess an
[2265.62 --> 2268.44]  appropriate understanding of the technology the development
[2268.44 --> 2271.72]  process and operational methods of AI systems including
[2271.72 --> 2275.22]  transparent and auditable methodologies data sources and
[2275.22 --> 2279.94]  design procedure and documentation. Fourth is reliable DoD AI systems
[2279.94 --> 2283.54]  should have an explicit well-defined domain of use and the safety
[2283.54 --> 2287.20]  security and robustness of such systems should be tested and assured
[2287.20 --> 2290.64]  across their entire life cycle within that domain of use. And fifth and
[2290.64 --> 2295.66]  finally governable DoD AI systems should be designed and engineered to
[2295.66 --> 2299.68]  fulfill their intended function while possessing the ability to detect and
[2299.68 --> 2304.06]  avoid unintended harm or disruption and for human or automated disengagement or
[2304.06 --> 2308.40]  deactivation of deployed systems that demonstrate unintended escalatory or other
[2308.40 --> 2308.82]  behavior.
[2308.82 --> 2313.38]  Yeah, there's a lot of jargon there. I would be interested in hearing kind of how those play
[2313.38 --> 2319.36]  out to to real real sorts of scenarios or maybe the sorts of scenarios that were in people's mind
[2319.36 --> 2320.76]  when when they were thinking of those.
[2321.58 --> 2327.26]  Sure. I think the overarching two things that I would say about these principles are one that the
[2327.26 --> 2332.88]  Department of Defense's, you know, ethical principles related to the use of force are those
[2332.88 --> 2340.12]  enshrined in the law of war, right? Military necessity, proportionality, distinction, humanity and honor.
[2340.12 --> 2345.16]  That really gets to the ethical question of what is the ethical use of force.
[2345.74 --> 2353.60]  So the DIBS principles are answering a different question, which is, you know, assuming that you are
[2353.60 --> 2360.24]  abiding by the ethical principles that govern the use of force, how do you have confidence that your
[2360.24 --> 2369.66]  technology will be able to implement your desires, right? You know, today, it is ethical to operate
[2369.66 --> 2376.34]  a commercial airline. In 1903, it would not be ethical to operate a commercial airline for passengers,
[2376.56 --> 2380.98]  because aircraft technology, I'm thinking specifically of, you know, fixed wing propeller
[2380.98 --> 2386.62]  aircraft was not ready, it was not safe enough for you to responsibly offer that on the commercial
[2386.62 --> 2394.74]  market. So part of the sort of, you know, the ethics of the technology relate to matching its current use
[2394.74 --> 2401.28]  to the maturity of that technology, and your processes for understanding that technology and
[2401.28 --> 2408.58]  ensuring that it is both robust and safe. And so that that sort of gets to the DIBS approach to ethics
[2408.58 --> 2414.50]  and how it complements the ethical principles that are enshrined in the law of war. If you say that you're
[2414.50 --> 2422.60]  going to have AI systems that abide by the law of war, how do you know that? And how do you prove
[2422.60 --> 2428.76]  that? And how do you have, you know, the relevant processes to ensure that? That's sort of what the
[2428.76 --> 2436.40]  DIB AI principles are going after is, you know, not what is the right or wrong way to use force, that
[2436.40 --> 2442.14]  question is best answered by the principles enshrined in the law of war. But if you are trying to do the
[2442.14 --> 2447.72]  right thing, how do you have confidence that your technology is going to allow you to do the right
[2447.72 --> 2454.98]  thing? And so that's about having the kinds of testing, evaluation, verification and validation
[2454.98 --> 2460.36]  procedures, so that we can rigorously test our systems to show that they are going to perform as
[2460.36 --> 2467.00]  intended. That gets to the training of your operators, so that they know that this is an appropriate
[2467.00 --> 2471.08]  time to use this technology and this is an inappropriate time to use this technology.
[2471.50 --> 2478.86]  Keeping with the aircraft analogy before, if your aircraft is only rated to fly at 40,000 feet,
[2479.02 --> 2485.44]  do not fly it at 80,000 feet, right? And so that gets to sort of what is the appropriate domain or
[2485.44 --> 2491.60]  mission use case for a technology and only using technologies for applications for which they have
[2491.60 --> 2499.36]  been appropriately and rigorously tested. And I think this is really valuable. We see AI ethics and AI safety
[2499.36 --> 2506.10]  as intimately interconnected, and that's reflected in our approach. I think one of the other things that
[2506.10 --> 2513.96]  the DIB study very helpfully pointed out is that the Department of Defense is not starting from scratch
[2513.96 --> 2522.12]  when it comes to reliability of incredibly complicated technologies operating in circumstances
[2522.12 --> 2528.08]  with life and death consequences. The Department of Defense stuff that uses technology in applications
[2528.08 --> 2533.88]  that are incredibly complicated, incredibly difficult, and not only that, there's potentially
[2533.88 --> 2540.38]  an adversary out there who is trying to make you fail in addition to the sort of inherent difficulties
[2540.38 --> 2546.24]  of the technologies. That's a good point. And we have a lot of experience doing really extraordinary
[2546.24 --> 2553.12]  work in that regard. One example that I like to point out is a system called GCAS. This is something
[2553.12 --> 2558.84]  that exists in the fighter aircraft that the United States uses. And if you know anything about what it's
[2558.84 --> 2564.30]  like to be a fighter pilot, you know that they undergo some really intense acceleration periods.
[2564.80 --> 2570.36]  And those acceleration periods can cause the pilot to blackout or to redout. And part of the autopilot
[2570.38 --> 2576.78]  system, which is, you know, a software, a software system mixed in with hardware, developed here in the
[2576.78 --> 2583.32]  United States, can automatically detect if the pilot has blacked out, and then fly the plane level and
[2583.32 --> 2588.40]  straight so they don't crash into the ground, fly the plane level until the pilot regains consciousness,
[2588.40 --> 2593.48]  and then transfer control back to the human. I mean, so it's not as though the Department of Defense
[2593.48 --> 2600.00]  is starting from scratch here. A lot of the techniques and processes and policies that we have rolled out
[2600.00 --> 2607.02]  related to traditional software will serve us very well in an era of AI powered software. And I think
[2607.02 --> 2612.96]  with the dibs sort of long form report, this is a 70 page report goes into quite some depth. A lot of
[2612.96 --> 2618.94]  what it's helpful for is pointing out, you know, here's where your existing processes kind of already do
[2618.94 --> 2624.68]  what you need to be done. And here are some areas where AI really does change the game. And you need to go
[2624.68 --> 2628.32]  through the hard work of improving upon these policies and processes.
[2629.04 --> 2635.18]  Absolutely. It just is a comment to finish that up. I want to note that for the F-16, that system you
[2635.18 --> 2639.80]  described is actually a Lockheed Martin system. I end up talking about that with folks quite a lot.
[2639.80 --> 2644.70]  I really appreciate you kind of diving into that because that's a question that so many people
[2644.70 --> 2650.96]  have in terms of the ethical and talking about lethal force policy and how you guys think about it.
[2650.96 --> 2656.80]  explaining how it fits into the law of war is very helpful as a framework. I guess as we kind of
[2656.80 --> 2662.20]  close out the show, I was wanting to just kind of understand as the Jake is going forward over the
[2662.20 --> 2669.20]  next few years, and we are in this industry that is moving so fast with all of the research and the
[2669.20 --> 2676.22]  new algorithms and new techniques and the compute that's racing along. How does the Jake look at AI
[2676.22 --> 2683.68]  related technologies going forward? What kinds of things draw your attention and make you sit up and
[2683.68 --> 2688.82]  go, that's something that has use cases that we particularly care about? What does that look like
[2688.82 --> 2696.28]  as you're seeing new things come across your screen? Sure. I think the sort of first answer is it's much
[2696.28 --> 2702.44]  of what you would expect. There have been some really exciting developments in computer vision and
[2702.44 --> 2707.38]  natural language processing. You know, these are two areas in which the performance of machine learning
[2707.38 --> 2714.34]  systems today is just orders of magnitude better than where we were a decade ago. And I think we still have
[2714.34 --> 2721.78]  not actually finished, you know, harvesting those gains. There are many parts of the Department of Defense
[2721.78 --> 2729.30]  where a lot of people's time and energy is devoted to, you know, applications where machine learning
[2729.30 --> 2735.84]  technology is already ready to start helping them do their jobs. And so I think the sort of next couple of years
[2735.84 --> 2743.02]  will continue to be focused on adopting the technology that already exists, and is already pretty capable and
[2743.02 --> 2749.96]  powerful. I think over the longer term, there are some really exciting things coming down the pike. Of course,
[2750.00 --> 2755.78]  I think the first folks to get to play around with these technologies will be in, you know, DARPA and the
[2755.78 --> 2760.82]  service laboratories who, as I said, you know, their mandate is a bit more focused on advancing the state
[2760.82 --> 2766.62]  of the art in AI technology. But these are things like the increasing relevance of transfer learning.
[2766.96 --> 2772.72]  So ML systems, if they learn something in one domain, can that help them not start from scratch
[2772.72 --> 2780.48]  as they look at related problems in perhaps different data sets? So for example, I think all of your
[2780.48 --> 2786.56]  listeners are probably familiar with the AlphaGo example. So the AlphaGo system was a literally
[2786.56 --> 2793.04]  better than the world's best Go player. But that system not only, you know, could not play chess,
[2793.46 --> 2799.14]  it could not play Go on a different sized Go board. You know, so some Go boards are 16 by 16,
[2799.26 --> 2806.24]  some are 32 by 32, etc. And so, you know, it really had no ability to apply what it had learned about
[2806.24 --> 2813.36]  Go and make that a better player for playing chess. And so that transfer learning capability
[2813.36 --> 2819.14]  was not present when AlphaGo. There have been some really interesting research results that indicate
[2819.14 --> 2825.86]  that researchers are making more and more progress at tackling the transfer learning problem. And so that
[2825.86 --> 2832.16]  could be really useful to DoD. If we're thinking about analyzing satellite images from a desert environment,
[2832.16 --> 2838.88]  you know, might that actually make our algorithms perform better, if they are also looking at images,
[2839.28 --> 2846.06]  you know, in a seaborne environment, for example. And so that ability to sort of combine what the
[2846.06 --> 2851.06]  machine learning system learns from different domains is something that I think is just going to have a ton
[2851.06 --> 2851.98]  of benefit for us.
[2851.98 --> 2858.10]  All right. Well, Greg, this has been a truly fascinating conversation. Thank you so much for
[2858.10 --> 2865.00]  coming on to the Practical AI podcast and kind of taking us through how AI, you know, integrates into
[2865.00 --> 2869.80]  the world of the DoD and defense at large. Really appreciate it. Thank you for coming on.
[2870.26 --> 2872.48]  Well, thanks very much for the opportunity. It was great to talk with you.
[2874.42 --> 2878.58]  All right. Thank you for tuning into this episode of Practical AI. If you enjoyed the show,
[2878.58 --> 2883.56]  do us a favor, go on iTunes, give us a rating, go in your podcast app and favorite it. If you are on
[2883.56 --> 2887.12]  Twitter or a social network, share a link with a friend, whatever you got to do, share the show
[2887.12 --> 2891.66]  with a friend if you enjoyed it. And bandwidth for changelog is provided by Fastly. Learn more
[2891.66 --> 2896.08]  at fastly.com. And we catch our errors before our users do here at changelog because of Rollbar.
[2896.32 --> 2901.52]  Check them out at rollbar.com slash changelog. And we're hosted on Linode cloud servers.
[2901.86 --> 2904.92]  Head to linode.com slash changelog. Check them out. Support this show.
[2904.92 --> 2911.04]  This episode is hosted by Daniel Whitenack and Chris Benson. The music is by Breakmaster Cylinder.
[2911.48 --> 2916.24]  And you can find more shows just like this at changelog.com. When you go there, pop in your
[2916.24 --> 2920.72]  email address, get our weekly email, keeping you up to date with the news and podcasts for
[2920.72 --> 2925.36]  developers in your inbox every single week. Thanks for tuning in. We'll see you next week.
[2925.36 --> 2929.86]  Bye.
[2929.86 --> 2930.44]  Bye.
[2930.44 --> 2931.38]  Bye.
[2933.04 --> 2933.50]  Bye.
[2951.66 --> 2951.86]  Bye.
