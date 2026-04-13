[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.86]  Learn more at Fastly.com.
[5.08 --> 8.14]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.96]  Check them out at Rollbar.com.
[10.18 --> 12.40]  And we're hosted on Linode cloud servers.
[12.74 --> 14.74]  Head to Linode.com slash Changelog.
[15.50 --> 18.54]  This episode is brought to you by our friends at Rollbar.
[18.66 --> 21.62]  Move fast and fix things like we do here at Changelog.
[21.74 --> 24.38]  Check them out at Rollbar.com slash Changelog.
[24.60 --> 26.96]  Resolve your errors in minutes and deploy with confidence.
[26.96 --> 30.14]  Catch your errors in your software before your users do.
[30.52 --> 33.16]  And if you're not using Rollbar yet or you haven't tried it yet,
[33.30 --> 36.78]  they want to give you $100 to donate to open source via Open Collective.
[36.88 --> 40.22]  And all you got to do is go to Rollbar.com slash Changelog, sign up,
[40.60 --> 41.84]  integrate Rollbar into your app.
[41.92 --> 45.92]  And once you do that, they'll give you $100 to donate to open source.
[46.32 --> 49.14]  Once again, Rollbar.com slash Changelog.
[56.96 --> 63.02]  Welcome to JS Party, a weekly celebration of JavaScript and the web.
[63.18 --> 69.64]  Tune in live on Thursdays at 1 p.m. Eastern, 10 a.m. Pacific at Changelog.com slash live.
[69.64 --> 74.74]  Join the community and Slack with us in real time during the show at Changelog.com slash community.
[74.94 --> 75.94]  Follow us on Twitter.
[76.04 --> 77.56]  We're at JSPartyFM.
[77.68 --> 79.00]  And now on to the show.
[82.40 --> 83.48]  Hello, world.
[83.48 --> 86.42]  We are here and we are ready for a pretty big party.
[86.54 --> 90.96]  We have four panelists on the show today and lots to talk about.
[91.06 --> 93.26]  Let's find out who's joining me, Jared.
[93.42 --> 94.36]  First up, Suze Hitton.
[94.50 --> 95.44]  Suze, how are you doing?
[96.06 --> 96.62]  G'day there.
[96.70 --> 97.14]  How's it going?
[97.52 --> 98.10]  Hanging in there.
[98.16 --> 98.64]  Hanging in there.
[98.88 --> 100.26]  Next up, Chris Hiller.
[100.42 --> 100.94]  What's up, Chris?
[101.34 --> 101.72]  Hello.
[102.04 --> 104.62]  And routing out our panel today, Nick Neesey.
[104.84 --> 105.26]  What's up, Nick?
[105.54 --> 106.00]  Hoi hoi.
[106.32 --> 106.92]  Hoi hoi.
[107.42 --> 111.38]  Well, we have three awesome segments for you as per the usual.
[111.38 --> 113.74]  Well, first up, we're going to do a news roundup.
[113.84 --> 117.74]  Lots going on, of course, in the JavaScript and web world.
[117.86 --> 127.52]  And then we're going to turn our attention to the Internet of JS things, in which probably Suze will do most talking and tell us all about the wacky world of hardware and stuff going on there.
[127.88 --> 133.12]  Finally, we'll finish up the show with some shout outs to people and projects who we appreciate.
[133.12 --> 136.12]  Let's get started with the news.
[136.32 --> 148.12]  And I think the biggest story of recent and perhaps the most exciting and or controversial we'll find out is this concept and announcement of built-in modules.
[148.76 --> 151.00]  Chrome just started shipping them.
[151.00 --> 157.86]  There is a article written by Philip Walton, who's an engineer at Google, who's working on the web platform.
[157.86 --> 168.12]  And he announces KV storage, a key value storage, akin to local storage, but asynchronous, is being launched alongside this concept.
[168.26 --> 171.34]  This is the web's first built-in module.
[171.34 --> 182.46]  So think of it like a standard library for JavaScript, where you don't have to bundle them with your other JS or load them from a CD in there right there in the browser.
[183.20 --> 185.22]  Nick, you were talking about this.
[185.28 --> 190.70]  You want to open up and tell us your thoughts on KV storage, built-in modules, etc.
[191.10 --> 191.34]  Yeah.
[191.56 --> 195.20]  So it's a pretty cool concept, potentially, that's now shipping.
[195.28 --> 196.24]  And it really caught me by surprise.
[196.24 --> 200.50]  I just saw a tweet that you can use it in Chrome and start playing around with it today.
[200.50 --> 208.44]  And the first standard module, or the first one that's built-in that they're shipping, is what looks to be a wrapper around local storage.
[208.56 --> 216.30]  Which, when I use local storage, I tend to write a quick module to make it easy to get and set things in there as one of the first things I do.
[216.46 --> 219.44]  So it seems like a good, easy first win for that.
[219.66 --> 225.30]  The thing that I'm curious about, and I'm not actually sure, there is actually a stage one proposal from TC39 to add a standard library.
[225.34 --> 227.50]  And I'm not sure if this is part of that or not.
[227.50 --> 237.54]  In the referenced article, which we'll include in the show notes, he does reference the TC39's proposal JavaScript standard library repo, stage one.
[238.00 --> 238.08]  Yep.
[238.20 --> 240.32]  So Philip is at least referencing that.
[240.48 --> 242.68]  So it seems like it's potentially the same thing.
[242.90 --> 243.02]  Yeah.
[243.10 --> 245.36]  So it's an interesting foray into this.
[245.62 --> 248.40]  And it will be cool to see what follows, I think.
[248.40 --> 255.70]  But I know that there are concerns with standard modules too, with a standard library, beyond just my not-invented-here syndrome.
[257.04 --> 259.28]  You'll write your own darn key value storage.
[260.12 --> 263.62]  Yeah, I mean, the concern always with standard libraries is rot.
[263.78 --> 269.56]  It seems like a lot of times a standard library can get out there and be used and then not be well-maintained.
[269.70 --> 276.58]  Now, in the browser world, it's even, I guess, a unique scenario where, I mean, you don't absolutely have a single vendor implementing these things.
[276.58 --> 284.32]  So if it's going to be in the browser by default, it has to be in all the browsers, or at least enough of them for you to use it, of course, with polyfills.
[284.54 --> 298.10]  But it seems like keeping all browser vendors in lockstep with introducing new things into the standard library, updating security fixes, etc., is a huge undertaking and one that could potentially go awry.
[298.10 --> 301.52]  Well, we're fixing that by just getting rid of browser vendors, it sounds like.
[303.10 --> 303.94]  No comment.
[305.64 --> 307.44]  Is there some sort of a coup that's going to happen?
[307.74 --> 311.92]  Yeah, I mean, if you're looking for ammo for that argument, like, there you go.
[312.04 --> 313.54]  It's happening already, right?
[313.90 --> 326.42]  So Chrome makes, I don't know what's behind this, but I mean, it appears to be a kind of unilateral thing that was just implemented at Google in Chrome.
[326.42 --> 331.68]  I don't know if it's in Chromium, but yeah, I feel like that's a problem.
[331.98 --> 337.98]  I disagree with starting out with KV storage as the first example.
[338.46 --> 346.06]  And part of that is because when you talk about a standard JavaScript library, you cannot just consider that it's only in a browser runtime.
[346.70 --> 351.76]  And you can't even limit it to things like, well, it can also run as part of the Node.js runtime.
[351.76 --> 356.68]  Like JavaScript is going to be interpreted and run in environments outside of that.
[357.14 --> 366.38]  And I think by considering that KV storage is part of the standard library is actually not even specifically correct when you think of it in that context.
[366.38 --> 368.32]  But I'm interested in other people's thoughts about that.
[368.58 --> 370.46]  I hadn't thought of that, but yeah, that's an issue.
[370.60 --> 372.96]  I mean, yeah, Node doesn't have local storage.
[373.06 --> 374.66]  Why would Node need local storage, right?
[374.66 --> 387.02]  I mean, I'm sure somebody in user land has made a polyfill, but I think the concern from Node is, first off, they're going to be basically forced to implement this thing.
[387.26 --> 397.06]  And secondly, the namespacing going on is also, it seems to be an open question about what this prefix, the STD prefix, would, what should that be?
[397.06 --> 398.66]  What does that look like in Node?
[398.80 --> 405.36]  In the future, Node is, it looks like there's tentative plans to support this idea of built-in modules.
[405.86 --> 408.30]  And will they have to use the standard prefix?
[408.52 --> 410.06]  Will they have to use a Node prefix?
[410.46 --> 412.98]  Is there a different prefix entirely?
[413.52 --> 419.14]  You know, it creates problems for, yes, other browser vendors, but especially Node.
[419.26 --> 423.24]  I don't know about everybody else, but from where I come from, STD means something completely different.
[423.24 --> 427.54]  Yes, it means something different in Australia as well.
[428.70 --> 433.20]  Although it also used to stand for like long distance calls as well.
[433.30 --> 437.34]  So if you're making a long distance phone call, so that would confuse the conversation even further.
[437.72 --> 437.84]  Wow.
[437.94 --> 451.28]  I mean, partially why I am particularly vested and interested and concerned about this is because I have a number of libraries that I maintain that were written in JavaScript that should run both in a Node environment and also in a browser environment.
[451.28 --> 464.54]  And I already have very interesting, I guess, bundling entry points and setups because, for example, you know, we have a native, I guess not native, but we have a WebSocket API that's available in all of the modern browsers.
[464.84 --> 466.98]  But we don't actually have that in Node.js.
[467.24 --> 471.20]  And so I have to swap that out with a specific third party library and things like that.
[471.20 --> 477.90]  And so introducing this concept actually just makes my life a lot harder in order to do this.
[478.20 --> 486.76]  And that's also where I'm coming from, even outside of just considering that key value storage is not the best first standard module, I guess, to have out in the world.
[487.08 --> 491.28]  What are some other modules that would make sense in terms of standard library chats?
[491.40 --> 499.34]  Mentioning we have a few things already, math and date, things that are in the global namespace, local storage in the browser, of course, also in the global namespace.
[499.34 --> 507.52]  I do like the advantage of being able to only import and pull in things into the runtime that you need and not having everything bogged down the VM.
[507.74 --> 519.24]  But what are some other modules that are so globally useful and yet don't exist that could be put in in addition to this one, which, like you said, Suze, isn't the best first one.
[519.36 --> 524.36]  But does anybody have any ideas or even a wish list of standard libraries that they would want to have in JavaScript?
[524.36 --> 531.50]  It would be better to have better, I guess, I would like to see better binary manipulation support, I guess.
[531.80 --> 539.04]  That would be nice to have because a lot of the bit manipulation techniques and everything, it's not 100% complete in JavaScript.
[539.48 --> 542.32]  I'm not sure this is actually necessary at all.
[543.08 --> 544.14]  I mean, what?
[544.30 --> 545.82]  I mean, I'm with Chris on this.
[545.90 --> 546.40]  I really am.
[546.44 --> 552.54]  I'm trying so hard, but I just don't think, I don't know, I can see only one advantage with this.
[552.54 --> 563.68]  And that is, remember when Node.js first came out and people were accidentally NPM installing standard library modules such as FS and crypto and things like that, right?
[563.82 --> 565.70]  And then that was obviously ripe for abuse.
[566.14 --> 573.74]  But also you were just installing and like shipping things that you didn't actually need to, even if people were just uploading the exact same standard built in.
[574.18 --> 578.48]  And I think that it can help with education when you're first learning what is part of the standard library.
[578.96 --> 582.00]  But I don't necessarily think that that's even compelling enough.
[582.00 --> 589.16]  Like it's just, if you learn the language and if you learn what comes standard, then you shouldn't need to have this.
[589.28 --> 593.82]  And I really don't think that the concerns are outweighed by that one small advantage.
[593.96 --> 596.14]  But I'm interested in Chris, given that I interrupted him.
[596.20 --> 596.52]  I'm sorry.
[597.12 --> 600.16]  Oh, no, I don't think I had much more to say than that.
[600.24 --> 606.58]  I mean, it's just, they're throwing this stuff into a built-in module when, why is it not just, I mean, okay.
[606.58 --> 615.70]  Yes, I understand that in the browser, people are adding new APIs and they go in the global namespace and the global namespace gets polluted.
[615.90 --> 619.24]  So let's take stuff out of the global namespace and put it in these built-in modules.
[619.46 --> 625.26]  But I think the concern then is just that, well, how do these built-in modules work?
[625.26 --> 626.36]  How are they standardized?
[627.28 --> 637.06]  And what about, I think, especially for Node, like if they don't elect to try to implement such a thing for any given built-in module,
[637.48 --> 646.36]  the namespacing is kind of a concern because Node may have different ideas about how they want to namespace their own internal modules.
[646.36 --> 656.20]  And if Chrome makes a decision that namespaces look like this, then, I mean, I just feel like they jumped the gun, essentially.
[656.72 --> 660.74]  I see advantages to built-in modules, but I don't know.
[660.82 --> 662.90]  It just kind of muddies the waters.
[663.08 --> 667.60]  Why is this a built-in module instead of, you know, just another thing in a global namespace?
[668.06 --> 668.80]  What's the difference?
[669.00 --> 671.48]  Why can't I use it via some other method?
[672.22 --> 674.48]  Why do I have to start importing things?
[674.48 --> 680.78]  This means that I, as a web developer, and there's, I think, an allusion to this in this post,
[681.20 --> 687.04]  if I want to use standard KV storage, I have to create some sort of exception in my bundler
[687.04 --> 694.78]  that just goes ahead and leaves this import statement in there instead of, you know, converting it to something else,
[695.42 --> 700.06]  downgrading for ES5 or whatever, polyfills and stuff.
[700.14 --> 701.64]  And that's also addressed.
[701.64 --> 709.48]  But, yeah, I think it makes the bundling situation even more complicated, essentially.
[709.96 --> 714.80]  Yeah, I think the biggest problem I have with it is the, and maybe this will be solved, would be solved later,
[714.94 --> 717.92]  but what's on global and what do you have to import?
[718.00 --> 721.96]  And just, like, knowing when you have to do which, I think will just be kind of confusing.
[722.46 --> 723.08]  Not worth it.
[723.08 --> 727.96]  But it could be a potential good thing, as Corbin's been saying in the chat room.
[728.26 --> 730.44]  Potentially you could version the modules that you bring in.
[731.02 --> 738.48]  You wouldn't be polluting the global namespace, and maybe we'll avoid any future problems, like Mutools has already done it or something like that.
[738.68 --> 740.12]  Well, it is still experimental.
[740.36 --> 741.56]  You can definitely go read the post.
[741.80 --> 742.32]  Check it out.
[742.46 --> 743.08]  Get involved.
[743.08 --> 748.82]  Of course, if you have strong opinions one way or the other to influence this, there are lots of concerns, especially right now.
[748.94 --> 753.48]  One of the things they bring up is import maps, which was a concept that was foreign to me until this.
[753.54 --> 754.74]  And, of course, you have polyfills.
[754.98 --> 764.14]  So very much at the bleeding edge of the web and something that the Google and Chrome teams are working on pushing forward, but still in the experimental phase.
[764.14 --> 771.64]  Let's turn now to a little bit different kind of news, not so much on the technical front, but on the community and sustainability front.
[771.86 --> 779.66]  If you recall back in JS Party 48, which was called Foundation Foundations, a show live at Node.js Interactive.
[779.78 --> 780.32]  Suzy, you were there.
[780.40 --> 782.10]  Nick, you were there along with KBall.
[782.94 --> 791.54]  And talking about this plan to merge the JS Foundation and the Node Foundation, the news of the week is that happened.
[791.54 --> 795.92]  So now we have no longer the Node.js Foundation and the JS Foundation.
[795.92 --> 810.50]  We have the Open.js Foundation, which they're calling the next phase of JavaScript ecosystem growth coming out of the this was announced at something like the Open Leadership Summit or something Linux Foundation event just last week.
[810.62 --> 811.96]  So that's news.
[812.18 --> 813.72]  Thoughts on Open.js Foundation?
[814.00 --> 816.36]  Is this going to make big waves?
[816.38 --> 819.50]  Is this kind of just a formalization of what we all already knew was going to happen?
[819.50 --> 821.46]  And what are thoughts on this news?
[821.54 --> 849.54]  I think that I mentioned like in that episode number 48 that I like the fact that it's merging together just because it's very similar to the things that I was saying actually in the previous topic, which is that it will help to kind of unify and help everyone keep in mind that JavaScript doesn't just run in the environment that you're most biased to kind of like think about, which usually means like your day job or just like your history with the language itself.
[849.54 --> 879.52]  I think that's a positive thing.
[879.52 --> 883.08]  I'm curious what your reservations are about foundations in general.
[883.28 --> 895.38]  If I might just poke and prod a little bit, I definitely see pros and cons with these things, but I generally come down on the side of more support is better, even if it's not ideal in certain circumstances.
[896.16 --> 903.68]  And organizing around supporting open source and JavaScript is a net win, even though there are drawbacks.
[903.68 --> 906.62]  So just curious what you think you said you have reservations about foundations.
[907.22 --> 909.36]  Are you willing to to unpack that at all?
[909.92 --> 911.04]  Yeah, I can unpack that a little bit.
[911.14 --> 917.18]  I mean, to be honest, like I don't I don't sort of I don't have a hill to die on with this stuff just to preface that.
[917.18 --> 922.06]  But I think that we need to get the money from somewhere that's obviously going to come from big companies.
[922.36 --> 930.46]  But as far as choosing the kind of projects to support is usually going to be skewed in favor of what projects are these big companies using, which is great.
[930.50 --> 939.94]  Right. Because, you know, that's going to hopefully reduce some of the exploitation where, you know, there's one or two people working on a specific project and all of these companies are leveraging it to make millions.
[939.94 --> 947.88]  I think that that side of thing is probably the best expression we've seen of actually being able to put money towards these projects.
[948.10 --> 957.30]  But I think that it introduces some politics around only, you know, the filter or the way that we choose these projects, for example.
[957.96 --> 961.04]  And also just money usually has the most influence.
[961.04 --> 969.78]  Right. And so that's what concerns me about what kind of influence are just general members going to be able to have outside of like their vote.
[969.94 --> 976.20]  You know, when it comes to having elections, things like that, how much influence can that person really have?
[976.44 --> 992.04]  And I just don't think it also solves the problem of people who want to be involved with being able to develop the future of the JavaScript language or the JavaScript ecosystem as far as like specs that get proposed to be put in browsers and things like that.
[992.04 --> 995.36]  I don't think that we do enough to really support those efforts.
[995.36 --> 1006.96]  Whereas in usual cases, people have to actually join a really large company such as, you know, a browser vendor company such as Microsoft or Google or Mozilla, just in order to even get their foot in the door with a spec.
[1006.96 --> 1017.78]  Because if you've got a full time job, it's very, very hard to justify traveling to things like TC39 meetings or being able to actually work on a spec and get the help to carry it all the way through.
[1018.26 --> 1021.82]  And I think that I think that we still don't do a good job of that.
[1021.82 --> 1037.72]  And after reading the information and the FAQ behind the OpenJS Foundation, I still don't think that they're addressing these kinds of problems where, you know, to get a spec through, you still, to a degree, have to have a certain amount of like power on your side in order to be able to develop that.
[1037.72 --> 1042.32]  I can't really speak to the standardization side of things.
[1042.72 --> 1061.22]  But as far as companies having influence over the projects coming into the foundation, so companies who donate or pay, essentially pay for membership, because this is a trade union type of nonprofit, they're given a board seat or something like that.
[1061.22 --> 1073.04]  This is all documented. I haven't read all the specifics, but they're given a board seat, but they don't have any say over what project or projects are allowed into the foundation.
[1073.42 --> 1086.52]  That is a process and there's a set of criteria that for different types of projects that want to come into the foundation and they have to fill this criteria, they have to apply.
[1086.52 --> 1093.42]  And the board members, so the board members, we can think of as there's community representation.
[1093.90 --> 1097.06]  There's, I think they're working on like an individual representation.
[1097.54 --> 1106.26]  There's, in addition to your member companies, they don't have any say over what that criteria is.
[1106.26 --> 1119.22]  The criteria is, or it has been proposed and debated by and will continue to be done by something called, I think it's called the CPC or Cross Project Council or Commission or I don't know.
[1119.56 --> 1124.90]  But it's, you know, outside of the reach of the board, essentially.
[1124.90 --> 1134.32]  And so they're going to have the ultimate say over what you need to do to get into the foundation.
[1134.68 --> 1144.32]  And then also they're going to be able to say, this is the criteria you have to fulfill in order to get, you know, these resources.
[1144.32 --> 1161.70]  So, for example, a project like Node, which has a very well-developed community and governance model and has proven itself sustainable, is going to be in a position to receive more resources from the foundation.
[1162.50 --> 1168.80]  Whereas a project that's much smaller essentially won't because, well, they don't need it.
[1169.14 --> 1173.10]  So there's lots of stuff that I think they've taken into account.
[1173.10 --> 1178.10]  But I've been kind of a fly on the wall in terms of the merger of these two foundations.
[1178.70 --> 1181.94]  And from what I've seen, I think people are doing this very carefully.
[1182.64 --> 1197.74]  They're being very protective of the projects and their own self-determination and trying to not let influence from any one company kind of change and screw stuff up, essentially.
[1197.74 --> 1202.40]  Will this have any effect on just everyday users of these projects?
[1202.40 --> 1203.50]  Probably not.
[1203.80 --> 1204.08]  Yeah.
[1204.38 --> 1214.30]  And as far as, you know, if you use any project that's in the JS Foundation now, do you notice that it's in the JS Foundation?
[1214.48 --> 1217.40]  Unless you're contributing to that project, probably not.
[1217.66 --> 1217.82]  Yep.
[1218.20 --> 1224.60]  And even then, the only thing I notice is the CLA bot making sure that I've signed the contributor license agreement, which I'll probably have to sign a new one.
[1224.60 --> 1227.38]  Yeah, probably.
[1227.76 --> 1246.36]  And of course, with the JS Foundation, and I don't know as much about the Node Foundation, but in the JS Foundation anyway, you know, projects, there's no technical projects are fully like, there's no like monkeying with the technical stuff from some board member or somebody way up in the organization.
[1246.54 --> 1248.48]  Projects have full control over what they do.
[1248.48 --> 1261.44]  Well, let's turn now to our last bit of news for this show, which is making a little bit of waves, not exactly JavaScript specific, but definitely related for anybody trying to bust into the industry.
[1261.44 --> 1279.58]  Land of School, which is well known, one of those nine month immersive programs that are teaching you everything you need to get started in web development or iOS or basically in software development, which already made waves by changing their funding model so that you don't pay them cash up front.
[1279.70 --> 1285.18]  You actually go for free and then they take a portion of your salary once employed afterwards, which is interesting.
[1285.18 --> 1291.80]  They're now also, as of recently, added an $18,000 stipend to select students.
[1292.10 --> 1302.24]  So Austin Allred, who's the co-founder and CEO, recently said that we know that one of the hardest parts of deciding to go back to school is figuring out how to make it work without a full time salary.
[1302.76 --> 1306.06]  And so they are launching this living stipend pilot program.
[1306.14 --> 1314.62]  It says we are looking at how we can create more products and innovative ways to help support our current students and to expand who can become a Lambda School student.
[1314.62 --> 1316.88]  So cool idea on the face of it.
[1316.98 --> 1322.74]  Seems like that's providing more access to people who, for financial reasons, wouldn't be able to try this out.
[1322.80 --> 1328.18]  What are your thoughts on Lambda School and this idea of basically paying people to go there while they're at school?
[1328.74 --> 1334.44]  I don't know about all of you, but I get a lot of questions from non-developer friends who want to become developers.
[1334.82 --> 1336.44]  And they ask, oh, how should I get started?
[1336.50 --> 1337.34]  How can I do this?
[1337.34 --> 1350.70]  And, you know, we've had coding schools in Omaha and around the country for a while, but they can be very immersive and you never know really the quality of them unless you look through the curriculum or go through it or work on it.
[1350.90 --> 1355.00]  It's tough to know, will this actually prepare someone for a real job?
[1355.00 --> 1363.12]  And I think that this has a real benefit in that the way that they will take money from you once you have a job and the job has to be paying over $50,000.
[1363.76 --> 1371.66]  So they are incentivized to give you the best education for your money because they're only going to be able to take that if they can help you land a good job.
[1371.66 --> 1380.86]  So I've recommended this in the past to friends, but it's been difficult for them to be like, okay, I will put my life on hold and quit my job to go do this and be fully immersed in it.
[1381.06 --> 1382.02]  It's just not practical.
[1382.32 --> 1386.42]  But with this stipend, I think that that does really open the doors to others.
[1386.52 --> 1393.48]  And I haven't looked at the curriculum personally myself, but just the way that their funding is set up, they are incentivized to make you succeed.
[1393.48 --> 1398.36]  I think, yeah, I had a look at the funding options in general just on the site.
[1398.58 --> 1410.48]  And I think what I was most pleased about was not just that they're introducing this, but that there were actually with three or four options for both studying and also being able to pay for the tuition in this case.
[1410.62 --> 1420.16]  And so if you don't want to do it for free upfront and then, you know, pay down a percentage of your salary, you can actually pay an upfront cost as well.
[1420.16 --> 1426.22]  And so, you know, that might work better for your arrangement where you feel that, no, I'm absolutely committed to this.
[1426.36 --> 1433.98]  Or if I actually put this amount of money upfront, I'm going to be, I guess, like psychologically more committed to it because I won't get that money back.
[1434.08 --> 1438.10]  And I like the fact that there are a number of different options that can work for everybody.
[1438.58 --> 1441.60]  And even at this school, you don't just have to do it full time for nine months.
[1441.62 --> 1443.94]  You can also do part time for 12 months as well.
[1443.94 --> 1452.50]  And so for me, I just think that having these options here and being able to weigh them all up is a healthy thing to have as part of these schools.
[1452.86 --> 1453.30]  Absolutely.
[1453.46 --> 1456.72]  Anytime you provide more options for more people, I think it's a good thing.
[1456.78 --> 1469.32]  I'm trying to find Austin actually posted a nice image to Twitter, copy link to tweet that I'll put now in the chat room, which really shows the options they have in terms of price upfront versus price afterwards.
[1469.32 --> 1472.40]  And then with the regular land of school and then plus the stipend.
[1472.78 --> 1486.82]  So basically what happens is if you are qualified for the stipend and there's a couple of questions that they ask in order to do that and you do decide to do the pay afterwards approach, they'll give you a $2,000 a month living stipend.
[1487.00 --> 1495.64]  While you are in the course, you will then share 10% of your income over the next five years for a maximum payback of $50,000.
[1495.64 --> 1501.54]  Whereas if you go without the stipend, it's a 17% income share for two years for a max payback of $30,000.
[1501.78 --> 1506.74]  So they're absolutely recapturing those costs over time, but they're willing to take the risk.
[1506.86 --> 1512.38]  And I think it shows that they're betting on themselves to a certain degree because they have to actually deliver for you.
[1512.72 --> 1522.80]  Not only are they giving you the upfront zero cost schooling, but now they're actually cash out of the business into your pocket in order to recapture it later.
[1523.20 --> 1524.36]  I think it takes a lot of confidence.
[1524.36 --> 1526.20]  I think it's an interesting proposal.
[1526.56 --> 1531.22]  And I think it's probably one that if successful, we'll see it more coding schools around the country.
[1531.92 --> 1540.66]  The only thing that I will say about this is that this model and, you know, maybe like you can correct me if you, if the math doesn't work out this way for you.
[1540.66 --> 1548.42]  So this model is very similar to other models in that if you are the least financially privileged, you will end up paying more in the long run.
[1548.52 --> 1550.24]  That is the only comment that I will make.
[1550.38 --> 1557.16]  You know, the best case scenario is that you have the tuition upfront because looking at that, it looks like you saved the most money there.
[1557.16 --> 1564.78]  The next best thing is that you can actually support yourself without the stipend because your maximum payback over time will be less.
[1565.02 --> 1573.52]  Even if you are spending your own money, it's just that you will probably not feel like you owe as much, you know, in the years after if you get a job.
[1573.52 --> 1584.74]  And then obviously the maximum thing is that you pay nothing upfront and you have the stipend and, you know, you're, you're tied to pay that money back and the most amount of money over the longest period of time.
[1584.86 --> 1589.76]  And so it doesn't, obviously, if you're supporting yourself, you're still spending that, that stipend.
[1589.84 --> 1591.64]  It's just, you've created the stipend for yourself.
[1591.64 --> 1600.90]  But I'm definitely seeing that in a lot of cases, it's the same with people saying, why don't poor people, you know, bulk purchase things because they save money.
[1601.22 --> 1605.26]  And it's because they just don't have the money upfront to be able to have those savings in the first place.
[1605.42 --> 1607.50]  So that's the only comment I will make about that.
[1607.58 --> 1620.90]  But again, I think it's healthy that there are a number of different options in order to just get people into finding a career that's either more stimulating for them intellectually or is better, puts them into a better financial situation.
[1620.90 --> 1622.42]  Like over the long term.
[1623.00 --> 1629.50]  Yeah, no doubt the disadvantaged is still disadvantaged under this system, but they now have access where they previously didn't.
[1629.60 --> 1630.98]  Right. I just wanted both sides.
[1631.24 --> 1632.98]  No, absolutely. A step in that direction, at least.
[1633.14 --> 1635.12]  Other thoughts before we call it a segment?
[1635.68 --> 1640.40]  I think that if I were in this position, I would probably be seriously considering this.
[1640.46 --> 1644.54]  Like if I wasn't a developer, but wanted to become one, I'd be considering this as an option.
[1645.08 --> 1648.00]  I don't know what the pricing models are for other schools, though, honestly.
[1648.00 --> 1655.70]  Well, if you're out there in listener land and you're aspiring JavaScript developer, definitely check out Land of School and this new program.
[1655.70 --> 1668.22]  This episode is brought to you by Linode, our cloud server of choice, and we're excited to share they've recently launched dedicated CPU instances.
[1668.22 --> 1685.10]  If you have build boxes, CI, CD, video encoding, machine learning, game servers, databases, data mining, or application servers that need to be full duty, 100% CPU all day, every day, then check out Linode's dedicated CPU instances.
[1685.68 --> 1689.78]  These instances are fully dedicated and shared with no one else.
[1689.86 --> 1693.80]  There's no CPU steal or competing for these resources with other Linodes.
[1693.80 --> 1697.74]  Pricing is very competitive and starts out at $30 a month.
[1698.08 --> 1701.94]  Learn more and get started at lino.com slash changelog.
[1702.06 --> 1704.16]  Again, lino.com slash changelog.
[1715.54 --> 1719.70]  Next up, it's time for the Internet of JS things.
[1719.70 --> 1731.86]  Yes, we have many folks here on the panel, myself excluded, who are big into IoT, bots, hardware hacking, doing all sorts of cool stuff with JavaScript that I never get to do.
[1732.22 --> 1741.78]  And so the first thing I would like to do is just kind of go around and find out what everybody's doing, whether in their home or on the road with IoT devices, with JS.
[1741.78 --> 1745.18]  What are you all up to?
[1745.88 --> 1748.22]  And then we can dig into some ideas and some stuff in there.
[1748.30 --> 1752.16]  Suze, I know you got the craziness going on with the plants are talking.
[1753.70 --> 1754.74]  I don't even know what.
[1754.94 --> 1760.20]  Maybe we'll start with you because you seem to have the most going on and you can impress us with what you're up to.
[1761.20 --> 1766.10]  Yeah, I don't want to repeat what I talked about in that OzCon bonus JS party episode.
[1766.10 --> 1767.88]  That is actually a work in progress.
[1768.08 --> 1770.26]  So I have made a lot of progress in that.
[1770.72 --> 1778.52]  But I've also added in the fact that instead of my plants talking, like the rest of the house is going to talk, but my plants are actually going to chirp at each other instead.
[1779.20 --> 1779.60]  Okay.
[1780.36 --> 1781.30]  What drove that decision?
[1781.88 --> 1783.22]  So I'm on the SEC.
[1783.62 --> 1789.88]  I've basically completed the prototype and then I'm now laying out the official PCB production version of that.
[1790.10 --> 1793.54]  But it uses an audio data protocol so that I can be offline.
[1793.54 --> 1798.30]  So I think I mentioned on that previous episode that I wanted all of this to be offline.
[1798.82 --> 1807.74]  And so an easy way to even not even have to set up a local network for yourself is to use something like an audio data protocol instead.
[1808.02 --> 1812.00]  And so that's obviously confined to a certain space, which is good.
[1812.24 --> 1817.26]  And there's already libraries out there that you can use, such as Chirp.io, which is what I'm using.
[1817.78 --> 1822.76]  And so instead, my plants can all synchronize with each other by chirping out like packets of data.
[1822.76 --> 1829.10]  They can basically show each other stats on the screens that are part of the PCB that I'm designing.
[1829.60 --> 1833.86]  And in that way, I don't actually have to have any kind of network set up.
[1834.00 --> 1842.70]  So I feel that I'm less susceptible to the IoT cliche of hacked devices and things like that.
[1842.92 --> 1848.96]  Do they use like a 8 dB speaker or what kind of speaker do they use?
[1848.96 --> 1849.72]  Mm-hmm.
[1849.86 --> 1856.60]  So the first prototype had a regular, very tiny speaker that was attached to a headphone jack.
[1857.30 --> 1861.42]  And that was kind of designed for iPhones and other smaller devices.
[1861.68 --> 1864.36]  But I was using a prototyping board that had an audio jack.
[1864.86 --> 1867.94]  So they all had their individual speakers that they could chirp out of.
[1868.04 --> 1871.66]  And then they each had a MEMS microphone to be able to hear each other's chirps as well.
[1872.12 --> 1873.76]  The second prototype is different.
[1873.76 --> 1880.52]  I'm actually going to be introducing another communication protocol called Bluetooth, which we're mostly familiar with.
[1880.98 --> 1888.46]  And they're each going to connect to one Bluetooth speaker in turn and use that as their kind of like broadcast loudspeaker to talk to each other.
[1888.60 --> 1891.38]  I need to see your code and stuff.
[1891.38 --> 1896.14]  It's very fun.
[1898.40 --> 1903.74]  So you have an ETA on completion or is this just the ongoing project that continues to evolve and adapt?
[1903.96 --> 1904.62]  Oh, so yeah.
[1905.00 --> 1906.00]  Yeah, that's a great question.
[1906.16 --> 1908.20]  So I'm actually going on a really long vacation soon.
[1908.36 --> 1912.10]  And I have some plants that need to be watered while I'm actually away.
[1912.10 --> 1917.64]  So I would come back to them being not in a good state if they weren't watered while I was away.
[1917.64 --> 1935.46]  So right now, my deadline at least for the second working version, which could end up being a last minute slapped together perfboard soldering situation if the PCBs don't arrive in time or if there's a bit of a hitch and a wrong soldered joint on the PCB.
[1936.10 --> 1937.68]  That needs to be done in two weeks.
[1937.80 --> 1939.90]  So it's actually going to be pretty soon.
[1940.66 --> 1943.86]  What did you use to design your PCB?
[1944.26 --> 1945.32]  Oh, I used KiCad.
[1945.38 --> 1945.86]  Tell us more.
[1945.86 --> 1947.06]  I have no idea what these things are.
[1947.06 --> 1947.50]  Oh, OK.
[1947.64 --> 1954.76]  So KiCad is the open source PCB slash schematic parts layout program.
[1954.90 --> 1955.90]  It's really, really cool.
[1956.16 --> 1958.22]  I've used a bunch of different ones in the past.
[1958.34 --> 1961.88]  I've used Fritzing because they support vectors properly.
[1962.00 --> 1969.48]  So if you want to do really artistic, cool looking boards or screen prints on the actual silk screen, sorry, on the boards, you can use that.
[1969.88 --> 1971.42]  But that's a little bit limited.
[1971.42 --> 1976.82]  And Eagle to me was closed source, very proprietary, very expensive.
[1976.82 --> 1980.82]  And so I ended up going with KiCad recently and I've really been enjoying it.
[1980.98 --> 1985.18]  The recent KiCad 5 was actually pretty big.
[1985.44 --> 1990.22]  Like there were a lot of improvements to the user experience and I've found it a joy to use.
[1990.22 --> 2000.16]  The only problem is I think it has some form of memory leak because if I leave it open on my computer for an hour, my computer will just start slowing down to a halt.
[2000.32 --> 2001.90]  And as soon as I quit it, it's fine.
[2001.90 --> 2004.64]  How did you learn to use KiCad?
[2004.94 --> 2006.72]  Video tutorials, actually.
[2007.08 --> 2011.02]  There's some really good ones that I can link in the show notes that helped me a lot.
[2011.44 --> 2019.86]  I think the advantage that I had was I'd already played around with Eagle and Fritzing and followed tutorials and I've made several PCBs already.
[2020.02 --> 2024.70]  So for me, I was really just looking for, oh, this is the equivalent functionality in this program.
[2024.70 --> 2032.86]  So I think it's a little tricky to get started with, but I can definitely link the videos that for me were the most straightforward and clear.
[2033.30 --> 2033.70]  Excellent.
[2033.94 --> 2035.18]  Please do that.
[2035.28 --> 2036.90]  We will put those in your show notes, listeners.
[2037.18 --> 2044.70]  So if you want to learn KiCad, links to KiCad, links to PCB stuff, whatever Suze gives us, we're going to put in the show notes.
[2044.82 --> 2048.18]  So expect notes full of links in there to get everybody started.
[2048.26 --> 2049.10]  Let's hop over to Nick.
[2049.12 --> 2050.32]  You got something in the list there.
[2050.48 --> 2052.70]  What's your home hacking story?
[2053.38 --> 2053.76]  What are you up to?
[2053.76 --> 2054.24]  Okay.
[2054.42 --> 2059.44]  First off, I'm not happy about following the amazing Suze on this because I should have asked you first.
[2059.56 --> 2060.68]  We should have closed with Suze.
[2061.58 --> 2064.54]  Mine looks like child's play compared to the amazing stuff she's doing.
[2064.84 --> 2065.68]  So that's awesome.
[2065.74 --> 2067.96]  I've never heard of this chirp thing and it looks so cool.
[2068.20 --> 2076.80]  But some cool stuff that I've done, which is not really all that cool in comparison is I created a photo booth and I used a Raspberry Pi for it.
[2076.80 --> 2080.52]  And the reason was it was for my sister-in-law's wedding.
[2081.04 --> 2083.48]  I guess just a fun project to play around with that.
[2083.48 --> 2090.62]  But I got a whole bunch of scattered components from Amazon, including a display that you're supposed to wire into a car.
[2090.62 --> 2106.20]  But I wired it into a Raspberry Pi and then a whole bunch of buttons and a breadboard and then hook that into a digital camera so that the Raspberry Pi could send signals to the digital camera and tell it to take pictures.
[2106.20 --> 2110.08]  Those would automatically get transferred back to the Raspberry Pi.
[2110.58 --> 2119.94]  And then that would, I think I had a cron job every minute, rsync those up to a server so that you could have a live photo booth and view the pictures right away, which is pretty cool.
[2119.98 --> 2128.94]  But it used, I think, ImageMagic to combine all of the pictures into what you call those, like a photo thing that you would have at a photo booth.
[2128.94 --> 2130.44]  It had multiple photos on it.
[2131.48 --> 2132.48]  Like a collage.
[2132.68 --> 2133.80]  Yeah, yeah, a collage.
[2134.16 --> 2141.12]  But the cool thing was it used physical buttons and had RGB LED on it so it would be green when it's ready to take a picture.
[2141.52 --> 2144.00]  And then you push a button and then that would start blinking yellow.
[2144.52 --> 2148.96]  And then it would turn red and take a picture and it would do that four times and then combine them all together.
[2148.96 --> 2154.14]  So you had this button just hanging off the side of it to do that.
[2154.58 --> 2157.84]  But I also had a hidden red button on the back of it.
[2157.90 --> 2163.86]  And that's because at the venue that it was actually being used at, there was no Wi-Fi at all.
[2163.86 --> 2171.54]  So I had it just tethering to my phone, which you can program the Raspberry Pi to automatically look for a specific SSID and connect to it.
[2171.60 --> 2173.52]  And you can have the password in it and all of that.
[2173.52 --> 2180.50]  But the problem is that was finicky because if I walked more than a few feet away with my phone, it would disconnect.
[2181.16 --> 2184.02]  And then I'd have to figure out how to unplug it and plug it back in.
[2184.40 --> 2193.90]  So I had a button on the back that would immediately tell the Raspberry Pi to just restart so that it would reconnect to the Wi-Fi, to my phone tethering so that it could do that.
[2194.36 --> 2195.14]  And it worked.
[2195.30 --> 2199.24]  There was over 100 pictures taken and uploaded in that day.
[2199.32 --> 2200.00]  So it was pretty cool.
[2200.00 --> 2206.66]  I noticed, Nick, that you're using Pygame, which is something that I've used on a Raspberry Pi as well to do hardware-related things.
[2206.80 --> 2211.74]  It almost gives you the Arduino setup and then loop functions.
[2212.08 --> 2212.18]  Yeah.
[2212.36 --> 2213.94]  I think that's actually really good.
[2214.50 --> 2214.74]  Yeah.
[2214.86 --> 2216.24]  And I should also caveat this.
[2216.36 --> 2217.62]  That part isn't really JavaScript.
[2217.82 --> 2219.52]  That's the only Python I've ever written to.
[2220.10 --> 2223.82]  But it was a node server that it was uploading everything to.
[2223.82 --> 2228.68]  So kind of a collage of technology going into it.
[2228.84 --> 2229.62]  To reuse the term.
[2230.00 --> 2230.28]  Yeah.
[2230.58 --> 2233.00]  Yeah, we should get you into Johnny5, Nick.
[2233.14 --> 2237.78]  I think you'll really like Johnny5 if you liked working with the general Python GPIO stuff.
[2237.80 --> 2240.94]  Actually, so this was in May of 2015.
[2241.60 --> 2253.52]  And I left the day after this wedding and went to JSConf 2015 and did the NodeBots day with Rick Waldron and built a little robot car with Johnny5.
[2253.60 --> 2254.26]  That was a lot of fun.
[2254.26 --> 2255.50]  Yay, that's awesome.
[2255.50 --> 2262.78]  I think I would have been there too now that I come to think of it because I've sort of been attending and helping out with those workshops for the last few years.
[2262.86 --> 2263.28]  That's awesome.
[2263.54 --> 2263.56]  Yeah.
[2263.82 --> 2267.44]  Well, you don't give yourself enough credit, Nick, because this is super cool.
[2267.44 --> 2273.34]  And I hope you're wearing your wizard costume to this wedding because there's like some serious wizardry right here.
[2274.36 --> 2275.94]  Yeah, this is a really cool project.
[2276.04 --> 2278.70]  There's a lot of moving pieces and it all came together really nicely.
[2279.16 --> 2279.88]  Yeah, amazingly.
[2279.88 --> 2290.34]  It's great when a good plan comes together, especially when you know that behind the scenes it's like patched together with super glue and string and tape, you know, but nobody gets to know about it.
[2290.40 --> 2291.02]  It works great.
[2291.28 --> 2292.70]  And that's what Hacken's all about.
[2292.78 --> 2293.94]  So that's a spectacular story.
[2294.82 --> 2295.88]  All right, Chris, how about you?
[2295.94 --> 2298.84]  Have you done any IoT stuff recently?
[2299.84 --> 2300.20]  No.
[2300.20 --> 2312.42]  So I moved like, I don't know, I moved last June and then I moved again and all my stuff is pretty much still kind of packed and it's in the garage.
[2312.66 --> 2313.50]  It's yeah.
[2313.62 --> 2318.16]  So I haven't gotten a chance to do much hacking, but there's a couple of things.
[2318.28 --> 2319.20]  One was a question.
[2319.34 --> 2322.10]  The other is this particular issue in Node.js.
[2322.22 --> 2323.70]  I wanted to bring to people's attention.
[2323.70 --> 2335.00]  So a little while ago, I don't know, a couple of weeks ago, maybe there was talk of actually removing support in Node for ARMv6.
[2335.30 --> 2340.50]  And so ARMv6, that's what Raspberry Pi 1 runs.
[2340.56 --> 2343.02]  And it's also what the Raspberry Pi 0s run.
[2343.02 --> 2352.84]  And essentially there are capital P problems with building Node and running CI against these boards.
[2352.84 --> 2361.26]  The first one being that there's no cloud provider that will give you a whole bunch of ARM devices.
[2362.72 --> 2364.90]  Anyway, like ARMv6 devices.
[2365.30 --> 2372.26]  And so it looks like enough people saw this and they were like, but I used that.
[2372.44 --> 2377.94]  And so it sounds like what's going to happen is they're not going to drop support for ARMv6.
[2377.94 --> 2388.02]  But they're going to have to essentially move it into kind of like an experimental area of the bill where it doesn't always get run.
[2388.14 --> 2395.24]  But it seems like we're still going to get ARMv6 support for now, which is great if you're trying to use Node on Pi 0.
[2395.24 --> 2406.24]  So my question, and I'm hoping maybe Suze has some insight into this, is like what has happened lately in the JavaScript on microcontrollers space?
[2407.20 --> 2415.82]  I know last time I was looking at this, there was a, of course, there's always, you know, the Esperino stuff.
[2415.82 --> 2427.56]  But there was somebody who was working on essentially re-implementing Node, which would run on ESP32, certain ESP32 devices.
[2428.18 --> 2430.22]  Essentially the ones with much more RAM.
[2431.70 --> 2432.90]  What's going on there?
[2433.04 --> 2439.82]  I've heard some mumblings about there's some cool implementations out nowadays, but I don't really know much about it.
[2439.82 --> 2445.92]  Yeah, so you might be talking about JerryScript, but I think there might also be another attempt to do Node.
[2446.02 --> 2452.30]  I know that JerryScript was focused more on the JavaScript side of it, but that's maybe what you're referring to?
[2452.66 --> 2459.50]  No, it was like a fork of duct tape that runs on ESP32, W Rover, I think.
[2459.50 --> 2462.12]  So that's not something I have looked at yet.
[2462.30 --> 2466.56]  I do know that JerryScript is at least under the JS, the new JS foundation.
[2466.98 --> 2469.90]  So I know that that's going to have work continued on it.
[2470.64 --> 2479.62]  I've attended a couple of talks about some of the hacks that were needed to fit JavaScript on these devices.
[2479.62 --> 2486.20]  So to be honest, I'm not super, I guess, excited or optimistic about it at this point.
[2486.26 --> 2489.42]  I would say just let it develop a little bit further.
[2490.08 --> 2496.52]  I guess there's MicroPython and CircuitPython, which is a fork of MicroPython.
[2496.68 --> 2500.02]  I think that they're having a lot more success than we're currently seeing with Node.
[2500.08 --> 2501.60]  I think it's a little too early right now.
[2502.12 --> 2508.00]  And so using a device that's a little bit more powerful, such as the Raspberry Pi or the TESOL even,
[2508.00 --> 2515.18]  the TESOL has a wonderful Node.js experience because it runs on an OpenWrt-driven chip.
[2515.58 --> 2521.46]  I think that they're probably the most promising uses of Node and JavaScript on devices that I've seen to this date.
[2521.62 --> 2525.04]  The rest, I would caution, is mostly experimental.
[2525.72 --> 2530.88]  And you're going to lose a lot of time to those sort of new stuff,
[2531.02 --> 2536.00]  as opposed to the time you already lose due to wiring issues and all sorts of other power considerations
[2536.00 --> 2540.34]  and the regular bugs that you run into in your first learning hardware.
[2540.62 --> 2543.18]  There was another one I'm trying to...
[2544.38 --> 2549.92]  It was kind of some tricky sort of JavaScript implementation from a company,
[2550.10 --> 2555.58]  or it was like a project, and I know it started with an M, but I'm having trouble finding it.
[2556.20 --> 2557.28]  That looked cool too.
[2557.28 --> 2562.72]  But yeah, I've played around with TESOLs and all sorts of things like that.
[2562.98 --> 2572.00]  And to me at this point, I'm not sure what a TESOL is going to buy you over just like a Raspberry Pi or a Pi Zero or whatever at this point.
[2572.06 --> 2574.92]  You get an ADC, which is very nice.
[2576.02 --> 2579.76]  My biggest frustration about Raspberry Pis is that you have no built-in ADC.
[2579.76 --> 2585.82]  So a whole bunch of analog sensors that you might have also bought that you're excited to use need that external ADC.
[2586.00 --> 2593.84]  And I'm actually soldering one onto that PCB that I'm designing just because I need it for one moisture sensor, which is very frustrating.
[2594.08 --> 2601.82]  So if the Raspberry Pi came out with an ADC on it, it would literally be the perfect thing to run JavaScript hardware on.
[2602.06 --> 2603.66]  So that's my last little caveat there.
[2604.66 --> 2608.32]  What kind of moisture sensors do you use?
[2608.32 --> 2612.80]  I don't even know why we're laughing.
[2613.80 --> 2616.76]  It's just because he asked it in such a strange kind of creepy way.
[2617.00 --> 2619.42]  It's like, what kind of moisture?
[2620.70 --> 2632.62]  You can buy moisture sensors that have been integrated into a breakout board and it can communicate via either SPI or I2C, which is perfect for the Raspberry Pi.
[2633.12 --> 2634.58]  But they can be really expensive.
[2634.58 --> 2643.76]  And so I'm using a very rudimentary one, which basically just uses, you know, copper exposure, you know, two rods that have the exposed copper on them.
[2643.82 --> 2646.54]  And then you basically drive that into the soil.
[2646.54 --> 2651.42]  And so you're just measuring, you give that power and ground.
[2651.68 --> 2656.28]  And then there is a signal wire that you're just literally reading your analog signal from.
[2656.42 --> 2662.56]  So it's, you know, when you do convert it to digital through the ADC, you end up with a value between zero and one oh two three.
[2662.68 --> 2662.92]  Right.
[2662.92 --> 2671.16]  And so just keeping costs down alone, but also just knowing that out of the box, no matter what sensor you buy will work is kind of important.
[2671.60 --> 2685.78]  When I have played with those before, whenever I used resistive sensors and I'd stuff it in the soil and it would, you know, I'd water the plant and it would sit in there and then I'd pull it out, you know, maybe a month later or something, it would be all corroded.
[2685.78 --> 2687.34]  Yeah, there's a hack for that.
[2687.40 --> 2688.48]  Do you have that problem?
[2688.68 --> 2688.92]  Yes.
[2689.26 --> 2694.78]  The reason for that is that you're supplying power to it at all times, which is going to be causing that corrosion.
[2695.20 --> 2701.42]  And so usually what we recommend is that you, and I was actually about to mention it and I thought it was totally tangential.
[2701.96 --> 2715.74]  But when you have your power wire hooked up, instead of just hardwiring it to something that's always on, you hardwire it to a digital pin that you can just turn on to do the reading and then turn back off again.
[2716.26 --> 2716.56]  Wow.
[2717.06 --> 2717.38]  Okay.
[2718.34 --> 2718.66]  Cool.
[2719.08 --> 2725.98]  So, yeah, it's okay to buy those really cheap resistive ones and you don't have to spend the money on a capacitive sensor.
[2726.16 --> 2726.48]  Awesome.
[2727.26 --> 2727.62]  Good to know.
[2727.62 --> 2727.80]  Yeah.
[2727.98 --> 2730.06]  It's just you got to learn the hacks, I guess.
[2730.06 --> 2733.02]  But, yeah, it is an unfortunate thing in that it's marked power.
[2733.26 --> 2738.06]  And so, naturally, you would hook it up so that it's always powered, but that does actually cause issues.
[2738.18 --> 2739.74]  So, I'm really glad you asked that question.
[2745.78 --> 2748.88]  This episode is brought to you by Manifold.
[2749.16 --> 2755.96]  Manifold is the easiest way for you to discover, buy, and manage the best developer services for your application, regardless of your cloud.
[2756.16 --> 2759.54]  Manifold is changing the way developers and cloud services work together.
[2759.80 --> 2762.90]  Easily find, integrate, and share the best cloud services.
[2762.90 --> 2772.30]  And what's interesting is as you assemble your stack, you can organize your services into projects, then create and invite team members to collaborate via role-based access controls.
[2772.80 --> 2774.62]  And I love their hacker-friendly sign-up experience, too.
[2774.82 --> 2780.34]  For example, if you're on a Mac, you can install the Manifold CLI via Homebrew, then run Manifold Sign-Up to get started.
[2780.60 --> 2781.38]  It's so easy.
[2781.76 --> 2784.90]  Learn more and discover the best cloud services for your projects at Manifold.co.
[2784.90 --> 2787.28]  Again, Manifold.co.
[2804.36 --> 2810.86]  Okay, now it is time for shout-outs, which we love because we get to tell people who do awesome things that they're doing awesome things.
[2810.86 --> 2815.08]  And then also, we hope you love it because then you get to hear about awesome things that people are doing.
[2815.62 --> 2818.08]  And maybe you haven't heard of these awesome things, and so you can check them out.
[2818.40 --> 2824.50]  So, with that being said, let's pass it over to Suze to give your shout-out.
[2824.58 --> 2825.20]  Suze, what you got?
[2825.70 --> 2827.82]  I'm really excited about GitHub Actions.
[2828.22 --> 2828.86]  Oh, yes.
[2829.90 --> 2835.50]  And I know not everyone's in the beta, and I feel really bad, and I'm sorry, but I'm in the beta, and I'm very excited about it.
[2836.46 --> 2837.38]  Like a humble brag.
[2837.38 --> 2848.22]  I think, no, I just got lucky in that, you know, with the GitHub acquisition with Microsoft, a few of us were lucky enough to be in the alpha before the beta was even announced.
[2848.56 --> 2848.88]  Nice.
[2849.40 --> 2853.76]  So, I've been playing around with these for a while because I was given access to them a while ago.
[2854.70 --> 2859.82]  I think the biggest strength is that you can run GitHub Actions in any language you want.
[2859.82 --> 2868.08]  And so, you know, obviously, try to just use a shell script to start with to do something simple, and if it gets more complicated, then that's where you can abstract out.
[2868.78 --> 2877.52]  And essentially, like, you know, the older way of doing things that's established is you have a webhook, and GitHub will hit that webhook on certain events that you're after.
[2877.78 --> 2881.00]  But you have to find a place to host that webhook, right?
[2881.00 --> 2885.30]  So, these days, a lot of the time, it's serverless, but you're still managing that infrastructure.
[2885.44 --> 2886.42]  You're still paying for it.
[2886.80 --> 2888.84]  You're still having to figure out how to deploy to it.
[2889.00 --> 2899.08]  And so, what I like about GitHub Actions is if you can make a container that, you know, is able to just, like, run the one command you need on the GitHub event payload that they send you,
[2899.46 --> 2909.54]  then you can just throw that up in Docker Hub, and GitHub will actually, you know, start that container up and run it every single time on your behalf without you having to host anything else.
[2909.54 --> 2911.78]  And so, that's what I've been playing with recently.
[2912.26 --> 2921.14]  I've had a few Node.js scripts that will send GitHub events to my Twitch extension so that when people are watching my stream, they know when my tests have passed, for example.
[2921.40 --> 2925.40]  Or they can tell me that someone opened a new pull request so that I can go and check it out.
[2925.84 --> 2927.36]  And so, that's been so fun.
[2927.66 --> 2936.02]  But I really like the fact that if you can create your own Docker container, then you can basically do anything you want with these payloads without having to find a place to host them.
[2936.02 --> 2937.82]  Which means free Bitcoin mining.
[2938.02 --> 2938.34]  Yay!
[2939.54 --> 2944.60]  I never thought of that, but someone always has to ruin it, don't they?
[2945.00 --> 2946.78]  This is why we can't have nice things, right?
[2947.60 --> 2948.50]  Yeah, totally.
[2949.04 --> 2950.80]  Anyway, I'm working on a blog post about that.
[2951.06 --> 2951.34]  Awesome.
[2951.52 --> 2952.36]  So, that should be out soon.
[2952.46 --> 2954.08]  And there's a few limitations right now.
[2954.18 --> 2957.76]  You can't automate a bunch of stuff, so it is a bit of a manual process.
[2958.08 --> 2961.78]  But I'm basically assuming that they're going to start automating that a little bit more.
[2961.78 --> 2965.86]  So, I'm hoping to move some webhooks over to GitHub Actions once that's all set up.
[2966.52 --> 2966.94]  Very cool.
[2966.94 --> 2972.30]  Well, if you are not like Susan, lucky enough to get in on the beta yet, I know there's lots of people still waiting.
[2972.48 --> 2976.86]  Well, while you wait, you can hear from Kyle Daigle all about it.
[2976.98 --> 2979.06]  We had him on the changelog a few weeks back.
[2979.46 --> 2980.14]  I'll link that up.
[2980.20 --> 2981.70]  GitHub Actions is the next big thing.
[2981.76 --> 2982.98]  We go deep into that.
[2983.04 --> 2984.94]  And he even answers my question about Bitcoin mining.
[2984.94 --> 2991.96]  So, they have a response to the leeches out there who want to have the free compute power.
[2992.54 --> 2993.94]  So, listen to that in the meantime.
[2994.56 --> 2996.82]  And hopefully, we'll all get in that beta soon.
[2996.88 --> 2998.00]  Or hopefully, it'll become out of beta.
[2998.50 --> 2999.40]  And we can all start using it.
[2999.44 --> 3005.04]  I'm excited for the community shared workflows to start flowing towards my repos.
[3005.10 --> 3006.56]  So, I don't have to write very much code.
[3006.64 --> 3007.44]  I can get all the benefit.
[3007.80 --> 3010.80]  That's just kind of the lazy, selfish guy that I am.
[3010.80 --> 3011.52]  All right.
[3011.72 --> 3012.50]  Thanks, Suze.
[3012.62 --> 3013.62]  Chris, you are up.
[3013.70 --> 3015.54]  How about some shout-outs from you?
[3015.78 --> 3024.50]  I just wanted to give a shout-out to Jory Burson, who's been helping the projects in the JS Foundation.
[3025.48 --> 3031.58]  And she's been involved with the Foundation Merger talks and planning.
[3031.58 --> 3038.56]  And she's been doing an awesome, awesome job of helping out with the projects in the JS Foundation.
[3038.56 --> 3046.02]  And essentially, you know, what they need from the Merged Foundation and basically any other question.
[3046.82 --> 3047.78]  She's been great.
[3048.68 --> 3049.98]  So, thank you, Jory.
[3050.34 --> 3050.68]  Awesome.
[3051.36 --> 3052.12]  Thanks, Jory.
[3052.40 --> 3053.44]  Give us a link to Jory.
[3053.54 --> 3057.20]  We'll link her up and y'all can connect with her on the interwebs.
[3057.32 --> 3057.64]  All right.
[3058.08 --> 3059.40]  Nick, got shout-outs for me?
[3059.66 --> 3059.88]  Yeah.
[3059.88 --> 3067.20]  So, this isn't really a shout-out to a specific person, but it is a shout-out to a new feature that I really like a lot.
[3067.70 --> 3070.18]  And that is suggested changes on GitHub.
[3070.80 --> 3077.00]  When you're going through doing a review of a pull request, sometimes you want to be nitpicky.
[3077.56 --> 3082.80]  And that can come off as, you know, you're just being too verbose in your feedback.
[3082.80 --> 3089.26]  But this is the best of both worlds because you can be that nitpicky and also make those changes yourself in a suggestion.
[3089.54 --> 3092.58]  And then the person can apply those changes, which is great.
[3092.64 --> 3095.52]  So, you're saving them work, but you're getting the results that you need.
[3095.52 --> 3104.20]  And it's pretty nice for projects where maybe you're not using something like Prettier and everything formatted perfectly all the time.
[3104.96 --> 3114.84]  Or if you have suggestions about how something could be written better or a bug fix or you noticed a bug and fixed it, you can suggest that right in line.
[3115.30 --> 3120.28]  And then all the other person has to do is click a button and that change is applied.
[3120.28 --> 3130.04]  So, really cool feature that makes working with reviews and working with people much easier because encoding people are the hard part.
[3130.72 --> 3131.04]  Absolutely.
[3131.34 --> 3138.64]  Pretty cool how many small features, I'm just saying small in terms of surface area, not in terms of how you implement it.
[3138.64 --> 3151.36]  But just GitHub has really been rolling out the incremental improvements to the platform really at a nonstop, at a breakneck pace over the last few months ever since, you know, the change in management, new CEO and all that.
[3151.52 --> 3153.22]  So, that's something that's new.
[3153.36 --> 3159.68]  Of course, actions is a huge thing, but it's just all these little refinements they've been doing is making it a better place to be part of the community.
[3159.84 --> 3160.74]  So, it's pretty awesome.
[3161.34 --> 3164.30]  All right, let's finish up this show with a few shout outs for me.
[3164.30 --> 3168.50]  I couldn't help but alliterate because I thought of two that started with a T, so I had to think of a third.
[3169.02 --> 3172.64]  I got three quick ones, Turbolinks, Tmuxinator, and Tree.
[3172.88 --> 3175.68]  Yes, the Tree command, which is super cool.
[3175.84 --> 3184.10]  So, first of all, Turbolinks, if you do not know, is a JavaScript library that allows your website to feel like a single page app when it's not a single page app.
[3184.16 --> 3187.42]  So, you get a little bit of the best of both worlds.
[3187.42 --> 3196.34]  Basically, it hijacks, anchor clicks, and requests the next page via Ajax, strips out the parts you don't want, and loads it into the page.
[3196.98 --> 3198.10]  It's very slick.
[3198.24 --> 3200.06]  We've been using it on changelog.com for years.
[3200.66 --> 3206.46]  And it's how we accomplish our on-site player, which is static and sticky in the footer.
[3206.54 --> 3211.66]  So, you go to an episode, you click play, and you continue to browse the site, and that player stays there.
[3211.66 --> 3216.94]  Usually, that kind of feature is only available if you have a single page app, but we do not have a single page app.
[3217.20 --> 3222.02]  Every single page is rendered server-side, and Turbolinks makes it feel like an SPA.
[3222.32 --> 3226.58]  So, shout out to the folks at Turbolinks for that library.
[3226.84 --> 3228.08]  It's very cool.
[3228.96 --> 3231.08]  Next one up, Nick, you might like this, Tmuxinator.
[3231.26 --> 3232.20]  Have you ever used Tmuxinator?
[3232.42 --> 3234.78]  Right when I was first starting to use Tmux.
[3234.92 --> 3235.80]  Oh, you graduated.
[3236.12 --> 3237.50]  I don't like YAML.
[3237.98 --> 3238.98]  It's the only problem.
[3238.98 --> 3245.26]  So, if you are a Tmux user, I've been using Tmuxinator for many years.
[3245.50 --> 3249.18]  And admittedly, I just kind of set it up, and I don't really do too much now.
[3249.26 --> 3252.32]  But what it is is a configurator for Tmux.
[3252.48 --> 3261.86]  So, if you think about Tmux in terms of a bunch of different sessions, it makes a lot of sense in terms of projects you're working on or individual libraries.
[3261.86 --> 3265.44]  If you have a separate setup for each one, and it's somewhat standard.
[3265.44 --> 3273.14]  So, for instance, for the changelog website, I'll have a server pane, a console, a shell, and then something running the tests.
[3273.44 --> 3275.60]  And I don't want to set that up each and every time.
[3275.86 --> 3278.92]  And so, with Tmuxinator, you basically get, yes, it's YAML.
[3279.34 --> 3281.90]  You get these little configurations for Tmux.
[3282.58 --> 3288.88]  And you can just say Tmuxinator, and then the name of the session, and it will bring it to life over and over.
[3288.88 --> 3291.28]  And you can configure the dogdo out of it.
[3291.44 --> 3292.38]  So, it's pretty cool.
[3292.90 --> 3294.02]  So, check that out, Tmuxinator.
[3294.16 --> 3296.10]  It is a Ruby gem, so you'll install it that way.
[3296.96 --> 3298.36]  But it is very cool.
[3299.12 --> 3301.64]  Last and not least is the tree command.
[3301.86 --> 3303.14]  Nick, you got to like the tree command, right?
[3303.40 --> 3303.92]  Love it.
[3304.34 --> 3304.92]  Love it.
[3305.04 --> 3306.46]  So, this is by Steve Baker.
[3306.96 --> 3308.46]  It's one of these almost built-ins.
[3308.56 --> 3311.58]  I think it actually do install, at least on a Mac with Homebrew.
[3311.68 --> 3313.82]  It may be installed on Linuxes by default.
[3314.40 --> 3317.54]  If not, I'm sure it's an apt-get or a YUM install away.
[3318.00 --> 3324.12]  The tree command is like LS, only it will actually recurse the current directory structure that you're in
[3324.12 --> 3327.50]  and print it out in a nice, digestible format.
[3327.50 --> 3332.86]  Think of it like, for you, Tim, or Nick, you can think of it like NerdTree, right?
[3332.94 --> 3337.88]  In your Vim tab, where it has them all kind of printed out in nice, color-coded ways,
[3338.24 --> 3339.54]  only just a one-off use.
[3339.66 --> 3343.80]  So, if you have a new project or you want to know what the heck's going on in a certain directory,
[3344.50 --> 3346.66]  and just see how far down the rabbit hole you can go,
[3347.16 --> 3350.18]  you just use the tree command, and it will show you that.
[3350.28 --> 3354.70]  I use it all the time, especially on new things, and it's a great little utility.
[3355.44 --> 3357.60]  So, those are our shout-outs for today.
[3358.12 --> 3361.56]  As always, links to everything mentioned in today's show will be in the show notes.
[3361.56 --> 3367.42]  We have a very cool episode in the work for next week, talking about a brand new package manager,
[3368.08 --> 3374.82]  working with modern modules and stuff called Pika, and we have a special guest to talk to us about that.
[3374.82 --> 3376.02]  So, that's our show for this week.
[3376.68 --> 3377.58]  We'll see you next time.
[3377.58 --> 3381.24]  All right.
[3381.24 --> 3383.12]  Thank you for tuning in to JS Party this week.
[3383.24 --> 3389.30]  Tune in live on Thursdays at 1 p.m. U.S. Eastern at changelog.com slash live.
[3389.60 --> 3392.30]  Join the community and Slack with us in real time during the shows.
[3392.68 --> 3394.10]  Head to changelog.com slash community.
[3394.74 --> 3395.38]  And do us a favor.
[3395.52 --> 3396.70]  Share this show with a friend.
[3397.02 --> 3398.20]  Read us in Napa podcast.
[3398.42 --> 3399.96]  Go into Overcast and favorite it.
[3400.38 --> 3402.68]  And thank you to Fastly, our bandwidth partner.
[3403.04 --> 3404.56]  Head to fastly.com to learn more.
[3404.98 --> 3407.56]  And we move fast to fix things right here at changelog because of Rollbar.
[3407.56 --> 3409.52]  Check them out at rollbar.com.
[3409.86 --> 3413.80]  We're hosted on Leno cloud servers at leno.com slash changelog.
[3413.88 --> 3415.28]  Check them out and support this show.
[3415.66 --> 3417.70]  Our music is produced by Breakmaster Cylinder.
[3418.08 --> 3421.16]  And you can find more shows just like this at changelog.com.
[3421.36 --> 3422.26]  Thanks for tuning in.
[3422.56 --> 3423.32]  We'll see you next week.
[3429.10 --> 3432.38]  Practical AI is a show hosted by Daniel Whitenack and Chris Benson
[3432.38 --> 3436.86]  about making artificial intelligence practical, productive, and accessible to everyone.
[3436.86 --> 3439.54]  You'll hear from AI influencers and practitioners,
[3439.96 --> 3442.50]  and they'll keep you up to date with the latest news and resources
[3442.50 --> 3444.18]  so you can cut through all the hype.
[3444.76 --> 3448.10]  As you were at the Thanksgiving table with your friends and family,
[3448.20 --> 3449.82]  were you talking about the fear of AI?
[3450.10 --> 3454.50]  Well, I wasn't at the Thanksgiving table because my wife has forbidden me from doing so.
[3455.32 --> 3459.36]  It's off limits for me, lest I drive her insane because I never stop.
[3459.80 --> 3461.24]  New episodes premiere every Monday.
[3461.58 --> 3464.18]  Find this show at changelog.com slash practical AI
[3464.18 --> 3465.70]  or wherever you listen to podcasts.
[3466.86 --> 3468.00]  New episodes conquers.
[3468.00 --> 3468.12]  Hey everyone, come on and see you soon.
[3468.72 --> 3471.38]  Come on just roll in five games.
[3471.46 --> 3472.42]  Charlie can kick off as you know tonight.
[3472.42 --> 3472.44]  And let's go back to the meeting.
[3472.46 --> 3473.20]  Come on to England.
[3473.20 --> 3473.58]  Have a winter muy early on.
[3473.68 --> 3474.60]  Gemeente.
[3475.84 --> 3476.54]  We will be on the weekend.
[3476.74 --> 3478.36]  We will hang out with the coordinator in Paris understands
[3478.36 --> 3478.98]  Yardy for about theivals dream.
[3479.04 --> 3480.90]  He will be on the weekend when he meets his website.
[3483.70 --> 3485.06]  He will get back to theangers in Paris dropdown.
