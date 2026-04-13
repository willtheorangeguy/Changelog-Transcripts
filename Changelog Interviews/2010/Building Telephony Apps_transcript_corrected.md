[0.00 → 18.00] Welcome to the Changelog episode 0.4.1.
[18.26 → 19.18] I'm Adam Stachowiak.
[19.54 → 20.34] And I'm Wend Netherlands.
[20.64 → 21.50] This is the Changelog.
[21.54 → 23.54] We cover what's fresh and new in the world of open source.
[24.04 → 26.94] If you found us on iTunes, we're also on the web at thechangelog.com.
[27.38 → 28.24] We're also up on GitHub.
[28.24 → 34.56] At thechangelog.com slash explore, you'll find some trending repos, some feature repos from our blog, as well as our audio podcasts.
[34.80 → 37.16] If you're on Twitter, follow ChangeLog Show.
[37.60 → 38.32] Not the Changelog.
[38.76 → 39.52] And I'm Adam Stack.
[39.72 → 42.20] And I'm Penguin, P-E-N-G-W-Y-N-N.
[42.70 → 43.90] Fun episode this week.
[44.10 → 46.04] But first, I guess, happy anniversary.
[46.58 → 47.08] Yeah, man.
[47.12 → 47.92] Happy anniversary, Wend.
[48.76 → 50.44] About a year ago, we cranked this thing up.
[50.52 → 55.78] I remember doing episode three for my in-laws at Thanksgiving, talking to Rob Pike over at Google.
[56.44 → 57.26] Rob Pike.
[57.44 → 57.70] Google.
[57.88 → 58.14] Go.
[58.38 → 59.06] It's a great episode.
[59.20 → 60.86] If you haven't caught that one, check that one out.
[61.24 → 61.78] Did you have a good holiday?
[62.26 → 63.36] I had an awesome holiday.
[63.44 → 63.86] How about you?
[64.22 → 64.78] Great holiday.
[65.04 → 65.88] It's one of my favourites.
[66.10 → 69.06] You know, to sit back and reflect, which we're thankful for this year.
[69.14 → 71.16] I know we're both thankful for the guys over at GitHub.
[71.70 → 74.94] Got a great announcement, but we should mention who we talked to first.
[74.98 → 75.58] Who'd you talk to?
[76.12 → 80.60] Talked to Chris Matthew from Voxel, Troop, Telugu.
[81.50 → 82.92] Pretty much all things telephony.
[82.92 → 85.02] He's a biz dev guy over there.
[85.02 → 87.92] He puts the development back in biz dev, I guess it is.
[88.64 → 92.98] And we talked about Photo, which is a jQuery-enabled, what is it?
[93.52 → 95.04] jQuery plug-in.
[95.30 → 101.28] It allows you to do telephony apps, basically, from the browser, kind of headless without having to have a server behind it.
[101.28 → 110.30] You know, Troop is your server, and, you know, you can create all the crank call scripts to your heart's content.
[110.94 → 116.38] So these front-end guys can now take jQuery and easily enable their websites to make phone calls.
[116.88 → 117.52] Can you believe it?
[117.56 → 118.94] You can order pizza right there from your browser.
[119.40 → 120.28] I can't wait to do it.
[121.24 → 122.82] What's this big announcement we've got?
[123.76 → 126.00] We are partnering with GitHub.
[126.00 → 131.66] We're going to help them promote the – not just if they need any help, really, but the job board.
[132.16 → 137.56] Got approached by Chris Wans troth to be their exclusive partner in promoting their jobs.
[137.72 → 140.32] So we'll be reading GitHub jobs on air.
[140.46 → 143.66] So if you go to GitHub.com forward slash jobs, you'll find some info there.
[144.18 → 149.00] Upon the sign-up process, you'll be able to check a little box that says promote my job on the changelog.
[149.00 → 157.52] So we'll read those jobs for $100, which is pretty inexpensive and a great gift for us, really, because the great GitHub guys have helped us out plenty, and we're grateful for them.
[158.00 → 159.46] You know, this is pretty much a labour of love.
[159.56 → 164.50] So if you want to keep the changelog on the air, this is a great way to support it.
[164.86 → 165.20] Absolutely.
[165.36 → 166.74] It helps us keep the lights on.
[166.94 → 175.76] I mean, it's not a huge amount of money, but it's good to keep the lights going and helps us travel and get out to the conferences we want to in the summer or throughout the year.
[175.76 → 183.14] So this is a perfect fit for us, and we're really thankful for Chris and the rest of the team at GitHub for giving us the opportunity to do it.
[183.28 → 183.72] It's awesome.
[183.92 → 185.78] Also thankful for the open source community.
[186.26 → 188.82] Without your projects, this whole podcast wouldn't be possible.
[189.38 → 195.82] So shout out to everybody that's contributed anything we've covered in the last year and keep the open source bits coming.
[196.52 → 199.20] Yeah, special thanks for everybody who sends those emails into ping.
[199.46 → 200.80] Ping at the changelog.com.
[200.84 → 204.12] We really appreciate the heads-up on some of those cool projects we hear about.
[204.12 → 208.70] So keep those coming, keep open source going, and we'll all keep doing what we do.
[209.00 → 209.90] Make a do-it-it-do, baby.
[211.48 → 212.28] Fun episode, man.
[212.30 → 212.86] You want to get to it?
[212.92 → 213.44] Let's do it.
[222.46 → 226.44] We're chatting today with Chris Matthew from Ruby ology and Voxel Labs.
[226.64 → 229.40] So Chris, why don't you introduce yourself and kind of your role over there?
[230.36 → 230.90] Hey, Wynn.
[231.10 → 233.70] Thanks, first, for having me on the show.
[234.12 → 238.30] So I'm the director of business development for Voxel Labs.
[239.00 → 241.58] And I was originally the founder of Telugu.
[241.84 → 244.86] So that's kind of how I came about this way.
[244.98 → 247.32] So Voxel Labs is part of Voxel.
[247.44 → 259.98] It's a 10-year-old company, very mature company, 150 engineers, offices in Orlando, Beijing, Germany, and folks all over the world.
[259.98 → 270.04] And the labs division is where all the advanced next-generation technology has taken place for Voxel.
[270.28 → 277.72] So Telugu, Troop, and now Photo are all products of Voxel Labs.
[277.72 → 284.22] And there's a few more in the pipe that we can't yet announce, but coming soon.
[284.34 → 288.46] Very exciting times in the life of telephony at the moment.
[289.18 → 293.32] So, yeah, we should mention Troop is a telephony company.
[293.46 → 294.62] It has a few products out there.
[294.62 → 298.98] So what's the state of open source telephony these days?
[299.92 → 302.56] Yeah, so we were talking earlier there.
[302.66 → 305.32] There's a lot of open source happening.
[305.42 → 308.42] I mean, Voxel prides itself on being open sourced.
[308.98 → 312.18] Just about everything we touch ends up being open sourced.
[312.44 → 314.66] So we mentioned Troop a minute ago.
[314.84 → 317.90] Troop is our cloud communications platform.
[317.90 → 324.90] It's almost two years old, and it's quite extensive in its delivery offering.
[325.86 → 336.32] It's a cloud communications platform that lets you build voice, telephone applications, SMS, instant messaging, and Twitter, all with a single API,
[336.64 → 345.90] which makes it really powerful from a communications perspective, being able to talk to customers on all four of those channels and interchange channels.
[345.90 → 353.38] So you could talk in the voice, drop a message on SMS, and then send them a tweet, all in one conversation.
[354.22 → 355.70] So that's pretty interesting.
[355.88 → 358.46] And that's open sourced on GitHub.
[358.58 → 364.64] If you go to GitHub.com slash troop, T-R-O-P-O, you'll find all the source code to that.
[366.72 → 368.56] Adhesion, we were talking about earlier.
[368.56 → 375.54] It's a Ruby library for building telephony applications using Asterisk.
[376.42 → 384.28] That's open sourced and being maintained, and Voxel is the official sponsor of that project now.
[384.50 → 386.46] So that's really cool.
[386.56 → 387.72] We can talk about that.
[387.94 → 397.64] And then Photo SDK, we just released a month ago at the jQuery conference, and we're getting a ton of buzz around that.
[397.64 → 402.16] In fact, a week or so ago, it was on Twitter's top tweets.
[402.60 → 406.82] So it's a telephone that runs in your web browser.
[406.96 → 418.44] It can place and receive phone calls and even do some XMPP-based I'm chat technology just by dropping jQuery,
[418.72 → 421.20] a few lines of jQuery script in your web browser.
[421.20 → 428.10] So that's pretty amazing, and that's also open sourced on GitHub as well, GitHub.com slash photo.
[428.28 → 429.44] Well, that's quite the lineup.
[429.60 → 430.58] Let's start with Adhesion.
[430.72 → 434.44] I remember seeing this, I guess, two or three years ago at Lone Star Rubicon.
[435.12 → 438.08] Jay was giving a demo of Adhesion.
[438.34 → 441.94] So this is a Ruby, I guess, framework more than just a library.
[442.04 → 442.74] It's a Ruby framework.
[442.98 → 445.08] Does it sit on top of Asterisk or relate it at all?
[445.08 → 451.08] Yeah, so it does sit on top of Asterisk, and Jay Phillips was the original author,
[451.54 → 458.66] and Jason Gecko over the years has gotten more in control of contributing and steering that product.
[459.54 → 462.70] And Jay is kind of taking a break.
[462.82 → 466.88] He's focusing full-time at Pivotal Labs on day-to-day stuff.
[466.88 → 471.96] And Jason is the VP of innovation.
[472.42 → 474.24] What a title for Voxel Labs.
[474.54 → 479.26] So he's actually my boss and still contributes to Adhesion.
[479.52 → 485.22] We have a guy by the name of Ben Clang who's actively involved on building
[485.22 → 490.74] and working through pull requests on features being added to Adhesion.
[490.74 → 500.40] And what I find really cool, just to show you just how techy, geeky all of these folks are,
[500.54 → 507.16] Jason being a VP at Voxel Labs, on the flight going to Lone Star Rubicon,
[507.48 → 512.42] he wrote a project that he calls Agitate.
[512.92 → 518.20] And what Agitate does is kind of a play on the Asterisk AGI protocol.
[518.20 → 526.56] Anything that runs on AGI, which Adhesion does, you can point that seamlessly at Troop.
[527.04 → 531.20] So for Ruby developers that are building on the Adhesion framework,
[531.84 → 540.36] instead of having to stand up your own asterisk boxes and manage scalability that way,
[540.76 → 544.26] you could easily just take your existing Adhesion app that you wrote
[544.26 → 550.66] and then redirect it to Troop and then let us scale it for you to millions and millions of calls,
[550.78 → 553.80] whatever you need to accommodate your Ruby app.
[554.46 → 557.56] So Adhesion, I guess, is pretty much the stand-up, run it yourself,
[557.68 → 560.42] and then there are other offerings in the cloud such as Troop?
[561.10 → 561.50] Exactly.
[561.70 → 565.54] So Troop makes it very easy to scale applications.
[565.54 → 573.26] Because the thing about Troop is it actually sits on Voxel's network, global voice network,
[573.40 → 577.86] which is, you know, if you look at things like Amazon EC2 and those types of cloud,
[577.98 → 581.84] you know what we web developers call cloud technology or cloud platforms,
[582.38 → 587.58] they're all optimized for really web traffic, not necessarily for voice.
[587.58 → 593.78] So in the voice world, you know, the whole concept of Los, quality of service,
[594.50 → 603.76] is very particular when it comes to managing packets of voice so that they get synced in the same order,
[603.96 → 613.86] that there's very low or no jitter, you know, of packets arriving in different formats
[613.86 → 618.00] or being assembled in the correct order.
[619.10 → 624.70] So Voxel has seven data centres around the globe that are very focused on voice traffic,
[625.20 → 626.94] delivering voice traffic and uptime.
[627.66 → 635.84] So Voxel's, like, evolution platform, it's, you know, 100% uptime guarantee SLA network.
[636.36 → 643.60] While Troop, we've discounted the price significantly of, like, what an enterprise customer,
[643.86 → 649.00] typically pays for that service, but we don't offer the SLA that goes along with it.
[649.06 → 651.94] But at the same time, we're riding on that same network,
[651.94 → 655.74] which makes it pretty cool to be able to, you know,
[656.04 → 661.82] elastically scale to whatever number of, you know, ports or, you know, volume is required
[661.82 → 664.16] to meet our customers' needs.
[664.32 → 667.92] So Troop has that luxury, if you will, of having, you know,
[667.92 → 672.00] one of the largest voice networks in the world at our disposal.
[672.00 → 675.04] Let's take a step back and give a little background here.
[675.10 → 680.18] I think the first time that I heard the term telephony was with the telephony API
[680.18 → 681.88] in Visual Basic way back in the day.
[681.94 → 686.40] You could drag the control to your form and now control your modem to make outbound calls,
[686.54 → 689.84] which back in the late 90s seemed like the coolest thing.
[691.10 → 695.74] What sorts of applications can you write with these types of APIs
[695.74 → 697.96] and what types of services can you perform?
[697.96 → 702.06] Wow. Hey, yeah, we've come a long way since, I think, the TAPI.
[702.14 → 704.40] I think that's what they call it. It's like the telephony API.
[704.50 → 705.34] Right, TAPI.
[705.52 → 708.26] It was TAPI and MAPI, the messaging API, right?
[708.52 → 710.94] Yeah, and then SAP was their speech API.
[711.32 → 712.28] Right, I forgot about that one.
[713.16 → 714.44] Yeah, we've come a long way.
[714.72 → 718.54] So really with Troop and to some degree Adhesion,
[719.10 → 722.74] Adhesion really focuses on just the voice side of calls,
[722.74 → 726.36] where Troop you can do lots of other things like SMS, et cetera.
[728.20 → 732.06] Any of the applications you call like banking applications,
[732.88 → 737.46] where you give it your account number, and it can tell you balance,
[737.54 → 739.32] you can move money from one to another,
[739.90 → 742.72] those are just typical what we just call IRS,
[742.74 → 744.44] Interactive Voice Response Systems.
[744.88 → 748.38] Those are kind of like old school what you can do.
[748.38 → 753.92] You know, even until just recently, a lot of websites still,
[754.16 → 757.02] a lot of them still have what they call click-to-call.
[757.26 → 759.94] Like, you know, if you want to talk to a customer service agent,
[760.04 → 761.96] you're on a website, you can enter your phone number,
[762.20 → 768.16] and then what happens is the voice platform calls your phone number,
[768.26 → 770.96] then it calls the agent, and then it bridges the calls together.
[771.62 → 773.78] That's a common click-to-call scenario.
[773.78 → 779.14] But with Photo, with the phone in a browser that we just recently released,
[780.28 → 783.86] when you hit the button to click-to-call, it's a phone in your browser,
[784.00 → 787.46] so it automatically just is your phone, doesn't have to call you,
[787.54 → 791.76] doesn't have to ask for your number, and it dials the agent with one step.
[792.32 → 797.18] So that's an example of advances that just happened a month ago
[797.18 → 801.70] in the telephony industry, and there are all sorts of, like,
[802.62 → 806.40] features or functionality that typically come with telephony,
[806.72 → 810.36] things like speech recognition that we've been doing for a very long time
[810.36 → 815.86] where you can define grammars, words to listen for, phrases to listen for,
[816.18 → 821.00] and that allows the customer to not only talk, you know,
[821.02 → 823.44] with their voice control the application,
[823.44 → 828.52] but, you know, they could always drop back down to touch tone if they wanted to.
[828.94 → 833.58] And things like transcription, so if you're building something where you want,
[833.72 → 836.96] you know, like Google Voice, where you want it transcribed, the voicemail,
[837.06 → 840.26] and sent to you, we have transcription services.
[840.26 → 849.68] And, you know, the ability to call many, many phone numbers at one time
[849.68 → 856.18] or receive many, many phone calls at one time is just a world of difference in the cloud world
[856.18 → 860.38] because in the old days, you know, like a couple of years ago or a year ago,
[860.60 → 865.56] when a company wanted to actually deploy an interactive voice response system,
[865.56 → 870.72] they would have to do all the math to say, okay, the busiest I think I'll ever be
[870.72 → 872.84] is a thousand simultaneous calls.
[873.02 → 878.74] So then they would go off and buy like a thousand ports of hardware, deploy it,
[878.88 → 882.16] you know, maybe they'd buy 2,000 ports because they needed high availability,
[882.38 → 887.42] deploy it at multiple sites to design something that could withstand that volume.
[887.74 → 890.92] And then on a typical day, they might only have 300 calls.
[890.92 → 896.82] So look at that wasted hardware and investment of just a port sitting idle.
[897.08 → 901.64] And in today's world with Troop, I mean, it's all elastic.
[901.82 → 904.98] So whether you're dealing with one call at a time or you get tech crunched
[904.98 → 907.78] or Oprah mentions your product, you know,
[908.34 → 913.04] now you can handle millions of calls without doing anything differently.
[914.00 → 915.48] We've come a long way since Happy.
[916.62 → 919.34] It seems like the standard today, I guess, is the SIP protocol.
[919.34 → 921.28] SIP, absolutely.
[921.56 → 926.70] So, I mean, everything we do with all of Voxel's products is open standard.
[926.92 → 929.62] So that's why we're big on open sourcing.
[929.74 → 932.26] We want to give back to the community, contribute.
[933.08 → 935.80] Everything we do supports SIP.
[936.40 → 939.64] And SIP stands for Session Initiation Protocol.
[940.30 → 944.14] And it's basically used interchangeably with voice over IP.
[944.14 → 948.92] It's the open standard of communicating with voice over IP.
[949.30 → 957.88] So with Troop, when you create an application, we give you a SIP address that can ring right into your application.
[958.30 → 962.34] We give you as many phone numbers as you want, toll-free or local.
[962.52 → 967.26] Or we have phone numbers in 41 countries we can give you at that point of your application.
[967.26 → 972.04] We also give you a Skype address that you can call with Skype for free into your application.
[972.98 → 977.62] And an INM number as well, which is bigger in Europe.
[978.80 → 986.60] And the cool thing about SIP is that everything with SIP, since it's open, all telephony carriers typically talk SIP.
[986.60 → 993.08] So it's easy to chain one app to another app to another app so that you can create like a best-of-breed solution.
[993.30 → 1002.74] So like if you like this one voicemail system, you could transfer your call from Troop to a different platform running SIP and vice versa.
[1003.46 → 1011.68] And what's interesting is with Photo, we're seeing lots of – we first were looking at this.
[1011.68 → 1021.38] I mean we just wanted to build the solution to let developers put phones in their web browser without really thinking or knowing what they would actually end up building.
[1022.16 → 1033.94] And while we were kind of thinking it was going to be click-to-call where a consumer calls a call centre, we're seeing interesting use cases where Fortune 500 companies now are building Troop apps.
[1033.94 → 1046.24] And then what they're doing is when you say you want to talk to an agent, they can actually route that call to another country over SIP and then ring the call in the agent's web browser using Photo.
[1046.82 → 1054.74] And they're bypassing all the long-distance tolls for sending a call to another country.
[1056.90 → 1057.90] Quite powerful.
[1057.90 → 1064.34] Yeah, and with Photo, I mean it's in the web browser so they have like a little screen pop that tells them information about the call.
[1064.84 → 1068.74] And then the phone being in their browser just transfers the call to their headset.
[1069.54 → 1077.16] I mean that is like next-generation call centre technology, you know, quite a long ways from Happy.
[1077.84 → 1079.50] So we're talking over Skype right now.
[1079.58 → 1082.40] I know we're recording locally so we can piece this together.
[1082.60 → 1086.72] But the quality is actually better than a phone call.
[1086.72 → 1090.64] What's the quality like on these SIP calls?
[1091.10 → 1096.24] Yeah, so Skype, they've got several advantages over a lot of other solutions.
[1096.92 → 1101.74] What we're talking with now is what a lot of people consider wideband.
[1102.26 → 1108.14] So it's able to use more of the frequency range than a typical like analog call.
[1108.70 → 1113.64] So that's why you're able to get like a high-def sounding audio stream.
[1113.64 → 1119.22] And the other interesting thing about Skype is that it installs locally.
[1119.70 → 1124.72] And they've got more controls or hooks into the operating system that it's installed on.
[1124.84 → 1129.54] So they can cancel echo more effectively, the echo cancellation.
[1129.54 → 1140.70] And they can also oftentimes control the codec that's used for, you know, wideband versus narrowband on the voice call.
[1140.82 → 1152.32] So that if you're on a DSL versus a cable modem, they can kind of change how they – the bandwidth, if you will, of that conversation.
[1152.32 → 1157.24] So there are a lot of advantages to being a locally installed application.
[1157.78 → 1159.00] There are disadvantages too.
[1159.26 → 1164.94] I mean Skype's got it, you know, in a good position because, you know, millions of customers already have it installed.
[1164.94 → 1178.42] When we set out to build Photo, our goal was to create a browser-based telephone that could receive and place calls without any downloads.
[1179.14 → 1186.36] So the goal was a headless application that with a click of a button, it's, you know, 95% of it's jQuery controlled.
[1186.36 → 1197.36] So you can listen to events, you can control the telephone, like touch tones, mute, hang up, all the controls of a telephone with jQuery commands.
[1197.98 → 1202.96] And the beauty is that there's no download, it's immediate, and you're online.
[1203.94 → 1213.28] The downside to that is you have to work extra hard to control echo and latency and all the things that go along with HTTP.
[1214.62 → 1215.64] That's the challenge.
[1216.36 → 1222.00] So let's talk about that, the Photo plug-in under the hood, the jQuery aspect of it.
[1222.10 → 1228.18] So are you dropping a Flash movie, I guess, or a Flash SWF file?
[1228.64 → 1230.72] Is that how you're pulling off the audio capture?
[1231.30 → 1231.56] Yep.
[1231.74 → 1240.80] So until HTML5 supports audio or mic and camera controls, which it will next year.
[1240.88 → 1243.82] I mean we have a guy on the W3C board working through that.
[1243.94 → 1244.84] Google's on the board.
[1244.84 → 1246.92] Everyone wants to see this happen.
[1247.20 → 1251.74] So until it happens, we really only had two options.
[1252.34 → 1256.14] We have Flash, and we have Java, like Java Media Framework.
[1256.14 → 1267.96] So when I talked about 95% of the app being jQuery, the other 5% is the Flash control that you have to give permission to control the microphone.
[1267.96 → 1280.92] What happens under the covers is we also have an RTP stack that handles the media inside of Flash.
[1280.92 → 1287.68] And it uses a protocol called Jingle instead of SIP.
[1288.18 → 1291.44] And the reason it uses Google Voice, by the way, uses Jingle also.
[1291.44 → 1296.40] So it's also an open standard, kind of goes hand-in-hand with like XMPP.
[1297.50 → 1307.00] And what Jingle does, it's a lighter weight protocol that can transport over HTTP audio.
[1307.00 → 1324.80] But what we do is we have these photo gateway servers that sit on the edge of our network that all their job is translating Jingle to SIP and SIP back to Jingle.
[1324.80 → 1335.68] So what happens is when you drop that photo object into your browser, and it loads, you actually get a SIP-looking address.
[1335.88 → 1342.38] So it's SIP colon, you know, this big long address like a typical SIP phone, soft phone SIP number.
[1342.94 → 1345.46] In reality, it's a DID.
[1345.56 → 1347.84] It's a Jabber ID, which is Jingle.
[1347.84 → 1355.74] So it looks like a SIP address, and when it talks to our gateway servers, that's where the translation happens from Jingle to SIP.
[1355.96 → 1364.16] So when you load – when your browser fires up, it dynamically gets a DID that looks like a SIP address.
[1364.46 → 1366.34] That is a real SIP address.
[1366.46 → 1372.84] I mean you can receive phone calls that second from any soft phone in the world in your browser, and it rings.
[1372.84 → 1382.08] So now that Google has introduced Google Talk directly into Gmail, has voice over IP finally arrived to the mainstream?
[1382.84 → 1383.88] I think so.
[1384.02 → 1386.06] I think it's getting more and more popular.
[1386.98 → 1394.30] And I know we've seen a lot of excitement around people, what they're doing with photo and connecting it to Troop.
[1394.30 → 1407.52] And interesting thing about Google Voice is a long time ago we all forgot about this, but I think when they launched Google Voice, there was also a native plug-in that we all kind of downloaded.
[1408.66 → 1420.02] And in their talk, their new like Talk voice client, it leverages that native plug-in to also reduce echo.
[1420.02 → 1429.10] So, I mean, it's a pretty good sounding effect, but you as a web developer, you can't really do anything with it.
[1429.42 → 1437.74] Whereas with photo, it's entirely spinnable with CSS, and you can control what it looks like, and the source code's up on GitHub.
[1438.50 → 1441.30] So you can extend it and send us pull requests.
[1442.12 → 1447.60] So hopefully what we've done is we've created a platform that's totally free, by the way.
[1447.60 → 1455.48] I mean, if you want to do browser-browser calls and use it in your application, even sell your application, it's 100% free to do so.
[1455.56 → 1457.84] It's licensed under the Apache 2 license.
[1458.74 → 1461.74] So, you know, be our guest to do whatever you want with it.
[1461.80 → 1467.24] But, you know, if you're going to extend it, we'd love to get some pull requests to build a community around it.
[1467.24 → 1479.50] But what we think that's doing is it's really empowering web developers to make it easier to get into the telephony space to start building fascinating apps.
[1479.66 → 1481.54] And I'll give you an example of something.
[1482.02 → 1489.06] When we launched at jQuery conference, we didn't even hardly get to see the rest of the conference.
[1489.06 → 1497.04] We had people in the audience hacking on it, and we had to, like, kind of regroup, and we were doing support for everyone hacking.
[1497.88 → 1503.62] And one guy built a really – another interesting use case that we never thought of.
[1504.56 → 1511.02] So what he did was he put, like, this talk button on a web page.
[1511.02 → 1517.44] And the web page had, like, forms – like, like, yeah, like web forms on it.
[1518.10 → 1527.72] And he used our speech recognition and text-to-speech to basically have a dialogue with someone sitting in front of the web browser.
[1527.72 → 1541.50] And based on their dialogue, he was transcribing what they said in certain instances and pre-popping or filling in forms for them on the screen.
[1542.14 → 1547.32] And it kind of really got me thinking that this is so much bigger than a telephone app.
[1547.32 → 1561.30] It almost blurred the lines in my mind of what you would think of a telephony application because what this was is it was almost like a two-way browser conversation with this intelligent bot, if you will.
[1561.36 → 1566.46] And it was controlling the browser for you and even typing for you in the form.
[1566.64 → 1574.76] So I was like, wow, that's a pretty interesting paradigm of what – a tangent of where this stuff could be going.
[1574.76 → 1577.64] You know, transcription is an exciting technology.
[1577.92 → 1580.40] Sometimes things get lost in transcription.
[1580.54 → 1584.12] Have you seen GVWTF, the Google Voice WTF site?
[1584.70 → 1585.22] Yeah, yeah.
[1585.68 → 1588.90] So there's some funny transcription errors on there.
[1589.02 → 1590.54] You know, and I get those occasionally too.
[1590.60 → 1592.12] I'm a Google Voice user.
[1592.30 → 1596.54] So you get the – it's probably 80% or 90% accuracy.
[1596.92 → 1601.18] How does it stack up on your end compared to what we get from Google?
[1601.72 → 1603.84] You know, I think that ours is better.
[1603.84 → 1610.04] And I need to say just right up front that we didn't write our transcription technology.
[1610.24 → 1616.84] We partnered with a company that's been in business doing transcription for probably about 10 years, maybe eight.
[1617.40 → 1620.22] And it's perfect, believe it or not.
[1620.30 → 1625.66] I mean when it's totally automated, you can also opt in for higher quality transcriptions.
[1625.76 → 1631.14] But the automated ones I find to be even much better than Google, which is interesting.
[1631.14 → 1632.28] I think Google should buy them.
[1634.12 → 1649.44] So, you know, it's interesting to see where all this technology is going because, you know, even Google kind of wonder what they're up to because, you know, they had the Goog411 service where they recently cancelled that service like just a couple of weeks ago.
[1649.44 → 1666.94] And a lot of people suspected that they were actually using all of us to test some speech recognition technology that they were putting together, you know, where we were using it as a free service but really helping them test their speech recognition.
[1667.30 → 1669.60] So who knows what they're up to?
[1669.90 → 1671.50] Unwitting beta testers as it were, huh?
[1671.76 → 1672.26] Exactly.
[1672.26 → 1677.32] So what's the difference, I guess, the main difference between Troop and Twilio?
[1678.10 → 1681.28] Well, Troop is, you know, really powerful.
[1681.66 → 1693.26] When you look at things like our ability to do instant messaging in Twitter and even SMS under the same API, Twilio has got a different API for SMS versus voice.
[1693.26 → 1698.98] Ours is all a single API, which is powerful because you build your application once.
[1699.68 → 1706.60] And no matter if someone calls that phone number of texts that number, you know, it creates the dialogue with the user.
[1706.74 → 1709.78] So that's really powerful from an application developer perspective.
[1710.88 → 1712.48] We also do speech recognition.
[1712.48 → 1720.28] We do it in nine different languages.
[1721.90 → 1729.14] And even with our text-to-speech, very elegant-sounding text-to-speech, very robust, it too is in nine different languages.
[1730.08 → 1734.94] And it supports male and female voices that are controllable in all nine languages.
[1734.94 → 1741.50] You know, we also have phone numbers, you know, like I mentioned, in 41 countries around the world.
[1741.50 → 1748.20] We've got SMS that we can do internationally, which Twilio doesn't do international SMS.
[1749.38 → 1752.54] And, oh, let's see.
[1754.24 → 1757.80] I think there are just lots of little subtle differences besides scale.
[1757.80 → 1764.74] I think that's the biggest one is what we see when they do outbound like dial campaigns.
[1764.96 → 1771.24] They typically throttle it at like a call a second where we can do, you know, millions of calls at one time.
[1771.36 → 1777.66] We have emergency notification systems that rely on our platform of services.
[1777.92 → 1785.04] So, like, if something ever happens at a school, you know, God forbid, no one would ever want something like that to happen.
[1785.04 → 1787.90] But when something does, that's a pretty serious situation.
[1788.84 → 1800.06] And some of our customers, I mean, they send out tens if not hundreds of thousands of simultaneous calls across Troop to get that message out in a state of emergency.
[1800.34 → 1806.54] You know, that's a very real scenario now with things that happened at Virginia Tech, I guess, a couple of years ago.
[1807.02 → 1807.14] Yep.
[1807.14 → 1815.56] And now when there's an emergency, there's really only a couple of technologies that you can get the word out in that kind of scale, and who checks their email every two minutes, you know?
[1816.02 → 1816.24] Yep.
[1816.38 → 1819.10] And, you know, I was talking to Bill Schreiber, the CTO of Seattle.
[1819.10 → 1824.80] And, I mean, that was what he was just excited about is that Troop is pay-as-you-go.
[1824.98 → 1826.20] So there are no contracts.
[1826.30 → 1828.38] There's no monthly or minimum commitments.
[1829.00 → 1832.06] In fact, if you're a developer, we give you total free access.
[1832.06 → 1835.50] We even give you phone numbers and don't even charge you for minutes or messages.
[1836.54 → 1842.66] So we've got 200,000 developers in the whole Voxel development community.
[1843.48 → 1851.28] So across all of, you know, 10 years' worth of Voxel developers in the community plus Troop, 200,000 developers.
[1851.28 → 1873.34] And Bill Schreiber at Seattle was thinking, wow, what an opportunity to create a citywide or Washington in general or even national emergency response system on the Troop platform because you don't pay anything for it in the good times.
[1874.04 → 1879.32] And in times of disaster, it just spins right up, you know, to whatever you need it to do.
[1879.32 → 1883.42] So it's a great use case for that type of communication.
[1884.14 → 1892.82] Are most of the applications that you're seeing being built, are they stand alone telephony applications or is telephony just an aspect to an overall web application?
[1893.72 → 1894.92] Well, that's a good question.
[1894.92 → 1905.70] I see a lot of, like, complementary apps that complement existing websites where they'll just put a voice aspect or an SMS aspect into it.
[1906.00 → 1914.46] But on the other hand, I do see ground-up telephony applications where that's all they do.
[1914.46 → 1923.76] They don't do any web screens, web pages, et cetera, while they're written in a web language that supports HTTP.
[1926.00 → 1931.44] I've seen a lot of them that even Fortune 500 companies are building purely telephony applications.
[1931.44 → 1941.74] And I should point out one more interesting difference with Twilio is that we have, you know, we both have a web API, RESTful web API that's really simple.
[1941.74 → 1948.74] Where we also, where we really shine is we have what I consider next-generation APIs.
[1949.76 → 1951.74] It's what we call a scripting API.
[1951.74 → 1965.30] And like Google App Engine, where you can write applications like in Python or Ruby and push them to the Google Cloud where they actually run on Google's platform,
[1965.90 → 1970.82] you can do the same with your telephony applications using our scripting API.
[1971.12 → 1973.64] So we support five languages.
[1973.64 → 1975.48] You write in Ruby as one of them.
[1975.60 → 1980.64] Ruby, Python, PHP, Groovy, and JavaScript.
[1980.64 → 1983.98] You write an application in any of those five languages.
[1984.34 → 1986.84] You push it to our cloud.
[1987.16 → 1991.90] And it's basically on the metal of our voice cloud.
[1992.12 → 1994.62] So there's, you know, zero latency.
[1995.00 → 1998.92] You know, all the back and forth that typically go with API like AJAX requests.
[1999.24 → 2000.58] All of that's eliminated.
[2000.96 → 2008.96] And your script runs in our voice cloud along with all of our SIP ports.
[2008.96 → 2012.82] You know, and our SIP ports are just crazy density.
[2012.98 → 2016.14] I mean, you know, 20,000 ports on a single server.
[2016.76 → 2018.72] You know, multiply that times seven data centres.
[2018.92 → 2027.42] You know, I mean, it's fascinating what you can do with like a scripting API that's that responsive that you don't have to pay to host it anywhere.
[2027.42 → 2031.38] It's free to host it on the Troop cloud.
[2031.76 → 2037.70] And it's just there waiting for, you know, an emergency situation or your app as you need it.
[2037.90 → 2040.12] You know, I hadn't realized how many languages were supported here.
[2040.22 → 2046.32] This is the scripting API environment is incredibly powerful yet incredibly dangerous, I think.
[2046.88 → 2047.24] Yeah.
[2047.24 → 2051.48] Dangerous in the hands of a 12-year-old that wants to do prank calls.
[2051.62 → 2053.86] This is like a prankster's dream.
[2054.60 → 2055.40] Exactly, man.
[2055.82 → 2058.94] Or imagine like the political, you know, we just had the election.
[2059.26 → 2064.16] You know, and I don't know if you were like me, and you got hundreds of calls from political advisors.
[2064.16 → 2066.84] I mean, this would be, you know, Obama's dream.
[2067.00 → 2079.50] You know, whoever's running for President of the United States, you know, to be able to push that type of volume and even automate it is totally at the hands of a couple of lines of code.
[2080.06 → 2082.04] Mail merge to Troop Export.
[2082.62 → 2082.86] Yeah.
[2083.84 → 2084.70] Basically it.
[2085.48 → 2086.96] So I know you're a Rubbish.
[2087.70 → 2089.04] You run Ruby ology.
[2089.54 → 2090.00] Absolutely.
[2090.00 → 2097.20] I've been doing Rails for about four years and I, you know, we joke about, you know, being Microsoft free for four years.
[2099.04 → 2100.84] I love Ruby.
[2100.98 → 2101.78] I know you do too.
[2102.10 → 2103.18] Yeah, Ruby's one of my favourites.
[2103.96 → 2105.34] Do you like me some JavaScript?
[2105.88 → 2110.04] You also support on the scripting environment PHP and Python.
[2110.24 → 2111.68] I know those are extremely popular.
[2112.80 → 2112.96] Yep.
[2113.00 → 2117.06] And, you know, with Node.js, I think, you know, JavaScript's, you know, cool again.
[2117.06 → 2123.50] You know, jQuery and Node.js, I mean, a lot of people are, you know, building Node libraries, running them on Troop.
[2123.76 → 2129.18] And it's getting a lot of, you know, it's coming full circle again, like they say with fashion.
[2129.54 → 2129.88] Right.
[2130.06 → 2130.86] Everything's cyclical.
[2131.54 → 2133.64] Hang around long enough, it's going to make another pass.
[2134.08 → 2138.70] So what's the difference between the Troop scripting environment and the Troop web API?
[2138.70 → 2141.32] So not much.
[2141.42 → 2145.20] I mean, the API itself is pretty typical.
[2145.58 → 2149.34] So it's just how you interact with the method calls.
[2149.56 → 2157.94] So you don't have all the back and forth JSON that necessarily everything's more self-contained in the scripting.
[2157.94 → 2159.34] I can tell you one thing.
[2159.42 → 2168.96] A lot of people maybe don't – you have to kind of put your head around, you know, the scripting API differently than you would a typical RESTful API.
[2169.74 → 2173.00] Because when everything's – and it's just like Google App Engine.
[2173.08 → 2184.08] When everything's running on someone else's cloud, kind of in their – on their platform, in their environment, you lose certain things like, you know, being able to write to a local database.
[2184.08 → 2189.96] Or, you know, what a developer might be accustomed to having at his disposal, his or her disposal.
[2190.32 → 2192.04] And you have to look at things a little differently.
[2192.24 → 2207.36] So like in the scripting environment, if you need to do data IOS, if you simply write a web service going back to your application that can look up data for you or write data when you need to write it,
[2207.36 → 2215.00] you can call web services from the scripting API externally.
[2215.32 → 2222.48] So that makes it really powerful where you can – you know, when a phone rings, you can come to your web service and look up like, you know,
[2222.50 → 2228.14] based on the caller ID or the number they dialled, you know, or what information you want to do about the call.
[2228.30 → 2231.66] And then proceed with handling it the way you want to handle it.
[2232.22 → 2236.46] So it's just a little bit differently, you know, you need to look at how you want to do things.
[2236.46 → 2238.64] And we're always looking at ways to improve that.
[2238.64 → 2248.94] So we're kind of playing around with adding like a fetch method to our API that make it, you know, even easier to get data or push data.
[2249.20 → 2251.12] But extremely powerful.
[2251.28 → 2254.20] I mean, that's – I write a lot of telephony apps in Ruby.
[2254.80 → 2260.34] And probably 90% of them now I'm entirely writing in the scripting API.
[2261.22 → 2262.02] So you're a podcaster.
[2262.74 → 2263.76] Yeah, that's right.
[2263.76 → 2269.44] Here's what I want as a podcaster, and you tell me how many years I'm going to have to wait on this.
[2269.54 → 2275.12] So I would like to be able to have all the guests dial in over cheap telephony, right?
[2276.04 → 2280.86] Record multichannel so that we can duck out audio when someone sneezes or chair creaks or something like that.
[2281.46 → 2285.62] Get the same audio quality that I would get if I'm recording locally.
[2285.62 → 2292.74] And not have to install any plug-ins to get it and not have to hassle the guests with any downloads.
[2294.34 → 2296.36] Well, you're pretty much there today.
[2296.66 → 2304.52] So like with Troop, it's probably a five to ten line application that can do all of it but one.
[2304.52 → 2306.04] I'm kind of thinking off the top of my head.
[2307.72 → 2313.84] You can create an application that just doesn't answer when you call it.
[2314.34 → 2320.70] If you use Skype or SIP to call it, you're going to get that wideband, high-quality, high-def audio sound.
[2320.70 → 2326.78] After you answer the call, you drop everyone into a conference.
[2328.30 → 2338.18] And you also – there's a record, start recording method that you can record individual calls or the conference itself.
[2339.32 → 2347.70] And then you can also – after it's done, you can submit the recorded file, which is already an MP3, which you can use for your downloading.
[2347.70 → 2352.26] And then you can submit it also to our transcribing API.
[2353.10 → 2361.60] And asynchronously, when it's done, it will place a callback to the URL you provide with all the dialogue of the transcription.
[2363.58 → 2367.64] So basically with less than ten lines of code, you could do all of that.
[2367.74 → 2377.54] The only thing off the top of my head is I think the way it's designed now, you typically just get the recording of the whole conference, not the channel-by-channel.
[2378.18 → 2386.98] But I think you could probably still – I think if you record at the phone level before you put it in conference, you might be able to do that.
[2387.26 → 2388.22] We'd have to play with it.
[2388.94 → 2389.30] Definitely.
[2389.48 → 2393.66] Give me something to hack on when I watch the Saints beat the Cowboys this Thursday, Thanksgiving.
[2395.30 → 2396.56] I'm a Saints fan too.
[2396.78 → 2397.32] Oh, are you?
[2397.62 → 2397.96] Yeah.
[2398.56 → 2399.16] Good deal.
[2401.16 → 2401.66] Go ahead.
[2401.66 → 2401.94] Yeah.
[2402.06 → 2410.48] So I was just going to say, less than ten lines of code, now web developers can basically build applications like that they see fit.
[2410.60 → 2414.14] And especially in a development environment, it's totally free.
[2414.48 → 2415.78] I'd say hack at it.
[2415.88 → 2416.34] Hack on.
[2416.78 → 2417.80] I'll definitely have to do that.
[2417.80 → 2424.86] So this is the part of the show where we're kind of turning it upside down and talk to the guests about what's got them excited about open source.
[2425.02 → 2431.42] So in the world of telephony or really anything out there, what's got you excited in open source that you just can't wait to bang on?
[2431.42 → 2436.54] Well, you know, I've been eating my own dog food.
[2436.54 → 2448.26] So I've been looking for consumer apps, like examples that can use Photo in what we deliver.
[2449.12 → 2454.02] And so in a couple of days, I built what's called Facebook Telephone.
[2454.02 → 2463.56] And we call it that because we unbelievably, luckily, I guess, were able to get the application name from Facebook Telephone.
[2464.00 → 2468.12] So it's literally apps.facebook.com slash telephone.
[2468.54 → 2478.96] And it's a browser to telephone number application where you can call your friends on Facebook using Photo.
[2479.70 → 2481.08] And that's all open sourced.
[2481.28 → 2482.96] It's kind of an example app.
[2482.96 → 2486.76] It's up on GitHub.com slash photo slash Facebook Telephone.
[2487.80 → 2497.44] And what's funny about that is I just submitted it to Facebook, and they approved it the next day for their gallery.
[2498.68 → 2506.12] And it already has over a couple of thousand registered users.
[2506.60 → 2510.22] And we never did any promotion about it.
[2510.22 → 2515.78] It's very similar to another project I know you have called Mellophone that does this with Twitter.
[2516.02 → 2521.18] So what's your feedback, I guess, in doing the Facebook APIs and the Twitter APIs?
[2521.74 → 2524.90] Well, you know, I've been doing Twitter APIs for a long time.
[2525.02 → 2529.92] I mean, with like Michael Blasé, you know, OAuth.
[2529.98 → 2530.96] From Patricia, right?
[2530.96 → 2531.32] Yeah.
[2531.56 → 2535.40] I mean, he makes things just so simple to do with Twitter.
[2536.50 → 2538.72] I've been playing a lot with Twitter apps.
[2539.66 → 2542.46] Mellophone I wrote like in about a day.
[2543.48 → 2545.94] And, yeah, I mean, it just does no auth.
[2546.02 → 2549.56] It lets you do browser-browser calls with your friends on Twitter.
[2549.56 → 2561.54] And if you enter your phone number in there when you set up your account, if you don't answer on your browser, it does elevate and place a call to your mobile device for free or your home phone or whatever you have.
[2561.74 → 2567.50] And Facebook, you know, that was my first time really playing with the Open Graph API.
[2567.50 → 2572.90] So, man, much, much better improvement over what they used to have.
[2573.56 → 2585.04] So that one took two days to build just to kind of get my head around the way they did OAuth 2, which was a little different and kind of quirky even on how they respond.
[2585.70 → 2589.78] And open source Mellophone up on GitHub also.
[2590.08 → 2594.24] So, I mean, I really enjoyed the Facebook one because it was a little bit more of a challenge.
[2594.24 → 2598.08] And the interesting factor, I think, is the viral factor.
[2598.24 → 2603.62] Facebook seems to be more viral in the way it spreads than what we've seen with Mellophone.
[2604.66 → 2611.38] Yeah, and maybe there's a more natural fit there on Facebook where people are connecting and messaging more than Twitter.
[2611.50 → 2612.98] It seems to be more of a broadcast medium.
[2613.08 → 2614.94] I know that's how I use each of those.
[2615.64 → 2616.64] Mm-hmm. Exactly.
[2617.22 → 2618.44] Well, thanks, Chris, for joining us.
[2618.52 → 2620.80] Definitely putting the development in business development.
[2623.70 → 2624.10] Cool.
[2624.42 → 2626.00] You know, Won, I really appreciate it.
[2626.00 → 2630.58] I love what you guys are doing on the change log, and I'm honoured to be on your show.
[2630.72 → 2635.10] So thank you so much, and, you know, thanks for helping us get the word out about our products.
[2635.26 → 2637.32] And, you know, we love the Ruby community.
[2637.50 → 2639.64] We love really all the development communities.
[2639.64 → 2649.12] I think that speaks for all the various languages we support on scripting as well as the web APIs of our solutions and the open source we contribute on GitHub.
[2649.12 → 2664.20] So we'd love to hear what people are working on, especially if it involves anything telephony related, you know, especially a troop or photo application or telecom for that matter.
[2664.20 → 2667.44] So thank you very much, Won.
[2667.44 → 2670.62] We really appreciate your help in getting our word out.
[2670.62 → 2671.06] Definitely.
[2671.14 → 2672.56] We'll be sure and put all this in the show notes.
[2673.06 → 2673.28] Cool.
[2673.58 → 2674.06] Thank you.
[2674.06 → 2675.20] You know, again, I'm one of the most people that are there for us.
[2675.22 → 2687.54] For you, I'll see you.
[2687.54 → 2692.42] I can see you and my eyes.
[2693.00 → 2695.88] So how could I forget where
[2695.88 → 2701.82] I found myself for the first time
[2701.82 → 2705.52] Safe in your arms
[2705.52 → 2708.74] As a dark passion shot
