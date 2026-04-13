[0.00 --> 6.70]  Bandwidth for Changelog is provided by Fastly. Learn more at Fastly.com. We move fast and fix
[6.70 --> 11.42]  things here at Changelog because of Rollbar. Check them out at Rollbar.com. And we're hosted
[11.42 --> 17.66]  on Linode servers. Head to linode.com slash Changelog. This episode of Practical AI is
[17.66 --> 23.28]  brought to you by Hired. One thing people hate doing is searching for a new job. It's so painful
[23.28 --> 28.32]  to search through open positions on every job board under the sun. The process to find a new
[28.32 --> 33.94]  job is such a mess. If only there was an easier way. Well, I'm here to tell you there is. Our
[33.94 --> 38.64]  friends at Hired have made it so that companies send you offers with salary, benefits, and even
[38.64 --> 44.04]  equity up front. All you have to do is answer a few questions to showcase who you are and what type
[44.04 --> 48.90]  of job you're looking for. They work with more than 6,000 companies from startups to large publicly
[48.90 --> 53.88]  traded companies in 14 major tech hubs in North America and Europe. You get to see all of your
[53.88 --> 58.88]  interview requests. You can accept, reject, or make changes to their offer even before you talk
[58.88 --> 62.68]  with anyone. And it's totally free. This isn't going to cost you anything. It's not like you have
[62.68 --> 66.52]  to go there and spend money to get this opportunity. And if you get a job through Hired, they're even
[66.52 --> 70.46]  going to give you a bonus. Normally it's $300, but because you're a listener of Practical AI,
[70.82 --> 75.74]  it's $600 instead. Even if you're not looking for a job, you can refer a friend and Hired will send
[75.74 --> 81.48]  you a check for $1,337 when they accept the job. As you can see, Hired makes it too easy.
[81.48 --> 84.70]  Get started at Hired.com slash Practical AI.
[97.94 --> 103.32]  Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[103.76 --> 109.26]  productive, and accessible to everyone. This is where conversations around AI, machine learning,
[109.26 --> 113.38]  and data science happen. Join the community and snag with us around various topics of the show
[113.38 --> 119.20]  at changelog.com slash community. Follow us on Twitter. We're at Practical AI FM. And now onto the show.
[123.60 --> 127.80]  So Chris, are you terrified of the GDPR?
[129.26 --> 134.40]  I am loving the GDPR from my standpoint. I'm trying to learn more about it, but I think
[134.40 --> 138.42]  though it might be imperfect, it's about time we finally
[138.42 --> 140.64]  start addressing this in a public manner.
[142.02 --> 144.36]  Sounds great. Well, I brought
[144.36 --> 147.76]  Matt and Andrew from Immuta onto our show today.
[148.22 --> 149.32]  Welcome, Matt and Andrew.
[149.70 --> 151.50]  Thanks so much. Thanks for having us.
[151.90 --> 152.94]  Welcome. Thanks for joining.
[153.40 --> 155.74]  Yeah, so I met Matt and Andrew
[155.74 --> 158.14]  back, I think, in the spring of
[158.14 --> 162.16]  2017. We ran into each other at a bunch of different conferences,
[162.16 --> 166.40]  and I realized that these guys have pretty much
[166.40 --> 171.96]  all knowledge around, you know, AI and regulation and data and privacy,
[171.96 --> 174.14]  and I was just learning a ton from them. So
[174.14 --> 177.56]  I think it's great to have them here to discuss some things around
[177.56 --> 182.56]  AI and how it should be regulated, how it is being regulated, what are what the trends are there.
[182.72 --> 184.58]  So I have so many questions for them.
[185.14 --> 188.52]  I know. I know. This is this is going to be this is going to be great.
[188.52 --> 192.86]  Right. So just to start out, Matt, why don't you give us a little bit of a personal
[192.86 --> 194.22]  intro? Yeah, sure.
[194.92 --> 197.30]  So, you know, by trade, chemist
[197.30 --> 199.34]  went into the U.S. government,
[200.20 --> 203.64]  deployed to Iraq, Afghanistan, fell in love with technology
[203.64 --> 204.68]  enabling that mission.
[205.26 --> 206.46]  And so
[206.46 --> 207.86]  leaving the government,
[208.18 --> 211.74]  went and started a services company, sold the services company,
[212.28 --> 214.96]  and then eventually got drawn right back into the government
[214.96 --> 219.84]  around the problem of how do we make the law and data science work together
[219.84 --> 222.92]  so we can solve problems at the speed of the business,
[223.12 --> 226.56]  but still maintain ethical and legal controls around our data.
[227.16 --> 230.36]  And so that kind of led in 2015 to the creation of Immuta.
[231.26 --> 234.28]  And so to today, I'm the CEO of the company.
[234.74 --> 238.04]  And we're, you know, tiny, going on 37 people,
[238.24 --> 240.06]  but are growing really fast.
[240.06 --> 244.72]  And it's a great market and, you know, just excited to be part of it.
[245.22 --> 246.32]  Yeah, I imagine that
[246.32 --> 249.38]  all the hype around GDPR and other things
[249.38 --> 251.06]  is definitely not hurting your business.
[251.22 --> 252.84]  No, certainly not quite the opposite.
[253.12 --> 254.80]  But I think the question really,
[254.96 --> 256.40]  and it would be great to talk about today's,
[256.42 --> 257.52]  is what does it actually mean?
[257.86 --> 260.26]  I think that's really, from a practical perspective,
[260.52 --> 262.88]  I think sometimes we get a little ahead of ourselves.
[263.52 --> 264.14]  Yep. Awesome.
[264.56 --> 267.54]  And Andrew, I believe, is a lawyer.
[267.66 --> 268.14]  Is that correct?
[268.14 --> 269.78]  Yes, guilty, as charged.
[271.26 --> 275.56]  Well, tell us a little bit about how you fit into this story.
[275.66 --> 278.84]  Yeah, so my title at Immuta is
[278.84 --> 280.92]  Chief Privacy Officer and Legal Engineer.
[281.76 --> 283.74]  And the legal engineer part, I think,
[283.80 --> 286.52]  is particularly relevant for today's discussion.
[286.74 --> 288.86]  And basically, my charge at Immuta
[288.86 --> 292.66]  is to think about how law and data science overlap
[292.66 --> 295.72]  and to think about what types of requirements
[295.72 --> 298.58]  law is placing on data science activities
[298.58 --> 300.66]  that we can embed within the platform.
[300.88 --> 303.14]  And so my background is I've been involved
[303.70 --> 306.86]  at Yale Information Society Project for a while.
[306.98 --> 307.42]  I'm a lawyer.
[307.42 --> 310.70]  I spent some time working for the FBI Cyber Division,
[310.84 --> 313.82]  really kind of understanding this conflict
[313.82 --> 315.58]  between compliance demands
[315.58 --> 319.30]  and the legal burden associated with data
[319.30 --> 322.14]  and all of the really new,
[322.36 --> 324.86]  really important projects that are going on
[324.86 --> 326.36]  in the data science community.
[326.62 --> 328.52]  And so the goal is to figure out
[328.52 --> 330.98]  how can we think about legal requirements
[330.98 --> 333.56]  and risk management in a new way.
[333.94 --> 334.30]  Awesome.
[334.70 --> 337.08]  Well, it sounds perfect for this discussion.
[337.46 --> 339.80]  Are you the only law engineer in the world,
[339.88 --> 341.00]  or are there more of those people?
[341.02 --> 341.44]  Legal engineer.
[341.44 --> 342.16]  Is it law engineer?
[342.16 --> 342.66]  Legal engineer.
[342.66 --> 343.24]  Legal engineer.
[343.24 --> 345.72]  So that's a hard question to answer.
[346.06 --> 347.78]  I don't know any others,
[347.78 --> 349.36]  but that doesn't mean they don't exist.
[349.98 --> 352.72]  And there's this kind of like funky history
[352.72 --> 354.64]  around even the term legal engineering.
[355.14 --> 357.74]  It actually was coined, I think,
[357.78 --> 360.36]  in the late 1980s by some folks at Stanford.
[361.10 --> 363.46]  So people have been thinking about
[363.46 --> 366.28]  what it would mean to like embed laws
[366.28 --> 368.40]  within technology for a really long time.
[368.82 --> 370.40]  So instead, you know, you're a lawyer.
[370.40 --> 373.00]  Instead of writing a memo, you write code.
[373.54 --> 375.26]  And people have been thinking about that.
[375.84 --> 378.84]  But I think really in the last few years
[378.84 --> 380.52]  with, you know, the intersection
[380.52 --> 382.38]  between data science and regulation,
[382.88 --> 385.52]  I think that we've seen a real need
[385.52 --> 387.10]  for this field of legal engineering.
[387.28 --> 389.28]  But I can neither confirm or deny
[389.28 --> 391.08]  that I'm the only legal engineer.
[392.30 --> 393.02]  All right.
[393.12 --> 394.90]  Well, thanks for those intros.
[395.36 --> 396.38]  One of you guys, maybe Matt,
[396.48 --> 397.72]  tell us a little bit about,
[397.90 --> 398.96]  you mentioned Amuta.
[398.96 --> 400.66]  What is Amuta?
[400.78 --> 402.56]  What are you guys trying to accomplish?
[403.04 --> 404.34]  What does Amuta do?
[404.86 --> 405.02]  Yeah.
[405.18 --> 406.98]  So long story short is,
[407.08 --> 409.28]  Amuta is a data management platform
[409.28 --> 410.30]  for data science.
[410.70 --> 412.38]  And the creation of Amuta
[412.38 --> 414.64]  was really at the intersection of,
[414.70 --> 415.90]  we have these three users
[415.90 --> 418.06]  that make up data science operations.
[418.06 --> 419.90]  We have data owners, you know,
[419.92 --> 421.26]  and they control the data.
[421.92 --> 422.80]  You get data scientists
[422.80 --> 423.66]  who want to use the data
[423.66 --> 424.66]  to do something with it
[424.66 --> 425.88]  and provide insight.
[425.88 --> 427.90]  And then we've got these governance
[427.90 --> 428.90]  and legal teams
[428.90 --> 430.94]  that need to oversee that process.
[431.46 --> 432.20]  And the problem is,
[432.24 --> 432.90]  is that, you know,
[432.94 --> 433.54]  what we found,
[434.12 --> 435.64]  all of these three parties
[435.64 --> 437.76]  are kind of acting as antagonists
[437.76 --> 438.30]  to one another.
[438.68 --> 439.88]  It's a very human process,
[440.00 --> 440.84]  lots of meetings,
[441.08 --> 441.80]  very slow.
[442.80 --> 443.96]  And so there wasn't a way
[443.96 --> 445.74]  to really provide each one of them
[445.74 --> 447.36]  with a single digital platform
[447.36 --> 448.90]  where they can all work symbiotically,
[448.96 --> 449.86]  even if they don't know it.
[450.38 --> 451.64]  And so we had to create Amuta
[451.64 --> 452.88]  because what we felt was
[452.88 --> 454.06]  data management
[454.06 --> 455.32]  for application development
[455.32 --> 456.06]  is very different
[456.06 --> 456.92]  than data management
[456.92 --> 458.58]  for data science operations.
[459.28 --> 460.90]  And there was a massive gap.
[461.08 --> 461.64]  So if, you know,
[461.76 --> 463.30]  other than the few companies
[463.30 --> 463.88]  in the world
[463.88 --> 465.24]  like Google
[465.24 --> 466.80]  or, you know,
[466.86 --> 469.22]  maybe even from the government side,
[469.28 --> 469.56]  NSA,
[470.12 --> 471.30]  where you have thousands
[471.30 --> 472.00]  and thousands
[472.00 --> 473.70]  of people that can write code
[473.70 --> 476.00]  that can request ad hoc access
[476.00 --> 478.18]  to all these distributed databases, right?
[478.22 --> 479.56]  There's all these silos of data,
[479.56 --> 481.82]  and they can just write ad hoc code
[481.82 --> 483.18]  to that to get access to it.
[483.42 --> 484.58]  Very few organizations
[484.58 --> 485.88]  in the world can do that.
[486.10 --> 487.30]  And the most successful,
[487.64 --> 487.98]  you know,
[488.30 --> 488.60]  can.
[489.08 --> 490.50]  But then there's all these others
[490.50 --> 491.60]  and they don't have people
[491.60 --> 492.30]  that can write code.
[492.48 --> 493.02]  So they have,
[493.12 --> 494.10]  they built applications
[494.10 --> 495.92]  and based on predicting
[495.92 --> 497.12]  the types of questions
[497.12 --> 498.42]  their analysts would want to ask
[498.42 --> 498.94]  of the data,
[499.34 --> 500.58]  they'd throw BI tools up,
[500.64 --> 501.14]  they would throw
[501.14 --> 503.16]  their own custom apps on top.
[503.52 --> 504.88]  And so their version
[504.88 --> 505.62]  of data science
[505.62 --> 506.70]  was much more complicated
[506.70 --> 508.30]  as they brought data scientists in
[508.30 --> 510.22]  who need to ask ad hoc questions
[510.22 --> 511.30]  across all these silos.
[511.68 --> 512.56]  They're managing
[512.56 --> 513.80]  their keys separately.
[513.96 --> 515.16]  So they've got hundreds of keys
[515.16 --> 516.50]  to get access to these databases.
[517.04 --> 518.34]  They're making lots of copies
[518.34 --> 518.72]  of the data
[518.72 --> 519.50]  and bring it local.
[519.86 --> 520.84]  So they're potentially
[520.84 --> 521.84]  breaking rules
[521.84 --> 522.60]  by doing that.
[522.98 --> 524.64]  And so it was very cumbersome
[524.64 --> 525.14]  and slow.
[525.64 --> 526.32]  So Amuta,
[526.62 --> 527.38]  what we did was
[527.38 --> 528.64]  is we built a,
[528.82 --> 530.40]  think of us as a data control plane
[530.40 --> 531.76]  where we can connect
[531.76 --> 533.52]  to any stored data
[533.52 --> 535.04]  in any storage system.
[535.04 --> 537.30]  We can then virtually expose
[537.30 --> 537.76]  that data
[537.76 --> 539.14]  in a read-only fashion
[539.14 --> 540.82]  to BI tools,
[540.96 --> 541.82]  data science platforms,
[541.96 --> 542.46]  IDEs,
[542.80 --> 544.20]  through generic access patterns
[544.20 --> 545.32]  versus custom APIs.
[545.48 --> 546.70]  So like file system,
[546.94 --> 547.26]  SQL,
[547.74 --> 548.16]  Spark,
[548.38 --> 548.74]  Hadoop,
[549.20 --> 549.98]  and connect to
[549.98 --> 551.54]  any of this disparate data
[551.54 --> 552.84]  through a single connection.
[553.42 --> 554.08]  And then finally,
[554.18 --> 554.76]  what we did was,
[554.82 --> 556.10]  and I think the most valuable thing
[556.10 --> 557.28]  that Amuta provides right now
[557.28 --> 558.58]  is we then built
[558.58 --> 560.50]  an interface for lawyers
[560.50 --> 561.42]  to be able to implement
[561.42 --> 562.46]  rules on this data
[562.46 --> 564.10]  and dynamically enforce
[564.10 --> 564.58]  those rules
[564.58 --> 565.88]  as people ask the questions.
[566.26 --> 567.42]  And so what that allows us
[567.42 --> 568.14]  to do is
[568.14 --> 569.38]  data owners
[569.38 --> 570.86]  can virtually expose
[570.86 --> 571.86]  their data in a catalog.
[572.14 --> 572.86]  Data scientists
[572.86 --> 574.22]  can bring any tool to bear,
[574.44 --> 575.52]  connect it to that data,
[575.92 --> 577.10]  and governance teams
[577.10 --> 578.26]  and general counsel
[578.26 --> 579.36]  can actually implement
[579.36 --> 580.08]  the law
[580.08 --> 580.92]  as it changes
[580.92 --> 582.38]  on that data
[582.38 --> 583.36]  without impacting
[583.36 --> 584.72]  any of the other parties.
[585.22 --> 586.30]  And so the idea is
[586.30 --> 586.78]  is that
[586.78 --> 588.14]  we can actually
[588.14 --> 589.24]  streamline the process
[589.24 --> 589.90]  by which people
[589.90 --> 591.06]  can get access
[591.06 --> 591.66]  to data
[591.66 --> 592.68]  so they can connect to it.
[593.14 --> 594.04]  They can control
[594.04 --> 594.86]  the data
[594.86 --> 596.00]  depending on
[596.00 --> 597.04]  the current state of law
[597.04 --> 597.94]  or where they are
[597.94 --> 598.90]  or what region they're in.
[599.22 --> 599.92]  But then we can also
[599.92 --> 601.12]  prove compliance.
[601.74 --> 602.60]  And some of that
[602.60 --> 603.34]  isn't just
[603.34 --> 605.24]  your user rights,
[605.36 --> 605.88]  but it's also,
[606.10 --> 606.76]  and I'm sure Andrew
[606.76 --> 607.64]  will talk about this later,
[608.14 --> 608.34]  it's,
[608.62 --> 609.24]  but why?
[609.86 --> 610.48]  Like for instance,
[610.64 --> 611.60]  like with the Facebook
[611.60 --> 612.84]  data leaks
[612.84 --> 613.60]  or scandal,
[613.72 --> 614.10]  if you will,
[614.44 --> 615.40]  it's not just that
[615.40 --> 616.24]  people use the data.
[616.34 --> 617.64]  They legally could use the data,
[618.14 --> 619.38]  but it was around,
[619.50 --> 621.00]  but why are you using it?
[621.00 --> 622.60]  And is it for nefarious purposes?
[622.60 --> 624.24]  So this concept of
[624.24 --> 625.56]  compliance
[625.56 --> 626.58]  and understanding
[626.58 --> 627.84]  who's using the data,
[628.06 --> 628.94]  what data is it,
[629.02 --> 629.40]  and why.
[629.96 --> 630.94]  And that's a Muta
[630.94 --> 631.48]  in a nutshell.
[632.00 --> 632.84]  That's pretty fascinating.
[633.34 --> 633.50]  Yeah.
[634.02 --> 635.64]  So you guys are,
[635.92 --> 636.96]  having thought about this
[636.96 --> 637.58]  for the last few years,
[637.62 --> 638.94]  are probably way ahead of us
[638.94 --> 640.62]  in terms of thinking about
[640.62 --> 642.04]  kind of where regulation
[642.04 --> 643.14]  around AI
[643.14 --> 643.88]  and data is
[643.88 --> 644.54]  at this point
[644.54 --> 645.96]  and kind of
[645.96 --> 646.50]  what the lay
[646.50 --> 647.40]  of the landscape is.
[647.48 --> 648.64]  Could you talk a little bit,
[648.64 --> 649.84]  in the context,
[649.92 --> 651.70]  especially with GDPR
[651.70 --> 652.86]  finally being a reality
[652.86 --> 653.62]  for everyone
[653.62 --> 654.90]  and where
[654.90 --> 656.60]  in general regulation
[656.60 --> 657.58]  is going
[657.58 --> 659.20]  and maybe even
[659.20 --> 660.20]  a bit about
[660.20 --> 661.54]  what GDPR
[661.54 --> 662.12]  is kind of getting
[662.12 --> 662.84]  right or wrong
[662.84 --> 663.74]  or could fix.
[663.98 --> 664.78]  Could you give us
[664.78 --> 665.50]  a lay of the landscape
[665.50 --> 666.92]  and maybe what we should see
[666.92 --> 667.36]  in the next
[667.36 --> 668.64]  months and years?
[669.46 --> 669.62]  Yeah.
[669.72 --> 671.20]  And we should probably say
[671.20 --> 673.04]  that the GDPR is,
[673.14 --> 673.76]  these guys are going to
[673.76 --> 674.80]  correct me if I'm wrong,
[674.98 --> 675.96]  the general data
[675.96 --> 677.74]  protection regulation.
[677.74 --> 678.46]  Is that the right,
[678.96 --> 679.54]  is that the right
[679.54 --> 680.40]  thing of the acronym?
[680.84 --> 681.58]  Bingo, yes.
[682.30 --> 682.66]  Awesome.
[682.84 --> 683.00]  Yeah.
[683.06 --> 684.88]  So it's an EU thing, right?
[685.30 --> 686.32]  Yes, it applies to.
[686.42 --> 687.44]  So I'm happy
[687.44 --> 688.10]  to take this one.
[688.30 --> 690.10]  So the GDPR
[690.10 --> 691.74]  basically applies
[691.74 --> 692.98]  to any EU data
[692.98 --> 694.10]  that could be
[694.10 --> 694.72]  considered
[694.72 --> 696.04]  personally identifying.
[696.66 --> 697.64]  And so the standard
[697.64 --> 699.02]  in practices
[699.02 --> 700.16]  was the data
[700.16 --> 701.34]  generated in the EU
[701.34 --> 703.50]  and could you use it
[703.50 --> 704.46]  to figure out
[704.46 --> 706.02]  anything about
[706.02 --> 706.88]  a human being?
[706.88 --> 707.54]  You know,
[707.60 --> 708.16]  could I identify
[708.16 --> 708.70]  your name?
[708.82 --> 709.42]  Could I identify
[709.42 --> 710.18]  where you live?
[710.58 --> 711.32]  IP addresses
[711.32 --> 712.40]  are widely considered
[712.40 --> 714.72]  to be identifying
[714.72 --> 715.68]  under the law.
[716.42 --> 717.36]  So if you're
[717.36 --> 718.20]  a data scientist
[718.20 --> 719.08]  and you're working
[719.08 --> 719.52]  with data
[719.52 --> 720.72]  that comes from the EU,
[721.26 --> 722.02]  the answer
[722.02 --> 723.24]  is that in practice
[723.24 --> 725.04]  this applies to you.
[726.72 --> 728.56]  And let me get to,
[728.80 --> 729.46]  so I'm happy
[729.46 --> 730.02]  to talk about
[730.02 --> 731.44]  the AI issue.
[731.84 --> 732.14]  That's a,
[732.32 --> 733.00]  those are really
[733.00 --> 733.66]  big questions.
[733.66 --> 734.98]  So, you know,
[735.16 --> 735.82]  jump in
[735.82 --> 737.80]  or follow up.
[738.22 --> 739.10]  But I think
[739.10 --> 740.14]  in a nutshell,
[740.68 --> 742.08]  every government
[742.08 --> 743.24]  in the world
[743.24 --> 744.68]  is realizing
[744.68 --> 746.30]  that the power
[746.30 --> 747.06]  of AI
[747.06 --> 749.12]  is new.
[749.22 --> 749.94]  It's a big deal.
[750.38 --> 751.02]  And they're talking
[751.02 --> 751.70]  about what to do
[751.70 --> 752.16]  about it.
[752.24 --> 753.68]  And so on the one hand,
[753.88 --> 754.62]  governments like
[754.62 --> 755.58]  France recently
[755.58 --> 756.28]  and the UK
[756.28 --> 757.32]  are saying,
[757.48 --> 757.80]  you know,
[757.80 --> 758.62]  we need to have
[758.62 --> 759.94]  an explicit strategy
[759.94 --> 761.90]  to promote
[761.90 --> 762.92]  this new technology.
[763.54 --> 764.36]  And then on the other hand,
[764.46 --> 765.04]  regulators
[765.04 --> 766.92]  like the ones
[766.92 --> 767.40]  that enforce
[767.40 --> 768.12]  the GDPR
[768.12 --> 769.10]  are saying
[769.10 --> 770.40]  we need to control this
[770.40 --> 771.14]  kind of like
[771.14 --> 772.12]  a not so fast.
[772.26 --> 773.54]  And so the GDPR
[773.54 --> 774.56]  is really the first,
[774.84 --> 774.98]  I think,
[775.04 --> 776.10]  major regulation
[776.10 --> 778.06]  that's been implemented
[778.06 --> 780.22]  that is explicitly
[780.22 --> 781.20]  or has parts of it
[781.20 --> 781.82]  that are explicitly
[781.82 --> 782.74]  focused on AI.
[783.04 --> 784.26]  And so in general,
[784.26 --> 785.08]  the way it's going
[785.08 --> 785.76]  to impact
[785.76 --> 786.42]  really like
[786.42 --> 787.50]  machine learning models
[787.50 --> 788.36]  is that
[788.36 --> 789.16]  there are different
[789.16 --> 790.66]  types of requirements
[790.66 --> 792.14]  for explainability.
[792.14 --> 792.88]  You might have heard
[792.88 --> 793.80]  to it as a right
[793.80 --> 794.70]  to explainability,
[794.90 --> 796.54]  which in my own opinion,
[796.54 --> 797.56]  I think is a little bit
[797.56 --> 798.20]  too much.
[798.74 --> 800.12]  But the basic idea
[800.12 --> 800.72]  is that
[800.72 --> 802.00]  when you're using models
[802.00 --> 803.46]  that are deployed
[803.46 --> 804.20]  autonomously
[804.20 --> 805.32]  or that might be
[805.32 --> 807.04]  inherently opaque
[807.04 --> 808.20]  or as some call them,
[808.26 --> 808.44]  you know,
[808.50 --> 809.44]  black box models,
[809.90 --> 810.98]  the people who are
[810.98 --> 812.60]  subject to these decisions
[812.60 --> 813.24]  whose data
[813.24 --> 814.46]  is being processed
[814.46 --> 815.26]  by these models
[815.26 --> 816.70]  have basic rights.
[816.82 --> 817.68]  And so those rights
[817.68 --> 818.18]  are,
[818.18 --> 819.44]  they should be able
[819.44 --> 820.24]  to understand,
[820.46 --> 820.96]  you know,
[821.00 --> 821.90]  how and why
[821.90 --> 822.36]  their data
[822.36 --> 823.04]  is being used
[823.04 --> 823.74]  by the model.
[823.92 --> 824.72]  They should be able
[824.72 --> 825.62]  to opt out
[825.62 --> 826.28]  or to say,
[826.46 --> 827.50]  I don't want a model
[827.50 --> 828.52]  to be making a decision,
[828.68 --> 829.00]  let's say,
[829.06 --> 829.88]  for a credit score.
[830.28 --> 830.60]  Instead,
[830.72 --> 831.64]  I want human review.
[832.08 --> 833.16]  So those are the types
[833.16 --> 833.82]  of requirements
[833.82 --> 834.94]  that the GDPR
[834.94 --> 835.90]  puts into place.
[836.58 --> 837.34]  So you alluded
[837.34 --> 838.14]  a moment ago
[838.14 --> 838.62]  about,
[838.74 --> 838.90]  you know,
[838.94 --> 839.82]  you thought that
[839.82 --> 840.94]  in that one instance
[840.94 --> 841.38]  they had gone
[841.38 --> 842.60]  a little bit too far
[842.60 --> 843.28]  or too much.
[843.42 --> 844.94]  And I really love
[844.94 --> 845.96]  your personal opinion
[845.96 --> 846.72]  on, you know,
[846.72 --> 848.46]  what do you think GDPR
[848.46 --> 849.40]  has gotten right,
[849.88 --> 850.94]  where it could stand
[850.94 --> 851.62]  a little improvement,
[851.62 --> 852.84]  and maybe even
[852.84 --> 854.28]  speculate a little bit
[854.28 --> 855.62]  about where you think
[855.62 --> 857.16]  regulation outside the EU
[857.16 --> 859.24]  or future versions
[859.24 --> 860.42]  of the EU might go,
[860.68 --> 861.88]  how will the U.S. respond,
[862.42 --> 863.22]  and just, you know,
[863.26 --> 863.78]  what are some
[863.78 --> 864.42]  of your thoughts there?
[864.42 --> 866.78]  Yeah, so the way,
[866.92 --> 867.90]  so the Europeans
[867.90 --> 870.42]  and folks like us
[870.42 --> 871.02]  in the U.S.,
[871.02 --> 872.38]  we really approach
[872.38 --> 873.68]  regulating technology
[873.68 --> 875.06]  very differently.
[875.36 --> 876.26]  In the U.S.,
[876.26 --> 878.00]  we tend to want
[878.00 --> 879.18]  specific regulations
[879.18 --> 880.78]  focused on specific problems.
[881.32 --> 882.34]  That's why we don't have
[882.34 --> 883.84]  one national regulation
[883.84 --> 885.72]  that just covers all data.
[886.28 --> 887.18]  And in the EU,
[887.72 --> 888.82]  they very much like
[888.82 --> 889.90]  the opposite approach,
[890.02 --> 890.48]  which is,
[890.62 --> 891.10]  they'll call it
[891.10 --> 892.08]  a principles-based
[892.08 --> 893.22]  approach to regulation.
[893.22 --> 894.68]  And so they want
[894.68 --> 896.40]  overarching rules,
[896.70 --> 898.02]  and the downside
[898.02 --> 899.26]  is that those rules
[899.26 --> 900.18]  come at the cost
[900.18 --> 901.96]  of very, very steep
[901.96 --> 903.38]  ambiguity and vagueness.
[903.54 --> 904.94]  And so I think
[904.94 --> 906.22]  there's a lot of good stuff
[906.22 --> 906.92]  in the GDPR,
[906.96 --> 907.64]  and I think the intent
[907.64 --> 908.26]  is wonderful.
[908.84 --> 909.70]  I think the intent
[909.70 --> 912.02]  of trying to mandate
[912.02 --> 913.38]  certain levels of fairness
[913.38 --> 915.24]  in automated decision-making,
[915.80 --> 916.74]  that's wonderful.
[916.94 --> 917.68]  But when the rubber
[917.68 --> 918.48]  meets the road,
[918.92 --> 919.72]  I think it's going to be
[919.72 --> 922.20]  very hard for a lot
[922.20 --> 923.80]  of data science
[923.80 --> 924.88]  and programs
[924.88 --> 927.10]  that are heavily investing
[927.10 --> 927.82]  in machine learning.
[928.20 --> 929.44]  It's going to be very hard.
[929.56 --> 929.88]  There's going to be
[929.88 --> 930.80]  a lot of fine-tuning
[930.80 --> 932.32]  as to what some
[932.32 --> 933.42]  of these specific provisions
[933.42 --> 934.46]  actually mean.
[934.58 --> 935.24]  How specific
[935.24 --> 936.52]  does the explanation
[936.52 --> 937.14]  of the model
[937.14 --> 938.86]  actually have to be?
[939.08 --> 939.82]  And in particular,
[940.48 --> 941.96]  when is it not specific enough?
[942.08 --> 943.72]  When is it vague enough?
[944.26 --> 945.18]  And when is an explanation
[945.18 --> 946.50]  not detailed enough
[946.50 --> 947.08]  that someone should
[947.08 --> 948.10]  actually be penalized?
[948.10 --> 949.30]  So those are really
[949.30 --> 950.02]  hard questions.
[950.20 --> 950.78]  Legal departments
[950.78 --> 952.26]  everywhere are focusing
[952.26 --> 952.78]  on them.
[953.38 --> 955.10]  And we're going to start
[955.10 --> 956.80]  to see how that regulation
[956.80 --> 957.94]  is enforced,
[958.08 --> 958.86]  and I think we'll start
[958.86 --> 959.70]  to learn from it.
[959.84 --> 961.14]  I would say that I think
[961.14 --> 963.50]  one of the strongest points,
[963.86 --> 964.60]  and this is something
[964.60 --> 965.38]  we've been really focused
[965.38 --> 965.98]  on at Immuta,
[966.44 --> 967.44]  one of the strongest points
[967.44 --> 968.60]  of the GDPR,
[969.00 --> 969.66]  in some senses,
[969.76 --> 970.82]  I think the genius of it,
[971.20 --> 972.08]  is that it bets
[972.08 --> 972.92]  really heavily
[972.92 --> 974.12]  on purpose-based
[974.12 --> 975.20]  restrictions on data.
[975.20 --> 977.42]  Most regulations
[977.42 --> 978.10]  around data
[978.10 --> 979.12]  are focused on
[979.12 --> 980.78]  data at collection time,
[981.56 --> 982.94]  and a lot of that means
[982.94 --> 984.08]  that the emphasis
[984.08 --> 984.96]  is on consent.
[985.14 --> 986.14]  So I consent
[986.14 --> 987.12]  at collection time
[987.12 --> 988.04]  to give you,
[988.06 --> 988.42]  you know,
[988.76 --> 989.56]  X, Y, and Z
[989.56 --> 990.16]  of my data.
[990.72 --> 991.94]  And that's the traditional
[991.94 --> 992.76]  approach to data.
[993.12 --> 994.68]  What the GDPR recognizes
[994.68 --> 995.80]  is that in addition
[995.80 --> 996.34]  to that,
[996.76 --> 998.46]  you need to be able
[998.46 --> 999.16]  to understand
[999.16 --> 999.70]  and restrict
[999.70 --> 1000.68]  how that data
[1000.68 --> 1002.32]  is going to be used
[1002.32 --> 1003.88]  as it's being generated.
[1004.50 --> 1005.02]  And so that's
[1005.02 --> 1005.88]  a really new
[1005.88 --> 1006.88]  type of concept.
[1007.60 --> 1008.12]  And frankly,
[1008.24 --> 1009.04]  I think we generate
[1009.04 --> 1009.82]  so much data,
[1010.28 --> 1011.48]  it is frankly impossible
[1011.48 --> 1012.64]  for us as consumers
[1012.64 --> 1013.34]  and individuals
[1013.34 --> 1014.18]  to understand
[1014.18 --> 1015.74]  what types of insights
[1015.74 --> 1016.66]  we're giving up
[1016.66 --> 1017.50]  as we generate
[1017.50 --> 1018.02]  this data,
[1018.44 --> 1019.00]  which is, you know,
[1019.06 --> 1019.62]  the beauty
[1019.62 --> 1021.26]  of data science.
[1021.66 --> 1022.80]  And so placing
[1022.80 --> 1023.30]  restrictions
[1023.30 --> 1024.66]  on that data's use
[1024.66 --> 1026.08]  as it's being generated,
[1026.54 --> 1027.16]  I think is really,
[1027.26 --> 1027.90]  like, I think that
[1027.90 --> 1028.32]  is going to be
[1028.32 --> 1028.80]  the future
[1028.80 --> 1030.48]  of regulation
[1030.48 --> 1031.22]  for data.
[1031.82 --> 1032.26]  Yeah, that's
[1032.26 --> 1033.24]  super interesting.
[1033.24 --> 1034.24]  And I guess
[1034.24 --> 1034.92]  it kind of,
[1034.98 --> 1036.16]  it kind of leads me
[1036.16 --> 1038.28]  into my next question.
[1038.38 --> 1039.10]  I was really trying,
[1039.22 --> 1040.22]  like, while you were talking,
[1040.36 --> 1041.00]  I was thinking
[1041.00 --> 1041.84]  in my own mind,
[1041.92 --> 1043.34]  like, holy crap,
[1043.34 --> 1044.44]  how do I make
[1044.44 --> 1046.58]  my models explainable?
[1046.88 --> 1047.88]  And I don't know
[1047.88 --> 1048.56]  if you've had
[1048.56 --> 1049.30]  the same thought.
[1049.38 --> 1050.10]  It's a realization
[1050.10 --> 1051.00]  I have every once
[1051.00 --> 1051.60]  in a while, Chris.
[1051.96 --> 1052.66]  I don't know
[1052.66 --> 1053.84]  if it's come to you
[1053.84 --> 1054.56]  yet as well,
[1054.58 --> 1055.44]  but I kind of freak out
[1055.44 --> 1055.84]  a little bit
[1055.84 --> 1056.84]  when I think about that.
[1056.84 --> 1058.12]  Um, because I remember,
[1058.42 --> 1059.10]  you know, like,
[1059.46 --> 1060.12]  in my first,
[1060.24 --> 1061.32]  first position,
[1061.52 --> 1061.94]  I, like,
[1062.16 --> 1062.98]  wrote all of these
[1062.98 --> 1063.52]  PowerPoint,
[1064.14 --> 1065.12]  well, it was Google
[1065.12 --> 1065.76]  slides, I guess,
[1065.82 --> 1066.54]  but presentations
[1066.54 --> 1067.28]  on, like,
[1067.54 --> 1068.28]  how my models
[1068.28 --> 1068.76]  were working
[1068.76 --> 1069.70]  and trying to explain
[1069.70 --> 1070.92]  it to just my own team.
[1070.92 --> 1071.60]  And it was, like,
[1071.74 --> 1072.74]  incredibly difficult.
[1072.92 --> 1074.00]  But it sounds like
[1074.00 --> 1074.64]  what you're,
[1075.08 --> 1075.72]  at least partially
[1075.72 --> 1076.40]  what you're saying
[1076.40 --> 1077.78]  in the near term,
[1077.90 --> 1078.92]  a lot of the focus
[1078.92 --> 1079.84]  is going to be
[1079.84 --> 1082.20]  on how your data
[1082.20 --> 1082.82]  was,
[1082.82 --> 1084.20]  was kind of processed
[1084.20 --> 1085.54]  through the pipeline
[1085.54 --> 1086.44]  to what end,
[1086.76 --> 1087.60]  not necessarily,
[1087.92 --> 1088.20]  you know,
[1088.26 --> 1089.26]  explaining a deep
[1089.26 --> 1089.98]  neural network
[1089.98 --> 1091.36]  to, you know,
[1091.64 --> 1093.22]  some, some random person.
[1093.40 --> 1093.78]  Is it,
[1093.78 --> 1094.74]  am I getting the right
[1094.74 --> 1095.30]  sense there
[1095.30 --> 1095.84]  or is that,
[1096.08 --> 1096.66]  or is that wrong?
[1096.92 --> 1097.52]  Well, uh,
[1097.52 --> 1098.44]  sadly, the answer
[1098.44 --> 1099.56]  to both of those questions
[1099.56 --> 1100.52]  is, is yes.
[1101.38 --> 1102.58]  Um, uh,
[1102.58 --> 1103.72]  and, and it's,
[1103.72 --> 1104.74]  it's yes in the sense
[1104.74 --> 1106.14]  that the GDPR is...
[1106.14 --> 1106.92]  You're not making me
[1106.92 --> 1107.78]  sleep any better.
[1107.92 --> 1108.74]  Yeah, no, I'm,
[1108.74 --> 1109.32]  I'm, I'm,
[1109.32 --> 1110.28]  I'm sorry not to be,
[1110.38 --> 1111.34]  uh, uh, uh,
[1111.34 --> 1112.12]  not, not to bring,
[1112.26 --> 1114.12]  uh, uh, easy news.
[1114.30 --> 1115.40]  Um, the GDPR,
[1115.54 --> 1116.94]  has a huge compliance
[1116.94 --> 1117.26]  burden.
[1117.42 --> 1117.90]  There's no,
[1118.04 --> 1118.96]  there's no kind of
[1118.96 --> 1119.90]  sidestepping that.
[1120.38 --> 1121.28]  Data being used
[1121.28 --> 1122.08]  for any purpose,
[1122.12 --> 1122.76]  like that needs
[1122.76 --> 1123.56]  to be documented.
[1124.18 --> 1124.72]  You're not going
[1124.72 --> 1125.38]  to be able to use
[1125.38 --> 1126.64]  EU data, um,
[1126.64 --> 1127.86]  at scale in a,
[1127.86 --> 1128.98]  in a data science shop,
[1128.98 --> 1129.74]  um, without,
[1129.74 --> 1130.42]  you know,
[1130.42 --> 1131.94]  a plan for how
[1131.94 --> 1132.66]  you got the data,
[1132.74 --> 1133.42]  the legal basis
[1133.42 --> 1134.12]  for that data,
[1134.68 --> 1135.44]  you know, uh,
[1135.44 --> 1135.82]  what you're going
[1135.82 --> 1136.50]  to do for it.
[1136.58 --> 1137.96]  At the same time,
[1137.96 --> 1138.88]  there are also
[1138.88 --> 1140.14]  requirements on
[1140.14 --> 1141.68]  the types of models
[1141.68 --> 1142.70]  you use.
[1142.70 --> 1143.86]  Um, or I should
[1143.86 --> 1145.02]  say there are
[1145.02 --> 1146.70]  explainability requirements
[1146.70 --> 1147.64]  surrounding those
[1147.64 --> 1147.92]  models.
[1147.92 --> 1149.36]  So it's not that
[1149.36 --> 1149.94]  you're going to have
[1149.94 --> 1151.08]  to be able to,
[1151.16 --> 1152.00]  you know, uh,
[1152.00 --> 1153.52]  explain the weighting
[1153.52 --> 1154.48]  on every single neuron
[1154.48 --> 1155.22]  in a neural net.
[1155.22 --> 1156.40]  Um, but you are
[1156.40 --> 1157.10]  going to have to be
[1157.10 --> 1157.86]  able to say,
[1157.86 --> 1160.36]  here is in general,
[1160.36 --> 1161.86]  um, how the model
[1161.86 --> 1162.40]  is working.
[1162.40 --> 1163.00]  Here's where it's
[1163.00 --> 1163.90]  getting data from.
[1164.24 --> 1165.88]  Here is, you know,
[1165.90 --> 1166.72]  here are the reasons
[1166.72 --> 1167.96]  why it's being used.
[1167.96 --> 1170.66]  Um, so, uh, uh, uh,
[1170.66 --> 1171.36]  it's, it's not the
[1171.36 --> 1172.46]  type of explainability
[1172.46 --> 1173.18]  I think that might
[1173.18 --> 1174.18]  have you, you know,
[1174.22 --> 1174.84]  waking up in the
[1174.84 --> 1175.32]  middle of the night
[1175.32 --> 1176.06]  in a cold sweat.
[1176.54 --> 1178.04]  Um, but, but still,
[1178.04 --> 1179.10]  uh, you're going to
[1179.10 --> 1179.84]  have to be able to
[1179.84 --> 1181.50]  provide very basic
[1181.50 --> 1183.36]  information about, uh,
[1183.36 --> 1184.14]  about the models
[1184.14 --> 1184.82]  that you're using.
[1185.12 --> 1185.56]  Yeah.
[1185.62 --> 1186.68]  And I, I, I think
[1186.68 --> 1187.76]  the reason that there
[1187.76 --> 1188.92]  you are, are concerned
[1188.92 --> 1189.96]  is, is that there's
[1189.96 --> 1190.88]  really no frameworks
[1190.88 --> 1191.76]  to automate this.
[1191.94 --> 1193.44]  Um, so there's this
[1193.44 --> 1194.90]  now massive legal burden
[1194.90 --> 1196.08]  on the data scientist
[1196.08 --> 1197.38]  who is typically
[1197.38 --> 1199.18]  not a lawyer to
[1199.18 --> 1201.30]  expound on, you know,
[1201.30 --> 1201.86]  why they made
[1201.86 --> 1202.52]  certain decisions,
[1202.72 --> 1203.74]  what data was used,
[1203.84 --> 1204.88]  who potentially was
[1204.88 --> 1206.32]  in that data, uh,
[1206.32 --> 1207.26]  for what purpose.
[1207.64 --> 1208.98]  Um, and so it's,
[1208.98 --> 1209.80]  it's not just about
[1209.80 --> 1211.00]  data provenance any
[1211.00 --> 1212.34]  longer, um, but it's
[1212.34 --> 1214.72]  also, uh, what types
[1214.72 --> 1216.24]  of activities were
[1216.24 --> 1217.50]  taken to ensure that
[1217.50 --> 1218.70]  there was proper
[1218.70 --> 1220.68]  ethical, um, curation
[1220.68 --> 1221.70]  of the data itself
[1221.70 --> 1223.20]  before the model is
[1223.20 --> 1223.82]  being trained.
[1224.12 --> 1225.60]  And then it's, what
[1225.60 --> 1226.50]  are the guardrails
[1226.50 --> 1227.50]  put in place to
[1227.50 --> 1228.18]  ensure that you're
[1228.18 --> 1229.04]  controlling the model
[1229.04 --> 1229.68]  as it's put into
[1229.68 --> 1230.08]  production?
[1230.82 --> 1231.80]  Um, and these are
[1231.80 --> 1232.68]  things that, you
[1232.68 --> 1234.26]  know, historically,
[1234.26 --> 1235.90]  uh, we've had
[1235.90 --> 1236.88]  guardrails in place
[1236.88 --> 1237.66]  through software,
[1237.66 --> 1238.08]  right?
[1238.14 --> 1239.04]  Through SAS, they've
[1239.04 --> 1239.64]  always had these
[1239.64 --> 1240.64]  guardrails in place
[1240.64 --> 1242.08]  and, you know, other,
[1242.08 --> 1243.42]  uh, types of software
[1243.42 --> 1244.46]  kind of automated a
[1244.46 --> 1245.52]  lot of these controls.
[1245.78 --> 1247.14]  And now the problem
[1247.14 --> 1248.14]  is, is that the
[1248.14 --> 1249.34]  ability for anyone
[1249.34 --> 1250.42]  to be a data scientist
[1250.42 --> 1251.34]  and use the data
[1251.34 --> 1253.06]  and, um, use open
[1253.06 --> 1254.58]  source tools, um, they
[1254.58 --> 1255.54]  just don't carry the
[1255.54 --> 1256.64]  rigor that's required.
[1256.64 --> 1258.04]  And I think that it's
[1258.04 --> 1259.84]  not just the GDPR, but
[1259.84 --> 1260.72]  we're seeing now, even
[1260.72 --> 1262.00]  in the U S California
[1262.00 --> 1263.28]  is looking at enacting
[1263.28 --> 1264.36]  legislation around data
[1264.36 --> 1264.80]  privacy.
[1265.10 --> 1266.22]  This is something people
[1266.22 --> 1268.00]  care about because what
[1268.00 --> 1269.60]  they're afraid of is, um,
[1269.60 --> 1270.78]  the open source community
[1270.78 --> 1272.18]  in large organizations
[1272.18 --> 1273.60]  like Google and, you
[1273.60 --> 1274.68]  know, Microsoft and
[1274.68 --> 1276.46]  Apple are making it
[1276.46 --> 1277.52]  easier and easier for
[1277.52 --> 1278.56]  anyone to be able to
[1278.56 --> 1279.40]  design these models
[1279.40 --> 1279.84]  because they're
[1279.84 --> 1281.24]  incentivized to buy up
[1281.24 --> 1282.24]  small little AI
[1282.24 --> 1282.76]  companies.
[1282.76 --> 1284.36]  And so we need to
[1284.36 --> 1285.48]  put rigor into these,
[1285.60 --> 1287.26]  um, into guardrails
[1287.26 --> 1288.22]  around these, these
[1288.22 --> 1289.00]  pieces of software.
[1289.00 --> 1291.06]  And so it's tough and
[1291.06 --> 1292.30]  it's hard and people
[1292.30 --> 1293.20]  aren't educated around
[1293.20 --> 1293.58]  the law.
[1293.62 --> 1295.04]  So that's what makes it
[1295.04 --> 1295.60]  even scarier.
[1295.86 --> 1296.30]  Yeah.
[1296.36 --> 1297.68]  And I, I think that
[1297.68 --> 1298.66]  like one of the things
[1298.66 --> 1299.66]  I'm hearing from, from
[1299.66 --> 1300.54]  you, Matt, and also
[1300.54 --> 1302.14]  in your kind of, when
[1302.14 --> 1302.72]  you're talking about
[1302.72 --> 1303.24]  what you're trying to
[1303.24 --> 1303.86]  accomplish with a
[1303.86 --> 1304.76]  Muta, I mean, this,
[1304.86 --> 1306.34]  this spans a lot of
[1306.34 --> 1307.38]  different areas, right?
[1307.38 --> 1308.48]  All the way from data
[1308.48 --> 1310.66]  curation to training of
[1310.66 --> 1312.32]  models to deploying of
[1312.32 --> 1313.20]  models to building
[1313.20 --> 1314.76]  APIs in which models
[1314.76 --> 1316.68]  are, are deployed and,
[1316.68 --> 1318.22]  and with which they
[1318.22 --> 1318.86]  interact.
[1318.94 --> 1319.78]  There's a lot of
[1319.78 --> 1321.38]  different, um, kind of
[1321.38 --> 1323.38]  teams involved in this,
[1323.60 --> 1324.60]  in this whole process,
[1324.66 --> 1324.86]  right?
[1325.72 --> 1325.94]  Yeah.
[1326.10 --> 1327.58]  And, um, the, the
[1327.58 --> 1328.62]  challenges is that
[1328.62 --> 1330.28]  they're traditionally, if
[1330.28 --> 1331.30]  you, if you look at
[1331.30 --> 1331.92]  most of these
[1331.92 --> 1332.92]  organizations, because
[1332.92 --> 1334.08]  mostly global 2000
[1334.08 --> 1335.26]  organizations that are
[1335.26 --> 1336.20]  really trying to
[1336.20 --> 1336.98]  accomplish this at
[1336.98 --> 1338.20]  scale, it's these
[1338.20 --> 1338.92]  teams aren't sitting
[1338.92 --> 1339.62]  next to each other,
[1339.62 --> 1340.50]  right?
[1340.50 --> 1341.64]  So they don't have
[1341.64 --> 1342.86]  the benefit of, through
[1342.86 --> 1344.58]  osmosis, the, to, to
[1344.58 --> 1345.74]  coordinate effects,
[1345.84 --> 1346.08]  right?
[1346.46 --> 1347.38]  A lot of them are
[1347.38 --> 1348.96]  operating on, you
[1348.96 --> 1349.74]  know, five to ten
[1349.74 --> 1350.68]  projects because there's
[1350.68 --> 1351.28]  not enough data
[1351.28 --> 1351.82]  scientists.
[1352.16 --> 1353.16]  There's definitely not
[1353.16 --> 1354.04]  enough counsel that's
[1354.04 --> 1355.28]  caught up in, in the
[1355.28 --> 1355.60]  space.
[1355.60 --> 1356.40]  So they're trying to
[1356.40 --> 1358.00]  get smart on, you
[1358.00 --> 1359.16]  know, how does each
[1359.16 --> 1360.02]  project function?
[1360.16 --> 1360.78]  What are they trying to
[1360.78 --> 1361.60]  build and why?
[1362.28 --> 1363.12]  Um, so it's all very
[1363.12 --> 1364.04]  slow and cumbersome.
[1364.24 --> 1365.32]  And the worst part about
[1365.32 --> 1366.92]  it all is, I think a
[1366.92 --> 1368.08]  worst case scenario is,
[1368.54 --> 1370.48]  you know, you build the
[1370.48 --> 1371.94]  most fantastic algorithm
[1371.94 --> 1374.32]  that can really change
[1374.32 --> 1375.10]  the way a legacy
[1375.10 --> 1376.12]  business is operating,
[1376.30 --> 1376.58]  right?
[1376.64 --> 1377.36]  Like, that's the whole
[1377.36 --> 1378.88]  point of this, is we
[1378.88 --> 1380.26]  can do things better and
[1380.26 --> 1380.72]  faster.
[1380.94 --> 1381.96]  And then the whole thing
[1381.96 --> 1382.76]  has to be brought down
[1382.76 --> 1383.64]  because they have no
[1383.64 --> 1384.62]  insight into how it's
[1384.62 --> 1384.92]  working.
[1385.16 --> 1386.52]  And the whole business is
[1386.52 --> 1387.52]  then crippled by this.
[1387.52 --> 1388.74]  And so that they don't
[1388.74 --> 1389.46]  want to make the
[1389.46 --> 1390.52]  investment in these
[1390.52 --> 1391.46]  advanced technologies
[1391.46 --> 1392.96]  and, um, because they
[1392.96 --> 1393.90]  don't have the legal
[1393.90 --> 1395.32]  understanding or the
[1395.32 --> 1396.84]  internal engineering to
[1396.84 --> 1398.38]  be able to do this, um,
[1398.48 --> 1399.50]  in an ethical manner.
[1399.84 --> 1400.88]  And that's the fear
[1400.88 --> 1401.30]  right now.
[1401.32 --> 1401.96]  And that's what, that's
[1401.96 --> 1403.04]  what the GDPR is for,
[1403.10 --> 1404.22]  I think, is I don't
[1404.22 --> 1405.12]  think they want to come
[1405.12 --> 1406.42]  around and, and, you
[1406.42 --> 1408.24]  know, destroy business.
[1408.24 --> 1409.22]  But I do think what they
[1409.22 --> 1410.92]  want to say is, listen,
[1411.02 --> 1412.02]  there's an ethical way
[1412.02 --> 1413.06]  and there's, just like any
[1413.06 --> 1414.40]  engineering process, there's
[1414.40 --> 1415.92]  got to be a governance
[1415.92 --> 1417.00]  end of it as well.
[1417.30 --> 1419.14]  Um, so, you know, Hey,
[1419.20 --> 1420.20]  global 2000, if you're
[1420.20 --> 1421.44]  going to use EU data, this
[1421.44 --> 1422.28]  is how you're going to
[1422.28 --> 1422.70]  do it.
[1423.28 --> 1424.30]  Well, I'll tell you what
[1424.30 --> 1425.14]  you guys have, have
[1425.14 --> 1426.16]  really had an impact on
[1426.16 --> 1426.92]  me in this podcast
[1426.92 --> 1427.46]  already.
[1427.46 --> 1428.48]  I started off the show
[1428.48 --> 1429.60]  saying, Hey, I'm excited
[1429.60 --> 1430.60]  about GDPR.
[1430.70 --> 1431.86]  And I think part of that
[1431.86 --> 1433.46]  is as a, as just a
[1433.46 --> 1434.44]  consumer out there and,
[1434.60 --> 1435.20]  you know, using many
[1435.20 --> 1436.90]  services, I am conscious
[1436.90 --> 1438.16]  of privacy, but when you,
[1438.60 --> 1440.34]  as you've educated us on,
[1440.46 --> 1442.40]  on just how, uh, what the
[1442.40 --> 1443.56]  burden really is that
[1443.56 --> 1444.22]  we're going to all be
[1444.22 --> 1445.12]  thinking about and the,
[1445.18 --> 1446.26]  and the lack of tools to
[1446.26 --> 1447.50]  do that a little bit
[1447.50 --> 1447.72]  worried.
[1447.78 --> 1448.60]  I was wondering, would
[1448.60 --> 1449.72]  you mind delving into
[1449.72 --> 1450.80]  some of the maybe
[1450.80 --> 1452.28]  specific industries where
[1452.28 --> 1453.82]  you see a impact in
[1453.82 --> 1454.74]  maybe healthcare or
[1454.74 --> 1455.90]  transportation or others
[1455.90 --> 1457.58]  where you think, uh,
[1457.58 --> 1458.08]  that they're going to
[1458.08 --> 1459.58]  have very specific, uh,
[1459.58 --> 1460.44]  problems to contend
[1460.44 --> 1460.64]  with?
[1461.42 --> 1461.82]  Yeah.
[1461.90 --> 1463.62]  So happily, Matt, do
[1463.62 --> 1464.54]  you want to, is there
[1464.54 --> 1465.32]  any part of that question
[1465.32 --> 1465.82]  you want to take?
[1466.10 --> 1466.38]  Go ahead.
[1467.04 --> 1467.40]  Okay.
[1467.82 --> 1469.14]  Um, so I think, I
[1469.14 --> 1470.32]  mean, so to start with,
[1470.34 --> 1471.10]  I think one of the most
[1471.10 --> 1473.20]  fascinating, um, uh,
[1473.20 --> 1474.44]  things about being a
[1474.44 --> 1476.12]  data scientist is that
[1476.12 --> 1477.58]  the work that you do can
[1477.58 --> 1478.50]  apply to so many
[1478.50 --> 1480.30]  different industries and
[1480.30 --> 1481.78]  the same techniques can
[1481.78 --> 1482.84]  be incredibly powerful
[1482.84 --> 1484.00]  across healthcare or
[1484.00 --> 1484.50]  finance.
[1484.50 --> 1487.04]  So I think GDPR in
[1487.04 --> 1488.76]  general, I think is, is
[1488.76 --> 1490.48]  meant to be as broad and
[1490.48 --> 1491.34]  as far reaching as
[1491.34 --> 1491.86]  possible.
[1491.86 --> 1492.88]  So if you are an
[1492.88 --> 1494.56]  organization that really
[1494.56 --> 1495.68]  cares about data and is
[1495.68 --> 1497.56]  using data, the GDPR
[1497.56 --> 1498.42]  applies, you know,
[1498.48 --> 1499.28]  directly to you.
[1499.28 --> 1500.78]  I think what we are
[1500.78 --> 1502.34]  seeing from, you know,
[1502.38 --> 1503.78]  the, the, the global
[1503.78 --> 1505.54]  2000 perspective is I
[1505.54 --> 1506.64]  think healthcare and
[1506.64 --> 1508.42]  life sciences, finance,
[1508.86 --> 1509.60]  transportation in
[1509.60 --> 1511.06]  particular, I think all
[1511.06 --> 1512.46]  of those groups, uh, and
[1512.46 --> 1513.82]  then, and then obviously
[1513.82 --> 1515.54]  advertising and marketing
[1515.54 --> 1517.04]  organizations, I think
[1517.04 --> 1517.98]  those groups are the
[1517.98 --> 1520.74]  first to, um, uh, really
[1520.74 --> 1522.46]  get, uh, kind of get hit
[1522.46 --> 1523.86]  by the GDPR or, or to
[1523.86 --> 1525.00]  take it seriously.
[1525.46 --> 1526.70]  But I mean, I think the
[1526.70 --> 1528.04]  bottom line with the GDPR
[1528.04 --> 1529.26]  is unlike in the U S
[1529.26 --> 1530.58]  where we try to do
[1530.58 --> 1531.42]  sector specific
[1531.42 --> 1532.60]  regulation, where, you
[1532.60 --> 1533.86]  know, we have an FDA
[1533.86 --> 1534.86]  and the FDA only
[1534.86 --> 1535.76]  regulates, you know,
[1535.98 --> 1536.98]  specific drugs and
[1536.98 --> 1537.44]  products.
[1537.88 --> 1539.04]  Um, this is really meant
[1539.04 --> 1539.90]  to touch everyone.
[1540.22 --> 1540.26]  Yeah.
[1540.32 --> 1541.46]  And I, I, I, to
[1541.46 --> 1542.56]  expound on that, I
[1542.56 --> 1543.98]  think the, the point of
[1543.98 --> 1545.36]  the GDPR, again, it's,
[1545.40 --> 1546.96]  it's not designed to be
[1546.96 --> 1549.24]  punitive to business
[1549.24 --> 1550.12]  generally, right?
[1550.16 --> 1551.06]  I mean, we want the
[1551.06 --> 1552.36]  global economy to scale
[1552.36 --> 1553.32]  and it's, it's all in,
[1553.40 --> 1554.12]  it's in our best
[1554.12 --> 1554.84]  interest for that to
[1554.84 --> 1555.08]  occur.
[1555.28 --> 1557.12]  I think that the focus
[1557.12 --> 1558.66]  though is they want
[1558.66 --> 1559.80]  to put teeth around
[1559.80 --> 1560.74]  a regulation, hence
[1560.74 --> 1561.90]  the, you know, 4% of
[1561.90 --> 1562.80]  your annual revenue
[1562.80 --> 1564.62]  or 20 million, uh,
[1564.62 --> 1565.38]  euros, whatever's
[1565.38 --> 1567.44]  larger is that they
[1567.44 --> 1568.32]  want to show people,
[1568.40 --> 1569.82]  listen, there is a
[1569.82 --> 1571.42]  massive slippery slope,
[1571.42 --> 1573.16]  you know, when we start
[1573.16 --> 1575.00]  to use people's data at
[1575.00 --> 1575.34]  scale.
[1575.60 --> 1576.98]  And I think that there's
[1576.98 --> 1578.02]  a couple of core pieces
[1578.02 --> 1579.12]  to this is one is we've
[1579.12 --> 1580.14]  never had so many people
[1580.14 --> 1581.68]  in the world that are
[1581.68 --> 1582.66]  producing data than
[1582.66 --> 1583.20]  ever before.
[1583.20 --> 1584.58]  It's only going to
[1584.58 --> 1586.18]  increase as we, as
[1586.18 --> 1587.32]  internet proliferates
[1587.32 --> 1588.50]  and 5G proliferates
[1588.50 --> 1589.18]  throughout the world.
[1589.18 --> 1590.44]  And so I think, you
[1590.44 --> 1591.90]  know, the goal here is
[1591.90 --> 1594.38]  this is a time in
[1594.38 --> 1595.62]  humanity where we can
[1595.62 --> 1597.10]  say, listen, we've got
[1597.10 --> 1598.48]  to put controls around
[1598.48 --> 1599.82]  this, um, because
[1599.82 --> 1601.28]  every industry is going
[1601.28 --> 1601.98]  to be impacted.
[1602.22 --> 1603.62]  Everyone wants to build
[1603.62 --> 1604.18]  algorithms.
[1604.90 --> 1605.58]  Everyone wants to
[1605.58 --> 1607.18]  operate faster and
[1607.18 --> 1608.98]  humans yearn for
[1608.98 --> 1610.56]  instantaneous gratification
[1610.56 --> 1612.08]  of all their apps.
[1612.08 --> 1613.96]  I mean, voice is the
[1613.96 --> 1615.12]  new cool thing, right?
[1615.28 --> 1617.10]  Like, very few people
[1617.10 --> 1618.78]  are now wanting to
[1618.78 --> 1620.30]  type in their search.
[1620.56 --> 1621.70]  They just, you know,
[1621.72 --> 1622.78]  use their assistant on
[1622.78 --> 1623.62]  their phone, right?
[1624.06 --> 1625.28]  And so there's all these
[1625.28 --> 1626.48]  personal items that are
[1626.48 --> 1627.42]  being introduced to
[1627.42 --> 1628.76]  physical devices and
[1628.76 --> 1629.70]  there's algorithms behind
[1629.70 --> 1631.24]  them and no one really
[1631.24 --> 1632.48]  knows how or why it's
[1632.48 --> 1633.08]  being used.
[1633.16 --> 1634.14]  And I think that's like
[1634.14 --> 1635.98]  generally the concern is
[1635.98 --> 1637.02]  that's every industry,
[1637.22 --> 1638.28]  it's every business in the
[1638.28 --> 1640.10]  world, small, mid to
[1640.10 --> 1640.88]  large businesses.
[1640.88 --> 1642.02]  But I think the global
[1642.02 --> 1642.96]  2000 are going to be
[1642.96 --> 1644.24]  impacted the most because,
[1645.16 --> 1645.94]  well, let's just be
[1645.94 --> 1646.22]  candid.
[1646.42 --> 1647.12]  They have the most to
[1647.12 --> 1648.22]  lose and the data
[1648.22 --> 1649.48]  scientists in those
[1649.48 --> 1650.98]  organizations are now
[1650.98 --> 1651.92]  carrying the largest
[1651.92 --> 1652.58]  amount of risk.
[1653.28 --> 1654.60]  Yeah, uh, no, that,
[1654.74 --> 1655.78]  that, that makes, that
[1655.78 --> 1656.62]  makes total sense.
[1656.70 --> 1658.88]  I, I think, um, I, I
[1658.88 --> 1659.84]  definitely, as Chris
[1659.84 --> 1660.98]  has, has mentioned, I've
[1660.98 --> 1662.68]  appreciated like the, uh,
[1662.70 --> 1663.52]  kind of the, the
[1663.52 --> 1664.80]  candor and the, the
[1664.80 --> 1665.80]  insight that, that
[1665.80 --> 1666.86]  we're getting kind of in,
[1666.96 --> 1668.80]  in the trends that,
[1668.94 --> 1670.06]  that you guys have been,
[1670.06 --> 1670.96]  been following and
[1670.96 --> 1671.78]  examining.
[1671.78 --> 1674.42]  I think as a data
[1674.42 --> 1676.64]  scientist or AI, ML
[1676.64 --> 1677.84]  engineer, or whatever I,
[1678.08 --> 1679.56]  whatever I am, um, what
[1679.56 --> 1680.78]  I'm thinking is, you
[1680.78 --> 1683.44]  know, as, as me or as
[1683.44 --> 1684.96]  Chris, who's, who's a
[1684.96 --> 1687.20]  chief scientist or as a
[1687.20 --> 1689.32]  software developer of, of
[1689.32 --> 1691.54]  AI apps, what are kind of
[1691.54 --> 1693.28]  some practicalities as far
[1693.28 --> 1695.22]  as, okay, we, we get that
[1695.22 --> 1696.18]  this is a big deal.
[1696.34 --> 1697.40]  Give us some good news.
[1697.40 --> 1698.28]  What, what can we do?
[1698.34 --> 1699.58]  What can, what are some
[1699.58 --> 1700.74]  kind of like initial
[1700.74 --> 1702.28]  practical steps that would
[1702.28 --> 1703.80]  help us kind of move in
[1703.80 --> 1705.80]  the right direction of, you
[1705.80 --> 1707.20]  know, being responsible and
[1707.20 --> 1708.28]  how we deal with people's
[1708.28 --> 1709.50]  data, even if we're not in
[1709.50 --> 1710.50]  the, even if we're not in
[1710.50 --> 1712.12]  the EU, um, what are kind
[1712.12 --> 1713.56]  of some, some first steps
[1713.56 --> 1714.28]  that we can take?
[1714.62 --> 1716.34]  Well, Andrew, go ahead.
[1716.34 --> 1717.62]  I think, yeah, go ahead.
[1717.76 --> 1719.78]  And, uh, I think one of the
[1719.78 --> 1721.20]  big steps here is, is
[1721.20 --> 1721.80]  probably best.
[1722.24 --> 1722.44]  Yeah.
[1722.44 --> 1725.26]  So happily, um, so I
[1725.26 --> 1726.52]  think one of the biggest
[1726.52 --> 1729.30]  takeaways is that, um, what
[1729.30 --> 1730.44]  makes for good governance
[1730.44 --> 1731.80]  actually makes for good
[1731.80 --> 1732.78]  data science.
[1733.14 --> 1736.70]  Um, so, uh, so, so
[1736.70 --> 1738.20]  basically good governance,
[1738.20 --> 1740.14]  um, I think translates into
[1740.14 --> 1742.38]  good data science and, and
[1742.38 --> 1743.54]  the reason is that's great
[1743.54 --> 1743.96]  to hear.
[1744.04 --> 1744.72]  Yeah, exactly.
[1744.78 --> 1744.92]  Yeah.
[1744.92 --> 1745.68]  So it should be, I think
[1745.68 --> 1746.94]  reassuring in the long run.
[1746.94 --> 1749.06]  Um, um, I think a good way
[1749.06 --> 1750.06]  to think about the, the
[1750.06 --> 1751.92]  GDPR is a little bit of a
[1751.92 --> 1753.34]  paradigm shift, which is
[1753.34 --> 1754.32]  right now, a lot of data
[1754.32 --> 1756.62]  scientists end up operating
[1756.62 --> 1757.50]  in a little bit of a
[1757.50 --> 1759.98]  vacuum where they say, um,
[1759.98 --> 1761.00]  kind of, here's a project,
[1761.10 --> 1762.30]  give me the data and then
[1762.30 --> 1763.58]  I'll get back to you and
[1763.58 --> 1764.48]  I'll tell, you know, I'll
[1764.48 --> 1765.38]  play around with it and I'll
[1765.38 --> 1766.38]  tell you what we can do.
[1766.80 --> 1769.14]  Um, and that is good and
[1769.14 --> 1770.82]  kind of one-off interactions.
[1771.28 --> 1773.44]  Um, it just does not scale.
[1773.44 --> 1776.04]  And so the ways to...
[1776.04 --> 1776.76]  Yeah, you've, you've
[1776.76 --> 1778.38]  summarized well so many
[1778.38 --> 1780.38]  years of my life in which,
[1780.44 --> 1784.16]  uh, I used to, I used to
[1784.16 --> 1785.26]  frequently refer to myself
[1785.26 --> 1786.56]  as the data monkey rather
[1786.56 --> 1787.56]  than a data scientist.
[1787.74 --> 1789.08]  Cause I, I felt like that
[1789.08 --> 1789.92]  was more appropriate.
[1790.04 --> 1792.02]  Um, cause I, cause of the
[1792.02 --> 1792.70]  way I operated.
[1792.82 --> 1793.14]  Yeah.
[1793.14 --> 1794.16]  Cause you're just kind of
[1794.16 --> 1795.40]  bouncing around and
[1795.40 --> 1797.12]  climbing things and, um,
[1797.42 --> 1798.08]  you know, the view looks
[1798.08 --> 1798.78]  good from here.
[1799.04 --> 1799.36]  Yeah.
[1799.46 --> 1800.04]  Climb a different view.
[1800.04 --> 1800.08]  Yeah.
[1800.20 --> 1801.76]  No, no flinging of poo.
[1801.76 --> 1803.88]  Um, so that was good, but,
[1804.02 --> 1805.52]  uh, but in other ways,
[1805.56 --> 1805.80]  yes.
[1805.80 --> 1806.94]  I was gonna, I was gonna
[1806.94 --> 1808.98]  ask, but, um, uh, thank,
[1809.10 --> 1810.14]  thank you for clarifying.
[1810.30 --> 1812.84]  Um, so I guess the, the
[1812.84 --> 1813.92]  really big takeaway is that
[1813.92 --> 1815.86]  if you're gonna do data
[1815.86 --> 1817.30]  science at scale and you're
[1817.30 --> 1818.58]  gonna run a program, you
[1818.58 --> 1819.88]  need to really have a sense
[1819.88 --> 1822.24]  of what data is available.
[1822.76 --> 1824.62]  How do I get access to that,
[1824.62 --> 1826.20]  that data as a data scientist,
[1826.20 --> 1827.96]  you need to have some way of
[1827.96 --> 1829.44]  documenting what it is you
[1829.44 --> 1830.64]  want to do with it and what
[1830.64 --> 1831.76]  you've done with it.
[1831.84 --> 1833.36]  If someone else gets added to
[1833.36 --> 1834.80]  the project or if you leave,
[1834.80 --> 1836.28]  these are just like kind of
[1836.28 --> 1838.58]  basic organizational measures
[1838.58 --> 1840.68]  to make sure that you can
[1840.68 --> 1841.84]  collaborate and that the
[1841.84 --> 1842.94]  documentation is there.
[1843.06 --> 1845.18]  And so if you split that up,
[1845.36 --> 1846.98]  what that really looks like is
[1846.98 --> 1848.86]  as soon as a project begins,
[1848.86 --> 1850.22]  understanding kind of key
[1850.22 --> 1851.30]  objectives that you want to
[1851.30 --> 1852.96]  achieve, key objectives that
[1852.96 --> 1853.72]  you want to avoid.
[1853.96 --> 1855.76]  Another way of stating that is
[1855.76 --> 1856.60]  legal liability.
[1857.04 --> 1858.10]  Um, and so that's where lawyers
[1858.10 --> 1859.22]  can come in and say,
[1859.22 --> 1861.10]  make sure you don't do this
[1861.10 --> 1862.96]  or if you do this, make sure,
[1862.96 --> 1864.06]  you know, you're going to
[1864.06 --> 1865.30]  mitigate it in some way.
[1865.38 --> 1866.78]  So that ends up being really
[1866.78 --> 1868.08]  important and then documenting
[1868.08 --> 1870.12]  it so people can be added and
[1870.12 --> 1871.48]  subtracted from that project.
[1871.48 --> 1873.32]  And then there's very specific
[1873.32 --> 1876.56]  ways that you can examine the
[1876.56 --> 1877.88]  data you're going to use and
[1877.88 --> 1879.42]  control and map, map use the
[1879.42 --> 1880.24]  word guardrails.
[1880.24 --> 1881.84]  And so kind of setting up some
[1881.84 --> 1883.38]  guardrails to think about
[1883.38 --> 1885.58]  potential biases embedded in the
[1885.58 --> 1887.78]  data, things you can do to try
[1887.78 --> 1889.00]  to compensate for it.
[1889.06 --> 1890.70]  And as we all know, you know,
[1891.02 --> 1892.30]  all data sets are biased.
[1892.44 --> 1895.26]  So the question is really just
[1895.26 --> 1897.50]  trying to prioritize what, what
[1897.50 --> 1898.42]  it is that you're trying to
[1898.42 --> 1898.82]  avoid.
[1899.30 --> 1901.16]  Um, so I could go on here for a
[1901.16 --> 1901.46]  while.
[1901.62 --> 1903.52]  Um, I think I mentioned to both
[1903.52 --> 1904.42]  of you before we started
[1904.42 --> 1905.94]  recording that a mute is going to
[1905.94 --> 1907.52]  be releasing a white paper with
[1907.52 --> 1908.54]  an organization called the
[1908.54 --> 1909.76]  future of privacy forum.
[1909.76 --> 1911.74]  And it's literally going to be a
[1911.74 --> 1913.52]  white paper designed to be a
[1913.52 --> 1915.08]  practical guide for managing
[1915.08 --> 1916.86]  risk and deploying machine
[1916.86 --> 1917.58]  learning models.
[1917.58 --> 1918.82]  And so it's meant to speak to
[1918.82 --> 1920.78]  both data scientists and lawyers,
[1920.78 --> 1922.60]  um, and to, to give some real
[1922.60 --> 1924.40]  kind of depth to some of these
[1924.40 --> 1925.02]  suggestions.
[1925.76 --> 1926.56]  And we'll, we'll definitely
[1926.56 --> 1927.74]  include that in the show notes
[1927.74 --> 1929.16]  so that, uh, as it's, as it
[1929.16 --> 1930.64]  becomes available, listeners are
[1930.64 --> 1931.86]  able to, to find it easily.
[1932.46 --> 1934.94]  Um, to deep dive into there, I
[1934.94 --> 1936.70]  think, as Andrew said, you know,
[1936.82 --> 1938.54]  um, good governance, you know,
[1938.54 --> 1939.98]  leads to good data science and
[1939.98 --> 1940.96]  they kind of go hand in hand.
[1940.96 --> 1942.32]  I think, I think the first thing
[1942.32 --> 1943.40]  is, is, you know, this is one of
[1943.40 --> 1944.20]  the things I learned in the
[1944.20 --> 1945.64]  government is, is lawyers are
[1945.64 --> 1946.70]  actually there to help you.
[1947.36 --> 1949.12]  Um, they're not there to slow you
[1949.12 --> 1949.38]  down.
[1949.48 --> 1950.68]  And I think in a lot of these,
[1950.74 --> 1951.66]  especially if you're a data
[1951.66 --> 1952.82]  scientist, that's working in a
[1952.82 --> 1954.82]  big organization, starting to
[1954.82 --> 1956.34]  align yourself into the
[1956.34 --> 1957.46]  governance organization and
[1957.46 --> 1959.20]  asking for support early and
[1959.20 --> 1961.12]  often is, is really key.
[1961.80 --> 1962.84]  Understanding that, you know,
[1962.84 --> 1964.74]  most large organizations have
[1964.74 --> 1967.38]  gone through a, some sort of
[1967.38 --> 1969.44]  semantic context around their
[1969.44 --> 1970.08]  data, right?
[1970.12 --> 1971.30]  They know what better data they
[1971.30 --> 1973.00]  have and generally where it is
[1973.00 --> 1974.58]  and what are the rules around
[1974.58 --> 1976.00]  that and starting to understand
[1976.00 --> 1977.14]  risk levels, right?
[1977.62 --> 1979.04]  And so bring those people in
[1979.04 --> 1980.38]  and working in your programs,
[1980.56 --> 1982.38]  it seems so simple, but yet
[1982.38 --> 1984.26]  when we talk to clients, this is
[1984.26 --> 1985.50]  not occurring, right?
[1985.54 --> 1987.96]  It's on a one-off kind of
[1987.96 --> 1990.16]  relationship where every so often
[1990.16 --> 1990.38]  they ask.
[1990.38 --> 1991.46]  Yeah, I've never seen that.
[1991.88 --> 1993.16]  Yeah, and it's unfortunate
[1993.16 --> 1994.42]  because, you know, the thing is
[1994.42 --> 1995.04]  that I learned in the
[1995.04 --> 1996.82]  government is, is they will
[1996.82 --> 2000.40]  very, very easily relieve a lot
[2000.40 --> 2001.92]  of risk off of you, right?
[2002.78 --> 2004.50]  And then you can start looking
[2004.50 --> 2005.68]  at it differently, right?
[2005.82 --> 2006.98]  It's the risk isn't on you.
[2007.08 --> 2008.66]  You've now brought in others to
[2008.66 --> 2009.58]  where you've gone to counsel,
[2009.68 --> 2011.44]  you've gotten review, and you
[2011.44 --> 2012.40]  can start looking at that.
[2012.44 --> 2013.08]  And it doesn't need to be
[2013.08 --> 2013.96]  technical, right?
[2014.12 --> 2014.90]  A lot of times it's just like,
[2014.94 --> 2016.06]  hey, I'm using this data, I'm
[2016.06 --> 2017.10]  using this data, I'm using this
[2017.10 --> 2017.72]  data, and I'm bringing it
[2017.72 --> 2018.04]  together.
[2018.54 --> 2019.50]  You know, where do you think my
[2019.50 --> 2020.36]  potential risk is?
[2020.38 --> 2022.28]  Are there any regulations
[2022.28 --> 2023.94]  where, you know, maybe it's not
[2023.94 --> 2025.36]  PI, but this is considered
[2025.36 --> 2026.52]  sensitive data or not?
[2026.92 --> 2029.10]  Should we be doing masking on
[2029.10 --> 2030.20]  this data or not?
[2030.42 --> 2032.06]  You know, and sometimes just the
[2032.06 --> 2033.92]  general rules change when you
[2033.92 --> 2035.36]  start bringing data together,
[2035.54 --> 2036.62]  right, and mashing it up.
[2036.78 --> 2037.90]  And so I think early and often
[2037.90 --> 2039.24]  bringing governance in and having
[2039.24 --> 2040.86]  a good working relationship,
[2041.24 --> 2042.72]  potentially even creating a
[2042.72 --> 2044.74]  working group to where you
[2044.74 --> 2045.92]  review different types of
[2045.92 --> 2047.22]  projects and potential risks as
[2047.22 --> 2048.38]  part of your development cycle.
[2048.38 --> 2049.96]  That's a fantastic idea.
[2050.44 --> 2052.24]  Yeah, and I think once you get
[2052.24 --> 2053.34]  to that point, then the second
[2053.34 --> 2055.32]  thing is it really comes down to
[2055.32 --> 2057.78]  what kind of data are you using?
[2057.90 --> 2060.00]  I think a lot of times we just
[2060.00 --> 2061.84]  tend to copy all data and then
[2061.84 --> 2063.00]  figure out what data we want to
[2063.00 --> 2063.92]  use, right?
[2063.96 --> 2066.96]  We figure out, like, how we want
[2066.96 --> 2068.42]  to analyze a problem and look at,
[2068.52 --> 2069.52]  then look at a bunch of data
[2069.52 --> 2070.46]  sets and bring it in.
[2070.46 --> 2073.28]  And I think at times we could do
[2073.28 --> 2075.70]  a much better job data engineering
[2075.70 --> 2077.20]  in the sense of planning it out
[2077.20 --> 2080.42]  and looking at it in a
[2080.42 --> 2081.50]  generalistic pattern.
[2081.62 --> 2084.52]  Meaning if I'm going to build an
[2084.52 --> 2087.04]  algorithm, right, to look at x-rays,
[2087.40 --> 2090.60]  do I really need all images with
[2090.60 --> 2092.32]  all the organs in there if I'm just
[2092.32 --> 2093.04]  looking at bones?
[2093.70 --> 2096.80]  Like, is there any value of trying
[2096.80 --> 2099.26]  to automate a boxer fracture?
[2099.26 --> 2101.26]  For any of you that had teenager
[2101.26 --> 2103.34]  angst, a boxer fracture is when
[2103.34 --> 2104.06]  you punch the wall.
[2104.18 --> 2104.76]  It's almost a...
[2104.76 --> 2105.78]  Or you punch someone's face.
[2106.02 --> 2107.06]  Hopefully you just punched the
[2107.06 --> 2107.94]  wall because you were angry,
[2108.38 --> 2109.60]  right, at your parents or
[2109.60 --> 2109.92]  something.
[2110.24 --> 2111.92]  And it's a very easy break.
[2112.38 --> 2113.84]  You know, and I've been on the
[2113.84 --> 2115.58]  wrong end of the wall a couple
[2115.58 --> 2115.98]  times.
[2116.24 --> 2118.28]  And so, you know...
[2118.28 --> 2119.42]  We won't go into that story.
[2119.70 --> 2120.26]  Yeah, we won't move with that
[2120.26 --> 2120.50]  here.
[2120.70 --> 2123.28]  But the point is, incredibly easy
[2123.28 --> 2126.72]  for an algorithm to look at your
[2126.72 --> 2128.88]  hand and look at the x-ray and
[2128.88 --> 2130.34]  see, yep, that bone is fractured
[2130.34 --> 2132.14]  at such an angle that is a boxer
[2132.14 --> 2134.22]  fracture and here's the prognosis
[2134.22 --> 2136.40]  and here's what we can do for you,
[2136.46 --> 2136.70]  right?
[2136.84 --> 2137.42]  Very easy.
[2137.88 --> 2139.44]  But you probably don't need to see
[2139.44 --> 2140.02]  all the tissue.
[2140.20 --> 2141.24]  You don't need to see all these
[2141.24 --> 2143.02]  other things, you know, in there
[2143.02 --> 2144.86]  where potentially there's, oh, well,
[2144.88 --> 2146.14]  there's calcification and there's
[2146.14 --> 2146.74]  this, there's that.
[2147.10 --> 2148.36]  Well, why do you need that
[2148.36 --> 2148.76]  information?
[2149.04 --> 2151.76]  Does my insurance company get that
[2151.76 --> 2153.38]  information or not?
[2153.38 --> 2155.50]  So these are the leading issues
[2155.50 --> 2156.48]  that we see where there's
[2156.48 --> 2159.12]  derived information out of the
[2159.12 --> 2160.80]  model itself that could
[2160.80 --> 2162.44]  potentially be misused against
[2162.44 --> 2162.72]  you.
[2163.36 --> 2165.58]  And so only provide the data
[2165.58 --> 2166.70]  that's really necessary.
[2166.90 --> 2167.96]  Like, really plan this out and
[2167.96 --> 2168.42]  think it out.
[2168.56 --> 2169.94]  Use, you know, kind of mind
[2169.94 --> 2170.56]  mapping, right?
[2170.62 --> 2173.08]  Like, I only need bone to this.
[2173.16 --> 2174.58]  Why do I have any other data in
[2174.58 --> 2174.70]  there?
[2174.96 --> 2178.56]  Why don't I remove out tissue out
[2178.56 --> 2179.52]  of the image itself?
[2180.08 --> 2181.26]  How do I isolate the bone?
[2181.92 --> 2183.48]  So, like, those are the types
[2183.48 --> 2185.08]  of things that I don't think
[2185.08 --> 2186.28]  people really think through when
[2186.28 --> 2187.10]  they're going to their models
[2187.10 --> 2188.74]  because they're, I think they
[2188.74 --> 2191.28]  have a, which is great, they're
[2191.28 --> 2193.24]  super positive about why they're
[2193.24 --> 2193.94]  building something.
[2194.44 --> 2195.82]  And it's just like they're
[2195.82 --> 2197.08]  looking at the upside, right?
[2197.12 --> 2197.92]  Which is, hey, I'm going to be
[2197.92 --> 2199.44]  able to solve this problem for
[2199.44 --> 2200.66]  radiologists and they can focus
[2200.66 --> 2202.88]  on really complex issues, not
[2202.88 --> 2203.98]  realizing that there's a
[2203.98 --> 2205.96]  potential nefarious use of the
[2205.96 --> 2207.14]  derived results of that model
[2207.14 --> 2207.50]  itself.
[2207.66 --> 2209.14]  So how do you keep that out?
[2209.22 --> 2210.54]  And then building that exercise
[2210.54 --> 2212.40]  into data engineering is just
[2212.40 --> 2214.42]  as critical as the data
[2214.42 --> 2216.40]  cleansing and the data
[2216.40 --> 2218.64]  preparation that goes into the
[2218.64 --> 2219.88]  model, you know, and feature
[2219.88 --> 2220.80]  building itself.
[2221.56 --> 2222.94]  Yeah, that's super interesting.
[2223.16 --> 2225.56]  I know, and I don't know, maybe
[2225.56 --> 2227.80]  you guys have seen this trend
[2227.80 --> 2229.06]  too, but I think we've kind of
[2229.06 --> 2230.96]  gotten into this trend of, like,
[2231.04 --> 2233.12]  kind of pawning off a lot of the
[2233.12 --> 2235.30]  intuition around the features in
[2235.30 --> 2237.48]  our models into kind of deeper,
[2237.48 --> 2239.84]  more complex models that kind of
[2239.84 --> 2241.56]  figure it out on on their own.
[2241.62 --> 2241.84]  Right.
[2241.84 --> 2243.48]  And we never really go back and
[2243.48 --> 2245.58]  say, well, these features or
[2245.58 --> 2247.28]  this data that we put in isn't
[2247.28 --> 2249.00]  really isn't really necessary.
[2249.16 --> 2249.98]  Why are we using it?
[2250.00 --> 2251.74]  It's both, you know, causing us
[2251.74 --> 2253.46]  potential, you know, compliance
[2253.46 --> 2255.02]  issues, but also it's just making
[2255.02 --> 2256.14]  things harder because it's more
[2256.14 --> 2257.88]  data and all of that.
[2257.98 --> 2259.24]  So, yeah, I don't know.
[2259.30 --> 2260.86]  That's that's definitely one trend
[2260.86 --> 2261.76]  trend I've seen.
[2261.98 --> 2262.10]  Yeah.
[2262.16 --> 2263.12]  More data isn't better.
[2263.20 --> 2264.18]  That's why I've always kind of
[2264.18 --> 2266.92]  despised about big data is just
[2266.92 --> 2267.86]  because you have a lot of data
[2267.86 --> 2269.12]  doesn't mean you should use it.
[2269.36 --> 2269.66]  Right.
[2269.92 --> 2271.98]  The point is, and I think this is
[2271.98 --> 2274.22]  just generally good data science,
[2274.44 --> 2275.80]  actually just generally good
[2275.80 --> 2276.32]  science.
[2276.32 --> 2276.62]  Right.
[2277.04 --> 2279.88]  Is you're usually on a mission to
[2279.88 --> 2281.92]  solve or answer a question or
[2281.92 --> 2282.66]  solve a problem.
[2282.88 --> 2283.14]  Right.
[2283.70 --> 2284.98]  And then work backwards.
[2285.14 --> 2286.66]  What do you need for that?
[2287.12 --> 2288.62]  But I think just throwing more and
[2288.62 --> 2290.96]  more data at a model for it to
[2290.96 --> 2293.40]  figure out, you know, intra model,
[2293.40 --> 2295.64]  potential patterns and useful
[2295.64 --> 2297.62]  features out of the data itself
[2297.62 --> 2299.14]  isn't necessarily useful
[2299.14 --> 2300.54]  holistically to the consumer.
[2300.70 --> 2302.18]  It's useful to you, not
[2302.18 --> 2303.04]  necessarily the consumer.
[2303.24 --> 2304.22]  And I think that's the
[2304.22 --> 2305.36]  challenges is that we have to
[2305.36 --> 2306.96]  take into account who's in the
[2306.96 --> 2308.50]  data just as much as the problem
[2308.50 --> 2309.42]  we're trying to solve.
[2309.98 --> 2311.96]  So it almost sounds like that
[2311.96 --> 2314.78]  maybe in if you look at the
[2314.78 --> 2317.60]  the AI space versus more
[2317.60 --> 2318.88]  traditional data science, like,
[2318.98 --> 2320.38]  you know, just analytics or ETL
[2320.38 --> 2321.20]  or visualization.
[2322.20 --> 2323.74]  As you talk about feature
[2323.74 --> 2324.98]  engineering and the fact that,
[2325.02 --> 2327.00]  you know, more data isn't always
[2327.00 --> 2328.08]  the right way to go.
[2328.28 --> 2330.28]  Is that a particular concern that
[2330.28 --> 2331.60]  I guess we're going to see in the
[2331.60 --> 2333.40]  AI space going forward is given
[2333.40 --> 2334.68]  the fact that we're used to
[2334.68 --> 2336.70]  throwing so much data at our
[2336.70 --> 2338.70]  models and letting letting the
[2338.70 --> 2340.34]  neural network figure out which
[2340.34 --> 2341.04]  features matter.
[2341.38 --> 2342.84]  Is that something that AI
[2342.84 --> 2344.12]  practitioners need to be
[2344.12 --> 2345.88]  particularly concerned about, do
[2345.88 --> 2346.18]  you think?
[2346.26 --> 2347.64]  Or is it really just the same
[2347.64 --> 2348.76]  level as the others?
[2348.76 --> 2351.64]  No, I and I'll let Andrew, you
[2351.64 --> 2354.04]  know, chime in on this, but I we
[2354.04 --> 2355.26]  have to stop being lazy.
[2356.08 --> 2357.22]  Lazy is bad.
[2357.84 --> 2359.64]  You know, we're engineers for a
[2359.64 --> 2360.20]  reason, right?
[2360.24 --> 2361.18]  There's a process.
[2361.68 --> 2364.96]  And laziness leads to bad
[2364.96 --> 2365.60]  actions.
[2365.60 --> 2367.28]  And there are bad actors out
[2367.28 --> 2367.56]  there.
[2367.92 --> 2370.40]  And as we move to a world which I
[2370.40 --> 2372.06]  think is fantastic where machines
[2372.06 --> 2373.42]  can provide the necessary
[2373.42 --> 2374.80]  intelligence to augment human
[2374.80 --> 2376.90]  decision making, it's on us
[2376.90 --> 2379.12]  collectively to ensure that we
[2379.12 --> 2380.44]  hold ourselves to the highest
[2380.44 --> 2380.90]  standards.
[2381.54 --> 2383.80]  And just randomly throwing a
[2383.80 --> 2385.36]  bunch of data in there, just
[2385.36 --> 2386.76]  because we are able to collect
[2386.76 --> 2388.30]  it, process it, and make
[2388.30 --> 2389.56]  decisions on it doesn't mean
[2389.56 --> 2391.54]  it's the ethically right
[2391.54 --> 2392.22]  decision.
[2392.78 --> 2394.14]  And I think what I'm concerned
[2394.14 --> 2395.98]  about is, and maybe this is
[2395.98 --> 2398.22]  just a broader theme, is people
[2398.22 --> 2400.00]  are really afraid of the Amazons
[2400.00 --> 2400.94]  of the world, right?
[2401.06 --> 2402.76]  I mean, the inertia behind an
[2402.76 --> 2403.74]  organization like that.
[2403.74 --> 2405.90]  And I think people are willing
[2405.90 --> 2407.56]  to take shortcuts to try to
[2407.56 --> 2409.52]  catch up through augmenting
[2409.52 --> 2410.92]  business operations through
[2410.92 --> 2411.66]  machine intelligence.
[2412.02 --> 2413.46]  So whether that's AI or it's
[2413.46 --> 2414.86]  just like a simple linear
[2414.86 --> 2415.66]  regression, right?
[2415.72 --> 2417.44]  They're trying to automate as
[2417.44 --> 2419.30]  much as they can because they
[2419.30 --> 2420.54]  feel like that's the only way
[2420.54 --> 2421.68]  they can compete against an
[2421.68 --> 2421.98]  Amazon.
[2422.98 --> 2424.42]  And so I think that's going to
[2424.42 --> 2425.84]  lower the barrier of entry to
[2425.84 --> 2427.04]  deploy into production.
[2427.20 --> 2428.64]  And that's my biggest fear,
[2428.92 --> 2429.32]  honestly.
[2429.66 --> 2431.20]  I'm not worried about Skynet.
[2431.20 --> 2432.36]  I'm really not.
[2432.50 --> 2434.22]  I'm more worried about we're
[2434.22 --> 2435.24]  going to start making bad
[2435.24 --> 2437.20]  decisions without understanding
[2437.20 --> 2439.46]  the potential repercussions to
[2439.46 --> 2440.40]  the direct consumer.
[2440.94 --> 2442.14]  Not that AI is going to take
[2442.14 --> 2444.12]  over, but rather our AI is
[2444.12 --> 2445.10]  incorrect and all of a sudden
[2445.10 --> 2447.36]  we're not providing mortgages to
[2447.36 --> 2448.48]  a subset of Detroit.
[2449.08 --> 2450.90]  Or insurance premiums are going
[2450.90 --> 2453.38]  up to for, you know, the $30,000
[2453.38 --> 2455.52]  to $60,000 per year, you know,
[2455.62 --> 2457.40]  socioeconomic sector, right?
[2457.40 --> 2461.24]  Is that we tend to, based on
[2461.24 --> 2463.26]  the data we have, isolate and
[2463.26 --> 2463.90]  polarize.
[2464.48 --> 2467.46]  And that's based on bad, you
[2467.46 --> 2468.64]  know, data governance, in my
[2468.64 --> 2468.92]  opinion.
[2469.32 --> 2470.84]  So you might summarize it as
[2470.84 --> 2473.70]  bias versus, you know, Skynet.
[2473.96 --> 2474.32]  Yeah.
[2474.46 --> 2475.64]  I mean, I think inadvertent
[2475.64 --> 2476.20]  bias, right?
[2476.22 --> 2477.62]  There's always bias in our data.
[2477.80 --> 2478.66]  I don't think that's ever going
[2478.66 --> 2479.60]  to be, I mean, otherwise there's
[2479.60 --> 2481.08]  no statistical relevance, right?
[2481.32 --> 2483.12]  But I think bias for the wrong
[2483.12 --> 2484.66]  reasons without us knowing it
[2484.66 --> 2487.48]  is potentially increased based
[2487.48 --> 2489.74]  on the more data we throw it
[2489.74 --> 2490.86]  because it's not possible for
[2490.86 --> 2493.14]  humans to run through all of the
[2493.14 --> 2493.46]  data.
[2493.78 --> 2494.98]  And I just don't think that
[2494.98 --> 2496.44]  algorithms aren't good at
[2496.44 --> 2497.58]  looking at risk where humans
[2497.58 --> 2497.88]  are.
[2498.44 --> 2499.78]  And so we need a good way to
[2499.78 --> 2502.02]  quantify the risk based on the
[2502.02 --> 2503.72]  type of model we're using, right?
[2503.84 --> 2505.76]  To the type of policies and the
[2505.76 --> 2507.72]  existence of regulations and law
[2507.72 --> 2510.08]  on that data and the potential
[2510.08 --> 2511.40]  negative outcome of the
[2511.40 --> 2512.16]  algorithm itself.
[2512.32 --> 2513.62]  And we need to merge that
[2513.62 --> 2515.00]  together to really think about
[2515.00 --> 2516.94]  quantifying risk in a different
[2516.94 --> 2517.32]  way.
[2517.72 --> 2519.24]  The days of parameterization
[2519.24 --> 2521.92]  around data to quantify risk
[2521.92 --> 2522.40]  are over.
[2522.96 --> 2524.50]  The data is too big and vast and
[2524.50 --> 2524.98]  complicated.
[2525.70 --> 2527.84]  And so it's really outcome-based
[2527.84 --> 2529.38]  decision making is really our
[2529.38 --> 2531.08]  future in the AI space.
[2531.22 --> 2532.98]  And it all starts with good
[2532.98 --> 2534.16]  governance and understanding what
[2534.16 --> 2536.66]  data is going in and why we're
[2536.66 --> 2537.26]  using it.
[2537.48 --> 2539.10]  And, you know, based on that,
[2539.18 --> 2540.52]  choosing the right models to
[2540.52 --> 2541.26]  attack the problem.
[2541.26 --> 2541.94]  Yeah.
[2542.10 --> 2544.40]  And let me just add in, I think
[2544.40 --> 2546.52]  what Matt said is 100% correct.
[2546.64 --> 2548.96]  And one of the reasons why I
[2548.96 --> 2551.52]  think more data is not just kind
[2551.52 --> 2555.24]  of blanket always better is I am
[2555.24 --> 2558.96]  worried about both bias and any
[2558.96 --> 2560.04]  potential failures.
[2560.04 --> 2562.54]  And I think what we're looking at is
[2562.54 --> 2564.56]  a world in, let's say, you know,
[2564.76 --> 2566.74]  two to four or five years, something
[2566.74 --> 2570.46]  like that midterm future where no
[2570.46 --> 2574.14]  one fully understands where all the
[2574.14 --> 2576.22]  models that are deployed have gotten
[2576.22 --> 2577.04]  their data from.
[2577.38 --> 2579.46]  And so if there's a problem, it's
[2579.46 --> 2581.64]  going to be really hard to identify
[2581.64 --> 2584.44]  exactly why that problem occurred.
[2584.70 --> 2586.94]  And so I think the type of like tech
[2586.94 --> 2590.06]  debt that we're looking at when we're
[2590.06 --> 2592.44]  in a world where machine learning is
[2592.44 --> 2595.10]  something we're really relying on is
[2595.10 --> 2596.86]  going to it's going to change the
[2596.86 --> 2597.30]  paradigm.
[2597.48 --> 2599.22]  It's going to mean that we need to
[2599.22 --> 2602.14]  do a lot of this governance and
[2602.14 --> 2604.04]  risk management up front.
[2604.46 --> 2606.88]  Otherwise, we simply won't be able to
[2606.88 --> 2609.24]  fully understand failures when they
[2609.24 --> 2610.14]  start to emerge.
[2610.66 --> 2612.38]  Yeah, this this is great.
[2612.48 --> 2612.78]  I don't know.
[2612.82 --> 2614.18]  I've thought for a long time.
[2614.24 --> 2616.24]  I mean, software engineering and
[2616.24 --> 2617.80]  software engineers have had a long
[2617.80 --> 2619.68]  time to kind of come up with their
[2619.68 --> 2621.76]  their standards and process around
[2621.76 --> 2623.16]  responsible software engineering.
[2623.16 --> 2625.18]  And we haven't really done that with
[2625.18 --> 2626.68]  AI and data science.
[2626.78 --> 2628.06]  I think a lot of what you guys are
[2628.06 --> 2630.92]  saying is is super relevant to that
[2630.92 --> 2632.98]  discussion and, you know, are great
[2632.98 --> 2633.38]  takeaways.
[2633.38 --> 2634.62]  I mean, be ethical.
[2634.76 --> 2636.96]  Don't be lazy with your your models and
[2636.96 --> 2637.40]  your data.
[2637.52 --> 2639.26]  Talk to your lawyers early.
[2639.26 --> 2639.78]  Right.
[2640.02 --> 2642.24]  Write docs, which everyone should be
[2642.24 --> 2643.28]  should be doing anyway.
[2643.28 --> 2645.78]  But, you know, docs with regards to
[2645.78 --> 2648.26]  to explainability and, you know, think
[2648.26 --> 2650.60]  about and quantify fairness on the
[2650.60 --> 2652.52]  on the outcomes and policies that you're
[2652.52 --> 2653.80]  trying to enforce and in your
[2653.80 --> 2654.22]  outcomes.
[2654.22 --> 2656.16]  I think all of these are just just
[2656.16 --> 2657.48]  super, super helpful.
[2658.04 --> 2660.06]  I know we we only have, you know, a
[2660.06 --> 2661.22]  little bit of time here to discuss
[2661.22 --> 2661.84]  all these things.
[2661.88 --> 2663.16]  I think you guys have done a great
[2663.16 --> 2665.92]  job at at giving us kind of a crash
[2665.92 --> 2667.98]  course into, you know, regulation
[2667.98 --> 2670.10]  around AI and practical steps we can
[2670.10 --> 2670.42]  take.
[2670.54 --> 2672.36]  Where can listeners follow up?
[2672.38 --> 2673.60]  You mentioned that there's this this
[2673.60 --> 2674.84]  white paper that you guys are coming
[2674.84 --> 2675.22]  out with.
[2675.26 --> 2677.42]  I'm super excited to to read that.
[2677.42 --> 2679.50]  You mentioned some institute that was
[2679.50 --> 2681.30]  associated with with that as well.
[2681.78 --> 2683.94]  What what are some other places if if
[2683.94 --> 2685.86]  you know, our listeners who are out
[2685.86 --> 2687.32]  there in the trenches developing
[2687.32 --> 2690.80]  models and developing software, where
[2690.80 --> 2692.40]  can they where can they start out
[2692.40 --> 2694.54]  there to try to get some get some more
[2694.54 --> 2696.88]  practical info about this that they'll
[2696.88 --> 2698.96]  be able to consume and and hopefully
[2698.96 --> 2701.04]  bring back to their to their teams and
[2701.04 --> 2701.66]  their discussions?
[2702.16 --> 2702.30]  Yes.
[2702.34 --> 2705.58]  So there's not sadly there's not a lot
[2705.58 --> 2706.08]  out there.
[2706.14 --> 2708.82]  And that's one of the reasons why we
[2708.82 --> 2711.02]  wrote this white paper and why, frankly,
[2711.06 --> 2713.04]  we're so enthusiastic about it, because
[2713.04 --> 2714.96]  I think there's this real need for
[2714.96 --> 2717.38]  guidance and, you know, practical
[2717.38 --> 2717.88]  guidance.
[2718.12 --> 2719.76]  And it's really hard to find.
[2719.94 --> 2721.66]  So that's going to be released.
[2721.66 --> 2723.30]  Plan right now is mid-June.
[2723.48 --> 2725.44]  The organization we're co-releasing it
[2725.44 --> 2727.08]  with is the Future of Privacy Forum.
[2728.00 --> 2729.42]  And that'll be on the Immuta website.
[2729.74 --> 2732.54]  We're giving a talk at Strata New York
[2732.54 --> 2736.00]  on basically exactly this, on practical
[2736.00 --> 2737.48]  ways to govern machine learning.
[2738.10 --> 2739.34]  And that'll be, I believe that's in
[2739.34 --> 2740.06]  early September.
[2740.56 --> 2742.04]  Matt, are there other places you'd
[2742.04 --> 2744.16]  recommend that listeners go to get
[2744.16 --> 2744.64]  more info?
[2745.72 --> 2747.94]  No, I mean, I'll kind of second that.
[2748.02 --> 2749.90]  There's not a lot on the open web.
[2750.04 --> 2752.38]  There's not a lot of formal reading out
[2752.38 --> 2752.56]  there.
[2752.66 --> 2753.88]  What I would say is this, though.
[2754.18 --> 2757.50]  In each domain, there is an abundance
[2757.50 --> 2760.22]  of proper governance frameworks,
[2760.22 --> 2762.84]  specifically to verticals, different
[2762.84 --> 2764.96]  regulations around management API.
[2765.22 --> 2767.02]  And I would say look internally, you
[2767.02 --> 2768.40]  know, for those who aren't, you know,
[2768.48 --> 2769.98]  individuals or small companies but
[2769.98 --> 2771.30]  reside in large companies.
[2771.30 --> 2774.76]  I think the place to start is meeting
[2774.76 --> 2776.20]  with your internal governance team.
[2776.46 --> 2778.28]  Ask what type of documentation exists
[2778.28 --> 2778.74]  out there.
[2779.00 --> 2782.02]  And then also talk to application teams
[2782.02 --> 2784.52]  as to, you know, what has their
[2784.52 --> 2786.00]  documentation process been?
[2786.12 --> 2789.28]  What is their standards as to how they
[2789.28 --> 2791.66]  work with governance teams and with
[2791.66 --> 2793.84]  internal data stewards and potentially
[2793.84 --> 2795.54]  even internal data protection
[2795.54 --> 2796.06]  authorities?
[2796.42 --> 2797.80]  I think the data protection officer is
[2797.80 --> 2800.28]  becoming a real title now where
[2800.28 --> 2802.24]  people actually, that is their job.
[2802.54 --> 2804.22]  So I would say look internal first.
[2804.62 --> 2806.52]  Externally, of course, you know, there's
[2806.52 --> 2807.74]  this thing called Google and you can
[2807.74 --> 2808.16]  search it.
[2808.24 --> 2809.10]  But yeah, Andrew's right.
[2809.16 --> 2809.60]  It's a shame.
[2809.70 --> 2812.16]  But there isn't a lot out there to
[2812.16 --> 2813.00]  really get started.
[2813.50 --> 2814.26]  All right.
[2814.32 --> 2814.54]  Yeah.
[2814.62 --> 2815.68]  Well, appreciate that.
[2815.68 --> 2819.00]  Definitely come see these guys at
[2819.00 --> 2819.56]  Strata.
[2819.88 --> 2821.22]  Check out their white paper.
[2821.74 --> 2823.44]  I know that I've learned a ton from
[2823.44 --> 2827.42]  them already and hope to hope to see
[2827.42 --> 2829.42]  you again at a conference soon and
[2829.42 --> 2832.54]  and maybe maybe go out afterwards and
[2832.54 --> 2835.18]  avoid those those boxer fractures for
[2835.18 --> 2835.42]  sure.
[2835.92 --> 2839.60]  But but appreciate appreciate your guys
[2839.60 --> 2840.16]  wisdom here.
[2840.20 --> 2842.20]  It's been it's been super helpful for me.
[2842.38 --> 2843.20]  Thank you so much.
[2843.30 --> 2843.94]  Thanks, gentlemen.
[2843.94 --> 2844.58]  And I appreciate it.
[2846.52 --> 2847.00]  All right.
[2847.04 --> 2848.74]  Thank you for tuning into this episode
[2848.74 --> 2849.66]  of Practical AI.
[2849.90 --> 2851.14]  If you enjoyed the show, do us a
[2851.14 --> 2851.40]  favor.
[2851.50 --> 2852.10]  Go on iTunes.
[2852.22 --> 2852.92]  Give us a rating.
[2853.16 --> 2854.84]  Go in your podcast app and favorite
[2854.84 --> 2855.04]  it.
[2855.12 --> 2856.42]  If you are on Twitter or social
[2856.42 --> 2857.86]  network, share a link with a friend.
[2857.92 --> 2858.60]  Whatever you got to do.
[2858.82 --> 2859.78]  Share the show with a friend if you
[2859.78 --> 2860.28]  enjoyed it.
[2860.58 --> 2862.06]  And bandwidth for ChangeLog is
[2862.06 --> 2863.24]  provided by Fastly.
[2863.36 --> 2864.80]  Learn more at Fastly.com.
[2865.00 --> 2866.38]  And we catch our errors before our
[2866.38 --> 2867.62]  users do here at ChangeLog because
[2867.62 --> 2868.20]  of Rollbar.
[2868.46 --> 2869.86]  Check them out at Rollbar.com
[2869.86 --> 2870.80]  slash ChangeLog.
[2871.06 --> 2872.94]  And we're hosted on Linode cloud
[2872.94 --> 2875.06]  servers at Leno dot com slash
[2875.06 --> 2875.58]  ChangeLog.
[2875.68 --> 2876.14]  Check them out.
[2876.20 --> 2877.06]  Support this show.
[2877.18 --> 2879.36]  This episode is hosted by Daniel
[2879.36 --> 2880.66]  Whitenack and Chris Benson.
[2881.14 --> 2882.56]  Editing is done by Tim Smith.
[2882.78 --> 2884.38]  The music is by Breakmaster
[2884.38 --> 2884.84]  Cylinder.
[2885.28 --> 2886.60]  And you can find more shows just
[2886.60 --> 2888.66]  like this at ChangeLog dot com.
[2888.88 --> 2890.06]  When you go there, pop in your
[2890.06 --> 2890.80]  email address.
[2891.10 --> 2892.50]  Get our weekly email keeping you
[2892.50 --> 2893.88]  up to date with the news and
[2893.88 --> 2895.64]  podcasts for developers in your
[2895.64 --> 2897.12]  inbox every single week.
[2897.48 --> 2898.30]  Thanks for tuning in.
[2898.42 --> 2899.22]  We'll see you next week.
[2899.22 --> 2899.26]  We'll see you next week.
[2899.26 --> 2901.26]  We'll see you next week.
[2901.26 --> 2902.26]  We'll see you next week.
[2902.26 --> 2902.76]  We'll see you next week.
[2902.76 --> 2932.74]  We'll see you next week.
