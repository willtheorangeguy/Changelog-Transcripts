[0.00 → 15.22] welcome back everyone this is the change log I'm your host Adam Stokowski this is episode 148
[15.22 → 21.24] and on today's show we're joined by Andrew Duran Andrew works on the go programming language at
[21.24 → 26.62] google you might remember him from back in episode 100 with rob pike this show we're talking about
[26.62 → 32.94] the state of go in 2015 great conversation today with Andrew we also had some awesome sponsors for
[32.94 → 38.54] the show code ship top towel and digital ocean we'll tell you a bit more about top towel and
[38.54 → 42.22] digital ocean later in the show but our friends at code ship released a brand-new feature called
[42.22 → 47.14] parallel CI we're super excited about it, they're super excited about it, and you should be too
[47.14 → 54.32] because now you can deploy your code to production 10 times faster if you want faster tests you have
[54.32 → 60.04] to run your builds in parallel with parallel CI you can now split up your test commands into up to 10
[60.04 → 66.10] test pipelines this lets you run your code in your test suite in parallel and drastically reduce the
[66.10 → 70.68] time it takes to run your code they integrate with GitHub and Bitbucket, and you can deploy to cloud
[70.68 → 77.08] services like ROK AWS and many more get started today by their I check out their free plan it includes
[77.08 → 83.46] 100 builds a month and five private projects, or you can use our offer code it's the change law podcast
[83.46 → 90.20] to get 20 discount on any plenty choose for three months again that code is the change law podcast
[90.20 → 95.18] head to codeship.com slash the change law to get started and now on to the show
[95.18 → 102.08] all right everybody we're back we got Andrew Duran on this on the call today Andrew how are you
[102.08 → 108.34] hey good great Andrew we're uh we're flying solo today we have no jarred with us so for long-time
[108.34 → 113.28] listeners to the show you're gonna miss jarred on the show I hope you miss him but not so badly that
[113.28 → 119.66] you don't like the show so right and I think the last time you were on the show uh jarred wasn't even
[119.66 → 126.28] a co-host on the show yet air uh Andrew was uh co-hosting with me and I think he did episode 100 with
[126.28 → 133.94] you and rob totally solo so that's that's kind of cool too almost 50 shows ago man wow
[133.94 → 139.78] not to believe I'm sure you excited to be back though right this is uh yeah it's great one of
[139.78 → 141.08] your favourite podcasts I'm sure
[141.08 → 149.76] I don't even know how to respond to that of course it is that's how you respond oh yeah of course great
[149.76 → 156.44] I love it right okay guys I don't listen to a lot of podcasts so uh no for the listeners if
[156.44 → 163.22] if you're not familiar with whom Andrew is Andrew works on the go programming language uh aka Golang
[163.22 → 170.86] or uh you know that's that's kind of how you say it I guess um yeah we just call it go okay
[170.86 → 178.46] not apparently my ex I can't say it in correctly because of my accent um maybe you should cut that
[178.46 → 184.02] out no go ahead say it one more time nice and clear well i say go um well you got the
[184.02 → 192.58] awesome Australian accent right so yeah awesome slash ridiculous uh I think it's awesome I mean I'm glad
[192.58 → 198.38] i kind of wish I had that accent sometimes not all the time, but man there are some really cool
[198.38 → 203.98] Australian accents out there that I mean you all have the same accent to a degree, but there are just some
[203.98 → 209.46] that sound better than others so I'm a fan sometimes people in Australia think that I'm
[209.46 → 214.76] not Australian because I guess I spend a lot of time speaking to international audiences and so i
[214.76 → 219.22] sort of round out my accent a little bit right then it just makes me sound weird to everyone
[219.22 → 225.32] so I don't know whether I'm seeing the benefits or not that's it well you hail from as we said
[225.32 → 230.32] Australia so you work at Google Sydney and in the pre-call I asked you a question that we had to pull
[230.32 → 235.32] into the show because I just thought your answer was pretty neat but uh just for some uh you
[235.32 → 240.56] know background you know what's different about google Sydney than like plain old google
[240.56 → 245.76] Sydney is definitely part of plain old google it's not a separate entity or anything like that I mean
[245.76 → 254.30] google has tens or probably hundreds of offices around the world um probably like tens of large
[254.30 → 260.16] engineering offices um and google Sydney is one of the largest Google offices outside of you know
[260.16 → 265.48] Mountain View the headquarters but google Sydney is kind of cool because um it has a long history at
[265.48 → 271.36] google it's one of the one of the first overseas engineering offices and the story behind it is kind
[271.36 → 279.34] of interesting because the team that built the product um that became Google Maps so it was a
[279.34 → 284.30] was a company outside Google that built it, and they sold the technology to google and they
[284.30 → 290.86] they also joined google when they sold it and so the people who built that original basically like a
[290.86 → 299.04] prototype they um became but the first employees of Google Sydney more or less and there's a lot more
[299.04 → 305.14] detail in there, but that's that's basically the story and so you know I think maps is one of
[305.14 → 311.64] the major ways in which google has affected the world you know search is the first one and then i
[311.64 → 317.80] would say like for me personally maps was the second big revelation that not i I've only been to
[317.80 → 321.76] google for five years so it has nothing to do with me, but it was one of the things that really impressed
[321.76 → 326.54] me about google, and so I think it's cool that you know Sydney and google Sydney was sort of the
[326.54 → 332.76] birthplace of that you said you've been with Google five years now so that's almost the age of go
[332.76 → 340.30] yeah well I joined google and the go team a couple of weeks after I'm sorry a couple of months after go
[340.30 → 347.90] was released what was that what month was that that was I started the start of February 2010 okay and
[347.90 → 354.20] go was released in November 2009 that's so crazy because that is our birthday the changelog was born
[354.20 → 362.70] November 19th 2009 right we'll go with November 10 so we're a little bit older slightly older
[362.70 → 371.04] that's funny because our third show was with rob bike oh really yeah our third show wow yeah three
[371.04 → 379.10] 1148 we covered go super early and uh you know when we say fresh and new and open source we mean it
[379.10 → 385.22] so episode number three the channel.com slash three is a show you listen to this is way back in the day
[385.22 → 389.82] too so if you want to get nostalgic uh listeners of this show long time fans of this show go back and
[389.82 → 396.32] listen to that show and hear the difference in audio quality this is like look this is the
[396.32 → 401.32] know the version of a developer going back and looking at code that's five years old
[401.32 → 407.74] you know not a great conversation but the know our production value is a lot different from
[407.74 → 415.86] win and I win Netherlands now he hacks on uh the Google or the uh the GitHub API, but we were so fresh
[415.86 → 420.90] and green with podcasting I think then it was just it was a different landscape this was before it was
[420.90 → 426.24] cool to you know so it's a different world you know podcasting is cool now didn't you hear
[426.24 → 434.30] I'm not even kidding I'm not even kidding yeah actually I must admit I have been thinking about
[434.30 → 441.56] recording my own podcast see um yeah I think it'd be cool to actually have a podcast where I interview
[441.56 → 447.14] people in the go community and talk to them about what they're doing and what they think and so on
[447.14 → 451.94] I don't disagree I don't disagree I think you should do it and I'm going to encourage you to do it
[451.94 → 457.88] yeah um in fact we may be able to help you oh we can talk about that later yeah let's let's
[457.88 → 462.88] definitely earmark that conversation but so a year and a half ago so we've been talking about the past
[462.88 → 467.98] a little bit in preparation for talking about today and the future but a year and a half ago episode 100
[467.98 → 472.40] you were on the show with rob you guys talked deeply about the history and the details of the
[472.40 → 477.96] language uh simplicity concurrency productivity it's not just a systems language it's sort of just
[477.96 → 483.68] giving a rough summary of some of the things that I pulled out there um but recently in February you
[483.68 → 490.56] gave a talk at uh is it FOS them or is it FOS them I guess it's if you're pronouncing it in Australian
[490.56 → 497.38] accent it's FOS them because we pronounce all s's like z's, but it's probably FOS them okay I'm going to go
[497.38 → 503.88] with I'm going to go with either I don't know FOS them I'll say FOS them because it seems like uh well we had
[503.88 → 513.62] the same uh conundrum with uh Oscan is it Oscan or is it Oscan or see yeah see you probably say Oscan
[513.62 → 521.90] right I say Oscan see now I would always say Oscan as well but even jarred myself and uh who was it
[521.90 → 527.02] that was on the show that time someone from Facebook and I can't remember her name right now
[527.02 → 532.98] it's its uh upsetting me but anyway we couldn't figure it out either so you talked about the state of
[532.98 → 539.26] go at FOS them uh it's basically the Oscan speaking of Oscan the Oscan of Europe basically right
[539.26 → 544.90] that's that's what that yeah I mean i actually I think not to say anything bad about Oscan i quite
[544.90 → 551.20] like Oscan as a conference but FOS them is almost something else it's its an amazing community-driven
[551.20 → 557.06] conference that's totally non-commercial it's hosted at a university, but the really remarkable part is
[557.06 → 562.60] it used to it used to have an emphasis on like the main track talks which were curated by the
[562.60 → 569.26] conference organizers um, but they had these things known as dev rooms where people in the community
[569.26 → 574.36] could register interest in running a dev room and basically that means that they would get a day
[574.36 → 580.50] and a room and some equipment, and they could run their own thing there and like it was they called
[580.50 → 585.68] dev rooms because originally it was like you know all the people working on like open step for instance
[585.68 → 590.24] would get together, and they would talk about all right well what are we going to work on over the next
[590.24 → 594.90] year, and maybe they'd even get some hacking done or some like API design or something like that
[594.90 → 600.82] and then gradually the emphasis has really shifted over to these dev rooms, and they've now become like
[600.82 → 606.42] curated many conferences inside the greater conference and so all the action actually happens
[606.42 → 612.30] at these dev rooms and the dev rooms yeah yeah and so like i the last couple of years I've organized
[612.30 → 617.86] the go dev room and curated you know speakers from the go community to talk about go stuff
[617.86 → 624.52] and um so it's its it's really awesome in that it's its just totally grassroots totally community
[624.52 → 632.22] driven um it's very, very much a free conference it's free to attend, and you know it's very sort of
[632.22 → 636.98] democratic in a way, and so I feel like more than any other conference I've been involved with
[636.98 → 640.22] FOSDEM really embodies like the spirit of the open source community
[640.22 → 648.54] well we have a weekly email we ship out on Saturdays and I am going to link up all the
[648.54 → 654.32] the playlists that you linked out on um I think it was a couple of weeks back or something like that
[654.32 → 660.98] maybe a month back or something like that so all the dev rim talk at FOSDEM is going to be
[660.98 → 668.02] in our weekly email this Saturday so um we're recording this on a Wednesday and actually the day uh
[668.02 → 676.90] I don't usually time stamp these but March 18th this show won't go live until the 27th of march
[676.90 → 681.48] just so you know and everybody else listening so it's the 27th or after if you're a member you're
[681.48 → 687.78] listening live potentially, but it's March 28th that's when we're recording this um so we'll actually
[687.78 → 692.82] link that up this Saturday which will be before this and uh you know I blew somebody's mind
[692.82 → 696.96] away whenever I was like we're recording this in the future, and you're listening to this in the past
[696.96 → 701.12] because it's kind of how the podcast is right we listen we record it in the past, and you listen
[701.12 → 706.56] to the future, and it's kind of all jacked up uh unless you're actually listening live but anyway
[706.56 → 712.92] the so the state of go FOSDEM you know you mentioned you've been running that room for the last couple
[712.92 → 717.26] years what are some of the things you've seen happen over the last couple of years running that room
[717.26 → 723.22] around the go community well you know with regard to the room specifically I mean it's just we've just
[723.22 → 728.92] seen some a lot of great talks from people particularly at the end of the day we tend to
[728.92 → 734.84] do lightning talks and people can sign up for the lightning talks on the day, and you know it's its
[734.84 → 740.64] really it's really fun to see people just pull out like their fun little projects that they've been
[740.64 → 746.14] hacking on you know things that they would never really bother submitting like a full-scale conference
[746.14 → 754.76] talk um, but you know for instance at the conference this year we saw a guy presented his um
[754.76 → 761.30] he wrote a like a backup system in go, and he was fairly serious about it and so it was actually
[761.30 → 767.72] quite a nice solid product that he produced another guy showed this really bizarre thing called a
[767.72 → 776.06] phonoscope I think which is like a old school way of producing moving images um by sort of uh
[776.06 → 780.64] it's probably too difficult for me to explain uh you'll have to google it, but you need a visual it
[780.64 → 786.04] was it was a visual thing it was kind of wild it was pretty unexpected so do you have the past
[786.04 → 791.14] years on video then yeah, yeah, so the playlist includes the uh the lightning talks and all the
[791.14 → 797.06] lightning talks are uh in the YouTube video description we have the time stamps of when each of the talks
[797.06 → 802.16] begin so you can skip through them awesome so definitely check them out actually last year there was a
[802.16 → 808.38] great one from one of our contributors a guy called Remy dumping who's who's a French guy who's been
[808.38 → 816.10] off and on contributing to the compiler and runtime very smart guy but he just i kind of like me and
[816.10 → 821.00] brad pushed him throughout the day to like you should give a talk Remy come on and um he was pretty shy
[821.00 → 826.36] but he ended up writing this talk like why you should contribute to go um, and it was a really nice little
[826.36 → 831.34] little talk about why it's nice to work on the go project which resonated with me at least
[831.34 → 837.24] you know I got sort of an off question I guess before we actually dig into the state of go
[837.24 → 845.50] but we just had a conversation about phoenix and elixir phoenix web framework and elixir built on top of
[845.50 → 851.76] the Erlang uh VM and one of the one of the pieces of that conversation that stuck out to me was the
[851.76 → 859.50] concurrency, and it talked about how um Erlang had been doing concurrency for years you know they saw this
[859.50 → 863.38] problem 20 years ago and I hear a lot and I've heard a lot over the last year and a half since
[863.38 → 870.44] the last time I've been on the show about go and concurrency in in that direction what is it
[870.44 → 876.34] about go in comparison to say like java which you're planning to supplant and languages like Erlang or even
[876.34 → 883.50] elixir how do you how does go uh compete with or what is the landscape like in comparison to those
[883.50 → 888.56] other languages that are concurrent as well there's a there's a lot in that question so it's
[888.56 → 897.00] it's quite a deep topic but I think what Erlang gives you and elixir as well is this environment in which
[897.00 → 905.08] to build distributed concurrent systems or maybe concurrent systems, and you know it's very much baked into
[905.08 → 912.46] like every part of working with those languages is you think about concurrency and message passing
[912.46 → 916.62] and so on because that's my understanding I don't have a lot of experience with them yeah um but
[916.62 → 922.36] that's that's how I took it as well yeah but with go um concurrency is always there you can always
[922.36 → 929.06] use it use the concurrency features um when you want to do something that involves concurrency so it's
[929.06 → 935.68] that we provide really nice tools for like modelling concurrent processes, but it's its not uncommon to
[935.68 → 941.82] write go programs that use no concurrency at all you know you don't have to use those tools or think
[941.82 → 946.72] in that mindset if it's not appropriate for what you're doing like if you're just if you're writing
[946.72 → 952.14] a tool to open a text file process a bunch of lines and compute something and print the output
[952.14 → 957.84] you know your concurrency is not really appropriate it's an inherently serial process um so you don't
[957.84 → 963.64] need the tools if they're not there uh if they're not necessary, but there's that aspect there's also the
[963.64 → 969.58] aspect that go is still very much you know an imperative programming language it's not a functional
[969.58 → 977.12] programming language um so it's a lot more familiar to most programmers and the model in which you're
[977.12 → 982.82] running go programs is also familiar you know you write a go program that runs as a process
[982.82 → 990.94] and then that process may talk to other processes, but there's no sort of infrastructure to manage those
[990.94 → 996.58] processes or pass messages between them or anything none of that's baked into the language unlike
[996.58 → 1001.92] Erlang which is gives you that entire framework for doing that and so with go it's its very much
[1001.92 → 1009.44] like you program with concurrency assuming that you're operating inside a single process and so
[1009.44 → 1015.30] you know like if you send a message um across the channel, and it's received by some other go routine
[1015.30 → 1021.56] in the process like you know if you're still executing than that other go routine must still be
[1021.56 → 1026.56] executing like if the program hasn't crashed then the program is still running and so it's
[1026.56 → 1031.60] actually even though there are parallels you can draw between the way you write code in Erlang and
[1031.60 → 1036.00] the way you write what the way you might write code and go you can't really compare them they're
[1036.00 → 1043.72] actually very, very different approaches I see I was you know when I was um on that call I was
[1043.72 → 1050.08] thinking Angie's going to be on the show I should talk to him about this because I don't I I don't write
[1050.08 → 1055.96] Erlang code I don't we're actually just uh tinkering with some elixir stuff as we speak but
[1055.96 → 1062.56] and I've never written much in go besides maybe some um you know a hello world so I'm actually not
[1062.56 → 1068.26] even a great candidate for asking you the deeper questions, but it always made me wonder about the
[1068.26 → 1074.78] concurrency issues um about that that that topic there whether you know why someone would
[1074.78 → 1079.08] choose or what kind of applications someone's building that are drastically different that makes
[1079.08 → 1085.18] someone choose elixir Erlang or go you know what kind of choices does that programmer go through
[1085.18 → 1088.96] when they're actually building the application like what makes them choose the language
[1088.96 → 1095.64] and like with for example with ruby you know a lot of the times you are building you know systems
[1095.64 → 1101.22] or for the web and you're choosing it for the elegance and the readability of the language and the
[1101.22 → 1105.90] the developer joy of the language and some of those things that come with it, you know so what are the
[1105.90 → 1111.04] reasons why someone chooses go over one of these other languages that have competing feature sets
[1111.04 → 1117.30] right well I mean i the reasons why like I choose go and I think other people choose go
[1117.30 → 1125.54] are a lot to do with that sort of programmer joy thing um you know very much uh the overwriting
[1125.54 → 1129.86] sentiment amongst go uses is that go just kind of gets out of your way and lets you write code
[1129.86 → 1136.16] um it doesn't really give you the tools to sort of over abstract things and so you tend to just like
[1136.16 → 1143.38] write the simple code that does the thing you want to do now as opposed to you know dreaming about how
[1143.38 → 1149.64] you might do like how you might want to abstract this so you can make it more useful later which is a
[1149.64 → 1156.50] a wonderful uh very interesting trap that programmers fall into all the time and so you know it kind of
[1156.50 → 1161.74] resists over engineering a lot but I think the features that it does provide are very well
[1161.74 → 1168.44] considered and just tend to work in predictable ways so you don't really spend time like looking at the
[1168.44 → 1175.04] language spec, or you know wondering if what you wrote is going to do what you think it does um once you
[1175.04 → 1181.38] know the language um which doesn't take very long you really you just know it and you can just use it
[1181.38 → 1186.98] yeah and that was one of the things I pulled out from to call back to episode 100 when you and rob
[1186.98 → 1191.60] were on was that uh when they were first writing I remember rob saying that he had remembered the
[1191.60 → 1197.20] entire language and is you know he can, he wanted to build a language that he can keep in his memory
[1197.20 → 1203.22] his current memory and not have to go back and forth to docs well that's that it is not just like
[1203.22 → 1209.64] at the language level like I was talking about to rob about this recently you know uh recently uh we've
[1209.64 → 1214.80] just converted the whole and I guess we're heading into talking about this um we just converted the
[1214.80 → 1222.16] the tool chain from c to go so it was originally written in c now it's written in go, and you know
[1222.16 → 1228.48] some there have been some criticisms um from people in the programming community saying you know are you
[1228.48 → 1234.46] the go people they should have just used SLBM, or they should have you know built this on GCC or
[1234.46 → 1241.14] something like that and the counterargument to that is we've just been able to do some really
[1241.14 → 1248.04] very interesting work on the compiler and the tool chain and there's more a lot more to come and part
[1248.04 → 1255.18] of the reason that that is possible is that it's its possible for people on the team to keep the
[1255.18 → 1261.42] entire tool chain in their head and that is just not possible with some of these larger compiler
[1261.42 → 1267.80] projects like they're so huge you know they're massive engineering projects that do a tremendous
[1267.80 → 1274.94] amount of work and that is really antithetical to the entire design philosophy of go and all the go
[1274.94 → 1282.82] tools and I think one way to be spectacularly productive is to keep things small enough so that
[1282.82 → 1288.50] you can know the entire thing so yeah I think that's that's really just a core tenet of what we're
[1288.50 → 1294.74] about, and it's been a source of great success for us so far that's certainly a great transition into
[1294.74 → 1300.16] the larger talk we'll have here in just a second so Andrew I didn't mention this before the call but
[1300.16 → 1304.98] I'm going to take a quick break here and do a spot for one of our sponsors for this show so
[1304.98 → 1309.92] we're back in just a second we'll talk to Andrew about the state of go his talk at Fordham and kind
[1309.92 → 1315.36] of dive into what we're talking about here transition to get and so much more so we'll be back in just a
[1315.36 → 1322.40] second top towel is the best place to work as a freelance software developer if you're freelancing
[1322.40 → 1327.18] right now as a software developer, and you're looking for a way to work with top clients on
[1327.18 → 1332.70] projects that are interesting challenging and using the technologies you want to use top towel might
[1332.70 → 1337.70] just be the place for you working as a freelance software developer with top towel means your days
[1337.70 → 1343.10] of searching for long-term high quality work and getting paid what you're worth will be over let's
[1343.10 → 1347.86] face it you're an awesome developer, and you deserve to be composite like one joining top means
[1347.86 → 1352.58] you'll have the opportunity to travel the world as an elite engineer on top of that top towel can help
[1352.58 → 1358.02] provide the software hardware and support you need to work effectively no matter where you are in the
[1358.02 → 1365.52] world head to top towel.com slash developers that's t-o-p-t-a-l.com slash developers to learn more
[1365.52 → 1367.10] and tell them the changelog sent you
[1367.10 → 1371.72] all right we're back the state of go in 2015
[1371.72 → 1378.32] Andrew you've kind of teed it off before we took that break there so um sorry I threw you curveball
[1378.32 → 1383.62] there too by the way it wasn't uh let me know I was going to do that but anyway so c2go you know when
[1383.62 → 1388.78] i when I read this in your talk when I now listening to your talk and reading your talk was two different
[1388.78 → 1395.52] things but whenever I heard you talk about the prep work for the c2go tool chain conversion I was like
[1395.52 → 1401.56] wow okay so they're writing and having gone back and listened to episode 100 just to kind of prep for this call
[1401.56 → 1405.22] too to kind of get back into grips with what you and Rob talked about with Andrew
[1405.22 → 1409.20] uh on the show before I was thinking man Rob's got to be excited because
[1409.20 → 1413.84] the c and c plus programs he had written 20 years ago cannot be reported to go
[1413.84 → 1420.38] and that's not the case so let's talk about the c2go tool chain conversion and what you actually mean by that
[1420.38 → 1428.98] right so you know originally when go was first being developed uh ken Thompson wrote the original
[1428.98 → 1437.48] compiler in c um which he was leveraging a lot of the work of and the design of the plan 9 c compiler
[1437.48 → 1446.16] which uh you know is just a standalone c linker and assembler, and it's nicely cross-platform
[1446.16 → 1451.12] or at least you know it was in its old form so that was just kind of an expedient way to get
[1451.12 → 1455.72] started, and it was the system that they already knew so they built it in c um, and then we've just
[1455.72 → 1463.06] kind of taken that and kept working on it for five years, and you know it got to the point where
[1463.06 → 1469.20] we have more and more people working on it, and it really wasn't an accessible code base at all
[1469.20 → 1478.32] I mean like ken is a tremendous programmer, but his code is unlike anyone else's code and I don't mean
[1478.32 → 1484.66] that in like a negative way it's not me being sort of snide about if it's just his mind actually works
[1484.66 → 1491.92] in a way that is very unusual and so you know first there's the ken factor and then there is
[1491.92 → 1497.40] you know the fact that the code had just kind of grown over a long period of time, and you know
[1497.40 → 1502.32] originally it suited us really well because we were developing a new language and making changes
[1502.32 → 1506.88] to the language and if we'd written the original compiler in go then we would have constantly had
[1506.88 → 1514.86] to sort of reboot strap and update the go compiler written in go as we change the go language and
[1514.86 → 1520.40] that would have been it would have added a lot of friction to making any kinds of language changes
[1520.40 → 1526.44] whereas you know having it in c you know we see as a language we understand hasn't changed for a
[1526.44 → 1531.76] very long time this is plain c not c plus you know we could make changes freely to the language
[1531.76 → 1536.84] without having to refactor the tool chain at the same time and so that suited us really well that's
[1536.84 → 1543.52] the project now we have so many more people working on the tool chain it's its about time that we use the
[1543.52 → 1548.84] nice stable language that we spend this time developing and so you know we made the decision to convert the
[1548.84 → 1554.72] tool chain into go so not to rewrite like if we rewrote we felt like it would just set us back
[1554.72 → 1559.68] you know you end up in second system syndrome you end up recreating the same bugs that you've already
[1559.68 → 1567.10] fixed we were somewhat hampered by not having a really thorough set of unit tests like we have a
[1567.10 → 1574.48] lot of integration tests but as a whole the sort of the compiler was more or less a black box
[1574.48 → 1580.08] we had these tests where we put stuff in and saw what came out so we decided that what we would do is
[1580.08 → 1585.96] convert the tool chain from c to go and that doesn't mean like by hand it means we actually
[1585.96 → 1592.78] well Russ cox wrote a program to convert the c sources into go, and it meant that work could continue
[1592.78 → 1601.14] on the c compiler while the trans the translator was being developed and when it was time to cut it over
[1601.14 → 1608.08] you know Russ could run the translator and check in all the go tool chain the tool chain written in go
[1608.08 → 1613.62] and then later delete the tool chain written in c and so this has actually been a really huge
[1613.62 → 1621.12] engineering project in a way, but the end result is like we now today have the go compiler written
[1621.12 → 1627.88] in go at the moment it's slightly slower than the c version because some things that you do in c are
[1627.88 → 1634.06] much more efficient in c than they are in go and vice versa, and so we're sort of gradually now we have a
[1634.06 → 1641.78] very ugly go program right because it's all written in a c style and so work is now being done to tidy
[1641.78 → 1646.94] that up and make it look more like a nice go program, and you talk about that a little bit where you go
[1646.94 → 1654.10] from c to go ugly and then go pretty well for instance you know the whole thing when you converted
[1654.10 → 1661.52] it was just one big package because c just has one uh namespace right that okay that everyone shares
[1661.52 → 1668.34] whereas go has these individual packages that each have their own namespace and so you know when you
[1668.34 → 1675.00] convert c to go you just end up with this one big package with like hundreds or even thousands of names
[1675.00 → 1681.62] inside it um and that's very that's very ugly go you know that's you would never do that if you
[1681.62 → 1687.24] were writing go from scratch, and you know all the function names are not really very idiomatic all the
[1687.24 → 1695.10] types and so on you know in the original go compiler there was one big c struct uh called node
[1695.10 → 1700.86] that represented like uh a node in the as tor a node in the generated code, and it was kind of like a
[1700.86 → 1706.52] multipurpose type that was used at different parts of the compiler and so it was this huge data structure
[1706.52 → 1715.12] which included unions um which is where you can have a struct that has the same kind of size
[1715.12 → 1720.46] but it can be used in different ways where fields can share the same piece of memory so you can only
[1720.46 → 1725.96] use one or the other of those fields simultaneously and that's not a feature that go has at all and so
[1725.96 → 1731.48] like when we converted that node type into go we had to like to explode out all of those unions and
[1731.48 → 1737.94] suddenly the nodes were so much bigger um and an interesting issue came up recently where
[1737.94 → 1741.80] I apologize if I'm getting a little bit wrong I just heard it in passing
[1741.80 → 1749.58] but in c you know you declare your variables like up front at the top of your function and then
[1749.58 → 1756.24] like reuse them and so on throughout the function and there were all these uh functions in the c the
[1756.24 → 1762.06] c version of the compiler that were very long that had lots and lots of variables and the number of
[1762.06 → 1767.44] variables like being used in there was something that you would never see in go and so the go compiler
[1767.44 → 1772.70] when it was doing registration for the function to see like which of those variables should be kept
[1772.70 → 1778.92] in CPU registers for efficiency it is just saw oh my god there's like 100 variables in this function
[1778.92 → 1785.12] I'm not going to registering anything and so this kind of like core parts of the compiler wouldn't use
[1785.12 → 1792.26] registers to do any of the work, and so they just became way slower whereas the c compiler could handle
[1792.26 → 1798.36] it fine because it was designed to cope with that and so it's just interesting uh I think
[1798.36 → 1803.40] we're going to see a talk probably at option this year that talks about a lot of this stuff so that
[1803.40 → 1809.48] should be that should be a pretty interesting talk yeah and so Russ got started on this I see the
[1809.48 → 1816.40] abstract that he has written for the overhaul is uh dated December 2013, so this is yeah like 18 months
[1816.40 → 1823.64] ago almost it's a while so this is an undertaking for sure oh yeah yeah, and you know I think Russ is
[1823.64 → 1829.02] looking forward to the compiler being more accessible to more people so that you know the responsibility
[1829.02 → 1834.92] is on his shoulders so much any more um yeah you know we have some great people that we've
[1834.92 → 1840.88] hired at Google to work on the compiler um recently and the and the runtime like garbage collector and so on
[1840.88 → 1845.62] and Russ has really been spinning up that team of people and also there are people in the community who
[1845.62 → 1850.80] are just really interested in working on this stuff and doing great work and so far they've been doing
[1850.80 → 1855.66] great work despite the fact that it's this really inaccessible c code base now that we have this go
[1855.66 → 1860.64] code base that's only going to get nicer um I'm excited to see you know what people will do
[1860.64 → 1868.04] so I guess we're sort of chicken and egg kind of in a sense because you'll be compiling go with go
[1868.04 → 1873.60] so if you don't have gone how do you compile go well what you do is you download a binary distribution of go
[1873.60 → 1881.94] and when you build go you just give it the location of that okay distribution it's the same thing as if
[1881.94 → 1888.30] you build GCC, or you know any c compiler you need a c compiler to build the c compiler I know that
[1888.30 → 1893.94] GCC actually has a pretty elaborate bootstrapping process to build itself from something very simple
[1893.94 → 1902.74] but we don't we don't have that the baseline for us is um go 1.4 so we're requiring that the
[1902.74 → 1911.42] compiler be written in go 1.4 compatible go so that if we add new libraries or um you know
[1911.42 → 1918.18] language features even though that's unlikely but if we add things in go 1.5 and above
[1918.18 → 1922.32] um we're not going to be able to use those in the compiler we're sort of guaranteeing that the
[1922.32 → 1930.36] compiler will always build with 1.4 you mentioned uh the garbage collector in there and I think that
[1930.36 → 1934.76] you got some something to mention that as well so you've got a concurrent garbage collector
[1934.76 → 1940.14] now you got new work on that that's going into the going to 1.4 can you talk a bit about that yeah
[1940.14 → 1946.08] look that'll go into 1.5 so oh sorry yeah yeah that'll be like in August yeah there's some really
[1946.08 → 1952.44] encouraging numbers sort of coming out you know they have an implementation of the concurrent
[1952.44 → 1960.22] collector so the major distinction when I say concurrent collector is between that and what is the
[1960.22 → 1966.66] garbage collector in 1.4 is that 1.4 collector is just to stop the world like mark and sweep collector
[1966.66 → 1974.12] which means that um once your program like allocates twice as much memory since the last garbage
[1974.12 → 1980.52] collection um it triggers a collection the whole program stops the garbage collector walks all of
[1980.52 → 1987.26] the data structures that are allocated and finds um data structures that are no longer like accessible
[1987.26 → 1993.92] by the application code, and then it marks all of those data structures actually does the reverse
[1993.92 → 1999.56] it marks the ones that are accessible um, and then it collects all the stuff that's inaccessible so and
[1999.56 → 2004.74] then it reallocates them and that happens quite quickly, but the program does pause while that happens
[2004.74 → 2008.98] and so it means you know the larger your heap is the more stuff you have allocated
[2008.98 → 2015.00] um the longer those garbage collection pauses will be and that can be an issue for interactive
[2015.00 → 2020.68] applications like you can imagine if you've ever played minecraft for instance you'll notice that
[2020.68 → 2026.08] after you've been running around for a while um there'll be like a few seconds where everything
[2026.08 → 2033.30] just chugs the frame weight plummets and um you know it gets kind of awful and Jacky and that's because
[2033.30 → 2041.60] the JVM is doing a big garbage collection at that point um what the concurrent collector in go
[2041.60 → 2049.88] will do is it does a lot more of the work um while the application code is running, and then it's able to
[2049.88 → 2058.00] incrementally collect uh unused memory as the by making very, very small pauses in which to do that
[2058.00 → 2064.78] so basically you're kind of smearing the larger collection over a longer period of time, and we're
[2064.78 → 2070.68] able to sort of specify an upper bound for like the longest your program will actually pause so it
[2070.68 → 2077.80] still will pause, but the size of the pauses should be um predictable that's the less yeah drastically
[2077.80 → 2083.00] less it comes at the cost of some runtime performance so because obviously if you're
[2083.00 → 2088.74] collecting at the same time as you're running the program then the program must therefore run a
[2088.74 → 2094.82] little bit slower but on balance I think you know for most go programs the net effect will just be
[2094.82 → 2102.14] a simple positive or just neutral, and then it also makes go useful for a wider variety of applications
[2102.14 → 2107.94] there are some people who have more interaction more interactive applications or applications that have
[2107.94 → 2112.44] stringent latency requirements that just couldn't go near go because of those
[2112.44 → 2117.78] but I think the 1.5 release will really make a lot more possible for a lot more people
[2117.78 → 2122.86] um and make go you know something that they can actually viably choose as opposed to
[2122.86 → 2126.24] ruled out simply because of the old garbage collector
[2126.24 → 2134.60] and you also talked a bit about the http2 server being in go is that planned for 1.5 as well or is that
[2134.60 → 2141.34] I know you got one point soon is that yeah probably not 1.5 I think the standard is the standard now
[2141.34 → 2165.68] so that's encouraging, but it's probably not ready for 1.5 it's not really battle tested or anything I'm not I'm not I'm not really sure um it could be, but it's more likely to be in 1.6 but there were so on the release cycle does that mean the following august or is that spring and sort of yeah that means like February six months later
[2165.68 → 2180.54] gotcha okay, but the nice thing is you know if you write go programs that are http servers when we do bring http2 support in they'll just become http2 servers so you won't actually have to do anything different in your application
[2180.54 → 2187.98] there's also an uh an active development repo out there from brad fits is that something that someone can
[2187.98 → 2196.46] kind of use in tandem and sort of use it before 1.6 absolutely yeah we have a demo site at http2.golang.org
[2196.46 → 2202.58] where you can, you know if you have a browser that supports it which uh at least chrome and Firefox do
[2202.58 → 2209.62] um you can see what it's like to talk http2 it also if you use Google.com or anything you're probably already using http2
[2209.62 → 2216.22] um not the go implementation of course but yeah brad if you go to GitHub.com slash brad fit slash http2
[2216.22 → 2222.22] you'll see um his sort of work in progress, and it's you know it's pretty solid it's very, very well
[2222.22 → 2228.66] tested brad's very good about writing comprehensive tests so he actually found a bunch of bugs in the
[2228.66 → 2234.14] spec and other people's reference implementations as he was writing his own implementation which is
[2234.14 → 2240.70] a sign that you're doing a decent job I think we just had uh ill Gregorio on the show not too long ago
[2240.70 → 2245.10] actually we were talking about our new nightly email we ship out this email called change lad nightly
[2245.10 → 2252.94] is actually the GitHub archive email that ilia stopped shipping started this year and uh ilia
[2252.94 → 2258.40] came on the show and said I'm an internet plumber that was his title because he was like i just i
[2258.40 → 2262.40] make the internet fast that's what I do, and he was just talking about the new spec being out there and
[2262.40 → 2267.98] it was just a few weeks back so it was like fresh and new than i think it's really cool I mean i
[2267.98 → 2274.14] think people criticize http2 because they expect it to be some because it's version two you know
[2274.14 → 2281.76] they expect it to be something amazing whereas I'm happy with just quantitatively better right that's
[2281.76 → 2290.06] that's that's i that's a great uh goal if is you can achieve that then I think you're doing well um
[2290.06 → 2296.28] and really I feel like it was the sort of the biggest incremental step we could take
[2296.28 → 2302.50] that people would viably adopt right I think some people disagree, but that's my take on it
[2302.50 → 2310.26] i if you look at the demo site which I guess you'll link to um there's a go for tiles demo where
[2310.26 → 2318.08] you get to see you know a bunch of images um loaded concurrently over http versus http2 and you
[2318.08 → 2325.88] can artificially like add latency to the requests and um http2 lets you pipeline like all of those
[2325.88 → 2332.60] requests simultaneously and so you can fire off like you know a hundred get requests down one TCP
[2332.60 → 2339.28] connection and then get all the responses back and the demo is startling and I think particularly on
[2339.28 → 2344.68] high latency connections like mobile connections it will really make the web a lot better I'm excited
[2344.68 → 2348.96] it's a perfect segue there into talking a bit about mobile we'll talk about get here in a bit too but
[2348.96 → 2355.72] let's start with talking about mobile um I know that it's some new stuff happening in 1.5 and
[2355.72 → 2362.16] you've got uh android support coming out uh or deeper android support, and you're also had plans for
[2362.16 → 2367.06] iOS support so what is the state of mobile for go right now and what are people building with go in
[2367.06 → 2374.58] mobile well I mean it's its still really nice and um you know the libraries are still very spot and
[2374.58 → 2381.04] and in flux um I'm not really aware of anyone doing anything serious with go on mobile at this
[2381.04 → 2389.70] point um but what we're hoping to have in 1.5 is a basic toolkit for writing like go programs that run
[2389.70 → 2396.32] on android and iOS so you'll be able to write the same go code that runs on either platform and you
[2396.32 → 2401.40] know there's a there's a huge amount of like grunge work involved in making this possible um which I've
[2401.40 → 2406.26] been sort of tangentially involved with um the other part of it that's really cool is we'll have
[2406.26 → 2413.52] this go mobile tool um that when you's a bit like the go tool you can just say you know go mobile
[2413.52 → 2419.94] install, and it builds your app and then uploads it to your phone, and you know if you're familiar with
[2419.94 → 2424.82] either the android or the iOS tool chains you know you know how painful that can be
[2424.82 → 2433.06] very and so-and-so you know I personally look forward to the day when I can actually do mobile
[2433.06 → 2440.40] development because I simply don't have the time to just like get into that and figure it out you
[2440.40 → 2446.20] know it would take me way more spare time than I have but I have all these great ideas about little
[2446.20 → 2451.80] games I want to build, or you know little tools you know i would be writing lots of programs
[2451.80 → 2457.98] my phone that I use all the time but I just don't have the time to actually learn how to make that
[2457.98 → 2467.08] work so yeah I'm very excited about that yes it's its funny because um over the weekend um or I guess
[2467.08 → 2471.42] this week too but over the weekend we had some family in and just a sort of side story on the
[2471.42 → 2476.30] desire to do some gaming i never really thought that I would ever have a desire to build a game but
[2476.30 → 2481.60] when I was sitting there with my niece um this is not a plug uh, and they're not paying us to say this but
[2481.60 → 2487.56] coolmath-games.com was pretty neat we went there on our on the iPad we were just sitting there
[2487.56 → 2493.12] just playing games for you know like an hour or whatever and I was just thinking like here's this
[2493.12 → 2497.22] little impressionable kid loving these games, and she doesn't realize that you can build these things
[2497.22 → 2503.68] with HTML CSS and JavaScript, and it's pretty you know some CSS animations and stuff like that
[2503.68 → 2508.48] um but going a little further to actually build an app part of it you know is what you're talking about but
[2508.48 → 2514.70] i never really had that desire to build a game yet and that was the moment where I had this moment
[2514.70 → 2520.36] where like I wish it was a little easier to jump into that or I'd sort of learn that so well I mean
[2520.36 → 2528.54] even in the web world like it's insanely complicated to understand HTML CSS and JavaScript
[2528.54 → 2533.48] you know with a lot of us have grown up in this environment, and so we've kind of
[2533.48 → 2539.70] learned, or we've written learned all the stuff we need to know to be productive in that environment
[2539.70 → 2547.86] yeah um I spent a lot of time as a web developer you know before I was at Google and I think it's
[2547.86 → 2552.54] it's astounding really the complexity that we put up with and so you know one of the things I'm excited
[2552.54 → 2562.10] about this go on android and iOS stuff is we'll have these simple toolkits for doing stuff
[2562.10 → 2568.72] like putting images and text on the screen moving them around animating them handling user input
[2568.72 → 2575.24] handling audio, and it would be a nice little environment that just works right and I know
[2575.24 → 2578.98] there are similar projects in other languages and so on goes the language I like using so
[2578.98 → 2583.68] obviously this appeals of course right but uh you have to take what's happening elsewhere and
[2583.68 → 2589.98] bring it into your camp that's how it works yeah let's take a quick break in here from one of our
[2589.98 → 2596.62] sponsors when we come back we're going to dive deep into goes transition to get from a curial uh kind of
[2596.62 → 2600.90] hear about the details behind that a lot of a lot of details shared and I got some questions for you
[2600.90 → 2605.08] there Andrew so let's take a break we'll be right back, and we'll, we'll go through that
[2605.08 → 2612.82] over 400 000 developers have deployed to digital zones cloud digital ocean is a simple cloud hosting
[2612.82 → 2618.84] provider built for developers in 55 seconds that's all the time it takes you'll have a cloud server
[2618.84 → 2624.12] with forward access, and it just doesn't get any easier than that pricing plans are super inexpensive
[2624.12 → 2630.78] just five bucks a month for half a gram 20 gigs of SSD drive space one CPU core and one terabyte of
[2630.78 → 2636.54] transfer all digital ocean servers run on SSDs that means they're blazing fast they have tier one
[2636.54 → 2641.98] bandwidth support and come with private networking use our special link to get a ten dollar hosting
[2641.98 → 2647.30] credit when you sign up head to the changelog.com slash digital ocean to get started and now back to
[2647.30 → 2654.52] the show all right we're back uh so Andrew I think it was a hot topic for you to kind of cover anyway
[2654.52 → 2659.74] which was the transition to get I know it made headlines um well it made hacking news
[2659.74 → 2666.30] that's well I mean what are headlines right it's good stuff you know it was in your talk so that's
[2666.30 → 2671.12] a headline yeah I mean in retrospect I was excited to hear this too I think everybody else was but it
[2671.12 → 2676.38] also you know in the wake of that you know how long has it been since the transition to get
[2676.38 → 2684.74] oh well a few months I guess it was December so a couple of months and so then the next question
[2684.74 → 2690.38] that came on the minds of those who follow go and obviously follow google code was like was that
[2690.38 → 2696.84] did you all know about google code or is that just by happenstance oh no like of course we
[2696.84 → 2704.98] knew um as a team because you know they're going to tell like their biggest clients about it in advance
[2704.98 → 2714.94] but like in a way um our transition to get help was kind of part of their preparing um this
[2714.94 → 2720.94] automated migration tool um that they've now given everyone access to so you know that so if you don't
[2720.94 → 2725.98] know they shut down google code and now there's this one click tool for um migrating your project
[2725.98 → 2731.04] from Google code to GitHub which you know it's pretty nice it works pretty well that's awesome yeah yeah
[2731.04 → 2736.76] and the team were really adamant that they didn't want to announce the deprecation of Google
[2736.76 → 2743.14] code until they had the plan totally worked out they had a tool that worked you know that they were
[2743.14 → 2751.56] able to make the process as painless as possible, and so we wanted to make the jump to coincide with
[2751.56 → 2759.36] the very beginning of our development cycle so our release was for the first of December or the start of
[2759.36 → 2766.58] December and um we really wanted to make the cutover directly after that and so yeah we did make the
[2766.58 → 2773.12] transition sort of motivated by the impending shutdown of Google code but really I think all the reasons
[2773.12 → 2777.40] that we gave at the time were genuine like there are a lot of good things about making the switch to
[2777.40 → 2783.44] get and GitHub and Garrett uh but yeah if is it wasn't going if Google wasn't going away maybe we
[2783.44 → 2786.92] wouldn't have done it I mean it was a tremendous amount of work, and you know nobody wants to do
[2786.92 → 2791.20] busy work that's what I'm curious though because you got some pros and cons in your list here that
[2791.20 → 2795.14] you talked about in your talk but as I was listening I'm like there's something deeper into that story
[2795.14 → 2799.60] there, and obviously we know now that google code is sunsetted so yeah there had to have been some
[2799.60 → 2804.90] reason there so you kind of throw a nugget in there of whether you may or may not have
[2804.90 → 2811.06] transitioned if google code didn't move away oh well it's you know it's just that you know I spent like
[2811.06 → 2817.88] two months of my life dealing with this problem of trying to seamlessly migrate all of our stuff
[2817.88 → 2822.50] from one service to another, and it's not something that I would have chosen to do
[2822.50 → 2829.70] like if I had an option not to torture right well it's I mean it's just it's just work that I would
[2829.70 → 2835.32] that I could have not done and right I like I don't I feel like we're in a're definitely in a
[2835.32 → 2841.84] better place now so you know I don't really feel bad about it um and i you know I respect the reasons
[2841.84 → 2847.58] for Google wanting to shut down google code I can totally understand that as well I think you know
[2847.58 → 2858.22] like chrome was um or even wave I guess was like a reason to try and shake up like you know the
[2858.22 → 2863.84] world of web browsers or the world of like online collaboration I think google code was really you know
[2863.84 → 2870.02] at the time if you remember like source forge was the thing yes yeah um and source forge was terrible
[2870.02 → 2876.66] you know so bad and google code was like just this breath of fresh air, and it made it I think it made a
[2876.66 → 2882.86] lot of people realize oh hey you know we can build better like open source code hosting sites and that
[2882.86 → 2888.94] paved the way for like GitHub and Bitbucket and other services of that nature and so you know it kind of
[2888.94 → 2894.46] it served its purpose, and you know it's its obviously no secret now that it's its not the
[2894.46 → 2900.94] place to be for open source projects now you know GitHub seems to be that place now and that's fine you
[2900.94 → 2906.14] know we don't we don't feel bad about it that's for us, it's mission accomplished there's something that
[2906.14 → 2910.66] people think is better they should be using that when google code came along that wasn't the case
[2910.66 → 2917.22] well this transition for you guys wasn't uh it was a lot of your life, but it's not a big deal for
[2917.22 → 2923.70] your it is a big deal sorry reverse uh analogy there, but it's a big deal for your contributors
[2923.70 → 2929.58] so those who actually contribute back to go or fork it and try to push-pull requests we'll get into that
[2929.58 → 2935.48] in a bit but um, but it's not so much important for go users so nothing's changing with go it's just a
[2935.48 → 2940.98] matter of yeah how you actually track versioning yeah yeah it's purely our projects' development
[2940.98 → 2945.76] process how you do things yeah and the and the know the only really like end user facing thing is
[2945.76 → 2952.10] they use the GitHub issue tracker now rather than the Google code issue tracker and that actually is
[2952.10 → 2956.70] generally better for our users because most users are more accustomed to using GitHub's issue
[2956.70 → 2963.52] tracking system something you had said um in your talk was that it was a steep learning curve for
[2963.52 → 2970.04] for coming from mercurial to git and uh you know Facebook back I think about a year and a half ago
[2970.04 → 2975.64] so I think almost last time you're on the show uh they had made a choice to move uh or choice of
[2975.64 → 2982.76] mercurial or git, and they chose mercurial for speed reasons, but you chose git do you think it's mainly for
[2982.76 → 2988.56] because of Google code obviously but then also because of GitHub in the community or is it git itself that
[2988.56 → 2996.90] attracted you I wouldn't say I'm particularly attracted to git nor am I particularly attracted
[2996.90 → 3004.34] to mercurial the main reason we switched to get is that the code review system Garrett is built on git
[3004.34 → 3014.08] and Garrett that um is partially maintained by people at Google and there is you know a team at Google that
[3014.08 → 3020.40] supports Garrett instances for Google is to use like so they use it on android extensively and you
[3020.40 → 3025.18] know if is it's developing infrastructure that is supporting android we know it's not going to go away
[3025.18 → 3030.76] like our code review system readied that we were using with mercurial um we were the were basically
[3030.76 → 3035.62] the last people maintaining the instance that we were using it used to be used by a lot of people
[3035.62 → 3041.80] and so, and we didn't really want to be in that position any more we wanted to be using something that
[3041.80 → 3048.40] was well-supported by um a team of people working full-time on making sure it works and so the Garrett
[3048.40 → 3053.22] team were already doing that for the android people and so it just seemed like a natural choice to go
[3053.22 → 3058.34] with that and there's a lot to like about Garrett it has its rough edges, but it's definitely
[3058.34 → 3064.70] a superior tool to what we were using before and so it was really Garrett that motivated the choice to
[3064.70 → 3070.74] switch to git and then once we decided to switch to git um GitHub seemed like the obvious choice for
[3070.74 → 3077.02] hosting our issues mostly it's mostly GitHub is mostly just used for hosting issues
[3077.02 → 3084.28] what uh what role does Garrett play in this process of building go and maintaining go well it's out it's
[3084.28 → 3090.10] the code review system sorry if I wasn't clear about that so um every single change that goes into go
[3090.10 → 3099.70] is reviewed and Garrett is the system that web a web-based code review system that we use to
[3099.70 → 3108.42] look at the diffs and um leave comments uh upload new revisions so they're like pull requests but the
[3108.42 → 3118.80] workflow is a lot more focused on doing detailed code review um you know I find that you know GitHub's
[3118.80 → 3125.48] pull requests are not very well suited to paying attention to all the details you know I find
[3125.48 → 3131.00] it very hard to um to sort of keep track of different revisions of a change so you know as
[3131.00 → 3135.42] you're working on something that's coming in you know you'll make changes based on reviewer feedback
[3135.42 → 3141.00] and GitHub makes it very hard to sort of see like what change from between one revision and the next
[3141.00 → 3146.96] it also you know forces you to do things like look at all the files that have been changed in one
[3146.96 → 3154.56] big fell swoop and actually probably the most crucial thing that I like about Garrett and
[3154.56 → 3159.64] the other code review tools that I've been using in the past is that when you're reviewing something
[3159.64 → 3167.92] you make a series of comments on all the code like on lines and so on and then when you're you've you've
[3167.92 → 3174.16] done the review you then send all those comments as one big atomic thing, and it comes as one mail
[3174.16 → 3179.68] message and then the the the author of the code responds to those messages whereas on GitHub
[3179.68 → 3188.32] I start commenting on the change and the author of the code is already receiving my comments
[3188.32 → 3195.38] by email like and so if I get halfway through the code and I'm saying like oh why did you do this here
[3195.38 → 3201.46] like this is confusing and then I get to like the next file, and it's like oh I totally understand
[3201.46 → 3206.90] why you're doing this now and like in Garrett I could go and delete those old comments or edit them
[3206.90 → 3214.44] but in GitHub I suddenly have to like send more comments to the author and say oh oh oh ignore my
[3214.44 → 3219.60] ignore my other comments you're like I didn't mean that I understand now meanwhile they're giving you a
[3219.60 → 3224.06] deep dive, and they're wasting their time commenting back like no I've fixed that down here, and you're both
[3224.06 → 3229.54] crossing wires yeah, and you know i think that that approach like it probably works for some
[3229.54 → 3236.28] people it probably works for people on small teams um but like I do dozens of code reviews a day and
[3236.28 → 3242.00] there are people on my team that do more, and you know it's crucial that the process be as efficient as
[3242.00 → 3249.50] possible and there are just too many inefficiencies in the GitHub way so that's that's why we didn't go
[3249.50 → 3255.66] with pull requests essentially uh that's another mention I want to mention here is why don't you
[3255.66 → 3259.46] accept pull requests we're kind of answering that so I won't ask you that directly so let's
[3259.46 → 3266.76] sort of roundabout answer that my thought is that like you use Garrett because it gives you a better
[3266.76 → 3271.82] user experience around code review accepting you know pull requests that aren't actually get a pull
[3271.82 → 3278.18] request, but you know reviewing code changes and for the reason you just mentioned there but if GitHub
[3278.18 → 3285.50] improved their pull request processes to let's say match the Garrett process let's say that became
[3285.50 → 3292.08] the new GitHub way would you stop using Garrett well I mean there are a lot of hypotheticals in that
[3292.08 → 3298.16] question right of course yeah plus you got the CLA or the yeah the CLA is involved in there so the
[3298.16 → 3303.92] contributors license agreement that is part of contributing to go yeah we actually thinks are
[3303.92 → 3310.08] happening yeah so licensing is obviously important we need to make sure that um the people who are
[3310.08 → 3317.60] contributing code actually give the project the license to use that code that's an important legal
[3317.60 → 3322.30] protection for us as a project it's important legal protection for our users as well and with Garrett
[3322.30 → 3328.74] you know you can't actually send a change until you've signed that agreement electronically um and so
[3328.74 → 3333.34] that's nice it means that if I'm reviewing someone's code it means that i actually legally am allowed to
[3333.34 → 3339.72] look at that code and submit it right on GitHub there's no sort of uh built-in support for that
[3339.72 → 3345.84] but we do have this Google bot that we can enable for projects that when a pull request comes in it
[3345.84 → 3351.20] checks whether the GitHub user has signed the CLA and so that's not actually a problem for us using
[3351.20 → 3357.62] GitHub I have a couple of projects like the code base for godoc.org the go documentation
[3357.62 → 3365.22] website um that is hosted on GitHub and I use pull requests for reviewing code because that predates the
[3365.22 → 3371.54] transition of the main project to GitHub yeah um and I use the Google bot for processing CLIS there and it works
[3371.54 → 3379.00] fine it's its great but look i could imagine like if is GitHub was able to give us a workflow
[3379.00 → 3384.12] that was I guess it would have to be better than Garrett at this point because we're not going to just change
[3384.12 → 3389.80] things again but it would definitely be preferable you know I don't like getting pull requests on
[3389.80 → 3396.26] because incidentally there's no way to disable pull requests on GitHub so like you can't opt out you
[3396.26 → 3401.68] can't opt out and i I don't like having a contributor send a pull request and me having to say I'm sorry
[3401.68 → 3406.34] we don't take pull requests that yeah that's a bummer too I almost feel like there should be like if you're
[3406.34 → 3413.14] not gonna not so much turn them off but point them elsewhere yeah you know so like if someone forks it
[3413.14 → 3417.34] and sends a pull request or wants to go through the process rather than going through the GitHub way
[3417.34 → 3422.46] it points to say a different public URL through Garrett or something else that still gives you the
[3422.46 → 3429.18] same abilities just not using native GitHub yeah I mean I would love if is anyone from GitHub listening
[3429.18 → 3434.78] you know there are a lot of small things that could be done to provide essential information to
[3434.78 → 3442.80] contributors early like if you put a contributing.md file in your project root when a user goes to file an
[3442.80 → 3448.08] issue they see a link at the top that says please read the contribution guidelines before filing an
[3448.08 → 3453.22] issue and that's that's nice I would actually prefer it if they just showed the contributing file
[3453.22 → 3461.56] you know on the issue filing page because our contributing file is very simple, but it says like
[3461.56 → 3466.90] for instance if you're filing an issue report please tell us these essential pieces of information
[3466.90 → 3473.76] and you know on Google code we actually had a template you know it would say what version of go are you
[3473.76 → 3478.46] running what platform are you running on what did you see what did you expect to see you know what did
[3478.46 → 3484.36] you do this kind of like these five essential questions and not having that template in the issue
[3484.36 → 3490.72] tracker means we get less informative bug reports, and they require more handling and more follow-up
[3490.72 → 3497.82] which means that they're less likely to get addressed and with the pull request thing as far as I'm aware
[3497.82 → 3503.50] the contributor doesn't get shown that that link to the contributing doc when you create a pull request
[3503.50 → 3509.50] and you know the essential line in that doc is we don't take pull requests here's the contribution process
[3509.50 → 3517.52] and so you know I feel like if GitHub would just surface that contributing file more readily in these
[3517.52 → 3523.86] processes we could really uh you know reduce the double handling that happens for a lot of these issues
[3523.86 → 3529.38] and reduce frustration because I think you know our contributors they want to contribute in the way that works
[3529.38 → 3535.98] for the project you know um nobody wants to be doing the wrong thing um but I think it's frustrating
[3535.98 → 3541.76] and you know upsetting to people when they think they're doing the right thing by sending a pull request
[3541.76 → 3547.32] and then they're told sorry that's that's not the way we do things, and they can't be faulted for not
[3547.32 → 3553.82] knowing that but at the same time as you know I get tired of telling people the same thing as every
[3553.82 → 3561.52] every day or two I think it's its surprising though when you have a disclaimer saying we don't accept pull
[3561.52 → 3567.66] requests I think you got to put a parentheses there and say kinda no it's its not exactly true there's
[3567.66 → 3574.80] some steps that require like the CLA being signed to hand the rights over to the project and whatnot
[3574.80 → 3579.66] so I think it's just kind of funny that you said you know we don't accept pull requests, but it's not
[3579.66 → 3585.90] it's not exactly true well no it is strictly true because we accept contributions, but they're not
[3585.90 → 3591.74] in the form of pull requests right yeah I think I almost feel like those are
[3591.74 → 3597.64] interchangeable terms to a degree I mean I know GitHub coined the phrase but because open source
[3597.64 → 3604.30] is becoming more and more in the public's eye GitHub is the place where people think open source
[3604.30 → 3610.90] happens you know so to the untrained hacker eye or developer eye trying to erase hacker from my
[3610.90 → 3617.54] my lingo because it's just not inclusive I want to be inclusive everybody um but anyway you know to
[3617.54 → 3622.34] the untrained developer eye everyone else thinks that GitHub is sort of the epicentre which it
[3622.34 → 3628.02] you know reasons you're there too with uh with go is that it's become the place where the community
[3628.02 → 3634.46] is and so to send a pull request is like saying I contribute and so that sort of becomes the
[3634.46 → 3639.96] somewhat interchangeable terminology at least in my opinion well you know i just hope that
[3639.96 → 3644.74] GitHub takes the feedback from people like us, and you know we're definitely not alone there's a lot of
[3644.74 → 3652.58] people who have similar issues with you know their pull request system and i I hope that you know they
[3652.58 → 3658.22] take this on, and you know being the kind of de facto centre of the open source world I think they have a
[3658.22 → 3663.72] responsibility to respond to these kinds of requests, but you know ultimately they are a business and
[3663.72 → 3671.66] personally I don't believe that um it's healthy for everyone to have this kind of dependence on
[3671.66 → 3676.42] one large business and obviously working for Google that might sound somewhat ironic coming out of my
[3676.42 → 3682.96] mouth but yeah a little bit, but you know I feel you I know what you mean i I am a big fan of running
[3682.96 → 3688.34] your own infrastructure um I think it makes sense to use infrastructure provided by other people where it
[3688.34 → 3693.70] makes sense, but you know I'm a contributor to brad Fitzpatrick's Cayley store project which is
[3693.70 → 3701.84] all about reclaiming control of your content, and you know you could, it's a storage system for things
[3701.84 → 3709.16] like photos or basically any kind of files or anything, and you know you can run it on cloud
[3709.16 → 3718.22] storage or s3 or whatever, but you can also run it on a server in your basement, and you can do both
[3718.22 → 3723.34] you can synchronize it between both things and I think it's you know I think we need to build
[3723.34 → 3731.56] systems that break our dependence on large organizations and so yeah I mean I hope people
[3731.56 → 3738.06] don't forget that git is not GitHub you know git is an open source tool that anyone can use to host
[3738.06 → 3744.42] source code anywhere um and I hope people don't you know I hope it's not quite true what you say about
[3744.42 → 3750.72] people thinking GitHub equals open source because um well I don't think that exactly means it
[3750.72 → 3755.20] equals, but you know when they think open source they think well is it on GitHub oh then it's not
[3755.20 → 3763.36] open sourced you know that's that it is not the truth but to the untrained eye it is starts to become
[3763.36 → 3770.76] truthy because anything that's happening around open source tends to be pointed back to some sort of
[3770.76 → 3779.12] GitHub.com slash URL yeah I mean like kudos to GitHub for building something people really love um
[3779.12 → 3786.14] and I think they've done a great job but i I think it's really important particularly in the open source
[3786.14 → 3793.02] community for everyone to remember to be self-reliant you know I think that's that's a really valuable
[3793.02 → 3798.96] thing, and it's kind of a core tenet of what open source is about let's talk a bit about uh
[3798.96 → 3803.28] we don't have much more time here we got maybe like eight minutes flat probably less than
[3803.28 → 3809.86] that since we've actually gone over time a bit but let's talk about uh go 1.5 is releasing uh
[3809.86 → 3816.30] august August 2015 with your new release cycle uh no c code will be in 1.5 you've got some new
[3816.30 → 3824.86] architectures supporting power pc 64 and maybe the arm 64 now when I saw this forgive me but the question
[3824.86 → 3830.60] I asked myself was what types of machines are running on power pc 64 and arm 64 because I guess
[3830.60 → 3834.94] i just never think about what my machine is running I write my back book and whatever they
[3834.94 → 3841.12] give me i just you know uh I just use it yeah no I know it's not power pc because they went to
[3841.12 → 3847.86] intel until a while ago but so what is the power pc 64 and arm 64 uh architectures right so places
[3847.86 → 3854.92] a consumer would see um is obviously phones um and arm 64 the big arm 64 platforms is the iPhone
[3854.92 → 3866.42] so everything from the 5s up is an arm 64 processor okay and um I think apple won't actually let you run
[3866.42 → 3875.42] 32-bit processes on some of the newer iOS versions on the arm 64 processes so for this go mobile stuff to
[3875.42 → 3881.60] work you know we need to we need to target arm 64 so that that's what arm 64 is about um there are
[3881.60 → 3886.66] probably some people doing um processes in this in the server environment but I'm not really aware of
[3886.66 → 3892.66] them power pc 64 is something I don't have a lot of visibility into but I know that you know there
[3892.66 → 3898.50] have been contributors from um companies like canonical who are pushing that support as well as
[3898.50 → 3904.16] other people in the community and people from Google you know power pc is is is an IBM
[3904.16 → 3914.56] processor architecture and um so I think the power pc 64 machines are very, very high spec multicore
[3914.56 → 3922.78] server machines and so the kind of processes that you wouldn't have much to do with as like
[3922.78 → 3928.42] an average developer um but I think it's its possible that we'll see them making inroads into the
[3928.42 → 3932.80] server market I'm not really I don't really have a lot of visibility into it but I think it'll make some
[3932.80 → 3941.04] particular sort of enterprise and customers happy and if you're trying to supplant java then you've
[3941.04 → 3948.20] got to do that right yeah I mean you know the go tool chain has been a cross-platform thing since
[3948.20 → 3955.04] the very beginning um and part of the rewrite actually has made it much, much easier to support
[3955.04 → 3961.98] other platforms like the actual uh architecture dependent part of the tool chain has gotten smaller and
[3961.98 → 3968.66] smaller over time, and now it's actually quite small so we just want to support go everywhere
[3968.66 → 3974.36] that we can um and if there are people willing to help contribute that support then we'll happily
[3974.36 → 3980.08] help them do that let's talk about the builder infrastructure real quick I know we don't have
[3980.08 → 3987.28] much time but I was really impressed by go mode and google compute engine so talk a bit about the
[3987.28 → 3992.06] the uh google compute engine and go mode what you were doing there that was pretty amazing
[3992.06 → 3998.76] right well, so the basic backstory is you know since go is so cross-platform we need to test it on all the
[3998.76 → 4005.76] platforms that we support and so you know we have this sort of homespun builder infrastructure um that
[4005.76 → 4011.40] you know we have a build dashboard, and we have these machines like this heterogeneous array of
[4011.40 → 4018.44] machines that are all around the world like macOS machines Linux and free BSD net BSD open BSD plan 9
[4018.44 → 4026.94] windows and all these machines run this go binary that like fetches our latest revision of go builds
[4026.94 → 4032.30] it runs all the tests reports the results back to the dashboard, but you know maintaining this array of
[4032.30 → 4040.08] machines is total pain right it's it's their all different they all work differently they're all owned by
[4040.08 → 4046.02] different people um you have to like email someone when something goes wrong and then if you have a
[4046.02 → 4051.02] problem on a particular architecture you know you need to um get access to one of the builder machines
[4051.02 → 4057.90] to be able to actually test your code on whatever that processor and architecture is but so brad Fitzpatrick
[4057.90 → 4064.32] mostly and a bit me have been working on some new builder infrastructure that uses compute engines so
[4064.32 → 4071.26] for all the all the operating systems that we can, we're running those on virtual machines on
[4071.26 → 4076.32] compute engine, and so we have this kind of like deterministic build environment that we can spin up
[4076.32 → 4082.88] at will and so we can do many more builds in parallel than we could before and also now we can do
[4082.88 → 4089.62] we can do speculative builds so if someone sends a change we can run uh the TRI bot on it as we say so
[4089.62 → 4094.96] you get to see whether the change builds before you actually merge it into the tree and so that's
[4094.96 → 4101.06] been really nice um currently works for like windows Linux uh FreeBSD and a couple of others
[4101.06 → 4108.18] um but uh we look forward to doing something similar with macOS it'll be a little bit different since we
[4108.18 → 4113.80] can't run that on compute engine but we have plans for how that might work um but a nice side effect
[4113.80 → 4117.94] from that is we have this tool called go mode where if you're a go developer and you see that your
[4117.94 → 4125.60] change breaks on like open BSD um you can spin up an open BSD instance on compute engine with just one
[4125.60 → 4132.40] command line invocation and then you know push your local changes to that machine run them see what
[4132.40 → 4137.56] happens and you know you get to actually sort of develop on the architecture that you're trying to
[4137.56 → 4143.64] support and then you don't have to actually have a bunch of VM sitting around or actual machines if
[4143.64 → 4147.48] that's the route you choose to go if you're a developer for go then this makes it a little
[4147.48 → 4152.46] easier to yeah sort of build you know write code for many but uh not have to actually own those
[4152.46 → 4157.36] machines yeah the one of the really nice side effects is uh we'll be able to make this available
[4157.36 → 4164.58] to go programmers in general um, so this will be free to anyone who's developing for go yeah yeah
[4164.58 → 4173.92] so you can just like um plug in your own google uh cloud project uh credentials, and then it will spin
[4173.92 → 4180.66] up instances on that you know that you pay for um, but you only have to pay for like you pay by the
[4180.66 → 4187.86] minute um so it's pretty much something maybe yeah yeah probably less even for an hour or something
[4187.86 → 4193.26] but um so it means that if you're a go programmer, and you know you want to test your stuff in other
[4193.26 → 4198.70] places um you should be able to do that pretty easily and also I think it's just a nice kind of
[4198.70 → 4204.06] demo of cloud orchestration stuff, although you know there are a lot of tools in that sphere
[4204.06 → 4210.14] um I don't necessarily recommend writing tools like this for us, it was kind of an experiment to see
[4210.14 → 4215.94] how our cloud libraries were in ways in which we can make that better um because obviously you know
[4215.94 → 4220.14] the go team here at Google we have a close relationship with the cloud team at Google, and we're very focused
[4220.14 → 4226.62] on trying to make um you know go the best language to use on Google's cloud platform and also other cloud
[4226.62 → 4233.08] platforms and so you know we've we've found a lot of weak points things that we want to improve
[4233.08 → 4240.50] um, and you know part of building this project was uh was just seeing how good our offerings are you
[4240.50 → 4243.90] know we're pretty happy with it, but obviously you know we find things that we want to improve and
[4243.90 → 4249.62] we're working on those too all right last question before we go into a couple of closing questions
[4249.62 → 4254.72] which are really short but I can't let it go without asking this question which is you've been here
[4254.72 → 4261.06] twice now was it has it been three times you've been no it's been twice rob was on way back when
[4261.06 → 4266.26] then you were back with rob on episode 100 and then now you're back here for episode 148, and it's been
[4266.26 → 4273.40] a year and a half since you've been on the show so what is the future for go like you got this last
[4273.40 → 4279.92] you know 1.4 to 1.5 we're shipping later this year what beyond that where are you seeing past like
[4279.92 → 4289.58] 1.6 or beyond I really think you know as far as like the go core is concerned you know it's going
[4289.58 → 4294.30] to get faster it's going to run in more places it'll be more efficient you know better optimization in the
[4294.30 → 4302.44] compiler optimization in the libraries you know improvements to the tool chain maybe you know
[4302.44 → 4309.80] some new sort of developer tools that kind of thing but i I think that you know the most exciting
[4309.80 → 4316.60] developments around go are really in the greater go community and actually one thing that I'm involved
[4316.60 → 4323.94] in is a project called go kit which a guy called peter boron from SoundCloud
[4323.94 → 4331.32] has initiated, and it's an open source project that's basically trying to build a standard
[4331.32 → 4339.32] library for building distributed systems so it's kind of described as like a toolkit um the purpose
[4339.32 → 4346.70] is you know if you want to build distributed systems in go so a lot of a lot of the the cloud
[4346.70 → 4353.88] services that people build are basically distributed systems and there are or people often call them
[4353.88 → 4359.58] like microservices you know you have um many services to talk to each other via RPC systems
[4359.58 → 4363.06] if you know what I'm talking about then you know what I'm talking about but basically
[4363.06 → 4372.02] basically um go kit is trying to define like a set of things that people need to build these kinds
[4372.02 → 4380.22] of systems and then provide like a canonical sort of set of recommendations or even like libraries
[4380.22 → 4387.66] and interfaces that you know various tools and libraries can satisfy so that you know you can
[4387.66 → 4392.74] have a well integrated developer experience for building distributed systems in go so that's that's
[4392.74 → 4397.68] kind of like the goal you should check out Peter's talk um go in the modern enterprise which he gave at
[4397.68 → 4403.76] FOSDEM uh for we're linking that up in the show notes so yeah we'll definitely have that talk in
[4403.76 → 4408.22] there yeah you know speaking of go kit we were actually wanting to have peter on the show but I wanted to
[4408.22 → 4413.56] have him on after we talked to you to kind of get an update on where go has been at for the last
[4413.56 → 4417.48] year and a half and what you've been doing so I wanted to have you on there and I didn't know you
[4417.48 → 4421.36] were working with peter on this so it might make sense to have you back on with peter if that's the
[4421.36 → 4426.20] case yeah well when i you know when I saw his talk it really I was like oh my god you know he's just
[4426.20 → 4431.00] really clearly articulated a lot of the same things that I'd been feeling about go you know we really
[4431.00 → 4438.12] need to focus on making this work um he called it like the modern enterprise which is sort of these
[4438.12 → 4446.38] you know medium-sized companies that are building you know these distributed systems um and i I feel
[4446.38 → 4451.38] like go is a great language for those companies but they we really need to focus on making it
[4451.38 → 4455.86] clearer and easier for people to make the right choices when building this kind of systems
[4455.86 → 4460.96] and also I think there are a lot of people in the go community working on these problems, and we've
[4460.96 → 4465.82] actually seen it with go kit you know when it was announced a lot of people joined the go kit project
[4465.82 → 4471.22] and they were like oh I've been working on x and the number of people that had kind of all been
[4471.22 → 4476.26] working on the same x in parallel it's like oh we should just focus those energies together
[4476.26 → 4483.18] on the one thing and so you know there's a RFC process in go kit where you know we take
[4483.18 → 4491.02] um comments from everyone and um trying to arrive at some kind of consensus, and so I'm really excited
[4491.02 → 4495.54] um for how this is going to turn out i think it's really promising um Pete is a really
[4495.54 → 4502.30] sharp guy I really appreciate his sort of thoughtfulness and also his taste I think his taste
[4502.30 → 4509.34] aligns very much with the taste of the go project and sort of what that's all about so I feel like
[4509.34 → 4515.84] that element of go's community is sort of in good hands with him and that project and so yeah I've
[4515.84 → 4525.14] been I've been trying to contribute I wrote a API stability policy which is sort of centred around
[4525.14 → 4530.00] sort of versioning package management side of things but um i I think you I think you should
[4530.00 → 4533.78] definitely get peter on the show and talk to him because it's always interesting to listen to
[4533.78 → 4541.62] we definitely do I know we cover that in uh in our weekly email I'm not sure which one but we
[4541.62 → 4546.90] share so much stuff in changelog weekly that it's just hard to even remember what we shared when but
[4546.90 → 4551.54] I know we covered go kit because I was pretty impressed with that and especially knowing
[4551.54 → 4555.52] that I wanted to have this conversation with you and sort of actually that same question which is you
[4555.52 → 4560.58] know what can programs anticipate for, and he coined it pretty well which is the modern enterprise but
[4560.58 → 4567.20] the workplace you know so if you're anticipating there's a plant java and those kinds of you know
[4567.20 → 4574.10] those kinds of projects in enterprise now and go is going to take over that then uh you know go kit
[4574.10 → 4580.74] makes sense totally all right well definitely would you be interested in coming back on the show to
[4580.74 → 4585.10] with peter or is that something I should have peter come on his own I guess you should ask him
[4585.10 → 4592.10] I would be more than happy to do it got you um okay so let's let's close out the show then I got a
[4592.10 → 4597.88] couple questions for you to close out the show some that are uh typical that we like to ask and then uh
[4597.88 → 4604.58] that's that's how it goes but um one of our favourites, and it certainly helps so you can kind of answer
[4604.58 → 4610.76] this as deep as you'd like to its kind of one part which is how can someone step into
[4610.76 → 4617.56] the go project either it's learning go or it's contributing back to go or supporting the efforts
[4617.56 → 4621.32] that you're doing and the rest of the team's doing, although they may not be googled employees
[4621.32 → 4627.24] but how can one be uh an open source contributor so what's a good way for someone to step into go
[4627.24 → 4633.80] where are some needs in the go community right now that people can step into i really my general
[4633.80 → 4639.52] recommendation when I'm asked this question it's just to you know solve problems that matter to you
[4639.52 → 4646.04] and then share those solutions because programming languages is way at the bottom of the stack
[4646.04 → 4654.26] and so everything that happens above there in that language helps that language and so you know if you
[4654.26 → 4661.04] want to sort of get involved with go you just need to start using it, and then you know sharing what
[4661.04 → 4665.52] you've learned or what you've made um and that just helps everyone
[4665.52 → 4671.76] all right that's a good that's definitely a good answer, and you know i actually i kind of lied it's
[4671.76 → 4676.80] two more questions but one's really easy for you um this one maybe not so much but definitely a good
[4676.80 → 4681.96] answer I'm hoping from you which is uh you know what's in your open source radar I can imagine that
[4681.96 → 4688.04] go is completely your radar but lets you know whichever direction you want to go but if you had a
[4688.04 → 4692.34] weekend clear, and you didn't have anything planned, and you were like I'm going to hack on something
[4692.34 → 4697.60] what would it be would it be gone or would it be around go there's a project that I've been working
[4697.60 → 4703.18] on for an embarrassingly long time that I've been neglecting lately um which is called Sigourney it's a
[4703.18 → 4712.22] it's an audio synthesizer uh yeah it's its it's a modular synthesizer so you know you it's similar
[4712.22 → 4719.70] to environments like uh max MSP or pure data that that people may have used um but basically I have a
[4719.70 → 4726.96] an actual physical modular synthesizer which is a you have various modules that like produce
[4726.96 → 4733.98] waveforms and then filter them, and then you know multiply them and so on, and you connect the modules
[4733.98 → 4739.14] with patch cables like actual physical patch cables, and then it makes sounds that some people might
[4739.14 → 4745.50] describe as music and um you know I wanted something similar because I travel a lot I wanted something
[4745.50 → 4751.42] similar when I'm travelling around and I also wanted to learn about digital signal processing and so
[4751.42 → 4757.48] I started sort of building this thing from first principles made a lot of progress pretty quickly
[4757.48 → 4763.26] um but then I've kind of stalled on it so definitely if I had some free time and probably more importantly
[4763.26 → 4768.50] some like free space in my brain to think um i would probably hack on that
[4768.50 → 4775.26] kind of reminds me a little bit of this thing we covered uh a while ago which has probably changed
[4775.26 → 4785.12] its name since but um i think it pronounced it Kiev host k-i-e-v oh yeah k-i-e-v-l-l host
[4785.12 → 4792.32] if that rings a bell to you yeah it's like a know digital audio uh workstation kind of thing and
[4792.32 → 4797.38] it does similar stuff where you connect different things and patch things together it's uh it's pretty cool
[4797.38 → 4806.02] there's a lot of amazing work being done in like the electronic music making uh world you know
[4806.02 → 4811.24] there's an it's a huge cottage industry people making both hardware and software so it's really
[4811.24 → 4817.44] exciting time to be doing that kind of thing, and you know uh I might gazump your last question now
[4817.44 → 4822.96] if I recall correctly like what would I be doing if I wasn't working on go um yeah and the answer is
[4822.96 → 4830.44] you know I would definitely be working in audio hardware and software so speaking of audio um you
[4830.44 → 4835.16] would like to hack on that if you weren't working on go what's one of your favourite podcasts you want
[4835.16 → 4844.60] to mention here on the show um so yeah my friends mike Bernstein or Mr and Aaron quint um they do a
[4844.60 → 4853.04] podcast called beats rye and types, and it's about music uh like food and drinks and uh programming
[4853.04 → 4859.62] languages and programming in general and um yeah they're just a couple of like a couple of guys
[4859.62 → 4866.14] from you know the east coast of the states I feel a great affinity to them as people so like
[4866.14 → 4872.90] listening to them talk about all these topics that I'm very interested in is uh it's always entertaining
[4872.90 → 4881.68] absolutely I got uh obviously I have a bug for audio so, and you mentioned that you might want
[4881.68 → 4888.38] to do a podcast so if you're a listener, and you were you know stuck on that give him a give Andrew
[4888.38 → 4892.96] props on Twitter yeah I don't know if people think that I should do a podcast you should tell me and
[4892.96 → 4897.46] that'll make it more likely I started doing these screencasts with brad Fitzpatrick called
[4897.46 → 4902.64] hacking with Andrew and brad um and that arose because you know I thought
[4902.64 → 4909.50] you know what i should stream some programming sessions, and you know people like
[4909.50 → 4913.10] the response on Twitter was overwhelming they were like hey you know yeah I've watched that that'd be
[4913.10 → 4919.02] great and so you know brad and eventually brad and I got together did one got some great feedback
[4919.02 → 4924.66] and then we just did a second one not that long ago, and we're looking forward to doing another one
[4924.66 → 4928.74] soon is there a list of those somewhere because I'll link it up on the show notes if there is yeah if
[4928.74 → 4936.16] you go to YouTube.com slash go coding okay um there's a there's a playlist of those two videos
[4936.16 → 4940.82] which obviously we'll add more to when we make them nice all right we'll link this up in the show
[4940.82 → 4946.32] notes for sure well I know that I've taken you much longer than I expected as a matter of fact my clock
[4946.32 → 4954.52] says we're 29 29 minutes over time, so thank you for not getting angry and if you're a listener and
[4954.52 → 4958.84] you're still listening right now thank you for listening all the way to the end it's kind of
[4958.84 → 4962.60] hard sometimes though when you come into a conversation that's about the state of go and
[4962.60 → 4967.22] there's a lot to talk about we did have a little bit longer intro than I thought we would have but
[4967.22 → 4970.92] you know hey that's that's how it works out sometimes I'm just glad you're a good sport with
[4970.92 → 4974.42] it, and you're not upset, but you are almost getting kicked out of the room so
[4974.42 → 4980.98] I'm happy always happy to talk about that all right Andrew well lets uh let's say goodbye to
[4980.98 → 4984.46] everybody, and thanks for coming on the show today man I appreciate it yeah, thanks for having me
[4984.46 → 4984.76] bye
[4984.76 → 4984.98] you
[5010.98 → 5011.48] you
