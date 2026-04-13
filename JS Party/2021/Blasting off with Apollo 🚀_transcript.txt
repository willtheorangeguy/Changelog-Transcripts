[0.00 --> 4.12]  If you're dying to work with like a certain technology, I see nothing wrong with hopping
[4.12 --> 5.50]  to a job that has it.
[5.66 --> 7.06]  I wanted to work with GraphQL.
[7.60 --> 9.22]  So I joined Apollo, right?
[9.24 --> 12.18]  I didn't think I was going to get to use it at any of my other companies.
[12.30 --> 13.24]  Straight from the source.
[13.86 --> 14.22]  Yeah.
[14.72 --> 15.48]  You're like, I'm not messing around.
[15.48 --> 16.58]  Drink it straight from the well.
[16.82 --> 17.78]  Like, just give it to me.
[17.78 --> 19.06]  You know?
[19.58 --> 19.94]  Nice.
[22.34 --> 24.96]  Big thanks to our partners, Linode Fastly and LaunchDarkly.
[25.32 --> 25.88]  We love Linode.
[25.96 --> 27.38]  They keep it fast and simple.
[27.50 --> 29.86]  Check them out at linode.com slash changelog.
[30.16 --> 32.16]  Our bandwidth is provided by Fastly.
[32.50 --> 36.06]  Learn more at Fastly.com and get your feature flags powered by LaunchDarkly.
[36.32 --> 38.06]  Get a demo at LaunchDarkly.com.
[40.98 --> 43.54]  This episode is brought to you by our friends at O'Reilly.
[43.54 --> 47.56]  Many of you know O'Reilly for their animal tech books and their conferences, but you may
[47.56 --> 50.02]  not know they have an online learning platform as well.
[50.40 --> 54.82]  The platform has all their books, all their videos, and all their conference talks.
[55.18 --> 59.38]  Plus, you can learn by doing with live online training courses and virtual conferences,
[59.38 --> 64.90]  certification practice exams, and interactive sandboxes and scenarios to practice coding
[64.90 --> 65.96]  alongside what you're learning.
[65.96 --> 71.80]  They cover a ton of technology topics, machine learning, AI, programming languages, DevOps,
[72.30 --> 78.48]  data science, cloud, containers, security, and even soft skills like business management
[78.48 --> 79.92]  and presentation skills.
[80.04 --> 81.82]  You name it, it is all in there.
[81.82 --> 85.76]  If you need to keep your team or yourself up to speed on their tech skills, then check
[85.76 --> 87.32]  out O'Reilly's online learning platform.
[87.82 --> 91.38]  Learn more and keep your team skills sharp at O'Reilly.com slash changelog.
[91.52 --> 93.78]  Again, O'Reilly.com slash changelog.
[93.78 --> 106.74]  This is JS Party, your weekly celebration of JavaScript and the web.
[106.88 --> 110.88]  If you haven't joined the JS Party community yet, what are you waiting for?
[111.02 --> 115.98]  It's a fun and welcoming place where you can discuss web dev, ask questions, get notified
[115.98 --> 119.38]  of live shows, and help make the podcast even more awesome.
[119.38 --> 123.90]  Just head to jsparty.fm slash community and sign up today.
[124.34 --> 125.54]  Okay, let's get into it.
[125.58 --> 127.12]  Hey, it's party time, y'all.
[137.06 --> 142.16]  Hello, JS Party people, and welcome to this week's JS Party.
[142.36 --> 142.94]  I'm K-Ball.
[143.02 --> 144.60]  I will be your emcee this week.
[144.72 --> 148.38]  I am joined both by some of my favorite panelists.
[148.38 --> 150.72]  They're all my favorites who I have not seen in a little while.
[151.04 --> 154.12]  Let me welcome them first and then introduce you to our amazing guests.
[154.22 --> 156.50]  So first off, welcome, Amel.
[156.86 --> 157.60]  How are you doing?
[158.00 --> 158.58]  Hey, everyone.
[158.92 --> 159.50]  And Feras.
[159.92 --> 162.30]  Long time no see, but I'm so excited to have you on.
[162.54 --> 162.78]  Same.
[163.04 --> 163.72]  Excited to be here.
[163.94 --> 166.64]  Next, let me introduce our guest for the week.
[166.76 --> 170.54]  We have a special guest today introducing Jen Creighton.
[170.68 --> 171.16]  Jen, hello.
[171.58 --> 172.02]  Hi.
[172.26 --> 173.00]  Hi, everyone.
[173.38 --> 174.08]  I'm glad to be here.
[174.30 --> 174.60]  Awesome.
[174.60 --> 179.00]  So let's actually get started a little bit with exploring who you are, Jen.
[179.08 --> 182.18]  Do you want to give us the quick, you know, Jen Creighton in 30 seconds?
[182.44 --> 183.76]  The too long don't read.
[184.22 --> 191.16]  I am a open source engineer at Apollo GraphQL, working very specifically on Apollo Client.
[191.94 --> 194.66]  And that's pretty much my life right now.
[194.76 --> 197.14]  I work in open source and that has consumed me.
[197.32 --> 199.98]  I have pink hair, pretty much enjoying that.
[199.98 --> 205.38]  Oh, and I also run my own podcast called Single Threaded that just wrapped up its first little
[205.38 --> 206.00]  mini season.
[206.38 --> 206.52]  Awesome.
[206.86 --> 207.98]  I love the hair, by the way.
[208.00 --> 208.56]  It looks great.
[208.86 --> 213.90]  And if anybody is listening but not looking, check out the YouTube stream of this.
[214.10 --> 219.84]  You can see it's matching Amel's typical looks, though Amel is not overshadowing Jen today.
[220.06 --> 220.82]  She's got to cover that.
[221.34 --> 221.64]  Awesome.
[221.78 --> 227.04]  So I know a lot of folks are interested in this idea of working in open source.
[227.16 --> 229.62]  Do you want to actually talk a little bit about how you got into that?
[229.62 --> 237.28]  Yes, I kind of fell into it by accident, which is to say that I was already working with open
[237.28 --> 239.08]  source technologies at my job.
[239.64 --> 248.34]  I worked with React for, I don't know, five, six years and started to decide that I wanted
[248.34 --> 254.56]  to speak at events about React and sort of brought myself into open source that way.
[254.72 --> 259.24]  And also occasionally you could like find me in the middle of the night, kind of like scrolling
[259.24 --> 261.98]  through the React code base, trying to understand how things worked.
[262.08 --> 265.52]  I was just curious about what was going on.
[266.12 --> 269.10]  And then Apollo reached out to me with this opportunity.
[269.10 --> 271.24]  And I was like, yeah, getting paid to do open source.
[271.86 --> 273.26]  Okay, yeah, I'm going to try that out.
[273.30 --> 274.64]  I'm going to see what that is like.
[275.08 --> 276.10]  It's a wild ride.
[276.10 --> 281.20]  That's a whole new thing from product engineering.
[281.88 --> 282.90]  Absolutely, absolutely.
[283.08 --> 287.62]  So then in that context, are you primarily doing coding?
[287.76 --> 288.84]  Are you managing community?
[289.00 --> 293.60]  Like I know when I was paid to work on open source, there was like a whole lot of things
[293.60 --> 297.58]  that maybe I hadn't even thought about as part of engineering prior to getting involved.
[297.58 --> 305.88]  My time right now is mostly in the actual code base, looking through issues, checking out
[305.88 --> 310.58]  reproductions, figuring out what we actually should be fixing, which is sometimes not the
[310.58 --> 313.76]  thing that people ask you to do in the issues.
[314.00 --> 316.88]  So those types of things, as well as like working on new features.
[317.38 --> 324.20]  I do some community work still, like I just hosted Apollo GraphQL Summit with my coworker,
[324.28 --> 324.48]  Ellen.
[324.48 --> 332.74]  And we both tag team that and occasionally like in other respects have to do like events
[332.74 --> 337.60]  like that or answer community questions or be available for those types of things.
[337.60 --> 338.86]  So it's a mix of both.
[338.86 --> 343.10]  It's like really daunting, I think, about doing your work in the open.
[343.88 --> 348.38]  And there's also something super liberating at the same time, you know, because it's like,
[348.88 --> 350.82]  hey, you know, nothing to forget.
[350.82 --> 356.38]  But there's this trail of easy access, I think, which, you know, is very liberating and can
[356.38 --> 359.46]  be very productive because you're able to like work with people across lots of different
[359.46 --> 359.86]  boundaries.
[360.40 --> 365.88]  But yeah, I mean, the transition of I think doing open source work, you know, full time,
[365.98 --> 367.68]  that's got to be pretty, pretty fun.
[367.90 --> 370.34]  Yeah, there's no hiding your code.
[370.76 --> 374.14]  Like if you really want someone not to see it, you can't push it up.
[374.26 --> 375.18]  I think that's the rule.
[375.72 --> 378.04]  If you're not ready for anyone to look at it, don't push it up.
[378.04 --> 379.46]  But like, that's all you got.
[379.72 --> 380.00]  Absolutely.
[380.22 --> 383.06]  For us, you've done a lot of your work in the open source world as well, right?
[383.50 --> 383.70]  Mm hmm.
[384.58 --> 384.84]  Yep.
[385.08 --> 388.08]  Pretty much most of my code is is online.
[388.56 --> 390.22]  And I remember feeling the same way at first.
[390.68 --> 394.02]  Actually, I remember getting interested in open source also kind of in a similar vein
[394.02 --> 398.06]  to Jen with but it was jQuery that I got really interested in.
[398.06 --> 405.82]  And I like remember watching some videos on YouTube where Paul Irish was explaining things
[405.82 --> 408.52]  that he learned from reading the jQuery code base.
[409.24 --> 413.52]  And I remember after I saw that, I was like, wow, this is like peeling behind, you know,
[413.58 --> 415.34]  like to see how the sausage is made.
[415.38 --> 416.16]  And it was really cool.
[416.34 --> 420.46]  And then I wanted to be, you know, cool enough to to do open source, too.
[420.72 --> 423.20]  That was kind of how how I got started.
[423.26 --> 425.66]  So it's it totally sounds familiar.
[425.66 --> 431.40]  Oh, yeah, I actually remember Paul Irish, like going through the jQuery source code
[431.40 --> 433.82]  and explaining why things work the way they did.
[433.94 --> 435.24]  And that was really cool.
[435.60 --> 437.08]  Yeah, so many browser hacks.
[437.38 --> 439.36]  And like, but there was like a reason for everything.
[439.36 --> 445.26]  It was like nice to actually know why you were seeing all these like arcane spells kind of
[445.26 --> 446.82]  yeah, just explaining how the stuff works.
[446.96 --> 447.96]  That's a random tangent.
[447.96 --> 450.18]  But I love the metaphor of software is magic.
[450.18 --> 455.18]  You know, it's it's got all of the same things of like bizarre incantations,
[455.18 --> 458.54]  very strange lines between what is easy and what is hard.
[458.80 --> 463.68]  And like, I don't know, the only question in my mind is, is it better represented as black
[463.68 --> 465.98]  magic or just magic in general?
[465.98 --> 472.90]  I think of it as there's some shows that have magic in them, but they take a scientific
[472.90 --> 478.62]  approach to it where they're like, actually, this is all about just manipulating like molecules
[478.62 --> 480.94]  depending on like how you do X, Y, and Z.
[481.18 --> 487.18]  So it's not magic in this like sense of like an unknown, how it's working, you actually do
[487.18 --> 488.02]  know how it's working.
[488.64 --> 491.10]  And that is like really close to like code.
[491.20 --> 495.64]  Because if you really fundamentally like break it down to the smallest possible unit, you're
[495.64 --> 497.28]  going to figure out like how the code works.
[497.28 --> 500.40]  It's not ultimately like something you can't understand.
[500.62 --> 502.32]  But yeah, I love code as magic, too.
[502.80 --> 503.18]  Totally agree.
[503.18 --> 508.14]  The best magic systems have their internal logic, and it's totally sealed up and it works
[508.14 --> 511.46]  and is bizarre if you don't understand that internal.
[512.24 --> 516.72]  One thing I've learned from peering through the React code base is a lot about scheduling,
[517.38 --> 517.60]  you know?
[517.66 --> 521.80]  So I think it's interesting how like different libraries, like they have their own little
[521.80 --> 523.72]  hard problems that they're trying to solve.
[523.80 --> 528.14]  And it's like, you really want to learn about complex scheduling with just JavaScript.
[528.14 --> 536.48]  You know, go look in the React code base, you know, lots of, you know, request idle callbacks
[536.48 --> 540.18]  and more, you know, so it's fun.
[540.56 --> 546.20]  So let's move a little bit more into specifically Apollo, because it's something that I know,
[546.28 --> 549.50]  you know, GraphQL in general has exploded in popularity.
[549.60 --> 551.78]  And it's something we've talked about a little bit here.
[552.18 --> 556.30]  Apollo seems to be the front runner of that movement in a lot of ways, but I don't think
[556.30 --> 557.34]  we've dug deep into it.
[557.34 --> 562.36]  So can you kind of flesh out for us, just starting with like, what is Apollo?
[562.50 --> 566.42]  Like when you say, I work in Apollo, like there's so many things that could mean.
[566.74 --> 567.90]  What do you think of?
[568.14 --> 568.26]  Right.
[568.54 --> 575.26]  I mean, for me, I tend to like, if I'm talking to an engineer, I caveat with like, I work on
[575.26 --> 576.36]  Apollo client.
[576.54 --> 579.88]  So I work on like the web caching system.
[579.88 --> 581.12]  Like that's what I work on.
[581.38 --> 585.34]  Because there are so many different things that Apollo does in this space.
[585.34 --> 593.42]  Like from your server to your client to the paid products that we offer for you to handle
[593.42 --> 595.64]  your schema and federation.
[596.04 --> 598.80]  There's just a whole host of things that we do.
[598.90 --> 603.06]  We just like our like a full service, like GraphQL, like front runner.
[603.28 --> 608.46]  If you're working with GraphQL and you want to make it like easy on your engineers, you tend
[608.46 --> 609.24]  to go with Apollo.
[609.24 --> 610.04]  That makes sense.
[610.10 --> 612.80]  So you're involved specifically with the client.
[613.28 --> 613.54]  Yes.
[613.78 --> 617.24]  And is that co-owned with the dev tools or those are separate?
[617.50 --> 620.16]  When you say the dev tools, do you mean the Chrome extension?
[620.56 --> 620.72]  Yeah.
[620.94 --> 621.20]  Yeah.
[621.34 --> 627.24]  My first project at Apollo was to completely rewrite those dev tools, which I had never
[627.24 --> 631.18]  written a Chrome browser extension before.
[631.18 --> 633.58]  And, oh, that's not fun.
[633.96 --> 635.16]  That's not a fun time.
[635.40 --> 638.08]  That's a system that feels terrible to work in.
[638.36 --> 639.82]  Do you want to expound on that a little bit?
[641.68 --> 647.64]  Because I mean, both the beauty and the pain of browser extensions today is they're all web
[647.64 --> 648.28]  technologies.
[648.58 --> 648.80]  Right.
[649.18 --> 653.08]  But with obscure APIs and permissions that you have to have in mind.
[653.08 --> 653.76]  Yeah.
[653.94 --> 659.52]  So ultimately, if you're using the dev tools, which are on Chrome and Firefox, you're ultimately
[659.52 --> 661.54]  using a React application.
[661.78 --> 665.10]  Like that's all built as a simple React web application.
[665.80 --> 669.92]  What's not simple about working with the browser extension is that you're dealing with
[669.92 --> 671.18]  sandboxed environments.
[672.04 --> 673.78]  And this makes sense for security reasons.
[673.78 --> 677.46]  You can't just run any code you want on anyone's web page.
[677.56 --> 681.24]  That's obviously very clearly a security concern.
[681.24 --> 686.46]  So they sandbox all the environments and you have to push messages back and forth using
[686.46 --> 694.38]  their API, which is not well documented, sometimes documented erroneously.
[695.16 --> 698.04]  Sometimes they just straight up tell you things are available when they are not.
[698.58 --> 702.50]  And you have to get, like you said, specific permissions to use specific things.
[702.90 --> 708.48]  So if you want to interact with the tab system, you have to kind of put that on a list of saying,
[708.48 --> 711.88]  I want to use the tab system and then you can use it.
[712.04 --> 715.62]  And then like Chrome extensions always go through like a review process.
[715.84 --> 718.66]  So it's like a very laborious process.
[719.18 --> 724.92]  And you're just trying to deal with like passaging like messages back and forth all over the place.
[725.22 --> 726.22]  It's kind of a nightmare.
[726.46 --> 732.56]  Also, like once you get the thing like actually working, that doesn't mean that it's going to
[732.56 --> 737.76]  work on everyone's browser with everyone's like system because you just never know what
[737.76 --> 740.18]  they're dealing with on their end of their setup.
[740.38 --> 743.86]  And so we just get like a lot of issues that are like, well, this doesn't work.
[744.10 --> 748.32]  I need to know a little bit more about your setup to fix that for you.
[748.80 --> 749.96]  I will fix it for you.
[750.08 --> 752.40]  But you've got to tell me more than it just doesn't work.
[752.40 --> 759.44]  I feel like anytime software at scale is outside of the standards process, you know, just gets
[759.44 --> 761.10]  into this, I don't know, weird world.
[761.42 --> 768.68]  But I feel like browser extensions are so due for just better standardization so that so
[768.68 --> 770.02]  developers don't go insane.
[770.44 --> 772.20]  Oh, but it's so much better than it used to be.
[772.28 --> 772.50]  Yeah.
[772.90 --> 773.72]  I believe you.
[773.72 --> 779.44]  Like the Chrome extensions were just this massive step forward from back when like you
[779.44 --> 784.08]  Firefox extensions where you're coding stuff in like XML things and.
[784.54 --> 785.06]  Oh, my God.
[785.14 --> 787.28]  Yeah, it was a disaster.
[787.60 --> 791.10]  But yeah, I do recall it's been a few years, so it may have changed.
[791.18 --> 795.64]  But I do recall build spending a very large amount of the time I spent on browser extensions
[795.64 --> 800.56]  in building abstraction layers on top of the message passing so that I could deal with all
[800.56 --> 805.84]  the different various ways that that interacted with permissions and was different in different
[805.84 --> 806.22]  ways.
[806.34 --> 810.22]  Yeah, that was the first thing I had to do was I had to like build an abstraction that
[810.22 --> 814.76]  was going to clean up when messages were being passed and what they were being passed to.
[815.32 --> 823.16]  And there's some historical way that you build certain things in the extensions where they call
[823.16 --> 824.76]  things a background page.
[825.24 --> 829.34]  But also you would have like these aren't in the docs, by the way, it's just like a back
[829.34 --> 831.54]  end system that's not a back end.
[831.80 --> 833.88]  And it never made sense.
[834.08 --> 839.20]  And so I just kind of redid it all so that like older structures actually, as it turns
[839.20 --> 840.32]  out, like kind of matter.
[840.52 --> 845.02]  And so putting everything that actually lives in the tab space under the tab folder actually
[845.02 --> 848.46]  makes sense as opposed to everything that lives in the dev tools space, as opposed to
[848.46 --> 849.98]  everything that actually does live in the background.
[849.98 --> 853.28]  Like turns out that's helpful for your mental model.
[859.34 --> 875.22]  What up party people?
[875.34 --> 879.24]  If you want to know what's happening with your code, track errors and monitor your app's performance
[879.24 --> 879.92]  with Sentry.
[880.30 --> 884.00]  Build better software faster with Sentry's application monitoring platform.
[884.00 --> 888.02]  Diagnose, fix, and optimize the performance of your code.
[888.36 --> 891.26]  Cut your time on error resolution from hours to minutes.
[891.58 --> 894.66]  It works with any language and integrates with dozens of services.
[895.10 --> 899.14]  Over 1 million developers and 68,000 organizations already use Sentry.
[899.48 --> 903.28]  And best of all, JS Party listeners new to Sentry get the team plan for free for three months.
[903.28 --> 907.26]  Head to Sentry.io to get started and use the code PARTYTIME when you sign up.
[907.48 --> 912.50]  Again, Sentry.io and use the code PARTYTIME because, hey, it's PARTYTIME, y'all.
[914.00 --> 943.86]  So let's hop back into things.
[944.00 --> 946.02]  And talk about Apollo Client.
[946.52 --> 950.32]  Jen, can you explain a little bit, like, what is the role that the client plays?
[950.38 --> 954.32]  If I'm somebody coming in who doesn't know anything about the GraphQL ecosystem, like,
[954.42 --> 957.86]  where should I put this in my mental map of how I'm going to start using this thing?
[957.86 --> 965.58]  If you've ever built application with React and Redux, you would swap out Redux for Apollo
[965.58 --> 967.68]  Client when you're working with GraphQL.
[967.68 --> 975.90]  Apollo Client is just made to work with caching your GraphQL responses on the front end and allowing
[975.90 --> 978.70]  you to do things on the front end with those GraphQL responses.
[979.06 --> 983.70]  That would be really difficult for you to do with another library.
[983.70 --> 990.26]  Because your data is now in a graph model, you actually need a caching strategy that understands
[990.26 --> 993.08]  that it's a graph model and how to store those things properly.
[993.26 --> 994.18]  So that's what we do.
[994.34 --> 994.54]  Got it.
[994.60 --> 998.54]  Well, and that actually fits, interestingly, with this idea of GraphQL as an evolution of
[998.54 --> 999.22]  state management.
[1000.08 --> 1003.58]  It's kind of like, on the front end, we've gone through this evolution of how we think about
[1003.58 --> 1009.00]  state and looking at state in terms of, you know, does it make sense to be down in the
[1009.00 --> 1012.62]  component versus some sort of centralized state manager and all these different pieces.
[1012.80 --> 1018.08]  And GraphQL, in some ways, is like, or at least I think of it as extending that state
[1018.08 --> 1023.68]  model in a way that sort of maps to our back end representation a little bit more.
[1024.28 --> 1028.86]  So that we've got a unified state model for the communication between back end and front
[1028.86 --> 1029.02]  end.
[1029.20 --> 1031.64]  We don't have to do that mapping all in our front end.
[1031.64 --> 1033.44]  See if anyone else wants to jump in.
[1033.52 --> 1034.60]  You can also ask questions.
[1034.90 --> 1035.06]  Yeah.
[1035.22 --> 1040.82]  There's this shift, I think, that was made with GraphQL that I consider it to be like
[1040.82 --> 1045.18]  very much of a milestone, noteworthy kind of shift, right?
[1045.20 --> 1046.86]  It's pretty pivotal, right?
[1046.90 --> 1048.04]  Where folks were like, you know what?
[1048.12 --> 1049.40]  Rest, like we're done with you.
[1049.82 --> 1051.42]  You don't actually work for the new world.
[1051.94 --> 1056.88]  You know, these like tiny devices and like all these different screens and contexts that we
[1056.88 --> 1057.58]  need to support.
[1057.58 --> 1062.56]  We're like, you know, can't be making all these API calls to stitch this data together
[1062.56 --> 1063.68]  in my clients.
[1063.90 --> 1067.90]  And I can't support different versions of APIs for mobile, you know?
[1068.08 --> 1070.10]  Like been really interesting to watch that shift.
[1070.10 --> 1075.60]  And then I think like to see this evolution with Apollo and like the services around this
[1075.60 --> 1076.20]  like world.
[1076.20 --> 1081.90]  What's it like to like have this kind of open source standard and really kind of be this
[1081.90 --> 1086.32]  like lead, you know, the lead implementation of the standard.
[1086.50 --> 1091.02]  But y'all are doing so much more than just, you know, providing clients.
[1091.02 --> 1092.54]  It's just like a full service.
[1092.92 --> 1093.86]  There's a lot to manage.
[1093.86 --> 1099.02]  Like I'm curious, what's that like that ecosystem of Apollo things that's growing?
[1099.02 --> 1104.88]  It's really interesting because you could see it as the leaders of Apollo sort of saw
[1104.88 --> 1108.78]  that GraphQL was a good use case and they should jump on board and create some things
[1108.78 --> 1110.62]  around it and build a company about it.
[1111.34 --> 1115.84]  But the truth is like at the very, very top, they just very deeply believe that GraphQL
[1115.84 --> 1118.26]  is a really great technology.
[1118.46 --> 1124.92]  And they wanted to make working with it something that companies could adopt more easily.
[1124.92 --> 1131.42]  GraphQL, while it is very popular in concept, isn't actually adopted in a lot of places yet.
[1131.56 --> 1133.70]  A lot of places are still using REST APIs.
[1133.98 --> 1137.38]  And in some cases, that's like what you should be doing.
[1137.48 --> 1138.14]  That's fine.
[1138.62 --> 1144.62]  But if your data actually needs to act as a graph, you are well served by GraphQL for obvious
[1144.62 --> 1151.32]  reasons, as well as if you have this problem that you just mentioned of your clients needing
[1151.32 --> 1157.72]  different things at different times, turns out being able to push that onto the client
[1157.72 --> 1162.56]  team to decide what they're actually going to pull out of your graph is a really great
[1162.56 --> 1168.94]  idea and really helpful and really lovely to work with, as well as a strong typing system,
[1168.94 --> 1172.80]  as well as just like looking more declarative in what you're getting.
[1173.10 --> 1178.70]  My biggest pain as a front-end engineer was always figuring out what the REST API was actually
[1178.70 --> 1180.88]  doing and why it was giving me things.
[1181.46 --> 1184.74]  And with GraphQL, you can even just like say like, hey, by the way, this field's deprecated.
[1185.18 --> 1190.02]  Like that's a wild concept to me as a front-end engineer that I could like be like, oh, I can
[1190.02 --> 1193.66]  look at this and just tell that it's deprecated instead of a back-end engineer being like, oh,
[1193.68 --> 1194.92]  no, you don't want to use that.
[1195.00 --> 1199.14]  You actually want to use this other thing that we added later, which almost always happens.
[1199.42 --> 1202.42]  And your tooling can tell you because it's declared.
[1202.42 --> 1202.90]  Yes.
[1204.02 --> 1208.58]  There's so much tooling you can do with GraphQL that it's just amazing.
[1209.38 --> 1215.60]  So it's a space that's like very sort of rapidly evolving at Apollo about what we want to push
[1215.60 --> 1220.64]  the graph to do, what we want companies to be able to do with their graph.
[1220.76 --> 1223.98]  You get into this with Apollo Federation, which we can definitely talk about.
[1224.04 --> 1224.80]  It's very cool.
[1225.40 --> 1231.06]  And being at like a company that's at the forefront of that, you were on just like a wild roller
[1231.06 --> 1231.74]  coaster ride.
[1231.84 --> 1233.76]  It's like, you're just learning a lot.
[1234.40 --> 1239.18]  I've learned so much in the past year at Apollo because to be honest, I wasn't working with
[1239.18 --> 1240.46]  GraphQL before I joined the company.
[1240.92 --> 1244.34]  And I had to really amp up all my knowledge about this in a year.
[1244.74 --> 1248.16]  And still every day someone says something else that I'm like, oh, what?
[1248.54 --> 1248.98]  What are we doing?
[1249.20 --> 1249.84]  Why are we doing it?
[1249.98 --> 1250.32]  Oh my God.
[1250.44 --> 1250.60]  What?
[1250.80 --> 1251.34]  You can do that?
[1251.80 --> 1252.08]  It's great.
[1252.08 --> 1256.30]  You're like the second person I know who's joined Apollo in the past year who didn't really
[1256.30 --> 1257.00]  use GraphQL.
[1257.00 --> 1262.12]  Well, like it's a trend that I think, you know, I love it that they're like recruiting
[1262.12 --> 1266.48]  folks that are like, you know, not necessarily users.
[1266.68 --> 1270.76]  Well, like I said, it's like popular in concept, but not fully adopted.
[1270.92 --> 1275.24]  So if we didn't, we would be limiting our hiring pool, right?
[1275.60 --> 1276.80]  You would not have hired me.
[1277.14 --> 1278.80]  I'm a pretty damn good engineer.
[1279.08 --> 1281.68]  Like that would have been a bad idea.
[1281.76 --> 1283.82]  I can learn things like you can learn GraphQL.
[1283.96 --> 1284.30]  It's cool.
[1284.66 --> 1285.42]  You can learn on the job.
[1285.42 --> 1288.16]  You're like, you're literally surrounded by experts at Apollo.
[1288.32 --> 1291.50]  So it's just like, you can't help but learn it by osmosis even.
[1291.90 --> 1292.90]  So I have a question about that.
[1293.02 --> 1298.58]  The part about it being popular in concept, but less so in practice.
[1298.98 --> 1301.00]  So why do you think that is?
[1301.40 --> 1305.38]  And related to that, I guess I started a company recently and it's just me and one other engineer
[1305.38 --> 1305.90]  right now.
[1306.42 --> 1310.68]  And I'm wondering if like, it's too early for us to use something like GraphQL.
[1311.28 --> 1314.36]  It sounds like the benefits are like coordination between different teams.
[1314.36 --> 1316.74]  And like right now we don't really have different teams.
[1316.86 --> 1319.32]  We just have the team of the two of us.
[1319.80 --> 1320.00]  So yeah.
[1320.00 --> 1324.36]  Is it like a thing that you actually see people using from the very beginning of their project?
[1324.58 --> 1328.02]  I mean, I might imagine some people are, but like, is that advisable?
[1328.22 --> 1332.72]  Is there, is there a lot of overhead or boilerplate, like extra things you need to do over like what
[1332.72 --> 1339.02]  you would need to do to just, you know, quickly write like an express route for a rest endpoint,
[1339.22 --> 1340.56]  you know, that you can do in a couple of lines?
[1340.68 --> 1344.92]  Is that the reason why you think it's more that people like the idea or like, what are
[1344.92 --> 1345.68]  your thoughts?
[1346.10 --> 1350.10]  So GraphQL isn't like the newest thing on the block, right?
[1350.16 --> 1351.20]  But it is newer.
[1351.20 --> 1357.22]  And so people are still actually grasping the concept of like what GraphQL actually is.
[1357.32 --> 1362.56]  And I remember when I learned about it the first time, I really didn't truly understand
[1362.56 --> 1363.44]  what was going on.
[1363.50 --> 1366.60]  It just seemed like going back to an earlier conversation, just magic.
[1366.60 --> 1371.18]  And I didn't understand what was under the hood that was making it kind of work together.
[1371.70 --> 1375.24]  And I was like, people just keep telling me, oh, you just use GraphQL and you can grab
[1375.24 --> 1375.76]  whatever you want.
[1375.82 --> 1376.56]  I was like, but how?
[1376.92 --> 1377.48]  Please tell me.
[1377.48 --> 1380.94]  Now that I have like a better conceptual like model about it that's different.
[1381.06 --> 1385.62]  So one, like just wrapping your brain around like how different this is from hitting your
[1385.62 --> 1386.78]  REST APIs.
[1387.10 --> 1390.96]  And then two, like, have you ever tried to make like a change at an org after things had
[1390.96 --> 1391.30]  been built?
[1391.40 --> 1392.22]  Like it's hard.
[1392.76 --> 1398.64]  So if GraphQL is like of interest to you, and I worked at multiple companies that the
[1398.64 --> 1405.52]  engineering team wanted to adopt GraphQL, but figuring out how to do it and how to get
[1405.52 --> 1410.04]  everyone on board with what we were going to do was really difficult.
[1410.60 --> 1412.58]  And that was at a startup size.
[1412.64 --> 1416.84]  So I imagine at a larger org, it's even more difficult to do.
[1417.22 --> 1422.22]  I would say if you want to like spin up an express API real quick and have some data versus
[1422.22 --> 1423.46]  like invest in GraphQL.
[1424.10 --> 1425.02]  Okay, that's fine.
[1425.26 --> 1425.82]  Like, it's cool.
[1425.94 --> 1428.04]  It really just depends on your trade-offs.
[1428.16 --> 1432.82]  And if you early on have like a really great use case for the fact that your data is going
[1432.82 --> 1437.38]  to be really graph heavy, yeah, you probably should just go ahead and early.
[1437.48 --> 1441.42]  But if you don't, okay, build your express API.
[1441.62 --> 1445.56]  Maybe try out like GraphQL at some point and see if it like gives you anything that you really
[1445.56 --> 1445.90]  want.
[1445.98 --> 1448.26]  I mean, it does have like some really nice features to it.
[1448.34 --> 1453.32]  But by no means does everyone have to like adopt GraphQL at all times.
[1453.32 --> 1456.52]  Like not even I think other people at Apollo like believe this.
[1456.80 --> 1461.48]  To jump in a little bit on some of those trade-offs, some of the things that we found at
[1461.48 --> 1465.46]  Humu where I'm working where we are using GraphQL, but we do have some REST endpoints
[1465.46 --> 1465.90]  as well.
[1466.42 --> 1472.52]  So on the drawback side, partly because of our setup, but partly also just because of
[1472.52 --> 1474.56]  how GraphQL is, there's more boilerplate to set up.
[1474.76 --> 1476.48]  There's more things that you have to declare.
[1476.62 --> 1477.96]  There's more stuff that you put out there.
[1478.42 --> 1482.38]  And so if you're setting something up quick and dirty, you're setting things up like it
[1482.38 --> 1484.50]  is more work to set up the GraphQL side of it.
[1484.50 --> 1489.88]  That being said, some of the things you get from it are one, you get end-to-end typing,
[1490.22 --> 1495.86]  which if you're working all in TypeScript front to back, you may already have some of
[1495.86 --> 1496.12]  that.
[1496.28 --> 1500.20]  We have Python on our back end and TypeScript on the front end.
[1500.28 --> 1505.10]  And so having end-to-end typing across languages in that way, just out of the box is beautiful
[1505.10 --> 1506.74]  and works really well.
[1506.98 --> 1512.32]  Another thing that you get that I didn't really appreciate until it had shown up a time or two
[1512.32 --> 1516.64]  is how reusable it makes the APIs that you build.
[1517.32 --> 1522.38]  I used to actually think REST APIs, if you do them really well, they're reusable too.
[1523.24 --> 1527.50]  And that turns out to not actually be as true as I thought it was.
[1527.78 --> 1534.72]  And in the sense that usually when you start using a REST API in a new situation, especially
[1534.72 --> 1538.06]  if you're developing it fast, like you didn't do a big, long API design, but you're just
[1538.06 --> 1538.84]  developing fast.
[1538.98 --> 1542.22]  You're going to have to come back and rethink about how you set it up so that you can
[1542.22 --> 1544.80]  it now works properly in all of your situations.
[1545.50 --> 1550.00]  Whereas with GraphQL, that's what some of that boilerplate is doing is you're declaring
[1550.00 --> 1555.84]  exactly what there is up front and people can pick and choose, oh, I want this piece of
[1555.84 --> 1555.94]  it.
[1555.98 --> 1556.80]  I want that piece of it.
[1556.86 --> 1557.52]  I want to do this.
[1557.66 --> 1562.74]  And so I've found that even though conceptually REST APIs seem to be like they should be as
[1562.74 --> 1568.34]  reusable, practically speaking, anytime we've built it in GraphQL, it ends up being far easier
[1568.34 --> 1571.30]  to reuse in new ways in our front end.
[1571.62 --> 1572.16]  Yeah, definitely.
[1572.16 --> 1576.54]  When you're setting up GraphQL, the thing you have to do that you can just kind of like
[1576.54 --> 1580.52]  wild, wild west with other things is like you have to design a schema.
[1580.94 --> 1584.60]  You have to actually design a schema and tell like what's available.
[1584.60 --> 1587.76]  And schema designs like its own whole thing.
[1587.88 --> 1592.48]  But I think you get a lot of value out of it because it is also besides the typings, it's
[1592.48 --> 1595.54]  like documentation being written for you.
[1595.86 --> 1600.76]  That other words, you would have to do extra work to be documenting these things and keeping
[1600.76 --> 1601.52]  them up to date.
[1601.80 --> 1604.06]  You don't have that issue with GraphQL.
[1604.48 --> 1606.58]  Your schema keeps everything up to date for you.
[1606.86 --> 1606.88]  Yeah.
[1606.94 --> 1610.70]  And you can start reusing those types that you've created in other places, right?
[1610.70 --> 1615.58]  If it's an entity in your system by putting it in a GraphQL schema, now it's an entity
[1615.58 --> 1616.28]  in your API.
[1616.46 --> 1621.68]  And if you want to have a new entity that happens to reference this old entity, it's super easy
[1621.68 --> 1622.06]  to do.
[1622.32 --> 1625.94]  Yeah, I have to say the TypeScript GraphQL story is pretty beautiful.
[1626.28 --> 1629.38]  And I'm saying that as somebody who's still a little grumpy about TypeScript.
[1629.76 --> 1631.84]  So that's a lot coming from me.
[1631.96 --> 1632.28]  I know.
[1632.48 --> 1632.88]  I know.
[1633.02 --> 1633.30]  Same.
[1633.74 --> 1639.18]  But I would say like, you know, on the GraphQL piece, I think my kind of critique,
[1639.18 --> 1643.84]  and this isn't like specific critique of the tool, it's more kind of maybe of the
[1643.84 --> 1645.56]  hive culture around JavaScript.
[1645.92 --> 1650.36]  It's, you know, you see folks needing to like, there's kind of misconception around
[1650.36 --> 1652.16]  like basic stack, right?
[1652.20 --> 1656.44]  And like, I would say GraphQL definitely is not part of your basic stack, right?
[1656.46 --> 1661.52]  Like it's very much a conscious decision that you bring into your application because you
[1661.52 --> 1664.74]  have a use case for it, you know, and it solves a problem for you.
[1664.74 --> 1669.10]  And one of the things that, you know, you just, there's a lot of hidden cost and maintenance,
[1669.32 --> 1672.32]  you know, with adopting every new tool, but especially GraphQL, right?
[1672.42 --> 1677.72]  So the hype thing is what's weird for me, because you see people using it to power their blogs
[1677.72 --> 1681.80]  or very, very simple websites with, you know, just, you know, you're putting it in front
[1681.80 --> 1683.20]  of like one or two REST APIs.
[1683.20 --> 1685.26]  And like, is that really necessary?
[1685.58 --> 1690.48]  You know, so just weigh your trade-offs, kids, you know, before adopting.
[1690.48 --> 1693.04]  That's all like, you know.
[1693.22 --> 1700.24]  That is also like 100% how I feel about TypeScript or people using React for something that like,
[1700.34 --> 1704.52]  I'm like, but you could have just written the HTML yourself.
[1704.84 --> 1706.52]  Why are you doing this?
[1706.58 --> 1709.78]  Or basic templating, like language or something.
[1710.26 --> 1711.34]  Yeah, I'm with you.
[1711.52 --> 1715.08]  I mean, you know, I think, you know, we have a lot of biases engineers and that bias tends
[1715.08 --> 1719.20]  to skew towards over-engineering and, you know.
[1719.34 --> 1719.96]  And shiny.
[1720.20 --> 1721.66]  And shiny new, right.
[1722.40 --> 1722.60]  Yeah.
[1722.74 --> 1723.12]  We love it.
[1723.14 --> 1726.60]  We're all raccoons going towards shiny new things.
[1726.62 --> 1730.46]  But if only we could get that fix out of the way somewhere safe, you know, like there's
[1730.46 --> 1734.02]  these shopping websites where, you know, you can put a bunch of stuff in your cart and
[1734.02 --> 1738.60]  then like even put in like a fake or real credit card and then, you know, it goes nowhere.
[1739.12 --> 1740.88]  You know, if only we had that equivalent.
[1740.88 --> 1748.78]  I do believe that's what they use the side projects for these days.
[1748.80 --> 1749.32]  Oh, yeah, yeah.
[1749.36 --> 1753.68]  I was going to say, I was going to say, I thought that was what engineering blogs are
[1753.68 --> 1753.94]  for.
[1754.12 --> 1754.90]  Yeah, that's true.
[1755.76 --> 1758.96]  Nick's blog that he keeps rebuilding and rebuilding and never publishing.
[1759.26 --> 1759.48]  Right.
[1759.68 --> 1761.22]  That's totally fair, you know.
[1761.34 --> 1765.48]  So just side project your fix for complexity.
[1765.80 --> 1770.12]  Or like if you're dying to work with like a certain technology, I see nothing wrong with
[1770.12 --> 1772.08]  like hop into a job that has it.
[1772.28 --> 1774.72]  Like I wanted to work with GraphQL.
[1775.50 --> 1777.64]  Like so I joined Apollo, right?
[1777.66 --> 1780.60]  I didn't think I was going to get to use it at any of my other companies.
[1780.92 --> 1781.66]  Straight from the source.
[1782.30 --> 1782.62]  Yeah.
[1783.14 --> 1784.26]  You're like, I'm not messing around.
[1784.28 --> 1784.98]  Drink it straight from the well.
[1785.24 --> 1786.22]  Like just give it to me.
[1787.10 --> 1787.48]  You know?
[1788.04 --> 1788.40]  Nice.
[1788.82 --> 1791.78]  I want to learn the thing from the thing maker, you know?
[1794.28 --> 1794.64]  Yeah.
[1794.90 --> 1795.24]  That's cool.
[1795.24 --> 1798.46]  So for us, do you want to throw GraphQL in front of like a node library?
[1798.78 --> 1803.76]  Do you want to like figure out a way to incorporate GraphQL into something that's totally pure
[1803.76 --> 1804.16]  JavaScript?
[1805.16 --> 1806.34]  Doesn't need a backend.
[1808.10 --> 1808.66]  It's a joke.
[1809.00 --> 1809.40]  Yeah, no.
[1810.28 --> 1811.16]  It's a joke.
[1811.28 --> 1811.42]  Yeah.
[1811.50 --> 1812.02]  But yeah.
[1812.22 --> 1812.50]  Yeah.
[1812.94 --> 1817.32]  I think I like the discussion about where it's appropriate because that often is a thing
[1817.32 --> 1822.80]  people don't really sit down and think about before just pulling in, you know, just pulling
[1822.80 --> 1823.72]  in a thousand packages.
[1824.20 --> 1825.44]  So totally makes sense.
[1825.66 --> 1828.60]  I think it so might be a little too early for us to look at.
[1828.70 --> 1832.84]  And our APIs are, I mean, we have like six endpoints right now.
[1832.90 --> 1835.58]  It's like in one table, one database table.
[1835.72 --> 1837.06]  It's like maybe a little early.
[1837.48 --> 1841.62]  I think maybe when we can start to have different clients consuming it and things like that,
[1841.72 --> 1843.48]  that it could make sense.
[1844.34 --> 1847.52]  Speaking as someone who's never used it before, one thing that I'm also kind of curious about
[1847.52 --> 1851.98]  is the, like the need, why is there a need for this schema layer?
[1852.16 --> 1856.10]  Like, I guess this is turning into like me, like asking all my GraphQL questions.
[1856.22 --> 1858.08]  Maybe we don't have to do this, but yeah.
[1858.10 --> 1860.70]  And I'm just curious, like, is there any way to infer it from the database?
[1860.70 --> 1865.62]  It seems like I've already gone out of my way to sort of explain like this table has a
[1865.62 --> 1868.30]  foreign key that references this column in this other table.
[1868.30 --> 1871.84]  And I've already expressed the types in the columns of the database.
[1872.06 --> 1873.50]  I've seen libraries that will do that.
[1873.62 --> 1873.88]  Oh, really?
[1874.00 --> 1874.16]  Okay.
[1874.28 --> 1874.82]  So it depends.
[1874.92 --> 1875.64]  That makes a lot of sense.
[1875.64 --> 1880.52]  If you want to directly expose your database schema to your front end, which is a question
[1880.52 --> 1881.12]  for you, right?
[1881.20 --> 1882.72]  Maybe you do, maybe you don't.
[1882.80 --> 1882.96]  Yeah.
[1883.10 --> 1887.20]  For a lot of sites that have just like most of the content is public and you're just sort
[1887.20 --> 1891.78]  of like letting the client query it, then it seems like that could be a good starting
[1891.78 --> 1892.18]  place.
[1892.18 --> 1898.16]  Like generate a schema from it and then maybe go in and tweak like hiding certain fields,
[1898.30 --> 1900.14]  but like could be a good starting place.
[1900.32 --> 1900.40]  Yeah.
[1900.42 --> 1903.86]  When we're talking about the tooling that can be done, like that's part of it.
[1903.86 --> 1909.26]  You can generate a schema from things, which is very useful, right?
[1909.26 --> 1915.50]  The other part of the schema though is that you may not be getting your data straight from
[1915.50 --> 1916.06]  a database.
[1916.50 --> 1918.80]  You might be getting it from somewhere else.
[1919.44 --> 1923.34]  So GraphQL is really agnostic about where you're getting it from, but it does need to
[1923.34 --> 1924.36]  know what it's getting.
[1924.90 --> 1929.20]  And that is then provided to anyone who wants to use your GraphQL endpoint.
[1929.20 --> 1935.90]  So it is important, I think, to have that schema layer and have it not have to be hooked into
[1935.90 --> 1937.18]  something specific like a database.
[1937.18 --> 1939.40]  It can just be generated somewhere else.
[1939.56 --> 1940.06]  But yeah.
[1940.52 --> 1945.74]  One really nice feature of that is you can have sort of computed fields essentially in
[1945.74 --> 1946.18]  your schema.
[1946.70 --> 1951.04]  And some of them may be quite expensive to compute, but you only have to compute them when
[1951.04 --> 1951.82]  someone requests them.
[1951.82 --> 1955.70]  There's also the layer to like annotate the schema.
[1956.08 --> 1961.18]  So being able to annotate that a field was deprecated or something else about it is useful
[1961.18 --> 1964.74]  as well, which you wouldn't get from just a straight up database layer.
[1965.04 --> 1965.14]  Right.
[1965.24 --> 1965.44]  Okay.
[1965.58 --> 1969.56]  Similar to the computed stuff, you can do compositional data as well.
[1969.68 --> 1975.20]  So you can create things from multiple sources and then, you know, you can kind of define
[1975.20 --> 1975.68]  a new thing.
[1976.10 --> 1976.58]  Yep.
[1976.58 --> 1982.12]  In some ways, that's why I go back and forth about using Gatsby as an example.
[1982.32 --> 1986.28]  But that's one of the really interesting things about what they did is they basically said,
[1986.44 --> 1991.38]  you can pull from any data source and we're going to agglomerate that all up into a single
[1991.38 --> 1993.08]  GraphQL representation of it.
[1993.32 --> 1997.02]  And so it can abstract away your backend data sources.
[1997.62 --> 1998.00]  Yeah.
[1998.04 --> 1999.66]  I just had a really interesting thought.
[1999.80 --> 2000.74]  Do you guys want to hear it?
[2001.14 --> 2003.96]  We can't just drop that and not tell us.
[2004.00 --> 2004.26]  All right.
[2004.32 --> 2005.12]  That's not a question.
[2005.12 --> 2011.12]  So based on, yeah, based on what you just said, K-Ball, I wonder if Google search input
[2011.80 --> 2013.48]  was like the original GraphQL.
[2014.38 --> 2021.64]  Like, you type something, you know, bolts from all the, I don't know, just internet search
[2021.64 --> 2022.42]  indexing.
[2023.22 --> 2028.92]  I mean, I wouldn't call it the original GraphQL necessarily, but I think that idea of being
[2028.92 --> 2034.86]  able to put a data pipeline layer where you source from many different possible sources,
[2034.86 --> 2042.28]  and then having that generate a kind of universally queryable middle layer is a really valuable
[2042.28 --> 2042.88]  concept.
[2043.22 --> 2049.68]  And you could do that in sort of a pre-processed manner, which Google search does, I think,
[2049.72 --> 2050.66]  and Gatsby does.
[2050.80 --> 2057.42]  Or you could do that in an on the fly manner where you're wrapping other APIs with a GraphQL
[2057.42 --> 2059.50]  layer or some other layer that does that.
[2059.50 --> 2066.04]  But I think that concept of being able to create sort of a linchpin data layer that you can
[2066.04 --> 2069.86]  then have a single format that all of your different clients can talk to is one of the
[2069.86 --> 2072.90]  incredibly powerful concepts that GraphQL adopts.
[2072.90 --> 2084.14]  What up, party people?
[2084.26 --> 2088.18]  If you want to know what's happening with your code, track errors and monitor your app's performance
[2088.18 --> 2088.84]  with Sentry.
[2089.24 --> 2092.94]  Build better software faster with Sentry's application monitoring platform.
[2093.52 --> 2096.94]  Diagnose, fix, and optimize the performance of your code.
[2097.30 --> 2100.22]  Cut your time on error resolution from hours to minutes.
[2100.22 --> 2103.62]  It works with any language and integrates with dozens of services.
[2104.10 --> 2108.08]  Over one million developers and 68,000 organizations already use Sentry.
[2108.48 --> 2112.22]  And best of all, GSParty listeners new to Sentry get the team plan for free for three months.
[2112.52 --> 2116.20]  Head to Sentry.io to get started and use the code PARTYTIME when you sign up.
[2116.42 --> 2121.44]  Again, Sentry.io and use the code PARTYTIME because, hey, it's PARTYTIME, y'all.
[2130.22 --> 2152.32]  Let's dig into some of these more advanced features.
[2152.50 --> 2156.10]  So you briefly mentioned, Jen, Apollo Federation.
[2156.34 --> 2158.30]  Can you flesh out a little bit more for us?
[2158.36 --> 2159.04]  Like, what is that?
[2159.04 --> 2164.50]  So Apollo Federation, it's a technology and an architecture.
[2165.16 --> 2168.16]  So it is a concept, but to break it down into a concept, right?
[2168.26 --> 2174.90]  If you have REST microservices and different teams working on these microservices, if you
[2174.90 --> 2178.30]  replace that REST with GraphQL, how does that work?
[2178.56 --> 2181.84]  So how can everyone have their slice of the data graph?
[2182.02 --> 2186.64]  But also there will be reusable parts of that that need to span across the teams.
[2186.64 --> 2188.06]  So how does that work?
[2188.58 --> 2194.40]  And it used to be that you would use a process called schema stitching to integrate all your
[2194.40 --> 2198.50]  separate microservice graphs together into the one big graph.
[2198.76 --> 2201.16]  That was a really manual process that you did on the server.
[2201.86 --> 2207.00]  So Apollo Federation is a way to do this without having to do that manual process.
[2207.00 --> 2213.44]  It has a declarative process that you use in the schema to say when you're extending a certain type.
[2213.96 --> 2221.98]  And there's a gateway that sits in front of your different microservices that will do the orchestration for you of picking what it needs from which graph.
[2221.98 --> 2229.16]  So all the small pieces of the graph come together into one endpoint that you can then query from any point in the graph.
[2229.68 --> 2232.24]  But it's nice because there's a separation of concerns.
[2232.66 --> 2242.12]  If one team is really only working on one slice of the graph, then they can do that without concern for having to build into a whole huge graph system.
[2242.26 --> 2244.46]  That's the high level of Federation.
[2244.46 --> 2246.38]  Where do fragments come into this?
[2246.44 --> 2247.24]  I'm just curious.
[2247.64 --> 2256.12]  Like, and because there's this funky area with fragments and, you know, needing to kind of do some extra setup if you want to get introspection working.
[2256.64 --> 2259.40]  And I guess maybe what's the philosophy on like shared?
[2260.02 --> 2262.86]  Well, I guess maybe we can define like what are fragments for folks?
[2262.98 --> 2268.46]  And then, you know, how are they supposed to be used and shared in the context of this Federation world?
[2268.76 --> 2270.56]  I can answer the first question for you.
[2270.64 --> 2273.76]  The second question I don't have as much knowledge about.
[2273.76 --> 2278.54]  I do know more about extending whole entities instead of fragments.
[2279.00 --> 2281.26]  So I'm unsure about fragment sharing between them.
[2281.56 --> 2287.24]  But if you don't know what a fragment is, it's basically like a piece of reusable fields.
[2287.44 --> 2290.42]  It's reusable fields, basically, that you can assign to different queries.
[2290.82 --> 2294.76]  You kind of use like a spread operator to like spread them out in your query.
[2295.18 --> 2295.30]  Yeah.
[2295.46 --> 2303.56]  I've found fragments to be super useful because they let you essentially define the data that you're going to want down at the level of whatever
[2303.56 --> 2306.14]  component is asking for it or using it.
[2306.28 --> 2309.86]  But then roll up your queries to do a single query at the top level of your page.
[2309.94 --> 2312.80]  So you're not you're able to consolidate the sets of things that you want.
[2313.06 --> 2315.86]  Are there caching implications of using fragments as well?
[2316.16 --> 2316.64]  I'm unsure.
[2317.06 --> 2323.46]  When we start to get into like the more like server side heavy stuff, I have less graphical knowledge on that side.
[2323.46 --> 2331.86]  In the client, are there or that's just all cached based on like which fields have been fetched and your related entity IDs?
[2332.20 --> 2339.32]  Yeah, that has more to do with entity IDs because your fragments don't really have that at the top level, right?
[2339.42 --> 2342.84]  They always roll up to a top level field that would have an ID.
[2342.84 --> 2350.04]  So you can do things like on the client, you can read a fragment or write a fragment into the cache.
[2350.44 --> 2364.90]  But as far as caching goes, the bigger concern is more about like arguments and variables to keep track of like what you set to your query and be able to allow you to pull it back that data if you want.
[2364.90 --> 2370.20]  So Federation feels like a pretty advanced feature in GraphQL.
[2370.38 --> 2375.26]  And it's something that I think came onto the stage a little bit more recently than some of the other things.
[2375.56 --> 2383.30]  What else is going on in terms of like moving the standard and the state of the art forward in GraphQL?
[2383.60 --> 2388.42]  I know that for Apollo, like Federation is like the future.
[2388.56 --> 2391.34]  We're investing very heavily in Federation.
[2391.34 --> 2402.64]  We see it as the way that companies can really adopt the graph more easily and get the most benefits out of this graph.
[2402.88 --> 2404.90]  We're building like a lot of tooling around it.
[2405.00 --> 2406.68]  We're really working heavily on it.
[2407.10 --> 2409.66]  That's really important to Apollo.
[2410.26 --> 2417.98]  As far as GraphQL and the spec in general, there hasn't been as much going on with that as of late.
[2418.20 --> 2420.44]  From what I know, I do know that.
[2421.34 --> 2431.00]  Defer and stream directives are still not fully adopted, though some GraphQL servers have already adopted them.
[2431.14 --> 2437.06]  And so we are going to, in Apollo, start to adopt those as well, including on the client.
[2437.68 --> 2441.28]  So we're going to be working on that next as part of our big Apollo client roadmap.
[2441.90 --> 2444.90]  That's really all I got on that side of things.
[2445.02 --> 2448.84]  By the way, the spec is like one of the nicer specs to read through.
[2448.84 --> 2450.92]  It's actually like quite clear.
[2451.62 --> 2452.52]  It's a nice bedtime reading.
[2453.02 --> 2454.82]  Just real chill bedtime reading.
[2455.00 --> 2455.50]  Oh, man.
[2455.76 --> 2458.28]  By the time we get that late, I can't focus on anything.
[2459.06 --> 2460.90]  And that late is like 830 for me, right?
[2460.90 --> 2467.58]  So I'm like seriously, like at 10 p.m. just like reading through the spec being like, oh, yeah, that's right.
[2467.66 --> 2468.44]  That is what that is.
[2468.54 --> 2468.78]  Cool.
[2468.86 --> 2469.28]  Thank you.
[2469.86 --> 2470.26]  Chill.
[2470.88 --> 2471.86]  It's reinforcing.
[2472.72 --> 2476.16]  I'm actually just like reassurance, you know.
[2476.24 --> 2476.48]  Yeah.
[2477.22 --> 2482.04]  Gravity, you know, like time space continuum, like reality check.
[2482.04 --> 2493.74]  So I think the spec originally came out of Facebook and the Facebook engineers, you know, folks have I've actually been fortunate to meet some of them worked really, really hard on making this a spec and they were really excited about it.
[2493.82 --> 2497.66]  And I remember like first version came out and was released publicly.
[2497.92 --> 2501.44]  What involvement folks at Apollo have with pushing the spec forward now?
[2501.56 --> 2506.92]  Like, is it is there more of a kind of open community around this now?
[2507.72 --> 2511.36]  GraphQL isn't a foundation or there is a foundation that exists.
[2511.36 --> 2512.52]  Yes, it is a foundation.
[2512.66 --> 2517.46]  So it's definitely like a project that's grown beyond Facebook in that sense, right?
[2517.62 --> 2518.40]  Yes, it has.
[2518.48 --> 2518.64]  Yeah.
[2518.82 --> 2524.08]  So it started at Facebook, but it is technically now a foundation.
[2524.88 --> 2529.98]  And so we do, you know, have representation in that same as we do TC39.
[2530.56 --> 2535.12]  You know, if we're involved in a technology, then we also need to be involved in pushing the spec forward.
[2535.12 --> 2542.04]  I would say, though, because there's not a lot of active like changes happening with the spec.
[2542.82 --> 2546.94]  And there's just not as much to try to move forward.
[2546.94 --> 2556.52]  A lot of Apollo's open source work now, too, is really shoring up the projects like Apollo Server and Apollo Client.
[2557.12 --> 2570.02]  So Apollo Client, for instance, my coworker on that, the lead architect on the project, Ben, rewrote all of Apollo Client, basically, for a huge like 3.0 release.
[2570.02 --> 2574.08]  That changed a lot of how we were doing caching on the front end.
[2574.22 --> 2577.30]  It used to be a little bit more of a manual thing.
[2577.42 --> 2580.98]  Now you can declare things a little bit more declaratively, and it's very nice.
[2580.98 --> 2583.24]  And so that's sort of where our focus has been.
[2583.50 --> 2594.90]  Less on, I would say, pushing the GraphQL spec to certain places and more on making sure that if you want to work with GraphQL, we're still giving you like the best experience possible.
[2595.08 --> 2599.52]  Yeah, it's very much like a Ferrari experience, I would say, Apollo Client.
[2599.88 --> 2601.54]  It's like lots is in there.
[2602.40 --> 2609.58]  I think my only feedback to y'all would be consider breaking it apart, you know, doing the Lodash thing and letting people like import certain modules.
[2609.58 --> 2611.94]  Because I think people don't use all of it.
[2612.18 --> 2618.50]  And then there's just a lot of bloat, I think, sometimes that you if you're trying to be conservative with your bundle size.
[2618.70 --> 2619.96]  That's my only gripe with it.
[2620.02 --> 2621.68]  But it's pretty impressive.
[2622.42 --> 2625.30]  There was some work done on that in 3.0.
[2625.40 --> 2631.02]  Like you can import specific things in 3.0 and leave like a bunch of stuff out.
[2631.14 --> 2631.46]  Nice.
[2631.56 --> 2633.64]  But I know that Ben has future ideas.
[2633.86 --> 2635.28]  Though Ben always has future ideas.
[2635.32 --> 2636.40]  So it's just like not surprising.
[2636.58 --> 2637.52]  Send Ben flowers.
[2637.52 --> 2638.82]  Oh, yeah.
[2638.94 --> 2646.84]  So send Ben like all the things because he worked basically alone on that for a long time and did incredible work on it.
[2647.18 --> 2650.02]  And cares very, very much about the end user's experience.
[2650.44 --> 2651.64]  So he's fantastic.
[2652.26 --> 2656.22]  Yeah, we're still on a two dot something variant of the Apollo Client at Home.
[2656.32 --> 2660.42]  And every time I try to figure something out and I go to the docs, I'm like, oh, this would be easy if we're on 3.
[2660.74 --> 2662.30]  It would be easy if you're on 3.
[2662.36 --> 2663.02]  That's correct.
[2663.34 --> 2664.62]  That's all the work Ben did.
[2664.62 --> 2666.96]  Got to figure out what that migration looks like.
[2666.96 --> 2667.22]  Yeah.
[2667.60 --> 2671.80]  Admittedly, it's not the easiest migration path because so much did change.
[2671.98 --> 2674.76]  But 3.0 is such a nice experience.
[2675.24 --> 2676.18]  Like really, really great.
[2676.60 --> 2677.02]  All right.
[2677.10 --> 2682.06]  Anything else you want to let folks know about or leave the audience with before we wrap up?
[2682.68 --> 2683.44]  I don't know.
[2683.60 --> 2684.52]  Try out GraphQL.
[2684.76 --> 2689.06]  If you've never experienced it, I mean, at least like spin up a side project.
[2689.22 --> 2690.58]  See what it's like, you know.
[2691.18 --> 2691.84]  Check it out.
[2691.84 --> 2694.04]  Maybe move to a company that uses it.
[2694.12 --> 2694.50]  I don't know.
[2695.00 --> 2695.18]  You know?
[2695.46 --> 2696.96]  Amel, are you using GraphQL at work?
[2697.18 --> 2697.68]  I am.
[2697.80 --> 2698.16]  Yes.
[2698.54 --> 2698.78]  Yeah.
[2699.12 --> 2699.40]  Okay.
[2699.56 --> 2700.74]  And your company is?
[2700.98 --> 2701.34]  Indigo.
[2702.06 --> 2702.42]  Indigo.
[2702.48 --> 2703.02]  Indigo AG.
[2703.22 --> 2703.42]  Yeah.
[2703.56 --> 2703.88]  Indigo.
[2704.48 --> 2704.80]  Okay.
[2705.14 --> 2706.44]  So yeah, you could go work at Indigo.
[2706.72 --> 2707.52]  Come work at Humu.
[2707.78 --> 2708.76]  Don't go work with Feras.
[2708.86 --> 2710.60]  Sounds like that's not going to happen for a little while.
[2710.60 --> 2710.96]  Yeah.
[2712.90 --> 2713.74]  Or go work with Apollo.
[2714.08 --> 2714.96]  You can come work at Apollo.
[2715.06 --> 2716.22]  We do have open recs.
[2716.36 --> 2717.22]  Like we're definitely growing.
[2717.48 --> 2718.90]  So come hang out.
[2718.94 --> 2719.14]  Yeah.
[2719.20 --> 2721.22]  You get to work with Ben and Jen.
[2722.06 --> 2722.98]  Their names rhyme.
[2724.84 --> 2726.20]  And it's an open source project.
[2726.20 --> 2731.66]  So if you can't get paid for it right now, you could still dig into the code, submit a PR, learn about it.
[2731.70 --> 2732.52]  Oh, yeah.
[2732.52 --> 2741.28]  If you want to contribute to an Apollo project, by the way, the one that I would say is the easiest to get started with is the Apollo Client DevTools project.
[2741.80 --> 2748.32]  That one is more similar to like a React application you would know, but you're still getting some GraphQL experience.
[2749.16 --> 2754.64]  Apollo Client as an open source project is really difficult to dig into.
[2754.86 --> 2761.66]  So like by all means do it, but just know like your contributions, like it might take you a while to like get one in the system.
[2761.66 --> 2762.10]  Awesome.
[2762.38 --> 2762.66]  Awesome.
[2763.02 --> 2765.02]  Well, thank you so much for joining us today, Jen.
[2765.06 --> 2765.84]  This has been fun.
[2766.00 --> 2766.82]  Thank you for having me.
[2766.82 --> 2773.26]  I am renewed in terms of energy to go and try to do a migration from Apollo to Apollo Client.
[2774.92 --> 2775.34]  Nice.
[2775.76 --> 2776.12]  Awesome.
[2776.36 --> 2777.96]  Well, thank you, Firas.
[2778.18 --> 2778.90]  Thank you, Amel.
[2779.56 --> 2782.26]  And that has been this week's JS Party.
[2782.46 --> 2784.60]  So catch us again next week.
[2784.80 --> 2787.60]  Every week, if you're not listening to this live, you can listen live.
[2787.60 --> 2791.04]  Thursdays, 10 o'clock Pacific, a.m.
[2791.06 --> 2791.66]  Not p.m.
[2791.66 --> 2793.66]  As noted, I'll be asleep by 10 p.m.
[2794.10 --> 2795.44]  Hope to see you next time.
[2795.54 --> 2795.78]  All right.
[2795.88 --> 2796.48]  Take care of all.
[2796.60 --> 2798.04]  This is K-Ball signing out.
[2798.04 --> 2803.44]  Thank you for listening to this episode of JS Party.
[2803.64 --> 2806.28]  If you enjoy the show, please do share it with a friend.
[2806.60 --> 2810.68]  Personal recommendations are the number one way people find new podcasts they love.
[2810.92 --> 2814.18]  Also, check out the back catalog at jsparty.fm.
[2814.42 --> 2820.68]  There you'll find our recommended episodes, plus listener favorites, and you can even request your own guest or topic idea.
[2821.08 --> 2822.96]  JS Party is produced by Jared Santo.
[2823.18 --> 2823.60]  That's me.
[2823.60 --> 2826.28]  With music by the mysterious Breakmaster Cylinder.
[2826.52 --> 2830.32]  Thanks again to our sponsors, Fastly, LaunchDarkly, and of course, Linode.
[2830.74 --> 2834.82]  On the next episode, Amel, Nick, and I welcome Googler Paul Backhouse to the show.
[2835.02 --> 2840.38]  Paul is heading up a new initiative to promote, educate, and equip web creators to do their thing.
[2840.62 --> 2841.56]  Stay tuned for that one.
[2841.68 --> 2843.04]  It'll be coming at you next week.
[2845.70 --> 2847.06]  Hey, JS Buds.
[2847.22 --> 2849.96]  I know lots of you have had some, quote, moments.
[2849.96 --> 2851.62]  Game on.
