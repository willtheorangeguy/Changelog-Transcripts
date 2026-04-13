[0.28 --> 3.16]  I'm Talatair, and you're listening to The Changelog.
[12.62 --> 16.40]  Welcome back, everyone. This is The Changelog, and I'm your host, Adam Stachowiak.
[16.50 --> 22.62]  This is episode 183, and on today's show, Jared and I are joined by Talatair.
[23.04 --> 26.86]  We talked about speech recognition, and specifically his project called Anyang.
[26.86 --> 32.40]  So if you heard that name before, and you listened to Arrested Development, or you watched that show, you know what I'm talking about.
[32.88 --> 38.30]  We also talked about Offline first and his project UpUp, and we also talked about promoting open source.
[38.84 --> 44.80]  We had four awesome sponsors, CodeShip, TopTow, Braintree, and also OpBeat.
[45.22 --> 47.46]  Our first sponsor for today's show is CodeShip.
[47.76 --> 52.72]  If you haven't checked out the blog from CodeShip, go check it out, blog.codeship.com.
[52.72 --> 56.98]  And there was a recent post I want to mention from Barry Jones titled Why Docker?
[57.44 --> 62.64]  And he dives deep into why Docker became a household name, why Docker instead of VMs.
[62.94 --> 71.98]  He even goes into how Docker enables consistent environments, and even the fact that Docker isn't going away, he makes that hypothesis that it's not going away.
[72.38 --> 74.86]  There's also an e-book mentioned in that article.
[75.02 --> 75.50]  It's free.
[75.92 --> 77.08]  It's from CodeShip.
[77.50 --> 78.96]  Super awesome e-book.
[79.06 --> 81.26]  It's titled Why Containers in Docker are the Future.
[81.26 --> 82.82]  This book is awesome.
[82.90 --> 83.56]  Go check it out.
[83.86 --> 87.80]  The link is in the article, and I'm going to put a link to the article in the show notes.
[87.88 --> 90.36]  So check out the show notes, and now on to the show.
[96.08 --> 96.96]  All right, we're back.
[97.02 --> 98.38]  We've got a fun show lined up today.
[99.34 --> 104.10]  I got an American accent, so I'm not going to say his name right, but the American way is Tal Ateir.
[105.72 --> 107.42]  Great open sourcer.
[107.74 --> 110.08]  Maybe a little mention to the end of the show.
[110.08 --> 113.72]  But Jared, this show has been teed up for a bit now.
[113.78 --> 116.26]  Can you talk a bit about the plans for getting Tal on the show?
[116.94 --> 117.14]  Yeah.
[117.28 --> 123.88]  Well, Tal, I think we first met you around your open source library on Yong, which was a couple of years ago.
[125.00 --> 129.98]  Recently, you released UpUp, which made a decent splash.
[130.18 --> 139.40]  And in the conversations around those two things, you mentioned that you got married, quit your job, on a six-month honeymoon, or traveling the world and working on open source.
[139.40 --> 139.88]  Wow.
[140.60 --> 142.08]  That's the dream right there.
[142.52 --> 143.68]  This guy's living the dream.
[143.76 --> 144.54]  Let's get him on the show.
[144.64 --> 145.02]  That's right.
[145.38 --> 146.30]  Well, welcome to the show, Tom.
[146.66 --> 146.90]  Yeah.
[146.94 --> 147.54]  Thanks, guys.
[147.84 --> 150.20]  So, yeah, actually, I said the name perfectly, Tal Ateir.
[150.20 --> 159.82]  Um, so, yeah, I've been, uh, so just to start, I'm, if anyone is worried about the accent here, it's me, not you guys.
[159.82 --> 163.88]  Like, I've been practicing for two weeks how to say the name of my own library.
[163.98 --> 166.58]  Like, UpUp, am I saying, is it an application?
[166.74 --> 167.22]  Is it Up?
[167.26 --> 168.68]  Like, I don't even know how to say it.
[168.68 --> 171.44]  Um, so you guys are good.
[171.54 --> 172.84]  Maybe give us, give us your roots.
[172.84 --> 175.46]  Where are you from and, um, how'd you get into this whole gig?
[176.58 --> 180.60]  So I'm a developer from Tel Aviv, Israel.
[180.80 --> 183.22]  As you can hear, um, developer.
[183.22 --> 192.00]  I've been a product guy, um, entrepreneur, um, maker, creator, all those stuff.
[192.50 --> 198.86]  Um, and yeah, as you said, like the, the slogan I like to attach to myself is, uh, I quit my job for open source.
[199.38 --> 200.62]  So you don't hear that every day.
[200.68 --> 204.42]  You can also, yeah, you can also add crazy to the list based on that.
[205.38 --> 209.72]  Well, the question is you're, you're newly married.
[209.72 --> 212.56]  So does your, does your wife think you're crazy?
[213.88 --> 214.32]  Yeah.
[214.48 --> 221.18]  So I guess we're going to have to talk about sustainability in open source at some point, a little bit of spoiler.
[221.66 --> 229.54]  Um, but yeah, I'm still figuring that out, but, uh, still took the, the jump and the plunge into it and let's see how it plays.
[229.92 --> 234.38]  So before you were doing open source, you're a developer and a product guy.
[234.60 --> 239.10]  You have a long history of, uh, working in the industry, writing code.
[239.10 --> 241.60]  What have you been up to before you quit your job for open source?
[243.22 --> 245.74]  So basically I've been doing this all my life.
[245.88 --> 251.72]  I mean, my, at around the age of seven, my dad got me a Sinclair Spectrum ZX.
[251.96 --> 253.80]  If you guys remember that one.
[254.34 --> 259.16]  Um, it was basically just a keyboard that you connected to a tape recorder, which connected
[259.16 --> 259.82]  to your screen.
[259.82 --> 262.74]  Um, and, um, you could program basic on that little thing.
[263.04 --> 267.80]  And, um, I didn't even know the, the English alphabet at that point.
[267.80 --> 269.58]  And I was already learning how to program.
[269.58 --> 274.60]  Um, I would go learn, uh, at a class, come home and my dad would teach me the ABC.
[274.82 --> 277.08]  So it was a bit of a slow start.
[277.84 --> 280.12]  Um, but I've been doing that ever since.
[280.12 --> 287.34]  I mean, in high school, um, and the minute they finished high school, went right into it.
[287.52 --> 291.38]  Um, after the army, of course, um, during the army even.
[291.38 --> 296.02]  Um, and I've, I've been building websites since 96.
[296.36 --> 297.88]  So it's almost 20 years now.
[298.40 --> 301.26]  That's the thing in Israel where you have to serve in the military, right?
[301.44 --> 301.64]  Yeah.
[302.12 --> 302.38]  Yeah.
[302.76 --> 305.70]  I had a friend, uh, from back in the day, his name was Dion.
[306.36 --> 309.04]  Probably similar where I pronounced his name incorrectly.
[309.66 --> 315.26]  Uh, or, you know, with my English American accent, but he was like, he lived here in the States
[315.26 --> 317.88]  and then he had to go back home because he was studying here.
[317.96 --> 320.12]  He had to go back home and serve in the military for a couple of years.
[320.12 --> 321.36]  And I was like, oh, that's, that's crazy.
[321.44 --> 322.80]  So they, they force you.
[323.22 --> 326.24]  What's like, not re it's not, uh, I shouldn't say forced.
[326.90 --> 329.50]  Um, you have to, it's maybe that is forced.
[329.56 --> 329.86]  I don't know.
[329.90 --> 330.66]  What can you say?
[330.84 --> 337.46]  I mean, you have to, but anyone who wants to get out of it can, um, it's, I mean, it's
[337.46 --> 338.32]  like getting ways.
[338.52 --> 338.70]  Yeah.
[338.74 --> 339.38]  There are ways.
[340.60 --> 347.18]  Um, but yeah, I mean, that didn't stop me from, uh, like continuing to, to, to read
[347.18 --> 350.10]  up and like, I would walk around with little, I would.
[350.12 --> 355.64]  Print out programming books and little, uh, um, pieces of paper and put them, uh, in
[355.64 --> 358.30]  my, you know, in my uniform and read them whenever I could.
[358.52 --> 360.18]  Like I took every minute I could.
[360.84 --> 363.92]  So you, you put guard duty to, uh, to its truest form there.
[364.02 --> 365.36]  You were guarding and learning.
[365.68 --> 366.16]  Yeah.
[366.16 --> 370.02]  So yeah, actually, I actually did that while, while on guard duty.
[370.54 --> 371.02]  Yeah.
[371.42 --> 376.16]  Um, so yeah, basically 20 years, which makes me sound really old.
[376.26 --> 377.44]  I'm 35 now.
[378.10 --> 382.10]  Um, and so basically in my entire life since high school.
[382.76 --> 390.06]  It's interesting to hear that perspective that you're, um, you know, that it was so
[390.06 --> 392.52]  important to you that you would go to any length.
[392.58 --> 396.12]  It seems like, you know, even printing out a programming book and kind of putting it in
[396.12 --> 400.60]  your shirt pocket, your uniform to, to, you know, find a way because of this passion.
[400.60 --> 401.04]  Yeah.
[401.94 --> 407.06]  Um, I find myself to be extremely lucky to still be so passionate about what I'm doing,
[407.06 --> 409.16]  um, and love it so much.
[409.16 --> 411.56]  And if anything, it grows with time.
[411.56 --> 414.40]  Like I still love it as much, so much fun.
[414.66 --> 419.72]  Like, and there's so much happening right now in, uh, with web development and JavaScript
[419.72 --> 424.24]  and, and everything is changing so fast and new things are coming out.
[424.24 --> 427.00]  So it's, it's, it's just exciting all the time.
[427.64 --> 430.56]  Um, I gotta ask you just because you mentioned it.
[430.60 --> 434.62]  But, uh, the programming book, can you recall what you may have been studying then?
[434.64 --> 437.44]  Like what languages, what paradigms, what, what in particular?
[438.08 --> 441.58]  Uh, so this is probably Pearl or ASP classic.
[441.98 --> 450.88]  I do have an image of myself after the army sitting on a beach in a Sinai in a Egypt, sitting
[450.88 --> 453.90]  there, my legs in the water, reading a Ruby and rails.
[454.28 --> 454.72]  Nice.
[454.92 --> 455.14]  Yeah.
[455.14 --> 456.44]  It was like 2001.
[457.30 --> 457.74]  Yeah.
[457.82 --> 458.82]  I want to see that picture.
[459.30 --> 460.40]  Please share it.
[460.40 --> 461.38]  I wish I had it.
[461.38 --> 465.80]  Like everyone around me was relaxing and smoking and relaxing.
[465.80 --> 469.88]  And I was like reading about Ruby and rails, which was like the, the new hotness back then.
[470.28 --> 471.96]  It's how you're, it's how you relax.
[473.00 --> 474.16]  Yeah, exactly.
[474.64 --> 475.30]  It's less stressful.
[475.50 --> 479.56]  That's one thing about the software industry that I love is, you know, a lot of people spend
[479.56 --> 484.30]  a lot of time finding what they're passionate about, what really, you know, floats their
[484.30 --> 485.04]  boat, so to speak.
[485.04 --> 490.86]  Like, and oftentimes once you find it, it's contrary to, uh, making a living.
[491.00 --> 496.48]  You know, like I love, uh, if you love music, like it's very difficult to make a living doing
[496.48 --> 498.46]  music because so many people are trying that.
[498.46 --> 504.44]  Uh, if you love to paint, like it's not the easiest way to make a living, but if you love
[504.44 --> 509.60]  to write software, you've fallen in love with something that you can do not just for fun,
[509.60 --> 514.22]  but you can do, you know, very lucratively, um, as a vocation as well.
[514.22 --> 515.46]  So we're pretty fortunate that way.
[516.28 --> 516.96]  Yeah, exactly.
[517.08 --> 521.20]  I mean, that's what I, I found like, Oh, I love doing this so much.
[521.24 --> 527.82]  I mean, like this is a bit embarrassing, but I've literally found myself jumping out and
[527.82 --> 534.28]  dancing alone in the room when I got, when I had to pull requests, uh, accepted to open
[534.28 --> 535.00]  source libraries.
[535.00 --> 542.12]  So when you're this passionate and this excited about open source, um, quitting my job and
[542.12 --> 546.58]  focusing full-time on open source suddenly makes sense to me, if not to my wife.
[547.44 --> 550.04]  I think that's a case where we need pics or it didn't happen.
[551.58 --> 553.60]  We can use the new iOS live photos.
[553.68 --> 556.84]  The next time you get a PR, you know, there's that project that'll take a picture of you
[556.84 --> 561.84]  each time you, your get, you know, your push doesn't happen or you have a merge conflict.
[561.92 --> 564.98]  I can't remember which one it is, but, uh, you should get a live photo.
[565.00 --> 567.20]  Every time you get a pull request.
[567.46 --> 568.92]  I haven't heard that one.
[569.00 --> 573.40]  Like it sounds amazing, especially for a SVN, whoever's still using those.
[573.86 --> 574.38]  Yeah.
[574.82 --> 579.54]  Well, speaking of, uh, interesting and somewhat amazing open source projects, uh, you have
[579.54 --> 580.76]  a couple of them under your belt.
[580.76 --> 587.76]  And the first one that seemed to take everybody by surprise and, um, was a big hit back in
[587.76 --> 592.08]  2013, I think was when, uh, first came out September time.
[592.08 --> 598.04]  I remember, uh, you emailing us about it is called on young, which is speech recognition.
[598.78 --> 600.00]  Uh, that just works.
[600.00 --> 601.66]  That's your, your little tagline there.
[601.66 --> 605.70]  And it's allows you to control a website, uh, by your voice.
[605.70 --> 608.36]  Can you, can you give us the background on that project?
[608.36 --> 609.16]  Okay.
[609.16 --> 614.32]  So I think the background behind this is pretty much the story behind every project I do.
[614.48 --> 620.66]  There's like so many exciting new technologies coming out and browser new, new things in browsers
[620.66 --> 621.40]  every day.
[621.40 --> 627.94]  And sometimes, you know, you gotta read through long specs and understand everything and the
[627.94 --> 631.78]  differences between different browsers and all those little things.
[631.78 --> 636.26]  So what I like to do is I like to call it, I read the specs so you don't have to.
[637.00 --> 643.24]  So with Anyang, what I, what I did was this new technology of speech recognition came out
[643.24 --> 647.64]  and it's such a part of our lives by now.
[647.64 --> 650.86]  I mean, we're, I was talking just today.
[650.96 --> 656.58]  I, I spoke to my phone, asked him question a few times already, but you don't really see that on the
[656.58 --> 657.08]  web yet.
[657.52 --> 664.78]  So what I went, what I set out to do was to take that and make it super easy for anyone to use.
[665.04 --> 670.28]  So you don't have to understand like all the different settings for web kit speech recognition,
[670.28 --> 676.04]  as it is called and understand the difference between browsers and HTTP and HTTPS and all those
[676.04 --> 676.40]  things.
[676.74 --> 684.62]  You just say, okay, Anyang, if the user says, show me search phrase, then run this function
[684.62 --> 686.12]  and pass it that search phrase.
[686.36 --> 687.96]  If it says do that, then do that.
[688.32 --> 691.40]  And then you just say Anyang start and it takes care of everything.
[692.24 --> 699.82]  So basically I'm taking a technology that is very powerful and has a lot of features.
[699.82 --> 707.86]  And build a very opinionated library that does one thing and does it well and super easy.
[708.98 --> 711.70]  So that's what Anyang does.
[712.04 --> 719.22]  I mean, if you want to add, if you, you can basically change the UI of your site.
[719.22 --> 725.48]  So if you're apple.com, for example, which is an awful example, because it doesn't work
[725.48 --> 727.76]  on Safari, like most things these days.
[728.34 --> 736.68]  But if you're on apple.com and there's a limited number of links, if you're looking for a monitor,
[736.84 --> 741.70]  you have to click through a few different pages before you find it.
[741.70 --> 747.20]  And if you're looking for store locations, whatever, there's a limited amount of screen
[747.20 --> 747.56]  space.
[748.08 --> 751.12]  But if you open up, in a way, it's another dimension.
[751.54 --> 757.52]  If you open it up to speech, like show me screens or show me monitors or show me
[758.42 --> 764.62]  HD monitors, whatever the user thinks he wants, the site can respond to that.
[764.62 --> 767.34]  So that's what I did.
[767.46 --> 769.60]  And that was the use case I had in mind.
[769.84 --> 773.98]  But of course, once you release something, that's the most exciting thing about open source.
[774.26 --> 777.92]  Once you release it, like people go crazy with it.
[778.06 --> 778.52]  If you're lucky.
[778.60 --> 779.46]  It takes a life of its own.
[779.56 --> 779.68]  Yeah.
[779.86 --> 780.18]  Yeah.
[780.18 --> 786.32]  I mean, I've seen people use Onion to create remote control cars that you can tell them
[786.32 --> 789.16]  to go left, go right, reverse, etc.
[790.08 --> 798.44]  I've seen people in a hackathon in Bangladesh, I think it was, that they built AR drones, those
[798.44 --> 803.84]  little flying drones, and you could tell them to dance or spin or do different things.
[804.00 --> 805.26]  And they built that with Onion.
[805.56 --> 806.36]  Very cool.
[806.36 --> 806.80]  Yeah.
[807.02 --> 815.62]  Actually, just two weeks ago, I saw a developer who built a bathroom mirror that he can talk
[815.62 --> 815.82]  to.
[816.10 --> 821.76]  So he's standing in front of his bathroom mirror, shaving or whatever, and he can actually ask
[821.76 --> 825.24]  it for stock quotes or ask the mirror about the weather.
[825.64 --> 831.18]  And he built it with a two-way mirror that has a tablet behind it that shows everything.
[831.28 --> 833.10]  And it looks super polished.
[833.68 --> 833.78]  What?
[834.34 --> 834.58]  Yeah.
[834.98 --> 835.74]  That's amazing.
[835.74 --> 839.10]  It looks like an Apple product from 2022.
[839.48 --> 842.22]  Like, it's so polished and so amazing.
[842.92 --> 848.16]  So doing things like that is really exciting, seeing what people are building, like taking
[848.16 --> 850.86]  these new technologies and making them more accessible.
[851.40 --> 853.04]  That's really fun.
[853.08 --> 853.18]  Yeah.
[853.20 --> 859.68]  So in those different use cases, specifically, you know, the bots and whatnot, are those all
[859.68 --> 861.32]  running embedded web browsers?
[861.32 --> 865.78]  Or is Anyang able to be used in a server side context or in like a node environment as well?
[865.86 --> 866.44]  How is that working?
[867.06 --> 868.32]  With a browser.
[868.94 --> 871.92]  There's like, yeah, it's still hard to run it on node.
[872.48 --> 872.90]  Very cool.
[872.98 --> 873.12]  Yeah.
[873.18 --> 877.88]  I think that is one of the most exciting things about open source is, you know, once you put
[877.88 --> 883.34]  it out there, especially something like this, which has, you know, a specific use case in
[883.34 --> 887.46]  mind, but then it is just generally interesting to dink around with.
[887.78 --> 891.76]  People tend to start using it in ways that that you couldn't imagine.
[891.84 --> 895.92]  Going back to your point about the third dimension or the, you know, the additional dimension that
[895.92 --> 896.32]  you're adding.
[897.08 --> 901.94]  One problem that I find with audio interfaces into websites, for instance, or even on the
[901.94 --> 904.66]  phone is that discoverability is really an issue.
[904.82 --> 908.68]  I don't know what I can and cannot say to this interface.
[909.48 --> 913.86]  Have you put any thought into that with regard to Anyang?
[915.26 --> 915.70]  No.
[915.80 --> 917.50]  So I guess that is a bigger problem.
[917.50 --> 922.82]  And that is something that I still run into with, with my Google phone.
[923.00 --> 926.26]  Like just yesterday, it was, I was telling him, okay, Google.
[926.26 --> 928.20]  And he was like, please retrain voice model.
[928.30 --> 930.78]  So I said, okay, Google retrain voice model.
[931.02 --> 935.46]  And like, he asked me to retrain and I said it back and it didn't understand.
[935.68 --> 940.58]  So it requires like, like machine learning.
[940.58 --> 942.54]  The words I've said to Siri is crazy.
[943.78 --> 946.02]  Siri upsets me on a daily basis.
[946.02 --> 947.38]  And I give her a chance.
[947.82 --> 949.64]  And I really want her to work better.
[950.14 --> 954.90]  And I'm like, no, I think I was looking for something the other day.
[956.38 --> 961.72]  I was looking for, looking up the word, a word in the Greek library or the Greek language.
[962.10 --> 963.84]  And I was trying to Google for it.
[963.90 --> 969.50]  And it just kept pulling back the Wikipedia page for Greek, what Greek means or what Greek
[969.50 --> 969.92]  is.
[969.92 --> 972.32]  And it like omitted everything after that.
[972.94 --> 976.58]  There's so many times I'm like upset with voice stuff.
[976.58 --> 979.54]  But it's a, it's a new paradigm.
[980.12 --> 980.22]  Yeah.
[980.38 --> 985.06]  It kind of reminds me of Clippy back in the day in Microsoft Clippy where it was, are you
[985.06 --> 986.54]  sure you spelled your name correctly?
[986.64 --> 987.60]  Can I help you with that?
[988.10 --> 988.50]  Yeah.
[988.50 --> 988.82]  Thanks.
[988.82 --> 989.10]  Yeah.
[989.10 --> 991.18]  I mean, I'm sure it's probably even more difficult.
[991.18 --> 997.84]  You know, being from middle America, you know, Omaha and Nebraska are kind of one of the telemarketing
[997.84 --> 1002.18]  capitals of America because we're kind of famous for having no accent and kind of the
[1002.18 --> 1004.32]  most boring dialect possible.
[1004.32 --> 1010.64]  So, so that we don't offend anybody, I guess, with our, with how normal eyes our voices are.
[1010.78 --> 1013.98]  But, you know, yourself being from Israel, you know, you have that accent.
[1014.34 --> 1017.80]  And I just think of the problem domain of speech recognition.
[1017.80 --> 1022.56]  And it kind of overwhelms me from the perspective of, of algorithms.
[1023.36 --> 1029.00]  Um, it's hard problem to solve, especially with people, you know, so many different, um,
[1029.84 --> 1030.78]  voices over the world.
[1030.82 --> 1032.42]  So how does Anyang do speech recognition?
[1032.42 --> 1033.98]  Is there a library it's using?
[1034.08 --> 1035.36]  Did you implement it yourself?
[1035.74 --> 1036.44]  How's that work?
[1036.44 --> 1043.76]  So Anyang is using a speech recognition, which is part of the W3 spec or proposition or who
[1043.76 --> 1044.78]  can keep track of those.
[1044.88 --> 1045.76]  They're so complicated.
[1046.28 --> 1049.42]  Um, but it uses what's available in the browser.
[1049.42 --> 1051.66]  So right now it's in a Google Chrome.
[1052.24 --> 1056.28]  Um, I think Firefox is working on implementing it soon.
[1057.00 --> 1061.02]  Um, but yeah, that's a problem with a speech recognition.
[1061.02 --> 1066.42]  I mean, most features you can browser vendors can implement, but this one's, this one requires
[1066.42 --> 1073.32]  a very sophisticated backend, uh, something that Google obviously has, but a lot of, um,
[1073.42 --> 1076.06]  smaller browsers, um, don't really have.
[1076.42 --> 1080.08]  So yeah, that is a major issue with, um, Anyang.
[1080.24 --> 1081.30]  It's Chrome only.
[1082.06 --> 1086.66]  Um, but it's, yeah, I know, I know other browsers are working on that.
[1086.76 --> 1092.28]  So the browser itself actually does the recognition, the speech to text, and it just hands off to
[1092.28 --> 1096.40]  the browser, you know, to your JavaScript library, the text, uh, and you take it from there.
[1096.42 --> 1098.78]  Yeah, exactly.
[1099.02 --> 1105.36]  So I, I take care of all those little, uh, uh, nuances and all those, like, for example,
[1105.36 --> 1109.50]  if you have a speech recognition running in two different windows, it can actually cause,
[1109.58 --> 1111.12]  uh, Google Chrome to crash.
[1111.44 --> 1117.46]  So I take care of, I actually reported this to them and they fixed it since then, but like,
[1117.46 --> 1119.00]  it takes care of issues like that.
[1119.36 --> 1124.46]  Um, so it's, it's an interface in a way, uh, a more friendly interface.
[1124.94 --> 1129.90]  I think it would be remiss to just keep saying Anyang over and over again and not mention the
[1129.90 --> 1130.40]  namesake.
[1131.10 --> 1134.48]  Um, I pulled back up our emails from back in the day, Tal.
[1134.60 --> 1140.66]  And, uh, the first thing I did when you emailed me was I started, uh, criticizing, uh, the spelling
[1140.66 --> 1141.28]  of your name.
[1141.28 --> 1147.16]  So, um, that's just like me to just immediately start bike shedding on something so minuscule
[1147.16 --> 1149.28]  as the, how you spell Anyang.
[1149.38 --> 1153.22]  Why don't you give us, for those who, uh, aren't huge Arrested Development fans, why don't
[1153.22 --> 1158.94]  you give the inspiration for the name and maybe your, uh, your justification for spelling
[1158.94 --> 1159.28]  it wrong?
[1161.78 --> 1169.86]  Uh, so yeah, Anyang is a, is a reference to, to one of the greatest shows ever made, Arrested
[1169.86 --> 1174.96]  Development, where there was a character who, I don't know if it's fair to say he was called
[1174.96 --> 1179.94]  Anyang, but that's what, yeah, that's what everybody called him.
[1180.10 --> 1184.74]  Because when he came, uh, the first time he just said Anyang, which means hello.
[1184.94 --> 1188.92]  And it, everyone just assumed that was his name and didn't bother to find out.
[1189.84 --> 1194.84]  Um, so yeah, it's, you can say it's spelled a bit differently.
[1195.24 --> 1195.60]  Um.
[1196.32 --> 1197.08]  You wouldn't say wrong.
[1197.16 --> 1197.78]  You'd say it differently.
[1197.86 --> 1198.34]  I like that.
[1198.34 --> 1202.38]  Well, there's no right or wrong way to spell it because it's not English.
[1202.96 --> 1207.62]  Um, you're just, it's phonetic spelling, which I'm phonetically spelling it wrong, but at
[1207.62 --> 1212.98]  least that way it looks less like the word, uh, annoying, um, which is the feedback I got
[1212.98 --> 1213.42]  initially.
[1213.62 --> 1213.90]  Ah.
[1214.24 --> 1218.88]  So I went with that, but yeah, I loved our, uh, back and forth when I sent this to you
[1218.88 --> 1223.50]  a few years ago, you're like very, very obsessed.
[1223.62 --> 1226.68]  And the more obsessed you get about it, the better I felt about it.
[1226.68 --> 1227.12]  Yeah.
[1227.12 --> 1230.60]  Well, it's something that, you know, Adam and I, we look at a lot of open source projects
[1230.60 --> 1234.40]  and so we're very, um, cognizant of names.
[1234.40 --> 1235.96]  You know, what catches, what catches your eye?
[1235.96 --> 1236.16]  Yeah.
[1236.16 --> 1236.80]  What doesn't.
[1236.80 --> 1241.40]  Um, sometimes names are offensive and, you know, we try to help people pick a better
[1241.40 --> 1243.70]  name or, you know, just ask where names came from.
[1243.78 --> 1248.92]  Sometimes it'll be a project that I have no idea whether or not it has merit based on
[1248.92 --> 1250.48]  its value proposition.
[1250.48 --> 1254.70]  But the name is so spectacular that I just think I just, you know, tweeted or included
[1254.70 --> 1255.52]  it in weekly anyways.
[1256.52 --> 1261.96]  Um, because you know, we do judge books by their covers, unfortunately, and with how fast
[1261.96 --> 1263.64]  open source moves, you kind of have to.
[1263.64 --> 1268.08]  So Anyang definitely immediately caught my eye and I thought, well, that's gotta be a reference
[1268.08 --> 1268.76]  to Arrested Development.
[1269.00 --> 1272.28]  So I went to the Arrested Development wiki and I saw it spelled differently there.
[1272.40 --> 1274.24]  And that's when I had to start giving you some jabs.
[1274.94 --> 1275.90]  But, uh, yeah.
[1276.14 --> 1277.34]  It wasn't just a mistake.
[1277.34 --> 1279.46]  It was, you actually said, well, it looked like annoying.
[1279.60 --> 1281.46]  So I'm going to change the A and that makes sense.
[1281.46 --> 1281.82]  Yeah.
[1282.82 --> 1283.70]  And I guess that's the point.
[1283.82 --> 1289.46]  I mean, if you're, if I caused you to, to pause and look it up and check it, then, you
[1289.46 --> 1291.32]  know, most things don't even cause you to pause.
[1291.38 --> 1292.82]  You just glance over and continue.
[1293.16 --> 1298.06]  And you remember it like a few years later, which, which says something.
[1298.74 --> 1300.94]  Um, yeah, absolutely.
[1301.14 --> 1305.14]  And I think, uh, I think it didn't hold it back the wrong spelling.
[1305.20 --> 1306.62]  I'll keep using the term wrong.
[1306.62 --> 1310.94]  Cause I'm going to stay on my side of that argument, but definitely didn't, definitely didn't
[1310.94 --> 1311.54]  hold it back.
[1312.18 --> 1314.46]  Um, it's been a couple of years.
[1314.46 --> 1317.46]  I saw at least on your GitHub that on young 2.0 has come out.
[1318.18 --> 1319.28]  What's the state of it?
[1319.30 --> 1320.02]  Is it done?
[1320.18 --> 1322.04]  Do you have future features for it?
[1322.32 --> 1324.48]  Um, tell us those kinds of things.
[1326.42 --> 1335.00]  Um, so like a lot of developers have a very short attention span, you know, I get very excited
[1335.00 --> 1339.70]  about something and I can build something pretty interesting.
[1339.70 --> 1346.36]  Like, you know, those whirlwind, whirlwind 48 hours after you get the idea, you can build
[1346.36 --> 1348.16]  something that would normally take you a month.
[1348.80 --> 1353.70]  Um, I wouldn't say it's done, but it's pretty feature complete.
[1353.70 --> 1358.82]  Um, from time to time people do ask for more things, uh, send pull requests.
[1359.36 --> 1366.02]  Um, so I add those, um, hopefully very soon I'll need to worry about other browsers besides
[1366.02 --> 1369.72]  Chrome, but it's pretty feature complete and definitely stable.
[1369.72 --> 1376.88]  I mean, if it's 2.0 and I'm, uh, very cement, like I use semantic versioning, so it's, it's
[1376.88 --> 1377.22]  stable.
[1378.72 --> 1380.08]  You gave me some examples.
[1380.32 --> 1383.82]  Uh, and you've already given a couple of where it's been used.
[1384.18 --> 1388.96]  Um, any others that come to mind of cool places that you've, this library has gone that you
[1388.96 --> 1389.86]  couldn't have imagined.
[1391.46 --> 1396.28]  So actually I'm gonna answer a different thing, a different question.
[1396.28 --> 1399.12]  Cause like, I don't know, you know what?
[1399.24 --> 1400.00]  I don't know.
[1400.36 --> 1405.40]  It seems like this is a real issue with open source cause you develop something and people
[1405.40 --> 1409.64]  use it and you don't really know who uses it, how they are using it.
[1409.64 --> 1414.76]  Um, and I mean, they don't tell you, um, there's no way for you.
[1414.86 --> 1416.68]  There's no analytics for open source.
[1417.24 --> 1421.58]  Um, so that is a real issue that I've thought a lot about how to solve.
[1421.82 --> 1426.40]  Uh, I don't have anything yet, but it's something that has been on my mind.
[1427.26 --> 1434.66]  Um, going back to your question, there has been a lot of Jarvis's if you remember from
[1434.66 --> 1435.18]  Ironman.
[1435.18 --> 1440.34]  Um, so a lot of people have built Jarvis's or Jarvi would be the plural.
[1440.52 --> 1440.88]  I like that.
[1441.38 --> 1446.12]  Um, so a lot of people have like, that was the go-to project.
[1446.26 --> 1453.74]  Uh, most people like really the first thing that pops to most people's minds, but that
[1453.74 --> 1456.68]  is a definitely an interesting problem to solve.
[1457.24 --> 1458.74]  Um, discoverability.
[1459.14 --> 1459.58]  Yeah.
[1459.62 --> 1464.70]  It might be interesting to have some sort of a built, you know, uh, similar to how a lot
[1464.70 --> 1468.78]  of websites for nerds like us will have, uh, will respond to keyboard shortcuts.
[1468.78 --> 1473.56]  And if you hit, you know, question mark, it'll pop up a, uh, uh, heads up display type of
[1473.56 --> 1473.90]  a look.
[1473.96 --> 1477.64]  It just says, you know, these are the kinds of keyboard shorts that we shortcuts that
[1477.64 --> 1480.06]  we, we, uh, support.
[1480.20 --> 1482.32]  Thank you, Jared, for being an idiot.
[1482.86 --> 1488.02]  Uh, the kind of keyboard shortcuts that we support, you could have some sort of a interface
[1488.02 --> 1492.84]  for Anyang as well, which when you include it, you know, allows you to pop up something
[1492.84 --> 1495.52]  and says like these specific voice commands are supported.
[1496.12 --> 1497.80]  Even that would need to be discoverable.
[1497.98 --> 1501.62]  So, you know, most people don't know there are, you can hit question mark and get those
[1501.62 --> 1503.20]  things, but your power users do.
[1503.88 --> 1506.36]  Um, that might be a step in the right direction.
[1506.44 --> 1509.94]  It definitely doesn't solve the problem altogether, but it would at least allow kind of a common
[1509.94 --> 1513.16]  way of people saying, you know, here are the types of voice commands this website
[1513.16 --> 1513.66]  supports.
[1513.66 --> 1514.26]  Yeah.
[1515.58 --> 1520.42]  I mean, that is something I live to the developer who uses Anyang, but definitely on the Anyang
[1520.42 --> 1522.00]  site itself, I do.
[1522.44 --> 1524.52]  I mean, that's how I introduce it.
[1524.58 --> 1529.70]  I mean, you land on the site, there's like barely two sentences, and then it's just telling
[1529.70 --> 1531.34]  you, say hello.
[1531.58 --> 1537.98]  And you say hello and the site says Anyang back, or it, or it says, show me cute kittens
[1537.98 --> 1539.46]  and it shows you kittens.
[1539.78 --> 1543.12]  Or then it says like, ask for anything.
[1543.12 --> 1544.16]  And the site response.
[1544.40 --> 1546.10]  So it's like a soft intro.
[1546.60 --> 1549.20]  And then sometimes it's just fun to discover.
[1550.46 --> 1550.70]  Very cool.
[1550.78 --> 1554.82]  Well, I think this is a good chance for us to step back and hear from one of our awesome
[1554.82 --> 1555.32]  sponsors.
[1555.64 --> 1559.76]  On the other side of the break, we're going to move on to your newest open source project,
[1560.52 --> 1560.84]  UpUp.
[1561.04 --> 1561.84]  So stay tuned for that.
[1561.84 --> 1571.26]  Our friends at TopTile launched a scholarship program for female developers to support aspiring
[1571.26 --> 1575.56]  female computer scientists, developers, and software engineers to help achieve their goals
[1575.56 --> 1577.90]  through financial support and also mentorship.
[1578.44 --> 1584.34]  Each scholarship winner will receive a $5,000 scholarship that can be used towards education
[1584.34 --> 1585.94]  and professional development goals.
[1585.94 --> 1590.44]  You can spend this money on anything you want from coding boot camps to online programming
[1590.44 --> 1592.40]  courses, textbooks, you name it.
[1592.80 --> 1599.50]  You also get one-on-one mentoring, an entire year of weekly one-on-one mentoring with a TopTile
[1599.50 --> 1600.18]  senior developer.
[1600.72 --> 1605.58]  And this person is going to help you with topics like project guidance, choosing an academic or
[1605.58 --> 1608.04]  career path, and also preparing for interviews.
[1608.04 --> 1612.26]  Head to TopTile.com slash scholarships to learn more and also to apply.
[1615.00 --> 1621.16]  All right, we are back with all a tear talking about a few awesome open source projects, the
[1621.16 --> 1623.54]  most recent of which is called UpUp.
[1623.88 --> 1631.56]  And you can find that at UpUp.rocks, making use of those awesome and or not awesome new domain
[1631.56 --> 1632.12]  names there.
[1633.82 --> 1638.02]  UpUp is a tiny script that makes sure your site's always there for your users.
[1638.04 --> 1640.62]  The offline first library.
[1640.76 --> 1642.64]  Why don't you give us the elevator pitch here?
[1643.82 --> 1644.34]  Okay.
[1644.58 --> 1650.10]  So, I mean, basically we're, the last big thing was mobile first.
[1650.22 --> 1655.68]  I mean, we're building sites that are ready to always be there for users when you're on
[1655.68 --> 1658.38]  your phone or, or wherever.
[1658.94 --> 1664.10]  But now that we're all on our phones, like we can't really rely on having a constant connection.
[1664.10 --> 1666.68]  I mean, no one's walking around with a wire connecting them.
[1666.68 --> 1674.40]  So, new technologies have come out to, to allow sites to still work even while the user is
[1674.40 --> 1675.22]  losing connectivity.
[1676.50 --> 1678.40]  And that is what UpUp does.
[1678.60 --> 1684.66]  I mean, it uses the new service worker APIs to achieve that.
[1684.66 --> 1686.30]  I'll talk a little bit more about that.
[1686.30 --> 1692.54]  But basically, I mean, this is something that happens all the time.
[1692.64 --> 1695.92]  I mean, usually when I tell people about this problem and they're thinking, yeah, I mean,
[1695.98 --> 1702.20]  like in the, in the less developed world, yeah, they don't have connectivity all the time.
[1702.20 --> 1706.70]  But I've been visiting the States for the past two months.
[1706.70 --> 1713.18]  And in downtown San Francisco, I couldn't get a service.
[1713.92 --> 1715.60]  And this is something that happens all the time.
[1715.60 --> 1722.32]  Like whether you're in San Francisco or going down the elevator or on a flight, you can't
[1722.32 --> 1727.34]  really rely on having that connecting to have that persistent connection to the internet
[1727.34 --> 1727.92]  all the time.
[1728.46 --> 1735.30]  So basically what UpUp does is allows the, the site developer to decide what experience
[1735.30 --> 1737.62]  he wants the user to see when he's not connected.
[1737.62 --> 1744.06]  So that can be as simple as if I go to a certain site and I don't have internet, I might see
[1744.06 --> 1748.94]  a message from the site saying you don't have a connection, connection, so you can't read
[1748.94 --> 1756.34]  your emails, come back later, or it can be a full single page application experience.
[1756.50 --> 1761.78]  I mean, you could have Gmail working even without a connection if they implement this.
[1761.78 --> 1769.04]  Um, so, and of course this requires the user to visit the site while he's online the first
[1769.04 --> 1774.02]  time, but once he did, every time he visits it again and he's offline, it'll still work.
[1774.36 --> 1779.08]  So the classic example for me would be like a site like a booking.com.
[1779.26 --> 1782.82]  So I, I know I'm flying to San Francisco.
[1783.42 --> 1785.40]  Um, I booked a number of hotels.
[1785.54 --> 1787.14]  I landed in San Francisco.
[1787.14 --> 1791.42]  I still don't have a local, uh, data plan or the connection didn't work.
[1791.42 --> 1796.98]  I sit in my, uh, I sit in a cab, open up my phone, go on booking.com.
[1797.06 --> 1802.04]  And instead of seeing that little, uh, Chrome dinosaur telling me I'm offline, I would still
[1802.04 --> 1807.14]  be able to see my reservations to see the address of my hotel, the phone numbers, et cetera.
[1807.82 --> 1814.60]  Um, and that's the idea behind app, app and the technology that enables its service worker.
[1815.28 --> 1819.26]  Uh, this is an interesting conversation around, you know, connectivity in general.
[1819.26 --> 1826.56]  I tend to live in, you know, a little bit of a bubble where I don't know if I'm ever not
[1826.56 --> 1827.06]  online.
[1827.88 --> 1832.64]  Um, of course airplanes is, is the big, you know, proof point against that.
[1833.16 --> 1835.02]  Um, and now they're adding in-flight wifi.
[1835.84 --> 1839.24]  Um, people are, you know, can get online on airplanes.
[1839.70 --> 1844.82]  It's limited, but you know, going to be coming obviously in a third world countries, places
[1844.82 --> 1847.06]  where there's less, uh, infrastructure.
[1847.38 --> 1850.74]  We do know that cellular infrastructure is way better than any sort of wired infrastructure
[1850.74 --> 1851.88]  has been in those places.
[1852.46 --> 1855.94]  And so, you know, maybe it's expensive, but access is there.
[1856.02 --> 1857.92]  Maybe it's slow, but there is connectivity.
[1858.92 --> 1863.34]  Do you think this is a problem that's going to exist five years from now, 10 years from
[1863.34 --> 1863.62]  now?
[1863.62 --> 1867.26]  Um, or is the network coming or is it not coming?
[1867.34 --> 1867.70]  What do you think?
[1868.70 --> 1870.22]  I, I really hope so.
[1870.40 --> 1877.92]  But, um, one of my first, uh, as an entrepreneur, one of my first companies was called, uh, Wiser
[1877.92 --> 1885.88]  and we were one of the first companies to, to add wifi to restaurants and cafes in Tel
[1885.88 --> 1886.16]  Aviv.
[1886.16 --> 1888.38]  And this was in 2004.
[1888.96 --> 1893.28]  And we tried to explain to people, to restaurant owners, why they even need to provide this
[1893.28 --> 1893.66]  service.
[1894.54 --> 1897.92]  And this was 11 years ago and we still have that problem.
[1898.70 --> 1903.22]  Um, so I think it'll be a few more years before, before coverages.
[1903.54 --> 1909.62]  Like I remember back then people were talking about, I think it was called Wimax, something
[1909.62 --> 1916.10]  like that, like wifi, but like Wimax routers that would cover entire cities 11 years ago.
[1916.16 --> 1919.80]  So I think it'll still be a while before this problem is solved.
[1921.10 --> 1922.16]  I'm with you though, Jared.
[1922.26 --> 1924.44]  I only have ever been out without a connection.
[1924.44 --> 1926.62]  Like I always have the internet.
[1926.74 --> 1928.02]  I think we're probably just in bubbles.
[1928.72 --> 1932.34]  Um, Wimax, I think is a, is a bit of a dead technology.
[1932.34 --> 1937.24]  I know sprint was one of the carriers that rolled it out in mass years ago and they've
[1937.24 --> 1939.14]  since switched technology.
[1939.14 --> 1943.00]  So I'm not sure if, you know, the, the promise of Wimax has never really arrived.
[1943.00 --> 1947.08]  Um, but yeah, it's hard be living in the bubble.
[1947.08 --> 1952.84]  It's difficult to empathize with people who aren't in that bubble, um, and see this for
[1952.84 --> 1954.06]  the real problem that it is.
[1954.28 --> 1959.32]  And then, you know, you have people who experience connectivity problems all the time who want
[1959.32 --> 1963.80]  to just like smash their, you know, whatever podcast listening device they're using right
[1963.80 --> 1967.16]  now, because we're so dumb that we think that this isn't a real problem.
[1967.16 --> 1971.62]  Um, it just seems like depends on where you are in life and you're in a unique perspective
[1971.62 --> 1972.94]  because you're traveling the world right now.
[1973.48 --> 1978.18]  And so you probably have lots of experiences, you know, recently with, am I online or am
[1978.18 --> 1978.70]  I offline?
[1979.30 --> 1983.34]  Just curious how many of those flights you've taken have had, uh, internet access.
[1984.24 --> 1987.56]  Uh, well, mostly domestic flights in the U S have a wifi.
[1987.86 --> 1989.68]  Uh, it still costs a lot.
[1989.68 --> 1997.42]  Um, and there's no company to expense it to, um, but yeah, it's the past two months I've
[1997.42 --> 1999.78]  been traveling all over the States.
[1999.78 --> 2002.10]  Uh, started in the East coast, West coast.
[2002.18 --> 2005.16]  Now I'm back in the East and you see it everywhere.
[2005.16 --> 2011.34]  I mean, the, the U S isn't covered yet by, uh, by all those networks.
[2011.34 --> 2021.02]  And with a lot of pressures on them to drop prices, they'll, that problem will still happen.
[2021.02 --> 2023.80]  I mean, even in the U S and I agree.
[2023.88 --> 2024.76]  I also live in a bubble.
[2024.92 --> 2028.08]  I mean, uh, in Tel Aviv, we call our city the bubble.
[2028.32 --> 2034.84]  Um, and yeah, you have connectivity wherever you go and it seems isolated in many, in many
[2034.84 --> 2035.16]  ways.
[2035.28 --> 2037.18]  If anything, it's like Silicon Valley.
[2037.18 --> 2042.26]  Um, but the issue of connectivity is a real one for most people.
[2042.82 --> 2049.02]  Well, I think up ups, um, interest and success early on has proven that this is a problem
[2049.02 --> 2051.40]  that developers want to solve.
[2051.52 --> 2054.00]  I think you're over 3000 stars on GitHub.
[2054.00 --> 2060.60]  You were definitely, uh, in change log nightly a few days in a row in the top start repos sections.
[2061.12 --> 2064.56]  Um, I think you were at the top of product hunt even.
[2064.72 --> 2066.70]  Can you speak about that experience on product hunt?
[2067.18 --> 2069.02]  Yeah.
[2069.02 --> 2070.46]  So that was very interesting.
[2070.46 --> 2079.82]  Um, it was actually, um, at my, my last day on the, uh, at my old company, I went into,
[2079.82 --> 2082.16]  um, basically say goodbye to everyone.
[2082.40 --> 2090.72]  And, um, suddenly I got a tweet from, uh, from product hunt that my, my, uh, that up up is
[2090.72 --> 2093.42]  there and has had over a hundred votes already.
[2093.42 --> 2099.96]  And they do this, uh, animated gif, uh, of Oprah, like going crazy.
[2100.84 --> 2103.02]  And that was so exciting.
[2103.26 --> 2108.16]  Um, I didn't even submit it there, but, um, it was super exciting.
[2108.16 --> 2114.52]  And I just, um, locked myself in a room and followed it, uh, throughout the entire day,
[2114.62 --> 2119.34]  talking to people, um, asking them to, to share it and look at it.
[2119.80 --> 2124.96]  Um, and yeah, at the end of the day, it was the, the most hunted, I guess is the term,
[2124.96 --> 2133.24]  the, the top product on product hunt, which brought in a huge amount of traffic, um, in
[2133.24 --> 2134.32]  the tens of thousands.
[2135.08 --> 2139.86]  Um, and yeah, um, up up has grown, has grown incredibly.
[2139.86 --> 2143.72]  And I think the only metric I have to measure that is in GitHub stars.
[2143.86 --> 2145.76]  That's our new currency, I guess.
[2145.76 --> 2154.52]  And it has surpassed Anyang in a month or two, what took Anyang, uh, two years to achieve.
[2154.96 --> 2156.56]  So that was very exciting.
[2156.98 --> 2161.42]  Um, you think it's because of product hunt or you think it's because of simply the library
[2161.42 --> 2161.80]  itself?
[2162.78 --> 2164.36]  Um, it's a lot of things.
[2164.54 --> 2166.32]  Product hunt certainly helped.
[2166.58 --> 2170.34]  Um, it was also featured on a lot of other places.
[2170.34 --> 2175.26]  You guys wrote about it, which also brought in a lot of, uh, um, traffic.
[2175.98 --> 2184.20]  Um, but I think a lot of it is what I love to talk about, uh, uh, later is, is simply looking
[2184.20 --> 2189.64]  at what you're building at, uh, at the library, even if it's open source, looking at it as a
[2189.64 --> 2194.24]  product, a product that even if you're not selling it for money, you need to grab the
[2194.24 --> 2194.98]  user's attention.
[2194.98 --> 2201.60]  You need to have him understand immediately why he wants to, to invest another minute of
[2201.60 --> 2203.22]  his time to understand what it is.
[2203.58 --> 2208.76]  Um, get him excited, want to make him want to try it or share it with, with his friends.
[2209.08 --> 2215.94]  And that is something that I think I did a little bit better in, in, uh, up, up than
[2215.94 --> 2218.46]  I did in Anyang, um, live and learn.
[2219.38 --> 2220.88]  Product hunt's interesting.
[2220.88 --> 2226.96]  It used to be, you know, it started off as simply a place where you post, you know, you
[2226.96 --> 2233.22]  saw new software as a service or, you know, try this app and they've seemed to have expanded
[2233.22 --> 2238.08]  their scope quite a bit, even so much so that there's podcasts now, which Adam, you and I
[2238.08 --> 2240.26]  just found that out earlier this week.
[2240.26 --> 2243.08]  I think when I said, Hey, they have podcasts, why aren't we on there?
[2243.08 --> 2252.64]  Uh, we were on there once before, um, somebody on Twitter, I can't recall the name, but,
[2252.70 --> 2254.20]  uh, I see her all the time.
[2254.24 --> 2254.82]  I know her avatar.
[2254.96 --> 2258.36]  I just can't think of the name right now, but, uh, we were submitted a couple of times.
[2258.36 --> 2262.50]  So I've, I've known about it, but I didn't think, I guess it was brand new then.
[2262.50 --> 2263.74]  It was like about three weeks ago.
[2263.74 --> 2270.10]  And I never really considered like, I've never been the one to subscribe to, oh, I've
[2270.10 --> 2273.62]  got to put my thing in this site and then it will become popular.
[2273.62 --> 2277.14]  And I just don't like feeding that beast, I guess.
[2277.74 --> 2281.60]  Um, but sadly product hunt has done well enough that you have to feed the beast.
[2282.20 --> 2285.96]  Uh, I don't want to feel like that, but at least products do, you know, my wife just launched
[2285.96 --> 2290.18]  a new product at her work and, you know, product hunt was a big part of that.
[2290.24 --> 2291.68]  They were on the front page of it for a while.
[2291.68 --> 2296.76]  They were like the top five for the day and, uh, you know, it made a big deal for, for
[2296.76 --> 2297.78]  their, uh, their adoption.
[2299.72 --> 2300.84]  Uh, and it's a great thing.
[2300.90 --> 2306.82]  Like I'm, I'm, I've become a huge fan of product hunt cause, uh, and one of the old
[2306.82 --> 2308.32]  gizzers of the internet, I guess.
[2308.88 --> 2314.94]  And I remember back in the days of dig and all those stuff like the slash dot dig.
[2315.02 --> 2315.26]  Yeah.
[2315.32 --> 2321.30]  Slash dot and today hacker news, Reddit, all those things like those places are very,
[2321.30 --> 2325.20]  communities that make you feel excluded in a way.
[2325.32 --> 2330.68]  They're full of trolls and product hunt just feels like a great place to be.
[2330.68 --> 2336.76]  I mean, it started when I, when I discovered that, uh, up, up was, uh, featured there.
[2336.86 --> 2342.04]  I got, uh, a tweet from the, um, from the founder, from Ryan Hoover.
[2342.26 --> 2346.12]  I, we started tweeting back and forth and he was super nice.
[2346.12 --> 2352.10]  Like when your product, they get features, they send you like funny, um, animated gifts
[2352.10 --> 2355.08]  and you can see the responses of the community there.
[2355.16 --> 2361.26]  They're all so supportive and interested and ask, asking constructive questions and trying
[2361.26 --> 2363.40]  to understand my story and stuff like that.
[2364.02 --> 2370.24]  Where, whereas in other places, it just seems like you're feeding the trolls in a way.
[2370.24 --> 2372.98]  Um, so it just feels different.
[2373.28 --> 2378.30]  I think some of that's, uh, you can attribute to the community itself and then you can also
[2378.30 --> 2385.62]  attribute some of it to the size and the, um, the relative, uh, youth of the site.
[2386.28 --> 2393.86]  Um, as things get bigger and as communities grow and as the stakes rise, which products hunts
[2393.86 --> 2398.74]  stakes are rising, meaning it becomes more and more valuable to be featured there prominently.
[2398.74 --> 2402.04]  It'll be very difficult for them and it'll be one of their main goals.
[2402.12 --> 2407.84]  I'm sure is to maintain that positive community and not have it turn into, um, a toxic one.
[2408.46 --> 2414.26]  And so it's possible that they're still in that stage where it's all, um, Kumbaya style
[2414.26 --> 2416.46]  and hopefully they can maintain that.
[2416.60 --> 2417.72]  I think that'll be a challenge for them.
[2418.06 --> 2419.70]  So now you're the grumpy old man.
[2419.70 --> 2422.42]  Well, I mean, success brings with it all sorts of troubles.
[2422.42 --> 2423.54]  I agree with you completely.
[2423.54 --> 2430.48]  Um, I was an early, early hacker news, uh, user and like actual commenter and stuff.
[2430.82 --> 2432.76]  And it was, it felt very much like that.
[2432.78 --> 2437.30]  It felt like, you know, people were, they were smart, they were helpful, they were insightful.
[2437.80 --> 2442.36]  And it was generally a place where you would learn and be uplifted and find new technologies.
[2442.36 --> 2448.24]  And I know it's kind of a recurring thing that happens with online communities is over time,
[2448.24 --> 2454.12]  like the difficulties to maintain that, that, you know, that early feeling, um, as more and
[2454.12 --> 2455.56]  more people and still be able to grow.
[2455.76 --> 2457.52]  I think it's just a really hard problem to solve.
[2458.36 --> 2462.90]  Well, let's get back to the topic at hand up, up, uh, Tal, what's behind this thing?
[2463.48 --> 2465.12]  Honestly, it does amazing things.
[2465.12 --> 2471.58]  Like it, it's really awesome, but this is all because of the technology that is under
[2471.58 --> 2474.76]  it, which I didn't develop, um, service workers.
[2475.24 --> 2480.28]  And in my opinion, service workers are like one of the biggest additions to the browser
[2480.28 --> 2486.04]  we've seen since, I don't know, Ajax and web 2.0.
[2486.04 --> 2488.74]  And it's, it's amazing.
[2489.10 --> 2496.54]  Um, just for people who still haven't played with it, uh, yet, um, basically service workers
[2496.54 --> 2503.18]  are scripts that, uh, sit between the, the users, the browser window and the server.
[2503.32 --> 2507.92]  It's a script that runs in the browser, independent of the window, independent of the DOM.
[2508.32 --> 2514.46]  And one of the things it can do, it can act as sort of a proxy that you can program.
[2514.46 --> 2521.62]  It can sit there and intercept every single request that comes out of, uh, um, the window
[2521.62 --> 2527.34]  before it reaches the server and decide whether to do something about it, change it, call the
[2527.34 --> 2531.82]  server, call a different asset, and then return the response if it chooses.
[2532.14 --> 2537.20]  Um, all within, of course, like this sounds like a very big security issue, but there's
[2537.20 --> 2543.70]  like, this has been thought through and I've tried to break it and it's very, it's built
[2543.70 --> 2544.30]  very well.
[2544.30 --> 2548.70]  Um, but what this allows is things like up, up, for example.
[2548.70 --> 2556.72]  Um, but also imagine a site that asks for HTML from the server and then the service worker
[2556.72 --> 2560.02]  detects that it's installed and says, okay, stop.
[2560.12 --> 2563.02]  Don't ask for HTML, ask for JSON instead.
[2563.36 --> 2571.08]  Calls for a JSON file and runs the templating inside the browser before it even reaches the
[2571.08 --> 2572.70]  window and returns back HTML.
[2573.42 --> 2576.76]  So it has a lot of power and a lot of possibilities.
[2577.12 --> 2578.68]  It can do amazing things.
[2578.76 --> 2583.10]  It can talk to the windows even when the windows are closed.
[2583.62 --> 2586.66]  Um, it has the ability for push notifications.
[2587.08 --> 2596.28]  Basically, this is like one of the things that are pushing, um, web pages as close as they,
[2596.28 --> 2599.04]  they've ever been to, to the power of applications.
[2599.82 --> 2602.06]  Um, it's really spectacular.
[2602.36 --> 2606.38]  The guys behind it have been doing amazing, incredible job.
[2606.94 --> 2608.54]  Let's dive deeper on service worker.
[2608.60 --> 2609.76]  We're going to take a quick break.
[2609.88 --> 2611.54]  You're from a sponsor on the other side.
[2611.80 --> 2614.30]  Um, I got some questions about it because I agree.
[2614.36 --> 2617.94]  I think that has huge potential and it seems like it's shrouded in mystery.
[2618.06 --> 2623.06]  Uh, you've given a good description there, but, uh, we'll do some Q and A on service worker
[2623.06 --> 2623.50]  when we get back.
[2623.50 --> 2632.58]  So braintree is all about making developer lives simpler with code for easy online payments.
[2633.04 --> 2637.84]  If you're searching for a simple payment solution, check out braintree for mobile app developers
[2637.84 --> 2638.32]  out there.
[2638.48 --> 2644.40]  The braintree B dot zero SDK makes it easy to offer multiple payment types.
[2644.52 --> 2651.30]  Start accepting PayPal, Apple pay, Bitcoin, Venmo, traditional credit cards, and whatever's
[2651.30 --> 2653.68]  next.
[2653.82 --> 2657.94]  Enjoy simple, secure payments that you can integrate in minutes and developers.
[2658.10 --> 2658.62]  They've got you.
[2658.72 --> 2660.94]  Don't worry about taking days to integrate your payments.
[2661.40 --> 2662.94]  With braintree, it's done in minutes.
[2663.44 --> 2667.36]  And if you don't have time, give them a call and they'll handle the integration for you
[2667.36 --> 2668.44]  and walk you through it.
[2668.98 --> 2672.80]  Braintree supports Android, iOS, and JavaScript clients.
[2672.80 --> 2675.02]  They have SDKs in seven languages.
[2675.60 --> 2680.38]  Dot net, node JS, Java, Pearl, PHP, Python, and Ruby.
[2680.88 --> 2683.92]  And their documentation is comprehensive and it's easy to follow.
[2684.26 --> 2691.84]  To learn more and for your first $50,000 in transactions fee free, go to braintreepayments.com
[2691.84 --> 2693.12]  slash changelog.
[2693.12 --> 2706.16]  So we are talking about UpUp, which smooths over and adds some things to service workers.
[2706.54 --> 2710.22]  Tal, you gave us a rundown of what service workers are.
[2711.72 --> 2712.82]  A few questions.
[2712.88 --> 2714.38]  Let's start with browser support.
[2716.06 --> 2719.06]  Who's implemented this and who hasn't?
[2719.06 --> 2726.52]  So service workers, and I'm Googling it so I don't mistake any of them.
[2727.02 --> 2731.32]  But basically, they just landed in Firefox.
[2731.78 --> 2734.78]  They've been in Chrome, Opera.
[2736.14 --> 2744.92]  The only ones who aren't part of the party yet are Explorer, the new Explorer, and Safari.
[2745.70 --> 2749.00]  And I've actually spoken with some of the guys at the team there.
[2749.06 --> 2750.60]  And they're looking into it.
[2750.66 --> 2751.86]  And it's on their roadmap.
[2754.16 --> 2761.32]  They actually wrote this on their roadmap plan that service workers, it looks like everyone
[2761.32 --> 2764.80]  is requesting this and thinks they need it.
[2764.80 --> 2766.52]  So it looks like we'll add it.
[2767.88 --> 2774.20]  But it might take a while before it lands in Safari, which unfortunately means no iPhone
[2774.20 --> 2775.54]  for now.
[2775.80 --> 2781.34]  But Chrome, Opera, and Firefox for now.
[2782.46 --> 2788.34]  And I've heard it described as allowing you to man in the middle yourself.
[2789.64 --> 2793.24]  Do you think that's an apt description of what service workers do?
[2793.24 --> 2797.34]  Yeah, it's an interesting way to think of it.
[2797.40 --> 2798.88]  Yeah, it's kind of like a proxy server.
[2800.48 --> 2803.02]  It's basically like it sounds like man in the middle.
[2803.20 --> 2805.40]  And what I describe, it sounds very dangerous.
[2805.40 --> 2812.70]  But basically, whatever JavaScript can do in the browser window, you're just taking it one level
[2812.70 --> 2814.58]  up, and it has the same permissions.
[2814.58 --> 2817.66]  It can access the same kind of resources.
[2819.10 --> 2824.16]  Only you can do it where it's a bit more powerful, and you can control the experience a bit more.
[2824.34 --> 2827.56]  Is it attached to the particular tab or window?
[2827.56 --> 2832.32]  No, so it's attached to a certain scope.
[2832.50 --> 2837.52]  So for example, talatera.com slash upup.
[2837.60 --> 2845.12]  You can have a service worker that is attached to every window that is under that directory
[2845.12 --> 2848.52]  in that domain, or any window that is in that domain.
[2848.76 --> 2850.96]  Kind of like cookies.
[2851.60 --> 2853.16]  Yeah, a little bit, you can say.
[2853.16 --> 2858.14]  So it can control any request that is within that scope.
[2858.30 --> 2860.22]  That's how it stays secure.
[2860.96 --> 2862.62]  So I like thinking of it like a proxy.
[2863.68 --> 2867.38]  We're used to server-side proxies or even browser proxies.
[2868.24 --> 2873.82]  And here you have, basically it's like you have a proxy inside the browser window that
[2873.82 --> 2881.54]  you can tell it what to do before it delivers the content to your application or any other
[2881.54 --> 2881.98]  direction.
[2881.98 --> 2884.50]  Maybe, we know what upup does.
[2884.58 --> 2888.14]  It allows you to have offline web apps.
[2888.26 --> 2892.78]  Maybe describe to us how upup uses service workers to get that done.
[2894.38 --> 2894.80]  Yeah.
[2895.14 --> 2903.74]  Okay, so what upup does is it sits above the, it registers a service worker that sits above
[2903.74 --> 2910.24]  the window and intercepts every request that goes, whether the user is asking for the HTML,
[2910.90 --> 2912.32]  images, et cetera.
[2912.88 --> 2915.50]  And it catches that request forward.
[2915.94 --> 2918.12]  It's like, doesn't touch it.
[2918.26 --> 2919.96]  Let it go to the server.
[2919.96 --> 2922.72]  But if, but it traps it in a promise.
[2923.12 --> 2929.84]  And if that promise is broken, that means the server couldn't be reached, whether no internet
[2929.84 --> 2932.76]  or, or even the server is down.
[2932.76 --> 2938.42]  Then that's when upup springs into action and, and says, okay, there's a problem.
[2938.58 --> 2941.14]  Let's see if I have something in the cache to show instead.
[2941.28 --> 2945.90]  It looks for alternate content in the cache and returns that.
[2945.90 --> 2950.18]  So what the user is seeing is, will be instantaneous.
[2950.18 --> 2955.62]  Like the user would go to a certain site and he would immediately get the offline content.
[2955.62 --> 2960.90]  But in the background, it's trying to reach the server, seeing that it fails and showing
[2960.90 --> 2961.84]  you alternate content.
[2962.00 --> 2966.36]  So the offline experience is actually faster than the online experience in that way.
[2967.22 --> 2972.82]  Man, I guess I'm just pedantic about naming, but you know, service worker, like, what does
[2972.82 --> 2973.18]  that mean?
[2973.34 --> 2974.56]  What does that mean to anybody?
[2974.56 --> 2976.34]  It reminds me of web workers.
[2976.54 --> 2980.46]  Can you tell us if there's any relation to web workers at all with service workers?
[2981.36 --> 2981.80]  Yeah.
[2981.90 --> 2987.90]  So I haven't played around much with web workers, but as far as I, as I understand, it's similar
[2987.90 --> 2993.28]  in a way that it is a script that runs in a background thread, in the background.
[2993.42 --> 2993.62]  Yeah.
[2993.76 --> 2994.62]  In your browser.
[2994.78 --> 2996.78]  So I guess that was the source of the name.
[2997.16 --> 2997.48]  I see.
[2997.56 --> 3000.22]  So one's for web and one's for service.
[3000.22 --> 3007.02]  Um, they'll still somewhat confounding, perhaps, you know, perhaps service worker, the name
[3007.02 --> 3012.32]  is one of the reasons why people struggle so much to embrace it and really know what
[3012.32 --> 3013.12]  it's used for.
[3013.16 --> 3018.82]  And maybe it's because it's just generally useful, but doesn't have a specific, uh, uses
[3018.82 --> 3022.82]  beyond just caching, um, where people can really latch onto it.
[3022.82 --> 3024.70]  I like what you do with your libraries.
[3024.80 --> 3028.08]  You seem to kind of take, you know, the cookies down to the bottom shelf, so to speak.
[3028.14 --> 3029.06]  You did that with on young.
[3029.14 --> 3032.40]  You said, let's make the speech recognition available to more people here.
[3032.48 --> 3037.14]  You're saying, let's make this specific feature of service workers, which is offline availability
[3037.14 --> 3039.12]  easier for people to implement.
[3039.12 --> 3044.78]  Um, what were some of the challenges that you ran into with regard to service workers implementation
[3044.78 --> 3047.54]  wise with up, up that you can share with us?
[3048.40 --> 3055.48]  Um, so just understanding how all of this works and fits together is like promises.
[3056.04 --> 3059.08]  They work differently than how we're used to doing JavaScript.
[3059.68 --> 3065.68]  Um, accessing the, the new caching API that is part of a service workers is difficult.
[3065.68 --> 3072.26]  There's been a lot of things that I'm, frankly, I'm still learning, um, or more correctly,
[3072.26 --> 3073.68]  I'm forgetting and relearning.
[3074.42 --> 3078.12]  Um, but it's not that easy to get into.
[3078.22 --> 3083.02]  I mean, there's a lot of things that you can achieve immediately, but if you're looking
[3083.02 --> 3088.02]  for a more sophisticated, uh, use case, there, there's some reading required, some learning.
[3088.14 --> 3089.64]  There's a learning curve there for sure.
[3091.40 --> 3093.36]  How about the learning curve with up, up?
[3093.36 --> 3100.24]  Um, have you found people that need to look under the covers and, you know, figure out
[3100.24 --> 3103.28]  how it's working underneath or has it been a pretty good abstraction layer?
[3104.98 --> 3105.96]  Um, no.
[3106.06 --> 3114.62]  So actually the only people who commented on the, uh, under the covers, as you say, like
[3114.62 --> 3119.30]  on the, uh, on the code of it were people who have been, uh, personally involved with,
[3119.30 --> 3125.26]  uh, the service workers spec and, um, other developers who have been building other service
[3125.26 --> 3125.96]  worker libraries.
[3126.08 --> 3131.94]  They've been looking under the covers and giving some awesome feedback, um, which improved the
[3131.94 --> 3132.30]  library.
[3132.30 --> 3141.76]  Um, but I think it targets, um, the developer who's just wants to build something and have
[3141.76 --> 3146.72]  it work without having to worry about service workers and stuff like that.
[3146.72 --> 3152.20]  Um, there are a few problems there with, uh, the learning curve of up, up in that you need
[3152.20 --> 3155.42]  to realize that it can only control a certain scope.
[3155.80 --> 3161.92]  So if you're placing the, the up, up JavaScript file inside the JavaScript folder, it will only
[3161.92 --> 3163.28]  be able to control what's in there.
[3163.28 --> 3164.66]  So you have to place it in the root.
[3164.66 --> 3171.00]  Um, you have to, uh, another limitation of service workers is your server has to be secure.
[3171.18 --> 3173.74]  So it only works over HTTPS.
[3174.50 --> 3177.40]  Um, but it's built as progressive enhancement.
[3177.70 --> 3181.80]  So if the user's browser doesn't support it, nothing will happen.
[3181.90 --> 3183.00]  It'll just see a normal site.
[3183.06 --> 3184.80]  It won't even load the script file.
[3184.86 --> 3188.42]  So it doesn't affect his, um, performance.
[3188.68 --> 3193.24]  Did you have to actually build that progressive enhancement into up, up, or is that how
[3193.24 --> 3198.42]  service workers are generally maybe, maybe better put, can I shoot myself in the foot
[3198.42 --> 3202.06]  with service workers or do they also just fail gracefully?
[3203.10 --> 3204.92]  No, they, they, they behave.
[3205.04 --> 3212.06]  They've been written based on a lot of experience with, uh, other technologies that have come before
[3212.06 --> 3212.36]  that.
[3212.36 --> 3221.22]  And, um, the guys who've written all of this, which I'll gladly talk about later are the
[3221.22 --> 3224.58]  really, really made sure these things work.
[3224.58 --> 3231.68]  And if you, the, the first thing it does is it tries to register a service worker and if
[3231.68 --> 3234.62]  it doesn't succeed and it doesn't do anything, so it doesn't affect you.
[3235.12 --> 3242.14]  Um, with, with, uh, Anyang, I did have to do some things to make sure, um, it loads the
[3242.14 --> 3245.32]  minimum amount of code before, uh, because it's only Chrome.
[3245.32 --> 3251.44]  So I had to make sure I check as early as possible for, uh, for support.
[3251.44 --> 3254.26]  And if the support isn't there, don't do anything.
[3254.26 --> 3257.76]  So as not to affect users who use unsupported browsers.
[3258.44 --> 3261.52]  So you mentioned that the service worker has to be registered.
[3261.52 --> 3267.64]  So like, um, what is the process of actually registering a service worker back to, I guess,
[3267.66 --> 3269.60]  does it install something to the client?
[3269.70 --> 3271.28]  How does that, what's the process of registering?
[3271.28 --> 3276.20]  So, yeah, um, this is service work is what I'm talking right now in general, not up, up
[3276.20 --> 3276.78]  specific.
[3277.00 --> 3278.46]  Is it different for up, up then?
[3278.56 --> 3281.48]  Or is it, did you have to do some hurdles for up, up to work?
[3281.58 --> 3282.34]  A tiny bit.
[3282.58 --> 3289.52]  Um, what service workers do is when the user first visits the site, it does a register.
[3289.92 --> 3295.18]  I forget the name of the command, but it registers a service worker, which then runs the service
[3295.18 --> 3296.76]  worker script in the background.
[3296.76 --> 3305.76]  And that, um, that has an installation process with then, uh, then shoots an event once it
[3305.76 --> 3306.40]  is installed.
[3306.68 --> 3313.78]  So that means that usually when you first use the, um, uh, arrive at the site and the service
[3313.78 --> 3320.52]  worker is registering and installing, um, it isn't available for the, for the site, uh,
[3320.82 --> 3324.66]  until you refresh and then find that it's already registered.
[3324.66 --> 3333.62]  I kind of did some hacks around that, um, in, uh, up, up to make sure it can, it can communicate
[3333.62 --> 3338.74]  to the service worker, which content you want cached and save that during the first view of
[3338.74 --> 3339.18]  the page.
[3339.78 --> 3342.18]  Um, this has since become a little bit easier.
[3342.42 --> 3347.18]  Um, this was a bit more, uh, it required a little bit of hacking in Chrome 42, I think,
[3347.26 --> 3348.84]  but it's much easier now.
[3348.84 --> 3355.50]  Um, so there's an installation process and then it's ready and you can do things.
[3355.62 --> 3362.36]  And that installation process is a great time, um, to cache content, to download stuff.
[3362.60 --> 3364.78]  Um, that's what it's there for.
[3365.30 --> 3368.84]  So while you're doing the installation, you can, you know, take the payload and also drop
[3369.46 --> 3373.16]  in some, uh, for example, what would you, what would you cache?
[3373.16 --> 3381.08]  So what I do with, uh, up, up, which is one example is when you run it for the first time,
[3381.08 --> 3387.88]  you tell him, I want you to cache this HTML, um, and show this for the user the next time
[3387.88 --> 3388.90]  he doesn't have a connection.
[3388.90 --> 3393.70]  So you can cache that HTML on you and you can also cache additional assets with it, like,
[3393.84 --> 3398.54]  uh, image file, CSS, MP4 is even like anything video.
[3398.54 --> 3403.78]  So it can, it can be, it looks like a full experience, a full web experience, even when
[3403.78 --> 3404.32]  it's offline.
[3404.92 --> 3411.76]  I guess from a user's perspective, I'm thinking of, you know, right now users don't really know
[3411.76 --> 3412.34]  it's available.
[3412.34 --> 3418.68]  So not so much us, like people who are geeks building technology, but users who, you know,
[3418.76 --> 3424.58]  aren't even sure what HTTP means or just, you know, anything in particular about how technology
[3424.58 --> 3425.02]  works.
[3425.02 --> 3428.18]  They're not expecting these applications to not work offline.
[3428.30 --> 3433.20]  So how does, I guess maybe this is more experiential than, than it is technological.
[3433.62 --> 3438.62]  You know, what do you think's happening around educating users that offline is an opportunity
[3438.62 --> 3444.92]  or application developers educating their users that, Hey, you know, while our, our application
[3444.92 --> 3449.06]  might require a lot of online interaction, normally there are some things you could do offline
[3449.06 --> 3451.24]  and to take advantage of it.
[3451.24 --> 3455.62]  So, yeah, as you said, like it should be a part of the experience.
[3455.62 --> 3456.60]  I don't want to educate.
[3456.78 --> 3461.88]  I don't want users to need to be educated, um, what to do differently when it's offline.
[3462.26 --> 3463.94]  Um, it should just work.
[3464.26 --> 3470.38]  Um, and only when it doesn't work and you get that little dinosaur in Chrome or a message
[3470.38 --> 3473.20]  in another browser, do you realize that something stopped working?
[3473.20 --> 3477.98]  And I'm looking forward to a web where that doesn't happen.
[3477.98 --> 3480.38]  Like maybe you'll get a slightly different experience.
[3480.38 --> 3484.24]  Like for example, uh, uh, the guardian just implemented service workers.
[3484.48 --> 3488.38]  So if you're going on the guardian site and you don't have a connection, you get a little
[3488.38 --> 3490.02]  crossword puzzle that you can do.
[3490.02 --> 3494.78]  Um, it's a, something interesting, something trivial.
[3495.58 --> 3496.06]  Yeah.
[3496.20 --> 3498.86]  I mean, you, you'll, you'll notice that it's offline.
[3499.00 --> 3505.54]  It's, uh, but another thing they can do is like, for example, still let you read the last,
[3505.60 --> 3511.80]  uh, 10 articles, even when you're offline, just save the text of the articles, some, uh,
[3511.80 --> 3513.40]  a template and show that to the user.
[3514.14 --> 3515.42]  Um, it's all possible.
[3515.72 --> 3518.52]  Um, the user doesn't even have to notice his offline.
[3518.52 --> 3520.98]  Um, to a certain limit.
[3521.46 --> 3521.82]  Yeah.
[3521.82 --> 3525.58]  Cause there's certain things that, you know, if you think that you're online and take your
[3525.58 --> 3530.30]  booking a situation, for instance, where you can look at your hotel information, you shouldn't
[3530.30 --> 3530.92]  have to be online.
[3531.02 --> 3532.92]  You already have that information in your phone, right?
[3533.34 --> 3535.76]  It should be displayed when you come back to that webpage.
[3536.38 --> 3539.98]  Um, but say you want to change it or you, you know, once you get out of read only mode,
[3539.98 --> 3546.92]  if you're offline and you know, there's no indication to the user that they're offline and just acting
[3546.92 --> 3550.68]  as if they aren't, um, they could create some confusion.
[3550.68 --> 3555.80]  Are there ways in up, up where you can, um, trigger certain things based on the offline
[3555.80 --> 3556.62]  online status?
[3556.62 --> 3559.48]  Or is that just something that you can do natively with the browser?
[3560.16 --> 3564.88]  Uh, not yet, but that is definitely something I'm very interested in allowing you to, to
[3564.88 --> 3572.74]  cache certain actions and, um, cue them in a way so that they can, they can be done once
[3572.74 --> 3577.82]  you're offline, you're online again, but it's definitely where I want to do next with
[3577.82 --> 3578.16]  up up.
[3578.68 --> 3579.12]  Yeah.
[3579.14 --> 3583.48]  I mean, I think that's where offline, it's really tricky is like queuing up, you know,
[3583.48 --> 3585.82]  changes because now reliably.
[3586.04 --> 3586.44]  Yeah.
[3586.44 --> 3592.40]  I changed my, uh, booking time and now the browser can't actually, you know, load that
[3592.40 --> 3593.10]  up to the server.
[3593.10 --> 3597.82]  And then maybe five minutes later I get back online and that, you know, that API call gets
[3597.82 --> 3599.42]  rejected for one reason or the other.
[3599.42 --> 3602.06]  Um, you start to get into all sorts of issues.
[3602.06 --> 3606.34]  I think a great middle ground in the meantime is like, what can you provide?
[3606.54 --> 3608.14]  You know, like start thinking of it like that.
[3608.64 --> 3610.64]  Um, we can put you in a read only mode.
[3610.72 --> 3614.82]  I don't think it's death, you know, telling the person that they're offline and yet showing
[3614.82 --> 3616.32]  them as much information as possible.
[3616.32 --> 3617.64]  People have that understanding.
[3618.40 --> 3620.48]  Um, so indicators I think are valuable.
[3620.68 --> 3622.76]  I think that crossword puzzle is kind of a fun idea.
[3623.38 --> 3629.40]  Um, where, you know, instead of dealing with all the problems of what happens with
[3629.40 --> 3633.20]  these requests as they're queued up and, you know, certain ones are dependent on others
[3633.20 --> 3638.34]  being successful and then seeing that all resolved when the user comes online, uh, which
[3638.34 --> 3644.84]  is technically, you know, can be quite a, uh, assess pool having this like middle ground
[3644.84 --> 3648.84]  between like your Chrome dinosaur and a fully functioning app.
[3650.52 --> 3651.54]  Yeah, for sure.
[3651.54 --> 3654.48]  Um, yeah, it's super important.
[3654.74 --> 3658.70]  Um, but that is something that is right now left to, to each side to implement.
[3658.96 --> 3659.32]  Sure.
[3659.54 --> 3660.58]  Um, yeah.
[3661.00 --> 3664.96]  What about, uh, you know, so you're, you, you basically tell up, up to start on this
[3664.96 --> 3668.08]  page and you tell it which content you want to cache when they come offline.
[3668.62 --> 3668.90]  Yeah.
[3668.92 --> 3672.42]  Like you said, you can pass it HTML or images, these kinds of things.
[3672.42 --> 3680.62]  Are there any limitations or incompatibilities with certain CSS frameworks or JavaScript libraries
[3680.62 --> 3681.80]  or frameworks that you found?
[3684.08 --> 3685.92]  Um, no, not so far.
[3686.00 --> 3691.86]  Cause basically because it doesn't sit within the browser window, it sits in the layer above
[3691.86 --> 3697.64]  it's returned to the browser as if it's a network, uh, as if it's a response from the
[3697.64 --> 3699.52]  network, it just works the same.
[3700.16 --> 3706.32]  Um, as long as of course it doesn't call for resources, which aren't available like JavaScript
[3706.32 --> 3709.24]  from a CDN or something like that.
[3709.24 --> 3715.60]  So you have to, um, you have to make sure all those resources can be cached and made available
[3715.60 --> 3716.46]  when you are offline.
[3718.70 --> 3724.14]  You mentioned before that, uh, that you tried to break it, which made me believe that you
[3724.14 --> 3729.10]  may also try to think about evil ways you can use this, uh, service worker opportunity.
[3729.44 --> 3734.24]  Is there anything that you can think of that might be, um, an evil possibility, so to speak
[3734.24 --> 3735.96]  for, for this to play a part?
[3737.14 --> 3743.58]  Um, no, I had some ideas and I tried to, I tried to do that.
[3743.64 --> 3751.80]  I tried to see if you can return stuff from, um, to bypass the, the existing security mechanisms,
[3751.80 --> 3754.04]  but it's pretty well written.
[3754.74 --> 3756.84]  Um, and this is just something like that.
[3756.90 --> 3757.50]  I like doing.
[3757.60 --> 3760.32]  I've done, I've did, I did it before in a speech recognition.
[3760.32 --> 3768.08]  I've found a number of bugs, which I reported to Google and, um, and most of them, they fixed
[3768.08 --> 3770.72]  a few of them, uh, they didn't.
[3770.72 --> 3776.14]  Um, um, but yeah, it's, it's fun to break things.
[3776.36 --> 3778.76]  I mean, people who make stuff also like to break stuff.
[3779.62 --> 3780.10]  That is true.
[3780.30 --> 3780.86]  That is true.
[3780.86 --> 3788.24]  Well, anything up, uh, on anything up, anything else on up, up, um, that you want to say specifically
[3788.24 --> 3793.10]  to the technology and how it works, um, before we move on to talk about your, your product
[3793.10 --> 3795.02]  thinking and your promotion of your open source projects.
[3797.00 --> 3803.10]  Uh, I think that is the point of the way I work with it to make, to make these things invisible.
[3803.56 --> 3810.30]  Um, um, but service workers are definitely something people should be looking into.
[3810.30 --> 3811.42]  People who are interested.
[3812.08 --> 3814.00]  It's definitely fascinating stuff.
[3814.96 --> 3815.32]  Yeah.
[3815.36 --> 3820.10]  And if you are interested in service workers, um, seeing a real world in use application
[3820.10 --> 3822.64]  of them, such as what's inside of up, up.
[3822.64 --> 3826.58]  It's probably a decent way of, of wetting your teeth, wetting your teeth.
[3826.58 --> 3828.76]  I'm doing it every, I'm doing it left and right here, guys.
[3829.32 --> 3831.56]  Wedding your, wedding your appetite, cutting your teeth.
[3831.90 --> 3833.04]  It's mixing metaphors.
[3833.42 --> 3836.04]  Let's take a break before I shoot myself in the foot again.
[3836.04 --> 3840.64]  And, uh, here one last time from one of our awesome sponsors.
[3840.64 --> 3845.04]  And we want to talk to you on the other side of the break about, uh, this promotion idea,
[3845.04 --> 3851.04]  how you're treating your, uh, open source projects as products and how you are getting
[3851.04 --> 3852.40]  them out there in mass.
[3852.40 --> 3855.36]  So we will talk about that on the other side of the break.
[3855.36 --> 3858.34]  Guess what, everyone?
[3858.60 --> 3863.74]  Opbeat is announcing their Node.js beta right here, right now, exclusively to our listeners.
[3864.60 --> 3869.68]  Opbeat combines performance metrics, release tracking, and error logging into a single simple
[3869.68 --> 3870.24]  service.
[3870.40 --> 3875.34]  And with all of your data in the same place, they're able to do smart things with it and
[3875.34 --> 3876.94]  help you make wiser choices.
[3877.62 --> 3881.76]  Opbeat integrates with your code base through Git and makes monitoring and debugging your production
[3881.76 --> 3882.88]  apps much faster.
[3882.88 --> 3885.76]  It's free for an unlimited number of users.
[3885.76 --> 3891.80]  And until now has only been available for Django and Flask, but now they're launching a private
[3891.80 --> 3895.34]  beta for Node.js and sharing it with our listeners first.
[3895.52 --> 3897.74]  So go check it out and sign up for the beta.
[3897.96 --> 3900.68]  Head to opbeat.com slash changelog.
[3900.78 --> 3906.02]  That's O-P-B-E-A-T dot com slash changelog.
[3908.42 --> 3910.06]  All right, we're back from the break.
[3910.06 --> 3912.42]  You know, it's always been fun.
[3912.62 --> 3913.98]  Anyang, up, up.
[3914.22 --> 3915.10]  A lot of fun.
[3915.20 --> 3920.30]  A lot of enthusiasm behind your pursuit of software, technology, open source.
[3921.84 --> 3924.88]  But you have a pretty good heart for promoting open source.
[3925.66 --> 3928.56]  You've done a pretty good job with these last two releases of yours.
[3928.62 --> 3933.20]  It seems like it's almost easier for you to have some success with your projects.
[3933.20 --> 3935.52]  Do you have secret sauce you can share?
[3935.70 --> 3936.86]  What are you doing well?
[3938.02 --> 3942.22]  What are you doing that's, you know, making these projects so great?
[3942.22 --> 3954.90]  So I think, and I'm making air quotes now, the secret is I was an entrepreneur for many years,
[3955.00 --> 3962.38]  freelancing, working, basically building things from A to Z and having to wear all the different hats,
[3962.38 --> 3967.86]  whether it's marketing, development, planning, all of that.
[3968.08 --> 3975.68]  So that is something that I think a lot of developers sometimes don't do.
[3975.68 --> 3984.68]  Because I know I worked in a company and there's product people and there's marketing people and there's development.
[3985.04 --> 3990.98]  And sometimes it's very comfortable not to do those other things.
[3990.98 --> 4001.14]  But once you get a little bit of experience trying those other things.
[4001.38 --> 4002.66]  I think I know what you're saying, though.
[4002.72 --> 4008.66]  I mean, I'm thinking like people get comfortable with their title or their job or the one thing they do.
[4009.62 --> 4012.74]  And, you know, because I'm a developer, I'm just a hypothetical here.
[4012.74 --> 4022.82]  Because I'm a developer, I can't write marketing copy or I can't help the marketing team say what our product does better than they can because that's their job.
[4022.90 --> 4024.14]  I can't do their job.
[4024.30 --> 4029.70]  But in the case of you, because of your past experience as an entrepreneur and, you know, kind of wearing many hats,
[4029.82 --> 4035.00]  it's easy for you to wear many hats and it's something you actually do well and thrive on.
[4036.40 --> 4036.84]  Yeah.
[4036.84 --> 4041.50]  And like we do it a certain way at our work.
[4041.50 --> 4049.74]  And once we go into open source and we're in charge of wearing all the different hats, it's a totally different issue.
[4050.30 --> 4061.42]  I find that there's like a tension between two opposing forces when you're developing because on the one hand, it's a very private, intimate experience.
[4061.64 --> 4065.28]  I mean, you're developing something that you're passionate about.
[4065.28 --> 4070.42]  You're sitting probably in the dark with headphones and I'm describing myself here.
[4071.50 --> 4075.98]  And writing code, like drinking Red Bulls.
[4076.14 --> 4080.74]  And like, it's very, very personal, very intimate.
[4080.74 --> 4083.16]  And you're so familiar with the code.
[4083.16 --> 4089.08]  And then you want to release it and you expect other people to be as excited about it as you are.
[4089.64 --> 4096.42]  But that is where the other force comes because other people didn't experience it as you have.
[4096.52 --> 4103.80]  So you have to distance yourself from it a little bit and understand how other people see it and look at it with fresh eyes.
[4103.80 --> 4110.84]  And that is something that I find is usually in my projects I've built.
[4110.84 --> 4113.04]  It takes up 90% of the time.
[4113.04 --> 4125.16]  So you build something like Anyang or UpUp and then you work on creating copy and a brand around this.
[4125.32 --> 4128.10]  Like it's a scary word, like brand and marketing and PR.
[4128.32 --> 4131.76]  It's something we're not used to doing, but it's just as important.
[4131.76 --> 4143.98]  Because, I mean, how many times have you seen like people who've released a library and you go and it's like there's a readme and sometimes it's documented or not.
[4144.06 --> 4145.78]  But there's like one star, two stars.
[4145.78 --> 4163.58]  And there's often like amazing libraries, but you need to go past that moment and realize that you need to look at the whole picture and turn it into a product and market it and make sure people want to find out about it and want to try it.
[4165.44 --> 4169.42]  And that is the biggest challenge for people like us, I think.
[4169.92 --> 4174.72]  Something Jared said earlier, which was, you know, we judge books off and by their covers more often.
[4174.72 --> 4185.52]  And I think that was more in reference to us seeing so much software and so much open source that a name matters.
[4185.84 --> 4187.24]  You know, a misspelling might matter.
[4187.50 --> 4190.26]  A collision with another library in a different language matters.
[4191.48 --> 4197.50]  What can you share about, let's say, like the lessons learned from Anyang to UpUp?
[4197.60 --> 4201.04]  Like what did you learn from Anyang that made UpUp even better in terms of releasing?
[4204.72 --> 4221.00]  So all this, I guess, is a matter of time passing because I know me personally, every time I, whether you write code or you design something or you do like fast forward six months later and you hate it.
[4221.00 --> 4224.48]  So maybe this will be the story of UpUp soon.
[4225.04 --> 4234.10]  But I think what I did was a better job at explaining what it does.
[4234.22 --> 4237.56]  So you immediately like it clicks and you immediately get it.
[4237.56 --> 4248.16]  And also to provide a hook right up front that the minute you land on the website, you're like intrigued and want to find out more about it.
[4249.20 --> 4255.84]  There's a, I read an article by one of the, I think the head product guy at Foursquare and Swarm.
[4255.84 --> 4263.42]  And he says there's a, there's a phrase they use a lot there of surprising and delighting users.
[4264.00 --> 4267.28]  So that is something I'm really looking forward to.
[4267.62 --> 4272.88]  That is the hook that catches the person who comes to a site and has like 20 tabs open.
[4273.32 --> 4283.34]  You need to catch him in those first 10 seconds and make him remember your, remember the name and want to actually read what you do before he switches to the next one.
[4283.34 --> 4296.06]  And so that can be something playful, like the name of Anyang or that you just start playing with it and it shows you pictures of kittens or whatever you ask it.
[4296.32 --> 4302.26]  And like there's other references there, like it's showing TPS reports and stuff like that.
[4303.54 --> 4311.16]  In UpUp, for example, that was like a big discussion I had in my head about how to do this.
[4311.16 --> 4317.02]  When you get to the homepage, there's a video on the top of it that doesn't look like a video.
[4317.14 --> 4324.34]  It just looks like an IDE or there's some code and a phone right next to it.
[4324.42 --> 4326.04]  And it doesn't, it looks like an image.
[4326.60 --> 4331.58]  And as the user scrolls down, it starts playing and there's no controls.
[4331.74 --> 4332.86]  It doesn't look like a video.
[4332.96 --> 4334.66]  It just like, looks like a live coding.
[4334.76 --> 4338.46]  And people are like, I've seen people react to it and they're like trying to play.
[4338.46 --> 4343.96]  And then when they're like realizing that it's a video, they're like, oh, they're like surprised.
[4344.74 --> 4354.30]  And that wasn't the safe choice to do there because about, I don't know, I think 20% of people I've showed to have missed that video.
[4354.56 --> 4361.08]  And they were like, oh, there's a video there when I told them later and there's, you should have a play button so we don't miss it.
[4361.08 --> 4371.60]  But it was worth it for me to have missed a couple of people for that reaction from the other 80% who were like surprised by it.
[4371.66 --> 4375.18]  And they were like, oh, and the reactions have been amazing.
[4375.18 --> 4379.48]  Like people have tweeted about it and tweeted how awesome it is.
[4379.58 --> 4383.66]  And that's how, that's how you catch people like in those 10 seconds.
[4383.66 --> 4385.46]  I love it.
[4385.52 --> 4387.56]  It's like an instant demo, honestly.
[4387.74 --> 4396.36]  And it's a passive way too because you might think, well, yeah, I should, you know, I should go to the demo section of your website and I should click a video button or something like that.
[4396.86 --> 4405.42]  But that's a, you know, an explicit way of doing it where you were sort of catching them off guard and surprising them in a way and maybe even delighting them that like, hey, right here real time.
[4405.42 --> 4412.46]  And in about, you know, less than 30 seconds, I can take this example website from an online to an offline version.
[4412.76 --> 4423.64]  And you actually see how easy it is to write, you know, the different scripts in there and include the up-up script and, you know, go through the different functions and, you know, what not to get to this point.
[4423.74 --> 4427.90]  I think it's, that's really awesome to, to, to do that.
[4427.94 --> 4431.36]  And even to take the risk, like, was that totally your idea or did your wife help you?
[4431.94 --> 4435.06]  Did you have some secret party say, hey, you should try this?
[4435.42 --> 4442.48]  Uh, no, that was my idea, but it's, it's not some, uh, stroke of inspiration.
[4442.48 --> 4445.46]  Like this was a painstaking process over months.
[4445.60 --> 4458.64]  Like I built something and I've worked months to, to have a website that I can feel comfortable with releasing, um, polishing and changing and over polishing it and showing it to a lot of people.
[4458.90 --> 4460.62]  It's a painful process.
[4461.54 --> 4462.90]  What drives it all?
[4463.06 --> 4464.12]  What's the, what's your MO?
[4464.12 --> 4465.94]  Why all the time?
[4466.08 --> 4467.02]  Why all the effort?
[4467.96 --> 4490.78]  Cause when, when you build something like that and you're so passionate about it, the, the, the payoff, the, the, that dance that I later do when I find someone doing something is from people actually not just glancing over it and going to the next thing, but actually, um, being caught in it.
[4490.78 --> 4493.88]  And understanding what it is and getting excited.
[4494.54 --> 4507.14]  So that is the most important part of, uh, like polishing that to have that experience from the user is the most important part in my, uh, for me, um, to get that payoff.
[4507.14 --> 4512.32]  To get people to, to, to use it, to get people sharing it and building awesome stuff with it.
[4512.32 --> 4521.66]  So what are, what are all the different parts that go into, uh, thinking about an open source project like a product you can use up, up as an example.
[4521.66 --> 4534.02]  You've obviously stated that the, the name of the project matters that the, the landing page, um, are there other aspects to it that you put so much thought into as, as those things?
[4534.02 --> 4543.90]  So a few other things are, yeah, of course, um, the name, I won't say I'm a hundred percent happy with the name up, up.
[4544.04 --> 4546.94]  I'm happy with anyang because it's a bit weirder.
[4547.70 --> 4557.92]  Um, but, uh, yeah, you have to consider how you let, how people, once they get excited, you have to give them an action to do next.
[4557.92 --> 4567.10]  So you have to consider how they're going to share it and when they share it, how that is going to translate into more people being excited about it.
[4567.44 --> 4575.94]  Um, you have to consider how you approach, um, other coders or bloggers or, um, developers, media.
[4575.94 --> 4577.78]  You have to consider all of that.
[4578.32 --> 4585.82]  Um, you have to consider how people in different countries are going to perceive what you've built.
[4585.82 --> 4590.34]  Uh, for example, anyang, which uses language, which would I, which I don't understand.
[4590.34 --> 4591.80]  So you need to be careful with that.
[4593.62 --> 4596.68]  Um, but Hey, it's not even a real world word.
[4597.24 --> 4597.68]  Yeah.
[4599.20 --> 4604.18]  Um, so there's a lot of thinking that goes and obsessing that goes behind this.
[4604.32 --> 4605.98]  It's, it's a labor of love.
[4606.78 --> 4610.08]  Earlier on, we talked about, you know, you, you ending up on product hunt.
[4610.42 --> 4613.94]  Um, you emailed us, you know, that you have a new project.
[4613.94 --> 4615.76]  Um, you're fine.
[4615.84 --> 4616.12]  You're okay.
[4616.20 --> 4620.32]  You're okay with promoting your projects and, and, um, you stated why.
[4621.36 --> 4626.80]  And, you know, Adam and I even revealed some of our thoughts around like, how do we feel about promoting the changelog on these different venues and stuff?
[4627.28 --> 4629.48]  Um, I think developers kind of have a.
[4630.06 --> 4633.90]  Icky factor when it comes to self-promotion or marketing.
[4633.90 --> 4635.74]  I know that's like, it's considered a bad word.
[4635.74 --> 4642.46]  Um, do you ever feel icky with any of this, the stuff that you do to get your projects out there?
[4642.52 --> 4646.48]  Do you ever feel like you've crossed a line or is it all just par for the course?
[4646.48 --> 4663.48]  No, because I don't think the, the icky experiences I've had were with, with marketers who weren't, who didn't believe in the product, who didn't like when it's someone who's a developer and he truly believes in it.
[4663.48 --> 4666.78]  And he talks about it with passion because he truly loves what he does.
[4667.72 --> 4669.06]  It, I love it.
[4669.14 --> 4679.66]  Like I love watching people, uh, um, do screencasts and talks about their technology because you get caught up in that, uh, excitement.
[4680.70 --> 4682.20]  It's, it's not marketing.
[4682.20 --> 4684.20]  It's just talking about what you love.
[4687.32 --> 4688.42]  It's not marketing.
[4688.54 --> 4689.50]  It's just talking about what you love.
[4689.56 --> 4690.04]  I like that.
[4690.20 --> 4690.58]  I like that.
[4690.58 --> 4691.04]  That's good.
[4693.48 --> 4694.60]  Was that a marketing slogan?
[4694.76 --> 4696.22]  That sounds like a good slogan.
[4696.40 --> 4697.08]  That might've been it.
[4697.26 --> 4697.44]  Yeah.
[4698.78 --> 4700.08]  Uh, I'll, I'll write that down.
[4700.90 --> 4703.52]  We, uh, we have a couple of closing questions.
[4703.62 --> 4706.80]  We obviously love to ask our guests and we've got a super secret one.
[4706.86 --> 4709.90]  I think you got something coming up that you might be able to talk about.
[4710.00 --> 4712.74]  So maybe we'll open with that super secret one first.
[4712.82 --> 4713.30]  What do you think, Jared?
[4713.64 --> 4714.16]  I think so.
[4714.20 --> 4714.72]  Let's do it.
[4714.72 --> 4715.46]  Let's do it.
[4716.44 --> 4722.82]  So, uh, Tal, is there anything super secret that you might be doing in the near future to promote open source?
[4722.82 --> 4724.78]  Something no one else knows about.
[4726.06 --> 4726.62]  Okay.
[4726.74 --> 4733.00]  So I'm actually right now obsessing about my latest labor of love.
[4733.32 --> 4741.74]  Um, as you can see, like, I'm super excited about this other aspects of open source that people usually don't talk enough about.
[4741.74 --> 4747.10]  But I think like, um, you guys do on the change log and that's why I enjoyed a lot.
[4747.16 --> 4753.50]  Cause there's a lot that goes into open source that has nothing to do with the code.
[4753.50 --> 4757.24]  And there's not enough places to talk about it.
[4757.24 --> 4764.52]  So one of the things I've been working on is, uh, is a new blog, a new site called the opensourcer.com.
[4765.28 --> 4771.84]  Um, where I'm going to be talking about everything that has to do with open source and nothing with the code.
[4771.84 --> 4773.60]  I was actually yesterday.
[4773.76 --> 4775.76]  I was like thinking of slogans for that.
[4775.84 --> 4778.84]  And I was like, beyond code, that's a good one.
[4780.42 --> 4781.50]  There's an issue with that.
[4781.58 --> 4784.94]  Like, I couldn't remember why it took me a second.
[4785.20 --> 4786.60]  Where did I hear that before?
[4788.14 --> 4789.24]  It's a good name, right?
[4789.88 --> 4790.18]  Yeah.
[4790.20 --> 4791.08]  It's a great name.
[4791.08 --> 4805.66]  Um, so the idea is, yeah, to talk about all those things, which, which are usually icky for us as developers, um, and turn them into something that you can approach.
[4805.66 --> 4819.62]  How, and so it's issues like once you release an open source library, what do you need to do, um, to make sure people get it, to make sure people, um, instantly understand it, how they can use it.
[4819.62 --> 4822.26]  What, what can you do to build a community around this?
[4822.44 --> 4823.92]  How can you market this?
[4823.98 --> 4828.76]  How can you approach, um, other bloggers or tweet about it?
[4829.42 --> 4839.96]  Um, so the product thinking behind, uh, open source, all those issues, which I think are underrepresented in open source right now.
[4840.62 --> 4844.64]  Um, which is a shame because there's so much good stuff out there.
[4844.64 --> 4847.28]  Like so many libraries that we never even hear about.
[4847.28 --> 4852.70]  Well, trust us, we, we feel the pain, Jared and I wish that we can do daily podcasts.
[4853.70 --> 4858.30]  Um, well, maybe not daily podcasts, but more often than four times a month.
[4858.30 --> 4866.46]  I mean, I feel like every time we turn around, Jared, we're, you know, we're approaching something more interesting, you know, something new in a new language.
[4866.46 --> 4871.80]  Um, and we just, you know, we're always striving to keep up ourselves.
[4871.98 --> 4876.20]  And so any more help in the area of covering open source is always good.
[4876.72 --> 4877.16]  Yeah.
[4877.48 --> 4877.70]  Yeah.
[4877.70 --> 4879.12]  There's so much awesome out there.
[4879.32 --> 4879.72]  Yeah.
[4879.72 --> 4891.92]  You mentioned earlier that you kind of teased when we asked you about, uh, I think Jared said, uh, something to sustainability and mentioned your wife and the travel that you've been doing and whatnot and being newly married.
[4892.48 --> 4898.94]  Um, how, how does sustainability play into Anyang, UpUp, and ultimately the open sourcer?
[4898.94 --> 4904.96]  Obviously, if I, I, I quit, uh, I quit my job, I decided I wanted to open source full time.
[4905.52 --> 4908.40]  Um, I have to be able to support myself somehow.
[4908.40 --> 4911.32]  So that is something I'm looking into right now.
[4911.32 --> 4925.36]  Um, one of the ideas is, uh, an inspiration for me has been actually, um, your shows with, uh, Mike Perham from Sidekick, who built Sidekick as a open source project.
[4925.36 --> 4937.12]  And has turned it into a business by offering, continuing to develop the open source version while developing software, while developing versions for the enterprise.
[4937.32 --> 4939.64]  And he's been thriving doing that.
[4939.70 --> 4941.34]  And it's very inspiring to me.
[4941.76 --> 4944.68]  Uh, actually, I just interviewed him for the open sourcer.
[4945.26 --> 4947.96]  Um, he's a very interesting, uh, developer.
[4947.96 --> 4948.52]  Yeah.
[4949.38 --> 4954.70]  Um, so one of the ideas is to turn.
[4955.36 --> 4957.80]  To create a version of UpUp that is.
[4959.68 --> 4964.66]  Even easier to use, um, and is available to non developers.
[4964.66 --> 4969.76]  So WordPress users, uh, are my main target right now.
[4969.76 --> 4980.06]  So if you have a WordPress site, even just including a script and adding two lines of code, um, sometimes you're uncomfortable with that.
[4980.06 --> 4987.52]  And there's like issues to consider and you have to move maybe your JavaScript from a CD and host it locally.
[4987.96 --> 4991.68]  And so I'm building something that will do all of that automatically.
[4992.36 --> 4998.22]  And that is a service that I believe people are going to be willing to pay a product that people are going to be willing to pay for.
[4998.22 --> 5011.12]  Um, if you're a hotel and you want, uh, people visiting your site to be able to access your, uh, your, um, your address, your details, even when they don't have connections.
[5011.34 --> 5011.76]  Yeah.
[5011.82 --> 5012.96]  It's, it's worth it.
[5012.96 --> 5023.06]  Um, so continuing to develop the open source projects I've been doing so far while considering other commercial aspects for them.
[5023.78 --> 5032.38]  Um, but of course, all of that gets funneled back to, to developing the open source more, just like Mike is doing with Sidekick.
[5032.38 --> 5038.56]  Um, and of course, hopefully one day the open source is going to be doing well.
[5038.80 --> 5040.00]  Maybe that'll be a part of it.
[5040.72 --> 5046.18]  Um, and yeah, maybe, maybe I'll also need to do some, do some consulting, uh, in the meantime.
[5046.62 --> 5048.06]  Uh, I'm open to that.
[5048.80 --> 5053.90]  Um, but the end goal is to build, uh, an open source empire.
[5055.94 --> 5057.38]  You heard it here first, everybody.
[5057.38 --> 5063.28]  We will definitely link up the open sourcer.com in our show notes.
[5063.28 --> 5066.88]  You can find those at changelog.com slash one eight three.
[5068.36 --> 5080.82]  And the last question we have for you here, uh, is the old saw who's your programming hero, but I'm going to just loosen the constraints a little bit since you're a product guy and say, you can pick a programming hero or a product hero.
[5080.82 --> 5084.62]  If you have somebody who has inspired you in your product thinking.
[5084.62 --> 5086.98]  So, um, what you got?
[5087.38 --> 5094.52]  So, uh, my, my hero, um, these days is Jake Archibald.
[5094.62 --> 5097.26]  He's a developer advocate and a Chrome team.
[5097.44 --> 5103.22]  He's also one of the people who wrote, um, the service worker, uh, specification.
[5103.82 --> 5110.76]  Actually, I got the idea for AppApp when I watched him, uh, speak at Google IO, um, a year ago.
[5111.24 --> 5116.54]  Um, he's obviously a great developer and very.
[5117.38 --> 5126.14]  He has done so much great work, but the thing that I find amazing is his ability to use humor to explain things.
[5126.14 --> 5140.48]  And I found myself like sitting in, in a cafe with headphones, uh, listening to, to, to, to one of his videos, explaining how to use service workers and simply laughing out loud.
[5140.48 --> 5164.48]  And people are looking at me, like his ability to, to, to, to, to, to, to draw comparison between, uh, um, between bad connections and, and, and, and, uh, one legged dog who is trying with the whole, all his, uh, might to fetch something, but his, all his enthusiasm doesn't work.
[5164.48 --> 5171.80]  Like his ability to use humor to explain things is, is, uh, is, uh, remarkable and it's inspiring.
[5171.80 --> 5180.38]  So definitely like, if you have some time, check out, uh, a few of his videos on YouTube.
[5180.38 --> 5181.74]  Very cool.
[5182.34 --> 5197.96]  Well, it's, uh, tell us, it's definitely been a pleasure having you on to, to learn about your passion behind software development and you're, you know, you're all in on open source and the work you've done on young and up, up and, uh, coming on here and sharing that with, uh, the open source community is, is really great.
[5197.96 --> 5204.20]  Look forward to the work you're doing with the open source or when, and we'll obviously, uh, you know, be here to help you.
[5204.28 --> 5205.64]  However, we could possibly help you.
[5206.50 --> 5210.80]  Um, any other closing thoughts before we close out the show on your side?
[5211.78 --> 5214.42]  No, I mean, thank you.
[5214.68 --> 5224.10]  Thanks for all, uh, like the changelog has really been an inspiration for a lot of, uh, this for, for talking about things that are not just code specific.
[5224.10 --> 5234.42]  I mean, I listened to other podcasts, which are like language specific, but talking about the bigger, the bigger picture, um, issues that affect all of us.
[5234.46 --> 5236.68]  That is something that has inspired me to do that.
[5237.00 --> 5237.66]  Very cool.
[5237.68 --> 5238.62]  So thanks guys.
[5239.10 --> 5239.54]  Yeah.
[5239.54 --> 5240.54]  Thank you for listening.
[5240.76 --> 5248.70]  And, uh, to those who are actually listening to this show, not just here on these mics talking, thank you for listening to those members out there that support us.
[5248.70 --> 5250.14]  Uh, we, we definitely thank you.
[5250.14 --> 5258.26]  We have four awesome sponsors, CodeChip, TopTile, Braintree, and OpBeat, uh, supporting this here particular show.
[5258.96 --> 5261.50]  But, uh, fellas, it's time to say goodbye, so let's do it.
[5261.78 --> 5262.00]  Goodbye.
[5262.42 --> 5262.88]  Thanks guys.
[5262.94 --> 5263.10]  Bye.
[5263.10 --> 5263.14]  Bye.
[5280.14 --> 5288.90]  Thank you.
[5289.00 --> 5306.00]  Bye.
[5306.00 --> 5306.40]  Bye.
[5306.44 --> 5306.90]  Bye.
[5306.90 --> 5309.04]  Bye.
