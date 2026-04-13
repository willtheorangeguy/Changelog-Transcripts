[0.00 → 21.26] Welcome to the Change Log, episode 0.1.1. I am Adam Stachowiak.
[21.72 → 24.02] And I am Wynne Netherlands. We've got a great show today.
[24.02 → 32.14] I interviewed John Bookmaker of RailsTip.org fame and Monographer fame, soon-to-be Harmony fame.
[32.54 → 33.38] Yeah, a lot of fame.
[33.74 → 37.16] A lot of fame. And you got a chance to see Harmony for the first time. Impressed?
[37.48 → 40.14] Yeah, I was really impressed with what you could do with that.
[40.38 → 43.52] A lot of the details he shares in this podcast is pretty good about Harmony, I guess.
[43.98 → 48.82] One thing to also mention is that while Harmony isn't open source, it's because of open source is even possible.
[48.82 → 54.88] So, you know, hat tip to John and Order List and Steve on being able to pull that off for sure.
[55.68 → 60.32] And John is I am me as we speak saying he keeps refreshing the Change Log. He's dying to see the episode.
[60.68 → 62.58] So we'll have to get this one out there.
[62.68 → 68.04] You know, John's work stands on its own merit as far as his contributions to open source.
[68.14 → 73.16] But, you know, anytime that we've got guys on that are talking about their fresh and new open source projects,
[73.38 → 77.32] you know if they want to plug what they're doing to pay the bills and keep the lights on, we're all for it.
[77.32 → 78.56] Yeah, absolutely, of course.
[78.82 → 81.72] And I guess, did we hear back from Sea of Clouds?
[81.82 → 85.12] We have not heard back from Sea of Clouds on the Fix Me contest.
[85.42 → 89.30] I hear he's got a winner. He's got a winner, but just no details to share yet, right?
[89.42 → 95.62] He's trying to keep it in spence. I guess he doesn't want to follow Defunct or Jay Wanamaker on the Change Log.
[95.68 → 100.10] He probably wants to wait for a way of a slow news day so he can fill that vacuum.
[100.48 → 101.32] Gotcha, gotcha.
[101.84 → 104.68] I guess some things to mention, too, that we released last week.
[104.72 → 108.12] If you didn't hear, head to tail.thechangelog.com.
[108.18 → 112.42] It's something very cool we put out there where you can actually watch open source and GitHub in real time.
[112.92 → 116.06] Yeah, and kind of tune in to the events and GitHub that you want to see.
[116.06 → 122.60] You can click the gears down in the bottom left and filter out all those events that you don't want to see, namely the push.
[122.64 → 128.06] If you remove the push events, it takes the feed down substantially, and it's a little easier to follow.
[128.70 → 133.04] And also, filter just by those languages that you care about.
[133.22 → 138.44] If you're a Python guy, just unselect everything but Python and just watch the open source flow.
[138.44 → 141.16] And we're also on GitHub now, too, right?
[141.70 → 143.30] GitHub.com slash explore.
[143.86 → 152.36] And that still amazes me that just after 10 episodes, we found ourselves there at the epicentre of open source, which I think GitHub is.
[152.44 → 155.18] We're really tickled and honoured to be there.
[155.58 → 156.82] Yeah, it was our first point release.
[156.98 → 164.30] And I think what's cool about that page, too, is maybe they don't even know this, maybe we shouldn't mention it, but 66% of that page is changelog content.
[165.04 → 165.62] That's awesome.
[165.62 → 176.46] You know, and I don't know if you looked at the stats, last episode with Chris is now our second most listened to all time and about to be number one just after a few days out.
[176.72 → 180.64] So kudos to Chris for bringing the followers.
[180.78 → 181.46] We appreciate it.
[181.64 → 182.12] Yeah, absolutely.
[182.90 → 184.10] Anything else you want to mention, WIM?
[184.44 → 194.22] Yeah, I should reiterate, if you want to follow Adam or me, you can follow us on GitHub or Twitter at Adam Stack or Penguin, P-E-N-G-W-Y-N-N.
[194.22 → 199.98] If you want to keep up with the show directly, go to twitter.com forward slash changelog show.
[200.56 → 200.88] Absolutely.
[201.42 → 203.06] All right, then I guess we should get on with the episode then.
[203.44 → 204.12] Let's get to it.
[204.26 → 204.50] All right.
[204.50 → 219.90] All righty, we're joined today by John Bookmaker, Rubbish and purveyor of railstips.org.
[220.16 → 220.84] Welcome, John.
[221.44 → 221.76] Hi.
[222.18 → 224.92] Why don't you tell everybody who you are and kind of what you do?
[225.88 → 226.86] I'm John Bookmaker.
[226.86 → 228.90] I work at orderedlist.com.
[229.06 → 232.38] It's a web consultancy, I guess, for lack of a better word.
[232.76 → 237.14] And basically, we do websites and web applications and stuff like that.
[237.90 → 239.58] And I like to blog.
[240.02 → 242.00] Blog at a lot of places, rails tips the most.
[242.24 → 245.46] And I love being inspired and doing open source work.
[246.36 → 248.68] I think you're probably best known for rails tips.
[248.74 → 249.90] How did that site come about?
[249.90 → 253.38] Um, actually, it's kind of a funny story.
[253.52 → 259.14] I randomly met this one other person that did Ruby in South Bend, near where I live.
[259.84 → 262.72] And they were like, yeah, there's this site called Rails tips.
[262.80 → 263.88] And this guy's giving it up.
[264.00 → 265.54] Like, he doesn't want to manage it anymore.
[266.22 → 268.00] And he was like, I think you should do it.
[268.20 → 270.76] And I was like, I don't know.
[270.90 → 274.14] And then I just hit the guy up and started blogging there.
[274.22 → 276.20] And then slowly kind of found my rhythm.
[276.48 → 278.16] And I mean, that's pretty much it.
[278.16 → 280.82] But yeah, I didn't even, I didn't register a domain originally or anything.
[280.82 → 282.00] I just kind of took it over.
[282.08 → 285.78] The guy literally just pointed it at my site and gave me a dump of the content.
[285.92 → 286.62] And I was good to go.
[287.00 → 291.74] So, John, I didn't realize that you didn't start Rails Tips, which is quite amazing,
[291.84 → 296.02] considering the success you've had, especially recently, that by your own admission, you have no talent.
[297.78 → 299.82] Yeah, I didn't start it at all.
[300.24 → 304.22] There's actually, you can still, even now, go back, like on the Smorgasbord page.
[304.22 → 311.18] And there's probably 20 or 30 of the first posts that, they say they're written by me just because I was too lazy to import.
[312.06 → 314.44] The previous guy, I believe it was Bill Turner, I think was his name.
[315.06 → 317.12] And I think he's on Twitter and everything still.
[317.28 → 319.12] And I think he's doing Ruby still.
[319.42 → 321.86] But yeah, he was doing it, and he just got tired of doing it.
[321.88 → 323.02] He was doing it more like a news site.
[323.76 → 325.92] And so I started it kind of as a news site.
[326.08 → 329.52] And then I realized, like, lots of people do news, so I should probably do something different and unique.
[329.52 → 331.76] So I just started writing my own stuff as I learned it.
[332.14 → 336.54] For those guys that don't know, I'm not calling John Talentless.
[336.66 → 339.04] He's said this by a mission on a recent blog post.
[339.16 → 341.94] So why don't you talk about that post because I understand it was quite popular.
[342.56 → 344.90] Yeah, it struck a chord, evidently.
[345.00 → 345.26] I don't know.
[345.72 → 353.60] It was actually one of the few posts that I wrote probably in a flurry of, like, not even anger or anything.
[353.60 → 361.74] Just, like, I had a couple of people lately, I see a lot of Subsists that say, or even just a lot of people that are starting out.
[361.78 → 368.30] And they're like, oh, I wish I could be like you or not me in particular, but, like, I wish I could be like X person.
[368.38 → 369.04] That's really awesome.
[369.80 → 373.60] And it was just always like, you know, I wish I could be great.
[373.64 → 374.30] I wish I could be great.
[374.38 → 375.68] And I finally just got fed up.
[375.74 → 376.44] I'm like, you can be.
[376.68 → 380.02] Like, if you want to be perfect, you just have to practice a lot.
[380.02 → 386.36] That's, you know, if you have a general competence level, then all you need is hard work, you know.
[386.40 → 391.44] And if you put in the time, and you work hard, and you enjoy it, like, A, it's not going to feel like work.
[391.62 → 392.84] And, B, you're going to get better.
[392.96 → 395.76] And eventually you're going to get to a point where, you know, you feel a lot better.
[396.18 → 400.52] And so I guess I was just trying to remind people, like, you can be as good as you want to be.
[400.58 → 401.94] You just have to work for it.
[402.40 → 407.12] And if you're not where you want to be, it's probably just because you're not working hard enough, or you haven't had enough time.
[407.18 → 407.56] That's it.
[407.56 → 415.68] You know, it's not like some people are just blessed from the coding gods to be able to, you know, break out threads or something.
[415.76 → 416.16] I don't know.
[416.88 → 426.00] So, I mean, for me, it was just like I just kind of got tired of hearing it from various people kind of more in the beginning stages that they wish they could be perfect.
[426.12 → 427.94] And I just wanted to remind everyone you can be.
[428.10 → 431.30] You know, I was horrible like a year ago, maybe two years ago.
[431.38 → 433.64] I mean, not that I'm even great now.
[433.70 → 435.26] I'm just, you know, I keep getting better.
[435.26 → 441.28] But, I mean, you just have to compare yourself against where you were and not against, like, the people that have been doing this for a long time.
[441.94 → 448.46] I like how you mentioned that because you mentioned in that post about your GitHub profile and how the stuff will code that from your past that you don't want to delete.
[448.56 → 450.14] It kind of reminds you of where you were.
[450.98 → 453.12] And I look back at that as like, you know, this is where I came from.
[453.16 → 455.28] So it's always helpful to push you forward.
[456.16 → 456.48] Exactly.
[456.68 → 457.22] Yeah, it is.
[457.22 → 459.26] It's extremely helpful.
[459.46 → 461.96] I mean, I like occasionally going back to projects.
[462.28 → 464.08] And I'm just like, why did I do that?
[464.22 → 466.06] Like, not even the code.
[466.14 → 467.76] Just why did I even start this project, you know?
[467.78 → 469.20] It's just like, that's so weird.
[469.28 → 470.66] But, you know, you learn with every one of them.
[471.48 → 479.06] You know, the flip side of that is when you turn out a lot of open source like you do, you know, you tend to collapse into the weight of your own work.
[479.06 → 482.00] And you're having to find folks to take over certain projects.
[482.12 → 486.82] I know I've been thrilled to be able to help you out maintaining the Twitter gem.
[486.88 → 494.80] And you're probably best known for the Twitter gem among other things like HTTP Party and Crack and some other projects you've turned out.
[494.92 → 499.02] But one that I'd like to highlight that perhaps folks don't know about is Monographer.
[499.22 → 504.06] You want to talk a little bit about how you came to Congo and why you fell in love with it?
[504.06 → 511.84] Yeah, so this is going to be a hat tip for Wynn because – or maybe even a hat tip for Jerry Richardson, a guy that I am in a Ruby group with.
[513.06 → 515.76] He was – you know, we were at Hailstone.
[516.04 → 517.20] Was that in Vegas?
[517.38 → 518.38] I think it was in Vegas.
[518.70 → 523.24] And I came down for breakfast one morning, you know, tired and barely awake.
[523.34 → 525.80] And I saw Jerry at the table, and I was like, I'll just go to Jerry.
[525.90 → 528.02] Like, I'm not even ready to talk to anyone, you know.
[529.22 → 534.02] And went to Jerry and then you guys happened to be there, and he introduced, you know, he said,
[534.10 → 536.30] oh, yeah, these guys do a lot of Twitter and stuff.
[536.58 → 542.74] And then you and Jim and I think there was maybe another person there and you guys were like, oh, yeah, we use the Twitter gem.
[542.82 → 544.56] We love it, and we use it with this database called Congo.
[544.72 → 545.96] And I was like, crazy.
[547.24 → 553.52] And then I went – you know, after that I remembered it and I – so I went back and checked it out when I got home.
[553.52 → 558.54] And I literally spent like a week reading the entire website that they have, which is really great.
[559.42 → 561.74] And Congo is just a – it's a phenomenal database.
[561.74 → 569.42] And the first thing that I got frustrated with when I tried to use it is there was nothing Active Record like – I mean, Active Record is great.
[569.66 → 571.38] It really takes a lot of pain away.
[571.66 → 575.48] And there was nothing like that for Congo that I was satisfied with.
[575.48 → 581.58] And so I just started playing around, and I was like, yeah, I can make an ORM or a mapper.
[582.20 → 587.26] And I started kind of hacking away and I, you know, got a few things done and thought it was like awesome.
[587.92 → 591.36] And looking back now, I realize how naive and small it was.
[591.52 → 596.60] But, you know, I just started making something that I could use and just mostly for intellectual purposes.
[596.60 → 598.04] I just thought it was kind of fun.
[598.04 → 602.58] And, you know, Congo was different and, you know, interesting and there wasn't really anything out there.
[602.72 → 607.20] And I've always been kind of curious about how the guts of Active Record and things like that work.
[607.60 → 616.16] And so I just started kind of hacking on it and did a lot of code reading on Data Mapper and SQL and Active Record and all those Ruby projects that map relational databases.
[616.16 → 619.26] And kind of just started going to town on Congo Mapper.
[619.56 → 625.64] And now it's getting to a point where, I mean, we use it on some projects and stuff, both for clients and for ourselves.
[625.96 → 627.22] And it's getting pretty cool.
[627.36 → 630.96] I mean, it still has a long ways to go, but it's getting better every day.
[631.54 → 634.66] How has Congo changed your approach to web development, especially with Rails?
[635.90 → 636.74] That's a good question.
[637.46 → 645.44] It's changed, I would say, it hasn't necessarily changed my approach.
[645.44 → 656.10] It's changed from the outside, but from the inside it's changed a lot because every – so the reason we even need mappers is that we don't have a way to store our objects.
[656.38 → 662.22] So anytime you do anything with the web, you have, you know, data, and you have to have some way to store that data.
[662.36 → 665.60] And you can't just store Ruby objects and then pull them back out.
[665.70 → 666.50] You can't do that.
[666.56 → 669.36] So you have to store them somewhere, so a database makes sense.
[669.36 → 674.32] And there are tons of, you know, good relational databases, so that's where you store it.
[675.44 → 693.58] But the thing that I think has changed the most with using Congo is that it takes, like, another layer away from – another layer of work off that normally you would have to do in order to fit your Ruby objects, your, like, domain model, into the database.
[693.58 → 698.26] So – because databases don't – you know, they're SQL, and they're relational and foreign keys and constraints and all this stuff.
[698.66 → 700.70] But your Ruby code is just objects.
[700.82 → 705.86] So you have to, like, you know, you have to convert them into something that can store in a relational database.
[706.38 → 712.18] So I think the biggest change, you know, is Congo takes away another layer because it has things like array keys.
[712.18 → 716.14] So you can store collections of things in Congo and also hash keys.
[716.30 → 723.04] So you can store, you know, like, associative arrays in PHP or hashes, dictionaries, structs, whatever you want to call it in whatever language.
[723.12 → 725.08] You can store those also in the database.
[725.20 → 734.02] And I think that's the biggest difference that it made for me is, like, things that normally in Rails I might have made, like, a join model for, you know, and do a has many through type thing.
[734.02 → 741.06] Now I can just store, you know, an array of IDs on, you know, the site model or on the user model or something like that.
[741.34 → 743.02] And it takes a lot of complexity out of the code.
[743.10 → 749.26] I don't have to have a whole other database table, a whole other, you know, model set up to do that.
[749.34 → 751.62] I can very simply just kind of make it work.
[752.66 → 763.14] So I think that's the biggest change that it's made for me is it kind of opened up my eyes and, like – and the other thing that I think is huge is, like, Rails has this golden path, you know, that they tell you to follow.
[763.14 → 770.32] And, like, if you don't – so you get used to following that and then all of a sudden, you know, you start with, like, something new that doesn't have a golden path like Congo.
[770.44 → 774.80] There's, like, there's not, like, a thing out there that says this is how you should do things in Congo.
[775.30 → 777.90] So at first you're like, I don't know how to program anymore.
[778.40 → 782.64] And then you start, you know, kind of just figuring out, well, what will work?
[782.80 → 787.62] And so you think through your problems in different ways than you would have if you would have just followed the golden path.
[788.00 → 792.52] So I think the golden path is great to have this, you know, these set conventions and things like that.
[792.52 → 802.18] But you still need to sometimes branch out and try this other, you know, new thing so that you can see if there are conventions that you're missing out on that could be perfect.
[802.38 → 809.30] And I think that's the biggest change that, you know, I think in one of the posts I mentioned, it's like, you know, taking the pill in the matrix or whatever.
[809.50 → 812.28] You kind of have to free your mind and there is no spoon kind of thing.
[812.96 → 817.32] And then once you do that, then there are a lot of opportunities for making things a lot more simple.
[817.32 → 824.48] And I know we switched from MySQL to Congo on a project and I feel like our code is a lot lighter and easier to understand.
[825.60 → 829.86] Maybe, you know, because we weren't as good with MySQL or something like that.
[829.92 → 834.16] But I think it's more just Congo kind of takes away some layers that you don't really need anymore.
[834.78 → 841.62] It's excellent for what I call stashing the hash, you know, calling a third party API and just grabbing a hash of values and just stuffing it.
[841.62 → 850.40] Especially if you don't have to worry too much about CRUD, although Congo Mapper does provide a lot of great validations and familiar approaches when you're dealing with the data.
[850.82 → 855.30] You know, last episode we announced our TAIL application at tail.thechangelog.com.
[855.38 → 866.36] And I should tell everyone that it's running on Congo Mapper, and it's also running on Congo HQ, which is hosted Congo for those that haven't tried to install MongoDB for themselves.
[866.36 → 869.76] Even though it's quite simple, but I understand you're a Congo HQ customer as well?
[869.76 → 877.48] Yeah, I just have a real tiny note app that, and, you know, I mark things to read later, bookmarks and just, I call it textual.
[877.58 → 879.86] I literally just store text stuff in it.
[880.44 → 884.44] It's my kind of like way of keeping track of stuff that I don't want to be social.
[885.14 → 889.94] And so, yeah, I'm using that with Heroku and Congo HQ.
[890.18 → 891.32] So, yeah, it's great.
[891.42 → 893.00] I really have not had any problems.
[893.00 → 898.12] I mean, it's zero traffic because it's just me and my wife storing, you know, grocery recipes and things like that.
[898.12 → 899.90] But it works wonderful.
[900.96 → 906.88] Now, I'm looking at your GitHub page for Congo Mapper, and it's at GitHub.com slash automaker slash Congo Mapper.
[908.00 → 911.62] 661 watchers and 128 forks as the time of this interview.
[911.78 → 918.60] So talk a bit about how GitHub has influenced how you run your open source projects,
[918.60 → 922.56] and especially with Congo Mapper, something that's been forked 128 times.
[922.70 → 924.44] I mean, what does that number really mean for you?
[925.86 → 926.50] Let's be honest.
[926.54 → 927.34] I ignore the forks.
[927.42 → 927.82] No, I'm just kidding.
[928.96 → 935.62] So I think what GitHub has done for me the most, I was one of those people who, like, I jumped on the open source bandwagon, like, right away,
[935.72 → 937.26] as soon as I, before I even should have.
[937.44 → 938.62] Because I was like, this is so cool.
[938.70 → 941.46] I mean, I can share code and things like that with other people.
[941.46 → 950.46] And so I had, like, an SVN, you know, repo on DreamHost where I first started, like, sharing my Rails plugins that were horrible and no one used.
[951.06 → 954.60] And it's probably still running somewhere just so I can embarrass myself sometimes.
[955.06 → 961.88] But I think the thing that GitHub has done that's so great, I mean, everybody, most people know GitHub is great.
[962.00 → 965.72] But I think the thing that's awesome is it makes it so easy to share back and forth.
[965.72 → 974.70] So the upside is, like, you know, with the network graph and the 4Q and some of those things, it's really, really simple to have people contribute to your project.
[975.32 → 976.20] So that's the upside.
[976.28 → 981.42] The downside of it is sometimes that you get people who, you know, only want their specific thing.
[982.12 → 987.28] And so they'll, because it's so easy, they'll fork it, add their specific thing, and then kind of expect you to pull it in.
[987.28 → 991.76] And so that's kind of one thing that's been a little bit – I wouldn't say it's a downside.
[992.14 → 1000.38] It's just kind of like you have to be a little more forthright about what you let into your project because they're going to go away eventually, and then you have to maintain that.
[1000.54 → 1003.20] So that's kind of one thing that I've caught.
[1003.32 → 1004.58] But, yeah, I mean, GitHub's great.
[1004.66 → 1006.02] It's so easy to get your project out.
[1006.14 → 1010.08] They do a lot of good work pushing open source, too, I mean, along with you guys.
[1011.30 → 1014.34] So, I mean, it just makes it really easy to share that code, to get it out.
[1014.34 → 1016.66] And the awesome thing is it's free.
[1016.82 → 1021.76] I mean, if you just want to share open source code, like – I mean, I have – I mean, you can see my GitHub page.
[1021.82 → 1023.12] There's a ton of projects on it.
[1023.40 → 1025.90] I don't think I'm even at, like, 5% of the free account.
[1026.14 → 1030.00] I mean, so, I mean, that's just – it's stellar on their part to offer that.
[1031.26 → 1036.96] A lot of forks, most of those forks are, like, people fork the project and then never touch it again.
[1037.46 → 1043.52] So, like, if you go to the network graph, it's a lot smaller because that pretty much only shows the forks that have done something.
[1044.34 → 1049.46] But it's definitely sometimes overwhelming.
[1049.72 → 1057.22] If you get a project that gets to a certain level of popularity, there are a lot of commits out there and stuff like that you kind of have to sift through.
[1057.48 → 1058.86] And the 4Q helps with that a lot.
[1059.26 → 1062.72] But, yeah, so, I mean, GitHub's great.
[1062.82 → 1065.96] I mean, it's totally changed the way I do pretty much everything open source-wise.
[1065.96 → 1072.44] It just makes it so much easier to share and to kind of get a community wrapped around real quick and get people working on stuff.
[1073.12 → 1075.62] So, you mentioned that you're using Monographer for some internal projects.
[1075.78 → 1076.78] I think I know what those are.
[1077.20 → 1086.48] Do you want to talk about Harmony App, this app that's greatly anticipated in the CMS space and what problem you guys are aiming to solve and where it's at?
[1086.48 → 1088.14] Yeah, I would love to.
[1088.34 → 1093.10] So, Harmony App, if you haven't heard of it, it's HarmonyApp.com.
[1093.86 → 1096.04] And Harmony, just like it sounds, and then APP.
[1097.46 → 1102.56] And basically, so Steve and I both worked at the University of Notre Dame for several years.
[1102.56 → 1106.94] And while we were there, we built a content management system that we called Conductor.
[1107.10 → 1110.56] So, it was, you know, Rails, Conductor, obviously that same line.
[1111.38 → 1112.40] And it worked really cool.
[1112.70 → 1120.76] It was kind of like, you know, a little bit of a mutation of Mephisto, I mean, written from scratch.
[1121.08 → 1122.70] And it was multi-site.
[1122.84 → 1128.30] It allowed us to, you know, add a site in quick and just really shortened our development time.
[1128.30 → 1136.00] And so, and then we both left Notre Dame, and so then we were like, oh, crap, it would be really nice to have Conductor again.
[1136.16 → 1140.28] But Conductor was owned by Notre Dame, so we can't just, you know, take that code and use it.
[1140.42 → 1143.30] And we kind of thought we would probably do a few things differently.
[1143.90 → 1156.24] And so, what Harmony is, is it's basically, we haven't found a content management or, you know, more specifically, something just for managing websites out there that we've really been satisfied with.
[1156.24 → 1159.02] And so, Harmony is like, is that.
[1159.16 → 1162.06] It's what we want from a content management system.
[1163.14 → 1172.32] And basically, what that is, is something that a developer can go in and like customize everything and make everything, not like Expression Engine customize everything.
[1172.54 → 1180.88] It's more, you know, more like, you know, you can define what fields content people will see and stuff like that in just a real simple fashion.
[1181.70 → 1184.60] And you can put your own markup and things like that around it.
[1184.60 → 1187.40] But the main goal is to separate.
[1187.62 → 1193.14] So, we're both, we were both kind of front-end developers that kind of migrated to back-end and then stuff like that.
[1193.48 → 1199.28] And the main thing that in front-end development is you separate the markup from the presentation.
[1199.28 → 1201.34] So, how it looks from what it is.
[1201.68 → 1206.22] And what we are trying to do in Harmony is separate the data you store from how it gets marked up.
[1206.34 → 1208.52] So, it's kind of like another layer on top of that.
[1208.52 → 1214.32] So, we say, you figure out how you want to store your data, and you store it that way.
[1214.72 → 1216.48] And using Congo, it's really easy.
[1217.06 → 1220.90] And then from there, you, you know, you say, what is this markup?
[1221.02 → 1221.90] You know, what is this data?
[1222.04 → 1225.96] So, you mark it up with your HTML templates and things like that for the web.
[1225.96 → 1233.14] And then you add your presentation files, so your theme files, which are like style sheets and JavaScript's and things like that, that give it a certain look and feel.
[1233.28 → 1238.76] And so, it's just kind of like another abstraction on separating your markup and your presentation and separating your data from your markup.
[1239.06 → 1243.54] And what it makes for is, you know, content entry, you know, you don't have to know HTML for.
[1243.70 → 1248.66] I mean, you have to know how to put in like a text field, or you have to know how to put in, you know, a description or things like that.
[1248.66 → 1254.12] But you don't really have to know a lot of HTML like this DIV makes this go over here or those kinds of things.
[1254.24 → 1258.04] It's not – what we found is the most content management systems are a title and a big description box.
[1258.28 → 1260.52] And that is just not how websites work.
[1261.34 → 1270.18] Websites are lots of tiny pieces of – you know, each page is lots of tiny pieces of data that just gets, you know, melded together into a page by a developer.
[1270.40 → 1271.26] And so, that's really the push.
[1271.26 → 1283.60] The push is developers who, you know, don't have the time to build a whole content management system or designers who can't build one but can learn how to, you know, how to do a little bit of programming to do some template stuff.
[1284.44 → 1289.72] And then they're making sites for themselves and for clients who can't do all the HTML and things like that themselves.
[1289.78 → 1294.16] And they just want to put, you know, their tiny little pieces of data, an event title or a date, stuff like that.
[1294.24 → 1299.26] And so, that's really the big push is I guess that would be kind of the target is those kinds of people.
[1299.26 → 1301.84] You mentioned Expression Engine in there.
[1302.06 → 1309.16] Is that one of your – what other CMSs do you have experience with using that kind of led you down this path besides the one you mentioned when –
[1309.16 → 1309.48] Sure.
[1309.84 → 1310.88] Your previous –
[1310.88 → 1316.08] So, the first one that I got in touch with that probably everybody gets in touch with is WordPress.
[1316.92 → 1317.06] Right.
[1317.48 → 1319.18] So, that's – I mean I started in PHP.
[1319.44 → 1320.04] I can admit it.
[1320.38 → 1321.98] And nothing wrong with PHP.
[1322.10 → 1322.90] I just always like to tease.
[1324.08 → 1325.28] But so, yeah.
[1325.36 → 1326.18] So, the first one was WordPress.
[1326.18 → 1332.42] I mean I had a WordPress blog like basically like as soon as I was out of college and, you know, I hacked something together and got going with it.
[1333.46 → 1336.90] And WordPress is great for blogging but they kind of bolt on pages.
[1337.46 → 1341.32] And so then, you know, we tried Mephisto when Techno came out with that.
[1341.44 → 1341.92] Bless his heart.
[1342.68 → 1344.76] And it's – you know, Mephisto is great.
[1345.38 → 1349.78] It really – you know, it was better than WordPress, but it still wasn't quite what we were looking for.
[1349.84 → 1350.98] But it was a lot closer.
[1350.98 → 1354.42] And, you know, we've linked around with Expression Engine a little bit.
[1354.58 → 1358.76] I wouldn't say that either of us has – I work with one other person, Steve Smith.
[1359.28 → 1363.02] And I wouldn't say either of us has really hacked around a lot enough to give an educated opinion.
[1363.20 → 1365.70] Just our initial impression was that it was really complex.
[1366.04 → 1370.24] Like you can do anything you want, but it just seemed like it was a lot of work.
[1370.64 → 1370.78] Yeah.
[1370.90 → 1372.02] I've had some experience with it.
[1372.02 → 1376.30] And it seemed like every – I too came from PHP.
[1376.36 → 1377.70] I think we all came from PHP, right?
[1378.50 → 1380.30] When we look back on our past, we can't hide that.
[1380.72 → 1386.68] But I had a lot of experience with building Expression Engine sites and I probably have done at least maybe 15 or more.
[1387.10 → 1392.30] And it seemed like every new project was just – you couldn't really build the framework that you could do with Rails.
[1392.30 → 1396.68] Like, you know, you could build a Rails template or, you know, now we have engines and stuff like that.
[1396.68 → 1401.26] But you just couldn't do that with – at least I couldn't.
[1401.34 → 1402.74] I didn't have enough skill set to do it.
[1402.76 → 1403.50] And that was the pain point.
[1403.58 → 1406.78] It was just each project took so much start time, and it was just a pain in the butt.
[1407.60 → 1407.86] Yeah.
[1408.40 → 1413.88] I mean I say yes in that I can relate with that, not in that I've run into that with Expression Engine.
[1414.28 → 1415.80] But, I mean, that is the thing.
[1415.90 → 1419.04] Like you want to make it – like most websites are very similar too, you know.
[1419.10 → 1425.08] So, I mean we're going to have – and pretty much the whole website in Harmony is driven by the theme.
[1425.08 → 1430.60] So, you have a theme, and then you have – themes have templates and, you know, includes and they have style sheets and JavaScript's.
[1430.68 → 1436.00] And templates have fields and fields kind of define what the form looks like.
[1436.02 → 1440.26] It's kind of like a form builder, you know, for a content person when they go to the content area.
[1441.66 → 1445.78] And so, I mean what we're going to do is have theme export and import and stuff like that.
[1445.82 → 1451.82] So, you can really easily, you know, create a site that's a certain way, you know, like products, blog, you know, et cetera, stuff like that.
[1451.82 → 1457.68] And then you can very easily dump that and reimport it somewhere else.
[1457.76 → 1462.88] Or literally we even have – if sites are in the same account, you can copy a theme directly from another one.
[1463.30 → 1467.62] And so, you have – you can kind of get a little bit of a framework going and just kind of dump it in real easy.
[1468.56 → 1471.66] But, yeah, I mean the main goal is just – we just want to make content management fun again.
[1471.78 → 1476.40] I mean we're just finding a lot of people that like they get frustrated with their various, you know, software.
[1476.70 → 1478.82] And so, then they don't blog, or they don't –
[1478.82 → 1481.28] That's my problem. That was my problem for a long time.
[1481.34 → 1483.22] It was just that, you know, the right tool.
[1483.50 → 1486.70] Like you said, you haven't found the right tool to get you into it and make it fun again.
[1487.46 → 1487.82] Exactly.
[1488.56 → 1494.02] Again, with WordPress, you know, you have custom fields and with Expression Engine you have options for stuff like that too.
[1494.44 → 1502.90] But you get so deep into the customization of it that it gets lost and you kind of go away from the, you know, the mainstream of who's using the app.
[1503.52 → 1504.44] It gets really difficult.
[1505.10 → 1507.18] Totally. And that's the strength of Congo.
[1507.18 → 1512.90] I mean we had Harmony 95% of the features that are in Harmony right now.
[1513.00 → 1515.12] We had it 95% done in MySQL.
[1515.88 → 1519.56] And it was just turning into a mess in spots.
[1520.68 → 1522.80] And it was getting really hard.
[1522.96 → 1523.90] And we were like, you know what?
[1524.62 → 1530.32] Let's just bite the bullet and let's just switch to this crazy new database, Congo, and see what happens.
[1530.32 → 1534.92] And we literally switched the whole site over in like a week or two of kind of nighttime hacking.
[1534.92 → 1539.42] And now we have this incredible flexibility.
[1540.58 → 1544.28] You know, like we literally built Harmony from the ground up with custom fields.
[1544.64 → 1547.24] Like that's – we're like this is not something we're going to tack on.
[1547.80 → 1549.48] This is what everybody uses.
[1549.86 → 1555.72] Everybody wants to say like here's the content on my page and then, you know, uses some kind of template or something to mark it up.
[1556.46 → 1557.70] So, I mean that's just kind of –
[1557.70 → 1561.30] Yeah, I mean yeah, I think it's really cool.
[1561.58 → 1567.00] So, I mean we've got a long ways to go before it's going to take over the world or anything like that.
[1567.32 → 1567.96] Let's hope, right?
[1568.02 → 1568.80] Let's hope for sure.
[1568.96 → 1570.14] Yeah, let's hope.
[1570.14 → 1577.96] So, you said a little bit earlier that you were – you know, you jumped on the open source bandwagon a long time ago.
[1578.18 → 1581.82] And obviously in Harmony you've used lots of open source stuff.
[1582.08 → 1584.92] But, you know, how has open source really fuelled your business?
[1585.82 → 1586.34] Oh, man.
[1586.50 → 1589.94] Well, it's – so it would probably be two ways.
[1590.06 → 1594.16] One, it's fuelled it in that, you know, we use open source for client projects.
[1594.16 → 1596.58] So, I mean that would be the first way.
[1596.66 → 1606.20] And then the second way would obviously be that because of, you know, open source projects that I've had and, you know, getting the name out there and stuff like that, we've gotten business from that.
[1606.28 → 1608.10] So, I mean there's kind of two ways that it's fuelled it.
[1608.16 → 1609.74] It's one, we use it.
[1609.84 → 1616.12] And two, by creating it and getting involved in that, you know, work comes in because people are like, oh, I saw you worked on this.
[1616.18 → 1617.12] Can you help us with this?
[1618.34 → 1623.04] And especially with Monographer now, I think we've noticed that a lot because a lot of people are really curious about Congo.
[1623.04 → 1627.56] So, I would say it's – and really in two ways it's fuelled our business like that.
[1627.84 → 1631.54] And probably the biggest way is using it in client projects, you know.
[1631.60 → 1634.98] I mean Harmony is like there's nothing paid in that thing.
[1635.14 → 1637.84] I mean, you know, we're using – I mean I could probably just run through a list.
[1637.90 → 1642.88] We're using, you know, Moonshine for like setup and deployment and stuff like that which is built on top of Puppet which, you know.
[1643.34 → 1648.56] And we're using all open source, you know, OS obviously for the servers and stuff like that.
[1648.60 → 1650.30] We're using Nazi for jobs.
[1650.40 → 1651.72] We're using Congo for the database.
[1651.72 → 1652.46] We're using Ruby.
[1652.46 → 1655.94] I mean everything from the ground up is all open source.
[1656.24 → 1661.74] And so, I mean it's completely driving our business I guess would be the best way to say it.
[1661.82 → 1664.58] I think it's so awesome how that happens, you know, how the community comes together.
[1664.88 → 1669.44] And, you know, GitHub starts two years ago and Git becomes more and more prevalent, and we all start to social code.
[1669.66 → 1675.36] And now everything you do is powered by what is out there from the social sphere of us open source developers.
[1675.82 → 1676.14] Yeah.
[1676.26 → 1678.68] And I spent some time in, you know, in other languages.
[1678.68 → 1684.54] I mean like I'm sure we all have and not all other languages have this kind of open source mindset.
[1684.78 → 1691.50] You know, I mean we spent at Notre Dame, you know, we spent probably two years in Cold Fusion before hopping on the Rails bandwagon.
[1691.50 → 1695.84] And, I mean, Cold Fusion doesn't – I mean there is definitely an open source movement in Cold Fusion.
[1695.98 → 1696.66] Like don't get me wrong.
[1696.82 → 1702.58] But like almost everything you want to use, like back in the day at least, you know, 2006 or whatever, it was all paid.
[1702.72 → 1705.98] Like you had to like, you know, pay $50 here or $100 here.
[1706.12 → 1707.68] There was nothing that was just like free.
[1707.68 → 1709.76] It was really hard to do that.
[1709.88 → 1716.56] So, I mean, I think there's a massive benefit to releasing this free, getting the whole community involved and making everything better.
[1716.86 → 1718.38] And I totally agree with that.
[1718.58 → 1720.26] You know, it's amazing to watch – sorry.
[1720.34 → 1729.00] It's amazing to watch, you know, the one business that releases a byproduct of their business as an open source project that another business will then take that and run with it.
[1729.18 → 1733.00] So, you know, Liquid, you're using that for template markup, right?
[1733.00 → 1734.08] And that came out of Shopify.
[1734.68 → 1738.18] And so, you know, how many apps have been built on top of Liquid?
[1738.26 → 1740.60] I think I've built, you know, just some personal projects myself.
[1740.70 → 1746.34] It's just amazing how, you know, the sum is greater than the parts, right?
[1746.84 → 1747.14] Mm-hmm.
[1747.42 → 1747.80] Totally.
[1747.96 → 1753.82] I can't imagine that we would have ever built Conductor or Harmony without Liquid.
[1754.02 → 1756.94] I mean, I don't know what we would have used.
[1757.04 → 1757.88] Liquid is just great.
[1757.98 → 1759.94] Especially – it's a little bit mind-bending at first.
[1760.00 → 1761.96] But once you really dive into it, it's really simple.
[1761.96 → 1768.74] I mean, we've – there are actually a few spots where we kind of even tweaked Liquid just to be – to do a few more things that we wanted to do.
[1768.86 → 1770.96] And it was not hard at all, you know?
[1771.04 → 1772.94] So, I mean, that's a really great point.
[1773.46 → 1773.68] Cool.
[1774.10 → 1774.50] All right, John.
[1774.54 → 1777.84] We're at the point of the show where we normally ask folks what's on their open source radar.
[1778.08 → 1780.20] So, you know, what's got you excited?
[1780.38 → 1781.72] And it doesn't have to be Ruby, of course.
[1782.24 → 1785.00] What's out there that just has you excited in the world of open source?
[1785.44 → 1786.38] Ah, good question.
[1786.38 → 1792.86] Well, I would say first off, I'm turning into a bit of a – I don't know what the word is.
[1792.96 → 1797.40] But like I love non-relational databases quite passionately.
[1797.76 → 1802.04] And, you know, my wife's okay with it, but it does make for some awkward times.
[1802.92 → 1805.54] But it's – I would say Regis, awesome.
[1805.70 → 1806.30] I mean, really cool.
[1806.42 → 1808.44] So like Rescue, I've been really curious about that.
[1808.64 → 1810.00] We were real tempted to try it.
[1810.00 → 1812.70] But we're kind of trying to stay simple with one database right now.
[1814.56 → 1816.86] But Regis and Rescue, I think, are really intriguing.
[1817.94 → 1820.04] So, yeah, I'd say Regis and Rescue are big.
[1820.80 → 1824.74] There's a ton of really – RISC or however that's pronounced.
[1824.90 → 1829.08] It's like an HTTP JSON database that I think looks really cool.
[1829.30 → 1832.36] The Persevere is like an interesting JSON database.
[1832.96 → 1834.94] Like I think it's more of a graph type thing.
[1835.30 → 1837.74] Or no, there's another one that's like a graph type database.
[1837.74 → 1848.04] But there are a lot of NoSQL databases out right now that I just think are really, fascinating from an intellectual standpoint in that I don't understand how they work at all, and I want to play with them.
[1849.32 → 1859.10] So, I mean, I think databases are kind of the biggest thing on my radar right now just because we're moving into a time when it doesn't always make sense to do everything with SQL.
[1859.34 → 1862.18] So that's probably what's been on my radar the most.
[1862.84 → 1865.12] I've been kind of interested in like testing as well.
[1865.12 → 1869.64] Like interesting – so like Nantes is a project on GitHub.
[1870.22 → 1873.92] I think the tagline is when all you need is Ruby.
[1874.52 → 1879.34] And so you literally just assert something and then use Ruby like array.include.
[1879.54 → 1883.54] And so you're just – your last line of the test always has to return true.
[1884.20 → 1885.68] And if it returns false, then it's a failure.
[1886.08 → 1887.58] So that's kind of an interesting idea.
[1888.26 → 1890.90] So, yeah, I would say mostly databases are on my radar.
[1890.90 → 1894.86] And then there are a few testing things that I think are fascinating as well.
[1895.52 → 1898.32] No, John, I think it's cool that you're that doubt into open source.
[1898.44 → 1900.36] I think it's – we didn't start this podcast.
[1900.48 → 1903.10] We didn't start this blog and what we're doing because –
[1903.10 → 1905.44] Well, we had an excellent name that we just could not turn down.
[1905.64 → 1906.06] That's true.
[1906.22 → 1906.30] Yeah.
[1906.50 → 1906.98] Change is lost.
[1906.98 → 1914.92] But there's people out there like you and like Marshall Culpeper from Accelerator and the people that started Congo.
[1915.08 → 1918.08] I mean those people need to have someone chime in for them.
[1918.16 → 1927.38] And I think this is awesome to hear you talk about open source so passionately and also to reflect on your business and this application called Harmony that you're doing and how much has fuelled what you're doing.
[1927.52 → 1928.10] It's awesome.
[1928.62 → 1929.00] Very cool.
[1929.20 → 1929.40] Yeah.
[1929.54 → 1930.52] I couldn't agree more.
[1930.64 → 1932.98] I mean it's a great time.
[1933.20 → 1936.44] It's literally the best time to be involved in web stuff right now.
[1936.44 → 1939.78] I can't think of a time that it would be more awesome.
[1939.94 → 1941.82] I mean there's just so many cool things happening right now.
[1942.46 → 1952.22] It's – sometimes I just sit awake at night thinking about all the crazy stuff that's happening and jealous that I have to sleep to be able to perform the next day.
[1952.76 → 1954.28] Well, one last plug for Harmony.
[1954.42 → 1955.04] I've seen it.
[1955.14 → 1955.78] I've kicked the tires.
[1955.98 → 1957.30] It's a great app.
[1957.32 → 1958.80] I can't wait to use it.
[1958.80 → 1961.72] I'm trying to decide which of our sides we want to bite off first with it.
[1961.72 → 1967.80] But any idea when a public beta might be available and guys listening can jump into Harmony?
[1968.22 → 1968.62] Yeah.
[1968.78 → 1975.46] I mean right now you can go to the HarmonyApp.com and there's a sign-up form at the bottom, and we'll notify people.
[1975.74 → 1984.82] As far as the public beta, we have a couple of things that we feel like we kind of need to get wrapped up like a way to import your sites and stuff like that.
[1984.82 → 1991.54] So some kind of API, and then I don't know that we'll really ever honestly to be – to just put it out there.
[1991.58 → 1993.04] I don't know if we'll have an open beta.
[1993.24 → 1999.00] We're probably just going to have kind of a smaller one and just keep letting people in and keep letting people in, and eventually we'll just open the doors.
[1999.96 → 2001.88] So I don't know that we'll really have it.
[2001.92 → 2005.26] We're really hoping – we're big South by Southwest fans.
[2005.26 → 2008.92] So we're really hoping to be launched like around there.
[2009.04 → 2009.62] We'd love that.
[2009.92 → 2015.10] But it's a side project that we're putting a lot of time into, but it's still a side project.
[2015.26 → 2015.82] So we'll see.
[2016.80 → 2018.34] We're also averse to deadlines.
[2019.58 → 2022.76] So it's hopefully in the next couple of months.
[2022.90 → 2026.82] I would say that is the most specific thing I can give, which is not very specific.
[2027.44 → 2028.60] Well, thanks for joining us today, John.
[2028.70 → 2032.00] We want to give a hat tip to all the projects that you mentioned today.
[2032.08 → 2033.78] We'll be sure and do that in the show notes.
[2033.78 → 2045.14] But I think the takeaway is that if you're building a business, and you've got an aspect of a product that you could release and give back to the community, please do so because you never know the next entrepreneur that's going to be standing on those shoulders.
[2045.94 → 2046.26] Absolutely.
[2046.48 → 2047.00] Thanks a lot.
[2047.34 → 2048.28] It was a lot of fun talking to you guys.
[2048.52 → 2048.98] Yeah, absolutely.
[2049.08 → 2049.76] Thanks for coming on the show.
[2055.86 → 2058.74] Thank you for listening to this edition of The Change Log.
[2058.74 → 2066.54] Point your browser to tail.thechangelog.com to find out what's going on right now in open source.
[2067.80 → 2076.28] Also, be sure to head to GitHub.com forward slash explore to catch up on trending and feature repos as well as the latest episodes of The Change Log.
[2076.28 → 2106.26] The Change Log.
[2106.28 → 2109.10] Forever Real.
[2109.38 → 2109.82] Forevermore.
[2109.98 → 2111.98] Forever Straight.
[2111.98 → 2141.96] Thank you.
