[0.00 --> 10.78]  what's up welcome back this is the changelog thank you for tuning in my name is adam stakovic
[10.78 --> 15.00]  i'm the editor-in-chief here at changelog if you're new to the pod head to changelog.fm for
[15.00 --> 19.08]  all the ways to subscribe if you're a long-time listener thanks for coming back thank you for
[19.08 --> 23.48]  tuning in if you haven't yet got changelog plus plus that's our membership it's for diehard
[23.48 --> 27.70]  listeners they want to directly support us they want to drop the ads and they want to get a little
[27.70 --> 32.20]  closer to the metal with bonus content and more on today's show we're talking with bruce schneier
[32.20 --> 37.56]  bruce is a cryptographer computer security professional privacy specialist and writer of
[37.56 --> 43.60]  many books he calls himself a public interest technologist a term he coined himself and works
[43.60 --> 48.50]  at the intersection of security technology and people he's been writing about security issues
[48.50 --> 54.46]  on his blog since 2004 his monthly newsletter has been going since 1998 he's a fellow and lecturer
[54.46 --> 60.20]  at harvard's kennedy school a board member of the eff and the chief of security architecture at
[60.20 --> 65.46]  interrupt long story short bruce has credentials to back up his opinions and on today's show we dig
[65.46 --> 70.56]  into the state of cyber security security and best practices his thoughts on bitcoin and other
[70.56 --> 76.06]  cryptocurrencies tim burners lee's solid project and of course we ask bruce to share his advice for
[76.06 --> 81.32]  today's devs who are building the software systems of tomorrow a massive thank you to our friends
[81.32 --> 87.14]  and our partners at fastly for having our back our cdm back that is our pods our assets our
[87.14 --> 93.68]  everything is fast globally because fastly is fast globally check them out at fastly.com
[93.68 --> 107.94]  this episode is brought to you by our friends at influx data the makers of influx db in addition to
[107.94 --> 111.66]  their belief in building their business around permissively licensed open source and meeting
[111.66 --> 117.38]  developers where they are they believe easy things should be easy and that extends to how you add
[117.38 --> 121.88]  monitoring to your application i'm here with vojt check and john the lead maintainer of telegraph
[121.88 --> 126.00]  operator for influx data vojt check help me understand what you mean by making monitoring
[126.00 --> 133.46]  applications easy our goal at influx data is to make it easy to gather data and metrics around your
[133.46 --> 139.18]  application specifically for kubernetes workloads where the standard is prometheus we've created
[139.18 --> 144.16]  telegraph operator which is an open source project around telegraph which is another open source project
[144.16 --> 149.60]  that makes it easy to gather both prometheus metrics as well as other metrics such as redis
[149.60 --> 155.20]  postgresql mysql any other commonly used applications and send it wherever you want to so it could be
[155.20 --> 159.92]  obviously influx db cloud which we would be happy to handle for you but it could be sent to any other
[159.92 --> 165.76]  location like prometheus server kafka any other of the supported plugins that we have and telegraph
[165.76 --> 171.10]  itself provides around 300 different plugins so there's a lot of different inputs that we can handle
[171.10 --> 175.70]  so data that we could scrape out of the box different outputs meaning that you can send it to multiple
[175.70 --> 182.06]  different tools there's also processing plugins such as aggregating data on the edge so you don't send
[182.06 --> 187.70]  as much data there's a lot of possibilities that telegraph operator could be used to get your data where you
[187.70 --> 192.78]  are today so with prometheus metrics but you can also use it for different types of data you can
[192.78 --> 197.76]  also do more processing at the edge and you can send your data wherever you want to voj check i love it
[197.76 --> 204.44]  thank you so much easy things should be easy listeners influx data is the time series data platform where you can
[204.44 --> 210.62]  build iot analytics and cloud applications anything you want on top of open source they're built on open
[210.62 --> 216.24]  source they love us you should check them out check them out at influx data.com slash changelog again
[216.24 --> 218.82]  influx data.com slash changelog
[218.82 --> 221.82]  you
[240.62 --> 256.70]  so we're here with bruce schneier who's a cryptographer computer security professional if you haven't heard of bruce you need to he's been around a long time been keeping a lot of us up to date with what's going on in
[256.70 --> 270.60]  cyber security infosecurity etc bruce thanks for joining us thanks for having me happy to have you so first of all you call yourself a public interest technologist this is a term that many of us probably haven't heard what does that mean yeah and i want you all to have heard of it because it's a big
[270.62 --> 282.04]  i think this is an important term and way of thinking public interest tech is kind of an umbrella term for people who somehow marry tech and policy
[282.04 --> 290.26]  and traditionally these are very different worlds technologists deal in computers and numbers and algorithms and true false yes no
[290.26 --> 297.48]  and policy people deal in consensus and just different ways of thinking and problem solving
[297.48 --> 302.82]  and we know when it goes badly wrong if you watch like you know the tech hearings in congress or
[302.82 --> 309.90]  attempts to reform various tech laws and i try to occupy this space between tech and policy
[309.90 --> 315.80]  so i am teaching cyber security policy at the harvard university kennedy school
[315.80 --> 323.14]  i'm teaching cyber security to students who deliberately never took math in college
[323.14 --> 331.78]  right so you imagined a technologist working on a lawmaker staff at a federal agency
[331.78 --> 334.88]  i don't know in the military for an ngo
[334.88 --> 340.90]  trying to figure out the policy of tech the tech of policy
[340.90 --> 344.28]  you know all the ways that tech and policy have to work together
[344.28 --> 346.20]  and can't be across purposes
[346.20 --> 348.48]  i think this is important
[348.48 --> 350.78]  you know i mean i tell you i'm here at harvard
[350.78 --> 353.74]  so there's a field called public interest law
[353.74 --> 357.34]  20 percent of the harvard law school graduates
[357.34 --> 359.68]  go into public interest law
[359.68 --> 361.48]  they don't work for a big law firm
[361.48 --> 362.58]  they don't work for a corporation
[362.58 --> 365.26]  they work on immigration law
[365.26 --> 366.56]  and housing law
[366.56 --> 368.40]  and discrimination law
[368.40 --> 370.92]  and all of these things that actually pay very well
[370.92 --> 373.02]  but make the world better
[373.02 --> 373.68]  yeah
[373.68 --> 377.12]  number of computer scientists who do that kind of thing is like here's like zero
[377.12 --> 379.14]  right they all go work for the big tech
[379.14 --> 382.90]  but we need this career path
[382.90 --> 387.12]  of people who want to do good with a tech degree
[387.12 --> 389.98]  or go to law school after a tech degree
[389.98 --> 393.62]  or you know they have a law degree and learn how to program
[393.62 --> 398.68]  and so all of these kind of bridging ways of thinking i think are really important
[398.68 --> 403.92]  the fundamental problems of our society in this century are tech
[403.92 --> 406.68]  and if you don't understand tech
[406.68 --> 408.34]  how could you deal with
[408.34 --> 409.90]  i don't know future of employment
[409.90 --> 413.00]  let alone algorithm discrimination
[413.00 --> 414.08]  right yeah
[414.08 --> 417.50]  so that's what i'm really trying to
[417.50 --> 420.92]  to preach and model and push for
[420.92 --> 421.52]  yeah
[421.52 --> 423.02]  right and it's not just me
[423.02 --> 424.18]  uh ford foundation
[424.18 --> 426.28]  is trying to fund
[426.28 --> 429.38]  public interest tech programs
[429.38 --> 430.92]  at universities around the country
[430.92 --> 435.08]  and you know they invented public interest law in the mid 70s
[435.08 --> 436.22]  so it's kind of good for them
[436.22 --> 439.28]  and this notion that we need to train people
[439.28 --> 441.12]  to bridge that gap
[441.12 --> 443.34]  to have one foot in both camps
[443.34 --> 443.98]  yeah
[443.98 --> 446.12]  what do you think is a more viable path
[446.12 --> 447.84]  is it taking lawyer types
[447.84 --> 449.80]  and teaching them computer science and security
[449.80 --> 451.76]  or taking computer science types
[451.76 --> 452.58]  and teaching them law
[452.58 --> 454.08]  and getting them interested in foregoing
[454.08 --> 455.38]  what are lucrative salaries
[455.38 --> 455.90]  right
[455.90 --> 457.88]  very relaxed work environments
[457.88 --> 459.04]  in many of these big tech companies
[459.04 --> 460.78]  what's the way to get it done
[460.78 --> 461.64]  you need both
[461.64 --> 463.04]  you need all ways to get it done
[463.04 --> 463.66]  right
[463.66 --> 464.26]  you know so
[464.26 --> 465.88]  aclu
[465.88 --> 467.46]  right pays what
[467.46 --> 469.00]  one third to one tenth
[469.00 --> 470.00]  that you can
[470.00 --> 471.68]  money you can make as a lawyer
[471.68 --> 472.84]  at a you know
[472.84 --> 473.94]  a big corporate law firm
[473.94 --> 476.18]  and they put out an application for us
[476.18 --> 476.58]  tourney
[476.58 --> 478.06]  and they get a hundred resumes
[478.06 --> 479.36]  i mean so there are
[479.36 --> 480.72]  lots of people
[480.72 --> 483.48]  who are not just pursuing money
[483.48 --> 486.30]  if there's a viable career path
[486.30 --> 488.12]  you work for the aclu as an attorney
[488.12 --> 490.04]  you feel good about your life
[490.04 --> 490.62]  when you come home
[490.62 --> 491.28]  right
[491.28 --> 492.66]  you're not working for some
[492.66 --> 494.16]  horrible corporate interest
[494.16 --> 494.98]  you're not doing something
[494.98 --> 495.74]  you don't believe in
[495.74 --> 497.22]  and we
[497.22 --> 498.54]  i don't think the problem
[498.54 --> 499.46]  is going to be supply
[499.46 --> 501.96]  i think a problem is going to be
[501.96 --> 502.40]  path
[502.40 --> 503.14]  demand
[503.14 --> 504.08]  and path
[504.08 --> 504.98]  and i want both
[504.98 --> 505.70]  right i want
[505.70 --> 507.02]  there to be a path
[507.02 --> 508.02]  for an attorney
[508.02 --> 510.22]  or a policy student
[510.22 --> 512.36]  to learn enough tech
[512.36 --> 513.54]  to bridge the gap
[513.54 --> 514.74]  i want a path
[514.74 --> 515.18]  for a
[515.18 --> 516.56]  for a cs student
[516.56 --> 517.94]  to learn enough law
[517.94 --> 518.76]  or policy
[518.76 --> 520.10]  to bridge that gap
[520.10 --> 521.46]  i mean i'm teaching
[521.46 --> 522.38]  cyber security policy
[522.38 --> 524.34]  and i will get cs students
[524.34 --> 525.34]  and that's fantastic
[525.34 --> 528.30]  and i'll get business school students
[528.30 --> 530.20]  and i want
[530.20 --> 531.24]  that mix
[531.24 --> 532.74]  what was your path then
[532.74 --> 533.72]  so if path is important
[533.72 --> 534.78]  what was your path to
[534.78 --> 536.58]  you kind of mentioned the why
[536.58 --> 537.46]  this is important
[537.46 --> 537.78]  but
[537.78 --> 539.26]  how did you get there
[539.26 --> 539.88]  what was your path
[539.88 --> 541.34]  to make this a thing for you
[541.34 --> 542.40]  or even care so much
[542.40 --> 543.84]  you know my path
[543.84 --> 545.60]  was becoming more general
[545.60 --> 545.98]  and
[545.98 --> 547.74]  path stories are interesting
[547.74 --> 548.22]  right now
[548.22 --> 549.94]  but every one of us
[549.94 --> 551.62]  is an exception
[551.62 --> 553.56]  and it has an exceptional
[553.56 --> 554.80]  and unique path
[554.80 --> 555.08]  right
[555.08 --> 555.92]  so it's not something
[555.92 --> 556.76]  that's mimicable
[556.76 --> 558.48]  because here i am
[558.48 --> 559.78]  oh in what
[559.78 --> 561.60]  the early 90s
[561.60 --> 562.68]  doing tech
[562.68 --> 563.64]  i get
[563.64 --> 565.46]  fired from at&t
[565.46 --> 566.24]  get laid off
[566.24 --> 567.52]  and uh
[567.52 --> 568.70]  i write a book
[568.70 --> 569.68]  about cryptography
[569.68 --> 571.02]  which becomes a bestseller
[571.02 --> 571.74]  because no one knew
[571.74 --> 572.40]  about cryptography
[572.40 --> 573.50]  the internet's taking off
[573.50 --> 575.02]  and really suddenly
[575.02 --> 576.70]  i'm in the middle
[576.70 --> 577.36]  of this
[577.36 --> 578.78]  tech renaissance
[578.78 --> 581.24]  i'm good at explaining
[581.24 --> 582.00]  right
[582.00 --> 583.30]  i'm good at making
[583.30 --> 584.64]  tech accessible
[584.64 --> 586.54]  and i naturally
[586.54 --> 587.86]  get drawn into policy
[587.86 --> 589.52]  and as i start generalizing
[589.52 --> 590.20]  i write about
[590.20 --> 591.76]  the mathematics of security
[591.76 --> 593.40]  then i write about
[593.40 --> 594.16]  computer security
[594.16 --> 594.96]  network security
[594.96 --> 596.04]  security policy
[596.04 --> 597.56]  the economics
[597.56 --> 598.96]  the psychology of security
[598.96 --> 600.50]  and then my latest books
[600.50 --> 601.22]  are about the public
[601.22 --> 602.20]  policy of security
[602.20 --> 603.62]  so i'm coming at it
[603.62 --> 604.54]  from tech
[604.54 --> 606.58]  but i'm making it up
[606.58 --> 607.58]  as i go along
[607.58 --> 608.84]  right you know
[608.84 --> 610.24]  be a best-selling author
[610.24 --> 611.60]  is not like a viable
[611.60 --> 612.50]  career path
[612.50 --> 613.50]  can't all do that
[613.50 --> 615.02]  it is a fun thing to do
[615.02 --> 616.02]  and i recommend it
[616.02 --> 616.72]  but you know
[616.72 --> 617.90]  if that's the only way
[617.90 --> 618.94]  we're not getting anywhere
[618.94 --> 619.66]  mm-hmm
[619.66 --> 621.34]  so you mentioned your books
[621.34 --> 622.26]  and i do have to thank you
[622.26 --> 623.34]  so when i was back in college
[623.34 --> 624.18]  i was studying
[624.18 --> 625.16]  computer science
[625.16 --> 626.08]  and information security
[626.08 --> 627.76]  and i was knee-deep
[627.76 --> 628.90]  in you know
[628.90 --> 630.20]  diffie-hillman key exchanges
[630.20 --> 632.62]  and like the hashing out
[632.62 --> 633.64]  one-way hashing algorithms
[633.64 --> 635.66]  and really staring right
[635.66 --> 636.22]  at the trees
[636.22 --> 637.74]  and i was assigned to read
[637.74 --> 638.58]  secrets and lies
[638.58 --> 639.40]  which you wrote
[639.40 --> 640.34]  the second edition
[640.34 --> 641.00]  i think you wrote
[641.00 --> 641.70]  the original one
[641.70 --> 642.22]  pre-9-11
[642.22 --> 643.30]  this was the post-9-11
[643.30 --> 644.28]  update
[644.28 --> 646.02]  and in that book
[646.02 --> 647.32]  you really made it
[647.32 --> 648.34]  clear to me
[648.34 --> 650.12]  how tangible
[650.12 --> 651.00]  and applicable
[651.00 --> 652.68]  these technical
[652.68 --> 653.80]  you know nuances
[653.80 --> 654.40]  and details
[654.40 --> 655.28]  that i was studying
[655.28 --> 657.02]  actually affect
[657.02 --> 658.32]  the real world
[658.32 --> 659.36]  and it was very useful
[659.36 --> 660.76]  and uh
[660.76 --> 661.30]  so i appreciate
[661.30 --> 662.26]  you writing that one
[662.26 --> 662.84]  of course you've written
[662.84 --> 664.52]  many books since then
[664.52 --> 665.24]  it's interesting
[665.24 --> 666.44]  your story's got a few
[666.44 --> 667.34]  holes in it
[667.34 --> 668.54]  so secrets and lies
[668.54 --> 669.30]  in my second book
[669.30 --> 670.58]  came out in i think
[670.58 --> 671.60]  2000
[671.60 --> 672.38]  i can actually pull it
[672.38 --> 673.26]  off the shelf and check
[673.26 --> 674.88]  i never updated it
[674.88 --> 677.04]  in 2003
[677.04 --> 679.28]  i wrote a book
[679.28 --> 680.52]  called beyond fear
[680.52 --> 681.34]  and that's where i actually
[681.34 --> 682.38]  talk about the terrorist
[682.38 --> 683.08]  attacks on 9-11
[683.08 --> 684.32]  you're holding up
[684.32 --> 685.10]  the paperback
[685.10 --> 685.82]  which might have been
[685.82 --> 687.54]  issued post 9-11
[687.54 --> 688.24]  even though it was
[688.24 --> 688.82]  published
[688.82 --> 690.06]  so i have chapter one
[690.06 --> 690.76]  the introduction
[690.76 --> 692.22]  was copyright 2004
[692.22 --> 693.68]  oh so i so
[693.68 --> 694.50]  in the paperback
[694.50 --> 695.82]  i wrote a new intro
[695.82 --> 696.94]  yeah they make you do that
[696.94 --> 697.88]  okay so that's the one
[697.88 --> 698.48]  that i got
[698.48 --> 699.88]  right because people
[699.88 --> 700.96]  think it's a new book
[700.96 --> 701.58]  but you just wrote
[701.58 --> 702.70]  like four new pages
[702.70 --> 703.74]  so fooled you
[703.74 --> 704.88]  good play
[704.88 --> 705.50]  good play
[705.50 --> 705.78]  yeah
[705.78 --> 707.52]  what was interesting
[707.52 --> 708.32]  the reason why that
[708.32 --> 709.08]  i was uh
[709.08 --> 709.92]  kind of flabbergasted
[709.92 --> 710.44]  when you said that
[710.44 --> 711.56]  is because in the intro
[711.56 --> 712.58]  you do say in that one
[712.58 --> 714.20]  that when you are
[714.20 --> 715.12]  making this update
[715.12 --> 715.96]  one thing that surprised
[715.96 --> 716.82]  you is how little
[716.82 --> 717.68]  had changed
[717.68 --> 718.82]  in between the two
[718.82 --> 719.56]  from the 2000
[719.56 --> 720.92]  to the 2004
[720.92 --> 721.86]  interesting
[721.86 --> 722.80]  and that's interesting
[722.80 --> 723.70]  because now we're what
[723.70 --> 725.02]  like 20 years from there
[725.02 --> 725.84]  and it's kind of like
[725.84 --> 726.36]  i wonder
[726.36 --> 727.92]  would you still say that
[727.92 --> 729.02]  or has so much
[729.02 --> 730.08]  changed since then
[730.08 --> 730.98]  in the world of security
[730.98 --> 731.56]  specifically
[731.56 --> 732.46]  you know it's interesting
[732.46 --> 733.50]  i mean a lot has changed
[733.50 --> 734.46]  and not a lot has changed
[734.46 --> 735.42]  i mean people still read
[735.42 --> 736.12]  secrets and lies
[736.12 --> 737.70]  and get a lot out of it
[737.70 --> 738.44]  because a lot of it
[738.44 --> 739.50]  is still true
[739.50 --> 741.54]  what's the threat
[741.54 --> 742.46]  landscape is now
[742.46 --> 743.54]  weirdly different
[743.54 --> 744.30]  you know we're worrying
[744.30 --> 745.22]  about nation states
[745.22 --> 746.62]  in ways we weren't
[746.62 --> 747.58]  uh ransomware
[747.58 --> 749.08]  didn't exist back then
[749.08 --> 749.76]  right
[749.76 --> 750.74]  uh business email
[750.74 --> 751.46]  compromise
[751.46 --> 752.46]  wasn't anything
[752.46 --> 753.40]  i wrote about
[753.40 --> 754.26]  i mean a lot of the
[754.26 --> 756.74]  business of cyber crime
[756.74 --> 758.38]  and almost like
[758.38 --> 759.22]  the business of
[759.22 --> 760.36]  cyber espionage
[760.36 --> 761.52]  it's become
[761.52 --> 762.66]  institutionalized
[762.66 --> 763.34]  in a way
[763.34 --> 764.54]  that you know
[764.54 --> 765.64]  we didn't really
[765.64 --> 766.44]  think about
[766.44 --> 768.00]  20 years ago
[768.00 --> 768.64]  right
[768.64 --> 770.04]  but it's surprising
[770.04 --> 771.58]  how much is the same
[771.58 --> 772.68]  the stuff on passwords
[772.68 --> 773.90]  is the same
[773.90 --> 776.10]  the stuff on firewalls
[776.10 --> 777.10]  and ids's
[777.10 --> 778.10]  and network security
[778.10 --> 779.00]  is the same
[779.00 --> 779.58]  right
[779.58 --> 780.88]  so both the same
[780.88 --> 781.42]  and different
[781.42 --> 782.30]  which i think is interesting
[782.30 --> 783.42]  yeah it's almost like
[783.42 --> 784.92]  uh the foundations
[784.92 --> 785.54]  are still there
[785.54 --> 786.26]  only everything's
[786.26 --> 787.20]  kind of just escalated
[787.20 --> 788.12]  gotten more mature
[788.12 --> 789.34]  more like you said
[789.34 --> 789.74]  the bit
[789.74 --> 790.86]  it's been businessified
[790.86 --> 792.04]  i remember like
[792.04 --> 792.94]  the early worms
[792.94 --> 793.72]  and stuff like
[793.72 --> 794.70]  people would do them
[794.70 --> 795.34]  as jokes
[795.34 --> 796.10]  or on accident
[796.10 --> 797.08]  and like cause
[797.08 --> 798.06]  major harm
[798.06 --> 799.04]  and then at a certain
[799.04 --> 799.72]  point it seemed like
[799.72 --> 800.28]  people realized
[800.28 --> 801.38]  well if i have this
[801.38 --> 802.42]  uh virus
[802.42 --> 803.26]  or if i have this
[803.26 --> 803.74]  attack
[803.74 --> 804.66]  actually if i keep it
[804.66 --> 805.52]  secret and don't let
[805.52 --> 806.40]  anybody know about it
[806.40 --> 807.64]  i can actually do a lot
[807.64 --> 808.50]  better for myself
[808.50 --> 809.84]  and make a lot more money
[809.84 --> 810.72]  and now you've got
[810.72 --> 812.20]  the russians who do this
[812.20 --> 813.42]  for espionage purposes
[813.42 --> 814.80]  i mean solar winds
[814.80 --> 815.60]  was you know
[815.60 --> 817.42]  not a worm in the same way
[817.42 --> 817.92]  but you think about
[817.92 --> 818.66]  wanna cry
[818.66 --> 819.50]  not pet ya
[819.50 --> 821.12]  and a lot of these
[821.12 --> 822.60]  nation state
[822.60 --> 824.32]  attacks
[824.32 --> 825.58]  i don't know
[825.58 --> 826.66]  if we really thought
[826.66 --> 827.80]  really about
[827.80 --> 828.84]  the internet
[828.84 --> 829.92]  as a battlefield
[829.92 --> 831.72]  in the same way
[831.72 --> 833.14]  we were still
[833.14 --> 833.96]  believing
[833.96 --> 834.70]  john perry
[834.70 --> 835.40]  barlow's
[835.40 --> 835.94]  declaration of
[835.94 --> 836.18]  independence
[836.18 --> 837.00]  in cyberspace
[837.00 --> 838.56]  that nations
[838.56 --> 839.52]  couldn't touch us
[839.52 --> 839.88]  there
[839.88 --> 842.28]  what's the most
[842.28 --> 842.74]  sophisticated
[842.74 --> 843.46]  or
[843.46 --> 844.46]  impressive
[844.46 --> 846.48]  current hack
[846.48 --> 847.00]  or technique
[847.00 --> 848.24]  that you've seen
[848.24 --> 848.64]  you know
[848.64 --> 849.88]  in in modern era
[849.88 --> 850.64]  what's really impressed
[850.64 --> 851.06]  you is like
[851.06 --> 851.42]  sometimes
[851.42 --> 852.12]  these things
[852.12 --> 852.84]  are so clever
[852.84 --> 853.42]  and interesting
[853.42 --> 854.00]  the way that people
[854.00 --> 855.10]  actually go about them
[855.10 --> 856.06]  you know
[856.06 --> 856.56]  solar winds
[856.56 --> 857.16]  was pretty clever
[857.16 --> 858.12]  right
[858.12 --> 858.82]  subverting
[858.82 --> 859.46]  the update
[859.46 --> 860.06]  mechanism
[860.06 --> 861.46]  of a random
[861.46 --> 862.44]  piece of network
[862.44 --> 863.30]  management software
[863.30 --> 863.70]  you didn't even
[863.70 --> 864.48]  know you had
[864.48 --> 865.52]  in a way
[865.52 --> 866.24]  to subvert
[866.24 --> 867.58]  14,000 networks
[867.58 --> 868.14]  worldwide
[868.14 --> 868.78]  and then pick
[868.78 --> 869.18]  and choose
[869.18 --> 869.50]  who you want
[869.50 --> 870.40]  to actually attack
[870.40 --> 871.94]  and go in
[871.94 --> 872.80]  and you know
[872.80 --> 873.60]  lay whatever
[873.60 --> 874.84]  groundwork you need
[874.84 --> 875.56]  so they can't
[875.56 --> 876.26]  possibly ever
[876.26 --> 876.92]  kick you out
[876.92 --> 877.52]  unless they burn
[877.52 --> 877.86]  their network
[877.86 --> 878.36]  to the ground
[878.36 --> 879.24]  which nobody
[879.24 --> 879.98]  ever does
[879.98 --> 881.12]  that was pretty
[881.12 --> 881.64]  impressive
[881.64 --> 882.64]  now
[882.64 --> 884.12]  what's interesting
[884.12 --> 885.36]  I think
[885.36 --> 886.04]  is to think
[886.04 --> 887.08]  back at
[887.08 --> 888.26]  the NSA
[888.26 --> 889.72]  documents
[889.72 --> 891.18]  that we saw
[891.18 --> 892.00]  because of Snowden
[892.00 --> 893.22]  this is 2013
[893.22 --> 895.52]  so it's almost
[895.52 --> 896.38]  a decade old
[896.38 --> 896.72]  now
[896.72 --> 897.82]  and a lot of
[897.82 --> 898.48]  that was really
[898.48 --> 898.94]  impressive
[898.94 --> 899.34]  right
[899.34 --> 900.18]  they had
[900.18 --> 900.88]  exploits
[900.88 --> 901.38]  that would
[901.38 --> 902.06]  survive
[902.06 --> 904.24]  reinstalling
[904.24 --> 904.98]  the operating
[904.98 --> 905.36]  system
[905.36 --> 906.20]  like wiping
[906.20 --> 906.66]  the computer
[906.66 --> 908.12]  and rebuilding
[908.12 --> 908.72]  it from scratch
[908.72 --> 909.46]  and that was
[909.46 --> 910.12]  10 years ago
[910.12 --> 911.86]  yeah right
[911.86 --> 912.52]  hasn't advanced
[912.52 --> 912.90]  since then
[912.90 --> 913.18]  surely
[913.18 --> 914.06]  and like
[914.06 --> 914.56]  they haven't
[914.56 --> 915.30]  done nothing
[915.30 --> 915.94]  in the past
[915.94 --> 916.50]  10 years
[916.50 --> 918.00]  so I think
[918.00 --> 919.36]  the impressive
[919.36 --> 920.12]  exploits
[920.12 --> 920.60]  are the ones
[920.60 --> 921.40]  we don't see
[921.40 --> 922.50]  and you never
[922.50 --> 923.22]  use them
[923.22 --> 923.62]  when they can
[923.62 --> 924.30]  be exposed
[924.30 --> 924.82]  right
[924.82 --> 925.50]  if you are
[925.50 --> 926.30]  an intelligence
[926.30 --> 926.92]  organizations
[926.92 --> 927.40]  Russians
[927.40 --> 927.92]  Chinese
[927.92 --> 928.42]  Americans
[928.42 --> 928.78]  Brits
[928.78 --> 929.08]  whoever
[929.08 --> 930.14]  you never
[930.14 --> 930.92]  use
[930.92 --> 931.98]  a more
[931.98 --> 932.44]  sophisticated
[932.44 --> 933.12]  attack
[933.12 --> 933.40]  than you
[933.40 --> 933.86]  absolutely
[933.86 --> 934.72]  have to
[934.72 --> 935.40]  you hold
[935.40 --> 935.68]  on to the
[935.68 --> 936.12]  best stuff
[936.12 --> 936.52]  for later
[936.52 --> 936.96]  you hold
[936.96 --> 937.28]  on to the
[937.28 --> 937.64]  best stuff
[937.64 --> 937.98]  until you
[937.98 --> 938.42]  really need
[938.42 --> 938.54]  it
[938.54 --> 939.14]  you know
[939.14 --> 939.56]  if you
[939.56 --> 939.92]  got a
[939.92 --> 940.32]  10
[940.32 --> 941.22]  and a
[941.22 --> 941.44]  3
[941.44 --> 941.88]  will get
[941.88 --> 942.44]  you in
[942.44 --> 942.74]  you're
[942.74 --> 942.82]  going to
[942.82 --> 943.14]  use a
[943.14 --> 943.40]  3
[943.40 --> 943.90]  or maybe
[943.90 --> 944.22]  use a
[944.22 --> 944.38]  4
[944.38 --> 944.64]  to make
[944.64 --> 944.84]  sure
[944.84 --> 946.16]  you save
[946.16 --> 946.74]  the 10
[946.74 --> 947.54]  when you
[947.54 --> 948.36]  need a
[948.36 --> 948.66]  10
[948.66 --> 949.30]  you don't
[949.30 --> 949.72]  waste
[949.72 --> 950.02]  it
[950.02 --> 950.86]  so
[950.86 --> 951.54]  the
[951.54 --> 952.62]  sophistication
[952.62 --> 953.82]  you don't
[953.82 --> 954.78]  almost need
[954.78 --> 955.26]  really
[955.26 --> 956.82]  the fact
[956.82 --> 957.14]  that there
[957.14 --> 957.40]  are now
[957.40 --> 957.90]  business
[957.90 --> 958.30]  models
[958.30 --> 959.02]  for ransomware
[959.02 --> 959.84]  it's
[959.84 --> 960.56]  organizational
[960.56 --> 961.36]  sophistication
[961.36 --> 961.82]  as opposed
[961.82 --> 962.18]  to technical
[962.18 --> 962.86]  sophistication
[962.86 --> 963.94]  what's the
[963.94 --> 964.18]  actual
[964.18 --> 964.54]  business
[964.54 --> 964.76]  model
[964.76 --> 965.28]  ransomware
[965.28 --> 965.72]  these days
[965.72 --> 966.14]  like what
[966.14 --> 966.38]  is the
[966.38 --> 966.62]  business
[966.62 --> 966.94]  model
[966.94 --> 967.38]  the
[967.38 --> 967.62]  business
[967.62 --> 967.88]  model
[967.88 --> 968.80]  is to
[968.80 --> 969.08]  ransom
[969.08 --> 969.80]  and to
[969.80 --> 970.30]  get money
[970.30 --> 970.78]  okay
[970.78 --> 971.32]  that's easy
[971.32 --> 971.86]  but there
[971.86 --> 972.72]  are organizations
[972.72 --> 973.74]  that do this
[973.74 --> 974.42]  as ransomware
[974.42 --> 974.94]  as a service
[974.94 --> 975.60]  you can
[975.60 --> 976.84]  rent ransomware
[976.84 --> 977.38]  capability
[977.38 --> 978.52]  there are
[978.52 --> 980.00]  criminal organizations
[980.00 --> 980.70]  that specialize
[980.70 --> 982.66]  in getting in
[982.66 --> 983.18]  there are ones
[983.18 --> 984.00]  specializes in
[984.00 --> 984.62]  getting the money
[984.62 --> 985.06]  they want to
[985.06 --> 985.76]  specialize in
[985.76 --> 986.30]  turning the
[986.30 --> 986.74]  bitcoin
[986.74 --> 988.00]  into actual
[988.00 --> 988.74]  cash you can
[988.74 --> 989.20]  spend
[989.20 --> 990.18]  there's a whole
[990.18 --> 991.10]  supply chain
[991.10 --> 992.80]  international criminal
[992.80 --> 993.56]  supply chain
[993.56 --> 994.82]  that's incredibly
[994.82 --> 995.36]  sophisticated
[995.36 --> 997.28]  that all
[997.28 --> 998.16]  is in the
[998.16 --> 998.64]  service of
[998.64 --> 999.18]  ransomware
[999.18 --> 1000.62]  one thing
[1000.62 --> 1000.90]  I heard you
[1000.90 --> 1001.16]  say about
[1001.16 --> 1001.66]  ransomware
[1001.66 --> 1002.36]  which is
[1002.36 --> 1002.82]  interesting
[1002.82 --> 1003.20]  to me
[1003.20 --> 1003.46]  I would
[1003.46 --> 1004.04]  love for
[1004.04 --> 1004.32]  you to
[1004.32 --> 1004.88]  elaborate
[1004.88 --> 1005.38]  even more
[1005.38 --> 1005.78]  on it
[1005.78 --> 1007.56]  is that
[1007.56 --> 1008.46]  it takes
[1008.46 --> 1008.92]  advantage
[1008.92 --> 1009.76]  of the
[1009.76 --> 1010.26]  fact that
[1010.26 --> 1011.04]  most people's
[1011.04 --> 1011.78]  data actually
[1011.78 --> 1012.42]  isn't all that
[1012.42 --> 1013.36]  interesting to
[1013.36 --> 1013.84]  anybody
[1013.84 --> 1014.32]  except for
[1014.32 --> 1014.80]  themselves
[1014.80 --> 1015.98]  and this is
[1015.98 --> 1016.28]  I think
[1016.28 --> 1016.90]  the fundamental
[1016.90 --> 1017.38]  insight
[1017.38 --> 1017.68]  there are
[1017.68 --> 1018.52]  really two
[1018.52 --> 1019.10]  and that's
[1019.10 --> 1019.42]  the first
[1019.42 --> 1019.74]  one
[1019.74 --> 1021.20]  if I steal
[1021.20 --> 1021.54]  your data
[1021.54 --> 1021.88]  what do I
[1021.88 --> 1022.18]  do with it
[1022.18 --> 1022.84]  I can sell
[1022.84 --> 1023.02]  it
[1023.02 --> 1023.82]  the only
[1023.82 --> 1024.12]  freaking
[1024.12 --> 1024.54]  person who
[1024.54 --> 1024.84]  wants to
[1024.84 --> 1025.20]  buy it
[1025.20 --> 1026.02]  is you
[1026.02 --> 1027.38]  nobody else
[1027.38 --> 1028.08]  wants your
[1028.08 --> 1028.48]  photos
[1028.48 --> 1029.22]  nobody else
[1029.22 --> 1029.70]  wants your
[1029.70 --> 1030.04]  email
[1030.04 --> 1030.66]  you know
[1030.66 --> 1031.56]  if you are
[1031.56 --> 1032.48]  an important
[1032.48 --> 1033.04]  celebrity
[1033.04 --> 1033.94]  then yes
[1033.94 --> 1034.68]  I can sell
[1034.68 --> 1035.10]  your stuff
[1035.10 --> 1035.48]  to somebody
[1035.48 --> 1035.70]  else
[1035.70 --> 1036.12]  but for the
[1036.12 --> 1036.86]  average person
[1036.86 --> 1037.20]  the average
[1037.20 --> 1037.60]  company
[1037.60 --> 1038.60]  no one else
[1038.60 --> 1038.88]  cares
[1038.88 --> 1039.56]  right so
[1039.56 --> 1040.04]  that's
[1040.04 --> 1040.76]  insight one
[1040.76 --> 1041.84]  not to
[1041.84 --> 1042.30]  steal your
[1042.30 --> 1042.58]  data
[1042.58 --> 1043.12]  but to
[1043.12 --> 1043.82]  block you
[1043.82 --> 1044.34]  from having
[1044.34 --> 1044.56]  it
[1044.56 --> 1045.00]  and then
[1045.00 --> 1045.66]  sell you
[1045.66 --> 1046.30]  your access
[1046.30 --> 1046.78]  back
[1046.78 --> 1047.38]  I mean I
[1047.38 --> 1047.68]  think that
[1047.68 --> 1048.06]  is a
[1048.06 --> 1049.04]  enormous
[1049.04 --> 1050.28]  insight
[1050.28 --> 1051.06]  and whoever
[1051.06 --> 1051.54]  thought of
[1051.54 --> 1051.88]  that was
[1051.88 --> 1052.40]  being incredibly
[1052.40 --> 1052.76]  creative
[1052.76 --> 1053.96]  the second
[1053.96 --> 1054.92]  thing that
[1054.92 --> 1055.58]  makes ransomware
[1055.58 --> 1056.18]  possible
[1056.18 --> 1057.54]  is Bitcoin
[1057.54 --> 1059.30]  you cannot
[1059.30 --> 1060.96]  criminals
[1060.96 --> 1061.54]  can't use
[1061.54 --> 1061.86]  the banking
[1061.86 --> 1062.28]  system
[1062.28 --> 1064.04]  so right
[1064.04 --> 1064.42]  so two
[1064.42 --> 1064.86]  problems
[1064.86 --> 1065.30]  right you
[1065.30 --> 1066.28]  criminals
[1066.28 --> 1066.66]  are prohibited
[1066.66 --> 1066.94]  from using
[1066.94 --> 1067.20]  the real
[1067.20 --> 1067.46]  banking
[1067.46 --> 1067.84]  system
[1067.84 --> 1068.92]  and suitcases
[1068.92 --> 1069.22]  full of
[1069.22 --> 1069.56]  hundred dollar
[1069.56 --> 1070.16]  bills are
[1070.16 --> 1070.72]  really heavy
[1070.72 --> 1071.82]  the only
[1071.82 --> 1072.62]  way for me
[1072.62 --> 1073.08]  to pay a
[1073.08 --> 1073.38]  ransom
[1073.38 --> 1074.40]  is through
[1074.40 --> 1075.14]  a cryptocurrency
[1075.14 --> 1076.34]  and I'm
[1076.34 --> 1076.84]  not making
[1076.84 --> 1077.20]  this up
[1077.20 --> 1077.70]  you go to
[1077.70 --> 1078.16]  your bank
[1078.16 --> 1079.02]  and try
[1079.02 --> 1080.18]  to wire
[1080.18 --> 1080.92]  fifty thousand
[1080.92 --> 1081.48]  dollars to
[1081.48 --> 1081.82]  a Russian
[1081.82 --> 1082.20]  account
[1082.20 --> 1082.98]  I mean just
[1082.98 --> 1083.40]  try
[1083.40 --> 1084.60]  you can't
[1084.60 --> 1085.70]  not like
[1085.70 --> 1086.40]  it's hard
[1086.40 --> 1087.86]  it's impossible
[1087.86 --> 1088.34]  what if you
[1088.34 --> 1088.78]  say but they
[1088.78 --> 1089.18]  kidnapped my
[1089.18 --> 1089.60]  daughter I
[1089.60 --> 1090.00]  have to do
[1090.00 --> 1090.30]  this
[1090.30 --> 1091.32]  you can't
[1091.32 --> 1091.68]  do it
[1091.68 --> 1092.66]  you will
[1092.66 --> 1093.10]  not be
[1093.10 --> 1093.40]  able to
[1093.40 --> 1093.56]  do it
[1093.56 --> 1094.12]  the banking
[1094.12 --> 1094.74]  system
[1094.74 --> 1095.72]  will not
[1095.72 --> 1096.36]  let you
[1096.36 --> 1097.26]  wire money
[1097.26 --> 1098.16]  that way
[1098.16 --> 1099.78]  right
[1099.78 --> 1100.40]  you know
[1100.40 --> 1100.72]  it's not
[1100.72 --> 1100.96]  going to
[1100.96 --> 1101.30]  reputable
[1101.30 --> 1101.70]  business
[1101.70 --> 1102.52]  it can't
[1102.52 --> 1102.88]  move
[1102.88 --> 1103.66]  there are
[1103.66 --> 1103.88]  a lot
[1103.88 --> 1104.24]  of banking
[1104.24 --> 1104.72]  regs to
[1104.72 --> 1105.02]  stop you
[1105.02 --> 1105.28]  from doing
[1105.28 --> 1105.54]  that
[1105.54 --> 1106.46]  so
[1106.46 --> 1107.32]  bitcoin
[1107.32 --> 1108.18]  makes
[1108.18 --> 1108.74]  ransomware
[1108.74 --> 1109.16]  work
[1109.16 --> 1109.78]  how do
[1109.78 --> 1110.04]  you feel
[1110.04 --> 1110.48]  about that
[1110.48 --> 1110.76]  does that
[1110.76 --> 1111.80]  make you
[1111.80 --> 1112.46]  negative
[1112.46 --> 1113.02]  bitcoin
[1113.02 --> 1113.50]  how does
[1113.50 --> 1113.86]  that make
[1113.86 --> 1114.14]  you feel
[1114.14 --> 1114.32]  about
[1114.32 --> 1114.66]  bitcoin
[1114.66 --> 1115.22]  it does
[1115.22 --> 1115.62]  not make
[1115.62 --> 1115.72]  me
[1115.72 --> 1116.00]  negative
[1116.00 --> 1116.52]  bitcoin
[1116.52 --> 1117.18]  bitcoin
[1117.18 --> 1117.40]  is
[1117.40 --> 1117.82]  completely
[1117.82 --> 1118.28]  stupid
[1118.28 --> 1118.72]  and useless
[1118.72 --> 1119.14]  for all
[1119.14 --> 1119.44]  sorts of
[1119.44 --> 1119.74]  other
[1119.74 --> 1120.16]  reasons
[1120.16 --> 1120.92]  this is
[1120.92 --> 1121.24]  just an
[1121.24 --> 1121.82]  ancillary
[1121.82 --> 1122.26]  bad
[1122.26 --> 1122.58]  thing
[1122.58 --> 1123.26]  no I
[1123.26 --> 1123.52]  mean if
[1123.52 --> 1124.22]  ransomware
[1124.22 --> 1124.60]  didn't
[1124.60 --> 1124.94]  exist
[1124.94 --> 1125.24]  bitcoin
[1125.24 --> 1125.44]  would
[1125.44 --> 1125.92]  still be
[1125.92 --> 1126.46]  stupid
[1126.46 --> 1126.94]  and useless
[1126.94 --> 1127.66]  and idiotic
[1127.66 --> 1128.24]  and we
[1128.24 --> 1128.54]  hope it
[1128.54 --> 1128.82]  dies
[1128.82 --> 1129.04]  in a
[1129.04 --> 1129.26]  fire
[1129.26 --> 1129.58]  as soon
[1129.58 --> 1129.72]  as
[1129.72 --> 1130.08]  possible
[1130.08 --> 1130.90]  who's
[1130.90 --> 1131.16]  we
[1131.16 --> 1131.94]  everybody
[1131.94 --> 1132.40]  who does
[1132.40 --> 1132.78]  security
[1132.78 --> 1133.24]  basically
[1133.24 --> 1133.98]  okay
[1133.98 --> 1135.04]  why is
[1135.04 --> 1135.36]  that
[1135.36 --> 1135.90]  why do
[1135.90 --> 1136.08]  they have
[1136.08 --> 1136.50]  that feeling
[1136.50 --> 1137.02]  because it
[1137.02 --> 1137.44]  doesn't
[1137.44 --> 1138.32]  solve any
[1138.32 --> 1139.30]  actual problems
[1139.30 --> 1140.20]  anybody has
[1140.20 --> 1141.74]  it isn't
[1141.74 --> 1142.34]  decentralized
[1142.34 --> 1143.22]  it isn't
[1143.22 --> 1143.76]  secure
[1143.76 --> 1144.40]  it isn't
[1144.40 --> 1144.88]  anything
[1144.88 --> 1146.08]  it causes
[1146.08 --> 1146.60]  all sorts
[1146.60 --> 1147.02]  of other
[1147.02 --> 1147.54]  problems
[1147.54 --> 1148.50]  and has
[1148.50 --> 1149.14]  absolutely
[1149.14 --> 1150.18]  no value
[1150.18 --> 1151.42]  at all
[1151.42 --> 1152.82]  plus speculative
[1152.82 --> 1153.44]  bubble people
[1153.44 --> 1153.74]  are losing
[1153.74 --> 1154.06]  lots of
[1154.06 --> 1154.66]  money
[1154.66 --> 1157.44]  gotcha
[1157.44 --> 1157.94]  so what
[1157.94 --> 1158.36]  about
[1158.36 --> 1159.34]  censorship
[1159.34 --> 1159.88]  resistant
[1159.88 --> 1160.88]  money exchange
[1160.88 --> 1161.16]  like the
[1161.16 --> 1161.70]  concept of
[1161.70 --> 1162.12]  bitcoin
[1162.12 --> 1162.44]  with the
[1162.44 --> 1162.96]  peer-to-peer
[1162.96 --> 1163.58]  exchange
[1163.58 --> 1164.04]  of money
[1164.04 --> 1164.42]  do you
[1164.42 --> 1164.84]  think there's
[1164.84 --> 1165.34]  value in
[1165.34 --> 1166.16]  that concept
[1166.16 --> 1166.88]  of not
[1166.88 --> 1167.42]  having an
[1167.42 --> 1167.96]  intermediary
[1167.96 --> 1168.38]  between the
[1168.38 --> 1168.88]  two of us
[1168.88 --> 1170.08]  no intermediaries
[1170.08 --> 1170.60]  serve value
[1170.60 --> 1171.20]  okay
[1171.20 --> 1172.28]  right I mean
[1172.28 --> 1173.00]  there's no
[1173.00 --> 1174.06]  value in a
[1174.06 --> 1174.82]  system where
[1174.82 --> 1175.36]  if you're
[1175.36 --> 1175.84]  exchanging money
[1175.84 --> 1176.32]  with somebody
[1176.32 --> 1177.14]  and they're a
[1177.14 --> 1177.98]  millisecond slower
[1177.98 --> 1178.34]  than you
[1178.34 --> 1179.48]  you lose all
[1179.48 --> 1179.86]  your money
[1179.86 --> 1180.98]  and there's no
[1180.98 --> 1181.54]  recourse
[1181.54 --> 1182.30]  that is not
[1182.30 --> 1182.72]  valuable
[1182.72 --> 1183.34]  sure
[1183.34 --> 1184.28]  there's no
[1184.28 --> 1185.40]  value in a
[1185.40 --> 1185.86]  system where
[1185.86 --> 1186.24]  if you forget
[1186.24 --> 1186.76]  your password
[1186.76 --> 1187.36]  you lose your
[1187.36 --> 1187.90]  life savings
[1187.90 --> 1189.22]  that's just
[1189.22 --> 1189.56]  dumb
[1189.56 --> 1191.12]  intermediaries
[1191.12 --> 1192.54]  have value
[1192.54 --> 1193.10]  that's why
[1193.10 --> 1193.70]  they exist
[1193.70 --> 1193.96]  and not
[1193.96 --> 1194.58]  just there
[1194.58 --> 1196.02]  because they
[1196.02 --> 1196.68]  hate us
[1196.68 --> 1197.82]  you want to
[1197.82 --> 1198.52]  exchange money
[1198.52 --> 1199.10]  use Venmo
[1199.10 --> 1199.92]  works great
[1199.92 --> 1200.86]  why don't you
[1200.86 --> 1201.36]  like it
[1201.36 --> 1202.46]  I like Venmo
[1202.46 --> 1202.70]  yeah
[1202.70 --> 1204.00]  I use Venmo
[1204.00 --> 1204.60]  right
[1204.60 --> 1205.20]  you know we
[1205.20 --> 1205.88]  all like it
[1205.88 --> 1206.52]  and you know
[1206.52 --> 1207.48]  and most people
[1207.48 --> 1208.26]  who actually think
[1208.26 --> 1208.84]  they have bitcoin
[1208.84 --> 1209.48]  don't actually
[1209.48 --> 1210.00]  have bitcoin
[1210.00 --> 1210.88]  right the
[1210.88 --> 1211.26]  blockchain
[1211.26 --> 1212.52]  does seven
[1212.52 --> 1213.24]  transactions per
[1213.24 --> 1213.54]  second
[1213.54 --> 1214.74]  most people on
[1214.74 --> 1215.28]  Coinbase
[1215.28 --> 1215.76]  they don't
[1215.76 --> 1216.40]  actually own
[1216.40 --> 1216.98]  their bitcoin
[1216.98 --> 1218.04]  Coinbase has a
[1218.04 --> 1218.84]  database just like
[1218.84 --> 1219.26]  Venmo
[1219.26 --> 1220.94]  that allocates
[1220.94 --> 1221.36]  ownership
[1221.36 --> 1222.52]  the whole
[1222.52 --> 1223.64]  blockchain is
[1223.64 --> 1224.66]  largely a myth
[1224.66 --> 1225.52]  for most users
[1225.52 --> 1227.62]  so one aspect
[1227.62 --> 1229.18]  of the idea
[1229.18 --> 1230.22]  of using cash
[1230.22 --> 1230.70]  I'm talking about
[1230.70 --> 1231.86]  actual physical
[1231.86 --> 1232.38]  cash
[1232.38 --> 1234.14]  is privacy
[1234.14 --> 1234.72]  concerns
[1234.72 --> 1236.00]  right so you
[1236.00 --> 1237.00]  you talk a lot
[1237.00 --> 1237.86]  about government
[1237.86 --> 1238.54]  espionage
[1238.54 --> 1239.68]  spying etc
[1239.68 --> 1240.90]  and of course
[1240.90 --> 1242.10]  digital currencies
[1242.10 --> 1243.18]  are easy to spy on
[1243.18 --> 1243.92]  what your citizens
[1243.92 --> 1244.88]  are doing etc
[1244.88 --> 1245.70]  now bitcoin
[1245.70 --> 1246.48]  public ledger
[1246.48 --> 1247.16]  of course that's
[1247.16 --> 1248.18]  easy to spy on
[1248.18 --> 1249.18]  and track as well
[1249.18 --> 1251.04]  right easy to spy on
[1251.04 --> 1251.70]  so the notion of
[1251.70 --> 1252.42]  that it's private
[1252.42 --> 1253.16]  isn't true
[1253.16 --> 1253.96]  I mean bitcoin's
[1253.96 --> 1254.66]  built on a whole
[1254.66 --> 1255.38]  lot of lies
[1255.38 --> 1256.20]  right well I was
[1256.20 --> 1256.64]  wondering what you
[1256.64 --> 1257.84]  think of if you
[1257.84 --> 1258.32]  look at other
[1258.32 --> 1259.16]  privacy coins
[1259.16 --> 1259.88]  people doing things
[1259.88 --> 1260.56]  like with monero
[1260.56 --> 1261.42]  and zcash
[1261.42 --> 1261.80]  if you think
[1261.80 --> 1262.32]  there's any value
[1262.32 --> 1262.74]  in those
[1262.74 --> 1263.92]  not really
[1263.92 --> 1265.36]  I mean yes
[1265.36 --> 1266.10]  it facilitates
[1266.10 --> 1266.70]  ransomware
[1266.70 --> 1267.88]  facilitates a whole
[1267.88 --> 1268.72]  lot of crime
[1268.72 --> 1270.28]  I know your
[1270.28 --> 1271.26]  customer rules
[1271.26 --> 1272.40]  anti-money laundering
[1272.40 --> 1273.02]  anti-terrorist
[1273.02 --> 1273.50]  financing
[1273.50 --> 1274.06]  I think these
[1274.06 --> 1274.42]  are things that
[1274.42 --> 1275.12]  are valuable for
[1275.12 --> 1275.58]  society
[1275.58 --> 1277.00]  I wouldn't toss
[1277.00 --> 1277.36]  them out the
[1277.36 --> 1277.68]  window
[1277.68 --> 1279.12]  you talk to
[1279.12 --> 1279.56]  people who
[1279.56 --> 1280.02]  deal in
[1280.02 --> 1280.68]  child exploitation
[1280.68 --> 1282.56]  and you know
[1282.56 --> 1283.08]  the fact that
[1283.08 --> 1283.56]  you can move
[1283.56 --> 1284.02]  that money
[1284.02 --> 1284.58]  around without
[1284.58 --> 1284.96]  a government
[1284.96 --> 1285.62]  stopping you
[1285.62 --> 1287.12]  it's not good
[1287.12 --> 1288.08]  it harms people
[1288.08 --> 1289.90]  it's like
[1289.90 --> 1291.10]  this might be a
[1291.10 --> 1291.64]  little left field
[1291.64 --> 1292.40]  but tinder
[1292.40 --> 1293.46]  swindler on
[1293.46 --> 1293.76]  Netflix
[1293.76 --> 1294.42]  have you seen
[1294.42 --> 1294.68]  that
[1294.68 --> 1295.28]  I don't even
[1295.28 --> 1295.76]  know what this
[1295.76 --> 1296.50]  is it doesn't
[1296.50 --> 1297.10]  sound good
[1297.10 --> 1298.04]  well yeah
[1298.04 --> 1298.94]  long I'll give
[1298.94 --> 1299.60]  you the TLDR
[1299.60 --> 1301.36]  somebody who
[1301.36 --> 1302.82]  was just able
[1302.82 --> 1303.74]  to con people
[1303.74 --> 1304.82]  with large amounts
[1304.82 --> 1305.32]  of money
[1305.32 --> 1306.88]  various bank accounts
[1306.88 --> 1307.34]  he would call
[1307.34 --> 1307.90]  one person
[1307.90 --> 1308.14]  to call
[1308.14 --> 1308.82]  another person
[1308.82 --> 1310.12]  credit cards
[1310.12 --> 1311.08]  bank accounts
[1311.08 --> 1311.64]  that match
[1311.64 --> 1311.96]  his name
[1311.96 --> 1312.40]  so when it
[1312.40 --> 1312.68]  comes to
[1312.68 --> 1313.26]  your customer
[1313.26 --> 1314.42]  and attaching
[1314.42 --> 1315.24]  a bank account
[1315.24 --> 1316.62]  to a cash app
[1316.62 --> 1317.44]  account or to
[1317.44 --> 1318.24]  a Venmo account
[1318.24 --> 1318.68]  that doesn't
[1318.68 --> 1319.40]  match your name
[1319.40 --> 1321.24]  that's anti-money
[1321.24 --> 1321.62]  laundering
[1321.62 --> 1322.18]  right that's what
[1322.18 --> 1322.90]  you're speaking of
[1322.90 --> 1323.72]  and so I
[1323.72 --> 1324.34]  mention that
[1324.34 --> 1324.84]  because this
[1324.84 --> 1326.24]  person never
[1326.24 --> 1326.94]  really used a
[1326.94 --> 1327.58]  bank account or
[1327.58 --> 1327.96]  a credit card
[1327.96 --> 1328.24]  that was in
[1328.24 --> 1328.58]  his name
[1328.58 --> 1328.92]  it was always
[1328.92 --> 1329.96]  somebody else's
[1329.96 --> 1330.74]  you know what I
[1330.74 --> 1331.58]  mean so that's
[1331.58 --> 1332.32]  so when it comes
[1332.32 --> 1333.34]  to these intermediaries
[1333.34 --> 1334.68]  I don't know how
[1334.68 --> 1335.02]  he's able to
[1335.02 --> 1335.94]  bypass this stuff
[1335.94 --> 1337.02]  but that's what
[1337.02 --> 1337.46]  they do
[1337.46 --> 1337.96]  they say okay
[1337.96 --> 1338.68]  your account
[1338.68 --> 1339.52]  is in this name
[1339.52 --> 1340.40]  Adam Stukowiak
[1340.40 --> 1341.32]  does your bank
[1341.32 --> 1341.84]  account that you're
[1341.84 --> 1343.08]  attaching money
[1343.08 --> 1343.68]  coming in or
[1343.68 --> 1344.42]  money going out
[1344.42 --> 1346.00]  match that same
[1346.00 --> 1346.96]  name if not
[1346.96 --> 1347.38]  we're going to
[1347.38 --> 1348.90]  flag it for
[1348.90 --> 1349.88]  anti-money laundering
[1349.88 --> 1350.28]  and you have to
[1350.28 --> 1351.38]  prove you own it
[1351.38 --> 1353.64]  by way of W-2
[1353.64 --> 1354.64]  or some sort of
[1354.64 --> 1355.36]  tax form or
[1355.36 --> 1356.06]  something that
[1356.06 --> 1356.70]  W-2 wouldn't
[1356.70 --> 1357.18]  fit there but
[1357.18 --> 1358.12]  some sort of tax
[1358.12 --> 1358.46]  form that you
[1358.46 --> 1359.08]  filled out that
[1359.08 --> 1359.88]  says this you
[1359.88 --> 1360.68]  know account is
[1360.68 --> 1361.50]  yours or whatever
[1361.50 --> 1363.08]  something right
[1363.08 --> 1364.34]  so that's where
[1364.34 --> 1364.84]  that comes into
[1364.84 --> 1365.26]  play this
[1365.26 --> 1366.90]  intermediary benefit
[1366.90 --> 1368.32]  yeah I mean I
[1368.32 --> 1368.74]  think there's real
[1368.74 --> 1370.10]  value in
[1370.10 --> 1371.64]  governance I
[1371.64 --> 1372.02]  mean you know
[1372.02 --> 1373.66]  like we need
[1373.66 --> 1374.32]  governance and you
[1374.32 --> 1375.16]  saw this in a lot
[1375.16 --> 1375.96]  of the hacks right
[1375.96 --> 1376.78]  the notion that
[1376.78 --> 1378.08]  blockchain money is
[1378.08 --> 1379.44]  secure they are
[1379.44 --> 1380.04]  hacked all the
[1380.04 --> 1380.84]  math is never
[1380.84 --> 1381.80]  hacked the
[1381.80 --> 1382.52]  exchanges are
[1382.52 --> 1383.04]  hacked the
[1383.04 --> 1383.68]  wallets are
[1383.68 --> 1384.50]  hacked right
[1384.50 --> 1385.28]  everything else
[1385.28 --> 1386.58]  is hacked all
[1386.58 --> 1387.18]  the time and
[1387.18 --> 1387.56]  there's nothing
[1387.56 --> 1388.02]  you can do
[1388.02 --> 1388.54]  about it or
[1388.54 --> 1389.02]  it's a complete
[1389.02 --> 1390.18]  con or it's
[1390.18 --> 1391.06]  a complete con
[1391.06 --> 1392.24]  in a lot of
[1392.24 --> 1393.06]  ways all
[1393.06 --> 1393.64]  of this
[1393.64 --> 1395.18]  blockchain based
[1395.18 --> 1395.90]  finance is
[1395.90 --> 1396.44]  speed running
[1396.44 --> 1397.20]  500 years of
[1397.20 --> 1397.80]  financial fraud
[1397.80 --> 1399.40]  you got wildcat
[1399.40 --> 1400.36]  banks you've got
[1400.36 --> 1401.44]  Ponzi schemes
[1401.44 --> 1402.28]  you've got
[1402.28 --> 1403.42]  unregulated
[1403.42 --> 1405.06]  securities you
[1405.06 --> 1405.84]  got pump and
[1405.84 --> 1406.80]  dump I mean
[1406.80 --> 1408.30]  it's all there
[1408.30 --> 1409.14]  front and running
[1409.14 --> 1410.64]  and it's all
[1410.64 --> 1411.72]  illegal in the
[1411.72 --> 1412.34]  normal banking
[1412.34 --> 1413.26]  world because
[1413.26 --> 1414.86]  it's bad and
[1414.86 --> 1415.70]  should be illegal
[1415.70 --> 1417.32]  but because
[1417.32 --> 1418.88]  nobody's regulating
[1418.88 --> 1420.00]  these blockchain
[1420.00 --> 1421.10]  based systems yet
[1421.10 --> 1422.36]  a lot of
[1422.36 --> 1422.74]  people are
[1422.74 --> 1423.30]  losing money
[1423.30 --> 1423.56]  I mean
[1423.56 --> 1424.24]  another fun
[1424.24 --> 1424.94]  experiment go
[1424.94 --> 1425.42]  on a twitter
[1425.42 --> 1427.22]  and type I'm
[1427.22 --> 1427.70]  having trouble
[1427.70 --> 1428.42]  with my bitcoin
[1428.42 --> 1429.06]  wallet can anybody
[1429.06 --> 1430.14]  help me no
[1430.14 --> 1430.98]  thanks you will
[1430.98 --> 1431.84]  get a lot of
[1431.84 --> 1433.46]  responses who
[1433.46 --> 1434.34]  will help you
[1434.34 --> 1434.90]  and if you
[1434.90 --> 1435.56]  follow their
[1435.56 --> 1436.84]  advice you will
[1436.84 --> 1437.98]  unwittingly give
[1437.98 --> 1438.66]  them control of
[1438.66 --> 1439.04]  your account
[1439.04 --> 1440.46]  wow that is the
[1440.46 --> 1441.10]  way that fraud
[1441.10 --> 1442.60]  works yeah and
[1442.60 --> 1444.20]  it's bitcoin there
[1444.20 --> 1445.54]  is nothing you can
[1445.54 --> 1446.48]  do about it
[1446.48 --> 1447.72]  period done
[1447.72 --> 1449.04]  this is not
[1449.04 --> 1449.58]  great
[1449.58 --> 1463.62]  this episode is
[1463.62 --> 1464.34]  brought to you by
[1464.34 --> 1465.34]  century build
[1465.34 --> 1466.04]  better software
[1466.04 --> 1467.78]  faster diagnose
[1467.78 --> 1469.14]  fix and optimize
[1469.14 --> 1470.30]  the performance of
[1470.30 --> 1471.42]  your code more
[1471.42 --> 1472.28]  than a million
[1472.28 --> 1473.76]  developers in 68
[1473.76 --> 1475.58]  thousand organizations
[1475.58 --> 1476.92]  already use century
[1476.92 --> 1477.58]  and that includes
[1477.58 --> 1478.62]  us here's the
[1478.62 --> 1479.12]  easiest way to
[1479.12 --> 1479.86]  try century
[1479.86 --> 1481.38]  head to century.io
[1481.38 --> 1482.30]  slash demo
[1482.30 --> 1483.10]  slash sandbox
[1483.10 --> 1484.88]  that is a fully
[1484.88 --> 1485.92]  functional version of
[1485.92 --> 1486.86]  century that you
[1486.86 --> 1487.92]  can poke at and
[1487.92 --> 1488.62]  best of all our
[1488.62 --> 1489.12]  listeners get the
[1489.12 --> 1489.80]  team plan for free
[1489.80 --> 1490.58]  for three months
[1490.58 --> 1491.58]  head to century.io
[1491.58 --> 1492.54]  and use the code
[1492.54 --> 1493.34]  changelog when you
[1493.34 --> 1494.36]  sign up again
[1494.36 --> 1496.38]  century.io and use
[1496.38 --> 1497.30]  the code changelog
[1497.30 --> 1520.80]  so fraud leads us
[1520.80 --> 1521.28]  to one of the
[1521.28 --> 1522.36]  problems we have in
[1522.36 --> 1523.50]  computer security which
[1523.50 --> 1524.40]  is social engineering
[1524.40 --> 1525.20]  right fraud is just
[1525.20 --> 1525.92]  sophisticated social
[1525.92 --> 1526.56]  engineering you're
[1526.56 --> 1527.32]  tricking somebody
[1527.32 --> 1528.06]  into doing something
[1528.06 --> 1529.12]  that benefits you
[1529.12 --> 1530.06]  and doesn't benefit
[1530.06 --> 1531.70]  them it seems like
[1531.70 --> 1532.36]  those kind of things
[1532.36 --> 1533.26]  like education is
[1533.26 --> 1533.70]  really the only
[1533.70 --> 1534.48]  solution to that
[1534.48 --> 1535.46]  particular problem is
[1535.46 --> 1536.12]  that is that what
[1536.12 --> 1537.18]  you think you know
[1537.18 --> 1539.54]  not really education
[1539.54 --> 1541.36]  is a lot to me
[1541.36 --> 1543.10]  victim blaming right
[1543.10 --> 1544.02]  if you were smarter
[1544.02 --> 1544.66]  you wouldn't have
[1544.66 --> 1546.36]  fallen for that I
[1546.36 --> 1547.98]  think that's a
[1547.98 --> 1549.16]  convenient crutch to
[1549.16 --> 1550.90]  hide bad design okay
[1550.90 --> 1552.32]  right so think about
[1552.32 --> 1553.20]  some of the security
[1553.20 --> 1554.24]  advice that we're
[1554.24 --> 1555.58]  given don't click on
[1555.58 --> 1557.48]  a random URL it's a
[1557.48 --> 1558.34]  URL what am I
[1558.34 --> 1558.88]  supposed to do with
[1558.88 --> 1560.24]  it right don't stick
[1560.24 --> 1561.50]  a USB stick into your
[1561.50 --> 1562.72]  computer it's a wait
[1562.72 --> 1563.52]  wait what kind of
[1563.52 --> 1564.22]  dumb advice is that
[1564.22 --> 1565.16]  what am I doing it's a
[1565.16 --> 1567.24]  USB stick the real
[1567.24 --> 1569.54]  problem to me is how
[1569.54 --> 1571.34]  can we design systems
[1571.34 --> 1572.62]  so that clicking on a
[1572.62 --> 1574.24]  URL isn't dangerous
[1574.24 --> 1576.12]  that's a design problem
[1576.12 --> 1578.50]  anytime I think you see
[1578.50 --> 1580.52]  a the user did
[1580.52 --> 1581.22]  something wrong and
[1581.22 --> 1583.02]  bad thing happened or
[1583.02 --> 1585.26]  educate the user go a
[1585.26 --> 1586.02]  little deeper and look
[1586.02 --> 1586.90]  at the design what is
[1586.90 --> 1588.86]  the design that forces
[1588.86 --> 1590.44]  us to throw this on
[1590.44 --> 1591.80]  the user I mean we
[1591.80 --> 1593.16]  don't talk about oh I
[1593.16 --> 1593.78]  don't know you know
[1593.78 --> 1595.98]  various uh salmonella and
[1595.98 --> 1596.74]  chickens or something
[1596.74 --> 1598.06]  and say well the user
[1598.06 --> 1599.58]  has to check no we have
[1599.58 --> 1601.32]  health codes right right
[1601.32 --> 1602.10]  you know you got sick
[1602.10 --> 1602.96]  at a restaurant you
[1602.96 --> 1603.60]  should have gone in the
[1603.60 --> 1604.36]  kitchen and done an
[1604.36 --> 1605.30]  inspection why didn't
[1605.30 --> 1606.92]  you hey we don't do
[1606.92 --> 1607.66]  that I'm doing that
[1607.66 --> 1610.72]  next time yeah I mean I
[1610.72 --> 1612.32]  I think we need to
[1612.32 --> 1615.14]  design systems so that
[1615.14 --> 1617.12]  naive and uneducated
[1617.12 --> 1618.76]  users can be safe
[1618.76 --> 1620.74]  right right I'm flying
[1620.74 --> 1621.68]  tomorrow first time in a
[1621.68 --> 1622.44]  while kind of exciting
[1622.44 --> 1623.46]  I'm going to get on the
[1623.46 --> 1625.40]  airplane and I'm not
[1625.40 --> 1627.20]  going to inspect the
[1627.20 --> 1627.90]  engine I'm not going to
[1627.90 --> 1628.78]  look at the flight logs
[1628.78 --> 1629.66]  not going to check the
[1629.66 --> 1631.64]  pilot's training record or
[1631.64 --> 1632.72]  did he have a mandatory
[1632.72 --> 1633.74]  rest period I'm not going
[1633.74 --> 1635.10]  to do any of that I'm
[1635.10 --> 1635.68]  going to get on the
[1635.68 --> 1637.62]  plane and not even think
[1637.62 --> 1638.56]  about it I don't even
[1638.56 --> 1639.76]  have to know what the
[1639.76 --> 1641.26]  safety looks like it's
[1641.26 --> 1643.42]  magically done for me by
[1643.42 --> 1644.96]  a government we need
[1644.96 --> 1645.74]  computers to be more
[1645.74 --> 1647.68]  like that it can't be
[1647.68 --> 1648.60]  that you need to be an
[1648.60 --> 1650.10]  intelligent user to
[1650.10 --> 1651.10]  safely use the internet
[1651.10 --> 1652.54]  that's not going to fly
[1652.54 --> 1654.04]  so to speak so you then
[1654.04 --> 1654.90]  the next question
[1654.90 --> 1656.06]  logically is well how
[1656.06 --> 1657.02]  do we get there and it
[1657.02 --> 1657.86]  sounds like the answer
[1657.86 --> 1660.76]  is policy I it and to
[1660.76 --> 1661.30]  be kind of like a
[1661.30 --> 1662.54]  policy I mean because the
[1662.54 --> 1663.52]  companies want to blame
[1663.52 --> 1664.62]  the user you know the
[1664.62 --> 1666.30]  companies love that we
[1666.30 --> 1667.76]  blame the user for
[1667.76 --> 1669.20]  security issues because
[1669.20 --> 1669.72]  they don't have to fix
[1669.72 --> 1672.02]  anything you know so I
[1672.02 --> 1672.64]  think it's all their
[1672.64 --> 1674.12]  answers in regulation and
[1674.12 --> 1676.76]  liability the markets
[1676.76 --> 1677.88]  don't reward safety and
[1677.88 --> 1678.66]  security pretty much ever
[1678.66 --> 1680.28]  and if you want to get
[1680.28 --> 1681.44]  that right if you want
[1681.44 --> 1683.44]  restaurants that you know
[1683.44 --> 1685.50]  won't poison you or drugs
[1685.50 --> 1687.14]  that are safe or cars that
[1687.14 --> 1688.86]  won't blow up on impact
[1688.86 --> 1691.12]  that is always government
[1691.12 --> 1692.80]  intervention that's that's
[1692.80 --> 1693.86]  the way we do it pajamas
[1693.86 --> 1695.14]  don't catch on fire you
[1695.14 --> 1695.88]  know whatever it is we we
[1695.88 --> 1696.80]  whatever it is we inside
[1696.80 --> 1698.44]  blankets yeah gosh well
[1698.44 --> 1699.64]  what's crazy is how data
[1699.64 --> 1700.36]  breaches are becoming
[1700.36 --> 1701.76]  normalized and they are
[1701.76 --> 1703.82]  normal and right right
[1703.82 --> 1704.94]  but and and the question
[1704.94 --> 1706.58]  is whose fault is it right
[1706.58 --> 1707.60]  so we talk about the
[1707.60 --> 1708.62]  Harvard Law School they
[1708.62 --> 1710.72]  deal a lot in partial
[1710.72 --> 1712.46]  liability and there's a car
[1712.46 --> 1715.10]  crash it's this driver it's
[1715.10 --> 1716.38]  that driver it's this car
[1716.38 --> 1717.38]  it's that car it's the road
[1717.38 --> 1719.80]  conditions it's you know the
[1719.80 --> 1721.46]  the signs and the way that
[1721.46 --> 1723.42]  the road is designed the
[1723.42 --> 1725.76]  weather and they figure
[1725.76 --> 1727.48]  out who's at fault and by
[1727.48 --> 1729.28]  how much we don't do that
[1729.28 --> 1730.60]  in the computer world we
[1730.60 --> 1731.78]  don't really have that
[1731.78 --> 1734.32]  notion of liability but you
[1734.32 --> 1735.26]  know some of it's going to
[1735.26 --> 1736.76]  be the fault of the vendor
[1736.76 --> 1739.06]  you know solar winds you know
[1739.06 --> 1740.96]  why you know did they have a
[1740.96 --> 1742.88]  faulty product that allowed
[1742.88 --> 1744.80]  the Russians to break into
[1744.80 --> 1747.42]  their update system and send a
[1747.42 --> 1750.44]  hacked backdoored update to
[1750.44 --> 1752.62]  14,000 customers you'd think
[1752.62 --> 1753.64]  they'd have some liability
[1753.64 --> 1755.14]  here I mean it wasn't my
[1755.14 --> 1758.44]  fault yeah I just had this
[1758.44 --> 1760.24]  conversation actually for an
[1760.24 --> 1761.38]  upcoming episode of another
[1761.38 --> 1762.04]  show we have called
[1762.04 --> 1763.44]  founders talk you have more
[1763.44 --> 1764.92]  than one episode one on
[1764.92 --> 1766.46]  show is that allowed yeah we
[1766.46 --> 1768.96]  have six different shows and
[1768.96 --> 1770.20]  maybe more in the future yeah
[1770.20 --> 1771.50]  there's no regulations so we
[1771.50 --> 1772.46]  just do what we want and we
[1772.46 --> 1773.56]  do what we want keeps you
[1773.56 --> 1775.62]  busy I guess yeah the
[1776.22 --> 1777.58]  conversation was really
[1777.58 --> 1779.62]  around incident management but
[1779.62 --> 1780.60]  the opposite of that which is
[1780.60 --> 1784.08]  reliability and this idea that
[1784.08 --> 1785.84]  as part of incident management
[1785.84 --> 1788.04]  and this pursuit of reliable
[1788.04 --> 1790.24]  software part of a good design
[1790.24 --> 1792.08]  in hierarchy of an organization
[1792.08 --> 1793.66]  is this idea of service
[1793.66 --> 1795.50]  ownership so when you speak to
[1795.50 --> 1796.78]  like solar winds and who's at
[1796.78 --> 1799.46]  fault some organizational things
[1799.46 --> 1801.04]  can happen to sort of showcase
[1801.04 --> 1802.90]  service ownership so if you have
[1802.90 --> 1804.10]  unreliable software you get
[1804.10 --> 1806.06]  called for pager duty that's one
[1806.06 --> 1807.44]  way to say who's not so much at
[1807.44 --> 1809.18]  fault but who sort of owns it
[1809.18 --> 1811.24]  could that kind of stuff begin
[1811.24 --> 1812.62]  like maturing engineering
[1812.62 --> 1813.62]  departments essentially could
[1813.62 --> 1815.36]  that begin to help more
[1815.36 --> 1817.18]  information more evidence to
[1817.18 --> 1819.32]  showcase who's at fault and to
[1819.32 --> 1820.78]  how much when it comes to these
[1820.78 --> 1822.32]  kind of hacks I think it makes
[1822.32 --> 1824.50]  some sense we're gonna need to
[1824.50 --> 1826.50]  figure out the way to really
[1826.50 --> 1829.30]  think about liability as a
[1829.30 --> 1832.28]  improvement tool is to look at
[1832.28 --> 1834.36]  who can fix the problem you want
[1834.36 --> 1838.08]  in general in society whoever has
[1838.08 --> 1839.32]  the ability to fix the problem
[1839.32 --> 1840.70]  to be in charge of the problem
[1840.70 --> 1842.84]  so you know credit cards is
[1842.84 --> 1844.38]  probably a decent example in the
[1844.38 --> 1846.82]  old days in this early 70s you
[1846.82 --> 1848.06]  were liable for credit card
[1848.06 --> 1850.28]  fraud on your card right someone
[1850.28 --> 1851.58]  stole your card charge a bunch of
[1851.58 --> 1853.88]  stuff you were liable now you
[1853.88 --> 1855.28]  couldn't fix the problem
[1855.28 --> 1857.16]  Congress passes the fair credit
[1857.16 --> 1859.54]  reporting act 1978 and now the
[1859.54 --> 1860.56]  maximum liability for the
[1860.56 --> 1862.90]  customer is $50 so now the credit
[1862.90 --> 1865.14]  car companies are suddenly losing
[1865.14 --> 1867.24]  money due to fraud so they do all
[1867.24 --> 1868.90]  sorts of things right they fix the
[1868.90 --> 1870.12]  problem right they fix it right
[1870.12 --> 1871.36]  they have they start doing a
[1871.36 --> 1872.62]  real-time verification of card
[1872.62 --> 1875.06]  number with these terminals they
[1875.06 --> 1878.56]  start doing better anti counterfeit
[1878.56 --> 1880.72]  protection holograms and micro
[1880.72 --> 1882.82]  printing on the cards they have the
[1882.82 --> 1885.54]  card and the pin they mail you the
[1885.54 --> 1888.58]  card and the activation separately you
[1888.58 --> 1890.26]  know all of these things they and the
[1890.26 --> 1892.28]  biggest thing is they have these giant
[1892.28 --> 1894.24]  expert systems in the back end
[1894.24 --> 1896.34]  looking at your spending patterns for
[1896.34 --> 1899.14]  patterns of fraud none of that the
[1899.14 --> 1901.78]  customer was able to do so pushing the
[1901.78 --> 1904.62]  liability onto the companies was for
[1904.62 --> 1907.72]  society better because society could fix
[1907.72 --> 1910.66]  it so if you think about solar winds
[1910.66 --> 1913.82]  if I'm a solar winds customer I get an
[1913.82 --> 1915.68]  update I install it you want me to do
[1915.68 --> 1917.22]  that right we want people to install
[1917.22 --> 1919.92]  updates if we want the update to be safe
[1919.92 --> 1923.04]  that has to be solar winds problem and
[1923.04 --> 1926.34]  no one else can fix that so from a
[1926.34 --> 1929.26]  societal perspective I want them liable
[1929.26 --> 1932.76]  for defects in the update because only
[1932.76 --> 1936.42]  they can improve the process the
[1936.42 --> 1939.02]  customer can't and then it becomes a
[1939.02 --> 1940.44]  thing you can leverage in terms of
[1940.44 --> 1942.70]  competitions like well who's better at
[1942.70 --> 1944.12]  keeping their software safe who's better
[1944.12 --> 1945.38]  keeping their software more reliable
[1945.38 --> 1947.44]  well this company so I give them my
[1947.44 --> 1948.76]  business it becomes a competitive
[1948.76 --> 1951.16]  advantage yeah somewhat that tends not
[1951.16 --> 1953.50]  to work right it tends not to be market
[1953.50 --> 1956.30]  driver nothing about no airline
[1956.30 --> 1959.38]  advertises themselves as we have fewer
[1959.38 --> 1961.30]  crashes than the other guy sure nobody
[1961.30 --> 1962.10]  they don't want you to think about
[1962.10 --> 1963.40]  crashing they're like don't mention the
[1963.40 --> 1965.32]  word crash don't say bomb right cars
[1965.32 --> 1967.46]  don't the exception was sob like in the
[1967.46 --> 1969.74]  80s they would advertise we're a safer
[1969.74 --> 1972.28]  car but pretty much nobody does yeah
[1972.28 --> 1975.28]  right restaurants supermarkets like they
[1975.28 --> 1978.98]  do not compete on these no salmonella
[1978.98 --> 1981.60]  here right right no salmonella here big
[1981.60 --> 1983.92]  sign no salmonella here you never see
[1983.92 --> 1985.94]  that and you're right they don't want
[1985.94 --> 1987.62]  you to think about salmonella when you're
[1987.62 --> 1990.34]  buying your chickens truth right so you so
[1990.34 --> 1993.38]  this isn't something the market can solve
[1993.38 --> 1998.00]  it is rare that you see market solutions
[1998.00 --> 2001.28]  for safety and security because they tend
[2001.28 --> 2004.70]  not to be things that are salient when
[2004.70 --> 2006.80]  someone makes a purchasing decision it's
[2006.80 --> 2009.10]  price and features yeah and convenience
[2009.10 --> 2010.70]  so we've seen it over and over again we'll
[2010.70 --> 2012.36]  trade convenience convenience is a feature
[2012.36 --> 2014.06]  yeah yeah it is but we'll trade our
[2014.06 --> 2016.04]  security our privacy for convenience I mean
[2016.04 --> 2017.78]  I all time we do it all time you know and
[2017.78 --> 2019.96]  it makes perfect sense yeah on the margins
[2019.96 --> 2023.40]  for sure so has any of these big breaches
[2023.40 --> 2027.56]  or cases been litigated in a sense that has
[2027.56 --> 2029.78]  brought the liability back to the vendors
[2029.78 --> 2033.18]  or is it just not the case not liability I
[2033.18 --> 2035.20]  mean there has been litigation I'm not up
[2035.20 --> 2037.20]  on the current state of litigation but
[2037.20 --> 2039.22]  there they are there class action lawsuits
[2039.22 --> 2042.20]  there there are some regulatory fines they
[2042.20 --> 2044.52]  tend to be rounding errors yeah right the
[2044.52 --> 2047.10]  exception is going to be Europe and GDPR and
[2047.10 --> 2050.70]  privacy violations Europe is the regulatory
[2050.70 --> 2053.92]  superpower on the planet they do issue fines
[2053.92 --> 2056.24]  that companies notice and don't say oh
[2056.24 --> 2057.40]  yeah you're that that was cheaper than the
[2057.40 --> 2060.26]  attorney fees we'll take it which the US
[2060.26 --> 2064.92]  tends to do but not enough yeah one of the
[2064.92 --> 2068.24]  problems with litigation as a driver of
[2068.24 --> 2071.46]  social change is that almost all cases
[2071.46 --> 2075.66]  never get to court where a judge decides
[2075.66 --> 2078.10]  I get settled they're almost always settled
[2078.10 --> 2081.90]  in private with nobody admitting any
[2081.90 --> 2082.58]  wrongdoing
[2082.58 --> 2086.86]  even if you know even ones that like the
[2086.86 --> 2087.34]  FTC
[2087.34 --> 2090.42]  brings to bear in companies so they tend
[2090.42 --> 2093.26]  not to be good models for others going
[2093.26 --> 2094.90]  forward I'm not sure how to fix that but
[2094.90 --> 2096.30]  that seems to be a problem we're having
[2096.30 --> 2099.08]  what's your take on GDPR are you happy
[2099.08 --> 2101.22]  with it do you think it's worked out the
[2101.22 --> 2102.96]  way that they wanted it to it seems like
[2102.96 --> 2103.40]  to me
[2103.40 --> 2105.22]  in a practical sense there's a whole bunch
[2105.22 --> 2107.44]  of cookie banners now that weren't and it's
[2107.44 --> 2109.12]  like was that the intended yeah I mean
[2109.12 --> 2112.38]  right I mean in a sense GDPR was
[2112.38 --> 2115.84]  medication to to stop the pain rather
[2115.84 --> 2120.00]  than medication to fix the illness it was
[2120.00 --> 2122.66]  a good start it probably did what the
[2122.66 --> 2125.32]  people who wrote it thought it would but
[2125.32 --> 2126.76]  there are too many loopholes too many ways
[2126.76 --> 2128.30]  to get around it too many things it doesn't
[2128.30 --> 2128.52]  do
[2128.52 --> 2133.28]  so you know we can't stop there but it is
[2133.28 --> 2135.42]  doing some it is not completely useless
[2135.42 --> 2137.98]  this only puts more pressure on your
[2137.98 --> 2141.12]  point which is policy this idea of tech
[2141.12 --> 2142.92]  and policy right like we need more people
[2142.92 --> 2145.80]  to have an understanding of technology to
[2145.80 --> 2148.94]  be involved in policy making so that the
[2148.94 --> 2150.60]  this is an iteration like you said it's a
[2150.60 --> 2152.40]  beginning you know I think if we're in
[2152.40 --> 2153.76]  software we have to believe in iteration
[2153.76 --> 2155.86]  right so we have to believe in I would
[2155.86 --> 2157.40]  imagine iteration at the policy level as
[2157.40 --> 2157.66]  well
[2157.66 --> 2160.16]  so while GDPR may be a start it's got to
[2160.16 --> 2162.46]  be something that begins in evolution
[2162.46 --> 2164.94]  and that begins with more and more
[2164.94 --> 2166.88]  people as you had said this vacuum that's
[2166.88 --> 2169.08]  there and demand for people involved in
[2169.08 --> 2169.76]  tech and policy
[2169.76 --> 2172.42]  I think that's right and these are not
[2172.42 --> 2173.92]  easy problems we're talking about
[2173.92 --> 2174.30]  yeah
[2174.30 --> 2177.68]  now the public policy of tech I mean look
[2177.68 --> 2179.98]  at the current battles on section 230
[2179.98 --> 2183.58]  and free speech on Twitter and sort of all
[2183.58 --> 2186.12]  of these these are not tech problems
[2186.12 --> 2189.56]  these are policy problems these are human
[2189.56 --> 2192.56]  value problems these are what kind of
[2192.56 --> 2194.60]  society you want to live in problems
[2194.60 --> 2197.70]  they're informed by tech you have to
[2197.70 --> 2200.14]  understand tech to think about the
[2200.14 --> 2202.14]  problems but you're not going to solve
[2202.14 --> 2205.76]  them with tech tech going to be a part of
[2205.76 --> 2208.10]  the solution so so yes very much so
[2208.10 --> 2211.06]  mm-hmm one thing that has come up to me
[2211.06 --> 2213.86]  though with policy and and I think even
[2213.86 --> 2215.76]  not so much to go back to Bitcoin but
[2215.76 --> 2217.68]  more so this idea that I think people
[2217.68 --> 2219.50]  believe in or want to believe in this
[2219.50 --> 2221.80]  idea of a decentralized currency and
[2221.80 --> 2224.14]  crypto and Bitcoin is this lack of
[2224.14 --> 2225.70]  trust in government I don't know I mean
[2225.70 --> 2227.14]  I think if you don't trust government
[2227.14 --> 2229.54]  you've got way bigger problems well
[2229.54 --> 2230.74]  isn't that what they do they're trying
[2230.74 --> 2232.36]  to hedge their bets against fiat currency
[2232.36 --> 2234.18]  that's controlled by government yeah you
[2234.18 --> 2236.60]  know no it's it's just a just a bunch
[2236.60 --> 2239.02]  of libertarian crypto bros it's not
[2239.02 --> 2243.46]  actually a legit sensical philosophy sure
[2243.46 --> 2245.30]  you know I don't buy it for a second
[2245.30 --> 2246.48]  well there's some out there that
[2246.48 --> 2248.06]  believe that even if it's not the
[2248.06 --> 2249.92]  majority right I mean a lot of people
[2249.92 --> 2251.96]  believe it doesn't mean it makes sense
[2251.96 --> 2253.30]  the point I'm trying to make to or to
[2253.30 --> 2255.24]  get to is less that but more so this
[2255.24 --> 2257.34]  idea that if we want to believe in
[2257.34 --> 2259.44]  policy change and policy updates which
[2259.44 --> 2262.54]  we do want I think we have to begin to
[2262.54 --> 2264.60]  trust our government more or the people
[2264.60 --> 2266.24]  that trust it less they need to have
[2266.24 --> 2268.24]  that that faith in it and you mentioned
[2268.24 --> 2271.14]  Snowden and spying on folks like that
[2271.14 --> 2272.56]  kind of stuff doesn't make you trust
[2272.56 --> 2273.88]  your government more it makes you trust
[2273.88 --> 2275.64]  them less so what are your thoughts on
[2275.64 --> 2278.18]  like government trust yeah it doesn't
[2278.18 --> 2280.02]  and you know also the the far-right
[2280.02 --> 2282.66]  paranoia on government can't do good
[2282.66 --> 2285.14]  there's a lot of anti-government fear
[2285.14 --> 2286.74]  being stoked by people who have ulterior
[2286.74 --> 2288.64]  motives you know I mean the people who
[2288.64 --> 2290.06]  want you to mistrust government are the
[2290.06 --> 2290.96]  people who want to poison your water
[2290.96 --> 2292.76]  supply and don't want anybody to stop
[2292.76 --> 2295.66]  them from doing it so you know I mean
[2295.66 --> 2298.46]  yes I did a book on trust you have no
[2298.46 --> 2300.84]  choice but to trust your government and
[2300.84 --> 2302.48]  government actually does a lot of good
[2302.48 --> 2305.18]  in our world so but yeah I think you
[2305.18 --> 2306.92]  are right that mistrusted government is
[2306.92 --> 2310.62]  a problem here and a bigger problem than
[2310.62 --> 2312.66]  this and you know it is one that we do
[2312.66 --> 2315.04]  have to solve yeah figure out how to get
[2315.04 --> 2317.96]  back to the notion of you know good
[2317.96 --> 2320.60]  government doing good things right well
[2320.60 --> 2322.18]  it doesn't help when as technologists we
[2322.18 --> 2324.66]  see these congress people questioning
[2324.66 --> 2326.24]  talking about technologies and they're
[2326.24 --> 2328.64]  completely you know out of their depth
[2328.64 --> 2329.68]  they have no idea what they're talking
[2329.68 --> 2331.28]  about it's hard to trust that person
[2331.28 --> 2333.84]  yeah all right remember who asked Mark
[2333.84 --> 2336.30]  Zuckerberg right how does Facebook make
[2336.30 --> 2339.32]  money a legit question asked at a Senate
[2339.32 --> 2341.76]  hearing like you people are trying to
[2341.76 --> 2344.24]  govern this and you have no idea that
[2344.78 --> 2347.14]  Facebook makes money by selling ads
[2347.14 --> 2349.78]  right we sell ads which is why I think
[2349.78 --> 2352.28]  skepticism of government regulation in that
[2352.28 --> 2354.62]  circumstance is I think well-founded having
[2354.62 --> 2356.72]  said that you're trying to change that
[2356.72 --> 2358.28]  but no government regulation is worse
[2358.28 --> 2361.28]  that's the problem sure I guess my point
[2361.28 --> 2362.44]  I'm trying to drive at is you're trying
[2362.44 --> 2364.48]  to change that by having a more well
[2364.48 --> 2367.68]  informed policy making body right like
[2367.68 --> 2370.78]  you're trying to instruct I'm sure you do
[2370.78 --> 2374.68]  you advise policymakers as a expert you
[2374.68 --> 2376.90]  know I have it is not something I know
[2376.90 --> 2378.68]  people who do that sort of full-time who
[2378.68 --> 2381.14]  work on congressional staffs and committee
[2381.14 --> 2383.78]  staffs and they do really good work I mean I
[2383.78 --> 2386.36]  do some of it but I that is not the one
[2386.36 --> 2388.88]  thing I do but you know I'm trying to teach
[2388.88 --> 2392.06]  here a generation yeah of people going into
[2392.06 --> 2394.98]  public policy teach them how to you know
[2394.98 --> 2397.92]  listen to technologists figure out what
[2397.92 --> 2401.44]  they're saying I'm really trying here yeah
[2401.44 --> 2404.24]  yeah so you're talking to an audience of
[2404.24 --> 2406.12]  software developers and technologists you
[2406.12 --> 2408.22]  know what would you teach us or instruct us
[2408.22 --> 2410.66]  what can we do you know in our little part of
[2410.66 --> 2412.52]  the world whether we're an independent
[2412.52 --> 2414.68]  contributor on a large code base or maybe
[2414.68 --> 2416.66]  we're starting a new business in a software
[2416.66 --> 2418.82]  as a service you know we're building these
[2418.82 --> 2420.76]  things of the future what are the kind of
[2420.76 --> 2423.22]  things that we can be doing now to push
[2423.22 --> 2424.58]  things in the right direction versus the
[2424.58 --> 2427.42]  wrong you know I want us to think about the
[2427.42 --> 2429.88]  policy implications of what we do so this is
[2429.88 --> 2432.54]  actually interesting a few years ago Google
[2432.54 --> 2436.76]  invented a new job title and it was I think
[2436.76 --> 2440.80]  it's called project council and so here's the
[2440.80 --> 2443.78]  idea that in the old way of doing things is
[2443.78 --> 2446.40]  the engineers would build the thing and at the
[2446.40 --> 2448.22]  end they'd show it to the attorneys and say
[2448.22 --> 2451.68]  will we go to jail if we do this is this good is
[2451.68 --> 2454.24]  this bad and the attorneys would give an opinion
[2454.24 --> 2458.40]  and Google realized it's way better to embed the
[2458.40 --> 2460.98]  attorneys into the design team from the beginning
[2460.98 --> 2465.14]  where the changes are cheaper right where we
[2465.14 --> 2466.66]  heard you can say you know if you did it this
[2466.66 --> 2470.02]  way and not that way it's better and that's what
[2470.02 --> 2473.96]  Google does it's a great idea I think we need staff
[2473.96 --> 2477.60]  policy people right I want a policy person on the
[2477.60 --> 2482.12]  design teams of these systems from the beginning to
[2482.12 --> 2485.24]  do the same thing to say you know if you did it
[2485.24 --> 2489.40]  this way your thing won't be racist isn't that
[2489.40 --> 2493.70]  better yeah instead of like at the end when it's
[2493.70 --> 2497.02]  too late and suddenly your system is racist and
[2497.02 --> 2502.38]  everyone hates you so you know I want us as
[2502.38 --> 2509.50]  developers as techies to be more open for non-tech
[2509.50 --> 2513.12]  input into our designs and development from the
[2513.12 --> 2517.44]  beginning I think that is incredibly valuable and
[2517.44 --> 2520.90]  if we can take into account human flourishing the
[2520.90 --> 2526.14]  environment lots of policy things I think that
[2526.14 --> 2529.60]  that that would be better what's the path then to
[2529.60 --> 2532.60]  get so if this is something you think could be on
[2532.60 --> 2536.86]  the up-and-coming SAS for example or the up-and-coming
[2536.86 --> 2542.46]  next thing happening that is you know maybe a well-funded
[2542.46 --> 2546.66]  company 50 million dollars series a you know half a
[2546.66 --> 2549.90]  billion dollar valuation which is pretty common for a
[2549.90 --> 2554.12]  SAS business how do they find that kind of person are they
[2554.12 --> 2557.06]  going through your course like where is the yeah so this is
[2557.06 --> 2559.12]  the hard part right this is we started with this right what's
[2559.12 --> 2561.34]  the career path right we're back to back to the beginning
[2561.34 --> 2564.64]  yeah and these jobs are out there you know my students are
[2564.64 --> 2571.26]  getting hired by tech companies to do tech policy but there's no
[2571.26 --> 2574.98]  good job board there's no way I can say here you want to do
[2574.98 --> 2578.08]  this here's where you go we're working on it my Ford
[2578.08 --> 2583.70]  Foundation is trying to build these paths these systems but it's
[2583.70 --> 2588.16]  not yet there so I don't have a good answer and that's bad
[2588.16 --> 2590.78]  right I mean I want to have a good I want to have an easy answer
[2590.78 --> 2594.08]  your question right you want to do this go do this thing yeah yeah
[2594.08 --> 2596.52]  right and there's a career path for you you could just go on
[2596.52 --> 2600.32]  Twitter and say I have some policy help needed and hope you don't
[2600.32 --> 2603.70]  get hacked or swindled or whatever it might be right maybe that
[2603.70 --> 2606.66]  could be one path just kidding right to your Bitcoin wallet address
[2606.66 --> 2610.72]  here for policy yeah and everyone I know who finds these jobs
[2610.72 --> 2616.80]  they're all exceptions and I do I do try to pay attention because I
[2616.80 --> 2619.80]  got a lot of students ask me you know I'm looking for a job and a job
[2619.80 --> 2623.56]  what do I do yeah but you know certainly Facebook and Google and the
[2623.56 --> 2626.30]  big guys hire them but I love you a lot of my students don't want to work
[2626.30 --> 2629.82]  for them because they're like evil they want to work for some small and
[2629.82 --> 2632.88]  more interesting company that's doing some social good
[2632.88 --> 2637.84]  so you mentioned this good idea inside of Google you mentioned that we should
[2637.84 --> 2642.24]  have you know policy decisions coming in in the beginning when we're
[2642.24 --> 2646.86]  starting software projects and it's making me think of sharing idea like idea
[2646.86 --> 2650.86]  sharing like this is a good policy it makes me think of open source and we
[2650.86 --> 2654.04]  talked about how cybersecurity has kind of grown up over the last 20 years
[2654.04 --> 2657.86]  gotten way more serious ratchet up the stakes open source has also matured
[2658.42 --> 2662.54]  during that time and gotten corporate and everything both good and bad yeah yeah
[2662.54 --> 2667.16]  and I'm just curious like how does open source weave into the story if at all and
[2667.16 --> 2670.08]  and what do you think is good and bad about it yeah I don't think it we did the
[2670.08 --> 2674.86]  story I mean open sources is a thing you know there's a myth that open source is
[2674.86 --> 2679.50]  more secure than closed source that that's not true right software that's
[2679.50 --> 2683.14]  more secure software that's been looked at and there's sort of two ways to have
[2683.14 --> 2686.86]  that happen one is you can be Microsoft and hire people to look at your software
[2686.86 --> 2692.80]  and two you could be Linux and put it out there and lots of people look at it but
[2692.80 --> 2696.02]  you could also be a company like most software companies that doesn't hire
[2696.02 --> 2699.40]  anybody look at their software you can be like most open source projects and
[2699.40 --> 2706.14]  nobody looks at it anyway so open source is another path but it is not sort of a
[2706.14 --> 2713.72]  magic elixir so I don't think open source closed source really matters here in any
[2713.72 --> 2718.62]  important way right I was thinking more like open source ideas applied to policies
[2718.62 --> 2722.54]  right apply so then now they're now here we're getting interesting and and it's
[2722.54 --> 2728.90]  open source ideas it's agile computing ideas right right how do we make policy at
[2728.90 --> 2733.28]  the speed of tech that's actually hard you know the the story I'll tell in class
[2733.28 --> 2736.86]  is about drones and if you remember the history of drones there are just a drone
[2736.86 --> 2741.08]  start appearing on the on the consumer market and everyone says you can't
[2741.08 --> 2746.34]  regulate drones it is too early you will destroy the nascent industry and then one
[2746.34 --> 2751.88]  year everyone gets on for Christmas and then you can't regulate drones it's too
[2751.88 --> 2755.32]  late everybody has them we're already flying them right there was never a
[2755.32 --> 2761.06]  moment when it was right to regulate drones now this is I think a microcosm of
[2761.06 --> 2765.58]  of the problem we have in the beginning you don't know what to do it's too early to
[2765.58 --> 2772.84]  do it and at the end there are too many I don't know rich lobbyists preventing you
[2772.84 --> 2778.98]  from doing anything so how do we navigate that this is actually I think a very big
[2778.98 --> 2784.88]  problem of regulation in the 21st century and way bigger than security anything we're
[2784.88 --> 2789.32]  talking about and you know it's something that we really need to think about you know
[2789.32 --> 2796.22]  can we use the ideas of open source or agile right agile software development and apply it
[2796.22 --> 2803.86]  to legislation apply it to policy I think the answer is yes I don't know how but we need to
[2803.86 --> 2809.02]  figure it out yeah what about the flip side of that on open source in terms of an attack vector
[2809.02 --> 2814.46]  what are your thoughts as uh as a security person you know again open source and closed source both
[2814.46 --> 2820.86]  have attack vectors you know we have seen uh open source attacked a lot of open source projects are
[2820.86 --> 2827.08]  very poorly maintained and so by by a hobbyist who's not doesn't have a lot of security you see an
[2827.08 --> 2833.68]  open source project being taken over by malicious actors and being subverted but you know you see a lot of
[2833.68 --> 2838.32]  this is a proprietary software as well I'm not sure it's a difference that makes a difference
[2838.32 --> 2845.14]  it kind of does some interesting things to open source too because you to make open source more
[2845.14 --> 2850.86]  secure in some ways you have to put money involved you have to put organization involved potentially
[2850.86 --> 2856.54]  more people involved you know eyeballs or just more watchers which essentially turns it into like a
[2856.54 --> 2861.40]  mini organization which isn't necessarily proprietary software it's still open it's still open source
[2861.40 --> 2866.88]  that's still permissory license all that good stuff which is the virtues of open source but it does
[2866.88 --> 2872.32]  create a lot of complexity around the idea of open source and there's also a tragedy of the commons
[2872.32 --> 2879.20]  right if everyone's using this open source project in their software everyone assumes somebody else is
[2879.20 --> 2884.68]  evaluating it and then nobody evaluates it and we see this a lot with log4j was an example of that
[2884.68 --> 2888.74]  right everyone thought someone else was paying attention log4j was actually just this guy and suddenly
[2888.74 --> 2896.54]  there's this huge vulnerability so there is a fix happening now I think it's the open source
[2896.54 --> 2903.70]  foundation has set up a program and they're getting the big tech companies to put in money I think
[2903.70 --> 2909.78]  Google and Microsoft each put in five million to we're all going to evaluate these open source projects
[2909.78 --> 2914.82]  so this third party is going to do the work the big companies that benefit are going to put in money
[2914.82 --> 2920.14]  and everyone benefits and it's called I think the alpha omega project the idea is they're going to
[2920.14 --> 2925.96]  look at the most popular and critical open source projects really carefully which is the alpha and
[2925.96 --> 2932.16]  then like run automatic vulnerability scanning tools against the top 10 000 libraries that's the omega
[2932.16 --> 2941.94]  and you know can we sort of bypass the tragedy of the commons and then get some real evaluation
[2941.94 --> 2947.20]  of these things that it turns out we're relying on even though we don't realize it
[2947.20 --> 2951.20]  you
[2971.94 --> 2978.36]  this episode is brought to you by our friends at fire hydrant fire hydrant is the reliability platform
[2978.36 --> 2985.36]  for every developer incidents they impact everyone not just sres they give teams the tools to maintain
[2985.36 --> 2991.50]  service catalogs respond to incidents communicate through status pages and learn with retrospectives
[2991.50 --> 2997.28]  what would normally be manual error prone tasks across the entire spectrum are responding to an incident
[2997.28 --> 3002.68]  they can all be automated in every way with fire hydrant they have incident tooling to manage
[3002.68 --> 3008.54]  incidents of any type with any severity with consistency declare and mitigate incidents all
[3008.54 --> 3014.18]  from inside slack service catalogs allow service owners to improve operational maturity and document
[3014.18 --> 3020.08]  all your deploys in your service catalog incident analytics light extract meaningful insights about your
[3020.08 --> 3025.66]  reliability over any facet of your incident or the people who respond to them and at the heart of it all
[3025.66 --> 3030.36]  incident run books they let you create custom automation rules to convert manual tasks into
[3030.36 --> 3036.28]  automated reliable repeatable sequences that run when you want you can create slack channels jira tickets
[3036.28 --> 3041.68]  zoom bridges instantly after declaring an incident now your processes can be consistent and automatic
[3041.68 --> 3047.40]  the next step is to try it free small teams up to 10 people can get started for free with all fire
[3047.40 --> 3054.96]  hydrant features included no credit card is required get started at fire hydrant.io again fire hydrant.io
[3054.96 --> 3060.00]  and by our friends at source graph they recently launched code insights now you can track what
[3060.00 --> 3064.32]  really matters to you and your team in your code base transform your code into a queryable database
[3064.32 --> 3069.60]  to create customizable visual dashboards in seconds here's how engineering teams are using code
[3069.60 --> 3075.54]  insights they can track migrations adoption and deprecation across the code base they can detect and
[3075.54 --> 3081.78]  track versions of languages or packages they can ensure the removal of security vulnerabilities like log4j
[3081.78 --> 3088.52]  can understand code by team track code smells and health and visualize configurations and services
[3088.52 --> 3093.02]  here's what the engineering manager at prezzi has to say about this new feature quote as we've grown
[3093.02 --> 3098.42]  so has a need to better track and communicate our progress and our goals across the engineering team
[3098.42 --> 3104.26]  and the broader company with code insights our data and migration tracking is accurate across our entire
[3104.26 --> 3110.72]  code base and our engineers and our managers can shift out of manual spreadsheets and spend more time
[3110.72 --> 3116.84]  working on code end quote the next step is to see how other teams are using this awesome feature
[3116.84 --> 3124.32]  head to about.sourcegraph.com slash code dash insights this link will be in the show notes again
[3124.32 --> 3128.56]  about.sourcegraph.com slash code dash insights
[3128.56 --> 3147.62]  one thing that's amazing to me about you bruce is just how long you've been going at it so
[3147.62 --> 3152.02]  stop telling me i'm old the second time first one was about the book you had when you were in college
[3152.02 --> 3157.40]  i'm getting tired of this longevity i'm speaking to your longevity not your age so you've been doing
[3157.40 --> 3162.14]  this monthly newsletter the cryptogram and i think i did subscribe to it after reading the book and i
[3162.14 --> 3169.48]  just subscribed to it pretty much my whole adult life now and since 1993 that's three sorry my question
[3169.48 --> 3176.60]  is what drives you like how do you stay so on this like every month this thing and what i find about
[3176.60 --> 3179.50]  it is a lot of times i just read the headlines because there's so much in there i mean you're
[3179.50 --> 3183.72]  writing a lot you're logging a lot how do you keep it going man so interesting story so cryptogram is
[3183.72 --> 3188.84]  from like 1998 i started a monthly newsletter so that was back when email newsletters were cool the
[3188.84 --> 3194.44]  first time before they got uncool and now they're cool again well you're cool again now right and then i
[3194.44 --> 3201.58]  then i turned that into a blog in 2004 and that's like the second wave of blogs when blogs were cool
[3201.58 --> 3205.48]  before they were uncool and now i guess something else is cool i don't know what's cool now
[3205.48 --> 3211.72]  so the monthly cryptogram is now just a compilation of the daily blog right so i don't know if you see
[3211.72 --> 3217.24]  you see it in the email some people see it on on my website right and i have been doing it pretty
[3217.24 --> 3227.52]  much every day the daily weekdays since 2004 that's all right a long time that's impressive and a lot of
[3227.52 --> 3235.18]  it is i it it forces me to stay current right it forces me to start reading around and you know seeing
[3235.18 --> 3243.26]  what's happening seeing what's being talked about and that's good for me i get a lot of uh my uh
[3243.26 --> 3251.44]  entries and news items from readers i get a lot of email which is uh really useful to me so some
[3251.44 --> 3258.22]  people will send me links all the time and that is something i use to stay current so that i really
[3258.22 --> 3264.00]  appreciate that any uh listeners who send me uh emails when they see a good crypto story thank you keep
[3264.00 --> 3272.54]  doing that and then i you know i to me writing is how i understand things so it's how i process the
[3272.54 --> 3282.32]  news it's how i process all of this so you're seeing my process of processing i just do it a
[3282.32 --> 3287.30]  little bit in public yeah super cool what would you say over the last since you said you've been doing
[3287.30 --> 3293.54]  a daily since 2004 but it's been longer than that maybe give us a trip down memory lane what are some of
[3293.54 --> 3297.44]  the biggest most surprising things you saw in security oh man i don't even know i'm terrible
[3297.44 --> 3301.14]  at memory lane i really am let's say the last five years last couple years what are some of the biggest
[3301.14 --> 3307.44]  deals well i mean i mean i remember uh writing about september 11 terrorist attacks i remember and
[3307.44 --> 3312.72]  i mean it was the first time i ever did an issue out of sequence and i wrote a bunch of articles i think
[3312.72 --> 3320.98]  and i go back and read it and this is you know september 30th 2001 i'm writing about i think a lot of
[3320.98 --> 3327.48]  things that were became part of the debate years later i thought what was really kind of interesting
[3327.48 --> 3332.42]  didn't you coin the term security theater security theater right i invented that term i think that's my
[3332.42 --> 3338.84]  uh that's my contribution to popular culture if that's what you want to call it yeah yeah they that's
[3338.84 --> 3343.98]  the notion the notion of security theater the other thing i was going to call it was potemkin security
[3343.98 --> 3350.46]  but it turns out that surprisingly few people younger than me recognize the term potemkin village
[3350.46 --> 3357.40]  yeah right it is a cold war term that people don't know anymore did that term come out of the post 9
[3357.40 --> 3364.20]  11 patriot act and no potemkin village is uh from uh communist russia no i mean the security theater
[3364.20 --> 3368.96]  like when were you thinking about it security theory yes yeah i mean i coined the phrase soon
[3368.96 --> 3375.48]  after 9 11 i mean uh wikipedia has the actual origin okay of where what does it mean what does it mean
[3375.48 --> 3381.04]  it means people are acting like it's secure but it's just for show yeah security theater is so the
[3381.04 --> 3385.82]  example i would use right after 9 11 i don't know if you remember there were national guard troops
[3385.82 --> 3391.64]  stationed at airports uh they were just inside security off to the side in uniform holding a big gun
[3391.64 --> 3396.82]  those guns had no bullets because my god a 22 year old with a gun in an airport what could go
[3396.82 --> 3401.34]  possibly go wrong you wouldn't you do not want to give him ammunition yeah but it was there to make
[3401.34 --> 3410.22]  people feel better it actually was theater to make people feel safer flying you got any modern examples
[3410.22 --> 3414.72]  of security theater things are going on today maybe you know there's a lot of uh of covet theater
[3414.72 --> 3420.60]  yeah right there's a lot of of health measures that that make no sense remember people wiping down their uh
[3420.60 --> 3427.30]  their mail it's amazing what uh what foot will do to you you know it is amazing wear the mask on the
[3427.30 --> 3431.22]  way into the restaurant but once you sit down you're safe right and you take it off what is it what are we
[3431.22 --> 3437.34]  doing here yeah but you know and and some of that is valuable because you know if people are more
[3437.34 --> 3443.20]  afraid than they should be then a little theater is good but some of it is just makes no sense yeah
[3443.20 --> 3449.26]  it's perception too it's like a perceived threat it's all about perception because because fear is a
[3449.26 --> 3456.06]  perception yeah even to yourself security is a feeling and a reality it's both and they are
[3456.06 --> 3463.14]  different yeah you can feel secure when you're not and you can be secure and not feel it yeah
[3463.14 --> 3467.88]  there's an old saying just because you're not paranoid doesn't mean someone's not out to get you
[3467.88 --> 3473.94]  and just because you are paranoid doesn't mean people are out to get you exactly either way it's
[3473.94 --> 3479.38]  both true yeah that's why i like it yeah that's funny jared asked the question before about
[3479.38 --> 3484.04]  developers and what they could do building systems tomorrow and you kind of mentioned some of the
[3484.04 --> 3489.08]  things they could do which was essentially find somebody in policy and hire them though the supply
[3489.08 --> 3493.76]  of them is challenging to find because the path is is challenging what else would you share with
[3493.76 --> 3499.20]  today's technologists that they need to know things that you're preaching that software devs
[3499.20 --> 3503.96]  engineers leaders of engineering departments people building products should know about the
[3503.96 --> 3509.36]  state of security today that they don't know so say secure so we're the state of the world that you
[3509.36 --> 3516.70]  know we are used to thinking that our what we do ends at the keyboard and screen and it turns out
[3516.70 --> 3524.46]  it's not true that the stuff we write affects the world affects society affects people affects human
[3524.46 --> 3531.62]  and flourishing and we need to think that way we really do we need to think that you know when we
[3531.62 --> 3537.06]  build a software product we're building a world and you know and this is an old story i think it's a good
[3537.06 --> 3543.16]  story i don't remember friendster friendster was a social network before myspace right and uh really old
[3543.16 --> 3548.36]  they had something called the top eight you could have as many friends as you want like any social network
[3548.36 --> 3554.40]  but the top eight would appear on your home screen it was eight it was not six it was not ten it was eight
[3554.40 --> 3560.98]  whatever reason some programmer decided eight multiple to power of two we're good in high schools all across
[3560.98 --> 3566.38]  the country who your top eight friends suddenly mattered right now the engineer just picked the number
[3566.38 --> 3573.22]  but wouldn't it be great if there was like a teen psychologist who said no no if you make eight
[3573.22 --> 3580.12]  it's going to be a disaster make it 12 you must make it 12 engineer would say okay it's 12
[3580.12 --> 3587.28]  unintended consequences right and it used to be the unintended consequences didn't matter nobody cared
[3587.28 --> 3593.18]  how usenet worked because usenet wasn't anything important ever no one kind of cared in the beginning
[3593.18 --> 3600.08]  how email worked but now it matters now the unintended consequences can affect democracy
[3600.08 --> 3610.38]  and maybe we should pay a little more attention to that yeah so my advice is that your tech system
[3610.38 --> 3619.44]  is not only a tech system it is a human system fundamentally and you need people who understand
[3619.44 --> 3625.60]  that on your design and development teams so you're saying don't move fast and break things
[3625.60 --> 3632.66]  move deliberately fix things there you go there you go uh bruce one thing i've noticed and you you
[3632.66 --> 3637.38]  you confessed it here today that you you live in your email like that's uh i guess in a sense it's
[3637.38 --> 3641.26]  kind of your primary social network right like that's how you communicate yeah and i'm not on any
[3641.26 --> 3645.98]  social network i mean email is my life i come from the generation where email is my life yeah and and
[3645.98 --> 3649.94]  of course kids these days don't use email they use text and i send me a text what are you doing just
[3649.94 --> 3654.36]  send me an email i was sending you a calendar invite you're like please don't just email me that don't don't
[3654.36 --> 3659.68]  send me a calendar just send me an email stop it keep it simple it made me wonder about some of your
[3659.68 --> 3664.04]  personal practices like some of the whether it's privacy or security best practice like what do you
[3664.04 --> 3670.64]  do in your life of technology that may be different or unique or at least is notable for people who
[3670.64 --> 3675.20]  want to be like you yeah you know i wouldn't recommend what i do to anybody because you know a lot
[3675.20 --> 3681.86]  of the stuff i do that's unique is like not using normal technology like calendar invites okay i mean i
[3681.86 --> 3688.62]  don't use the cloud for anything that makes me a weirdo right i don't keep my email in the cloud
[3688.62 --> 3693.34]  is that because you know better no because i've always done it my way and it and i that means i can
[3693.34 --> 3698.14]  do my stuff but i don't have an internet connection okay i mean i hate google docs i mean i don't do and
[3698.14 --> 3707.10]  and it does make me a freak and hard to get along with so so i've hard pressed to uh to like give you my
[3707.10 --> 3713.66]  advice as something to follow i'm i'm think i'm a cautionary tale of something to avoid okay but yet
[3713.66 --> 3719.30]  you do it yet i do it right you know and i can get away with it because i could be ordinary and you
[3719.30 --> 3723.02]  still want me on your show but if i was someone like you know less important you'd say who is this
[3723.02 --> 3727.76]  idiot we're not we're not going to interview him he doesn't even use a calendar invite well said
[3727.76 --> 3732.98]  well said you don't use the cloud i think are you involved at least a company there's a tie to
[3732.98 --> 3737.32]  the the solid project i wanted to ask you about that project tim berners lee solid we talked about
[3737.32 --> 3742.40]  decentralized networks with cryptocurrencies but here's one that's decentralized storage it's got
[3742.40 --> 3745.80]  of course tim berners lee attached to it so it sounds like it's interesting are you attached to
[3745.80 --> 3750.52]  that somehow are you working on that so i i am so i'm a big fan of decentralization which is you don't
[3750.52 --> 3756.46]  need don't use a blockchain okay email is decentralized i can send an email to anybody regardless of what
[3756.46 --> 3762.24]  they're using which is different than like a facebook message sms is decentralized web pages are
[3762.24 --> 3770.10]  decentralized lot centralization is great and uh solid is a vision of decentralized data
[3770.10 --> 3777.78]  the idea being right now your data is siloed right fitbit has your health data and your phone has your
[3777.78 --> 3783.92]  location data and someone else has your photographs and on and on and on wouldn't it be great if all your
[3783.92 --> 3789.44]  data was in one place and you got to decide and then you can do things with your data that you
[3789.44 --> 3796.56]  couldn't do otherwise you know the uh i don't know my airline has a lot of my data in this
[3796.56 --> 3802.42]  figure flyer program so it is uh the hotel program i like they don't actually want my data they just want
[3802.42 --> 3811.46]  access to it my data was in my and this the term solid uses is pod i have control over it i can uh see
[3811.46 --> 3817.34]  who accesses it i can give permissions if my address changes i just change it in my pod it propagates
[3817.34 --> 3824.40]  everywhere you know i had to uh fill out i mean i had to download an app because i'm going to spain to
[3824.40 --> 3831.16]  type in my health information to get a qr code so when i land in spain i can show it and get into the
[3831.16 --> 3838.20]  country so i'm entering my data again and again and again right that doesn't make sense and once this
[3838.20 --> 3841.18]  app has my i don't even know what they're going to do with it i have no idea what spain's gonna do my
[3841.18 --> 3847.54]  data probably know they're going to sell it to cambridge analytica they could who knows and and
[3847.54 --> 3853.42]  this is a way of thinking about data that puts people in control it's actually a way that actually
[3853.42 --> 3858.58]  solves the problems that gdpr tried to solve so yeah i'm involved i think it's a big deal he's really
[3858.58 --> 3864.04]  important and i think it's valuable that guy is tim berners lee it could conceivably change the world
[3864.04 --> 3871.16]  he has a track record for doing that so so yeah i'm super excited about it what's the status is it
[3871.16 --> 3879.50]  is it usable is it private it's a couple of things it is a w3c standard so it's a web standard there's
[3879.50 --> 3885.56]  also a company so i'm actually involved in a company called interrupt which is basically the red hat of
[3885.56 --> 3893.20]  solid right they are making a commercial server and system for the public standard so there's a free
[3893.20 --> 3899.12]  server and all kinds of free tools but there's also these commercial series of tools can you use
[3899.12 --> 3904.08]  it today yes you can use it today you can get your pod you can do it you know you kind of got to be
[3904.08 --> 3909.58]  a techie to use it today it's like the early days of the web you have to be program html to use it
[3909.58 --> 3919.12]  the early browsers were not at all intuitive so it's it's early for like regular people but for techies
[3919.12 --> 3923.94]  it's it works great i think it's got good premises though it's like here's my data and i have
[3923.94 --> 3929.68]  integrations to that data and i can give them permission i can fine tune those permissions yeah but
[3929.68 --> 3935.50]  the rest of the world has to begin to accept it like hilton honors club or airlines right and it's
[3935.50 --> 3941.00]  going to happen slowly but i think that from a liability perspective like marriott was hacked by the
[3941.00 --> 3947.06]  chinese and they lost everybody's data so having everybody's data is a huge liability for marriott hotels
[3947.06 --> 3954.36]  what they actually want is access to your data when they need it if they knew they had that they
[3954.36 --> 3960.16]  wouldn't need to store a copy locally because that is just dangerous right but you can't guarantee
[3960.16 --> 3965.22]  access so they need to store a copy locally fixing that i think is important have you ever had like to
[3965.22 --> 3971.24]  write a contract and have somebody sign it yeah it's challenging though right oh yeah right yeah right
[3971.24 --> 3976.16]  because contracts are very human right so the reason why they're five years and not one year is
[3976.16 --> 3980.52]  because every time you got to go back you're reminding them right so i think maybe the challenge
[3980.52 --> 3987.18]  however with solid might be that okay hilton wants access but man they're accessing it quite often
[3987.18 --> 3992.40]  way more than i want whereas if they actually had it they could do whatever they wanted and access it
[3992.40 --> 3996.36]  whenever they wanted which we don't want actually right you know we don't want to have that kind of
[3996.36 --> 4002.98]  now i like i would like to know when they're using it what they're using it for yeah it seems fair
[4002.98 --> 4009.14]  yeah yeah and maybe you could even build payment layers on top so now instead of you know facebook
[4009.14 --> 4014.58]  selling my data i can certainly can i just change banks and and i had to give them a whole lot of
[4014.58 --> 4020.72]  data yeah why can't i just like say here here's my pod you now have access to all that data right
[4020.72 --> 4026.66]  done yeah or for a dollar you can have access to my data well you know but i'm opening a bank
[4026.66 --> 4029.98]  account i kind of want them to have well i know i'm just thinking in general so there's a
[4029.98 --> 4034.10]  transaction here i want to give them the data sure i just don't want to type all the damn stuff in
[4034.10 --> 4039.20]  again right that reminds me of your you have this great quote from the data and goliath book you
[4039.20 --> 4043.50]  said data is the pollution problem of the information age and protecting privacy is the environmental
[4043.50 --> 4047.86]  challenge i like that casting of that i think that plays well into this whole solid idea isn't it
[4047.86 --> 4053.66]  i do too you know and it's actually a pretty rich metaphor yeah right because if you think about it
[4053.66 --> 4063.14]  all all computer processes produce data it stays around kind of festering we spend a lot of time
[4063.14 --> 4069.78]  talking about its reuse how it's recycled how it's disposed of what its secondary characteristics are
[4069.78 --> 4077.78]  and i actually if you think back to the early decades of the industrial age you know we as society
[4077.78 --> 4088.00]  kind of ignored pollution in our rush to build the industrial age today we are ignoring data in
[4088.00 --> 4092.76]  our rush to build the information age and i think just as we look back at those people 100 years ago
[4092.76 --> 4098.64]  and say how could you have been so short-sighted we will be judged you know a couple of generations
[4098.64 --> 4106.12]  from now on how we could be so short-sighted so i actually think the metaphor is really robust
[4106.12 --> 4112.24]  the data is the pollution problem of the information age well i'll be fascinated to see how solid goes
[4112.24 --> 4117.02]  hopefully it gets adoption because i do think from what i've read about it what you're telling me about
[4117.02 --> 4122.68]  it i think it has a lot of fundamental things done well and it is a huge chicken and egg problem in all
[4122.68 --> 4131.48]  of these yeah but you know we're we're getting uh traction with uh governments oddly enough the notion of a
[4131.48 --> 4139.34]  country giving every citizen a pod because governments also don't want their citizens have to type the same
[4139.34 --> 4145.56]  stuff in again and again and want them to be able to share data among different government agencies
[4145.56 --> 4152.66]  so uh mostly in europe but governments seem to be the uh early adopters here which is weird because
[4152.66 --> 4158.48]  government as early adopter is like an insane thing i just said yeah yeah that was surprising actually too
[4158.48 --> 4166.94]  well on the note of policy it meets technology uh meets repetition i would just like to take a moment
[4166.94 --> 4172.78]  to say to the stack overflow folks i've already accepted your cookie policy okay i don't want to
[4172.78 --> 4178.18]  accept it every single time i come to your website oh my gosh every single time it's like you know you
[4178.18 --> 4183.18]  should remember i just said you can keep my cookies so put that information in a cookie and store it
[4183.18 --> 4187.42]  so i don't have to accept your cookie policy every time just or just put it into the browser
[4187.42 --> 4193.26]  bake it into the browser they might be required by the regulation to ask you every time i don't know
[4193.26 --> 4201.16]  the answer to that but it's that's interesting yeah right and and now can we solve that by you having
[4201.16 --> 4209.32]  your cookie policy in your browser yes so it would check you know what is this person's cookie policy did
[4209.32 --> 4215.50]  he did he change his mind i mean we need to give you the ability to change your mind so how do we do that
[4215.50 --> 4221.26]  so we're solving it the dumb way by asking you every time do you consent do you consent right
[4221.26 --> 4230.04]  maybe you can put your consents in some kind of accessible document that they can look at
[4230.04 --> 4235.16]  but here again right this is a problem yeah we have to ask you every time so then we've asked you
[4235.16 --> 4240.84]  already sounds like something that they might build into the google chrome browser and i know from
[4240.84 --> 4245.00]  our previous conversations that you refuse to use such things i'm curious yeah but they build a
[4245.00 --> 4253.96]  chrome browser it would be like default you know spy on you default spy yeah firefox fan over here i'm i'm
[4253.96 --> 4259.90]  a firefox user yes fair enough fair enough all right bruce well we've used lots of your time i really
[4259.90 --> 4264.68]  appreciated this conversation adam any other questions before where you let him go i'm clear this was fun
[4264.68 --> 4268.20]  this was a lot of fun bruce i i appreciate i'm gonna catch up with one of your books
[4268.20 --> 4272.56]  all right mentioned atop the show that's cool which is the one that we should read you know
[4272.56 --> 4277.66]  so i mean i love them all for different reasons so in the new book the newish books that are worth
[4277.66 --> 4284.82]  reading i'm staring at my shelf uh data and goliath is about data and privacy after that i wrote a book
[4284.82 --> 4289.66]  called click here to kill everybody my favorite title which is really about the internet things and
[4289.66 --> 4296.12]  safety and before that i wrote a book on called liars and outliers which is about trust
[4296.12 --> 4304.48]  and how systems enable trust so those are my three most recent i'm coming out with a book next year
[4304.48 --> 4311.40]  which is due in two weeks so i'm kind of panicky about this which is really about hacking society
[4311.40 --> 4318.22]  broader social systems well what's that one going to be called can you tease us uh probably a hacker's
[4318.22 --> 4324.08]  mind who still was still finalizing a title nice very cool yeah bruce thank you so much for
[4324.08 --> 4328.00]  all your wisdom and you know what honestly the book writing while you may not become rich and
[4328.00 --> 4333.14]  famous because of it you will become rich and famous in terms of helping other people you know
[4333.14 --> 4338.46]  i think that nobody writes books to make money with the exception of like you know the top new york
[4338.46 --> 4344.04]  times bestseller thriller right nobody writes books to make money your wealth is in the appreciation of
[4344.04 --> 4347.64]  the knowledge you're sharing so that's that's my point is like you know right for someone to say
[4347.64 --> 4352.82]  i read your book in college and it changed my life that's like the best compliment you could ever get
[4352.82 --> 4357.94]  yeah all i know that's the point is thank you for sharing your wisdom i appreciate that hey thank you
[4357.94 --> 4358.88]  for having me
[4358.88 --> 4365.94]  all right that's it for the show thank you for tuning in thanks again to bruce for joining us to talk about
[4365.94 --> 4371.24]  such an important subject what are your thoughts on the security of tomorrow's software let us know in
[4371.24 --> 4377.52]  the comments links are in the show notes if you haven't yet subscribed now is the time head to
[4377.52 --> 4382.44]  changelog.fm for all the ways and if you dig what we're doing on this show you might enjoy our other
[4382.44 --> 4387.68]  pods in the changelog podcast universe for fans of my show founders talk i've been cranking out some
[4387.68 --> 4393.22]  awesome episodes here's a clip from episode 89 with sitza brandage ceo of gitlab on the biggest
[4393.22 --> 4400.38]  difference between gitlab and github yeah there's strong network effects around open source projects so if
[4400.38 --> 4404.36]  you're going to host your open source project somewhere you can pick either but there's an
[4404.36 --> 4410.54]  incentive to be on github because a lot of open source developers are already there that network
[4410.54 --> 4415.62]  effect is much reduced if you're talking about a company if it's a company i'm going to choose a
[4415.62 --> 4421.04]  platform i can just tell all the people in the company working on the proprietary code to use
[4421.04 --> 4428.60]  something else so that's something where we specialize gitlab is an open source platform
[4428.60 --> 4436.40]  that mostly hosts closed source code github is the opposite it's closed source and you're really
[4436.40 --> 4443.02]  good at hosting open source projects so we've chosen different adventures and we're really
[4443.02 --> 4449.60]  comfortable with our adventure making companies more productive having a devops platform that allows
[4449.60 --> 4453.94]  them to go quicker from planning something to getting it out there and getting the feedback
[4453.94 --> 4459.86]  by integrating all the steps on the devops like cycle in a single application a single data store
[4459.86 --> 4465.44]  and make that work really really well continue listening to that pod at founderstalk.fm slash 89
[4465.44 --> 4472.16]  that is episode 89 big thanks again to our friends and partners at fastly check them out at fastly.com
[4472.16 --> 4476.66]  also to break master cylinder for making those awesome beats they're fresh they're banging and we love
[4476.66 --> 4480.46]  them all right this show's done thank you again for tuning in we'll see you next week
[4480.46 --> 4483.50]  so
[4503.34 --> 4503.40]  so
[4503.40 --> 4507.84]  so
[4507.84 --> 4511.00]  Game on.
