[0.00 --> 6.24]  we added a certain class of features that are very useful for most people developing Node.js applications.
[6.64 --> 11.82]  And these are the key things that you really want to stay in Fastify, use Fastify for those,
[12.08 --> 14.12]  probably not for the speed in most apps.
[14.38 --> 18.12]  However, Fastify will not let you down when your product starts scaling.
[20.76 --> 24.18]  Big thanks to our partners, Linode Fastly and LaunchDarkly.
[24.18 --> 27.04]  We love Linode. They keep it fast and simple.
[27.04 --> 30.22]  Get $100 in credit at Linode.com slash changelog.
[30.32 --> 34.04]  Our bandwidth is provided by Fastly. Learn more at Fastly.com.
[34.96 --> 39.40]  And get your feature flags powered by LaunchDarkly. Get a demo at LaunchDarkly.com.
[41.44 --> 45.00]  What's up, party people? This episode is brought to you by Auth0.
[45.54 --> 50.48]  Auth0 is a for developers, by developers identity platform built for the cloud era.
[50.84 --> 52.98]  They secure billions of logins every year.
[52.98 --> 56.14]  Identity is the front door of every user interaction,
[56.14 --> 59.64]  and the login experience can make or break a user's first impression.
[60.08 --> 62.92]  Identity and authentication is never a set it and forget it thing.
[63.30 --> 64.98]  That means when teams decide to roll their own,
[65.20 --> 68.56]  they are taking on the full burden of constantly evolving industry standards,
[68.80 --> 70.92]  customer expectations, and data breach tactics.
[71.16 --> 75.48]  And they often don't have the time, expertise, or resources to meet those needs.
[75.72 --> 79.42]  This takes away from critical time needed to innovate and to improve their core product.
[79.42 --> 82.10]  Auth0 has solved this problem for every developer
[82.10 --> 85.94]  to give teams their time back and to make applications more secure.
[86.36 --> 89.58]  With Auth0's security, compliance, and industry standards,
[89.70 --> 91.08]  they're always up to date.
[91.42 --> 94.84]  Developers are free to provide the login options their users want
[94.84 --> 97.70]  with the security their application demands.
[98.14 --> 100.18]  Make login Auth0's problem, not yours.
[100.74 --> 102.42]  Learn more at Auth0.com.
[102.66 --> 104.46]  Again, Auth0.com.
[104.46 --> 116.86]  This is JS Party, your weekly celebration of JavaScript and the web.
[117.66 --> 123.98]  Our next front-end feud takes place at the React Advanced After Party on October 22nd.
[124.12 --> 125.14]  It'll be a lot of fun.
[125.34 --> 126.14]  You don't want to miss it.
[126.28 --> 128.54]  Find out more at ReactAdvanced.com.
[129.20 --> 130.26]  All right, let's do it.
[130.26 --> 131.68]  Hey, it's party time, y'all.
[131.68 --> 148.38]  Hello, party people.
[148.78 --> 153.36]  We are so, so, so, so, so, so, so, so excited to be with you today.
[153.78 --> 157.86]  We're excited to welcome a very special guest, Mateo Colina.
[158.40 --> 159.22]  Welcome, Mateo.
[159.22 --> 160.46]  I am Al.
[160.70 --> 162.72]  I'm so happy to be here again.
[162.92 --> 163.28]  Hello.
[164.08 --> 165.18]  We're so excited to have you.
[165.58 --> 168.14]  And on the panel with us, we've got Nick Nisi today.
[168.32 --> 168.46]  Hello.
[168.58 --> 169.14]  Welcome, Nick.
[169.32 --> 169.84]  Ahoy, ahoy.
[170.02 --> 170.88]  Excited to be here.
[171.16 --> 171.58]  Hi, Nick.
[171.76 --> 172.06]  Yeah.
[172.18 --> 178.04]  So, we could probably invite Mateo on for the next month, like continuously,
[178.42 --> 180.48]  and not run out of topics.
[180.48 --> 187.12]  But we're going to try and limit the discussion today to talk about his open source work on Node
[187.12 --> 193.00]  and specifically a couple of really popular packages in the Node ecosystem that he's the
[193.00 --> 196.12]  lead maintainer of, Fastify and Pnode.
[196.52 --> 203.92]  And so Fastify is like one of the fastest Node web server frameworks out there, no pun intended,
[204.14 --> 204.36]  right?
[204.36 --> 209.76]  And Pnode is an incredible logger, definitely the fastest and best in class logger in the Node.js
[209.76 --> 210.28]  ecosystem.
[210.94 --> 212.18]  I'm a proud user of it.
[212.68 --> 213.74]  So, yeah.
[213.88 --> 217.68]  So, Mateo, before we get into the specifics on the libraries, why don't you introduce yourself?
[217.86 --> 222.80]  Can you tell us a little bit about your background, how you got started in open source, and what
[222.80 --> 226.70]  led you to becoming a member of the Node.js Technical Steering Committee?
[226.70 --> 227.14]  Okay.
[227.62 --> 230.16]  So, this could be the show, right?
[230.26 --> 231.18]  You have asked me a question.
[231.26 --> 232.14]  I try to limit it.
[232.42 --> 233.54]  It's a long story.
[233.66 --> 233.90]  Okay.
[234.10 --> 235.80]  I'm going to cut it very shortly.
[235.98 --> 238.68]  I started coding very early, way too early.
[238.80 --> 240.84]  That's healthy for a kid.
[241.46 --> 247.40]  So, that probably not, I don't know, maybe not something that we all want to do with our
[247.40 --> 247.60]  kids.
[247.70 --> 248.02]  I don't know.
[248.08 --> 252.16]  I don't know if I'm going to put my kid in front of a keyboard coding at four.
[252.78 --> 253.68]  That was my dad.
[253.68 --> 256.10]  I was watching my dad coding when I was four.
[256.32 --> 258.32]  That was probably a little bit too early.
[258.80 --> 261.06]  Anyway, that was the starting time.
[261.22 --> 266.86]  I started bubbling into the open source world and community.
[267.22 --> 269.74]  I started using Linux when I was a teenager, something like that.
[270.26 --> 272.72]  So, Linux came in CDs at the time.
[272.98 --> 275.20]  That was a long, long, long time ago.
[275.70 --> 276.52]  Then what else?
[276.64 --> 280.88]  Well, after that, I went to a very, very normal thing.
[280.88 --> 284.70]  I went to uni, did my bachelor and master.
[284.92 --> 285.54]  Did you finish?
[285.74 --> 287.26]  I finished them all.
[287.48 --> 289.04]  I enjoyed my time.
[289.22 --> 290.94]  And then I even, you know, it was not enough.
[291.02 --> 291.86]  And then I did a PhD.
[292.14 --> 292.26]  Okay.
[292.44 --> 295.34]  Well, I went back one year in the industry, here in Italy.
[295.34 --> 298.42]  I did not like what I saw in the industry.
[298.42 --> 311.38]  Like during my time at my master, I was studying how to build custom databases, robot arms, how to do the equations to send a rocket to the atmosphere.
[311.38 --> 311.96]  I don't know.
[312.04 --> 313.92]  That was the type of stuff that I was doing.
[314.36 --> 321.38]  After that, I ended up writing the W, WS star, the death star microservices.
[321.58 --> 323.14]  I don't know how many of you have had to deal with.
[323.56 --> 326.70]  Excel, SST, WSDL, SOAP.
[327.28 --> 330.02]  A lot of libraries that start with a J at the beginning.
[330.70 --> 331.72]  PTSD for me.
[332.30 --> 332.82]  Yeah.
[332.82 --> 333.26]  Okay.
[334.48 --> 337.32]  Like Java being one, two, three.
[337.68 --> 342.96]  At the time, my first encounter with open source was when I tried to fix.
[343.30 --> 347.22]  So when I was doing my master, I started publishing.
[347.70 --> 349.22]  The NPM came out more or less.
[349.30 --> 349.74]  I don't remember.
[349.84 --> 350.20]  Not NPM.
[350.36 --> 352.56]  GitHub came out more or less.
[352.64 --> 354.28]  Like, I don't remember the year.
[354.56 --> 355.44]  Can probably look it up.
[355.44 --> 360.12]  But these were probably 2008, 2009 type of years.
[360.38 --> 362.18]  I started publishing my first thing.
[362.18 --> 365.74]  I was really into Ruby at the time.
[366.00 --> 368.20]  I was not using Ruby in my job.
[368.42 --> 371.42]  And I loved, I wanted really to use Ruby and Ruby on Rails.
[371.54 --> 374.74]  But I loved Ruby language more than Rails for whatever reason.
[375.46 --> 378.14]  And then I went one year in the industry.
[378.24 --> 379.22]  Didn't like what I saw.
[379.72 --> 382.48]  Tried to get a job out of Italy.
[383.22 --> 385.96]  Applied at a few of the big co's.
[386.60 --> 388.24]  Typically, I wanted to move to London.
[388.40 --> 389.28]  So London jobs.
[389.78 --> 391.30]  So I applied a few there.
[391.30 --> 394.42]  I failed spectacularly at all the job interviews.
[394.86 --> 396.24]  So you know what, folks?
[396.60 --> 398.84]  If you fail at job interviews, it's totally normal.
[399.28 --> 400.70]  The miracle is when you pass.
[401.02 --> 401.22]  Okay?
[401.30 --> 402.34]  It's not when you fail.
[402.70 --> 405.56]  The starting point is, I will know about that.
[405.66 --> 408.84]  I will understand that later in my career.
[408.84 --> 410.86]  But not at the time.
[410.92 --> 414.34]  It was totally not clear to me why I was keep failing those interviews.
[414.50 --> 416.10]  And I was passing the interviews in Italy.
[416.10 --> 419.10]  But I did not want those kind of jobs.
[419.24 --> 422.84]  I really wanted to bring up the boundaries of...
[422.84 --> 423.98]  You wanted to write Java.
[424.12 --> 426.18]  Java beans like all those other cool kids.
[426.18 --> 426.66]  Yeah.
[426.66 --> 426.78]  Yeah.
[427.20 --> 429.32]  The problem was not even that.
[429.44 --> 433.42]  The problem was that it was not the top latest Java.
[433.56 --> 435.66]  It was the Java five years before the problem.
[435.94 --> 436.92]  You know, it's...
[436.92 --> 437.22]  I don't know.
[437.30 --> 437.46]  Sorry.
[437.56 --> 438.64]  I was not very excited.
[438.88 --> 441.88]  Not to go on a huge tangent, but you know, I mean, I am Amel.
[442.06 --> 442.96]  I'm just curious.
[443.28 --> 447.92]  Like in Europe, I always hear this like, oh, Europe is like five to ten years behind the
[447.92 --> 451.92]  United States when it comes to like enterprise infrastructure technology.
[452.34 --> 452.86]  Like is that...
[452.86 --> 454.00]  Would you say that that's accurate?
[454.82 --> 456.94]  No, it's not that.
[457.36 --> 458.06]  It depends.
[458.32 --> 458.66]  Okay.
[458.66 --> 460.66]  It was like that when I...
[461.82 --> 464.74]  Especially Italy, when I entered the career.
[465.32 --> 469.14]  However, it's accelerating significantly things here in Europe.
[469.30 --> 470.08]  You have more engineers.
[470.56 --> 472.06]  No, it's not about the engineers.
[472.32 --> 473.38]  It's about the consumers.
[473.68 --> 475.46]  But you do have more engineers, right?
[475.60 --> 477.54]  There are more software engineers in Europe.
[477.54 --> 478.92]  I don't know the stats.
[479.28 --> 484.90]  What I know is that the consumers expect a certain level of quality now and is driven
[484.90 --> 487.42]  by big US companies.
[487.94 --> 491.62]  So they want that same level of quality for products built in Europe.
[492.16 --> 496.10]  So even for internal company software, that's usually not very nice.
[496.42 --> 500.66]  So they expect this level of technology and this level of user experience.
[501.00 --> 505.72]  Because of that, that has crippled down into how can we implement those things?
[505.72 --> 509.04]  How can we improve the user experience for our products?
[509.22 --> 513.30]  So this has been pushing the technology in Europe to catch up.
[513.62 --> 514.86]  So it's catching up.
[514.92 --> 516.04]  It's still not probably there.
[516.12 --> 520.40]  It's probably a little bit late, at least on certain class of companies.
[520.40 --> 522.10]  But it's catching up quickly.
[522.10 --> 527.76]  Like we start to see like some good class of startups emerging, producing really interesting
[527.76 --> 531.96]  technology, especially in London, Amsterdam, and so on.
[531.96 --> 537.10]  Even a few interesting startups in Italy, which, you know, one that raised 300 million this
[537.10 --> 537.34]  year.
[537.52 --> 538.72]  So I was like, whoa.
[539.02 --> 540.40]  Is it 300 million lira?
[541.24 --> 541.68]  No.
[542.08 --> 543.20]  You know, euros.
[543.36 --> 543.68]  Euros.
[543.68 --> 544.12]  Okay.
[544.60 --> 546.06]  The liras is, okay.
[546.14 --> 546.70]  You want some?
[546.84 --> 547.18]  Yeah, yeah.
[547.18 --> 547.56]  You have some.
[547.60 --> 548.26]  You want some liras?
[548.46 --> 549.04]  I can't, I can't.
[549.32 --> 550.72]  There's nothing anymore.
[550.80 --> 551.16]  No, no.
[551.20 --> 552.60]  My parents are Somali.
[552.88 --> 555.08]  And I mean, they both left when they were teenagers.
[555.28 --> 556.74]  But shilling is the same thing.
[556.84 --> 558.94]  You know, it's buckets and buckets of cash.
[559.30 --> 560.92]  You buy a cup of tea, you know?
[561.22 --> 561.44]  Yeah.
[561.50 --> 563.36]  So it's like that.
[563.50 --> 567.46]  So after this, I ended up going back to doing a PhD.
[567.46 --> 574.76]  Doing my PhD, I started my PhD at the beginning of 2011.
[575.90 --> 576.02]  Okay.
[576.28 --> 580.02]  And at that time, Node.js existed already.
[580.72 --> 583.82]  The super famous talk from Ryan Dahl happened.
[584.48 --> 587.24]  And there was a lot of very interesting community forming.
[587.76 --> 591.30]  At that same time, there were people trying to put JS everywhere.
[591.84 --> 595.28]  So they were doing the Node.bots.
[595.38 --> 596.90]  They were doing the drones.
[596.90 --> 598.86]  They were doing all the things, JavaScript.
[599.00 --> 599.88]  JavaScript, all the things.
[600.50 --> 606.90]  So I tried this and I needed to do, wanted to do a certain level of research during my
[606.90 --> 607.28]  PhD.
[607.72 --> 611.44]  And instead of using, it was alone and I wanted to be very productive.
[611.80 --> 616.30]  And I know how faster I could write Ruby compared to what I could write Java.
[616.50 --> 618.86]  But Ruby, let's face it, is slow.
[618.98 --> 620.68]  It was a very slow language at the time.
[620.80 --> 623.82]  Like you could not do parallel programming and so on.
[623.82 --> 629.18]  And I needed a language that would perform as good as Java, but would take a third of the
[629.18 --> 631.92]  time or a tenth of the time to write because it was alone.
[632.40 --> 633.06]  I tried Node.
[633.20 --> 634.82]  Ransom Benchmark was totally...
[635.98 --> 636.58]  Mind blown.
[636.80 --> 637.40]  Mind blown.
[637.66 --> 638.64]  Then I tried NPM.
[638.64 --> 642.78]  And when I tried NPM, that was totally clear to me.
[643.30 --> 648.04]  Node.js was going to take over the industry.
[648.60 --> 650.74]  The reason, it's Maven.
[653.12 --> 654.38]  Please hold.
[654.64 --> 656.54]  We're having technical difficulties.
[656.54 --> 670.40]  One of the key fundamental issues in Maven was that you could not have the same library
[670.40 --> 673.52]  at two different versions at the same time.
[673.52 --> 679.66]  So let's say that you wanted to use a library that had a certain version of an utility library.
[680.12 --> 685.54]  Now, that utility library yourself, your software would not compile because they needed to all
[685.54 --> 691.58]  be at the same version, which meant that people could not break backward compatibility and innovate
[691.58 --> 692.06]  freely.
[692.94 --> 693.92]  NPM allows this.
[694.26 --> 698.92]  NPM allow the same dependency to be present thousands of times at all the possible versions,
[698.92 --> 703.44]  which means that we have solved the reusing software problem.
[703.44 --> 706.68]  It also means that Node modules become the heaviest object in the universe.
[706.90 --> 708.48]  We have been successful at it.
[708.56 --> 714.16]  We have been trying hard to make that happen for at least as long as I've been in the industry.
[714.40 --> 716.80]  And with NPM, we actually reached that state.
[717.16 --> 717.20]  Okay.
[717.28 --> 721.84]  So, I mean, I feel like it's not an issue for me, like them being the heaviest objects in
[721.84 --> 725.14]  the universe because it's a server tech, you know, it's a server technology.
[725.26 --> 727.04]  It's never getting shipped in the browser.
[727.04 --> 732.80]  But I feel like these issues with, you know, dependencies really became a problem once
[732.80 --> 738.78]  the front end community kind of like hijacked Node as their like build chain and their dependency
[738.78 --> 740.28]  management and like, you know.
[740.50 --> 741.72]  It's totally fine.
[742.12 --> 744.22]  They're not shipping it, them in the browser.
[744.34 --> 748.54]  So, all of those things that NPM is in Node modules, most of them is not stuff that you
[748.54 --> 750.00]  want to ship in the browser anyway.
[750.54 --> 751.90]  So, it's solved the tool chain.
[752.58 --> 754.70]  It's, in fairness, it's bytes on disk.
[755.32 --> 756.34]  Disk is very cheap.
[756.34 --> 756.78]  Right.
[756.94 --> 763.94]  It's bytes on network and bytes on the wire are somewhat cheap in the vast majority of
[763.94 --> 766.54]  the world where you would develop software anyway.
[767.24 --> 771.52]  So, the reality is that that's fine.
[771.74 --> 772.04]  Okay.
[772.58 --> 775.48]  And that's the price of reusing a lot of software.
[775.84 --> 779.34]  So, you can build everything yourself and not have all those things you have to download.
[779.34 --> 781.08]  But, I don't know.
[781.20 --> 786.10]  For all my time, I have been, you know, at some point in order to have the new version
[786.10 --> 789.02]  of the Red Hat, I needed to receive a CD.
[789.66 --> 791.58]  So, you see, that was low.
[792.00 --> 793.96]  Downloading a few megabytes over the wire?
[794.20 --> 795.32]  Well, it's not slow.
[795.58 --> 795.92]  I don't know.
[796.02 --> 796.74]  I have a different.
[797.10 --> 799.84]  But that thing was actually, the full disk was 600 megabytes.
[799.94 --> 801.90]  And now Node modules is 100 and something.
[801.90 --> 802.38]  Yeah.
[802.62 --> 805.94]  No, I think that's a really good analogy because you're absolutely right.
[806.06 --> 808.34]  Like, you're not getting CDs in the mail, right?
[808.36 --> 809.86]  You're able to just NPM install.
[810.42 --> 816.56]  I think the concern is more that, like, bytes to parse and then making users wait while your
[816.56 --> 821.92]  JavaScript is parsing or creating janky experiences because your JavaScript is parsing.
[821.92 --> 823.62]  Like, that's the problem.
[823.94 --> 827.76]  And, you know, I understand, like, open source is working because, like, you know, I think
[827.76 --> 833.68]  most people only write, like, 10% of the code actually needed to run their application these
[833.68 --> 833.94]  days.
[834.44 --> 837.10]  Everything else, that 90% comes from open source modules.
[837.86 --> 840.44]  And, yeah, if you wanted to write that yourself, knock yourself out.
[840.80 --> 843.56]  You're not going to do as good of a job, I can tell you that, you know, because you're
[843.56 --> 845.86]  not going to beat, like, millions of developer brains.
[846.10 --> 848.32]  But it's still something we need to manage, right?
[848.32 --> 852.80]  And I can tell you when I'm picking a package, like, I have a rubric, like, how many dependencies
[852.80 --> 854.00]  does this package have, right?
[854.00 --> 856.34]  Because I don't want my packages to have a bunch of dependencies.
[856.50 --> 860.52]  Like, I don't need packages that have, like, bring their own luggage to the party, right?
[860.56 --> 862.66]  Like, it's like, okay, you're my house guest.
[862.80 --> 864.84]  You're not allowed to invite your own set of guests.
[865.46 --> 869.12]  So I try to keep it very light with my dependencies as much as possible.
[869.12 --> 874.26]  And I'm very careful about the number of dependencies I use that require peer dependencies as well,
[874.36 --> 874.52]  right?
[874.52 --> 878.30]  Because peer dependencies is like an ecosystem that you need to, like, keep an eye on.
[878.32 --> 882.14]  And so there is a cost, is what I'm trying to say, Matteo.
[882.50 --> 883.60]  Yeah, oh, absolutely.
[883.82 --> 886.84]  Like, I don't think this is simple in any form or fashion.
[887.34 --> 895.28]  It's just that the level of efficiency that the industry requires to us right now in how
[895.28 --> 901.66]  we develop software, it's impossible to reach without massive software reuse across projects.
[902.14 --> 902.92]  Right, right.
[902.92 --> 903.36]  Exactly.
[903.36 --> 903.70]  Exactly.
[904.20 --> 909.32]  And so what led you down the path of, like, because you now have, like, hundreds of NPM
[909.32 --> 909.84]  packages.
[910.54 --> 912.26]  400 and something, likely.
[912.44 --> 913.12]  Something like that.
[913.20 --> 914.62]  A lot of them are quite popular.
[914.82 --> 916.70]  So what led you down that rabbit hole?
[916.88 --> 919.28]  Was it just, like, were you your first customer?
[919.66 --> 920.26]  Or like...
[920.26 --> 921.00]  Yeah, totally.
[921.14 --> 922.88]  Like, I don't, like, I code things for myself.
[923.04 --> 924.60]  No, it's not necessarily true.
[924.88 --> 927.46]  I code this because I need them to exist.
[928.12 --> 932.66]  So I'm not necessarily certain that I need...
[932.66 --> 937.26]  And I first try small with low investment of time to develop something and then grow, invest
[937.26 --> 942.98]  more time as I see if something is getting popular and it's useful.
[942.98 --> 944.88]  So it's a slow curve.
[945.62 --> 949.22]  Typically, I am the first client of all my modules.
[949.40 --> 953.68]  Like, I need something to exist in order to what I do, to what I want to do.
[954.14 --> 955.88]  This is also part of my job.
[955.98 --> 958.58]  Like, I work for a company called Nearform.
[958.74 --> 960.14]  I am essentially a consultant.
[960.68 --> 962.02]  I have companies using JavaScript.
[962.44 --> 963.66]  That's part of what Nearform does.
[964.04 --> 964.34]  Okay.
[964.58 --> 969.90]  And which means that we have teams, we have our clients and so on that, you know, might need
[969.90 --> 970.20]  something.
[970.20 --> 973.20]  So I have a very good pulse of...
[973.20 --> 974.54]  I always had a very good pulse.
[974.84 --> 978.12]  I've been at this company for seven years and nine months or something.
[978.68 --> 982.80]  So I have a good pulse on what the users of Node needs.
[983.18 --> 986.76]  I can see what is missing and I can start developing it.
[987.16 --> 994.66]  Or I don't know, I can foretell problems and plan for the worst and start something so
[994.66 --> 997.10]  that when the time is right, you have it done.
[997.74 --> 999.06]  And that was kind of what happened.
[999.06 --> 1002.74]  So that's kind of what I've done so far.
[1003.06 --> 1008.46]  So in between, I ended up doing a PhD and this is the story on itself.
[1008.70 --> 1010.26]  And then I worked for Nearform.
[1010.54 --> 1012.18]  That was the gap that we didn't cover.
[1012.82 --> 1016.82]  And then somewhere you also joined the Node.js Technical Steering Committee and you've been...
[1016.82 --> 1018.00]  I joined after...
[1018.00 --> 1022.44]  I joined the Node Tech Steering Committee before Pino and Fastify existed.
[1022.94 --> 1025.18]  First of all, I tried to work on Node.com for a while.
[1025.18 --> 1028.96]  At that point in time, the leadership was at Giant.
[1029.26 --> 1031.82]  They were doing a really bad job at maintaining Node.
[1032.44 --> 1034.50]  And they did not want Node to evolve.
[1035.02 --> 1036.76]  And they considered things done.
[1037.08 --> 1040.82]  And they had a huge amount of bugs to fix and they didn't want them to be fixed.
[1041.26 --> 1041.58]  Interesting.
[1041.58 --> 1041.70]  Interesting.
[1042.36 --> 1045.34]  I'm like, okay, we should do a show on this open source drama.
[1045.58 --> 1047.38]  Yeah, that's open source drama.
[1047.70 --> 1049.52]  Drama is very real, very real.
[1049.86 --> 1053.74]  But despite it all, what's it been like being on the TSC?
[1053.98 --> 1057.90]  I mean, that's a very elite club of people, but also there's a lot of...
[1057.90 --> 1059.54]  It's very simple to get on the TSC.
[1059.96 --> 1060.32]  Okay.
[1060.38 --> 1061.14]  It's not hard.
[1061.22 --> 1061.58]  Okay.
[1061.92 --> 1067.62]  It's not hard in the sense of, oh, this is an impossible job and you need to be such
[1067.62 --> 1070.32]  an incredible developer to be there.
[1070.74 --> 1072.14]  That's not true.
[1072.82 --> 1073.34]  Okay.
[1073.34 --> 1083.20]  What is true is that in order to be at the TSC, you need to keep a same level of contributions
[1083.20 --> 1085.48]  to Node.js through the time.
[1085.80 --> 1090.84]  So it means that you need to keep a strong, consistent number of contributions for three,
[1091.06 --> 1097.30]  six months, more or less, and show that you deeply care about the success of the platform.
[1097.86 --> 1103.32]  And after that, somebody will notice, somebody will tap your shoulder and you're going to
[1103.34 --> 1104.72]  you will get on the TSC.
[1105.40 --> 1105.54]  Okay.
[1105.70 --> 1107.82]  So that is the simplicity of it.
[1108.00 --> 1108.14]  Okay.
[1108.24 --> 1109.26]  It's not...
[1109.26 --> 1111.42]  It just requires hard work.
[1112.20 --> 1116.70]  And essentially, it's probably three months to become a collaborator, another three, six
[1116.70 --> 1119.92]  months to get to the TSC if you want to reach.
[1120.06 --> 1124.40]  So if you want to get there, it's probably a one-year project overall.
[1125.06 --> 1125.82]  That's cool.
[1126.16 --> 1127.38]  Like, it's not something that...
[1128.52 --> 1132.36]  Then the problems that we fix at the TSC can be hard, can be a lot of drama.
[1132.36 --> 1133.84]  The drama ones are the worst.
[1134.12 --> 1140.30]  Like, you know, it's from time to time, we want to discuss problems, technical problems
[1140.30 --> 1141.04]  and things.
[1141.38 --> 1143.40]  And instead, we ended up discussing drama.
[1143.90 --> 1145.34]  There's been a lot of drama over the years.
[1145.76 --> 1147.08]  Some of that was handled well.
[1147.18 --> 1148.64]  Some of that was handled less well.
[1149.14 --> 1150.60]  I'm proud of certain things.
[1150.66 --> 1152.12]  I'm not proud of certain others.
[1152.46 --> 1154.52]  We have our own scars as a community.
[1155.20 --> 1157.38]  However, the project now is in a very good shape.
[1157.38 --> 1161.94]  Like, we are, you know, very focused on shipping new things, improving it where it's lacking.
[1162.62 --> 1165.06]  I feel it's moving into the right direction.
[1165.18 --> 1166.70]  We have shipped ESM, right?
[1166.82 --> 1167.16]  I don't know.
[1167.24 --> 1168.98]  That was a miracle.
[1169.50 --> 1171.04]  Everybody was betting against ESM.
[1171.10 --> 1172.00]  We can talk about ESM.
[1172.18 --> 1172.56]  Oh, my God.
[1172.60 --> 1173.92]  ESM has got to be its own show.
[1174.00 --> 1175.12]  We need like an ESM follow-up.
[1175.12 --> 1178.38]  Yeah, but, you know, we need to invite a bunch more people, not me.
[1178.54 --> 1179.96]  Invite Miles to talk about ESM.
[1180.18 --> 1183.98]  Miles is like the poster child for Node's implementation of ESM.
[1184.20 --> 1189.78]  But I think for me, what's really impressive, obviously, on the JavaScript, on the language
[1189.78 --> 1193.18]  side, you know, the TC39 has been kicking butt for quite a while.
[1193.36 --> 1197.70]  You know, they've been really helping shape the language and evolve it in the right direction.
[1197.70 --> 1203.24]  But I think on the other side of that, you know, I think the Node contributors and collaborators
[1203.24 --> 1206.44]  have really, I think, done a good job of keeping up with the spec.
[1207.00 --> 1211.12]  More and more of new features in the language are being supported natively.
[1211.22 --> 1214.88]  You don't need that experimental flag or harmony flag as much.
[1215.12 --> 1216.32]  And then also modules.
[1216.50 --> 1217.90]  You know, that's a huge, huge win.
[1218.04 --> 1222.94]  I mean, you know, I don't know if people really fully understand how difficult it is to implement
[1222.94 --> 1228.28]  a module system in Node because, like, Node had its own module system.
[1228.90 --> 1232.16]  Getting that to work and be back compat and not break the web.
[1232.34 --> 1234.30]  And, you know, that's a huge, huge accomplishment.
[1234.80 --> 1236.72]  So really, kudos to the team.
[1242.44 --> 1243.38]  What's up, party people?
[1243.52 --> 1244.96]  Are you ready for Core Web Vitals?
[1245.18 --> 1247.30]  Well, our friends at Raygun can help.
[1247.64 --> 1251.10]  These modern performance metrics play an important role in determining the health of your website.
[1251.10 --> 1255.40]  That's exactly why Raygun has made them into their real-time user monitoring tools.
[1255.78 --> 1260.70]  Now you can see how your Core Web Vitals scores are trending across your entire website in real time
[1260.70 --> 1265.92]  and drill into individual pages to focus your efforts on the biggest performance gains.
[1266.40 --> 1269.94]  Unlike traditional tools, Raygun surfaces real user data, not synthetic,
[1270.34 --> 1276.88]  giving greater insights and control, filter your score by time frame, browser, device, geolocation,
[1277.26 --> 1278.74]  whatever matters most to you and your team.
[1278.74 --> 1283.88]  And what makes Raygun truly unique is the level of detail they provide so you can take action quickly,
[1284.24 --> 1286.46]  identify and resolve front-end performance issues,
[1286.62 --> 1289.72]  with full waterfall breakdowns, user session data,
[1290.06 --> 1292.96]  instance level, diagnostics of every page request,
[1293.18 --> 1294.10]  and a whole lot more.
[1294.48 --> 1296.48]  Learn more at Raygun.com today
[1296.48 --> 1298.62]  and take control of your Core Web Vitals.
[1299.06 --> 1300.38]  Plan start at $8 a month.
[1300.56 --> 1303.80]  Again, Raygun.com for your free 14-day trial.
[1303.80 --> 1328.82]  That was a fascinating journey through the early days of Node in your early career,
[1328.82 --> 1330.46]  and very exciting.
[1330.82 --> 1334.38]  You were also on JS Party 103 talking about streams,
[1334.38 --> 1337.48]  so we've definitely heard some great things from you,
[1337.56 --> 1338.42]  more great history,
[1338.62 --> 1341.00]  and we were just talking in the break about how we need to have you back,
[1341.08 --> 1342.24]  so we will definitely do that.
[1342.54 --> 1345.74]  But I definitely wanted to segue us into your libraries,
[1346.14 --> 1348.16]  and particularly Fastify and Pino.
[1348.28 --> 1351.16]  And if I understand correctly, Fastify came out of Pino,
[1351.28 --> 1354.48]  so maybe let's start with Pino and talk about what it is and how it came to be.
[1354.48 --> 1357.26]  Pino is a login library for Node.
[1357.56 --> 1359.16]  Now, logging, what is logging?
[1359.34 --> 1360.74]  Logging is the thing that you do,
[1361.16 --> 1364.40]  the most crude way of logging in Node is doing console log something.
[1364.76 --> 1366.20]  It's printing on a terminal.
[1366.84 --> 1368.92]  However, when you're printing on a terminal,
[1369.36 --> 1371.64]  you really don't want to be just printing on a terminal
[1371.64 --> 1374.70]  because you want to add a lot of other metadata to it.
[1374.90 --> 1377.26]  You want to add the timestamp,
[1377.36 --> 1379.30]  the time at which you have been logging your things.
[1380.00 --> 1383.32]  You want to add the, for example, this is one, for example,
[1383.32 --> 1385.68]  you can add the time.
[1386.28 --> 1389.38]  You might want to change and make it pretty and add colors,
[1389.38 --> 1395.44]  or you might want to change the format and ship it to Elasticsearch, for example,
[1396.02 --> 1397.36]  or OpenSearch, whatever.
[1397.62 --> 1399.66]  You know, let's be friendly to everybody.
[1400.18 --> 1402.22]  This is another fight that I don't want to open,
[1402.42 --> 1404.56]  but this is an interesting one to have on the show.
[1405.10 --> 1406.80]  Anyway, there is Elasticsearch.
[1406.88 --> 1408.42]  You might want to ship it to Syslog.
[1408.42 --> 1415.04]  You might want to get it collected via the Docker logs or CloudWatch or I don't know.
[1415.24 --> 1415.92]  LogRotate.
[1416.44 --> 1417.42]  Or LogRotate.
[1418.20 --> 1418.32]  Okay.
[1418.52 --> 1422.72]  So one of the earliest problems in Node is when Node came to be,
[1422.86 --> 1425.42]  people started developing loggers,
[1426.12 --> 1430.94]  which is that are useful for creating structured information from your application.
[1431.20 --> 1434.52]  And they are often required for even for some regulations
[1434.52 --> 1438.96]  or for actually knowing what is going on in your app the moment you have a bug.
[1439.24 --> 1440.40]  So very useful.
[1440.86 --> 1443.12]  It saved my life a few times already.
[1443.68 --> 1447.52]  You really want a good logging library in your system and use it.
[1448.18 --> 1451.94]  So what happened at the time was the popular ones were,
[1452.34 --> 1454.58]  we were talking about 2016, something like that.
[1455.02 --> 1458.56]  And in 2016, there were two main popular logging libraries.
[1458.56 --> 1461.40]  One was Bunion, developed by Giant.
[1462.04 --> 1469.26]  And one was Winston, maintained by our friend, Charlie, Index Zero, Charlie Robbins.
[1469.72 --> 1472.90]  However, they both had the same approach, which is,
[1473.02 --> 1477.42]  oh, I follow the Java approach for loggers,
[1477.68 --> 1481.64]  which is I have a logger that wraps a logger that wraps a logger three,
[1481.76 --> 1485.02]  four times before I am going to write down to a file.
[1485.02 --> 1488.30]  And they have this approach of nesting things
[1488.30 --> 1492.68]  and be able to create multiple loggers and so on,
[1492.74 --> 1494.66]  create multiple destinations and so on and so forth.
[1495.14 --> 1497.28]  The typical problem those loggers had,
[1497.64 --> 1501.06]  one was throughput and the other one was memory usage.
[1501.62 --> 1504.70]  So it was very hard to control the amount of memory
[1504.70 --> 1506.50]  those loggers were using before writing.
[1506.92 --> 1509.16]  You know, you want your log, you do console log, right?
[1509.30 --> 1511.56]  You don't, Node.js is a synchronous platform,
[1511.56 --> 1516.76]  but you're not waiting for that log line to be written to continue.
[1517.54 --> 1520.08]  So, however, you're doing something synchronous,
[1520.26 --> 1523.12]  but it's something that is asynchronous in nature or synchronous in nature.
[1523.28 --> 1524.88]  So you have this dichotomy.
[1525.20 --> 1527.56]  And in some cases, memory could actually explode
[1527.56 --> 1529.30]  because let's say that, you know,
[1529.32 --> 1531.36]  you want to send all your logs to Elasticsearch,
[1531.80 --> 1533.16]  for example, then, you know,
[1533.28 --> 1536.14]  you might produce more logs than what you can send ship
[1536.14 --> 1537.30]  to Elasticsearch in time.
[1537.68 --> 1539.94]  And in the meanwhile, your memory will start ballooning.
[1539.94 --> 1542.88]  All of that comes to be very complicated, okay?
[1543.20 --> 1545.08]  Well, I would say, like, log management
[1545.08 --> 1548.04]  is honestly one of the most complicated things
[1548.04 --> 1550.86]  that seems so simple on the surface.
[1551.14 --> 1552.70]  Yeah, and it's also so boring.
[1552.86 --> 1554.10]  Like, it's also so boring.
[1554.34 --> 1554.70]  Yes.
[1555.04 --> 1558.00]  Like, yeah, the least glamorous, attractive thing.
[1558.08 --> 1559.88]  It's like, oh, yeah, I just got to build a logger.
[1559.96 --> 1563.12]  I got to find a way to get my logs to the cloud off of the server.
[1563.24 --> 1564.50]  I need to get it to another cloud, right?
[1564.50 --> 1565.98]  I need to get it to another part of the cloud
[1565.98 --> 1566.96]  to be more specific, right?
[1567.30 --> 1567.84]  It's crazy.
[1567.84 --> 1569.40]  And then there's always a cost to logging.
[1569.40 --> 1570.78]  And people always forget that.
[1571.08 --> 1575.40]  You have to log carefully and selectively and, you know...
[1575.40 --> 1576.48]  And it's very tricky.
[1576.82 --> 1577.20]  Exactly.
[1577.44 --> 1581.56]  So at the time, I started doing some performance optimizations
[1581.56 --> 1583.10]  to clients' applications.
[1583.30 --> 1587.84]  There were a lot of startups and big companies
[1587.84 --> 1591.38]  that were starting shipping Node.js projects at scale.
[1591.38 --> 1595.10]  And they were having such a big problem.
[1595.72 --> 1598.74]  And it turned out that it was...
[1598.74 --> 1600.10]  This is a fun story, as usual.
[1600.38 --> 1605.38]  I was in London for doing one of those consulting
[1605.38 --> 1608.00]  with my friend, David Mark Clements,
[1608.08 --> 1609.88]  that you have met, Amal, Dave.
[1610.00 --> 1611.68]  And I don't know if you, Nick, you have met Dave,
[1611.80 --> 1614.34]  but we have some stories together, okay?
[1614.76 --> 1616.46]  He was working with Nearform at the time,
[1616.46 --> 1618.76]  and we are doing a lot of those things together.
[1619.24 --> 1621.18]  We were doing some consulting in London.
[1621.58 --> 1624.58]  We had the company do some performance optimization and so on.
[1624.62 --> 1627.48]  And then we reached a point that their biggest problem
[1627.48 --> 1628.68]  was the logger.
[1629.46 --> 1631.12]  Like, they were logging so much,
[1631.84 --> 1633.82]  but they were not really logging so much.
[1633.98 --> 1636.80]  But the main bottleneck for their application was the logger.
[1636.80 --> 1639.04]  And I was asked, what should we use?
[1639.20 --> 1640.92]  They said, well, your bottleneck is...
[1640.92 --> 1644.20]  They told me, we found out that the bottleneck was the logger.
[1644.58 --> 1646.40]  And then they asked us, what should we use?
[1646.50 --> 1648.76]  This was Bunyan.
[1649.08 --> 1651.60]  And this is the most popular logger that...
[1651.60 --> 1653.84]  We really like this logger, and what can we do?
[1654.26 --> 1658.22]  So I said, well, the only thing that I can do is write one.
[1658.54 --> 1662.08]  So we start writing a very, very minimal version of the logger.
[1662.28 --> 1663.20]  That's so heroic.
[1663.20 --> 1668.42]  That's like the romantic comedy line that's like, you know...
[1668.42 --> 1669.12]  Wait a second.
[1669.14 --> 1672.76]  If this most popular logger is treating you so badly,
[1672.92 --> 1675.64]  well, you know, the best thing I can do is write you a new one, baby.
[1675.82 --> 1677.80]  Yeah, and it was unvalentic.
[1679.00 --> 1681.38]  So that happened, okay.
[1681.74 --> 1684.68]  And we started developing the thing,
[1685.02 --> 1687.60]  and it's called Pinot because pine was taken.
[1688.10 --> 1690.40]  And in front of my house at the time, there was a pine.
[1690.98 --> 1691.30]  That's it.
[1691.30 --> 1693.12]  It's Italian for pine, right?
[1693.12 --> 1693.82]  It's not in English.
[1693.96 --> 1694.76]  Yes, of course.
[1694.86 --> 1695.32]  Of course.
[1695.42 --> 1695.84]  Of course.
[1696.06 --> 1698.20]  All of your packages were actually Italian.
[1698.38 --> 1700.08]  I mean, what's the Italian way to say fast?
[1700.62 --> 1701.06]  Veloce.
[1701.60 --> 1701.96]  Veloce.
[1702.02 --> 1704.78]  See, Veloce would be a great name for a Node Packer.
[1705.40 --> 1706.54]  I know.
[1706.70 --> 1707.24]  Yeah, I know.
[1707.48 --> 1709.30]  I went for Fastify at the time.
[1709.46 --> 1714.18]  Anyway, this shipped in the summer of 2016, something like that.
[1714.18 --> 1714.50]  Okay.
[1714.50 --> 1719.60]  And we presented in a talk at Node Summit.
[1719.60 --> 1721.84]  I think it was August 2016.
[1722.36 --> 1722.48]  Okay.
[1722.96 --> 1724.96]  But the module was already done.
[1725.08 --> 1726.18]  We were using it in production.
[1726.76 --> 1732.62]  Typical thing is memory reduction in such cases were dropped by 200, 300 megabytes.
[1732.70 --> 1732.92]  Easy.
[1733.74 --> 1736.76]  And throughput was removing the bottleneck.
[1736.76 --> 1741.32]  So the throughput was one and a half, two times, essentially, for the application with the problem.
[1741.42 --> 1742.24]  So, hey, success.
[1743.04 --> 1746.32]  Problem is, all those logger, Bonion and Winston, were doing a lot of many things.
[1746.52 --> 1748.86]  And we didn't need to do all those things to log.
[1748.96 --> 1753.44]  They just want to write things out as fast as possible to standard out.
[1753.44 --> 1754.50]  Because that's what we use.
[1754.54 --> 1755.62]  We use containers, right?
[1755.70 --> 1761.96]  We don't do what to do to rotate log files or ship it to Elasticsearch on process and so on.
[1761.96 --> 1762.12]  No.
[1762.58 --> 1766.16]  Just send out to standard output or write them to a file.
[1766.34 --> 1770.68]  And then somebody else will pick those things up and ship it where they need to be shipped,
[1771.00 --> 1773.68]  which is the philosophy of cloud-based logging anyway.
[1773.92 --> 1775.94]  So why the heck you want to do something different?
[1776.60 --> 1781.54]  So after that, I was, I think, having a beer or dinner with David.
[1781.54 --> 1783.58]  And David said, yeah, we have done Pino.
[1783.84 --> 1785.34]  So what are we doing next?
[1785.74 --> 1791.82]  And I told him, well, the next biggest bottleneck for Node.js is Express.
[1792.06 --> 1792.26]  Yeah.
[1792.76 --> 1794.26]  Express is slow.
[1794.72 --> 1798.60]  Just by using Express, you are cutting your throughput by five.
[1799.14 --> 1801.08]  So, and Happy was worse.
[1801.14 --> 1805.32]  As opposed to the vanilla HTTP module.
[1805.44 --> 1806.34]  Yeah, exactly.
[1806.54 --> 1807.34]  Yes, yes.
[1807.62 --> 1809.66]  I don't remember what was at the time.
[1809.66 --> 1811.78]  It's five, six, ten right now.
[1812.00 --> 1815.48]  It's like, it's not ten, but it's probably five to six times.
[1815.62 --> 1816.46]  Is Cola faster?
[1816.54 --> 1818.44]  I've never done any benchmarking for Cola.
[1818.56 --> 1819.94]  It's slightly faster.
[1820.30 --> 1822.04]  It's kind of 2x compared to Express.
[1822.30 --> 1824.66]  Probably half what Node Core can do.
[1824.96 --> 1829.20]  Still, you're still paying a significant penalty on using those frameworks.
[1829.46 --> 1829.62]  Okay.
[1829.88 --> 1834.12]  And what about, I'm just curious, like this is a, I'm sorry, this is the stuff I nerd out about.
[1834.12 --> 1837.64]  So, like Netflix, I know they're using a bunch of nodes.
[1838.08 --> 1840.76]  Restify, Restify and Express.
[1841.28 --> 1845.54]  And they are more or less happy because they have a lot of code base using it developed back in the day.
[1845.68 --> 1849.58]  So, it's probably not worth to change it unless you really need to.
[1849.96 --> 1851.38]  The problem, I was already on the TSC.
[1851.38 --> 1863.34]  And the question was, why the heck are we spending effort in improving the performance of Node if then you use a logger and a web framework that will destroy your performance?
[1863.90 --> 1871.72]  So, it's not worth optimizing Node Core or improving Node Core if we have those problems in the ecosystem.
[1872.00 --> 1873.74]  So, I started doing some research.
[1874.40 --> 1876.04]  However, I picked one choice.
[1876.04 --> 1885.22]  So, writing a web framework, like if you try to look at the HTTP spec, the GP101, 1.1 RFC and cry and run away.
[1885.66 --> 1887.20]  It's a gargantuan job.
[1887.76 --> 1888.48]  Please start reading.
[1888.66 --> 1894.34]  Everybody should, that should be a very important read at every course, bootcamp, university, whatever.
[1894.78 --> 1897.10]  But it's a big, big, big spec.
[1897.54 --> 1902.88]  So, I know it was a massive problem, a massive gargantuan task.
[1902.88 --> 1905.70]  So, I decided, well, I can do this alone.
[1906.20 --> 1910.40]  So, and I can get near from Tupay for it because it's a new web framework.
[1910.52 --> 1912.22]  It will take years to get it done.
[1912.62 --> 1914.38]  So, how can we get it done?
[1914.64 --> 1922.76]  I decided, well, let's see if there is somebody else that is seeing the same problems and if they wanted to join me on that journey.
[1923.34 --> 1927.80]  At that time, I was giving a Node.js workshop in Bologna.
[1927.80 --> 1931.66]  One of the students that came there was a university graduate.
[1932.14 --> 1933.44]  Like he was a university student.
[1933.54 --> 1935.42]  He was just finishing his degree.
[1935.84 --> 1937.46]  Anyway, we were doing that.
[1938.10 --> 1942.60]  And at that time, he asked me, well, I want to get into open source.
[1943.16 --> 1946.42]  And then I said, well, of course, we can build this together.
[1946.54 --> 1947.76]  And he said, sure, why not?
[1948.06 --> 1950.62]  We started developing this thing together.
[1950.62 --> 1956.24]  Then I used a little bit of my open source and conference time to develop it.
[1956.42 --> 1960.66]  So, at the beginning, it was really conference-driven development, I call it.
[1961.18 --> 1967.02]  So, you write a talk and then you pitch for a talk and then you write the software to sustain that talk.
[1967.60 --> 1968.12]  I don't know.
[1968.18 --> 1970.78]  At the beginning, it was something like that to create some attention.
[1971.50 --> 1977.60]  However, it became the concept of, well, if you want something, it's a very open community.
[1977.60 --> 1980.82]  So, if you want something to happen, you should join the community.
[1981.36 --> 1981.48]  Okay?
[1981.68 --> 1984.72]  Does it make sense?
[1985.04 --> 1986.14]  It's an open community.
[1986.74 --> 1992.02]  So, this is the source of the problem with Express and Restify.
[1992.46 --> 2001.94]  So, those communities have a little bit stagnated over the years because a few individuals kept all the decision-making to themselves.
[2001.94 --> 2008.00]  And they did not open it up to everybody to contribute.
[2008.54 --> 2010.80]  So, instead of saying, oh, I have a bug.
[2011.00 --> 2012.80]  Instead of saying, hey, can you send me a fix?
[2013.04 --> 2015.44]  They were burning out trying to fix everybody's bug.
[2015.60 --> 2016.06]  Oh, wow.
[2016.16 --> 2017.74]  So, I have noticed that.
[2017.88 --> 2020.42]  So, I know that it was a non-sustainable model.
[2020.76 --> 2026.90]  The reason why Fastify instead embraced, you know, if you have a bug with my software, it's your problem, not mine.
[2028.12 --> 2028.50]  Okay?
[2028.78 --> 2030.04]  You have two choices now.
[2030.04 --> 2033.56]  Either you fix it yourself or you'll pay somebody to fix it.
[2034.32 --> 2040.04]  The only thing I'm happy to do is I'm happy to review your fix and guide you through getting the fix done.
[2040.68 --> 2042.42]  That's the only thing that I'm willing to do.
[2042.48 --> 2047.52]  I have a sustainable attitude for somebody who has 400 packages on NPM, for God's sake.
[2048.06 --> 2049.72]  Yes, exactly.
[2049.72 --> 2056.18]  So, I know there is a tiny fraction of those bugs that I need to fix myself.
[2056.74 --> 2057.10]  Okay?
[2057.20 --> 2058.72]  Because it's probably not...
[2059.36 --> 2062.44]  Some of those bugs are not for everybody to fix.
[2063.18 --> 2063.48]  Okay?
[2063.68 --> 2067.88]  There are probably some hard piece of code that I need to...
[2067.88 --> 2069.14]  A very few people can touch.
[2069.14 --> 2073.14]  So, there are not many, but they exist.
[2073.14 --> 2077.84]  As in every code base, there is that little file where you idle your secrets.
[2078.14 --> 2078.30]  Okay?
[2078.54 --> 2079.86]  So, you know, it's...
[2079.86 --> 2080.32]  Yeah, yeah.
[2080.46 --> 2081.38]  Under the rug.
[2081.46 --> 2082.44]  Don't look here.
[2082.78 --> 2084.38]  Like, we'll fix someday.
[2085.00 --> 2086.26]  Like, there be dragons.
[2086.54 --> 2087.46]  You know, all of that stuff.
[2087.46 --> 2091.28]  Apart from those type of files, which have been decreasing over the years.
[2091.28 --> 2091.74]  Right, right.
[2091.78 --> 2094.00]  No, it's good to encapsulate those files, right?
[2094.08 --> 2095.32]  Though it's good to have them, like...
[2095.32 --> 2096.40]  I'm even better than that.
[2096.48 --> 2098.60]  Usually, I put that stuff in a different module.
[2098.74 --> 2099.38]  Oh, nice.
[2099.46 --> 2102.08]  So, all Fastify dirty secrets are not in Fastify.
[2102.20 --> 2103.76]  The Fastify code base is very clean.
[2104.14 --> 2108.34]  But there is another module, which I'm not going to mention because it has a nice story on its own,
[2108.78 --> 2110.20]  which has all the secrets.
[2110.20 --> 2122.28]  And it's all the dirty code that will make a few of my Node.js colleagues be very nervous about some of the things that I'm doing with Node to make it behave like I want it to behave.
[2122.68 --> 2124.72]  But the end result is quite a nice user experience.
[2124.88 --> 2126.04]  So, I'm very happy about it.
[2126.28 --> 2127.04]  Oh, my God.
[2127.16 --> 2127.48]  All right.
[2127.56 --> 2129.28]  Well, that's great to know.
[2129.44 --> 2131.22]  Thank you for sharing that incredible story.
[2131.22 --> 2140.28]  So, we're going to take another break and we're going to get into some of the more kind of specific perks around these really key libraries in the Node.js ecosystem.
[2141.10 --> 2144.56]  And then, yeah, I'm still going to ask that burning question, like, where...
[2144.56 --> 2146.04]  Mateo, what do you think of Dino?
[2146.16 --> 2147.06]  So, stay tuned, kids.
[2147.12 --> 2147.92]  We'll be right back.
[2161.22 --> 2165.62]  This episode is brought to you by our friends at Square.
[2166.02 --> 2167.98]  Square is the platform that sellers trust.
[2168.46 --> 2175.32]  There is a massive opportunity for developers to support Square sellers by building apps for today's business needs.
[2175.74 --> 2178.48]  And I'm here with Shannon Skipper, Head of Developer Relations at Square.
[2178.90 --> 2182.88]  Shannon, can you share some details about the opportunity for developers on the Square platform?
[2183.20 --> 2183.62]  Yeah, absolutely.
[2183.84 --> 2186.52]  So, we have millions of sellers who have unique needs.
[2186.52 --> 2189.90]  And Square has apps like our point of sale app, like our restaurants app.
[2189.90 --> 2196.28]  But there are so many different sellers, tuxedo shops, florists, who need specific solutions for their domain.
[2196.54 --> 2207.60]  And so, we have a Node SDK written in TypeScript that allows you to access all of the backend APIs and SDKs that we use to power the billions of transactions that we do annually.
[2207.86 --> 2212.20]  And so, there's this massive market of sellers who need help from developers.
[2212.20 --> 2223.62]  They either need a bespoke solution built for themselves on their own Node stack where they are working with Square dashboard, working with Square hardware, or with the e-com, you know, what you see is what you get builder.
[2223.80 --> 2224.88]  And they need one more thing.
[2224.96 --> 2226.24]  They need an additional build.
[2226.56 --> 2234.58]  And then finally, we have the app marketplace where you can make a Node app and then distribute it so it can get in front of millions of sellers and be an option for them to adopt.
[2234.58 --> 2235.38]  Very cool.
[2235.48 --> 2235.72]  All right.
[2235.74 --> 2243.50]  If you want to learn more, head to developer.squareup.com to dive into the docs, APIs, SDKs, and to create your Square Developer account.
[2243.80 --> 2245.60]  Start developing on the platform seller's trust.
[2246.04 --> 2248.28]  Again, that's developer.squareup.com.
[2248.28 --> 2269.74]  Let's talk about Fastify and get into a little bit more of its features and its API.
[2269.74 --> 2274.34]  And I guess we can start off and probably presume that it's fast, given the name.
[2274.94 --> 2275.90]  So, okay.
[2276.00 --> 2277.04]  Fastify has two goals.
[2277.20 --> 2277.36]  Yep.
[2277.36 --> 2283.84]  One is to not create overhead compared to not what Node Core provides.
[2283.94 --> 2286.64]  Of course, it's not Rust, so it will have some overhead.
[2286.82 --> 2291.28]  But to minimize that overhead compared to what Node.js can provide.
[2291.44 --> 2292.64]  This is possible.
[2292.80 --> 2298.82]  And in fact, Node.js is as fast as the core HTTP module by providing a set of added features.
[2298.82 --> 2310.30]  So, given that focus on not adding overhead, we add a certain class of features that are very useful for most people developing Node.js applications.
[2310.30 --> 2315.48]  And these are the key things that you really want to stay in Fastify.
[2315.48 --> 2316.70]  Use Fastify for those.
[2316.70 --> 2319.22]  Probably not for the speed in most apps.
[2319.22 --> 2323.78]  However, Fastify will not let you down when your product starts scaling.
[2323.78 --> 2328.64]  So, it's having a very good developer experience without overhead.
[2328.64 --> 2329.24]  Nice.
[2329.24 --> 2337.58]  Is there anything that it is sacrificing to stay true to that in terms of like not adding too much overhead to the HTTP?
[2337.58 --> 2340.68]  There was more at the beginning than there is now.
[2341.10 --> 2344.62]  We have been able to do most things at this point in time.
[2344.62 --> 2350.62]  A key part of that experience has been to embrace the concept of plugins.
[2350.90 --> 2353.74]  And this is part of the great success of the framework.
[2353.74 --> 2359.70]  So, instead of middlewares, which is the most popular thing in Express land, we have the concept of plugins.
[2360.16 --> 2364.86]  Plugins can either add some functionality to the library.
[2365.22 --> 2371.62]  Oh, by the way, Fastify has one critical feature that Express does not have, nor Restify or CoA or others.
[2371.96 --> 2373.20]  It has a boot sequence.
[2373.20 --> 2378.60]  So, you can start a Fastify server and it's a synchronous startup sequence.
[2378.82 --> 2387.14]  So, you can do your database connections, do your all the things, do your rendering, pre-rendering if you want to do pre-rendering of your things.
[2387.78 --> 2389.22]  And it's all asynchronous.
[2389.52 --> 2396.82]  So, you don't need to have that complex code base at the beginning to bootstrap your node process, which can get very ugly.
[2397.42 --> 2402.84]  This is a critical feature because then it enables very fine-grained unit testing.
[2403.20 --> 2404.46]  of the library.
[2404.86 --> 2411.72]  So, this is the type of decisions where you can have a great user experience because testing is as important as the rest.
[2411.98 --> 2415.78]  Before we get into testing, though, could you explain to me why this boot sequence is important?
[2416.04 --> 2424.70]  Because, I mean, if I write my asynchronous code with some control flow, I could mimic that boot sequence, right?
[2424.70 --> 2426.44]  Yes, of course, of course.
[2426.44 --> 2428.46]  So, it is the typical problem.
[2428.46 --> 2439.30]  You want to start your application and then you need to connect to your Postgres, Mongo, Redis, MySQL database or whatever you want to connect to.
[2439.84 --> 2443.46]  Then you want to listen, to open the port and listen.
[2443.92 --> 2447.56]  Once you have all your dependencies, you know that all your dependencies are up and running.
[2447.56 --> 2456.64]  If you want to open the port to the Word and say, hey, I am exposing my, here I am available.
[2456.96 --> 2457.66]  It is the port.
[2458.06 --> 2460.14]  You can start sending me a HTTP request.
[2460.70 --> 2470.52]  The reason why you want your boot sequence to be controlled, fine-grained controlled, it's because you want to be able to unit test them.
[2470.52 --> 2472.58]  And this, I'm going back to testing.
[2472.90 --> 2478.40]  You want to be able to spin up multiple instances of your app, one for each of your tests.
[2479.12 --> 2494.46]  The predominant pattern back in 2016, 2015 was, and it still is to some extent in certain companies, is to have one global Express app or RESTify or HAPI that's more or less exposed as a singleton.
[2494.98 --> 2497.40]  And it's there to exist.
[2497.40 --> 2505.76]  And then you have the problem that when you run tests against that, you start having flaky tests or conflicting tests.
[2506.08 --> 2508.98]  Or you have problem with mocking, for example.
[2509.16 --> 2517.44]  You have problem with ensuring that your code is well written and tested and ends up being even reusable.
[2517.84 --> 2518.04]  Okay?
[2518.12 --> 2523.72]  Because then I can pack things up in a certain way and reuse them across several areas of my code.
[2523.72 --> 2528.28]  So, that is part of the reason why Fastify has a boot sequence.
[2528.92 --> 2533.62]  On top of that boot sequence, it loads multiple plugins one at a time.
[2534.08 --> 2537.18]  Now, they are loaded as a re-entering graph.
[2537.86 --> 2545.82]  So, you can load one plugin that can have its own dependencies, that can have their own dependencies, and so on and so forth.
[2546.22 --> 2546.36]  Okay?
[2546.56 --> 2548.56]  And they will all be loaded one at a time.
[2548.56 --> 2550.60]  And this becomes the hard things.
[2550.82 --> 2554.74]  All of these can be done written using async await or callbacks.
[2555.38 --> 2564.42]  And you can even await in between so that, oh, I want to wait that all this tree of plugins is loaded, and then I want to execute some more code.
[2564.52 --> 2566.46]  And all of this is seamlessly done by Fastify.
[2566.46 --> 2571.86]  And all of this can be, you know, nesting level of, several nesting levels of plugins.
[2572.06 --> 2573.10]  I've seen it in the wild.
[2573.58 --> 2577.28]  And it's probably the most important feature because it enables reuse.
[2577.74 --> 2587.50]  So, I can even develop a good chunk of my wall application as its own plugin, and then later on take, oh, I have all this part of my app.
[2587.50 --> 2591.96]  Instead of deploying inside my container, I can take and put it in a Lambda.
[2592.40 --> 2599.80]  And the only thing that I need to do is to change how I start on my server and use the Lambda adapter, and it's done.
[2600.30 --> 2604.58]  Or I want to take it and deploy it in a microservice, and then I can do that as well.
[2604.80 --> 2607.12]  It takes very little effort to move those things around.
[2607.66 --> 2613.74]  So, that type of flexibility, it's more or less almost unique in the frameworks.
[2613.74 --> 2618.76]  It's also the fact that that flexibility does not come at a huge performance penalty.
[2618.96 --> 2626.74]  So, you will still get more or less a consistent level of throughput throughout the, as much as you add complexity to a Fastify application.
[2627.46 --> 2635.08]  So, while Express, for example, decreased very quickly, even more when you add a lot of complexity, especially on the routing side.
[2635.22 --> 2641.24]  It has a very naive router, which is great simplicity because a lot of people can understand it very quickly how it works.
[2641.46 --> 2643.68]  However, it's also not great for Perf.
[2643.74 --> 2646.06]  It's the most naive router that you can implement.
[2646.46 --> 2650.26]  Just a set of regular expression and test them one at a time.
[2650.46 --> 2652.20]  Yeah, and order matters.
[2652.62 --> 2658.42]  In Fastify, order matters, but they are created in a shared data structure.
[2658.70 --> 2661.82]  So, it's called a tree, and it's a Radix Preface tree.
[2662.48 --> 2667.64]  And it's a complex data structure built more or less for this specific use case,
[2668.16 --> 2672.74]  and where all the routes are being inserted in, and it's actually pretty fast.
[2672.74 --> 2674.22]  What kind of a tree did you say it was?
[2674.44 --> 2678.74]  It's a Radix Prefix tree, and I'm going to pass it in the chat.
[2678.88 --> 2680.38]  Yeah, we'll have to put that in our show notes.
[2680.52 --> 2680.78]  So, okay.
[2680.88 --> 2683.40]  So, Express was really cool because of middleware, right?
[2683.44 --> 2686.08]  Everybody loved middleware, easy to use, easy to understand.
[2686.80 --> 2689.42]  You're saying not the best to scale, right?
[2689.42 --> 2694.20]  And so, could you explain more specifically, or even if you have to repeat yourself, I apologize,
[2695.12 --> 2702.72]  but the actual difference between middleware patterns and classic plug-in architecture pattern.
[2702.96 --> 2705.60]  What if I want something to still work like middleware, right?
[2705.68 --> 2705.96]  Perfect.
[2705.96 --> 2709.34]  Let's talk about how middleware works, okay?
[2709.76 --> 2713.90]  Whenever a request comes in, you add a bunch of middleware to your applications.
[2714.28 --> 2716.56]  Each one of them, they have this pattern.
[2716.98 --> 2720.96]  They say if something, and then they do whatever they need to do.
[2721.02 --> 2721.52]  Right, right.
[2721.52 --> 2721.82]  Okay.
[2722.48 --> 2730.14]  So, if you want to parse a body, if request.method equals equals equals body, I'm parsing a body.
[2730.52 --> 2730.86]  Okay?
[2731.20 --> 2738.32]  Or if this method matches a certain prefix, then I want all those routes, all those requests
[2738.32 --> 2740.32]  to be authenticated, for example.
[2740.50 --> 2741.08]  Okay?
[2741.36 --> 2741.72]  Correct.
[2741.72 --> 2750.12]  Now, a typical Express application has between 20 to 30 middleware installed before it reaches
[2750.12 --> 2750.94]  any of the routes.
[2750.94 --> 2751.66]  Mm-hmm.
[2752.04 --> 2752.34]  Okay?
[2752.76 --> 2760.66]  So, for each one of them, in order to fully implement that pattern, you need to have three
[2760.66 --> 2761.46]  function calls.
[2761.92 --> 2764.10]  So, it's three nested function calls for each one of them.
[2764.26 --> 2764.60]  Wow.
[2764.78 --> 2765.12]  Okay.
[2765.62 --> 2767.06]  I can see why this isn't scaling.
[2767.84 --> 2775.82]  So, now, if none of them triggers, or if some of them triggers whatever, you are at least
[2775.82 --> 2783.84]  talking about a call stack of more or less 100 call stack, 100 function nested within each
[2783.84 --> 2784.06]  other.
[2784.12 --> 2784.48]  Jeez.
[2784.70 --> 2785.08]  So, yeah.
[2785.16 --> 2787.88]  So, this is the reason why the middleware pattern is problematic.
[2787.88 --> 2789.28]  Let me clarify that, though, Matteo.
[2789.36 --> 2794.18]  Is it the middleware pattern, or is it Express's implementation of the middleware pattern?
[2794.34 --> 2802.60]  It's the middleware pattern as a whole in the sense of, you know, it comes, like, JavaScript
[2802.60 --> 2804.24]  does not have tail call optimization.
[2804.24 --> 2806.62]  If it had tail call optimization, things will be different.
[2806.88 --> 2806.92]  Okay?
[2807.06 --> 2807.28]  Right.
[2807.42 --> 2810.28]  But things are, with JavaScript being what it is...
[2810.28 --> 2812.40]  Didn't we implement that with ES6?
[2812.56 --> 2813.48]  No, it was not.
[2813.56 --> 2814.30]  That was crap.
[2814.40 --> 2816.48]  Every engine didn't do it, I know.
[2816.54 --> 2817.90]  No, they didn't do it.
[2817.98 --> 2819.14]  So, it's not there.
[2819.60 --> 2824.88]  So, anyway, the problem is that, you know, you put all those calls in the call stack.
[2824.88 --> 2825.18]  Okay?
[2825.62 --> 2833.34]  Now, the fundamental issue, instead, is what we do in Fastify is, if you want to have a
[2833.34 --> 2839.78]  certain class of routes authenticated, we only run the authentication logic for those
[2839.78 --> 2840.14]  routes.
[2840.38 --> 2843.98]  Is this because the data structure stores that information?
[2844.38 --> 2844.66]  Aha!
[2844.96 --> 2847.04]  So, this is the beauty of data structures, you know?
[2847.40 --> 2848.24]  You literally...
[2848.24 --> 2850.70]  It is like a logic path for your code.
[2851.06 --> 2854.86]  Without them, you're just running around blind, doing everything, checking all the
[2854.86 --> 2855.68]  things, you know?
[2855.80 --> 2856.10]  Yes.
[2856.18 --> 2860.36]  But, yeah, memorization and using keys, I mean, this is what it's made for.
[2860.42 --> 2866.82]  So, in Express and Restify and Coa and all those things, you have your routes, you have
[2866.82 --> 2869.10]  your middlewares coming in one at a time.
[2869.10 --> 2872.96]  You can only do that because you never know when you will encounter a route.
[2873.74 --> 2877.34]  So, with Fastify, the first thing that we do is routing.
[2877.96 --> 2880.40]  We decide what is the route that's going to match.
[2880.54 --> 2883.36]  Honestly, that's like what I want out of a web framework is routing.
[2884.34 --> 2884.72]  Yes.
[2884.86 --> 2887.72]  So, it decides what route you're going to hit.
[2888.06 --> 2888.28]  Okay?
[2888.36 --> 2890.12]  And this is one of the limitations of the frameworks.
[2890.44 --> 2896.00]  Like, in Express, you could do, oh, I'm routing a route, but if I can decide I'm not handling
[2896.00 --> 2899.42]  this payload, I can bump it to the next one in the chain.
[2899.66 --> 2899.84]  Yeah.
[2900.26 --> 2901.58]  In Express, you could do that.
[2901.66 --> 2902.88]  You can't do it in Fastify.
[2903.26 --> 2906.60]  In Fastify, whenever route is decided settled, it's settled.
[2907.00 --> 2908.06]  You can't unsettle it.
[2908.60 --> 2911.52]  And this is one of the limitations that we were talking about.
[2911.52 --> 2912.90]  That you asked me, there is limitation.
[2913.06 --> 2916.02]  This is one of the decisions that we had to take.
[2916.10 --> 2917.36]  Well, so what happens?
[2917.50 --> 2919.04]  I mean, because that's the beauty of Express.
[2919.04 --> 2920.74]  You can just go next, right?
[2920.98 --> 2921.86]  Yes, exactly.
[2922.16 --> 2923.24]  You can do that in Fastify.
[2923.42 --> 2926.84]  So, does that put that onus back onto the caller?
[2926.84 --> 2930.30]  So, what we do is that you call it with a given route.
[2930.70 --> 2930.86]  Okay?
[2931.30 --> 2938.56]  So, in that route, we decide what code is going to be executed and what we call them lifecycle
[2938.56 --> 2939.08]  hooks.
[2939.72 --> 2944.90]  So, essentially, we do something like when we receive a request, something before the
[2944.90 --> 2948.08]  handler is called, we all do something after the body is parsed.
[2948.12 --> 2950.84]  So, there are moments where you can inject your code in the sequence.
[2950.84 --> 2953.72]  And then we execute your function code.
[2953.82 --> 2956.40]  And then you can execute some more things at the end.
[2956.86 --> 2957.64]  And that's the cycle.
[2957.86 --> 2958.00]  Okay?
[2958.44 --> 2960.34]  So, it's very straightforward.
[2960.70 --> 2962.78]  And there are no weird turns here.
[2962.98 --> 2965.94]  So, the weird turns are exception paths and so on.
[2966.02 --> 2968.54]  So, in this way, the code can be very streamlined.
[2969.04 --> 2973.54]  The logic that I cannot write, and you were right, is there's no next.
[2974.06 --> 2974.42]  Okay?
[2974.54 --> 2977.42]  In the sense of the next level, there is a done.
[2977.42 --> 2982.94]  We call it done in Fastify to differentiate of that because it's, if you resolve, or even
[2982.94 --> 2986.16]  when you resolve a promise, you move to the next step.
[2986.46 --> 2989.44]  But there is no, you cannot fork it in that sense.
[2989.66 --> 2995.88]  So, let's say that you have a route that, I don't know, matches, you put something around
[2995.88 --> 2997.08]  that matches certain IDs.
[2997.64 --> 3005.02]  And you want to say, oh, if I cannot find this in the database, call, move to this other
[3005.02 --> 3007.30]  route that generates it on the fly.
[3007.42 --> 3007.72]  Okay?
[3007.78 --> 3008.36]  Or something.
[3008.94 --> 3010.22]  You can do that in Fastify.
[3010.32 --> 3014.26]  You will need to find some other different pattern to implement this same logic, which
[3014.26 --> 3016.14]  is probably a little bit more complex.
[3016.54 --> 3023.38]  But nevertheless, it enables us to minimize the amount of checks that we need to execute
[3023.38 --> 3024.42]  to reach your route.
[3024.42 --> 3033.52]  So, a complex 30-something, 30 or 50-something hook multiplied by three become a smaller, maybe
[3033.52 --> 3035.62]  510 multiplied by two.
[3035.96 --> 3039.28]  So, we have shrinked completely the call stack.
[3039.76 --> 3042.86]  And this is part of the reason why Fastify is good.
[3043.54 --> 3050.42]  And Fastify can maintain that level of performance while providing a good level of user experience.
[3050.42 --> 3051.62]  That makes a lot of sense.
[3051.78 --> 3058.14]  And so, like, so Fastify does borrow from Express and Happy a little bit.
[3058.26 --> 3059.06]  Yeah, both of them.
[3059.12 --> 3059.36]  Yes.
[3059.50 --> 3062.00]  So, I mean, how big of a transition is it for users?
[3062.14 --> 3065.22]  Kind of like, like, for example, like, I don't need to think about Express.
[3065.36 --> 3067.42]  Like, I can use Express without looking at the docs.
[3067.60 --> 3068.18]  You know what I mean?
[3068.60 --> 3070.08]  It's been so many years, right?
[3070.08 --> 3073.88]  It's like the go-to hello world for Node is Express for me.
[3074.22 --> 3076.68]  Not even Koa, as much as I love Koa.
[3076.98 --> 3078.84]  If I use Koa, I have to look at the docs.
[3079.26 --> 3081.70]  If I use Express, I don't have to look at the docs, you know?
[3081.90 --> 3084.08]  And so, how do you translate that?
[3084.16 --> 3087.72]  How do you bring that very familiar experience into the Fastify API?
[3088.18 --> 3089.72]  So, we have a bunch of things, okay?
[3090.16 --> 3094.92]  So, first of all, if you are migrating from an Express app, you can actually just run your
[3094.92 --> 3096.12]  Express app on top of Fastify.
[3096.92 --> 3098.72]  What about all those call stacks?
[3098.72 --> 3104.16]  Yeah, well, you know, you can migrate your things a little bit whenever you're ready,
[3104.40 --> 3104.62]  okay?
[3104.66 --> 3105.04]  Interesting.
[3105.26 --> 3106.04]  Module by module.
[3106.46 --> 3111.14]  There is a module called Fastify Express, and it enables you to mount a full Express application
[3111.14 --> 3117.38]  on top of Fastify model, because that level of routing and checks is so flexible.
[3117.58 --> 3119.92]  Well, what's the actual benefit of doing that, though?
[3120.16 --> 3121.86]  So, it's a migration benefit.
[3122.24 --> 3126.98]  So, let's say that you want to migrate your application from using Express to Fastify.
[3126.98 --> 3128.28]  You can do that.
[3128.72 --> 3132.54]  Or maybe there is a chunk of your application that you don't want to migrate for whatever
[3132.54 --> 3136.98]  reason, and you can keep it there and use it the rest somewhere else.
[3137.04 --> 3141.12]  I've seen there's a few companies that have done this, because it's simpler doing that
[3141.12 --> 3143.76]  than provide that piece, essentially.
[3144.00 --> 3144.30]  Okay.
[3144.78 --> 3145.70]  That's very cool.
[3145.88 --> 3147.22]  I love the migration benefit.
[3147.36 --> 3149.18]  I mean, that's very forward-thinking.
[3149.18 --> 3150.18]  Yes.
[3150.18 --> 3152.42]  We introduced this on Fastify V3.
[3152.56 --> 3157.50]  That was not possible in Fastify V2, but we reached that level in Fastify V3 last year.
[3157.50 --> 3159.80]  For us, we're using Nest.js.
[3159.88 --> 3162.10]  And we talked about Nest actually last week on the show.
[3162.36 --> 3168.22]  And it does, by default, use Express under the hood, but it can easily use Fastify as well.
[3168.48 --> 3169.22]  Yeah, it's pretty good.
[3169.32 --> 3172.92]  And Nest is not my loaf of bread, as you say.
[3173.44 --> 3177.52]  But if you're looking for that type of experience, it's a great framework.
[3177.52 --> 3182.08]  I'm typically doing a lot of more custom things to benefit from a framework like Nest.
[3182.52 --> 3186.60]  But usually, it can be a good choice for a certain class of products.
[3187.22 --> 3193.56]  So going back to the Express thingy, so the API is very familiar, however, with a few key
[3193.56 --> 3194.00]  differences.
[3194.36 --> 3198.86]  First of all, it supports Async Await out of the box, which is not there with Express.
[3199.60 --> 3204.36]  If you try to use Async Await with Express out of the box, you're going to get some very,
[3204.46 --> 3206.10]  very bad surprises very soon.
[3206.10 --> 3209.10]  So that's the problem that everybody has.
[3209.62 --> 3211.18]  So that is not being evolved.
[3211.50 --> 3218.24]  OK, it's Express 4, which is the current released version and stable version of Express, was
[3218.24 --> 3222.28]  released seven years ago and, you know, not updated in the last two years.
[3223.72 --> 3226.62]  It's extremely stable, as you say.
[3226.86 --> 3227.04]  Yeah.
[3227.24 --> 3229.32]  But it's also not being...
[3229.32 --> 3229.86]  Yeah, yeah, yeah.
[3229.88 --> 3230.94]  It's quite stagnant.
[3231.04 --> 3231.74]  Yeah, I know.
[3232.00 --> 3233.30]  It's stagnating at the minute.
[3233.54 --> 3233.74]  OK.
[3233.74 --> 3239.34]  What's familiar if I need to do something really quickly and it's prototyping code?
[3239.70 --> 3245.88]  Funnily enough, if you open up the docs, OK, it's actually very, you know, it will get
[3245.88 --> 3246.86]  a sense of familiarity.
[3247.54 --> 3252.32]  The snippet is actually very, very similar to what you would use with Express.
[3252.32 --> 3256.74]  OK, so even if Express with the callback version of it.
[3257.24 --> 3257.42]  OK.
[3257.86 --> 3260.82]  And I'm going to pass the callback snippet in here.
[3261.58 --> 3263.24]  So, oh, it didn't render correctly.
[3263.74 --> 3266.20]  But you can find it on the website.
[3266.50 --> 3267.72]  So it's in there.
[3267.88 --> 3269.32]  But it also supports Async Await.
[3269.32 --> 3271.92]  So you can just return from your Async function.
[3272.54 --> 3277.80]  And if you return an object, that will automatically be rendered as a JSON, which is essentially even
[3277.80 --> 3279.30]  simpler than using .send.
[3279.36 --> 3279.98]  No, that's cool.
[3280.12 --> 3282.52]  Well, no, Matteo, I mean, Festify is awesome.
[3282.68 --> 3285.08]  Pino, so I haven't used Festify in production.
[3285.72 --> 3286.96]  I've been following the project.
[3287.20 --> 3288.04]  It's very cool.
[3288.04 --> 3291.32]  I can't wait to try it, like, at a real company.
[3291.70 --> 3293.84]  But I've been using Pino, and I love Pino.
[3294.20 --> 3296.16]  And Pino is just, it's incredible.
[3296.44 --> 3297.98]  And the ecosystem around it's great.
[3298.14 --> 3300.16]  It's very easy to create your own abstractions.
[3300.74 --> 3301.82]  Really low overhead.
[3302.62 --> 3304.74]  And, yeah, log management is hard, people.
[3305.02 --> 3306.06]  Don't diss it, OK?
[3306.34 --> 3308.24]  A great interview question, I think.
[3308.50 --> 3309.26]  Oh, yes.
[3309.46 --> 3313.80]  By the way, I don't ask logging when I'm interviewing candidates, OK?
[3313.82 --> 3316.04]  So I do interview a lot of candidates at NearForm.
[3316.04 --> 3317.74]  So we are adding a lot at the moment.
[3317.74 --> 3319.00]  We are adding so many people this year.
[3319.34 --> 3320.28]  We are keep adding more.
[3320.56 --> 3323.64]  So if you want to join nearform.com slash careers, have fun.
[3323.80 --> 3326.42]  Good place to write JavaScript and learn from people.
[3326.72 --> 3328.34]  Yeah, and Festify and Pino.
[3328.90 --> 3332.98]  So going back to Pino, which is actually one of the nicest things,
[3333.40 --> 3337.76]  is that we are actually shipping a new major release of Pino, Pino 7,
[3338.04 --> 3343.52]  which I have been writing on my newsletter for probably the last six months now.
[3344.12 --> 3347.08]  So it took a long time to get there.
[3347.08 --> 3354.12]  We are moving part of the logic of producing those logs to work at threads.
[3354.46 --> 3361.92]  But does that mean you're going to require certain, like, you have to have this node version and this OS and whatever, you know?
[3361.94 --> 3363.48]  It's supported in Node 12+.
[3363.48 --> 3365.16]  So, yes, it's your requirement.
[3365.24 --> 3365.92]  Yeah, yeah, I'm saying.
[3366.06 --> 3368.86]  You can't use it with Node like 11 or 10.
[3368.86 --> 3372.92]  Well, yes, but you should not be using those anyway because they're people there.
[3372.92 --> 3372.94]  I agree.
[3372.94 --> 3373.78]  I'm with you.
[3373.94 --> 3374.74]  100% with you.
[3374.90 --> 3379.72]  But believe it or not, you and I both know there's lots of servers in the world.
[3379.84 --> 3380.72]  Oh, don't tell me.
[3381.36 --> 3383.12]  We were working on one this morning.
[3383.56 --> 3384.02]  Yeah, yeah.
[3385.22 --> 3390.90]  Somebody opened an issue during this show that they were running Node 6 in production and they were just like...
[3390.90 --> 3391.96]  Oh, my God.
[3392.48 --> 3393.04]  Yeah.
[3393.18 --> 3395.54]  Where's your security and compliance team, you know?
[3395.64 --> 3398.12]  But anyways, so, Mateo, awesome projects.
[3398.22 --> 3401.08]  Thank you so much for all the incredible work that you do in the open source community.
[3401.08 --> 3403.10]  And you give back a lot in terms of teaching.
[3403.10 --> 3410.58]  You've got some really great courses that I think helped me understand promises and async code a lot better.
[3410.58 --> 3418.06]  Like, we'll link those in the show notes, but Mateo's got a lot of really great material on just asynchronousness in JavaScript.
[3419.46 --> 3419.94]  Asynchronousness.
[3420.44 --> 3427.86]  So, Mateo, before we end this show, we promised everyone we were going to talk about Dino briefly, if that's even possible.
[3428.12 --> 3428.42]  Okay.
[3428.66 --> 3430.62]  I'm dying to hear.
[3430.78 --> 3434.58]  I have yet to actually have this conversation with a nodi, like a hardcore nodi.
[3434.58 --> 3439.76]  I've had this conversation with lots of people in the JavaScript community, yet to have this conversation with a Node TSC.
[3439.76 --> 3440.78]  What do you think?
[3441.18 --> 3442.58]  I would say a few things.
[3442.92 --> 3446.40]  So, the first one is I did not like at all.
[3447.22 --> 3448.46]  Why am I not the price?
[3448.54 --> 3448.88]  Just kidding.
[3448.94 --> 3449.24]  Just kidding.
[3449.66 --> 3465.96]  The marketing approach that they've taken in the first few period of the years that have been written communicates about essentially that we're stating falsehood or even pointing out, you know, certain things.
[3465.96 --> 3477.22]  And just telling a very specifically framed part of the story that did not really reflect reality or did reflect some part of the reality without telling the rest.
[3477.38 --> 3482.74]  I have been not happy about the way they launched it.
[3483.06 --> 3483.18]  Okay.
[3483.64 --> 3484.48]  Let me be.
[3484.64 --> 3487.76]  Not the way that Ryan did the talk at JSConf.
[3488.00 --> 3488.64]  That was fine.
[3488.94 --> 3489.22]  Okay.
[3489.40 --> 3490.10]  The talk was good.
[3490.10 --> 3492.82]  And I think he was spot on on most of the things that he said.
[3493.38 --> 3499.08]  What I did not, the follow-on narrative on the project, it was not good.
[3499.20 --> 3503.28]  They changed the narrative lately and starting focusing on their own specific features.
[3503.78 --> 3504.60]  I like that.
[3504.72 --> 3504.90]  Okay.
[3504.90 --> 3516.46]  I think you should be focusing on your own features and what you can do for the community and not on, you know, throwing rocks at others without even justifying them, to be honest.
[3516.60 --> 3524.96]  It's quite hard to praise new work without totally pooping on old work, right?
[3525.12 --> 3527.74]  I mean, it takes class.
[3527.74 --> 3528.74]  It takes finesse.
[3528.84 --> 3529.52]  It takes effort.
[3530.26 --> 3537.22]  And sometimes even when people aren't intending to poo-poo on someone else's parade, like, they do so, right?
[3537.28 --> 3539.26]  It's just, it's nerd sniping.
[3539.38 --> 3540.92]  It's what we experience.
[3541.36 --> 3542.82]  And I'm sorry about that, you know.
[3543.22 --> 3545.34]  And there's no excuses there.
[3546.02 --> 3555.94]  But that being said, if we kind of move the conversation to focus on the API itself and the actual, like, the actual code, like, what are your thoughts there?
[3555.94 --> 3559.52]  Just, you know, we are driving a car with three wheels, right?
[3559.62 --> 3566.06]  There was definitely some architectural and fundamental decisions that were made, like even Ryan's talk covered.
[3566.28 --> 3566.96]  Oh, yeah.
[3567.38 --> 3570.30]  That have hampered the project's success.
[3570.60 --> 3573.46]  Nobody knew it was going to take off in the way that it did, right?
[3573.56 --> 3575.48]  And similar to JavaScript, right?
[3576.18 --> 3577.24]  Yes, exactly.
[3578.00 --> 3580.62]  I am not a fan of the approach, okay?
[3580.62 --> 3587.48]  If I code something that's not correct and that I think is not correct, I go in and try to fix what I did.
[3587.96 --> 3589.14]  It did something else, okay?
[3589.22 --> 3592.90]  That's the type of the part of the approach that I am not fond of.
[3593.22 --> 3594.74]  The project itself is amazing.
[3594.92 --> 3595.60]  Like, Dino is amazing.
[3595.70 --> 3597.78]  It's an amazing piece of software, okay?
[3597.92 --> 3599.58]  It's really great.
[3599.58 --> 3610.22]  So, it's actually being the force that was necessary to Node to unlock itself from some of the mud that it was in.
[3610.58 --> 3618.58]  Thanks to Dino existing, Node.js could do a lot of things and move faster and remove a lot of the discussion.
[3618.92 --> 3623.42]  And at some point, we were sitting a little bit on ourselves.
[3623.76 --> 3625.16]  We were, you know, oh, we are Node.
[3625.28 --> 3625.94]  We are the TSC.
[3626.16 --> 3626.64]  We are great.
[3626.78 --> 3627.22]  Blah, blah, blah, blah.
[3627.30 --> 3628.42]  There was a little bit of that.
[3628.42 --> 3630.28]  But that's gone.
[3630.74 --> 3634.56]  And we are back shipping things and improving things and maintaining things.
[3635.42 --> 3639.92]  So, in fact, some of the stuff, like a lot of the drama is not existing even anymore.
[3640.06 --> 3643.24]  There was a lot of drama in some years on the Node community.
[3643.52 --> 3644.60]  That's gone, okay?
[3645.10 --> 3646.32]  So, it's no drama.
[3646.56 --> 3648.54]  People are doing things, contributing.
[3648.94 --> 3649.90]  Who is contributing?
[3650.14 --> 3652.18]  Maybe some other people are not contributing.
[3652.38 --> 3655.90]  But more or less, their level of contribution has stayed the same.
[3655.90 --> 3660.16]  And new people went, some people went away, new people came in.
[3660.56 --> 3662.42]  It's still a good project to contribute to.
[3662.62 --> 3663.90]  And there is a lot of work to do.
[3664.36 --> 3665.52]  Things are moving really well.
[3665.64 --> 3667.44]  So, it was a great benefit for Node.
[3667.44 --> 3679.26]  And my main take here is how much time it will take for Node to get a bunch of the features that makes Dino really, really useful.
[3679.44 --> 3679.72]  Okay?
[3679.86 --> 3681.20]  In which Dino is better.
[3681.58 --> 3683.84]  And how much time it will take Node to catch up there.
[3684.10 --> 3686.08]  Dino is better in certain areas.
[3686.22 --> 3689.02]  For example, web standard compatibility and so on and so forth.
[3689.42 --> 3690.68]  But the ecosystem is not there.
[3690.80 --> 3691.72]  NPM is not there.
[3691.72 --> 3696.56]  You have a massive amount of ecosystem network value on Node.
[3696.68 --> 3700.00]  And Node needs to keep existing to support the JavaScript community.
[3700.58 --> 3706.36]  So, all those people that started using, oh, when Dino came out, oh, Node modules boom.
[3706.94 --> 3708.20]  And Node is dead.
[3708.40 --> 3709.42]  And all those things.
[3709.70 --> 3709.90]  Yeah.
[3709.96 --> 3713.82]  I mean, people who say that, I'm like, Jesus Christ, have you looked at the internet?
[3714.38 --> 3717.84]  Like, jQuery is still the most popular framework in the world.
[3718.00 --> 3720.96]  And React is like, what, 2% of websites, if even?
[3720.96 --> 3723.80]  I mean, it's just that web devs are in a bubble.
[3724.08 --> 3726.22]  And they don't understand the arc of software.
[3726.56 --> 3729.76]  Like, software gets shipped, written, never updated.
[3730.32 --> 3730.42]  Okay?
[3730.90 --> 3731.10]  Yay!
[3732.00 --> 3737.48]  But anyways, so just real quick, we'll link to how to get started as a Node contributor.
[3737.76 --> 3739.66]  There's some really great, like, guides.
[3740.14 --> 3740.56]  Yes.
[3741.54 --> 3742.66]  Node2do.org.
[3742.80 --> 3745.10]  C++ do you need to know versus JavaScript?
[3745.56 --> 3747.60]  Like, do you need to even know C++?
[3747.92 --> 3749.12]  Can you just know JavaScript?
[3749.12 --> 3750.68]  You can just know JavaScript.
[3750.96 --> 3754.30]  But you might be willing to learn something as possible.
[3754.54 --> 3755.00]  Yeah, yeah.
[3755.54 --> 3756.10]  I don't know.
[3756.38 --> 3757.28]  I learned it.
[3757.34 --> 3759.00]  I feel like I'm relearning it now.
[3759.40 --> 3763.06]  But, like, you know, it's a very good investment, I think, you know, learning how to write C++.
[3763.42 --> 3767.56]  Learning about memory management will just, it'll change your whole framework as an engineer.
[3767.56 --> 3772.64]  So it's good, good fundamentals if and when you're ready for that next step, but you don't have to.
[3773.14 --> 3774.94]  So, Matteo, where can people find you online?
[3775.24 --> 3777.34]  And then there's Node comps coming up, right?
[3777.54 --> 3777.92]  Yes.
[3777.98 --> 3778.80]  So, a few things.
[3778.92 --> 3782.32]  So, you can find me online at twitter.com slash Matteo Collina.
[3782.32 --> 3787.84]  And, yeah, just, you know, reach out and ask me whatever question you want.
[3788.40 --> 3790.92]  So, I have a newsletter, so you can check that.
[3791.06 --> 3795.74]  It's, if you like me writing and rambling about Node.js, that's probably the right place.
[3796.16 --> 3805.72]  This is a quick announcement because we have Node.com on the 18th of October, from the 18th to the 21st of October.
[3805.72 --> 3808.92]  So, it's 10 days from now, a little bit more than 10 days.
[3809.32 --> 3810.36]  So, it's 10 days from now.
[3810.88 --> 3812.90]  You can definitely, you want definitely to attend.
[3813.12 --> 3823.72]  It's packed off Node core contributors and Node users that are going to speak on how they improve the platform or use the platform that you all know and love.
[3823.88 --> 3825.46]  So, it's a great conference.
[3825.74 --> 3827.44]  I can tell because I assembled the agenda.
[3827.64 --> 3829.86]  So, I can definitely tell it's a great agenda.
[3830.32 --> 3831.84]  I ended up running most of it.
[3832.28 --> 3834.64]  So, it's my major to-do list.
[3834.64 --> 3835.16]  Yeah.
[3835.72 --> 3836.70]  No, that's great.
[3836.82 --> 3839.50]  Well, thank you again for everything that you've done for our community.
[3840.34 --> 3846.26]  All the contributions, all the great software, for making my code better and everyone else's that uses your software.
[3846.98 --> 3851.14]  And, yeah, I'm off to go look for that module now with all the secrets at Fastify.
[3851.42 --> 3852.94]  You said Fastify had no dependencies.
[3853.10 --> 3855.04]  So, is this module like an internal module?
[3855.38 --> 3855.76]  No, no.
[3855.82 --> 3857.06]  Fastify has plenty of dependencies.
[3857.40 --> 3858.44]  Oh, okay, okay, okay.
[3858.46 --> 3859.66]  I was like, wait a second here.
[3859.70 --> 3860.70]  I thought it had dependencies.
[3860.86 --> 3861.30]  No, no.
[3861.48 --> 3862.42]  Okay, so I misunderstood.
[3862.78 --> 3864.32]  If you find it, shh.
[3864.32 --> 3865.34]  If I find it, shh.
[3865.34 --> 3866.04]  Okay, got it.
[3866.08 --> 3867.54]  That's the name of the package, actually.
[3867.70 --> 3868.76]  It's shh, you know.
[3870.24 --> 3871.12]  All right, everyone.
[3871.48 --> 3872.68]  Thank you again, Mateo.
[3872.80 --> 3873.72]  It's a wrap, kids.
[3873.88 --> 3874.82]  Talk to you next week.
[3874.94 --> 3875.28]  Bye.
[3875.72 --> 3876.12]  Bye.
[3876.44 --> 3876.82]  Bye-bye.
[3876.82 --> 3882.60]  That's JS Party for this week.
[3882.60 --> 3883.28]  Thanks for listening.
[3883.28 --> 3885.70]  We have some awesome guests queued up.
[3885.70 --> 3886.46]  Nader Dabbit.
[3886.46 --> 3887.54]  Chris Ferdinandi.
[3887.80 --> 3888.74]  Rachel Neighbors.
[3888.98 --> 3889.56]  Rich Harris.
[3889.78 --> 3890.32]  And more.
[3890.52 --> 3892.90]  If you haven't subscribed at this point, what are you waiting for?
[3893.34 --> 3896.06]  And of course, we would love for you to help spread the word about the show.
[3896.64 --> 3899.36]  Word of mouth is the number one way people find out about us.
[3900.24 --> 3903.72]  JS Party is produced by Jared Santo with music by Breakmaster Cylinder.
[3903.72 --> 3905.82]  We are brought to you by our awesome sponsors.
[3906.22 --> 3908.84]  Special thanks to Fastly, LaunchDarkly, and Leno.
[3909.74 --> 3916.46]  Next up on the pod, we are talking Web3, DApps, Ethereum, and all that craziness with Nader Dabbit.
[3916.68 --> 3918.38]  We'll have that one ready for you next week.
[3918.38 --> 3948.36]  We'll be right back.
