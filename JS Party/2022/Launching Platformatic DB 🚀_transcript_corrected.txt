[0.00 → 7.06] It reads up your database schema, and it creates a REST API with OpenAI definition,
[7.26 → 10.72] as well as a GraphQL API on top of your schema.
[11.04 → 13.26] It supports relations and a few other bits.
[13.42 → 14.92] It also does migrations.
[15.24 → 15.92] It does log.
[16.32 → 18.36] It does what you would expect from a demo.
[18.52 → 19.92] Like a code generator or no?
[20.18 → 21.36] No, it just runs.
[21.54 → 22.88] It is what we wanted, okay?
[22.88 → 26.30] We believe that the best line of code is the one that you don't have to write.
[26.30 → 31.36] So if you need a code generator, we are essentially implying that you will need to maintain that code.
[31.50 → 33.00] We want to minimize friction.
[33.26 → 34.74] We want to remove the problem.
[39.32 → 42.08] This episode is brought to you by our friends at Square,
[42.30 → 44.02] developing the platform that sellers trust.
[44.30 → 45.24] Here's what you can do with Square.
[45.34 → 46.80] You can bridge more experiences.
[46.80 → 50.40] You can build online, mobile, and in-person commerce experiences
[50.40 → 52.68] that connect more customers and sellers.
[53.06 → 54.88] You can build custom booking solutions.
[54.88 → 56.14] You can create and track orders.
[56.14 → 57.24] You can accept payments.
[57.38 → 59.28] You can manage and curate inventory.
[59.68 → 60.76] You can organize customers.
[60.88 → 61.80] You can manage employees.
[62.34 → 64.42] You can extend Square gift cards to your app.
[64.52 → 66.02] You can use Afterpay.
[66.36 → 68.80] So much is available as a Square Solutions partner.
[69.28 → 71.88] Learn more and get started at changelog.com slash Square.
[72.04 → 74.62] Again, changelog.com slash Square.
[86.14 → 91.46] This is JS Party, your weekly celebration of JavaScript and the web.
[91.46 → 93.90] We record live each and every Thursday.
[94.42 → 95.88] Join in on the hi jinks.
[95.88 → 100.94] In our community Slack, sign up for free at jsparty.fm slash community.
[101.40 → 106.40] Special thanks to our partners at Vastly for shipping JS Party superfast to wherever you listen.
[106.76 → 108.44] Check them out at fastly.com.
[108.62 → 110.34] And to our friends at fly.io.
[110.58 → 112.68] Host your app servers close to your users.
[113.06 → 113.92] No ops required.
[114.22 → 116.28] Learn more at fly.io.
[116.28 → 118.54] Okay, hey, it is party time, you all.
[130.64 → 132.28] Hello, JS Party listeners.
[132.78 → 135.82] We are so excited to be back with you this week.
[136.10 → 138.70] We have a super hot off the presses show.
[138.94 → 143.02] Like this announcement just got dropped literally like less than an hour ago.
[143.02 → 146.38] I haven't even finished reading the blog post, but that's okay.
[146.68 → 155.52] But we're here to kind of announce and kind of usher into the world a new baby that's like open source from the Node community.
[155.52 → 157.00] It's called PlatformIO.
[157.16 → 159.28] We're here with the founders, creators today.
[159.86 → 163.22] And before we meet them, on the panel with me today is Chris Miller.
[163.66 → 164.36] Hello, Chris.
[164.70 → 165.38] Hello, Chris.
[165.68 → 166.14] Hi.
[166.64 → 168.02] You always make me laugh.
[168.10 → 169.02] Like, don't distract me.
[169.12 → 170.76] We have a tight show today.
[170.76 → 172.78] So I have to stay focused, okay?
[173.02 → 173.78] No distractions.
[174.10 → 175.92] So Chris, hello, Chris.
[176.26 → 176.64] Hi.
[177.06 → 177.42] Hi.
[177.74 → 178.06] Okay.
[178.62 → 180.60] I'll try not to screw things up for you.
[181.30 → 181.78] Thanks.
[182.22 → 186.96] On the show today to introduce their new project, PlatformIO, are Matteo Colin.
[187.22 → 188.12] Hello, Matteo.
[188.66 → 189.42] Hi, Amal.
[189.68 → 190.32] Hi, Chris.
[190.40 → 190.80] Hi.
[190.98 → 191.54] Hi.
[191.72 → 192.58] So glad to be back.
[192.94 → 193.36] Yeah.
[193.90 → 194.16] Yay.
[194.70 → 196.70] And Luca, Luca Karachi.
[197.24 → 198.56] Karachi, but he's perfect.
[198.92 → 199.36] Karachi.
[199.58 → 200.44] Yeah, hey, everyone.
[201.14 → 201.60] Hi.
[201.82 → 202.46] Hi, welcome.
[202.46 → 202.82] Yay.
[203.22 → 205.06] We're so excited to have you both today.
[205.28 → 207.70] So, Matteo, like, this is so funny.
[207.80 → 210.80] Like, I have not talked to you since the last time you were on this show.
[211.28 → 216.26] And so today's show is going to be kind of a mix of, like, me catching up with what's
[216.26 → 220.16] been going on in Matteo's life, because a lot seems to have changed since he was last
[220.16 → 220.74] on the show.
[221.56 → 224.32] And we're also going to learn about his new project.
[224.32 → 229.78] And what's really great is, like, Luca is someone who, as well as, like, in my friends, wider
[229.78 → 232.38] friend circle, we have a lot of very close mutual friends.
[232.70 → 236.48] And Luca and I have been, like, we've, like, had this friendship that was supposed to get
[236.48 → 238.24] started a few years ago, and it never happened.
[238.24 → 241.58] So now, like, this is, like, hopefully the beginning of that friendship.
[241.58 → 244.94] So hopefully informal show, we're learning about their new projects.
[244.94 → 248.42] And before we get into PlatformIO, Matteo, can you tell us a little bit about yourself
[248.42 → 249.52] and same thing for you, Luca?
[249.52 → 252.86] So let's, I don't know, I don't know where to start.
[253.30 → 253.72] Let's see.
[253.82 → 256.30] Let's remember what I said last time in the show.
[256.44 → 259.70] So if you don't, the previous part, it's on the previous show.
[259.88 → 262.18] So you go and watch and listen to that one.
[262.28 → 262.84] No, I'm joking.
[263.30 → 265.34] I have been coding for more than 30 years.
[265.82 → 272.52] I have been doing Node since 2010, 2011, putting Node in production since then.
[272.52 → 281.56] Part of the Node collaborators group since 2015, after a few years, got into the Node.js
[281.56 → 282.62] technical steering committee.
[282.82 → 283.00] Yeah.
[283.64 → 285.38] Kept working, maintaining Node.js.
[285.86 → 291.44] In the meanwhile, I started a new project called Hastily, which we talked about maybe one of
[291.44 → 297.22] the shows at some point, probably, and which is a web framework for Node that is getting
[297.22 → 298.12] some traction lately.
[298.70 → 300.02] So it's great.
[300.12 → 300.80] It works very well.
[300.80 → 304.16] It's super battle tested for high production usage of Node.js.
[304.94 → 307.68] For the last eight, years and a half, I've been in professional services.
[307.86 → 310.16] I work for a company called Near form.
[310.52 → 314.14] This is where I actually, when I was working at Near form, this is actually where I met Luca.
[314.92 → 317.32] And we have been colleague for a bit.
[317.56 → 323.22] Then we both had kids in 2020, which is, yeah.
[323.28 → 324.56] The world's greatest year.
[325.18 → 325.66] Yeah.
[325.66 → 329.48] The most fantastical year of the most fantastical century.
[329.48 → 330.70] Yes.
[330.70 → 331.10] Yes.
[331.10 → 331.16] Yes.
[331.16 → 335.44] And then we kept in touch after he left Near form a few years back, he will tell.
[335.44 → 336.74] And then we kept in touch.
[336.74 → 341.70] And in mid-June, I left Near form.
[341.70 → 347.96] And I have jumped into this new adventure with Luca, PlatformIO.
[347.96 → 354.62] And you can, it's, we have been keeping it to shoes for a couple of months because we need
[354.62 → 358.46] a little bit of time to actually develop something to announce to the world.
[358.64 → 358.80] Yeah.
[359.18 → 359.90] No vaporware.
[360.04 → 361.82] That's like the opposite of most developers though.
[361.86 → 365.90] Because like most developers, their first thing is like, they buy the URL, then they make
[365.90 → 368.08] the like vaporware announcement on like the internet.
[368.30 → 369.38] Then they go build the tool.
[369.52 → 371.78] Then they kind of like get demotivated halfway through.
[371.78 → 372.88] And then it just fizzles out.
[372.96 → 376.62] Like, I'm so impressed that people who managed to like to get to the end and actually launch
[376.62 → 376.96] something.
[377.26 → 381.62] But then I'm also amazed that people who launched something in secret, like I didn't even know
[381.62 → 382.00] about this.
[382.04 → 384.26] And Mateo, we have so many close mutual friends.
[384.48 → 387.24] And granted, like I've been living under a rock for the past few months too.
[387.34 → 391.90] But like, I'm just like, whoa, I heard about this morning from Jared, and I was like, this
[391.90 → 392.66] is hot stuff.
[392.72 → 395.90] Like, can't wait to hear about it and also catch up with Mateo.
[395.90 → 398.54] And then Luke, I had no idea that you went to Near form.
[398.68 → 399.58] I like missed that.
[399.76 → 403.56] That's so cool that you all had a little bit of overlap at Near form because Near form is
[403.56 → 407.56] a really like fascinating company for those of you who might not be familiar.
[408.18 → 413.14] Like, you know, if anyone is out there looking for like node consultants, like node contractors,
[413.38 → 416.98] like people who understand how to build node services at scale, go to Near form.
[417.18 → 419.20] Like they are deep experts in JavaScript.
[419.58 → 425.18] They're deep experts in scale and distributed systems and like how to cleanly like scale your
[425.18 → 425.56] architecture.
[425.72 → 426.96] Like they're incredible engineers.
[427.44 → 429.56] They also do a lot for the community as well.
[429.74 → 430.84] Oh, I love my previous company.
[431.06 → 431.28] Yeah.
[431.56 → 433.58] Huge open source element to their work as well.
[433.70 → 435.86] So that's kind of the roots that Mateo is coming from.
[436.02 → 438.74] And I guess it's great to hear, Luca, that you had some of that.
[438.80 → 440.88] So yeah, why don't you tell us a little bit about yourself, Luca?
[440.88 → 444.42] Yeah, I also started very early coding.
[444.90 → 449.56] I still remember the first time, but I come from a family of entrepreneurs.
[449.56 → 457.30] And so I kind of blended my passion for computers with the passion for building businesses and
[457.30 → 459.18] making impactful products.
[459.18 → 464.32] So I started when I was very young at 12 years old, and I built along the way a few companies
[464.32 → 467.28] that I was able to sell.
[467.28 → 473.76] And I went through this cycle of learning something new and applying to business.
[474.82 → 480.10] In 2014, something like that, I met Mateo or 15.
[480.18 → 483.84] I met Mateo in the backstage of Node Summit.
[485.36 → 493.82] And yeah, basically in 2016, I was in front of a big decision to switch from moving to a
[493.82 → 496.76] large company or join Near Form.
[497.32 → 503.36] And I still remember Kian in the castle in Ireland kind of like convincing me to join
[503.36 → 503.96] Near Form.
[504.10 → 509.82] And so it took just a few months and I, yeah, I joined Near Form mostly because I was excited
[509.82 → 516.24] to work with people like Mateo, other very close friend, Dave at the time, Peter.
[516.36 → 518.06] So I was very excited about all these people.
[518.18 → 519.82] And I said, wow, it's a great opportunity.
[520.38 → 523.80] So Mateo and I started travelling a little bit around the world for a couple of years.
[524.82 → 529.72] And in 2017, I moved to Canada.
[530.14 → 531.36] Well, not I moved to Canada.
[531.50 → 534.56] Sorry, I visited Canada, and then I decided to stay in Canada where I moved.
[534.70 → 537.00] You remember when we were all in Canada, Amal?
[537.12 → 538.18] Yeah, no, I was there.
[538.48 → 539.18] Yeah, I was there.
[539.28 → 541.38] Luca, then stayed there.
[541.46 → 542.46] Yeah, no, we hung out.
[542.56 → 543.60] It was a really fun time.
[543.76 → 544.30] Yeah, I was there.
[544.56 → 546.00] Yeah, we met through Ahmed.
[546.52 → 548.14] That was the common denominator.
[548.30 → 550.42] Yeah, Ahmed is one of our biggest mutuals.
[550.42 → 550.64] Yeah.
[551.02 → 551.40] Yeah.
[551.40 → 551.44] Yeah.
[551.74 → 559.56] And so basically, long story short, I moved to work again for large corps like Talos, following
[559.56 → 565.84] the path of Ahmed and then back into startups and doing some CTO work.
[566.20 → 566.64] Consultancy.
[566.90 → 567.14] Yeah.
[567.14 → 567.54] Yeah.
[567.54 → 567.66] Yeah.
[567.94 → 571.46] And so basically, it was actually natural.
[571.56 → 573.60] Mateo and I kept in touch for such a long time.
[573.68 → 577.28] We were so close, and we had been thinking about this idea for way too long.
[577.84 → 582.48] And so basically, in the beginning of the year, we kind of like gather all our thoughts
[582.48 → 582.92] together.
[583.20 → 588.94] And here we are a few months later, kind of like making off a small side project and
[588.94 → 593.02] crazy idea that we were building just in our minds.
[593.02 → 594.54] It was all in our minds.
[594.70 → 596.82] There was nothing really, you know, solid.
[597.14 → 597.26] Yeah.
[597.54 → 600.54] We talked and said, well, it could be nice one day to build a company.
[600.82 → 601.02] And then...
[601.54 → 605.08] We can call it Mozzarella.js or Pizza.js or what?
[605.18 → 605.54] I don't know.
[605.70 → 606.02] Like...
[606.02 → 606.54] Pizza.js.
[606.90 → 607.14] Okay.
[607.24 → 611.84] So honestly, though, I'm just fascinated that like you both are Italians in tech from the
[611.84 → 617.02] Node community, have both had like really prolific and very successful careers, like
[617.02 → 617.74] independently.
[617.74 → 619.56] And you're now re...
[619.56 → 622.82] Like you're forming a union around this company and this project.
[622.96 → 623.90] Like I think that's so cool.
[624.22 → 626.64] And you're like, Matteo, you're like an Italian that's still living in Italy.
[626.94 → 631.86] And then Luca is like an Italian that's like globe hopping and is currently based in Canada.
[632.04 → 633.06] Like that's so cool.
[633.86 → 634.00] Yeah.
[634.32 → 638.08] So like, can you tell us a little bit about PlatformIO?
[638.44 → 639.52] What is it?
[639.90 → 641.10] What inspired it?
[641.26 → 642.96] What problems are it uniquely solving?
[643.74 → 645.48] Like give us all the things.
[645.48 → 649.20] I've been building backend systems for all of my career.
[649.74 → 652.56] And to be honest, it has always been a more or less a disaster.
[653.08 → 656.54] It's actually very ugly building backend systems.
[656.82 → 656.98] Okay.
[657.10 → 663.38] It requires a lot of sweating, a lot of hard work, a lot of...
[663.38 → 666.54] To some extent, some sweating, because if you don't sweat, you're sweating and then
[666.54 → 670.90] you're also sweating because from time to time, the computer reacts way better if you
[670.90 → 676.24] start insulting it, insulting my computer in Italian from time, sometimes.
[676.24 → 677.88] Oh, actually.
[678.12 → 679.12] I don't know.
[679.52 → 681.42] That's probably going to get censored out, but okay.
[682.16 → 682.64] Beep.
[682.96 → 683.40] Beep.
[683.54 → 685.74] Because it's in Italian doesn't mean it's not a curse word.
[686.92 → 687.40] Right.
[687.40 → 687.76] Right.
[688.24 → 693.58] And then when I became a consultant, I helped teams deliver software and building backend
[693.58 → 694.00] systems.
[694.74 → 698.12] And I saw all the problems that they were facing.
[698.50 → 706.10] And this is what has prompted me to create Hastily and create a lot of the libraries that
[706.10 → 708.80] a lot of people now are using to build those systems.
[708.80 → 715.24] The next step for me was I started thinking, well, I can, how can I increase my impact?
[715.34 → 717.14] How can I help more people?
[717.30 → 719.12] How can I improve more?
[719.46 → 725.34] And it seemed natural to build a company around this dream.
[725.74 → 725.96] Okay.
[726.20 → 732.00] It's, it seemed the next step mainly because after being so much in consulting, I really
[732.00 → 736.86] wanted to, to build a product now and use what I've learned to build something new.
[736.86 → 745.00] So that was essentially the, the gist of why PlatformIO and, and why now, why now it's
[745.00 → 746.96] because of other things, but yeah, go for it.
[747.04 → 747.28] Yeah.
[747.74 → 748.50] No, that makes sense.
[748.58 → 750.88] So I just kind of want to share something really insightful here.
[750.88 → 756.12] Actually, one of our other mutual friends, Joey Barton is the person who I heard this from.
[756.28 → 758.16] She, her and I were having a conversation about this.
[758.56 → 760.38] So I worked at a place called Baku a long time ago.
[760.46 → 765.76] That's like this kind of famous web platform consultancy, you know, like other experts in
[765.76 → 770.02] JavaScript, but we were kind of more everything above the API more.
[770.16 → 774.46] So we did a lot of stuff full stack as well with node, but yeah, and electron.
[774.66 → 779.90] But I would say that a lot of like what Baku was famous for is like, you know, a deep expertise
[779.90 → 780.96] of like the web platform.
[780.96 → 781.24] Right.
[781.26 → 786.00] And so interesting kind of echo to near form, just like on the other side of the spectrum.
[786.00 → 786.94] And so, yeah.
[787.10 → 789.84] But anyway, so Jury was like CEO of Baku for a while.
[789.94 → 794.06] And interestingly, she kind of, her and I were talking about this, this pattern of like,
[794.12 → 798.56] once you're in consulting, a lot of consultants end up starting successful businesses after
[798.56 → 803.46] they've been in the game for a while, because they see patterns, you know, you see patterns
[803.46 → 807.52] like the same problems at different companies, just different flavours of the problem.
[807.52 → 812.14] And it's so interesting because like, I'm seeing this now, just like I'm at a point in my career
[812.14 → 818.16] where like, you know, I have enough experience where I've seen like multiple phases of web
[818.16 → 818.64] technologies.
[818.64 → 822.46] And also like I've worked at enough companies where I see every company is kind of having
[822.46 → 824.64] the same problem in a different flavour.
[824.88 → 825.32] Right.
[825.36 → 830.24] And so it's interesting to see like how your consultants see, like being a consultant in
[830.24 → 834.66] the node space and the API space for such a long time, like you were able to kind of see
[834.66 → 838.24] this, the needs and the gaps in the tooling and the process, you know?
[838.36 → 843.72] So, so how does PlatformIO like uniquely fill in the gaps in the white space that's in the
[843.72 → 844.50] community right now?
[845.18 → 846.86] Yeah, maybe I can tell you something.
[847.02 → 848.20] It's about the pattern, right?
[848.66 → 857.04] So what we, Matteo and I observed is that there was some sort of like a gap in between different
[857.04 → 859.22] kind of like successful stories on the market.
[859.22 → 866.70] And if on one side we saw the front end being enormously accelerated and commoditized and
[866.70 → 871.36] on a certain sense, you know, perfect reaction to what happened to infrastructure with the
[871.36 → 875.90] cloud and different, you know, initiatives like we all know about, for example, Terraform
[875.90 → 879.86] has been revolutionary, changing the world of infrastructure.
[879.86 → 887.90] We're exactly sitting in the middle where most of our experience in building for clients
[887.90 → 892.96] and for our own companies in, when I was, for example, at Talos, building a platform that
[892.96 → 899.36] would accelerate the day-to-day job of developers, making their life not a repetitive task, but
[899.36 → 904.52] in transforming what was seen before as a repetitive task to some sort of innovation.
[905.26 → 908.40] And for us, the most important thing was the social impact of that change.
[908.40 → 911.46] The fact that could actually catalyst new ideas, right?
[912.02 → 917.38] And so when we spoke like on the ideal world, what we were looking on the market, we were
[917.38 → 924.46] basically looking on some sort of like experience that would put building backends on some sort
[924.46 → 931.56] of rails and focus on building the best train in the world and not just the best set of rails
[931.56 → 939.12] in the world because we wanted to have, we wanted to provide to our users being first ourselves,
[939.12 → 939.38] right?
[939.38 → 945.68] The consumer, something that could, you know, facilitate and accelerate building APIs.
[945.68 → 949.30] Like for example, today we just released this first bit.
[949.30 → 954.58] How can we actually commoditize building APIs on top of databases, right?
[954.60 → 961.06] How many times I've been like going through my gist and my, you know, toolbox to look at
[961.06 → 966.00] which library should I use to connect to Postgres, and how can I actually structure that and
[966.00 → 966.90] so on and so forth, right?
[966.96 → 972.84] And transforming all this kind of repetitive tasks, not really mechanical tasks because that
[972.84 → 976.92] would still imply a lot of work, but in something that would basically be an out-of-the-box
[976.92 → 979.00] experience for people.
[979.00 → 981.16] And so we imagine this ecosystem, right?
[981.16 → 987.36] The digital platform world to be a puzzle, to be, as you can see there, I'm very passionate
[987.36 → 993.42] about Lego, and luckily you don't see that side, but I am completely like bought into the Lego
[993.42 → 994.42] mentality, right?
[994.42 → 999.04] We have all this kind of pre-made sets, but you can, fantasy is just the only limit that
[999.04 → 1000.04] you have.
[1000.04 → 1001.68] And so the same thing is for PlatformIO.
[1001.68 → 1006.88] We want to give the tools and the building blocks to build whatever people want to build
[1006.88 → 1010.30] but having the constraints of a four by two blocks, right?
[1010.34 → 1010.96] The most famous.
[1011.44 → 1013.46] Yeah, no, I think that is so cool.
[1013.56 → 1018.60] I love this, this idea of you're not interested in just building the rails because I definitely
[1018.60 → 1020.52] think you're absolutely right.
[1020.62 → 1023.46] That's kind of has been the focus for us for a long time.
[1023.52 → 1027.48] Like everyone's focused on let's build the rails, let's build the rails and everybody
[1027.48 → 1028.52] builds their own train.
[1028.62 → 1029.82] But like, guess what?
[1030.26 → 1032.84] Trains are like 95% the same.
[1033.18 → 1036.64] Like everything, you know, you need an engine, you need a core, you need a, you need seats,
[1036.64 → 1037.98] the, the, the, the, the, the, the, the, the, right?
[1038.06 → 1042.60] Like, so it's like, I love this idea of like, okay, how can we, like, what kind of innovation
[1042.60 → 1047.02] can come out of people having more time to focus on the business logic and the interesting
[1047.02 → 1049.12] parts of the of their applications, right?
[1049.14 → 1051.24] Like all this other stuff is busy work.
[1051.36 → 1053.80] And I couldn't agree with you more.
[1054.14 → 1058.74] For me, I feel like a challenge that I've hit is like in the past, and I've seen this,
[1058.78 → 1062.84] you know, at multiple places now is like this not invented here kind of syndrome that
[1062.84 → 1063.42] we have, right?
[1063.42 → 1066.74] Like engineers want to reinvent the wheel because I don't know.
[1066.86 → 1067.60] I have no idea.
[1067.80 → 1070.16] It's not a personal value of mine.
[1070.34 → 1076.70] So I have a hard time relating to folks who want to reinvent the wheel for like a 1% difference
[1076.70 → 1078.14] in API interface.
[1078.30 → 1082.06] Like, oh, they use the strings instead of integers or something.
[1082.20 → 1082.94] I have no idea.
[1083.08 → 1088.50] Like, it's like for 1% or 2% difference, you're going to reinvent the wheel completely
[1088.50 → 1090.66] because you're not happy with this thing's interface.
[1090.82 → 1091.62] Like, why?
[1091.74 → 1092.24] I don't know.
[1092.34 → 1093.48] But it's a real problem.
[1093.60 → 1098.90] Like, how do you fight that problem of people wanting to do it like their way, you know?
[1099.46 → 1099.68] Yeah.
[1099.72 → 1104.98] And there's also the, the other kind of like effect in enterprise, for example, the space
[1104.98 → 1109.76] where we kind of operated the most is that it's just that the enterprise has different
[1109.76 → 1116.62] type of needs than the startup developer, for example, or the independent developer.
[1116.62 → 1122.26] The enterprise has really the need of having this kind of like predefined also structures
[1122.26 → 1127.06] that they can work within the so-called best practices, right?
[1127.56 → 1137.02] And so we actually felt that in this, especially in the node space, Matteo extensively and myself
[1137.02 → 1143.28] too in the architecture side, we have been actually kind of like every time trying to redefine
[1143.28 → 1146.72] those best practices, bringing them from the outside to the inside.
[1147.22 → 1151.76] But with PlatformIO, we just want to standardize those best practices and say, well, we bring
[1151.76 → 1152.30] Oh, wow.
[1152.44 → 1153.36] That is so cool.
[1153.54 → 1155.22] You know, the best value of open source.
[1155.38 → 1159.66] So the best value that we are generating in this century, that is the community work,
[1159.82 → 1165.50] the collective work into a space where we actually create a harmonized way to distribute
[1165.50 → 1170.86] those best practices into some sort of like predefined starter kits, predefined libraries.
[1171.50 → 1175.78] And we give you actually kind of like the space not to start a contention or a discussion
[1175.78 → 1180.88] around the same topics, but an evolution-based discussion and say, how can you make it better?
[1181.30 → 1185.40] We give you like in music, you give the first note to set the tone.
[1185.56 → 1187.72] And the same we are giving with PlatformIO.
[1187.72 → 1193.62] We want to set the stage and say, this is how we, from our expertise and the community,
[1193.80 → 1200.86] see this particular problem being resolved and being commoditized in a set of tools.
[1201.10 → 1201.24] Yeah.
[1201.48 → 1201.64] Yeah.
[1201.70 → 1205.38] Now, if you want to contribute, it's all open.
[1205.86 → 1207.30] Please help us make it better.
[1207.54 → 1208.28] That's so cool.
[1208.34 → 1211.66] I love this bold bet of like elevating and setting standards.
[1211.66 → 1217.00] And like, that's such a Mateo thing to do, like, is to just like say, here you go.
[1217.46 → 1218.94] You know, it's done now.
[1219.06 → 1219.74] Problem solved.
[1219.86 → 1220.76] Like, bold bet.
[1220.92 → 1222.32] I can totally see that.
[1222.54 → 1224.34] And like, I'm, that's like so cool.
[1224.40 → 1226.04] But anyhow, I'm eager to hear from Chris.
[1226.52 → 1226.80] Yeah.
[1226.88 → 1230.14] So can you kind of tell us about what did you release today?
[1230.50 → 1231.92] It's called PlatformaticDB.
[1232.56 → 1233.28] What does it do?
[1233.84 → 1234.18] Okay.
[1234.34 → 1235.66] So it does a few things.
[1235.66 → 1240.32] So at the outside, what you can scratch from the reading, the getting started.
[1240.82 → 1241.14] Okay.
[1241.14 → 1250.58] It reads up your database schema, and it creates a REST API with OpenAI definition, as well
[1250.58 → 1253.76] as a GraphQL API on top of your schema.
[1254.18 → 1257.52] So that's the simple or easy part of it.
[1257.90 → 1260.18] It supports relations and a few other bits.
[1260.54 → 1262.04] It also does migrations.
[1262.54 → 1263.34] It does log.
[1263.34 → 1265.74] It does, you know, what you would expect from a demo.
[1266.22 → 1268.92] Is it like a code generator or no?
[1269.18 → 1269.58] No.
[1269.58 → 1270.38] So it just runs.
[1270.52 → 1271.56] So it is what we wanted.
[1271.70 → 1271.88] Okay.
[1272.10 → 1275.72] We believe that the best line of code is the one that you don't have to write.
[1276.18 → 1281.02] So if you need a code generator, we are essentially implying that you will need to maintain that
[1281.02 → 1281.26] code.
[1281.40 → 1283.08] We want to minimize friction.
[1283.08 → 1284.80] We want to remove the problem.
[1284.80 → 1285.16] Okay.
[1285.48 → 1286.52] Hashtag just do it.
[1286.86 → 1288.02] Hashtag it just works.
[1288.16 → 1288.50] Just do it.
[1288.50 → 1289.54] Hashtag it just works.
[1289.54 → 1290.86] Hashtag the right kind of magic.
[1291.26 → 1293.44] I'm certain things I'm okay with being magic.
[1293.70 → 1295.68] Like, you know, it's like, I don't need to see the boilerplate.
[1295.84 → 1297.80] Like, you're welcome to hide that or abstract that.
[1297.92 → 1299.04] Like, I don't need to maintain it.
[1299.10 → 1300.20] I don't need to see it either.
[1300.40 → 1301.36] Like, that's beautiful.
[1301.76 → 1302.18] Love that.
[1302.18 → 1303.76] Pretty much my take.
[1303.86 → 1308.36] Because if I needed to generate stuff, it will require even, like, I've tried different
[1308.36 → 1310.20] things of this kind.
[1310.80 → 1311.78] There is a catch, though.
[1311.88 → 1316.24] And this is why the code generators are somewhat popular in the industry.
[1316.46 → 1322.34] It's because those code generators enable people to deeply customize the behaviour that
[1322.34 → 1322.78] they need.
[1323.48 → 1325.04] And this is why they are so powerful.
[1325.40 → 1325.60] Okay.
[1325.60 → 1328.32] How do we cater for that case in PlatformIO?
[1328.46 → 1329.74] Well, in PlatformaticDB.
[1329.74 → 1336.22] What we do is we enable you to completely customize our server using Hastily plugins.
[1336.92 → 1338.86] So, I've talked about Hastily before.
[1339.02 → 1344.36] Hastily is this more or less 3 million downloads a month web framework for Node.js.
[1345.60 → 1347.20] Right now, it's probably the best.
[1347.20 → 1350.26] I'm the author, lead maintainer of that, so I can probably boast a little bit.
[1350.64 → 1354.00] It's probably the best way to write servers in Node these days.
[1354.00 → 1358.06] It has, I think, 17, 18 collaborators maintaining it now.
[1358.32 → 1363.92] Like, every single release, it has 20 different people, commits from 20 different people, 10
[1363.92 → 1366.22] of which are first-time contributors, like something like that.
[1366.48 → 1367.06] That's so cool.
[1367.12 → 1368.10] It has amazing stats.
[1368.22 → 1369.22] So, that's battle-tested.
[1369.80 → 1374.96] And you can use that battle-tested framework to actually completely customize PlatformIO
[1374.96 → 1375.14] DB.
[1375.24 → 1379.00] In fact, PlatformIO DB is just built as a set of Hastily plugins.
[1379.00 → 1384.62] So, if you want those features, and you have an existing Hastily application, you can just
[1384.62 → 1388.36] use our Hastily plugins and get the same functionality yourself.
[1388.36 → 1389.96] Without needing to...
[1389.96 → 1393.64] You can just directly jump into the advanced case.
[1393.64 → 1394.14] Okay?
[1394.14 → 1397.32] And essentially, completely write the stuff yourself.
[1397.32 → 1401.16] On top of that, it has a few more interesting things.
[1401.16 → 1402.90] It has a development environment embedded.
[1402.90 → 1407.16] It does a hot reload of Node.js modules.
[1407.16 → 1407.84] Okay?
[1407.84 → 1409.74] And yay.
[1409.74 → 1413.96] So, next, I'm hearing that I need to talk about this feature later.
[1413.96 → 1414.58] So...
[1414.58 → 1414.96] Yes!
[1414.96 → 1415.42] Yes!
[1415.42 → 1415.72] Yes!
[1415.72 → 1416.46] I'm like, Mateo!
[1416.46 → 1416.96] Mateo!
[1416.96 → 1418.80] Let's save this for the second segment.
[1418.80 → 1420.24] I want to dig into all this and more.
[1420.24 → 1420.30] Okay.
[1420.30 → 1421.72] This is so cool, though.
[1421.72 → 1422.22] Oh my god.
[1422.22 → 1422.60] Oh my god.
[1422.60 → 1422.86] All right.
[1422.86 → 1424.10] So, I'm gonna just like...
[1424.10 → 1426.68] I need a minute to even just like to contain my excitement.
[1426.68 → 1428.68] But we will be right back, you all.
[1428.68 → 1429.18] Bye.
[1448.92 → 1451.70] This episode is brought to you by Sentry.
[1451.70 → 1453.54] Build better software faster.
[1454.04 → 1457.68] Diagnose, fix, and optimize the performance of your code.
[1457.68 → 1464.80] More than a million developers and 68,000 organizations already use Sentry, and that includes us.
[1464.80 → 1466.64] Here's the easiest way to try Sentry.
[1466.64 → 1469.92] Head to Sentry.io slash demo slash sandbox.
[1470.38 → 1474.26] That is a fully functional version of Sentry that you can poke at.
[1474.62 → 1477.38] And best of all, our listeners get the team plan for free for three months.
[1477.66 → 1481.26] Head to Sentry.io and use the code SHIP IT when you sign up again.
[1481.70 → 1484.12] Sentry.io and use the code SHIP IT.
[1487.68 → 1499.66] Okay, everyone.
[1500.00 → 1502.80] So, had a minute to kind of freak out offline.
[1503.12 → 1505.24] So, we're back and this is amazing.
[1505.46 → 1507.64] So, Mateo, I'm eager to hear about all of this.
[1507.64 → 1516.58] And I love this concept of, like, boilerplate is popular because boilerplate lets you take the custom code, which is the hot path for most people.
[1516.68 → 1520.36] But then it lets you edit that code to, like, customize it and whatever.
[1520.36 → 1533.24] And you're like, okay, well, how about we use a plugin architecture so that we can actually abstract away that boilerplate hot path, but then enable that extensibility through a clean kind of plugin interface.
[1533.24 → 1535.90] Like, that is freaking genius.
[1535.90 → 1542.64] But in many ways, it's also kind of the core principle and architecture behind Hastily, which is what we talked about last time you were on the show.
[1542.70 → 1543.96] We had a show on Hastily and Pinot.
[1544.06 → 1545.02] Totally awesome.
[1545.20 → 1545.68] Worth a listen.
[1545.78 → 1547.32] We'll link it in the show notes.
[1547.70 → 1547.98] But, yeah.
[1548.04 → 1551.12] Can you kind of just jump back in there and talk us through that?
[1551.12 → 1557.76] So, the plugin architectures enable us to cater for the complex part of your application.
[1557.76 → 1567.86] So, you can write your custom business logic, your custom routes, add your custom resolvers, or even, I don't know, would you want to add Next.js into the system?
[1567.98 → 1568.56] Yeah, you can.
[1568.86 → 1571.52] Throw the Hastily Next.js plugin and it will work.
[1572.10 → 1572.36] Okay.
[1572.36 → 1578.78] So, the idea is that you can completely customize how the daemon is, how that server is running.
[1579.18 → 1585.34] As I said, it also provides some level of developer experience, dash, live reload on it.
[1585.48 → 1593.50] So, you can just edit your files, and it will automatically reload them and run them inside and load them as Hastily plugins.
[1593.96 → 1595.20] It's actually pretty neat.
[1595.38 → 1598.78] This is a problem that some of you have been in the Node community.
[1598.78 → 1604.72] It's actually a hard problem because I also support ESM and, you know, this is tough, and I'm so sorry.
[1604.72 → 1610.60] Now, I think Chris' face is a little bit skeptical on how that would work, but it actually does.
[1610.80 → 1611.38] Oh my god.
[1611.38 → 1614.30] Did you say sane ESM experiences in Node?
[1614.30 → 1615.10] Oh my god.
[1615.10 → 1616.18] Yeah, seamless.
[1616.36 → 1617.50] That's a heavy promise.
[1618.46 → 1619.58] It's completely seamless.
[1619.58 → 1622.52] You just load it up and it will adjust.
[1622.92 → 1626.78] How about if I add different packages from different NPM libs?
[1626.78 → 1627.78] It's fine.
[1627.78 → 1630.26] That are like in different module formats.
[1630.26 → 1630.90] It's fine.
[1630.90 → 1632.02] All good and supported?
[1632.02 → 1633.62] Yeah, because it just uses Node.
[1633.62 → 1634.42] Oh, okay.
[1634.42 → 1639.70] So, you have all the same rules for Node, but what we do is that we have hot reloading of all of this.
[1640.26 → 1645.62] So, even if some dependency changes and stuff, it gets hot reloaded in code.
[1645.62 → 1646.90] V8 isolates.
[1646.90 → 1650.42] So, there is a little bit of C++ in there stuff.
[1650.42 → 1651.62] Really fun stuff.
[1651.62 → 1660.66] And I need to, by the way, I did not invent most of this stuff or most of the key fundamental, the stepping stone, if you want to.
[1660.66 → 1666.50] What that gives me the inspiration for this feature comes from Anna Ensign, Ada lex on Twitter.
[1666.50 → 1671.38] She wrote this module called Synchronous Worker that does the…
[1671.38 → 1673.14] Did you say Anna?
[1673.14 → 1673.94] Anna.
[1673.94 → 1674.50] Yeah, Anna.
[1674.50 → 1676.58] Oh my god, I love Anna so much.
[1676.58 → 1677.14] Ah, yeah.
[1677.14 → 1677.94] I mean…
[1677.94 → 1679.86] She's so humble.
[1680.58 → 1682.42] She's so incredibly humble.
[1682.42 → 1684.74] No, I've been trying to get her to kind of come on the show for a while.
[1684.74 → 1685.70] I have to go…
[1685.70 → 1686.82] Yeah, yeah, I'll go insist.
[1686.82 → 1687.30] She's amazing.
[1687.30 → 1688.82] She's brilliant, yeah.
[1688.82 → 1690.10] I love you, Anna, if you're listening.
[1690.66 → 1691.54] Yay.
[1691.54 → 1700.10] And basically, this module enables you to create a full worker, like worker thread, completely isolated from the rest of the Node.js,
[1700.10 → 1706.10] or your main Node.js execution, but on the same thread and on the same event loop.
[1706.10 → 1709.62] Wait, so is it different execution contexts that are sharing…
[1709.62 → 1710.82] The same event loop.
[1710.82 → 1713.70] The same event loop, like that's black magic right there.
[1713.70 → 1714.42] Pretty much.
[1714.42 → 1715.94] So is this leveraging V8's…
[1715.94 → 1716.34] Isolate.
[1716.34 → 1717.22] …isolate technology?
[1717.22 → 1717.54] Yeah.
[1717.54 → 1718.42] Okay, okay.
[1718.42 → 1718.66] Yeah.
[1718.66 → 1721.30] So interesting, that is some really black magic.
[1721.30 → 1722.66] I didn't even know that was a thing.
[1722.66 → 1726.42] Are they using this for Atomics, to support Atomics in the browser as well?
[1726.42 → 1729.22] Like how, or is this just a Node thing?
[1729.22 → 1735.94] This is just V8, it's just V8 isolates, it's just more or less the bits that you can already do.
[1736.10 → 1741.30] It's how Cloudflare workers are implementing certain things and so on and so forth.
[1741.30 → 1741.94] I see.
[1741.94 → 1744.98] What are the chances of something like that getting into Node Core?
[1744.98 → 1746.42] Oh, that's my next step.
[1746.42 → 1746.98] Yeah.
[1746.98 → 1751.54] All of this is open and Anna did the first implementation.
[1751.54 → 1757.14] I had to fork the module because I needed some modifications for my stuff to get through,
[1757.14 → 1763.06] but I would really love to get into Node Core because it's so powerful that it will be…
[1763.06 → 1768.10] Like right now, in order to run Automatic DB, it basically says if you don't have a compiler
[1768.10 → 1773.46] certain features available for compiling this little bit of glue, C++ glue to make everything work,
[1774.02 → 1781.78] we need to… we run with a polyfill that does some of it, but does the best that you can do with
[1781.78 → 1782.66] the tool at hand.
[1782.66 → 1786.18] Okay, but the full experience is amazing.
[1786.18 → 1791.78] You get to figure out a few hard crashes, which are a lot of fun when your system has a very bad
[1791.78 → 1793.62] crash in the sense of…
[1793.62 → 1794.58] That sounds cool.
[1794.58 → 1795.78] …the V8 crash.
[1795.78 → 1798.34] Okay, like not another V8 crash.
[1799.22 → 1800.42] It's fun to debug.
[1800.42 → 1803.30] So, no, that was very, very interesting.
[1803.30 → 1807.62] It provides the core of the development experience for writing plugins so that you have…
[1807.62 → 1814.34] Imagine Node-Mon, but instantaneous. I had to actually… it was so fast that I had to introduce a timeout
[1814.34 → 1820.26] because… yeah, it's… I had to introduce a 100 millisecond timeout because it was too fast.
[1820.26 → 1825.14] Oh my god. And you're a fast typer, you're saying that. So it's like, oh my god, I can only imagine.
[1825.14 → 1826.82] Yeah, that's awesome.
[1826.82 → 1829.62] Something like that seems like it could even fix Jest.
[1829.62 → 1831.38] Actually, yes!
[1831.38 → 1834.90] And this is not a miracle worker, okay, Chris Miller? Like, this is like…
[1834.90 → 1837.46] You're asking for too much now. Don't tempt the gods.
[1837.46 → 1838.58] I'm serious. Okay.
[1838.58 → 1839.14] I'm serious.
[1839.14 → 1840.74] I know, I think you're right. Yeah.
[1840.74 → 1843.86] Jeff's done also all the TypeScript memory leaks.
[1843.86 → 1844.34] Like…
[1844.34 → 1844.90] Oh…
[1844.90 → 1847.86] Yeah, I will tell you about that.
[1847.86 → 1850.02] That TypeScript is on the path.
[1850.02 → 1853.38] Oh yeah, yeah. Let's talk about that. I wish Nick Nisi was on the show.
[1853.38 → 1856.82] He'd just like perk right up right now. Did somebody say TypeScript, you know?
[1856.82 → 1857.38] TypeScript.
[1857.38 → 1863.78] I'm like… I'm not on the fence about TypeScript. I totally get it. Furthermore, I see the benefits and all of that.
[1863.78 → 1867.46] I'm just… Like I said, I'm more like pragmatic TypeScript.
[1867.46 → 1869.62] Like, I'm not spending a ton of time on generics.
[1869.62 → 1874.26] I'm not going to spend a ton of time fighting TypeScript for use cases that are like inner,
[1874.26 → 1876.50] inner, inner, inner, inner, inner deep interfaces.
[1876.50 → 1880.50] Like, you know, I focus more on my public interfaces and places where it's touchpoints,
[1880.50 → 1881.14] you know?
[1881.14 → 1883.46] So anyway, I'm team pragmatic TypeScript.
[1883.46 → 1885.54] But anyway, I'm targeting.
[1885.54 → 1890.90] So Luca, I'm curious, like, before we get more into like the specifics of the functionality here,
[1890.90 → 1897.78] like what's your role versus Matteo's role? Like, are you like CEO, CTO? Are you like co-CT? Like,
[1897.78 → 1901.30] what's the like… What's the dynamic here between the two of you?
[1901.30 → 1911.06] Yeah, the dynamic is I'm CEO and try to do the all Excel and more legal side.
[1911.06 → 1912.02] All the PowerPoints.
[1912.02 → 1915.14] Well, Matteo helps and leads the technology.
[1915.14 → 1916.58] So you're building the business basically.
[1916.58 → 1916.66] Yeah.
[1916.66 → 1919.54] Basically. And he's focusing on the tech. It's a good partnership.
[1919.54 → 1920.10] Yeah.
[1920.10 → 1924.26] We both kind of like design the product and design the different features.
[1924.26 → 1924.98] Mm-hmm.
[1924.98 → 1930.10] Is like I said, the product itself came out from experience that we shared together.
[1930.10 → 1930.74] Mm-hmm.
[1930.74 → 1935.86] And, you know, sharing architecture and ideas around that.
[1935.86 → 1939.06] So the product is kind of like, you know, very organically designed.
[1939.06 → 1939.62] Mm-hmm.
[1939.62 → 1946.10] But that's how kind of like we split them more focusing on getting the engine to always have oil
[1946.10 → 1948.50] in and smoothly work and operate.
[1948.50 → 1949.62] Yeah, yeah, yeah, yeah.
[1949.62 → 1950.18] Yeah.
[1950.18 → 1951.14] No, that's so cool.
[1951.14 → 1952.90] Okay. We'll have to talk about the business later.
[1952.90 → 1954.74] So back to the tech now.
[1954.74 → 1956.98] So Matteo, what else can this thing do?
[1956.98 → 1964.18] So we have crazy awesome hot module reloading that's like instantaneous basically, which is
[1964.18 → 1964.74] incredible.
[1964.74 → 1969.06] That's leveraging like under the hood black magic via V8.
[1969.06 → 1970.02] Pretty much.
[1970.02 → 1971.38] If it doesn't crash, pretty much.
[1971.38 → 1972.42] It seems stable.
[1972.42 → 1972.50] Yeah.
[1972.50 → 1973.54] We tried it heavily.
[1973.54 → 1974.18] It seems stable.
[1974.18 → 1976.42] Is that like an experimental feature for now?
[1976.42 → 1977.46] Is it like labelled as like...
[1977.46 → 1978.10] I would say...
[1978.66 → 1980.90] Well, it's the wall of PlatformaticDB.
[1980.90 → 1982.66] I would call it experimental.
[1982.66 → 1983.30] Okay.
[1983.30 → 1986.34] I just marked 0.1.0.
[1986.34 → 1990.82] So just to be clear, it's the first time this is seeing the light.
[1990.82 → 1995.78] We have been using ourselves in production for some of the commercial part of the business,
[1995.78 → 1999.22] which we are developing, which Luca is the person leading all of that.
[1999.22 → 1999.62] Okay.
[1999.62 → 2004.58] But right now, it's essentially the first time that we are exposing it to the wide world.
[2004.58 → 2006.98] So I expect a lot of bugs.
[2006.98 → 2007.78] Yeah, yeah, yeah.
[2007.78 → 2009.30] So it's still not V1, right?
[2009.30 → 2009.86] We haven't hit.
[2009.86 → 2011.14] No, it's...
[2011.14 → 2016.26] I would say it needs a little bit of seasoning to get to a V1 type of...
[2016.26 → 2017.22] Yeah.
[2017.22 → 2017.78] Or...
[2017.78 → 2018.42] Really.
[2018.42 → 2020.50] ...general availability type of thing.
[2020.50 → 2020.58] Right.
[2020.58 → 2023.22] It's more of, oh, we've built this.
[2023.22 → 2026.34] We would like some feedback, and we are looking for early users...
[2026.34 → 2026.82] Okay.
[2026.82 → 2029.62] ...to help us out in debugging and making sure this is great.
[2029.62 → 2030.42] Okay.
[2030.42 → 2037.30] So we have this PlatformaticDB and there's an SDK on top of it that helps you manage your routes
[2037.30 → 2039.22] and requests and whatever else.
[2039.22 → 2042.74] And so what else can this thing do besides having a great developer experience?
[2042.74 → 2045.30] PlatformaticDB is the SDK to some extent.
[2045.30 → 2045.78] Okay.
[2045.78 → 2048.26] You use it with your SQL database.
[2048.26 → 2050.26] So you can use it with SQLite.
[2050.26 → 2052.58] You can use it with Postgres.
[2052.58 → 2055.06] You can use it with MariaDB.
[2055.06 → 2056.02] You can use it with MySQL.
[2056.02 → 2056.82] Cassandra.
[2056.82 → 2057.38] Cassandra?
[2057.38 → 2057.94] Cassandra.
[2057.94 → 2060.58] You can't use it with Cassandra, unfortunately.
[2060.58 → 2062.50] Ah, I found a hole.
[2062.50 → 2063.22] Yet.
[2063.22 → 2064.26] Filing a bug.
[2064.26 → 2065.46] Filing GitHub issue right now.
[2065.46 → 2066.10] No, I'm just kidding.
[2066.10 → 2067.14] Ah.
[2067.14 → 2071.62] So we focused on SQL at the beginning for two reasons.
[2071.62 → 2074.82] And I want to reconnect a little bit of what we talked about before.
[2074.82 → 2075.62] Okay.
[2075.62 → 2081.22] Part of our challenge and what we want to solve is to empower developers in building backends.
[2081.22 → 2084.34] And this is essentially our core.
[2084.34 → 2089.78] And in fact, we see there is a huge amount of material out there right now on how to use
[2090.34 → 2091.38] SQL databases.
[2091.38 → 2092.50] How to use MySQL.
[2092.50 → 2094.02] How to use Postgres.
[2094.02 → 2095.06] How to use SQLite.
[2095.06 → 2097.22] There is massive amount of material.
[2097.22 → 2098.02] Okay.
[2098.02 → 2104.26] Like 40 years worth, 40, 50 years worth of material on how to build SQL databases.
[2104.26 → 2104.58] Okay.
[2104.58 → 2106.10] This is taught in every course.
[2106.10 → 2106.98] SQL.
[2106.98 → 2107.06] Yeah.
[2107.06 → 2108.50] It's not the problem.
[2108.50 → 2110.26] It's taught in all possible courses.
[2111.06 → 2115.70] And using SQL as the base, it's kind of the reason.
[2115.70 → 2119.30] So like one of the fundamental reasons, because most of the developers will know this stuff.
[2119.30 → 2120.02] Okay.
[2120.02 → 2122.58] So they know that they can use the database.
[2122.58 → 2129.46] And it's to some extent, it's a little bit better from my point of view or my use case of just
[2129.46 → 2132.58] using ORM on top of your custom code.
[2132.58 → 2138.10] Because if you use an ORM, you have the problem of, you know, you're always passing through the ORM
[2138.10 → 2139.38] interface, right?
[2139.38 → 2144.98] While when you start developing stuff straight on top of the database by using plugins,
[2144.98 → 2146.58] you can actually write raw SQL.
[2146.58 → 2148.50] And that's what we recommend using.
[2148.50 → 2154.34] In fact, internally, we use another project from another phenomenal developers that you should probably
[2154.34 → 2156.50] invite here.
[2156.50 → 2158.66] It's called at databases.
[2158.66 → 2161.14] And it's from Forbes list day.
[2161.14 → 2164.18] At databases, like ampersand databases.
[2164.18 → 2166.18] Is that like a Twitter handle or what is that?
[2166.18 → 2166.74] Yeah.
[2166.74 → 2166.98] Yeah.
[2166.98 → 2167.06] Yeah.
[2167.06 → 2168.58] I'm posting a couple of links now.
[2168.58 → 2169.30] So.
[2169.30 → 2169.70] Okay.
[2169.70 → 2170.74] You don't have to do it live.
[2170.74 → 2172.82] We can do it later.
[2172.82 → 2173.46] Yeah.
[2173.46 → 2175.22] But you know, you see, I am.
[2175.22 → 2176.98] Thank you for sharing them.
[2176.98 → 2177.94] Here is the link.
[2177.94 → 2178.74] Okay.
[2178.74 → 2179.54] It's amazing.
[2179.54 → 2179.78] Okay.
[2179.78 → 2181.70] It's an amazing library by Forbes.
[2181.70 → 2184.18] It is a one and a...
[2184.18 → 2188.66] Another of the old Node.js people type of...
[2188.66 → 2189.78] Did you say Forbes?
[2189.78 → 2191.22] Forbes list day.
[2191.22 → 2192.74] Forbes or Forbes Lindsay.
[2192.74 → 2193.30] Okay.
[2193.30 → 2195.38] I thought you meant, um, Forbes like...
[2195.38 → 2196.34] Nah, not the big one.
[2196.34 → 2197.46] Well, it's called the same.
[2197.46 → 2200.66] I was like Forbes like the business magazine.
[2200.66 → 2201.62] What do they know about?
[2201.62 → 2202.10] No.
[2202.10 → 2202.90] Nope.
[2202.90 → 2203.30] Okay.
[2203.30 → 2203.70] Got it.
[2203.70 → 2204.66] The person.
[2204.66 → 2205.06] Nope.
[2205.06 → 2206.26] It's Forbes Lindsay.
[2206.90 → 2214.02] He is one of the most, uh, it's a very old Node.js author.
[2214.18 → 2215.78] NPM author out there.
[2215.78 → 2217.06] And it's a great project.
[2217.06 → 2217.62] Mm-hmm.
[2217.62 → 2221.22] And it supports all the database that I mentioned and more.
[2221.22 → 2221.78] Nice.
[2221.78 → 2222.26] Yeah.
[2222.26 → 2224.18] At databases.org.
[2224.18 → 2226.18] At like AT databases.org.
[2226.18 → 2228.26] And then we'll put a show link in our notes as well.
[2228.26 → 2234.74] So in this way, you can use your own SQL queries to build your own and all the top features of your databases.
[2234.74 → 2242.58] If you are building just ORM, okay, you are not, you know, if you're using ORM, you're stuck to what the Arms provide you.
[2242.58 → 2244.58] I am team no ORM.
[2244.58 → 2245.06] I'm sorry.
[2245.06 → 2247.54] I think it is a really not worthwhile abstraction.
[2247.54 → 2248.90] I'm so sorry to say that.
[2248.90 → 2249.30] Like...
[2249.30 → 2249.78] Pretty much.
[2249.78 → 2252.02] It's like more headache than not.
[2252.02 → 2255.94] And then what happens is the ORM stops getting maintained sometimes.
[2255.94 → 2258.10] And then, oh, everyone's like, oh, darn it.
[2258.10 → 2260.58] This is end of life for this thing is in a year and a half.
[2260.58 → 2261.62] What are we going to do?
[2261.62 → 2262.74] Like, come on.
[2262.74 → 2265.22] Like, no, it's like not even worth it.
[2265.22 → 2267.70] It's like your database is your gold.
[2267.70 → 2274.26] Like, why put something between you and the DB that is like crap and buggy and whatever and slow?
[2274.26 → 2275.46] Pretty much.
[2275.46 → 2280.42] If I need to write code, okay, I want just to write, I want to talk to my database directly.
[2280.42 → 2281.22] Yeah.
[2281.22 → 2286.02] And that's the gist of the reason why we are using this tool and not other stuff that
[2286.02 → 2287.86] mediate between us and the database.
[2287.86 → 2288.58] Yeah.
[2288.58 → 2292.50] It was a pretty good journey about this.
[2292.50 → 2299.06] And we hope to help all those developers that are coming up from boot camps, or they are juniors
[2299.06 → 2301.38] at the university and so on and so forth.
[2301.38 → 2301.70] Yeah.
[2301.70 → 2304.50] So that they can be productive immediately.
[2304.50 → 2305.30] Essentially.
[2305.30 → 2306.42] Learn it the right way.
[2306.42 → 2310.34] And like, it's also SQL is one of those things where it's like, learn once, write everywhere,
[2310.34 → 2311.22] use all the time.
[2311.22 → 2313.46] It's like Git and like bash.
[2313.46 → 2317.54] You just have to bite the bullet once, and you're going to use it for the rest of your career.
[2317.54 → 2317.86] Like...
[2317.86 → 2318.42] Like VAM.
[2318.42 → 2319.38] Is this a new library?
[2319.38 → 2320.50] How do I not know about this?
[2320.50 → 2322.34] It's a new library.
[2322.34 → 2324.26] I've been living under a rock, clearly.
[2324.26 → 2325.06] I don't know.
[2325.06 → 2325.62] Yeah.
[2325.62 → 2327.38] It's been around for quite some time now.
[2327.38 → 2327.70] Yeah.
[2327.70 → 2329.06] This is the first time I've heard about it.
[2329.06 → 2333.22] And I think for me, what's exciting is like a few years ago was in that situation where like,
[2333.22 → 2338.90] yeah, some popular Postgres ORM was like going out of style and was heading end of life.
[2338.90 → 2340.66] And then like the whole company was freaking out.
[2340.66 → 2340.98] Right.
[2340.98 → 2343.30] Like, so yeah, good to know.
[2343.30 → 2345.70] But anywho, so back to PlatformIO.
[2345.70 → 2351.78] So you have a same DB line of communication, no RRM.
[2351.78 → 2355.22] So it's fast and will scale for many use cases.
[2355.22 → 2356.02] So what else?
[2356.02 → 2360.82] Like what else is in the what else is in the oven here that we're getting with this first release?
[2360.82 → 2361.54] And what's coming?
[2361.54 → 2362.50] What's coming soon?
[2362.50 → 2363.54] What's new?
[2363.54 → 2364.74] So what's coming?
[2364.74 → 2366.42] I believe it's coming to Luca.
[2366.42 → 2366.74] Okay.
[2367.30 → 2368.58] What we didn't talk yet.
[2369.14 → 2373.14] It's the basic authorization capabilities.
[2373.14 → 2380.82] So essentially you can integrate PlatformIO DB with your JWT authentication server, for example.
[2380.82 → 2388.34] So if you're using out zero or analog, you could just send the tokens to PlatformIO DB
[2388.34 → 2394.74] and implement very basic role-based authorization, actual role-based access control.
[2394.74 → 2395.38] Oh, nice.
[2395.38 → 2398.66] That's another big one that's usually like tricky and most people get.
[2398.66 → 2399.22] Yeah.
[2399.22 → 2400.02] Oh my God.
[2400.02 → 2400.74] Pretty much.
[2400.74 → 2401.70] What is up with that?
[2401.70 → 2403.70] Oh, everybody messes this up.
[2403.70 → 2404.82] It's so like.
[2404.82 → 2406.18] Oh, it's everywhere.
[2406.18 → 2407.46] Everybody messes this up.
[2407.46 → 2408.66] It's like, yeah.
[2408.66 → 2409.46] Geez.
[2410.10 → 2415.30] In the UI and in the API, like both implementations are always messed up.
[2415.30 → 2417.06] We are not talking about the UI.
[2417.06 → 2417.38] Okay.
[2417.38 → 2417.54] Yeah.
[2417.54 → 2417.78] Yeah.
[2417.78 → 2418.10] I know.
[2418.10 → 2423.38] I am as bad as a front end developer dash designer that you can probably get.
[2423.94 → 2428.90] So, you know, I was fighting last night in order to get the website app out and says,
[2428.90 → 2433.70] I literally Googled up, how do I add the HTML element?
[2433.70 → 2435.46] Oh, that's so hilarious.
[2435.46 → 2436.10] Actually, you know what?
[2436.10 → 2438.10] I saw you use Thesaurus.
[2438.10 → 2438.90] That is so cool.
[2438.90 → 2440.34] Isn't Thesaurus amazing?
[2440.34 → 2441.54] Yeah, it is.
[2441.54 → 2442.90] We can have them on the show sometime.
[2442.90 → 2443.70] Yeah.
[2443.70 → 2447.54] These latest release, they've done these two.0 release.
[2447.54 → 2449.94] These two.0 release is actually amazing.
[2449.94 → 2454.34] It overcomes all the previous bits that I didn't like about Thesaurus.
[2454.34 → 2458.50] So, there were quite a few parts of the workflow that were not great before.
[2458.50 → 2466.10] And this two.0 release, they actually cracked a very hard problem, which is the multi-version
[2466.10 → 2467.14] setup.
[2467.14 → 2471.54] And we did a very interesting integration with GitHub Actions.
[2471.54 → 2472.02] Oh, interesting.
[2472.02 → 2480.02] So that whenever we do a release on the main project, it gets its documentation are lifted from there,
[2480.02 → 2485.22] copied into the Thesaurus website and committed by itself.
[2485.22 → 2486.90] So, all of these happens behind the scenes.
[2486.90 → 2487.54] Very cool.
[2487.54 → 2494.90] And so, it's frozen, and we don't need to maintain multiple versions on the docs on the current tree.
[2494.90 → 2496.90] Because that's a problem for a role.
[2496.90 → 2497.86] That's revolutionary.
[2499.54 → 2501.62] It enables this kind of workflow.
[2501.62 → 2503.54] Yeah, that's so cool.
[2503.54 → 2505.70] And I'm very happy about the setup.
[2505.70 → 2507.94] The build is not fast, but we'll get there.
[2507.94 → 2508.50] Yeah, yeah.
[2508.50 → 2508.90] No, yeah.
[2508.90 → 2509.62] You can't have it all.
[2509.62 → 2510.34] We can't have it all.
[2510.34 → 2512.50] But anyway, so that sounds really exciting.
[2512.50 → 2517.30] So, you've solved the role-based access, permission-based access problem.
[2518.02 → 2522.02] You've built in some good conventions and standards and good rails there.
[2522.34 → 2523.06] That's exciting.
[2523.62 → 2526.90] And so, there's just so much to dig into.
[2527.38 → 2528.82] I'm eager to hear about what's next.
[2529.14 → 2530.90] I'm eager to hear about the business plan.
[2530.90 → 2533.46] I'm eager to hear about what's your plan to make money.
[2533.46 → 2534.18] How are we making it?
[2534.18 → 2534.82] It's all Luca.
[2534.82 → 2541.94] You see, I have been so entrenched in shipping this that I completely, more or less,
[2541.94 → 2546.10] got into my hole and coded on my keyboard.
[2546.10 → 2546.90] A couple of things.
[2546.90 → 2547.86] So, what's next?
[2547.86 → 2550.34] Next week, we are going to Node Cone.
[2550.34 → 2551.06] Or this week.
[2551.06 → 2552.02] I don't know when this is.
[2552.02 → 2553.22] You are listening to this?
[2553.22 → 2553.46] Yeah.
[2553.46 → 2555.46] Well, the show's dropping next week.
[2555.46 → 2556.02] Yes.
[2556.02 → 2557.22] So, this week.
[2557.22 → 2559.70] So, this week on Sunday, we are heading to...
[2561.70 → 2562.18] Like this.
[2562.18 → 2565.86] I've been in so many shows lately where there's some time warp.
[2565.86 → 2567.14] We are a time warp.
[2567.14 → 2567.70] Yeah.
[2567.70 → 2571.78] So, this week on Sunday, in a few days from when
[2571.78 → 2572.82] this show drops.
[2572.82 → 2578.90] On Sunday, in a few days, we will add to Kilkenny for Node Cone.U.
[2578.90 → 2584.50] And at Node Cone.U, we will be doing a workshop on PlatformaticDB.
[2584.50 → 2586.66] Ooh, fancy.
[2586.66 → 2590.74] So, essentially, we will be there promoting this.
[2590.74 → 2597.78] Then we will be around talking about PlatformIO in November in London.
[2597.78 → 2599.62] Wearing t-shirts, giving away stickers.
[2599.62 → 2600.66] Giving away t-shirts.
[2600.66 → 2602.26] You see, we have t-shirts.
[2602.26 → 2603.70] You see, that's the important part.
[2603.70 → 2604.66] We have t-shirts.
[2604.66 → 2605.54] We have stickers.
[2605.54 → 2606.26] I have stickers.
[2606.26 → 2607.14] You see, I have stickers.
[2607.14 → 2607.54] Yeah.
[2607.54 → 2609.14] I also have some nice swag.
[2609.14 → 2613.46] The priorities are all correct for PlatformaticDB, honestly.
[2614.02 → 2614.42] Like, yeah.
[2614.42 → 2617.22] Who needs API features when you have cool stickers?
[2617.22 → 2617.70] Yeah.
[2617.70 → 2620.34] But anyway, so we're going to get into all this stuff and more.
[2620.34 → 2626.82] The business, the open sourcing strategy, roadmap of what's next, all that in our last segment.
[2626.82 → 2641.86] So, we'll be right back, you all.
[2641.86 → 2644.50] We'll be right back.
[2644.50 → 2647.46] This episode is brought to you by our friends at Fly.
[2647.46 → 2652.34] Fly lets you deploy full-stack apps and databases close to your users, and they make it too easy.
[2652.34 → 2653.78] No ops are required.
[2653.78 → 2658.74] And I'm here with Chris McCord, the creator of Phoenix Framework for Elixir and staff engineer at Fly.
[2658.74 → 2663.54] Chris, I know you've been working hard for many years to remove the complexity of running full-stack apps in production.
[2663.54 → 2667.86] So, now that you're at Fly, solving these problems at scale, what's the challenge you're facing?
[2667.86 → 2673.06] One of the challenges we've had at Fly is getting people to really understand the benefits of running close to a user.
[2673.06 → 2677.94] Because I think, as developers, we internalize, as a CDN, people get it.
[2677.94 → 2681.14] They're like, oh yeah, you want to put your JavaScript close to a user and your CSS.
[2681.14 → 2685.30] But then for some reason, we have this mental block when it comes to our applications.
[2685.30 → 2689.54] And I don't know why that is. And getting people past that block is really important because
[2689.54 → 2694.18] a lot of us are privileged that we live in North America, and we deploy 50 miles a second and hop away.
[2694.18 → 2700.34] So things go fast. Like when GitHub, maybe they're deploying regionally now, but for the first 12 years
[2700.34 → 2705.30] of their existence, GitHub worked great if you lived in North America. If you lived in Europe or anywhere
[2705.30 → 2708.82] else in the world, you had to hop over the ocean, and it was actually a pretty slow experience.
[2708.82 → 2714.34] So one of the things with Fly is it runs your app code close to users. So it's the same mental model of like,
[2714.34 → 2718.42] hey, it's really important to put our images and our CSS close to users. But like, what if your app
[2718.42 → 2722.74] could run there as well? API requests could be superfast. What if your data was replicated there?
[2722.74 → 2727.62] Database requests could be superfast. So I think the challenge for Fly is to get people to understand
[2727.62 → 2732.26] that the CDN model maps exactly to your application code. And it's even more important for your app to
[2732.26 → 2737.22] be running close to a user because it's not just requesting a file. It's like your data and saving
[2737.22 → 2741.62] data to disk, batching data for disk, that all needs to live close to the user for the same reason that your
[2741.62 → 2745.70] JavaScript assets should be close to a user. Very cool. Thank you, Chris. So if you understand why
[2745.70 → 2749.54] you CDN your CSS and your JavaScript, then you understand why you should do the same for your full
[2749.54 → 2754.98] stack app code. And Fly makes it too easy to launch most apps in about three minutes. Try it free today at
[2754.98 → 2770.90] fly.io. Again, fly.io.
[2770.90 → 2784.58] Luka, so can you tell us more about PlatformIO, the business? What's coming next? How do you plan to
[2784.58 → 2790.98] actually make money? Yeah, well, we're not going to like in every good Michelin star restaurant,
[2790.98 → 2796.82] we give you a little bit of... We're not going to spill our secrets, secret sauce. The play thing
[2796.82 → 2804.02] and make you a little bit more hungry. But we are actually going to progress into a broader kind of
[2804.02 → 2813.30] vision and product. Our first step is to work towards our cloud proposition, which is not like
[2813.30 → 2820.66] yet another AWS. We just want to actually provide a simple way and easy way for developers to kind of
[2820.66 → 2828.26] like test outside their own machine what they're building. And from there, we actually imagine that
[2828.26 → 2835.14] that journey shouldn't stop. Developers should be able to have a first entry to the open world,
[2835.14 → 2841.38] where they can test their API, then a way to scale it, and a way to integrate within their own
[2841.38 → 2847.94] organization. Because we imagine that the journey is a multistep journey, right? A crawl, walk, run approach.
[2847.94 → 2851.94] We try to reverse it. We try to let them run as fast as they can, then walk and slow down
[2852.58 → 2858.10] into the crawling when, you know, we touch compliancy and other kind of enterprise level
[2858.10 → 2863.86] requirements. But our progression in terms of the overall strategy is going to be around our...
[2863.86 → 2869.46] We'll host your s*** basically, right? To sum it up. We host your s***. We will host your s***.
[2869.46 → 2876.34] Yeah, okay. Not quite exactly that, but like, yes. Yeah. In summary. Yeah. That's like the for sale strategy,
[2876.34 → 2882.10] right? Is like open source the core. Correct. And we'll give you a bunch of really awesome,
[2882.10 → 2885.86] even better developer experiences in cloud integrations with your deployment pipeline.
[2885.86 → 2890.50] Correct. Like very strategic and solid strategy, dude. Like high five from me.
[2890.50 → 2894.50] Yeah. Until you land into the enterprise proposition, which is...
[2894.50 → 2898.58] No, Miguel. Enterprise is hard to please though. Enterprise, they always want bespoke solutions.
[2898.58 → 2902.02] Correct. Like it doesn't matter. They are always like, no, our problems are different,
[2902.02 → 2905.62] we swear, but they're actually not. They are actually all the same.
[2905.62 → 2909.06] They're all the same, you know? I swear to God, it's the worst. And I think what's interesting
[2909.06 → 2913.06] about enterprise is I'm eager to see if this ever happens in the business world,
[2913.70 → 2920.26] where they really start to understand the value is in your business logic, not in where your APIs
[2920.26 → 2926.02] live, what stack you're using. It's about how quickly can you execute and how much agility do you
[2926.02 → 2932.10] have to pivot with the market. And they need to understand like there's a cost to having a bunch
[2932.10 → 2936.58] of your engineer. Like you have a hundred engineers out of those hundred engineers. If
[2936.58 → 2943.14] 60% of their time is spent doing basic stuff that can be outsourced, then like imagine how much stuff
[2943.14 → 2948.18] you can unlock in terms of your business being agile. And so that's something that needs to happen.
[2948.18 → 2953.54] And it's just not happening. I'm like, I'm a whole PlatformIO will be part of that strategy,
[2953.54 → 2959.06] but you know, it's just a gap. It's a serious, serious gap. For me, it's a form of talent waste.
[2959.06 → 2959.46] Correct.
[2959.46 → 2963.94] Like I see a lot of smart people doing things that are not that exciting anymore, you know?
[2963.94 → 2968.34] And it's like, come on, man. Like we solved this problem 20 years ago. Why are we solving
[2968.34 → 2970.18] it again here? You know? So.
[2970.18 → 2976.82] Correct. And that's exactly our strategy. Our strategy is exactly to tap into that exact
[2976.82 → 2982.50] problem and give us a solution. This kind of out of the box experience. And the issue with the
[2982.50 → 2988.98] enterprise and that kind of like we notice, and we experience is that like you were saying, right?
[2989.54 → 2995.30] Nothing is new there. How can we actually value more the investment that the enterprise does to
[2995.30 → 3000.74] create value for their customers? Yes. More than actually trying to actually spend a huge amount of
[3000.74 → 3008.02] OPEX capital into operating something that fundamentally- It can be bought. Exactly. Right.
[3008.02 → 3011.78] Yeah. We need to shift the standards for build versus buy. Correct.
[3011.78 → 3017.30] We need to shift the line in the sand a little bit more. And I feel like platform and PlatformIO is
[3017.30 → 3022.74] helping hopefully elevate that. Yeah. And there is actually a perception problem there, right? In
[3022.74 → 3030.34] build versus buy. And Matteo and I have been also there. Like for engineers, when you hear we buy something,
[3030.34 → 3037.46] you feel like if your brain power has been diminished to something like an implementation, right? And we
[3037.46 → 3043.06] actually want to kind of like completely flip the equation completely there and say, no, actually the
[3043.62 → 3051.30] the buy is mostly a buy-in into certain practices, certain out of the box. Oh, right. Outsourcing your
[3051.30 → 3056.02] brain power to some degree. Correct. Like, like here's, I'm going to follow this thought leadership. Yeah.
[3056.02 → 3061.78] Exactly. It's all about kind of like also redirecting energy in something that is more valuable. Like,
[3061.78 → 3068.34] let's be very honest, building a logging system. I don't find it personally challenging. It's nice to
[3068.34 → 3073.22] solve it at scale the first time, and then it's like, okay, copy and paste, right? Yeah. Basically,
[3073.22 → 3079.22] the Auth0's entire business strategy is like everybody outsources. Yeah. But distributive systems,
[3079.22 → 3083.62] if you think they are actually kind of like, they have nuances that are nice to solve,
[3083.62 → 3087.70] but then once that you solve them, you can apply them everywhere. Yeah. And so on thing that we
[3087.70 → 3093.46] actually are going to accomplish with PlatformIO without revealing the secret ingredients, we actually
[3093.46 → 3104.26] wanted to try to abstract away the operational side of building APIs and also kind of like the complexity
[3104.26 → 3111.94] of, for example, managing the team that builds APIs. So we actually are focusing mostly on how can we
[3111.94 → 3121.94] actually make sure that people focus only on that business logic and the rest it's out of the box.
[3121.94 → 3126.58] It's just given. Mathieu and I always use this term. It's a given. It's there. Furthermore, it's just like use it,
[3126.58 → 3131.54] right? Don't question it too much. But make it still composable, right? Because it has to be composable
[3131.54 → 3136.42] for the different environments. So you're planning to build stuff out like, I don't know, load balancing
[3136.42 → 3143.86] and all this orchestration and all that junk that people want. Yeah. So kind of, I've been personally,
[3143.86 → 3150.58] right, very vocal on the time about service mesh when it was just at the beginning of exploding.
[3151.30 → 3157.38] And I always then started calling it a little bit of a lie to developers because it's a great story
[3157.38 → 3162.98] for operators, but developers, they don't get any direct benefit out of that. So we actually want to
[3162.98 → 3169.54] bring that equation back to be favourable for developers. So we are actually trying to build,
[3169.54 → 3178.10] in our vision, there is to build some sort of, let's call it a runtime that is some sort of like a
[3178.10 → 3184.58] kernel to these applications and then start to replicate itself, you know, in the different
[3184.58 → 3190.26] distributed applications, distributed teams. So we actually imagine that the ultimate abstraction
[3190.26 → 3195.86] is something that will be able to run this business logic more than produce the business logic.
[3195.86 → 3200.82] Cool. So also, I wanted to ask about, it seems it's not just you two, right?
[3200.82 → 3201.70] Yeah, it's not.
[3201.70 → 3202.26] Yeah.
[3202.26 → 3203.46] We have a small team.
[3203.46 → 3208.74] I noticed more contributors on the project than just you two. So are you like, what, five people now?
[3208.74 → 3209.94] Or are you looking to grow?
[3209.94 → 3216.50] Something like that, yeah. We are just, just there. We are not looking to grow and anything else.
[3216.50 → 3223.38] Actually, I just wanted to thank all the people that have worked on, on this journey so far,
[3223.38 → 3233.14] believing on two wild Italians that, and you know, you jump on and on a new company and so on. It's been
[3233.14 → 3235.54] a huge leap of faith from everybody.
[3235.54 → 3240.10] Well, I mean, I would imagine that you probably will have the best like staff meeting food and just
[3240.10 → 3243.94] the best office parties like, right? Like the food's always going to be great. And
[3243.94 → 3249.70] look, we don't have an office. Some of us have never met in person.
[3249.70 → 3255.22] Met in person. Okay. But that is a fricking cool story though, right? Like a true modern company,
[3255.22 → 3262.10] like you all are working remotely in the open. And some of you haven't even met like that. I mean,
[3262.10 → 3269.14] that is like, for me, just like the cherry on top of the story, like fascinating. It's like,
[3269.14 → 3273.30] you're pushing things forward in many ways. So do you feel like PlatformIO is going to be
[3274.10 → 3278.26] beloved and kind of embraced by startups initially, right? Because like startups are the ones that are
[3278.26 → 3282.50] always more open to like, what can we do to quickly ramp up, right? Like they're the ones that really
[3282.50 → 3288.66] need that true agility, and they need to catch up on their engineering, you know, help. So is it a startup?
[3288.66 → 3293.78] Perfect. First, and this is, I don't care too much about startups.
[3293.78 → 3296.82] Oh no, don't say that out loud. What I care about is-
[3296.82 → 3300.26] You just got this off the show. No, no. No, let me finish. Let me finish.
[3300.26 → 3304.82] Your bread and butter, Matteo. Like everybody has a customer, and they don't always need to love them.
[3304.82 → 3310.74] They just need to love their money, right? No. I deeply love developers. Okay.
[3310.74 → 3317.78] Okay. The fundamental great part is that I deeply love developers. I want them to have the best
[3318.42 → 3323.78] experience that they can have. Right. And of course, we want to serve startups at their best.
[3324.26 → 3331.22] Okay. But first and foremost, as this is this initial phase of our company, what we want is to
[3331.86 → 3337.46] help developers get off the ground, help them deliver software very quickly. And of course,
[3337.46 → 3343.06] help companies that want to adopt this, help startups, help medium, small shops, okay?
[3343.62 → 3347.78] Small agencies, help all the companies that need these kinds of tools the most.
[3347.78 → 3352.02] Yeah. There's a big need. There is a big need for this kind of stuff. So we are happy to receive all
[3352.02 → 3355.30] the feedback and incorporate all the feedback into our product. Yeah.
[3355.30 → 3358.98] But that's me. Luca will tell you that he's all in for the clients.
[3358.98 → 3366.90] Just to add, right, for us, it's very important that we are taking out of context the problem. And we go
[3366.90 → 3373.14] back to your point, Amal, that was before, right? We are looking at problems in a very abstracted
[3373.14 → 3378.82] and lateral way. We actually believe that the context on which this problem is going to be
[3378.82 → 3383.86] operated changes certain variables of that operation, but shouldn't change the solution,
[3383.86 → 3389.14] right? Authentication authorization are exactly the same for a startup with two people running
[3389.14 → 3397.30] whatever application to a hundred thousand people organization. The problem is that, and I go back
[3397.30 → 3402.26] to my best friend Einstein, is the observation point, right? Where you observe this problem from.
[3402.26 → 3409.46] That's what changes the equation of that solution. And for us, we actually want to try to change that
[3410.18 → 3417.62] total misconception and say, well, authentication and authorization are exactly the same. It's just that
[3417.62 → 3421.86] you need different type of scales and different probability requirements, but the holistic problem
[3421.86 → 3426.98] is exactly the same. Yeah. And so with PlatformaticDB, that's how we actually started this journey,
[3426.98 → 3432.26] right? Towards our cloud. And we said, any developers that need to use a database,
[3432.26 → 3437.46] ourselves included, to build our own product, has these requirements. So let's go back to first
[3437.46 → 3442.98] principles, build it up and stack up on, stack up on, stack up on. But it's always about the context.
[3442.98 → 3448.34] That's why we believe that it works on my machine. It's something that we want to make true. It works
[3448.34 → 3453.70] on my machine. It works on your cloud. Furthermore, it works in our cloud with no changes. That's our promise.
[3453.70 → 3459.22] That's our ultimate goal is that we want to have this runtime, this atomic application to run
[3459.86 → 3464.26] everywhere with no changes. That's incredible. And is everything MIT license?
[3464.26 → 3466.58] So we have an Apache license. It's Apache 2.
[3466.58 → 3471.14] Oh, we'll go. Apache 2. Okay. Interesting. Very, very cool. Yeah. I mean,
[3471.14 → 3476.58] I'm excited about this future. I'm here for it. We've had a huge need in the community, as you
[3476.58 → 3483.54] know. I'm really eager to hear when was the first commit for Problematic and Problematic. Oh my God.
[3484.10 → 3488.66] I made this mistake too in a video. You called it Problematic too. I was like, what the hell?
[3489.30 → 3495.86] Where did this word Problematic even come from? You've been calling it Problematic DB. Okay. When was the
[3495.86 → 3499.94] first commit for PlatformIO? And like, when was the first handshake for both of you? Like,
[3499.94 → 3503.78] I'm just curious because I, Matteo said June earlier, and I'm like, damn, like you all created
[3503.78 → 3507.94] a company and a concept in four months. Like, I'm like, do I need to quit my job? I don't know.
[3507.94 → 3512.58] Like, this is so cool. Like, I'm so impressed. I'm not going to quit my job if anybody's saying,
[3512.58 → 3512.90] don't worry.
[3512.90 → 3518.42] The handshake, Amal, was actually extremely easy. We, as friends, we have been chatting,
[3518.42 → 3527.06] we have been sharing a lot of thoughts and we actually, and shook and we kind of came to an agreement
[3527.06 → 3532.90] that it was the right journey to start. I think it was the end of April, beginning of May when we
[3532.90 → 3538.42] first started to be very, very serious about it. So that was kind of like there when we started to
[3538.42 → 3544.26] say, well, probably we need to take the leap. And yeah, we need to incorporate, and we need to create
[3544.26 → 3549.54] a company and quit our jobs to get this going. Like, we need to get this done now.
[3549.54 → 3552.42] Yeah. Yeah. All the logistics need to come later. Okay.
[3552.42 → 3558.58] That's the gist essentially. Like we, it was very late. I was on a two-week trip on vacation for two
[3558.58 → 3566.50] weeks with my family doing a road trip with our kid in the south of France. And in the meanwhile,
[3566.50 → 3572.02] I was doing the day, I was doing all the family activities and stuff. And during the nights,
[3572.02 → 3577.38] I was reviewing documents for the company with all the incorporation staff and so on and so forth
[3577.38 → 3581.86] with Luca. It was quite a wild ride at that point in time. So yeah.
[3581.86 → 3587.62] Yeah. Super cool. Well, again, so where can people find you online? Where can they continue
[3587.62 → 3592.26] learning about the project? You're going to be at Node Comp U this week. Hopefully there will be a
[3592.26 → 3597.14] recorded workshop that folks can listen to and watch. But what's your website? What's your handle?
[3597.14 → 3604.02] What's all your stuff? Our website is platformatic.dev. And you can find us there. That's the company
[3604.02 → 3612.66] website. All the open source stuff are at oss.platformatic.dev. Or you can find us at the...
[3612.66 → 3620.02] GitHub org. You can find us on Twitter at PlatformIO. Or you can just simply NPM i PlatformIO, and you're
[3620.02 → 3625.86] good. Yeah. So... All the things. All the things. Yeah. And Mateo, you have a cool newsletter too.
[3625.86 → 3630.50] I'd love to plug that for you. Yeah. Yeah. If you want to listen to the wisdom of Mateo Colin,
[3630.50 → 3635.38] who's like a wonderful teacher and very generous with all of his knowledge. Thank you. He's on the
[3635.38 → 3639.38] Node Technical Steering Committee. He's a huge open source contributor and maintainer. Furthermore, he's awesome.
[3639.38 → 3642.66] Someone I think everyone from our community should be learning from, to be honest. But yeah. Do you want
[3642.66 → 3645.38] to tell us about your newsletter? And nodeland.dev.
[3645.38 → 3651.86] NodeLand.dev. And we'll put a link in our show notes. So with that said, kids, we are wrapping
[3651.86 → 3656.90] this show up. I'm super excited. Can't wait to try it. Definitely going to use this for my next
[3656.90 → 3661.54] few projects to play around with it. And it was really great spending time with you,
[3661.54 → 3669.86] both Luca and Mateo. Thank you. I think it's safe to say ciao. Ciao. Absolutely. Ciao. Ciao,
[3669.86 → 3676.34] everybody. Ciao, ciao. Ciao. Bye bye. Thank you. Ciao.
[3680.34 → 3685.06] All right. That's our show. Thanks for hanging with us. If this is your first time listening,
[3685.06 → 3691.54] subscribe to the pod at jsparty.fm. And if you're a long time JS Party animal, do us a solid by sharing
[3691.54 → 3698.34] the show with your friends. Help us help more people with weekly web dev goodness. Thanks again to Vastly and
[3698.34 → 3702.98] Fly for partnering with us. Please check out what they're up to. They support all of our work.
[3702.98 → 3707.70] And of course, thank you to our Beat Freakin' Residence, Break master Cylinder. These beats are
[3707.70 → 3714.66] dope because BMC makes dope beats. That's how it works. Next up on the pod, Ball, Nick, and myself
[3714.66 → 3720.10] discuss what's new and noteworthy in the community. Cloudflare's recent announcements, updates from the
[3720.10 → 3725.62] latest TC39 meetings, something grumble TypeScript, the Figma acquisition, and a lot
[3725.62 → 3740.26] more. Stay tuned for that. We'll drop it into your podcast app next week.
