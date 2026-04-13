[0.00 → 17.90] Welcome to the Changelog episode 0.2.2.
[18.06 → 19.18] I'm Adam Stachowiak.
[19.48 → 20.40] And I am Wynne Netherlands.
[20.54 → 21.40] This is the Changelog.
[21.46 → 23.50] We cover what's fresh and new in the world of open source.
[23.92 → 27.20] If you found us on iTunes, we're also on the web at thechangelog.com.
[27.20 → 30.76] Or for a real-time view, check out tail.thechangelog.com.
[31.10 → 33.40] Also head over to GitHub.com forward slash explore.
[33.50 → 37.90] You'll find some trending repos, some feature repos from the blog, as well as our audio podcasts.
[38.28 → 42.58] If you're on the Twitter, you can follow ChangeLog Show, not The Changelog.
[42.68 → 44.06] And I am Adam Stack.
[44.48 → 47.02] And I am Penguin, P-E-N-G-W-Y-N-N.
[47.60 → 53.04] Such a fun interview this week with Aaron Quint, Sammy JS, a fun little JavaScript framework
[53.04 → 56.34] built on top of jQuery fashioned after Ruby Sinatra.
[57.20 → 59.28] Yeah, it's pretty exciting to have this conversation.
[59.98 → 64.30] Yeah, since we're using it in our project ourselves, it's really helped to organize our jQuery
[64.30 → 67.68] and bring some sanity back to our JavaScript's.
[67.74 → 68.10] Absolutely.
[68.60 → 70.62] So what do you think about this little framework?
[71.32 → 72.62] Yeah, I'm excited about what it does.
[72.74 → 76.38] I mean, I think having, especially when you talked about multiple applications of Sammy
[76.38 → 80.76] inside one app, I think it just provides a lot of functionality that we've really been craving
[80.76 → 83.66] but hadn't really had an ability to do.
[83.66 → 89.46] It's nice because it splits the middle between adding some organization to your JavaScript
[89.46 → 95.34] and responding to events and things like that, but without getting full bore MVC on the client
[95.34 → 99.06] like Sprout Core or some others that tend to be a little heavier for a lot of projects.
[99.50 → 102.62] Yeah, I think that was one part of the interview I really enjoyed was where he talks about how
[102.62 → 106.38] you can just easily integrate it or just, you know, you don't have to like to make a large
[106.38 → 107.30] decision to get into it.
[107.38 → 109.08] It's just easy to pull into any project.
[109.08 → 112.58] And Aaron gave us some updates on Scoff as well.
[112.86 → 114.28] Bum that we had to miss that.
[114.30 → 117.16] But we're looking forward to Texas JavaScript coming up in June.
[117.50 → 118.36] Yep, absolutely.
[118.84 → 119.94] It's going to be a fun time down there.
[120.02 → 121.54] The lineup is just outstanding.
[121.64 → 122.66] Well, it's a fun interview this week.
[122.70 → 123.26] Do you want to get to it?
[123.34 → 123.80] Let's do it.
[132.36 → 135.36] All right, we're joined today by Aaron Quint from Sammy JS.
[135.36 → 137.72] Aaron, why don't you tell the folks who you are and why they should care?
[137.72 → 140.74] Yeah, so my name is Aaron Quint.
[141.52 → 144.92] I'm a born and raised Brooklynese, Brooklyn, New York.
[145.74 → 150.92] I've been doing Ruby development for about six years now.
[151.28 → 157.56] And before that, did some PHP and all sorts of other fun web stuff.
[158.06 → 162.26] But recently, in the past year and a half, I've gotten really into JavaScript programming
[162.26 → 170.20] and actually almost did full-time JavaScript over the past couple months with some little bits of Ruby thrown in.
[170.84 → 178.34] And out of that and out of kind of my desire to kind of, I guess, organize my thoughts
[178.34 → 181.24] and organize this kind of JavaScript applications that I was building,
[181.24 → 187.42] I kind of stole some ideas from one of my favourite Ruby projects, Sinatra,
[187.98 → 195.88] and kind of brought those same API and the same beautiful kind of simple structure that Sinatra has
[195.88 → 200.66] into JavaScript and into kind of the jQuery world with Sammy JS.
[200.66 → 208.62] So Sammy is kind of a, I wouldn't say direct copy, but it implements a similar,
[208.90 → 214.92] a very similar API to what everyone's familiar with in the Ruby community with Sinatra,
[215.26 → 218.96] which is kind of new to a lot of people in the JavaScript community.
[218.96 → 226.72] But what it allows you to do is kind of simply structure these applications and create kind of single-page apps
[226.72 → 232.82] the way Gmail or Google Reader and a lot of the other Google apps work,
[232.96 → 238.68] where you kind of operate on this hashtag so that you can, you know,
[238.74 → 244.28] maintain the state of a JavaScript app within a URL but without actually reloading the page.
[244.28 → 250.32] And it goes beyond that too, but that was kind of the first, that's kind of the first general overview
[250.32 → 253.48] and then it goes a little deeper for sure.
[255.12 → 259.20] Yeah, I'm a big Sinatra fan myself and I think that's one of the things that attracted me to it
[259.20 → 265.64] because in Sinatra, you know, it's very close, the routes that you respond to with the implementation
[265.64 → 266.66] that respond to those routes.
[266.90 → 271.80] And so Sammy's got a really natural DSL to allow you to organize that JavaScript.
[271.80 → 277.84] You know, one of the digs on jQuery is with all this unobtrusiveness.
[278.62 → 284.60] When I was trying to bring a lot of my fellow Subsists into the jQuery unobtrusive JavaScript fray,
[285.20 → 289.44] you know, they would complain about not knowing where particular functionality was coming from
[289.44 → 291.80] and where elements were being hijacked.
[291.80 → 304.58] So talk a bit about the routes and Sammy applications and kind of this ability to have multiple applications on a single page.
[305.14 → 305.32] Sure.
[305.94 → 315.68] So actually, to step back a minute too, kind of funny thing is that where Sammy actually started was,
[315.68 → 326.40] it actually was a, I'd love to lie and say that it was kind of 37 signals, you know, myth that, you know,
[326.48 → 331.24] I built it as part of an app, and then I extracted it out into this awesome framework.
[331.80 → 332.02] Sure.
[332.46 → 334.10] It wasn't that at all, actually.
[334.20 → 337.34] It was kind of like I'd been working so much in Sinatra and talking about Sinatra
[337.34 → 343.20] and working with Blake and those awesome guys in the Sinatra community
[343.20 → 353.76] and I kind of dared myself as an academic experiment to kind of see if I could replicate a lot of the functionality in JavaScript.
[354.52 → 360.02] And first pass, I was able to do it, but then I was kind of like, okay, what do I really use this for?
[360.02 → 368.60] And it was actually this guy, Alex Lang from Germany, who started using it before I even had a perfect use for it
[368.60 → 383.00] and turned it and kind of showed me kind of what I did, which was organized, make it so that this simple API is really useful
[383.00 → 392.00] for organizing jQuery code and organizing and kind of building these applications from the ground up, which is very cool.
[392.16 → 397.16] So the way the applications kind of work is they're centred around, as you said, these routes.
[397.28 → 404.88] And a route is really just, in SAMI, it's a path, a verb, a path, and a callback.
[404.88 → 411.42] So the verb is kind of like your classic HTTP verb, which is got, post, put, delete.
[411.42 → 416.56] And in SAMI, though, that means something kind of different.
[417.26 → 425.82] You know, since we're not actually making round trips to the server and there are no real, you know, get or post requests,
[426.32 → 433.44] in SAMI, a get request means you're actually hitting that path, which could be part of the hashtag
[433.44 → 437.80] or it's kind of a location that's stored somewhere.
[438.16 → 441.80] The location changes to that path.
[441.90 → 442.74] That's a get request.
[442.82 → 447.32] The post request or actually put and delete, too, are all focused on form.
[447.48 → 452.94] So if a form submission happens on the page, SAMI intercepts it with the magic of JavaScript
[452.94 → 459.74] and the magic of jQuery and turns that into this, forces it through this route,
[460.12 → 462.88] which then you can respond to, and you have this callback function,
[462.96 → 470.24] which allows you to, you know, execute on whatever path you're working on.
[470.80 → 473.42] So one of the nice things about that, just to interrupt for a second,
[473.50 → 479.18] one of the nice things that I've noticed about that is the parameter handling inside those routes.
[479.18 → 485.50] So it feels very natural if you're a Rails or a Rubbish to have a parameter sash coming from the form that's been submitted
[485.50 → 487.80] without having to do a lot of form mapping.
[488.94 → 497.02] Yeah, I think it also, in terms of just organizational and sort of your mind workflow-wise, at least for me,
[497.44 → 505.86] I'm realizing that it's very much a Ruby approach and a Ruby and Rails and Sinatra kind of mindset
[505.86 → 510.68] that's driving this and that makes it easy for Ruby developers.
[510.98 → 520.08] It's kind of a bigger mind jump, almost, for PHP or developers who aren't kind of used to this routes approach.
[521.10 → 526.08] And people I've talked to kind of have to make that mind jump, but once they do, they understand it.
[526.08 → 532.12] And it's kind of, if you think in the workflow of an application like this,
[532.16 → 536.32] where you have, you know, paths that do specific things and a path is really a state,
[536.82 → 540.78] or a get path is really a state, and then a post path is like an action,
[541.36 → 545.86] when you start thinking about it like that and organizing your code like that,
[545.86 → 554.36] like you said before, where jQuery, you know, jQuery applications can often become this kind of chain,
[554.86 → 558.68] you know, enough chain to hang yourself, I guess you could say.
[559.96 → 565.92] And you kind of have a whole page full of these just, you know, bindings to different elements.
[566.60 → 572.00] You know, there's no concept of really state or what page you're on or what action you're on
[572.00 → 574.48] in that kind of workflow.
[575.16 → 581.40] So the goal, or one of the goals of Sammy is that if you start from this kind of application,
[581.58 → 584.76] you're building an application perspective as opposed to,
[585.10 → 587.08] hey, I'm just adding some behaviour to this page.
[588.30 → 598.48] It gives you a lot of structure so that you can easily, you know, rethink your application
[598.48 → 603.76] or when you're starting from scratch, really lay it out in a way that other people can understand it
[603.76 → 606.70] and that it's a lot easier to maintain, I would say.
[607.22 → 611.22] You know, while ideas have been borrowed from Ruby heavily in this,
[611.40 → 614.96] we should mention that, you know, it's got a very JavaScript flavour to it.
[615.02 → 618.94] So it doesn't feel like, you know, you ported one DSL from one language to the next.
[619.10 → 620.88] This is a JavaScript framework.
[622.02 → 622.42] Thanks.
[622.42 → 632.56] I think something that I really owe to jQuery in general is that, you know,
[632.62 → 636.82] as a Rails developer and as a Ruby developer, when I started doing JavaScript,
[637.02 → 638.46] I mean, I'd played around with it forever.
[638.62 → 640.74] I've been doing websites since I was like 12.
[641.22 → 645.12] So, I mean, I, you know, I made elements on the page blink and I, you know,
[645.18 → 648.10] made little dots on the screen, follow your cursor,
[648.10 → 652.00] but that's not JavaScript in the way we use JavaScript today.
[652.42 → 656.52] Um, but then when I got into Rails, it was kind of prototype was a thing.
[656.92 → 661.04] And though I, though I, I enjoyed programming prototype and it kind of showed me a way
[661.04 → 665.18] and I think it showed a lot of people like kind of, oh wow, JavaScript can actually be powerful.
[665.78 → 672.16] Um, my opinion is that, uh, JavaScript, a prototype in general kind of,
[672.16 → 677.84] at least the way it is now kind of hides a lot of the, you know,
[677.84 → 685.90] core kind of awesomeness that JavaScript has in favour of, uh, making it more Rubbish.
[686.50 → 689.64] And so if you're a Ruby developer, and you're coming into Rails, and you're like,
[689.72 → 692.96] oh, here's prototype, you make this awesome kind of,
[693.04 → 695.02] you can easily translate the way you're thinking,
[695.08 → 697.02] you've been thinking about applications in Ruby
[697.02 → 703.60] or the way you've been thinking about arrays and enumerable in Ruby easily to, um, prototype.
[703.60 → 711.92] But what happens is you kind of lose the first step, which I think jQuery at least gave me,
[712.06 → 717.48] which is, oh, in order to learn jQuery, I kind of have to learn a lot more about JavaScript.
[718.22 → 727.00] And not only that, but, um, jQuery really only deals with a very specific subset of browser JavaScript,
[727.00 → 729.12] which is like the DOM and events.
[729.12 → 733.32] Um, and because of that, anything else you want to do, you kind of have to figure out,
[733.44 → 737.46] oh, I need to figure out what a function is, and I want to learn how to organize my code.
[737.58 → 742.90] And that kind of leads you or should lead you into kind of learning more about JavaScript itself,
[742.96 → 745.04] which is actually a pretty awesome language.
[745.98 → 748.94] Well, anytime you, uh, you actually pull a framework together like you have,
[748.98 → 751.30] you always come up with plugins and different extensions
[751.30 → 753.92] that sort of help you get to a certain point faster.
[754.50 → 757.88] Uh, talk about the, the list of plugins that you already have available, uh,
[757.88 → 760.98] there are lists of your docs, but more importantly, talk about, um,
[761.34 → 763.80] your idea to design the plugins the way that you did.
[764.46 → 764.84] Sure.
[765.52 → 772.96] So, um, another thing I kind of stole from Sinatra or tried to steal from the Sinatra community
[772.96 → 779.14] was kind of this, uh, which actually, actually it applies better even to JavaScript than Ruby
[779.14 → 789.90] is really kind of, you know, forcing myself to keep the core library as small as I possibly can.
[790.40 → 798.58] Um, and you know, the Sinatra guys between 0.9 and 1.0, they removed more code than they added.
[799.08 → 805.14] Um, and I think that that was kind of, I took that, I mean, it makes even more sense on the client side
[805.14 → 809.44] when, when you actually have to download the file, if you can eliminate as much code as possible
[809.44 → 815.28] and make the core as tight as possible, then people can use it in more places and, um,
[815.42 → 817.30] only bring in the functionality they need.
[817.72 → 821.64] So a little while back I was like, okay, how am I going to do this?
[822.00 → 829.64] And then the beautiful power of JavaScript functions and closures dawned on me.
[829.64 → 834.60] And I realized that, you know, a, a SAMI application is actually just a function
[834.60 → 837.82] or a SAMI application block, as I like to call it.
[838.06 → 844.50] Um, even though it's a closure, it's really a function that gets applied to this SAMI application object.
[844.76 → 848.96] So that's an application, but why can't plugins just be the same thing?
[849.02 → 854.16] So plugins are really just functions that are named like SAMI dot something.
[854.16 → 861.16] And all you're doing is when you do this dot use is you're applying the function that is that plugin
[861.74 → 868.18] to the, to the application that you're including it in and adding all the helpers or whatever else you need.
[868.80 → 874.78] So SAMI has this idea of helpers, which, you know, you can use inside your routes and inside your templates.
[875.26 → 880.92] Um, and a plugin for the plugins for the most part, uh, add, add those helpers.
[880.92 → 887.78] So right now, um, the main, the main plugins that I kind of use on a daily basis, we have, we have a bunch
[887.78 → 892.62] and they're all, most of them are, um, user contributed, and I'm happy.
[892.78 → 899.54] I, I would love to get more people adding them and extracting functionality that common functionality into these plugins.
[899.82 → 903.92] But, um, the main ones right now that people use are kind of the emulating plugins.
[903.92 → 910.48] And so we have a, a moustache plugin that's just basically kind of, a thin wrapper around, uh,
[910.86 → 914.58] Jan Land hart's and Chris Monstrous's mustache.js.
[914.92 → 920.02] And then there's a Haml.js one, which is Tim Caswell from the Node community.
[920.02 → 925.12] His Hall, um, client side Hall parser is also having a thin wrapper.
[925.66 → 931.20] Uh, I actually just worked on this one that Ruby and Rails guys would appreciate.
[931.20 → 940.68] But in building this kind of bigger application, I was, uh, yearning for some of the form helpers that, uh, Rails has.
[940.84 → 946.80] Specifically, like, being able to have a text field and have it be autopopulated with an object.
[946.80 → 958.90] So there's this new Sammy. Form plugin that I just added recently that kind of tries to replicate some of the, um, form helper functionality that Rails has, but as small as possible.
[958.90 → 963.46] And it's really just putting DOM nodes into strings and stuff like that.
[963.86 → 971.84] Um, but yeah, there's the one, the one that I actually have been around for a while, but people don't actually know about,
[971.84 → 976.40] which I'm going to pull back into core, is this Sammy, uh, Google Analytics plugin.
[976.90 → 983.30] Um, because you can actually track Google Analytics, uh, or track, you know, hashtags and stuff like that through Google Analytics.
[983.30 → 989.14] They have a thing mainly for Flash, but it's pretty easy to adapt for Sammy apps, too.
[989.14 → 999.38] One of the ones that I'm excited about is, uh, nested parameters allows you to have those rich, deep object caches if you build your forms a certain way, a la the Rails approach.
[999.92 → 1008.58] But talk a minute about, uh, Sammy storage and Sammy cache and, and how you see a front-end framework like this paired with the back-end, uh, persistence layer,
[1008.66 → 1011.48] like, uh, something you would see from Couch or one of the other NoSQL stores.
[1012.04 → 1012.82] Sure, sure.
[1012.82 → 1026.80] So Sammy. Storage, um, is like a, a basically a really simple wrapper around all the or a lot of the options for client-side storage.
[1026.80 → 1041.92] So it can write to cookies, it can write to, um, HTML local storage and HTML session storage, and it can also write to jQuery data and memory, um, just straight up, basically just a hash.
[1041.92 → 1048.34] But the idea was that all of these different, um, storage engines kind of have different APIs.
[1048.70 → 1058.06] So I wanted to try to unify them into a simple, basically key-value store API that I could use for storing any local data in an app.
[1058.44 → 1067.60] Um, I also want to kind of add, uh, I'm looking forward to adding the kind of SQL storage that WebKit has now and add that as a back-end, too.
[1067.60 → 1081.78] But, um, like you were saying, it, it really, it's really for local storage and almost to allow you to kind of do sessions, um, and stuff like that and caching in, uh, in the browser.
[1082.22 → 1086.86] For back-end storage, I mean, in the end, it's all just JSON being stored as key values.
[1086.86 → 1108.52] So, um, so, ideally, the API could be extended to, um, to also Couch DB or any other kind of these, uh, HTTP or RESTful stores like Couch or even just a, a general Rails app that you have a, a RESTful resource, and you're pushing stuff up.
[1108.52 → 1111.00] The only difference is that would be asynchronous.
[1111.64 → 1116.84] So dealing with that and how you deal with asynchronous storage is kind of a, a different question.
[1117.02 → 1118.94] But I'm, I'm, I'm looking to answer that.
[1119.42 → 1126.28] Um, in general, uh, SAMI plays really well with these RESTful and JSON, server-side JSON stores.
[1126.48 → 1138.30] And, um, Couch DB specifically is just such a cool, has such a cool, uh, API and just such a it just seems to fit the web and SAMI so well.
[1138.30 → 1147.68] That, uh, I, I think it's kind of the first choice for a lot of people who have been developing these SAMI apps to just kind of use Couch because it's, it just kind of works.
[1148.20 → 1153.56] Um, and I'm pretty happy about that, that marriage, to say the least.
[1154.48 → 1161.52] You know, I don't think I got the, uh, the play on words with the name until I checked out your, the Twitter page, SAMI underscore JS on, on Twitter.
[1161.72 → 1163.46] It's, uh, Sammy Davis Jr., right?
[1163.98 → 1164.66] Yep, yep.
[1164.66 → 1166.04] As opposed to, to Frank Sinatra.
[1166.38 → 1166.96] That's a nice one.
[1166.96 → 1167.18] Yeah, exactly.
[1167.30 → 1167.92] The Rack Pack.
[1168.30 → 1172.72] Talk a minute about, you know, building a successful project, uh, open source project.
[1173.20 → 1179.60] Um, do you think open source projects stand on their own merits or is it key in finding influential?
[1179.60 → 1183.88] Like you mentioned, uh, Alex Lang and, and, uh, I've seen Jan talk about SAMI before.
[1184.48 → 1190.72] What's the, uh, I guess the, the recipe for getting a project over the hump and, and to a wider audience?
[1191.54 → 1193.66] Yeah, that's a that's actually a perfect question.
[1193.66 → 1199.18] And I, I don't know if I have the answer because I don't know if SAMI is quite there yet.
[1199.18 → 1203.68] But, um, I think, I think there are a lot of things.
[1203.76 → 1214.02] I think, um, one of the main things that I, I think for, at least for me, browsing open source projects, one of the things is documentation.
[1214.02 → 1218.56] And I think, um, I have pretty decent documentation for SAMI.
[1218.60 → 1222.78] And I think that's one of the first things that I really worked hard on, and I'm continuing to work on.
[1222.78 → 1244.40] Um, but a lot of projects, it's, it's really hard for as an end user, if you're, you know, browsing GitHub or just browsing jQuery plugins and whatever, whatever it is to, um, to just really jump into something or trust something if the documentation isn't there.
[1244.40 → 1252.00] And, uh, I think, I think a lot of people neglect that and don't really spend a lot of time documenting their code.
[1252.20 → 1264.60] And it's really, it's time-consuming, but it's totally worth it because when you start documenting, at least for me, I often find that I find holes in my API or find, you know, ways I can make things better.
[1264.60 → 1269.36] Because if I can't really explain it in documentation, then no one else will probably understand it.
[1269.36 → 1273.34] Um, so I think that's one thing.
[1273.40 → 1294.30] I think the other thing is, yeah, I don't, I don't know if it's actually tying yourself to other projects, but I think it is, uh, it's good to, you know, be a part of a make yourself a part of a community and show how, you know, for SAMI, I wasn't the first one that used SAMI with couch.
[1294.30 → 1300.66] Um, it was this guy, Alex, but he kind of, and he kind of, um, realized the potential there.
[1300.78 → 1307.52] But since then I've kind of pushed that and made that, you know, connection or that marriage clear.
[1307.66 → 1315.48] And I think that that's helped out a lot, um, in terms of gaining users and getting some momentum on the project.
[1316.02 → 1321.78] Uh, you know, I know what I'm considering a new open source project, whether I want to use it in one of my projects.
[1321.78 → 1324.90] I think documentation is key, as you mentioned, what's your breakdown?
[1325.02 → 1327.02] How much time do you actually spend documenting SAMI?
[1327.08 → 1329.94] Because SAMI's got some really nice docs that, that talk to the API.
[1330.20 → 1333.88] How much, what's the split between documenting your code and slinging code?
[1335.02 → 1348.52] Yeah, it, it kind of depends, but often, often I'd say it's at least, I spend at least, well, I, I guess if you include, you know, uh, doing the working on the mailing list and responding to questions on the mailing list.
[1348.52 → 1356.56] And responding to GitHub issues and responding to, um, you know, uh, people in IRC and stuff like that.
[1356.64 → 1368.80] If you count all that as like kind of support time and writing documentation, all in that, I'd say it's almost like 40% writing code, 60% support, if not more.
[1368.80 → 1375.32] Um, once you have a project in the wild that people actually use, it's, it's great at the same time.
[1375.40 → 1378.28] It's, it's also time-consuming to actually support it.
[1378.28 → 1390.94] And I think, um, I'd say, yeah, if you want, if you want actually, if you actually want people to use it, which if you're putting stuff out there, either you want people to use it or just putting it out there to kind of put it out there.
[1390.94 → 1405.08] And if you want people to use it, I think the, the key is getting other people involved and getting other people to kind of start, you can eventually start delegating support, but for a long time, it's, it's just you.
[1405.22 → 1417.68] And getting other people involved means that eventual hopeful, eventual, you know, goal of a successful open source project, which I guess it's hard to define specifically, but it really means, you know, having a lot of contributors.
[1417.68 → 1421.34] And getting a lot of people involved more than just using it.
[1421.94 → 1426.90] So if you want that, I think, yeah, it's, it's, it's a lot, it's spending a lot of time documenting.
[1427.16 → 1433.38] And, um, for me, I just kind of write a lot of inline docs and, but also kind of write, try to write these tutorials too.
[1433.60 → 1444.86] And those are all very time-consuming, but in the end, the goal is that, you know, eventually I'll be able to delegate those tasks, I guess, to other people in the community.
[1444.86 → 1445.16] Yeah.
[1446.92 → 1454.40] I was going to dub out and say it because, uh, I think that anyone who's gotten this far into the podcast has got to be just thinking, what is the sweet spots for Sammy?
[1454.54 → 1462.26] Like at what point do you decide to turn over a, a JavaScript functionality to Sammy and why, where does, where does it really fit into an application?
[1462.90 → 1463.12] Sure.
[1463.12 → 1473.06] Um, for me, I wouldn't, I wouldn't necessarily suggest that someone takes an application that's, you know, totally working and rewrite it for Sammy.
[1473.06 → 1487.66] I think it's in general, I think it's more of a, uh, it works better to start with it, um, rather than, you know, try to force a lot of applications into it.
[1487.66 → 1497.10] However, um, it doesn't mean that you have to have your entire, if you're writing like a big Rails app, it doesn't mean that you have to have, or a big, any kind of big server side app.
[1497.20 → 1501.82] And you have kind of like, uh, a lot of different pages and features on your site.
[1501.92 → 1504.28] It doesn't mean that the whole site has to be Sammy.
[1504.40 → 1517.30] In fact, um, at my current position, um, I, we've, we've begun integrating, um, people's, I mean, at Paperless Post, we've begun integrating, uh, Sammy into different parts of our application.
[1517.30 → 1527.08] So it's not like the entire web app, which is pretty feature rich and has a lot of different parts of the site are all Sammy JS.
[1527.40 → 1534.20] But we noticed that there are kinds of these smaller applications within the larger application that we're using it for.
[1534.50 → 1541.26] So for example, we have kind of like an inbox system where you manage the invitations and stuff like that you've gotten.
[1541.26 → 1552.98] And there it's like kind of, oh, this is a perfect use for Sammy where, you know, you're navigating folders, you're navigating, um, different pieces of the invitation, and you're going to details.
[1552.98 → 1557.02] And it, it just, it's a stateful thing that we can exist on a single page.
[1557.02 → 1560.92] And that's almost like the perfect, perfect use case for Sammy.
[1561.60 → 1563.34] So there, yeah, sorry.
[1563.34 → 1569.68] It's just to continue on, on that thread, you know, it's, I love how Sammy is not an all or none proposition, right?
[1569.78 → 1580.48] So with other JavaScript frameworks like Sprout Core and some of these others that implement full-blown MVC in the client, you know, you kind of start with either a JavaScript entry point or you don't.
[1580.48 → 1591.48] With Sammy, you can come into an existing application and say, you know, I think we could take these parts of the application and really organize them and maintain state better just by dropping in a Sammy application on this page.
[1591.48 → 1591.76] Totally.
[1592.56 → 1592.86] Yeah, I agree.
[1593.54 → 1594.18] Totally, yeah.
[1594.30 → 1600.06] And I, I think, I think the key with that is that, um, or one of the keys of that is that it's pretty small.
[1600.06 → 1608.50] So, I mean, when you compress it, I forget the number as of today, but it, it's, you know, it's like less than 15K or less than 20K.
[1608.58 → 1612.60] And that, that makes a big difference for when you're, you know, building these big apps.
[1612.80 → 1621.42] If you want to include something, you know, if you want to include something like jQuery UI right now, that's going to be, you know, 50 to 500K almost.
[1621.84 → 1628.20] So if you're thinking about something like that, it's pretty, it's kind of like a non-issue to include something like Sammy that's sort of small.
[1628.64 → 1635.76] And because of that, I think it's really cool to be able to just bring it in piece of the application that I'm working on, the big application I'm working on.
[1635.76 → 1641.72] I've been bringing in, you know, piece by piece and kind of replacing or using it for this kind of smaller applications.
[1641.72 → 1645.52] But it also, I want to point out, we were talking about Couch before.
[1646.12 → 1654.18] And in that way, if you're building kind of these, what I like to call this kind of like full client-side applications where either, yeah.
[1654.18 → 1660.46] And I know some people have been using it in, within Phone Gap too, and within iPhone structure.
[1660.62 → 1661.60] And that's awesome.
[1661.60 → 1674.70] But within Couch and the Couch app framework, it's pretty awesome because it just allows you to kind of add structure instantly to data that you have in your database.
[1674.70 → 1682.64] And to kind of this building an application that exists entirely on the client side, which is something I'm really excited about.
[1683.66 → 1685.24] You really have the choice in emulating.
[1685.36 → 1690.68] You mentioned Moustache and Halls and some of the others out there.
[1690.74 → 1697.44] But you really have the option still to use server-side emulating if you want to do that as well and just render partials in line.
[1698.40 → 1700.56] What are some of your other JavaScript frameworks?
[1700.66 → 1702.50] I know this one's built on top of jQuery.
[1702.50 → 1708.10] What about things like underscore.js and some of the others that are jQuery add-ons?
[1709.06 → 1709.26] Yeah.
[1709.66 → 1709.92] Yeah.
[1710.02 → 1711.92] I think underscore is really cool.
[1712.14 → 1713.94] That's actually represent.
[1714.04 → 1722.16] That's another New York City JavaScript guy, Jeremy, who built that and also CoffeeScript.
[1722.42 → 1727.12] And he's obviously pretty prolific and does some pretty awesome stuff.
[1728.30 → 1728.42] Yeah.
[1728.42 → 1748.32] I mean, the cool thing is because it's really just a jQuery plugin and I really tried to make it as – use as few global namespaces as possible and make it as, I guess, you could say, you know, it doesn't really overlap or hurt to include it.
[1748.32 → 1759.24] I tried to make it really easy for you to build it with other UI components, jQuery components or underscore or whatever you want.
[1759.24 → 1768.88] Or even, you know, touch, which is the iPhone library that's built on top of jQuery too.
[1768.88 → 1780.62] Even though it has its own hash kind of navigation system, you could easily use kind of the I guess, the, you know, the UI elements that come with that too.
[1780.62 → 1783.82] But as you said, server-side emulating works too.
[1783.98 → 1799.14] And I've done that in a bunch of cases where we're really just rendering full HTML and using Same almost as kind of just a – it's really just a controller to control the navigation structure and control the elements that are going to be populated onto the page.
[1799.14 → 1813.98] I think – I think actually you bring up – when you mentioned emulating, I wanted to mention that it's actually – that's the – right now we're at Same 0.5.3, and I'm going to get 0.5.4 out hopefully in the next couple of days.
[1814.50 → 1820.38] But I've been wanting to hit 1.0 just because I know a lot of people are already using it in production.
[1820.90 → 1827.46] And according to Tom Preston Warner's semantic versioning spec, if someone's using it in production, it should be 1.0.
[1827.46 → 1829.32] So I feel a little bad about that.
[1829.90 → 1833.00] So I'm hoping that we can hit 1.0 pretty soon.
[1833.52 → 1845.70] And kind of the big thing that I want to fix for 1.0 is the emulating system because I think right now though it works, it doesn't do as much as I wish it could.
[1845.82 → 1850.40] And it doesn't actually – we were talking about support before.
[1850.40 → 1868.16] And from a support perspective, I've been spending – I'd say out of the 60% time that I spend on support, I spend 40% of that – I don't know, like 50% or maybe even 60% of that time dealing with questions around the emulating system and rendering and partials and stuff like that.
[1868.16 → 1873.70] So that's kind of a smell to me that we should do something about it.
[1873.70 → 1887.72] So I've been kind of stealing ideas and building up a kind of interesting – what I think will be an interesting approach to how we handle temptings based on some of the work that Dave Furs is doing for Labs.
[1887.72 → 1894.66] And – not Labs, sorry, Sexy JS, which is a cool kind of sequential AJAX plug-in.
[1895.24 → 1916.22] And also kind of the stuff that Tim Caswell has been doing, Creation for the Step library and the Do library and how he does these fascinating kind of work with continuations and using functions to kind of progressively – to kind of progressive AJAX, I guess you could call it.
[1917.72 → 1921.44] So tell us about Scoff and making bacon.
[1923.08 → 1927.98] Yeah, so I mean Scoff was awesome.
[1928.30 → 1929.42] I'm sorry you guys weren't there.
[1929.64 → 1930.60] You would have had a great time.
[1932.74 → 1942.86] I can't say enough how awesome Chris Williams or Vujutiki got on Twitter to organize the whole thing and how awesome a job he did.
[1943.86 → 1944.66] I don't know.
[1944.66 → 1948.56] I've been to a lot of conferences and a lot of regional conferences and a lot of bigger conferences.
[1949.30 → 1962.60] And this Scoff is really like kind of this perfect middle where it feels almost like a Hankerson but as opposed to kind of young guys or guys who are not that experienced or just kind of trying to learn.
[1962.60 → 1973.00] It feels like there are a lot – everyone's there to learn but everyone there is – I mean I can't speak for myself but everyone I met was some kind of – on some kind of other level of awesome.
[1973.00 → 1984.12] And, you know, between Brendan Eich and Crockford who kind of bailed really early, but every single talk was just awesome.
[1984.68 → 1991.30] And even beyond the talks, just one of the best things I think about Scoff is the hallway track as you can call it.
[1991.30 → 2001.74] And I just spent a lot of time hanging out with a bunch of really, really talented JavaScript developers and hearing about their projects and listening to their opinions.
[2002.06 → 2004.26] And it was awesome.
[2004.78 → 2009.70] If you didn't see, I did – my talk was a little off subject.
[2009.70 → 2028.42] Chris kind of dared me to do – or not dared me, but we had a kind of long ongoing challenge going on that he said – he told me that if I talked about bacon or make – if I made bacon on stage at Scoff then he would let me be a keynote speaker.
[2029.78 → 2035.02] So we worked out something and unfortunately the hotel wouldn't actually let us cook bacon on stage.
[2035.02 → 2056.74] But we – I did a little presentation and I tried to actually tie it back into the JavaScript community about how Heritage Foods and the whole slow food movement, the JavaScript community and the development community in general should take some ideas about sustainability and knowledge and respect from that community too.
[2057.60 → 2058.96] In general, it was a lot of fun.
[2058.96 → 2071.58] I think you've probably seen some pictures and some blog posts, and it's – I'm still – it's almost been a week since it – or actually as of tonight it'll be a week since it started.
[2071.78 → 2078.06] And I'm still not done digesting or processing all the information that I got out of it.
[2078.56 → 2081.52] A lot of bacon flying around in the IRC channel right now too.
[2081.52 → 2089.48] So talk a minute about this renaissance in JavaScript that we've gotten over the – I guess the last few months, maybe over a year.
[2089.90 → 2098.04] It seems like we've got it on the client with jQuery and Prototype before that and some of these other frameworks that made JavaScript suck less.
[2098.12 → 2103.84] But now it's really being embraced as a newish language and being used on the server.
[2104.12 → 2108.28] And see that you guys have a New York's nyc.js meetup.
[2108.38 → 2109.26] We've got a Dallas.js.
[2109.26 → 2114.18] You see – I mean the thought of the JavaScript meetup five years ago would have just been crazy.
[2115.32 → 2115.60] Totally.
[2115.90 → 2117.18] So what's fuelling all of this?
[2117.92 → 2119.30] I think there are a lot of things.
[2119.44 → 2129.06] I think one, the simplest explanation is just that browsers are just getting exponentially faster.
[2129.56 → 2133.80] So Chrome and Chromium is just an order of magnitude faster.
[2134.38 → 2135.96] At least for a little while it was.
[2135.96 → 2139.82] Everybody else is slowly catching up but faster than everyone else.
[2139.94 → 2143.56] And that was already faster than every browser a year before that.
[2143.98 → 2154.90] So I think for client side at least, now that we can actually build kind of really complex applications and even 3D and OpenGL and Canvas stuff,
[2154.90 → 2171.10] which we couldn't have even dreamed of two years ago, people are starting to see, oh, we don't have to build a Java app, or we don't have to necessarily build an entire Flash application to sit on top of our server-side application.
[2171.10 → 2182.00] And because of that, it's just like, wow, JavaScript developers, there's actually a need and desire for talented JavaScript developers now that there wasn't two years ago.
[2182.00 → 2189.02] On the server-side JavaScript has actually been around for a really, really long time.
[2189.48 → 2192.24] It's just almost the same thing.
[2192.40 → 2200.14] There was never a – everyone kind of thought it was a joke because if you ran Rhino, you know, everyone says Ruby is pretty slow.
[2200.14 → 2203.84] But Rhino was like an order – like another level of slow.
[2204.02 → 2216.10] Like if you tried to run, I guess, XJS or NVIC.js or one of these really early server-side JavaScript frameworks, it was really slow.
[2216.24 → 2224.78] And it was fun because, hey, I'm programming JavaScript on the server, but there wasn't any actual – you know, you couldn't actually use it in production.
[2224.92 → 2225.82] It was just too slow.
[2225.82 → 2231.90] But now with Node, which is also based on, you know, Chrome's V8 too, the speed is just incredible.
[2232.04 → 2240.28] And not only speed, but this idea of kind of invented applications is kind of I think where a lot of people think the web is heading,
[2240.82 → 2253.70] which is, you know, kind of these real-time or collaborative web applications that Node and this kind of server-side and pairing in with the client-side frameworks allow you to have.
[2253.70 → 2266.96] But I think what I would say what I really love about the JavaScript community is it brings together some of the best minds in all these different communities.
[2266.96 → 2279.36] Whereas if, you know, you go to a Ruby meetup, or you go to a PHP meetup, everyone's kind of just doing – everyone's doing something different and working on different projects, but everyone's kind of doing very similar things, you know.
[2279.62 → 2286.42] Especially in the Ruby world, it's like, okay, you go to a Ruby meetup and 90% of the people are doing Rails.
[2286.42 → 2289.86] And if they're not, then they're working on something else, or they're teaching.
[2290.76 → 2299.80] And, you know, obviously it's great to talk to people who have a lot of things in common, but there's not as many new ideas, I think, being tossed around as in the JavaScript community.
[2299.90 → 2311.94] In the JavaScript community, like I went to jQuery Cone last year and Scoff this weekend too reminded me of this, but it's just, you know, you have so many people whose day job isn't necessarily full-time JavaScript.
[2311.94 → 2322.50] It might start becoming full-time JavaScript, but, you know, you have people from the .NET community, you have people from the PHP community, and everyone kind of has their own ideas that they're bringing to the table.
[2322.88 → 2335.00] And beyond that, some people are using jQuery, some people are using prototypes, they're the Cappuccino guys, and it's just like – it's just so cool because everyone has so many different ideas to share and really learn from each other.
[2335.48 → 2339.74] And it's just a really exciting thing to be a part of right now, I'd say.
[2339.74 → 2344.46] Yeah, absolutely. I think open source is a pretty wild world to be in, and there's lots of movement.
[2344.78 → 2347.88] But on that note, and open source software, what's on your radar?
[2348.00 → 2353.78] What's got you excited about the next big thing or whatever you're really excited about in open source?
[2353.86 → 2354.36] What's on your radar?
[2355.22 → 2356.92] Yeah, that's a good question.
[2356.92 → 2369.32] I think right now I'm kind of – after Scoff, one of the big things that I took away was kind of performance and really thinking about front-end performance.
[2369.32 → 2384.98] And some of the things that tie into that are Kyle Simpson's or Testify's Labs framework, which is kind of like a progressive download and loading framework, which is pretty cool.
[2385.08 → 2388.12] And he says he's working on some even cooler stuff after talking to him.
[2388.12 → 2392.18] And so I'm really keeping an eye on that and hoping I can bring that into some projects.
[2392.76 → 2395.88] I'd say, you know, Couch App, I've been a fan of for a while.
[2395.88 → 2409.54] But J. Chris, one of the main Couch TV guys, and Yon are both working on making Couch App like an actual usable thing and kind of building frameworks within Couch App.
[2409.72 → 2416.78] And this evenly framework that's part of Couch App now is kind of – steals some ideas from Sammy.js.
[2417.08 → 2420.22] And at least they admitted that, which is cool.
[2420.22 → 2425.36] But it's pretty cool, and it has some pretty cool functionality built into it.
[2425.88 → 2434.44] I think – I mean, I'm still keeping an eye on Node, and I'm ready to – I don't think I'm ready to jump ship from Ruby anytime soon.
[2434.62 → 2438.64] But I've been playing around with it for, you know, over a year now.
[2438.64 → 2450.42] And it's – I'm looking forward to it actually stabilizing so that, you know, a lot of people can start building, like, real – a real standard lib almost on top of it.
[2450.42 → 2457.08] So that, you know, people who actually want to use it for full-blown applications can really, really make use of it.
[2457.42 → 2461.04] I think on top of Node, there's the FAB framework.
[2461.30 → 2468.04] Jed Schmidt's FAB framework, and he talked about it at – he gave an actually an awesome, awesome presentation at Scoff.
[2468.04 → 2473.78] That he gave a presentation actually at NYC.js about four or five months ago.
[2474.30 → 2478.64] And I talked to him about it then, and we watched it, and I think everybody kind of left and was like, oh, what?
[2479.62 → 2491.48] Kind of had a funny reaction to it because it's a very interesting style of basically turning JavaScript into almost like a lisp – a really lisp type of DSL.
[2491.48 → 2500.40] But he's worked on it a lot since then, and his presentation at Scoff was pretty incredible and really did an awesome job of explaining how it worked.
[2500.76 → 2504.28] So I urge anyone to check that out if they're interested in it.
[2504.76 → 2512.64] Now, I'm actually really excited about doing the show notes when we do this episode in post just to find all the links to a lot of the cool projects that you mentioned.
[2512.82 → 2519.36] Because, you know, Adam and I tend to stay on the bleeding edge, but there are a lot of projects that you mentioned that aren't on my radar yet.
[2519.36 → 2521.22] And I'm interested in checking them out.
[2521.48 → 2521.68] Yeah.
[2522.04 → 2526.30] When – making note to get the one from TP-Dubs is – what was that?
[2526.66 → 2530.14] Again, Aaron, what did you say that it was his list of –
[2530.14 → 2531.22] Oh, yeah.
[2531.62 → 2532.98] That's semantic versioning.
[2533.40 → 2533.96] That's semantic versioning.
[2534.06 → 2535.02] That's semver.org.
[2535.38 → 2536.64] Semver.org, yeah.
[2537.12 → 2547.74] It's – I mean, when he put it out there, it was kind of like a – you know, kind of just pulling together ideas of, you know, how people have been doing it for a while.
[2547.74 → 2550.54] And I don't think even he would say that it's something new.
[2550.54 → 2566.94] But it's cool for this kind of – for me as a young developer and I think for everybody else who kind of maybe hasn't been around in the open source community for forever to kind of put kind of meaning behind the X.Y.Z numbers that everyone uses.
[2566.94 → 2571.34] Yeah, I know we're using that as a guide over on the Twitter gem and some others.
[2572.14 → 2575.68] And it's not – like you mentioned with Sammy, it's not always easy to do.
[2575.82 → 2582.86] But I'm glad there's, you know, kind of framework out there for giving meaning to the ones, zeros, majors, and minors.
[2583.04 → 2583.78] Yeah, exactly.
[2583.78 → 2585.64] Well, thanks for joining us today.
[2586.60 → 2589.64] Really excited about using Sammy on a couple of different projects.
[2589.82 → 2595.46] And when we stumbled across it, we just wanted to have you on and share the word with the rest of the audience.
[2595.58 → 2596.56] We appreciate you taking the time.
[2597.22 → 2597.48] Awesome.
[2597.62 → 2598.48] Thank you guys so much.
[2599.24 → 2602.14] I'm a big fan of the show too, so excited to be on.
[2603.12 → 2603.48] Awesome.
[2603.48 → 2612.76] Thank you for listening to this edition of The Change Log.
[2613.84 → 2620.56] Point your browser to tail.thechangelog.com to find out what's going on right now in open source.
[2621.78 → 2630.30] Also be sure to head to GitHub.com forward slash explore to catch up on trending and feature repos as well as the latest episodes of The Change Log.
[2633.48 → 2663.46] Thank you.
[2663.48 → 2665.48] Thank you.
