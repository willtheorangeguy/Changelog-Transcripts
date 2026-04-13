[0.00 → 17.98] Welcome to the Changelog episode 0.4.6.
[18.26 → 19.20] I'm Adam Stachowiak.
[19.42 → 19.98] And I'm Wynne.
[20.10 → 21.36] This is the Changelog.
[21.40 → 23.00] We cover what's fresh and new in open source.
[23.42 → 26.20] If you found us on iTunes, we're also on the web at thechangelog.com.
[26.36 → 27.48] We're also up on GitHub.
[27.48 → 29.44] Head to GitHub.com slash explore.
[29.52 → 33.48] You'll find some trending repos, some feature repos from the blog, as well as the audio podcasts.
[33.90 → 37.70] If you're on Twitter, follow Changelog Show, Changelog Jobs, and me, Adam Stack.
[38.08 → 40.46] And I'm Penguin, P-E-N-G-W-Y-N-N.
[41.00 → 43.90] This week's episode is sponsored by GitHub Jobs.
[44.00 → 47.86] If you want us to feature your jobs on the show, head to thechangelog.com slash jobs.
[48.84 → 51.68] Select advertise on the Changelog when posting your job, and we'll take care of the rest.
[52.36 → 54.08] Drumbeat's looking for a front-end web developer.
[54.08 → 62.80] If you rock the HTML5, the CSS3, jQuery, and want to work with Mozilla at drumbeat.org, head to LG.Gd slash 5v.
[63.30 → 68.08] And the good folks over at Remember the Milk need JavaScript Pros, Scala engineers, and sysadmins.
[68.16 → 72.30] Check out LG.Gd slash 5z, 5d, and 5l.
[72.30 → 76.10] Le'Vein's looking for a UI designer with programming experience.
[76.92 → 82.62] Experience needed with Rescue, Delayed Job, XMPP, Blather, Windows API knowledge, even Objective-C.
[82.74 → 89.30] If it sounds like your sort of gig, check out LG.Gd slash 5x, because it's five times the size of ordinary gigs.
[89.72 → 90.14] That's right.
[90.54 → 91.32] Fun episode this week.
[91.38 → 94.78] Talk to the guys over at Yahoo about the GUI library.
[95.52 → 97.84] Node.js came up again, so we kept that streak alive, I think.
[98.14 → 98.66] There you go.
[98.66 → 104.64] Found out what happens when you commit bad JavaScript when Douglas Crockford's on staff at your team.
[105.02 → 107.18] Yeah, they seem kind of scurry about that one.
[107.38 → 108.96] They run you through the JS Lint.
[109.42 → 110.06] They sure do.
[111.62 → 112.60] Fun episode this week.
[112.62 → 113.18] Should we get to it?
[113.44 → 114.10] Let's do it.
[123.06 → 125.48] We're chatting today with the GUI team from Yahoo.
[125.48 → 129.64] So why don't you introduce yourself, guys, and a little bit about what you do with the project.
[130.00 → 131.24] Well, my name's Adam Moore.
[131.56 → 134.40] I have been with the project since the beginning.
[135.06 → 144.08] I work on the core part of the library, the GUI global object and the loading system and the customer-fitting system.
[145.68 → 147.22] My name's Satan Desai.
[147.48 → 150.02] I've been with GUI for about four years now.
[150.02 → 160.64] And on the GUI 3 side of things, I work with the component infrastructure, so things like the attribute subsystem, the widget infrastructure, plugins, that kind of thing.
[161.42 → 167.16] For the uninitiated, why don't you give the elevator pitch in GUI and a little bit about what this rather large framework does.
[167.76 → 169.44] Yeah, so let me jump in.
[171.08 → 174.70] GUI is your JavaScript platform library.
[174.70 → 188.62] We have the classical browser normalization layer, the ability to include script on the page, the ability to normalize DOM interaction and DOM event interaction.
[189.60 → 202.16] But then on top of that, we have kind of pretty robust app development pieces, generic utilities, which help with internationalization, data access, remote data retrieval.
[202.16 → 212.64] And then on top of that layer, we kind of have the typical widget subsystem with a set of out-of-the-box widgets for browser-based web development.
[213.28 → 219.02] And now we're kind of branching into other environments, such as the server and mobile-based devices.
[219.74 → 221.52] So, Adam, you said you've been with the project since the beginning.
[221.72 → 225.14] How long ago was that, and what's also new in version 3.3?
[225.92 → 230.40] Okay, well, I started here in May in 2005.
[230.40 → 233.60] That's when we first started the project for Yahoo.
[234.10 → 239.66] When we first did it, we were tasked to build this library for Yahoo.
[240.80 → 243.46] There was no talk at the time of open sourcing it.
[243.46 → 255.02] It was in February 2006, I believe, that we actually released GUI 2.0, we called it, because the first version was internal to Yahoo only.
[255.96 → 258.76] And that one was the first open source effort.
[259.82 → 261.22] Or, yeah.
[262.16 → 265.70] So since then, obviously, lots happened.
[265.70 → 275.10] And GUI 3.0 was a complete rewrite of the library in many levels.
[276.10 → 278.30] We launched that in 2009.
[278.30 → 296.36] And it has a whole new sort of architecture for being a little more robust on the page and cooperating with other, protecting your code from foreign code that might be on the page as well.
[296.36 → 304.84] And a more sophisticated infrastructure for dynamic loading and custom events.
[305.28 → 312.50] And I'll let Satin talk about 3.3.0, which was just released last week.
[312.50 → 312.78] Yeah.
[313.50 → 320.80] So with 3.3.0, I think the release was mainly centred around filling out some of our core widgets.
[321.32 → 326.98] So we're trying to get kind of parity in terms of porting over the GUI 2 widgets to the GUI 3 world.
[327.92 → 334.54] And 3.3.0 kind of had the autocomplete control, which is a big control on the GUI 2 side of things.
[334.54 → 343.70] And that was kind of completely redesigned, refactored for GUI 3, leveraging a lot of the kind of submodularization pieces in GUI 3.
[344.06 → 349.56] We had the initial data table drop, which is your basic data grid, data table infrastructure.
[350.36 → 353.00] We had a new dial component, which is rather cool.
[353.70 → 359.82] It's an alternate approach to slider-based type interactions to select values between a range.
[359.82 → 368.86] And then we had our charts component, and we went from a flash-based component in GUI 2 to a JS-based component in GUI 3.
[369.58 → 378.40] Additionally, we had the community kind of contribute resize or your typical draggable resize utility to the stack.
[378.48 → 383.02] So I think those were the major highlights of 3.3, if I'm not missing anything.
[383.02 → 388.66] So this project started back in 2006, and it's called GUI, and it's an acronym.
[388.86 → 393.04] So it's kind of easy to, I guess, forget that it's Yahoo User Interface Library.
[393.28 → 396.84] What was the core cause for Yahoo even starting this project in the first place?
[397.62 → 409.84] So in 2005, when we first started this, there wasn't actually a lot of toolkits that do all the core sort of browser normalization
[409.84 → 412.88] and additional utility layers that we needed at Yahoo.
[413.12 → 421.24] People were writing things, and we ended up with a lot of different implementations of the same thing, of various quality.
[422.02 → 425.46] And so the idea was that this is, you know, now that we know we need all this stuff,
[425.62 → 431.08] that we really needed to build something that would be common across the company.
[431.08 → 439.58] At the time, there was not very many open source projects for doing this.
[439.68 → 442.64] I think Dojo was around, and maybe Prototype.
[443.08 → 444.84] jQuery hadn't been out yet.
[446.12 → 447.46] So we evaluated.
[447.84 → 453.06] I guess before I got hired, they evaluated what was out there and decided they wanted to do a new library.
[454.70 → 455.98] And so I was hired.
[455.98 → 466.84] And the first utilities were we needed drag and drop, and we needed tree control, and we needed animation.
[467.80 → 475.24] And out of that, the event system was born, and it just ballooned out from there.
[475.82 → 477.02] It kind of just grew organically.
[477.20 → 481.64] So in terms of growing organically, Yahoo is a pretty large organization.
[481.64 → 485.98] What's the adoption rate across the various different properties you guys manage?
[486.76 → 490.56] Well, I don't know that there's any property that doesn't use GUI anymore.
[491.66 → 493.20] At first, we did have to sell it.
[493.32 → 500.80] I mean, we had to build something good and then teach people how to use it and sell it to them, essentially.
[501.38 → 508.42] Now it's sort of the standard platform for any new product that comes out of Yahoo that's going to be running on GUI.
[508.42 → 519.00] So as a large organization, what has this done for you in terms of teaching new developers and bringing on a good team and then ultimately leading to faster releases of product?
[519.94 → 526.78] Well, I guess I'm not the best person to answer that just because I'm not actually shipping those products, right?
[526.78 → 538.46] I'm building this library, and we see it as being a great success for properties being able to do more with less resources.
[538.94 → 549.82] We've certainly seen the sort of front-end engineering culture at Yahoo mature, and we think it's gotten better.
[549.82 → 564.68] We think we've helped towards that, but you'd have to ask maybe somebody at a big property like the Yahoo front page or Mail or Flickr how much they think it's really helped them.
[564.84 → 569.16] I think you'd get pretty positive feedback from them.
[569.70 → 572.82] What has putting your source up on GitHub done for community contributions?
[572.82 → 578.62] I think it was at the time at which we did it, it was long overdue.
[579.52 → 581.04] So we were an open source product.
[581.18 → 585.58] We were open source in terms of sharing what we built with the external world.
[586.32 → 600.80] And just the very nature of a platform product, having six or eight people work on platform solutions for an entire community really doesn't scale.
[600.80 → 611.24] So allowing people to look at the source code in progress, contribute to it, and give us code back into the library I think was a massive win.
[611.60 → 622.66] And then just exposing the source that way I think drove more community involvement in general in terms of driving roadmaps and use case analysis for different features as they came on board.
[623.00 → 630.02] They could pick up components earlier in the release cycle, give us use case feedback on them, which we could roll back into the final release of the product.
[630.02 → 634.90] So I think it was something we intended to do for a while.
[635.38 → 637.48] It just took us a while to get the infrastructure together.
[637.78 → 640.72] And I think the value is evident after that.
[640.96 → 648.46] Were you guys using Git before that, or was it a mirroring process just to get the code up on GitHub?
[649.62 → 650.00] Yeah.
[650.00 → 653.08] So we actually do use Git locally here.
[653.18 → 667.28] We have sort of a source of truth Git server here that we push out to the GitHub, which we do that for control of our build process.
[667.28 → 684.80] So people submit stuff, and we sort of – we get it into our system so that we can verify it and then build it, do all the post-build things, and then shoot it off right back to GitHub.
[684.80 → 684.88] Yeah.
[685.36 → 704.74] By the time we released code on GitHub, we had already – our initial thoughts were that we were going to have a Git server ourselves, but then when we saw GitHub and all the great things it did before we ever hosted our own server, we switched to that.
[705.42 → 711.50] So one of the things that has done a great job of evangelizing the platform has been GUI Theatre.
[712.16 → 713.12] So how did that come about?
[714.80 → 731.58] Oh, so that came about really because we have Eric Moravia as being, you know, really incredibly talented at putting all this stuff together, presenting it, doing the videos themselves.
[731.58 → 748.14] And then also just because we have so many great resources here, people like Douglas Crawford and Nicholas Sakis speaking often on, you know, giving high-quality presentations and teaching high-quality classes.
[749.02 → 752.42] And Eric's in there filming them, so we just have all this great content.
[752.42 → 754.06] And so it's just thrown and grown.
[754.06 → 762.46] And I think it goes hand-in-hand with just the notion of promoting front-end development as a professional, you know, professional engineering skill.
[763.28 → 764.70] So the theatre is part of it.
[764.76 → 766.18] Training is another part of it.
[766.86 → 769.16] Best practices, principles are another part of it.
[769.16 → 773.40] So I think it goes all hand-in-hand, and Yahoo does a good job at that in general.
[778.20 → 784.12] So what's it like working with Douglas Crawford if either of you had a get-commit smackdown by Douglas?
[784.12 → 803.28] You know, Douglas is, you know, he has a reputation out there for laying down smackdowns, again, especially for people who are complaining about JS Lint hurting their feelings.
[803.28 → 815.78] But he's a very thorough and considerate evaluator of some of our code and projects and everything, and it's nice to have him around helping us out.
[815.94 → 826.82] Adam and I had the opportunity to meet Douglas last year at Texas JS and found him just to be a really nice guy, not what I expected from the severity of JS Lint on my code.
[826.82 → 835.08] So one of the titles that intrigued me on GUI recently was GUI and Node.js.
[835.08 → 837.68] Have you guys played around with that setup?
[838.10 → 838.86] Oh, yeah, absolutely.
[839.38 → 850.56] In fact, I gave a little presentation at last year's Scoff in Washington.
[850.56 → 865.52] In the early going of getting that stuff to work, Dave Glass has done a lot since then, getting our full infrastructure open running underneath Node.js.
[865.52 → 880.98] And there's a lot of, as we're still actively developing, we're using this as a platform for doing some new and fun things that this year is going to be one of our focus.
[882.30 → 889.16] You know, Node is extremely hot right now, but I think people are still, it reminds me of what the Ruby stack looked like two or three years ago,
[889.18 → 894.04] where people are trying to figure out what the stack looks like and the surrounding components.
[894.04 → 900.82] To the extent that you can share, what other technologies are you looking at as far as front-end proxies and other things for Node?
[901.22 → 909.08] So in general, I think if you look at the library as a whole, and in particular GUI 3, you know, there's a bottom-most layer,
[909.34 → 913.78] which involves the DOM normalization and the DOM event normalization.
[914.40 → 920.90] And once you move above that, everything we have in terms of utilities and even component development frameworks,
[920.90 → 927.34] like, you know, the custom event framework, for example, and the attribute infrastructure, attribute base, and plug-ins,
[927.60 → 931.84] all of that stuff is generically useful for any kind of development.
[932.02 → 935.78] You know, so whether it's developing apps on the client, in the browser,
[936.18 → 938.58] or whether it's developing apps on the server side of things.
[938.68 → 944.90] So I think the way we look at it is that we write generic, useful components,
[944.90 → 950.28] which can be used on either side of the fence, on the server side or the client side.
[950.80 → 953.96] And I think the real value, which kind of Node.js adds to the pictures,
[954.08 → 957.98] now you have the option of deploying and running that code, writing it once,
[958.04 → 961.10] and then deploying and running it on either side of the fence, you know,
[961.14 → 963.64] based on bandwidth and latency and things like that.
[963.64 → 971.12] So you can have your server do more stuff for less capable clients or clients which are coming over kind of low bandwidth,
[971.46 → 976.00] high latency connections, or you can move all that same code down to the client.
[976.14 → 977.66] So I think that's really appealing to us.
[977.84 → 982.06] And if you look at everything on top of the kind of base normalization layer,
[982.38 → 985.46] all of that stuff can be used on the server for the most part.
[985.76 → 987.52] You know, even the widget infrastructure, for example,
[987.76 → 990.24] you can take a widget, render it on the server,
[990.24 → 995.10] so you get your progressively enhanced markup solution and deploy that to the client
[995.10 → 999.84] and then add interaction capabilities on clients which support them.
[1000.08 → 1004.58] So it's just exciting to be able to develop one solution which works on both sides of the fence.
[1005.70 → 1011.36] This weekend I noticed a thread on the Node.js mailing list that the title was I Can't Code Like This.
[1011.44 → 1019.12] And it was basically a rant against the complexities that arise from the asynchronous setup of Node.js.
[1019.12 → 1028.86] Do you think that that kind of Russian doll coding style will evolve the language to include other constructs to deal with that sort of complexity?
[1029.18 → 1030.00] Yeah, I think so.
[1030.10 → 1041.60] I think there's certainly, you know, if you look in the modules, additional modules section of the Node.js website,
[1041.60 → 1048.98] you'll see maybe 20 different utilities dealing with, you know, parallel processing of all these asynchronous actions.
[1049.12 → 1051.80] Because everybody's having a hard time with that.
[1052.60 → 1056.80] And I think that you'll see a lot of that.
[1056.86 → 1061.96] A lot of people are needing to rely on that sort of thing to get their program to work.
[1062.02 → 1069.58] Of course, in some of those cases, using that stuff kills some of the performance benefits of the event loop.
[1069.58 → 1080.30] But ultimately, there are some pieces of code that you just can't do right without some kind of mechanism to help straighten that out for you.
[1080.84 → 1086.56] We're actually going to have some utilities for that, I think, directly in GUI,
[1086.56 → 1091.86] because we're going to be our sort of Node.js, GUI framework.
[1092.48 → 1102.48] We'll, you know, be using GUI to handle some of these things that we'll be calling asynchronous Node.js calls.
[1102.74 → 1102.86] Yeah.
[1103.16 → 1107.72] And on the flip side of that, I think, to a certain extent, when you're developing for the browser,
[1108.14 → 1112.16] you're kind of developing with an event loop mindset anyway.
[1112.16 → 1117.54] So a lot of people who are developed for the browser are somewhat already familiar with the notion of callbacks
[1117.54 → 1122.76] and your code not being called in line with, you know, the thing which initiates the action.
[1122.94 → 1125.18] So I think that helps, too, in general.
[1126.28 → 1130.42] Speaking of targeting certain, I guess, platforms and browsers,
[1130.78 → 1135.12] I noticed in your commit logs you're actually working on mobile with this.
[1135.16 → 1137.56] So what is GUI doing in the mobile space?
[1137.56 → 1148.14] I think the way we think of mobile, I think that one of the recent talks I gave is out on GUI theatre right now.
[1148.22 → 1153.00] But the way we'd like to address it is not think of it as a separate development environment.
[1153.36 → 1158.58] So, you know, a lot of the problems or a lot of the challenges which the mobile space brings up,
[1159.62 → 1163.10] addressing those challenges could help across the board, you know,
[1163.10 → 1168.34] regardless of whether it's a desktop environment, you know, IE7 running on a crappy desktop.
[1168.84 → 1171.40] Anything we can do to address kind of performance constraints,
[1171.52 → 1175.94] which the mobile environment adds to the picture, helps across the board.
[1176.30 → 1181.10] And then when you look at the feature side of things, things like touch interaction, for example,
[1181.58 → 1186.08] there's no reason that you couldn't deploy gesture-type support.
[1186.24 → 1188.36] You know, so if I'm looking at a carousel on the desktop,
[1188.36 → 1192.52] instead of clicking a previous and next button, it would be nice if I could flick my mouse
[1192.52 → 1194.30] to scroll through carousel items too.
[1195.12 → 1200.08] And moving further, I mean, touch is just going to end up on the desktop at some point or other anyway.
[1200.58 → 1204.60] So even in terms of features, it seems like we'd like to address them more
[1204.60 → 1208.54] in terms of analyzing the discrete features, which we'd like to address things like, you know,
[1208.54 → 1213.30] offline caching, touch capabilities, transition support,
[1213.46 → 1216.72] which leverages hardware acceleration on certain devices.
[1216.72 → 1221.52] All of that stuff can be just as useful on the desktop as it is on, you know,
[1221.64 → 1223.76] what people call mobile devices.
[1224.48 → 1226.46] And with tablets, that line gets blurred anyway.
[1226.66 → 1231.94] So that's how we're addressing the whole mobile space is treating it more in terms of features
[1231.94 → 1237.38] and constraints and applying solutions to specific features or specific constraints
[1237.38 → 1242.84] so they help across the board, whether it's the server, the desktop, or a mobile device.
[1243.00 → 1246.02] I see specifically in the commit law that it's mentioning iOS.
[1246.02 → 1249.44] Is it something that you can actually run native, or is it something that, like,
[1249.48 → 1252.42] you're building native apps with this, or is it something behind the scenes that's running?
[1252.42 → 1255.62] No, it's all web-based application development.
[1256.68 → 1262.20] The references to iOS probably refer to, you know, abstractions we needed to apply
[1262.20 → 1263.88] for a particular environment.
[1263.88 → 1266.14] But it's all web-based development.
[1266.72 → 1269.16] You know, JavaScript as a language is extremely flexible.
[1269.16 → 1276.38] In other server-side and sometimes client-side languages, you know, as adoption grows,
[1276.48 → 1278.74] you get a common library that develops.
[1279.00 → 1281.74] And like in the Ruby world, it's Ruby Gems, that, you know,
[1281.76 → 1284.00] an ecosystem of pluggable code that I can drop in.
[1284.64 → 1288.74] For JavaScript, there seems to be, you know, a million different ways to do things.
[1288.82 → 1294.08] And we discuss things like the module pattern and how not to pollute the global namespace.
[1294.08 → 1299.30] Do you see JavaScript as a language ever maturing to a point where this is the way to do something,
[1299.40 → 1305.24] or is it going to be always, you know, just a multifaceted, multilayered world to develop in?
[1305.84 → 1310.74] Well, I think that it's, you know, the flexibility is part of its charm.
[1310.74 → 1321.12] And I think that we develop conventions, and we're going to rely on tools like JS Lint to help us avoid doing the wrong thing.
[1322.32 → 1331.00] I don't really see it getting, I don't really see us getting, getting, getting, you know,
[1331.20 → 1334.12] these two or three patterns that we use all the time.
[1334.12 → 1342.34] Although in a library like GUI 3, it does sort of encourage you to code in a certain style.
[1343.14 → 1348.14] So I think that, and you see that with, you know, jQuery and everything as well,
[1348.68 → 1358.42] that because how the boilerplate for GUI sets up this module for you,
[1358.42 → 1371.14] this function scope for you to work in, that it makes you program differently than if you were working directly in the global space.
[1372.00 → 1378.64] And it gives you think like being able to declare local variables without global pollution and that sort of thing.
[1378.64 → 1385.68] And so I think, and then all of our documentation, also we have certain styles of doing everything.
[1385.86 → 1391.04] And that translates into implementations outside what we do to look a little bit like that.
[1391.46 → 1395.76] From my two cents, you know, I don't really have too many complaints about it in general.
[1395.90 → 1398.34] I mean, I used to develop in a Java world.
[1398.56 → 1405.26] And, you know, a lot of Java developers now are trying to do the types of things you can do with JavaScript's flexibility,
[1405.26 → 1410.44] you know, like not be tied into a static class hierarchy, be able to mix and match, you know,
[1410.50 → 1414.84] sets of methods on the fly dynamically, that kind of thing.
[1414.92 → 1419.24] So I think that the patterns and the idioms apply to any given language.
[1419.40 → 1422.84] You know, there's a best practice of how to develop stuff in Java,
[1423.00 → 1426.88] and there are ways to work around kind of private method access in Java and that kind of thing.
[1426.94 → 1428.86] And I think the same thing applies to JavaScript.
[1428.86 → 1438.06] Now, looking over the landing page for GUI 3, it seems that there are a lot of different features that are here.
[1438.14 → 1442.30] How do you guys manage the feature set of it itself?
[1442.44 → 1445.18] And then also, how do you add more into it when that time comes?
[1445.22 → 1447.86] Is it from, like, production code that you guys have developed?
[1448.06 → 1451.90] Or is this, you know, how do you even manage bringing in stuff from the open source world too?
[1451.90 → 1463.02] Well, I think one of the things that's happened the last year was the GUI 3 gallery.
[1464.18 → 1473.78] And the gallery is great because it gives anybody the opportunity to add their code easily to the GUI ecosystem
[1473.78 → 1482.64] and have these components discoverable and even lets you deploy this code.
[1483.88 → 1491.16] If you sign a contributors' agreement, we will deploy the code onto our CDN,
[1491.38 → 1495.42] and so you get the benefit of having your code hosted on the Yahoo servers.
[1495.42 → 1507.30] And all that's really – and so on of the reasons we have it this way is I look at external features sort of debuting on the gallery.
[1507.88 → 1516.08] And as they mature and get the full set of documentation, everything that we really would want it to be as, you know,
[1516.26 → 1523.92] have in order to be part of the library, examples and API docs and all that.
[1523.92 → 1527.66] Then it can actually be rolled into the library.
[1528.84 → 1533.32] So when looking at the – when talking to developers, the guys who are listening to this podcast right now,
[1533.88 → 1536.58] and when you're looking for contributions from the open source community,
[1536.66 → 1539.96] what are some of the core things that you're looking for from the community itself?
[1541.32 → 1543.56] That's a good question in general, I think.
[1543.72 → 1549.44] So one thing we kicked off at the beginning of this year – so we just had an open hour session, for example,
[1549.44 → 1556.50] this morning with the community to outline what we have in mind based on, you know,
[1556.56 → 1558.86] input from the component developers themselves.
[1559.34 → 1564.28] You know, I, as the developer of widget, for example, know what the demand set is for widget in general
[1564.28 → 1569.14] based on, you know, external enhancement requests and bug requests and things like that.
[1569.70 → 1574.94] Based on that, we've kind of taken a first stab at our roadmap for, you know, Q1, Q2,
[1574.94 → 1580.74] plus the year based on what we think the inputs are, and we shared that this morning with the community.
[1581.56 → 1584.38] You know, it gets fuzzier as it gets into Q3, Q4 space.
[1584.60 → 1589.44] But even there, they can see, you know, what we're looking to aim for in Q3, Q4.
[1589.74 → 1593.08] And if they have something which is under development, you know, they can say, you know,
[1593.10 → 1597.10] I have something, you know, like Colour Picker, for example, which I've already got worked out.
[1597.18 → 1598.78] You have it scheduled for Q4.
[1599.08 → 1601.14] I have one which is pretty much ready to go.
[1601.38 → 1604.52] I'll put it in the gallery, and if you want to roll it in, you know, you can roll it in.
[1604.52 → 1605.18] That kind of thing.
[1605.34 → 1610.46] So I think just giving the community visibility into what we're thinking of developing next,
[1610.82 → 1612.54] seeing how much they want to help out with,
[1612.58 → 1615.52] and then using the gallery mechanism to feed that back into the library,
[1615.84 → 1617.68] I think is where we'd like to get.
[1618.40 → 1621.48] So when we chatted with Douglas Crockford last summer,
[1621.80 → 1627.04] one of the things that we talked about was the importance of having heroes in for programmers, right?
[1627.12 → 1632.94] It seems like as a profession we rarely know folks in our field over 40, right?
[1632.94 → 1635.42] I'm going to put you on the spot for a moment.
[1635.74 → 1641.32] And who are your programming heroes, and who do you think paved the way for you to do this as a living?
[1644.52 → 1652.60] You know, I have to say that, you know, programming I started when I was very young,
[1652.60 → 1656.56] and, you know, for me, it's going to sound kind of geeky,
[1656.62 → 1658.30] because I like to play computer games,
[1658.38 → 1664.42] and I think I like to program computer games first before anything else.
[1664.42 → 1680.28] So the people that did the old text-based games like Adventure and then Hunt the Campus game,
[1680.38 → 1681.52] whatever that's called, all those.
[1684.34 → 1687.06] Those guys probably paved the way for me.
[1687.06 → 1693.90] So for me, I don't necessarily know if I have heroes in terms of individuals as such.
[1695.00 → 1702.80] I think way in the beginning, the reason I got into programming was pretty much along the lines of what Adam mentioned.
[1702.88 → 1707.32] I like games, and I like programming games or parts of games.
[1707.32 → 1714.72] And I think, to me, just to focus on games originally,
[1715.52 → 1719.02] and if I had a second chance, I'd probably focus on that aspect of it again,
[1719.10 → 1720.82] or the 3D rendering part of things.
[1721.38 → 1727.62] But the reason I chose kind of UI or user interaction-based programming
[1727.62 → 1733.10] was just the ideal combination of kind of my need for some visual feedback
[1733.10 → 1736.98] with the logical and analytical aspect of programming, I think.
[1737.32 → 1739.22] It provided the ideal mix.
[1740.04 → 1742.92] And then in terms of the JS world in particular,
[1743.14 → 1744.96] I think you've said the name enough times,
[1745.04 → 1749.40] but Douglas Crockford was kind of the first guy whose material I read,
[1749.52 → 1752.98] which made me think about kind of JavaScript as a mature language.
[1753.44 → 1755.58] And I think that's probably true for most people.
[1756.28 → 1758.40] And then aside from that, I think the people I work with,
[1759.12 → 1760.16] a bunch of really smart people.
[1760.96 → 1763.24] So when you look at the open source landscape right now,
[1763.24 → 1766.04] we talked about Node, and you guys kind of got a little bit excited
[1766.04 → 1769.42] when we talked about Node for a second there and how it reflected onto GUI.
[1769.56 → 1773.06] But beyond, and you can say Node if that's the case,
[1773.18 → 1777.48] but beyond GUI, what else in open source is out there
[1777.48 → 1778.60] and is something you want to play with?
[1780.94 → 1783.06] I'm a bad person to ask.
[1783.26 → 1786.90] I'm kind of heads down on what I'm working with right now,
[1786.96 → 1788.82] so I don't really have a good answer for you there.
[1788.82 → 1791.96] I can't say I have either.
[1792.28 → 1793.80] I feel kind of bad about that,
[1793.86 → 1799.52] but there's so much that I just have to focus on in my little world here
[1799.52 → 1804.08] that I haven't gotten a lot of chance to play with a lot of new fun toys.
[1804.36 → 1805.88] We'll put a different spin on that then.
[1807.62 → 1809.08] Bash, Z-Shell, other.
[1809.08 → 1816.62] You know, Bash, I would use Z-Shell
[1816.62 → 1820.10] if I felt like customizing things to my heart's content.
[1820.20 → 1822.72] I kind of like just opening the MacBook now
[1822.72 → 1824.70] and having everything work, so Bash.
[1825.12 → 1827.98] I used to work on a Windows box until a couple of years ago,
[1828.04 → 1829.04] so I won't even comment.
[1831.10 → 1833.44] All right, so Vim, TextMate, or Notepad?
[1833.80 → 1834.20] Vim.
[1834.50 → 1835.54] I'm an Eclipse user.
[1836.30 → 1837.28] Jason or XML?
[1837.28 → 1837.56] Jason.
[1838.20 → 1838.72] Jason.
[1841.60 → 1843.00] CSS or SAS?
[1844.30 → 1844.88] Good God.
[1845.88 → 1848.38] I have a newfound appreciation for CSS
[1848.38 → 1852.32] after I tried to do some Java-based UI development,
[1852.58 → 1855.30] and I ended up working with Swing and SWT.
[1855.92 → 1856.48] Well, thanks, guys.
[1856.50 → 1858.22] We appreciate you joining us today and taking the time.
[1858.80 → 1859.92] Well, thank you very much.
[1860.38 → 1860.74] Thanks.
[1860.80 → 1861.18] It was a pleasure.
[1867.28 → 1880.20] I see it in my eyes.
[1880.66 → 1883.78] So how could I forget when
[1883.78 → 1889.60] I found myself for the first time?
[1889.60 → 1890.76] Of course.
[1890.76 → 1893.32] Safe in your arms
[1893.32 → 1896.00] And the dark passion
[1896.00 → 1896.18] Chen
[1896.32 → 1896.82] walk
[1896.82 → 1897.52] .
