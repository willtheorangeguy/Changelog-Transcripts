[0.00 --> 6.94]  What's up, friends?
[7.02 --> 8.20]  This is the Change Law.
[8.26 --> 13.02]  We feature the hackers, the leaders, and the innovators who are moving us closer to the
[13.02 --> 13.74]  future of software.
[14.26 --> 19.20]  Today's show is a rebroadcast of a very special episode of Founders Talk.
[19.20 --> 21.82]  You can check out Founders Talk at founderstalk.fm.
[22.14 --> 27.16]  I was invited by our friends at Square to host a fireside chat with Jack Dorsey as the
[27.16 --> 30.60]  feature finale of their annual developer conference called Square Unboxed.
[31.04 --> 33.36]  Jack is one of the most prolific CEOs out there.
[33.66 --> 38.00]  He's a hacker turned CEO at that, and he's often working at the very edge of what's to
[38.00 --> 38.30]  come.
[38.64 --> 40.74]  He is focused on what the future has to offer.
[41.04 --> 45.82]  He's considered an innovator by many, and he's also a Bitcoin maximalist, and he's positioned
[45.82 --> 48.12]  himself and block long on Bitcoin.
[48.62 --> 51.84]  Big thanks to our friends and our partners at Fastly and Fly.io.
[52.22 --> 56.02]  Our pods are fast to download globally because Fastly is fast globally.
[56.02 --> 58.08]  Learn more at Fastly.com.
[58.46 --> 60.74]  And our friends at Fly let you deploy your app closer to your users.
[61.06 --> 64.96]  It's like a CDM, but for your entire application, if it runs in Docker, it runs on Fly.
[65.34 --> 67.18]  Try it free at Fly.io.
[74.18 --> 77.06]  This episode is brought to you by our friends at Fly.
[77.40 --> 81.64]  Fly lets you deploy full stack apps and databases closer to your users, and they make it too
[81.64 --> 82.00]  easy.
[82.32 --> 83.40]  No ops are required.
[83.40 --> 87.98]  And I'm here with Chris McCord, the creator of Phoenix Framework for Elixir and staff engineer
[87.98 --> 88.50]  at Fly.
[88.66 --> 92.22]  Chris, I know you've been working hard for many years to remove the complexity of running
[92.22 --> 93.36]  full stack apps and production.
[93.60 --> 97.38]  So now that you're at Fly, solving these problems at scale, what's the challenge you're facing?
[97.84 --> 101.72]  One of the challenges we've had at Fly is getting people to really understand the benefits
[101.72 --> 102.86]  of running close to a user.
[102.86 --> 107.90]  Because I think as developers, we internalize as a CDN, people get it.
[108.00 --> 110.70]  They're like, oh, yeah, you want to put your JavaScript close to a user and your CSS.
[111.30 --> 114.74]  But then for some reason, we have this mental block when it comes to our applications.
[115.36 --> 116.38]  And I don't know why that is.
[116.50 --> 120.40]  And getting people past that block is really important because a lot of us are privileged
[120.40 --> 124.00]  that we live in North America and we deploy 50 milliseconds I hop away.
[124.00 --> 125.66]  So things go fast.
[125.92 --> 130.90]  Like when GitHub, maybe they're deploying regionally now, but for the first 12 years of their existence,
[131.16 --> 133.22]  GitHub worked great if you lived in North America.
[133.42 --> 137.06]  If you lived in Europe or anywhere else in the world, you had to hop over the ocean and
[137.06 --> 138.52]  it was actually a pretty slow experience.
[138.78 --> 142.50]  So one of the things with Fly is it runs your app code close to users.
[142.62 --> 146.12]  So it's the same mental model of like, hey, it's really important to put our images and
[146.12 --> 147.26]  our CSS close to users.
[147.26 --> 149.18]  But like, what if your app could run there as well?
[149.30 --> 150.82]  API requests could be super fast.
[150.90 --> 152.58]  What if your data was replicated there?
[152.58 --> 154.08]  Database requests could be super fast.
[154.20 --> 159.20]  So I think the challenge for Fly is to get people to understand that the CDN model maps
[159.20 --> 160.76]  exactly to your application code.
[160.82 --> 164.08]  And it's even more important for your app to be running close to a user because it's
[164.08 --> 165.24]  not just requesting a file.
[165.26 --> 169.28]  It's like your data and saving data to this, especially data for disk that all needs to
[169.28 --> 172.84]  live close to the user for the same reason that your JavaScript assets should be close
[172.84 --> 173.28]  to a user.
[173.94 --> 174.12]  Very cool.
[174.18 --> 174.76]  Thank you, Chris.
[174.76 --> 178.50]  So if you understand why you CDN your CSS and your JavaScript, then you understand why
[178.50 --> 180.34]  you should do the same for your full stack app code.
[180.34 --> 183.52]  And Fly makes it too easy to launch most apps in about three minutes.
[183.92 --> 185.74]  Try it free today at fly.io.
[185.90 --> 187.38]  Again, fly.io.
[187.38 --> 214.72]  I'm here with Jack Dorsey.
[214.72 --> 215.80]  Jack, this is your conference.
[215.92 --> 217.36]  You need no introduction course.
[217.90 --> 223.14]  Before we go into all the details of the announcements of this conference and obviously the name
[223.14 --> 227.44]  change from square to block and this bigger vision that you're implementing and doing,
[228.14 --> 229.44]  can we talk a bit about you?
[229.56 --> 232.92]  The reason why I think I want to do this is because this is a developer conference.
[233.14 --> 234.78]  You're in your own words.
[234.78 --> 235.66]  You've said you're a hacker.
[235.82 --> 237.06]  You're a hacker trend CEO.
[237.06 --> 243.02]  I watched the Lex Friedman podcast you're on and I love that podcast and your appearance
[243.02 --> 243.28]  on there.
[243.36 --> 247.26]  But what does it mean to be a hacker turned CEO today?
[248.06 --> 248.26]  Yeah.
[248.38 --> 252.98]  When I was 14, I was a legitimate hacker.
[253.40 --> 260.28]  I just loved tinkering with computers and I found BBSs and I found the internet through
[260.28 --> 267.14]  those BBSs and it was the only way I really learned in the early days was trying to find
[267.14 --> 273.28]  ways into these systems and then seeing the source code for a lot of it because a lot
[273.28 --> 276.64]  of the source code of the early internet was open, still is.
[277.64 --> 279.58]  Most of the internet runs on open source software.
[279.58 --> 287.14]  So I have so much gratitude for the people that chose usually as their side things to
[287.14 --> 290.14]  build software for the public and in the public.
[291.28 --> 294.40]  And it was, I was really into punk rock at the time as well.
[296.00 --> 300.72]  And one of the interesting things around punk rock is like, you know, someone gets up there
[300.72 --> 303.46]  first time with a band and they're absolutely terrible.
[303.86 --> 307.74]  And then you see them the next month and they get a little bit better and you see them two
[307.74 --> 310.06]  months after that and they're really good.
[310.34 --> 311.16]  And then they get great.
[311.56 --> 316.02]  And just being able to like create in public and make your mistakes in public.
[316.26 --> 322.82]  I saw the same sort of attitude and approach in, on the internet and open source software
[322.82 --> 327.18]  where you're not, you're a terrible programmer and you put something out there and, and you
[327.18 --> 332.36]  get feedback and it's usually super negative feedback and, you know, angry people behind
[332.36 --> 336.30]  keyboards, but it gets you into a better state.
[336.30 --> 337.68]  It helps you learn.
[338.76 --> 342.96]  And you learn from others just by watching their work and watching what they're doing and
[342.96 --> 344.48]  what mistakes they're making.
[344.88 --> 348.98]  The other thing of hacker to me means like you do whatever it takes to make it work.
[349.32 --> 350.54]  I was not an engineer.
[350.78 --> 352.70]  I would never an engineer.
[353.46 --> 357.56]  I just don't have the skill for that engineer being someone who actually can make something
[357.56 --> 363.68]  work, but also it be stable and scalable and, and be fail safe.
[363.68 --> 370.24]  Um, I learned enough to make the thing work, barely work, and it would probably fall down
[370.24 --> 371.06]  at some point.
[371.76 --> 377.52]  Um, so I wrote all the original code for square, uh, back then, and it was quickly replaced
[377.52 --> 379.52]  by people who could actually make a scale.
[379.52 --> 380.12]  Yeah.
[380.12 --> 383.30]  Although I thought mine was pretty good in this case.
[383.90 --> 383.96]  Yeah.
[383.98 --> 386.08]  You're doing some cool stuff in the public too, especially with Spar.
[386.14 --> 391.10]  We'll talk about some of the stuff that you're doing in the open, you know, the, the Bitcoin
[391.10 --> 396.02]  wallet, of course, mining Bitcoin, the hardware aspects, but this aspect of embracing open
[396.02 --> 400.84]  source software, embracing, you know, really the public aspect of getting that feedback loop,
[400.86 --> 401.76]  which I think is pretty interesting.
[401.76 --> 406.52]  So feel free to pepper that as we get closer to it, but I know that you mind Bitcoin.
[406.68 --> 408.34]  Do you do anything, anything developer today?
[408.46 --> 413.12]  Like if you're hacking today, how would you describe a hack that you might do?
[413.24 --> 416.00]  Not so much today specifically, but today in terms of the timeframe.
[417.12 --> 417.20]  Yeah.
[417.24 --> 421.40]  I mean, just on that point, like, I think it's really important as companies get more successful
[421.40 --> 425.42]  that they give back to what they've taken so much from and open source was that for
[425.42 --> 425.68]  us.
[425.68 --> 431.18]  So we're doing a lot with open source because we, because we've been successful because
[431.18 --> 432.80]  of it and we need to give back.
[433.76 --> 439.30]  So today I'm learning how to program Rust and that's literally today, but also over the
[439.30 --> 439.94]  past few months.
[440.12 --> 441.72]  And I love the language.
[441.90 --> 442.76]  I think it's incredible.
[443.44 --> 449.94]  It, it's compiler is amazing because it points out so many errors that you would have not otherwise
[449.94 --> 451.16]  seen until you run it.
[451.60 --> 455.04]  Some weird occurrence happens and then you come into contact with it.
[455.04 --> 461.36]  So it's, it's an amazingly well-designed language and I, like, it's a joy to write
[461.36 --> 462.20]  stuff in it.
[462.82 --> 463.16]  Pro Rust.
[463.28 --> 463.52]  All right.
[463.76 --> 465.36]  What kind of things you're hacking on with Rust?
[465.42 --> 466.06]  Anything in particular?
[466.54 --> 467.74]  Just basic stuff.
[467.84 --> 471.10]  I, I really love like low latency real-time systems.
[471.26 --> 476.36]  So I'm trying to get more into that, but obviously like there's a lot of Bitcoin in the broader
[476.36 --> 478.70]  crypto ecosystem that's written in Rust.
[478.70 --> 484.74]  So, um, it's, it's very good at real-time low latency system level work.
[484.74 --> 487.06]  And that's kind of what I'm fascinated by.
[487.14 --> 492.08]  Not that it would be useful at all, but, um, it's a, it's a great challenge for me.
[492.44 --> 494.12]  I think it's so important to tinker, right?
[494.12 --> 495.14]  You got to remain curious.
[495.14 --> 502.04]  And if you get stagnant, if you don't, I mean, it would be semi easy for someone like you
[502.04 --> 505.96]  to be where you're at in terms of your, you know, what you've achieved in your life and
[505.96 --> 508.36]  what you lead to just sort of just lean back a little bit.
[508.46 --> 513.40]  But I think being curious is always important to kind of progress and grow and, and just
[513.40 --> 514.30]  still innovate.
[514.30 --> 514.60]  Really.
[514.68 --> 517.58]  You see the edge of things and you're not, you're not letting go.
[517.96 --> 518.36]  Yep.
[518.44 --> 518.94]  A hundred percent.
[519.18 --> 519.96]  That's why I do it.
[519.96 --> 525.76]  Well, the theme of this conference, uh, is this new world and it could be sort of framed
[525.76 --> 526.38]  in a couple of ways.
[526.38 --> 530.10]  Obviously this new world in terms of what happened in the last couple of years, but also this
[530.10 --> 535.96]  new world in terms of this name change square term block, uh, square being the synonymous
[535.96 --> 538.90]  name for your seller's platform and everything you're doing there.
[538.90 --> 543.94]  But what is, uh, this was announced back in December, the, the name of block, et cetera.
[544.26 --> 546.86]  The site is obviously super beautiful.
[546.98 --> 547.82]  I love the site.
[547.82 --> 550.54]  When it first came out, I was like, what is this block dot X, Y, Z.
[550.68 --> 551.58]  And it was really cool.
[552.44 --> 555.98]  Uh, TBD spiral title, you know, cash app.
[556.02 --> 561.10]  You've got a lot of things happening, but share the bigger picture of what happened with
[561.10 --> 563.20]  the behind the scenes of this name change.
[563.32 --> 563.48]  Sure.
[563.84 --> 569.22]  People see in December, this new name, these new, these new desires for, for square now
[569.22 --> 574.88]  is block, but help me understand when this journey began and why block exists today.
[575.02 --> 575.70]  What you plan to do?
[575.70 --> 575.98]  Yeah.
[575.98 --> 581.28]  It really began like at the start of the company, we, we made a conscious choice not to name
[581.28 --> 584.12]  our company after anything having to do with payments or finance.
[584.76 --> 591.90]  So we wanted a word, a name that allowed us flexibility and didn't keep us into the payments
[591.90 --> 592.14]  world.
[592.26 --> 597.74]  We didn't really know why we had no plans or intentions about expanding beyond what we originally
[597.74 --> 601.02]  started with, which was just a credit card reader that plugged in the phone.
[601.02 --> 601.50]  Yeah.
[601.82 --> 606.32]  But little by little, as we saw people use it, we realized we weren't building a credit
[606.32 --> 606.76]  card reader.
[607.40 --> 610.20]  We were building a way for people to make a sale.
[610.20 --> 614.76]  And then we stepped back and said, well, credit card reader is one way to make the sale, but
[614.76 --> 615.44]  it's not the only one.
[615.50 --> 617.16]  There's many ways for someone to make a sale.
[617.58 --> 622.48]  So that led us to like build a register to help people organize, you know, their information
[622.48 --> 626.76]  around their business and make better decisions, which would grow their sales and make more
[626.76 --> 627.10]  sales.
[627.50 --> 632.62]  It allowed us to get to square capital, which allowed us to lend people money to build up
[632.62 --> 633.02]  their business.
[633.02 --> 639.90]  $5,000 for a few new salon chairs could double or triple your business just with that small
[639.90 --> 642.54]  loan, which no bank was doing under $25,000.
[643.14 --> 649.54]  And it allowed us to build something like Cash App that was more focused on individuals instead
[649.54 --> 650.40]  of sellers.
[651.66 --> 657.86]  And that was a moment, especially as Cash App got bigger and bigger in terms of scale, that
[657.86 --> 661.72]  we realized that there might be something here.
[662.12 --> 667.62]  We're not just building an ecosystem for sellers, but we're building an ecosystem of ecosystems.
[668.00 --> 672.42]  And what I mean by that is like the seller business has always been about what are all
[672.42 --> 677.10]  the tools that we can build for a seller to help them make the sale and make more sales?
[677.52 --> 680.32]  And how do they positively reinforce one another?
[680.50 --> 685.96]  Utilizing the register, using the register and payments allows you access to get a square
[685.96 --> 687.66]  capital loan, for instance.
[688.28 --> 695.10]  Using the developer platform allows you to build other functionality on top of or get
[695.10 --> 698.12]  functionality for a small business or a larger size business.
[698.84 --> 703.20]  So we were really excited about that idea of building this ecosystem.
[703.50 --> 705.80]  And now we had two ecosystems at scale.
[706.70 --> 710.02]  And so we asked, why not add others?
[710.22 --> 715.92]  And we found another one called Tidal, which is a music streaming service, which to a lot of
[715.92 --> 719.64]  people felt like a very weird thing to do, a financial company buying a music streaming
[719.64 --> 720.08]  service.
[720.66 --> 725.86]  But if you look at what an artist has to go through to start their career or grow their
[725.86 --> 728.00]  career, it's not all that dissimilar from a small business.
[728.42 --> 732.44]  So we're focused on the artist problem, not the streaming aspect.
[732.44 --> 740.18]  And then we started a new business in a new ecosystem called TBD, which intends to build a developer
[740.18 --> 745.40]  platform for people to build exchanges, Bitcoin exchanges all around the world.
[745.40 --> 755.64]  So when we got to those four, we're like, you know, Square doesn't, Square, sellers know Square as Square.
[755.84 --> 757.88]  They don't consider Cash App to be part of that.
[758.00 --> 760.06]  Cash App doesn't consider Square at all.
[760.14 --> 763.32]  And in fact, most of the Cash App customers don't even know that Square exists.
[763.32 --> 767.14]  So we needed a new name.
[767.22 --> 771.66]  We needed to give the Square name to Square, to the seller business.
[772.44 --> 774.16]  And therefore, we needed a new name.
[774.22 --> 778.84]  And we went through a lot of names, some terrible, some amazing.
[779.30 --> 783.36]  And we ended up at Block because there's a reference to the Square shape.
[784.22 --> 786.58]  It's just as boring as the name Square.
[786.78 --> 791.34]  We wanted a boring name originally because we didn't want to be in front of our customers.
[791.78 --> 792.88]  We wanted to be invisible.
[792.88 --> 793.98]  We wanted to be behind them.
[794.06 --> 794.90]  We wanted to be under them.
[795.96 --> 801.70]  It's a reference to a block, like a neighborhood block where we found our sellers, a block party
[801.70 --> 806.02]  for Tidal, blockchain for all the Bitcoin stuff we're doing.
[806.16 --> 808.08]  So the name just worked.
[809.04 --> 814.78]  And, you know, it's simple and boring and we can work to make it cool.
[814.88 --> 818.72]  But it's never meant to be a consumer-facing brand.
[818.72 --> 832.46]  It's only for our recruiting efforts, our investors, and like a way to reference this thing that contains all these companies inside of it.
[832.46 --> 833.10]  Yeah.
[833.10 --> 838.04]  One of the things you said in the announcement for, I think, is really interesting.
[838.82 --> 844.02]  You said block is a new name, but our purpose of economic empowerment remains the same.
[844.40 --> 847.24]  You said no matter how we grow or change, we will continue.
[847.32 --> 853.28]  And this is the point I want to kick on is we will continue to build tools to help increase access to the economy.
[853.28 --> 862.10]  And that's obviously where you began with Square with sellers and this realization going from the original hardware to the platform and all the software and all the data science behind things.
[862.56 --> 869.54]  I think that's really interesting how that vision process, because as you had said, all the things you were doing grew beyond the Square brand.
[869.64 --> 873.68]  And it actually kind of hindered Square because it's like I was a cash-up user.
[873.78 --> 875.02]  I've been a cash-up user since 2013.
[875.48 --> 877.10]  And I talked to other cash-up users.
[877.22 --> 877.88]  I pay florists.
[878.02 --> 879.28]  I pay my masseuse.
[879.44 --> 880.66]  I mean, I pay a lot of different people.
[880.66 --> 882.30]  I pay my housekeeper.
[882.42 --> 886.04]  I pay my babysitter all through Cash-Up, but they don't know that it's Square.
[886.86 --> 896.64]  And it's interesting how this name changed to allow you to zoom out further, but still kind of anchor into that core point of increasing access to the economy.
[897.12 --> 897.64]  Can you speak to that?
[898.78 --> 899.00]  Yeah.
[900.00 --> 910.14]  So our purpose is economic empowerment, which, as you said, is a way of saying, how do we build tools to allow people to participate in the economy more or better?
[910.66 --> 916.94]  In the early days of Square, it was just like, I need to accept credit cards and my bank is not allowing me to.
[917.46 --> 921.32]  They didn't have the infrastructure to do that or they chose not to.
[922.04 --> 928.98]  So we enabled millions of businesses who otherwise couldn't get a credit card acceptance account to get one.
[928.98 --> 932.02]  And that was purely access.
[932.28 --> 940.46]  The same thing was true for Cash-Up, which is like access to fast, speedy, simple financial rails to send money peer-to-peer.
[940.68 --> 947.02]  But then we started holding balances for people so they could effectively get a savings account with Cash-Up or a checking account.
[947.02 --> 954.48]  We issued Visa credit cards for them that works at ATM so they can get extra paper cash, allow them to buy and sell Bitcoin.
[955.14 --> 958.86]  All these things go towards that purpose.
[959.20 --> 960.22]  And that's what we decided.
[960.94 --> 965.20]  You know, we have these four business units now and each one of them effectively has a CEO.
[965.20 --> 972.88]  And each one of them can do whatever they want in terms of the culture, the values, the operating principles.
[973.58 --> 976.52]  But the one thing they must align around is our purpose.
[976.98 --> 980.70]  Are they serving more access to the economy?
[980.88 --> 984.16]  Are they serving more economic empowerment?
[984.16 --> 995.40]  And that's why Tidal made sense for us is because if we get this right, then we're empowering economically artists, which has been the biggest issue for artists and musicians specifically.
[995.78 --> 997.58]  The label takes so much from them.
[997.82 --> 1002.16]  They're not making a lot of money from a stream.
[1002.30 --> 1005.44]  They're making money from merchandise and touring.
[1005.84 --> 1009.86]  And they don't have a lot of options to make that part easy.
[1009.86 --> 1011.28]  Like that part is hard.
[1011.28 --> 1020.50]  And that's the part that we made easy with Square, like our e-commerce sites and in-person and services like touring and ticketing and whatnot.
[1020.76 --> 1037.74]  So to give them all of that infrastructure for any artist, whether they be very small or very large, and to put it into one download and to have an API associated with it to this conference, to put in this conference, is, I think, pretty incredible.
[1038.52 --> 1038.74]  I agree.
[1038.74 --> 1042.96]  I want to speak to the evolution, I suppose, of Square.
[1043.04 --> 1044.04]  Let's zoom into Square itself.
[1044.20 --> 1053.24]  Since we've got Square as the primary brand that was there before this rename and obviously all these changes described.
[1054.00 --> 1055.40]  But there was an evolution that took place.
[1055.50 --> 1058.86]  You began with, as you said before, this hacker mentality.
[1059.28 --> 1065.36]  Some of the – all the early code for Square was written by you and obviously replaced over time because, you know, better people.
[1065.40 --> 1066.30]  You hire better people, right?
[1066.34 --> 1067.00]  Smarter people than you.
[1067.00 --> 1068.00]  Smarter people than you.
[1068.00 --> 1069.70]  But there's this evolution that took place.
[1069.70 --> 1074.46]  You started with this hardware device and you had this idea to sort of just accept payments.
[1074.46 --> 1075.64]  But then something else happened.
[1075.64 --> 1080.74]  Something else happened that it wasn't just simply about, oh, help this seller accept credit cards.
[1080.74 --> 1082.68]  Then it was helping them get access to it.
[1082.68 --> 1084.12]  But now it's a platform.
[1084.28 --> 1090.90]  And it's a full-fledged platform with open source APIs and tons and tons of developers and tons of partners being a part of this.
[1091.60 --> 1097.80]  So far, it was talked about lots of different things happened around this implementation of this platform for folks.
[1097.92 --> 1108.72]  But help me understand what Square is today and how it's evolved from this initial idea of a hardware device that you had together for an iOS device or the 3.5-inch jack or the 3.5 jack.
[1108.72 --> 1115.16]  We resisted building an API and a platform for a long time, mainly due to my experience with Twitter.
[1115.58 --> 1119.74]  Like with that service, we released the API day one.
[1120.34 --> 1121.86]  And there was a lot of benefit to it.
[1121.86 --> 1124.10]  But all of our downtime was because of that API.
[1124.78 --> 1129.44]  Like people were just doing, you know, unexpected crazy things, as you would expect them to do.
[1129.62 --> 1129.98]  Yes.
[1130.10 --> 1130.96]  Really open API.
[1131.42 --> 1136.16]  And we should have had more constraints and controls over that.
[1136.74 --> 1139.20]  But we just didn't know what we didn't know.
[1139.64 --> 1143.08]  And with Square, I knew more of that.
[1143.08 --> 1145.04]  And now we're moving money around.
[1145.72 --> 1151.48]  So people doing crazy, unexpected things could come at a different cost.
[1152.54 --> 1159.16]  So we want to be very thoughtful about how we thought about a platform and how we built it out.
[1159.16 --> 1169.52]  And it wasn't until we hired Alyssa, who runs Square in our seller business, that we felt comfortable, like, really going for it.
[1170.26 --> 1174.74]  And the reason why is because we had experience building that at Microsoft and Amazon.
[1175.02 --> 1176.62]  And I'm sure made a bunch of mistakes there.
[1176.72 --> 1178.74]  And all those mistakes will not be repeated.
[1178.84 --> 1180.06]  We can make new mistakes now.
[1180.06 --> 1184.32]  So we, you know, took that experience.
[1184.58 --> 1199.76]  And then she did something really cool, which was, like, everything that we use, everything that we build that's front-facing to our customers should use the exact same API that we're giving to external developers as well.
[1200.48 --> 1208.16]  So the register uses the same API and platform that any third-party developer can.
[1208.16 --> 1214.74]  It really simplified how we thought about building generally and made us slower for a little bit.
[1214.92 --> 1219.56]  But then, you know, the gains compound and make us much faster.
[1219.84 --> 1224.38]  But it put us on a level playing field with our developers as well, which I think is really important.
[1224.92 --> 1225.00]  Yeah.
[1225.06 --> 1226.86]  A lot of companies tend to do that.
[1228.78 --> 1232.46]  So that was a critical insight.
[1232.46 --> 1247.72]  And I think that was, you know, one of the reasons our platform has been as successful as it has is because, like, this principle of, like, we're going to use what we're giving out to other people as well.
[1247.84 --> 1249.94]  And, like, if we feel the pain, they're going to feel the pain.
[1250.02 --> 1250.86]  And they can't feel pain.
[1250.86 --> 1255.76]  So let's make sure that we're building in such a way that we don't feel the pain either.
[1256.08 --> 1256.24]  Yeah.
[1256.34 --> 1271.12]  It really changed our company and gave us an opportunity for our customers to build on top of us, to build alongside of us, and then also create a developer ecosystem that's doing it for businesses, small businesses, larger businesses.
[1271.12 --> 1288.08]  But allows us to, you know, fit into whatever arcane system that exists or anything that people want to build that, you know, we will never build because it's too specific, too niche, but really meaningful to that particular person or that organization.
[1301.12 --> 1316.78]  This episode is brought to you by our friends at FireHydrant.
[1317.12 --> 1319.84]  FireHydrant is a reliability platform for every developer.
[1320.34 --> 1322.82]  Incidents are a win, not an if situation.
[1323.30 --> 1327.32]  And they impact everyone in the organization, not just SREs.
[1327.32 --> 1330.96]  And I'm here with Robert Ross, founder and CEO of FireHydrant.
[1331.30 --> 1336.94]  Robert, what is it about teams getting distracted by incidents and not being able to focus on the core product that upsets you?
[1337.24 --> 1348.12]  I think that incidents bring a lot of anxiety and sometimes fear and maybe even a level of shame that can cause this paralysis in an organization from progress.
[1348.50 --> 1359.60]  And when you have the confidence to manage incidents at any scale of any variety, everyone just has this breath of fresh air that they can go build the core product even more.
[1359.60 --> 1364.52]  I don't know if anyone's had the opportunity, maybe is the word, to call the fire department.
[1364.72 --> 1370.36]  But no matter what, when the fire department shows up, it doesn't matter if the building is hugely on fire.
[1370.52 --> 1374.04]  They are calm, cool and collected because they know exactly what they're going to do.
[1374.30 --> 1377.22]  And that's what FireHydrant is built to help people achieve.
[1377.42 --> 1378.00]  Very cool.
[1378.08 --> 1378.62]  Thank you, Robert.
[1378.62 --> 1385.38]  If you want to operate as a calm, cool, collected team when incidents happen, you got to check out FireHydrant.
[1385.70 --> 1389.52]  Small teams, up to 10 people can get started for free with all the features.
[1389.96 --> 1391.30]  No credit card required to sign up.
[1391.60 --> 1393.28]  Get started at FireHydrant.com.
[1393.28 --> 1395.64]  Again, FireHydrant.com.
[1410.12 --> 1412.04]  I'm obviously a developer myself.
[1412.30 --> 1413.16]  I got a heart for developers.
[1413.40 --> 1417.50]  My company is totally focused on media that is for software developers.
[1417.68 --> 1419.50]  So our audience, when you say, who's your audience?
[1419.60 --> 1420.50]  It's software developers.
[1420.50 --> 1426.06]  So given that, and we're at this conference, Square Unboxed 2022, it's for developers.
[1426.20 --> 1427.34]  You've got sellers here too, I'm sure.
[1427.60 --> 1428.40]  You've got partners here.
[1428.42 --> 1431.84]  You've got the larger ecosystem, but it's focused on software developers.
[1432.26 --> 1442.86]  And this is where I was really captured by this vision of Square because I think there's some folks who may have a misconception or an incorrect assumption of what Square is.
[1443.30 --> 1448.86]  But this platform for developers to build upon, help me understand what the opportunity is for developers.
[1448.86 --> 1453.72]  Because I've been speaking to folks behind the scenes, Shannon Skipper and others about this.
[1453.92 --> 1459.60]  And it's like, well, this is a place for developers to come and build apps for millions of sellers globally.
[1460.26 --> 1464.22]  And as you roll out to Japan and other markets, the opportunity only gets greater.
[1464.22 --> 1473.50]  And as Bitcoin maybe becomes, you know, an internet native currency, Cash App, and as it gets integrated with Cash App Pay, et cetera, that's happening now.
[1473.92 --> 1476.88]  This is an interesting space to be in.
[1476.94 --> 1479.36]  Help me understand the opportunity specifically for developers.
[1479.36 --> 1488.96]  We learned a lot from the seller platform such that, you know, Cash App is going to do something similar.
[1489.26 --> 1492.56]  And TBD is an entirely, you know, it's entirely a platform.
[1492.92 --> 1495.58]  Like that's its only reason to be and to exist.
[1495.58 --> 1498.96]  So, you know, we're definitely on that track.
[1499.16 --> 1505.74]  And we want to make sure that we're building more and more platform type things forevermore.
[1505.88 --> 1509.16]  Like everything that we do in the future should have platform elements.
[1509.36 --> 1512.70]  Even we're building a Bitcoin wallet and a Bitcoin miner.
[1512.86 --> 1513.30]  Yeah.
[1513.38 --> 1515.28]  We're building it so that it's open source.
[1515.86 --> 1517.00]  All the code will be available.
[1517.12 --> 1518.58]  The hardware design will be available.
[1519.18 --> 1523.30]  Everything about it will be completely open for any developer to use.
[1523.38 --> 1524.70]  They don't need to build on top of it.
[1524.70 --> 1528.00]  They can just steal all the code and the ID and just build whatever they want.
[1529.64 --> 1531.50]  Learn from your mistakes or get rights.
[1531.70 --> 1532.94]  That's by design.
[1533.06 --> 1533.66]  That's by design.
[1533.76 --> 1535.00]  Again, giving back to the community.
[1535.52 --> 1537.58]  We'll compete on our build quality.
[1537.70 --> 1538.98]  We'll compete on our experience.
[1539.16 --> 1541.54]  We'll compete on services like security.
[1542.14 --> 1545.44]  That's, you know, we wanted to find that lane and then stick to it.
[1545.48 --> 1548.16]  But everything else should be usable by everyone.
[1548.50 --> 1550.94]  And that, I think, is the opportunity.
[1552.40 --> 1554.40]  We want to open as much as possible.
[1554.70 --> 1557.14]  And again, like we don't know what we don't know.
[1557.22 --> 1566.98]  And like the more open you are and the less constraint you have on what can be built, the more surprising and unexpectedly great things can happen.
[1566.98 --> 1570.12]  And that benefits the whole ecosystem.
[1570.12 --> 1579.92]  It goes back, like in the seller case, certainly everything built by developers on the platform benefits sellers and benefits Square and Block.
[1579.92 --> 1583.46]  In the Bitcoin wallet and the Bitcoin miners space.
[1584.14 --> 1589.82]  If someone just takes the designs and takes the code and builds their own thing, it benefits the Bitcoin ecosystem.
[1590.06 --> 1596.36]  It doesn't benefit Block directly, but over time, because the Bitcoin ecosystem is stronger and better than Block is stronger and better.
[1596.36 --> 1598.36]  So that's just the mindset.
[1598.80 --> 1605.88]  And, you know, this platform that we're discussing today started off.
[1606.58 --> 1606.66]  Okay.
[1606.66 --> 1612.78]  So in terms of some key API announcements, you've got a lot of fun stuff happening this conference today.
[1614.08 --> 1616.82]  You've got Cash App Pay, which is GA for developers.
[1617.10 --> 1618.22]  I believe it's in the U.S. only.
[1619.00 --> 1621.48]  You've got Afterpay, which is in GA for developers.
[1621.68 --> 1624.18]  That's U.S. and Australia because it's originated in Australia.
[1624.26 --> 1624.70]  It makes sense.
[1625.18 --> 1626.18]  You've got your Bookings API.
[1626.40 --> 1627.24]  You've got your Checkout API.
[1627.24 --> 1630.92]  Of these particular APIs, obviously, they extend the platform.
[1631.12 --> 1632.30]  They enable more to happen.
[1632.90 --> 1639.48]  Is there anyone in particular that you're just personally excited about or played a hand in or there's any excitement around there for you?
[1641.60 --> 1643.38]  This is going to sound like a non-answer.
[1643.54 --> 1643.74]  Sorry.
[1643.88 --> 1645.34]  I apologize for that.
[1645.46 --> 1653.26]  But the reason I think we're successful as a company is because we're not focused on any one thing.
[1653.70 --> 1656.46]  It's the in-between that matters.
[1656.46 --> 1658.98]  It's a connection between all these things that matter.
[1659.42 --> 1659.50]  Right.
[1659.58 --> 1661.94]  And the breadth of our offering that matters.
[1662.20 --> 1668.28]  We compete with registers and payment providers and lenders.
[1668.62 --> 1674.56]  But the fact that we have it all in one app is what sets us apart and makes us unique.
[1674.74 --> 1682.82]  It makes us a little bit slower because we have to manage all the complexity instead of a seller hooking all these things together and having that complexity.
[1682.82 --> 1685.12]  So we've taken that complexity on.
[1685.12 --> 1687.70]  But it makes us a lot more deliberate.
[1687.70 --> 1689.38]  And I think it makes us a lot more resilient.
[1689.96 --> 1690.02]  Yeah.
[1690.02 --> 1692.30]  So we approach the platform in the same way.
[1692.40 --> 1696.42]  Like, if you use any one of these parts, they can be exciting.
[1696.42 --> 1702.16]  But if they positively reinforce one another, then it's real.
[1702.16 --> 1714.00]  So what I'm most excited about is we continue to build out things as a potential to positively reinforce another aspect of the platform or the API or the broader ecosystem.
[1714.74 --> 1717.30]  And, you know, Afterpay is a good example of that.
[1717.50 --> 1722.22]  Like, this is exactly in between Square and Cash App.
[1722.78 --> 1722.92]  Yeah.
[1722.92 --> 1724.18]  Exactly in between.
[1724.18 --> 1731.56]  And it's, like, the best way for us to show, like, we intend to connect these ecosystems together.
[1732.00 --> 1732.86]  That's the power.
[1733.26 --> 1738.10]  Like, there are competitors that have all the seller tools we have potentially.
[1738.26 --> 1739.08]  They don't have Cash App.
[1739.08 --> 1742.52]  They don't have any, you know, consumer focus.
[1742.74 --> 1746.78]  And the competitors that have a Cash App type thing, they don't have any of the seller side.
[1747.40 --> 1750.26]  And then, you know, we get into the music and nobody has that.
[1750.48 --> 1753.88]  So, like, it's – that's the exciting bit for me.
[1753.94 --> 1757.42]  It's just, like, how these things work together rather than the individual parts.
[1757.42 --> 1767.26]  I love that you're able to give these companies and their CEOs, really, that room to do what they need to do, provided that one adherence that you mentioned.
[1768.54 --> 1771.92]  But the platform that you're building enables them all to be connected.
[1771.92 --> 1788.34]  As you'd mentioned, Afterpay sort of sits in between Square and Cash App and, in many ways, kind of caters to that Cash App consumer who maybe is less excited about using a credit card and more excited about using their own cash or Bitcoin or the credit card you give – or I guess it's not really a credit card.
[1788.40 --> 1791.38]  It's more of a – it uses the credit card system, but it's not a credit card itself.
[1791.48 --> 1795.50]  It's that just simply a cash card that enables all those things to connect.
[1795.50 --> 1807.04]  That's really, I think – you know, when I asked you the question earlier about developers, I think that's what's beautiful because if you choose this platform – and we're going to get into SoFi and what's happening there, this is a larger implementation for a seller.
[1807.70 --> 1818.18]  What happens for developers is now they've got, like, this – all these interconnected abilities, really, between Cash App, Afterpay, Square the Platform, Tidal, TBD, Spiral, all these fun things you're doing.
[1818.34 --> 1820.46]  Like, it's really astounding.
[1820.46 --> 1822.36]  I mean, I got to ask you more questions.
[1822.44 --> 1825.68]  I'm not even sure where to go because we just have so – there's just so much we could cover.
[1826.16 --> 1832.34]  In terms of Cash App, in terms of Afterpay, like, why did that acquisition make sense for you?
[1832.42 --> 1834.54]  Like, how did that click for you?
[1834.56 --> 1838.20]  Because it was – when that acquisition came out, a lot of folks were like, why?
[1838.60 --> 1839.96]  That's interesting, but why?
[1840.50 --> 1841.68]  Help us understand the why to that.
[1842.62 --> 1847.68]  I mean, the other thing I'm really proud of is, like, this is not a strategy that came from me.
[1847.68 --> 1852.74]  It came from Alyssa, who runs Square, the seller business, and Brian, who runs Cash App.
[1853.16 --> 1862.84]  And they work together because, you know, I had been pushing them for, you know, for some time to, like, push the ecosystems together and, like, find the connections between the two.
[1862.90 --> 1864.36]  Because we know they're there.
[1864.96 --> 1867.06]  They might start off as very small.
[1867.06 --> 1876.40]  But it came out of that push where they found an obvious connection that was large, and that was Afterpay.
[1876.82 --> 1886.04]  And we met with the entrepreneurs and the leads there, Nick and Ant, and, you know, just loved their values and what they were trying to do in the world
[1886.04 --> 1893.06]  and how much humility they have and, like, what they care about.
[1893.32 --> 1895.54]  And it just felt like a fit.
[1895.64 --> 1897.34]  Like, it felt like one thing.
[1897.44 --> 1903.26]  So we made it one thing, even though it was a very, very large thing to do, the biggest thing we've ever done, and extremely risky.
[1903.26 --> 1914.62]  But I trusted Brian and Alyssa because they did the work, and they showed why this connection makes sense and why it's the future
[1914.62 --> 1921.76]  and why it's really important for each one of their businesses, but more importantly for our business, Block.
[1922.58 --> 1928.64]  And, you know, the majority of my time right now is focused on the smaller things, like Tidal and the Bitcoin stuff.
[1931.10 --> 1931.94]  Small for now.
[1931.94 --> 1933.32]  Yeah, small for now.
[1934.16 --> 1942.94]  And I had that same relationship with Square and Cash App, where before I was in every product review, now I have no idea what they're doing.
[1943.32 --> 1947.74]  And I hear about it usually when the world hears about it, and it's awesome.
[1948.00 --> 1949.02]  Like, I just, I love it.
[1961.94 --> 1966.16]  This episode is brought to you by Sourcegraph.
[1966.24 --> 1971.26]  With the launch of their Code Insights product, teams can now track what really matters in their code base.
[1971.56 --> 1977.86]  Code Insights instantly transforms your code base into a queryable database to create visual dashboards in seconds.
[1978.28 --> 1981.30]  And I'm here with Joel Cortler, the product manager of Code Insights for Sourcegraph.
[1981.84 --> 1985.90]  Joel, the way teams can use Code Insights seems to pretty much be limitless,
[1985.90 --> 1991.48]  but a particular problem every engineering team has is tracking versions of languages or packages.
[1992.06 --> 1994.66]  How big of a deal is it actually to track versions for teams?
[1995.12 --> 1996.88]  Yeah, it's a big deal for a couple of reasons.
[1997.04 --> 1998.86]  The first is, of course, just compatibility.
[1999.12 --> 2003.00]  You don't want things to break when you're testing locally or to break on your CI systems, test systems.
[2003.38 --> 2006.74]  You need to have some sort of level of, like, version unification, minimum version support,
[2006.90 --> 2009.64]  and all of that needs to be, you know, compatible forward.
[2009.64 --> 2014.90]  But the other thing we learned was that for a lot of customers, especially, you know, engineering organizations that are pretty established,
[2015.28 --> 2019.42]  they have older versions of things or even older versions of, like, SaaS tools they don't use anymore
[2019.42 --> 2023.80]  that they haven't fully removed because they're, like, not sure if it's still used or they, you know, lost focus on that.
[2024.06 --> 2026.92]  And they're spinning up old virtual machines that they're still paying for.
[2027.02 --> 2031.02]  They're using, you know, old SaaS subscriptions they're afraid to cancel because they're not sure if anyone's actually using it.
[2031.14 --> 2036.54]  And so getting off of those versions not just, like, saves you the headaches and the risks and the vulnerabilities of being on old versions,
[2036.54 --> 2044.42]  but also literally the money of, you know, older systems running more slowly or the build times or, you know, virtual machines and SaaS tools that you're no longer using.
[2044.74 --> 2046.60]  Before you had this ability, we talked to teams.
[2046.92 --> 2048.30]  There are basically three ways you could do this.
[2048.54 --> 2052.02]  You could slack a million people and ask for just, like, an update point in time.
[2052.30 --> 2057.84]  You could have sort of one human in one spreadsheet where, like, it's somebody's job every Friday or every two weeks to just, like,
[2058.10 --> 2061.28]  search all the code and find all the versions and write it down in a Google sheet.
[2061.54 --> 2065.80]  Or there were a couple of companies I think I came across with in-house systems that were sort of complicated.
[2065.80 --> 2068.94]  You had to know, you know, maybe Kotlin, but you didn't know Kotlin.
[2069.02 --> 2070.64]  But if you wanted to use this system, you had to learn Kotlin.
[2071.10 --> 2076.22]  And you'd have to sort of build the whole world from scratch and run basically a tool like this with a pretty steep learning curve.
[2076.58 --> 2080.34]  And now for all three of those, you could replace it with a single line source graph search,
[2080.52 --> 2084.12]  which is basically just the name of the thing you're trying to track and the version string in the right format.
[2084.38 --> 2087.66]  And then we have templates that will help you get started if you're not sure what that format is.
[2087.76 --> 2090.92]  And then it'll automatically track all the different versions for you, both historically.
[2091.08 --> 2093.24]  So even if you start using it today, you can see your historical patterns.
[2093.34 --> 2094.72]  And then, of course, going forward.
[2094.72 --> 2095.96]  Very cool. Thank you, Joel.
[2096.06 --> 2100.50]  So right now there is a treasure trove of insights just waiting for you.
[2100.84 --> 2107.34]  Living inside your code base right now, teams are tracking migrations, adoption, deprecations.
[2107.68 --> 2110.54]  They're detecting and tracking versions of languages and packages.
[2110.54 --> 2114.50]  They're removing or ensuring the removal of security vulnerabilities.
[2115.02 --> 2116.46]  They understand their code by team.
[2116.56 --> 2118.24]  They can track their code smells and health.
[2118.40 --> 2122.78]  And they can visualize configurations and services and so much more with code insights.
[2122.78 --> 2129.42]  A good next step is to go to about.sourcegraph.com slash code dash insights.
[2129.70 --> 2132.24]  See how other teams are using this awesome feature.
[2132.56 --> 2137.32]  Again, about.sourcegraph.com slash code dash insights.
[2137.66 --> 2139.36]  This link is in the show notes.
[2139.36 --> 2144.80]  And by our friends at Influx Data, the makers of the time series data platform InfluxDB.
[2145.42 --> 2147.82]  Influx Data believes in putting the developer first.
[2148.22 --> 2150.76]  That's why they built their time series platform with tools.
[2150.92 --> 2155.26]  So you don't have to make wholesale changes to your product or your application just to use InfluxDB.
[2155.72 --> 2163.08]  You can code in your language of choice using your preferred tools and wherever you're building applications in the cloud, on premise or locally.
[2163.08 --> 2168.14]  So if you build IoT, analytics or cloud applications, you might want to check out InfluxDB.
[2168.44 --> 2175.76]  It has a powerful API and tool set, a high performance time series engine and a community of developers in both cloud and open source.
[2176.20 --> 2185.46]  InfluxDB delivers visibility with real time analytics so you can quickly act on your data, identify patterns, predict future outcomes and turn insights into action.
[2185.86 --> 2189.24]  Check it out and start free at InfluxData.com slash changelog.
[2189.52 --> 2192.74]  Again, InfluxData.com slash changelog.
[2192.74 --> 2222.72]  InfluxData.com slash changelog.
[2222.74 --> 2234.28]  Has generally been florists, barbers, masseuse, you know, those types of folks where they're smaller, they have your point of sale, they have all that, the hardware there on that front.
[2234.42 --> 2239.10]  But SoFi Stadium is a different kind of seller for you to approach.
[2239.36 --> 2246.88]  You were invited to the RFP as a dark horse candidate, which I think is super interesting, essentially saying you're not going to win and you do win.
[2246.88 --> 2251.02]  And, you know, SoFi Stadium is a massive stadium.
[2251.48 --> 2256.80]  It's all high tech from the engineering of the architecture itself up to integrating square.
[2257.02 --> 2259.38]  But this RFP got invited to it as a dark horse candidate.
[2259.38 --> 2265.92]  Can you speak to just what that means to attract the invitation of and win that kind of seller?
[2267.28 --> 2273.38]  From the dawn of the company, like maybe a year or two years in, we were wanting to be in stadiums.
[2273.38 --> 2275.74]  But we didn't have an API back then.
[2277.00 --> 2290.22]  And it would have been, and this is what we did for a few things, a lot of custom work that we had to build and take away from, it took away from everything else that we were doing.
[2290.22 --> 2299.02]  And it was the API and the platform that really enabled us to even consider being in that RFP process.
[2299.84 --> 2309.00]  I think I could be wrong that Warriors Stadium in San Francisco came slightly earlier than SoFi, but the Chase Center.
[2309.80 --> 2314.98]  But in both cases, like the, I think one of the key winning differentiators was a platform.
[2314.98 --> 2322.04]  Like this is a huge, massively scaled operation, like hardware is failing all the time.
[2322.28 --> 2323.54]  Networks are going down.
[2324.94 --> 2330.82]  Back-end software and legacy software is failing all the time and has massive amounts of redundancy.
[2331.68 --> 2336.58]  So these are the things that we could not build alone for any customer, any client.
[2337.26 --> 2341.04]  It had to be a function of like how good and flexible the platform was.
[2341.74 --> 2343.50]  And it really comes down to that word flexibility.
[2343.50 --> 2346.54]  I think we are the most flexible, and I think that's why we won.
[2347.16 --> 2349.64]  I think it's all due to what we've done with the platform.
[2350.22 --> 2352.50]  So obviously we left out Spiral from the deeper conversation.
[2352.70 --> 2357.52]  We touched on the open source nature of it, the Bitcoin wallet, the hardware to mine, all that stuff.
[2357.64 --> 2360.82]  But it began as Square Crypto.
[2361.14 --> 2367.52]  And obviously I did some research in terms of when it began for this.
[2367.52 --> 2373.34]  Listen, you had said, what's the biggest thing we could do for Bitcoin, the Bitcoin community and one of your co-partners?
[2373.88 --> 2379.42]  Mike had said, hire five open source developers and just let them do fun stuff.
[2379.52 --> 2384.46]  Can you talk about the inception of Square Crypto and how that's evolved into Spiral and what you're doing there?
[2384.98 --> 2385.08]  Yeah.
[2385.08 --> 2387.86]  I mean, that's exactly what it was.
[2388.36 --> 2389.58]  Mike and I were having dinner.
[2389.70 --> 2392.50]  He runs TBD now, by the way, Mike Brock.
[2393.42 --> 2398.90]  And he was the one I read Bitcoin in cash up started as a hack week project with me and Mike.
[2398.90 --> 2401.78]  So we were both building it.
[2402.34 --> 2405.76]  So he's kind of been my partner all along the way on the Bitcoin side of things.
[2406.68 --> 2411.50]  And I asked him, what's the greatest thing we can do for the community to give back?
[2411.74 --> 2415.78]  Because I just kept feeling like we're not giving back enough.
[2416.90 --> 2422.08]  He said, just hire five Bitcoin engineers and let them do whatever they want.
[2423.12 --> 2424.56]  Don't give them Square Equity.
[2424.90 --> 2425.60]  Give them Bitcoin.
[2426.96 --> 2428.64]  Give them no direction whatsoever.
[2428.90 --> 2430.86]  And see what happens.
[2431.68 --> 2444.70]  And I texted Amrita, our CFO, and said, let's spare $5 million a year for this thing that we just decided to do.
[2445.12 --> 2446.26]  And she's like, okay.
[2446.48 --> 2450.32]  And we kicked off a hiring process to find a lead.
[2450.98 --> 2453.30]  And that person was Steve Lee.
[2454.26 --> 2464.38]  And we didn't even want to say like, you know, all of you need to work on one project or you can all work on different projects.
[2464.50 --> 2465.52]  We wanted that to be up to them.
[2465.98 --> 2470.76]  So Steve hired four other people and assembled a team.
[2470.76 --> 2473.26]  And then they all went to an offsite to kick things off.
[2473.26 --> 2475.60]  And they decided that they wanted to work together on one project.
[2476.24 --> 2485.78]  And they wanted to work on a lightning development kit to make lightning easy for wallet developers.
[2485.78 --> 2488.66]  And they wanted to do it in Rust.
[2488.66 --> 2493.08]  And they built it in two years.
[2493.36 --> 2495.40]  And again, they told me all this.
[2495.50 --> 2496.50]  I'm like, great, amazing.
[2497.66 --> 2500.62]  And, you know, we introduced them to the broader company.
[2500.88 --> 2501.84]  And great, amazing.
[2501.84 --> 2504.82]  We didn't expect anything from it.
[2505.68 --> 2512.56]  And then two years later, as Cash App is launching its lightning feature, it's using LDK.
[2512.74 --> 2513.52]  It's using what they do.
[2514.10 --> 2527.64]  So that, I mean, if you're ever into a state where like you can fund open source developers, not just around Bitcoin, but anything, you might get something back that's extremely valuable to your company.
[2527.64 --> 2531.86]  I mean, it would have taken Cash App so much longer if LDK did not exist.
[2532.82 --> 2535.74]  And again, like they weren't building that for Square's interest.
[2535.88 --> 2542.86]  They were building it for like wallet developers that were not Cash App because Cash App had no interest in that time of using lightning.
[2544.70 --> 2547.42]  And I just think that's, I'm really proud of that.
[2547.50 --> 2550.46]  Like it just happened and we didn't force it to happen.
[2550.56 --> 2551.18]  It just happened.
[2551.66 --> 2552.72]  I mean, I think you're an innovator.
[2552.72 --> 2561.30]  And I think that what you've done so far and what you've enabled with the teams you've hired and you've given just flexibility to do fun things, do whatever you want.
[2561.46 --> 2565.36]  And something actually comes out of it is pretty admirable and quite an accomplishment.
[2565.60 --> 2568.60]  So I'm really excited about what happens in this space.
[2569.42 --> 2571.38]  I saw a tweet from you to Cardi B.
[2571.84 --> 2574.94]  She said something like, you know, is Bitcoin going to take over the dollar?
[2575.54 --> 2576.50]  You said, yes, it will.
[2577.06 --> 2579.18]  Is Bitcoin going to replace the US dollar?
[2579.58 --> 2580.64]  Is that something you expect?
[2580.64 --> 2586.96]  I don't think there will ever be a replacement for any of these things, but I do think there will be one that is more dominant.
[2587.84 --> 2601.02]  And I think there's a potential for the, I think there's a very strong potential that the US dollar loses its global singular reserve currency status.
[2601.62 --> 2605.04]  And there may be a second one in the Chinese one.
[2605.70 --> 2608.56]  And there might be a third one in Bitcoin.
[2608.56 --> 2611.58]  And I think that's a net positive.
[2612.42 --> 2625.14]  I'm obviously rooting for Bitcoin because of the properties behind it, because it's transparent, because no company or individual controls it, because no government controls it, because it's resilient.
[2625.44 --> 2625.90]  It's secure.
[2626.06 --> 2626.94]  It's never been hacked.
[2627.82 --> 2629.86]  You know, it's never gone down.
[2629.86 --> 2632.30]  And that's what I want out of my money.
[2632.58 --> 2633.88]  But I want the transparency.
[2634.22 --> 2636.82]  I want it to be owned by the people as well.
[2636.92 --> 2645.06]  So having a world reserve currency that is owned by the people and developed in the way that Bitcoin is developed, I think is very, very powerful.
[2645.06 --> 2655.34]  And I think would be ideal for everyone on the planet not to be controlled by the dominance of any one government's currency.
[2656.28 --> 2663.76]  But I do think that we're moving away from a time when there's one and there will probably be many and then maybe one will become dominant.
[2663.76 --> 2669.24]  That's it for this special episode of Founders Talk.
[2669.24 --> 2674.24]  Thank you so much to Jack Dorsey for having this awesome fireside chat with me as part of Square Unboxed.
[2675.10 --> 2678.94]  And thank you to those behind the scenes at Square making this happen.
[2679.28 --> 2682.36]  Shannon, Mary Elise, Katie, and many others.
[2682.62 --> 2684.58]  It's truly a pleasure working with you.
[2684.92 --> 2690.04]  If you have thoughts about Square, Block, Jack, Bitcoin, whatever, let us know in the comments.
[2690.24 --> 2691.70]  Links are in the show notes.
[2691.70 --> 2695.64]  And, of course, thanks again to our friends and partners at Fastly for having our back.
[2695.84 --> 2697.84]  Check them out at Fastly.com.
[2698.18 --> 2701.02]  And, you know, Breakmaster Zylinder is our beats master in residence.
[2701.62 --> 2702.46]  Thank you, BMC.
[2702.60 --> 2704.94]  Our beats are banging and you are awesome.
[2705.48 --> 2710.18]  Of course, last but not least, thank you to you for listening all the way to the very end.
[2710.40 --> 2713.10]  I appreciate everyone listening to this show all around the world.
[2713.48 --> 2716.52]  If you haven't yet, subscribe at FoundersTalk.fm.
[2716.78 --> 2717.62]  That's it for this week.
[2717.70 --> 2718.64]  Thanks again for tuning in.
[2718.96 --> 2719.72]  We'll see you again soon.
[2721.70 --> 2751.68]  We'll see you again soon.
[2751.70 --> 2766.30]  Today
[2766.30 --> 2768.68]  here
