[0.00 → 22.36] welcome to changelog and friends a weekly talk show about the joy of missing out big thanks
[22.36 → 29.54] as always to our partners at fly the public cloud built for developers who ship learn all about it
[29.54 → 32.98] at fly.io okay let's Kaiden
[32.98 → 48.62] well before the show I'm here with jasmine chassis from sentry jasmine I know that session replay
[48.62 → 54.98] is one of those features that just once you use it, it becomes the way how widely adopted is session
[54.98 → 60.64] replay for sentry I can't share specific numbers, but it is highly adopted in terms of if you look
[60.64 → 66.20] at the whole feature set of sentry replay is highly adopted I think what's really important to us is
[66.20 → 72.54] sentry supports over 100 languages and frameworks it also means mobile so I think it's important for
[72.54 → 78.12] us to cater to all sorts of developers we can do that by opening up replay from not just web but
[78.12 → 81.92] going to mobile I think that's the most important needle to move so I know one of the things that
[81.92 → 88.86] developers waste so much time on is reproducing some sort of user interface error or some sort of
[88.86 → 94.86] user flow error and now there is session replay to me, it really does seem like the killer feature
[94.86 → 101.16] for sentry absolutely that's a sentiment shared by a lot of our customers, and we've even doubled down
[101.16 → 106.78] on that workflow because today if you just get a link to an issue alert in sentry an issue alert for
[106.78 → 111.98] example in slack or whatever integration that you use as soon as you open that issue alert we've
[111.98 → 117.12] embedded the replay video at the time of the error so then it just becomes part of the troubleshooting
[117.12 → 121.56] process it's no longer an add-on it's just one of the steps that you do just like you would review
[121.56 → 126.66] a stack trace our users would just also review the replay video it's embedded right there on the
[126.66 → 132.92] issues page okay sentry is always shipping helping developers ship with confidence that's what they do
[132.92 → 137.50] check out their launch week details in the link in the show notes and of course check out session
[137.50 → 142.82] replays new edition mobile replay in the link in the show notes as well and here's the best part if
[142.82 → 148.88] you want to try sentry you can do so today with a hundred dollars off the team plan totally free
[148.88 → 157.74] for you to try out for you and your team use the code changelog go to sentry.io again sentry.io
[157.74 → 182.26] well Gerhard did you create a slideshow for us, I did do you want to see it I absolutely want to
[182.26 → 188.92] see it all right let me screen share it this is you chaining our Kaiden episodes with slideshows
[188.92 → 193.20] of course you have to have them it just makes things so much more interesting I haven't posted
[193.20 → 203.08] the last one but I will do this time okay see screen window boom boom there you go Kaiden 17 oh man
[203.08 → 208.90] I feel like it's a nice font what's that font I'm not sure let me double-check I think this is a
[208.90 → 217.00] default one at the template has I like the one San Francisco it's inter i-n-t-e-r inter
[217.00 → 224.50] interesting okay inter is cool I've used that font i am presenter i am presenter been loving their stuff
[224.50 → 231.32] i am writer I've been using it for seven eight years so i am presenter is this is i a presenter okay
[231.32 → 237.70] yeah I love like how they write about it and like the whole idea behind it so it's nice and simple
[237.70 → 242.62] and I can knock these out so quickly love it well take us on a ride Gerhard you know your
[242.62 → 250.68] your magic carpet ride of Kaiden cool okay well the big thing or the main thing should be the main
[250.68 → 256.48] thing so I was thinking we should start with the main thing if Adam is ready for it, I'm ready for it
[256.48 → 261.54] always be ready we're ready for it Gerhard okay what's the main thing well you tell us I don't
[261.54 → 268.90] I'm making it too oh you're talking about cpu.fm and the change we're making oh yes this is good
[268.90 → 277.06] stuff so there's a very famous person his name is newton at least sir Isaac and Isaac Newton sir
[277.06 → 284.40] Isaac Newton, and he said to go to paraphrase him and to paraphrase a very awesome movie humans the
[284.40 → 289.20] only one they've found to move forward in life or to get somewhere is to leave something behind
[289.20 → 299.68] and so as part of that idea and mantra we have decided to change things in 2025 to focus solely
[299.68 → 305.58] on making this podcast you're listening to right now the single best developer podcast experience
[305.58 → 312.50] news on Monday interviews on Wednesday Fridays on the weekend or on Friday mostly and uh that's gonna
[312.50 → 316.28] be some fun stuff so that's what we're doing some of our favourite shows are going away
[316.28 → 325.64] transitioning moving on spin offing continuations but that's what we're doing what do you think was
[325.64 → 332.74] this a shock to you, it makes sense it was I was surprised when it when you know we talked about it
[332.74 → 339.30] honestly I could see it coming I mean it just makes sense it resonates with you know how I like to
[339.30 → 345.50] approach things, and it just fits with that mentality double down on the thing that you enjoy doing the
[345.50 → 352.38] most and the thing that you know I think makes you special yeah because this is what makes you special
[352.38 → 357.86] I think on that note though we really enjoyed producing go time JS party ship it and practically
[357.86 → 363.28] like we loved the people the shows like jerry will tell you because he hasn't spoken about it yet
[363.28 → 370.40] at least in this podcast we really deliberated over this for a while I would say so long that it's
[370.40 → 378.62] it's probably at least a year or more of considering how to change to get to where we're trying to go
[378.62 → 386.88] and it was a struggle because it's not easy to retire something move on from something
[386.88 → 395.50] to give someone or an entire world of audience bad news and that's not something that you do quickly
[395.50 → 401.50] or lightly you do it with intention and precision and even than even when you do it precisely and with
[401.50 → 407.02] with precision and intentionality it's still hard to get it right you know and so there's no really
[407.02 → 414.56] good version some will be upset and that's that's how it goes I guess, but our intention is to love well
[414.56 → 420.60] and to love the hosts and panels we work with for many years very well and to ease this process of
[420.60 → 426.80] them either spinning off something to do their own thing which almost every show has some version of
[426.80 → 434.72] continuation actually every one of them does JS party is uh has a new show called dysfunctional.fm
[434.72 → 443.22] nick cabal Amy go time has its own spinoff called fall through.fm Chris IAN and more extended friends
[443.22 → 451.66] from our existing podcast family of people who listen uh ship it has its own spinoff called fafo.fm
[451.66 → 456.74] fork around and find out cool love that Justin and autumn and then practically either keeping their
[456.74 → 462.20] name because Chris and denied are unique we've been working with them for many years probably the
[462.20 → 467.94] the longest running show, and independently they had no other panellists it was just those two yeah just those
[467.94 → 474.30] two for many years, and you know it's just uh it's a labour of love to produce these shows it's an it's a
[474.30 → 478.94] treadmill in the media world, and we've been doing this for 15 years it's not like we've been doing
[478.94 → 487.10] this for a day you know we've got some reps under our belt you know we're sole so to speak in
[487.10 → 492.94] the podcast world it's its funny to say out loud, but we've been doing this for a while and I think just
[492.94 → 499.90] having a chance to sort of pause for a moment and think about okay to produce a perfect podcast
[499.90 → 506.24] that has a video first production workflow to do that even for this show that produces three shows
[506.24 → 512.02] a week we have no more bandwidth to do it we would only be able to do that if we scale the team or if
[512.02 → 517.04] we just didn't do it, and we haven't done it for many years you go on YouTube, and you have clips only
[517.04 → 522.58] which is great but people have been asking us for years can I get the full show on YouTube the full
[522.58 → 529.04] video show and I think we've there's opportunity cost they're not doing it we've missed out on
[529.04 → 536.76] audience growth connection you know more in-depth content etc and the only way to get there really is
[536.76 → 546.56] to make a major change that's what we did but I think cpu.fm is a big vision burgeoning new idea
[546.56 → 552.52] that hasn't does have the full fruition yet, but it has a big vision so I think what we'll do
[552.52 → 559.12] to support these shows and to support this change law podcast universe that's why it's called cpu.fm
[559.12 → 566.68] I think it has big opportunity, and so I think if people continue to trust us join cpu.fm let us
[566.68 → 572.66] support them, but they produce their own shows we're no longer part of the media machine they are where
[572.66 → 579.36] we're helping them ship shows daily weekly that's a tough one it's arduous yeah I think that the
[579.36 → 587.60] end result of this there's a very real possibility that this change while it effectively takes away
[587.60 → 595.52] shows in the short term I think it actually might result in better developer pods down the road
[595.52 → 603.06] because we had reached our capacity and for many years we've turned down ideas and opportunities
[603.06 → 609.84] because we are just maxed out I mean how many times has a listener requested a podcast from us
[609.84 → 618.02] about rust probably a hundred maybe slightly less but many many many times and I hate that I don't hate
[618.02 → 623.24] it but I like I have an internal anxiety about that request because it's like I just knew I couldn't do it
[623.24 → 629.90] we couldn't do it under our current structure now there was another option like we could grow our
[629.90 → 637.26] business we could grow our team we could build out that way and I think a large part of life is
[637.26 → 642.30] knowing what you want and I've lived long enough to know that I didn't want to do that I don't think
[642.30 → 646.78] Adam wanted to do that, and so we just that wasn't an option for us just because we just don't want
[646.78 → 655.94] that to be our life and so the other option is either stay at capacity five shows a week technically
[655.94 → 662.08] it's like seven shows a week because the change log is three episodes a week and live that life and
[662.08 → 668.70] make those shows, and we did that for a long time and that was a totally legit route or double down
[668.70 → 674.96] on the main thing let a few of the things that we love to go and see if their love returns to us tenfold
[674.96 → 680.34] now that's just the corny saying about if you love something let it go right encourage the people who
[680.34 → 687.46] have been making those shows with us to make same or similar or new shows that we could support them
[687.46 → 695.72] but independently as their own thing so they could have full ownership they could have equity and we
[695.72 → 702.64] can all podcast together and work together and collaborate, and so I'm very excited about where
[702.64 → 709.10] it's going to go obviously in the short term it's on the bitter end of bittersweet especially for me
[709.10 → 715.92] I mean speaking very personally JS party is like one of my favourite things I've grown very fond of that
[715.92 → 723.14] podcast and those people and what we do together and go time very similar I'm not on go time on a
[723.14 → 727.72] regular basis I do show up from time to time but like I'm a regular on JS party and so that is just
[727.72 → 732.80] emotionally it's just a very hard thing to stop I'm very excited that nick and cable and Amy
[732.80 → 739.40] are going to continue podcasting together and that I have a standing offer to join their show whenever
[739.40 → 744.50] I want and hang out because I just love the shows that we made together and the times that we spent
[744.50 → 748.90] so it's been a hard decision it's been a long time coming for us obviously we don't talk about our
[748.90 → 756.00] indecisions publicly we talk about our decisions, but we've been toiling over this change like Adam said
[756.00 → 760.92] probably for a year we almost did it a year ago honestly, but we didn't, and now we're doing it
[760.92 → 767.50] sometimes you just got to pull the band-aid off you know, and it's hard, but it feels right and I'm
[767.50 → 775.44] excited about January because I think it's going to breed some new life into our show into these other
[775.44 → 782.04] shows and uh yeah those are my initial thoughts on it embracing change if we could use the title again
[782.04 → 788.20] I think we should yeah because it fits it really, really well yeah change happens whether we like
[788.20 → 793.72] it or not this way we are in control gaining something losing something you know just all
[793.72 → 799.52] part of the game you have to go back to the roots doing the things that you love first knowing
[799.52 → 805.62] what that thing is it's really hard because the world is a busy noisy place and there's always the
[805.62 → 810.80] imposter syndrome we know how well that works, and we also know there's always the grass is greener on
[810.80 → 817.48] the other side yeah the FOMO it's not exactly but the joy of missing out right the Como I really like
[817.48 → 824.30] that take the jomo exactly this could be it another baby title idea the joy of missing out
[824.30 → 828.92] that's the first time I've heard that oh really it's brand new to me right to this moment yeah I think
[828.92 → 835.24] I've heard it first at uh from DHH oh really yeah the joy of missing out and the context of remote work
[835.24 → 840.08] of course he would make that up I'm sure he did I don't know the point is the point is its about
[840.08 → 846.08] leaving slack in the system focusing on the things that you know you enjoy, and you're good at
[846.08 → 852.30] sharpening that axe and doing the best work that you can leave room to do that and that's really
[852.30 → 858.00] hard and really challenging, but it's worth it because at the end of it you look back 10 years from now
[858.00 → 864.96] 20 years from now, and you realize how rich your experience was because you made the choice it all
[864.96 → 870.54] starts with a choice, and it's not like you're stopping everything right you're finding another
[870.54 → 875.62] home you're just like there's like a whole like new twist a new perspective it's the next evolution
[875.62 → 884.34] in the changelog universe and I like that yeah you know just to laser focus on one specific thing
[884.34 → 891.36] that I've personally had angst with is that we've had a great opportunity to help many brands reach
[891.36 → 895.94] developers over the years like obviously we're sponsored most podcasts are any podcast that's
[895.94 → 901.08] sustainable or being sustained is usually sponsored in some way shape or form you find any podcast out
[901.08 → 906.46] there the biggest ones out there even Joe Rogan like he's he's sponsored you know we've had this
[906.46 → 912.90] ceiling of ability to help folks because we have limited shows I really believe that jarred and I are
[912.90 → 920.10] pretty good tastemakers and I think the idea with CPU is pretty cool, and we want to help more of
[920.10 → 925.76] those brands reach more developers, and we had a ceiling I would often tell folks because I'm a big
[925.76 → 930.62] big helper when I reach when I work with these different brands and I know that I'm like I can only help you
[930.62 → 938.26] this well with the shows I command under our belt and I think that jarred and I are two people we have
[938.26 → 944.04] limited bandwidth we add folks onto our team as necessary over the years to support us in producing
[944.04 → 950.16] podcasts but at some point like we had a limit, and now we have so much more opportunity to help more
[950.16 → 955.98] brands reach more developers through CPU so I think that's the coolest thing for me, I think being able to
[955.98 → 964.98] expand that to you know 10 or 15 podcasts with an index with a single subscribe point for many really
[964.98 → 971.92] awesome developer podcasts that join this I would say somewhat of a movement in a way world-class
[971.92 → 977.64] developer podcasts like that's a cool thing in my opinion and we have this big vision that is
[977.64 → 986.68] literally at the spark you know of the moment at cpu.fm and I have, and we have a big vision for it
[986.68 → 991.20] and I think it'll be good for us good for like jarred said the awesome shows will come from it
[991.20 → 996.04] but then more importantly like helping developer brands reach developers is really, really hard the
[996.04 → 1002.86] ones who have a good story they're just so new they have they need great awareness, but they're just so
[1002.86 → 1009.78] you know brand new in that story they have almost nowhere to easily go to execute to get the word out
[1009.78 → 1017.94] of who they are what they do and like that self-serving way to me is one cool way that I see a much more
[1017.94 → 1023.66] bigger opportunity for them and for us and for the shows that get supported from it one other point
[1023.66 → 1030.20] I'd like to make on this and then I'd love to get into your work Gerhard is that we had built out
[1030.20 → 1036.86] this portfolio of shows that we love and listeners love and hosts love, and it was all good there was no
[1036.86 → 1043.58] real struggle or there's no it was just like of course there's the work of scheduling and rescheduling and
[1043.58 → 1048.88] and sponsors and this happens and that happens and we have to get the thing out like that's all just work
[1048.88 → 1054.88] right of producing podcasts but I got to a point where we're doing these seven shows a week
[1054.88 → 1062.76] and this is relevant to Kaiden that I didn't have any bandwidth to actually experiment and I was writing
[1062.76 → 1067.90] I almost said this the other day Adam we had Chris coyer and Dave Rupert on the show last week on
[1067.90 → 1075.18] friends last week yeah, and we were talking about my desire to stay in the trenches and be actively
[1075.18 → 1079.54] developing I was I just have not been writing enough software lately like I want to build stuff
[1079.54 → 1084.92] more and I just didn't have any room to breathe, and so I literally would just do Kaiden driven
[1084.92 → 1089.42] development which is every two and a half months right like please don't look at my commit messages
[1089.42 → 1094.66] between the last you probably already did between the last Kaiden, and now it's not very much
[1094.66 → 1101.28] I just don't have the bandwidth and that's not good for our show that's not good for me personally
[1101.28 → 1108.58] that's not what I want to be doing I want to build stuff more and I'm so excited as we do laser focus on
[1108.58 → 1115.28] the changelog as we do take these productions off of our weekly calendar even though the shows will exist
[1115.28 → 1122.36] in spirit as other people's productions I got room to breathe I got room to code I can block an entire day
[1122.36 → 1129.54] and just be like I'm going to build something today and that I think is a huge benefit to this
[1129.54 → 1134.42] particular change which brings us to the work you've been doing because I haven't done jack squat
[1134.42 → 1139.06] gear hard hopefully even Kaiden because we've just been producing podcasts if not we don't have a show
[1139.06 → 1149.24] if not so I really get that to at a very deep level because that was at the root of the ship it shows
[1149.24 → 1155.42] me putting it on hold that was exactly its room to breathe room to experiment room to do other things
[1155.42 → 1162.30] room to do things differently that's how it started, and it's coming up to a year, and it still feels right
[1162.30 → 1172.36] and you're right being like it takes a certain amount of adulthood and strength of character
[1172.36 → 1178.64] to know that that's what's happening and I'm really glad that you're in this point it's an amazing
[1178.64 → 1183.68] point very important one essential for what's to come next it's a catalyst so it's the beginning of
[1183.68 → 1191.12] something amazing and I'm so excited to be a friend of this amazing journey very, very excited
[1191.12 → 1195.06] you are a friend you're part of it you've been a part of it for a long time thank you very much
[1195.06 → 1200.28] we're excited to keep you as a part of this as we grow and change we didn't highlight that much
[1200.28 → 1205.58] though in the in our post like there's nothing changing about Kaiden like Kaiden is oh no is now
[1205.58 → 1213.28] embedded into the changelog podcast itself like just to be super, super clear yeah it was implicit
[1213.28 → 1218.86] uh it will be more explicit here right there's nothing changing about Kaiden in fact I think it
[1218.86 → 1222.96] it won't get more frequent I think it might get better because I think jarred to your point I think
[1222.96 → 1230.06] you and I might have more time to do more development to make us less like Gerhard what did you make
[1230.06 → 1235.92] right so that we can have a podcast right and some iteration and some change so to everyone listening
[1235.92 → 1245.92] I want you to know that this conversation has been thought out weeks in advance you're at the baseline
[1245.92 → 1251.50] it only gets better from here yeah so stick with us this was the big announcement this was the important
[1251.50 → 1261.52] stuff, and now we're going to have some fun okay all right and trust me the last thing I'll be
[1261.52 → 1268.30] trying to keep it a secret for a while I think I've succeeded, and it's going to be amazing oh man
[1268.30 → 1274.88] so sit down you want to sit down for this one okay I'm more anxious now than I was early Christmas
[1274.88 → 1280.22] it is early Christmas I love if it is actually yes, so things are coming together so Gerhard has some
[1280.22 → 1285.70] presents for us, I think okay lets one can we oh just one, but it's great I hope you're hard you know
[1285.70 → 1291.68] the philosophy have two of everything come on man well there is another one but anyway see I can't
[1291.68 → 1296.92] hide this from you, you know you don't be too loud can we just skip to the end can we just not do this
[1296.92 → 1300.46] middle part this is why we need to have video podcasts too because you listen to naughty all
[1300.46 → 1305.82] these years have not seen the extreme laughter we've had on this podcast in particular that's true as a
[1305.82 → 1309.48] video like you may have seen it in clips, but you haven't seen the full length, and you can hear
[1309.48 → 1314.30] Gerhard's joy in his voice, but you can see it in his face even more yes oh yeah all right take us on the
[1314.30 → 1320.78] ride Gerhard I'm so excited for whatever it is by the way this little part was for Jason the editor
[1320.78 → 1326.64] oh I met him for the first time when we recorded the last ship it episode oh nice and uh that was
[1326.64 → 1331.90] very nice, so this laughter was for you Jason okay there you go right so this bit you may edit but i
[1331.90 → 1337.20] knew this is going to be fun and I thought about you as we're going through the show oh nice hopefully
[1337.20 → 1341.48] it won't be just my laugh it'll be everyone's laughter because we'll go a bit crazy okay but in a good
[1341.48 → 1347.88] tasteful way okay this is now telling Jason what to do make sure it's good and tasteful Jason exactly
[1347.88 → 1356.30] no wet wipes nothing like that okay so let's start all right so in the last Kaiden you were thinking
[1356.30 → 1363.10] jarred of getting a brand-new mac that's true try out the newly introduced just contribute that's true
[1363.10 → 1368.42] and you were saying that you've been waiting for a reason to upgrade right it was Black Friday
[1368.42 → 1371.46] Christmas is coming true, and you're saying that you're saying that you're saying that you're
[1371.48 → 1376.94] and I hear that the m4 is all the rage these days I've heard so much good so good yeah I've
[1376.94 → 1383.66] resisted hardcore but yes I almost went out yesterday and to the Apple Store.com whatever
[1383.66 → 1391.98] the website is and priced one out my trepidation is like we really maxed out these macs that we're
[1391.98 → 1399.78] currently using like my current MacBook Pro which is a 2021 m1 max and one yeah it was the first m but it
[1399.78 → 1406.54] was the maxed CPU first it's still very good and so that makes it hard to buy something
[1406.54 → 1413.72] brand new it is the 2021, but it's 64 gigs of ram it's got a massive like multi-terabyte hard drive
[1413.72 → 1418.76] like it was basically like go to the configurator and hit the max on everything besides the size it
[1418.76 → 1425.26] is a 14 inch not the 16 inch so aside from the screen size it's just maxed out, and so I hate to
[1425.26 → 1431.72] go buy one new that has fewer specs than this one but when I go max out the new one again I'm like
[1431.72 → 1438.40] can I justify this because my one's working pretty well you know yeah and so or I could go downstream
[1438.40 → 1443.68] and like do I really need all that storage do i really need all the ram and so that's where i just
[1443.68 → 1449.74] like close tab and move on for a little while so no I do not have a new mac but gosh I want one
[1449.74 → 1452.14] did you try just contribute because that was the point
[1452.14 → 1459.82] I'm already a contributor Gerhard so I didn't really have I've used just but I have not tried
[1459.82 → 1465.44] just contribute so no I failed you in that way Adam no sir sorry oh man
[1465.44 → 1474.00] now in all honesty I know that a few uh listeners have tried I forget um who exactly it was there
[1474.00 → 1478.34] was someone that mentioned that a lot of work has gone into it um do you remember that jarred
[1478.34 → 1484.62] it was one of the comments maybe I forget his name that's all I know it was uh I want to say it was Adam
[1484.62 → 1489.46] but no it wasn't Adam it was someone else anyway it was somewhere I'm not going to look for it now
[1489.46 → 1494.74] but it's there people can try it, and we'll be building on top of that also in the last Kaiden
[1494.74 → 1501.34] and by the way there's going to be video this will work well I was mentioning that um I'll be
[1501.34 → 1509.14] talking at saloon about how I took my home lab into production and so that happened nice something
[1509.14 → 1515.76] special about that was that it was a recorded talk by myself I did the editing I had multiple cameras
[1515.76 → 1522.10] and it's out on YouTube so you can check it out very cool the one thing that was one of my favourite
[1522.10 → 1528.88] moments about this talk is me showing off the actual home lab, so the home lab was a latte panda
[1528.88 → 1539.24] sigma and the size for comparison it's exactly as big as an iPhone maxi phone pro max okay so you have
[1539.24 → 1547.00] an iPhone sized home lab which is insanely powerful you can run Kubernetes on it 16 cores ddr5
[1547.00 → 1555.56] multi-terabyte NVMe drives, and it can serve 300 billion requests per minute sorry per month
[1555.56 → 1563.88] sorry that would be crazy no 300 billion sorry requests per month okay so a lot of like many
[1563.88 → 1569.38] billions requests per month anyway um we may link to the talk for you to go and check out absolutely
[1569.38 → 1575.58] so the one thing that was fascinating about or that's fascinating about this specific
[1575.58 → 1581.72] device is that it has an intel CPU and I know that intel now has not been doing that great this year
[1581.72 → 1590.00] but they do have a video sync which means they can do trans video transcoding really, really well
[1590.00 → 1596.70] so they have GPUs that can do video transcoding this one has an intel iris he graphics which means
[1596.70 → 1604.06] they can do video transcoding amazingly well so okay let's take the nerdiness level plus one okay
[1604.06 → 1610.54] always and for this both of you'll need to take out your browsers okay, and you will need to go
[1610.54 → 1620.36] to Jellyfin oh dot make it work dot TV are you going to share with us your home theatre setup or what
[1620.36 → 1630.14] uh no okay I'm there you're there so enter your GitHub username and for the password by the way if
[1630.14 → 1635.98] you're listening this will change the password is kaizen17 I'm in okay what do you see tell us
[1635.98 → 1644.84] my media I'm in the Jellyfin home page I see drafts and recently added in drafts I see some vertical
[1644.84 → 1651.38] video thumbnails and a horizontal video thumbnail excellent click on one click on the drafts okay
[1651.38 → 1661.78] and uh pick the 4k one 2160 full 2160p I see a loading spinner great it's running on my shelf by
[1661.78 → 1668.28] the way there is a CDN, but it's running on my shelf the home lab and the video is being served
[1668.28 → 1675.82] from that home lab instance, so this is home lab taken further what is this video is the last
[1675.82 → 1683.40] conversation that we had with jams and Matt about building out the pipe dream CDN this was august
[1683.40 → 1690.30] it took me a while to edit the video did it load by the way yes I just had a Post so I could listen
[1690.30 → 1695.84] to you talk it's running smoothly too excellent, so this video is running off that latte panda sigma
[1695.84 → 1704.52] it's being fronted by a CDN so it's turtles and turtles and this is the content which i
[1704.52 → 1710.90] always imagined I would produce content that has the conversation part and content, and then we do
[1710.90 → 1716.46] screen sharing, and we go deep the content that you're looking at is about an hour the whole thing
[1716.46 → 1722.82] the whole hour, and it was edited down for about three hours that was a long conversation yeah and
[1722.82 → 1729.08] it's still a draft so it hasn't been published yet, but it's coming so taking the home lab further
[1729.08 → 1735.18] doing the CDN in a way it's the adventure it's a CDN adventure I think that's what's happening
[1735.18 → 1740.32] and chaining our home labs and chaining the devices that we all love whether it's a m4
[1740.32 → 1749.74] or an intel based home lab so you're part of something special just like cpu.fm is special
[1749.74 → 1755.68] and it's coming it's not there yet but there will be little more things coming maybe just in time for
[1755.68 → 1764.06] Christmas series of videos that are I'm thinking of them as movies for infrastructure nerds and
[1764.06 → 1769.52] makeitwork.tv will be the place for this when it's done let's also makeitwork.fm
[1769.52 → 1775.60] but makeitwork.fm is just for the conversations just like the audio part so that's how this works
[1775.60 → 1782.78] nice love it, so changelog is very embedded in this because you know a lot of the experimentation
[1782.78 → 1788.74] that I do happens in the context of changelog and then on top of that take it further make the time
[1788.74 → 1794.56] to create the content that uses that but obviously there's like so much more that happens like the
[1794.56 → 1799.54] editing you have no idea how much it takes me to do the actual editing that is my biggest issue
[1799.54 → 1805.74] so I have an appreciation for video 4k video done well and sound and everything for it to sound
[1805.74 → 1811.72] right to look right to the colour grading it just takes a while da Vinci resolve I think I've been
[1811.72 → 1817.34] using that app more than my terminal in the last I don't know six months I've been learning it I've
[1817.34 → 1825.70] been it's its amazing but anyway back to Kaiden like to back to the Kaiden 17 so we talked about the
[1825.70 → 1832.88] CPU FM we talked about the home lab, and we finally did it the thing that we talked about for a while
[1832.88 → 1841.56] jarred right enable team members to replace changelog dev with a prod dB dump let's pull request 533
[1841.56 → 1852.84] did you try that yes sir tell us about it is works great that's what I care about it was fast it was
[1852.84 → 1860.06] seamless uh it just worked I think I did have to configure something the first time I think you
[1860.06 → 1865.48] were making some changes to NRC files or yeah there's just been some like environment variable
[1865.48 → 1873.70] things that I had to do the first time but I can tell how you made the last time around by using this
[1873.70 → 1882.74] just is it a toolkit is it a what is it library I would call it an um a CLI utility it's like a
[1882.74 → 1888.10] make, but it just improves on make basically right if you've used make that's what it commands runner
[1888.10 → 1897.64] some would say right so we'll just call it this CLI tool that you made the change easy
[1897.64 → 1902.92] and now you're making the easy change yeah call back to the previous episode call back to of course
[1902.92 → 1909.76] Kent beck's first make the change easy warning this may be hard then make the easy change classic
[1909.76 → 1914.00] quote from Kent beck because this was like a pretty easy change for you, it looked like
[1914.00 → 1919.62] in terms of this particular one now you had some neon things to do, but you can tell us about the
[1919.62 → 1924.62] details of how it worked yeah the PR itself seemed pretty straightforward and small, and then it worked
[1924.62 → 1931.02] so that was my experience very nice I'm very glad that you experienced it that way I'm curious when Adam
[1931.02 → 1938.16] tries it out how well this works for him the idea is that we wrap a bunch of commands that you would
[1938.16 → 1944.34] need to run locally right so for example installing the neon CLI so that you can, you know control to
[1944.34 → 1949.98] you and by the way there's two you can do it like via NPM, or you can go and download the binary the
[1949.98 → 1957.02] binary the version it's a slightly different one, so there's like some inconsistencies in the CLI
[1957.02 → 1963.24] binary from neon, but this basically handles all of that and what I thought would be easy like I thought
[1963.24 → 1968.40] this change would be easy but actually there were like quite a few rabbit holes that I had to go down
[1968.40 → 1974.06] on one for example was how to download in the format which is compressed right because you don't want
[1974.06 → 1980.40] to download many gigabytes locally so how do you compress it automatically and then how do you handle
[1980.40 → 1985.36] extensions that exist on neon they're installed on neon, but you don't have locally in your Postgres
[1985.36 → 1990.46] database, so there was that as well so I had to uninstall an extension which is giving us metrics
[1990.46 → 1995.94] that you can do via SQL queries, so there are like a few things like that I had to go through
[1995.94 → 2004.68] but still what it means is that this command just restore DVD from prod that's exactly how we call
[2004.68 → 2010.00] it you can look at the pull request there's even a video just shows how it works it wraps all that
[2010.00 → 2014.74] complexity like all that like know-how you have to run this command, and you have to pass this value
[2014.74 → 2020.16] and the other thing is the credentials they're pulled just in time from the one password vault
[2020.16 → 2027.14] you don't have to remember them, and it orchestrates all of that so the integration I was really happy
[2027.14 → 2035.30] with it how it worked, and it feels like an easy thing like to wrap your head around there's
[2035.30 → 2040.20] nothing complex about like what's like obviously there are like a couple of like niggles to sort out but
[2040.20 → 2044.82] you don't see them when you use it, and you can even like to see the commands before they run you can
[2044.82 → 2051.16] copy and paste the commands, so everything runs locally and I think this was the hard part before because
[2051.16 → 2056.12] when we were using dagger for this that was running in containers, but you don't use containers so we had
[2056.12 → 2062.22] to make that big change so that you would have this nice local experience everything runs again doesn't
[2062.22 → 2067.66] need docker doesn't need anything like that doesn't need dagger it's just commands installing binaries
[2067.66 → 2071.42] things like that so I'm glad that you tried it I'm glad that it's working do you see yourself using
[2071.42 → 2077.82] this yes immediately yes it's just so straightforward I mean all the things that you just said right now
[2077.82 → 2084.70] are things that I love, and so I'm way more likely to pick up this simple tool especially following your
[2084.70 → 2094.36] example then I was honestly even with the old make files which because of your expertise in make files
[2094.36 → 2101.32] I was perpetually lost I've looked at the just files, and they're just easier for me to grok the fact
[2101.32 → 2107.32] that there are no containers there's no dagger there are no things that I generally put in the black box of
[2107.32 → 2115.56] like gear hard land it just for me as a regular app developer like it's more approachable, and so I script
[2115.56 → 2122.04] stuff all the time you know this is basically taking a script of mine that I would do and just have my
[2122.04 → 2127.96] local machine to do all these steps, and it's formalizing it into a shared repository I'm way
[2127.96 → 2133.56] more likely to follow that lead and create additional just commands and now I have time to so I'm totally
[2133.56 → 2150.04] into this gear hard for a second oh I'm so happy I'm so happy that's that's a huge score
[2152.04 → 2171.80] what's up friends I'm here with cal barberry co-founder and CTO at coder.com so coder.com is
[2171.80 → 2181.08] a cloud development environment a CDE, and you run on all the cloud saws azure GCP you're on prem and
[2181.08 → 2186.60] you're no stranger to competition right the competition out there is well known but what
[2186.60 → 2192.04] shocks you what surprises you about the state of cloud development environments and how developers
[2192.04 → 2195.88] are leveraging them you know it actually shocked me the majority of like our largest provisioned
[2195.88 → 2199.48] customers do not use containers with their development environments they actually use VMS
[2199.48 → 2205.96] on like GCP AWS or some kind of mixture of them one of the largest auto manufacturers they have like a
[2205.96 → 2211.80] little bit over a thousand devs that use coder every day and uh they use a mixture of azure AWS and GCP
[2212.36 → 2219.24] so I've used docker I've used VMS but take me into the technical details what is it that's different
[2219.24 → 2224.92] between a VM and running something in docker kind of like all existing solutions like kind of our
[2224.92 → 2229.56] competitors in the market all really have a container-based approach where you build like a
[2229.56 → 2234.92] dock container and developers work inside of that, and it faces a couple limitations because you know Adam like
[2234.92 → 2239.24] if you know on your machine right now 100 you're not working inside a dock container doing this
[2239.24 → 2244.36] discussion right it's just very different, so there are a lot of software expectations that actually
[2244.36 → 2250.84] don't really work inside a container an example is a customer of ours is square, and they do stuff
[2250.84 → 2256.20] with a payment terminal, and so they need essentially like hardware accelerated android that is just
[2256.20 → 2261.80] really finicky to get working in a container you totally can pass dev KVM into a container and get
[2261.80 → 2266.12] hardware accelerated virtualization, but it's a little trickier and a little more Jacky and so
[2266.12 → 2270.68] they'd rather just be like no the simple thing is give everyone a VM there's no point to change the
[2270.68 → 2275.48] way that we work in entirety to do some weird virtualization uh bank it just makes more sense
[2275.48 → 2282.52] to give them a VM that we know works well it might be time to consider a cloud development environment
[2282.52 → 2290.20] and open source is awesome and coder is fully open source you can go to coder.com get a demo or try it
[2290.20 → 2299.32] right now or even start a 30-day trial of coder enterprise once again coder.com that's c-o-d-e-r.com
[2299.32 → 2300.68] coder.com
[2304.28 → 2311.72] the next one was enabling team members the next pull request 534 was basically building on top
[2311.72 → 2318.12] of this, and it just enables team members to run dev with a neon dB branch, so this is a rework of what we
[2318.12 → 2324.28] had before that's why it removed more lines than it added but basically built on top of the same
[2324.28 → 2331.64] just approach did you try this command jarred no, no okay will you ever have an interest to try this
[2331.64 → 2339.24] command, so this creates a new branch on neon not just that it also configures your app it starts your app
[2339.24 → 2344.84] with that neon branch, so there's no more manual it's like one command, and it will run everything it
[2344.84 → 2350.28] will create the branch, and then it will configure your app to use the branch there's no more manual
[2350.28 → 2358.04] digging around, and you can believe this yeah potentially I do like to develop against production
[2358.04 → 2365.16] as a branch I prefer to have it pulled down locally so I think I would probably opt for the other one
[2365.16 → 2370.60] that you just created which is why this one wasn't as exciting to me and I didn't even try it but would
[2370.60 → 2378.20] this also do sync between those two branches because that's my bugaboo is you do a branch off
[2378.20 → 2383.80] of prod yeah then you're developing against the branch, and then you want fresh data and so i already
[2383.80 → 2389.72] have a command that gets me the fresh data locally but if I didn't than I go to the neon deal and I go
[2389.72 → 2396.52] find the place in the UI where I hit sync to main or whatever and I don't like that step so if this
[2396.52 → 2401.40] could do that I mean maybe be a second command that just I'm sure it's available via the CLI somehow
[2401.40 → 2406.20] yeah I haven't looked into that it does make sense it does make sense to add it by the way
[2406.20 → 2411.80] and even if the CLI doesn't support it maybe there's an um a curl request that we can do to the API
[2412.36 → 2417.16] to get this synced but that makes sense yeah because that's really what I want is I want the freshens
[2417.16 → 2424.36] every time and so it would be nice to have something like this right so the freshens ones to get the
[2424.36 → 2430.28] freshens ones which is a great idea by the way the first command will take longer because it has to
[2430.28 → 2435.88] pull down the entire database and that takes a while, and then it has to load the entire database
[2435.88 → 2441.08] it basically removes what you have locally, and it's all towards everything so that can take up to five
[2441.08 → 2446.44] minutes depending on internet connection a bunch of things yeahs I experienced that and so this would
[2446.44 → 2452.76] be faster this would be fast yes generally when it's time for me to develop I issue that command
[2452.76 → 2458.52] I go get a fresh cup of coffee I come back and I'm ready to rock coffee so like for you're
[2458.52 → 2464.12] going to do it once a week maybe yeah it doesn't bug me to have the five minutes if I was doing more
[2464.12 → 2469.32] experimenting and changing and stuff I think having these immediate branches like without any sort i
[2469.32 → 2473.48] would still have a little trepidation that like maybe I'm pointed at the wrong thing that's why the
[2473.48 → 2477.40] command now handles all of that so that you don't have to worry today so the correct environment
[2477.40 → 2482.20] variables is everything correct and because everything happens inside the command once it gets to a
[2482.20 → 2489.08] point like we had for example Adam's um, um case where you know sometimes it fails, and then you don't
[2489.08 → 2495.16] like what state am I in this command tends to be self-contained in the point what that means is that
[2495.16 → 2501.00] once it gets to a certain point you're safe you're sure it will continue, and it will finish it will do the
[2501.00 → 2507.16] right thing, and it's all embedded in the actual command now this command when you're connected to a remote
[2507.16 → 2513.96] database it's can be slightly slower so for me for example i I preferred downloading all the data
[2513.96 → 2520.04] locally and having all that locally because it felt snappier and even though we the query planner we
[2520.04 → 2524.12] warm up the query planner so that you know things are cached, and we do a couple of things like that
[2524.92 → 2529.16] it still feels slower it still is slower because it has to do all those round trips right, and they're
[2529.16 → 2535.64] all remote they're all remote calls to this remote database so I think the choice is between paying the
[2535.64 → 2541.32] penalty once five minutes three minutes depending on your internet connection to load all the data
[2541.32 → 2547.56] and then you know you have the latest or pay a little bit of penalty every time you do load the
[2547.56 → 2552.92] page because it may take I don't know a second slower sometimes depending on how many queries you're
[2552.92 → 2559.00] running, so both options are there I think knowing Adam I think he would prefer the second option so that
[2559.00 → 2563.24] he's connected against a remote database and I think you would prefer the first option so we have a mix of
[2563.24 → 2567.32] both I think that's probably accurate yeah, but we'll make sure that this works for Adam as well
[2567.96 → 2576.04] not in this context but as a follow-up for sure cool well the next thing which improved for us and this
[2576.04 → 2582.92] was great to see was the all in Zulip approach Zulip how do you pronounce it Zulip
[2582.92 → 2589.72] Zulip pretty much that's how we pronounce it great Adam pronounces it zuli that's right like hold
[2589.72 → 2595.24] he thinks they should drop the p like hold exactly okay kindred spirits that's Adam's idea drop the p
[2595.80 → 2601.64] call it Zulu that's right so I think at this point everyone basically migrated from our slack
[2601.64 → 2609.08] to Zulu or Zulu yeah everyone's there the conversations are there I won't call it Zulip
[2609.08 → 2618.44] Zulip yes just a joke, so everyone migrated to Zulip how does it work uh amazing its awesome
[2618.44 → 2624.44] I think it's easier to track and follow better than slack when I go back to slack now I feel like I'm in
[2624.44 → 2630.60] like some sort of archaic way of communicating which is just like throw it at the wall and
[2630.60 → 2636.60] if you see it cool you can't compartmentalize conversations threading is obviously there but
[2636.60 → 2642.44] it's not the same as Zulip it's threaded conversations for teams is what their mantra is basically
[2643.96 → 2648.52] the one key thing I think that makes it look different in terms of how you interact with it
[2648.52 → 2654.20] as a user to communicate is that everything is based on a topic so if you're starting something
[2654.20 → 2659.24] new you're beginning a new topic which can be to some degree daunting because you think well
[2659.24 → 2663.88] if I want to say something I must have a place to say it and if there's no place to say it then you
[2663.88 → 2669.00] feel like oh i have to create it so is it that important maybe that's what stops you from communicating
[2669.00 → 2673.40] I don't fully disagree with that sentiment i kind of wish there was a merger of the worlds where you
[2673.40 → 2680.12] have like a single place in Zulu that is non-threaded where it's just like this is where
[2680.12 → 2685.16] that everything goes then I can kind of feel the angst against that because like if your principle
[2685.16 → 2692.76] is it must communication must correspond with a topic, and you're that's your way I can understand
[2692.76 → 2699.00] why they've sort of harkened into their ways to not do that but as a user i kind of want the slack
[2699.00 → 2703.48] world in a way where it's just like everything goes where it can go like a main channel for example
[2703.48 → 2711.72] and then also still have the topic world, but topic based inside ours we have you know the
[2711.72 → 2719.56] different podcasts their episodes you can comment on a Kaiden 17 for example you know it's really
[2719.56 → 2724.60] compartmentalized which I like a lot and those threads are long-lived like we've got this WordPress
[2724.60 → 2729.96] drama thread that was not started by me or jarred it was started by the community, and it's still being
[2729.96 → 2736.28] active today whereas in Slack that conversation would have just died and got reborn
[2736.28 → 2743.96] and the context of prior conversations isn't there so you have this community keep it together long run
[2743.96 → 2752.28] conversations that can be potentially months maybe even years and that's just not equally possible
[2753.32 → 2758.76] in slack you can do if it's just not present so easily in the UI that's what I love about Zulu
[2758.76 → 2766.04] yeah it did take me a while to get used to the idea that everything is a thread yeah but then once
[2766.04 → 2771.16] you make that switch you realize actually this allows me to be more focused I can just pick a
[2771.16 → 2775.40] thread and I'm there that's the context I can see it everywhere so I can see everything that was
[2775.40 → 2781.64] discussed in that thread so that's really cool also having a thread per episode I think that's a great idea
[2781.64 → 2788.28] I cannot remember how many times there was a comment on an episode on the changelog website which i just
[2788.28 → 2794.44] couldn't find I couldn't find how do I get to the comments on an episode now so much easier yeah I think
[2794.44 → 2800.76] that's been really nice especially for podcasts where they are consumed not just asynchronously but like
[2800.76 → 2806.92] massively asynchronously where there's people who are like living off the fire hose, and they listen to the
[2806.92 → 2811.96] episode when you drop it and then there's people who are like three months behind perpetually and then
[2811.96 → 2816.04] there's people who are like back catalogue dwellers where they're like listening back through the
[2816.04 → 2821.32] catalogue, and they may listen to it years later well there was never a place where all those people
[2821.32 → 2827.80] could easily find here's where that discussion is and so the thing that I've heard the most and which
[2827.80 → 2834.52] I've enjoyed is people's ability to hop back into an older episode and either strike that conversation
[2834.52 → 2839.80] back up or even just read it what people had to say in the time between it shipping and you listening
[2839.80 → 2845.48] to it so that's really cool I do have after living and anytime you live somewhere for a while you see
[2845.48 → 2850.92] all the warts you know I'm starting to have a little bit of the not buyer's remorse but just like Zulip
[2851.64 → 2858.52] wart finding adventures if I might call it that the mobile app leaves a lot to be desired I know they are
[2859.32 → 2863.88] rewriting it right now in flutter, and so they're working on that there are all kinds of
[2863.88 → 2873.56] little UI things that just bother me about Zulip but the URLs I'm an I'm a URL guy I can't
[2873.56 → 2879.24] believe some of the URLs these folks put together because it's basically it's a spa and everything
[2879.24 → 2883.32] is like go read the URLs they're just not pretty and when you're trying to deep link into stuff I don't
[2883.32 → 2887.72] know that matters to me, it offends my sensibilities when you're deep linking into something you're like
[2887.72 → 2893.16] look at this URL i have to go give somebody stuff like that just not minor nitpicks um, but it's definitely
[2893.16 → 2900.04] better it's better than slack and in many ways and while we are all in pretty much on using Zulip we
[2900.04 → 2906.20] haven't done any sort of finalization in terms of like the blog post I was going to write probably
[2906.20 → 2911.88] still will like we haven't closed our slack probably can't at the moment there's still conversations
[2911.88 → 2917.24] happening they're mostly in private team chats some with collaborators who we don't want to just ask them
[2917.24 → 2922.84] to move to Zulip because it's just kind of odd and strange to be like by the way from now on if you
[2922.84 → 2928.68] want to communicate with us switch to Zulip you must come over here so yes we are living in a little bit
[2928.68 → 2934.76] of a blue-green I would call it blue long blue-green yeah it's a blue-green deployment yeah exactly and
[2934.76 → 2941.16] there's lots of green on this side of the grass, but it's not entirely there yet yeah do you see us
[2941.16 → 2948.20] shutting down slack at some point sure hope so we certainly can especially for just like the public
[2948.20 → 2954.04] discussions of like there's no like Slack is cut off at this point in terms of joining like the website
[2954.04 → 2960.68] is all you join the community you get invited to Zulip you can't get a slack invite unless you go inside
[2960.68 → 2967.64] a slack and invite somebody um and so it's like essentially cut off from the world and there's no
[2967.64 → 2972.04] conversations happening there in the public at all every once in a while somebody will say something
[2972.04 → 2976.84] mostly they're spammers um our new episodes are still posting there I haven't quite made that change
[2976.84 → 2982.28] yet I figured we'd do some sort of more big announcement first and like encourage people
[2982.28 → 2987.88] who are still in slack one last time to come over to Zulip, but we do have a lot of team chats and private
[2987.88 → 2995.48] chats that are ongoing and used that we haven't quite gotten cut over to and some of them like I said
[2995.48 → 3001.16] are with like folks from partner podcasts and stuff I don't know we haven't decided if we're going to
[3001.16 → 3008.44] actually like close the slack, but we would like to yes it would be nice to just have not had to have
[3008.44 → 3015.24] it as an option so that you miss conversations or have to track one more place I think it's the sad
[3015.24 → 3021.08] part about our slack is that it is a free slack and so that means after the rolling time schedule they have
[3021.08 → 3028.44] conversations just go away and that's not cool i just really hope that slack goes away for us, I love
[3028.44 → 3034.52] slack i you know my real hope I suppose maybe if I rewinded prior to Zulip my I have two hopes
[3035.40 → 3042.92] I would love slack to support communities better and support uh non-enterprise not so that they can
[3044.20 → 3049.00] I think there's just there's just so many people have Slack embedded into their world it's not going
[3049.00 → 3053.72] away I'm part of other slack, so slack isn't going to go away from me, it might go away for changelog
[3053.72 → 3058.44] but it's not going to go away for me as an individual human being same I would love it if slack
[3059.00 → 3066.52] supported communities better and that way places like changelog could have had some sort of
[3066.52 → 3070.60] relationship that didn't have to be free we don't want to be freeloaders to slack we would love to pay but
[3071.24 → 3076.76] we have 7 000 people in main eat one point not all of them active but like if we had to pay for
[3076.76 → 3082.76] everybody in there OMG we would go broke right we can get it sponsored maybe, but then it's like well
[3082.76 → 3089.08] does that really add value to a sponsor you know to support that Slack channel maybe I mean there's
[3089.08 → 3093.16] there might be ways we could do it, but it would be kind of maybe icky to enable that so I just would
[3093.16 → 3099.40] love slack to revisit the idea of the ubiquity and embeddedness that they have with developers
[3099.40 → 3104.44] and the community aspect that just doesn't get to foster without paying large sums of money
[3104.44 → 3109.56] uh find a different business model that supports those folks I think you'd change some things
[3109.56 → 3117.32] second I think that Zulu has so much potential and I say that not negatively in the fact
[3117.32 → 3123.64] they're not reaching it, but they have so much potential to reach and a lot of people I've had
[3123.64 → 3128.36] to say to people we don't use Slack any more we use Zulu, and they're like what is that that is an
[3128.36 → 3133.16] absolute shame that's what that is because Zulu is so cool it's open source there's an amazing team
[3133.16 → 3137.96] behind it, they have an iOS app an android app a web app but for the faults that jarred mentioned
[3137.96 → 3144.28] I think they just they're held back by some beliefs they have that have just held them back
[3145.00 → 3150.76] but then again they're held back may be perception for me and not them they're held back is like no
[3150.76 → 3155.96] we're doing exactly what we want to do we're we're reaching communities, and they're supporting us like
[3155.96 → 3160.12] we fit perfectly in their world in terms of how we as a community use Zulip
[3160.12 → 3170.36] I just think there's they could more thoroughly compete with slack if they changed a couple of things
[3170.36 → 3175.00] I don't know how to say that really in this podcast, but there's opportunity there's hidden potential
[3175.00 → 3179.56] they can seize and I hope they do it my two hopes are slack support better communities
[3181.40 → 3183.88] support communities better and Zulu to reach their full potential
[3183.88 → 3191.24] yeah by the way just as you solved your problem with one password nice I solved my problem with
[3191.24 → 3197.96] who posted that just contribute worked well that was my Johnson it was in zulip it was Kaiser
[3197.96 → 3203.64] just do it that was the thread I found it, and he wrote Matt Johnson wrote just and install and just
[3203.64 → 3209.96] install worked pretty cool I then ran just contributing wow yeah that does a lot it worked though so just
[3209.96 → 3217.48] contributed worked for Matt Johnson September 2024 so now I know how to find if it was in Zulu
[3217.48 → 3227.40] polo long nice cool okay well one thing which I also liked is how when you post an episode there's a
[3227.40 → 3232.44] markdown for all the chapters and that was jarred's magic so even though he didn't do a lot which I think
[3232.44 → 3237.32] he did by the way he's just being modest this was the one thing that he did and I love that improvement
[3237.32 → 3245.16] uh thank you this was one of these moments where you're just like it's markdown that's easy markdown
[3245.16 → 3250.36] has tables I wonder if they support tables yes Zulu supports Markdown tables that's pretty easy
[3251.48 → 3256.12] why not add chapters and the cool thing about it was I I had a little bit of concern that it would be
[3256.12 → 3260.84] too long if you do that however Zulu will take long messages and collapse them by default when you
[3260.84 → 3264.84] first look at the thread and so if you don't want to look at the chapters it doesn't bug you at all you
[3264.84 → 3269.32] want to get straight to the other people's conversations so that was nice to see and yeah
[3269.32 → 3275.40] you know one of the cool things about having our database our admin our back end as the central
[3275.40 → 3281.16] source of truth for our chapters versus in the mp3 file or in the RSS feed is that we can basically
[3281.16 → 3286.36] emit those in different places that make sense and this seems like a place that really makes sense
[3286.36 → 3290.44] because if you're just hanging out in Zulip, and you're not sure if you want to listen to an episode
[3290.44 → 3294.52] because it's not really your bag of tricks, but maybe we talked about something you're interested
[3294.52 → 3298.52] in somewhere in the middle yeah you could just scan the chapters real quick and see if anything
[3298.52 → 3305.56] catches your eye I thought about linking up each chapter directly to the start time over on the
[3305.56 → 3310.44] website so you can actually click on them and listen from there I didn't quite get that far I'm not
[3310.44 → 3316.12] sure if that's would you love that I would love that honestly like once I've seen these chapters
[3316.12 → 3321.56] that was the point like wow this like this all of a sudden made Zulip 10 times more useful for me
[3321.56 → 3326.76] than Slack ever was nice because now I can see the episodes I can comment on the episodes same
[3326.76 → 3333.48] interface and I can see the topics right these chapters super useful the one thing which I was
[3333.48 → 3340.20] missing is where's the link to click on the chapters so this would be so amazing that was like
[3340.20 → 3344.52] on my to do next list because it's just easy for I've already done most of the hard work
[3344.52 → 3349.64] it's just a matter of making those links clickable and so maybe what I needed was a
[3349.64 → 3354.68] little encouragement I'm happy to add that as an easy Kaiden would love that I would concur and plus
[3354.68 → 3360.12] one that because uh that would make me click a chapter start time easily because it would be
[3360.12 → 3366.28] clickable for one and I want to now I want to but I can't and I cannot do that yeah I will say that
[3366.28 → 3370.76] when we go to a video first world, and we're bifurcated temporarily while we have
[3370.76 → 3375.64] interview this is sort of somewhat in the weeds we may roll out one show as video first and
[3375.64 → 3382.52] the next second it might make that integration slightly harder, but you know because it
[3382.52 → 3387.08] might link to need to link to YouTube for example to a timestamp versus to our site as a timestamp
[3387.64 → 3391.40] but you still need to write like the timestamps in YouTube so you have to generate the chapters
[3391.40 → 3396.20] ahead of time yeah just they text they convert them automatically so yeah hence the workflow
[3396.20 → 3401.24] challenges we've talked about in the new era for the changelog podcast universe is this the
[3401.24 → 3407.80] question becomes do we have one artifact yeah that is identical in both platforms or do you have a
[3407.80 → 3413.40] slightly different show on YouTube than you do yeah in the audio because of reasons, and so we're still
[3413.40 → 3419.08] in the throes of figuring all that out but I think once we figure all that out adjusting the stuff for
[3419.08 → 3424.28] the chapters won't be too hard because we already had done all the hard work I did try both approaches and
[3424.28 → 3429.00] I do find that YouTube is a different medium and I think to get them to get the best out of it you
[3429.00 → 3434.84] have to cater to the audience that's on YouTube and that audience prefers the content to be a bit
[3434.84 → 3440.20] punchier a bit like more to the point right like don't lose the audience because they have certain
[3440.20 → 3445.80] expectations, and we're not even talking shorts is completely different sure right, so this is
[3445.80 → 3451.96] just when you put a video on YouTube yes great but I think the transitions they need to be a bit quicker
[3451.96 → 3457.48] than you would have in a conversation yeah I mean even just the way that we do a pre-roll ad in our
[3457.48 → 3463.24] podcast we come up with like the intro the voiceover and then a pre-roll ad, and it's like is a YouTube
[3463.24 → 3469.24] video with a pre-roll ad at the beginning going to get you know action over there I don't think the
[3469.24 → 3473.00] people on YouTube want that do we just cut straight to the interview there, so there's like a lot of those
[3473.00 → 3477.48] kind of and then also now you have basically two shows you're doing yeah for the price of one and so
[3477.48 → 3482.20] yeah we're still figuring all that out yeah two cuts it's like a director trying to do like oh
[3482.20 → 3488.20] here's the extended cut and the theatrical and the know producer's version of it all in the
[3488.20 → 3493.00] same release like no that doesn't happen right the extended cut always comes later it's usually like
[3493.00 → 3496.36] oh that was much better or in the case of really Scott that was much worse because he likes his
[3496.36 → 3501.64] original cuts better first well sometimes the extended cuts are much worse because it's the director
[3501.64 → 3506.44] being like entirely up their own butt with their love of their story, and it's like no the cut was
[3506.44 → 3511.08] perfect actually your editors are excellent yeah other times the extended cuts awesome so it is
[3511.72 → 3516.60] it is hit or miss but for sure I am on the 10th conversation editing the 10th conversation
[3516.60 → 3522.28] right now the one that you saw in drafts and the conclusion which I reached is that audio has to be
[3522.28 → 3528.92] separate right you focus on a listener not a watcher then you focus on the YouTube audience that they
[3528.92 → 3533.72] want something quick they want something free they want something entertaining, and then you have to
[3533.72 → 3539.56] focus and cater to the real nerd they want to see the whole thing they want to see like a great cut
[3539.56 → 3545.40] but they want to see they want to immerse themselves in the story that is not your YouTuber that is i
[3545.40 → 3549.72] don't think that's your listener because especially if you have some video which is like screen sharing
[3549.72 → 3554.92] that is different that's more engaging that just basically ups the ante and ups the story
[3554.92 → 3561.08] and takes it to a whole new level, so those three audiences are very different and I end up with
[3561.08 → 3566.76] three types of content same conversation three types of content catering to the audience, and again we're
[3566.76 → 3574.28] not even talking shorts or Instagram or ticktock which just requires another approach speaking of
[3574.28 → 3580.68] improvements there's one more that I noticed and I was so happy to see jarred do that notifications
[3580.68 → 3586.92] deploy notifications in Zulip that was so cool yay I forgot I did that how was it building that
[3586.92 → 3591.40] like how was that building it I don't even remember to be honest in fact when I saw those
[3591.40 → 3595.80] code deploys I thought did Gerhard do that or did I do that that's how much it's been a bit of a
[3595.80 → 3604.76] whirlwind around here wow easy I guess I do remember once you have basically the Zulip API like their stuff
[3604.76 → 3610.20] is so simple that's one of the things I like about them there's no OAuth there's no like craziness it's just
[3610.20 → 3616.20] like look go ahead and generate a token and then throw that token in a header and all the requests
[3616.20 → 3619.88] that you have that token in the header we're going to let you do what you want to do now there are some
[3619.88 → 3624.84] fine grain controls beyond that, but they just start from the basic place and so that made me
[3625.64 → 3634.28] getting Zulip abilities inside our app like 30 lines of code you know for the module that changelog.Zulip
[3634.28 → 3641.72] module yeah which invites people and posts stuff and once you can post stuff then you're just
[3641.72 → 3648.84] basically you're halfway there now how does this work honestly I don't recall is this going through
[3648.84 → 3653.48] GitHub actions it is yeah so from GitHub actions okay, so this probably isn't even my code doing this
[3653.48 → 3657.64] it's probably just a GitHub action I installed yeah I think all right how'd I do it Gerhard how'd I do it
[3657.64 → 3662.20] it let me open it up because it's been a while since I looked at that and there's no pull request
[3662.20 → 3666.84] there's code so I have to go look that's me that's me no pull request yes spread across a couple of
[3667.32 → 3673.64] actually commits so that's also me yeah so you recognize that this is how I roll that's how you
[3673.64 → 3680.76] roll it is so I cannot be myself you know PR is actually aligned with the idea of topics in Zulip like
[3680.76 → 3688.60] you know to get code into a repo your way is PR driven topic driven yeah the reason why we do it
[3688.60 → 3694.60] that way or the reason why I prefer to do that way is because it provides an interface to a conversation
[3694.60 → 3699.00] right so if people want to check it out if people want to for example they just want to see the video
[3699.00 → 3705.24] of how the thing works well you go there it also allows me to capture a lot more content like how do
[3705.24 → 3709.64] you put a video in a commit message I mean you could put the URL but then where do you host the video
[3709.64 → 3716.04] with the pull request you can put all this context there to capture why did it, and it's useful for
[3716.04 → 3722.60] me as well so all the previous pull requests that we mentioned the 533 the 534 there is a section which
[3722.60 → 3728.52] which captures how does that thing work and that's me making sure that I ran it myself on a different
[3728.52 → 3733.48] machine to make sure that the thing works and how does it work and sometimes more often than not i
[3733.48 → 3739.00] find issues and I fix them it's just a more I don't know wholesome way of approaching something and
[3739.00 → 3744.76] I enjoy it I think it's more professional way as well however I still do commits have their
[3744.76 → 3750.60] place so I'm not dissing them I'm saying all I'm saying is like different approaches and different
[3750.60 → 3757.96] contexts and different ways of sharing that information I think your way is definitely better
[3757.96 → 3761.72] I think the difference between you and me is you want to have a conversation about this stuff
[3761.72 → 3766.52] mm-hmm and I just want to get stuff done, and so I just do stuff yeah and i for and then I'm like
[3766.52 → 3771.72] well Gerhard I'll figure out how to talk about it on Kaiden yeah that's it yeah so I off i offshore
[3771.72 → 3775.96] my conversations which reminds me how did I do this how did I accomplish this did you find it I think i
[3775.96 → 3781.48] just I must have just installed a GitHub action you do use a GitHub action this is I'm looking at in our
[3781.48 → 3788.12] changelog repository uh GitHub workflows dagger on namespace that's one that I'm looking at, and it's line
[3788.12 → 3795.00] right now 68 announce deploy in Kaiden Zulip, and you're using the Zulip GitHub action Zulip send
[3795.00 → 3801.80] message v1 you have an API key have the email organization URL two type topic content I think
[3801.80 → 3806.68] the content was the interesting one because you had to trim uh the git shah you had to use like a short
[3806.68 → 3812.60] shah I've seen a couple of commits where you were trying to fix I was tweaking that integrate exactly yeah
[3812.60 → 3818.92] yeah all right so yeah it's just basically you use an existing GitHub action, and you tweak it to
[3818.92 → 3824.20] your liking yeah and so it's even easier than writing your own API client which I did for all
[3824.20 → 3830.92] the other integrations but yeah this one was so easy I forgot yeah well it looks good it works well i
[3830.92 → 3838.28] was very happy to see this, and it's in the Kaiden channel it's exactly where it needs to be code deploys
[3838.28 → 3845.24] it's all there so Kaiden you can go and check it out that's very nice so the one thing which i
[3845.24 → 3851.48] had to do like as a follow-up pull request 536 right we have two of everything we are running the
[3851.48 → 3858.60] primary deploys through namespace they run dagger for us, and they run the actual the CI and CD parts as
[3858.60 → 3865.32] well, but we also run GitHub as a fallback so what we wanted to do is announce deploys in z loop as well
[3865.32 → 3869.48] on the GitHub runners so all I did was just basically copy what you've done jarred and
[3869.48 → 3873.88] put it there the fact that I copied it makes me think that you know there should be refactored
[3873.88 → 3878.44] there should be simplified in some way there's quite a lot of configuration so it's something for
[3878.44 → 3886.12] my list however we discussed in the last Kaiden the namespace runners and how much will they cost us
[3886.12 → 3898.20] per month right, so now the numbers are in, and we get to pick so option an it cost 50 50 yeah 40 cents
[3898.84 → 3910.12] I'm typing this up 40 cents so 0.4 dollars that's option one option no, no no I went too far I went too
[3910.12 → 3915.00] far hang on I'm doing this like as a live edit and I don't want to live editing his slideshow cool
[3915.00 → 3922.28] for those listening b is one dollar and c is two dollars how much do you think it cost us per month
[3922.28 → 3930.68] 40 cents a correct it was exactly 54 cents wait a second you just said 40 cents, and then you said
[3930.68 → 3936.44] correct, and then you said it was 54 cents well out of these options option an is closest to the reality
[3937.72 → 3942.20] I didn't give you the right number it was I didn't want to make it 50. It'd be too obvious I guess
[3942.20 → 3947.00] yes exactly yes so maybe I could have done like 0.5 it was yeah that would have made more sense
[3947.00 → 3954.92] there you go 0.5 say fixed it so half a buck half a buck for a month of namespace.so yeah concurrent
[3954.92 → 3961.80] runners that's what they're offering right it's a fast GitHub actions runner with caching built in
[3961.80 → 3966.36] and a bunch of features like for example nice UI it shows you how long your builds are taking
[3966.36 → 3971.72] um how much CPU they're using memory using so just get more insights into what's happening when
[3971.72 → 3977.00] the builds run right not a sponsor, but they certainly should be I think so they're on my
[3977.00 → 3983.00] list I really think so put that on your list Adam okay cool 2025 named that so I'm coming for you
[3983.00 → 3988.04] thanks for spotting us Gerhard this is on your credit card right it is yes 0.5 dollars so just
[3988.04 → 3992.68] invoice us for the first month we'll see how the next month goes the pay as you go thing is
[3992.68 → 3999.24] the basic, but yeah yeah pull request 535 this is also follow up uh we improved on the Zelig
[3999.24 → 4005.64] auth integration, so this is my problem this is my fault too yeah you remember it like the old way
[4005.64 → 4013.00] or we just basically configure environment variables like secrets in our fly.io app and um
[4013.80 → 4018.04] we don't want to do that the reason why we don't want to do that is because we have the one password
[4018.04 → 4023.64] CLI integration yeah which means that when the app boots just in time it loads all the secrets
[4023.64 → 4028.36] so that's what the 535 is yeah I just forgot about that so I just did the old-fashioned way
[4028.36 → 4032.44] and, so thanks for fixing it that's we have two of everything you want to back up you want to
[4032.44 → 4034.60] develop you up yeah cool
[4037.96 → 4044.68] what's up friends I love my eight sleep check them out eight sleep.com I've never slept better and you
[4044.68 → 4051.80] know I love biohacking I love sleep science and this is all about sleep science mixed with AI to
[4051.80 → 4057.88] keep you at your best while you sleep this technology is pushing the boundaries of what's possible in our
[4057.88 → 4064.52] bedrooms let me tell you about eight sleep and their cutting edge pod for ultra so what exactly is the
[4064.52 → 4073.32] pod imagine a high-tech mattress cover that you can easily add to any bed, but this isn't just any cover
[4073.32 → 4079.00] it's packed with sensors heating and cooling elements, and it's all controlled by sophisticated
[4079.00 → 4086.04] AI algorithms it's like having a sleep lab a smart thermostat and a personal sleep coach all rolled
[4086.04 → 4093.16] into one single device and the pod uses a network of sensors to track a wide array of biometrics while
[4093.16 → 4099.72] you sleep it tracks sleep stages heart rate variability respiratory rate temperature and more and the really
[4099.72 → 4105.88] cool part is this it does all this without you having to wear any devices the accuracy of this
[4105.88 → 4111.24] thing rivals what you would get in a professional sleep lab now let me tell you about my personal
[4111.24 → 4117.16] favourite thing autopilot recap every day my eight sleep tells me what my autopilot did for me to help
[4117.16 → 4122.36] me sleep better at night here's what it said last night autopilot made adjustments to boost your
[4122.36 → 4133.00] REM sleep by 62 wow 62 that means that it updated and changed my temperature to cool to warm and helped
[4133.00 → 4140.20] me fine-tune exactly where I wanted to be with precision temperature control to get to that maximum REM sleep
[4140.20 → 4146.20] and sleep is the most important function we do every single day as you can probably tell I'm a massive fan
[4146.20 → 4152.04] of my eight sleep and I think you should get one so go to eight sleep.com slash change log and right now they
[4152.04 → 4157.72] have an awesome deal for Black Friday going from November 11th through December 14th the discount code
[4158.20 → 4166.60] changelog will get you up to 600 off the pod for ultra when you bundle it again the code to use is
[4166.60 → 4172.76] changelog and that's from November 11th through December 14th once again that's eight sleep.com
[4173.32 → 4178.60] change log I know you'll love it I sleep on this thing every night and I absolutely love if it's a game
[4178.60 → 4184.92] changer, and it's going to change your game once again eight sleep.com slash changelog and also by
[4184.92 → 4191.16] our friends over at Wix I've got just 30 seconds to tell you about Wix studio the web platform for
[4191.16 → 4199.96] freelancers agencies and enterprises so here are a few things you can do in 30 seconds or less on studio
[4199.96 → 4209.00] number one integrate extend and write custom scripts in a VS Code based IDE to leverage zero setup dev test
[4209.00 → 4215.88] and production environments three ship faster with an AI code assistant and four work with Wix headless
[4215.88 → 4223.00] APIs on any tech stack Wix studio is for devs who build websites sell apps go headless or manage clients
[4223.00 → 4229.08] well my time is up, but the list keeps going on step into Wix studio and see for yourself go to
[4229.08 → 4233.56] wix.com studio once again wix.com studio
[4238.68 → 4244.44] all right we have a bit of more time so now we're going to go into one of my favourite topics that has
[4244.44 → 4249.72] become one of my favourite topics and that's the pipe dream yes what is a pipe dream tell us jarred
[4249.72 → 4255.48] the pipe dream is a world a future world in a world in which oh Adam should tell us he has the
[4255.48 → 4263.08] actual trailer voice in which you can just run your own little CDN with a varnish config deployed
[4263.08 → 4269.40] around the world on fly.io machines, and you don't need to have a CDN anymore because you've built your
[4269.40 → 4275.48] own CDN, and it makes sense, and you can just open source it and share it with the world and
[4275.48 → 4281.40] everything's simple, and you got 20 lines of varnish maybe 50 maybe 100 lines maybe 200 you
[4281.40 → 4286.60] have to update us on the lines of varnish still 60 we're still on 60 that has no chance that's
[4286.60 → 4291.32] pipe dream that's pipe dream single purpose single tenant CDN for changelog.com
[4292.20 → 4297.48] that runs varnish cache the open source one on fly.io so we've been we've been working towards
[4297.48 → 4303.16] this you've been building it last time around I remember saying can I can have test suite or something
[4303.16 → 4308.68] like that yeah pretty much and I know I looked at a test suite pull request so I think I know
[4308.68 → 4317.16] where this is going yeah so the issue that jarred opened in the true open source spirit is wire up a
[4317.16 → 4324.28] test harness that's right because I said uh create an issue open source for the win that's right did it
[4324.28 → 4330.36] you know i I opened that issue after listening to Kaiden 16 and hearing it back and you're telling me to open
[4330.36 → 4335.80] an issue I was like oh I never did so there I went did I even quoted myself and I quoted you in the
[4335.80 → 4342.44] issue yeah very nice you did that was amazing so that was issue two that was a pull request
[4342.44 → 4350.20] pull request three which adds tests yes so what is interesting about this well we're using just same
[4350.20 → 4355.96] as before one tool we seem to be standardizing on that yeah it runs just test and when we run when we
[4355.96 → 4363.88] run it is creates a report why does it create a report it uses this amazing tool many have heard of
[4363.88 → 4373.40] it hurls h-u-r-l not sure if it's the best name but anyway we didn't pick it hurl.dev and hurl.dev is
[4373.40 → 4381.48] orange open source it's a CLI that is actually it's more than the CLI, but you interact with it through a CLI
[4381.48 → 4391.96] which allows you to write tests and assertions about http requests so the focus is on testing http
[4391.96 → 4398.92] endpoints, and it's written in rust which means it's really fast it has a very simple DSL you put it in
[4398.92 → 4405.24] .hurl files and what does it look like well let's have a look at this fast changed so we're going to
[4405.24 → 4411.48] look at the fast changed there's a workflow which runs it, and it just tests that's it and when
[4411.48 → 4416.76] it comes to the hurl file I've put it in test by the way there's the just file we'll scroll past that
[4416.76 → 4424.12] let's look at this one test admin. Hurl we get the host admin we repeat it twice so that we can confirm
[4424.12 → 4432.20] the caching behaviour we expect the http status code to be 302, and we say we want http 2 you can specify this
[4432.20 → 4438.04] in the file when you do like your configuration, and then you can write a bunch of assertions in this
[4438.04 → 4444.52] case we make sure that the response comes back in a second by a thousand milliseconds in this case
[4444.52 → 4451.00] we check that the header the location header sends us back to home page right because we're not
[4451.00 → 4457.48] authenticated right we also check that there's an x varnish header because that means this request
[4457.48 → 4463.24] has been served by varnish we are looking at the age header which should be zero because they
[4463.24 → 4469.00] should never be stored from cache we look at cache status just to double-check and the miss the
[4469.00 → 4476.20] cache status header should contain in this case hits zero and should also always contain miss all this
[4476.20 → 4482.04] very nicely laid in a way that I think is easy to understand and the fact that we can do repeats too
[4482.04 → 4487.08] that's all we have to do to make sure the request gets run twice which I think is really nice
[4487.08 → 4494.60] yeah so this is like a hurl specific DSL which is text-based and as I said in your pull request
[4495.56 → 4500.44] seems super simple and easy to use so I'm excited about that so this is pull request three on the
[4500.44 → 4505.72] pipe dream and again there's a video how does this work so I'm just going to play through it there's no
[4505.72 → 4512.04] sound but the thing which I wanted to go to is this report which is really cool so after you run the test
[4512.04 → 4518.52] you can have a look at the output which shows you exactly the requests how they happened what headers
[4518.52 → 4525.40] were sent how did this behave which I think is really cool did you try running this locally jarred
[4525.40 → 4530.52] I watched your video I didn't try running it excellent so the video works, and you get like a nice waterfall
[4530.52 → 4536.76] like to see how much like different parts of the request take I think super useful so my question that i
[4536.76 → 4543.40] had after this which I didn't ask yet I was saving it was obviously you run the thing you get the
[4543.40 → 4550.28] report but I assume the thing also has some sort of automated one or zero at the end of it whether or
[4550.28 → 4555.56] not your tests passed without the report right the reports an additional thing it's not like the output
[4555.56 → 4562.20] that is correct yes that is correct so the report is separate so the report is separate from whether
[4562.20 → 4571.48] this the test was successful or not and right now this commit has failed, so this test on main has failed
[4571.48 → 4579.96] so we see the failure and the failure is that string edge grace hit stale should not contain string stale
[4580.60 → 4588.68] and it does and also the age like how long this has been cached for we expect it to be less than 60, but it's been 67
[4588.68 → 4595.72] so the system doesn't seem to behave the way we thought it would, so this is testing not
[4596.36 → 4603.24] the varnish config specifically this is testing the actual running yes nodes like this is the thing in
[4603.24 → 4609.72] production that is testing right yes that's it okay so it's almost like an integration test it is an
[4609.72 → 4614.92] integration test yes how would you use it for development then right, so this is the big thing which
[4614.92 → 4622.20] which is currently is missing it's not testing the configuration that is local it's
[4622.20 → 4626.52] testing the deployed configuration I see that's what I was just asking about yeah because what I want
[4626.52 → 4634.60] to do is TDD some changes exactly so for that we need to put more stuff which spins up varnish locally
[4635.16 → 4642.60] and then the question is should the local varnish hit changelog the origin or should we also spin up an
[4642.60 → 4648.68] origin are you asking me that are you saying yeah we are going through this to see because
[4648.68 → 4652.28] here are the questions that we need, I couldn't tell that's a rhetorical question or no, no he's the
[4652.28 → 4657.80] question that we need to answer so that we know how do we want to continue developing this because
[4657.80 → 4663.88] based on what we choose there's almost like different trade-offs and different levels of how hard this is
[4663.88 → 4671.16] going to be so do we for example want to run the entire changelog app locally and if we do then we
[4671.16 → 4676.52] need the database as well which we can do it's not a problem, and then we put varnish in front which is
[4676.52 → 4682.44] the one that we develop right just in time loaded with the varnish config, and then we run the test right
[4682.44 → 4688.04] so we need almost like four things to be running locally to be able to test everything how the entire
[4688.04 → 4697.00] system fits together my desire would be to have my changes and additions to the pipe dream config aka
[4697.56 → 4705.16] varnish tested to assure that what I'm changing actually affects its way upstream or downstream
[4705.16 → 4710.04] whichever way you want to look at it right I do not care in this context whether the upstream or the
[4710.04 → 4715.80] downstream actually work correctly in fact I would like to be able to mock them in different ways like
[4715.80 → 4721.64] what if the app doesn't respond the way we expect to i would like to mock that response from the app
[4722.44 → 4727.96] because the app's interactions and stuff is all tested elsewhere and then our other upstreams is like
[4728.68 → 4733.48] Cloudflare r2 that's it and so like that's outside our control right so we don't want to test that
[4733.48 → 4738.04] that thing's working as it should so I think we just want to keep it isolated to pipe dream and not
[4738.04 → 4744.12] like spin up an entire working system with nodes around the world and stuff like that okay does that answer
[4744.12 → 4748.52] your question it does answer my question yes that's exactly what I was thinking I just want to double
[4748.52 → 4753.80] check if you're thinking about it the same way, and it seems that you are right we only care about the
[4753.80 → 4760.68] configuration and pipe dream itself yeah and how it interacts with origins different origins in this
[4760.68 → 4767.08] case right that I mean to begin with we can just point it to those origins so that won't change but what
[4767.08 → 4772.44] will change is that we are testing the thing that is being developed the local thing we're not testing the
[4772.44 → 4776.68] thing which is being deployed because the reason why I wanted to obviously test the local thing is
[4776.68 → 4782.20] well is my change going to work before I push this out absolutely, and we could even take those origins
[4782.20 → 4790.04] responses and do something like a VCR and have those be play backed played back yes, yes, and then we avoid
[4790.60 → 4797.16] production altogether VCR remember VCR yeah for exactly for people that don't know ruby are not coming
[4797.16 → 4802.36] from that world like the moment you said that like of course VCR and the cassettes and damn it I had to
[4802.36 → 4808.12] recreate them, so many times right but yeah I remember that yeah it's an it's a ruby gem which
[4808.12 → 4814.52] basically allows uh http requests to be recorded and replayed so that you don't make the real requests
[4814.52 → 4820.76] that's right and for those people who are even less old originally VCR was a tape-based medium in which
[4820.76 → 4827.32] you could record and play back television the OG VCR yeah I hated those movies because the quality was
[4827.32 → 4832.76] so bad and like the more you watched it the worse it would get the worse you get because yeah the
[4832.76 → 4839.08] media would degrade so yeah luckily we don't have that problem anymore plus my original Star Wars VCR
[4839.08 → 4843.88] which was recorded off of television it got recorded over like halfway through for like a
[4844.60 → 4848.92] basketball game or something it's like goodness gracious man trying to watch Star Wars here you
[4848.92 → 4856.04] know what's funny about VCR it stands for video cassette recorder, but you would use a VCR to play
[4857.08 → 4863.24] primarily right as a user you could do both for both you can but like generally most people assimilate
[4863.24 → 4869.32] or you know think of the VCR as you put a cassette in yeah, and you play it is all right to say is like
[4869.32 → 4877.32] the general usage is not so much the art part of if it's the VCP video cassette player I think what we
[4877.32 → 4881.80] learn here is separation of concerns is a good thing you know don't make the recorder and the
[4881.80 → 4886.20] player in the same exact medium you're going to record over my Star Wars, but you remember the
[4886.20 → 4892.20] safety mechanism that cassettes had there been a latch if the latch was on you couldn't record over it oh
[4892.20 → 4899.16] yes the tab yes, and you can just tape over it right physical little thing oh gosh the days
[4899.16 → 4905.72] the bad old days okay so this all makes sense I think for this what I would do and again that's
[4905.72 → 4911.32] why we're talking about this I would introduce dagger for this the reason why I would do that is
[4911.32 → 4917.80] because I need to create containers quickly programmatically I need to create services connect
[4917.80 → 4924.12] into multiple containers together and check that everything works in a programmatic way and if we don't
[4924.12 → 4929.32] have that we would need to have some sort of container runtime to run all these things so that's
[4929.32 → 4937.48] what I'm thinking here sounds good SGM cool make it so we're almost at the end this is
[4937.48 → 4944.60] what happy we have been building up let's see how this lands so we talked a few name ideas in the last
[4944.60 → 4953.56] Kaiden for pipe dream correct what do you remember as a name that stuck with us all ripely ripely ripely
[4953.56 → 4963.16] okay so we threw around a couple of domain names uh correct so one that we liked that we all liked
[4963.16 → 4971.00] let's like load like a who is oh gosh who is who let us do who is do you remember the main which we
[4971.00 → 4980.12] wanted no it was pipe dot LI pipe dot LI that was I think that was already registered as far as no it's
[4980.12 → 4985.72] unavailable actually we can't even register it ah so for shame yeah I mean it says it's already
[4985.72 → 4992.76] registered you know there's no info yeah dot LI domains are difficult for various reasons
[4992.76 → 4999.32] so what was the other TLD that we wanted tech ripely dot tech let's see if ripely dot tech is
[4999.32 → 5007.64] available no someone registered it when did they register it let's see what happens if you go to ripely dot
[5007.64 → 5018.28] what's the other TLD tech oh gosh oh somebody else has the idea a new CDN is born
[5019.48 → 5026.60] what do we see it looks like it what are we looking at three uh this is us
[5026.60 → 5035.24] get out of here are these are uh the three magi that oh goodness Christmas new things get born
[5036.44 → 5040.36] so a CDN is born oh the stars in the sky
[5042.52 → 5048.92] the CDN has risen I don't want to burst your bubble gear heart, but it wasn't three magi three wise men
[5049.48 → 5053.72] yeah what was it well it was a group of wise men there were three gifts given and so people always
[5053.72 → 5057.64] think there was just three of them, but people don't read the account very closely, but this is
[5057.64 → 5061.72] cool looking I actually thought of like these were Jedi at first so I thought you're going because that
[5061.72 → 5068.92] looks like a futuristic city out there yep certainly that's not uh Jerusalem or no Bethlehem or anything in
[5068.92 → 5076.60] the in the story looks like Dubai it does look like Dubai so you know maybe a modern take but uh
[5076.60 → 5082.28] hilarious a new CDN is born ripely coming what coming on the 25th or what are you trying to do here
[5082.28 → 5092.76] maybe I don't know so if you go to pipely.tech is a domain, and it tells the whole story right so
[5093.32 → 5099.80] should we build a CDN I can click on that oh cool that's us that's always three that's interesting so
[5099.80 → 5105.40] three seems to be the theme here not two three so we're going now there's three wise men is that
[5105.40 → 5112.04] what you're going to say I like it, I think so I think so comparing CDNs that's that as well with nice
[5112.04 → 5117.56] screenshots we have so the whole story the whole ripely story which I really like I like the name
[5117.56 → 5123.96] ripely I'm sold on it, you sold on ripely well you bought it pipely.tech yeah it's a thing now
[5123.96 → 5131.32] that's the one that I remember mm-hmm I like it, I'm so down like beyond so down ripely's coined
[5131.88 → 5139.00] can I share some behind the scene nuggets this is fresh this is on a pod coming to you soon actually next
[5139.00 → 5148.28] week's Wednesday so on Wednesday of this week which is the week of I guess the fourth no what was Monday
[5148.28 → 5154.68] the second Monday was uh second yeah, yeah second December second it's December 6th so on December
[5155.40 → 5162.68] 4th I had a conversation with Kurt Mackie and I think you know his name because he's the one of the
[5162.68 → 5170.84] founders and CEO of fly.io which we know and love here obviously I love fly so much it's so cool and
[5170.84 → 5177.56] during that conversation because we talked about Tigris and the rebel alliance he said it out loud
[5177.56 → 5182.44] on the pod so I thought it was secret we talked deeply about the rebel alliance and all the things
[5182.44 → 5187.24] that he had envisioned for it, and he's not I won't spoil it let's just say that's not the point
[5187.24 → 5192.28] I'm trying to make I said go to this URL and tell me what you think about this and I mentioned
[5192.28 → 5199.56] this pipe dream idea and I had forgotten about ripely until this moment in terms of a name i
[5199.56 → 5204.52] laughed so hard the last time we said it and I'm the one that said it but uh Gerardo mentioned in the
[5204.52 → 5212.04] podcast and so that conversation was focused around you know the pipe dream idea, and he looked at it
[5212.04 → 5217.96] he's like I love this is so cool I can't believe you guys are doing this so I'll just say
[5217.96 → 5226.12] that in the fact that Kurt is excited about this and there is this idea of a rebel alliance just saying
[5227.40 → 5238.84] so we have support and a blessing and a fan yeah and a name and a name and a story and a domain and a
[5238.84 → 5244.60] domain exactly gosh it is really does begin with a name and a domain because you can have a good name
[5244.60 → 5248.76] I was actually bummed I was like holy crap somebody took pipely.tech who had this idea
[5250.92 → 5253.80] that is so cool yeah I mean you did
[5256.28 → 5262.52] I just had the execution okay that's cool let's go for it, i I love the creativity though I love
[5262.52 → 5267.16] the idea that this might be Jedi honestly and this is a futuristic city with this star out there
[5267.16 → 5273.96] the rebel alliance is born yeah I think this is just really it plays in well i I like it a lot I'm
[5273.96 → 5279.64] beyond excited i I don't know how much to share in this podcast but I'm like beyond excited well I'm
[5279.64 → 5286.44] glad this is a great way to begin something new and I didn't know that you'll make room for this but
[5286.44 → 5291.88] I think you just did without knowing that ripely would be a thing think about how we began and think
[5291.88 → 5297.40] where we're now to rewind the conversation back to the beginning like jarred said something to me
[5297.40 → 5303.40] jarred don't jarred I don't see each other face to face too frequently a couple of times a year and it
[5303.40 → 5308.28] actually I've said this on the air I think I said this in face to face, but he said to me, he's like
[5308.28 → 5312.28] Adam when you tell me new ideas it's like almost immediately cancel them because we have no time to
[5312.28 → 5317.40] do anything and I'm paraphrasing what you said, but the sentiment is roughly there so correct me jarred if
[5317.40 → 5322.28] you want to but it kind of bummed me out because I'm generally not so much the idea guy but like
[5323.00 → 5327.72] someone sort of like generating vision in some way shape or form and like when he said that i also
[5327.72 → 5333.40] thought in my brain at the moment like gosh I've kind of stopped like casting any sort of vision in my
[5333.40 → 5340.68] own brain because I'm kind of tapped too so like anytime I have a new idea I don't have any room to
[5340.68 → 5347.24] explore it because we're doing all the ideas we can essentially and I think and I don't know where
[5347.24 → 5353.48] jarred's at with this but I would so make room for I think this certainly makes room for ripely, and it's
[5353.48 → 5360.12] certainly the main thing because we need an amazing CDN and I shared in that podcast with Kurt some of the
[5360.12 → 5365.56] challenges he said well you know Adam that uh quickly and Cloudflare and every CDN out there is not
[5365.56 → 5373.00] it's not in their best interests to cash your all of your content on all their pops across the globe
[5373.56 → 5378.04] forever that's not in their best interest they there's cash misses not because they can't cash it
[5378.04 → 5384.44] because they don't want to and so the CDN we build that we want to build will always cache everything you
[5384.44 → 5391.16] need to across the globe, and it will only expire when you say this is expired there will never be a
[5391.16 → 5397.40] cache miss in this world and that to me is what a CDN is and so if we can build that world I think
[5397.40 → 5402.60] other people like that that world and I think people don't need and this is even curt concurring
[5402.60 → 5408.52] this like I don't think everybody needs what these larger CDNs can offer or do offer because they just
[5408.52 → 5414.76] offer so much more than you need so I think there's a lot of a lot of opportunity here honestly
[5414.76 → 5421.96] I like it, I'm behind it, I could tell as much time or as little time as I have you know little by
[5421.96 → 5428.04] little step by step I mean this is honestly like mornings and evenings and weekends and all sorts of
[5428.04 → 5433.80] like the time to the point doesn't even matter as much time as I have I enjoy doing this and on top of
[5433.80 → 5440.52] all the other things, and it's fun and I can see the need I can see me wanting to use this me wanting to
[5440.52 → 5449.64] build this and just i I honestly see this improving a bunch of things and if it doesn't work out it
[5449.64 → 5456.28] may not work out the story is amazing and at the end of the day that's what people remember we tried
[5456.92 → 5465.16] we showed up every day and let's see what happens we came we saw we dreamt we pipe dreamt we pipe dreamt
[5465.16 → 5472.36] and uh we pipe lead we pipe lead dot tech the pipe piper we'll be like the three of us are the pipe pipers
[5474.04 → 5483.32] look at me so in all honesty I think the reason why uh these magi they are faceless is because it can be
[5483.32 → 5491.96] many other people I know that we had mad Johnson help us we had jams a Rosen help us and how many
[5491.96 → 5495.88] people out there are doing something similar maybe they don't have time maybe they want to
[5495.88 → 5502.20] they're thinking about it crazy groups of people that have an idea and just go for it, you know it
[5502.20 → 5509.40] doesn't matter where it goes or how far it goes as long as you have fun with it and yeah don't take
[5509.40 → 5515.08] it too seriously I suppose it's not about the profit it's not about like this VC funding or at least
[5515.08 → 5519.96] that's how I think of if it's an idea that we should keep investing in because it's the right thing to do
[5519.96 → 5526.92] do, and it's a great story to tell looking back 10 years from now 20 years from now be like wow we
[5526.92 → 5534.84] were part of that on I guess a different note how close are we to this pipe dream not being a pipe dream
[5535.48 → 5544.12] how real and how quickly can this be truly real if it's not real so honestly it just depends on how much
[5544.12 → 5552.44] time me personally can dedicate to this over the next coming months that's that's what this comes
[5552.44 → 5557.16] down to I don't mean ripely the company or anything like that I mean like our usage of pipe dream our
[5557.16 → 5563.48] usage okay the thing becoming real for us as the first in quotes customer if that's the thing like
[5563.48 → 5572.68] true usage does it make sense can it scale for us is it truly Devi usable etc and then I think
[5572.68 → 5578.04] everything else after that is just like comes natural if it makes sense so let's talk through the
[5578.04 → 5583.48] roadmap we have it right in front of us we've added tests we know there's more that we need to do here
[5584.04 → 5588.76] but the same number of VCR lines so that's still there the functionality hasn't changed
[5588.76 → 5595.32] the feeds backends the only reason why this is not done is that I wanted to do pipely.tech
[5595.32 → 5600.20] I thought that was a cool idea that's the only reason I did part of it by the way this now works
[5600.20 → 5606.52] it didn't use to work the feed XML now this loads we only had HTTPS so I've taken small steps towards
[5606.52 → 5611.96] it, but it's not complete the reason why we need http and not HTTPS because we're using the open source
[5611.96 → 5618.60] varnish and that does not terminate TLS so we can only connect to http backends that's something that
[5618.60 → 5625.40] we discovered the hard way so this as in terms of configuration we're talking a few hours to get
[5625.40 → 5631.40] it all done lift it from our existing ICL and maybe do a few changes right because this already exists
[5631.40 → 5640.84] as ICL in our fast config then sending logs to honeycomb this again a day roughly it's just like
[5640.84 → 5644.92] I'm just basically making stuff up because they don't only once you pick it up you realize how much
[5644.92 → 5651.56] like yeah all the rabbit holes well we still have to determine if the way we send logs the fast way
[5651.56 → 5656.52] is the way of the future you know we know that we like a lot about what that does real time etc I'm
[5656.52 → 5661.96] assuming that's what you mean by that so it's more around making sure that we send logs to honeycomb
[5661.96 → 5667.40] so we can understand what's happening in the system yeah we want to keep the same structure as fast so
[5667.40 → 5672.36] that all the queries will work, so there'll be like no interruption of service or like no big changes
[5672.36 → 5677.88] so that's why I mentioned this we just need to have some way of sending all the request logs to
[5677.88 → 5683.48] honeycomb that that's what I mean by this we also need to send logs to s3 this is something that jarred
[5683.48 → 5689.40] mentioned last time uh when we talked about pipe dream and the roadmap so we need for stats we
[5689.40 → 5694.28] need to set just like to keep the compatibility right what about swapping out tigers for that or
[5694.92 → 5699.96] min Io or mini if we wanted to not s3 it is there any reason to not do that it doesn't matter where
[5699.96 → 5705.24] we send the logs as long as we send logs to a s3 compatible API gotcha which I tried to switch
[5705.24 → 5713.64] over to r2 by the way but I couldn't because of the way r2 implemented streaming versus the way s3 does
[5714.20 → 5719.56] and the way quickly actually pushes over to that interesting, and so we could have been on r2 entirely
[5720.28 → 5725.48] but we're actually in both now because our logs still go to s3 and everything else goes to r2 now we
[5725.48 → 5731.24] wouldn't have that problem inside pipe dream necessarily so it could be sent logs to r2 but
[5731.24 → 5736.76] we want to keep the exact same format so that our analytics stuff doesn't get rewritten exactly yeah
[5736.76 → 5741.72] so once that's why we do like the first part which seems a bit easier to just send the requests it
[5741.72 → 5746.28] doesn't matter which way you do them honestly, but this will ensure that the service behaves the way it
[5746.28 → 5751.96] should and I think this is more valuable from a functionality perspective than fairly hard to
[5751.96 → 5757.16] implement purge across all app instances I say fairly hard oh ban I can see me and jarred getting
[5757.16 → 5762.68] together here because we need to figure out how to purge these correctly and how to do this from the app
[5763.24 → 5769.72] right so the application itself will know which are the pipe dream or ripely instances and will send
[5769.72 → 5774.60] these purge requests, and we're looking at the fly Io machines like we're running the same network
[5774.60 → 5779.16] we can discover them we have DNS, so a lot of the building blocks are there, but this is where the
[5779.16 → 5785.24] application needs to come together with the actual CD and runtime in this case fly.io to implement this
[5785.24 → 5793.56] purge via Oban and like how we do things so we don't introduce a third or an extra service and then adding
[5793.56 → 5798.28] the edge redirects this is really easy because it's just basically adding more ICL config most of it is
[5798.28 → 5808.36] copy and paste maybe a few adjustments so it's very feasible, and we're talking I would say maybe weeks of work
[5808.36 → 5815.32] work in total but weeks of work spread over a long period of time that's what's hard like the time on
[5815.32 → 5821.88] my part you know have the time to actually go through all these things but I can make this my focus that
[5821.88 → 5828.84] is a possibility where should we end this pod should we end it right here the possibility of these uh
[5829.64 → 5836.36] these Jedi wise dudes bring into fruition the ripely dream yeah I think ripely is a good idea
[5836.36 → 5841.88] new CD, and he's born I mean we can see the journey that we've been on right since January that's when
[5841.88 → 5847.08] he started talking about was like the first Kaiden this whole year yeah so you know we have been taking
[5847.08 → 5853.00] all these small steps towards it, we were uncertain for a long time you know is this real should we
[5853.00 → 5858.92] really do this is a good idea so we weren't like all in to begin with and i think that
[5858.92 → 5864.92] we are getting close to being all in as in let's go for this let's implement it let's see how it would
[5864.92 → 5871.24] work in practice like most of the problem space I think we have discovered it like we know like what
[5871.24 → 5876.68] are like the big items not the actual implementation, but this seems a lot more feasible and a lot more
[5876.68 → 5881.64] realistic than it was in January for example when it was just a question and I think now it's not like
[5881.64 → 5887.08] like we're building it is like we are I would say maybe a third way through maybe a quarter through
[5887.08 → 5893.16] something along those lines and there's still challenges around for example like the TLS termination
[5893.16 → 5901.80] that is a big one and that means that we can only proxy or forward request the origins they have to be
[5901.80 → 5908.52] http the backends as match calls them have to be http I think that's not a problem for us, it's not a
[5908.52 → 5913.00] problem in the context of fly because everything is running like we have a private network so all
[5913.00 → 5918.68] the endpoints are http, and they're private no one can connect to them so I think that makes sense
[5919.40 → 5924.84] r2 can also be public it's its not a problem and when it comes to pushing logs that's the one thing
[5924.84 → 5930.44] which I don't know but honestly I don't see varnish being the thing which will push the logs anyway
[5930.44 → 5936.36] what I would use that I've been using for years is vector.dev vector.dev is a great tool
[5936.36 → 5941.96] for sending logs and metrics or anything like that anywhere data that required them you know
[5941.96 → 5947.96] since I've been using them but since I've been using vector, but it's all very simple and straightforward
[5947.96 → 5953.56] and even to this day I use it in the context, and we use it in the context of the dagger infrastructure
[5953.56 → 5957.64] this is a very important component and other teams are using it in their own infrastructures that
[5957.64 → 5963.32] we are collaborating with so vector seems to be the piece to pick and the tool to use in this
[5963.32 → 5971.72] context again written in rust super performant nice CLI has a lot of things so I think the building
[5971.72 → 5978.44] blocks are getting clear just a matter of going for it new beginning new year I think that could be
[5978.44 → 5985.24] the focus let's go for it man let's do it right let's do it so excited good stuff Gerhard always
[5986.12 → 5992.92] always a pleasure man so fun I'm impressed it is always a pleasure make a great team really do we do
[5992.92 → 5998.76] make a great team we do great things together and uh we've stood the test you've been here
[5999.32 → 6006.28] Gerhard since the proverbial beginning you know the new beginning the latest era not
[6006.28 → 6011.88] including this new one we're about to go on to yeah 2016 like 2015 and that really brings my heart a lot
[6011.88 → 6019.08] of joy honestly i I like relationships that stand the test of time really obviously that's a good thing for
[6019.08 → 6025.08] relationships, but it's uh yeah it brings me a lot of joy that's all I'll say I guess I'm excited
[6025.08 → 6036.28] likewise pipely.tech we have it OMG we have if it's real a new CDN is born let's do it kaizen
[6036.28 → 6049.72] Kaiden oh my goodness that was a fun Kaiden even though we had some serious talk up front there were
[6049.72 → 6055.88] lots of laughs lots of progress being made of course and lots of surprises Gerhard always has something
[6055.88 → 6062.76] up his sleeve by the way I'm sure some of you are sad and or upset by our 2025 plans and I totally get
[6062.76 → 6069.24] it I've had my favourite podcasts and indie shows go away so I know exactly how that feels hopefully
[6069.72 → 6075.72] this will be a net positive in the long run and even if not we've had a lot of fun all these years
[6075.72 → 6081.80] haven't we next week on the changelog it's news on Monday our final edition of the year so I'm doing
[6081.80 → 6089.16] a roundup of all the code pros and pods that shaped 2024 and our interview on Wednesday is gonna
[6089.16 → 6096.04] be a banger Mitchell Hashimoto joins us for a deep dive on forty his new terminal emulator
[6096.04 → 6101.64] that's so good and shipping out to the public before the end of the year and on Friday our
[6101.64 → 6108.04] seventh annual state of the log spectacular it's almost too late to get your voicemail in but if
[6108.04 → 6114.28] you're listening to this on the 13th or maybe the 14th go to changelog.fm slash soil and leave us a
[6114.28 → 6120.28] message it means a lot one more thanks to our partners at fly to break master cylinder who's hard
[6120.28 → 6125.24] at work on our state of the log voicemail remixes and to each one of you for listening to
[6125.24 → 6132.04] our shows we love that you choose to spend time with us each week that's all for now we'll talk to you
[6132.04 → 6146.04] again next time
[6146.04 → 6163.88] finally the end of change logging friends with Adam and jarred some of the random we love that you love
[6163.88 → 6172.12] didn't stay until the end, but now it's over its time to go we know your problems should be coding
[6172.12 → 6183.08] and your deadline is pretty foreboding your ticket backlog is an actual problem so why don't you go inside
[6183.08 → 6189.88] no more listening to change lock and fence the badminton chamber in Silicon Valley
[6189.88 → 6200.12] and no one gave the gag will come to an end, but honestly that will probably be our finale
[6202.12 → 6205.08] the end of the day
[6205.08 → 6211.08] you best be slinging ones and zeros and that makes you one of our heroes
[6212.28 → 6217.96] your list of to-do's is waiting for you so why don't you go inside
[6218.68 → 6221.08] no more listening to change lock and friends
[6221.08 → 6230.04] change lock and friends
[6230.04 → 6232.04] change
[6232.04 → 6232.52] change
[6232.52 → 6233.48] and talk to your friends
[6233.48 → 6236.76] it's you're a favourite ever show
[6236.76 → 6241.88] favourite ever show
[6242.68 → 6243.48] by
[6243.48 → 6244.68] you
[6244.68 → 6245.88] energy
[6245.88 → 6248.04] a
[6248.04 → 6248.60] light
[6248.60 → 6250.06] a
[6250.06 → 6250.68] good
