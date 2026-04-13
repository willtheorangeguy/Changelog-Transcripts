[0.00 → 1.54] I'm Christopher Allen.
[1.86 → 2.88] And I'm Julie Moronic.
[3.28 → 5.16] And you're listening to The Changelog.
[14.12 → 15.12] Welcome back, everyone.
[15.24 → 18.06] This is The Changelog, and I'm your host, Adam Stekowiak.
[18.18 → 20.44] This is episode 198.
[21.00 → 24.10] Got a great show lined up today talking about Haskell, the programming language.
[24.10 → 30.10] We talked to Chris Allen and Julie Moronic about Haskell, about their book, Haskell Programming.
[30.84 → 33.00] We talked about their passion for this awesome language.
[33.16 → 38.32] We talked about also Julie's path to Haskell because Julie, in this case, is a beginner.
[38.52 → 41.40] She was brought to Haskell and also programming from Chris.
[41.72 → 44.34] They have this mentor-mentee relationship.
[44.50 → 46.14] They're also co-authoring this book together.
[46.36 → 48.22] Really great deep dive into this language.
[48.98 → 50.78] We had four sponsors for the show today.
[50.78 → 54.86] Total, Linde, Upbeat, and True sight Pulse.
[55.48 → 59.50] Our first sponsor for the show today is our friends at Total.
[59.86 → 63.58] Now, if you're new to the show, let me tell you, we love Total.
[63.72 → 66.98] If you've been listening for a while now, you know that we love Total.
[67.46 → 72.40] Total is an exclusive network of top freelance software developers and designers.
[72.98 → 79.18] Top companies every single day rely on Total freelancers for their most mission-critical projects.
[79.18 → 87.14] And one of the things we love about Total is that it's this worldwide community of engineers and designers that just love to enrich the community.
[87.72 → 97.68] As a Total engineer or designer, you'll have the flexibility to travel the world, be able to blog on their blog, be able to apply for open-source grants and contribute back to things you really care about.
[97.94 → 99.70] Head to TopTal.com to learn more.
[99.82 → 103.18] That's T-O-P-T-A-L.com to learn more.
[103.18 → 108.20] Or for a more personal introduction, email me, Adam at changelaw.com.
[108.50 → 111.20] I'd love to help you take your first step with Total.
[111.44 → 112.90] And now, on to the show.
[118.80 → 120.68] Everyone, we got an awesome show today.
[121.50 → 123.92] Jared, this one started off as many shows.
[124.00 → 127.08] I said this is the last couple shows, but it started off with an issue.
[127.08 → 136.14] I think the issue number was 384 from Zach, I think, Manny, and I'm not really sure if that's exactly it.
[136.16 → 145.98] But we got Chris Allen here, and we got Julie Morawiecki here talking about Haskell programming a book, a language, obviously, and a lot of fun for beginners.
[146.32 → 152.30] But, Jared, what do you think about issues always spun in these great shows, hopefully, for our listeners?
[152.30 → 161.02] Well, I love it because there's no better way to know that we're specifically treating the topics that our audience is interested in.
[161.92 → 171.06] And we've had Haskell brought up a couple of times as requests, and we just have never had an opportunity to discuss the language specifically.
[171.28 → 174.08] And this particular issue wasn't open too long ago.
[174.08 → 183.80] It was like January 31st, but there was like three or four immediate thumbs-ups and testimonies that learning Haskell was a lot easier with this particular book.
[184.52 → 192.72] And so, yeah, it was a good opportunity to have Julie and Chris come on and talk to us about it.
[193.44 → 195.80] I guess with that, Chris, Julie, welcome to the show.
[196.74 → 197.34] Thank you.
[197.42 → 198.08] Happy to be here.
[198.50 → 198.90] Thanks.
[198.90 → 208.36] So maybe for – it's a little easy here because you've got a man and a woman, but for separation of voices, let's get a couple introductions out of the way.
[208.50 → 212.36] Chris, maybe give us a brief introduction to who you are, and Julie, we'll follow up with you.
[213.52 → 220.72] So I'm Chris Allen, and I'm a working programmer that has worked mostly in small, medium-sized businesses and startups.
[222.18 → 224.44] I'm just a working programmer.
[225.44 → 226.36] And Julie, what about you?
[226.36 → 235.88] Well, my name is Julie Moroni, and I am not a working programmer, or at least I wasn't before I met Chris.
[236.20 → 239.86] And I was a teacher and a linguist.
[240.74 → 246.34] And so programming is all pretty new to me in the world of programmers.
[246.34 → 257.14] Maybe the best start would be to just kind of pry a bit more out of your backgrounds and just quoting you, Julie, in your About section for the book.
[257.14 → 265.46] And so just kind of to overarch the long conversation we'll have here today for the listeners, we're going to talk about Haskell, obviously.
[265.82 → 268.20] Also, this book they've written together called Haskell Programming.
[268.50 → 278.72] And just in general, the path to becoming a programmer, going for beginner, going from the background, Julie, you've had to being a beginner programmer.
[278.72 → 279.16] Right.
[279.16 → 281.00] And this path you've taken.
[281.20 → 288.36] But this book, as you've said, and I'm quoting you, this book developed out of the mentor-mentee relationship that you and Chris have.
[288.90 → 289.34] Yes.
[289.40 → 296.78] Out of your dialogues, out of your friendship and your commitment to sharing all the things you've learned in this path, and you and Chris together with as many people as possible.
[296.78 → 302.00] So I think it's kind of interesting to sort of like paint the picture of your perspectives.
[302.22 → 304.68] It sounds like you've got this.
[305.28 → 314.66] And I just put it in parentheses here for us behind the scenes, but I put Julie, you are the beginner, and I put Chris, the professional, because you both say those things in your About section for the book.
[314.72 → 325.32] But maybe we can kick off with just some backgrounds, a little deeper, kind of where each of you kind of maybe, and maybe Julie, you're a little sooner rather than Chris, but where you each picked up programming.
[325.32 → 327.94] Like, what got you into being a developer?
[328.76 → 328.92] Okay.
[329.18 → 333.52] I'll start, because mine is the most recent development.
[334.06 → 338.78] I just, I was never really interested in programming at all.
[338.90 → 349.46] I mean, when I was in linguistics graduate school, there was, this was back in the late 90s, and there was starting to be some interest in, like, computational linguistics.
[349.72 → 354.38] Well, not just starting, but at our school, there was starting to be a lot of interest in computational linguistics.
[354.38 → 359.86] And people tried to get me interested in programming, and I just was always really resistant to it.
[360.16 → 362.46] I'm not sure why exactly.
[362.68 → 368.90] But then in a couple of years ago, in 2014, I met Chris on Twitter.
[368.90 → 379.10] And Chris was really excited about the fact that I have a background in linguistics and tried to, well, did, not tried.
[379.44 → 388.88] He did persuade me to learn Haskell because he wanted me to become interested with him in natural language processing.
[388.88 → 393.16] So, I was still pretty resistant for quite some time.
[393.32 → 398.16] But then Haskell itself just started to become interesting to me as a language.
[399.00 → 409.38] And then as you start to actually, for me anyway, as I started to get some familiarity with Haskell, and then it started to become exciting.
[409.38 → 416.62] Like, it started to become exciting for me to be able to do all kinds of things.
[416.70 → 424.34] Like, I just started my blog with Haskell now, and so I had to learn about how to get things on a server and stuff like that.
[424.38 → 425.52] And it was all really exciting for me.
[425.58 → 434.50] And I know that sounds sort of, sort of, oh, Haskell is a Haskell is a.
[434.50 → 434.90] Yeah.
[435.14 → 436.98] It's, it's a static site generator.
[437.30 → 439.94] It's, the name is actually a riff off of Jekyll.
[440.36 → 440.38] So.
[440.70 → 440.86] Oh, nice.
[441.08 → 441.70] That made sense.
[441.96 → 442.28] Yeah.
[442.38 → 442.54] Yeah.
[442.54 → 444.80] It's a it's a site generator written in Haskell.
[444.98 → 447.84] And so it's, anyway, I just started using that for my blog.
[447.86 → 449.60] So I had to learn what a server was and stuff like that.
[449.60 → 451.94] And being able to do those things now is really exciting for me.
[451.94 → 461.12] But really five years ago, if you'd asked me if I was ever interested in, you know, learning about servers, I would have said, absolutely not.
[461.60 → 461.74] So.
[462.98 → 463.82] I have to be honest with you.
[463.82 → 469.76] I talk to people that they learned that I do this show and Jared and I do what we do around software development.
[469.76 → 472.26] And these are people who have never touched it.
[472.38 → 476.32] Educated people, teachers, you know, you know, smart people.
[476.76 → 479.64] But, you know, they, they look at me, and they say, what's a server?
[479.78 → 480.46] Like, what does a server do?
[480.48 → 483.46] And I just, I fumble with even trying to tell them exactly what a server does.
[483.50 → 484.66] It's like, its server serves.
[484.66 → 492.16] It's, I feel like the guy in Pink Panther, you know, you're the trainer who trains, like trainers train and a server serve.
[492.16 → 495.20] But I'm with you on the whole deploying to a server.
[495.28 → 496.56] It seems like this black box.
[497.04 → 497.70] It does.
[497.70 → 502.72] Yes. And, you know, like Chris last week, last weekend, he was helping me get this started.
[503.06 → 507.28] And, you know, he said, okay, so we're going to, you know, set up your server now.
[507.28 → 508.26] And so that was fine.
[508.40 → 510.62] So I have this account with AWS now.
[510.90 → 512.24] So big time, right?
[512.44 → 517.62] So, and then he was, and then he was talking about Nginx and Nginx is your server.
[517.62 → 518.64] And I was like, well, wait a second.
[518.64 → 520.12] I thought this other thing was the server.
[520.24 → 523.28] He's like, oh, well, so there are two things called server.
[524.12 → 524.44] Right.
[524.88 → 530.56] And, and so he was explaining to me how all of this works and, and it actually is fascinating.
[530.68 → 531.40] I don't know why.
[534.34 → 534.94] I don't know.
[534.98 → 540.28] I've always been kind of more like, I really like to be outside and more of an outdoors kind of person.
[540.28 → 547.32] And so I think I just had this resistance to spending a lot of time sitting in front of a computer, but there's a lot of fun stuff you can do.
[547.32 → 549.04] And so I'm glad I got into it.
[549.04 → 550.26] All right.
[550.26 → 552.22] Let's turn to Chris then, Chris, for your background.
[552.92 → 555.62] You'd mentioned that you're, you've been professionally programming for a while.
[555.70 → 562.82] Kind of give us a take us as far back as you have to go to help us understand where it came from for you.
[562.86 → 566.70] Like when did you get interested in technology and software development and programming?
[566.80 → 567.94] What was it for you to got you in there?
[568.46 → 570.14] Well, I mean, technology is super early.
[570.26 → 574.68] My, I don't know if you remember, but do you remember those arcade style joysticks for the NEW?
[575.08 → 575.26] Yeah.
[575.42 → 575.66] Oh yeah.
[575.94 → 578.14] Those were a lot easier for a three-year-old to use.
[578.14 → 580.82] So that's how my dad got me started on, on the Nintendo.
[581.68 → 585.46] Um, so technology started then programming started later.
[585.46 → 587.02] I basically ran out of games to play.
[587.12 → 588.26] I'm on the DOS computer.
[588.74 → 594.02] My dad had set me up with, and I was complaining about having run out of games to play.
[594.44 → 600.14] So he handed me a floppy in this really thick AT&T manual for GW basic and told me to make my own games.
[600.54 → 602.20] And eventually I did figure it out.
[602.24 → 606.40] But the problem is playing your own text adventure games, kind of boring because you already know all the puzzle answers.
[606.66 → 607.92] So that was kind of a problem.
[607.92 → 608.32] Yeah.
[608.90 → 610.06] You got to play somebody else's game.
[610.40 → 610.58] Yeah.
[610.74 → 611.10] Yeah.
[611.36 → 612.30] Yeah, exactly.
[612.64 → 616.20] If only, you know, I'd had a modem, maybe I could have found a game.
[616.44 → 619.14] But, um, that, that's where that started.
[619.58 → 624.28] Uh, I didn't really get serious about programming until I started having more success with it.
[624.28 → 628.94] I'd spent a lot of time kinds of fumbling with C and Linux when I was in middle school.
[629.70 → 632.82] And, um, I'd learned a lot about Linux.
[632.82 → 634.70] It didn't get too far with C.
[634.70 → 638.78] And where I really started kind of being able to do things was actually with Common Lisp.
[639.58 → 645.06] And, uh, eventually that translated after high school into me wanting to work as a programmer.
[645.06 → 647.92] Because I couldn't really imagine enjoying myself doing anything else.
[647.92 → 651.74] I wonder, like for me, because I never enjoyed playing video games.
[651.82 → 654.64] I wonder if that's part of why I was resistant to like learning how to program.
[654.64 → 660.92] I was thinking about that because, you know, we ask a lot of people what they got, how they
[660.92 → 663.92] got into programming who come on the show and a surprising amount.
[663.92 → 665.30] It starts with video games.
[665.44 → 666.06] I was going to say that.
[666.10 → 666.32] Yeah.
[666.40 → 666.70] Yeah.
[666.70 → 668.54] It's like some sort of game got them in there.
[668.62 → 671.96] Some sort of hackability to it that made them want to push the boundaries.
[671.96 → 676.54] And I noted in your about, Julie, that you actually said you were never really into games.
[677.22 → 678.08] No, I don't.
[678.16 → 679.36] I don't play video games at all.
[679.42 → 681.14] And I mean, I don't have anything against them.
[681.20 → 683.76] I don't want people to think I'm like judging them for playing video games.
[683.76 → 684.84] Cause that's what people always think.
[684.86 → 689.26] And I don't, it's not that they just don't interest me.
[689.32 → 696.06] I mean, I've played a couple that were fine, but it's not something I would ever like think,
[696.36 → 698.32] sit down and think, okay, I have some free time.
[698.32 → 700.18] Like, so I should, I really want to play this game.
[700.18 → 702.22] That's just never really happened to me.
[702.28 → 705.78] I don't know why, but like for my son, you know, I'm teaching my son Haskell now.
[705.90 → 710.16] And that was his, that's why he got interested in programming was because of Minecraft.
[710.34 → 712.64] And he wanted to learn how to make Minecraft mods.
[712.64 → 715.26] And so that's where it started for him too.
[715.26 → 733.40] So, so after I got out of high school and started working as a programmer, my first job was actually using C sharp.net to recover old database file formats from mainframes and get imported over to, you know, a pretty standard white box setup.
[733.40 → 745.24] Eventually I ended up in New York and started using Python and Django to, you know, make a content management system because what programmer hasn't worked on that sort of thing.
[745.36 → 745.50] Right.
[745.50 → 756.02] And, uh, my interest in open source though began when I was much younger because almost everything I used in common list was open source.
[756.20 → 760.96] The community was by and large on IRC and mailing lists.
[760.96 → 769.68] And I couldn't have become a programmer without, you know, these hundreds and thousands of people ready to help me and write all this stuff that I could use for free.
[770.18 → 775.96] What was the, the, the moment where you found joy, you know, tell us about the first joyous moment.
[776.04 → 778.06] We were like, this is my thing.
[778.06 → 779.32] I'm going to do this.
[779.40 → 780.38] I know how to do it.
[780.38 → 782.98] And you got some, some level of confidence.
[784.02 → 796.02] I think the first thing for me was I wrote a very, um, a very dumb text-based, uh, file format for storing data from one of my common list programs.
[796.02 → 798.38] Because I didn't understand how to use databases or anything yet.
[798.38 → 810.44] And, um, the first time I had a program that could persist its data without relying on common list image format thing and was in a format that I could read and modify with a text editor if I wanted.
[810.44 → 822.08] That was when I started really enjoying myself because, um, because then it felt like I could actually write programs that did, you know, whatever I wanted, or previously they'd all, they'd all been in memory.
[822.42 → 824.36] How about Haskell specifically?
[824.36 → 832.16] Um, you say that you've been programming for 15 years or over 15 years, and you became interested in Haskell about six years ago.
[832.40 → 834.10] What brought you to Haskell?
[834.10 → 847.10] And then as a follow-up to that in 2014, when you started, you know, talking with Julie on Twitter, what made you want to, you know, to pique her interest to teach her what you have about Haskell?
[847.98 → 851.82] Well, to start with the language, um, that was kind of a winnowing process.
[851.82 → 861.08] So Python was kind of like a okay, I'd rather be using common list, but I understand this thing is more popular and it captures most.
[861.26 → 867.98] I'm sure an actual, you know, somebody still use common list would crucify me for this, but it captures most of the benefits that most people would care about.
[867.98 → 873.74] Um, in terms of, you know, being able to do runtime metaprogramming and having a functional is kind of base.
[874.44 → 883.94] Um, but I eventually moved on to closure because I needed, um, something with a more mature runtime that had threading, uh, that sort of thing.
[883.94 → 887.54] And being able to go back to a list was just kind of a plus, right?
[887.58 → 888.20] That was nice.
[888.30 → 890.04] It was nice to have macros and stuff again.
[890.76 → 901.44] Um, but I kept running into these problems, um, problems that because I had used a bit of OCaml and a bit of Haskell, just a teensy tiny bit before.
[901.44 → 904.42] I knew that these problems weren't really necessary.
[904.56 → 905.80] These problems didn't need to happen.
[906.18 → 906.40] Right.
[906.60 → 914.42] I knew that, you know, everything that, and not everything, but the vast majority of errors I was having at runtime really could just be type errors.
[914.42 → 916.32] And it started really kind of eating at me.
[917.06 → 926.02] And, um, after one particular incident where I was at kind of, uh, closure meetup, like let's hack on, you know, everybody breaks up in these hemes and hacks on a problem together.
[926.02 → 934.46] I ended up having a runtime error that would have been prevented in Haskell and very easily found, but in closure, the vectors are actually functions.
[934.68 → 938.26] You can just use like a piece of data as if it was a function, apply it to an argument.
[938.50 → 940.80] And when you do that, you're using it like an index.
[941.42 → 948.32] And the problem is, is that the, um, are, are you guys familiar with the like the concept of like a source to sync distance?
[948.88 → 949.44] Not me.
[950.88 → 951.24] Okay.
[951.24 → 962.60] So if you ever work in like static analysis or on like, uh, like, you know, something kind of like code climate or one of those like kind of static analysis, linkers, typers, kind of things, you're trying to keep your source to sync distance as small as possible.
[962.68 → 964.84] And what that is, source is what caused the problem.
[965.52 → 969.32] Sync is where the static analyzer says there's a problem.
[969.48 → 969.68] Right.
[969.72 → 971.94] And obviously you want it to just kind of pin it on the nose.
[972.62 → 979.58] The problem is, is that people think that, you know, runtime errors can help shrink that distance, but in many cases, it can actually make it much worse.
[979.58 → 981.44] And in this case, that that's what happened.
[981.56 → 991.18] And it basically led to a situation where multiple people that use closure professionally, myself included, spent four hours tracking down a runtime error and 200 lines of code.
[992.14 → 994.56] And I knew that was just nuts.
[994.68 → 996.30] I mean, it's not like I hadn't debugged it.
[996.36 → 999.74] I, you know, I put print lines all over the entire program and it was still a massive pain.
[999.74 → 1009.76] And I realized that if I had been using, you know, Haskell or OCaml, it would have just pinned it right where I made the original mistake, not the thing, you know, 50 lines down.
[1010.40 → 1015.94] So the problem is I realized I knew I still wanted a functional language, not just types.
[1016.16 → 1016.48] Right.
[1016.56 → 1023.08] Because I did like, you know, other things about closure, like having, you know, software transactional memory and other things like that.
[1023.08 → 1032.10] So that narrowed it down to OCaml and Haskell and then, you know, concurrency and laziness, a few other things kind of decided it for Haskell for me.
[1032.10 → 1044.54] Um, then from there, I realized that although Haskell was really nice, I wasn't going to be able to use it at work unless I could get other people going.
[1044.74 → 1045.52] There you go.
[1045.70 → 1046.28] With Haskell.
[1046.46 → 1046.78] Right.
[1046.94 → 1059.74] So I realized that I had to take responsibility for, um, increasing the size of the community more generally, but also specifically I needed a path or a means of like saying to three coworkers, okay, do this, this, this, and this.
[1059.74 → 1062.24] And then we'll start pair programming to get you going.
[1062.70 → 1062.94] Right.
[1063.40 → 1066.32] So that's what led to the guide that I wrote.
[1066.40 → 1069.02] It's by my app slash learn Haskell on GitHub.
[1069.18 → 1071.16] It has over 3000 stars now.
[1071.66 → 1078.02] That guide was basically a recommended order of free resources to get going with Haskell as quickly as possible.
[1078.84 → 1087.40] Um, and it was that desire to be able to tell, you know, my manager with a straight face that yes, I can get people going with it.
[1087.40 → 1095.18] And that's also when I realized that I just had to get better at teaching in order for that not to be a super messy and painful process.
[1095.68 → 1105.86] Um, that all kind of culminated in me deciding, okay, I just need to write a book because I couldn't figure out how to kind of fit the Lego pieces of existing free resources together in a way that would really satisfy me.
[1105.86 → 1116.36] Um, around the time I decided I was going to write a book, um, a few months prior to that, Julie and I had become friends via Twitter for reasons.
[1116.52 → 1116.76] Random.
[1117.44 → 1118.96] You know, totally unrelated to programming.
[1119.14 → 1119.38] Yeah.
[1119.42 → 1120.72] Just some shared interests.
[1120.92 → 1121.12] Yeah.
[1121.16 → 1128.76] We were talking, it was actually, we first met in a thread about, um, history, some kind of historical topic that we were both engaged with.
[1128.76 → 1131.96] I don't remember exactly what it was, but that had nothing to do with programming.
[1134.02 → 1134.66] Sounds right.
[1135.06 → 1135.24] Yeah.
[1135.84 → 1143.48] And, uh, you know, I, I have had an abiding interest in natural language processing for a while now.
[1143.48 → 1158.96] And when I found out she was a linguist, um, the idea of getting her going to Haskell was kind of exciting because there is some good kit in Haskell for NLP, but it's not as mature as, you know, like say the Stanford NLP stuff for, for Java and all that.
[1159.02 → 1159.24] Right.
[1159.62 → 1163.98] So I thought maybe that could, it could be fun to learn NLP side by side with a linguist.
[1163.98 → 1171.96] And since I already had this book that I was going to work on, it would be kind of nice to have a beginner vet the material as I'm writing it.
[1172.08 → 1177.52] Um, of course she had, you know, upgraded from, you know, somebody vetting the material to a coauthor.
[1178.04 → 1178.40] Yes.
[1178.74 → 1179.28] Yes, I did.
[1179.68 → 1180.26] Very cool.
[1180.30 → 1181.78] I think that sets a good stage.
[1181.90 → 1183.76] Uh, we're going to take a quick break here.
[1184.12 → 1185.78] We want to talk more about Haskell.
[1186.14 → 1188.46] Um, we found out why Chris likes it.
[1188.46 → 1191.36] Julie, we're going to ask you specifically how you came to love Haskell.
[1191.36 → 1199.14] Um, which I think has something to do with your linguistics background and just have some more questions about the programming language itself.
[1199.14 → 1206.54] But I think this is a really nice setup for this, for this book, which people are finding quite useful is the idea of let's write a book.
[1207.00 → 1216.88] Um, not just a professional talking as if some sort of, uh, hypothetical beginners out there, but let's actually have a beginner alongside helping write the book.
[1216.88 → 1221.00] I think that's a, I don't know if it's a unique take, but it's an interesting one to say the least.
[1221.00 → 1224.42] So we'll pause here, take a break, and we'll be right back.
[1225.60 → 1228.52] Our friends at Linde offer a pretty cool service.
[1228.66 → 1229.72] I wanted to tell you about today.
[1229.82 → 1230.94] It's called Professional Services.
[1231.42 → 1240.58] This is something where you can hire them to take care of set migrations, one-off system admin tasks, server installs, or anything else you can think of.
[1240.58 → 1243.04] They offer this as an add-on to their customers.
[1243.04 → 1250.60] And I talked to Dave Messina, the product manager of Professional Services, and I asked him what it's all about and why their customers love it.
[1250.60 → 1277.58] Professional Services is geared towards existing and prospective customers that are looking for a system administrator to take on maybe a test that they don't have resources available to execute on, or just don't have the time to get in there, you know, into the command prompt, diagnose, troubleshoot, configure their Linde to meet the needs of their application.
[1277.58 → 1282.50] So our team here is diverse, and, you know, we specialize in, you know, multiple areas.
[1282.62 → 1285.08] We've been in, you know, the hosting industry for many years now.
[1285.36 → 1287.52] We specialize on Linux, so that's our forte.
[1287.90 → 1295.40] So we have excellent people here that are skilled and experienced in multiple areas of Linux.
[1295.40 → 1303.46] So they can typically execute these projects or solutions efficiently for these customers that need our assistance.
[1304.10 → 1308.44] Well, Dave, now that we know more about Linde's Professional Services, talk us through getting started.
[1308.54 → 1309.68] What's that process like?
[1310.18 → 1319.26] Existing and prospective customers can visit linode.com, click on add-ons, professional services, and there's going to be a get a quote button there.
[1319.26 → 1329.20] That's a scoping forum where they can fill out the technologies that they'd like to use and any notes that they'd like to provide us regarding their application or their goals.
[1329.46 → 1335.28] Once that happens, we'll follow up and speak to them further on solidifying the solution.
[1335.86 → 1337.84] And if everything looks good, then we get to work.
[1338.54 → 1341.94] And so once a customer decides to move forward, what happens next?
[1341.94 → 1348.78] Are they assigned a person who works with them to take care of their needs and kind of walks with them through the process?
[1349.08 → 1351.06] Take us through the process of what happens next.
[1351.66 → 1358.04] We have implementation specialists here that get assigned your project, and they'll see it from A to Z.
[1358.46 → 1367.72] So that is, you know, working on, if it's a new deployment, working on building out the stack and then potentially migrating your data over.
[1367.72 → 1379.48] It may be, you know, going through a validation process with you to determine, make sure that everything looks good in terms of, you know, the data that's been moved over and how your website functions on the new Linde.
[1379.62 → 1387.86] And then if you sign off on that, then we move forward to go live where, you know, if it's in the project, and we're handling it, we'll do the DNS cutover as well.
[1387.86 → 1392.32] All right. That was Dave Messina, product manager for Linde's professional services.
[1392.72 → 1395.80] As you can see, if you've got a need, Linde's got your back.
[1396.04 → 1398.70] Head to linode.com slash proser vices.
[1399.18 → 1404.56] Once again, linode.com slash proser vices to learn more and tell them the changelog sent you.
[1407.46 → 1410.94] Okay, we are back with Chris and Julie, and we are talking about Haskell.
[1410.94 → 1417.46] We found out what brought Chris to Haskell, and we know that Chris brought Julie to Haskell in many ways.
[1418.26 → 1419.62] But you came to love it, Julie.
[1419.76 → 1429.66] And one thing that you say is that you came to love Haskell for its own sake, in part because of connections I see between it and the logic of generative syntax.
[1430.58 → 1436.40] One of the things we say here on the changelog is we face our imposter syndrome, so you don't have to.
[1436.56 → 1440.62] And I have to say, when I read the logic of generative syntax, I feel like the beginner.
[1440.74 → 1441.68] I don't even know what that means.
[1442.68 → 1445.18] So I think the linguistics thing, I'm not sure.
[1445.18 → 1448.66] Can you help me out, unpack that sentence, and elaborate for us?
[1449.32 → 1450.72] Yeah, it is a linguistics thing.
[1450.80 → 1455.58] That's what I was, I worked on syntax, mostly syntax in graduate school.
[1456.54 → 1459.16] Particularly, I was working on the argument structure of verbs.
[1460.20 → 1463.56] And I'll talk about that in just a second.
[1463.56 → 1482.24] And so with Haskell, the connection is with generative syntax, what you're trying to do is find the rules that can produce all the legal or grammatical sentences for a language and not produce or allow any illegal or ungrammatical sentences.
[1482.24 → 1498.26] So a lot of linguists, not all, because Chomsky is a little bit controversial sometimes, but a lot of linguists think that we have this kind of internalized rules of syntax that we use to produce grammatical sentences.
[1498.26 → 1502.96] And that's why we can produce grammatical sentences like colorless green ideas sleep furiously.
[1503.66 → 1506.98] That's why we can produce grammatical sentences that don't actually have any meaning.
[1509.32 → 1515.42] Leaving aside the controversy of that statement, that's the idea behind generative syntax.
[1515.56 → 1517.40] And that's kind of what I was working on in graduate school.
[1517.40 → 1526.00] So not too long, I guess it was a few months after Chris started trying to teach me Haskell, I was listening to a talk.
[1526.68 → 1528.36] I think it was from Strange Loop.
[1528.48 → 1533.48] And I think it was Paul Snively and Amanda, I'm not sure how to pronounce her last name, Lake?
[1533.94 → 1534.96] Lake? Lake?
[1535.32 → 1536.08] Something like that.
[1536.08 → 1540.28] And I believe it was in one of their talks.
[1540.36 → 1554.32] They said something like the goal of a type system is to allow any legal functions or expressions, but not allow any illegal ones.
[1555.36 → 1558.82] And that's the same thing as what generative syntax is trying to do.
[1558.82 → 1568.18] So I started sort of thinking of types and type classes in Haskell as they relate to grammatical categories that I had been studying in linguistics.
[1568.36 → 1572.52] And that's when I sort of started to love it.
[1572.74 → 1575.16] Like, to me, that was fascinating, those connections.
[1575.78 → 1583.60] And a friend of mine that I also know from Twitter, he's a Greek Haskeller named George.
[1583.68 → 1584.18] Hi, George.
[1584.18 → 1604.34] He, one day when I was first starting, he also told me, like, if you think of it, a function like a sentence, and so the function is a verb, and then the arguments that it takes in the language would be the subject and the object and any prepositional phrases, for example, that it takes as arguments.
[1604.34 → 1611.48] But in Haskell, it's not taking subjects and objects as arguments.
[1611.66 → 1615.10] It's taking these typed data as arguments, right?
[1615.72 → 1619.42] And so those kinds of connections are what made me sort of fall in love with Haskell.
[1619.92 → 1629.36] And that's why I'm not really sure that even though I'm developing now a more general interest in programming, I'm not sure if I'd come to programming through any other language.
[1629.36 → 1632.78] Like, it would have kind of hooked me as much as Haskell did.
[1632.78 → 1641.20] So the type system is obviously a big piece of how Haskell works, and it's something that people either love or hate.
[1641.64 → 1648.22] You know, dynamic, static, strong, loose typing is one of those age-old flame wars.
[1648.46 → 1652.64] You know if we're not arguing about Vim versus Emacs, it's dynamic versus static type systems.
[1652.64 → 1654.64] Yes.
[1654.64 → 1667.04] And so here's a reason to love this type system with regard to Haskell is because of this connection that you see through it to this generative syntax idea.
[1667.18 → 1670.28] Chris, could you help us with the type system?
[1670.28 → 1674.18] Explain exactly what that means.
[1674.24 → 1676.80] It's strongly static type, how that works.
[1677.00 → 1686.02] And you have the real-world programmer experience of like, this makes me productive in ways that I wasn't without a strong type system.
[1686.42 → 1688.50] Like the error checking.
[1688.66 → 1696.44] Can you kind of just give maybe the 30,000-foot blimp view of Haskell's type system and why it's so interesting?
[1696.44 → 1701.78] Haskell's type system is nice, but it is kind of an instrumental thing for me.
[1702.44 → 1710.94] I like it because it's relatively small and easy to understand compared to languages that are trying to blend multiple paradigms.
[1712.00 → 1718.10] Part of the appeal of, say, something like Python is that, you know, there's pretty common patterns to the way people do things.
[1718.10 → 1723.20] People aren't really trying to be overly clever where it's not merited.
[1723.86 → 1731.24] It's, you don't have to guess as much with the semantics of a line of code in Python as compared to, say, you know, Ruby or Perl.
[1731.36 → 1732.80] No offence to users of those languages.
[1733.08 → 1735.96] Tons of Ruby and Perl users in the Haskell community.
[1736.62 → 1738.74] But, you know, I don't think a lot of people would debate that.
[1738.74 → 1743.50] So in Haskell, the nice thing about the type system is it's actually very compact.
[1744.28 → 1749.26] The semantics of the language are pretty alien to people, but the type system itself isn't that big.
[1749.64 → 1751.22] There are not a lot of rules to it.
[1751.26 → 1752.92] For example, it doesn't have subtyping.
[1754.02 → 1761.62] It ends up that you don't actually need subtyping if you just kind of piece it apart into orthogonal components, different things that you might want to use.
[1762.04 → 1763.80] Type classes are one of those things.
[1763.80 → 1768.36] And one of the advantages of that is it just makes the results more predictable.
[1769.30 → 1773.94] You don't have to guess how, you know, a piece of code, what its type will be inferred as.
[1774.62 → 1784.98] So for me as a working programmer, Haskell's type system is in kind of the sweet spot where I don't really have to do any more work than I would otherwise do to make the type checker happy.
[1785.68 → 1789.70] Because it really only disallows stuff that I would never want to do anyway.
[1789.70 → 1794.28] And I know a lot of people who don't have a lot of experience with stack type systems aren't going to believe me on that point.
[1794.82 → 1797.16] But it legitimately is the case, at least for me.
[1797.56 → 1802.12] It does take some time to kind of remold your brain to think in those terms.
[1802.40 → 1803.34] But it does happen.
[1803.94 → 1816.42] So from there, I mean, the basic idea of the type system in Haskell is that you have these types that enumerate possible valid kind of, you know, we call them inhabitants.
[1816.42 → 1820.04] But we're really just talking about like, okay, this is a valid value that inhabits this type, right?
[1820.80 → 1823.34] So book is a type in Haskell.
[1823.78 → 1829.16] It's not just an alias for an integer like it is in like C, that kind of thing.
[1830.02 → 1834.72] It just has two values or two data constructors as they're called in Haskell.
[1834.82 → 1836.92] But they're just two kind of null area values.
[1837.56 → 1838.74] And they're just true and false.
[1838.74 → 1841.98] So that has two things that are a valid book.
[1842.20 → 1842.94] And then that's it.
[1843.60 → 1848.72] So unlike a lot of languages, there are no implicit nulls in Haskell.
[1848.90 → 1852.90] So there's not, you know, true, false, and null are a valid book.
[1853.04 → 1853.80] We don't have that.
[1854.12 → 1855.42] It's just true and false.
[1856.02 → 1857.68] So that's the basics of it.
[1857.68 → 1866.38] And then if you want to write a function that takes a book input, then you're going to match on true or false, or you're just going to pass it on down the line to a different function.
[1867.28 → 1873.86] Then from there, it expands into type classes, which give you a way to, I don't think I would call it abstraction.
[1874.04 → 1875.42] I think I would call it generalization.
[1875.64 → 1878.26] But basically type classes give you ad hoc polymorphism.
[1878.26 → 1885.06] The best analogy to draw would be kind of like Java's interfaces, but considerably more powerful.
[1886.26 → 1892.94] But basically you're generalizing an interface that a bunch of types may be able to satisfy and have in common.
[1894.84 → 1901.48] In fact, one of the things I like about Haskell's type classes is that they lend themselves pretty well to efficient code generation.
[1901.48 → 1912.34] So as a result, we're able to have polymorphic numerics in Haskell by default without it actually necessarily costing us at runtime, which is kind of nice.
[1913.46 → 1918.68] So you don't have like a separate like plus and then plus dot for instant floats, that sort of thing.
[1919.30 → 1925.02] It also means you can extend other types to, you know, implement the sum type class if you so desire.
[1925.70 → 1926.78] But there are some constraints.
[1926.78 → 1929.62] Like you don't really want to use type classes willy-nilly.
[1929.62 → 1939.58] You want to, you know, make certain they satisfy some laws or constraints that are designed to describe, you know, what behaviour makes a type class predictable.
[1940.18 → 1941.06] Or, you know, like it shouldn't.
[1941.22 → 1946.58] It's basically how you encode like the principle of least surprise on a per-type class basis.
[1947.54 → 1953.40] Then from there, contrary to popular belief, the Haskell type system has some escape hatches.
[1953.40 → 1961.58] For example, you can put like an error value in the definition of a function if you want to say it has a type, but you don't have time to implement it right now.
[1962.48 → 1974.52] And this actually turns out to be a really powerful technique because it means that I can work in terms of types alone without having actually written the code or implemented any of the functions.
[1974.52 → 1978.60] And then test combining the functions together without executing them.
[1978.80 → 1985.98] Just seeing what, just asking my REPL, my redeveloped print loop, what type would it be if I compose, you know, functions F, G, and H?
[1986.48 → 1988.20] Given that I've only defined their types.
[1988.58 → 1989.94] I haven't actually implemented them.
[1990.44 → 1992.48] Evaluating would actually produce a runtime error.
[1993.02 → 1993.78] Tell me what would happen.
[1994.14 → 1999.46] And then I can figure out if I'm actually figuring out the right design or combination of functions that achieves what I want.
[1999.46 → 2001.38] Before I've really done any real work.
[2001.86 → 2005.12] I just wanted to say here about this, what he's talking about right now.
[2005.50 → 2008.64] This is something I didn't really believe him.
[2009.44 → 2013.06] He told me that you could do this, and I didn't really believe him for a long time.
[2013.06 → 2017.74] But we've actually demonstrated how to do this to a certain extent in the book.
[2017.84 → 2020.32] And it's really, really helpful.
[2020.82 → 2025.40] I mean, it does work, and it's a really powerful way to figure out what you're doing with your program.
[2025.40 → 2037.06] And basically the idea is that the types are this, you know, kind of way to step away from the specifics so that you can make certain you're even thinking the right thoughts before you do all the work out front.
[2037.98 → 2048.96] So just as a way of getting a little bit more background about Haskell itself, you know, a lot of most languages come out of a specific need or specific design constraints.
[2048.96 → 2054.72] It's, you know, the most obvious one that comes to mind for me is Perl, which was created, you know, as an extract.
[2055.68 → 2057.26] I'm forgetting what the acronym is.
[2057.32 → 2058.44] It's for text extraction.
[2058.68 → 2060.02] And what's Perl's acronym?
[2060.16 → 2060.68] Help me out here.
[2062.98 → 2063.68] No help.
[2064.20 → 2064.60] Googling.
[2065.08 → 2066.14] I'm not actually sure.
[2066.32 → 2067.36] It's for text processing.
[2067.90 → 2068.70] Practical extraction and report language.
[2068.72 → 2069.00] Yeah.
[2069.26 → 2069.82] Text extraction.
[2069.82 → 2071.74] Practical extraction and report language.
[2071.74 → 2072.04] Yeah.
[2072.08 → 2077.88] So its whole purpose was for manipulating and performing reports on text.
[2077.88 → 2079.58] And so it's designed like that.
[2081.54 → 2083.02] Where did Haskell come from?
[2083.12 → 2085.96] What problems was it set out to solve?
[2086.12 → 2090.60] And why is it designed in such a way that you've just described it, Chris?
[2090.68 → 2095.82] And then as a follow-up to that, therefore, what kind of problems is it particularly good at solving?
[2097.42 → 2104.62] Well, it came out of they wanted to see if they could make a programming language that was a pure lambda calculus, right?
[2104.62 → 2107.96] Kind of, yeah.
[2108.20 → 2116.98] So they took it for granted that they wanted a language that was going to be only a lambda calculus.
[2117.14 → 2124.08] But the motivation was that prior to Haskell, there were a bunch of different research languages running around in the 1980s.
[2125.66 → 2128.20] Haskell descends from the ML family of languages.
[2128.20 → 2136.48] ML started in 1973, and it was kind of descended from Landon's ice swim from the 1960s.
[2136.54 → 2141.14] But basically, we had the foundations of a language like Haskell back in the 1970s.
[2141.14 → 2144.64] But those languages were strictly evaluated.
[2145.14 → 2150.02] And what that means is what you already take for granted in all the languages you currently use.
[2150.02 → 2155.82] When you pass arguments to a function in a strict language, they've already been evaluated.
[2155.94 → 2158.56] They're evaluated immediately whenever you bind them, right?
[2160.36 → 2168.48] The research that was going on in the 1980s was to figure out a lazy functional programming language.
[2168.48 → 2175.44] And Haskell was this collection point of, okay, we've got all these different implementations and designs running around.
[2175.72 → 2183.20] Let's try to combine forces and come up with one good implementation of a lazy functional programming language.
[2183.78 → 2193.62] And what laziness means here is that your code doesn't get executed or evaluated until it's actually needed, rather than when it's kind of bound to a variable.
[2193.62 → 2198.42] This is actually something that a recent release of our book deep dives into.
[2199.68 → 2210.80] But part of the motivation for this is that it means that you can write this nice, clean, maybe an experienced programmer could even say naive code.
[2211.28 → 2218.54] But because you're not doing any of the work immediately upon binding, it leads to the situation where you can have code that looks nice and looks naive,
[2218.54 → 2223.54] but actually optimizes to what you would actually want to execute as.
[2223.60 → 2230.42] So a good example is when you map, you know, say a function F, G, and H over a list, right?
[2231.34 → 2241.68] The non-naive way to do it is to compose all the functions that you're going to map over that list all at once so that you do only one map over the list, right?
[2241.68 → 2250.38] Because if you're using JavaScript or Ruby or Python or whatever, I mean, they all have a map, right?
[2250.64 → 2261.54] And the problem is if you keep going map F, map G, map H, map I, map J, you've now done like five loops over your list and constructed like five lists, right?
[2261.96 → 2263.86] Well, in Haskell, that's not what happens.
[2264.00 → 2265.38] It actually fuses them together.
[2265.38 → 2274.94] But the only reason it can do that is because of both the lazy or, if you will, non-strict semantics that don't obligate it to do all the work up front all at once immediately,
[2275.38 → 2282.80] but also because it knows where effects could happen so it knows when it can move certain bits of code around.
[2283.02 → 2291.10] It means it's actually free to reorder your code because it knows where that is and is not allowable.
[2291.94 → 2294.24] The purity fell out of the non-strictness, actually.
[2294.24 → 2305.66] The non-strictness means you can't actually really have an impure or, to explain impurity, it means you can't have a language that has an imperative kind of sub-language like OCaml does,
[2305.92 → 2307.92] and it means you can't have effects be implicit.
[2308.54 → 2314.26] When you perform effects, you know, whether that be talking over a network socket or printing or whatever,
[2314.92 → 2320.00] it shows up in your types explicitly in Haskell, unlike most languages.
[2320.00 → 2325.46] I've actually used an impure language that was also non-strict.
[2325.80 → 2326.88] It was a scheme dialect.
[2327.76 → 2332.38] And let me tell you, getting it to do things in the right order as you intended was a nightmare.
[2332.94 → 2337.22] And I think that particular scheme implementation was a cruel joke on some grad students.
[2337.22 → 2342.14] But the point is, is it basically laziness forced purity.
[2342.68 → 2346.58] But then later on, people realized the purity was really quite valuable in its own right.
[2347.82 → 2349.78] Purity in the sense of being a pure lambda calculus.
[2349.92 → 2353.90] People get really hung up on that word and think it's like a moral judgment on other languages.
[2353.90 → 2356.62] And it's just, it just means that it's just a lambda calculus.
[2356.62 → 2363.50] So I was going to, as a follow-up to that was kind of, where do we see Haskell getting used out there in the wild?
[2364.16 → 2368.40] It has crossed my radar a few times in terms of web type things.
[2368.52 → 2374.06] Of course, every language that's still actively used and maintained has web type of things.
[2374.56 → 2379.24] But what are some other people might know about Haskell projects, maybe open source,
[2379.52 → 2385.46] that you guys are aware of, of where Haskell is being used to solve cool problems?
[2385.46 → 2392.00] To compare it to some other languages, it gets used in roughly the same domains as languages,
[2392.16 → 2402.60] ranging from Java, Go, Scala, to all the way out to, say, Python, Perl, Ruby, Prologue.
[2403.00 → 2406.90] So that kind of spans basically pretty much anything you use the garbage collected language for.
[2409.00 → 2414.02] It leans more on the side of, you know, say, like, Go, OCaml, Java, Scala,
[2414.02 → 2416.54] because it is threaded, it is compiled.
[2418.04 → 2422.24] So you're seeing network services, you know, plain old web apps.
[2422.34 → 2427.80] There's actually multiple ways to compile Haskell to JS now.
[2428.16 → 2432.38] So you can use it for a front-end web app if that's your cup of tea.
[2432.78 → 2436.18] There is a Haskell-like, not exactly the same thing,
[2436.18 → 2441.22] but a Haskell-like compiled a JS language called Prescript that has a pretty vibrant community
[2441.22 → 2447.46] and a very good person behind it, Phil Freeman.
[2447.70 → 2449.90] He's amazing, super nice guy.
[2450.04 → 2452.38] I've seen Prescript recently be compared to Elm.
[2452.74 → 2453.42] Is that right?
[2454.88 → 2455.32] Yeah.
[2455.62 → 2457.98] So, I mean, they kind of exist on the same continuum,
[2458.36 → 2460.10] but Prescript's a lot closer to Haskell.
[2460.10 → 2464.12] So it's not identical, and you still lose some stuff going to Prescript from Haskell,
[2464.24 → 2466.20] especially if you've been using any of the advanced features.
[2467.04 → 2470.20] But, I mean, for example, like, Prescript has type classes.
[2470.72 → 2471.44] Elm doesn't.
[2471.58 → 2476.28] And Elm is kind of stripping the shit there
[2476.28 → 2479.38] in an attempt to attract more people
[2479.38 → 2481.60] who haven't necessarily used a functional language
[2481.60 → 2484.76] or a typed functional language before.
[2485.00 → 2485.20] Gotcha.
[2486.44 → 2489.20] Prescript is trying to kind of inhabit a...
[2490.10 → 2493.00] It's kind of a Haskell that's been redesigned
[2493.00 → 2497.18] with the needs of front-end DOM manipulation in mind.
[2497.68 → 2501.40] Yeah, somebody just requested a show on Prescript in ping.
[2501.70 → 2502.50] I don't know if it was last week.
[2502.98 → 2506.68] Just while you're talking, Chris, as a proxy for success,
[2506.98 → 2511.92] I've searched the most starred GitHub repos with the Haskell language.
[2512.76 → 2516.72] Number one is Postgres, which was a REST API for any Postgres database,
[2517.12 → 2518.54] which seems pretty cool.
[2518.54 → 2521.36] Also, Elm's compiler is written in Haskell.
[2521.88 → 2524.86] As you mentioned, Prescript is a top five.
[2525.80 → 2530.62] So just to give people a taste of what people are out there doing with Haskell.
[2532.18 → 2533.16] I think that's good.
[2533.24 → 2536.02] Let's change pace a little bit and talk about learning.
[2536.02 → 2540.88] You guys recently gave a speech at LambdaConf called
[2540.88 → 2543.10] How to Learn Haskell in Less Than Five Years,
[2543.44 → 2547.22] which seems like a long time, but can you share more?
[2547.78 → 2550.08] And why does it take five years to learn?
[2551.36 → 2553.54] Aside from the dreaded Monad concept,
[2553.70 → 2557.16] which we've all but skirted so far in this show,
[2557.60 → 2560.12] what makes Haskell so hard to pick up?
[2560.12 → 2565.08] Well, at least as a working programmer,
[2565.56 → 2571.88] part of the reason that it took me five years is that I'm very impatient.
[2572.84 → 2577.48] And if I don't get traction with something in what seems like a reasonable span of time,
[2577.48 → 2582.88] then I kind of, you know, like an unbalanced flywheel,
[2582.96 → 2584.26] kind of spin out and give up.
[2584.26 → 2587.48] And I went through that process, I think probably, I don't know,
[2587.76 → 2589.46] once or twice a year for those five years.
[2589.56 → 2591.14] This isn't five years of steady learning.
[2591.70 → 2594.34] This is five years of, okay, I'm going to try to pick this up again.
[2594.98 → 2596.52] Nope, still can't write a web app.
[2596.66 → 2597.58] Okay, I'm out.
[2599.36 → 2601.62] So we're actually trying for five years.
[2601.92 → 2604.36] It was sort of over a span of five years.
[2604.54 → 2606.32] Yeah, no, it wasn't consistent effort.
[2606.84 → 2610.92] But yeah, but each false start was, you know, at least like a week or two, right?
[2610.92 → 2615.42] And like kind of alternating with that, I'd also play with OCaml
[2615.42 → 2618.78] because it was kind of scratching some of the same itches, right?
[2619.58 → 2626.14] And I realized the problem was, was that the foundational kind of like the actual way
[2626.14 → 2629.98] the language thinks, so to speak, is just totally different.
[2630.22 → 2634.80] And it's actually faster if you just roll back and just tell yourself,
[2634.90 → 2636.36] you know what, I don't know how to program.
[2636.64 → 2637.96] Why don't you tell me how, Haskell?
[2638.32 → 2640.22] And it turns out doing that is much faster.
[2640.22 → 2643.30] I can get somebody going with Haskell in weeks easily,
[2643.48 → 2645.42] especially if I have some pair programming time with them.
[2646.32 → 2649.78] If I toss them our book and pair program with them,
[2649.80 → 2652.52] I can get them going in like two weeks hacking on a web app in Haskell.
[2652.88 → 2654.04] It doesn't have to be hard.
[2654.14 → 2657.26] It's just that the existing resources were a bit rough.
[2658.32 → 2662.06] And Sellers don't have the same language, or sorry,
[2662.18 → 2666.96] the same community around documentation and education
[2666.96 → 2668.30] that some other communities have.
[2668.30 → 2673.52] Like, I mean, you can use, if you're in Python, Ruby, JS,
[2673.86 → 2677.90] you can use just how well designed the landing page for a library is
[2677.90 → 2679.90] to gauge how much the maintainer cares about it
[2679.90 → 2681.24] and how much effort they're putting in, right?
[2681.82 → 2686.22] Those cues, those social cues, they don't exist in Haskell.
[2686.44 → 2689.50] The best library for something, it's going to have the same Hackage,
[2689.94 → 2691.72] boring landing page that everything else has.
[2691.72 → 2694.30] So that's another problem is that newbies will get trapped
[2694.30 → 2696.98] by these like abandonedware libraries.
[2697.38 → 2700.28] And since nobody really makes an effort to, you know,
[2700.34 → 2702.12] put on their best face for their library,
[2702.28 → 2703.82] you don't really have a good way to discriminate.
[2704.36 → 2707.24] Let's really tease up the learning path for us.
[2707.54 → 2711.28] Chris, I know it's taking you five years to false start your way
[2711.28 → 2714.68] into Haskell and still be a professional at the same time.
[2715.56 → 2718.02] Julie, it seems like you've got a much faster path.
[2718.02 → 2719.08] So let's take a break.
[2719.96 → 2721.42] And when we come back from this break,
[2721.44 → 2724.12] we'll kind of dive a little bit more into the book,
[2724.20 → 2726.84] the learning process, and maybe, Julie,
[2726.92 → 2729.06] you can share how you got there so quickly
[2729.06 → 2731.40] versus Chris's five years of false starts.
[2731.70 → 2733.48] We'll break here, and we'll be right back.
[2735.80 → 2738.86] I'm here with Thomas Watson of Upbeat.
[2738.98 → 2740.96] And as listeners of this show, you know
[2740.96 → 2743.02] that we love to turn things on their heads.
[2743.02 → 2745.20] And that's no different from sponsorships.
[2745.34 → 2747.58] And one thing we're doing is we're going deeper
[2747.58 → 2749.28] into the organizations we work with.
[2749.74 → 2751.46] Upbeat is doing some fascinating things
[2751.46 → 2753.58] around application performance monitoring,
[2754.02 → 2755.24] specifically around Node.js.
[2755.54 → 2757.20] And Thomas has an interesting story
[2757.20 → 2758.90] on how he got started with Upbeat
[2758.90 → 2761.48] and also starting off their Node support.
[2761.62 → 2762.34] So Thomas, say hello.
[2763.08 → 2764.06] Hey, hello, everybody.
[2764.80 → 2767.66] Thomas, you got an interesting story here
[2767.66 → 2769.80] with how you came to be at Upbeat.
[2769.80 → 2771.92] It seems like the Node support
[2771.92 → 2773.38] is kind of in thanks to you.
[2773.44 → 2775.08] So what's the backstory on that?
[2775.86 → 2777.36] Yeah, so I've been doing Node.js
[2777.36 → 2779.10] for almost five years.
[2779.38 → 2780.80] And I found Upbeat
[2780.80 → 2784.16] and they were doing application performance monitoring.
[2784.32 → 2786.18] And I wanted to have that for my stuff
[2786.18 → 2786.78] that I was doing.
[2786.90 → 2787.90] And they didn't have Node support.
[2788.14 → 2790.34] So I basically approached them and said,
[2790.42 → 2792.94] hey, can I do an unofficial Node.js implementation?
[2792.94 → 2795.94] And they were like, yeah, sure.
[2796.12 → 2796.82] We would love that.
[2797.12 → 2798.10] And I did that.
[2798.90 → 2803.36] And then slowly we started to work more and more together.
[2803.64 → 2804.58] And all of a sudden,
[2804.82 → 2807.96] I find myself being employed now at Upbeat,
[2808.50 → 2809.96] being the Node.js lead.
[2810.20 → 2813.30] And I'm now responsible for this agent
[2813.30 → 2816.36] that I started back in the days as an open source project.
[2816.50 → 2819.22] I'm now responsible for that at Upbeat.
[2819.22 → 2822.42] And that's the one you install on your production servers
[2822.42 → 2825.46] to monitor the health and performance of your application.
[2826.06 → 2828.08] And so that module is Upbeat Node.
[2828.38 → 2830.90] And so things began with that open source repo.
[2831.08 → 2832.52] Is that how things began for you with this?
[2832.70 → 2836.22] Yeah, I started under my own GitHub account
[2836.88 → 2840.04] and just did it for myself and my own projects.
[2840.20 → 2841.50] And then people started using it
[2841.50 → 2844.02] and the Upbeat guys were really happy with it.
[2844.44 → 2848.44] And then when we decided to join forces,
[2848.44 → 2851.42] we moved it to the Upbeat org on GitHub.
[2851.84 → 2856.28] So now it resides on GitHub.com slash Opbeat Node.
[2856.74 → 2858.58] That's fascinating to see,
[2858.90 → 2860.26] because we'll get into this here in a second,
[2860.30 → 2862.10] but you have this passion for open source,
[2862.24 → 2865.78] but how your own personal drive
[2865.78 → 2867.22] and desire for something
[2867.22 → 2870.62] on a particular language platform like Node
[2870.62 → 2872.54] and then a service like Upbeat
[2872.54 → 2874.52] to get that application performance monitoring
[2874.52 → 2875.42] into your own apps,
[2875.64 → 2876.86] you were like, hey, you don't have it,
[2876.86 → 2878.06] but I can write this.
[2878.22 → 2879.66] And now you actually work there
[2879.66 → 2880.42] and you're building it out.
[2881.08 → 2882.10] Yeah, that's the beauty of open source.
[2882.62 → 2884.06] It connects you with a lot of people
[2884.06 → 2886.32] and you can basically do what you want for yourself.
[2886.72 → 2888.20] And then if people like it,
[2888.56 → 2889.98] you see where it takes you.
[2890.24 → 2890.84] In this case,
[2890.94 → 2892.46] it took me to this really awesome place.
[2892.52 → 2894.68] I'm doing this really awesome stuff with Node
[2894.68 → 2897.12] that's really down in the machine room,
[2897.36 → 2897.88] so to speak,
[2898.44 → 2900.84] which is really, fascinating to do.
[2900.84 → 2901.88] Right now we actually,
[2902.12 → 2903.96] we're just going out of beta soon.
[2904.36 → 2906.46] You can go to upbeat.com slash Node.js
[2906.46 → 2907.36] and sign up for the beta
[2907.36 → 2910.12] if you want to try out the stuff.
[2910.52 → 2912.88] So the Upbeat Node module,
[2913.00 → 2914.40] can you talk a bit about what it does?
[2914.92 → 2916.72] So basically it sits on your server
[2916.72 → 2919.28] inside your Node.js app.
[2919.52 → 2922.60] You require it at the top of your main program
[2922.60 → 2925.44] and it just monitors the overall health
[2925.44 → 2928.26] of your application on a request basis.
[2928.54 → 2931.88] So incoming HTTP requests to your Node server.
[2932.22 → 2933.46] Figures out what's slow,
[2933.62 → 2935.12] what's performing badly,
[2935.28 → 2937.92] what should you take a look at to optimize.
[2938.10 → 2939.14] Maybe it's a database thing,
[2939.24 → 2942.14] maybe it's a Reddish cache or something else.
[2942.52 → 2945.50] And it also monitors errors happening in production.
[2945.82 → 2947.90] So we will break down the error,
[2948.04 → 2950.06] figure out who made that code,
[2950.16 → 2951.00] when was it committed
[2951.00 → 2953.96] to Git when was it pushed to production.
[2954.48 → 2956.20] So we can order assign errors as well
[2956.20 → 2957.74] to the developers who actually
[2957.74 → 2960.12] is responsible for the code that is breaking.
[2960.86 → 2962.88] So obviously your passion for open source
[2962.88 → 2964.82] and your passion for giving back,
[2965.64 → 2967.68] you know, got you to doing some of this stuff
[2967.68 → 2969.64] with Upbeat and what we just described there
[2969.64 → 2971.18] with your Node support and whatnot.
[2971.52 → 2974.32] Can you talk a bit about your work at Node School,
[2974.94 → 2976.04] the open source you've written,
[2976.16 → 2977.78] just some of your passions around open source
[2977.78 → 2979.76] and kind of how you think about open source?
[2979.76 → 2982.34] Yeah, I really love open source
[2982.34 → 2985.16] and I've been a big open source software user
[2985.16 → 2986.08] for over 20 years.
[2986.74 → 2989.24] So when I joined the Node.js community five years ago
[2989.24 → 2991.50] and finding such a big open source spirit
[2991.50 → 2994.06] in the community, it was really exciting.
[2994.26 → 2996.82] So I've now gone from an open source user
[2996.82 → 2997.78] to an open source developer.
[2998.32 → 2999.70] I love to teach.
[2999.90 → 3001.14] That's one of my passions
[3001.14 → 3002.26] and especially, of course,
[3002.30 → 3003.16] I love to teach programming.
[3003.16 → 3005.58] So there's something called a Node School
[3005.58 → 3008.18] where I try to help out as much as I can
[3008.18 → 3010.66] to teach other people Node.js.
[3011.16 → 3013.26] And you get to do that not only, you know,
[3013.32 → 3015.68] on the web, you know, kind of remotely, so to speak,
[3015.72 → 3017.46] but you also get to do it face-to-face.
[3018.02 → 3021.36] Yeah, you can go into nodeschool.io
[3021.36 → 3023.38] and you can take some courses online,
[3023.44 → 3026.62] but you can also join some of the regional chapters
[3026.62 → 3027.74] and you can meet up at a city.
[3028.32 → 3029.76] There'll be a Node school event
[3029.76 → 3031.42] where we will have tutors
[3031.42 → 3033.72] who can help you out with your Node questions
[3033.72 → 3036.24] and you can actually do some of these online courses.
[3036.38 → 3038.38] You can do them in person, in real life
[3038.38 → 3041.48] with people who know Node really well.
[3041.74 → 3043.20] And I try to do that as much as I can.
[3043.28 → 3044.78] I've been organizing one here in Copenhagen
[3044.78 → 3045.30] where I'm from.
[3045.84 → 3046.08] Well, cool.
[3046.14 → 3047.52] If you want to follow up with Thomas,
[3047.88 → 3051.14] you can check him out at GitHub.com slash Watson.
[3051.14 → 3054.18] That's his last name, W-A-T-S-O-N.
[3054.28 → 3057.36] If you want to sign up for the Upbeat Node.js beta,
[3057.36 → 3060.00] you can do so at opbeat.com slash Node.js.
[3060.86 → 3061.88] And now back to the show.
[3064.02 → 3065.50] All right, we're back from the break.
[3065.86 → 3067.02] And so before the break,
[3067.02 → 3069.88] we got kind of a tease of this learning process.
[3069.88 → 3072.84] So Chris, we got to hear your five-year false starts
[3072.84 → 3074.94] and the deeper story behind that for you.
[3075.06 → 3078.12] And Julie, you come from a background of linguistics
[3078.12 → 3079.70] and philosophy,
[3079.70 → 3082.80] and you were roped into this gig, so to speak,
[3082.80 → 3087.42] from Chris's perspective towards programming.
[3087.68 → 3089.08] And I'm sure you're happy about it now,
[3089.20 → 3091.78] but help us understand the path for that,
[3091.88 → 3093.52] like the process to learn,
[3093.66 → 3095.72] like what were some of the hurdles you'd faced?
[3096.06 → 3097.78] Help us understand your path of learning Haskell.
[3098.56 → 3100.60] Well, I mean, everybody says,
[3100.66 → 3101.76] or I see it said a lot,
[3101.84 → 3103.68] that it's easier to learn Haskell
[3103.68 → 3105.94] if you don't know any other programming languages
[3105.94 → 3108.82] than if you're trying to come from a different language
[3108.82 → 3109.78] and then start learning Haskell
[3109.78 → 3113.26] because people who already know some other languages
[3113.26 → 3115.72] have to kind of clear out
[3115.72 → 3117.10] what they already know about programming
[3117.10 → 3119.16] because Haskell does things so differently.
[3120.02 → 3121.54] And I think there's some truth to that.
[3121.62 → 3122.56] I mean, you do have to,
[3123.26 → 3126.00] from what little I know of other programming languages now,
[3126.12 → 3127.50] I can see why people say that.
[3127.58 → 3129.42] I mean, you definitely have to think differently
[3129.42 → 3131.52] about how you're programming to do it in Haskell
[3131.52 → 3133.06] than in a lot of other languages.
[3134.06 → 3135.92] So I didn't obviously have that problem
[3135.92 → 3137.86] because I didn't know any other programming languages.
[3137.86 → 3140.10] So in that sense, it was easier.
[3140.34 → 3142.90] But for me, the big hurdles have been,
[3143.40 → 3144.50] well, two big things.
[3145.08 → 3148.14] The first one is that very, very few people
[3148.14 → 3150.94] learn Haskell as a first language.
[3151.36 → 3154.06] I mean, that's fairly uncommon as far as I can tell.
[3154.28 → 3157.84] And so the Haskell learning materials,
[3158.64 → 3159.86] almost all of them assume
[3159.86 → 3161.66] that you've already got some programming experience.
[3161.66 → 3164.92] So they don't explain a lot of really fundamental concepts.
[3164.92 → 3169.60] And they often explain things in terms of like,
[3169.68 → 3171.36] like real world Haskell, the book,
[3171.52 → 3175.42] not to, you know, disrespect it or anything like that,
[3175.48 → 3178.22] but they explain a lot of things in terms of C,
[3178.38 → 3179.08] which I don't know.
[3179.56 → 3184.06] And so things like that were really hard.
[3184.76 → 3186.96] And a lot of the books explain recursion
[3186.96 → 3189.74] in terms of like looping and imperative languages.
[3189.84 → 3191.50] And that was really hard for me to understand
[3191.50 → 3194.50] because I'd never looped anything in an imperative language.
[3195.30 → 3198.16] So that was one of the hurdles.
[3198.32 → 3199.78] The other hurdle for me was that
[3199.78 → 3204.50] a lot of the knowledge that programmers accumulate
[3204.50 → 3206.56] over a period of years,
[3206.56 → 3209.00] doing it as a hobby before they even become professionals,
[3209.74 → 3212.18] things like how to use Git
[3212.18 → 3215.68] and how to use like a lot of the command line stuff,
[3216.28 → 3217.78] those kinds of things I had to learn
[3217.78 → 3220.56] kind of all at the same time that I was starting to learn Haskell.
[3220.70 → 3222.52] And so the first few months of Haskell
[3222.52 → 3225.78] were just like really rough because...
[3227.40 → 3228.92] Rather than learning the programming language
[3228.92 → 3231.74] or actually learning the things to learn a programming language.
[3231.84 → 3232.20] Exactly.
[3232.34 → 3233.64] I was learning the, you know,
[3234.06 → 3235.30] this kind of background knowledge
[3235.30 → 3236.96] that programmers really take for granted.
[3237.34 → 3239.58] And I mean, they didn't always, of course,
[3239.64 → 3241.10] they just learned it so long ago
[3241.10 → 3243.36] for many of them that they've kind of forgotten
[3243.36 → 3247.34] that like these things are not obvious, right?
[3248.28 → 3252.68] So those were the two biggest hurdles for me.
[3253.76 → 3255.26] Haskell itself, I don't think,
[3255.78 → 3258.20] for me, it hasn't been,
[3258.50 → 3260.36] I mean, there are difficult things about it for sure.
[3261.66 → 3263.58] But I really think that
[3263.58 → 3266.62] a lot of it just comes down to how it's taught.
[3266.78 → 3269.74] So one of the things is like not explaining things
[3269.74 → 3271.92] in terms of other languages.
[3271.92 → 3273.68] I don't think that that's actually very helpful
[3273.68 → 3275.86] because Haskell is just so different.
[3276.72 → 3278.92] But a lot of the...
[3280.84 → 3283.68] Well, I mean, everybody starts,
[3283.78 → 3285.76] like you mentioned monads a few minutes ago
[3285.76 → 3288.34] and like kind of everybody or a lot of people
[3288.34 → 3290.30] when they're coming from other programming languages,
[3290.60 → 3292.90] they think, oh, if I'm going to learn Haskell,
[3292.98 → 3293.98] I have to learn about monads.
[3294.06 → 3295.40] And so they try to start there
[3295.40 → 3297.24] and it's really not a good place to start.
[3297.40 → 3298.20] And then they're just kind of,
[3298.20 → 3302.72] they don't really understand the monad.
[3302.84 → 3304.46] And so then they just are like,
[3304.50 → 3305.80] oh, Haskell is going to be too hard.
[3306.30 → 3306.72] And yeah.
[3307.04 → 3307.74] On that note, then,
[3307.74 → 3311.12] what's the best place to start, in your opinion, then?
[3311.16 → 3313.48] Since you came from scratch, so to speak,
[3313.48 → 3314.52] and you even learned what it took
[3314.52 → 3317.44] to learn a programming language,
[3317.54 → 3318.72] what's, in your opinion,
[3318.78 → 3319.86] what's the best place to start?
[3319.94 → 3320.92] What's the what got you?
[3320.92 → 3326.52] One thing I would say about this is that the
[3327.62 → 3329.10] when we started writing the book,
[3329.40 → 3332.82] we had to figure out how to break the language down
[3332.82 → 3336.20] into kind of order,
[3336.92 → 3339.26] a sensible order of how to, how to learn things.
[3339.96 → 3342.58] And if you start really critically analyzing it,
[3342.60 → 3345.14] you realize that, okay, to understand monad,
[3345.22 → 3346.84] which is just a type class, you know,
[3346.84 → 3349.18] it's just a generalization of a pattern, basically.
[3349.18 → 3353.10] Um, you realize that you need to learn certain things
[3353.10 → 3355.78] about type classes, certain kinds of type classes.
[3356.14 → 3358.54] And then you realize in order to understand type classes,
[3358.54 → 3361.52] you got to learn, you know, how types in Haskell work,
[3361.74 → 3363.22] you know, just normal concrete types,
[3363.22 → 3365.38] not just type classes specifically, right?
[3365.60 → 3367.66] And if you follow this kind of regression,
[3368.22 → 3370.24] you'll just land it.
[3370.70 → 3371.18] Okay.
[3371.28 → 3373.10] What's an expression, right?
[3373.16 → 3376.08] And that's more or less where we started in the book.
[3376.08 → 3382.02] And, um, we did end up adding a Lambda Calculus chapter, uh,
[3382.02 → 3384.86] later on before expressions in Haskell,
[3385.08 → 3388.26] but that was the result of having tested the book with learners.
[3388.26 → 3393.02] And it was us addressing a problem that we observed empirically.
[3393.38 → 3393.86] Yeah.
[3394.60 → 3394.82] Okay.
[3394.82 → 3397.52] So you've been talking about the Lambda Calculus
[3397.52 → 3400.48] and the various things you've talked about in the
[3400.52 → 3400.96] in the book.
[3400.96 → 3402.14] So let's just break that open.
[3402.14 → 3404.92] Um, there's a process behind this book.
[3404.96 → 3407.24] You got tons of chapters, a lot of different topics.
[3407.86 → 3410.54] Um, you know, what's the process behind this book?
[3410.60 → 3413.78] How did you actually start the process of writing the book?
[3413.84 → 3415.04] What's behind this book?
[3415.50 → 3416.60] What's behind this book?
[3416.66 → 3419.00] Well, when he first decided he wanted to write the book,
[3419.04 → 3422.46] um, as he mentioned, he, um,
[3422.70 → 3425.84] he wanted to write this book so that he could, um,
[3426.48 → 3428.94] hopefully in his work,
[3429.00 → 3430.90] get people going with Haskell faster, right?
[3430.90 → 3433.20] So the first chapter he sent me,
[3433.86 → 3436.80] actually that material has now been split across a few different chapters.
[3437.14 → 3439.80] Um, but it was already talking about algebraic data types,
[3439.90 → 3441.54] which is, um, is,
[3441.74 → 3445.66] it's in the first half of our book as it currently is.
[3445.82 → 3446.66] But, um,
[3447.02 → 3453.50] the, the way then I responded to the algebraic data types material that he sent
[3453.50 → 3458.00] me was with a lot of questions like, wait, okay,
[3458.00 → 3460.70] I still don't understand this thing and I don't understand this thing.
[3460.70 → 3461.94] And I don't understand this thing.
[3462.74 → 3463.70] And, um,
[3464.24 → 3468.96] as I told him all the things that I didn't understand,
[3468.96 → 3472.48] then he started getting a better idea of how to break down the things that come
[3472.48 → 3473.84] before algebraic data types.
[3473.84 → 3477.08] And some of the other topics,
[3477.08 → 3478.74] in fact, we, um,
[3479.02 → 3484.20] like we have this section of the book that goes from basic data types to type
[3484.20 → 3484.58] classes.
[3484.74 → 3487.84] And originally we didn't have a type classes, um,
[3487.84 → 3488.88] chapter scheduled,
[3488.88 → 3493.52] or I think the types and type classes chapter were both sort of condensed into one
[3493.52 → 3493.94] originally,
[3493.94 → 3495.72] but there were so many things that,
[3495.72 → 3496.86] um,
[3497.34 → 3497.54] well,
[3497.58 → 3497.82] really,
[3497.82 → 3498.72] because I'm the beginner,
[3498.80 → 3500.50] there were so many things that I kept saying,
[3500.50 → 3501.80] I don't understand this.
[3501.92 → 3502.88] I don't understand this,
[3502.88 → 3504.44] that they became two separate chapters.
[3505.32 → 3505.76] One,
[3505.94 → 3511.14] one of the reasons they got split apart is that one of the things that we try to
[3511.14 → 3515.40] do kind of like what you said about the change log itself is we try to be
[3515.40 → 3518.72] honest about how we arrived at an understanding of something.
[3519.06 → 3519.24] Yes.
[3519.24 → 3521.24] And so in the book,
[3521.24 → 3522.68] we include type errors,
[3522.88 → 3524.32] explanations of the type errors.
[3524.44 → 3529.32] We try to anticipate what kind of things they're going to trip over in the course of
[3529.32 → 3532.74] following along with the code and exercises in the book.
[3532.96 → 3536.00] So a lot of the splitting that happened in types and type classes is,
[3536.54 → 3536.68] Oh,
[3536.96 → 3541.34] Julie and I tripped over this weird error or whatever in the process of doing this.
[3541.36 → 3541.70] So we,
[3541.88 → 3542.10] you know,
[3542.12 → 3544.06] we don't want to just address that that's a possibility.
[3544.06 → 3545.44] We want to explain it properly.
[3545.56 → 3546.86] We don't want to just skip over it.
[3546.86 → 3552.24] So the kind of content inflation that happened through that process is also part of
[3552.24 → 3554.62] why they underwent meiosis and split apart.
[3555.00 → 3555.16] Yeah.
[3555.34 → 3560.72] Several people have commented actually on how thorough we are about explaining the
[3560.72 → 3562.04] type errors that you get from the
[3562.24 → 3562.86] from GHC,
[3562.94 → 3563.52] from the compiler.
[3564.32 → 3569.48] But it's really important to be able to read them and be able to understand what
[3569.48 → 3571.48] they're telling you so that you can fix things.
[3571.48 → 3571.70] Right.
[3572.62 → 3574.98] So anyway,
[3574.98 → 3577.52] and so it's been through the process of me,
[3578.26 → 3578.94] mostly me,
[3579.00 → 3579.84] not entirely me.
[3579.94 → 3582.12] Sometimes I ask a question and Chris is even like,
[3582.40 → 3582.58] Oh,
[3582.74 → 3583.80] I'd never thought of that.
[3583.80 → 3585.58] And then he has to investigate it more.
[3587.42 → 3591.68] But it's really been through that process that we kind of came to the order as it is
[3591.68 → 3592.08] now.
[3592.46 → 3597.48] And one thing that I like about it is that then by the time you do get to Monad,
[3597.48 → 3600.02] they don't really,
[3600.02 → 3604.32] they seem completely obvious by the time you get to them.
[3604.40 → 3604.80] It's like,
[3605.12 → 3605.34] Oh,
[3605.54 → 3606.66] if you know what a functor,
[3607.04 → 3607.84] what functors are,
[3608.00 → 3608.24] what an
[3608.34 → 3609.88] what the applicative type class does,
[3610.00 → 3610.62] it's like,
[3610.72 → 3610.94] okay,
[3610.94 → 3612.96] the Monad actually just seems really obvious.
[3612.96 → 3616.58] And I don't know if I'd go so far as simple,
[3616.68 → 3616.98] but yeah,
[3616.98 → 3617.22] I mean,
[3617.22 → 3617.96] it's simple,
[3618.02 → 3618.94] not in the sense of easy,
[3618.96 → 3621.04] but in the sense of not really being that complex.
[3621.38 → 3621.66] Yes.
[3622.10 → 3622.26] Oh,
[3622.28 → 3622.58] I just,
[3623.26 → 3624.86] you can finish your thought when I do that.
[3624.94 → 3625.24] I'm just,
[3625.36 → 3625.86] I finished.
[3626.16 → 3626.32] Oh,
[3626.46 → 3626.72] okay.
[3627.46 → 3629.28] I was going to say something here is,
[3629.36 → 3630.00] is the
[3630.44 → 3634.24] is this idea you mentioned where you began with Monads was that,
[3634.24 → 3634.88] you know,
[3635.30 → 3638.48] your advice early Julie was that maybe that's not the best place to start.
[3638.56 → 3639.36] It was the best,
[3639.50 → 3643.62] the better place to start would be something around the types and things like that to,
[3643.62 → 3645.12] to get into it and to,
[3645.78 → 3647.02] as part of the writing this book,
[3647.06 → 3647.38] you've,
[3647.50 → 3648.64] you've found a
[3648.74 → 3650.74] a better way to go about the
[3650.74 → 3651.82] the Monad situation,
[3651.82 → 3652.28] I guess,
[3652.50 → 3652.78] coming,
[3653.00 → 3657.30] coming to it as a learner rather than being so intimidated by it,
[3657.32 → 3660.06] starting there and getting maybe Chris's perspective,
[3660.06 → 3663.92] which was the several years of false starts and maybe finding a better path into the
[3663.98 → 3665.82] into the language rather than the
[3665.90 → 3667.38] the biggest hill possible,
[3667.38 → 3667.94] so to speak.
[3668.48 → 3668.62] Right.
[3669.26 → 3671.38] So one of the things that,
[3671.68 → 3673.46] so I started with Outbreak Data Types because,
[3673.62 → 3676.78] that seemed to be one of the initial kind of sticking points for people.
[3677.44 → 3678.76] Just kind of observationally,
[3678.80 → 3680.68] because I've prior to working on the book,
[3680.72 → 3683.24] I spent a lot of time working with teaching people one-on-one.
[3683.96 → 3685.36] And I mean,
[3685.36 → 3686.92] I've spent probably hundreds,
[3687.02 → 3690.92] if not over a thousand hours just in IRC the last couple of years,
[3691.10 → 3694.56] helping people learn Haskell and Outbreak Data Types just kind of stood out because,
[3695.64 → 3695.96] again,
[3696.16 → 3701.54] most of the resources didn't really give a super compelling or exercise driven explanation of them.
[3701.54 → 3702.36] They just kind of show you like,
[3702.42 → 3702.56] hey,
[3702.62 → 3707.02] this is how you make a product or what you would call a struct in other languages.
[3707.36 → 3708.02] And then it says,
[3708.10 → 3708.28] hey,
[3708.34 → 3713.68] here's how you make a sum type or what you would call like an enum or enumeration or a union in other languages.
[3714.68 → 3714.96] And,
[3715.04 → 3715.72] and then they're like,
[3715.76 → 3715.88] oh,
[3715.94 → 3716.12] yep,
[3716.20 → 3716.68] that's it.
[3716.76 → 3717.00] Okay,
[3717.04 → 3717.44] we're done.
[3717.54 → 3718.08] Let's move on.
[3718.08 → 3719.76] And that's pretty abrupt.
[3719.98 → 3720.70] So that's why it stood out.
[3720.76 → 3721.42] And I started there.
[3722.30 → 3728.20] Breaking down Monad arose again from that one-on-one teaching process where I,
[3728.54 → 3731.04] I wouldn't call it Socratic,
[3731.38 → 3736.28] but I try to be more inquisitive when teaching somebody in a tutoring environment than most teachers are.
[3736.28 → 3740.04] So when somebody got confused with something like Monad,
[3740.14 → 3742.16] it was usually the questions,
[3742.46 → 3742.60] you know,
[3742.64 → 3745.16] kind of like almost like a Toyota five wise,
[3745.40 → 3748.46] but for education where you keep asking a question until you get to the root cause.
[3750.16 → 3752.16] The root cause was never Monad itself.
[3752.36 → 3757.64] It was this vast sea of other things that nobody had bothered to explain to them.
[3757.82 → 3757.84] Yeah,
[3757.92 → 3758.36] that's true.
[3758.84 → 3760.12] I didn't really understand.
[3760.12 → 3760.68] Well,
[3761.68 → 3764.54] we had already kind of written the type classes chapter, and it was almost finished,
[3764.54 → 3768.32] but then Chris was already working on the Monoid chapter,
[3768.44 → 3773.54] which is kind of the first one of our big chapters about a specific type class.
[3774.60 → 3776.34] So he's writing the Monoid chapter.
[3776.46 → 3779.46] And I realized when I was reading his first draft of that,
[3779.76 → 3780.16] that like,
[3780.36 → 3783.02] actually there were still things about type classes I didn't understand.
[3783.14 → 3788.20] And so we went back then and revised the type classes chapter more based on my
[3788.20 → 3789.62] misunderstandings of type classes.
[3790.12 → 3792.56] So that then by the time you do get to Monoid,
[3792.82 → 3793.18] it's like,
[3793.26 → 3793.38] okay,
[3793.38 → 3796.30] this thing is a type class that just does this,
[3796.48 → 3796.64] right?
[3796.76 → 3798.94] It just is a way to talk about these functions,
[3799.18 → 3800.38] basically these operations.
[3801.50 → 3807.74] I have an anecdote from when I went to Philadelphia for the Hack Phi kind of Haskell meetup.
[3808.70 → 3811.68] And one of the
[3811.78 → 3812.94] this was long,
[3813.08 → 3816.38] this was after we had already written the Monoid chapter and kind of figured a lot of this out,
[3816.38 → 3819.94] but I was helping a student at Penn.
[3820.12 → 3823.54] who was taking the CIS 552 class,
[3823.64 → 3825.44] which sounds grad student-y,
[3825.56 → 3827.72] but really like a lot of juniors and seniors take it.
[3827.84 → 3829.88] And it's kind of an intermediate Haskell class.
[3830.02 → 3830.14] It,
[3830.24 → 3831.32] you know,
[3831.40 → 3835.06] and it goes into Monads and Monad Transformers and that sort of thing.
[3835.60 → 3836.04] And,
[3836.04 → 3837.04] um,
[3837.04 → 3838.36] I really like teaching people one-on-one.
[3838.48 → 3839.60] I have a lot of fun doing it.
[3840.08 → 3844.22] And so we were towards the end of the little meetup or mini conference thing.
[3844.46 → 3847.00] So I ended up working with him for about three,
[3847.10 → 3847.94] three and a half hours.
[3848.44 → 3848.76] And,
[3848.76 → 3851.66] but his original problem was I don't understand Monads.
[3851.66 → 3856.42] And I asked the TA that was working with him,
[3856.48 → 3857.18] if I can try,
[3857.34 → 3857.66] you know,
[3857.84 → 3858.80] try doing my thing with him.
[3858.92 → 3859.60] And then the TA,
[3859.72 → 3859.88] you know,
[3859.88 → 3860.02] said,
[3860.08 → 3860.24] yeah,
[3860.32 → 3861.74] I'd love to see how you do it.
[3862.12 → 3862.48] And,
[3862.64 → 3863.20] but the thing is,
[3863.20 → 3866.54] is pretty quickly within the first like 10 minutes of just asking him questions,
[3866.92 → 3867.96] Monad was not the problem.
[3867.96 → 3872.84] We had to go all the way back to just how the type system worked because he didn't understand how the
[3872.84 → 3874.22] how polymorphism worked.
[3874.50 → 3875.38] And since,
[3875.38 → 3876.02] you know,
[3876.76 → 3883.50] Monad itself is a generalization that uses the polymorphism in the type class to have those generalized operations.
[3883.66 → 3885.70] How can you possibly understand if you don't roll back to that?
[3886.06 → 3887.42] I didn't get him all the way to Monad.
[3887.52 → 3889.74] I got him from types all the way up to functors,
[3890.12 → 3892.04] but that was enough.
[3892.74 → 3892.92] He,
[3893.10 → 3895.44] I talked to him and email a couple of times after that.
[3895.44 → 3898.50] And once he understood higher kind of types and type classes,
[3898.50 → 3899.26] he was good to go.
[3899.92 → 3900.86] So you guys have this,
[3901.10 → 3902.18] this approach to this book,
[3902.18 → 3903.32] which I haven't seen elsewhere,
[3903.32 → 3909.56] which does you don't just have a professional speaking to a hypothetical audience.
[3909.56 → 3912.18] You have kind of a beginner professional relationship.
[3912.94 → 3914.32] You have the mentor mentee model.
[3914.70 → 3916.38] Tell us how that comes through.
[3916.80 → 3923.02] Obviously it makes sense to me intuitively that just having the beginner feedback as Chris,
[3923.10 → 3924.84] you write makes tons of sense.
[3924.84 → 3926.28] And it makes a book a better product,
[3926.28 → 3928.10] but how does your,
[3928.16 → 3929.04] you're coauthoring it?
[3929.08 → 3931.96] So how does the Julie's voice and your voice,
[3932.04 → 3933.06] how does the tone work?
[3933.16 → 3934.68] You guys actually have like,
[3934.78 → 3936.96] is there a dialogue through this book?
[3937.04 → 3937.82] Tell us the style,
[3937.90 → 3938.80] how it reads and,
[3938.90 → 3941.94] and how your guys' coauthor ship plays into that.
[3942.94 → 3944.66] Let me give you an idea of how we write,
[3944.82 → 3947.64] how we are process of writing a chapter.
[3947.64 → 3948.20] Um,
[3948.44 → 3952.08] so Chris lays down an initial,
[3952.08 → 3956.86] an initial scaffold or skeleton of what's going to be in the chapter so that I can start
[3956.86 → 3959.42] reading other materials.
[3959.42 → 3965.24] So like I'll go to the other books that exist for Haskell or blog posts or whatever I can find on the
[3965.40 → 3965.88] on that,
[3966.16 → 3968.22] those topics and start reading them.
[3968.22 → 3969.42] So I get a sense of what's coming.
[3969.42 → 3971.08] And then he starts laying out a bunch of,
[3971.08 → 3975.54] usually a bunch of bare code examples.
[3975.54 → 3975.84] We'll,
[3975.90 → 3976.26] we'll say,
[3976.40 → 3980.78] and sometimes he makes me just figure out the code by myself.
[3980.78 → 3982.48] And then I write the surrounding pros,
[3982.54 → 3983.64] explaining what's going on.
[3983.90 → 3984.22] Um,
[3984.24 → 3989.12] sometimes he writes a little bit of pros and I just go through and start editing it,
[3989.12 → 3990.58] but his pros tend to be,
[3990.58 → 3991.22] um,
[3992.18 → 3994.82] his pros tends to be on the dense side.
[3995.02 → 3995.88] And so,
[3995.88 → 3996.42] um,
[3996.42 → 3997.70] it can be a little hard to,
[3998.48 → 4003.66] and so part of my job is to tease out the
[4003.66 → 4005.00] the things that are,
[4005.24 → 4006.74] that we're wanting people to get out of it.
[4006.88 → 4007.06] So,
[4007.48 → 4007.96] um,
[4008.38 → 4009.72] then he,
[4009.72 → 4011.60] after I've written some stuff,
[4012.00 → 4012.32] he,
[4012.66 → 4014.74] it goes back to him, and he starts,
[4014.74 → 4016.40] um,
[4016.54 → 4017.90] adding things,
[4018.14 → 4021.36] adding more examples and places where I had questions,
[4021.84 → 4022.94] answering my questions,
[4023.40 → 4023.94] um,
[4024.28 → 4026.98] and so on.
[4026.98 → 4032.98] And then it'll come back to me, and I'll sort of go through and make everything,
[4032.98 → 4035.28] make sure everything has kind of a coherent flow.
[4035.62 → 4036.46] and,
[4036.56 → 4036.88] um,
[4037.80 → 4038.76] I try to,
[4038.86 → 4039.38] you know,
[4039.38 → 4041.36] pretty up some of our typos and stuff like that.
[4041.46 → 4043.46] I do miss some, and we get emails about them,
[4043.70 → 4046.46] but that's kind of perspective for the
[4046.62 → 4047.06] for the book.
[4047.10 → 4051.48] Is it written from Chris's perspective with your influence or is it both of your
[4051.48 → 4052.98] voices in the book?
[4052.98 → 4054.72] Is it Julie and Chris together?
[4054.72 → 4058.30] Or is it simply Chris with Julie's influence behind the scenes?
[4058.30 → 4060.70] I think at this point early in the book,
[4060.70 → 4062.80] I think it was Chris with just Julie's influence.
[4063.12 → 4063.44] Um,
[4063.96 → 4065.44] I think at this point though,
[4065.82 → 4066.32] um,
[4066.82 → 4069.66] I think it's really both of us co-writing.
[4070.02 → 4070.24] I mean,
[4070.60 → 4070.90] you can,
[4071.02 → 4072.06] you can see,
[4072.06 → 4074.54] there are times when I,
[4074.54 → 4077.86] when I look at a paragraph from say like the folds chapter,
[4078.02 → 4079.40] which I haven't looked at in a while.
[4079.40 → 4080.80] And if I go back and reread it,
[4080.84 → 4082.26] I'll look at a paragraph and be like,
[4082.34 → 4082.54] yep,
[4082.74 → 4083.56] Chris wrote that paragraph.
[4083.56 → 4085.10] Like I can totally tell that's his voice,
[4085.10 → 4085.92] but,
[4086.10 → 4086.46] um,
[4086.46 → 4088.84] most of it now is not that distinctive.
[4088.84 → 4091.06] Like we've kind of converged on,
[4091.06 → 4092.62] uh,
[4093.16 → 4093.70] I think a
[4093.82 → 4095.74] a fairly,
[4095.94 → 4096.80] yeah.
[4097.10 → 4098.32] A together writing voice,
[4098.38 → 4099.44] a co-writing voice.
[4099.44 → 4100.14] I think now.
[4100.36 → 4101.06] I would agree with that.
[4101.14 → 4101.48] And I mean,
[4101.48 → 4104.08] Julie's confidence picked up relatively early in the book,
[4104.08 → 4104.82] uh,
[4104.82 → 4105.86] partly out of necessity.
[4105.86 → 4107.52] It started with the Thai classes chapter,
[4107.52 → 4107.94] I think.
[4108.02 → 4108.34] Yes.
[4108.40 → 4112.44] Where she started really doing a lot of the original writing explanation herself.
[4112.60 → 4112.80] Yeah.
[4112.80 → 4115.88] And part of the reason for that is that I was,
[4115.88 → 4116.88] uh,
[4117.28 → 4117.62] very,
[4117.62 → 4120.96] very quickly about to lose my mind in the folds chapter.
[4121.32 → 4121.52] Yeah.
[4121.70 → 4123.50] He was working on the folds chapter when I,
[4123.54 → 4124.82] and he just kind of,
[4125.36 → 4125.58] he,
[4125.70 → 4126.58] he did put some,
[4126.86 → 4130.10] some code and a general outline of what needed to be in the type classes
[4130.10 → 4130.42] chapter.
[4130.52 → 4131.56] He put that there for me.
[4131.56 → 4132.62] And then he was like,
[4132.64 → 4134.16] I have to deal with this fold stuff.
[4134.20 → 4137.56] He was trying to explain how folds evaluate in Haskell.
[4137.88 → 4138.16] And,
[4138.22 → 4138.54] um,
[4138.94 → 4140.00] it got into,
[4140.48 → 4141.36] it got,
[4141.98 → 4142.42] he,
[4142.54 → 4143.90] he sort of started,
[4144.02 → 4144.74] did start,
[4145.12 → 4146.28] sort of start losing his mind.
[4146.28 → 4146.72] Um,
[4146.72 → 4149.20] and so he just kind of threw me the type classes chapter.
[4149.30 → 4150.62] And that's when I really started to,
[4150.62 → 4151.94] um,
[4152.28 → 4154.42] kind of insert my own voice into that,
[4154.72 → 4155.78] into the book a lot more.
[4155.78 → 4158.10] But I think by this point we've,
[4158.44 → 4161.88] we've really converged on like the chapter has a more sort of,
[4161.96 → 4162.14] you know,
[4162.28 → 4165.98] each chapter has sort of a more unified voice of the two of us writing
[4165.98 → 4166.38] together.
[4166.38 → 4168.44] So I do write,
[4168.44 → 4170.90] I do write example code for the books.
[4171.06 → 4171.42] Um,
[4171.42 → 4174.06] and I write some of the exercises even now too.
[4174.18 → 4176.40] Whereas when we first started writing the book together,
[4176.40 → 4176.62] I mean,
[4176.62 → 4180.26] I was terrified of putting any of my own code in the book because I was
[4180.26 → 4181.80] certain it was going to be wrong,
[4181.86 → 4182.12] you know,
[4182.12 → 4183.18] because I was such a beginner,
[4183.38 → 4183.62] but,
[4183.96 → 4184.36] um,
[4184.90 → 4185.98] he does check them.
[4185.98 → 4189.02] So he does check my code,
[4189.16 → 4189.30] but,
[4189.30 → 4192.50] and I check his,
[4192.70 → 4193.52] I make sure it runs.
[4194.86 → 4195.06] So Julie,
[4195.12 → 4196.42] you definitely as a linguist bring,
[4196.52 → 4198.50] I'm sure excellent pros,
[4198.54 → 4199.12] uh,
[4199.12 → 4201.86] to the book as well as the perspective that you have.
[4202.46 → 4202.94] Um,
[4203.22 → 4205.30] you're also a homeschooling mom.
[4205.46 → 4205.62] So,
[4205.62 → 4206.72] um,
[4207.42 → 4207.62] yeah,
[4207.62 → 4210.88] how does that play into your teaching style or is there any,
[4210.88 → 4211.68] uh,
[4211.68 → 4216.22] influence from your teaching your children into writing the book or vice
[4216.22 → 4216.52] verse?
[4217.36 → 4217.80] Well,
[4217.88 → 4218.60] I was a teacher,
[4218.60 → 4219.58] um,
[4219.88 → 4221.06] before I was a
[4221.52 → 4222.32] before I was a mom,
[4222.42 → 4223.40] before I was a homeschooler,
[4223.44 → 4223.84] I was a teacher.
[4223.84 → 4225.72] I taught when I was in graduate school,
[4225.72 → 4226.66] I was a teaching assistant.
[4226.66 → 4228.62] So I taught composition and I taught,
[4228.62 → 4229.38] um,
[4229.48 → 4230.58] English as a second language.
[4230.58 → 4234.54] I think actually the English as a second language experience helped quite a
[4234.54 → 4235.08] bit because,
[4235.08 → 4235.84] um,
[4236.14 → 4239.90] there's some overlap between teaching a human language and teaching a
[4239.90 → 4240.66] programming language.
[4240.66 → 4241.14] Um,
[4241.32 → 4243.52] I think.
[4243.82 → 4244.26] And,
[4244.34 → 4244.90] um,
[4245.34 → 4247.50] so for homeschool,
[4247.76 → 4248.32] um,
[4248.60 → 4253.70] one of the things I really like about homeschool is that,
[4253.70 → 4254.76] um,
[4254.98 → 4259.60] I can give my kids a lot of freedom to explore topics that they're
[4259.60 → 4261.08] interested in and to,
[4261.30 → 4261.84] you know,
[4261.84 → 4262.40] we can,
[4262.40 → 4264.78] we can get off of our homeschool schedule.
[4264.78 → 4265.84] If there's something that they're,
[4265.84 → 4267.34] that they've taken a real interest in.
[4267.34 → 4267.56] Right.
[4267.56 → 4267.78] And,
[4267.78 → 4270.76] and they want to explore it for a few more days.
[4270.76 → 4271.04] Right.
[4271.10 → 4275.16] And we go through this almost every spring when they discover some new type of
[4275.16 → 4276.34] insect, and they just want to,
[4276.46 → 4276.94] I have boys,
[4277.00 → 4278.86] I have two boys, and they'll find,
[4278.92 → 4279.10] you know,
[4279.10 → 4280.10] some new kind of insect.
[4280.10 → 4284.72] And we spent like a week talking about nothing but roly-polies and how they're
[4284.72 → 4286.58] not actually insects one time.
[4287.14 → 4289.18] And so we have the freedom to do that.
[4289.18 → 4289.58] And,
[4289.64 → 4290.10] um,
[4290.10 → 4294.50] I think to a certain extent that has informed the way we've written the book,
[4294.50 → 4299.90] because we really encourage people to take like some example in the book and
[4299.90 → 4303.26] some example code or some concept in the book and just play with it.
[4303.26 → 4303.66] And like,
[4303.74 → 4304.20] well,
[4304.20 → 4306.98] what's going to happen if you change it to do this and what's going to happen if
[4306.98 → 4307.44] you change,
[4307.66 → 4308.14] you know,
[4308.14 → 4311.12] the type signature to this and just play with it,
[4311.12 → 4311.32] you know,
[4311.32 → 4312.70] just explore this and see,
[4312.80 → 4316.78] because you're going to learn a lot by doing that and not only doing just
[4316.78 → 4317.96] exactly what we tell you.
[4318.04 → 4318.18] Right.
[4318.70 → 4322.02] Another thing we do in the book to try to encourage people to explore and kind
[4322.02 → 4322.66] of,
[4322.66 → 4322.94] you know,
[4323.06 → 4325.48] dig as deep as is going to satisfy them is beginning,
[4325.48 → 4328.18] even with the initial Lambda calculus chapter,
[4328.50 → 4332.80] we put follow-up reading at the end of pretty much every chapter.
[4332.92 → 4334.28] There may be one we don't,
[4334.40 → 4338.78] but there's for the most part follow decent list of follow-up reading in every
[4338.78 → 4339.14] chapter.
[4339.14 → 4343.02] And one of the things we do with that list of follow-up reading is we try to
[4343.02 → 4347.56] order it by both what's going to be easiest for them to understand and also
[4347.56 → 4351.50] what's nearest to hand or nearest to their experience.
[4351.76 → 4353.66] So the more theoretical stuff will come later,
[4353.70 → 4355.32] even if it's not necessarily harder.
[4356.28 → 4359.98] And a fair number of our readers have really appreciated that because some of
[4359.98 → 4361.40] them are more theoretically inclined.
[4361.98 → 4364.94] Some of them just want to dig more into operational and technical details,
[4364.94 → 4366.98] but that's available for them.
[4366.98 → 4369.66] Even if we don't really have time in the book to talk about it.
[4369.92 → 4374.08] And then they have kind of a recommended list of materials that we've vetted and
[4374.08 → 4376.80] checked out for ourselves and kind of ranked in that little listing.
[4377.40 → 4377.64] Yeah.
[4378.70 → 4379.10] So,
[4379.28 → 4380.12] um,
[4380.40 → 4381.26] and then of course,
[4381.38 → 4382.16] now I'm,
[4382.40 → 4382.76] um,
[4382.76 → 4384.60] as part of homeschool,
[4384.60 → 4386.96] I'm actually testing the book with my 10-year-old son,
[4387.10 → 4387.98] soon to be 11.
[4388.08 → 4389.12] He'll be 11 in two weeks.
[4389.12 → 4390.48] Um,
[4390.74 → 4395.22] and I was really surprised because when he first started the book,
[4395.22 → 4396.06] um,
[4396.06 → 4398.06] we didn't have a Lambda calculus chapter yet.
[4398.06 → 4401.20] And then a bunch of crazy things happened in our life.
[4401.20 → 4402.56] And so he wasn't able to,
[4402.56 → 4405.08] to keep doing Haskell like over the summer and stuff.
[4405.08 → 4407.90] And so when he came back to the book,
[4407.90 → 4408.22] I said,
[4408.28 → 4408.40] well,
[4408.40 → 4412.12] now we've added this chapter on the Lambda calculus and I want to see if you can do it.
[4412.12 → 4416.38] It's fully expecting that a 10-year-old would have a really hard time with the Lambda
[4416.38 → 4416.76] calculus.
[4416.76 → 4418.58] Because it's something I learned about in college,
[4418.66 → 4419.04] you know?
[4419.84 → 4420.24] And,
[4420.30 → 4420.68] um,
[4421.54 → 4424.30] he read the chapter.
[4424.52 → 4427.28] There were some terms that he didn't understand very well.
[4427.46 → 4428.84] And so he gave us some,
[4429.16 → 4432.94] that gave us some ideas of how we could revise it so that it's,
[4433.00 → 4433.40] um,
[4433.40 → 4437.54] the terms are a little clearer to people who maybe don't have some of that vocabulary
[4437.54 → 4438.06] already.
[4438.88 → 4439.32] Um,
[4439.92 → 4440.68] and,
[4440.68 → 4441.82] but he,
[4442.02 → 4443.62] he read the Lambda calculus chapter.
[4443.72 → 4444.60] He did the exercises.
[4444.60 → 4445.54] He really liked it.
[4445.54 → 4446.56] He thought it was really cool.
[4447.24 → 4447.60] And,
[4447.66 → 4447.96] uh,
[4448.38 → 4450.98] that was exciting for me to be able to introduce that to,
[4451.10 → 4452.10] to him,
[4452.12 → 4452.40] you know,
[4452.40 → 4452.58] and,
[4452.86 → 4453.06] and,
[4453.16 → 4453.36] uh,
[4453.36 → 4454.46] find that he enjoyed it.
[4454.60 → 4457.26] So there was only that one exercise he got stuck on.
[4457.32 → 4458.78] He was able to do all the others by himself.
[4458.78 → 4459.20] Wasn't he?
[4459.34 → 4459.36] Yeah.
[4459.36 → 4459.58] Yeah.
[4459.58 → 4460.80] The last exercise of the
[4461.00 → 4462.36] of the reduction.
[4462.64 → 4462.96] Yeah.
[4462.96 → 4463.68] The hardest one.
[4463.88 → 4463.90] Yeah.
[4463.90 → 4464.50] The hardest one.
[4464.56 → 4467.64] He got kind of stuck on because he lost track of some of his variables.
[4467.90 → 4470.06] There's some tricky stuff with alpha renaming in that one.
[4470.24 → 4470.40] Yeah.
[4470.44 → 4472.32] So I just kind of got him over that hump.
[4472.32 → 4475.82] Like we traced his steps back to where he got confused and then,
[4476.10 → 4477.26] and then he was able to figure it out.
[4477.28 → 4477.60] And I was,
[4477.98 → 4479.28] that was really exciting for me to,
[4479.38 → 4480.12] to share that with him.
[4480.12 → 4481.32] And so now he's in chapter,
[4481.32 → 4482.26] uh,
[4482.26 → 4482.62] four,
[4482.70 → 4483.08] I think,
[4483.38 → 4483.76] and,
[4483.82 → 4484.12] um,
[4485.12 → 4485.84] going strong.
[4485.84 → 4486.98] So he occasionally,
[4487.52 → 4489.42] occasionally stuff that he stumbles over,
[4489.50 → 4490.92] we find a place where we need to,
[4490.92 → 4491.34] you know,
[4491.78 → 4492.50] go back.
[4492.70 → 4497.56] And so writing the book informs my homeschool to a certain extent.
[4497.64 → 4499.28] And then homeschool informs the writing of the book.
[4499.32 → 4501.22] And it's all kind of nice synthesis.
[4501.48 → 4502.30] I'll just say for the listeners,
[4502.54 → 4506.58] Julie's been writing about the process of teaching Haskell to her 10-year-old on
[4506.58 → 4507.12] her blog.
[4507.38 → 4509.42] We will link that up in the show notes.
[4509.42 → 4513.70] I wanted to point out this quote because I just loved it where he gives you,
[4513.70 → 4514.06] uh,
[4514.06 → 4514.64] an ultimatum.
[4514.76 → 4518.00] I think you're quoting yourself on Twitter here where your son said,
[4518.08 → 4518.30] well,
[4518.36 → 4522.92] I'm going to keep learning JavaScript until you teach me Haskell and,
[4522.92 → 4523.42] uh,
[4523.58 → 4524.62] hashtag it ultimatum.
[4524.72 → 4528.40] So it seems like he was ready to go, and he was ready to use JavaScript against
[4528.40 → 4528.64] you.
[4530.06 → 4530.50] Yeah.
[4530.70 → 4530.94] Well,
[4531.12 → 4531.44] he,
[4531.60 → 4531.96] um,
[4533.00 → 4535.76] JavaScript was the first sort of experimenting he did.
[4535.76 → 4537.18] And I think with Khan Academy,
[4537.74 → 4539.24] I think it might,
[4539.42 → 4540.12] it's Khan Academy.
[4540.24 → 4542.72] They have like an hour of code every winter.
[4542.72 → 4543.54] I think it is.
[4543.76 → 4547.32] And so they have this little JavaScript program that the kids can do to make a
[4547.32 → 4548.84] Christmas card is what he made.
[4549.66 → 4551.24] And he had a perfect time with that.
[4551.34 → 4555.14] But a lot of the things that he was doing with the JavaScript were really opaque
[4555.14 → 4555.54] to him.
[4555.58 → 4557.32] He didn't really understand what he was doing.
[4557.82 → 4558.64] And then,
[4558.64 → 4559.42] um,
[4560.36 → 4561.34] after that,
[4561.34 → 4562.42] he was taking this,
[4562.42 → 4562.92] um,
[4562.92 → 4565.96] class learning how to make Minecraft mods.
[4566.54 → 4568.98] And I think there was a lot of good stuff in the class.
[4568.98 → 4569.88] And he was really excited,
[4570.00 → 4570.22] of course,
[4570.22 → 4571.80] to be making his own mod,
[4571.88 → 4572.08] you know,
[4572.08 → 4574.34] and making his own weapons for Minecraft and stuff.
[4574.76 → 4576.26] But that's of course,
[4576.34 → 4576.64] Java.
[4576.84 → 4577.08] And,
[4577.20 → 4577.50] um,
[4577.88 → 4578.24] he,
[4578.58 → 4579.62] again,
[4579.62 → 4582.62] he didn't understand a lot of what was going on with the actual Java.
[4582.72 → 4584.40] A lot of it was like kind of copying and pasting.
[4585.42 → 4585.82] And,
[4585.82 → 4586.74] um,
[4586.74 → 4588.10] when he started learning Haskell,
[4588.64 → 4590.70] I think he felt more like,
[4590.70 → 4591.38] oh,
[4591.40 → 4593.40] now I actually understand what's happening.
[4593.40 → 4595.76] So even though it's taking me a little bit longer to learn,
[4595.76 → 4597.60] like I'm not just copying and pasting things,
[4597.60 → 4600.28] I'm actually understanding what I'm doing.
[4600.28 → 4601.70] And that was really exciting for him.
[4601.70 → 4606.68] I think the counterintuitive takeaway from this experience is that I think that
[4606.68 → 4610.14] having graphics or something interactive can definitely help get kids
[4610.14 → 4610.56] interested.
[4611.02 → 4611.12] Yeah.
[4611.18 → 4615.84] But I think that we undervalue the intrinsic motivation that comes with
[4615.84 → 4618.86] actually understanding what you're doing instead of copying and pasting.
[4618.86 → 4619.34] Yeah.
[4619.48 → 4620.88] And I mean,
[4621.42 → 4623.12] our book basically starts with arithmetic,
[4623.64 → 4623.96] you know?
[4624.48 → 4624.62] Yeah.
[4624.76 → 4625.16] Um,
[4625.76 → 4627.14] but that's still enough,
[4627.48 → 4627.82] you know?
[4627.90 → 4630.82] And I think that if you can make it interactive,
[4630.82 → 4632.02] then I think that's valuable,
[4632.02 → 4635.46] but I don't think it's worth sacrificing real comprehension for.
[4635.96 → 4636.40] Yeah.
[4636.52 → 4637.30] I'd say if you can,
[4637.38 → 4638.94] if you can pick the curiosity,
[4638.94 → 4640.74] then you're,
[4641.08 → 4641.20] you know,
[4641.20 → 4644.36] cause a lot of the times the interaction is to pique curiosity,
[4644.36 → 4644.76] right?
[4644.76 → 4646.38] It's to get them interested,
[4646.38 → 4648.76] but if you can get them interested without the interaction,
[4648.76 → 4650.52] there's more substance,
[4650.52 → 4651.46] uh,
[4651.46 → 4652.36] than a lot of the
[4652.44 → 4653.26] um,
[4653.26 → 4654.02] other ways of doing it.
[4654.02 → 4654.18] I've,
[4654.20 → 4655.54] I've gone through, and I love,
[4655.78 → 4658.74] I love what they have up on the code.org with the
[4658.84 → 4659.04] uh,
[4659.26 → 4662.54] the different things for kids to get into it and just to get them interested.
[4662.54 → 4663.48] And then the idea is like,
[4663.54 → 4663.96] that's,
[4663.96 → 4664.98] that's a
[4665.04 → 4667.26] to whet your appetite and now take you somewhere else.
[4667.26 → 4668.30] Um,
[4668.30 → 4668.46] and,
[4668.64 → 4669.96] and my experience with my kids,
[4670.00 → 4670.10] I,
[4670.22 → 4670.98] my oldest is seven.
[4671.08 → 4671.74] So a little bit younger,
[4671.74 → 4672.42] but it's,
[4672.82 → 4674.70] it's very much the end of,
[4674.80 → 4675.36] of the road,
[4675.36 → 4675.96] of the road,
[4676.00 → 4676.42] unfortunately,
[4676.54 → 4676.72] at least,
[4676.74 → 4677.34] at least for now.
[4678.00 → 4678.36] Um,
[4678.90 → 4679.18] yeah,
[4679.30 → 4680.72] because there's not much beyond that.
[4680.72 → 4683.86] It's like we were saying earlier how,
[4683.98 → 4684.24] um,
[4684.28 → 4684.54] you know,
[4684.54 → 4686.82] a lot of people came to programming because they were,
[4687.06 → 4688.56] they were interested in video games,
[4688.56 → 4688.80] right?
[4688.80 → 4689.02] That,
[4689.16 → 4689.80] that,
[4690.00 → 4691.62] that interest just.
[4692.88 → 4695.24] Whets their appetite for learning a lot more about it.
[4695.28 → 4696.66] And I think that was true for him.
[4696.66 → 4697.22] Um,
[4697.52 → 4698.42] but you know,
[4698.42 → 4701.52] I think that one thing that disappoints me is sometimes like,
[4701.52 → 4703.04] um,
[4703.04 → 4709.22] when I hear people talk about teaching programming to kids and stuff is that kids are really a lot smarter than we often give them credit for.
[4709.78 → 4710.22] Um,
[4710.64 → 4714.80] they're not the same as adults, and obviously they don't have the same vocabulary as a lot of adults,
[4714.80 → 4718.20] but they're really a lot smarter and more capable of figuring things out than,
[4718.20 → 4718.76] um,
[4718.78 → 4720.28] a lot of people want to give them credit for.
[4720.40 → 4721.74] And so,
[4721.94 → 4722.66] um,
[4723.10 → 4725.40] I try to do that.
[4725.40 → 4727.82] And I guess the attitude is also kind of informed the book.
[4727.82 → 4729.46] Like we don't want to,
[4729.46 → 4732.08] we want to make Haskell accessible,
[4732.08 → 4737.52] but without like ever talking down to our readers or assuming they're not capable of learning things,
[4737.58 → 4737.80] you know?
[4737.80 → 4739.00] Yeah,
[4739.02 → 4740.66] this was actually an issue we had.
[4740.84 → 4745.86] We were publishing this book independently right now and making it available independently,
[4745.86 → 4748.74] but we actually had a publisher before that we separated from.
[4748.74 → 4749.50] And one of the
[4749.60 → 4752.80] one of the many points of disagreement we had with them was,
[4752.80 → 4759.52] so the big scary sequence of chapters in the book that begin the second half or monoid functors,
[4759.62 → 4760.42] applicative and monad,
[4760.86 → 4762.42] you don't know what those words mean.
[4762.76 → 4763.40] That's fine.
[4763.62 → 4764.36] You don't have to.
[4764.44 → 4765.28] We'll explain it.
[4765.68 → 4771.54] But one of the issues is that they didn't want to send him the chapters after what the chapters were about,
[4771.54 → 4774.22] because people were afraid of the names,
[4774.36 → 4774.88] the words.
[4775.44 → 4778.52] And part of the way we write and the way we talk to our readers is we say,
[4778.60 → 4778.92] all right,
[4779.62 → 4780.98] suspend your fear for a bit.
[4781.44 → 4782.90] We will get you where you need to go,
[4783.32 → 4784.36] but you can't,
[4784.36 → 4786.62] you can't just permanently hide stuff like that.
[4786.62 → 4788.78] One of the problems with renaming things,
[4789.28 → 4789.40] you know,
[4789.46 → 4794.90] like monoid and monad is that you're essentially taking control over their education.
[4795.58 → 4797.40] Because if you use some other term for monad,
[4797.50 → 4798.68] like say computation expression,
[4799.16 → 4802.62] are they going to be able to find all the research and all the writing about monad?
[4802.84 → 4802.98] No.
[4803.50 → 4805.20] You're now fractured quite a bit too,
[4805.28 → 4807.08] by just creating confusion.
[4807.66 → 4807.92] Yeah.
[4808.20 → 4808.56] Yeah.
[4808.56 → 4814.66] And the thing is really what we would rather do is get people to a place where they're no longer afraid of things that they don't understand.
[4815.08 → 4820.76] And instead react to those experiences with curiosity and more of an open,
[4820.96 → 4821.04] like,
[4821.12 → 4821.44] okay,
[4821.58 → 4823.36] this is a thing I don't know.
[4823.58 → 4824.78] Why don't you explain it to me?
[4824.90 → 4825.06] Right.
[4825.28 → 4825.64] And,
[4825.82 → 4826.02] you know,
[4826.02 → 4829.28] the honest is on us to actually make it understandable and that's our responsibility.
[4829.38 → 4833.56] But I don't think you do anyone any favours by just fragmenting the
[4833.56 → 4834.46] you know,
[4834.48 → 4834.96] vocabulary.
[4835.50 → 4841.92] And calling the chapter functor and keeping that word in there instead of trying to rename it to something else gave me a chance to talk about Rudolf Carnap.
[4842.10 → 4842.24] So,
[4842.36 → 4843.28] you know,
[4843.28 → 4844.14] very close to my heart.
[4844.46 → 4844.64] Oh,
[4844.68 → 4844.94] yes.
[4845.20 → 4845.84] It's a good excuse.
[4846.54 → 4846.68] Well,
[4846.68 → 4846.86] Julie,
[4846.92 → 4848.86] you've gotten me interested on two points.
[4848.94 → 4849.84] First,
[4849.88 → 4852.62] you said really poise aren't insects.
[4852.74 → 4853.28] And so I'm over here.
[4853.32 → 4854.06] I'm just going to,
[4854.06 → 4856.04] I'm just going to teach myself that one with Google.
[4856.04 → 4857.72] And then I don't know who that fellow is.
[4857.72 → 4858.22] You just mentioned,
[4858.32 → 4859.80] but maybe you can tell me off.
[4860.60 → 4861.74] Rudolf Carnap was a
[4861.74 → 4862.18] um,
[4862.22 → 4862.64] a large,
[4862.78 → 4863.42] a logician.
[4863.96 → 4864.34] Um,
[4864.34 → 4865.68] and he,
[4866.24 → 4867.12] as far as I can tell,
[4867.16 → 4868.18] he's the first one who,
[4868.36 → 4868.80] um,
[4868.92 → 4870.12] used the word functor.
[4870.46 → 4873.06] He is actually using the word functor to,
[4873.54 → 4873.88] um,
[4874.02 → 4876.06] in a work of that he wrote about language.
[4876.06 → 4877.68] So it was a philosophy of language book.
[4878.68 → 4879.08] And,
[4879.20 → 4879.62] um,
[4879.70 → 4882.16] that's why I was familiar with it.
[4882.16 → 4884.38] So he describes a functor as being,
[4884.38 → 4885.06] um,
[4885.62 → 4888.46] a sentence level sort of operation.
[4888.46 → 4890.98] So it lifts a sentence up into a different,
[4890.98 → 4893.86] up into this new sort of semantic category.
[4893.86 → 4896.96] So like negation is a functor in his philosophy of language,
[4896.96 → 4899.82] because once you've negated a sentence,
[4899.82 → 4902.44] like that negation applies to like the whole sentence,
[4902.44 → 4902.68] right?
[4902.68 → 4905.72] So it lifts the whole sentence into the realm of negation.
[4905.90 → 4906.42] Right.
[4906.44 → 4908.16] And so that's a functor for Carnap.
[4908.52 → 4909.78] So we,
[4910.00 → 4912.74] there's a paragraph in the introduction to the chapter where it's,
[4912.74 → 4913.20] um,
[4913.24 → 4914.44] I got to indulge my,
[4914.64 → 4914.92] um,
[4915.10 → 4917.80] my love of linguistics.
[4918.38 → 4918.94] We can,
[4918.94 → 4919.28] we can,
[4919.44 → 4921.50] we can definitely detect your passion for sure.
[4921.62 → 4923.80] Great name to Rudolph Carnap.
[4924.56 → 4926.24] Just fun to say.
[4927.54 → 4927.94] Yeah,
[4928.00 → 4928.40] it is.
[4928.98 → 4929.40] Well,
[4929.42 → 4929.62] let's,
[4929.72 → 4929.84] uh,
[4929.84 → 4932.12] let's pause here for our final break and we come back.
[4932.20 → 4935.14] We're going to talk to you guys a little bit more about the book,
[4935.22 → 4936.00] the process,
[4936.06 → 4937.02] where it's at,
[4937.22 → 4938.94] where you think it's going to be LTs.
[4939.20 → 4941.12] It's probably going to be about 1300 pages.
[4941.12 → 4943.28] So there's going to be a lot in there.
[4943.30 → 4944.98] We'll talk about what's in there process.
[4945.08 → 4946.14] You guys are to write it,
[4946.14 → 4948.26] and then we'll close off with our closing questions.
[4948.26 → 4949.86] So stay tuned, and we'll be right back.
[4952.76 → 4957.56] We're working with our friends at BMC to spread the word about true site pulse,
[4957.56 → 4961.34] the real time monitoring service for apps and infrastructure.
[4961.70 → 4963.30] I talked to Mike Moran,
[4963.38 → 4969.12] the senior architect about the idea of dev teams out there rolling their own
[4969.12 → 4973.26] monitoring system using something that's open source or building their own from
[4973.26 → 4973.86] scratch.
[4973.86 → 4975.44] And he had this to say,
[4975.44 → 4980.78] I think if you want to roll your own and spend the dev effort of having to build that
[4980.78 → 4981.30] internally,
[4981.30 → 4982.18] that's great.
[4982.18 → 4985.52] My only question to you is if you spend your time doing that,
[4985.78 → 4990.30] are you providing value to your customer and are you actually moving your product forward
[4990.30 → 4991.70] or are you holding your product back?
[4991.88 → 4995.78] And I think a lot of what something like true site pulse offers you is we take a lot
[4995.78 → 4996.78] of that on for you.
[4996.86 → 4999.80] So you can provide that value to your customer on your product instead.
[4999.80 → 5004.20] So we have plugins for 30 plugins for different parts of your infrastructure.
[5004.20 → 5008.10] We have an agent that's been running for three years written in C that takes a very
[5008.10 → 5009.30] small amount of your resources.
[5009.70 → 5011.14] As you add more servers,
[5011.34 → 5013.24] you're not going to have to worry about the scalability as much.
[5013.26 → 5015.52] And we've written the chef and the puppet scripts for you.
[5015.58 → 5016.62] So that's all taken care of.
[5016.82 → 5018.30] It's letting us worry about it.
[5018.30 → 5019.90] So you can focus on your customers.
[5020.34 → 5022.52] That's kind of the value that true site pulse ads,
[5022.60 → 5024.50] as opposed to you having to do it yourself.
[5024.82 → 5028.12] We've all been in organizations where we've joined and had to rewrite the entire
[5028.12 → 5029.00] monitoring stack.
[5029.36 → 5031.72] And that's just something we didn't want to have to do.
[5032.00 → 5032.84] We want to come in.
[5033.04 → 5034.28] We want that taken care of.
[5034.38 → 5037.52] And then that way we can focus on the things that are going to matter to our customers.
[5038.18 → 5040.92] So of course you want to focus on what matters to your customers.
[5041.30 → 5042.58] That's the whole point.
[5042.58 → 5047.26] But I had to press Mike further about these teams out there that just have to roll their
[5047.26 → 5047.98] own things.
[5048.10 → 5049.94] They get attracted by shiny objects.
[5050.04 → 5050.78] They love to tinker.
[5051.36 → 5056.66] And his advice on remaining focused on delivering customer value and how true site pulse enables
[5056.66 → 5058.00] that is just awesome.
[5058.12 → 5063.06] Developers have this innate ability to want to tinker and to want to build their own and
[5063.06 → 5065.68] to want to customize something exactly as they need it.
[5065.80 → 5066.92] And that's in our DNA.
[5067.18 → 5068.52] It's what makes products great.
[5068.64 → 5070.46] It makes why customers come back.
[5070.60 → 5075.24] I think sometimes we get a little distracted, and sometimes it's either the new shiny toy
[5075.24 → 5077.04] or something I read on Hacker News.
[5077.04 → 5079.68] And that's where my focus gets deviated into.
[5079.98 → 5083.84] And I think monitoring is one of those perfect examples because it's something that everybody
[5083.84 → 5086.90] wants to work exactly the way they think they want it to.
[5087.02 → 5090.92] When if they take it to step back, they don't actually need maybe some of that customization
[5090.92 → 5091.76] they're going to do.
[5091.90 → 5093.86] And it took them a large amount of time.
[5094.12 → 5096.88] And in the end, they didn't deliver any extra customer value.
[5097.26 → 5102.04] If they took that effort instead, would be building on their product, they'd be more successful.
[5102.04 → 5105.54] And I think that's a lot of what we're trying to do at True Sight Pulse, which is to kind
[5105.54 → 5106.58] of give you that level up.
[5106.72 → 5108.04] So you have that already.
[5108.34 → 5109.76] You have the infrastructure monitoring.
[5109.92 → 5110.70] You have the plugins.
[5110.84 → 5111.58] You have the alerting.
[5111.78 → 5114.78] You have that whole workflow so you can focus on your customers.
[5115.20 → 5116.08] It's fun to tinker.
[5116.24 → 5117.72] And we support that fully.
[5117.84 → 5119.72] All of our plugins are open source.
[5119.86 → 5120.32] They're on GitHub.
[5120.74 → 5124.06] So you can create new ones, or you can extend those.
[5124.32 → 5125.88] We have actions that we can do.
[5125.94 → 5127.82] We can pull in more things for hooks and triggers.
[5127.82 → 5130.62] But the core value is your product.
[5130.76 → 5132.50] And it's how you deliver that to your customers.
[5132.60 → 5134.08] And that's what we want to help you focus on.
[5134.20 → 5136.02] So we can take some of that load away from you.
[5136.24 → 5138.58] We think you can do better from a product point of view.
[5138.64 → 5139.76] And you can deliver more value.
[5140.06 → 5143.46] That was Mike Baron, Senior Architect at True Sight Pulse.
[5143.72 → 5148.58] To learn more about True Sight Pulse and how it helps you deliver more value to your customers,
[5149.14 → 5153.22] head to bmc.com slash True Sight Pulse, all one word,
[5153.60 → 5155.72] and tell them Adam from the changelog sent you.
[5157.82 → 5159.68] All right, we're back.
[5159.74 → 5162.74] We're ready to close up this conversation all about Haskell,
[5163.14 → 5166.00] learning Haskell, teaching other people Haskell.
[5166.42 → 5169.20] And we focused on the book that you two are co-authoring.
[5169.72 → 5174.02] You told us kind of your process of tag teaming the authorship.
[5174.40 → 5176.72] Still sounds like you have a singular voice coming through,
[5176.86 → 5184.72] but the perspective of both a professional with the beginners helping guide the content.
[5184.72 → 5189.26] Can you tell us more about the book, kind of where it stands in its completion?
[5189.82 → 5194.16] The new thing these days is to have books out there that people read and participate in,
[5194.20 → 5195.40] but they're not finished yet.
[5196.94 → 5198.52] Where is your guys' book at?
[5198.70 → 5200.92] And give us just more information about it.
[5200.92 → 5205.50] So a common misconception about the book is that it's only a beginner's book.
[5206.30 → 5210.32] That's one of the reasons it's over a thousand pages right now is that we actually,
[5210.74 → 5215.18] our goals were based on a functional objective, non-specific topics we wanted to cover.
[5215.64 → 5221.18] And basically the goal was taught them enough Haskell that they can either know or learn on their own
[5221.18 → 5225.12] everything they would want to know in order to use Haskell for pretty typical projects,
[5225.12 → 5227.24] like a web API or something.
[5228.76 → 5233.94] Right now the book, 90% of the content that we're going to write is already out for release.
[5234.06 → 5235.74] That's 29 out of 32 chapters.
[5236.38 → 5239.72] We have the final three chapters about half done,
[5240.20 → 5244.52] and we expect to be content complete by the beginning of April.
[5245.16 → 5249.38] And in April, we are going to do our final editing pass.
[5249.38 → 5254.04] And we hope to have, you know, what software we call a release candidate by the beginning of May.
[5254.34 → 5255.30] Pretty close then.
[5255.48 → 5256.76] You're, uh...
[5256.76 → 5257.12] Yes.
[5257.64 → 5260.86] I mean, based on the site, it says you're 90% through the book,
[5261.06 → 5263.50] 50% through the last 10% remaining.
[5264.16 → 5264.40] Yep.
[5264.58 → 5264.76] Yep.
[5265.70 → 5271.18] Something else that is kind of interesting that I took note of was the code to learn to code.
[5271.50 → 5276.60] And we mentioned in the breaks, which is sad because our listeners don't get to hear the breaks.
[5276.60 → 5282.30] Because Jared and I are actually laughing behind the scenes that we might actually release a show called Just Breaks
[5282.30 → 5284.84] and just put the breaks content in the break show.
[5285.02 → 5288.44] But we'll see about that one because sometimes it's off-air stuff.
[5288.62 → 5293.68] But nonetheless, the length of the book is also attributed to the code examples.
[5293.94 → 5297.58] And it's loaded, as you say, each chapter is loaded with examples and exercises
[5297.58 → 5300.54] so that it can follow along with what you just said there, Chris,
[5300.54 → 5303.32] which is learning Haskell to a point where you can actually use it.
[5303.32 → 5311.26] Can you talk a bit about this idea of and why it's so important for both of you to code to learn, to learn to code?
[5312.62 → 5319.58] So one of the things we do that we think sets the book apart is we try not to make assertions
[5319.58 → 5325.14] that aren't somehow provably or observably true.
[5325.14 → 5333.60] Basically, if you make an assertion about how the language works, well, I mean, if you can't actually demonstrate it,
[5333.66 → 5336.42] then how would it ever make a difference in how their code works, right?
[5337.12 → 5338.06] Seems to make sense.
[5338.56 → 5346.04] Well, the thing is, is that basically means you're writing a lot of examples each and every time you describe some facet or feature of the language.
[5346.04 → 5352.90] And that's where really where most of the book's length comes from is the fact that we, you know, we make an assertion.
[5353.12 → 5355.86] And then Julie, you know, says, hey, you said this.
[5356.26 → 5358.40] Show me, you know, it's Missouri all the way through.
[5359.12 → 5361.36] And that's where most of the length comes from.
[5361.74 → 5364.44] Our readers have actually told us it's an it's a pretty breezy read.
[5364.80 → 5366.90] Some of the blasted through the book pretty quickly.
[5366.90 → 5371.88] So it's not really super prose heavy, and it's not it doesn't feel dense.
[5371.88 → 5374.00] It's just code takes up a lot of room in a book.
[5374.26 → 5375.16] That's just how it is.
[5375.20 → 5376.44] Nothing we can do about that.
[5377.00 → 5380.04] But we think it really, really benefits from that.
[5380.28 → 5381.18] Yeah, it needs to be there.
[5381.62 → 5388.88] And then the code to learn thing is just that we try to get them working through the book and the exercise and examples
[5388.88 → 5394.28] in a way that translates fairly naturally natively to how they would actually work in Haskell.
[5394.28 → 5400.30] So to that end, we teach and show them how to use, you know, the ACI redevelop print loop.
[5400.94 → 5406.98] If you're using Python, like the equivalent would be like IPython or IRB if you're a Ruby user, that kind of thing.
[5407.06 → 5407.28] Right.
[5407.54 → 5415.44] And then learning how to kind of interact and talk to your code and types through the book gets you the practice you need to be able to figure out things when you're on your own.
[5415.84 → 5419.26] So I've made a note here that we've gone this entire show without mentioning.
[5419.84 → 5422.62] I'm not sure if we actually said the name of the book or the URL.
[5422.62 → 5427.46] So as part of saving into our closing questions, let's talk about the URL.
[5427.74 → 5429.60] It's Haskellbook.com.
[5430.00 → 5431.88] And is it called Haskell Programming?
[5431.92 → 5433.08] Is that the official name of the book?
[5433.62 → 5437.76] Yeah, it's Haskell Programming from First Principles or Haskell Programming.
[5437.82 → 5441.00] But a lot of people just call it Haskell Book because that's the name of the URL.
[5441.44 → 5442.82] So I just wasn't sure on that.
[5442.82 → 5446.74] So I guess at this point we can probably tell in some closing questions.
[5446.74 → 5456.64] Definitely, you know, loved learning all about the process of this book and even the perspective you two add to it.
[5457.14 → 5466.12] The one way we like to close this show out is by asking some questions more or less around heroes and also things that are on your radar.
[5466.12 → 5469.22] So do you have a programming hero?
[5470.34 → 5472.44] Yeah, we were talking about this before the show.
[5472.54 → 5481.90] I would go with I'm going to go with Simon Peyton Jones because not only is he obviously really important in that in the history of Haskell and the development of Haskell.
[5481.90 → 5495.38] But he also just every time you see a talk from him or people that I know who've met him, they say he's just really super friendly and likes to engage with, you know, conversation with people, even if they disagree with him.
[5495.66 → 5497.10] And I think that's really admirable.
[5497.10 → 5503.60] And I also like he's been involved with getting computer science education into schools for kids.
[5503.72 → 5514.32] And I really like his perspective about how to teach fundamentals of technology to kids instead of just making them consumers of technology, like how to actually make them creators of technology.
[5514.32 → 5516.40] And I really like things he has to say about that.
[5517.32 → 5521.98] Mine would be Grace Hopper because, well, for a few reasons.
[5522.08 → 5523.22] Because she's everybody's.
[5523.22 → 5534.24] Grace Hopper essentially invented the compiler prior to her work on that.
[5534.72 → 5535.90] Nobody even thought that was impossible.
[5536.04 → 5543.96] They thought they had to talk to the machine purely in terms that the machine understood, you know, with, you know, what we would call assembler these days.
[5544.66 → 5549.64] And her colleagues, you know, in the Navy even told her, oh, that's not possible.
[5550.34 → 5551.54] It actually was.
[5551.54 → 5557.38] So, you know, in a sort of proof by construction method, she made a working compiler.
[5557.76 → 5561.52] And then the language that she wrote eventually became COBOL.
[5561.74 → 5564.44] And one of my pet peeves is people attributing COBOL to her.
[5564.60 → 5564.90] No, no, no.
[5564.94 → 5566.88] That was the committee that picked up her work afterward.
[5567.06 → 5567.80] That wasn't her fault.
[5568.54 → 5570.96] So, but yeah, she invented the compiler.
[5571.44 → 5574.76] Much like Simon Payton Jones, she was a very, very charming personality.
[5574.76 → 5580.64] There's some hilarious and awesome interviews that you can find on YouTube with her.
[5581.02 → 5587.88] And I just, I don't think you could really hope for much more out of a pioneering contributor to CS.
[5588.30 → 5597.96] I mean, she did really great, important work that got us started on the right track in terms of, you know, designing and building paralanguages instead of just, you know, not abstracting with machine.
[5597.96 → 5601.76] And she happened to be what seems to be a really lovely person, too.
[5602.62 → 5602.94] Very good.
[5603.08 → 5609.82] So second question and final question for the day is what is on your open source radar?
[5609.82 → 5615.54] So things that you may or may not have even played with, but has your interest peaked?
[5615.64 → 5620.96] If you had a free weekend, perhaps you'd go get clone this and check it out or read more on it.
[5622.24 → 5623.82] Maybe we start with Julie this time.
[5623.92 → 5624.96] What's on your open source radar?
[5625.82 → 5632.70] Well, I've been trying to make a Twitter bot that does some really basic language analysis.
[5633.38 → 5635.46] And so analyzing people's tweets.
[5635.46 → 5643.44] And so I've been looking at the Chatter library in Haskell's for it's a what?
[5645.46 → 5646.34] Sorry, it's fine.
[5646.44 → 5646.78] Go ahead.
[5646.98 → 5648.12] I was going to talk about Chatter.
[5649.32 → 5649.94] That's why.
[5650.88 → 5652.94] Oh, you mean both of you guys have the same answer?
[5653.14 → 5657.26] He's well, he's helping me write the Twitter bot.
[5657.40 → 5662.04] And so because there's a lot about streaming that I don't know that I need to know for writing the Twitter bot.
[5662.14 → 5663.82] And so he's what?
[5664.28 → 5664.68] It's fine.
[5664.76 → 5665.14] It's fine.
[5665.14 → 5672.64] And so we've both been looking at Chatter and really excited about that project.
[5672.82 → 5673.80] Should we take that from the top?
[5674.70 → 5675.98] I think it's great having that.
[5676.40 → 5679.34] I mean, unless it's a true fight, then I think it's cool.
[5679.84 → 5682.78] No, it's just I make facial expressions, and it throws her off.
[5683.08 → 5687.12] And I'm just like rubbing my forehead because it's like now I'm just going to talk about something really silly.
[5687.38 → 5688.06] I love it.
[5688.12 → 5688.52] Keep it.
[5688.74 → 5689.72] It's good stuff.
[5690.02 → 5691.18] She's on your radar, man.
[5692.96 → 5694.84] You guys just happen to have the same radar.
[5694.84 → 5695.50] It makes sense.
[5695.58 → 5697.00] You guys are working on the same Twitter bot.
[5697.40 → 5697.58] Right.
[5697.68 → 5704.40] Well, that's why he got I mean, that all goes back to why he brought me into Haskell in the first place is because we were both interested in natural language processing.
[5704.60 → 5707.84] And so now we're interested in this Haskell natural language processing library.
[5708.60 → 5709.26] I mean, it makes sense.
[5709.34 → 5709.94] Makes sense.
[5710.46 → 5711.18] Makes sense.
[5711.18 → 5712.00] And specifically.
[5712.00 → 5712.04] And specifically.
[5712.38 → 5716.68] So the chatter library is on Hackage, and it's by Rogan Query.
[5717.40 → 5719.36] And it's pretty cool.
[5719.50 → 5726.08] It seems to be the kindest of complete parts of speech analysis library for Haskell.
[5726.24 → 5727.92] It has some pretty good stuff in it.
[5727.92 → 5730.12] And I have an interest in parsers, too.
[5730.24 → 5735.84] So one thing I thought I might do is use a different kind of back end parser for it.
[5737.24 → 5738.78] Another project I'm interested in.
[5738.92 → 5740.48] I may get the name wrong here.
[5740.52 → 5741.26] And if so, I apologize.
[5741.26 → 5748.48] But there was a recent plotting library for Haskell that was posted to the Haskell Subreddit recently called Quick Plot, I think.
[5749.20 → 5757.84] And it really appealed to me because it kind of had the kind of the immediate satisfaction of using like ggplot2 and R, that kind of thing.
[5758.60 → 5769.50] And that would be something I'd like to hack on is got a chance to extend it maybe to using Cairo like R does instead of like a web app thing.
[5770.36 → 5771.12] Well, cool.
[5771.50 → 5774.56] That is the tail end of the show here.
[5774.64 → 5778.00] It's been a fun time to take this journey with you.
[5778.08 → 5783.52] I feel like Jared and I in some ways have joined your effort to a degree with just talking through all this with you.
[5783.68 → 5786.96] It's certainly interesting to hear your dynamic between one another.
[5787.98 → 5794.28] And then also just to kind of see this veil be pulled back to see how it is to learn Haskell,
[5794.36 → 5800.92] but also just to take a beginner's approach to learning programming, period, to see the pros and cons.
[5800.92 → 5804.92] And all the ins and outs and the hurdles that can come up as part of that.
[5804.92 → 5808.02] But is there anything you guys want to mention as we close out the show?
[5808.08 → 5810.44] Is there anything else you want to quickly mention?
[5811.34 → 5818.60] Well, we are going to be at LambdaConf this year, which is in May, towards the end of May.
[5818.72 → 5819.90] And it's in Boulder, Colorado.
[5819.90 → 5823.44] We're actually going to be gold sponsors for it this year.
[5823.64 → 5823.90] Nice.
[5823.90 → 5830.98] And we actually kind of launched the book for last year's LambdaConf, so it's kind of nice to have that continuity.
[5831.66 → 5832.00] Yeah.
[5832.32 → 5844.32] And we're also sponsoring the child care at LambdaConf because, you know, I mean, Julie's a mother of two, homeschooling mother of two.
[5844.32 → 5851.60] And we feel pretty strongly about, you know, primary carers of children being able to participate and be part of an open source community as well.
[5851.70 → 5852.78] Yes. And can I say something exciting?
[5853.18 → 5853.46] Yes.
[5853.46 → 5864.36] So I had asked the LambdaConf organizers if they had ever thought about having children's workshops with the conference since the kids are already there in child care.
[5864.86 → 5868.26] And they agreed to do it.
[5868.34 → 5877.84] So I am coordinating some children's workshops that will be about we're going to have a workshop for kids learning how to do sorting algorithms and some other exciting things.
[5877.84 → 5879.74] So I'm really, really excited about it.
[5879.74 → 5893.08] In addition, for two days prior to LambdaConf, we're going to be offering commercial Haskell training because it's something that a lot of people have asked for some one-on-one time with us.
[5893.68 → 5897.38] It's beginner and intermediate commercial Haskell training for two days.
[5898.18 → 5904.68] And there's also if you're only paying for yourself, if you don't have an employer covering it, we actually have a self-pay discount for that as well.
[5904.68 → 5912.62] What's the best way to get in touch if someone out there is like, hey, I wouldn't mind helping out with the child care part of that?
[5913.82 → 5914.30] Is that Julie?
[5914.70 → 5915.52] How do they get in touch?
[5916.96 → 5920.06] If they want to help, you mean support it?
[5920.22 → 5920.76] Support it.
[5920.84 → 5924.80] Like if they have questions, and you're organizing, how can people get in touch if they have some questions?
[5924.80 → 5932.82] Like how they participate, you know, if they want to influence it, they have, if they're going to be coming to the, to the conference, and they want to have their child go into that.
[5933.02 → 5936.32] What's the process of like interacting with you around what it is?
[5936.92 → 5937.28] Right.
[5937.44 → 5942.22] The best way is probably to initially send questions through the LambdaConf website.
[5942.22 → 5948.54] And then if, if there are specific things that, that need to get to me, then the organizers will send it to me.
[5948.68 → 5953.92] You can, I mean, anybody's free to reach me on, I need to have a public email address, don't I?
[5954.18 → 5954.38] Yeah.
[5954.96 → 5956.26] Anybody's free to reach me on Twitter.
[5956.46 → 5964.42] But if you're not on Twitter, then, then Lambda, through the LambdaConf is probably currently the best way to reach me.
[5964.42 → 5971.80] Um, and then Courtney, that goes, who's one of the organizers will follow any questions that need to come to me, to me.
[5972.30 → 5972.92] Good deal.
[5973.64 → 5980.88] Well, I just want to make sure we give people a way to get in touch or at least mention something that, uh, that makes some sense as a lead.
[5980.88 → 5983.88] So we have people out there listening like, Hey, I, you know, I've got some questions.
[5984.04 → 5984.80] You want to get in touch?
[5985.16 → 5985.56] Yeah.
[5985.64 → 5990.02] Put both of your GitHub profiles and Twitter profiles in the show notes.
[5990.20 → 5990.88] This is episode 198.
[5990.88 → 5994.26] So for listeners listening to this, this is episode 198.
[5994.44 → 5999.70] So go to changelog.com slash 198 or open up or look back at your phone.
[5999.76 → 6004.36] If you're listening to this on your phone in a podcast app or something like that, go to the show notes.
[6004.46 → 6006.10] We put all that stuff in there.
[6006.52 → 6009.96] Heroes, all the links we talked about in this show will be there again.
[6010.02 → 6010.94] Episode 198.
[6011.62 → 6014.80] But, uh, Julie, Chris, it's been an absolute pleasure having you on the show today.
[6015.16 → 6017.24] Uh, getting to learn all this stuff we have with you.
[6017.36 → 6019.66] So, uh, everyone else listening, stay tuned.
[6019.66 → 6021.92] We have a ton of great shows coming up on the schedule.
[6022.36 → 6024.74] Uh, some, some upcoming shows.
[6024.84 → 6028.72] We've mentioned this one a couple of times, 20 years of Ruby with Matt's.
[6028.80 → 6030.36] We do have that scheduled.
[6030.52 → 6032.82] It's a little further out than I thought we would have had.
[6033.02 → 6036.88] So we're really hoping it can be episode 200, but I don't think it's going to be.
[6036.88 → 6044.46] Uh, we also have a show scheduled with Andrew Continuo on Hugging and also Raquel Vélez talking
[6044.46 → 6046.76] about NPM, JavaScript, and a bunch of fun stuff.
[6046.82 → 6048.66] So those are some of our upcoming shows.
[6048.74 → 6051.90] We also have a further out scheduled show with Jewel Bots.
[6052.44 → 6053.04] Uh, that's Sarah J.
[6053.10 → 6054.34] Chips and George Stocker.
[6054.60 → 6055.86] Great show there coming up.
[6055.90 → 6061.06] Talking about, yet again, kids in programming and influencing girls into programming.
[6061.06 → 6064.92] So, and also women into programming with girls, because they do grow up, of course.
[6065.38 → 6067.02] Uh, but that has been the show.
[6067.12 → 6068.44] So everybody let's say goodbye.
[6069.08 → 6070.16] Thanks for having us.
[6070.28 → 6071.28] Thank you for having us.
[6071.36 → 6071.62] Bye.
[6071.72 → 6072.26] Thanks for coming.
[6072.26 → 6073.80] benzene for keeping up the show.
[6073.84 → 6074.26] Bye.
[6074.34 → 6074.86] Bye.
[6074.92 → 6075.46] Bye.
[6075.46 → 6075.96] Bye.
[6084.46 → 6085.38] Bye.
[6090.74 → 6094.70] Bye.
[6099.38 → 6101.30] Bye.
[6101.30 → 6101.80] Bye.
[6102.26 → 6132.24] Thank you.
