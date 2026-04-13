[0.00 → 3.28] I'm more of a Python guy than I am a Ruby guy.
[3.52 → 6.64] And I really loved the Django model for a long time, batteries included.
[7.10 → 9.22] It was kind of everything you needed to run a web app.
[9.42 → 11.70] Like, cool, here's authentication, here's caching,
[11.98 → 14.50] here's all these things that I normally have to go grab off a shelf
[14.50 → 15.66] when I'm building a web app.
[15.90 → 17.50] And Postgres is kind of that for databases.
[17.66 → 18.58] It's like batteries included.
[18.84 → 19.64] Here's all the things.
[19.74 → 20.52] Here's your data types.
[20.82 → 22.24] Here's your extra indexes.
[22.34 → 23.16] Here's your Pub Sub.
[23.28 → 24.24] Here's you're geospatial.
[24.48 → 26.04] Here's your queue functionality.
[26.44 → 27.78] Here is all that.
[27.88 → 29.70] And it's like, cool, we've checked all those boxes.
[29.70 → 31.98] Now let's just keep making it stable.
[32.30 → 33.84] A little new feature here and there.
[34.02 → 34.68] More polished.
[34.82 → 35.64] Easier to use.
[35.98 → 37.38] And a big one's always faster, right?
[39.94 → 42.62] Bandwidth for Changelog is provided by Vastly.
[43.00 → 44.88] Learn more at Fastly.com.
[45.12 → 48.20] We move fast and fix things here at Changelog because of Rollbar.
[48.34 → 50.02] Check them out at Rollbar.com.
[50.26 → 52.44] And we're hosted on Linde cloud servers.
[52.78 → 54.78] Head to linode.com slash Changelog.
[55.10 → 56.18] What up, friends?
[56.18 → 58.88] You might not be aware, but we've been partnering with Linde
[58.88 → 60.22] since 2016.
[60.58 → 61.54] That's a long time ago.
[61.94 → 65.70] Way back when we first launched our open source platform that you now see
[65.70 → 66.88] at Changelog.com.
[67.38 → 68.90] Linde was there to help us.
[69.30 → 70.98] And we are so grateful.
[71.52 → 73.02] Fast forward several years now,
[73.22 → 75.04] and Linde is still in our corner,
[75.44 → 76.30] behind the scenes,
[76.42 → 79.74] helping us to ensure we're running on the very best cloud infrastructure
[79.74 → 80.46] out there.
[80.92 → 81.74] We trust Linde.
[81.74 → 82.96] They keep it fast,
[83.08 → 84.34] and they keep it simple.
[84.66 → 87.86] Get $100 in free credit at linode.com slash Changelog.
[88.02 → 88.50] Again,
[88.80 → 93.88] $100 in free credit at linode.com slash Changelog.
[93.88 → 107.56] Welcome back, everyone.
[107.70 → 110.40] This is the Changelog podcast featuring the hackers,
[110.98 → 111.54] the leaders,
[111.92 → 114.00] and the innovators in the world of software.
[114.56 → 115.60] I'm Adam Stachowiak,
[115.70 → 117.12] editor-in-chief here at Changelog.
[117.48 → 117.90] Today,
[118.06 → 119.64] Jared talks to PostgreSQL,
[119.64 → 121.58] aficionado Craig Kirsten's,
[121.88 → 124.92] about his and our favourite relational database,
[125.28 → 125.60] yes,
[125.98 → 126.28] Postgres.
[126.72 → 130.16] Craig details why Postgres is unique in the world of open source databases,
[130.62 → 132.26] which features are most exciting,
[132.66 → 134.66] the many things you can make Postgres do,
[135.02 → 136.40] and what the future might hold.
[136.78 → 136.98] Oh,
[137.16 → 140.42] and also some awesome PSQL tips and tricks.
[140.90 → 141.30] Here we go.
[146.34 → 147.06] So, Craig,
[147.12 → 149.62] you're in an interesting position because you've done so much for,
[149.64 → 151.30] or Postgres the project,
[152.16 → 153.36] and you've taught,
[153.52 → 154.38] and you've spoken,
[154.60 → 155.42] and you've blogged,
[155.44 → 157.34] and you've provided endless resources.
[157.56 → 159.62] You've curated the PG Weekly newsletter.
[160.12 → 162.88] I've been following a lot of your stuff for a long time,
[162.94 → 165.06] just learning as you kind of put stuff out there,
[165.10 → 166.54] as I'm a casual Postgres user.
[166.86 → 167.56] Long-time user,
[167.70 → 168.42] but just casual.
[168.50 → 171.08] I don't really dive into the nitty-gritty very often,
[171.16 → 172.18] because I just don't have to.
[172.70 → 173.94] But you've done all of this,
[174.18 → 176.10] and yet Postgres the project,
[176.22 → 176.36] like,
[176.42 → 177.58] it's not your baby.
[177.58 → 178.88] Maybe it feels like it now,
[178.88 → 179.28] but, like,
[179.32 → 182.68] it's a long-standing open-source thing with dozens of people.
[182.84 → 186.24] Tell us how you came involved with the project,
[186.24 → 187.88] and maybe how you fell in love with the database.
[188.52 → 188.74] Yeah.
[188.94 → 189.28] So, I mean,
[189.30 → 189.90] I think, you know,
[189.98 → 191.04] Postgres itself is interesting.
[191.18 → 191.30] Like,
[191.60 → 194.86] I've actually never contributed a single line of code myself to it.
[195.64 → 198.24] That's so many other people that know the ins and outs.
[198.44 → 199.00] I've read it,
[199.04 → 199.72] I've looked at it,
[200.06 → 202.46] but maybe one day I actually will.
[202.46 → 203.26] But yeah,
[203.36 → 206.62] my contributions have mostly been on the community side, right?
[206.84 → 207.20] Speaking,
[207.80 → 208.50] talking with others,
[208.62 → 209.32] working with people.
[209.80 → 211.30] I actually came to it,
[211.92 → 214.52] I guess the first place was at a startup many years ago,
[214.62 → 215.46] that I joined Treviso.
[216.22 → 217.38] I joined it about 10 people.
[217.98 → 221.86] They were taking Postgres and transforming it into a streaming database,
[221.86 → 224.26] that basically did map reduce on data as it came in.
[224.90 → 227.60] It was back in about 12 years ago,
[227.80 → 229.22] during one of the last crashes.
[230.08 → 231.54] And basically,
[232.00 → 235.00] that complex events processing was this new kind of cool,
[235.36 → 235.78] sexy thing.
[236.30 → 239.64] I had familiarity with it from college and university,
[239.64 → 240.88] but hadn't really used it there.
[241.00 → 244.00] But we were basically taking and transforming it into something,
[244.12 → 244.26] you know,
[244.40 → 245.22] really advanced,
[245.38 → 246.86] handling a lot of data.
[247.02 → 248.12] We had customers like,
[248.76 → 251.34] I think MySpace was one of our customers back in the day,
[251.34 → 252.84] when they were still the hot thing,
[252.92 → 253.04] right?
[253.12 → 254.40] Which states it pretty well.
[255.06 → 256.34] And from there,
[256.66 → 257.92] we built a product,
[258.20 → 261.22] and the company grew and dwindled back down to about 10 people,
[261.28 → 262.00] and I moved on.
[262.54 → 265.14] And I found myself a few years later at Heroku.
[265.60 → 267.24] And it was fascinating,
[267.52 → 270.04] because it was kind of like yourself, right?
[270.20 → 271.08] You're an app developer,
[271.28 → 271.68] it's there,
[271.78 → 272.46] you're using it.
[272.96 → 274.24] And even internally at Heroku,
[274.36 → 274.70] we had,
[274.72 → 275.00] you know,
[275.80 → 276.60] 50 employees,
[276.88 → 277.42] and they're like,
[277.46 → 277.60] yeah,
[277.74 → 278.46] Postgres is fine,
[278.62 → 278.84] whatever,
[278.96 → 279.46] I'll use it.
[279.46 → 279.72] Right.
[279.82 → 280.10] I'm like,
[280.26 → 280.50] guys,
[280.50 → 281.90] you've got a great database here.
[282.50 → 285.66] And I found myself starting to blog more and more about,
[285.92 → 286.02] like,
[286.84 → 287.90] I'm a lazy blogger.
[288.20 → 290.10] I think I have a blog post talking about,
[290.16 → 290.34] like,
[290.40 → 291.04] why I blog,
[291.10 → 291.92] and it's because I'm lazy.
[292.04 → 292.16] Like,
[292.20 → 293.60] once I explain something twice,
[294.22 → 295.36] I don't want to explain it again.
[296.26 → 297.80] So I'll just write a blog post on it.
[297.86 → 297.98] Like,
[298.02 → 299.96] once I found myself teaching something,
[300.08 → 300.22] like,
[300.26 → 300.92] let's just go,
[301.04 → 302.74] and it doesn't have to be polished or useful.
[303.70 → 305.34] I tell a lot of people that about blogging,
[305.40 → 305.56] like,
[305.72 → 306.72] don't worry about getting it perfect,
[306.80 → 307.44] just get it out there.
[307.44 → 309.14] It probably has value for a lot of people.
[309.14 → 313.04] And you just send people the link when they ask you questions instead of having to rewrite the answers,
[313.12 → 313.28] right?
[314.16 → 315.22] I absolutely do.
[315.30 → 317.22] Sometimes I feel like an absolute jerk when I'm like,
[317.30 → 317.72] hang on,
[317.80 → 319.06] I'm not going to actually answer.
[319.14 → 320.90] I'm just going to send you a link to a blog post.
[321.04 → 321.28] Right.
[321.36 → 322.86] I definitely feel a little bit like a jerk,
[322.98 → 324.16] but it's why it exists,
[324.20 → 324.36] right?
[324.52 → 324.82] Right.
[325.48 → 326.08] It's kind of like,
[326.14 → 327.00] go read my book,
[327.08 → 327.38] you know?
[327.48 → 327.62] Oh,
[327.62 → 328.06] that's worse,
[328.06 → 330.06] because you have to buy the book with the blog post,
[330.14 → 330.60] at least it's free.
[330.60 → 331.80] But I know people are like,
[331.88 → 332.58] just go read my book.
[332.64 → 333.30] It tells you the answer.
[333.36 → 333.52] It's like,
[333.56 → 333.70] well,
[333.70 → 335.00] I asked you the question right here,
[335.38 → 337.46] but it's online, and you're asking,
[337.62 → 338.86] like sending a link is useful.
[339.00 → 339.74] I understand it.
[339.78 → 339.86] Yeah.
[340.76 → 341.04] Yeah.
[341.18 → 341.50] So,
[341.70 → 342.10] um,
[342.16 → 345.48] I found myself really kind of speaking to like app developers,
[345.56 → 345.72] right?
[345.74 → 347.26] Like I'm not a DBA,
[347.88 → 350.40] but I helped out developers all the time with,
[350.50 → 350.66] you know,
[350.70 → 351.76] how do I troubleshoot this?
[351.84 → 353.00] How do I troubleshoot that?
[353.60 → 354.04] Um,
[354.12 → 355.34] if I go way back at Heroku,
[355.52 → 355.76] you know,
[356.00 → 360.88] we had all these rails developers asking for a database and we kind of
[360.88 → 361.04] thought,
[361.20 → 363.14] how hard could this be back at that time?
[363.30 → 364.84] Amazon RDS didn't even exist.
[365.56 → 365.96] Um,
[366.04 → 366.28] right.
[366.42 → 367.30] And we looked and said,
[367.44 → 368.98] Postgres is a really solid database.
[369.16 → 370.62] Like it has good fundamentals,
[370.82 → 371.76] a good core.
[372.02 → 372.52] I mean,
[372.52 → 374.02] if you go back to the history of it,
[374.02 → 376.94] like Postgres has the same roots as so many other databases.
[376.94 → 377.80] Like it's in the name.
[378.26 → 380.54] Ingress was one of the early origins,
[380.54 → 382.98] like grandfathers of databases that came out of UC Berkeley.
[383.82 → 386.36] post Ingress is Postgres.
[386.50 → 386.90] There it is.
[387.42 → 391.24] And so many other databases have that same root of Ingress,
[391.36 → 391.88] like Base,
[392.00 → 392.60] SQL server,
[392.90 → 397.30] but it's over 20 years old now, and it's just solid and sturdy.
[397.52 → 399.94] So I got started with it way back,
[400.18 → 404.20] really got into it at Heroku running and helping build Heroku Postgres for a
[404.20 → 406.84] number of years and have found myself doing it,
[407.04 → 407.48] um,
[407.64 → 407.92] you know,
[407.92 → 409.42] at Cites and now at Crunchy,
[409.42 → 411.80] Crunchy data building and running their cloud service,
[411.80 → 414.10] basically just running Postgres for people for a while.
[414.10 → 414.66] Mm-hmm.
[415.22 → 417.74] So you may remember this history better than I do,
[417.84 → 420.28] but I was an early Rails developer and I know that Rails,
[420.38 → 422.90] the original stack was MySQL,
[423.22 → 425.38] was the production database.
[425.50 → 426.72] Now it started with SQLite,
[426.78 → 427.88] so you could just run your tests,
[427.98 → 429.08] but like people,
[429.08 → 430.92] even Basecamp ran MySQL.
[431.74 → 436.76] And at a certain point it was like MySQL fell out of favour and Postgres came
[436.76 → 437.60] into favour,
[437.60 → 440.64] just like amongst the zeitgeist of Rails developers.
[440.94 → 442.54] And I can't remember why,
[442.64 → 443.90] like what triggered that?
[443.98 → 446.92] Was it because of Heroku's influence and Heroku Postgres?
[447.46 → 450.58] I'm pretty sure it was Heroku's influence.
[450.74 → 451.30] Like at Heroku,
[451.44 → 452.52] you've got a Postgres database.
[452.72 → 454.18] Every Rails app got a Postgres database.
[454.18 → 457.84] So I'm pretty sure we can thank Heroku for a lot of it.
[458.48 → 461.28] I wish I could say it was wonderfully thought out and strategic.
[461.50 → 462.90] We thought Postgres was a good database.
[463.10 → 464.36] We decided to run Postgres.
[464.48 → 465.72] Like I think it was the right choice.
[466.28 → 468.34] And we invested a lot in it to make it better.
[468.76 → 471.70] Postgres for the longest time wasn't the most user-friendly.
[471.96 → 473.84] It wasn't the most sexy database.
[473.96 → 475.04] Can databases be sexy?
[475.50 → 475.96] I don't know.
[476.04 → 477.22] I hear people say that all the time.
[477.28 → 477.82] I'm like, really?
[478.14 → 479.22] But I know what you're saying.
[479.36 → 480.88] Maybe exciting is a better word.
[481.48 → 481.60] Yeah.
[481.60 → 481.92] Right.
[482.10 → 486.58] It's not my idea of like a Friday night is to go hack on Postgres.
[487.20 → 489.48] But it's gotten the cooler features, right?
[489.72 → 491.92] Like JSON was a big one.
[492.14 → 492.34] Yeah.
[492.62 → 495.60] So I think that really shifted with Heroku.
[495.88 → 500.40] I actually remember Heroku supported it probably five years before Amazon RDS did.
[501.24 → 504.58] I was at, I go to a lot of Amazon conferences, reinvents, a big one.
[504.74 → 506.30] It's massive, massive conference.
[506.30 → 511.28] And they roll out product announcement after product announcement after product announcement.
[511.98 → 513.40] And I remember being there.
[513.54 → 514.90] Like I had a heads-up.
[514.96 → 515.58] It was coming.
[515.80 → 519.60] So I made sure to actually go to that keynote to kind of see the announcement, that sort of thing.
[520.00 → 522.20] And there was literally a standing ovation.
[522.82 → 526.12] Like I've never seen this before at a tech conference or a product announcement.
[526.12 → 529.48] Like there was this big pause, standing ovation.
[529.80 → 531.12] Like the speaker started talking again.
[531.24 → 533.36] And like people still standing on their feet clapping for this.
[533.54 → 534.82] I've never seen this before.
[534.92 → 539.18] Never seen this after at a tech conference when you announce a new product.
[539.18 → 542.20] So why do you think Postgres is so beloved?
[542.32 → 545.04] I know that I switched myself from MySQL to Postgres.
[545.36 → 549.78] Mostly when I switched, maybe it was because of just the flow of the tutorials and like this
[549.78 → 552.00] general lemming status of developers.
[552.00 → 553.42] And I was just in there amongst them.
[553.42 → 555.70] But I remember I had some data.
[555.90 → 557.72] This is way back in like 05, 06.
[557.82 → 560.84] I had data consistency problems with my MySQL stuff.
[560.98 → 566.36] And I read some blog posts about how MySQL can just like be recording nothing, and it's not
[566.36 → 567.04] going to report it.
[567.04 → 570.72] And like there were these edge cases that are in there where it's like kind of less safe.
[570.98 → 576.80] And Postgres was there, and it had this reputation of being just rock solid, consistent and more
[576.80 → 578.12] strict with your data.
[578.88 → 583.08] And because of the ease of switching in Rails, I could switch very quickly.
[583.42 → 588.08] And so I just started switching all my projects over, and I found it easy to use to administer.
[588.80 → 590.70] And so that was kind of my switching point.
[590.78 → 593.22] I didn't really have much more thought than that.
[593.22 → 598.56] I think if you look at it, there's, you know, Postgres was that.
[598.76 → 601.14] It was like, I'm going to be safe and reliable.
[601.36 → 602.48] I'm not going to lose your data.
[603.00 → 606.10] That's a funny thing to think about when it comes to a database, right?
[606.22 → 608.50] Like keeping your data, not losing it.
[608.52 → 611.38] But that was like Postgres's kind of core value.
[611.46 → 613.84] Like we're not going to add shiny new things.
[613.84 → 620.28] The MySQL defaults got some flack for a little while because, hey, certain modes it would run.
[620.38 → 621.82] It had a different type of storage engine.
[621.98 → 623.84] Certain ones weren't as safe.
[624.50 → 627.64] MySQL, it's funny when you do like search in MySQL.
[627.80 → 629.94] By default, it's case-insensitive.
[630.70 → 631.68] Uber, it was hilarious.
[631.76 → 635.04] Uber switched from MySQL to Postgres and then Postgres to MySQL.
[635.04 → 637.96] So they've gone, you know, back and forth a couple of times.
[638.08 → 648.18] But when they swapped to Postgres, they had to go and figure out that they had all this app logic that relied on things being case-insensitive because the database just doesn't respect case search.
[648.52 → 650.54] To me, that's a little bit of an anti-feature.
[650.78 → 653.04] I can go on about, you know, MySQL versus Postgres.
[653.40 → 655.92] Like I think MySQL is a good database and does good things.
[656.34 → 659.12] I think Postgres really started at being safe and reliable.
[659.46 → 659.54] Yeah.
[659.64 → 662.44] And then we said now there's these rich user features.
[662.88 → 664.22] There are things like JSON.
[664.22 → 667.62] There are things like common table expressions, window functions.
[667.96 → 673.16] There's a really rich set of features that I think we're going to hit on a bunch of them scattered throughout.
[673.34 → 673.44] Yeah.
[673.44 → 679.34] Like I could give you the laundry list of them right now, but it's like each one is unique in its own right.
[680.04 → 682.32] But it started with that being really safe and reliable.
[682.72 → 688.68] I look at a lot of other databases, you know, Congo didn't start as safe and reliable and work to catch up to that.
[688.80 → 690.02] It started as easy to use.
[690.02 → 694.66] And I think that developers have come around to respecting and appreciating that, right?
[694.70 → 699.32] Like you have corruption, you spend two weeks, hey, and data's gone.
[699.82 → 701.66] How do you answer that to a customer, right?
[702.00 → 702.24] Right.
[702.58 → 708.10] For all the shiny things we like, you know, new frameworks that come out every single day, old and reliable just works.
[708.10 → 713.92] And I've really started to appreciate that, like, hey, I've got my Braille stack or my Python and Django stack and my Postgres database.
[714.12 → 716.06] And this app can go really far.
[716.18 → 719.16] I don't need shiny new things to build an interesting business.
[719.74 → 719.76] Yeah.
[719.76 → 722.38] I like that as well, especially for a database.
[722.48 → 730.62] It's like there are areas in my application where I'm willing to experiment, and I'm willing to, you know, go with the bleeding edge and bleed a little bit, but get those bleeding edge features.
[731.14 → 738.50] And there's something just, like, makes you sleep well at night, just like this database stores my data and I can just trust it to do that.
[739.36 → 741.54] And I think that was one of the reasons why I just stuck with it.
[741.62 → 743.94] It never really stabbed me in the back.
[744.06 → 747.10] You know, I never had that moment where I was like, oh, Postgres, you screwed me over.
[747.28 → 747.48] Right?
[747.86 → 748.08] Right.
[748.48 → 750.16] It's the case with so many others, too.
[750.24 → 751.40] You have that bad experience.
[751.76 → 753.22] And, yeah, it's shiny and new.
[753.32 → 755.04] But, man, you lose data.
[755.18 → 757.12] I think there's kind of nothing worse you can do, right?
[757.20 → 759.44] Like, obviously, I'm a data guy.
[759.52 → 760.28] I like databases.
[760.78 → 764.06] But that's more valuable than downtime, right?
[764.14 → 764.36] Fine.
[764.42 → 767.02] Go be down for an hour, a few minutes, or a day.
[767.06 → 769.20] But don't lose the data that you can't get back.
[769.48 → 776.68] If you're banking or something like that, like, and you lost my deposit, I couldn't be more unhappy with you.
[776.68 → 777.80] Yeah, exactly.
[777.80 → 777.88] Exactly.
[778.18 → 779.64] So help us out with a little bit of the history.
[779.72 → 788.56] Because one of the things that happened was, like, by the time all this developer movement over to it, I'm sure it was popular, you know, amongst DBA's and amongst, you know, different people around the world.
[788.56 → 789.94] But, like, really, there was a groundswell.
[790.32 → 793.90] And maybe it was the Rails and the Heroku's and whatever this trend was.
[794.20 → 798.20] People started picking up Postgres as, like, their default starter database.
[798.90 → 801.28] But by then, it had been around for a very long time.
[801.36 → 802.90] Like, maybe that's why it was so rock solid.
[803.04 → 804.62] It had the ingress roots.
[804.62 → 812.46] And then it had, I mean, by the time 2006, 2007, when I started using it, it had been actively developed as Postgres for, like, a decade at that point.
[812.64 → 816.00] And it didn't have, like, the JSON features and all the stuff that we're going to get into at that point.
[816.10 → 819.60] But help us unpack, like, where it came from.
[819.68 → 824.18] Who works on this thing and, like, the history and kind of the community around Postgres?
[825.14 → 828.38] Yeah, so a lot of it, we can go way, way back to UC Berkeley, right?
[828.52 → 836.16] Like, Stone breaker, I think, I don't know that he won a Turing Award just for Postgres, but Postgres is a huge piece of that, right?
[836.20 → 838.34] And he wanted to build this kind of extensible database.
[839.24 → 842.70] So he looked at ingress and said, you know, how can we evolve it to the next thing?
[843.12 → 845.24] I think that's a lot of the way back history.
[845.24 → 849.88] There's a great article in ACM looking back at Postgres.
[850.04 → 852.14] I think it goes through a lot of that history.
[852.14 → 861.36] I think there's a lot, too, of those years kind of right after it came out from UC Berkeley of a good stewardship of community that really gets all the credit, right?
[861.46 → 868.50] Like, I go out here and talk about it, but people just slogging away and working on it, making sure it was rock solid.
[869.18 → 875.34] I got in a little bit of trouble a little bit ago when I listed off a few names and I started listing off three or four or five, right?
[875.34 → 882.74] And I think one you've got to point to is Tom Lane, who Tom Lane has contributed to so much open source.
[883.02 → 887.66] He helped create JPEG and TIFF and PNG.
[888.16 → 890.36] Like, he helped authored some of those specs.
[891.08 → 893.52] He helped write lib JPEG, lib PNG.
[894.32 → 897.28] And this is 20, 25 years ago.
[897.44 → 900.08] And then said, yeah, I'm kind of tired of image formats.
[900.42 → 901.50] What's this database thing?
[901.54 → 902.66] Let me spend some time on that.
[902.66 → 909.12] And it's contributed to a massive amount of Postgres code if there are bugs digging in, making sure they're fixed.
[909.22 → 910.10] But you've got him.
[910.28 → 911.44] You've got Bruce Morgen.
[911.62 → 912.84] You've got Robert Haas.
[912.98 → 914.02] You've got Andres Freud.
[914.26 → 916.46] You've got Stephen Frost.
[916.58 → 917.64] You've got Joe Conway.
[917.76 → 918.82] You've got Simon Riggs.
[918.86 → 923.30] You've got a bunch of people that just sit here and work on Postgres.
[923.86 → 926.04] And you can go see all the activity in the open.
[926.18 → 927.34] It's all on the mailing list.
[927.92 → 932.38] It's still, development still happens that way that it did 15 years ago on the mailing list, showing up with patches.
[933.14 → 939.52] It's fascinating that they've got a set of solid committers, major contributors, minor contributors.
[939.78 → 941.70] There's this whole kind of hierarchy there.
[941.80 → 943.10] It's not too formal.
[943.10 → 952.20] There's a lot of debate within the community of like, okay, do we have a major contributor for docs or for community contributions or other things?
[952.30 → 954.22] But the code just moves forward.
[954.38 → 959.10] And I think it's fascinating to me in that it does work that way.
[959.52 → 960.86] Often we talk about open source.
[961.10 → 963.86] Like open source is not a new topic anymore.
[963.86 → 964.90] We talk about it plenty.
[965.52 → 966.98] And databases say they're open source.
[967.22 → 969.08] But Postgres is unique.
[969.42 → 970.26] Yeah, it's open source.
[970.42 → 971.76] And other databases are open source.
[971.82 → 972.74] But no one owns Postgres.
[973.50 → 975.08] No one can own Postgres.
[975.20 → 979.26] You can't go and buy up a company and say, my SQL is now owned by Oracle.
[979.58 → 981.22] Like they own the copyright.
[981.36 → 982.44] They own the code.
[982.44 → 990.92] So Postgres, I guess, in theory, if you went and, you know, had a few billion dollars that you wanted to try to hire all the people that commit to it, maybe.
[991.20 → 993.14] But I just don't see it happening.
[993.28 → 1000.28] And the core structure and the way it's delivered and developed, it's kind of in its own category of what is open source.
[1000.38 → 1003.36] It's community led, community run, community managed.
[1003.64 → 1005.02] It's kind of a purebred that way.
[1005.34 → 1008.70] It's not even like Linux because Linux, you had a benevolent dictator.
[1009.14 → 1009.26] Right.
[1009.58 → 1010.68] Postgres doesn't have that.
[1010.68 → 1012.96] It's got people on equal footing.
[1013.58 → 1018.40] So is there like a governance structure set up or is it just like people debate on mailing lists?
[1018.48 → 1019.46] How does it actually run that?
[1019.82 → 1019.98] Yeah.
[1020.02 → 1021.64] So there's definitely debates on mailing lists, right?
[1021.96 → 1023.58] It is open source in that sense.
[1024.56 → 1026.06] You're not getting away from that at all.
[1026.50 → 1027.54] So there's a core committee.
[1027.74 → 1028.64] That's five people.
[1029.10 → 1034.02] They kind of oversee and there's an entity set up to maintain copyrights and that sort of thing.
[1034.12 → 1039.34] And the Postgres, you know, there is a license that is owned by, you know, a Postgres entity there.
[1039.34 → 1040.74] And they're set up in multiple companies.
[1041.40 → 1044.24] The core team isn't who says what goes in.
[1044.48 → 1046.14] Like core is kind of a steering body, right?
[1046.48 → 1047.44] So there's five people.
[1047.76 → 1051.84] There is no more than two from any company at a time, right?
[1052.04 → 1052.62] I think it's like 40%.
[1052.62 → 1056.52] So if core were to grow to seven, it might change in that sense.
[1056.98 → 1060.48] But basically you don't have a ruling set from any one company.
[1060.96 → 1062.54] So it's distributed across companies.
[1062.80 → 1066.82] But in the actual development, you've got basically you earn a commitment.
[1067.16 → 1067.88] You show up.
[1067.96 → 1068.48] You contribute.
[1068.76 → 1069.52] You review patches.
[1070.84 → 1073.22] Postgres is released a major release once a year.
[1074.36 → 1077.52] Things show up in, you know, ideas on mailing lists, patches.
[1078.20 → 1079.56] There's debate and discussion.
[1080.12 → 1084.96] There's a couple of kinds of sprints, commit fests, where patches are submitted.
[1085.10 → 1085.64] There's an app.
[1085.94 → 1090.26] And the biggest way to build your credibility is come in and review a patch for people.
[1091.46 → 1093.82] Like reviews are always welcome, always helpful.
[1093.96 → 1098.76] Like if you want to build credibility, you don't show up with a, hey, I want to, you know, fix this thing.
[1098.96 → 1101.28] It's show up on the mailing list and engage.
[1101.46 → 1103.42] There are two mailing lists that are the big ones.
[1103.42 → 1107.16] There's a PG SQL hackers list and a PG SQL users.
[1107.48 → 1110.56] The hackers list is where all the interesting stuff happens.
[1110.68 → 1112.26] It's what I read to fall asleep at night.
[1112.54 → 1117.44] But if you want to learn the internals of Postgres, it's a fascinating area to go and read.
[1117.98 → 1119.98] You said earlier you haven't committed a single line of code.
[1120.16 → 1122.30] Have you dove into the code as a readability standpoint?
[1122.46 → 1125.22] I mean, it's a C project, probably millions of lines of code at this point.
[1125.30 → 1128.62] Have you tried to actually tease it apart and look underneath the hood at all?
[1128.62 → 1133.92] At times, not in any in recent years, but at times, absolutely in my career.
[1134.14 → 1134.60] It's funny.
[1134.80 → 1141.42] It's C, but I've heard people, you know, describe that they don't like writing C, but they're okay with writing Postgres C.
[1142.02 → 1144.60] Like it's really well-structured, well-defined.
[1144.78 → 1149.44] Like if you want to see a good example of a large C project, it's a pretty good one.
[1149.44 → 1154.26] It has to be to keep going this long and to stay actively worked on.
[1154.38 → 1166.58] I mean, over the course of all of these years, if you had that much technical debt, and you're just, if you're just slaying in C code, like without good architecture, good refactoring over time, you would just slow to a crawl, crawl to a slow.
[1166.76 → 1167.34] I can't say it right.
[1167.70 → 1169.54] You would just stop moving fast.
[1169.72 → 1174.12] And we see Postgres just keeps on that yearly release cadence, like new features just keep rolling out.
[1174.16 → 1176.92] And they're just built on top of that foundation over and over again.
[1176.92 → 1183.32] Yeah, and I like, it's a testament to so many people long before me that do keep plugging away.
[1183.56 → 1189.12] And there's been an active focus in the community to, I think, to grow that number of committers.
[1189.34 → 1197.56] I think it's at about 40 now that have a commit bit, but you earn that over several years, and you've got to stay active.
[1197.82 → 1202.22] If you don't commit something every year or two, you lose that commit bit.
[1202.22 → 1208.12] And so I think, you know, it takes work to earn it, and it takes work to maintain it.
[1208.88 → 1210.76] And then they're watching each other, right?
[1210.82 → 1212.54] Like you can't go and commit something.
[1212.90 → 1218.02] There have been releases where features got in and some of the code quality wasn't there.
[1218.02 → 1225.78] And that engineer spent, you know, the rest of that next release, that next major release, not writing new features, cleaning up, right?
[1225.78 → 1229.40] Like they hold themselves accountable in a good way.
[1229.52 → 1235.90] So it's definitely an interesting kind of testament of a project that I don't know many other examples like it.
[1235.90 → 1252.64] This episode of The Change Log is brought to you by Chemistry.
[1253.14 → 1260.52] Chemistry is a podcast that tells the stories of teams who work together in new and unexpected ways to achieve remarkable things.
[1260.52 → 1267.32] Each episode of Chemistry tells a story and in each story, you'll find practical lessons for your team and your business.
[1267.80 → 1270.66] I got a sneak preview of season two, and I couldn't stop listening.
[1271.08 → 1277.72] I was once in the U.S. Army and nothing gets me more excited than seeing teams achieve great things when they learn to work together.
[1277.98 → 1279.42] And that's exactly what the show delivers.
[1279.42 → 1289.02] This season, the show travels deep into the underwater caves of northern Thailand to discover how divers, medics, soldiers and volunteers saved a group of trapped teenagers,
[1289.52 → 1296.56] explains how a world-renowned watch company pit their two factories against each other in an attempt to become the best watchmaker in the world,
[1296.86 → 1303.04] and finds out how Iceland went from having one of the highest COVID-19 death rates to a model example of how to deal with the virus.
[1303.34 → 1307.72] These are stories that entertain, and they're packed with business cases you can actually use.
[1307.72 → 1309.86] Season two of Chemistry is out right now.
[1310.16 → 1312.16] Search for Chemistry anywhere you listen to podcasts.
[1312.52 → 1313.72] Check the show notes for a link to subscribe.
[1314.22 → 1316.48] And many thanks to our friends at Chemistry for their support.
[1331.44 → 1336.80] So we talked about its stability and how it doesn't let you down and the data consistency.
[1336.80 → 1346.14] There was also this NoSQL trend, or NoSQL if you prefer, trend, where a lot of shiny new databases were coming out.
[1347.22 → 1351.32] And I'm not sure what year this was, maybe 2010, maybe 2012.
[1352.38 → 1355.06] Time kind of moulds into a continuum.
[1355.06 → 1359.10] But in that range where it was like, look what this thing can do.
[1359.64 → 1365.86] And traditional relational database management systems, RMSs like Postgres and MySQL were really kind of thrown under the bus.
[1366.08 → 1366.90] Like they were stodgy.
[1367.18 → 1369.66] They didn't have the flexibility that you need.
[1369.66 → 1373.26] And a lot of people left Postgres at that time.
[1373.32 → 1377.10] They left SQL altogether to move to NoSQL.
[1378.30 → 1384.88] And those of us that were a little more patient and just kind of like, Postgres just kept adding things that was like, hold on a sec.
[1385.26 → 1387.62] There's that nice feature over there in NoSQL land.
[1387.62 → 1398.18] And you can actually get pretty close or good enough and not have to lose all the, you know, the ACID guarantees and all the things that you have over here with Postgres.
[1399.06 → 1400.06] One of those was JSON.
[1400.26 → 1409.04] Talk about some of the exciting features that have come into the project over the last decade, which have really made it not just be the stable rock that it is, but also it's kind of exciting.
[1409.38 → 1413.18] It's got a lot of cool stuff that they've been adding over the years.
[1413.68 → 1415.20] Tell us some things that excite you about it.
[1415.20 → 1415.68] Yeah.
[1416.46 → 1418.80] So, I mean, JSON's the big one, right?
[1418.96 → 1422.36] Like I can't talk about Postgres and not talk about JSON.
[1423.00 → 1425.16] And for context, that was eight years ago.
[1425.42 → 1427.80] That's pretty old in terms of like technology, right?
[1427.88 → 1431.86] Like what was our front end JavaScript stacks like at that point?
[1431.98 → 1434.16] Like were we still using JQuery maybe?
[1434.70 → 1435.14] Like, yeah.
[1435.70 → 1438.64] For context, a lot's changed and that was landscape, right?
[1438.64 → 1438.82] Right.
[1439.24 → 1441.36] And JSON was a fascinating one.
[1441.36 → 1447.94] I remember having, you know, conversations with the Postgres core community and some of them were really dismissive at first.
[1448.02 → 1449.10] They're like, I've seen this before.
[1449.52 → 1454.72] Like 10 years ago, document databases, XML databases were going to replace relational databases.
[1455.62 → 1457.56] And they came and went.
[1457.78 → 1459.40] They just like went by the wayside.
[1459.86 → 1461.62] Postgres added an XML data type.
[1461.62 → 1468.60] So, technically, Postgres was a document database like 18 years ago when it added the XML data type.
[1468.74 → 1474.18] So, I, you know, defend that Postgres has been a document database for nearly 20 years or so now.
[1474.74 → 1478.20] But, you know, some of them don't write web apps.
[1478.46 → 1482.30] Some of the core developers, they're like, yeah, I built a website once upon a time.
[1482.44 → 1484.18] So, like JSON is foreign to them.
[1484.28 → 1485.40] What is this JSON thing?
[1485.66 → 1487.28] Now, that's not all of them.
[1487.28 → 1492.96] So, I think there were a lot of interesting conversations around that time about NoSQL and JSON.
[1493.38 → 1498.52] And there's really no reason JSON didn't fit into Postgres just fine, right?
[1498.60 → 1500.38] Like, you can leverage JSON.
[1500.62 → 1507.28] And I think the broader debate on a, you know, SQL, NoSQL, or Schema List is a perfect one.
[1507.32 → 1510.18] And we should get into that a little bit because I think there's a lot there.
[1510.86 → 1513.28] But JSON first came in eight years ago.
[1513.52 → 1515.12] And really, we cheated.
[1515.50 → 1516.50] Like, we totally cheated.
[1516.50 → 1522.28] We did validation on JSON, on, as JSON as it came in and stored it in a text field.
[1523.30 → 1525.22] There's nothing special about it.
[1525.50 → 1527.06] Yeah, it wasn't even really like a data type.
[1527.14 → 1530.44] It was just like a text field with like some stuff on top of it, right?
[1530.58 → 1531.14] Pretty much.
[1531.32 → 1533.06] It just went into a text field under the covers.
[1533.66 → 1535.94] Postgres did the validation that it was standard JSON.
[1536.76 → 1537.54] That's about it.
[1537.90 → 1538.76] So, we totally cheated.
[1539.10 → 1541.84] Everyone still loved it and said, okay, cool, I'm going to use this.
[1542.18 → 1546.10] Just proves you don't have to always be technically correct to kind of advance your case.
[1546.74 → 1548.98] And then JSON came a couple of years later.
[1549.26 → 1553.52] And so, JSON is a binary representation on disk of compressed JSON.
[1554.02 → 1556.82] I use it in almost every project.
[1557.16 → 1560.56] Like, I usually have a column called like extras.
[1561.28 → 1562.52] And it's really easy.
[1562.72 → 1563.74] I didn't know I needed this.
[1563.80 → 1564.58] I can throw it in.
[1564.58 → 1566.74] I don't know if it's going to be there long term.
[1567.20 → 1569.24] Feature flags are a great example for it.
[1569.70 → 1571.82] And so, now you've got two data types in Postgres.
[1571.96 → 1573.78] You've got JSON, and you've got JSON.
[1574.34 → 1575.50] So, the B stands for binary.
[1576.14 → 1579.82] One of the an engineer I've worked with for a long time says it stands for better.
[1580.50 → 1584.10] I prefer that version a little bit more.
[1584.10 → 1586.70] Is there any reason to just use regular JSON as text now?
[1586.86 → 1588.14] Is there still reasons to do that?
[1588.50 → 1589.48] So, there's a few.
[1589.76 → 1591.40] And it's a pretty narrow set of use cases.
[1591.60 → 1596.58] But if you're not indexing and querying into that, if you want to just save logs, right?
[1596.62 → 1598.02] If you've got logs coming in.
[1598.02 → 1602.88] Or if you want to say, like, you've got an API that's accepting and ingesting stuff.
[1603.06 → 1604.56] And you want to save the exact format.
[1604.80 → 1606.04] You're not querying that all the time.
[1606.12 → 1606.98] You just want to really quick.
[1607.40 → 1610.74] It's going to be a little bit faster because it doesn't have to go and compress it to a binary format.
[1610.98 → 1611.30] Right.
[1611.66 → 1613.72] If you care about preserving the white space.
[1614.10 → 1617.26] Like, logging and API logs are huge for this.
[1617.30 → 1620.34] Like, I just want to save them and I want to replay them exactly as they were.
[1620.86 → 1624.02] If you want to go and replay your API logs, just throw them in JSON.
[1624.32 → 1626.88] So, it's really fast, efficient.
[1626.88 → 1628.16] There's no extra processing.
[1628.46 → 1630.56] If you're not querying at a time, JSON is useful.
[1631.04 → 1636.28] But most of the time, you've got a, you know, key you want to index and query into.
[1636.72 → 1637.98] You do want JSON.
[1638.60 → 1640.92] JSON comes with all the extra perks.
[1641.44 → 1644.44] So, with JSON, you can index, like, a very specific key.
[1645.02 → 1651.20] With JSON, you can put a gen index on and index all the keys and columns kind of within that JSON document.
[1651.32 → 1655.16] So, then when you go and query it, it's going to be really, really fast like your other index tables.
[1655.16 → 1659.22] So, JSON is usually what you want when you're developing in most cases.
[1659.22 → 1659.40] Gotcha.
[1659.76 → 1663.34] Maybe real quick, do a quick, when should I use JSON in general?
[1663.44 → 1664.68] You mentioned extras.
[1665.14 → 1669.32] It makes total sense if you're splatting logs into a thing or API responses.
[1669.56 → 1672.48] Like, just take the API response and store it as JSON.
[1672.48 → 1674.18] So, you're going to store it as the type of JSON.
[1675.12 → 1678.36] There's a balance of when it's, like, smart to actually use this.
[1678.46 → 1680.36] And when, nah, you actually needed a separate table there.
[1680.42 → 1682.92] But you denormalized when you shouldn't have.
[1682.94 → 1684.00] And now you're going to have problems.
[1684.42 → 1685.80] Usually data consistency problems.
[1686.40 → 1687.24] What's your heuristics?
[1687.38 → 1689.38] Like, when does JSON be a good idea?
[1689.82 → 1690.84] And when is it not a good idea?
[1691.40 → 1691.60] Yeah.
[1691.78 → 1697.80] So, I mean, there's, it dives a little bit into, like, relational versus no SQL, right?
[1697.80 → 1700.58] Like, I think it's worth a quick detour there.
[1700.72 → 1703.98] It's, like, you always have a schema no matter what.
[1704.26 → 1707.28] You're just, like, maintaining that in the database, or you're maintaining that in code.
[1707.76 → 1711.88] Like, if your application expects something to be there, now you're building an if statement to say,
[1711.96 → 1713.76] if this is there, otherwise do this, right?
[1713.82 → 1715.14] Or write out a default value.
[1715.50 → 1715.70] Yeah.
[1715.76 → 1718.86] Whereas when you add a column in Postgres, you're adding a default value.
[1719.44 → 1723.44] There are a number of things that, hey, if you don't rely on that being there, great.
[1723.44 → 1727.90] In a schema, there's really usually some things that always exist.
[1728.04 → 1730.72] Like, hey, you've got a user's table and there's, like, a username and a password.
[1731.32 → 1732.54] That's always going to exist.
[1732.68 → 1734.48] You've got some really basic fields.
[1735.26 → 1742.56] And what I tend to do is, like, oh, if it's a temporary use thing or if it's, like, a tags thing or this is kind of extra.
[1742.68 → 1744.02] So it doesn't exist on every model.
[1744.08 → 1751.60] Instead of creating a whole other table, for us, we run a database as a service that exists on top of AWS and Azure.
[1751.60 → 1755.26] And some things we need for AWS, some things we need for Azure.
[1755.58 → 1758.16] We could create completely separate tables for those servers.
[1758.58 → 1761.88] Or I could just say, oh, this extra field I need only for Azure is over here.
[1762.44 → 1765.22] So it's kind of when it's, you know, optional extra fields.
[1765.46 → 1765.56] Right.
[1766.34 → 1769.10] It's a really, really common case that I see quite a bit.
[1769.56 → 1771.08] That's kind of that extras' category.
[1771.42 → 1771.74] Right.
[1772.26 → 1773.64] I use it for settings a lot.
[1773.88 → 1776.32] So, for instance, notification settings on a user.
[1776.32 → 1779.08] Like, here are a bunch of emails we may or may not send.
[1779.24 → 1782.08] And these are, like, triggers for them to say whether they want those emails.
[1782.96 → 1785.04] And I don't really want to have my own table for that.
[1785.56 → 1787.92] Some users, they've never filled it out.
[1787.98 → 1788.78] It's just the defaults.
[1788.82 → 1791.78] And then every once in a while, we're going to add a new email that we want to send.
[1791.92 → 1800.88] And so it's easy to just add that in your code and not have to go through a migration process to add a new column to another table.
[1801.02 → 1802.40] So I'll just be like, well, here's a new email.
[1802.78 → 1803.78] Just throw it in code.
[1803.88 → 1804.86] And it's just flexible that way.
[1804.86 → 1808.40] Yeah, I think that's a really kind of good way to think about it.
[1808.50 → 1811.74] It's basically a lightweight table right there on that object, right?
[1812.02 → 1818.68] You've got, hey, maybe some nested data, but I kind of don't want to go two or three layers deep because now I'm basically, you know,
[1818.72 → 1823.42] now I've got to go and figure out and recompute all those dependencies and constraints and all that stuff.
[1823.58 → 1830.28] So a layer or two deep as a table kind of works really well as a heuristic of if it's light enough weight.
[1830.80 → 1834.26] I think the other piece is, you know, how are you going to do analytics on it?
[1834.26 → 1844.66] Like, this is a big one for NoSQL databases where, hey, even if you get to manage your schema, you suddenly want to ask a question and say, hey, how many users signed up in the last week?
[1844.70 → 1850.88] And now when you're like traversing down a document three layers deep, that's some, you can write that SQL, but it's pretty gnarly.
[1850.88 → 1853.04] Maybe the joints aren't going to be as efficient, that sort of thing.
[1853.14 → 1861.74] So if I'm doing lightweight filtering, like give me a user that has some Boolean of true in my JSON, that's really easy.
[1861.98 → 1869.86] But if I'm doing aggregation on some, like, give me, you know, all the users that signed up based on some data, and I'm parsing that out from JSON,
[1869.86 → 1875.36] like now I'm doing a lot more overall kind of on the SQL side, which is not where I want to be.
[1875.86 → 1878.72] A lot of applications start without analytics and add that on later.
[1879.32 → 1887.28] And this comes back to where, to me, part of the reason that Postgres won is people started building these applications and said, oh, now I need to do analytics.
[1887.46 → 1889.70] Oh, wait, that's hard on a NoSQL database.
[1889.70 → 1895.96] Like, how do I group by and aggregate and filter and all that stuff inside documents?
[1896.66 → 1897.34] Not so trivial.
[1897.84 → 1900.42] And some of those you can actually only query on indexes, right?
[1900.52 → 1903.48] Like there's nothing, you can't even write an ad hoc query in certain cases.
[1903.48 → 1907.46] Like you have to have a predefined index or something on some NoSQL databases.
[1908.36 → 1911.94] Yeah, I think they're, you know, they often start there, and they get more advanced over time.
[1912.02 → 1915.00] There's not a foundational limit that they couldn't.
[1915.00 → 1917.96] But yeah, some definitely start there and try to get more and more.
[1917.96 → 1919.98] But it's not going to be as efficient.
[1920.28 → 1923.90] I look at the roots of SQL, and it was really well-designed.
[1924.02 → 1926.24] It's relational algebra and relational calculus.
[1926.46 → 1929.70] And if you want to geek out on it, that's where I say, like, learn those things.
[1929.70 → 1932.98] And then you understand all the power of SQL, and it blows your mind.
[1933.60 → 1935.12] Most people never need to go that route.
[1935.22 → 1940.22] But to throw away all that as a foundation, you lose a lot, you know, going the other side.
[1941.48 → 1945.94] So JSON, over eight years ago, JSON a couple of years later.
[1946.04 → 1947.24] But this is like a longstanding.
[1947.24 → 1948.90] This is a thing that I now take for granted.
[1949.24 → 1950.62] So it's not like a shiny new feature.
[1950.70 → 1951.36] It's still shiny.
[1951.74 → 1952.80] It just isn't new.
[1953.02 → 1957.76] What else about Postgres that's exciting in terms of features for relational databases?
[1958.76 → 1964.12] So I think I look and, you know, Postgres just moves forward each year with something new.
[1964.76 → 1966.80] JSON, JSON are the shiny ones.
[1967.34 → 1971.04] There's, I can go back and probably each release and there's some interesting new thing.
[1971.04 → 1973.68] One big area for me is indexing.
[1975.06 → 1977.08] Most databases have an index type.
[1977.20 → 1979.54] When you do create index, it's creating a B-tree index.
[1979.74 → 1984.86] Like if you have a CS degree, this is what you learned as, you know, the basics of a B-tree.
[1986.26 → 1987.66] Postgres has had that for a while.
[1987.66 → 1991.32] And it's also getting more exotic with its indexes.
[1991.82 → 2003.08] So, you know, with JSON, when you index it, you use a GIN index, a generalized inverted index, which flips it on its head and basically indexes every key and value inside that JSON document.
[2003.74 → 2007.62] So fascinating that I don't have to say index this column or this little piece.
[2008.04 → 2009.28] It indexes everything for me.
[2009.32 → 2010.50] So when I query it, it's fast.
[2012.26 → 2014.82] Postgres has five different index types.
[2015.30 → 2027.04] For a long time, you know, I would read the docs and look, and I finally got, you know, I just kind of like got over my humility and asked like the core engineers, like, can you actually explain to this to me in plain English?
[2027.20 → 2030.94] Like English, I read the docs, and I'm like, I don't, I don't get it.
[2030.94 → 2031.10] Right.
[2031.46 → 2031.60] Yeah.
[2031.60 → 2040.42] And so you've got GIN, which is really useful when you've got multiple values inside the same column.
[2040.84 → 2046.34] So if you think about that, right, like JSON, you've got multiple keys and values, you've got arrays, that sort of thing.
[2046.52 → 2046.64] Right.
[2047.66 → 2049.32] Postgres has an array data type.
[2049.72 → 2050.76] That's super handy.
[2050.88 → 2054.84] If you're doing something with like tagging your categories, it's wonderful.
[2054.98 → 2058.54] Like, please don't go build a whole categories table and join against it.
[2058.86 → 2059.50] You don't need it.
[2059.50 → 2060.78] Just go ahead and use the array type.
[2060.78 → 2061.26] Okay.
[2061.44 → 2065.48] So GIN, really useful on arrays, JSON, this sort of things.
[2065.54 → 2068.38] You've got a GIST index, a generalized search tree.
[2068.96 → 2069.94] This is useful.
[2070.10 → 2075.92] The way I best describe it is when you think about you've got records that overlap values between rows.
[2075.92 → 2086.54] So if you think about like full text search, so you've got like a sentence and like, maybe you want to index on like the dog, but not the, right?
[2086.58 → 2091.28] So like you need both parts and hey, the may appear in a bunch of other places, but it's not going to be in the index.
[2091.28 → 2094.84] So you've got parts of the values that span across rows.
[2094.84 → 2099.08] Geospatial is another one where GIST is really useful.
[2099.22 → 2102.80] So if you've got like polygons, like how do you find the dot within the polygon, right?
[2102.90 → 2106.28] So it's useful for things that can kind of overlap in that sense.
[2107.00 → 2110.54] You've got SPG IST, space partition GIST.
[2110.54 → 2113.74] SPG IST I only know is useful for phone numbers.
[2114.20 → 2116.92] I keep asking, give me other examples.
[2117.22 → 2119.36] And they're like, uh, phone numbers.
[2119.46 → 2119.82] That's when.
[2120.30 → 2120.76] Why phone numbers?
[2120.84 → 2121.92] What's unique about phone numbers?
[2122.22 → 2124.72] It's something about how like things naturally cluster together.
[2124.82 → 2132.60] So if you think about like area code, then some three number prefix, like, hey, this clusters together, this clusters together, then this is kind of the unique part.
[2132.72 → 2137.06] So like there's kind of distinct blocked groupings of values there.
[2137.06 → 2137.50] Hmm.
[2138.14 → 2146.90] So maybe zip codes might be another one because this kind of have, you have a certain area we'll have, they'll start with the first two letter or numbers and a zip code.
[2146.90 → 2148.90] And then the last real be different or something like that.
[2149.08 → 2149.36] Yeah.
[2149.46 → 2153.78] That's a, I'm going to ask one of the core developers next time I see them, if that's it, that's a.
[2153.78 → 2154.70] Add that to your list.
[2154.72 → 2155.26] Equal use case.
[2155.34 → 2155.50] Yeah.
[2156.10 → 2158.40] But yeah, typically really, really large data sets.
[2158.40 → 2166.32] You also got brand indexes, block range, which is really similar where you've got, you know, billions and billions and billions of records.
[2166.32 → 2168.10] It's some that naturally cluster together.
[2168.74 → 2170.40] Those are definitely a little more specialized.
[2170.74 → 2173.66] So like, if you think about it, you're using JSON in arrays.
[2174.38 → 2175.44] You want to use a gen index.
[2175.62 → 2179.20] If you're using geospatial stuff or full text search, you want to use a gist.
[2179.88 → 2184.54] If you have no clue, you know, a B tree just created index is kind of for a single column.
[2184.76 → 2189.16] But it's interesting that each one of this kind of comes in, you know, a new year.
[2189.16 → 2193.04] Like for a little while there, I think three years in a row, we had a new index type every year in Postgres.
[2193.82 → 2196.22] And it just marches forward.
[2196.88 → 2200.88] A lot of this has come out of a group that we, you know, within the community called the Russians.
[2201.04 → 2210.10] There's a professor from University of Moscow that I'm not sure if he still teaches or used to teach on like astrophysics and then like hacks on Postgres for fun.
[2210.10 → 2216.66] Like we have different definitions of fun, but he'll show up with some like, hey, I read this research paper.
[2216.78 → 2217.76] I wrote this research paper.
[2217.84 → 2218.72] What do you think about this?
[2218.76 → 2223.42] And for a little while there, it was kind of like, well, this is an absolutely crazy idea.
[2223.54 → 2226.62] Like Postgres is stable and solid, and we don't do these crazy things.
[2226.62 → 2230.42] And he'd show up with a patch on the mailing list and do the back and forth in debate.
[2230.48 → 2232.06] And it's like, here's the performance.
[2232.24 → 2233.68] Here are the characteristics of it.
[2233.74 → 2235.84] It's, you know, OK, great.
[2235.90 → 2236.50] You'll maintain it.
[2236.52 → 2237.14] You'll support it.
[2237.30 → 2237.84] Here it is.
[2237.84 → 2241.62] You know, there's I think right now he is Russian.
[2242.14 → 2243.10] He says we have gin.
[2243.22 → 2245.16] He's working on a type called vodka right now.
[2245.28 → 2246.40] He says, you know, we need that.
[2246.72 → 2249.24] I hope that's just the working name.
[2249.30 → 2250.46] I'm not sure if that's true or not.
[2250.62 → 2250.80] Yeah.
[2250.98 → 2252.58] But yeah, it just keeps moving forward.
[2252.64 → 2252.82] Right.
[2252.90 → 2260.76] Indexing is one of those things that as a developer, I don't go in like my checklist of features when I'm evaluating a database.
[2260.76 → 2262.94] Like how many indexes do you have?
[2263.60 → 2267.18] And yet when I need it, it's its there.
[2267.84 → 2270.72] Really, there's just so much in the box for Postgres.
[2271.38 → 2273.70] Some of it I have absolutely no experience with.
[2273.96 → 2274.02] Yeah.
[2274.08 → 2276.18] PostGIS is one huge area.
[2276.58 → 2278.00] Is that a third party thing, though?
[2278.06 → 2280.54] Or it's like it's maintained as its own separate?
[2280.62 → 2281.92] Because I have used it one time.
[2282.02 → 2282.96] It's been years now.
[2283.04 → 2288.36] And I remember I had to install it as an extension and maintain its upgrade cycle was different from Postgres's.
[2288.36 → 2292.76] And there was some pain there where like upgrading one, not upgrading the other.
[2292.76 → 2295.16] Or I remember being like, oh, this is a little bit.
[2295.56 → 2299.72] So it's like it's like an extension of Postgres or is it?
[2299.72 → 2299.94] Yeah.
[2300.02 → 2300.86] So it's an extension.
[2300.86 → 2303.98] And I think we'll probably get to this in a little bit.
[2304.26 → 2306.42] Like extensions are a whole fascinating area.
[2306.58 → 2306.74] Yeah.
[2306.86 → 2310.10] PostGIS being one of the largest, biggest ones.
[2310.10 → 2312.16] Like I'm not a geospatial developer at all.
[2312.68 → 2314.68] In some sense, there's a completely parallel community.
[2315.00 → 2319.68] Like there's a PostGIS set of committers and a PostGIS core team.
[2320.30 → 2322.44] And they collaborate.
[2322.62 → 2323.52] They're at the same conferences.
[2324.02 → 2327.82] But some of the things they do are completely separate from core.
[2328.12 → 2328.26] Right.
[2328.68 → 2331.90] And so I think there were a couple of rough years there.
[2332.06 → 2339.52] I think it was upgrading to PostGIS 2.5, or it was 2.5 to 3 that it was a really it was the dark time.
[2339.52 → 2340.40] I think you drilled it.
[2340.46 → 2342.32] I think those are actually the version numbers I was on.
[2342.54 → 2342.76] Yeah.
[2343.16 → 2345.98] I think I had words with some of the PostGIS committers then.
[2346.82 → 2354.10] And they understand, I think, the world of how many developers are using it now and what the upgrade process is.
[2354.24 → 2357.28] And I don't think we're ever going to see that again, hopefully, knock on wood.
[2357.86 → 2365.82] It's one of those situations where I had enough competence and confidence in Postgres maintenance and administration that it didn't worry me.
[2365.82 → 2368.88] But when I pulled the PostGIS stuff in, it worked great.
[2368.88 → 2369.92] And I was using it.
[2370.16 → 2375.08] But maintaining it over time because I wasn't actively working and doing that.
[2375.16 → 2377.00] It was just this thing that I also had to do.
[2377.44 → 2379.84] When I upgraded Postgres, I would run into issues.
[2379.94 → 2383.68] And I wouldn't know how to solve them because it was this third leg kind of thing.
[2383.96 → 2385.24] It was definitely a rough one.
[2385.32 → 2387.70] And I think you've got a range of indexes.
[2387.78 → 2389.70] And some things are core in Postgres.
[2389.84 → 2390.70] Some things are extensions.
[2391.36 → 2393.78] You've got really lightweight extensions that are a little safer.
[2394.20 → 2396.18] PostGIS is a huge one.
[2396.18 → 2397.72] It's a whole geospatial database.
[2398.34 → 2403.02] Like, it passes up functionality that, like, Oracle geospatial doesn't have.
[2403.28 → 2406.48] Like, an open source thing is better than Oracle at something.
[2406.66 → 2408.02] And that's geospatial for sure.
[2408.16 → 2409.94] Like, that's not disputed at all.
[2410.18 → 2415.66] It has new data types, new operators and functions and all sorts of things in there.
[2415.66 → 2419.76] So, it's definitely a massive one that kind of has its own path.
[2419.98 → 2424.06] But I think if you look, there are other things that are more in core.
[2424.18 → 2425.66] You've got, like, full-text search.
[2426.26 → 2428.98] I think it was a couple of years ago I saw someone write a blog post.
[2429.38 → 2431.74] That was, like, a deep dive on full-text search.
[2432.12 → 2436.50] And the title was something like, Postgres full-text search is good enough.
[2436.76 → 2437.86] Like, it works.
[2438.00 → 2438.64] Like, it's fine.
[2438.72 → 2439.32] I installed it.
[2439.34 → 2439.84] It works.
[2439.84 → 2442.10] And it was a wonderful post.
[2442.32 → 2449.40] And people were like, yeah, why do I need Elastic or whatever else when I can just try this and see if it works?
[2449.64 → 2453.42] And you can kind of replace full-text search with almost anything in Postgres.
[2453.64 → 2456.44] Like, Postgres geospatial is good enough.
[2456.94 → 2464.68] One of my favourite small ones that you shouldn't use all the time, but listen, notify, is pub sub directly inside Postgres.
[2465.34 → 2469.30] Like, if you want to use Postgres for a queue, you can do that.
[2469.30 → 2475.42] Yeah, I've seen that done, and it's really cool because you don't expand your maintenance surface area at all.
[2475.52 → 2479.38] I know we're in the world of serverless and all these things, so nobody has to maintain servers and stuff.
[2479.94 → 2485.82] But if you have to have a Regis instance somewhere in your stack, you're either paying somebody to maintain it or you've built that into your infrastructure.
[2486.46 → 2492.80] And a lot of times when people go to queue background jobs, they have to pull in some other thing, whether it's Regis or people use Teacake for that.
[2492.86 → 2493.24] Probably not.
[2493.32 → 2494.48] But there are queue things.
[2494.64 → 2495.44] Celery, I don't know.
[2496.64 → 2498.52] Beanstalk, there are words that come to my mind.
[2498.52 → 2502.64] But anyway, if you can do it right in Postgres, like, you're already backing that up.
[2502.70 → 2504.50] Like, it's there with everything else.
[2504.56 → 2506.76] There's not another, you know, cog in your wheel.
[2507.42 → 2508.20] That's pretty cool.
[2508.32 → 2510.98] And I've seen people use that to do background jobs.
[2511.82 → 2515.58] Yeah, and like you say, it's one more thing I don't have to deploy and manage.
[2515.72 → 2516.80] Like, that's as strong as anything.
[2516.80 → 2527.82] Like, even if this thing is 10%, 20%, even if it's 2x better, Postgres is just this kind of stable workhorse that gets a new feature every so often that, oh, I can do that.
[2527.92 → 2528.66] And I can do that.
[2528.82 → 2529.52] And I can do that.
[2530.18 → 2533.44] Postgres 13 just came out, you know, a few weeks back.
[2533.44 → 2537.10] And it kind of epitomizes Postgres to me.
[2537.28 → 2541.06] Like, there's not, of all releases, I think there's not a shiny new feature.
[2541.18 → 2542.98] It's kind of like upgrade, and it's just better.
[2543.46 → 2547.82] Like, it's like you get space savings from B3 indexes.
[2547.92 → 2551.54] If you were using, you know, partitioning before, it's just better now.
[2551.54 → 2555.86] Now you can have, like, better constraints between your partition tables.
[2556.20 → 2558.62] And, you know, joins are more efficient.
[2559.28 → 2563.38] It's like more and more, I think, like Postgres itself.
[2563.52 → 2569.94] Like, we've kind of reached the point where it's got, I'm more of a Python guy than I am a Ruby guy.
[2570.16 → 2573.30] And I really loved the Django model for a long time, batteries included.
[2573.74 → 2575.88] It was kind of everything you needed to run a web app.
[2576.06 → 2581.16] Like, cool, here's authentication, here's caching, here's all these things that I normally have to go grab off a shelf
[2581.16 → 2582.34] when I'm building a web app.
[2582.54 → 2584.16] And Postgres is kind of that for databases.
[2584.30 → 2585.22] It's like batteries included.
[2585.50 → 2586.28] Here's all the things.
[2586.40 → 2587.18] Here's your data types.
[2587.46 → 2588.90] Here's your extra indexes.
[2589.00 → 2589.80] Here's your Pub Sub.
[2589.94 → 2590.90] Here's you're geospatial.
[2591.12 → 2592.68] Here's your queue functionality.
[2593.10 → 2594.44] Here is all that.
[2594.52 → 2596.36] And it's like, cool, we've checked all those boxes.
[2596.36 → 2602.30] Now let's just keep making it stable, a little new feature here and there, more polished, easier to use.
[2602.62 → 2604.02] And a big one's always faster, right?
[2611.16 → 2620.60] What's up, friends?
[2620.66 → 2623.18] Have you ever seen a problem and thought to yourself, I bet I could do that better.
[2623.48 → 2624.78] Our friends at Equinix agree.
[2625.16 → 2631.12] Equinix is the world's digital infrastructure company, and they've been connecting and powering the digital world for over 20 years now.
[2631.34 → 2633.82] They just launched a new product called Equinix Metal.
[2634.12 → 2638.64] It's built from the ground up to empower developers with low latency, high performance infrastructure anywhere.
[2638.64 → 2640.88] We'd love for you to try it out and give them your feedback.
[2641.20 → 2647.00] Visit info.equinixmetal.com slash changelog to get $500 in free credit to play with, plus a rad t-shirt.
[2647.48 → 2651.68] Again, info.equinixmetal.com slash changelog to get $500 in free credit.
[2652.06 → 2653.44] Equinix Metal, built freely.
[2668.64 → 2676.14] As I kind of take a step back, I think more and more is going to happen in extensions.
[2676.42 → 2677.86] Like, PostGIS is a big one.
[2678.48 → 2683.86] There's roughly, I think, 250 extensions that exist on one of the kinds of extension networks.
[2684.70 → 2685.58] Extensions are unique.
[2685.94 → 2688.36] They're low-level hooks deep into Postgres.
[2688.36 → 2694.50] I kind of hate the term extensions because you think, like, every database and tool and library has, like, extensions, right?
[2694.58 → 2696.86] Like, they're, like, extensions in air quotes.
[2697.00 → 2700.08] It's like a plug-in layer that you can just throw something on top.
[2700.68 → 2702.64] But this is, like, deep, low-level C hooks.
[2702.72 → 2704.40] Like, you can write an extension in SQL.
[2705.02 → 2706.92] You can write an extension in C.
[2707.12 → 2709.54] You can write an extension in other languages.
[2710.18 → 2713.94] And you can completely change the underlying behaviour of what Postgres can do.
[2714.02 → 2715.22] You can have new data types.
[2715.22 → 2717.34] You can have new functions and access methods.
[2717.92 → 2719.62] And it can move at a separate pace from Core.
[2720.42 → 2723.60] Core can still have that same mantra of, like, I'm not going to lose data.
[2724.02 → 2724.80] I'm going to be safe.
[2725.24 → 2726.02] I'm going to be reliable.
[2726.46 → 2729.72] They can maintain that C code base at a really high quality.
[2730.50 → 2735.36] And now we've got this world where something can happen in an extension, improve over time.
[2735.60 → 2738.98] And the Core community can sit there and say, like, well, this is really solid.
[2739.12 → 2739.80] Everyone needs this.
[2739.86 → 2740.56] Let's put it in Core.
[2740.68 → 2741.12] Pull it in.
[2741.24 → 2741.38] Yeah.
[2741.38 → 2751.66] So, to me, I think as we, you know, I start to look at the landscape of Postgres and what's the future, extensions are absolutely huge.
[2752.02 → 2754.40] And what you can do with them is kind of unbelievable.
[2755.16 → 2759.18] Can you give some more examples of extensions in addition to Postgres?
[2759.26 → 2761.78] I know there was one called Store, which I remember using.
[2761.78 → 2770.28] But what are some other things that people have built in the community that you can pull in and use that extend, for lack of a better term, Postgres?
[2770.48 → 2770.60] Yeah.
[2771.18 → 2771.52] Yeah.
[2771.64 → 2771.76] Yeah.
[2771.88 → 2772.06] Right.
[2772.12 → 2774.56] It's, it makes sense.
[2774.80 → 2779.64] And I think it's, you know, the term, it kills me because it's like, hey, what extends it?
[2779.90 → 2782.92] But it does it uniquely that that's the part that hangs me up.
[2783.18 → 2783.34] Right.
[2783.46 → 2784.10] There's a bunch.
[2784.10 → 2791.12] One of my previous employers, Cites Data, turned Postgres into a sharded, distributed, horizontally scalable database.
[2791.80 → 2796.22] So, when you were at 100 terabytes of data, hey, that doesn't fit easily on a single node.
[2796.34 → 2797.08] How do you get performance?
[2797.88 → 2799.24] Under the cover, everything was sharded.
[2799.56 → 2802.08] It still looked like a single node database.
[2802.52 → 2807.02] But, you know, to your application, you didn't have to think about sharding, right?
[2807.26 → 2810.22] You don't have to go hire the experts like Instagram did.
[2810.22 → 2816.94] You can just work with it in your, you know, your Rails, your node app, and just pretend it's a single node database.
[2817.66 → 2819.26] PostGIS is obviously a big one.
[2819.56 → 2820.60] There's really simple ones.
[2820.88 → 2825.98] You know, one of my colleagues at Crunchy Data, he's on the like, the core for PostGIS.
[2826.80 → 2830.02] But he wrote one that's, like, just HTTP Git, basically.
[2830.24 → 2831.90] Like, I want to go and curl this website.
[2832.38 → 2832.48] Huh.
[2832.98 → 2834.08] There's patron.
[2834.18 → 2837.96] So, if you think about this, right, you've got patron, which is iron in your database.
[2837.96 → 2840.50] You could go and then curl something.
[2841.30 → 2843.70] And then you could go and, like, parse that website.
[2843.86 → 2850.04] You could do screen scraping automatically inside your database without ever having to run, like, a separate scheduler web process.
[2850.44 → 2852.66] You've got different procedural languages.
[2852.88 → 2856.26] You've got, like, plv8, which is v8 directly inside Postgres.
[2856.86 → 2860.34] So, that's an extension that you can run JavaScript inside your database.
[2860.62 → 2861.44] Okay, it's getting crazy.
[2862.04 → 2863.40] So, how would you trigger that then?
[2863.46 → 2865.40] Well, let's go back to the iron one.
[2865.62 → 2867.56] Like, do you use a select or something?
[2867.56 → 2869.48] Like, how do you actually interact with these things?
[2869.56 → 2874.54] Is it using the query language, standard SQL query language, or extensions as for that?
[2875.02 → 2878.40] Yeah, so, the basics is you just run create extension, right?
[2878.42 → 2880.42] You've got to have it built, and they're available on your system.
[2880.50 → 2882.18] Then you run create extension, and it's available.
[2882.42 → 2884.66] Depending on what it does, it's going to enable something new.
[2884.80 → 2885.80] So, store is a great one.
[2886.28 → 2887.18] store is a data type.
[2887.24 → 2888.68] So, you run create extension store.
[2889.32 → 2890.74] And now you have this new data type.
[2890.82 → 2893.24] So, now when you're creating tables, you use the store data type.
[2893.42 → 2893.72] Right.
[2893.72 → 2896.90] And store is a key value store directly in Postgres.
[2897.00 → 2898.82] So, it was kind of the precursor of JSON, right?
[2898.90 → 2903.62] I think that's when I used it was back before either JSON didn't exist or I didn't know it was in there.
[2903.82 → 2904.70] So, I used store.
[2905.02 → 2905.88] Similar fashions.
[2906.00 → 2908.42] It wasn't as nice because there was all these little edge cases with it.
[2908.70 → 2909.06] Yeah.
[2909.28 → 2912.98] So, it's, you know, and I think it proved the point of like, hey, why don't you use store?
[2913.14 → 2913.38] Yeah.
[2913.70 → 2915.94] Maybe we need something more official in JSON, right?
[2916.52 → 2920.36] JSON went directly into core because of how the community saw that being used.
[2920.36 → 2923.42] Just, Mad lib is one that's out of UC Berkeley.
[2924.06 → 2925.64] It's a whole analytics package.
[2926.14 → 2930.20] Like, when people talk about data science, like, cool, I'm going to go and do something in Spark.
[2930.40 → 2935.78] Like, I'm kind of going to pick up Mad lib because it has like supervised learning, unsupervised learning.
[2935.92 → 2939.24] Like, you want to like look at K-median, you know, run a regression.
[2939.76 → 2940.82] It's right there.
[2940.86 → 2943.84] And it's been maintained for north of 10 years now.
[2943.84 → 2944.60] It's ancient.
[2944.68 → 2949.12] And we just had the ability to do all this data science directly in Postgres for a long time now.
[2949.12 → 2952.36] Now, when you enable it, you get whole new functions, right?
[2952.44 → 2956.26] And you basically execute these functions and pass in the right things, and you get something back.
[2957.62 → 2963.68] Something like a PLV8, which I'm becoming a bigger and bigger fan of PLPython.
[2964.30 → 2969.30] To me, this, like, you mentioned like, hey, things are getting crazy when we've got JavaScript in our database.
[2969.46 → 2969.84] Yeah, right.
[2969.84 → 2975.04] For a long time, we had this idea of like, no, no, never put application logic in your database, right?
[2975.12 → 2978.42] Like, the database is this dumb store.
[2978.84 → 2980.06] Think, you know, PHH.
[2980.40 → 2980.68] Put it in.
[2981.02 → 2981.12] Yeah.
[2981.68 → 2983.26] A big hash in the sky.
[2983.44 → 2985.90] And I'm like, no, it's useful.
[2986.04 → 2987.98] It has all the data, and you can do interesting things.
[2988.12 → 2993.46] So, like, PLPython, a couple of weeks ago before we launched our product, I was like, what can I do with this?
[2993.46 → 2997.02] And I just started poking, and I installed SciPy, NumPy, and Pandas.
[2997.54 → 2998.60] And I started live tweeting.
[2998.72 → 3001.30] I probably shouldn't have because it could have gone horribly wrong, right?
[3001.38 → 3002.96] Like, I'm going to see what I can do.
[3003.06 → 3004.84] And then, you know, two hours later, there's like crickets.
[3005.38 → 3012.62] But no, I actually was able to in about 20 lines of Python, which I basically wrote a function that executes Python inside my Postgres database.
[3012.76 → 3013.06] Okay.
[3014.00 → 3014.94] Imports Pandas.
[3015.26 → 3017.66] I pass in some records to it.
[3017.82 → 3022.26] And I pass in like a history of orders and what's in a shopping cart.
[3022.26 → 3026.38] And it's basically a recommendation engine of you should recommend these products to this person.
[3027.38 → 3029.30] 20 lines of Python directly in my database.
[3029.68 → 3041.24] I didn't have to go and spin up a Kafka queue to get the data out of Postgres into Spark to run some model to feedback in to Regis to then, you know, show this to the user.
[3041.66 → 3045.94] Literally 20 lines of Python directly in my database to have a recommendation engine for products.
[3047.80 → 3051.74] And it breaks the mould, I think, of what we've been thinking for the past five or ten years.
[3052.26 → 3062.52] But if I look at it from a practical standpoint, like this gospel of never put logic into your database, like the large enterprises have been doing this for years and years and years.
[3062.52 → 3069.30] If you look at things like Oracle and SAP applications, they're almost nothing but huge procedural, you know, code.
[3069.30 → 3078.00] And with Postgres, now that we can do it in things like JavaScript with PLV8 and Python, it can be more native to an app developer.
[3078.56 → 3080.26] So I'm kind of weird.
[3080.34 → 3081.52] I kind of enjoy writing SQL.
[3082.22 → 3084.38] I ask a lot of people who enjoys writing SQL.
[3084.56 → 3086.50] And, you know, if there's 100 people, there's like three hands.
[3087.18 → 3092.38] But I have asked to people like, well, do you enjoy writing other people or reading other people's SQL?
[3092.72 → 3094.24] And there's never like a hand that goes up.
[3094.78 → 3094.96] Yeah.
[3095.16 → 3095.44] No.
[3095.44 → 3098.54] It's not a pretty language and someone else writes it.
[3098.62 → 3099.72] It's probably not well formatted.
[3099.84 → 3100.90] Like it gets the job done.
[3101.34 → 3107.20] But if I can write Python to do the same thing or JavaScript, how do you feel about that?
[3107.86 → 3110.54] Yeah, I think that's more legible to more people.
[3110.98 → 3112.32] How do you maintain that?
[3112.36 → 3114.56] And like, where does that live in the software system?
[3115.06 → 3116.88] Basically, it's like a create function call.
[3116.98 → 3118.66] So you run a create function here.
[3118.76 → 3119.84] You define your function directly.
[3120.24 → 3122.20] Then you can execute that within the database.
[3122.20 → 3122.56] Right.
[3122.64 → 3127.60] So I've defined my function, and then I can just do select, get recommendations for my recommendation engine.
[3128.10 → 3133.28] So a lot of extensions come, and basically they packaged up all of these functions for you in that C format.
[3133.62 → 3133.98] Yeah.
[3134.04 → 3135.40] Like Mad lib does all this.
[3135.46 → 3137.84] So now all you've got to do is go through and say, what's the function?
[3137.96 → 3139.32] What's my inputs and what do I get out?
[3139.98 → 3142.20] But if you want to write your own, you absolutely can.
[3142.30 → 3149.14] You can go down that deep path of creating an extension or writing your own functions and deploying, you know, just like you would other schema stuff.
[3149.14 → 3149.54] Yeah.
[3149.54 → 3149.86] Yeah.
[3149.96 → 3153.26] Let's say, let's just get real practical with this Python example.
[3153.36 → 3159.58] Maybe if you have the code, or you have the tweets or something, you can provide links to somewhere where people can look at what you exactly you did.
[3159.62 → 3160.34] Because it's fascinating.
[3160.88 → 3163.52] Are you just storing that in its own Python file?
[3163.62 → 3165.88] You're actually, you're writing the Python inside a function.
[3166.00 → 3169.92] So this is like an SQL file that you're piping into the system via PSQL?
[3170.58 → 3171.16] Is that how you get it in there?
[3171.16 → 3172.90] Yeah, I'm just connecting via PSQL.
[3172.90 → 3177.78] And I'm just like, so a few PSQL tips, right?
[3177.86 → 3179.96] So I'm a CLI guy.
[3180.36 → 3181.48] I think a lot of developers are.
[3181.92 → 3183.60] PSQL is really great and powerful.
[3184.38 → 3187.50] I don't like, you know, like you're in there for the first time, and you're just kind of typing.
[3187.78 → 3196.14] Like a big tip is if you set your editor environment variable, just like the, you know, pound kind of editor.
[3196.14 → 3198.96] And you do backslash E, that'll open up your default editor.
[3199.58 → 3207.48] So like if you want to edit your queries in Vim or Tmux or Emacs or whatever, just set that and then do backslash E.
[3207.60 → 3210.08] Now you can kind of work as native as possible.
[3210.44 → 3211.54] It can be sublime text either.
[3212.00 → 3212.34] TIL.
[3212.62 → 3213.76] I've been using PSQL for years.
[3213.82 → 3215.08] I did not know that until just now.
[3215.72 → 3216.48] You just taught me something.
[3217.06 → 3218.18] There's a bunch of things.
[3218.70 → 3223.00] Backslash timing will automatically show how long it took to run a time query.
[3223.00 → 3229.88] I'll give a link as well to like, here's how to customize your PSQL editor.
[3230.62 → 3234.68] You probably have like a bash profile set up or a bash RC.
[3235.22 → 3239.32] You can set up a PSQL RC that I'll customize all this for you.
[3240.28 → 3250.30] A friend just set his null character value so that when you have nulls in your database, he set it to the poop emoji so that you know it's a null.
[3250.40 → 3251.46] It's not an empty string.
[3251.54 → 3252.66] It's actually a null in your database.
[3252.66 → 3253.06] Right.
[3253.90 → 3255.84] I have picked up a few things over the years.
[3256.08 → 3258.30] That backslash E I've never picked up.
[3258.38 → 3260.78] I'm reading my PSQL RC right now.
[3261.04 → 3262.70] And I have like the slash timing on.
[3262.88 → 3265.30] I have the SET null, but I just have like the word null.
[3265.42 → 3267.16] I need to replace that with poop emoji for sure.
[3267.64 → 3268.52] A couple other things.
[3268.60 → 3269.54] Then it unsets quiet.
[3269.70 → 3270.44] I don't know what it's doing.
[3270.56 → 3272.94] Oh, it starts with quiet, does some stuff, unsets quiet.
[3273.30 → 3274.44] I think that's to set up the prompt.
[3274.44 → 3279.40] So yeah, definitely link that up because we love to trick out our environments.
[3279.40 → 3283.94] And if you can be more productive inside your PSQL, then why not, right?
[3284.94 → 3285.18] Yeah.
[3285.50 → 3286.78] Mine's back to Vim right now.
[3286.78 → 3292.20] But like for the longest time, it was actually like sublime text, which people are like, wait, how are you doing that?
[3292.24 → 3294.58] And it's executing inside PSQL.
[3294.58 → 3297.22] So it pops open your sublime text in a new window.
[3297.36 → 3300.48] And then when you save that, somehow it pipes it back into your command line.
[3300.62 → 3302.92] And it's executing whatever you save.
[3303.10 → 3309.14] Like you can basically, you know, in Vim, I can quit, not save, or I can, you know, write and quit.
[3309.44 → 3311.42] And if I write and quit, it's going to execute that.
[3311.60 → 3311.94] It executes.
[3312.40 → 3312.90] That's cool.
[3313.32 → 3315.10] And so that's what I was doing with the Python.
[3315.20 → 3318.04] I was basically, you know, building it up a few lines at a time.
[3318.14 → 3320.02] And it was created or replace function.
[3320.36 → 3321.28] I've got my inputs.
[3321.28 → 3325.38] I started with just a couple of inputs and saying, okay, now I'm going to import Pandas.
[3325.84 → 3327.70] Like did that error for me or did that work?
[3328.02 → 3331.58] Now I'm going to see, can I, you know, parse this into a data frame?
[3332.04 → 3333.30] Nope, I didn't parse it right.
[3333.40 → 3340.02] Okay, how do I get from a set of arrays in Postgres and transcribe that into what Python wants for a data frame?
[3340.52 → 3346.78] So it was definitely, you know, a couple of hours of debugging, but probably not much longer than like,
[3347.32 → 3350.40] I haven't written anything in Pandas in probably a year.
[3350.40 → 3354.06] So probably no longer than it would have taken me directly in Pandas.
[3354.14 → 3355.60] And I'm just kind of creating that function.
[3355.72 → 3359.38] And then I'm calling that select as soon as I create it to kind of iterate and test.
[3359.46 → 3361.10] I'm saying select, get my recommendations.
[3361.70 → 3363.96] Oh, error or did it execute and do something.
[3364.98 → 3366.02] Pretty cool stuff, man.
[3366.12 → 3366.88] Pretty cool stuff.
[3367.50 → 3369.66] So that's in present day.
[3369.76 → 3372.06] That's presently available in Postgres.
[3372.18 → 3373.38] What's the future look like then?
[3373.46 → 3376.70] Is there more like this coming or what do you think is going to happen next?
[3377.76 → 3379.64] Yeah, I fully expect a lot of this, right?
[3379.64 → 3382.12] Like you're going to see new extensions doing all sorts of things.
[3382.12 → 3385.88] You're going to see, you know, you've got time series ones like PG Part Man.
[3386.46 → 3388.46] You've got things like Cites for Sharded.
[3388.62 → 3389.38] You've got PostGIS.
[3389.66 → 3395.14] There are ones that show off that I'm like, I had no idea you could or wouldn't want to do that.
[3396.00 → 3401.34] You know, your reaction of like, this is crazy when we've got JavaScript in our databases is spot on.
[3401.72 → 3402.14] Thank you.
[3402.52 → 3403.14] I thought so.
[3403.14 → 3406.36] As you pause and think about it, why not?
[3406.84 → 3410.00] Like kind of the art of the crazy is really fun as developers, right?
[3410.10 → 3412.22] Like, yeah, we're going to see a lot more of this.
[3412.32 → 3414.00] And I, I see them.
[3414.54 → 3416.30] Combo DB is a fascinating one.
[3416.30 → 3420.14] So it'll keep your Postgres data in sync in Elasticsearch.
[3420.46 → 3425.42] And you can maintain Elasticsearch indexes and query them from directly within Postgres.
[3426.06 → 3429.02] Say that again for us slower folks like myself.
[3429.02 → 3432.52] So if you want to use Elasticsearch for your full text search, right?
[3432.64 → 3434.78] Normally you've got to pipe all that data over somehow.
[3435.48 → 3444.18] So what this is going to do is going to, as you write a record and it's a transactionally consistent record, it's going to sync it over to Elasticsearch and maintain that index.
[3444.94 → 3455.12] And now when you query this, you could go to Elastic and query it, but you've already got, you know, your, your application connected to Postgres.
[3455.36 → 3457.70] Like why not just use that index?
[3457.70 → 3462.34] So you can basically have a little like kind of reference to say, use this Elasticsearch index.
[3462.56 → 3468.90] It's automatically going to call out, use Elastic for full text search and get that back in your standard SQL Postgres query.
[3469.48 → 3470.32] I see.
[3470.58 → 3473.92] So it's like a proxy for Elastic without having to worry about it.
[3474.04 → 3478.52] Like you feel like you're just using Postgres, but it's actually proxying to Elasticsearch back, back there.
[3478.62 → 3479.02] Exactly.
[3479.30 → 3480.00] That's cool.
[3480.42 → 3484.32] And it's, I'm like, who, who thought you would like to need that?
[3484.32 → 3490.10] Like, it's like, you're still running Elastic, but like now I don't have to worry about transactional consistency and keeping things in sync.
[3490.10 → 3491.90] And how do I query this?
[3492.02 → 3493.38] There's nothing new to learn in that way.
[3493.48 → 3493.66] Yeah.
[3493.92 → 3495.14] So I think we're going to see a lot of that.
[3495.20 → 3498.18] I think we're going to see a lot of that on extensions, just continuing to advance.
[3498.72 → 3504.08] Within Postgres itself, one huge area is going to be pluggable storage.
[3504.08 → 3508.76] So a couple of years ago, Postgres got this committed into core.
[3509.14 → 3512.54] It's still early on, but basically you can have a different storage engine.
[3512.86 → 3515.46] This is going to unlock a lot in coming years.
[3515.56 → 3519.06] I think it's, will Postgres core ship with multiple storage engines?
[3519.12 → 3519.70] I don't know.
[3519.90 → 3520.74] That's a good question.
[3521.44 → 3523.14] I think probably at some point you'll have a choice.
[3523.84 → 3524.88] There's a few in development.
[3525.08 → 3530.16] I don't think we'll see hundreds and hundreds like we do extensions because it's a higher bar to write.
[3530.16 → 3536.78] Like you've got to, it's deep C code and understanding, you know, how the Postgres storage engine works and how you change it and optimize it.
[3536.84 → 3541.22] But like one of the biggest pains with Postgres that people complain about is vacuum.
[3542.12 → 3546.14] Like Postgres under the covers, what it is, it's a giant append only log.
[3546.90 → 3551.70] Like you do an update and what happens is it doesn't go and update those bytes on disk.
[3551.96 → 3555.22] It basically flags that record as dirty, then writes out a whole new record.
[3555.50 → 3557.82] So it basically, it's like a logical delete, right?
[3557.82 → 3561.44] Where if you have like a deleted at column that's hiding everything, it's kind of like that.
[3562.00 → 3568.16] Now what happens is when the system's at low load, vacuum comes in and cleans up all that.
[3568.70 → 3570.14] It says, okay, let's free up some space.
[3570.22 → 3571.18] Now let's free up some space.
[3571.56 → 3575.42] So people have this love-hate relationship with vacuum because they're like, oh man, vacuum's running.
[3575.50 → 3576.24] My system's slower.
[3576.90 → 3579.38] Well, it's actually going and deleting things that you didn't want to be there.
[3579.50 → 3583.44] So it's a good thing, but it's, there is this love-hate relationship with it.
[3583.44 → 3590.46] But there's a new backend type that aims to completely change that and like changes how the heap works.
[3590.74 → 3592.60] All sorts of things under the cover.
[3593.54 → 3596.86] Cheap is the backend that's under active development.
[3597.36 → 3605.08] Shows really promising kind of improvements around how Postgres handles vacuum, and you don't have to deal with it quite as much.
[3605.52 → 3611.48] Basically, it's some better space savings and performance on all that front, which is really, fascinating, right?
[3611.48 → 3615.94] So the idea that we didn't have to go and do a complete rewrite of Postgres and make this change for everyone.
[3616.54 → 3617.90] For some people, this is really beneficial.
[3618.10 → 3620.24] Other people, they may not need it, right?
[3620.84 → 3622.58] Zed Store is another one, which is Column.
[3623.10 → 3624.86] So that's an active development right now.
[3625.40 → 3629.14] Column data stores are, they flip things on their head.
[3629.22 → 3632.20] Instead of storing rows, they store things kind of by columns.
[3632.88 → 3633.00] Okay.
[3633.58 → 3637.04] What that means is things compress down really well.
[3637.04 → 3642.36] So if you've got things like time series data, you could imagine like, oh, I store something for an hour.
[3642.54 → 3643.74] I don't have to store a record.
[3643.86 → 3651.00] I just say at record 101, I've got like 12 o'clock and 12 o'clock goes all the way to record 2000.
[3651.38 → 3654.36] So I don't have to write 1900 records.
[3654.86 → 3657.36] I just say like right here, start right here, stop.
[3658.50 → 3661.00] And so Column is really useful in time series.
[3661.14 → 3664.76] It compresses data down really, really tightly from like a 3x to 10x.
[3664.76 → 3667.82] So you're storing less on disk, you have to scan less.
[3668.46 → 3671.08] Now Column, like all these things are trade-offs.
[3671.22 → 3672.84] Column isn't perfect for every application.
[3673.64 → 3677.50] Yeah, that sounds like a much different way of going about storage.
[3677.50 → 3682.16] It seems like it would be backwards for a lot of what Postgres normally is used to do, right?
[3682.22 → 3685.54] Like you wouldn't want to, you wouldn't be like, hey, I got my Postgres database,
[3685.68 → 3688.04] and I'm just going to like swap out some backends and see which one I like.
[3688.20 → 3692.00] I don't think the Column one is going to, for your normal use case, is going to be advantageous, right?
[3692.50 → 3692.82] Right.
[3692.92 → 3695.48] Well, I think normal is a tough question, right?
[3695.52 → 3697.56] Because it's like, that's the world you come from.
[3697.64 → 3701.12] But like Postgres is at the core of a lot of data warehousing tools.
[3701.60 → 3707.38] Postgres, because of its license, people take Postgres and kind of modify the code and change it and make a Column.
[3707.38 → 3709.34] If you look at some things like Green plum or...
[3709.34 → 3711.70] That's why I call it abnormal, because they're modifying Postgres.
[3711.92 → 3713.08] They're changing the way it works, right?
[3713.14 → 3713.68] That's abnormal.
[3713.68 → 3722.36] Yeah, I think like from a traditional Rails or Node or web application, the transactional workload, yes, right?
[3722.46 → 3728.90] Like now we're completely changing what Postgres, the bread and butter of it, but there's no reason it can't do this, right?
[3729.18 → 3733.16] And it can work this other way, but it's a really different set of trade-offs.
[3733.50 → 3735.12] And this isn't for everyone.
[3736.08 → 3737.98] I think it's going to be interesting how it evolves.
[3737.98 → 3746.36] I don't know if the core community will maintain a bunch of these or if it's, you know, some side companies or, you know, whole new companies that evolve out of this.
[3747.00 → 3749.46] But it really just expands what Postgres can do.
[3749.86 → 3752.20] Pluggable storage to me is one of those next big frontiers.
[3752.34 → 3754.66] It's going to be an exciting area for five or ten years.
[3755.18 → 3757.44] You can see remnants of where people have taken Postgres.
[3757.80 → 3759.12] Amazon Redshift is a great example.
[3759.70 → 3762.38] That was Postgres like 10 or 15 years ago.
[3762.54 → 3764.32] They got modified and modified and modified.
[3764.32 → 3768.18] It was a company called Par Excel that got kind of sort of bought by Amazon.
[3768.54 → 3774.22] And you see hints of it, but it's like, I think it was like Postgres 8.1, which is north of 10 years old.
[3774.32 → 3776.34] So it doesn't have things like JSON.
[3777.04 → 3784.14] So I think that extensions world is fascinating and pluggable storage of the next five, ten years.
[3784.26 → 3791.20] We're going to see a lot there because Postgres can keep moving, be safe and stable, reliable, not lose my data.
[3791.20 → 3793.48] As a database, the most important thing.
[3793.48 → 3795.46] But it's worth stating.
[3795.62 → 3802.60] And then we get all these, like you say, this kind of crazy things that, well, yeah, I actually do want this.
[3802.74 → 3809.74] As my stack evolves, and I want to do more, I do want to write a recommendation engine inside my Postgres database.
[3809.74 → 3818.32] And not have to like to have this ETL job that feeds into like a data lake that feeds into Regis that I'm maintaining five things.
[3818.86 → 3820.40] I just wanted to do this one thing.
[3820.48 → 3825.56] So I think like extensions, pluggable storage to me are a lot of excitement.
[3825.88 → 3829.38] Though I, a ton of credit to just core Postgres, right?
[3829.52 → 3833.62] Postgres is just going to keep new indexes, new polish.
[3833.62 → 3840.56] There's maybe some really new, awesome, kind of sexy feature like JSON-B that I'm forgetting.
[3841.50 → 3843.92] But I think we've got a pretty good base.
[3844.04 → 3848.16] Now it's, you know, keep working on performance, ease of use, this sort of things in the core.
[3848.30 → 3854.42] And a ton of credit to the people, you know, the 40 or so committers and all them that just keep plugging away.
[3854.42 → 3860.96] Not a lot of them kind of in the limelight, just making it available for millions and millions and millions of developers out there.
[3861.86 → 3863.68] Well, Craig, I can tell you're very excited about this.
[3863.82 → 3871.40] I want to ask you one last question, which are you've been doing all of this work on education and evangelism, for lack of a better word, right?
[3871.48 → 3876.36] Getting the word out there about all the cool stuff Postgres is able to do and will be able to do in the future.
[3876.54 → 3881.52] What's the best place to get started for people who are like brand new to the world of interacting with the database?
[3881.52 → 3885.24] Surely you have resources, maybe your website.
[3885.60 → 3890.00] Where do people go to learn Postgres and keep up with the new features coming out?
[3890.60 → 3895.62] Yeah, so I mean, there are a few places, you know, one shameless plug, I help curate Postgres Weekly.
[3896.40 → 3897.80] It's not a DVD newsletter.
[3897.96 → 3899.38] It's really targeted at app developers.
[3899.74 → 3905.40] Like, it's like, here are the how-tos, here's this tutorial, here's this shiny new feature, right?
[3905.44 → 3911.42] We'll talk about extensions and pluggable storage, but it's really targeted at kind of app developers that want to learn more.
[3911.64 → 3916.04] It's, you know, once a week, you've got kind of five to 15 articles in there.
[3916.14 → 3919.80] It's not a here's a hundred things to read, so pretty easy to parse.
[3920.44 → 3922.38] I blog about things a good bit.
[3922.48 → 3925.58] There are a number of companies out there that blog a good bit as well.
[3927.18 → 3931.60] There's a Planet Postgres, kind of syndication of a bunch of people that blog.
[3931.60 → 3934.78] It's a great resource if you want to follow, you know, every article that comes out.
[3935.36 → 3937.22] Those are my two top recommendations.
[3937.62 → 3942.18] If you really want to learn about the internals, go subscribe to the PG-SQL hackers mailing list.
[3942.54 → 3942.96] Read that.
[3943.42 → 3948.02] If you want to get some more of the basics, the PG-SQL users mailing list.
[3948.20 → 3951.18] Like, if you want to learn, like, hey, how do I debug a slow query?
[3951.54 → 3953.02] There are a bunch of great resources there.
[3953.02 → 3958.92] There's a Postgres team community Slack that there are thousands of people in just hanging out.
[3959.44 → 3962.04] There's still an active PostgreSQL IRC.
[3963.44 → 3968.54] There's some really loyal people in there that, hey, if you've got trouble with a query, they'll come in and help there.
[3969.00 → 3970.74] Those are kind of my offhand lists.
[3970.74 → 3976.72] There's, you know, a lot of blogs, but a lot of those try to hit in Postgres Weekly and that sort of thing.
[3977.34 → 3977.44] Yeah.
[3977.76 → 3986.64] So those are my defaults, and there are probably a few others links that I can come up with after that I can make sure to kind of send over, and we can get added as well.
[3987.48 → 3987.88] Absolutely.
[3988.16 → 3995.72] Listeners, all the links to all the things, including things maybe that he didn't even mention right now, but he thought of later, will be in your show notes.
[3996.16 → 3997.88] You know how to access those.
[3997.98 → 3998.86] Craig, this has been a lot of fun.
[3998.86 → 4004.74] You got me excited once again about Postgres, not even just the future, but the present of Postgres.
[4004.88 → 4006.48] I want to get out there and play with some of these extensions.
[4007.44 → 4012.60] Thanks so much for coming on the Changelog, and thanks so much for keeping us all abreast of what's going on with Postgres over the years.
[4012.66 → 4013.46] We really appreciate it.
[4013.70 → 4014.72] Yeah, thanks so much for having me.
[4016.96 → 4018.44] That's it for this episode of the Changelog.
[4018.50 → 4019.56] Thank you for tuning in.
[4019.68 → 4022.80] If you haven't heard yet, we have launched Changelog++.
[4022.80 → 4031.48] It is our membership program that lets you get closer to the metal, remove the ads, make them disappear, as we say, and enjoy supporting us.
[4031.82 → 4036.36] It's the best way to directly support this show and our other podcasts here on ChangeLog.com.
[4036.36 → 4040.42] And if you've never been to ChangeLog.com, you should go there now.
[4040.58 → 4045.30] Again, join Changelog++ to directly support our work and make the ads disappear.
[4045.82 → 4048.36] Check it out at ChangeLog.com slash plus.
[4048.54 → 4053.06] Of course, huge thanks to our partners who get it, Vastly, Linde, and Rollbar.
[4053.50 → 4055.96] Also, thanks to Break master Cylinder for making all of our beats.
[4056.36 → 4057.90] And thank you to you for listening.
[4058.00 → 4058.88] We appreciate you.
[4059.20 → 4060.18] That's it for this week.
[4060.36 → 4061.38] We'll see you next week.
[4061.38 → 4091.36] We'll see you next week.
[4091.38 → 4121.36] We'll see you next week.
