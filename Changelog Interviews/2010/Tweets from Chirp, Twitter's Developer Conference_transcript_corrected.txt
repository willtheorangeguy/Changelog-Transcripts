[0.00 → 3.38] I'm Christy Taylor with Open Source Bridge, and you're listening to The Change Log.
[16.58 → 22.24] Welcome to The Change Log, episode 0.2.1.
[22.42 → 23.60] I'm Adam Stukowiak.
[23.76 → 24.72] And I am Won Netherlands.
[24.86 → 26.94] We cover what's fresh and new in the world of open source.
[26.94 → 31.00] If you found us on iTunes, we're also on the internet at thechangelog.com.
[31.20 → 35.90] For a real-time view of the happenings on GitHub, check out tale.thechangelog.com.
[36.60 → 39.72] And speaking of GitHub, go over to GitHub.com forward slash explore,
[39.84 → 42.48] where you'll find some training repos, some featured repos,
[42.52 → 44.68] as well as the audio podcast from The Change Log.
[45.10 → 49.78] If you're on the Twitter, you can follow changelog show, not the changelog,
[50.00 → 51.72] and also Adam Stack.
[52.68 → 55.12] And I'm Penguin, P-E-N-G-W-Y-N-N.
[55.12 → 59.68] And such a fun time out in San Francisco last week at the Chirp Conference,
[59.78 → 61.58] the first ever Twitter developers conference.
[62.12 → 64.72] Loads of fun, lots of new happenings with the Twitter API,
[65.02 → 69.54] and finally got to match faces with avatars from folks I've worked with the last couple of years.
[70.84 → 72.82] And who do we speak with over there?
[73.56 → 75.12] We spoke with Hayes Davis from Austin.
[75.12 → 80.10] He maintains a Twitter Ruby library competing with the Twitter gym.
[80.10 → 85.12] And then we also met with Christy Paler from Open Source Bridge.
[85.24 → 91.64] It's a cool new popular conference up in Portland, up in June.
[92.04 → 99.18] And then we also spoke with John and Eric from 140 Proof Ads about some cool open source projects they've got.
[99.34 → 105.34] One of them is kind of an ambient sound project for monitoring your log files.
[105.48 → 106.56] I think you'll get a kick out of it.
[106.56 → 107.98] Oh, wow. Sounds kind of fun.
[108.54 → 110.26] It was. Fun to be back.
[111.36 → 114.08] Got a great interview lined up this week with Facebook.
[114.54 → 117.16] So hopefully this will air before we record that interview.
[117.30 → 119.32] If you've got questions for the Facebook team, let us know.
[119.54 → 122.88] Anything about hip-hop or the 320 iPhone platform?
[123.64 → 124.52] Yeah, that sounds exciting.
[124.52 → 127.62] I'm actually really excited about the Thursday recording.
[127.80 → 130.46] It's exciting to see what Facebook is doing in Open Source
[130.46 → 133.40] and also to have them on the show even better.
[133.40 → 136.54] You know, and Facebook has their F8 conference this Wednesday.
[136.66 → 139.40] Hopefully there will be a ton of news coming out of the conference
[139.40 → 142.04] and we can talk to these guys firsthand about it on Thursday.
[142.42 → 144.14] Maybe a scoop. Who knows?
[144.62 → 145.06] Hope so.
[145.72 → 146.58] Great interview this week.
[146.80 → 147.82] Or interviews, I should say.
[147.88 → 148.42] Should we get to it?
[148.70 → 149.34] Yeah, let's do it.
[149.34 → 160.20] All right, we're joined by Eric Michaels-Over
[160.20 → 163.48] and John Mongolian from 140 Proof
[163.48 → 165.48] talking about some open source stuff they're doing out there.
[166.24 → 167.04] Hey, how's it going?
[167.28 → 167.84] I'm Eric.
[168.92 → 169.70] Hey, what's up, man?
[169.72 → 170.16] It's GM3.
[171.08 → 171.32] Cool.
[171.38 → 172.38] So you guys have a couple of projects
[172.38 → 175.10] we're going to feature in this Chirp Roundup edition,
[175.44 → 176.84] the first one being Racket.
[177.24 → 178.16] So who's responsible for Racket?
[178.16 → 178.86] Let's talk about it.
[179.14 → 179.82] I am.
[179.88 → 181.50] We both work on it, Eric and I, together.
[181.68 → 184.52] But it came out of an idea that I had a long time ago.
[184.54 → 186.34] I was reading a paper by a guy who had built
[186.34 → 187.72] what he called a sonic compiler.
[188.28 → 189.90] And so this was back in the days when, like,
[189.98 → 190.90] most code was compiled.
[191.34 → 192.66] And so you'd be running your C compiler
[192.66 → 194.34] and as it was outputting different warnings
[194.34 → 195.96] and dramas and errors and whatever else,
[196.22 → 197.28] it would actually make audio
[197.28 → 199.16] corresponding to what the compiler was doing.
[199.44 → 200.78] And so you'd kind of walk across the room
[200.78 → 202.08] and go get a cup of coffee or something
[202.08 → 203.66] and just listen to how your program was doing.
[203.70 → 204.68] You'd be able to tell right away, like,
[204.92 → 206.92] oh, crap, you know, it's doing all this crazy stuff.
[206.92 → 209.80] And so what we are at 140 Proof
[209.80 → 210.76] is we're kind of data geeks.
[210.86 → 211.84] We have a lot of graphing.
[211.94 → 212.66] We have a lot of stats.
[212.76 → 213.66] We're an advertising platform.
[213.76 → 215.10] So there are just tons and tons of data.
[215.54 → 217.98] And so ambient visualization is fascinating to us
[217.98 → 220.46] because otherwise you just get drowned in the data.
[220.56 → 222.76] And so we said, you know, everybody does visualization.
[223.16 → 224.52] What if we did ruralization
[224.52 → 226.30] and we had sort of an audio representation
[226.30 → 227.96] of our app in real time
[227.96 → 230.34] so that you could actually listen to the performance of your app
[230.34 → 232.72] and kind of out of the corner of your ear or whatever
[232.72 → 234.16] detect when things are going wrong?
[234.36 → 236.14] Eric can tell you, like, a little more about how it works.
[236.14 → 236.62] Sure.
[237.52 → 241.56] So, yeah, basically we just map events in a log table.
[241.74 → 245.84] So you can use regular expressions to define, you know,
[245.90 → 247.82] certain events in a log file.
[248.34 → 252.04] Map those to an audio file, so like a WAV or AIF or whatever.
[252.62 → 254.44] And that way when good things are happening,
[254.64 → 256.72] you can hear positive sounds.
[256.80 → 257.96] When neutral things are happening,
[258.18 → 261.22] it's sort of just good ambient noise in the background.
[261.22 → 262.56] And then when there are errors,
[262.68 → 264.22] you can also have sort of louder noises
[264.22 → 266.16] or more dissonant alerts.
[266.78 → 267.56] What we've done,
[267.64 → 270.70] because we're basically a Twitter app company,
[271.12 → 273.84] we've mapped most of the good sounds to birds chirping.
[274.06 → 275.66] So when the app's running fine,
[275.72 → 276.60] when good things are happening,
[276.70 → 279.32] it sort of sounds like this aviary in the background.
[279.56 → 282.08] And then there's a big, loud, meowing cat
[282.08 → 283.36] whenever there's an error.
[284.02 → 284.68] I love it.
[284.68 → 285.66] So how do you spell racket?
[285.88 → 288.40] Like the tennis racket or like the sound racket?
[289.30 → 290.92] Like the sound racket.
[291.30 → 291.70] Cool.
[291.76 → 292.74] And what's the GitHub URL?
[293.54 → 295.22] I think the latest version,
[295.38 → 296.90] I don't even know what the master is,
[297.08 → 299.56] but I think it's probably jm3,
[300.02 → 302.78] GitHub.com slash jm3 slash racket.
[303.28 → 306.64] Any dependencies on language or is it just standalone?
[307.10 → 308.16] It's written in Ruby,
[308.16 → 310.36] and I think it has some crazy dependencies,
[310.82 → 312.44] but they're in the gem file.
[312.44 → 314.32] I think we've simplified the dependencies.
[314.54 → 315.38] In the beginning days,
[315.46 → 317.16] it required like 14 Ruby libraries,
[317.34 → 319.76] because as I found playing sound in Ruby,
[319.86 → 322.64] it was very kind of non-trivial.
[322.88 → 324.90] I come from actually like a Flash multimedia background
[324.90 → 326.38] where it's super easy to play a sound file.
[327.10 → 327.94] So we've kind of,
[328.46 → 330.06] Eric has kind of helped us simplify the dependencies.
[330.22 → 332.42] So I think now you can pretty much run,
[332.66 → 333.60] I forget if there's a make script
[333.60 → 334.76] or there's a Ruby setup.Rb,
[335.10 → 335.58] run that,
[335.58 → 337.08] it pulls all the dependencies, and you're good to go.
[337.22 → 338.34] But can I watch any log file?
[338.92 → 340.14] Yeah, it's pretty customizable.
[340.38 → 342.02] So you just define the regular expressions
[342.02 → 344.84] to match whatever sort of strings you want,
[345.24 → 347.12] and then it'll play any sound.
[347.44 → 348.04] I forgot to mention,
[348.14 → 350.30] so this project also owes a huge debt
[350.30 → 352.80] to kind of inspiration from Fuji's GL tail, right?
[352.86 → 354.36] So GL tail is kind of this thing
[354.36 → 356.02] that can take arbitrary log files.
[356.12 → 356.70] You have a parser,
[356.92 → 358.02] it listens to that log file,
[358.06 → 359.18] and then it does these visualizations.
[359.42 → 360.14] And we were like,
[360.34 → 361.00] all right, that's cool,
[361.08 → 362.74] but how can we make it our own
[362.74 → 363.94] and kind of enhance that a little bit?
[363.94 → 366.02] So we definitely owe a debt of inspiration to that.
[366.74 → 368.22] So Eric was eavesdropping,
[368.28 → 369.20] I was talking to the Heroku guys
[369.20 → 369.94] about Pairing,
[369.94 → 371.46] and I was talking earlier,
[371.50 → 372.64] and he says it's the new MIR.
[373.00 → 374.94] He got us talking about some MIR admin stuff
[374.94 → 375.74] he wrote back in the day
[375.74 → 377.62] that he's got a new project called Rails Admin
[377.62 → 379.34] that he's working on for Rails 3.
[379.52 → 380.12] Let's hear about it.
[380.54 → 382.68] Yeah, so way back in the day,
[383.10 → 383.52] we were,
[383.88 → 385.68] before we were building Rails 3 apps,
[385.76 → 386.96] we were building MIR apps.
[386.96 → 390.04] And one sort of thing
[390.04 → 392.44] that's always been missing from Rails
[392.44 → 394.46] and was also missing from MIR
[394.46 → 397.46] is this nice admin interface
[397.46 → 400.74] that actually exists in the Python web framework Django.
[401.12 → 403.30] So basically what I did for MIR admin
[403.30 → 406.30] was I just took all the CSS and JavaScript
[406.30 → 408.44] from Django
[408.44 → 410.82] and rewrote the backend in Ruby
[410.82 → 413.72] and made it basically a MIR slice,
[413.84 → 415.32] which is kind of their plugin architecture,
[415.32 → 418.22] so that all you did was define your models
[418.22 → 419.78] and add this plugin
[419.78 → 421.28] and you would get this nice admin interface.
[421.94 → 424.44] And now I'm rewriting that for Rails 3.
[424.64 → 427.06] So it should be live and ready to go
[427.06 → 427.70] as soon as,
[428.24 → 430.36] before Rails 3 official launches.
[430.78 → 431.66] Active model base,
[431.80 → 433.68] is it ORM agnostic?
[433.94 → 436.68] So MIR admin was ORM agnostic.
[437.20 → 439.04] So the V1 that I'm working on now,
[439.18 → 440.54] just to kind of get it working,
[440.76 → 441.80] is active record only.
[441.80 → 444.94] But the original MIR admin,
[445.18 → 446.84] which you can still use if you have a MIR app,
[447.60 → 449.48] worked completely agnostically with,
[450.02 → 452.92] there were adapters written for active record
[452.92 → 455.22] as well as data mapper and SQL.
[456.06 → 456.88] So, yeah.
[457.08 → 458.02] So basically unfold,
[458.14 → 459.82] you get CRUD screens for your models,
[459.92 → 460.94] is that the notion?
[461.20 → 464.00] Yeah, and it looks exactly like the ones for Django.
[464.16 → 466.00] So basically all the functionality that's in that
[466.00 → 466.76] you would have,
[466.84 → 468.90] which is, you know, I'm a Ruby guy,
[468.90 → 471.36] but I really like the Django admin app.
[471.68 → 473.08] We steal everything from Python, don't we?
[473.86 → 474.58] No comment.
[475.38 → 476.26] Well, thanks, guys.
[483.64 → 485.92] Hi, we're talking to Hayes Davis from Austin, Texas,
[486.52 → 489.12] about his Twitter API wrapper called Grackle.
[490.00 → 490.30] Hi.
[491.48 → 493.02] Hayes, tell the audience, I guess,
[493.08 → 494.58] who you are and what you're doing with the Twitter API.
[495.12 → 495.50] Sure.
[495.50 → 497.78] Like Won said, I'm Hayes Davis.
[498.40 → 499.98] I run CheapTweet.com,
[500.10 → 501.78] which is a search engine for all the deals,
[501.90 → 503.76] sales, and coupons people talk about on Twitter,
[503.88 → 505.62] as well as TweetReach.com,
[505.70 → 508.10] which is a Twitter campaign analytics tool.
[508.54 → 511.34] So that's who I am, a developer,
[511.62 → 514.54] and the founder of the company that does both those things.
[514.96 → 518.50] So there's already a Twitter API wrapper out there.
[518.58 → 522.28] Some of the books may maintain that one for John Wanamaker's Twitter, Jim.
[522.34 → 522.92] Why Grackle?
[523.24 → 524.30] What problems are you trying to solve?
[524.90 → 527.10] Well, because the other wrappers out there, it's terrible.
[527.54 → 527.64] No.
[528.28 → 531.94] No, you know, I had a specific set of needs when I was building Cheap Tweet,
[532.10 → 536.80] and basically the core thing that I came up with is my problem with the Twitter API
[536.80 → 538.64] was a fast-moving target,
[538.86 → 542.48] and it was, at least at the time especially, a little bit of a flaky target.
[542.62 → 545.74] So you never quite knew exactly what you were going to get back,
[545.90 → 548.14] and you knew things were going to change a lot.
[548.14 → 553.00] So basically the way I implemented Grackle was just assuming change from the beginning,
[553.16 → 556.46] and I tried to provide a very lightweight wrapper around the API.
[557.14 → 563.32] So Grackle's method syntax basically mirrors the calls that you make to the API,
[563.52 → 565.24] REST endpoints, precisely.
[565.64 → 567.30] And that's actually all done dynamically.
[567.30 → 572.38] So if they introduce a brand-new endpoint, it doesn't require any updates to Grackle.
[572.46 → 577.30] You can actually just chain your calls together and access that endpoint without any other work.
[577.50 → 579.00] So no new releases for me.
[579.32 → 583.02] It's less work for me, and I think most people want to be able to just go ahead and get started.
[583.02 → 585.92] Sure, and I should say I'm a fan of Grackle too.
[586.16 → 588.84] I've used it as well in a number of projects.
[589.42 → 591.70] You know, it provides a very different experience.
[591.84 → 596.64] I think one of the things that the Twitter gem does is abstracts a lot of the API,
[596.90 → 600.26] where Grackle you have to know more about the API you're implementing,
[600.38 → 601.74] but that's also a good thing and a bad thing.
[601.78 → 602.36] Why don't you speak to that?
[602.90 → 603.14] Sure.
[603.28 → 606.28] I mean, I think depending on the level of extraction you want,
[606.38 → 609.50] I mean, I think that can be very, very good, right?
[609.50 → 613.66] If you really want to interact with something that's very clearly a user object
[613.66 → 617.84] that has methods on it to access information about that user, I think that works great.
[617.92 → 621.70] I think what happens is you get locked into a particular model.
[621.70 → 628.52] So at one point, whenever they change the model, and they add new things,
[628.62 → 631.88] then I think that you get a little bit of leakage there.
[631.96 → 633.26] You have to kind of work around things.
[633.64 → 639.20] So I feel like a lot of times I end up doing better when I work with other APIs,
[639.20 → 646.34] just staying kind of light above it and not wrapping it with a lot of other assumptions
[646.34 → 648.58] about how that API is going to work.
[648.66 → 652.44] I mean, one of the first APIs I worked with in Ruby was Flickr.
[652.74 → 655.26] And I just felt one of the, you know, I tried a couple different gems,
[655.36 → 657.88] and I just felt like they had layered all this stuff on top,
[657.94 → 659.44] and there had been some, you know, change.
[659.68 → 662.24] And, you know, it was just, it wasn't a great experience.
[662.24 → 666.60] And so I felt like I like to be a little bit closer to the endpoints, but that's just me.
[666.60 → 672.18] You know, one of the benefits of that is your API doc is now your wrapper doc, right?
[672.48 → 673.04] Yeah, absolutely.
[673.24 → 675.54] So, you know, I definitely like that part of it.
[675.96 → 682.00] And also it feels fairly Rubbish to me to be able to just kind of say, you know,
[682.08 → 686.34] here's my magic incantation, which looks like the URL that I'm trying to hit,
[686.40 → 689.12] and the parameters kind of look like the parameters that are being passed.
[689.34 → 692.78] And, you know, it just, it feels Rubbish to me.
[692.92 → 693.70] So I like that part.
[693.70 → 696.18] Let's talk a moment for the Ruby nerds out there.
[696.30 → 698.14] How are you pulling off this syntax?
[698.40 → 701.12] Is it method missing, or how are you mirroring those?
[701.50 → 701.78] Sure.
[701.92 → 706.32] So the way the syntax works is, yeah, I mean, so short answer, yes, primarily method missing.
[706.82 → 710.66] But basically what I do is I have to know when you're done, right?
[710.66 → 715.56] So the actual tricky part was to know that once you've chained together this random set of calls,
[715.66 → 717.50] I have to know that you're wanting to execute it.
[717.50 → 722.96] So I implemented, one thing that I kind of like is that when the last method, you can end it with a bang,
[723.18 → 725.08] and if you end it with a bang, that's a post.
[725.42 → 726.84] If you end it with a question mark, it's a get.
[726.94 → 728.58] And to me that just felt, it felt right.
[728.66 → 731.04] You're like, I'm going to change something, or I'm going to just retrieve it.
[731.48 → 733.64] And so it actually, again, it looks kind of like the URL.
[733.64 → 739.54] But you can also do different formats, so it actually checks for a bang, a question mark,
[739.74 → 745.90] or if you end it with like .Jason or .xml, and you can bang and question mark those depending on what you want to do.
[747.06 → 748.72] Since then, we've had to tweak things a little bit.
[748.82 → 755.78] They've actually tweaked the lists API, for example, is actually more restful than some of the other APIs.
[756.06 → 760.28] So we've allowed some syntax for puts and deletes and all that stuff as well.
[760.28 → 764.66] So that's fitting because I think most of my AP calls either end with a bang or end with a question.
[766.08 → 767.24] Why the name Grackle?
[768.16 → 773.10] So if you're not from Austin, you won't probably have seen these really annoying birds.
[773.80 → 775.60] But this is my nod to Texas.
[775.88 → 780.04] It's like a, a Grackle is a bird, so of course, you know, on Twitter you've got to have some kind of bird thing.
[780.10 → 781.48] At least it's not murder, all right?
[783.30 → 788.66] But basically, you know, they're this kind of like crow on steroids, sort of super crow thing.
[788.66 → 790.26] And anyway, I just like the name.
[790.48 → 792.08] So I actually can attribute that to my wife.
[792.18 → 793.22] She told me, she gave me that.
[793.98 → 794.38] Kudos.
[794.78 → 798.98] Well, plug the services that you built one more time, Cheap Tweet and Tweet Reach.
[799.50 → 799.98] Yeah, sure.
[800.52 → 801.42] CheapTweet.com.
[801.60 → 808.02] And also you can follow us on Cheap Tweet, and you'll be able to, you know, find all the deals, sales, and coupons that people are talking about.
[808.14 → 809.48] And there's a lot out there.
[809.66 → 812.08] We found more than a million last month alone.
[812.30 → 813.68] So they're out there.
[813.76 → 815.48] There are all sorts of interesting stuff.
[815.58 → 818.36] It's not just kind of things you can find anywhere else.
[818.36 → 819.84] It's lots of things.
[820.02 → 820.54] You know, it's Twitter.
[820.66 → 821.64] It's all sorts of stuff happening.
[821.88 → 824.40] And Tweet Reach is Twitter campaign analytics.
[824.76 → 833.40] So if you're into marketing PR or know someone who is, this is kind of the service for them to see what's been happening with links or hashtags that have been spread around Twitter.
[833.40 → 838.68] We should mention we're outside the Chirp conference for audio, and that's what the seagulls are.
[839.48 → 845.80] One final thing I've been asking if you're familiar with the show, The Change Log, you know, we ask in all the interviews with, what's in your open source radar?
[845.98 → 851.04] Here I've been asking the Twitter developers what's got you most excited about the developments here at Chirp.
[851.04 → 855.96] So I think the thing I'm most excited about is actually annotations.
[856.52 → 860.54] I think that could open up just some really amazing stuff.
[861.04 → 862.28] I was a little worried here.
[862.40 → 865.90] I just heard that it sounds like you might not be able to annotate existing tweets.
[866.10 → 868.84] And that might, so I don't know, I could put a little bit of a dampener on it.
[868.84 → 877.12] But there are so many different things you could do with different clients able to add different metadata that other clients could potentially consume and interact with.
[877.56 → 882.72] And then just depending on what Twitter does, the ability to query tweets by, you know, random metadata.
[882.88 → 886.00] I mean, there's a lot of power there to really surface some interesting stuff.
[886.00 → 890.64] So I'm eager to see what happens with that, as Ryan said, next quarter or whenever we're going to see that.
[891.42 → 892.32] Cool. Thanks, Hayes.
[892.50 → 893.18] Yeah, thanks, man.
[898.84 → 909.66] We're joined today with Christy Paler from Open Source Bridge in Portland, a new conference for open source.
[910.56 → 914.26] Explain to the folks what the conference is about and what you're doing up in Portland.
[915.30 → 919.70] Yeah, this is our second year doing the conference, and it's geared towards open source developers.
[920.10 → 924.76] The last day is actually conference, but the first three days are scheduled.
[925.38 → 928.12] And we're actually working on finalizing the schedule now.
[928.12 → 932.18] So it'll be posted on the website soon, opensourcebridge.org.
[932.58 → 935.74] And it's an all-volunteer-run grassroots conference.
[935.96 → 939.98] Last year we had about 500 people, and I think we'll have about that many this year.
[940.40 → 945.56] Tickets are pretty cost-effective, and it's in beautiful Portland in the first week of June.
[945.74 → 947.42] So consider, come on out.
[948.76 → 950.48] Any idea who might be speaking?
[950.58 → 952.84] I know you're finalizing the panel, Maggie.
[952.84 → 959.32] I know that Mayor Sam Adams come out to do one of the keynotes.
[959.56 → 964.42] I really shouldn't speak to the rest of the schedule until we get it posted on the site, though.
[965.46 → 966.84] And last year you had about 500 attendees.
[967.70 → 968.22] What about this year?
[968.30 → 968.68] What do you expect?
[969.48 → 970.54] I expect about the same number.
[970.94 → 972.06] So we're going pretty strong.
[972.14 → 973.94] We had awesome feedback last year.
[973.94 → 979.10] One of the really cool things about the conference is that we have an on-site 24-hour hacker lounge.
[980.22 → 988.58] So after the sessions are done, you can hang out and get stuff done, get code contributed to your projects, and learn from your peers.
[989.88 → 991.40] What's the language representation?
[991.62 → 993.06] I know you're a PHP developer by day.
[993.14 → 995.18] What's the language breakdown, do you think?
[995.18 → 1000.56] From the talks that we got and the talks that we're considering, it's all over the board.
[1000.66 → 1002.72] We've got some good PHP talks.
[1003.38 → 1007.32] We have a lot of embedded development that will be represented this year.
[1008.48 → 1011.80] Ruby, Perl, things on Carrot.
[1011.94 → 1014.52] There will definitely be some DevOps talks.
[1015.16 → 1017.00] So I think it's a perfect spread this year.
[1017.14 → 1017.70] It's going to be awesome.
[1018.62 → 1020.84] On the changelog, we covered NoSQL quite a bit.
[1021.00 → 1023.36] So any NoSQL coverage in those talks?
[1023.36 → 1029.18] We will definitely have some NoSQL talks, including a talk on maybe it shouldn't be called NoSQL,
[1029.40 → 1035.60] maybe how relational databases and non-relational databases can help solve problems for people.
[1036.58 → 1037.14] Awesome.
[1037.30 → 1041.74] So you mentioned earlier, Elf Mike, about your day job with Shop Igniter.
[1042.04 → 1043.76] Explain to the folks what that is.
[1045.00 → 1048.74] Shop Igniter is an e-commerce startup, and we're pre-launch.
[1048.80 → 1050.80] We're going to be launching very soon, in the middle of May.
[1050.80 → 1054.78] And we're based on the PHP platform CodeIgniter.
[1056.54 → 1061.46] And, yeah, so look more for information about Shop Igniter, ShopIgniter.com.
[1062.40 → 1063.68] Anything out of a community edition?
[1063.80 → 1064.50] Will that be open source?
[1065.78 → 1066.30] Yeah.
[1067.02 → 1070.16] We are offering a SaaS right now on the Rackspace cloud,
[1070.16 → 1074.86] and eventually we'll have a downloadable community edition that is open source.
[1075.34 → 1076.66] So we're really looking forward to that.
[1077.66 → 1077.98] Awesome.
[1078.04 → 1080.88] One more time, plug the website for the conference and how folks might sign up.
[1081.64 → 1086.22] Go to opensourcebridge.org, and there's information there on how to register.
[1087.26 → 1088.44] And on Twitter, you are?
[1088.44 → 1094.38] I am Christy Paler, C-H-R-I-S-T-I-E-K-O-E-H-L-E-R,
[1094.58 → 1098.56] and open source bridge is Oxbridge, and Shop Igniter is Shop Igniter.
[1099.64 → 1100.34] Thanks, Christy.
[1100.34 → 1101.02] It was literally...
[1101.02 → 1109.76] Thank you for listening to this edition of The Change Log.
[1109.76 → 1117.54] Point your browser to tail.thechangelog.com to find out what's going on right now in open source.
[1118.68 → 1124.26] Also be sure to head to GitHub.com forward slash explore to catch up on trending and feature repos,
[1124.36 → 1127.28] as well as the latest episodes of The Change Log.
[1127.28 → 1132.08] Safe in your arms
[1132.08 → 1135.74] As a dark passion show
[1135.74 → 1140.20] Was mine alone
[1140.20 → 1145.98] Open, open
[1145.98 → 1150.18] For us to try
[1150.18 → 1153.68] Bring it back, bring it back to
[1153.68 → 1155.66] Open
[1157.28 → 1185.98] Other
[1185.98 → 1186.68] However
