[0.00 --> 2.86]  I'm Slava Akmichet, and you're listening to The Change Log.
[12.84 --> 13.86]  Welcome back, everyone.
[14.00 --> 16.70]  This is The Change Log, and I'm your host, Adam Stikowiak.
[16.82 --> 19.10]  This is episode 181.
[19.60 --> 23.16]  And on today's show, we're joined by Slava Akmichet.
[23.58 --> 27.50]  Slava is the co-founder and CEO of RethinkDB.
[27.50 --> 33.14]  And before you think this is Founders Talk, another show I've done in the past that you may have listened to,
[33.38 --> 34.40]  this is not Founders Talk.
[34.48 --> 35.32]  This is The Change Log.
[35.48 --> 37.18]  But Slava is a co-founder.
[37.32 --> 38.32]  He's also a CEO.
[38.90 --> 41.34]  And Slava is also a software developer.
[42.06 --> 43.92]  And it was great having Slava on.
[43.98 --> 45.40]  We talked all about databases.
[45.62 --> 51.84]  We talked about what RethinkDB is doing for databases in this reactive, real-time web world we're living in.
[51.84 --> 59.12]  We had four awesome sponsors, CodeShip, Braintree, Harvest, and also DigitalOcean.
[59.82 --> 65.34]  Our first sponsor is CodeShip, longtime supporter and huge fans of The Change Log.
[66.10 --> 73.40]  And CodeShip wants you to focus on your code and automate all the things that are involved in delivering your application to the server.
[73.40 --> 78.74]  And also with CodeShip, you can run your tests lightning fast using Parallel CI,
[78.88 --> 82.84]  an awesome feature that allows you to split up your test commands and speed up your test suite.
[83.18 --> 88.62]  And out of the box for the first two weeks, they're going to give you a complimentary set of 20 parallel testing pipelines
[88.62 --> 93.90]  to speed up those builds and get that code in production so much faster, obviously, after it's tested.
[94.44 --> 100.22]  Use our coupon code, TheChangeLawPodcast, to save 20% off any plan you choose for three months.
[100.22 --> 103.34]  Head to CodeShip.com slash TheChangeLaw to get started.
[103.68 --> 104.88]  And now, on to the show.
[113.84 --> 114.90]  All right, everyone, we're back.
[114.98 --> 117.00]  We've got a catch-up show here for you, Slava.
[117.46 --> 119.30]  And Slava, I didn't ask you how to say your last name.
[119.42 --> 121.24]  And I think even if I tried, I might butcher it.
[121.26 --> 123.30]  So do me a favor and tell us your last name.
[123.66 --> 125.00]  It's Slava Akmichat.
[125.44 --> 125.80]  Okay.
[126.40 --> 127.34]  I'm going to call you Slava.
[127.66 --> 128.22]  That's cool.
[128.22 --> 131.40]  Jared, obviously, is here on the call today.
[131.52 --> 133.12]  And this is, Jared, this is a catch-up show.
[133.22 --> 138.70]  This is kind of a tail-off to episode 114, which you and I weren't even on, which is kind of interesting.
[139.78 --> 139.96]  Yeah.
[140.14 --> 143.58]  So Andrew did that show back in December of 2013.
[143.76 --> 144.46]  Slava was there.
[145.00 --> 145.66]  Yes, of course.
[146.12 --> 146.80]  But you and I were not.
[146.92 --> 148.52]  So we'll be catching up on lots of stuff.
[149.82 --> 154.38]  And Slava, you are the co-founder and CEO of RethinkDB.
[154.38 --> 157.00]  And that's an open source database.
[157.54 --> 161.34]  For those who didn't catch 114, give us an intro to who you are.
[161.94 --> 162.82]  Well, hey, guys.
[162.90 --> 164.70]  Thank you for having me on the show.
[165.50 --> 166.50]  You already introduced me.
[166.58 --> 167.22]  My name is Slava.
[167.34 --> 169.02]  I'm one of the founders at RethinkDB.
[170.18 --> 175.02]  RethinkDB is an open source scalable database for building real-time applications.
[175.02 --> 181.00]  And I'm sure we'll get into some of the stuff and talk about the project and what it's for.
[181.58 --> 184.10]  But just a little bit about myself.
[184.10 --> 185.36]  I was born in Ukraine.
[185.36 --> 188.72]  I moved to New York City with my parents when I was 13.
[189.02 --> 193.72]  I basically grew up in New York or spent half my life in New York.
[193.88 --> 196.62]  I am a computer scientist and a programmer.
[196.78 --> 197.94]  I love building things.
[198.00 --> 199.04]  That's my passion.
[199.34 --> 200.86]  I love developer tools.
[200.86 --> 205.20]  So, you know, I love building things for people who build things.
[205.92 --> 208.90]  And now I'm in California, Mount of View, California.
[209.52 --> 212.50]  I moved here to start RethinkDB about five years ago.
[212.62 --> 218.40]  So that's a very short summary of, you know, the past 32 years of my life.
[219.40 --> 221.86]  Well, we're definitely going to get into RethinkDB.
[222.10 --> 224.74]  And we'll have plenty of time to just talk about that.
[224.82 --> 229.06]  But first, you know, you have a blog, which is deafmacro.org.
[229.06 --> 230.70]  And I like your writing style.
[230.82 --> 232.70]  You're the kind of person who doesn't write very often.
[232.70 --> 236.62]  But then when you do, it seems like very well thought out long pieces.
[237.40 --> 240.96]  So I thought we'd maybe just camp out there a little bit and talk about a few of your posts
[240.96 --> 242.56]  because you have some interesting things to say.
[243.16 --> 249.26]  The first one is from, hey, about the same time you were on the show, December of 2013.
[250.08 --> 252.54]  You get a post called Learn to Code Like It's 1996.
[253.80 --> 254.08]  Oh, yeah.
[254.08 --> 258.76]  This was when you're kind of sounding off on the code school movement.
[259.10 --> 263.70]  This was about the same time that Obama said all Americans should learn to code or something like that.
[264.22 --> 269.88]  But you had a unique perspective on that with regard to kind of the Russian immigrants in New York City.
[270.04 --> 271.48]  Can you tell us about it?
[272.64 --> 272.90]  Yeah.
[272.90 --> 281.68]  So I think, you know, one advantage of having been in the industry for a while is that you start seeing patterns in things.
[282.28 --> 286.46]  And learn to, so the blog post Learn to Code Like It's 1999 that you're referring to,
[286.92 --> 292.14]  is about this learn to code movement, the idea that everyone should be learning to code.
[292.14 --> 295.08]  And so I remember I moved to the United States.
[295.16 --> 297.00]  I moved to New York in 1996.
[297.00 --> 298.40]  I was 13 years old.
[298.86 --> 304.02]  And at the time, we were in the middle of the dot-com boom, right?
[304.10 --> 309.58]  And I distinctly remember how, so my family moved to New York City from Ukraine.
[310.36 --> 315.72]  And my uncle, my aunt, and a lot of other people, you know, they moved to this new country.
[315.84 --> 317.10]  They barely spoke English.
[317.36 --> 319.36]  And they had to figure out how to make a living.
[319.36 --> 325.76]  And one of the most popular ways for the immigrant, for the Russian immigrant community in New York at the time,
[325.84 --> 327.48]  was to go to these hacker schools.
[327.76 --> 333.14]  Except they weren't called hacker schools at the time, but it was, it was something very similar.
[333.26 --> 336.38]  I forget what they were called, but it was basically, you know, they teach you how to program.
[336.52 --> 337.74]  It was a short course.
[337.82 --> 344.54]  It was about, most of them were about, you know, maybe six weeks to 12 weeks or something like that.
[344.54 --> 349.68]  And I remember back then, like, literally everybody was doing it.
[349.80 --> 352.62]  You know, it was people who had backgrounds in engineering and math.
[352.96 --> 358.62]  It was people who had no backgrounds in any kind of engineering disciplines whatsoever.
[358.92 --> 361.26]  And everyone in the Russian community was doing it.
[361.30 --> 365.94]  And I remember at the time, everyone in other immigrants, immigrant communities was doing it too.
[366.02 --> 367.52]  I mean, it was immensely popular.
[367.52 --> 369.70]  And there were tons of these schools.
[369.86 --> 380.06]  And I remember in New York, so I lived in Brooklyn, New York, and there was this Russian TV channel that's in, you know, it's in America.
[380.18 --> 383.26]  It's produced in America and it's designed specifically for American immigrants.
[383.26 --> 384.74]  So people don't watch it in Russia.
[384.88 --> 387.18]  It's just an American Russian, like, television channel.
[387.36 --> 392.44]  And there would be these ads for hacker schools that they play, you know, every half an hour.
[392.44 --> 399.02]  So that's how, you know, I just remember when people started talking about, oh, everyone should learn to code.
[399.10 --> 402.80]  I just remembered that movement and I decided to write a post about it.
[403.70 --> 404.14]  Yeah.
[404.30 --> 407.80]  So that movement didn't end so well, right?
[408.52 --> 410.70]  No, that one didn't end so well.
[411.16 --> 412.90]  But so it wasn't a complete failure.
[413.06 --> 419.70]  So my uncle, for example, I mean, he, after that was over, so he was working in a furniture factory,
[419.70 --> 423.08]  making furniture like sofas and beds and stuff.
[423.38 --> 425.26]  And at night he'd go to this hacker school.
[425.76 --> 430.84]  And after it was over, he did get a job and he's been working, you know, in the field for years,
[431.40 --> 433.62]  being kind of very productive about it.
[433.74 --> 436.56]  But for most people, it didn't work out well at all.
[436.86 --> 444.96]  Because after the dot-com bubble burst, basically all of the, these were the first jobs to get caught, right?
[444.96 --> 449.00]  Because people learned a very narrow, very specific set of skills.
[449.32 --> 455.08]  But the moment, the moment they have to expand out of this narrow skill set, it's, it's very, very hard for them
[455.08 --> 457.10]  because they don't have the basics and the fundamentals.
[457.10 --> 463.26]  And that's kind of what I really remember about that learn to code movement version one,
[464.02 --> 467.38]  is that people learn narrow skills, but not the fundamentals.
[467.38 --> 475.56]  And it turns out to be very hard to maintain gainful employment if you just don't have the basics of computer science.
[475.98 --> 476.00]  Yeah.
[477.02 --> 479.92]  Yeah, I think round two seems to be going a little bit better.
[480.02 --> 483.18]  Of course, we haven't had the bubble bust like last time around.
[483.18 --> 490.90]  Yeah, well, I'm not even sure, you know, I'm not even sure if it's worthwhile to make the parallel.
[491.26 --> 495.48]  Like, oh, the first one didn't go so well, so the second one isn't going to go so well too.
[495.56 --> 499.42]  Like, it's a very common fallacy to make arguments like that.
[499.48 --> 500.58]  But it is really interesting.
[500.72 --> 501.18]  It's kind of suggestive.
[501.78 --> 505.20]  Like, you want to look at it and at least think about it a little bit.
[505.92 --> 507.86]  Who were these ads from that were on the TV?
[508.00 --> 509.48]  Were they from the schools themselves?
[509.48 --> 516.04]  Or were they from, you know, was it part of some sort of movement where someone else was advocating to get people to code?
[516.10 --> 517.00]  Was it true advertisements?
[517.76 --> 521.04]  So it was true advertisements from the schools themselves.
[521.16 --> 523.08]  And there were lots of different schools like that.
[523.20 --> 526.06]  And the ads were, I mean, they were out of this world.
[526.24 --> 532.42]  It was like the ads were literally like this immigrant coming to the ass off the boat, doesn't have a job.
[532.42 --> 539.30]  And then the next scene is he's sitting at a pool in, like, his giant mansion with limos and stuff.
[539.62 --> 540.72]  I mean, it was really that bad.
[540.84 --> 544.46]  Like, I wish that YouTube didn't exist and internet was just getting started.
[544.68 --> 547.54]  So I wish I could find clips of that for you guys.
[547.70 --> 548.02]  I can't.
[548.18 --> 552.56]  So I actually, when I wrote the blog post, I was looking for the clips, but I couldn't find them anywhere.
[552.66 --> 554.22]  But, yeah, they were really ridiculous.
[554.60 --> 554.80]  Yeah.
[555.24 --> 556.68]  That's borderline pandering.
[558.20 --> 558.60]  Interesting.
[558.60 --> 562.10]  I think it was way, it was not even borderline pandering.
[562.10 --> 562.70]  Okay, okay.
[563.08 --> 564.24]  I was trying to be gracious.
[564.40 --> 565.54]  Yeah, so flat out pandering.
[566.96 --> 570.96]  Yeah, definitely an interesting perspective and one that I had no idea that that even took place.
[572.04 --> 572.68]  Me either.
[572.74 --> 575.30]  These unique, you know, moments in history.
[577.78 --> 582.26]  But, so speaking to the boom and the bust, you're also a startup guy.
[582.36 --> 584.62]  Obviously, RethinkDB is your startup.
[585.28 --> 585.46]  Yeah.
[585.46 --> 587.38]  And you have another post, which is more recent.
[587.38 --> 591.52]  I think it was this year, even in February, about picking startup ideas.
[592.58 --> 594.74]  And, man, you went deep on this one.
[594.84 --> 596.08]  You had lots of thoughts.
[596.44 --> 598.24]  So you've obviously put a lot of thought into this.
[598.34 --> 600.44]  And, you know, a lot of our audience is engineers.
[600.66 --> 607.30]  We also have solo developers and a lot of people who, you know, both develop and are business people.
[607.90 --> 607.94]  Right.
[608.18 --> 610.50]  You know, even last week we had Mitchell Hashimoto on.
[611.12 --> 613.00]  Another one of those hybrids.
[613.00 --> 622.66]  And so I thought maybe you could share with us some of your findings and some just pick out some maybe takeaways from your post, how to pick startup ideas and share them with the audience.
[622.66 --> 623.16]  Yeah.
[624.16 --> 624.36]  Yeah.
[624.56 --> 626.52]  So that was a big post.
[627.08 --> 627.16]  Right.
[627.16 --> 628.66]  There was a lot there.
[628.86 --> 629.08]  Absolutely.
[629.48 --> 634.74]  But the impetus for the post was, so when we started RethinkDB, we started it in 2009.
[635.30 --> 641.54]  And I was, you know, at the time I was in grad school and I was a pretty good, well, I want to say I was a pretty good engineer.
[641.70 --> 642.04]  I don't know.
[642.04 --> 643.38]  I guess the jury is still out.
[644.06 --> 645.78]  And my co-founder was the same way.
[645.84 --> 647.38]  But we never started companies before.
[647.48 --> 648.86]  We never started a business before.
[649.06 --> 652.20]  So we didn't know, you know, we didn't know anything about that.
[653.54 --> 664.50]  And as RethinkDB evolved and as we learned more and more and more about what works and what doesn't work, I just kept thinking about it really hard because it's important for our business to succeed.
[664.50 --> 668.34]  And then every once in a while, things kind of start clicking in place in my mind.
[668.42 --> 675.18]  And I figured, okay, now that I feel like I understand this a little bit, I can go out and share this with people.
[675.74 --> 677.12]  So the post was pretty big.
[677.18 --> 689.24]  But I think the most important thing in it is that, so like, okay, when you jump into this completely new discipline or you're trying to learn something completely new, it's a huge field.
[689.24 --> 694.60]  Like, let's say you know nothing about chemistry or physics and you're just jumping into physics.
[694.72 --> 696.32]  Like, there's so much to learn, right?
[696.98 --> 698.94]  And you don't always know where to get started.
[699.06 --> 703.54]  So typically for physics, you'd, like, go to school and there's a curriculum and people teach you stuff.
[704.14 --> 710.06]  And picking startup ideas, picking business ideas, it's, so it's a soft science, right?
[710.08 --> 712.30]  It's not like physics, but it is complicated.
[712.38 --> 713.60]  It's extremely complicated.
[713.60 --> 719.78]  There's a lot of laws about how markets behave that you can't really learn.
[719.94 --> 721.38]  Like, you could get an economics degree.
[721.50 --> 723.94]  That would probably be the closest thing to it.
[724.52 --> 728.58]  But generally, like, it's very hard to learn how the stuff works.
[728.66 --> 731.08]  You kind of have to see it for a while.
[731.70 --> 740.84]  But in physics, if you wanted to just get, you know, if you ask the physicist, okay, what is, like, if I needed to know the one thing that would really help me, what would it be?
[740.84 --> 750.86]  And I think there are certain laws that, so for example, like conservation of energy, right, is the kind of thing where, by the way, I'm going somewhere with this.
[751.54 --> 770.46]  So conservation of energy is this thing where if you're trying to solve a problem and it's really complicated, just knowing about conservation of energy and how it works will kind of guide you to the right solution without necessarily understanding all the forces involved and all the math involved.
[770.46 --> 771.00]  Right.
[771.06 --> 779.18]  So once you learn about conservation of energy, you can kind of navigate your way through physics a little bit without understanding all this other stuff.
[779.34 --> 783.92]  And you can, you know, start catching up and start learning other things, but you can kind of make correct decisions.
[784.16 --> 789.80]  So I think for startup ideas, that law is the efficient market hypothesis.
[790.12 --> 799.52]  If you understand the efficient market hypothesis, I think you can make a lot of correct decisions without really knowing the details about everything else that's going on.
[799.52 --> 808.64]  And the basics of the efficient market hypothesis, I mean, anybody could look it up, but it's essentially this idea that the markets are efficient.
[808.64 --> 817.00]  And if you think you're going to do better than other people, you're probably wrong because, you know, because there's lots of other people looking at the same thing.
[817.12 --> 821.46]  There's lots of other people that have information that you don't, things like that.
[821.46 --> 828.58]  So that generally, just having that knowledge about the efficient market hypothesis will help you make correct decisions.
[828.72 --> 833.84]  So, for example, many, you know, oftentimes people think of like conspiracy theories.
[833.84 --> 842.18]  They'll say, oh, you know, we already have like, you could cure cancer with cucumbers or something, but like big pharma wants to keep that away from you.
[842.62 --> 851.84]  And if you understand the efficient market hypothesis, you just wouldn't make that mistake because it's fundamentally not how the universe works.
[852.28 --> 861.02]  So most of the polls is about, okay, how can I take this idea of the efficient market hypothesis and apply it to making correct decisions about picking startup ideas?
[861.02 --> 865.58]  Like, does that make sense? I'm not sure if I'm doing a good job articulating the summary of the post.
[865.80 --> 868.06]  Yeah, let me reiterate and make sure that I'm following you.
[868.20 --> 872.50]  So the efficient market is the idea that markets are efficient.
[872.88 --> 878.94]  So if there is a valid market, then there would be other competitors in it.
[879.04 --> 880.30]  There'd be people trying it.
[880.40 --> 888.56]  And if you find one that's completely wide open and no one's trying it, like cancer curing via cucumbers, it's probably a bad idea.
[889.34 --> 890.40]  Yes, that's right.
[891.02 --> 898.02]  And there's a lot of, so you could look, you know, if you start analyzing businesses, you could look at startups and kind of tell whether it's going to work out.
[898.02 --> 905.86]  Like, for example, if someone, let's say someone proposes a startup where they say we're going to make batteries like five times as efficient as they are now.
[905.86 --> 918.78]  Well, then you'd think, okay, why is it that these two people or three people can make batteries five times as efficient when there's been, you know, billions of dollars poured into this industry?
[919.00 --> 924.94]  And there are huge battery manufacturers with R&D departments that try to research this for years and years and years.
[924.94 --> 928.80]  How come is this small company can make that better?
[928.92 --> 930.42]  What do they have that no one else has?
[930.44 --> 932.00]  And usually the answer is nothing, right?
[932.26 --> 938.70]  Every once in a while, something will happen where people just missed something obvious, but it's extremely rare.
[938.84 --> 941.80]  And if you're starting a business, it's probably not going to happen to you.
[941.80 --> 950.22]  It seems like how to, not how to pick startup ideas, but how to kill startup ideas because you really do is disqualify.
[950.40 --> 954.64]  I appreciated your contrast to the biology piece.
[954.64 --> 957.12]  You know, we're like, if life can exist, it was just basically.
[957.12 --> 957.94]  It's not going to go anywhere.
[958.52 --> 959.12]  Yeah, right.
[959.24 --> 965.76]  I mean, it's basically an ecosystem and the biological ecosystem is if life could arise, it would have already.
[965.76 --> 974.26]  And similarly in startups, if a startup could arise to solve a problem, like if the market could support it, it probably already would.
[974.58 --> 977.28]  So the question is, okay, how do you pick new ideas?
[977.28 --> 983.12]  And the general thrust there is that the world is changing all the time.
[983.30 --> 985.84]  Like, for example, some states legalize marijuana, right?
[985.98 --> 990.78]  That's a huge, that gives you a huge opening to start a business.
[990.78 --> 997.58]  So just generally, the way change happens is societies get more liberal, laws get more liberal.
[997.58 --> 999.10]  That opens up possibilities.
[999.90 --> 1007.04]  Certain technological advancements, they start out as quantitative advancements, but over time they become qualitative.
[1007.04 --> 1011.60]  And that gives you opportunity to build new technology on top of that technology, right?
[1011.60 --> 1018.72]  So you always have to look at what's changing about the world rather than, oh, like I'm going to pick this idea because I'm better than other people.
[1018.72 --> 1020.16]  Because that generally doesn't work.
[1020.78 --> 1025.54]  This makes me think about RethinkDB and your startup idea.
[1026.18 --> 1027.34]  Seven years old now.
[1028.82 --> 1034.08]  Take us back to that seven years ago, I guess, when you guys spawned the idea.
[1034.96 --> 1042.84]  And what advantages did you think you had or what technological change was happening that you thought you could latch on to?
[1042.92 --> 1044.52]  And then has that paid off for you?
[1045.56 --> 1045.76]  Yeah.
[1045.94 --> 1048.46]  So RethinkDB has gone through a couple of iterations.
[1048.46 --> 1050.92]  I think we're six years old now.
[1051.04 --> 1055.24]  But when we started at the beginning, this was in 2009.
[1055.42 --> 1058.26]  We were looking at solid state drives.
[1058.88 --> 1063.20]  And at the time, solid state drives weren't nearly as popular as they are now.
[1063.32 --> 1064.68]  Like they didn't exist in laptops.
[1064.76 --> 1066.04]  They didn't exist in most servers.
[1066.04 --> 1067.24]  They were just taking off.
[1067.88 --> 1071.18]  And, you know, everyone was on rotational drives.
[1071.30 --> 1074.14]  Solid state drives were about maybe five times as expensive.
[1074.14 --> 1076.42]  But they were like 20 or 30 times faster.
[1076.68 --> 1077.94]  And they didn't have seeks.
[1078.50 --> 1084.16]  So unlike rotational drives, you can read from any location in a solid state drive without paying this huge penalty.
[1084.16 --> 1091.66]  So when we started Rethink, we thought, okay, this is going to be a new technology.
[1091.94 --> 1094.10]  It was kind of obvious, at least to me.
[1094.16 --> 1099.90]  I don't know if it was obvious to a lot of other people that everyone's going to adopt SSDs for high performance applications.
[1099.90 --> 1104.52]  And we thought databases were designed entirely around seeks.
[1105.22 --> 1108.70]  They were designed entirely around the limitations of rotational drives.
[1108.76 --> 1111.12]  And now this new solid state technology is coming along.
[1111.56 --> 1119.38]  What can we do to design a new database product to kind of like if we were doing it from scratch?
[1119.38 --> 1121.14]  And now we've got these solid state drives.
[1121.24 --> 1121.82]  What can we do?
[1122.02 --> 1123.98]  So that was the impetus for starting RethinkDB.
[1123.98 --> 1130.46]  And right now, so today RethinkDB is very, very different from what it was back then.
[1130.50 --> 1132.52]  And maybe we'll talk about it in a little bit.
[1132.86 --> 1136.68]  But just going back to picking startup ideas and efficient markets.
[1137.60 --> 1143.38]  So this idea was pretty good because there was this new change, new technology that was happening.
[1144.30 --> 1152.74]  But we should have thought a little bit more about how to explain, okay, there's already existing vendors that make database software.
[1153.98 --> 1157.80]  You know, what is it that we can do that they're not going to be able to do?
[1157.90 --> 1159.88]  And in practice, that's actually what happened.
[1159.98 --> 1165.90]  And it turned out that with a few small changes, most databases just out of the box are really good in SSDs.
[1165.98 --> 1168.26]  And there wasn't a whole lot we could have done there.
[1168.26 --> 1172.06]  So there were also lots of other companies that were doing databases for SSDs.
[1172.06 --> 1178.16]  And they kind of had the same fate where they just couldn't build a product that was really compelling to people.
[1178.16 --> 1184.62]  Because ultimately, if you take MySQL or Postgres or Oracle and put it in an SSD, it worked really, really well.
[1185.18 --> 1185.98]  That's interesting.
[1186.10 --> 1191.32]  I remember your initial sales pitch all those years ago because it definitely caught my eye.
[1191.32 --> 1196.28]  You know, SSDs were, like you said, they were coming into mass production and use.
[1196.52 --> 1200.78]  And nobody had really designed data stores for an SSD.
[1201.08 --> 1205.54]  And so when I heard you guys say that fact, I was like, okay, that makes sense.
[1205.64 --> 1210.42]  And now we're going to create a database specifically designed with this technology in mind.
[1210.48 --> 1212.04]  I thought, that's a good idea.
[1213.58 --> 1215.90]  It's interesting that, you know, you thought it was a good idea.
[1216.02 --> 1216.74]  I thought it was a good idea.
[1216.74 --> 1223.20]  It turns out there weren't that many things that you could leverage or change to differentiate yourselves.
[1224.74 --> 1228.96]  Yeah, it was definitely promising and it felt like there was something there.
[1229.12 --> 1235.10]  But as we set out to build out the technology and the product, it turned out that there's just not a whole lot you could do.
[1235.50 --> 1237.38]  And I think it's interesting how it turned out.
[1237.56 --> 1240.66]  Like, I don't know how often that happens when there's a new change.
[1240.82 --> 1242.72]  So actually, maybe another example of this.
[1242.88 --> 1245.40]  I don't know if you remember this idea of augmented reality.
[1245.40 --> 1253.54]  Like, back when smartphone first came out, people had this idea that, oh, I could lift a phone and move it around and see all kinds of augmented things.
[1254.06 --> 1256.42]  And there were lots of companies getting started trying to do that.
[1256.48 --> 1257.56]  And it felt really promising.
[1257.78 --> 1261.76]  But then it turned out that no one wants to, like, lift their phone and stare at it.
[1261.80 --> 1265.38]  So there was not a whole lot you could build for that market.
[1266.38 --> 1272.34]  What's funny, too, is now all the cloud providers, especially this show here, where this show is sponsored by DigitalOcean.
[1272.48 --> 1274.46]  So everything out there now is SSD only.
[1274.46 --> 1274.90]  Yes.
[1275.16 --> 1290.50]  And so you're now in a market where, you know, six years ago when you were producing RethinkDB and trying to solve this problem of rotational drives versus SSD drives and that whole problem of the databases being designed for rotational drives.
[1291.18 --> 1297.58]  I mean, so what has happened, I guess, since maybe that's something we can do when we come back from the break, Jared, just kind of answer that question, maybe.
[1298.12 --> 1298.36]  Yeah.
[1298.36 --> 1299.84]  Well, that's a good break then.
[1300.06 --> 1302.06]  Not really a perfect break, but a good break.
[1302.12 --> 1302.86]  We do have this show.
[1302.96 --> 1303.46]  It's sponsored.
[1303.92 --> 1304.86]  So we have to take a break now.
[1304.94 --> 1306.50]  This is the time we take that break.
[1306.54 --> 1307.40]  So let's break real quick.
[1307.84 --> 1308.42]  We'll come back.
[1308.48 --> 1309.82]  We'll dive deeper with Slava.
[1309.82 --> 1317.00]  Braintree is all about making developer lives simpler with code for easy online payments.
[1317.00 --> 1320.86]  If you're searching for a simple payment solution, check out Braintree.
[1321.30 --> 1328.80]  For mobile app developers out there, the Braintree V.0 SDK makes it easy to offer multiple payment types.
[1329.22 --> 1337.98]  Start accepting PayPal, Apple Pay, Bitcoin, Venmo, traditional credit cards, and whatever's next, all with a single integration.
[1337.98 --> 1341.40]  Enjoy simple, secure payments that you can integrate in minutes.
[1341.84 --> 1343.04]  And developers, they've got you.
[1343.10 --> 1345.32]  Don't worry about taking days to integrate your payments.
[1345.80 --> 1347.36]  With Braintree, it's done in minutes.
[1347.84 --> 1352.82]  And if you don't have time, give them a call and they'll handle the integration for you and walk you through it.
[1353.38 --> 1357.20]  Braintree supports Android, iOS, and JavaScript clients.
[1357.54 --> 1364.78]  They have SDKs in seven languages, .NET, Node.js, Java, Perl, PHP, Python, and Ruby.
[1364.78 --> 1368.34]  And their documentation is comprehensive and it's easy to follow.
[1368.54 --> 1377.54]  To learn more and for your first $50,000 in transactions fee-free, go to braintreepayments.com slash changelog.
[1380.54 --> 1382.82]  All right, we're back from our break.
[1383.02 --> 1389.34]  And my jacked up kind of question prior to that break wasn't really a question, but you guys had a slogan change.
[1389.42 --> 1391.46]  Obviously, you couldn't really innovate in this area.
[1391.46 --> 1395.64]  But the point I was trying to make was that now we're in an era where it is SSD only.
[1395.76 --> 1400.54]  So if you had been able to innovate, it would have been perfect or a perfect world for Rethink.
[1400.66 --> 1403.12]  But you had to rethink your own thing.
[1403.52 --> 1407.10]  So your slogan now is the open source database for real-time web.
[1407.44 --> 1407.82]  Yeah, yeah.
[1407.82 --> 1415.88]  So the thing with SSDs, another kind of reason why it was a good idea but not a great idea.
[1416.00 --> 1417.02]  And I can start.
[1417.28 --> 1421.56]  So now, in hindsight, I realize that it didn't start with the customer.
[1422.14 --> 1424.12]  The idea was, well, something changed in the world.
[1424.22 --> 1425.20]  There is this new technology.
[1425.32 --> 1426.52]  What can we do around it?
[1426.52 --> 1431.46]  But it was a very much like technical, almost academic undertaking.
[1431.68 --> 1438.50]  We never really looked at, okay, what can we do for the customer and how can we actually build something that's valuable to other people?
[1438.78 --> 1441.76]  So what ended up happening is SSDs are everywhere now, right?
[1441.78 --> 1447.36]  We built a storage engine designed for cell estate drives, and it's still running in RethinkDB.
[1447.54 --> 1449.84]  It's still the fundamental kind of underpinning of RethinkDB.
[1449.84 --> 1459.64]  But then we found out that very quickly that if you just take a normal database, like a traditional database like MySQL, and put it in SSD, it works really, really well.
[1459.74 --> 1467.90]  And there's been some tweaks that people made to make MySQL faster in SSDs, but it was pretty relatively simple to do, right?
[1467.96 --> 1468.70]  So we couldn't.
[1468.92 --> 1472.52]  So, you know, having a database designed for SSDs wasn't very much an advantage.
[1472.72 --> 1479.48]  But at the time, we had this technology, and the storage engine was really, really good, or we thought it was really, really good.
[1479.48 --> 1482.92]  And we thought, okay, what else can we do?
[1482.98 --> 1484.56]  Can we do anything with this technology?
[1484.92 --> 1487.78]  Should we keep building, or should we go on to do something else?
[1488.26 --> 1498.70]  And what became obvious to us is that the world – so there was another change that was going on at the time, and we're in the middle of it right now.
[1499.10 --> 1505.74]  And the change is that the world is moving towards real-time applications, reactive applications with engaging experiences.
[1505.74 --> 1514.88]  So, for example, if you ever use Google Docs, when you're editing a document in Google Docs and someone else makes a change to it, you see that change right away.
[1515.26 --> 1518.72]  So that's an example of what we call a reactive real-time application.
[1519.08 --> 1520.32]  Another example is Slack.
[1520.86 --> 1524.16]  If people are familiar with it, it's a chat for Teams.
[1524.16 --> 1531.78]  And Slack is an extremely engaging product because – so it's just messaging on some level, but on another level, it's very engaging.
[1532.00 --> 1532.74]  You can send images.
[1532.94 --> 1533.78]  You can send videos.
[1534.24 --> 1536.22]  You can hop on and off between devices.
[1536.64 --> 1538.06]  You see everything right away.
[1538.14 --> 1538.86]  It's very snappy.
[1538.94 --> 1540.46]  It's an extremely engaging experience.
[1540.96 --> 1550.58]  So we saw that people are building these apps, but in order to build a real-time application, you have to push data to the browser in real-time because things change very, very quickly.
[1550.58 --> 1553.78]  And traditional tools weren't designed around that, right?
[1553.84 --> 1557.02]  They were designed around HTTP, and HTTP is all request response.
[1557.58 --> 1570.36]  So what we saw happening is that on the front end, people started building reactive software with things like Angular and React.js where everything is event-driven instead of kind of request response-driven.
[1570.62 --> 1576.24]  And the same thing happened in middleware with Node.js, but no one was doing that for the database.
[1576.24 --> 1578.68]  So we thought, okay, we've got the storage engine.
[1578.86 --> 1581.72]  It's a really great piece of technology, but it's not a great product.
[1581.94 --> 1587.70]  And people are building – people want to build these real-time applications, but it's hard because they have to pull the database all the time.
[1587.90 --> 1588.90]  It brings it down.
[1588.98 --> 1589.84]  It's hard to scale.
[1590.24 --> 1594.04]  So we decided to keep going, and we built a distributed database.
[1595.72 --> 1597.46]  It's designed for the web entirely.
[1597.60 --> 1598.64]  It's designed for real-time.
[1598.64 --> 1609.50]  And the way it works is that instead of kind of querying the database, getting the data, and then having to query it over and over again, the developer specifies, okay, this is what I'm interested in.
[1609.54 --> 1612.40]  I'm interested in this query or this data or this computation.
[1612.92 --> 1617.40]  And then anytime something changes on the database, the database pushes information back to the user.
[1617.40 --> 1630.34]  And what it does is it makes building reactive apps like Google Docs or Slack or multiplayer games or real-time analytics just dramatically easier than it would have been with a traditional database.
[1630.58 --> 1634.52]  So that's the change that happened over the last few years.
[1635.58 --> 1640.78]  Now, when did you guys start that change, and then when would you consider it finished?
[1641.14 --> 1645.70]  Like when were you actually – you had moved to real-time and were ready to have that as a product?
[1645.70 --> 1655.08]  Yeah, so I think we started thinking about it probably around the time when we did the last podcast.
[1656.08 --> 1657.88]  But it wasn't announced yet.
[1658.70 --> 1667.14]  And the reason why is that – so the real-time functionality just kind of happened that way, that that's how the storage engine was built.
[1668.22 --> 1670.40]  And then we built a distributed database.
[1670.70 --> 1672.26]  We added support for a query language.
[1672.52 --> 1674.72]  There's a lot – you know, there's distributed joins.
[1674.72 --> 1676.56]  There's a lot that RethinkDB can do.
[1677.16 --> 1681.38]  And under the hood, it was all this reactive – it had all the reactive technology.
[1681.60 --> 1685.46]  But it took a while to expose it to people in a way that's consumable.
[1685.90 --> 1691.76]  So I'd say that the first – and by the way, so the feature in RethinkDB that does this is called Change Feeds.
[1691.92 --> 1695.92]  And it allows people to subscribe to any query that they write.
[1695.92 --> 1704.82]  And I think the first version of Change Feeds we shipped it maybe – I don't remember, but I want to say about a year ago, maybe a little bit less than a year ago.
[1705.38 --> 1717.16]  And as far as when it's finished – so when we started – when we shifted to this notion of a real-time database for real-time applications, RethinkDB like really took off.
[1717.16 --> 1724.66]  So in the last few months, we've been growing at 30% month-over-month in just developers using RethinkDB.
[1725.16 --> 1728.56]  It's number one document database on GitHub right now.
[1729.16 --> 1731.54]  It's really started taking off.
[1732.16 --> 1736.84]  And when a product or a project starts taking off, it's like almost never finished, right?
[1736.84 --> 1748.54]  Because our feature list is longer than it's ever been because the more people adopt the technology, the more different things they want to do with it, especially with databases because it's so horizontal.
[1749.12 --> 1751.52]  So, yeah, I don't know if it will ever be finished.
[1751.64 --> 1754.94]  I think it's always going to be – there's always going to be more to do.
[1755.46 --> 1755.74]  Well said.
[1755.82 --> 1759.14]  Yeah, I meant finished as in like the transition had changed, had finished.
[1759.54 --> 1760.40]  Oh, I see.
[1760.46 --> 1760.88]  I'm sorry.
[1761.16 --> 1764.46]  I think – yeah, that was – so between the –
[1764.46 --> 1765.54]  Jared likes to ask that question.
[1765.62 --> 1766.42]  When are you shipping it?
[1766.42 --> 1767.14]  Yeah, when are you done?
[1767.26 --> 1767.44]  Yeah.
[1768.16 --> 1785.06]  Yeah, I think we realized we should do something around maybe mid-2013 that we should shift, you know, we should ship these real-time features and design the whole – like redesign the whole database around the real-time web and make it easy for people to build real-time applications.
[1785.36 --> 1791.86]  And I think it took about six months before we had the first release that was – that provided value to people that was usable.
[1791.86 --> 1792.38]  Nice.
[1792.38 --> 1792.68]  Nice.
[1792.68 --> 1797.50]  So this seems like more of a differentiator, but do you have competition?
[1797.64 --> 1801.34]  Are there other databases that do push-based architecture?
[1801.34 --> 1806.60]  Okay, so the real-time space is really exciting right now because there's a lot going on.
[1807.40 --> 1816.20]  So there aren't a lot of other databases doing it because – so just kind of going back to this – the conversation we had about startup ideas.
[1816.20 --> 1823.56]  So this is something that's super valuable to customers, super valuable to users because everyone wants to build these real-time apps.
[1823.78 --> 1828.28]  The world has really changed in this direction, and it's kind of obvious that it's not going back.
[1828.28 --> 1836.70]  But if you look at other database vendors, having this push functionality where you could subscribe to queries, that's really, really hard to do.
[1836.84 --> 1843.10]  You kind of have to bake it into the architecture, and you can't just take an existing database and overhaul it to support this.
[1843.18 --> 1843.82]  That's really hard.
[1844.06 --> 1846.86]  So there's a lot going on in the space in general.
[1847.10 --> 1849.12]  So, you know, I already mentioned React and Angular.
[1849.28 --> 1850.02]  There is Node.js.
[1850.02 --> 1858.42]  There is Meteor, and I don't know if you're familiar with it, but Meteor is a real-time app development framework.
[1858.88 --> 1870.86]  And the way they do real-time is they build a really complicated layer called Live Query on top of the databases – on top of databases that they run on top of Mongo, and they listen to Mongo's what's called Uplog.
[1871.46 --> 1878.90]  And they try to provide similar functionality, but because it's not baked into the database itself, it's very, very hard.
[1878.90 --> 1884.22]  There are certain things you just can't do, like you can't do scalability, you can't do advanced computations.
[1884.32 --> 1885.82]  You can only really do document sync.
[1886.12 --> 1889.02]  So that's one example of when it's happening outside of the database.
[1889.88 --> 1893.82]  Another example is Firebase, and Firebase is also kind of similar.
[1894.02 --> 1904.04]  It's a service that does document sync, and it's a really, really great service for what it does, but it's also fairly limited in the sense that it's not a general-purpose database.
[1904.16 --> 1906.20]  So there's an enormous amount of stuff you can't do.
[1906.20 --> 1914.50]  You can build relatively simple applications, but it's hard to kind of get outside of that and build more complicated apps.
[1914.62 --> 1922.34]  So there's a lot going on in general, but there isn't like a traditional open-source database vendor that's doing the same thing.
[1923.40 --> 1926.28]  Firebase, you mentioned, acquired by Google, right?
[1926.94 --> 1927.20]  Yes.
[1927.54 --> 1929.16]  So are they leaving them alone?
[1929.36 --> 1931.00]  Is it being Google-ized?
[1931.88 --> 1933.44]  Just Google-ized.
[1933.58 --> 1934.24]  I like that.
[1934.24 --> 1936.98]  I don't know.
[1937.10 --> 1940.94]  As far as I can tell, Firebase is still shipping things.
[1941.02 --> 1941.74]  It's still running.
[1942.56 --> 1947.24]  I don't think, you know, I think they're integrating it with the Google Cloud services.
[1948.52 --> 1951.94]  But yeah, from what I understand, they operate almost independently.
[1953.00 --> 1955.38]  On the site, it doesn't seem like it's very Google.
[1955.88 --> 1957.32]  It does say sign up with Google.
[1957.32 --> 1962.80]  You can sign up for it with Google, but it doesn't seem like it's been Google-ized, as you said, Jared.
[1963.22 --> 1964.88]  I think they did a little bit of integration.
[1965.28 --> 1968.40]  But yeah, it feels like they're operating independently.
[1969.00 --> 1969.82]  What about Pusher?
[1969.88 --> 1974.54]  That's another service that I'm familiar with that seems to provide this type of feature.
[1975.62 --> 1975.94]  Oh, yeah.
[1976.02 --> 1978.42]  So there is another class of services.
[1978.66 --> 1979.64]  So Pusher is an example.
[1979.64 --> 1981.94]  There's another one called PubNob.
[1983.06 --> 1985.24]  And I don't know if you're familiar with that company.
[1985.64 --> 1989.96]  So that's also an example of what's happening in the real-time space.
[1990.08 --> 1994.86]  So what these guys do is they provide messaging in what's called the network edge.
[1995.18 --> 1997.70]  So they don't deal with storing of data.
[1997.70 --> 2000.34]  So they don't let you do it.
[2000.38 --> 2005.64]  For example, if you wanted to do a leaderboard and say, what are the top 10 players in my game?
[2006.80 --> 2009.52]  So Pusher and PubNob, they don't let you solve that problem.
[2010.02 --> 2014.98]  But what they do let you do is once you know what you want to push out to different clients,
[2015.10 --> 2019.00]  they provide kind of like a message queue or a PubSub as a service.
[2019.32 --> 2024.48]  And it's very, very useful when you have millions of concurrent clients that all have to send messages to each other.
[2024.48 --> 2032.10]  Pusher and PubNob are doing a really good job offering a service to businesses where they solve a lot of problems in that space.
[2032.96 --> 2033.18]  So, okay.
[2033.26 --> 2041.70]  How about compare it a little bit to perhaps a more traditional database or even a key value store that has PubSub as a feature?
[2041.86 --> 2043.58]  I know Postgres has PubSub as a feature.
[2044.04 --> 2045.44]  Redis has PubSub as a feature.
[2047.12 --> 2048.88]  Compare everything to that.
[2049.68 --> 2050.24]  Okay.
[2050.40 --> 2054.30]  So PubSub is something relatively narrow.
[2054.48 --> 2058.78]  So it's extremely useful in a wide range of use cases, but it's a relatively narrow feature.
[2058.88 --> 2063.66]  And the feature is, you know, you have clients subscribing to channels.
[2063.86 --> 2067.84]  So let's say you have a chat application and you have a channel in that, you know, a room or a channel.
[2068.28 --> 2071.42]  You have different people who are in that chat.
[2071.54 --> 2072.52]  They subscribe to the channel.
[2072.62 --> 2076.70]  And then every time anyone pushes information to the channel, everyone else sees that.
[2076.70 --> 2079.08]  So that's what PubSub generally lets you do.
[2079.88 --> 2082.18]  And it's, of course, useful for a lot of other things.
[2082.18 --> 2088.22]  What RethinkDB lets you do, it really takes the abstraction down to the database level.
[2088.38 --> 2092.06]  So people who are building these apps, they don't have to think about PubSub at all.
[2092.48 --> 2101.06]  You don't need a separate, so you don't need to have a separate piece of infrastructure to distribute messages to clients and a piece of infrastructure to compute information.
[2101.06 --> 2118.22]  So, for example, even if you had a chat application, so what you typically would have to do with PubSub in something like Postgres is if you want to provide chat history, anytime someone writes a message, you'd have to write it to the database and push it into this PubSub feature.
[2118.60 --> 2123.72]  And then the clients, when they start up, they'd have to read from the database and subscribe to PubSub.
[2123.72 --> 2130.26]  So you're fundamentally dealing with two different technologies that just happen to be in one project and one piece of infrastructure.
[2130.74 --> 2136.72]  And by contrasting RethinkDB, the way it works is you don't think of PubSub and data as two separate things.
[2137.06 --> 2141.70]  You just say, you know, I have a table with chat messages.
[2141.70 --> 2145.54]  And you say, you write a query that says, OK, I'm interested in chat message.
[2145.64 --> 2152.06]  Get me all the chat messages in this channel and then keep sending me information anytime the results have changes.
[2152.58 --> 2157.56]  Right. So you just write, you still think of it in terms of database queries, but these are live queries that send you updates.
[2157.86 --> 2162.22]  And every client that connects can say, this is the stuff I'm interested in.
[2162.26 --> 2166.40]  I'm interested in, you know, this analytical query, like let's say dashboard.
[2166.40 --> 2168.20]  I'm interested in this chat room.
[2168.34 --> 2176.22]  I'm interested in, you know, maybe all the players in my game within a certain location, like within a mile next to me, things like that.
[2176.78 --> 2179.84]  And they get, so they get the data and then they get all the updates.
[2179.96 --> 2184.74]  So you don't even, so you as a developer don't even have to think about PubSub versus database.
[2184.86 --> 2185.44]  How are they different?
[2185.58 --> 2187.76]  You don't have to build all the infrastructure yourself.
[2187.90 --> 2191.02]  We just, it kind of comes, it's the right abstraction.
[2191.38 --> 2193.72]  It's a different abstraction for real-time apps.
[2193.96 --> 2194.74]  Does that make sense?
[2195.00 --> 2195.76]  I think so.
[2195.76 --> 2202.76]  So from an application developer's perspective, are you removing the need for the server side?
[2203.00 --> 2215.22]  And I mean, are you actually writing your app logic against RethinkDB or do you still have that middleman between your, you know, say your 30, you know, JavaScript fat clients and your data store?
[2215.72 --> 2219.58]  Well, you have JavaScript clients that run in the browser and mobile.
[2219.76 --> 2222.84]  Then you have your Python and Ruby or Node.js application.
[2222.84 --> 2226.04]  That communicates with the browser via WebSockets.
[2226.48 --> 2229.84]  And then the Node.js or Python app or whatever communicates with RethinkDB.
[2229.84 --> 2236.00]  So it's a pretty standard three-tier architecture right now, the way it works with other databases.
[2236.84 --> 2240.68]  It's just that your server side doesn't need a query for updates.
[2240.68 --> 2244.76]  It's just receiving them on the fly as Rethink receives them, basically.
[2245.30 --> 2245.92]  That's right.
[2246.28 --> 2246.48]  Okay.
[2246.64 --> 2247.54]  I am following you.
[2247.66 --> 2247.86]  Adam?
[2247.86 --> 2250.64]  I'm obviously following to a degree.
[2251.24 --> 2255.82]  I'm trailing behind, but I do have maybe a clarifying question.
[2256.02 --> 2264.88]  So for the developers out there that are, like, used to using something like Pusher or PubSub, what are the – it sounded like you said some of the advantages, but I guess it's – maybe there's more.
[2265.12 --> 2266.74]  You know, there's obvious advantages.
[2266.74 --> 2267.62]  So what are the advantages?
[2267.62 --> 2267.78]  Yeah.
[2267.84 --> 2274.18]  So if you use Pusher or PubNub or any kind of a PubSub system, you have to do two things.
[2274.24 --> 2278.34]  You have to write data to your database, and then you have to send messages out to other users.
[2278.44 --> 2279.88]  So you're kind of splitting your code.
[2280.38 --> 2287.42]  And then the moment you're doing something more complicated than just sending messages, you have to start querying the database and, you know, do long polling.
[2287.42 --> 2303.26]  And in a naive application, when you poll the database every few seconds, it turns out okay, but as you get more and more concurrent users, that turns out to be extremely hard to scale because you start bringing down your database with just constant polling of all the users.
[2303.26 --> 2319.22]  So what happens in practice is people's infrastructures for real-time apps become progressively more and more and more complicated as they start dealing with the scalability challenges and the code complexity challenges of having, you know, polling and multiple infrastructures and things like that.
[2319.60 --> 2328.68]  And the benefit of RethinkDB is that it takes the abstraction down to the database layer where the user just specifies, okay, this is what I'm interested in.
[2329.22 --> 2331.00]  And you don't have to do long polling.
[2331.00 --> 2335.92]  You don't have to write code that writes to two different pieces of infrastructure.
[2336.56 --> 2344.46]  When your app reaches a certain degree of complexity where you want to do more complicated real-time queries, you can do that without any change, right?
[2344.50 --> 2354.20]  So just the fundamental process of building real-time apps on top of RethinkDB becomes dramatically easier because the database was designed for this kind of a use case.
[2354.20 --> 2367.24]  It almost seems like PubNub, and I'm not going to call these people, you know, workarounds, but it almost seems like hearing what you're saying that Rethink is a direct path while these others are more of a workaround.
[2367.70 --> 2368.50]  Yeah, a little bit.
[2368.58 --> 2373.76]  So I think something like PubNub, so first of all, as a service, whereas RethinkDB is an open source product.
[2373.76 --> 2381.62]  So it's very, very useful if you're doing simple, like it's very good at what it does, which is pushing messages and routing messages around clients.
[2382.14 --> 2389.18]  But routing messages is only a small, it's like a tip of the iceberg of what you might want to do with a real-time application.
[2389.18 --> 2390.70]  So you still have to deal with storage.
[2390.82 --> 2393.08]  You still have to do a lot of different things.
[2393.08 --> 2394.82]  You still have to do complex computations.
[2394.82 --> 2403.32]  So PubNub is, it's very, very good at what it does, but it's a very small part of the solution for a full-blown real-time app.
[2403.38 --> 2410.00]  You really need to bring it down to the database to make building these things dramatically easier and accessible to every team.
[2410.12 --> 2417.62]  So you said that it was, you know, real-time focused, but you did say that Rethink is a general purpose data store.
[2417.62 --> 2425.76]  Would you only use it if you're building a real-time app, or could you possibly use it for more traditional request-response web apps?
[2426.46 --> 2429.94]  So you can use RethinkDB for request-response web apps.
[2430.04 --> 2436.50]  So if you don't want to do anything real-time, RethinkDB just looks like a traditional NoSQL database.
[2436.60 --> 2439.92]  It still has pretty important advantages.
[2440.06 --> 2441.12]  It's very easy to scale.
[2441.64 --> 2443.50]  It does server-side joins.
[2443.60 --> 2445.70]  It does complex computation subqueries.
[2445.70 --> 2449.70]  So it's a very good, full-featured, general-purpose database.
[2450.20 --> 2460.08]  And the reason why we designed it this way is very often people, they don't just start building a real-time app in its entirety, right?
[2460.14 --> 2464.58]  They'll say, they have an app, and then they'll say, oh, I want to make this bit of it real-time.
[2465.02 --> 2467.48]  And then I want to make this bit of it real-time.
[2467.56 --> 2469.54]  So it's kind of, they do it piecemeal, right?
[2469.54 --> 2476.38]  And right now, people are starting to build full-blown real-time applications on day one where everything is real-time, and that's wonderful.
[2476.88 --> 2483.08]  But very often, when you already have an app and you want to start making changes, it's not something where you'll just make, you'll change everything.
[2483.22 --> 2485.00]  You start adding these piecemeal features.
[2485.00 --> 2497.56]  And that's why it was really important to give people the smooth migration path from, oh, I just, I already know how to build a traditional request response application, and now I get to start adding these features really easily.
[2497.56 --> 2509.88]  I think that's well said, and I think that's true that, you know, people a lot of times will start off traditional and then just have, you know, it's kind of the same thing with JavaScript.
[2510.22 --> 2526.08]  Are you going to jump all in and go with a front-end framework, you know, that's hidden at JSON API, or are you going to have a traditional HTML rendered page that just has, as DHH calls it, JavaScript sprinkles, which is both a good thing or a bad thing, depending on who says it.
[2526.08 --> 2533.46]  And it seems like here it's kind of like, do you have WebSocket sprinkles and, you know, real-time sprinkles?
[2534.42 --> 2539.80]  Or do you know that you're building something from the ground up that needs to be real-time?
[2539.98 --> 2553.08]  And it seems like RethinkDB can be used, if you're not sure, it can be used as a traditional data store, but it's there for you in the case that you either switch to a real-time app or you know that you need one.
[2553.08 --> 2557.74]  Right. Real-time sprinkles is actually a really good way to put it.
[2557.88 --> 2565.26]  I didn't know about this phrase, JavaScript sprinkles, but yeah, DHH is really good at coining some of these phrases.
[2565.26 --> 2575.46]  Yeah, it's one of these terms that is a term of derision by some people, and it's a term of endearment for those that are for it and those that are for against it, but both sides seem to like it.
[2575.46 --> 2578.42]  So it's one of those interesting words.
[2579.94 --> 2580.92]  Let's see here.
[2581.58 --> 2585.94]  I want to talk to you about a couple transport layer things that have come up this year.
[2586.74 --> 2597.06]  You know, we have typical REST APIs, the old SOAP APIs, RPC APIs, and it seems like Facebook and Netflix are kind of trying to change the game with how you speak to your back end.
[2597.60 --> 2600.54]  And I want to talk about how Rethink fits into that story.
[2600.54 --> 2605.00]  If it does, let's take a break and we will pick up with that on the other side.
[2606.70 --> 2613.58]  All right, listeners out there who are working solo or on a team tracking time for your projects and billing for invoices.
[2614.48 --> 2615.62]  Imagine this scenario.
[2615.98 --> 2622.84]  You thought you were wrapping up a project and the client asked for a new feature at the last minute and they got questions about time spent on the project.
[2622.84 --> 2629.08]  Well, do you know how much time you're spending on every feature, tweak, or bug fix to give them that feedback?
[2629.94 --> 2636.42]  Well, Harvest is a time tracking tool built just for that, for understanding where your time is going and billing for that time.
[2636.82 --> 2644.16]  They even have built-in reporting that lets you know how much time your projects took so you can use that information to make better estimates in the future.
[2644.16 --> 2652.02]  Not only will you understand how much time you're tracking on your client work, you'll also be able to turn those billable hours into invoices in minutes.
[2652.56 --> 2656.60]  Create a free 30-day trial today at GetHarvest.com.
[2656.92 --> 2662.50]  After your trial's over, enter our code CHANGELOG to save 50% off your first month.
[2662.50 --> 2675.98]  So one interesting new trend, it seems like this year, 2015, has been the introduction of alternate ways of sending data back and forth between your JavaScript clients and your servers.
[2676.16 --> 2682.16]  Facebook has its GraphQL, Netflix has its Falcor, which by the way, Adam, we need to get Netflix on here.
[2682.60 --> 2683.16]  Talk about Falcor.
[2683.16 --> 2683.42]  We do.
[2684.18 --> 2685.46]  Making a note right now.
[2685.60 --> 2686.78]  Yeah, just write that down.
[2686.94 --> 2687.38]  Jot it down.
[2687.90 --> 2688.30]  I'm doing it.
[2688.30 --> 2692.88]  RethinkDB seems like it would fit somewhat into that story.
[2693.76 --> 2695.36]  Is it complementary to these?
[2695.46 --> 2696.44]  These aren't really technologies.
[2696.68 --> 2700.12]  They're more thoughts or patterns.
[2700.80 --> 2702.20]  Well, they're protocols.
[2703.26 --> 2707.96]  I think I call them protocols with kind of de facto implementations.
[2709.44 --> 2710.66]  Yeah, I was gapping the word.
[2710.74 --> 2712.00]  That's definitely what I would call them.
[2712.00 --> 2715.52]  So, yeah, does it play well with these protocols or is it against them?
[2716.42 --> 2716.62]  Yeah.
[2716.62 --> 2718.04]  So what's really interesting.
[2718.22 --> 2724.98]  So one thing about RethinkDB is that we're, you know, we're completely open source, but it's not just a matter of keeping the source code out in public.
[2724.98 --> 2727.14]  We do all of our development in public.
[2727.32 --> 2727.92]  It's all on GitHub.
[2728.52 --> 2729.70]  If you go to RethinkDB.
[2730.00 --> 2735.92]  If you go to, sorry, GitHub slash RethinkDB, you'll see everything that's going on.
[2735.92 --> 2748.82]  And on the issue tracker, we always collaborate with our users on pretty much everything and every new feature, every design decision, everything that's going on that lets us build a really wonderful product.
[2748.82 --> 2765.66]  And when GraphQL first came out and then, well, Felcor came out, people immediately, so our users immediately opened issues on the issue tracker saying, hey, it'd be great if, you know, RethinkDB seems like it's a really good fit for GraphQL or it's a really good fit for Felcor.
[2765.82 --> 2768.16]  It would be wonderful if you guys had an implementation.
[2768.16 --> 2777.30]  So we started thinking about this about six to eight months ago when Facebook and Netflix first started promoting these technologies.
[2777.76 --> 2785.74]  And actually on that issue, there's a little bit of a back and forth with the creator of GraphQL who's on the Facebook team right now.
[2786.64 --> 2788.56]  So it's a really interesting issue.
[2788.66 --> 2793.68]  I'll send you guys a link that you can share with our viewers or listeners.
[2793.68 --> 2795.66]  I'm on your issues now.
[2795.74 --> 2796.48]  I see this one.
[2796.60 --> 2802.78]  It says support Facebook's GraphQL and there's like 60 some responses and there's deep, deep conversations going on here.
[2802.88 --> 2803.92]  So this seems like that's the one.
[2803.92 --> 2804.58]  Yeah, that's the one.
[2805.08 --> 2808.18]  So RethinkDB definitely fits into that paradigm.
[2808.56 --> 2820.50]  And the reason why, you know, so just to kind of a brief introduction to GraphQL and Felcor, the idea is if you're building modern single page applications with Reactor Angular, then what happens is you start dealing with a couple of challenges.
[2820.50 --> 2826.38]  You have to create all these endpoints where most of the code you're writing is just boilerplate code.
[2827.16 --> 2832.58]  On the browser, you have to do multiple requests to the server to render anything.
[2832.90 --> 2840.28]  So, you know, to render one component which has subcomponents, you might have to do multiple network round trips, which slows everything down.
[2840.28 --> 2842.76]  So there's challenges like that.
[2842.82 --> 2852.26]  And the idea between GraphQL and Felcor is that you kind of unify that and replace REST with this new protocol that's composable, declarative.
[2852.56 --> 2855.46]  So every component can specify the kind of data it needs.
[2855.94 --> 2858.64]  You can do one round trip instead of multiple.
[2858.82 --> 2860.70]  You could do things like optimistic updates.
[2860.70 --> 2865.30]  So it really fits better into the new paradigm of web development.
[2866.12 --> 2874.70]  And RethinkDB would work really, really well with GraphQL and Felcor because you can do bidirectional communication.
[2875.64 --> 2878.96]  So GraphQL has some provisions for that and Felcor is adding it.
[2879.64 --> 2886.00]  And in general, just the way the structure, the way the data is laid out works really well with Rethink's data model.
[2886.00 --> 2890.56]  So we are working on an integration and we're very excited about it.
[2890.74 --> 2892.90]  It's hopefully going to come out pretty soon.
[2894.44 --> 2895.48]  That sounds excellent.
[2895.60 --> 2899.40]  So you mentioned the, you know, it's difficult sometimes.
[2899.52 --> 2904.22]  We talk about Rethink, you know, the company, Rethink, the open source project.
[2904.46 --> 2904.78]  Right.
[2904.92 --> 2909.32]  Comparing you with Pusher, which is a service and this is an open source project.
[2909.46 --> 2912.26]  And you pointed that out that this is like in the open, open source.
[2912.26 --> 2918.98]  One thing that comes up with open source, especially with data stores and, you know, large infrastructure is licensing.
[2919.78 --> 2926.72]  And maybe now is a good time we can talk about what is Rethink the company versus Rethink the open source project.
[2926.88 --> 2930.00]  And then as part of that is like, what's the licensing story?
[2931.26 --> 2931.38]  Okay.
[2931.48 --> 2933.80]  Well, so RethinkDB is a venture funded company.
[2934.36 --> 2936.18]  So it's really a corporation.
[2936.58 --> 2940.24]  But our product, RethinkDB the project is completely open source.
[2940.24 --> 2952.70]  So what the company does is the way, you know, our business model right now is we provide client services to a lot of our users who use RethinkDB in production.
[2952.88 --> 2956.56]  And the services we provide is development support as people build apps.
[2956.74 --> 2958.26]  We provide production support.
[2958.26 --> 2964.86]  So when the apps on top of RethinkDB are deployed, we help people in case something goes wrong and we give them that security.
[2965.84 --> 2974.90]  You know, if they have a mission critical application running on top of RethinkDB, it's very important to them to be able to pick up the phone and call somebody and make sure their problems get solved.
[2975.30 --> 2982.58]  And we also provide on-site training to help come out, train their developers on how to build these types of apps, how to use Rethink, things like that.
[2982.58 --> 2987.78]  But RethinkDB, the open source project, is licensed under AGPL.
[2988.38 --> 2997.76]  And it was really important to us to protect the project in such a way that anytime someone uses it and improves it, they have to release the changes to the community.
[2998.28 --> 3007.70]  And then the drivers, so these are the bits, the kind of libraries you use in your Node.js or Python or Ruby or whatever programming language to connect to RethinkDB.
[3007.70 --> 3009.08]  They're all Apache licensed.
[3009.70 --> 3013.92]  So basically, you know, you can use RethinkDB for free for any reason.
[3014.54 --> 3018.80]  If you make any changes, you have to release them to the community.
[3020.44 --> 3023.50]  But yeah, there's no restrictions on how you use the project.
[3023.68 --> 3025.82]  It's just like any other piece of open source software.
[3025.82 --> 3037.60]  How do you balance being venture funded and your product being open source, having services that obviously the VCs gave you money for a reason they want to return?
[3037.76 --> 3037.88]  Right.
[3038.20 --> 3051.08]  How do you as a developer and a CEO balance the direction of the product, which is open source, and the direction of the company, which needs to make money to ultimately feed the people that are giving you money?
[3051.08 --> 3063.24]  Well, so to be honest, it's not much of a balance because if you're building a developer tool, if you're building a database in particular, it's a fundamental piece of infrastructure.
[3063.70 --> 3068.82]  And in 2015, you just couldn't build that as a closed source project.
[3069.50 --> 3072.16]  Like that just wouldn't be possible because nobody would adopt it.
[3072.60 --> 3077.60]  So everything to be, I mean, we use a lot of software, but we don't pay for any closed source software.
[3077.60 --> 3082.04]  It's just not something that we do, and we assume other developers don't do that either.
[3082.50 --> 3083.82]  And that's where the world is going.
[3084.02 --> 3085.30]  Like no one's going to pay.
[3085.68 --> 3090.58]  No one's going to use a fundamental piece of infrastructure if it's a closed source software and, you know, pay for licenses.
[3091.02 --> 3098.38]  So old style companies like Oracle and Microsoft can get away with that because they have, you know, huge infrastructures that they've built up.
[3098.44 --> 3099.64]  They have existing customers.
[3099.64 --> 3109.50]  But you can't, I don't believe you can build a new company that builds a fundamental piece of infrastructure software targeted at the developers.
[3109.74 --> 3112.22]  I don't think you can build a new company that makes it closed source.
[3112.48 --> 3114.28]  So for us, it's not much of a balance.
[3114.42 --> 3116.32]  We think it has to be open source.
[3116.44 --> 3117.64]  We're all open source developers.
[3118.42 --> 3122.56]  I don't think it would ever be successful if it were a closed source.
[3122.56 --> 3123.86]  So it's very, very simple.
[3124.00 --> 3128.86]  But, of course, the flip side of that, we have to figure out, you know, how to make the company commercially successful.
[3130.02 --> 3134.34]  And the way to do that, so right now we're providing client services to people.
[3134.46 --> 3139.38]  We're also learning a lot about the kind of patterns that our customers run into.
[3139.74 --> 3144.82]  And now we're building products to take many of those patterns, operationalize them, productize them,
[3144.82 --> 3151.74]  and then ship those as kind of software services as opposed to client services that are provided by humans.
[3152.16 --> 3153.48]  So that's the balance.
[3154.76 --> 3159.32]  That's, you know, our approach for building a commercially viable company.
[3159.44 --> 3162.82]  But as far as we think of the project itself, there's no balance there.
[3163.00 --> 3163.80]  It's open source.
[3163.90 --> 3165.46]  It's always going to be open source.
[3165.76 --> 3170.60]  I don't think there's not a whole lot of discussion internally about this at all.
[3171.30 --> 3172.66]  I don't mean balance on the open source.
[3172.66 --> 3178.50]  I know the, I guess, I know that Rethink is open source and there's no change.
[3178.56 --> 3186.64]  I guess if you're trying to commercialize, which we just had the same word come up with when we talked to Mitchell from HashiCorp,
[3186.76 --> 3187.98]  was commercializing software.
[3188.40 --> 3191.58]  When you're trying to commercialize your company and those things,
[3191.86 --> 3197.84]  I guess as long as your revenue path and the open source product you are kind of committed to maintain,
[3198.10 --> 3201.56]  it's always going to be open source and the community can take over if something happened to the company.
[3201.56 --> 3206.82]  I'm not saying that, but so long as your mission and the open source mission is kind of in line,
[3207.14 --> 3208.46]  it's easy to balance, it sounds like.
[3208.54 --> 3209.54]  Yeah, it's very easy.
[3209.64 --> 3214.34]  I think fundamentally there are things that people will pay for and things they won't pay for.
[3214.48 --> 3215.72]  And you can't, you know, you can't.
[3215.76 --> 3217.54]  So that's one of the laws of economics, right?
[3217.54 --> 3220.30]  Like you can't sell people something they don't want to pay for.
[3220.30 --> 3226.00]  And I think people just don't want to pay for infrastructure software targeted at developers.
[3226.28 --> 3228.72]  I mean, we expect it to be free now for better or worse.
[3228.80 --> 3234.28]  And I think it's for the better because we've seen this enormous amount of innovation in software.
[3234.76 --> 3238.38]  So, yeah, the revenue path for us, though, is when we look at the patterns,
[3238.72 --> 3242.94]  the problems that our customers solve and that we solve for them,
[3243.22 --> 3244.92]  we now take them and productize them.
[3244.92 --> 3250.14]  And we're going to be shipping a lot of services around productizing those patterns.
[3250.44 --> 3252.36]  So that's our revenue path.
[3252.42 --> 3254.44]  And for now, it's client services.
[3254.58 --> 3255.90]  So the future is very bright.
[3256.02 --> 3257.26]  It's very, very exciting.
[3257.96 --> 3261.74]  But, yeah, it's not, you know, it's not very difficult to balance, surprisingly.
[3262.80 --> 3265.26]  What can you share with people out there that are listening to this and thinking,
[3265.40 --> 3265.94]  OK, that's cool.
[3265.96 --> 3266.72]  You got some services.
[3267.46 --> 3271.44]  What can you share about how you developed out those services
[3271.44 --> 3274.12]  and what actually you consider revenue generators?
[3274.12 --> 3275.28]  What can you share about that?
[3275.48 --> 3279.40]  Well, so revenue generators, I guess that's things people pay for.
[3280.60 --> 3280.88]  Yes.
[3283.36 --> 3286.34]  Yeah, but the way we're developing it is we look at, so, you know,
[3286.74 --> 3291.24]  the way people buy client services for everything to be right now is,
[3291.34 --> 3295.40]  you know, a developer in some organization picks Rethink,
[3295.86 --> 3300.64]  builds a prototype, and then he or she shows the prototype to their colleagues,
[3300.64 --> 3303.20]  and then it starts turning into a real commercial app.
[3303.20 --> 3306.98]  And then when it gets to deployment or as they're building the application,
[3307.12 --> 3309.22]  they realize, hey, we need client services.
[3309.22 --> 3312.94]  So they give us a call and they say, OK, here's the kind of stuff we're interested in,
[3312.98 --> 3314.66]  and we tell them, you know, about what we offer.
[3315.04 --> 3317.04]  And then as we work with these customers,
[3317.04 --> 3319.78]  we learn a lot about the challenges that they're facing.
[3319.94 --> 3323.68]  So fundamental challenges are often, you know, deployment.
[3323.68 --> 3327.86]  Like people have their cloud provider, they have their internal cloud,
[3327.92 --> 3329.94]  and they have to figure out how to deploy RethinkDB.
[3331.04 --> 3334.56]  RethinkDB right now is very scalable and it's very easy to scale,
[3334.96 --> 3338.72]  but very often people need some guidance for complicated setups.
[3338.90 --> 3342.20]  Like they'll say, you know, we want to run this in three data centers,
[3342.38 --> 3344.40]  two of them are in Europe, one in the U.S.
[3344.40 --> 3345.82]  How do we even set this up?
[3345.82 --> 3351.70]  So that challenge of figuring out how do I set up my database, that's a huge thing.
[3352.04 --> 3354.86]  There's things like auditing, monitoring,
[3355.08 --> 3357.00]  just all kinds of challenges you run into
[3357.00 --> 3359.88]  when you start having a really big enterprise deployment.
[3360.46 --> 3362.52]  And what we're doing is we're taking all of that,
[3362.58 --> 3364.46]  that we're advising them, you know,
[3364.50 --> 3369.42]  that our support team is basically giving human services like client services,
[3369.42 --> 3372.10]  and we're building products and services around it
[3372.10 --> 3375.72]  where people can now solve these problems in the click of a button.
[3376.42 --> 3378.86]  But instead of, you know, talking to a human,
[3378.98 --> 3383.18]  they get to pay monthly for this service that helps them solve all these problems.
[3384.34 --> 3388.24]  I think the addition of these product eyes, you know,
[3388.28 --> 3391.44]  software as a services as part of your business model is interesting
[3391.44 --> 3394.60]  because when I first heard that you're doing client services,
[3395.14 --> 3401.06]  I thought, can client services really drive a VC-backed company
[3401.06 --> 3403.26]  to where they're trying to go all on their own?
[3403.56 --> 3407.50]  It seems like, and this is just hunches and like me putting things together,
[3407.60 --> 3412.32]  I think, I feel like a support company, right, a services company
[3412.32 --> 3414.94]  makes a lot of sense for a bootstrapped company,
[3415.06 --> 3417.48]  one with little expectations like, you know,
[3417.48 --> 3419.20]  you got to pay salaries and make a profit.
[3419.70 --> 3421.74]  But you're VC-backed, you have, you know,
[3422.06 --> 3425.40]  other people's money that are hoping for returns on those investments.
[3425.40 --> 3429.86]  Has that pressure or that expectation to not just, you know,
[3429.92 --> 3434.04]  pay yourselves and pay your workers, but to actually have huge growth,
[3434.10 --> 3438.02]  has that driven you towards some of these additional revenue paths?
[3439.40 --> 3443.98]  It has, but I think, so I think if we weren't VC-funded
[3443.98 --> 3447.72]  and we didn't have any expectation of huge growth,
[3447.78 --> 3450.64]  I think we'd probably still arrive at the same conclusions
[3450.64 --> 3454.82]  because, so, you know, I'm a developer
[3454.82 --> 3458.00]  and I think, I always think as a developer,
[3458.18 --> 3459.92]  even though I do a lot of other jobs now.
[3460.38 --> 3462.04]  And it's like, you know, when you look at code
[3462.04 --> 3464.36]  and you have two pieces of code that look kind of similar
[3464.36 --> 3466.86]  and you think, man, I got to abstract that away into a function,
[3467.02 --> 3468.62]  like that just doesn't feel right.
[3469.16 --> 3471.40]  It's the same thing when you're running a company
[3471.40 --> 3474.12]  and you have people picking up the phone
[3474.12 --> 3476.66]  and it's like every time I hear someone explain something
[3476.66 --> 3481.48]  to a customer twice, I'm like, okay, this should be like a library, right?
[3481.50 --> 3484.44]  We shouldn't have to do this over and over and over again.
[3484.74 --> 3486.32]  So it's a very, very similar thing
[3486.32 --> 3489.24]  where you start seeing these patterns and you're like,
[3489.30 --> 3491.34]  okay, how can we turn these patterns into software
[3491.34 --> 3494.28]  and abstract them away so we don't have to do the same thing
[3494.28 --> 3495.14]  over and over again?
[3495.14 --> 3499.60]  So I think having VC funding is the kind of thing
[3499.60 --> 3502.70]  that definitely guides you in that direction
[3502.70 --> 3505.82]  where you start building, you know, software as a service
[3505.82 --> 3507.24]  and products like that.
[3507.42 --> 3509.82]  But I think ultimately we would have done the same thing
[3509.82 --> 3511.26]  because it feels very natural.
[3511.88 --> 3514.00]  It feels very natural to me as a developer,
[3514.00 --> 3516.96]  like when I see the same problem being solved multiple times
[3516.96 --> 3518.66]  over and over again, I'm like, okay,
[3518.66 --> 3520.14]  how do we turn this into software?
[3521.52 --> 3524.68]  In hindsight, since we're talking about VC funding
[3524.68 --> 3527.20]  and open source, and we just had this conversation
[3527.20 --> 3529.50]  last episode with Mitchell,
[3530.04 --> 3532.70]  and I'm thinking for those out there that are like Mitchell
[3532.70 --> 3534.88]  that are developing open source,
[3535.54 --> 3539.06]  talented enough to be in the lead like you are
[3539.06 --> 3541.16]  and develop this technology,
[3541.32 --> 3543.92]  I'm wondering if in hindsight you can think back and say,
[3544.04 --> 3547.46]  did you really need VC funding to accomplish this mission?
[3548.30 --> 3550.76]  And if you had to do it over again, I guess,
[3551.20 --> 3552.18]  maybe that's not the question I want to ask,
[3552.24 --> 3554.12]  but more so, do you think the VC funding
[3554.12 --> 3556.52]  was required to be where you're at today?
[3556.88 --> 3558.56]  Or could you have done it a different way
[3558.56 --> 3559.90]  and be exactly where you're at
[3559.90 --> 3562.72]  with maybe less commitments or less ties?
[3564.14 --> 3567.50]  So I think very often people,
[3567.86 --> 3570.22]  I'm kind of going to go a little bit around
[3570.22 --> 3571.54]  your question to answer it,
[3571.56 --> 3573.36]  but very often people set up this like
[3573.36 --> 3575.56]  almost adversarial model in their mind.
[3575.68 --> 3578.06]  So they say, oh, I'll raise, you know,
[3578.10 --> 3580.08]  I'll raise VC money,
[3580.08 --> 3583.06]  and I'll be pressured to do things I don't want.
[3583.92 --> 3585.38]  You inherently think it's a bad thing.
[3585.56 --> 3587.40]  So people inherently think it's a bad thing.
[3587.48 --> 3589.58]  They always think like, oh, there's going to be this pressure.
[3589.72 --> 3591.80]  They think there's this like evil capitalist,
[3592.06 --> 3595.28]  you know, conspiracy or something like that.
[3595.36 --> 3597.50]  Like I haven't experienced that at all.
[3597.90 --> 3601.00]  I am extremely grateful to everyone's,
[3601.00 --> 3602.62]  first of all, you know, we're in Silicon Valley
[3602.62 --> 3604.80]  and I'm extremely grateful to everyone I met here.
[3604.80 --> 3606.48]  I'm extremely grateful to investors
[3606.48 --> 3607.98]  that invested in our company
[3607.98 --> 3609.86]  and kind of believe in us and support us.
[3610.30 --> 3611.82]  And the reason why is that
[3611.82 --> 3614.16]  it's sort of like if you want to make movies,
[3614.16 --> 3615.32]  you've got to go to Hollywood,
[3615.50 --> 3617.56]  at least for a little bit to learn what they've learned.
[3617.66 --> 3619.46]  Like these industries are very crafty
[3619.46 --> 3621.28]  and people in these industries
[3621.28 --> 3623.22]  know an enormous amount of stuff
[3623.22 --> 3625.38]  and they're perfectly happy to share that knowledge,
[3625.52 --> 3626.58]  not just for free,
[3626.68 --> 3627.84]  but they like give you money
[3627.84 --> 3630.14]  and then guide you, right?
[3630.20 --> 3631.70]  Like otherwise you'd have to pay
[3631.70 --> 3633.00]  an enormous amount of money
[3633.00 --> 3634.34]  to them as consultants.
[3634.34 --> 3635.72]  So yeah, I don't feel,
[3635.84 --> 3636.88]  you know, I certainly feel,
[3637.54 --> 3638.68]  I wouldn't call it pressure.
[3638.94 --> 3640.94]  It's more like an expectation
[3640.94 --> 3643.36]  of doing something important and meaningful,
[3643.36 --> 3646.00]  but I don't think it's a bad thing at all.
[3647.52 --> 3650.24]  I've learned an enormous amount from these people
[3650.24 --> 3652.08]  and I think it helps our users
[3652.08 --> 3654.70]  because our users are,
[3654.82 --> 3656.76]  the more successful everything DBA is
[3656.76 --> 3658.50]  as an open source project and as a company,
[3658.58 --> 3660.12]  the more successful our users are
[3660.12 --> 3661.92]  because there's a bigger ecosystem,
[3662.14 --> 3663.36]  they can learn from each other,
[3663.36 --> 3665.16]  the product gets better, right?
[3665.22 --> 3667.00]  So I think it's like kind of everyone,
[3667.20 --> 3668.20]  it's one of those things
[3668.20 --> 3669.52]  where it's not a zero sum game.
[3669.62 --> 3670.98]  It's like everybody benefits.
[3671.78 --> 3674.32]  So could we have done it without VC funding?
[3675.02 --> 3676.20]  I think for a database,
[3676.20 --> 3677.66]  it's extremely hard
[3677.66 --> 3679.88]  because it's a very complicated piece of software
[3679.88 --> 3682.34]  and it takes years to get it to a point
[3682.34 --> 3683.64]  where it's useful to people.
[3684.06 --> 3684.76]  And in the meantime,
[3684.96 --> 3685.96]  you know, you have to pay people
[3685.96 --> 3687.50]  and you have to kind of sustain yourself
[3687.50 --> 3688.88]  and pay rent and stuff.
[3688.88 --> 3691.22]  So for our particular project,
[3691.22 --> 3692.84]  it would be very, very hard,
[3692.94 --> 3693.92]  if not impossible,
[3693.92 --> 3695.04]  without VC funding.
[3695.66 --> 3697.14]  I think for other projects
[3697.14 --> 3698.36]  where you could build something
[3698.36 --> 3701.18]  that can start generating money very quickly
[3701.18 --> 3703.06]  because it's useful to people very quickly,
[3703.06 --> 3704.22]  that's probably easier.
[3704.86 --> 3706.18]  But for a thing to be,
[3706.28 --> 3707.12]  that'd be pretty hard
[3707.12 --> 3708.16]  just because it took,
[3708.38 --> 3708.62]  you know,
[3708.64 --> 3709.72]  it took like three years
[3709.72 --> 3710.98]  to get version one out.
[3711.58 --> 3713.12]  It kind of goes back to your
[3713.12 --> 3714.70]  how to pick a startup idea
[3714.70 --> 3715.88]  and the innovation process
[3715.88 --> 3717.58]  where you,
[3718.94 --> 3720.18]  because of the VC funding
[3720.18 --> 3722.10]  and because databases
[3722.10 --> 3722.76]  are the way they are,
[3722.80 --> 3723.76]  you really had to innovate
[3723.76 --> 3725.06]  to get to where you are today
[3725.06 --> 3725.84]  with Rethink
[3725.84 --> 3726.84]  and the,
[3726.94 --> 3727.52]  you know,
[3727.58 --> 3728.86]  the solution that it solves
[3728.86 --> 3729.84]  and the way it tackles
[3729.84 --> 3730.96]  the problem itself.
[3731.66 --> 3731.88]  Yeah.
[3732.08 --> 3733.40]  So anytime there is,
[3733.50 --> 3735.42]  I think greatness comes out of pressure
[3735.42 --> 3736.46]  almost, right?
[3736.50 --> 3737.52]  Like, does that make sense?
[3737.94 --> 3738.22]  Totally.
[3739.36 --> 3739.76]  Totally.
[3740.46 --> 3740.62]  Yeah.
[3740.64 --> 3741.88]  I didn't want to ask that question
[3741.88 --> 3742.54]  in a negative way
[3742.54 --> 3743.84]  and if it came out that way,
[3743.86 --> 3744.24]  I didn't really,
[3744.24 --> 3746.30]  I was thinking more like
[3746.30 --> 3748.88]  informative to those out there
[3748.88 --> 3749.52]  that are like you.
[3749.58 --> 3750.54]  So the next Slav,
[3750.60 --> 3751.30]  the next Mitchell,
[3751.30 --> 3751.86]  who's like,
[3752.22 --> 3753.86]  I want to build this open source software
[3753.86 --> 3755.18]  for the good of the open source community
[3755.18 --> 3756.76]  and just technology in general,
[3757.22 --> 3758.44]  but how the heck do I get there?
[3758.64 --> 3760.20]  And did I need to make that choice
[3760.20 --> 3761.42]  that I made to take VC funding?
[3761.72 --> 3762.96]  Was it actually bad for us
[3762.96 --> 3764.10]  and could we have gotten there differently?
[3764.56 --> 3765.38]  And I think more like
[3765.38 --> 3766.36]  you've been down this road
[3766.36 --> 3767.62]  and can you share some experiences
[3767.62 --> 3769.20]  with those that are
[3769.20 --> 3770.54]  potentially in your shoes,
[3770.64 --> 3771.26]  maybe in your shoes,
[3771.32 --> 3772.60]  because someone may listen
[3772.60 --> 3773.94]  to this podcast a year,
[3774.26 --> 3775.54]  two years later from today
[3775.54 --> 3777.44]  and be in a similar situation
[3777.44 --> 3778.50]  with brand new innovations
[3778.50 --> 3780.44]  and be thinking,
[3780.64 --> 3782.54]  should I approach VC funding
[3782.54 --> 3783.26]  for these reasons
[3783.26 --> 3784.90]  or should we find another model,
[3785.08 --> 3785.70]  which is what Jared
[3785.70 --> 3786.34]  was talking about earlier,
[3786.40 --> 3787.34]  like React
[3787.34 --> 3788.90]  as another database
[3788.90 --> 3790.50]  that did support and stuff
[3790.50 --> 3792.18]  to kind of bolster their business
[3792.18 --> 3792.84]  and they didn't,
[3793.06 --> 3794.56]  I don't know if they took VC funding or not,
[3794.62 --> 3796.26]  but just kind of hoping
[3796.26 --> 3797.56]  you can share some experiences back.
[3797.66 --> 3798.12]  That was my...
[3798.12 --> 3798.56]  Yeah, totally.
[3798.72 --> 3799.02]  I'm sorry.
[3799.08 --> 3800.12]  I apologize if it came out,
[3800.20 --> 3801.34]  if my answer came out a lot.
[3801.34 --> 3802.10]  I wanted to apologize.
[3802.32 --> 3803.52]  I didn't mean to do that,
[3803.70 --> 3805.16]  but...
[3805.16 --> 3805.86]  You're all good.
[3805.92 --> 3806.94]  Don't worry about apologizing.
[3807.70 --> 3808.72]  You're always in the right here.
[3808.78 --> 3809.26]  Don't worry about it.
[3809.52 --> 3810.56]  Not always, but...
[3810.56 --> 3811.92]  I feel like I should apologize too.
[3812.78 --> 3813.24]  All right.
[3813.54 --> 3814.38]  You should, Jared.
[3814.38 --> 3814.84]  Sorry, guys.
[3814.84 --> 3815.06]  So you're sorry.
[3815.62 --> 3817.56]  I have a new question.
[3818.00 --> 3819.58]  Let's shift to this here.
[3820.00 --> 3820.50]  So we're talking,
[3820.74 --> 3821.12]  you know,
[3821.22 --> 3822.32]  funding side.
[3822.40 --> 3823.28]  Let's talk about sales
[3823.28 --> 3824.52]  with regard to
[3824.52 --> 3825.96]  convincing developers,
[3826.22 --> 3827.08]  convincing companies.
[3828.28 --> 3829.16]  We're all developers.
[3829.62 --> 3830.60]  We know how we are.
[3831.56 --> 3832.06]  You know,
[3832.10 --> 3833.30]  we're very stuck in our ways.
[3833.42 --> 3834.44]  We're also very fickle,
[3834.56 --> 3835.00]  which is kind of
[3835.00 --> 3836.20]  an interesting combination.
[3836.50 --> 3836.62]  You know,
[3836.64 --> 3837.84]  we switch often,
[3837.92 --> 3838.78]  but we also get stuck
[3838.78 --> 3839.94]  in our terminals
[3839.94 --> 3840.60]  and our...
[3840.60 --> 3842.18]  I'm stuck on my Postgres,
[3842.30 --> 3843.12]  have been for years,
[3843.56 --> 3844.50]  but still interested.
[3844.80 --> 3846.02]  And I'm sure it's been
[3846.02 --> 3847.26]  kind of hard to convince people,
[3847.42 --> 3848.62]  especially with their data.
[3849.26 --> 3849.46]  You know,
[3849.50 --> 3850.44]  a data store is like,
[3850.72 --> 3851.22]  like you said,
[3851.24 --> 3852.46]  it's critical infrastructure.
[3853.66 --> 3854.36]  So I'm guessing
[3854.36 --> 3855.28]  you've had some troubles
[3855.28 --> 3856.40]  convincing people
[3856.40 --> 3857.50]  to try Rethink.
[3857.50 --> 3858.24]  I'm guessing you've had,
[3858.94 --> 3859.06]  you know,
[3859.10 --> 3860.16]  you've been here for six years.
[3860.16 --> 3860.84]  You've shifted
[3860.84 --> 3861.96]  and you're still being successful.
[3862.50 --> 3862.98]  And now you had,
[3863.16 --> 3863.38]  you know,
[3863.44 --> 3863.82]  what'd you say,
[3863.84 --> 3865.46]  30% per month growth
[3865.46 --> 3866.14]  or something like that.
[3866.34 --> 3867.60]  So you probably had some wins
[3867.60 --> 3868.28]  along the way,
[3868.40 --> 3868.90]  both personally
[3868.90 --> 3870.14]  and as a team.
[3870.84 --> 3871.82]  I'm curious if you can share
[3871.82 --> 3873.04]  some of those big wins.
[3873.16 --> 3873.32]  Like,
[3873.68 --> 3875.18]  what was a customer
[3875.18 --> 3875.96]  that you brought on,
[3876.06 --> 3876.88]  whether they were even,
[3877.10 --> 3877.42]  you know,
[3877.76 --> 3878.98]  hiring you for your client services,
[3879.10 --> 3880.66]  but just users of RethinkDB,
[3881.56 --> 3882.56]  big companies
[3882.56 --> 3884.34]  or cool companies
[3884.34 --> 3886.26]  or people that you respect
[3886.26 --> 3887.84]  that you've convinced
[3887.84 --> 3888.54]  or have been,
[3889.00 --> 3890.54]  have become RethinkDB users
[3890.54 --> 3891.12]  over the years?
[3892.40 --> 3892.58]  Yeah.
[3892.72 --> 3893.66]  So we actually
[3893.66 --> 3895.28]  haven't had to do
[3895.28 --> 3896.62]  a whole lot of convincing
[3896.62 --> 3898.48]  because an open source,
[3899.06 --> 3900.74]  open source really helps with that
[3900.74 --> 3901.86]  because when we first
[3901.86 --> 3903.24]  launched RethinkDB,
[3903.98 --> 3904.80]  there was a lot of,
[3904.88 --> 3905.02]  you know,
[3905.06 --> 3906.14]  because people are building
[3906.14 --> 3906.92]  these real-time apps,
[3906.96 --> 3907.88]  there was a lot of interest.
[3908.04 --> 3908.48]  But of course,
[3908.54 --> 3909.78]  when you're in a bigger company,
[3909.88 --> 3911.00]  very often people are like,
[3911.06 --> 3911.16]  oh,
[3911.16 --> 3912.34]  this is a new technology.
[3912.98 --> 3914.54]  It's hard to convince people.
[3915.32 --> 3917.20]  But what happened over time is,
[3917.80 --> 3919.08]  so some developer
[3919.08 --> 3920.06]  and some organization
[3920.06 --> 3921.50]  will just download RethinkDB
[3921.50 --> 3923.02]  without asking for permission
[3923.02 --> 3924.24]  just because,
[3924.36 --> 3924.52]  you know,
[3924.56 --> 3925.64]  they like playing
[3925.64 --> 3926.56]  with new technologies.
[3926.56 --> 3927.32]  They like playing
[3927.32 --> 3928.02]  with new software.
[3928.14 --> 3929.16]  They like learning things.
[3929.56 --> 3930.98]  And they'll build a prototype
[3930.98 --> 3932.08]  on top of Rethink.
[3932.50 --> 3933.66]  And sometimes that prototype
[3933.66 --> 3934.80]  doesn't go very far.
[3935.20 --> 3935.90]  And that's okay.
[3936.02 --> 3936.24]  You know,
[3936.28 --> 3937.14]  people have learned
[3937.14 --> 3938.08]  and experimented
[3938.08 --> 3938.60]  and then maybe
[3938.60 --> 3939.46]  they'll use it again.
[3939.82 --> 3940.92]  But every once in a while,
[3941.02 --> 3942.30]  what would happen is that
[3942.30 --> 3943.90]  they showed the prototype
[3943.90 --> 3944.76]  to their colleagues
[3944.76 --> 3945.60]  or to their boss
[3945.60 --> 3946.44]  and people were like,
[3946.58 --> 3946.70]  wow,
[3946.80 --> 3947.70]  that's amazing.
[3947.82 --> 3948.82]  Let's productize it.
[3950.08 --> 3951.70]  And after that,
[3952.28 --> 3953.84]  so in those cases
[3953.84 --> 3954.66]  when that happened,
[3954.74 --> 3955.34]  it was very,
[3955.46 --> 3957.40]  very easy for us
[3957.40 --> 3958.16]  because we didn't have
[3958.16 --> 3959.42]  to like convince anybody
[3959.42 --> 3960.56]  or sell anybody, right?
[3960.58 --> 3961.74]  It was very organic.
[3962.96 --> 3964.46]  And once that happens,
[3964.54 --> 3965.74]  if they already have an app
[3965.74 --> 3966.28]  and they've built
[3966.28 --> 3967.46]  on top of this technology,
[3967.80 --> 3968.28]  very often,
[3968.40 --> 3969.50]  so someone usually
[3969.50 --> 3970.74]  in DevOps or operations,
[3970.94 --> 3971.92]  they have to make sure
[3971.92 --> 3973.64]  that when it goes live,
[3974.24 --> 3975.02]  you know,
[3975.06 --> 3975.80]  it stays up.
[3975.90 --> 3976.76]  And so someone has to
[3976.76 --> 3977.46]  wake up at night
[3977.46 --> 3978.46]  if something goes wrong.
[3978.88 --> 3979.80]  And then at that point,
[3979.86 --> 3981.04]  it's people just like,
[3981.12 --> 3981.26]  hey,
[3981.28 --> 3982.02]  we need to buy,
[3982.40 --> 3982.96]  you know,
[3982.98 --> 3983.48]  we need to buy
[3983.48 --> 3985.20]  commercial services.
[3985.88 --> 3987.38]  So as far as
[3987.38 --> 3988.78]  really cool companies
[3988.78 --> 3991.16]  that use RethinkDB
[3991.16 --> 3992.94]  that we're very happy with,
[3993.80 --> 3995.26]  there's lots.
[3995.26 --> 3996.24]  So there's lots of
[3996.24 --> 3998.32]  exciting companies using it.
[3998.32 --> 3998.90]  So one example,
[3999.02 --> 3999.94]  I'll bring up some
[3999.94 --> 4000.78]  that I really love.
[4001.24 --> 4002.14]  So one company,
[4002.20 --> 4003.20]  I met with them recently,
[4003.56 --> 4005.28]  it's called NextGXDX.
[4005.58 --> 4006.86]  They use RethinkDB
[4006.86 --> 4007.88]  to provide an efficient
[4007.88 --> 4009.86]  marketplace for genetic testing.
[4010.74 --> 4011.40]  So for example,
[4011.40 --> 4012.40]  someone has a disease,
[4012.50 --> 4013.44]  they go to their doctor,
[4013.82 --> 4014.62]  their doctor needs
[4014.62 --> 4015.88]  to run a genetic test,
[4016.42 --> 4017.22]  which by the way,
[4017.26 --> 4018.62]  it's a very common thing
[4018.62 --> 4019.92]  now in medicine,
[4019.92 --> 4020.86]  which I didn't realize
[4020.86 --> 4021.90]  until I even talked to them.
[4021.96 --> 4023.04]  I thought genetic testing
[4023.04 --> 4024.40]  is kind of,
[4024.40 --> 4024.62]  you know,
[4024.62 --> 4027.00]  to pick therapies,
[4027.00 --> 4028.66]  it's kind of the future,
[4028.78 --> 4029.40]  but it turns out
[4029.40 --> 4030.12]  to have been happening
[4030.12 --> 4030.72]  for a while.
[4030.92 --> 4031.68]  But the marketplace
[4031.68 --> 4032.48]  is very inefficient
[4032.48 --> 4034.06]  and what NextGXDX does
[4034.06 --> 4039.64]  is they scout
[4039.64 --> 4040.88]  all the different
[4040.88 --> 4042.06]  genetic testing labs
[4042.06 --> 4042.70]  and provide
[4042.70 --> 4044.02]  like a unified marketplace
[4044.02 --> 4045.08]  with all the information
[4045.08 --> 4045.70]  that you need
[4045.70 --> 4046.26]  for doctors
[4046.26 --> 4047.44]  to make a good decision.
[4047.68 --> 4048.58]  So that was really,
[4048.74 --> 4049.18]  really cool
[4049.18 --> 4050.04]  because RethinkDB
[4050.04 --> 4050.68]  is used,
[4050.90 --> 4052.80]  you know,
[4052.80 --> 4053.72]  it's used in a way
[4053.72 --> 4054.94]  that legitimately makes
[4054.94 --> 4055.92]  like people's lives
[4055.92 --> 4056.52]  a lot better.
[4057.22 --> 4058.42]  So we were very happy
[4058.42 --> 4058.98]  with that.
[4059.64 --> 4060.68]  Another company
[4060.68 --> 4062.72]  that uses RethinkDB now
[4062.72 --> 4064.06]  is Fidelity Investments.
[4064.40 --> 4064.74]  So, you know,
[4064.78 --> 4065.80]  the big Fidelity
[4065.80 --> 4066.42]  that we know
[4066.42 --> 4067.04]  that manages
[4067.04 --> 4068.40]  people's pension funds
[4068.40 --> 4068.82]  and stuff.
[4068.92 --> 4069.74]  So they rebuilt
[4069.74 --> 4072.50]  their website
[4072.50 --> 4073.56]  to kind of be
[4073.56 --> 4074.66]  a little bit more modern
[4074.66 --> 4075.66]  and they use RethinkDB
[4075.66 --> 4076.62]  to back, you know,
[4076.78 --> 4078.00]  tens of millions of users.
[4078.14 --> 4078.80]  That was really,
[4078.94 --> 4079.34]  really cool.
[4081.82 --> 4082.80]  Another company
[4082.80 --> 4083.22]  is Get,
[4083.28 --> 4084.32]  it's called Get Narrative.
[4084.32 --> 4085.24]  So it's a camera
[4085.24 --> 4086.38]  that people
[4086.38 --> 4088.10]  just wear all the time
[4088.10 --> 4089.18]  and they store metadata
[4089.18 --> 4090.14]  in RethinkDB.
[4090.34 --> 4091.14]  And now I believe
[4091.14 --> 4092.12]  that camera is used
[4092.12 --> 4093.26]  in many police departments
[4093.26 --> 4094.06]  around the world.
[4094.42 --> 4095.26]  So that's really cool
[4095.26 --> 4096.52]  because it's an interesting
[4096.52 --> 4097.46]  technical use case,
[4097.56 --> 4098.14]  but it also,
[4098.14 --> 4098.94]  like,
[4099.00 --> 4100.22]  really helps improve
[4100.22 --> 4101.92]  police officers' lives
[4101.92 --> 4102.90]  and, you know,
[4102.96 --> 4104.10]  regular people's lives.
[4104.44 --> 4105.58]  So when we see people
[4105.58 --> 4106.52]  pick up RethinkDB
[4106.52 --> 4107.18]  for these cool
[4107.18 --> 4108.36]  technical use cases
[4108.36 --> 4111.02]  and they build products
[4111.02 --> 4112.10]  that people use and love,
[4112.18 --> 4113.34]  that's always been very cool.
[4113.34 --> 4114.40]  And then once that happens,
[4114.44 --> 4115.14]  it's very easy.
[4116.32 --> 4116.82]  You know,
[4116.86 --> 4117.64]  the detraction
[4117.64 --> 4118.94]  kind of just picks up
[4118.94 --> 4119.74]  because people start
[4119.74 --> 4120.70]  seeing these examples.
[4121.50 --> 4121.60]  Nice.
[4122.66 --> 4123.10]  All right,
[4123.16 --> 4123.28]  well,
[4123.34 --> 4124.14]  let's do this.
[4124.18 --> 4124.70]  I want to set up
[4124.70 --> 4125.42]  a question for you.
[4125.50 --> 4125.94]  I'm going to give you
[4125.94 --> 4127.18]  the break to think about it.
[4128.12 --> 4128.78]  I'm going to have you
[4128.78 --> 4129.88]  address a naysayer.
[4130.26 --> 4130.98]  So, you know,
[4131.02 --> 4131.76]  there's a lot of neckbeards
[4131.76 --> 4132.26]  out there
[4132.26 --> 4133.64]  and I'll just play one.
[4134.28 --> 4134.88]  And I'll say,
[4134.88 --> 4138.08]  it's okay to experiment.
[4138.20 --> 4138.86]  New technologies,
[4139.04 --> 4140.48]  you have to stay up to date.
[4141.14 --> 4142.22]  But with your data
[4142.22 --> 4143.60]  and your data store,
[4144.24 --> 4145.48]  at the last place,
[4146.12 --> 4146.92]  you should be experimenting
[4146.92 --> 4147.80]  with new technologies.
[4147.98 --> 4148.42]  You should pick
[4148.42 --> 4149.44]  boring technologies,
[4150.12 --> 4150.76]  things that will
[4150.76 --> 4152.54]  persist your data reliably.
[4153.36 --> 4154.08]  And, you know,
[4154.12 --> 4155.54]  any NoSQL solutions
[4155.54 --> 4157.14]  or any new databases
[4157.14 --> 4158.46]  is just bad news.
[4158.92 --> 4159.28]  So,
[4159.40 --> 4160.62]  I'd like you to address
[4160.62 --> 4161.28]  that concern
[4161.28 --> 4162.26]  because I know it's out there.
[4163.10 --> 4164.00]  And I'll give you
[4164.00 --> 4165.18]  the break to think about it
[4165.18 --> 4166.70]  and we will have Slava
[4166.70 --> 4167.26]  address that
[4167.26 --> 4167.88]  on the other side.
[4169.70 --> 4171.24]  DigitalOcean has expanded
[4171.24 --> 4171.78]  their reach
[4171.78 --> 4172.54]  even further
[4172.54 --> 4173.60]  into Canada's startup
[4173.60 --> 4174.92]  and developer scene
[4174.92 --> 4175.48]  with the launch
[4175.48 --> 4176.54]  of Tor1.
[4176.94 --> 4178.06]  That's T-O-R-1,
[4178.42 --> 4179.44]  their first Canadian
[4179.44 --> 4180.04]  data center
[4180.04 --> 4181.10]  in Toronto.
[4181.64 --> 4182.18]  Head to
[4182.18 --> 4183.74]  DigitalOcean.com
[4183.74 --> 4184.56]  and use the code
[4184.56 --> 4185.20]  CHANGELOG
[4185.20 --> 4186.00]  to get a $10
[4186.00 --> 4186.88]  hosting credit
[4186.88 --> 4188.04]  when you sign up.
[4188.04 --> 4188.48]  Again,
[4188.90 --> 4190.10]  DigitalOcean.com
[4190.10 --> 4191.02]  use the code
[4191.02 --> 4191.62]  CHANGELOG
[4191.62 --> 4192.48]  to get a $10
[4192.48 --> 4193.40]  hosting credit
[4193.40 --> 4194.64]  when you sign up.
[4196.74 --> 4197.36]  All right,
[4197.40 --> 4197.86]  we're back.
[4197.98 --> 4198.32]  Slava,
[4198.46 --> 4199.14]  before the break,
[4199.22 --> 4199.96]  I set up a question
[4199.96 --> 4200.36]  for you.
[4200.46 --> 4201.18]  The naysayer
[4201.18 --> 4202.70]  who does not want
[4202.70 --> 4203.16]  to experiment
[4203.16 --> 4204.84]  with their data store,
[4204.94 --> 4206.32]  that's the most precious
[4206.32 --> 4207.10]  thing that we have
[4207.10 --> 4207.60]  is our data,
[4208.22 --> 4209.46]  and who says,
[4209.54 --> 4209.74]  you know,
[4209.82 --> 4210.46]  you really shouldn't
[4210.46 --> 4211.88]  be trying these,
[4212.00 --> 4212.62]  you know,
[4212.70 --> 4214.38]  newfangled data stores,
[4214.58 --> 4215.34]  especially with your
[4215.34 --> 4216.12]  production data.
[4216.74 --> 4217.50]  What do you say
[4217.50 --> 4218.08]  to that concern?
[4219.02 --> 4219.42]  Well,
[4219.48 --> 4220.62]  we work with a lot
[4220.62 --> 4221.24]  of users
[4221.24 --> 4222.82]  who use all kinds
[4222.82 --> 4223.76]  of different technologies,
[4223.76 --> 4224.58]  and we have a lot
[4224.58 --> 4225.22]  of friends
[4225.22 --> 4226.52]  who don't use
[4226.52 --> 4227.06]  RethinkDB,
[4227.48 --> 4227.88]  but, you know,
[4227.88 --> 4228.78]  they all build software.
[4229.26 --> 4229.96]  And one thing
[4229.96 --> 4230.68]  I can say
[4230.68 --> 4231.60]  about just the general
[4231.60 --> 4232.38]  trend of where
[4232.38 --> 4233.40]  software is going
[4233.40 --> 4234.26]  is that it's going
[4234.26 --> 4234.82]  toward more
[4234.82 --> 4235.92]  specialized tools.
[4236.68 --> 4236.74]  So,
[4236.94 --> 4238.04]  I've never seen
[4238.04 --> 4238.76]  an environment
[4238.76 --> 4240.46]  that was built
[4240.46 --> 4241.72]  in the last five years
[4241.72 --> 4242.72]  that uses a single
[4242.72 --> 4243.16]  database.
[4243.16 --> 4243.56]  So,
[4243.62 --> 4243.88]  back,
[4243.94 --> 4244.16]  you know,
[4244.22 --> 4244.94]  in the 90s,
[4245.24 --> 4245.82]  you'd very often
[4245.82 --> 4246.62]  just pick Oracle
[4246.62 --> 4247.16]  and everything
[4247.16 --> 4247.74]  would be built
[4247.74 --> 4248.16]  in Oracle
[4248.16 --> 4249.10]  and that would be it.
[4249.46 --> 4250.76]  But in modern environments,
[4250.88 --> 4251.62]  because the apps
[4251.62 --> 4252.90]  are getting so sophisticated,
[4253.22 --> 4254.34]  there's lots of different
[4254.34 --> 4256.32]  technologies in general,
[4256.44 --> 4257.82]  but also database technologies
[4257.82 --> 4258.86]  that are used
[4258.86 --> 4259.72]  for different reasons.
[4259.84 --> 4259.98]  So,
[4260.02 --> 4260.52]  for example,
[4260.94 --> 4262.00]  people use RethinkDB
[4262.00 --> 4264.22]  for the real-time
[4264.22 --> 4264.82]  functionality
[4264.82 --> 4265.80]  as a platform
[4265.80 --> 4266.42]  to build their
[4266.42 --> 4267.12]  real-time apps.
[4267.30 --> 4268.58]  They use Elasticsearch
[4268.58 --> 4269.66]  for fuzzy matching.
[4270.06 --> 4271.10]  They use Hadoop
[4271.10 --> 4271.64]  for,
[4271.82 --> 4272.32]  you know,
[4272.40 --> 4272.94]  for analytics.
[4273.08 --> 4273.18]  So,
[4273.24 --> 4273.74]  there's a lot of
[4273.74 --> 4274.44]  different database
[4274.44 --> 4275.04]  technologies
[4275.04 --> 4276.66]  that people will use.
[4277.04 --> 4277.20]  And,
[4277.32 --> 4277.46]  of course,
[4277.50 --> 4278.46]  they'll use a traditional
[4278.46 --> 4279.52]  relational database
[4279.52 --> 4280.34]  like Postgres
[4280.34 --> 4282.46]  for things
[4282.46 --> 4283.42]  where that makes sense,
[4283.50 --> 4284.50]  for asset compliance,
[4284.84 --> 4284.98]  you know,
[4285.00 --> 4286.04]  for financial stuff.
[4286.44 --> 4286.54]  So,
[4286.68 --> 4288.60]  the thing I'd say is
[4288.60 --> 4290.30]  that seems to be
[4290.30 --> 4291.26]  really where the world
[4291.26 --> 4291.78]  is going.
[4291.88 --> 4292.52]  It's going towards
[4292.52 --> 4293.36]  microservices.
[4293.60 --> 4294.30]  It's going towards,
[4294.42 --> 4294.98]  you know,
[4295.06 --> 4297.06]  using different technologies
[4297.06 --> 4297.90]  and different tools
[4297.90 --> 4298.50]  for the job
[4298.50 --> 4299.42]  where it makes sense.
[4299.88 --> 4299.98]  And,
[4300.12 --> 4300.42]  of course,
[4300.82 --> 4302.34]  caring about the data
[4302.34 --> 4303.58]  and data consistency
[4303.58 --> 4305.10]  is extremely important.
[4305.78 --> 4305.98]  So,
[4306.12 --> 4307.18]  what people very often
[4307.18 --> 4308.32]  do in real environments
[4308.32 --> 4309.16]  is they'll have
[4309.16 --> 4311.18]  one authoritative
[4311.18 --> 4312.10]  source of data
[4312.10 --> 4312.76]  which is
[4312.76 --> 4314.00]  a technology
[4314.00 --> 4314.56]  that they're really
[4314.56 --> 4315.42]  comfortable with.
[4315.50 --> 4315.60]  So,
[4315.66 --> 4316.06]  it could be
[4316.06 --> 4317.26]  HBase or HDFS.
[4317.62 --> 4318.88]  It could be Postgres.
[4319.00 --> 4319.46]  It could be
[4319.46 --> 4320.20]  whatever they want.
[4320.60 --> 4321.44]  And then they
[4321.44 --> 4322.54]  take these
[4322.54 --> 4323.76]  specialized databases
[4323.76 --> 4324.82]  and build around
[4324.82 --> 4326.42]  that authoritative
[4326.42 --> 4327.52]  source of information
[4327.52 --> 4328.44]  to help them
[4328.44 --> 4329.18]  build their apps.
[4329.24 --> 4329.80]  And then if something
[4329.80 --> 4330.44]  goes wrong,
[4330.82 --> 4331.46]  they still have
[4331.46 --> 4332.42]  their authoritative
[4332.42 --> 4333.24]  source of data.
[4333.34 --> 4333.44]  So,
[4333.50 --> 4334.12]  that's what I see
[4334.12 --> 4334.58]  happening.
[4335.74 --> 4336.62]  It's becoming
[4336.62 --> 4337.28]  very,
[4337.44 --> 4337.98]  very common.
[4338.12 --> 4338.58]  I haven't seen
[4338.58 --> 4339.18]  an environment
[4339.18 --> 4339.74]  where people
[4339.74 --> 4340.52]  don't do that.
[4340.92 --> 4341.30]  And I think
[4341.30 --> 4341.84]  that's kind of
[4341.84 --> 4342.62]  the market's
[4342.62 --> 4343.96]  response to this
[4343.96 --> 4345.20]  very valid concern
[4345.20 --> 4345.46]  of,
[4345.64 --> 4345.68]  hey,
[4345.80 --> 4346.58]  I really care
[4346.58 --> 4347.24]  about my data.
[4347.34 --> 4347.72]  I want to make
[4347.72 --> 4348.22]  sure everything
[4348.22 --> 4348.78]  goes right.
[4349.64 --> 4350.02]  I think that's
[4350.02 --> 4350.60]  a good response.
[4350.98 --> 4351.72]  I agree.
[4352.04 --> 4352.24]  You know,
[4352.28 --> 4353.06]  polyglot storage
[4353.06 --> 4354.90]  is a thing
[4354.90 --> 4356.60]  and specialized
[4356.60 --> 4357.66]  tools is
[4357.66 --> 4358.06]  definitely
[4358.06 --> 4360.14]  the trend.
[4361.02 --> 4362.42]  And I think
[4362.42 --> 4362.78]  that definitely
[4362.78 --> 4363.18]  addresses the
[4363.18 --> 4363.72]  concern of,
[4363.90 --> 4363.94]  well,
[4364.12 --> 4364.86]  I'm not going
[4364.86 --> 4365.58]  to put my
[4365.58 --> 4366.50]  most precious
[4366.50 --> 4367.62]  data in this
[4367.62 --> 4368.40]  thing that I
[4368.40 --> 4369.08]  don't trust yet.
[4369.12 --> 4369.44]  And it's like,
[4369.48 --> 4369.58]  well,
[4369.58 --> 4369.98]  you don't really
[4369.98 --> 4370.40]  have to.
[4370.50 --> 4371.48]  It can be a
[4371.48 --> 4372.42]  secondary storage
[4372.42 --> 4372.96]  or it can be
[4372.96 --> 4373.62]  for this specific
[4373.62 --> 4374.08]  use.
[4374.76 --> 4375.52]  And then I suppose
[4375.52 --> 4376.30]  over time you'd
[4376.30 --> 4377.50]  build up trust
[4377.50 --> 4379.18]  for that particular
[4379.18 --> 4379.90]  technology or
[4379.90 --> 4380.74]  lack of trust
[4380.74 --> 4381.10]  and then you
[4381.10 --> 4381.52]  move on to
[4381.52 --> 4381.96]  the next one.
[4382.34 --> 4382.66]  Yeah.
[4383.80 --> 4384.68]  I think that's
[4384.68 --> 4385.42]  pretty level-headed.
[4385.96 --> 4386.48]  I was hoping for
[4386.48 --> 4386.72]  something,
[4387.20 --> 4388.22]  can you be more
[4388.22 --> 4389.36]  divisive for us,
[4389.42 --> 4389.74]  please?
[4390.10 --> 4390.72]  All this level-headed
[4390.72 --> 4391.40]  answers are,
[4392.44 --> 4392.92]  I'm just kidding.
[4393.02 --> 4393.20]  Well,
[4393.24 --> 4394.20]  I think old-school
[4394.20 --> 4395.42]  long-polling databases
[4395.42 --> 4396.12]  are absolutely
[4396.12 --> 4396.94]  terrible and they
[4396.94 --> 4397.60]  should never be
[4397.60 --> 4398.24]  used for any
[4398.24 --> 4398.60]  reason.
[4399.60 --> 4400.20]  You know,
[4400.20 --> 4400.62]  and you should
[4400.62 --> 4401.58]  clearly use
[4401.58 --> 4402.88]  real-time reactive
[4402.88 --> 4403.74]  databases for
[4403.74 --> 4404.50]  everything even
[4404.50 --> 4405.66]  when it doesn't
[4405.66 --> 4406.26]  really make much
[4406.26 --> 4406.58]  sense.
[4408.04 --> 4408.36]  You're here.
[4408.72 --> 4409.08]  Perfect.
[4409.08 --> 4410.08]  So,
[4410.32 --> 4411.22]  for those who
[4411.22 --> 4411.70]  listen to the
[4411.70 --> 4412.36]  show regularly,
[4412.50 --> 4412.82]  they know we
[4412.82 --> 4413.36]  have some good
[4413.36 --> 4414.08]  closing questions
[4414.08 --> 4414.88]  and today we've
[4414.88 --> 4416.24]  prepared a special
[4416.24 --> 4417.90]  one literally just
[4417.90 --> 4418.18]  for you.
[4418.30 --> 4418.64]  We will never
[4418.64 --> 4419.52]  probably ask this
[4419.52 --> 4420.22]  question again unless
[4420.22 --> 4420.90]  we have a database
[4420.90 --> 4421.58]  expert on the
[4421.58 --> 4421.84]  show.
[4422.44 --> 4422.56]  You know,
[4422.64 --> 4423.04]  Jared and I like
[4423.04 --> 4423.76]  to hypothesize
[4423.76 --> 4424.26]  about the future
[4424.26 --> 4424.68]  when we have
[4424.68 --> 4425.38]  somebody like you
[4425.38 --> 4425.82]  on the show that
[4425.82 --> 4426.88]  can help us
[4426.88 --> 4427.50]  depict what that
[4427.50 --> 4428.12]  might look like.
[4428.76 --> 4429.68]  We ask questions
[4429.68 --> 4430.16]  like this.
[4430.22 --> 4430.36]  So,
[4430.50 --> 4431.42]  what is the next
[4431.42 --> 4432.70]  big thing in
[4432.70 --> 4433.18]  databases?
[4433.76 --> 4435.02]  The next big
[4435.02 --> 4435.60]  thing in
[4435.60 --> 4436.20]  databases?
[4436.20 --> 4438.50]  I think that
[4438.50 --> 4440.12]  so the
[4440.12 --> 4440.78]  polyglot
[4440.78 --> 4442.10]  storage is a
[4442.10 --> 4442.52]  huge,
[4442.52 --> 4443.06]  you know,
[4443.14 --> 4444.08]  huge trend that
[4444.08 --> 4444.74]  we see in every
[4444.74 --> 4445.42]  infrastructure.
[4446.20 --> 4446.92]  But what's going
[4446.92 --> 4447.54]  on is people
[4447.54 --> 4448.22]  very often,
[4448.38 --> 4448.66]  so the
[4448.66 --> 4449.16]  databases,
[4449.34 --> 4450.04]  different databases
[4450.04 --> 4451.38]  don't interoperate
[4451.38 --> 4452.44]  very well yet.
[4452.96 --> 4453.32]  So,
[4453.40 --> 4454.08]  people very often
[4454.08 --> 4454.70]  have to solve
[4454.70 --> 4455.24]  that problem
[4455.24 --> 4455.72]  themselves.
[4456.14 --> 4456.30]  So,
[4456.30 --> 4456.70]  I think the
[4456.70 --> 4457.26]  first thing that
[4457.26 --> 4457.82]  will happen in
[4457.82 --> 4458.50]  the short term
[4458.50 --> 4460.00]  is there will
[4460.00 --> 4461.06]  be much better
[4461.06 --> 4462.06]  interrupt tools
[4462.06 --> 4463.10]  between different
[4463.10 --> 4464.36]  databases.
[4464.36 --> 4465.94]  so it will
[4465.94 --> 4466.38]  be much,
[4466.52 --> 4467.00]  much easier
[4467.00 --> 4467.62]  to build
[4467.62 --> 4468.28]  these kinds
[4468.28 --> 4468.90]  of environments.
[4469.36 --> 4469.90]  The second
[4469.90 --> 4470.64]  thing I think
[4470.64 --> 4470.92]  that will
[4470.92 --> 4471.78]  happen is
[4471.78 --> 4473.56]  many,
[4473.72 --> 4474.24]  many more
[4474.24 --> 4475.00]  vendors will
[4475.00 --> 4475.70]  start offering
[4475.70 --> 4476.28]  real-time
[4476.28 --> 4477.38]  features because
[4477.38 --> 4478.74]  like once you
[4478.74 --> 4479.56]  experience a
[4479.56 --> 4480.36]  real-time app
[4480.36 --> 4481.06]  and once you
[4481.06 --> 4481.82]  see an
[4481.82 --> 4482.30]  infrastructure
[4482.30 --> 4483.38]  that uses
[4483.38 --> 4484.44]  real-time
[4484.44 --> 4484.94]  tools,
[4485.28 --> 4485.50]  it's,
[4485.88 --> 4486.18]  I don't know,
[4486.22 --> 4486.52]  it's sort of
[4486.52 --> 4486.88]  like if you
[4486.88 --> 4487.38]  remember when
[4487.38 --> 4488.08]  Ajax came
[4488.08 --> 4488.42]  along,
[4488.52 --> 4489.02]  like once you
[4489.02 --> 4489.64]  used a
[4489.64 --> 4490.28]  website that
[4490.28 --> 4490.84]  used it
[4490.84 --> 4492.10]  and really
[4492.10 --> 4492.66]  took advantage
[4492.66 --> 4493.06]  of it,
[4493.32 --> 4494.06]  it was hard
[4494.06 --> 4494.72]  to imagine
[4494.72 --> 4495.12]  what it
[4495.12 --> 4495.52]  even would
[4495.52 --> 4495.94]  be like
[4495.94 --> 4496.28]  to go
[4496.28 --> 4496.76]  back and
[4496.76 --> 4497.02]  I think
[4497.02 --> 4497.36]  the same
[4497.36 --> 4497.74]  thing is
[4497.74 --> 4498.08]  happening
[4498.08 --> 4498.84]  with real-time
[4498.84 --> 4499.50]  so I
[4499.50 --> 4500.32]  really fundamentally
[4500.32 --> 4501.08]  believe that
[4501.08 --> 4501.52]  many more
[4501.52 --> 4502.08]  tools will
[4502.08 --> 4502.62]  be built
[4502.62 --> 4503.64]  around solving
[4503.64 --> 4504.36]  problems for
[4504.36 --> 4505.04]  real-time apps
[4505.04 --> 4505.48]  and I think
[4505.48 --> 4506.20]  everything will
[4506.20 --> 4507.58]  shift to
[4507.58 --> 4507.98]  real-time
[4507.98 --> 4508.82]  applications on
[4508.82 --> 4509.34]  the web in
[4509.34 --> 4509.84]  the next few
[4509.84 --> 4510.18]  years.
[4511.46 --> 4512.36]  Side question,
[4512.52 --> 4513.10]  this one is
[4513.10 --> 4513.72]  for everybody.
[4514.28 --> 4514.94]  Do you remember
[4514.94 --> 4515.80]  the very first
[4515.80 --> 4516.90]  Ajax interaction
[4516.90 --> 4517.78]  that wowed you
[4517.78 --> 4518.48]  and what was
[4518.48 --> 4518.68]  it?
[4519.62 --> 4520.10]  Yes.
[4521.12 --> 4521.40]  Gmail.
[4522.64 --> 4522.90]  Oh,
[4522.94 --> 4523.18]  Gmail,
[4523.40 --> 4523.58]  okay.
[4523.58 --> 4524.56]  So Gmail
[4524.56 --> 4525.44]  wasn't that,
[4526.08 --> 4526.58]  Gmail was
[4526.58 --> 4527.06]  definitely
[4527.06 --> 4527.72]  impressive,
[4527.88 --> 4528.24]  but the one
[4528.24 --> 4528.86]  I was most
[4528.86 --> 4529.56]  impressed with
[4529.56 --> 4530.06]  is Google
[4530.06 --> 4530.62]  Suggest.
[4531.44 --> 4531.92]  Okay.
[4532.38 --> 4532.82]  Do you remember
[4532.82 --> 4533.06]  that?
[4533.16 --> 4533.50]  Like when you
[4533.50 --> 4534.70]  start typing
[4534.70 --> 4535.12]  your query
[4535.12 --> 4535.86]  and it suggests,
[4536.10 --> 4536.28]  yeah,
[4536.70 --> 4537.72]  that just blew
[4537.72 --> 4538.20]  me away.
[4538.62 --> 4538.84]  Also,
[4538.92 --> 4539.46]  Google Maps
[4539.46 --> 4540.10]  was probably
[4540.10 --> 4540.70]  the closest
[4540.70 --> 4541.32]  second one.
[4541.36 --> 4541.78]  That's true.
[4542.00 --> 4542.46]  Google Maps
[4542.46 --> 4542.72]  too.
[4542.84 --> 4543.32]  I must be
[4543.32 --> 4543.90]  easy to please
[4543.90 --> 4544.30]  because I
[4544.30 --> 4544.78]  remember way
[4544.78 --> 4545.26]  back in the
[4545.26 --> 4545.98]  day when
[4545.98 --> 4546.86]  Dig would
[4546.86 --> 4547.24]  let you
[4547.24 --> 4548.10]  upvote without
[4548.10 --> 4548.68]  reloading the
[4548.68 --> 4549.06]  page.
[4549.06 --> 4550.80]  like that
[4550.80 --> 4551.14]  was my
[4551.14 --> 4551.44]  first,
[4551.44 --> 4551.94]  that was my
[4551.94 --> 4552.46]  very first
[4552.46 --> 4552.94]  Ajax.
[4553.02 --> 4553.28]  I was like,
[4553.34 --> 4553.72]  why didn't the
[4553.72 --> 4554.36]  page reload?
[4554.94 --> 4555.56]  I had no idea
[4555.56 --> 4556.20]  what had happened
[4556.20 --> 4556.80]  at that point
[4556.80 --> 4558.02]  and that was,
[4558.18 --> 4558.68]  that's when I
[4558.68 --> 4560.10]  knew Web 2.0.
[4560.42 --> 4561.60]  I knew Web 2.0
[4561.60 --> 4562.06]  was here,
[4562.78 --> 4564.36]  but definitely
[4564.36 --> 4564.96]  not as impressive
[4564.96 --> 4566.60]  as any of those
[4566.60 --> 4567.12]  things you all
[4567.12 --> 4567.96]  got impressed by.
[4568.12 --> 4569.20]  So I'm easy
[4569.20 --> 4569.70]  to please.
[4569.84 --> 4570.48]  Let's talk about
[4570.48 --> 4571.14]  open source
[4571.14 --> 4571.84]  radar.
[4571.84 --> 4573.50]  So, Slava,
[4573.62 --> 4574.06]  if you had a
[4574.06 --> 4574.66]  free weekend
[4574.66 --> 4576.54]  and it was
[4576.54 --> 4576.84]  you and your
[4576.84 --> 4577.40]  text editor
[4577.40 --> 4577.82]  and you had
[4577.82 --> 4578.30]  some code
[4578.30 --> 4578.76]  out there,
[4579.26 --> 4579.68]  it wasn't
[4579.68 --> 4580.02]  your code,
[4580.10 --> 4580.58]  someone else's
[4580.58 --> 4580.86]  code,
[4581.60 --> 4582.12]  what would it
[4582.12 --> 4582.60]  be that you'd
[4582.60 --> 4583.88]  want to dig
[4583.88 --> 4584.68]  in, read
[4584.68 --> 4585.16]  it, play
[4585.16 --> 4585.58]  with it?
[4586.28 --> 4586.96]  What's on your
[4586.96 --> 4587.46]  open source
[4587.46 --> 4588.10]  radar right now?
[4589.26 --> 4590.10]  So I'll tell you
[4590.10 --> 4591.00]  what I have been
[4591.00 --> 4591.74]  digging into over
[4591.74 --> 4592.26]  the past few
[4592.26 --> 4592.58]  weekends.
[4592.74 --> 4593.38]  So I'm really,
[4593.62 --> 4594.12]  really excited
[4594.12 --> 4595.08]  about new
[4595.08 --> 4596.20]  language advancements.
[4596.68 --> 4597.12]  So I've been
[4597.12 --> 4598.24]  looking at C++.
[4599.14 --> 4600.56]  So C++11 came
[4600.56 --> 4601.34]  out a while ago,
[4601.34 --> 4602.02]  but now people
[4602.02 --> 4602.68]  are talking about
[4602.68 --> 4604.30]  C++14,
[4604.56 --> 4604.92]  it's getting
[4604.92 --> 4605.72]  kind of better
[4605.72 --> 4606.28]  support,
[4606.90 --> 4607.84]  and the next
[4607.84 --> 4608.50]  few iterations.
[4608.72 --> 4609.14]  So I'm really
[4609.14 --> 4610.02]  excited about that.
[4610.08 --> 4610.58]  I've been playing
[4610.58 --> 4611.04]  with that.
[4611.40 --> 4611.86]  I'm excited
[4611.86 --> 4612.92]  about ES6
[4612.92 --> 4613.98]  and ES7,
[4614.58 --> 4616.04]  although ES7
[4616.04 --> 4616.60]  is still in
[4616.60 --> 4617.34]  planning stages.
[4617.46 --> 4618.34]  So if you're
[4618.34 --> 4619.14]  really interested,
[4619.30 --> 4619.94]  there is a
[4619.94 --> 4620.66]  wonderful cross
[4620.66 --> 4621.80]  compiler called
[4621.80 --> 4622.58]  Babel that will
[4622.58 --> 4623.78]  take kind of
[4623.78 --> 4625.50]  future ES6 or
[4625.50 --> 4626.30]  7 code and
[4626.30 --> 4626.90]  compile it to
[4626.90 --> 4627.50]  ES5.
[4627.68 --> 4628.24]  That's been
[4628.24 --> 4629.06]  super exciting.
[4629.22 --> 4629.84]  I've been playing
[4629.84 --> 4630.60]  with that a lot.
[4631.34 --> 4632.74]  And it's a lot
[4632.74 --> 4633.26]  of fun because
[4633.26 --> 4634.06]  it makes JavaScript
[4634.06 --> 4634.86]  code dramatically
[4634.86 --> 4635.32]  easier.
[4635.78 --> 4636.32]  And the last
[4636.32 --> 4636.74]  thing, so I
[4636.74 --> 4637.18]  haven't actually
[4637.18 --> 4637.96]  played with this,
[4638.02 --> 4638.38]  but I've been
[4638.38 --> 4639.00]  watching it
[4639.00 --> 4639.76]  forever and
[4639.76 --> 4640.72]  I really want
[4640.72 --> 4642.12]  to just carve
[4642.12 --> 4642.92]  out a weekend
[4642.92 --> 4644.18]  and build
[4644.18 --> 4644.64]  something,
[4644.76 --> 4645.28]  is the
[4645.28 --> 4645.60]  programming
[4645.60 --> 4646.26]  language called
[4646.26 --> 4647.50]  Rust, which
[4647.50 --> 4648.22]  is supposed to
[4648.22 --> 4648.74]  be the next
[4648.74 --> 4649.76]  generation systems
[4649.76 --> 4650.90]  language that
[4650.90 --> 4651.36]  will kind of
[4651.36 --> 4652.10]  maybe hopefully
[4652.10 --> 4653.08]  replace or
[4653.08 --> 4653.96]  augment C++.
[4653.96 --> 4655.22]  So these
[4655.22 --> 4655.84]  would be my
[4655.84 --> 4656.52]  picks.
[4656.82 --> 4657.88]  And I guess
[4657.88 --> 4659.10]  I'm always a
[4659.10 --> 4659.92]  programming language
[4659.92 --> 4660.18]  guy.
[4660.30 --> 4660.82]  I really like
[4660.82 --> 4661.66]  programming languages
[4661.66 --> 4662.42]  and playing with
[4662.42 --> 4662.70]  them and
[4662.70 --> 4663.28]  experimenting.
[4663.68 --> 4664.26]  So that's what
[4664.26 --> 4664.90]  I typically
[4664.90 --> 4665.42]  look at.
[4666.42 --> 4667.06]  All right,
[4667.08 --> 4667.64]  next question
[4667.64 --> 4667.98]  for you.
[4668.02 --> 4669.16]  We actually
[4669.16 --> 4669.72]  introduced this
[4669.72 --> 4671.16]  question maybe
[4671.16 --> 4671.76]  for the first
[4671.76 --> 4672.16]  time on the
[4672.16 --> 4673.04]  show last
[4673.04 --> 4673.70]  episode with
[4673.70 --> 4673.94]  Mitchell.
[4674.12 --> 4674.80]  So since
[4674.80 --> 4675.40]  you're similar
[4675.40 --> 4676.86]  in nature to
[4676.86 --> 4677.72]  Mitchell, we'll
[4677.72 --> 4678.12]  ask you the
[4678.12 --> 4678.68]  same question,
[4678.74 --> 4679.92]  which is, we
[4679.92 --> 4680.24]  call it our
[4680.24 --> 4680.68]  super secret
[4680.68 --> 4681.12]  question.
[4681.12 --> 4681.82]  So what's
[4681.82 --> 4682.40]  something super
[4682.40 --> 4683.76]  secret no one
[4683.76 --> 4684.48]  else knows about,
[4684.60 --> 4685.12]  something that
[4685.12 --> 4686.08]  either you,
[4686.50 --> 4686.98]  Rethink, is
[4686.98 --> 4688.58]  doing, something
[4688.58 --> 4689.62]  that not many
[4689.62 --> 4690.18]  people know about
[4690.18 --> 4690.86]  or no one knows
[4690.86 --> 4691.24]  about that you
[4691.24 --> 4691.70]  could share here
[4691.70 --> 4692.00]  on the show
[4692.00 --> 4692.34]  today?
[4693.12 --> 4693.96]  So the one
[4693.96 --> 4694.90]  thing that we're
[4694.90 --> 4695.66]  doing at Rethink
[4695.66 --> 4696.44]  DB that not
[4696.44 --> 4697.38]  many people know
[4697.38 --> 4698.04]  about, which I
[4698.04 --> 4698.66]  think will blow
[4698.66 --> 4700.46]  people away, is
[4700.46 --> 4701.56]  we're building a
[4701.56 --> 4702.24]  layer on top of
[4702.24 --> 4702.96]  Rethink DB that
[4702.96 --> 4703.86]  will allow people,
[4704.08 --> 4704.48]  and it's an
[4704.48 --> 4705.70]  open source layer,
[4705.82 --> 4706.36]  that will allow
[4706.36 --> 4707.74]  people to build
[4707.74 --> 4708.24]  real-time
[4708.24 --> 4709.24]  applications without
[4709.24 --> 4710.12]  building any
[4710.12 --> 4710.98]  back-end code.
[4711.56 --> 4712.20]  And we're
[4712.20 --> 4712.96]  super excited
[4712.96 --> 4713.88]  about it because
[4713.88 --> 4714.90]  Rethink DB is
[4714.90 --> 4715.62]  very easy to
[4715.62 --> 4717.70]  get started with,
[4717.78 --> 4718.32]  it's easy to
[4718.32 --> 4718.94]  build real-time
[4718.94 --> 4720.42]  apps, but there's
[4720.42 --> 4721.14]  still quite a bit
[4721.14 --> 4721.82]  of boilerplate
[4721.82 --> 4722.48]  people have to
[4722.48 --> 4723.16]  figure out, like
[4723.16 --> 4723.56]  they have to
[4723.56 --> 4724.28]  figure out how
[4724.28 --> 4725.78]  do I hook up
[4725.78 --> 4727.14]  my Node.js to
[4727.14 --> 4727.82]  Rethink DB and
[4727.82 --> 4728.62]  WebSockets in
[4728.62 --> 4729.34]  the browser, how
[4729.34 --> 4730.14]  do I do identity
[4730.14 --> 4730.96]  management, how
[4730.96 --> 4731.24]  do I do
[4731.24 --> 4732.42]  authentication, like
[4732.42 --> 4732.86]  all these really
[4732.86 --> 4733.70]  common questions.
[4734.24 --> 4735.12]  So we're building
[4735.12 --> 4735.98]  a platform that
[4735.98 --> 4736.90]  will make that
[4736.90 --> 4738.72]  dramatically easier
[4738.72 --> 4739.36]  and people will
[4739.36 --> 4740.22]  be able to get
[4740.22 --> 4741.12]  started and build
[4741.12 --> 4741.92]  their React or
[4741.92 --> 4742.90]  Angular apps that
[4742.90 --> 4743.70]  are real-time,
[4744.18 --> 4745.08]  super engaging
[4745.08 --> 4747.20]  experiences without
[4747.20 --> 4749.00]  writing any
[4749.00 --> 4749.74]  back-end code.
[4750.00 --> 4750.58]  And then as
[4750.58 --> 4751.12]  their app gets
[4751.12 --> 4751.86]  more complicated
[4751.86 --> 4752.48]  and they need
[4752.48 --> 4754.20]  more functionality,
[4754.54 --> 4755.02]  they need to do
[4755.02 --> 4755.84]  more, they can
[4755.84 --> 4756.86]  start incrementally
[4756.86 --> 4757.68]  adding back-end
[4757.68 --> 4758.52]  code and because
[4758.52 --> 4759.30]  it's built on top
[4759.30 --> 4759.96]  of Rethink DB,
[4760.66 --> 4761.62]  they'll get a
[4761.62 --> 4762.26]  full-featured
[4762.26 --> 4763.54]  database to keep
[4763.54 --> 4764.22]  extending their
[4764.22 --> 4764.72]  application.
[4764.72 --> 4765.52]  So we've been
[4765.52 --> 4766.36]  designing this with
[4766.36 --> 4766.80]  some of our
[4766.80 --> 4767.66]  community members.
[4767.90 --> 4768.64]  It's in progress
[4768.64 --> 4769.12]  right now.
[4769.18 --> 4769.60]  We'll hopefully
[4769.60 --> 4770.54]  ship it in about
[4770.54 --> 4771.14]  eight weeks.
[4771.62 --> 4772.10]  We're super
[4772.10 --> 4772.96]  excited about it.
[4773.00 --> 4774.02]  This project, it
[4774.02 --> 4774.60]  doesn't sound too
[4774.60 --> 4775.28]  impressive because it
[4775.28 --> 4775.98]  doesn't even have a
[4775.98 --> 4777.64]  name yet, but I
[4777.64 --> 4778.46]  think when it comes
[4778.46 --> 4779.50]  out, people will be
[4779.50 --> 4780.62]  really excited about
[4780.62 --> 4780.78]  it.
[4780.80 --> 4781.62]  So I'm really looking
[4781.62 --> 4782.34]  forward to it.
[4782.94 --> 4783.92]  Is there anything we
[4783.92 --> 4784.54]  can put in the show
[4784.54 --> 4785.28]  notes for a link?
[4785.64 --> 4786.44]  Anything to share
[4786.44 --> 4787.70]  yet on the web?
[4788.34 --> 4789.18]  Yes, actually the
[4789.18 --> 4790.64]  GraphQL issue, at the
[4790.64 --> 4791.48]  end of it, there's a
[4791.48 --> 4792.30]  bit of a discussion
[4792.30 --> 4793.30]  about this and I
[4793.30 --> 4795.02]  can give you a link
[4795.02 --> 4795.98]  to the specific
[4795.98 --> 4797.44]  comment that covers
[4797.44 --> 4797.76]  this.
[4797.96 --> 4798.10]  Okay.
[4798.16 --> 4798.74]  But there's not a
[4798.74 --> 4799.18]  whole lot of
[4799.18 --> 4799.92]  information there.
[4800.02 --> 4800.74]  It's being designed.
[4800.86 --> 4801.52]  It's not designed
[4801.52 --> 4802.22]  openly yet.
[4802.90 --> 4803.24]  Awesome.
[4803.32 --> 4803.70]  I'll make a note
[4803.70 --> 4803.86]  of that.
[4803.92 --> 4804.58]  We definitely have
[4804.58 --> 4805.24]  the support
[4805.24 --> 4806.58]  Facebook's GraphQL
[4806.58 --> 4809.00]  support issue in
[4809.00 --> 4809.22]  there.
[4809.54 --> 4810.94]  So we'll put it in
[4810.94 --> 4811.48]  the show notes and
[4811.48 --> 4812.08]  we'll add the
[4812.08 --> 4812.92]  comments as well
[4812.92 --> 4813.68]  that talks about
[4813.68 --> 4813.96]  that.
[4814.20 --> 4814.48]  Okay.
[4814.80 --> 4815.48]  Sounds cool, man.
[4816.24 --> 4817.92]  Well, Slava, it's
[4817.92 --> 4819.44]  always good to have
[4819.44 --> 4820.94]  a repeat guest,
[4821.32 --> 4822.22]  getting a chance to
[4822.22 --> 4822.78]  catch back with
[4822.78 --> 4823.00]  you.
[4823.20 --> 4823.78]  Like we said
[4823.78 --> 4824.38]  early in the show,
[4824.50 --> 4825.20]  Jared and I weren't
[4825.20 --> 4825.78]  on the original
[4825.78 --> 4826.06]  show.
[4826.22 --> 4827.44]  So, Andrew, if for
[4827.44 --> 4828.12]  some reason you're
[4828.12 --> 4828.48]  listening to the
[4828.48 --> 4829.92]  show, I don't know
[4829.92 --> 4830.40]  if you listen to the
[4830.40 --> 4831.02]  changelog anymore or
[4831.02 --> 4832.80]  not, but episode
[4832.80 --> 4833.64]  114 was awesome.
[4833.74 --> 4834.26]  So thank you for
[4834.26 --> 4835.06]  that and thank you,
[4835.12 --> 4835.62]  Slava, for coming
[4835.62 --> 4836.62]  back on the show to
[4836.62 --> 4838.38]  not just catch us up
[4838.38 --> 4839.36]  with Rethink and what
[4839.36 --> 4839.94]  you're doing there,
[4839.96 --> 4841.34]  but also all the
[4841.34 --> 4841.84]  wealth of knowledge
[4841.84 --> 4842.54]  you bring to
[4842.54 --> 4843.96]  software development,
[4844.14 --> 4845.12]  databases, open
[4845.12 --> 4847.04]  source, and even
[4847.04 --> 4848.10]  your CEO hat where
[4848.10 --> 4849.18]  you kind of help us
[4849.18 --> 4850.44]  navigate the waters
[4850.44 --> 4851.42]  of the evil VC.
[4852.22 --> 4853.48]  Thank you guys so
[4853.48 --> 4854.32]  much for having me.
[4855.00 --> 4855.96]  And obviously we
[4855.96 --> 4857.12]  thank our sponsors,
[4857.52 --> 4858.42]  CodeChip, Braintree,
[4858.84 --> 4859.76]  Harvest, and Digital
[4859.76 --> 4860.50]  Ocean for making this
[4860.50 --> 4861.76]  show possible, and
[4861.76 --> 4863.04]  we would never ever
[4863.04 --> 4863.90]  end a show, and
[4863.90 --> 4864.50]  maybe we have in the
[4864.50 --> 4865.04]  past, but we're never
[4865.04 --> 4865.64]  going to do it again
[4865.64 --> 4866.56]  without thanking our
[4866.56 --> 4867.12]  awesome listeners.
[4867.54 --> 4868.24]  Without you, it
[4868.24 --> 4868.76]  wouldn't be possible
[4868.76 --> 4869.54]  to do this show, so
[4869.54 --> 4870.34]  we really appreciate
[4870.34 --> 4870.90]  your support.
[4871.34 --> 4873.30]  Also, our members, we
[4873.30 --> 4874.42]  appreciate your support,
[4875.00 --> 4876.56]  and that's it, so
[4876.56 --> 4876.96]  let's say goodbye.
[4876.96 --> 4878.08]  Goodbye.
[4879.18 --> 4879.80]  Goodbye.
[4882.80 --> 4884.48]  The dramatic pause.
[4884.48 --> 4906.44]  EARLY
[4906.44 --> 4936.42]  Thank you.
