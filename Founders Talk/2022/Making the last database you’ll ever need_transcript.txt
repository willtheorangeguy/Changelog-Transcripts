[0.00 --> 8.58]  What's up? This is Founders Talk. I'm Adam Stachowiak. Thank you for tuning in here on
[8.58 --> 15.84]  Founders Talk. I share one-on-one conversations I have with founders, CEOs, and makers about their
[15.84 --> 20.54]  journey, their lessons learned, and what it takes to build and run their business. Today,
[20.62 --> 26.36]  I'm joined by Sam Lambert, CEO of PlanetScale. Now that PlanetScale is in general availability,
[26.78 --> 29.98]  I had to get Sam on the show to talk about the behind the scenes of building this database
[29.98 --> 35.50]  platform, how this is the last database you'll ever need, and what that means for developers.
[35.98 --> 42.10]  It's open source underpinnings with Vitesse, and Sam also teases what's to come. Big thanks to Fastly,
[42.18 --> 47.50]  our bandwidth partner listeners around the globe. Enjoy speedy downloads of our MP3s,
[47.70 --> 51.48]  and that's all because of Fastly. Learn more at Fastly.com.
[51.48 --> 63.30]  This episode is brought to you by our friends at FireHydrant. FireHydrant is the reliability
[63.30 --> 69.40]  platform for every developer. Incidents impact everyone, not just SREs. FireHydrant gives teams
[69.40 --> 74.04]  the tools to maintain service catalogs, respond to incidents, communicate through status pages,
[74.04 --> 79.32]  and learn with retrospectives. What would normally be manual, error-prone tasks across the entire
[79.32 --> 84.60]  spectrum of responding to an incident? This can all be automated in every way with FireHydrant.
[84.60 --> 90.16]  FireHydrant gives you incident tooling to manage incidents of any type with any severity with
[90.16 --> 96.06]  consistency. You can declare and mitigate incidents all inside Slack. Service catalogs allow service
[96.06 --> 100.78]  owners to improve operational maturity and document all your deploys in your service catalog.
[101.34 --> 105.92]  Incident analytics like to extract meaningful insights about your reliability over any facet of
[105.92 --> 110.54]  your incident or the people who respond to them. And at the heart of it all, Incident Runbooks,
[110.60 --> 115.66]  they let you create custom automation rules to convert manual tasks into automated, reliable,
[116.00 --> 121.30]  repeatable sequences that run when you want. Create Slack channels, Jira tickets, Zoom bridges
[121.30 --> 126.34]  instantly after declaring an incident. Now your processes can be consistent and automatic.
[126.34 --> 131.24]  Try FireHydrant free for 14 days. Get access to every feature. No credit card required.
[131.24 --> 135.62]  Get started at FireHydrant.io. Again, FireHydrant.io.
[149.30 --> 154.64]  Well, Sam, welcome to Founders Talk. It's been a bit. We've talked a few times, at least once,
[154.70 --> 159.38]  let's say. Big fan of what you're doing to plan to scale. Big fan of your journey to get here.
[159.38 --> 164.62]  The name says it all, right? Planet scale. Isn't that cool when you have like a brand that says
[164.62 --> 169.84]  exactly what your intentions are? Absolutely. Yeah. Yeah. And I think people have made many
[169.84 --> 176.34]  comments about the name and the ambition that the name kind of implies. And I like it. It's not easy
[176.34 --> 180.98]  to make a logo with the planet. I'll tell you that because there's many planet themed logos,
[180.98 --> 186.00]  but I do really like the name and it certainly kind of piques people's interest. Certainly.
[186.00 --> 192.78]  Mm hmm. Everybody. I mean, at least me, I'll say me as in everybody. I like space a lot. I'm a real
[192.78 --> 197.84]  big fan of physics. I'm a real big fan of the very, very big and the very, very small and the
[197.84 --> 203.14]  examination of that, which is physics, right? Yes. Metaphysics. You've got interstellar physics.
[203.34 --> 207.42]  You've got all sorts of different stuff you're looking at when it comes to that. But I think planets,
[207.64 --> 211.48]  the planet idea totally makes sense for what you're doing with planet scale.
[211.48 --> 216.82]  When I've talked to many different entrepreneurs here on the show, the big issue tends to be
[216.82 --> 223.16]  the database at some point, right? You might start someplace and pick something off the shelf that
[223.16 --> 227.80]  works, or maybe you don't put a lot of thought into it. And I think over time, the entrepreneur
[227.80 --> 233.82]  and developers interaction with software creation and product development is evolving and maturing,
[233.82 --> 242.48]  but you tend to begin somewhere that is developer friendly, easy to deploy, easy-ish to manage for
[242.48 --> 247.40]  the most part, right? And then hopefully provides the end experience that your customers need and want.
[247.82 --> 255.56]  But I think what happens at today's scale from, say, a startup to a company like whomever that will
[255.56 --> 262.48]  eventually IPO, somewhere along that road, you hit some major bumps, typically in the database part,
[262.48 --> 268.40]  right? So that's what planet scale is trying to do to solve that big problem. How did you become
[268.40 --> 271.28]  involved in planet scale? What's your journey to here?
[271.90 --> 277.46]  So exactly what you said completely resonates with me, and I've lived through it a couple of times.
[277.70 --> 284.32]  And it's also very much the journey that our customers have been through. So every day,
[284.32 --> 290.84]  multiple times a day, we speak to engineers or founders and people that are scaling their business,
[290.84 --> 297.44]  and they picked the database that was right for day one, which is like exactly what you should do.
[297.76 --> 305.14]  Pre-optimizing too much for a future that you may not even earn is like unwise, right? You shouldn't do it.
[305.50 --> 312.04]  You've got to build for today, get that first user, get the first 10, 100,000, 10,000,
[312.04 --> 319.02]  million, maybe even a billion, if you're very lucky. And so there is a bunch of tools that there's a
[319.02 --> 324.28]  bunch of databases out there that are appropriate for that, right? Like two clicks, you're up and
[324.28 --> 331.34]  running, super easy, the constraints are just not there, or they're hidden, or the trade-offs that
[331.34 --> 337.48]  early database has made is like super user-friendly, super developer-friendly, and it makes it very easy
[337.48 --> 343.64]  to build upon. But then that doesn't last. Like you remember the old days of Heroku, right? Like,
[344.28 --> 349.64]  and still probably is one of the most default places to start beginning and building an application.
[349.64 --> 350.24]  It is.
[350.38 --> 355.86]  But then the Heroku tax kicks in and things get expensive. Like I've spoken to multiple people
[355.86 --> 363.46]  that run everything on Heroku, except the database, which like talks out to Amazon RDS or whatever,
[363.46 --> 367.86]  because the database is the first thing that crumbles and then you've got to do more. And I
[367.86 --> 373.20]  think this is kind of a fairly depressing state of the world, but I'll wind back and I'll get to,
[373.30 --> 378.36]  like, I'll get to the overall answer. So how I came to know Planetscape, well, I've been in databases
[378.36 --> 384.72]  for a long time. And I was a database engineer sort of by trade. And I joined GitHub in 2013.
[385.26 --> 391.82]  It was an amazing company. It was just growing like a weed, growing incredibly. Actually,
[391.82 --> 397.10]  I was thinking about this the other day. GitHub Series A was at like $100 million.
[397.58 --> 397.68]  Yeah.
[397.86 --> 402.64]  Like people are talking about how insane the funding environment is right now. That happened in 2012,
[402.86 --> 408.18]  2013, I think. Yeah, I think it just happened when I joined. So nearly 10 years ago,
[408.90 --> 414.54]  that valuation for Series A was incredible. So this company was just so special, so much going on.
[414.60 --> 414.90]  Right.
[414.90 --> 420.20]  So much growth, loved by developers, but we were having database problems. And that's why I joined
[420.20 --> 428.18]  to work on those issues. And we kind of never resolved them. I mean, you just about put scale
[428.18 --> 433.30]  problems to bed, no matter what the tool is, like no matter what part of the stack, you fix those scale
[433.30 --> 439.50]  problems. And if you're in a high growth company, I mean, six months to a year, all of those decisions
[439.50 --> 446.10]  you made to scale for this order of magnitude are just completely out of date again. And you're back
[446.10 --> 454.30]  at it. And this is a undifferentiated journey for all companies that are scaling. And we,
[454.64 --> 458.98]  you know, eventually kind of, I ended up being lucky enough to run the infrastructure team,
[459.32 --> 464.38]  the GitHub and the platform team and became quite a large group. And we were running into more and
[464.38 --> 470.74]  more scale issues. And we discovered Vitesse. Now, sharding had always been seen as this
[470.74 --> 478.14]  pattern that was used by all the mega scalers. So like YouTube, Google, Facebook, Yahoo, LinkedIn,
[478.28 --> 483.14]  like Twitter, Twitter. Yeah. Yeah. The list is like you shard your database. Eventually you like
[483.14 --> 489.58]  horizontally scale, like you're very soon in your journey. And now even quicker in most startups,
[489.58 --> 495.22]  because of the way everything is accelerating, you outlive what a single box can do. And then like
[495.22 --> 501.44]  having a master box and replicas, you know, that falls down eventually as well. And so you eventually
[501.44 --> 507.26]  get to sharding. And that is a very hard problem to solve, like just very difficult. And we were stuck
[507.26 --> 513.18]  between this, well, we're scaling, do we do it ourselves? And like, just at the right time,
[513.86 --> 521.60]  Vitesse came along and was a sharding solution based on MySQL that had been proven at massive scale.
[521.60 --> 531.56]  So Vitesse was the database layer for YouTube. And it ran across 20 data centers, up like 70,000 nodes,
[532.18 --> 537.82]  just this huge database cluster. And it all presented as a single application as well,
[538.02 --> 542.96]  which was very handy for us because GitHub was a Rails app. And we didn't want to make things
[542.96 --> 547.36]  extremely complex. And we didn't want to put sharding logic in the app. So we wanted something
[547.36 --> 552.24]  that was like fairly transparent. So we discovered this technology. And I was just sort of, you know,
[552.24 --> 557.38]  the team loved it, made a great database team at GitHub. They loved it, they saw the value.
[557.96 --> 561.72]  So I met with the founders and I asked if I could invest in the company because I thought, you know,
[561.76 --> 566.80]  this is a great technology like this that you find impactful, you should. So I did. And then I was
[566.80 --> 570.88]  advising for the company for a little while. And then I was thinking about what I wanted to do next.
[570.88 --> 575.86]  And I thought if you have, you know, after being through the GitHub journey and seeing
[575.86 --> 583.02]  the power that developers bring and what a phenomenal audience they are to build for and build with,
[583.48 --> 590.54]  I thought if we can take this extremely powerful backend technology and deliver it so that we are
[590.54 --> 595.68]  that first database, right? Like right now, it's like a trade-off at either end of the spectrum.
[595.68 --> 602.22]  You don't pick the large scale, hard to implement, hard to learn technologies. You do that later on in
[602.22 --> 606.66]  your journey when it's appropriate, when you have loads of money and you can hire loads of engineers.
[606.90 --> 609.56]  Yeah. When engineering teams, you can just buy it out.
[609.72 --> 610.42]  Right. Exactly.
[610.68 --> 611.36]  Throw people at it.
[611.48 --> 616.46]  And like we always say, like, it's a nice problem to have. And it is, right? If you hit that checkpoint,
[617.00 --> 622.12]  you staff up your army to take the next, you know, milestone or whatever. So it's good. But I thought to
[622.12 --> 628.98]  myself, it's 2021. There's been incredible disruption and innovation in places like serverless and the
[628.98 --> 634.90]  front-end stack. And we see companies like Vercel and Netlify and what Cloudflare are doing. And I thought
[634.90 --> 641.90]  to myself, the time is now. If we have this backend tech that's so good, we can do this. We can be not only
[641.90 --> 648.12]  the best database to pick on that day one, we can be the best database for IPO. And the test is already
[648.12 --> 653.50]  proven at one end. And then we built PlanetScale on top, which is our serverless platform that we
[653.50 --> 660.84]  launched in May that became GA last week. And we made it happen. And I've honestly been blown away
[660.84 --> 667.48]  by the reaction since I think there was need, there was demand. There was a miss, a massive miss
[667.48 --> 672.70]  in developer experience. So the trend with databases previously was, oh, we're doing,
[672.70 --> 678.42]  solving some hard problems for you. So I'm going to pass on a bit of that pain. But a PlanetScale,
[678.48 --> 685.02]  that's a no. We want to deliver. That's a no. That's a no. We want to deliver incredibly powerful
[685.02 --> 691.70]  experiences that are incredibly simple and easy. And that is possible thanks to a very proven and
[691.70 --> 697.42]  mature technology under the hood. If you're starting a database startup from scratch, you're battling both
[697.42 --> 702.68]  great experiences, building a database. It takes decades to build a really solid database.
[702.70 --> 706.06]  Like really does. MySQL is what, 25 years old now?
[706.16 --> 706.58]  Super old.
[706.80 --> 707.46]  Still maturing.
[707.60 --> 707.74]  Yeah.
[708.12 --> 713.60]  Postgres has been around ages. And this is not bad stuff. Like this is good. This is maturity.
[713.76 --> 718.56]  This is what you want from your database. It's like, can't be being risky. And so being a building
[718.56 --> 724.16]  on those solid foundations, but with an eye for the beauty and the eye for this great experience
[724.16 --> 727.90]  is really what we're here to do. And it's been amazing so far.
[728.30 --> 732.56]  PlanetScale as a company is, from my estimation, at least four years old, right?
[732.70 --> 733.18]  Three.
[733.62 --> 734.36]  Three years. Okay.
[734.58 --> 738.50]  Yes. We just hit three and it was, it was co-founded by Sugo and Jatane.
[738.62 --> 738.90]  Okay.
[739.06 --> 742.50]  When they came out of YouTube and they took Vitesse with them basically.
[743.12 --> 751.42]  Okay. So was Vitesse always open source? What's the trend line since the possibility of PlanetScale
[751.42 --> 756.64]  is only possible because of Vitesse from, based on what you just said there, like if Vitesse is the
[756.64 --> 763.20]  underlying technology and PlanetScale is the developer experience slash user experience of
[763.20 --> 768.76]  implementing that as a serverless application to use, a serverless platform to use for developers.
[769.56 --> 776.16]  What's the trend line for Vitesse? What's the lifespan of that? Where did it begin? Where did it come to open source?
[776.16 --> 779.70]  How did you come to know it? Did you use a GitHub? Give some deeper details there.
[779.98 --> 786.48]  Yeah. So Vitesse was developed around, I think about eight years ago, at YouTube. And it was again,
[786.58 --> 792.16]  same story. YouTube was becoming massively prolific website that we all know now. Did you know
[792.16 --> 794.42]  YouTube is the second largest search engine in the world?
[794.56 --> 794.98]  Is it really?
[795.34 --> 795.66]  Yeah.
[795.66 --> 799.12]  It's definitely one of the first I go to when I research anything products.
[799.40 --> 799.64]  Anything.
[799.78 --> 804.20]  If we buy something new, I'm like, babe, have we, my wife will ask me questions and my response is,
[804.26 --> 807.78]  babe, have we looked on YouTube yet to confirm this is, because there's always somebody on there
[807.78 --> 813.78]  talking about how that thing works, how it actually is used. It's everyday folks in most cases.
[814.48 --> 818.54]  Like we just bought, I don't know if you saw this, this TV called the frame from Samsung.
[818.98 --> 822.38]  It sits on your wall, like a frame, like a picture frame.
[822.58 --> 822.76]  Yes.
[822.76 --> 829.22]  Very flat. It's got a component box that goes in a separate room or in a separate cabinet. It's very
[829.22 --> 836.54]  sleek and it can look just like art. And so before we bought it, I'm like, I can't believe this TV
[836.54 --> 841.26]  exists and it can perform in that way. And so just to be short before we bought it, I'm like,
[841.48 --> 845.58]  let's go check it out on YouTube. So yeah, definitely agree that it's like one of my go-to
[845.58 --> 846.64]  places for new information.
[847.20 --> 850.76]  I do know the frame and I have a number of friends that have it and it's an amazing TV.
[850.76 --> 856.30]  I did buy a bunch of TVs before this and now feel very jealous. And I'm in that horrible,
[856.72 --> 861.56]  I'm in that horrible state you get with products where it's like, I can't justify getting rid of
[861.56 --> 865.14]  what I, you know what I mean? Like when something's like, you're like, yeah, maybe this will hopefully
[865.14 --> 868.14]  break next year. So I have an excuse, but, but it won't.
[868.22 --> 873.10]  That's kind of what happened in our case. Our, uh, something happened with our current TV and we had to
[873.10 --> 878.48]  take it down and do some stuff behind it. We had a hungover over our, uh, our mantle in our main room
[878.48 --> 883.26]  and a long story short, we had to, we had to make some changes basically. And while we had it down,
[883.28 --> 888.22]  we're like, maybe we should look at this, the frame. So long story short. Yeah. I mean,
[888.22 --> 892.58]  and then as soon as we thought about it, we're like, okay, before we actually push by now,
[892.66 --> 896.98]  let's go to YouTube, let's search, let's see what people are using. Cause for me, it's not just a TV.
[896.98 --> 901.64]  It's how I can actually make the image look when watching movies. Like, does it have cinema mode?
[901.72 --> 906.84]  Does it have particular gamut, you know, gamma changes that you can do with the color and the
[906.84 --> 911.74]  spectrums to make it really shine. And let me just say real quick, this is not an ad for the frame.
[912.14 --> 916.96]  I love the TV. It's phenomenal. I just set it up recently, like yesterday for, to be exact.
[917.32 --> 921.36]  And I like it a lot. I've watched 4k content through it. Phenomenal. So I don't mean to make you
[921.36 --> 922.50]  more jealous, Sam. I'm sorry.
[922.50 --> 926.80]  Samsung though, if you do want to send us some money for, for shilling the product,
[926.94 --> 931.98]  you're also more than welcome as well. If you want some brand ambassador or use our database,
[932.42 --> 935.76]  plain and scale. Yeah. Just use it. Samsung as well. If you need a database, there you go.
[935.84 --> 940.64]  Two way. I'll buy the frame. You buy the database. That's right. So also YouTube, by the way,
[941.06 --> 947.30]  if you need to change, like change a socket or, or fix a thermostat, YouTube. Oh yeah.
[947.46 --> 950.36]  It's also the biggest education platform in the world. So anyway, YouTube was booming
[950.36 --> 956.34]  and now they're in the billions of user scale. And they were of course running MySQL because
[956.34 --> 963.12]  MySQL is just ubiquitous in the very large website space. And they had to come up with a solution for
[963.12 --> 968.28]  scaling it. And actually Sugu, our co-founder, he did a really good talk at Prisma's serverless
[968.28 --> 972.22]  data conf that happened last week. And I really recommend checking that out. And he really,
[972.22 --> 977.40]  he tells the story and goes into the story of, of how we did this, how we did this with Vitesse.
[977.40 --> 985.10]  And, you know, and so Vitesse was born on Borg. So people may know Borg as the predecessor to
[985.10 --> 991.36]  Kubernetes. Kubernetes is kind of architecturally based on Borg, which is this very, very large
[991.36 --> 997.42]  container runtime system that powers pretty much all of Google. And some of the core tenants of Borg are
[997.42 --> 1002.92]  no real persistence. Like if you lose a node, it's gone, it's never coming back.
[1002.92 --> 1009.96]  And so they had to orchestrate and run MySQL on this environment. And so they needed to build this
[1009.96 --> 1015.80]  orchestration and sharding system to do this. And that's how they built Vitesse. And it was built
[1015.80 --> 1020.66]  very pragmatically. And in fact, it was also one of the earliest Go projects. People don't realize
[1020.66 --> 1027.96]  this, but Vitesse was running on Go from such an incredibly early day. And the Go team actually,
[1027.96 --> 1033.12]  when there was this history of Go article came out a while back, they called out our co-founders
[1033.12 --> 1040.12]  as a thank you, because them building Vitesse, and Vitesse is one of the largest Go sort of applications
[1040.12 --> 1046.18]  out there, really helped actually Go evolve. And they gave lots of feedback. And so it's very interesting.
[1046.40 --> 1051.46]  It's kind of, Vitesse was born at this incredible moment of time when Go was coming up about,
[1051.46 --> 1057.92]  when the way of running applications, the kind of the Borg way that became the Kubernetes way.
[1058.58 --> 1062.76]  And then so it was those two ingredients, right? Like, you know, new language, a new way of running
[1062.76 --> 1069.94]  applications. And then the final piece that is essential, demand. So building deeply technical
[1069.94 --> 1078.12]  systems without the pressure of a reason to do so, right? Without it, like, there's something special
[1078.12 --> 1083.14]  when you're building a technology to serve a single website. And you have to deploy this technology
[1083.14 --> 1089.56]  over and over again, with continual load, that means you're kind of born in the fire. Like,
[1090.08 --> 1097.84]  when they deployed Vitesse, if it had a bug, you with a billion users, you discover that immensely
[1097.84 --> 1102.14]  quickly. And that is another challenge that if you're building a database from the grounds up,
[1102.14 --> 1107.86]  it's a hard thing to do without that immediate demand. You can't like, you're not always deploying
[1107.86 --> 1112.96]  into your customers environments, you're not always like debugging it. So Vitesse had a really
[1112.96 --> 1119.96]  smart team of engineers, building it for a very, very long time, with the demands of an extremely
[1119.96 --> 1127.38]  rapidly growing website. And I think all of those things together made a very powerful and resilient
[1127.38 --> 1132.98]  system. And so when they decide to open source it, and they, and it is truly open source, you know,
[1133.16 --> 1138.68]  it's out there for everybody to use, modify, do, do whatever, host themselves if they feel free.
[1139.18 --> 1144.72]  They sold it over to the CNCF. So it's kind of neutralized, neutral. And they basically put it out
[1144.72 --> 1149.86]  there. And other companies started to adopt it. Slack being one of those very, very early adopters.
[1150.70 --> 1156.42]  And Slack have blogged about Vitesse and how they use Vitesse. And it's their main database,
[1156.42 --> 1161.88]  just again, giant scale. And thank you to Slack. And they're fantastic engineers that
[1161.88 --> 1169.66]  have continued to commit to Vitesse and make modifications and improve it based on their needs.
[1169.70 --> 1175.48]  And if you look at the commit history, and if you look at the contributors to Vitesse,
[1176.42 --> 1180.72]  it is just a litany of some of the biggest sites in the world, or platforms in the world.
[1181.28 --> 1186.22]  And so this base of people that run the software, and improve it and continue to make it better,
[1186.22 --> 1191.18]  means that we have a very, like we talk about standing on the shoulders of giants.
[1191.68 --> 1198.34]  These are giant giants. And that's the history of Vitesse. We started using it GitHub. It's been
[1198.34 --> 1203.08]  fantastic. And that's how I came in contact with it. It's beautiful in the sense that it's wonderful
[1203.08 --> 1208.04]  to see all these companies collaborating. There's a game I play, like, you know, a game a little bit.
[1208.04 --> 1212.64]  And we found out from the game creators that the new version of said game, they hit us up and
[1212.64 --> 1216.78]  they were like, oh, yeah, we're using Vitesse as the back end for this. It's just crazy. I sit there
[1216.78 --> 1221.34]  playing the game thinking, this is awesome. Or every Slack message I send, you know, it's really
[1221.34 --> 1226.44]  delightful to know that the technology that we contribute to and that we maintain, and we do
[1226.44 --> 1231.90]  maintain the project and the project maintainers work here, has such an impact. It just feels amazing.
[1231.90 --> 1239.48]  And then the icing on the top is that now thousands of the startups that have started this year that
[1239.48 --> 1245.08]  use PlanetScale have that stack factored in. And they're not going to go through that painful middle
[1245.08 --> 1251.14]  period of like redoing the database, ripping the database out. They factored scale in early.
[1251.82 --> 1256.02]  And that's the real moment in time. And you think about it, all these other platforms that you can
[1256.02 --> 1262.74]  consume. Now, you can build an incredibly scalable stack, while still picking the stack that is
[1262.74 --> 1267.38]  appropriate for day one is still the fastest to use fastest to build against. It's awesome.
[1267.38 --> 1273.94]  It's interesting. All right. I mean, you've got this history personally, with the database engine
[1273.94 --> 1279.92]  itself, a test coming from GitHub, I'm curious, what was it like to implement it, I suppose, there to
[1279.92 --> 1285.66]  some degree, like maybe just roll it out? What were you converting from? What was the migration like?
[1285.66 --> 1293.64]  And how much of that pain, I suppose, surfaced when you came over to PlanetScale eventually? I like
[1293.64 --> 1298.32]  your story, how you said you invested in the company and you advised, and then you came over as
[1298.32 --> 1303.70]  chief product officer. And then I think a few months later, if not just a very short time later,
[1303.70 --> 1310.40]  was announced as a new CEO. I think that's an interesting journey. So I'd love to pick out how
[1310.40 --> 1317.44]  the test was looked at inside of GitHub, at what scale, how it came to be, and then kind of dovetail
[1317.44 --> 1325.46]  into your journey to PlanetScale itself, to think, now we could take this database in much different
[1325.46 --> 1329.82]  directions, like you said, at the right time, at the right place, with the right demand.
[1329.82 --> 1337.12]  Yeah, so the adoption of GitHub is bumpy, like it is with every, so Vitesse is an amazingly powerful tool,
[1337.70 --> 1343.02]  but it's not perfect. And what it does for you is way more than, you know, you just couldn't build it
[1343.02 --> 1346.78]  yourself, right? Like, you know, starting from scratch to do all this yourself would just be
[1346.78 --> 1352.56]  wild and take way too long. So what Vitesse gives you in return is you cut to the chase very quickly on
[1352.56 --> 1356.86]  scaling. But if you're just installing it yourself, you're likely going to need a team of engineers to
[1356.86 --> 1361.82]  learn. It's like with every system, right? You have to learn the quirks, you have to learn its failure
[1361.82 --> 1367.26]  modes. And so we did it incrementally. Had a great team of application engineers at GitHub that started
[1367.26 --> 1375.14]  to split specific tables out of the database and put it in Vitesse. So there was a lot of like,
[1375.70 --> 1380.86]  very, very large tables that just kept growing and growing. And like, everyone has these in the
[1380.86 --> 1386.48]  application, like your notifications table was one that was just a complete pain. And it was just like,
[1386.48 --> 1391.30]  every notification on GitHub just got put in this table, right? So it just started to get massive.
[1391.78 --> 1397.02]  The others is like statuses or whatever. So you know, like at the bottom of your pull request,
[1397.14 --> 1401.80]  when you sort of all the CI checks come back and GitHub was developing the product around this and
[1401.80 --> 1406.28]  all of these statuses for pull requests, like pass, fail, whatever, was just again,
[1406.38 --> 1410.68]  all piling up into a massive table. And people look at pull requests, they're like three years old,
[1411.16 --> 1414.26]  and they might want to resurrect them. So these statuses needed to be there.
[1414.26 --> 1417.88]  And so again, it was just like massive amount of data. And I think around the time,
[1418.46 --> 1423.48]  GitHub was probably around 30 million users at the time, with a lot of heavy usage.
[1424.06 --> 1429.94]  My favorite thing to look at in the usage graphs that GitHub was, you could see all of the cron ticks
[1429.94 --> 1434.58]  for the world, because everyone had crons that would like pull their repo down and do testing,
[1434.70 --> 1440.24]  right? So and you could see this spike through all of the graphs, whether it was like front end CPU
[1440.24 --> 1446.22]  load, whether it was database queries, like every single like performance graph at GitHub
[1446.22 --> 1451.88]  had these ticks, like had these large spikes, like on the hour was the largest, then half an hour,
[1452.08 --> 1457.36]  then 15, 10, five, one minute. And you would just see these little because all of the world's crons
[1457.36 --> 1462.88]  are running to pull code down from GitHub and start up CI processes and whatever. Anyway, so
[1462.88 --> 1468.54]  we were trying to scale that. So we adopted things incrementally table by table and move them over to the
[1468.54 --> 1473.86]  tests. And it just worked fantastically. And you know, we still see the enthusiasm from the
[1473.86 --> 1479.00]  different engineering teams that get to use it. And that's how I got involved. And so then when I
[1479.00 --> 1482.70]  was here at plant scale, I thought, you know, we can democratize this tech, we can give it to
[1482.70 --> 1487.54]  everybody. And then it came to the team. And I have to give all of the credit to the great team that we
[1487.54 --> 1494.94]  have at plant scale. Not only do we have the test team that are just literal wizards,
[1494.94 --> 1500.66]  they're writing query planners. And you look at the annotation and their notes and the formula
[1500.66 --> 1504.82]  that they're working on. And I just look at this and just think, I don't know anything about
[1504.82 --> 1511.44]  computers. Like you just think, wow, these people are phenomenal. Databases are tough. The trust people
[1511.44 --> 1517.52]  put in a database is immense, right? You have to take it so seriously what you're doing. And they do
[1517.52 --> 1524.42]  take it incredibly seriously. And they work incredibly diligently. Like we did a big effort to be like for
[1524.42 --> 1529.76]  compatibility, to make sure we were just compatible with all the frameworks that are out there. And
[1529.76 --> 1535.20]  we're very compatible with MySQL. There's a few caveats and a few things that we don't support.
[1535.38 --> 1540.68]  And we do that in the favor of scale and user experience in the long run. And there's just
[1540.68 --> 1547.00]  certain things that just kind of don't work fundamentally in the long run. And they just put
[1547.00 --> 1552.38]  list after list of things that were incompatible and just burned it down. And they work with such pace
[1552.38 --> 1557.00]  and they deliver such reliable software. They're an amazing team. So you pair that team and those
[1557.00 --> 1563.02]  people, these experts in databases and in the very kind of core essence of what a database is.
[1563.50 --> 1569.12]  And then we have this team of folks that build the experiences like the soft service. If you think
[1569.12 --> 1573.54]  of the test as this like incredibly powerful engine, then we have people that are equally dedicated
[1573.54 --> 1580.06]  towards building an amazing interior and something that has that quality and refinement. So,
[1580.06 --> 1585.70]  you know, when you slam the car door on a really good car and it just makes that clunk that just
[1585.70 --> 1586.80]  feels so satisfying.
[1587.40 --> 1590.32]  It's like a very soft, hard close. It's like a...
[1590.32 --> 1590.80]  Yes.
[1590.90 --> 1592.46]  It's not kachunk. It's more like...
[1592.46 --> 1596.84]  You can't describe it. You know it. I love that you tried to make those sounds there.
[1596.98 --> 1599.84]  Well, I had to because I mean, I just, I know exactly what you're saying.
[1600.04 --> 1602.90]  I feel like we're really bringing the audience with us. It's interactive.
[1602.98 --> 1604.38]  Yeah. We're really taking them on a journey here.
[1604.38 --> 1609.20]  It's an audible journey. And so they really put the effort into refining things. And I think we're
[1609.20 --> 1614.26]  all scratching an itch of kind of building the database we wish we had at all points in our
[1614.26 --> 1618.98]  career. And they put so much dedication into building these experiences. We have this Twitter
[1618.98 --> 1625.50]  channel that kind of all of the mentions of PlanetScale go into it. And you see people commenting
[1625.50 --> 1632.14]  like, this is the nicest logging experience I've ever had. All the CLI is just incredible to use.
[1632.14 --> 1636.30]  And we're going to copy PlanetScale's way of doing logins or all of these various little
[1636.30 --> 1644.40]  details that get put into the product. And so much of it, it's like unnecessary and extremely
[1644.40 --> 1650.62]  necessary at the same time. Right? Like people will buy a proven enterprise grade database.
[1650.96 --> 1656.20]  Right? Like there's like, we have something so unique and so powerful that people will buy
[1656.20 --> 1660.74]  that. Right? Like that's for sure. But we take it to this extent where we want it to be
[1660.74 --> 1667.16]  delightful and accessible to absolutely everybody. And that is where the detail comes in. And we have
[1667.16 --> 1673.16]  the, you know, the teams that work on the details and the experiences that people kind of run into
[1673.16 --> 1678.86]  are so diligent, so dedicated and so talented and they have taste. And that is something that
[1678.86 --> 1684.28]  is very hard to replicate. I just feel constant excitement whenever they share their work or wherever
[1684.28 --> 1691.40]  I see them deliver things. I just, I feel so like excited and humbled and just, and it just makes me happy
[1691.40 --> 1698.22]  just to see them work. Like the import feature we just released last week. It's just, no one's ever done it
[1698.22 --> 1704.54]  that way before. And when I looked at every other competitor of how they do imports and it's like, well,
[1704.54 --> 1710.96]  here's the instructions on how to dump your database. And you have to restore that database into our thing
[1710.96 --> 1718.20]  and connect up here or like, let's set some environment variables and this and that. And it's just a mess.
[1718.80 --> 1724.42]  With what our team delivered, you just put in credentials. We connect. Thanks to Vitesse and V replication,
[1724.42 --> 1729.52]  we just pull the data in, no dumping, nothing, no restoring. And then you can switch your connections
[1729.52 --> 1734.88]  to PlanScale and we'll proxy back to your old database and do a cut. And you can do a fully online
[1734.88 --> 1741.70]  migration on our platform with this tool. And thanks to Vitesse, thanks to the, like the refinement and
[1741.70 --> 1747.60]  polish they put on. It's just magical. I've seen people take months to do something as complex as that.
[1747.70 --> 1753.72]  And now it's a fully online operation and it is just the import tool, right? Like it's, we could have just
[1753.72 --> 1758.22]  gone, ah, do it the lazy way like everyone else does it and move on. But we didn't because our
[1758.22 --> 1762.86]  standards are much higher than that. We want to make something that's delightful for every second
[1762.86 --> 1767.88]  that you use it. How did that feature come about in particular? I want to put some heavy weight on
[1767.88 --> 1772.94]  this because this to me is like the clincher, right? If you can get this down, right? Like you said,
[1773.00 --> 1778.56]  fully online, it's one thing technically to make it possible, but then two, to make the user experience
[1778.56 --> 1784.36]  so easy to do. Just establish your connection to your database. It does all the magic inside of it.
[1784.72 --> 1789.96]  And you can essentially proxy to PlanitScale in between to try it out. Essentially, we always say
[1789.96 --> 1795.16]  like, if you could try it and prove to yourself and your team that it's reliable, that it's a good fit,
[1795.24 --> 1802.96]  whatever it might be, that's the magical way to get people to one, try it and then potentially switch.
[1803.08 --> 1808.12]  But this seems a lot easier because like you just swap to PlanitScale when it's time without any
[1808.12 --> 1814.36]  downtime. Yeah, so it came about in like multiple ways. Like nothing ever comes about the way you
[1814.36 --> 1818.86]  would imagine it or the way your memory summarizes things, right? Like it came about from first of all,
[1818.86 --> 1824.96]  we knew we needed to do it. Like it's table stakes to have imports. So we looked at the technology we have.
[1825.28 --> 1832.04]  We know Vitesse can manage external nodes and we can, we know Vitesse can like, this is primitive
[1832.04 --> 1838.10]  in Vitesse called vReplication, which is incredibly powerful. If you think of resharding as a
[1838.10 --> 1846.78]  problem, it's actually very, very complicated. So to reshard, you essentially have lots of buckets or
[1846.78 --> 1854.62]  nodes with full of data that is separated by a scheme. So you may shard on user ID, tenant ID,
[1854.76 --> 1861.08]  whatever. And then to reshard, to like change that scheme, you have to fan in all of the data from those
[1861.08 --> 1869.00]  shards and fan it out to another sharding scheme while on being online, while being completely safe
[1869.00 --> 1875.86]  with the data. And it's very hard to do. And that again was solved at YouTube, right? And we have
[1875.86 --> 1882.04]  customers that do multi petabyte reshards, like resharding, fanning in this data, fanning it back.
[1882.04 --> 1888.70]  And so that itself is a really hard problem to solve. And Vitesse has solved it. And in building
[1888.70 --> 1893.08]  that kind of replication stream technology, vReplication, you can do many, many other things.
[1893.82 --> 1899.80]  And one of those things is look at other MySQL nodes and use it to kind of nibble the data into
[1899.80 --> 1904.70]  Vitesse. So we looked at that as a functionality, like, great, that's one strength. And then it's about
[1904.70 --> 1910.72]  giving the kind of overall feeling of what we want to build and what we want to, what needs to be
[1910.72 --> 1917.90]  possible. And handing it to the engineering team, who are incredibly picky, and talented,
[1918.38 --> 1921.56]  and have a very high bar. And this is what they came back with.
[1921.66 --> 1924.08]  I like to use the word selective, selective instead of picky.
[1924.20 --> 1925.72]  Slacky, yeah, selective, picky.
[1926.00 --> 1927.14]  Highly selective, highly picky.
[1927.38 --> 1931.72]  Yeah, they just have a high bar for things. They want to build really great things. And so
[1931.72 --> 1936.16]  that's what they came back with. And there was always that, like, and another, and like one more
[1936.16 --> 1940.70]  thing, and we're going to do the proxying, and we're going to make this possible. And yeah,
[1940.72 --> 1944.76]  it's just mind blowing every time we see it. And then obviously, we put our incredibly talented
[1944.76 --> 1949.82]  product designers on who are very, very good at what they do. And then kind of some magic
[1949.82 --> 1956.06]  comes out. And that's, it's an intertwining of culture, talent, knowing what users want,
[1956.72 --> 1961.20]  knowing what our standard is, and coming together as a group to build it.
[1961.20 --> 1983.64]  What's up, friends? This episode is brought to you by Rewatch. Rewatch gives product and engineering
[1983.64 --> 1989.66]  teams async superpowers, and it helps them move faster with greater clarity. And I love clarity.
[1989.66 --> 1996.20]  Imagine this, all of your team's videos, all in one place. Record, organize, and share the videos
[1996.20 --> 2001.06]  that your team needs to ship great work. Keep everyone in the loop by sharing team meetings,
[2001.26 --> 2007.08]  from sprint planning to daily standups to project retros. Empower new hires to get up to speed
[2007.08 --> 2012.06]  faster with onboarding and training videos that are easy to watch. And of course, Rewatch.
[2012.34 --> 2016.28]  You can streamline knowledge sharing by creating a library of product demos, tech talks,
[2016.28 --> 2020.76]  architecture reviews, and so much more. And we're using Rewatch here to change the login.
[2020.84 --> 2026.22]  The killer feature for us is every video is automatically transcribed and searchable.
[2026.54 --> 2031.04]  And the transcripts are surprisingly very accurate, which makes it so easy for us to search key
[2031.04 --> 2037.80]  phrases, terms, and find and play the exact spot in a video. Plus, there's commenting and
[2037.80 --> 2043.00]  threaded conversation options on every single video. Now we have a home for all our videos to
[2043.00 --> 2048.36]  enable our growing and distributed team to participate in any conversation asynchronously
[2048.36 --> 2053.92]  and on their own time. Check them out, get started for free with a 14-day trial at Rewatch.com.
[2054.32 --> 2056.02]  Again, Rewatch.com.
[2056.02 --> 2079.44]  So you said you got exposed to the tests inside GitHub. What do you think GitHub would have been
[2079.44 --> 2085.78]  like in your day if PlanetScale existed exactly as it is now, with the promise that exists now,
[2086.40 --> 2091.46]  in that day for GitHub? How would GitHub have changed if it had PlanetScale then?
[2091.64 --> 2096.44]  It's an interesting thought experiment, right? Like, as the person building databases back then,
[2096.46 --> 2100.54]  I would have loved to have a product like this around. And that's what I think about, right? I think
[2100.54 --> 2106.00]  about the limiting factors. I think one of the amazing things about GitHub
[2106.00 --> 2112.70]  was very selective, very talented early engineers that had great taste and knew what to build.
[2112.88 --> 2116.48]  And I would like to believe that what we're building would pass the test of
[2116.48 --> 2122.50]  getting out of their way and enabling them to build and scale such an incredible product.
[2122.84 --> 2126.62]  And that's who we're doing. We're doing it for the next generation. The next GitHub is the next
[2126.62 --> 2132.94]  Slacks, the next Stripes, whoever's building the next big startup. We have a startup. Obviously,
[2132.94 --> 2136.30]  I'm not going to name names, but they're not really a startup now. They're just crushing it. But they've
[2136.30 --> 2143.04]  been on the platform for a little while now. And they see 40% growth month on month. Every month,
[2143.26 --> 2151.08]  their data size, their usage goes up by 40%. It's amazing. It's just amazing to see when the database
[2151.08 --> 2155.48]  gets out of the way. And obviously, we can't take full credit for everything. But it is just awesome
[2155.48 --> 2162.38]  once to solve problems for companies that are growing and scaling so quickly. It's just immense fun.
[2162.38 --> 2163.96]  It's just, it's really awesome.
[2164.80 --> 2171.32]  Let's talk about your journey then to CEO. Did you expect to, I suppose, have this exposure early
[2171.32 --> 2179.44]  on to Vitesse, this desire to invest, to advise, to eventually rethink, you know, what's next for you,
[2179.66 --> 2186.10]  make that move to chief product officer at PlanetScale. And then how many months after that was it that you
[2186.10 --> 2191.64]  were promoted to CEO? What's that journey been like for you to go from that journey to like
[2191.64 --> 2199.20]  exposure to it, investment, advisement, chief product officer, now CEO? What's that? Is it like
[2199.20 --> 2205.04]  expected, unexpected, delightful? Like, how do you feel about this journey of yours?
[2205.26 --> 2213.02]  It's completely unexpected. I think it would kind of be a little, it'd be a bit aggressively
[2213.02 --> 2219.72]  ambitious, I think, to maybe expect it all to happen this way. And honestly, it's been amazing.
[2219.72 --> 2225.52]  I don't really think too far ahead for myself personally. I think very far ahead in terms of
[2225.52 --> 2229.88]  what I would love the company to become and what I want our product to become. And it feels like we
[2229.88 --> 2236.18]  haven't even gotten started and it's already been incredible. But I tend to just see what comes up
[2236.18 --> 2242.40]  and try and capitalize on what's there and make the best decisions I can at the time to make things
[2242.40 --> 2247.58]  kind of happen. And that's kind of been this journey. I joined GitHub because it was this
[2247.58 --> 2256.78]  crazy, incredible company full of absolutely amazing people. And I kind of just followed where
[2256.78 --> 2261.78]  that went. And I don't think you need to have a grand plan. Just do great things with great people.
[2262.36 --> 2264.86]  And the rest kind of sorts itself out from there.
[2265.06 --> 2268.24]  Yeah. What was the early impression for you, though? Like when you were,
[2268.24 --> 2272.44]  I mean, I don't want to say your time at GitHub was done. I'm just trying to capture maybe how
[2272.44 --> 2276.96]  you felt then. But what was it that was making you kind of question what was next for you? And why,
[2277.48 --> 2282.58]  what was the attractive piece for you for playing the scale for you? What was that attraction?
[2283.22 --> 2285.38]  So I went to Facebook for a little while after GitHub.
[2285.68 --> 2285.98]  Okay.
[2286.22 --> 2292.26]  I wanted to work on systems that were just at colossal scale. And then there's this scale and
[2292.26 --> 2297.16]  there's like Facebook, YouTube type scale, right? Like it's a different world, right?
[2297.16 --> 2304.30]  There's a team of Facebook that just adds overlays for graphs that explain world events. Because if
[2304.30 --> 2310.10]  you have like three and a half billion active users, world events like elections and things
[2310.10 --> 2314.64]  actually meaningfully affect engagement on the platform. And so it was just this like
[2314.64 --> 2318.96]  gigantic scale problem to work on. And it was very, very interesting.
[2318.96 --> 2324.82]  On the other side, I felt there was something missing. I loved developing products and getting
[2324.82 --> 2331.42]  to work on GitHub actions was some of the most fun I had in my career. And I wanted that again.
[2331.98 --> 2336.72]  And I love databases. And I just got chatting to the co-founders of PlatteScale and just,
[2337.20 --> 2343.86]  it kind of just came together. And I just saw an immense amount of potential here. And I knew that
[2343.86 --> 2348.88]  myself and a few folks were kind of ready to move on to the next thing. By the time I left GitHub,
[2348.88 --> 2354.00]  it had been that eight years, which is a long time in startup world. And the company had evolved and
[2354.00 --> 2359.54]  changed a lot. And so I just felt like I was ready to do something new. And I came over here and started
[2359.54 --> 2365.06]  talking to some old colleagues and pitch them on what I thought we could do. And one by one,
[2365.12 --> 2370.02]  they came along and we made some really fantastic hires. And now we, the company has grown immensely,
[2370.02 --> 2374.56]  even in the last year. And it just feels awesome. It just feels right. You're on this journey. You're,
[2375.18 --> 2378.76]  you kind of get into a state of flow, right? You know, when you're in that, you have those days where
[2378.76 --> 2385.94]  you go from one thing to the next and it feels like there's almost a soundtrack playing to your
[2385.94 --> 2390.68]  life. Like everything feels, it's like, it almost feels like a montage in a show or a movie or whatever.
[2390.78 --> 2396.74]  It just kind of flows from one thing into another. And that's what has started to build up here.
[2396.74 --> 2402.32]  And now we're definitely in that state of flow. And it just feels incredible. You hop from like
[2402.32 --> 2408.28]  customer call with a major brand and they're like, we're on, we want to do this. Or you jump into a
[2408.28 --> 2413.10]  product review and the engineers have just far exceeded everything you expected you could do.
[2413.16 --> 2418.24]  Or you have a leadership meeting and you meet a bunch of folks on this journey with you who are
[2418.24 --> 2423.28]  trying to not just build a great product, but build a great product and kind of view the experience
[2423.28 --> 2430.58]  internally almost as a product. And the days just kind of melt away and you have so much fun. And
[2430.58 --> 2435.58]  I'm kind of dedicated to enjoying every second of it, even the low points. Cause I,
[2435.68 --> 2441.64]  I never thought I'd get to do something as fun as GitHub again and getting to do something like
[2441.64 --> 2447.18]  this. The second time I'm, I'm taking it all in, right. And just enjoying the small moments,
[2447.18 --> 2452.54]  the late nights where you're with a few colleagues and you're just like batting around ideas and hopes for
[2452.54 --> 2458.08]  the future. And, or just the little conversations, we're going to be certain people's first,
[2458.08 --> 2464.06]  first ever job and it will shape their career. And that's just awesome. I mean, it's just so
[2464.06 --> 2469.56]  amazing. It's such a, you know, people mock it and laugh at it. And I sound silly when I talk about
[2469.56 --> 2473.24]  the, it's about the journey. It's so cliche, but it really feels like it.
[2473.42 --> 2473.96]  I'm with you, man.
[2473.98 --> 2474.50]  It's amazing.
[2474.64 --> 2478.46]  I agree with that. You have a sort of reverence for the process, not just the,
[2478.46 --> 2484.08]  not just the possibility, but for the people involved and all the details. I got, I love that
[2484.08 --> 2489.92]  you think about the fact that working at PlanetScale is going to be somebody's first job and
[2489.92 --> 2495.72]  what that impact will be. I think in many ways it does shape you. It gets to shape you. And if you
[2495.72 --> 2500.52]  can build the company right and the culture, right. And the, and the trajectory of where you can go
[2500.52 --> 2504.50]  right and have the right kind of team at the right time with the right kind of demand.
[2504.50 --> 2511.82]  I agree with your sentiment on the sort of soundtrack to daily life, bouncing from one
[2511.82 --> 2516.08]  day to the next. And it just sort of seems to click, even when it doesn't fully click
[2516.08 --> 2521.04]  perfectly, like a bad day or a down moment doesn't, doesn't seem like it's, those are
[2521.04 --> 2522.42]  the days truly to enjoy, honestly.
[2522.96 --> 2523.36]  Absolutely.
[2523.72 --> 2524.34]  They really are.
[2524.46 --> 2530.22]  And you have hard days where you have problems, but if you frame them with like the gratitude
[2530.22 --> 2536.18]  that you're still around and like, you think about it, like we are through so many filters,
[2536.18 --> 2543.24]  right? We're our staging company with the demand that we have and the people we have, we've got
[2543.24 --> 2548.84]  so much further than 99% of companies. So that when you have problems, you think, I'm sure
[2548.84 --> 2553.80]  glad I have this problem versus the opposite. Right. And you can feel very grateful for that.
[2553.80 --> 2562.28]  And there's great learning and fun to be had from even going through shitty things, but with great
[2562.28 --> 2567.74]  people and especially people that have a sense of humor. I think we definitely do have a very strong
[2567.74 --> 2573.16]  sense of humor in our culture. And a lot of people are very funny and you can take things seriously
[2573.16 --> 2580.00]  all the time, but I think that just wears on you. There's certain situations that happen in your
[2580.00 --> 2585.08]  company life where you can either take them super seriously and sort of beat yourself up and beat
[2585.08 --> 2588.84]  each other up about it. Or you can say, it's kind of funny that that happened. That's just like,
[2588.92 --> 2594.82]  what a stroke of luck. Well, you know, what a fluke. Oh dear. And then just move on and kind of laugh
[2594.82 --> 2600.10]  it off and make a joke and, and carry on. And so I like working with people with great sense of
[2600.10 --> 2604.12]  humor. So we've got some really funny, talented people over here. It's great.
[2604.12 --> 2610.32]  For me, it's a three words I use to help me shift my perspective in moments like that,
[2610.32 --> 2617.74]  rather than thinking I have to do X to shift it to a gratitude position. I say I get to do X.
[2618.24 --> 2623.88]  So I might think, gosh, I got to ship two podcasts between today and tomorrow because it's Thanksgiving
[2623.88 --> 2629.96]  coming up. Right. And that is a burden because producing great podcasts is a lot of work.
[2629.96 --> 2636.14]  Yep. There's a lot of detail that goes into all the process and all the bits and whatnot. And I
[2636.14 --> 2643.10]  could, despite what an awesome job it is that we get to do here at changelog is there's a day when I
[2643.10 --> 2647.40]  was like, man, one day I hope all I can do every day is just produce podcasts. Right. And then now
[2647.40 --> 2652.86]  it's like, well, that's the burden. Right. Yeah. So you can say, I have to, uh, with like this
[2652.86 --> 2659.62]  regression heart, or you can shift to a gratitude position, which is I get to, I get to produce two
[2659.62 --> 2665.22]  podcasts this week. Yeah. And not only do I get to produce these awesome podcasts, somebody out
[2665.22 --> 2672.24]  there is going to hear Sam share his story about why planet scale is what it is and why he believes
[2672.24 --> 2676.42]  in it and why the team is phenomenal around it, et cetera, et cetera. And somebody's going to get
[2676.42 --> 2682.74]  impacted and their life will be changed rather than just saying, um, I got to ship two podcasts this
[2682.74 --> 2687.28]  week and I got to deal with this bug or this feature. I got to be on incidents this weekend or
[2687.28 --> 2693.72]  whatever. Reframing is very powerful. Yeah. And it's a really hard thing to admit to ourselves,
[2693.72 --> 2700.06]  but you can choose your experience of the world. Like it's exceptionally difficult. Like once you
[2700.06 --> 2705.88]  realize that, I think a burden, you get even more sort of a burden on yourself, right? In the sense that
[2705.88 --> 2714.58]  you can choose how you perceive what happens and how you remember the effects it has on you. So like
[2714.58 --> 2721.96]  I used to think extreme positivity was being very naive or like optimists were naive, right? Like
[2721.96 --> 2728.12]  surely nothing's perfect. Nothing, you know, an optimism, you know, is not about admitting that
[2728.12 --> 2733.12]  thinking the world is perfect and thinking whatever, but being optimistic. And now I try and be extremely
[2733.12 --> 2736.56]  optimistic and the optimism that, you know, we'll get through things, we'll do something.
[2737.02 --> 2737.08]  Yeah.
[2737.36 --> 2740.94]  I mean, it took me a long time and I was extremely pessimistic and kind of learning that
[2740.94 --> 2746.78]  in a lot of scenarios, like how many scenarios where you text someone and they don't reply and
[2746.78 --> 2750.26]  you're like, Oh my God, I've offended someone or whatever, but you don't know, you truly don't
[2750.26 --> 2758.00]  know. And in 99.9% of the time you haven't done anything right. The people that just chose to say,
[2758.16 --> 2763.68]  I don't know. So I'm just going to assume the absolute best versus the worst. Like neither's more
[2763.68 --> 2769.98]  wrong or correct, right? Like it doesn't matter either way. It took me a long time to think about that
[2769.98 --> 2776.46]  truly and realize that even in terrible situations, even when someone's being rude to you or mean or
[2776.46 --> 2783.70]  whatever, you can just put a positive spin on it, commit it to disc, get it out of your head and move
[2783.70 --> 2790.52]  on. Once you learn to do that, the world starts to get a lot easier and better. But it is very, very hard.
[2790.88 --> 2795.56]  We're an industry of pessimism, I think, but you only build great things if you're super optimistic
[2795.56 --> 2801.82]  about them. Yeah, exactly. I mean, I happen to be the optimist, at least in my relationship with
[2801.82 --> 2809.76]  Jared, my business partner and my wife, she's more, I'm sunshine and rainbows as she's sunburned
[2809.76 --> 2816.26]  cavities. So when we look at scenarios, we look at them slightly differently and I'm not always
[2816.26 --> 2822.38]  perfectly an optimist, but I tend to be like, what's the good in this scenario? Yeah. One thing I heard
[2822.38 --> 2830.02]  was that you can't choose how people will behave, react or respond to life events, but what you can
[2830.02 --> 2836.08]  control is how you respond. Exactly. And I think that's kind of what you say before is like, you can
[2836.08 --> 2841.90]  choose how you respond to life events. Now, granted, there's some things you go through that's super
[2841.90 --> 2846.92]  challenging and you're not gonna be the best person ever, but just knowing that you have the choice
[2846.92 --> 2852.86]  on how to respond. Even if you don't do it right the first time, the next time it happens, or the next
[2852.86 --> 2859.58]  time it happens, that you get to change and evolve how you respond, because how we respond to the goods
[2859.58 --> 2865.52]  and the bads and the ups and the downs, in a lot of cases, it's our choice on how we respond to those
[2865.52 --> 2873.66]  things. Because I can get mad and throw a fit and maybe even smash something nearby, or I can pause for
[2873.66 --> 2878.56]  a moment, take a breath, think about it a little differently. What's the upside here? What's the
[2878.56 --> 2883.08]  next step I could take in the positive direction versus the negative direction? And then take that
[2883.08 --> 2888.78]  first step. And the momentum tends to be the thing that carries us. So just creating that momentum in
[2888.78 --> 2893.12]  the right direction you want to go or should go is truly half the battle. Once you're there, it's like,
[2893.54 --> 2898.18]  wow, it's almost like your days now that you're in. It's like, that momentum was a little hard to get
[2898.18 --> 2900.88]  to, but once you got there, it's like, it just sort of keeps clicking.
[2900.88 --> 2907.38]  You're right. I sort of think manifestation is both quite dumb and probably the most amazing thing
[2907.38 --> 2912.28]  that you can actually do, right? Like, there's people who are like, oh, I'm going to manifest this.
[2912.36 --> 2918.32]  And it's like, yeah, your bank account isn't growing if you just sit and think about it. But at the same
[2918.32 --> 2923.60]  time, if you manifest this new idea of wanting to be successful and make something, and like, it actually
[2923.60 --> 2930.98]  changes everything. If you believe in doing something great and awesome, I've never thought
[2930.98 --> 2936.82]  of a good way of framing this. Maybe someone has already done so, but it's those micro decisions
[2936.82 --> 2941.82]  and attitude that you bring to things, right? Like this morning I was like, I woke up, I was really
[2941.82 --> 2946.66]  grumpy and pissed off. And I thought I was going to have like a really rough day. And then I worked out
[2946.66 --> 2955.02]  and my entire attitude towards the day changed. None of the, my schedule ahead of me, the criteria
[2955.02 --> 2960.68]  for the day, the things I was, nothing changed. Literally nothing changed while for that hour I was
[2960.68 --> 2967.26]  working out, but the attitude did. And it completely changed how I approached everything and that
[2967.26 --> 2972.24]  feeling. And I think if you do that on a larger scale for your life and sort of try and manifest the
[2972.24 --> 2976.68]  life that you want, it kind of takes care of itself in a lot of ways. You kind of just have to push
[2976.68 --> 2981.96]  forward and flow from one of those states to the other. And going back to what you said, I think
[2981.96 --> 2987.88]  you can probably go to the extent of saying at some point you can say you're responsible for every
[2987.88 --> 2992.70]  action or reaction that you take. It's just impossible to control all of them, right? Like
[2992.70 --> 3000.20]  ultimately you are, right? Some people have managed to gain incredible self-control. I think for most of us,
[3000.20 --> 3006.52]  that level is fairly unachievable. Yeah. Well, there's some edges of emotional intelligence
[3006.52 --> 3010.08]  and emotions that I'm not that familiar with, which is why I kind of cavited with
[3010.08 --> 3013.64]  most of the things you're in control of. Cause I think there's some things around
[3013.64 --> 3019.40]  just humanity and emotion that we can't often change that something would make us depressed or
[3019.40 --> 3023.50]  make us sad if a sad thing happened. So I don't want to say that you have full control, but like
[3023.50 --> 3032.76]  in many ways, it is a result of your action. And if you practice behavioral change and emotional
[3032.76 --> 3039.54]  intelligence and things like that, that really shape and mature your perspectives on, I guess,
[3039.58 --> 3047.18]  life events, then with all practice like that, you eventually get better or improve. Like you're
[3047.18 --> 3052.22]  just not born with emotional intelligence. You're not born with the best way to change. So you are in
[3052.22 --> 3055.96]  control of it, but I think over time you get better and better at it. Agreed. Which is an interesting
[3055.96 --> 3063.46]  thing, honestly. Well, and kind of controlling the lizard brain and controlling those default reactions
[3063.46 --> 3070.86]  that you have to things and how you react. So let's come back to current really. So new CEO,
[3071.14 --> 3076.80]  this is a first time CEO position for you. Yes. Is it the best time of your life? The mostly best
[3076.80 --> 3082.18]  time of your life. How have you taken on this new role? What are some of the particular challenges
[3082.18 --> 3088.80]  that you've won, hated, but then also enjoyed? I love the job. I absolutely love the job and I feel
[3088.80 --> 3094.42]  incredibly lucky and privileged to be able to do the job. I will say though, it's a very tough job
[3094.42 --> 3102.94]  and it's funny. I didn't imagine what it would feel like until I took the job and I knew I was going to
[3102.94 --> 3111.22]  be the CEO for probably a month before it happened. But even just minutes after it was announced,
[3111.76 --> 3118.56]  you just feel this very strange feeling. And people say it's the loneliest job in the world.
[3118.62 --> 3123.68]  And I think that's true. Again, just insanely unfortunate to have such an amazing team at
[3123.68 --> 3129.62]  Planscale. But in a lot of ways, you're responsible for the final say, right? And if things go wrong
[3129.62 --> 3135.40]  inside your company, it's your fault. It's up to you to fix. Yeah, it's your fault. Ultimately,
[3135.70 --> 3144.28]  you can trace back every single issue in the company to being my fault at some point. That's
[3144.28 --> 3148.90]  hard. It's also an immense privilege though, because you get the ability to shape things and
[3148.90 --> 3155.52]  change the things you don't like. And I try and do that, right? I really want to build a phenomenal
[3155.52 --> 3161.44]  culture for people, for people to work here and be happy and do the best work of their careers.
[3162.36 --> 3169.62]  And sometimes that means not always doing what people are asking. Or you have all of these sources
[3169.62 --> 3175.28]  of information. You have a picture of the world, like we all do, that is completely different and
[3175.28 --> 3182.96]  unique. And you try and balance things. And I think some of the best businesses and products are built
[3182.96 --> 3190.88]  on unresolvable tensions. Like put it this way, in every company, the sales team always want more,
[3190.96 --> 3197.94]  more, more. The engineering team want more time to do X type of work. The marketing team wish this was,
[3198.08 --> 3201.26]  you know, and it happens in, I'm not saying specific to Planscale, it happens everywhere,
[3201.40 --> 3207.04]  right? There's overlapping priorities for each type of parts of the organization. And if you can hold
[3207.04 --> 3213.36]  them in balance, you can build a pretty healthy culture, right? And you're the one who has to do
[3213.36 --> 3219.40]  that. And it means disappointing some people at certain times. And I saw a really good tweet about
[3219.40 --> 3226.94]  this the other day, where someone basically said, nothing destroys an organization faster than a leader
[3226.94 --> 3232.66]  with a desire to be well liked. I think that's true. I think if your goal is to be liked all of the time,
[3232.66 --> 3238.20]  you just give people the sugar rather than the vegetables, right? Like, if I gave my two year
[3238.20 --> 3244.16]  old everything he asked for, for his dinner, he'd be eating a lot of ice cream, and he'd be happy for
[3244.16 --> 3249.22]  the moment. In the long run, I don't think it'd be so good for him, definitely not his teeth, at least,
[3249.32 --> 3255.22]  right? And so sometimes you just have to kind of say, you know, you have a perspective or a view of
[3255.22 --> 3260.18]  things, and you have to hold firm to it, even though it's not exactly the most popular thing to do. But
[3260.18 --> 3266.90]  in the long run, I think you're measured in years, maybe even decades. And so sometimes it can feel
[3266.90 --> 3271.52]  a bit lonely from that perspective. On the other hand, if you surround yourself with a great team,
[3272.10 --> 3277.40]  and I think this team is phenomenal, I love this team, it is incredibly delightful in ways that I
[3277.40 --> 3281.54]  also never expected. So it's a mix. It's a big mix, but I wouldn't change it.
[3282.00 --> 3287.38]  The balance you speak of is certainly part of the joy and frustration, because it's like, wow,
[3287.38 --> 3292.14]  I get to balance, you know, these different things, or I get to put certain practices or
[3292.14 --> 3298.02]  systems in place to organize the chaos that might ensue if there is an organization. You know,
[3298.04 --> 3303.18]  I get to help orchestrate that. And maybe not solo, but I get to influence, I get to put the right
[3303.18 --> 3308.66]  people in place to lead in the best way as possible to create that balance. Yeah, I think
[3308.66 --> 3313.22]  you're spot on with the balances. If you don't have that balance, things really get off kilter,
[3313.22 --> 3320.36]  and it can be a bad thing. Exactly. And you can barely influence the now. Like you get about six
[3320.36 --> 3326.60]  months of the decisions you make now are probably come into fruition in six months time. And that
[3326.60 --> 3332.58]  kind of filters like, you know, down through the different organizations and whatever. And so
[3332.58 --> 3338.76]  you have to think clearly about where you want to be in the long term and whether things are being
[3338.76 --> 3343.76]  shaped towards it. And also, I don't really want to build the type of company where I make all the
[3343.76 --> 3351.12]  decisions. I'm not the smartest person in the room, right? There's amazingly talented folks here that
[3351.12 --> 3357.84]  have honed their craft over many years. The more I can give them to decide and build against and do
[3357.84 --> 3363.30]  what they know, decentralize how things are done, the better things will be. If you just limit the
[3363.30 --> 3370.88]  company behind the world that you'd see, you will stumble because you have your own perspective and
[3370.88 --> 3375.56]  viewpoint on the world. And it's not the same as everyone else's. That's why I try and also talk to
[3375.56 --> 3382.30]  young developers that are very unreasonable and have very unreasonable views of the world or what
[3382.30 --> 3387.78]  products can do, because it tells you something. That's why I think serverless is such a fantastic
[3387.78 --> 3392.36]  movement, because it's really unreasonable in wonderful ways, right? Like the demands
[3392.36 --> 3397.28]  on building a serverless product are really hard. Like it goes against the trend of how we
[3397.28 --> 3401.98]  traditionally build applications. But it's that unreasonableness that is so optimistic to me.
[3402.08 --> 3408.08]  It's like, yeah, like actually previously you couldn't do this or you, you know, actually this is a
[3408.08 --> 3411.50]  really hard problem, but you know what? We're not going to stop until you reduce it into something
[3411.50 --> 3419.28]  that can be simply understood and mastered. And that is really, really tough, but it's an amazing
[3419.28 --> 3422.98]  discipline and it's great fun to do with really awesome people.
[3423.40 --> 3426.94]  What do you think you've changed in your life as you've taken on this new role? Like when you,
[3427.62 --> 3431.46]  I can just, the reason why I ask this question is I can see in my life when I've taken on new,
[3431.76 --> 3436.60]  new challenging roles that I've never filled before, how I would shift and change my perspective
[3436.60 --> 3442.38]  and my psyche. I might not so much change my habits and eating habits and whatnot, but I might just
[3442.38 --> 3446.88]  be a bit more disciplined in certain things. Do you intend to get more sleep than you did before?
[3446.88 --> 3452.12]  Did you commit to reading certain books or getting a coach or like, what were some things that you
[3452.12 --> 3454.78]  bolted on new when you took on this role?
[3455.36 --> 3462.72]  I think my appreciation for anyone that's managed to build a successful company and learning from them.
[3463.30 --> 3469.78]  And I think people, you know, we oversimplify what it takes and the immense kind of emotional burden
[3469.78 --> 3476.04]  that it puts on everyone involved in doing so. And I've gained an incredibly strong appreciation
[3476.04 --> 3480.84]  for that. And I think it's made me a lot less critical of others because you kind of walk a
[3480.84 --> 3485.46]  mile in their shoes and you're like, yes, it's hard. I've tried to be more disciplined. I've tried
[3485.46 --> 3491.24]  to stick to more of a routine. I've tried to be less reactive to just general things that happen
[3491.24 --> 3500.38]  and just more focused because I've realized that scope creep and time creep, like you have to be so
[3500.38 --> 3506.54]  much more disciplined with your time because no one will value your time as much as you will yourself.
[3507.24 --> 3516.36]  And a loss of time and burning and wasting time has and can have an extremely detrimental effect on you
[3516.36 --> 3523.32]  and your company. And at the end of the day, I just want to bring home a massive win for everyone that's
[3523.32 --> 3529.80]  come to this company and is here building something. And I want to deliver something amazing
[3529.80 --> 3536.32]  for our users. And I take that just extremely seriously. And it just takes daily thinking
[3536.32 --> 3542.70]  and iterating over the problems continually. And look, I don't want anyone to listen to me and think
[3542.70 --> 3549.02]  that I've made it or there's any advice here worth taking. You have to find your own path.
[3549.02 --> 3554.28]  But I think just dedicated to being learning, learning and seeing how you're wrong. And you
[3554.28 --> 3560.32]  kind of learn that over and over again. And you really see the effects of your decision compound
[3560.32 --> 3566.08]  over time. And it's very stark. It's great to have that kind of challenge. I think it makes you better
[3566.08 --> 3567.34]  if you're dedicated to being better.
[3567.82 --> 3573.04]  What about the fact that you're now in general availability? How does that shift the focus of the
[3573.04 --> 3577.62]  company? It's like being in like closed beta or limited beta, you're in one way, you're like
[3577.62 --> 3582.24]  perfecting product, you're doing certain things behind the scenes, not quite focused on growth,
[3582.30 --> 3587.32]  but kind of focused on growth because, hey, it's the you want to. But like, how does the company
[3587.32 --> 3591.88]  momentum shift at large now being general availability?
[3592.54 --> 3597.30]  It definitely accelerates in the sense that we're now it's on, right? Like you launch,
[3597.30 --> 3605.56]  you kind of launch once and it's happened. It feels awesome. We were very lucky that even during
[3605.56 --> 3610.72]  beta major websites moved to PlanScale, which is so awesome.
[3610.94 --> 3615.12]  You want to name some names? Can you name any names? A couple, I'm sure, at least they're on your
[3615.12 --> 3615.80]  website, right?
[3616.16 --> 3620.50]  Unfortunately not. So we have some case studies coming out soon.
[3620.60 --> 3620.86]  Okay.
[3620.86 --> 3626.30]  But yeah, like to see that happen, to see people up and running and successful while in beta
[3626.30 --> 3633.16]  is a testament to how our teams have worked and how well they build things. Yes, like we have rough
[3633.16 --> 3638.34]  edges. Everyone does. That's not, you know, we always will. But it was an awesome period to be in
[3638.34 --> 3644.60]  beta. Like it was really fun to learn and meet customers and talk to customers. And now it's just
[3644.60 --> 3649.40]  about continuing that. And it's like the beginning of the beginning. We've only just started to deliver
[3649.40 --> 3655.24]  the very beginning of what our technology can do. And like in the announcement post, I said,
[3655.64 --> 3660.78]  probably around 10% of the Tesla's power has been shown through the PlanScale platform.
[3660.78 --> 3661.26]  Yeah.
[3661.56 --> 3666.74]  So the next year, the next couple of years is really about starting to show that and really
[3666.74 --> 3673.42]  changing people's expectation of what databases can do and should do. We've been in this kind of
[3673.42 --> 3678.60]  conventional wisdom up until now has been do less with the database, move,
[3678.60 --> 3684.80]  concerns and pieces of the architecture away from the database. And I think we're going to lead
[3684.80 --> 3690.52]  a new way of thinking in terms of bringing more back to the database. Actually, a well-run,
[3690.52 --> 3696.26]  well-factored database can actually do a lot for you. That's going to get super exciting. So being
[3696.26 --> 3702.00]  out of GA was good. It was good for all of us. It feels like a release of tension. And now we're there and
[3702.00 --> 3709.70]  the product's ready. And it just helps even more with companies and sales getting on board. Now
[3709.70 --> 3711.82]  we're past the whole phase of the beta.
[3711.82 --> 3726.70]  This episode is brought to you by Gitpod. Gitpod lets you spin up fresh, ephemeral,
[3726.86 --> 3730.78]  automated dev environments in the cloud in seconds. And I'm here with Johannes Landgraf,
[3730.90 --> 3734.98]  co-founder of Gitpod. Johannes, GitHub made a big announcement recently with Codespaces,
[3735.30 --> 3738.90]  validating that it is now time for dev teams to consider what automated dev environments
[3738.90 --> 3742.86]  can do for them. What do you have to say to that? I'd say welcome to the party,
[3743.04 --> 3748.38]  GitHub and Microsoft. No, honestly, we were very excited because it validated to the developer
[3748.38 --> 3753.00]  community what we have been pioneering over the last years, that developer environments need to
[3753.00 --> 3757.88]  be automated and ephemeral. We are now at the right place and the right time to move software
[3757.88 --> 3761.96]  development to the cloud for everybody, not just for developers working for the Googles,
[3762.12 --> 3767.26]  Facebooks, or Shopify's who left local development already for several years. Gitpod is open source
[3767.26 --> 3772.14]  and provisions for every development team on GitHub, GitLab, and Bitbucket cloud-powered dev
[3772.14 --> 3776.38]  environments. You can access your developer environments via upstream VS Code running on
[3776.38 --> 3781.64]  your desktop or in the browser and soon also all JetBrains IDs. Very cool. If this gets you excited,
[3781.72 --> 3787.56]  learn more and get started for free at gitpod.io. Gitpod is free for individual developers for 50 hours a
[3787.56 --> 3793.14]  month, can be self-hosted and is available for every developer today. Again, gitpod.io.
[3793.14 --> 3821.26]  Another thing you mentioned in that announcement post was just the framing of the beginning. You said
[3821.26 --> 3827.00]  the beginning of the journey was December 1st, 2020. You said this is when the first line of
[3827.00 --> 3834.02]  code was committed on PlanetScale's cloud database platforms. I mean, like, okay, I'm not that bad at
[3834.02 --> 3840.92]  math, but like it's not even December 1st of 2021. So less than a year later, beta to general availability.
[3841.58 --> 3846.70]  I didn't add up all your funding. I think it's probably 80-ish, 100-ish million dollars in funding
[3846.70 --> 3852.32]  raised so far. Most recent year, Series C, $50 million Series C, led by Kleiner Perkins.
[3852.76 --> 3855.22]  You're moving at an incredible clip.
[3855.86 --> 3862.86]  Yes. That astounds me, honestly. And again, it's like that compounding just improvement daily
[3862.86 --> 3869.50]  and just the pace. And we talk about pace internally. Pace is an incredible competitive advantage.
[3869.50 --> 3875.98]  I think any company can be quick and develop something quickly for three months or whatever,
[3876.58 --> 3884.60]  and then it becomes reckless or whatever. We obsess over having a pace that is aggressive,
[3885.24 --> 3886.84]  but sure-footed.
[3887.18 --> 3890.52]  How do you do that? How do you put that pace into motion? Can you give me some of the mechanics?
[3890.64 --> 3895.66]  Like, how do you say, hey, team, this is our pace? And they're like, okay. What are the mechanics
[3895.66 --> 3896.94]  of how you put that pace into motion?
[3896.94 --> 3901.04]  Yeah, you're right. We are moving a real clip. And that's actually why I put that in there,
[3901.10 --> 3905.92]  because I want people to know this. One, because I'm just so incredibly proud of the team and how
[3905.92 --> 3910.76]  they've done it. And two, I want people to know that buying and kind of being part of this journey
[3910.76 --> 3918.80]  means you're going to get more and more amazing things very quickly. And so we talk about pace a lot
[3918.80 --> 3925.76]  internally at PlanetScale and having the right pace of delivering things quickly with high quality
[3925.76 --> 3930.26]  and being short-footed. And pace is this incredible competitive advantage.
[3930.78 --> 3936.08]  If you look at companies like Apple, people judge their individual things they deliver.
[3936.76 --> 3940.80]  This doesn't make sense. They've removed the headphone jack or whatever.
[3941.70 --> 3948.06]  And then over time, you see that they're moving at this pace that is measured in the decade.
[3948.06 --> 3952.50]  And then you look back at what Apple has done in a single decade, you're like, my God,
[3952.56 --> 3958.24]  they've changed personal computing again. But if you zoom in at a quarter, it just doesn't look like much.
[3958.46 --> 3964.38]  And so we want to hold this steady pace that means we don't lose focus.
[3964.38 --> 3970.88]  We don't slow down because it's sustainable. And I think most engineering teams or most companies could probably
[3970.88 --> 3978.42]  put all their employees on a death march for a quarter and catch up and deliver something kind of quickly.
[3978.60 --> 3983.22]  But by the end of it, everyone's burnt out. They're tired. They're upset. And they're not going to do it again.
[3983.22 --> 3991.88]  But if you have a pace where people feel energized and motivated and the pace is a focus, because if you think about your pace as a company
[3991.88 --> 3998.00]  and you obsess over it, you can avoid getting dragged down by unnecessary process.
[3998.52 --> 4005.20]  How many companies lament when they were tiny and small and agile and could get things done?
[4005.78 --> 4008.82]  And they slow down as more people get added into the mix.
[4008.82 --> 4015.88]  And if you focus extremely hard on your culture and not losing that pace, you question why things have slown down.
[4016.46 --> 4024.84]  You can deliver things well and reasonably without becoming this slow, like big company that doesn't get anything done.
[4025.14 --> 4029.36]  And we don't want to be that. We want to keep delivering year after year.
[4030.28 --> 4036.34]  And yeah, everything that exists on our platform pre-December of last year is pretty much just for tests.
[4036.34 --> 4041.24]  Everything else was rewritten from the ground up to deliver the PlanetScale platform.
[4041.90 --> 4044.76]  And the team did a phenomenal job. Really phenomenal.
[4045.38 --> 4048.28]  When it comes to, I guess, competition, so to speak.
[4048.40 --> 4050.20]  So Vitesse is open source.
[4050.72 --> 4055.26]  You're talking about pace and being able to be ahead of competition, so to speak.
[4055.66 --> 4064.60]  If Vitesse is open source, obviously somebody else can adopt Vitesse and do universe scale versus planet scale.
[4064.60 --> 4067.96]  You know what I'm saying? Or a solar system scale.
[4068.10 --> 4069.86]  Whatever the next layer up is.
[4070.18 --> 4070.28]  Yeah.
[4070.44 --> 4073.06]  How do you look at, say, MySQL, Postgres?
[4073.34 --> 4075.80]  How do you look at serverless, not serverless?
[4075.86 --> 4079.54]  How do you look at the different options when it comes to a database and compete against them?
[4079.96 --> 4082.20]  Or just showcase what you do better or do differently?
[4082.62 --> 4084.60]  How do you map out the whys of what you've done?
[4084.60 --> 4086.16]  So we are open source.
[4086.62 --> 4089.80]  We don't hide behind BSL licensing.
[4090.96 --> 4093.16]  And it is true that someone could go and use Vitesse.
[4093.80 --> 4095.28]  It wouldn't be as easy for them.
[4095.52 --> 4097.02]  We have the Vitesse experts.
[4097.20 --> 4100.26]  The Vitesse maintainers and core contributors work for PlanetScale.
[4100.46 --> 4102.78]  So that's an advantage that we have.
[4103.34 --> 4105.42]  But also people can't really clone taste.
[4105.54 --> 4106.58]  And I've said this before.
[4106.58 --> 4112.90]  When you're building things well, with taste, with quality, it's very hard for companies to copy.
[4113.88 --> 4117.10]  And we make it harder the higher that we raise the bar.
[4117.60 --> 4118.44]  MySQL is great.
[4118.60 --> 4119.94]  Great backend technology.
[4120.28 --> 4122.54]  Postgres, again, is a great backend technology.
[4123.44 --> 4125.48]  They are storage engines.
[4126.24 --> 4129.18]  And they both do good things that are very similar to each other.
[4129.30 --> 4134.84]  I think the fact that that's still the debate between the two in 2021 is quite depressing.
[4134.84 --> 4145.62]  I don't think about the competition much because the vision we have for the company and for databases far exceeds anything anyone is doing right now or has done.
[4146.12 --> 4148.22]  And so I keep my eye on that.
[4148.64 --> 4150.18]  We've already started to show this, right?
[4150.80 --> 4152.20]  We put branching out there.
[4152.76 --> 4153.84]  Hadn't been seen before.
[4154.30 --> 4155.36]  Very quickly copied.
[4155.52 --> 4157.68]  Five or six vendors just copying it.
[4157.74 --> 4157.94]  Fine.
[4158.66 --> 4159.24]  It's good.
[4159.52 --> 4162.56]  I would rather be in the situation being copied than doing the copying.
[4162.56 --> 4171.50]  And we will make sure that the bar goes up every single year for what it takes to put a competitive market database into the market.
[4171.96 --> 4173.90]  And we'll fight that war on every front.
[4174.08 --> 4176.74]  There's the taste, the ease of use front.
[4176.90 --> 4177.94]  And then there's the scale front.
[4178.66 --> 4184.70]  When we are in calls with customers and if they're competitive with other database platforms, you ask them what's the biggest customer.
[4184.70 --> 4188.48]  And then you compare it to whoever's running Vitesse or whatnot.
[4188.78 --> 4192.32]  And it just ends the conversation very quickly usually.
[4192.96 --> 4196.46]  You seem like you're trying to do something different to databases than anybody else is trying to do before.
[4196.54 --> 4203.28]  Like you're just truly trying to look at every different angle of the way a developer would, one, interact with and use it.
[4203.28 --> 4210.12]  And then, two, the way it obviously gets put into production and works for the end user because that's the goal, right?
[4210.12 --> 4210.40]  Yes.
[4210.50 --> 4220.42]  The necessary detail of the database is that it performs in production so that it can satisfy a user's desired feature so they can get their job done doing whatever they do.
[4220.42 --> 4233.64]  Whether it's searching YouTube or whether it's posting a Slack message or looking at a GitHub commit and seeing some of the history, whether it's today or last year, you want that to perform very well.
[4234.10 --> 4235.30]  And that is the table stakes.
[4235.50 --> 4237.34]  And we take that extremely seriously.
[4237.50 --> 4242.02]  And that's why we put equal focus on the back end and what the database does.
[4242.70 --> 4246.16]  We just decided to take it further onward from there, right?
[4246.16 --> 4251.66]  Like most PMs at database companies, I think all they think about is how queries perform, how well it works.
[4251.72 --> 4252.94]  And, of course, we think that way.
[4253.74 --> 4261.44]  You know, we wouldn't be the most scalable and we wouldn't have the tests perform in such a proven way if that wasn't a focus.
[4262.10 --> 4263.14]  We just obsess it.
[4263.20 --> 4266.00]  And like you said, we obsess over the daily lives of developers.
[4266.00 --> 4271.88]  It's not just enough to do what databases are meant to do and then just throw our hands up and give up.
[4271.88 --> 4279.42]  We think about, no, how does the database join you in your software development lifecycle?
[4280.16 --> 4285.88]  That's why branches are not just there to be a place where you experiment or stage schema changes.
[4286.24 --> 4288.52]  They're designed to be your development environment.
[4288.64 --> 4289.86]  They're designed to be isolated.
[4290.10 --> 4300.26]  The reason we don't have a local, you can download the tests locally, but we don't have a local copy of like PlanetScale's functionality is because we're long on the future of development being cloud-based.
[4300.26 --> 4305.88]  Back in December of last year, I did an internal demo of PlanetScale working with GitHub Codespaces.
[4306.62 --> 4317.34]  And we thought about the ergonomics of using PlanetScale as your development database because we go that far into thinking about how we make developers' lives better all over.
[4318.06 --> 4320.14]  And the database is such a source of pain.
[4321.08 --> 4324.68]  And you've done a great job if you get it to not be a source of pain.
[4325.02 --> 4326.78]  We want it to be a source of delight.
[4327.00 --> 4329.38]  And that takes that additional level of obsession.
[4330.26 --> 4331.16]  Why serverless?
[4331.24 --> 4332.24]  Why the big bet on serverless?
[4332.32 --> 4333.02]  You say cloud.
[4333.66 --> 4334.70]  Why the big bet on serverless?
[4334.80 --> 4335.56]  Why is this the future?
[4336.02 --> 4338.34]  Well, I think it's what the cloud is supposed to have been.
[4338.84 --> 4344.06]  You look at what a lot of the major clouds provide for you now, and some provide very good services.
[4344.20 --> 4348.30]  And Amazon has some great services like S3 and whatever.
[4348.92 --> 4350.34]  But that didn't go far enough.
[4350.54 --> 4352.80]  I think the real promise of the cloud has yet to be met.
[4353.00 --> 4354.50]  And it's starting with serverless.
[4354.50 --> 4364.42]  It's starting, we think of this cloud of this like ever-expanding, powerful thing that can just enable so much for what we do.
[4364.54 --> 4367.48]  And everything is connected to the cloud and whatever.
[4367.48 --> 4370.86]  But it's got a long way to go in terms of user experience and usability.
[4371.44 --> 4372.68]  And it's complex.
[4372.90 --> 4380.90]  And people who say they have a large Amazon architecture or whatever, they've got a large operation scene behind that.
[4381.00 --> 4390.88]  And with this new era of products and these new companies that are kind of baking themselves into this mold of this serverless model, I think that will start to change.
[4390.88 --> 4392.08]  We'll still need operators.
[4392.20 --> 4392.88]  Of course we will.
[4392.98 --> 4396.98]  And they're so important and critically important internally in what we do.
[4397.66 --> 4399.38]  But it's not just about that.
[4399.50 --> 4404.66]  It's about what our customers can do without having to hire up massive teams.
[4404.80 --> 4419.10]  And I've said this before, and a lot of people have made the similar prediction, which is there's going to be massive, multi-billion-dollar companies that are like five or ten people because they have managed to leverage so many of the tools and serverless platforms out there.
[4419.10 --> 4431.98]  And so serverless is this all-in, much more refined view of how you can deliver cloud products without passing on silly, meaningless abstractions.
[4432.08 --> 4437.94]  Like I remember I signed up when I was doing my sort of early discovery of what we should build as a product.
[4438.20 --> 4441.20]  I was signing up for other database products.
[4441.32 --> 4446.98]  And it's like they're asking you to specify vCPUs and stuff like this.
[4446.98 --> 4459.96]  And it's like if you're a founder with the next stripe in your head that you need to bring to the world, why the hell are you trying to work out what a vCPU means?
[4460.08 --> 4460.88]  What does it mean?
[4461.06 --> 4463.68]  Like I don't know how bad your software is.
[4463.76 --> 4465.90]  I don't know what resources are consumed.
[4466.08 --> 4470.22]  I just want to do the thing you promised you were going to do, right?
[4470.22 --> 4476.34]  Like how do I reason about 10 vCPUs versus 24 vCPUs on software I've never used before?
[4476.70 --> 4477.36]  It's just silly.
[4477.54 --> 4478.30]  It's lazy.
[4478.50 --> 4479.64]  It's hostile to the user.
[4480.08 --> 4490.44]  We just say we're going to give you a performant database and we're going to charge you for the things you know you do with it, which is query it and store data on it.
[4490.92 --> 4492.04]  And that's the experience.
[4492.04 --> 4498.02]  It seems so logical the way you describe it and put it into market.
[4498.26 --> 4501.52]  I mean it seems like that's – maybe that's why you're winning.
[4502.22 --> 4503.08]  That's how it should be.
[4503.34 --> 4504.26]  You know, it could be.
[4504.36 --> 4505.08]  We haven't won yet.
[4505.18 --> 4512.52]  But I think it's – when you look at the amount of other serverless databases that have followed suit, it's clearly resonant with people.
[4513.28 --> 4515.48]  Yeah, and I think, again, we're going to keep moving that boundary.
[4515.48 --> 4524.36]  It would have just seemed weird, like, to develop a product like this now or in the last three or four years and not make it something serverless.
[4525.24 --> 4526.80]  You've had a big November.
[4527.00 --> 4528.90]  You've got Managed Cloud out there.
[4529.06 --> 4529.64]  You went GA.
[4530.14 --> 4531.58]  We talked about database imports.
[4532.06 --> 4539.86]  We didn't touch on – because this is an announcement podcast by any means – but we didn't touch on the Prisma data platform integration that you've got going on.
[4539.86 --> 4546.24]  And I'm sure that's a big win for you as well, how that plugs into Vercel and how easy it is to take essentially an application of production.
[4546.32 --> 4556.74]  Like you said, like just this idea, and I think that's what's really interesting about where you're going and what Vercel is doing and what Netlify is doing and what Prisma is doing in terms of their data platform.
[4556.74 --> 4567.88]  I'm just like enabling that future founder who's got the next stripe idea in their head to just build the company initially technologically pretty easily, in quotes, pretty easily.
[4568.36 --> 4576.74]  You know, with these – being able to use technology like yours that's still on the shoulders of giants, the giants, the giant shoulders essentially, as you've said before.
[4577.48 --> 4580.44]  And you don't have to scale to a certain amount of people.
[4580.44 --> 4586.28]  I think actually – I mean if you have a billion-dollar company, if you have five or ten people, that's pretty impossible.
[4586.64 --> 4587.02]  So I don't know.
[4587.08 --> 4588.02]  I'm not sure about that, Sam.
[4588.06 --> 4589.32]  You have to check your math on that one.
[4589.48 --> 4589.88]  We'll see.
[4590.68 --> 4593.24]  We'll meet up in a few years and we'll see who's right.
[4593.40 --> 4593.66]  Okay.
[4593.90 --> 4595.28]  We'll see where that prediction is.
[4595.66 --> 4598.86]  We'll have to get more specific on it to make the prediction right though because, I mean –
[4598.86 --> 4599.10]  Okay.
[4599.24 --> 4602.84]  A billion dollars, five or – let's say sub-ten people.
[4603.02 --> 4603.34]  Yes.
[4603.38 --> 4604.30]  Would you say sub-ten people?
[4604.44 --> 4604.78]  Yes.
[4604.80 --> 4606.04]  Would be a good stretch for you then?
[4606.24 --> 4606.46]  Yeah.
[4606.46 --> 4612.70]  I think that'd be possible, but they would be eking at the seams for sure with ten people.
[4612.82 --> 4614.04]  They'd need to scale people.
[4614.58 --> 4615.50]  Nice problem to have.
[4615.64 --> 4615.82]  Yeah.
[4615.94 --> 4618.16]  At least it wasn't their tech stack that was getting in the way.
[4618.22 --> 4618.60]  That's true.
[4618.72 --> 4618.90]  Okay.
[4619.00 --> 4619.26]  Touche.
[4619.44 --> 4619.96]  Got you, Sam.
[4620.02 --> 4621.80]  That's an amazing amount of answer.
[4621.96 --> 4622.22]  Okay.
[4622.28 --> 4624.34]  So they don't have a staff of DevOps potentially.
[4625.08 --> 4625.38]  Right.
[4625.44 --> 4625.82]  Exactly.
[4626.16 --> 4626.72]  They'll have just –
[4626.72 --> 4626.96]  Okay.
[4627.18 --> 4628.66]  A few motivated developers.
[4629.04 --> 4629.36]  Yeah.
[4629.36 --> 4639.74]  I've heard of one-person teams making $8 to $10 million a year in like the Haroku app store and things like this, like single developers building useful bits of functionality.
[4640.40 --> 4642.50]  We'll see what the world comes – what it comes to.
[4642.78 --> 4644.46]  But working with Prisma has been fantastic.
[4644.64 --> 4644.86]  Okay.
[4644.86 --> 4648.48]  That is a team of people that, again, have just great taste.
[4648.48 --> 4656.28]  They have attracted and inspired a whole audience of young, talented, motivated developers.
[4657.02 --> 4658.64]  We love working with the Prisma team.
[4659.30 --> 4664.52]  When we started speaking to them, it was clear there was a big unmet need in terms of the back end.
[4665.18 --> 4672.88]  How a truly powerful serverless SQL database would just be perfect for their user base.
[4672.88 --> 4677.48]  And we were just really grateful to be able to partner with them on their platform.
[4677.80 --> 4683.70]  And, you know, being the database there that is powering the back end just is great.
[4684.28 --> 4692.70]  Every day on Twitter, multiple times a day, I see people saying, oh, just picked up my new stack, PlantScale, Prisma, Netlify, Vercel, whatever.
[4693.48 --> 4694.42]  And they just love it.
[4694.48 --> 4696.28]  And they're just like up and running, producing people.
[4696.34 --> 4699.92]  People are doing tutorials of like building apps in like an hour.
[4699.92 --> 4707.50]  And you think to yourself, well, that stack is going to scale to like probably a few million users really before it has problems.
[4707.76 --> 4709.70]  And that's just never been done before.
[4709.96 --> 4712.78]  And that just makes me so excited and optimistic.
[4713.40 --> 4723.54]  And just working with like-minded companies that love developers and love building great user experiences as much as we do is, it's awesome.
[4723.94 --> 4727.42]  Can I call out one of the tweets that you're probably mentioning, if you don't mind?
[4727.52 --> 4728.12]  Can I call out one of them?
[4728.32 --> 4729.32]  Yes, go for it.
[4729.32 --> 4730.10]  Brian Lovin.
[4730.28 --> 4731.04]  You probably know him.
[4731.28 --> 4733.00]  Co-founded Spectrum, acquired by GitHub.
[4733.38 --> 4734.44]  I love Brian Lovin.
[4734.66 --> 4736.78]  He's a great person, incredibly talented.
[4737.18 --> 4737.42]  Yeah.
[4737.88 --> 4746.16]  He says, it's wild how Prisma and PlantScale together have empowered me to build things I would have never even tried to make before.
[4746.30 --> 4752.66]  And I think that's what's interesting about timing, as you said before, momentum and demand.
[4752.78 --> 4754.16]  Because demand, that's demand, right?
[4754.16 --> 4761.74]  Once you realize when you couple a few things together in a unique way that was never possible before because one, it didn't exist.
[4761.74 --> 4765.10]  And now the internet might even have the user base.
[4765.10 --> 4770.56]  Because like you couldn't have built the application 10 years ago that had that kind of demand because it just, the people weren't there.
[4770.78 --> 4779.62]  10 years ago, the internet did not have the same amount of people on it to have that demand or that accessible demand that mobile phones bring or whatnot.
[4779.62 --> 4784.88]  I mean, I just think that's interesting how you could be at a certain place in a certain time, have that kind of demand.
[4785.08 --> 4790.14]  In Brian's case, that you could put these two things together and build things you never thought before because they just weren't there.
[4790.62 --> 4790.96]  It's awesome.
[4791.38 --> 4800.16]  It makes me so excited about our future as an industry or a species that technology is getting so much better that it's enabling these things to happen.
[4800.84 --> 4801.44]  It's just awesome.
[4801.44 --> 4803.62]  I mean, it's the same with the power of open source as well.
[4803.76 --> 4808.00]  It's just the things that are happening, the collaboration that's happening, people coming together.
[4808.68 --> 4811.62]  It really feels like the promise and the future.
[4812.40 --> 4813.90]  And Brian is wonderfully complimentary.
[4814.14 --> 4817.80]  And it makes me so excited to read people.
[4817.84 --> 4820.16]  You know, people say these things every day now.
[4820.58 --> 4822.14]  And it has the same effect on me.
[4822.20 --> 4828.28]  Every time you read it, you just feel so proud and also so excited because you know what's coming next.
[4828.28 --> 4832.54]  We know, I know, at PlanetScale, that we have just begun.
[4833.16 --> 4836.44]  And it feels like we're just welcoming people through the door of the chocolate factory, right?
[4836.50 --> 4838.86]  And there's such a big wild ride to come.
[4839.48 --> 4841.54]  And that gets me up every single day.
[4841.80 --> 4842.46]  I just wake up.
[4842.70 --> 4845.44]  Sometimes it gets to Friday night and I'm just sad the week's over.
[4846.06 --> 4850.34]  I wake up every day just so hyped and excited to do this.
[4850.88 --> 4851.60]  I just love it.
[4851.72 --> 4852.60]  I absolutely love it.
[4852.70 --> 4854.08]  And I love the people we get to do it with.
[4854.08 --> 4858.10]  Well, speaking of what's next, you mentioned or we talked about your serious funding.
[4858.36 --> 4858.80]  Congratulations.
[4859.60 --> 4859.98]  Thank you.
[4860.16 --> 4863.16]  General availability of the platform is out there.
[4863.48 --> 4865.36]  You've got some adoption happening, obviously.
[4865.78 --> 4872.00]  And you're shifting your focus to something new since only 10% of what you've been able to do is out there.
[4872.64 --> 4873.62]  I love to ask this question.
[4873.82 --> 4874.82]  I didn't prep you for it.
[4874.88 --> 4879.16]  So this is sort of a curveball to some degree, but I'm sure you'll handle it no problem.
[4879.70 --> 4880.68]  But what's on the horizon?
[4880.68 --> 4885.72]  What's something people know nothing about or very little about that you can share?
[4885.84 --> 4889.70]  What can you tease about the very next big thing coming from PlanetScale?
[4890.06 --> 4890.38]  Okay.
[4890.54 --> 4896.34]  It is a tease because we don't publicly share our roadmap just because we don't want to disappoint people.
[4896.76 --> 4901.02]  The tease I will say is Vitesse wasn't just YouTube's database.
[4901.46 --> 4907.58]  It filled a number of roles that are essential to building a very large scale operation.
[4907.58 --> 4910.84]  Those things are Invertest, they're mature, they're stable.
[4911.94 --> 4916.82]  And throughout next year, a bunch of those primitives are going to peek through into our product.
[4916.98 --> 4924.36]  Our job now is to build incredibly simple and beautiful user experiences on top of what's already there.
[4925.12 --> 4930.88]  And yeah, it's coming soon for folks that are already on the platform and getting them excited.
[4930.88 --> 4941.06]  There's a lot of fundamental work we could do to make developers' lives simple in terms of learning databases, gaining knowledge, and harnessing that power.
[4941.56 --> 4953.14]  And we have a lot of great ideas on how we can do that and bring modern database practices to the modern developer and really start to meet their expectations.
[4953.14 --> 4955.10]  So it's going to get very exciting.
[4955.48 --> 4967.46]  There's a feature that is nearly done that just we would have avoided hours or days in total of downtime with GitHub if that existed when we were doing our thing.
[4967.76 --> 4970.40]  So I'm very excited to put that into the world.
[4970.76 --> 4971.94]  No other product has done it.
[4972.08 --> 4973.70]  It has not been achieved so far.
[4974.32 --> 4977.06]  It is fully stable and ready in the back end.
[4977.14 --> 4979.24]  And now we're just adding the polish and making it happen.
[4979.78 --> 4980.06]  Okay.
[4980.14 --> 4981.04]  So coming soon then?
[4981.36 --> 4981.92]  Coming soon.
[4981.92 --> 4982.64]  All coming soon.
[4982.64 --> 4984.88]  It's going to be a Christmas gift or a New Year's gift.
[4984.98 --> 4987.32]  What's a rough – you mean a rough ETA?
[4987.68 --> 4994.02]  I wouldn't want to ruin everyone's Christmases by taking them away from their families to play with great, fun database products.
[4994.16 --> 4995.70]  So it will be early next year.
[4995.80 --> 4996.18]  Q1.
[4996.30 --> 4996.54]  Okay.
[4996.78 --> 4997.28]  Q1.
[4997.44 --> 4997.64]  Yeah.
[4997.90 --> 4999.30]  The big Q1.
[4999.44 --> 5011.18]  Sam, I've had so much fun talking to you through your journey, through the test, through what you've done with the test, with PlanetScale, the way that you love on developers, the way that you care about the – you know, that day one.
[5011.18 --> 5013.58]  That day one decision that doesn't have to be a day one only.
[5013.58 --> 5021.58]  That it doesn't have to be a redo into year three or four or five whenever you begin to scale beyond your abilities with current databases.
[5021.58 --> 5030.68]  And I just love the way that you have that gratitude perspective and how you look at each new hire as like this could be their first job ever.
[5030.82 --> 5032.32]  I just love the perspective that you bring.
[5032.42 --> 5039.22]  So I can imagine how fortunate your team must feel to have you as CEO of the company with the perspective you have.
[5039.22 --> 5041.38]  So I've really enjoyed the conversation we've had.
[5041.44 --> 5043.18]  Is there anything else that I haven't asked you?
[5043.20 --> 5046.18]  Anything else you want to put out there before we call this show a show?
[5046.74 --> 5049.10]  I just want to say a massive thank you for having me.
[5049.18 --> 5051.92]  It's been really enjoyable getting to know you and getting to chat.
[5052.18 --> 5061.88]  To everyone listening, if you want to experience the future of databases, planetScale.com or at iSamLambert on Twitter if you want to engage and chat about the world we're building.
[5062.44 --> 5063.44]  Sam, thank you so much.
[5063.62 --> 5064.30]  It's been awesome.
[5064.78 --> 5065.38]  I appreciate you.
[5065.60 --> 5066.00]  Thank you.
[5066.00 --> 5069.58]  That's it for this episode.
[5069.86 --> 5070.94]  Thank you for tuning in.
[5071.04 --> 5072.68]  If you enjoyed the show, do me a favor.
[5073.02 --> 5073.76]  Share it with a friend.
[5074.18 --> 5077.28]  And of course, thank you to Fastly for all that awesome bandwidth.
[5077.84 --> 5081.10]  And also Breakmaster Cylinder for making all of our awesome beats.
[5081.42 --> 5082.44]  Here's a pro tip for you.
[5082.66 --> 5084.60]  Check out changelaw.com slash master.
[5084.78 --> 5086.62]  That is our master feed.
[5086.94 --> 5089.88]  Get all our shows in one single feed.
[5089.88 --> 5094.68]  And for those super little listeners, check out changelaw.com slash plus plus.
[5094.80 --> 5095.38]  That's our membership.
[5095.38 --> 5098.44]  Get all our shows with no ads plus some other perks.
[5098.60 --> 5101.46]  Again, changelaw.com slash plus plus.
[5101.80 --> 5103.02]  That's it for this episode.
[5103.22 --> 5104.10]  Thanks for tuning in.
[5104.38 --> 5105.30]  We'll see you next time.
[5105.30 --> 5112.94]  We'll see you next time.
[5112.94 --> 5142.92]  We'll see you next time.
[5142.94 --> 5162.08]  We'll see you next time.
