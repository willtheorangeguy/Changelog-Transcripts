[0.00 --> 6.70]  Bandwidth for Changelog is provided by Fastly. Learn more at Fastly.com. We move fast and fix
[6.70 --> 11.42]  things here at Changelog because of Rollbar. Check them out at Rollbar.com. And we're hosted
[11.42 --> 17.34]  on Linode servers. Head to linode.com slash Changelog. This episode is sponsored by our
[17.34 --> 22.18]  friends at Rollbar. How important is it for you to catch errors before your users do? What if you
[22.18 --> 26.80]  could resolve those errors in minutes and then deploy with confidence? That's exactly what Rollbar
[26.80 --> 31.60]  enables for software teams. One of the most frustrating things we all deal with is errors.
[32.10 --> 37.70]  Most teams either A, rely on their users to report errors or B, use log files and lists of errors to
[37.70 --> 43.28]  debug problems. That's such a waste of time. Instantly know what's broken and why with Rollbar.
[43.64 --> 49.04]  Reduce time wasted debugging and automatically capture errors alongside rich diagnostic data
[49.04 --> 53.76]  to help you defeat impactful errors. You can integrate Rollbar into your existing workflow.
[53.76 --> 58.28]  It integrates with your source code repository and deployment system to give you deep insights
[58.28 --> 63.66]  into exactly what changes caused each error. Give Rollbar a try today at no cost to you.
[63.94 --> 69.72]  No credit card is required. Our listeners get access to the bootstrap plan with 100,000 events for free
[69.72 --> 74.44]  for 90 days. To get started, head to rollbar.com slash Changelog.
[83.76 --> 93.94]  Welcome to JS Party, a weekly celebration of JavaScript and the web. Tune in live on Thursdays
[93.94 --> 100.48]  at 1 p.m. Eastern, 10 a.m. Pacific at changelog.com slash live. Join the community and Slack with us
[100.48 --> 105.22]  in real time during the show at changelog.com slash community. Follow us on Twitter. We're
[105.22 --> 114.88]  at JS Party FM and now onto the show. Hello world. This is JS Party where we're throwing a party every
[114.88 --> 121.08]  week about JavaScript and the web. My name is Jared Santo and hey, it's the pre-party this week for next
[121.08 --> 128.32]  week's live party at JSConf. If you're going to JSConf, do not miss it. We will have four awesome
[128.40 --> 134.58]  JS Party panelists live at lunch hour on Tuesday, August 21st. If you're not going to JSConf, well,
[134.58 --> 139.94]  I guess emoji sad face, you're in the same group as me. I sadly will not be there, but K-Ball, Nick,
[140.56 --> 146.84]  Suze, and Feras will be live on stage. Do not miss that, but we have a show for you today and as
[146.84 --> 153.42]  always, awesome panelists. So welcome back, Chris. What's up, Chris? Hello, how you doing? All good.
[153.56 --> 158.18]  Nick Niecy is here. What's up, Nick? Hello. Tell the people all you're doing at JSConf next week so we
[158.18 --> 165.32]  can all pity you. Well, I'm part of the JS Party live panel and then immediately following that,
[165.40 --> 172.82]  I'm doing a Track B talk. The title is No Time for Types. It's secretly about TypeScript though.
[173.50 --> 177.90]  And then I'm also there with the TalkScript podcast doing interviews.
[177.90 --> 184.46]  So very busy and nerve wracking, of course. K-Ball also here. K-Ball, you're going to be
[184.46 --> 189.78]  running the JS Party show next week. What's up, man? You got it. I'm excited to be emceeing that
[189.78 --> 196.22]  JS Party live and then I will also be interviewing folks for JS Party. So if you're going to be there,
[196.32 --> 199.68]  especially if you're a speaker, but even not, you have something awesome you want to talk about,
[199.76 --> 206.06]  come find me in the hallways. There you have it. So for this show today, we have a few new things.
[206.06 --> 209.96]  We're always liking to experiment here on the show and find out what works well, what doesn't
[209.96 --> 215.60]  work well. You know, that old fashioned iteration that we developers love so much. So I've kind of
[215.60 --> 220.46]  ginned up a few new segments that we're going to give a try. If you like these, let us know. If you
[220.46 --> 224.68]  think these are the worst ideas ever after having listened to them, please tell us. We want a show
[224.68 --> 229.64]  that is good, not necessarily a show that is just new and unique, but we're going to try out a few
[229.64 --> 235.14]  different things this week and see how it goes. The first segment we are calling Story of the Week.
[235.14 --> 241.52]  Now, the way this works is we have all found different stories around the ecosystem throughout
[241.52 --> 245.80]  the week, maybe even going back a little bit further than a week. No big deal. But what's
[245.80 --> 250.18]  the biggest thing that happened this week or the most important news, maybe just to you personally,
[250.26 --> 256.40]  maybe for everybody involved, we will all share a new story and we will try to convince one another
[256.40 --> 262.60]  why it's a big deal, why it's important, why perhaps it's the story of the week. So let's give it a
[262.60 --> 265.76]  shot. Nick, you are up first, my friend. What's your story of the week?
[266.14 --> 272.22]  So mine is probably one that falls in the not actually this week part because I was really
[272.22 --> 278.36]  struggling. It seems like a slow week in the JavaScript world, at least. And so I was going
[278.36 --> 286.30]  back through the recent things that were popular on Twitter and I found this tool, NDB, by Google
[286.30 --> 293.58]  Chrome Labs on GitHub. And it's a NPM module that you can install that vastly improves debugging node
[293.58 --> 299.20]  with the Chrome DevTools. And so if you haven't done that before, it's really cool. I think we
[299.20 --> 303.94]  might've talked about it on a previous episode, but you can type in like node dash dash inspect
[303.94 --> 311.64]  dash BRK or dash dash inspect, and then give it a command to run or a file to run in node. And it will
[311.64 --> 317.38]  open up or it'll give you a link that you can paste into the Chrome DevTools. Chrome Canary,
[317.50 --> 323.90]  at least also immediately puts a dedicated node DevTools button in your DevTools if you have that
[323.90 --> 331.30]  open. So that's pretty cool. Completely unrelated to this, what this is, is a node module that
[331.30 --> 337.00]  will streamline that process for you a little bit. It'll automatically open up the Chrome DevTools
[337.00 --> 342.76]  and you can actually open it for your projects. You can just say NDB space period, and it will
[342.76 --> 348.70]  open it up for that project. And I don't know if it's like broken or if I'm not running it correctly,
[348.70 --> 354.80]  but it actually lists out all of the scripts for my package.json in there with a little run button
[354.80 --> 360.44]  next to them. But when I try and do that, I can't actually get it to run. So not sure if that's just
[360.44 --> 364.44]  broken or the way that I had it, but if that works, that would be really cool because I'm constantly
[364.44 --> 369.20]  having to go look up what scripts are actually available in whatever project and just having
[369.20 --> 373.42]  them listed there and immediately being able to run them kind of as like a dashboard that also does
[373.42 --> 378.48]  the debugging would be really cool. And then finally, the big thing that this does that's
[378.48 --> 383.80]  way better than just running node with the dash dash and spec flag is typically I'll want to debug
[383.80 --> 388.94]  scripts. Like I'll want to actually be running TS node or I want to be running gulp or grunt or something.
[388.94 --> 395.56]  Uh, and I want to be able to debug that. And if you want to do that with a node, you have to run
[395.56 --> 401.30]  node and then point to the binary for that. So like gulp, you'd have to go look in your node modules
[401.30 --> 407.60]  directory and the dot bin directory, and then, uh, the gulp script there. And then, uh, it will run for
[407.60 --> 413.36]  that and you can set break points in there. This will just automatically let you say NDB gulp, uh,
[413.36 --> 418.16]  test or whatever. And it will immediately set that up and it sets up watchers, uh, for all of the
[418.16 --> 423.64]  child processes that might get kicked off in there. The other cool thing that it does is it, um,
[424.54 --> 429.18]  anything that's not in your sources directly, like anything that's, uh, in your node modules,
[429.26 --> 435.00]  for example, uh, it black boxes that by default. So that means that when you're looking at a stack
[435.00 --> 439.76]  trace, you don't actually see the code from your node modules directories. You just see the code that
[439.76 --> 443.56]  you're actually running and debugging. And you just kind of assume that the node modules are correct.
[443.56 --> 448.10]  I'm just looking at this now and this thing actually looks pretty cool. At first I was like,
[448.18 --> 451.74]  well, what's the difference between this and just using Chrome dev tools, but it looks like it,
[451.74 --> 458.60]  it definitely streamlines things. Like if you want to, uh, debug tests say in Mocha and, um,
[458.60 --> 465.60]  you want to do that with Chrome dev tools, you have to call the not, not Mocha, um, executable,
[465.60 --> 472.36]  but the underscore Mocha executable, because this is a child process that, that Mocha launches and
[472.36 --> 479.98]  you can't just attach to, you know, Mocha because the, the inspector won't know that you're actually
[479.98 --> 484.64]  running your tests at the child process. But if this thing actually works, I haven't tried it, but
[484.64 --> 491.88]  I'm, I'm looking at the interface. Um, yeah, that's, that's awesome. This, this is really going to,
[491.88 --> 498.54]  you know, make things a lot easier for a lot of people. Yeah, definitely. And I love that it's,
[498.54 --> 505.08]  uh, Google Chrome lab. So it's, uh, so I would assume going to be well supported going forward.
[505.86 --> 509.36]  I don't know if you can assume that from Google, like Google reader.
[510.14 --> 511.50]  Oh, good point.
[512.84 --> 516.46]  Salt in the wound still hurts. It still hurts. Yeah. Too soon, Jared.
[517.08 --> 518.62]  Too soon. It's been like five years.
[518.62 --> 524.40]  I, I, I am curious what they're using puppeteer for. Um, I, I assume it's just to like launch the
[524.40 --> 534.18]  browser and then basically, you know, launch, um, dev tools and, and fiddle with, fiddle with dev
[534.18 --> 540.42]  tools and stuff like that. Um, that's pretty neat. So yeah, this is, this is really cool. And it just,
[540.56 --> 545.66]  I installed it and it took a few seconds and it works and it's pretty awesome. So cool. Thanks.
[545.66 --> 551.14]  All right. Nick sounds like you might have one vote for a story of the week there. Chris's might
[551.14 --> 554.14]  be phoning for you. Well, Chris, what'd you bring to the table here? What's your story of the week?
[555.06 --> 564.64]  So yeah, uh, slow week. Um, it really was, but, uh, you know, there are babbles, uh, seven is going
[564.64 --> 572.68]  to be released very soon. And, um, if you haven't been keeping tabs on what's happening there, like the,
[572.68 --> 581.44]  the big thing that people are probably going to, um, get up in arms about, um, is that babble is
[581.44 --> 591.56]  deprecating, um, uh, the stage modules. So you can't go in, um, in babble seven and say, um, you know,
[591.74 --> 598.18]  install babble preset stage three or whatever. They're not going to support those anymore. Um,
[598.18 --> 609.30]  they're going to basically expect you to, uh, more or less figure out which features you need.
[609.80 --> 616.72]  Um, you know, I think it sounds like, you know, babble preset ENV will help with that, but, uh,
[616.72 --> 622.70]  it sounds like they're encouraging people to make their own presets. Um, because, you know,
[622.70 --> 630.86]  um, the, the rationale, and there's a blog post on, on, um, their site, it's, uh, like babble JS.io
[630.86 --> 637.82]  or, uh, something. And so there's a, uh, blog post there where, uh, Henry talks about, um, well,
[637.82 --> 644.38]  this is why we're, we're deprecating stages. And, um, one of the reasons is that people will be like,
[644.38 --> 652.30]  hey, how can I use feature X? Um, and then somebody will say, oh, use babble preset stage zero,
[652.30 --> 657.98]  or something like that. And so people install babble preset stage zero, and they don't really
[657.98 --> 664.78]  know what they're getting into. Um, and so if, if, for those that don't also don't know, so stage,
[664.90 --> 672.08]  a stage zero contains features that have not been approved, um, for, for the JavaScript spec and may
[672.08 --> 678.06]  not ever be approved. And so they're, they're very experimental. And if you're using that in,
[678.06 --> 683.66]  in your production code, well, you, you may have kind of coded yourself into a corner, um, because
[683.66 --> 690.28]  those features that you may be using, um, you know, those, you might need to back those out,
[690.28 --> 696.54]  uh, at some point. And so babble doesn't, doesn't want this to happen because I think they, they feel
[696.54 --> 700.84]  like they are partly responsible for, for people doing this because they're making it essentially
[700.84 --> 705.92]  too easy to shoot yourself in the foot. And so there's, they're, they're going to drop these,
[705.92 --> 713.38]  these, uh, presets. And if you need a feature, um, you have to go and basically add the plugin,
[713.68 --> 719.82]  um, or, or again, create your own preset. Uh, so that's kind of a big change. There is a tool
[719.82 --> 726.74]  that they wrote to help you upgrade to babble seven from, uh, I assume just version six, um,
[726.74 --> 733.30]  where they probably will go and see which stage presets you're using and actually go and change all
[733.30 --> 741.24]  your stuff to, um, to use the individual plugins. Uh, it does stuff like there's all sorts of things.
[741.24 --> 747.74]  So it, it, it, it changes a bunch of dependencies. Um, it modifies, uh, if you're using babble with
[747.74 --> 753.14]  mocha, it'll find that in your, in your package JSON, which is really neat. And it'll, it'll change,
[753.14 --> 759.56]  uh, uh, some of the module names. Um, they're now going to publish all of their modules because,
[759.56 --> 765.56]  you know, there's like hundreds of babble modules. They're going to use the at babble, um,
[766.08 --> 772.30]  scope namespace now at NPM. Um, and so you're going to, you're going to be using that instead of
[772.30 --> 778.40]  like babble loader or whatever, babble dash register, you're going to use at babble slash
[778.40 --> 783.16]  forward slash register. Um, and so there's all these things that they're working on to help you migrate.
[783.16 --> 790.90]  Um, but once you're there, yeah, I, I, I haven't read any, any, um, anything that people have
[790.90 --> 796.08]  written, but I assume somebody is going to get really upset and write this. Uh, I hope they don't,
[796.14 --> 800.22]  but you know, things happen, but somebody's going to write this big thing about how this was the
[800.22 --> 804.04]  wrong thing to do and it makes everything really difficult and it was already difficult and blah,
[804.08 --> 810.48]  blah, blah. Um, so I, I want to see how this shakes that, but, uh, I agree with, with the direction
[810.48 --> 817.00]  they're heading, even though it maybe makes things a little more, um, a little more, it makes you
[817.00 --> 820.62]  think a little bit more about how you're using babble and what you're doing. And I don't think
[820.62 --> 827.80]  that's a bad thing. So question, are they, what's, what's the, you said they're going to release soon.
[827.80 --> 833.06]  And I just Googled for, you know, 7.0 babble release or babble seven release. And I see articles
[833.06 --> 837.44]  going back a year saying we're nearing the release. So what, what's different this time? How do we know
[837.44 --> 843.54]  they're actually releasing soon? They just keep saying it. Well, uh, so there's been betas for
[843.54 --> 849.98]  quite a while. Uh, and now they're at like RC two or whatever. So, I mean, it's being actively
[849.98 --> 857.46]  developed. Um, I don't know. I mean, it seems like it's coming pretty soon to me, but, uh, it sounded
[857.46 --> 864.50]  like from the, the release notes that they don't intend to make any more changes. Um, they don't intend
[864.50 --> 870.84]  to add anything or, or fix anything. And this is, uh, or necessarily, uh, unless there's some last
[870.84 --> 876.20]  minute critical deal. Um, it sounds like they're going to release soon. I can't, I don't know,
[876.20 --> 882.58]  but it sounds like it from the, the, the change, uh, the change logs. So it'll be good to get this
[882.58 --> 888.38]  out for sure. Uh, it's been confusing. The website specifically has been confusing, uh, for me for a
[888.38 --> 895.92]  little while now. Uh, like if you go to the docs section of Babel, BabelJS.io, uh, under tooling,
[895.92 --> 899.96]  it talks about all of the different modules that they have, including like Babylon, but you click
[899.96 --> 904.70]  on that and it just takes you to a 404 on, on the live page right now. Uh, but if you switch over to
[904.70 --> 913.10]  the, the pre-release docs, then it's Babel parser and it, it does correctly point you to that. Um,
[913.44 --> 917.82]  so I'm excited for this to get out so that things become less confusing around all of this tooling.
[917.82 --> 924.52]  Yeah. I mean, uh, people are still going to be using Babel six and they're probably going to be
[924.52 --> 929.92]  looking for the documentation and have, have trouble finding it. But sure. Yeah. Again,
[930.00 --> 937.24]  Babel is a, is not a, as far as I know, it's not, it doesn't have any corporate sponsorship directly.
[937.24 --> 943.36]  Um, you know, it's pretty much Henry and, uh, some other people that are, that are, you know,
[943.36 --> 947.22]  volunteering their time to work on it. And so I assume they don't have a whole lot of resources
[947.22 --> 954.24]  to do things like keep old documentation up to date. So I sympathize, but, um, yeah,
[954.68 --> 959.84]  definitely sympathize. I do thought they did have some success at least on open collective in terms of,
[959.84 --> 966.62]  uh, corporate sponsorship, but surely nothing that's like driving, uh, full time. Well,
[966.64 --> 967.48]  maybe they are. I don't know.
[967.48 --> 973.68]  Uh, I think Henry has a Patreon or something that, that he's, he's basically working on open source
[973.68 --> 978.88]  full time now, but, um, you know, you can have all the money in the world and if you don't have,
[979.52 --> 985.18]  you know, there's 24 hours in a day. So if you're the only person working on it, um, there's only so
[985.18 --> 990.98]  much you can do. And, or if, if, if people don't have time to dedicate, you know, you could be flush with
[990.98 --> 998.48]  cash and, and not be able to get much done because, you know, time keeps on slipping, slipping,
[998.62 --> 1004.78]  slipping into the future. Speaking of cable, Hey, your turn, man. What's a, what your story of the
[1004.78 --> 1012.92]  week? Yeah. So the thing I wanted to talk about was, uh, there's been a resurgence of interest and
[1012.92 --> 1019.22]  focus on JavaScript performance. And in particular JavaScript load and parse performance, not that,
[1019.22 --> 1023.90]  you know, we had all this stuff about, okay, is react making it faster to update the DOM or how
[1023.90 --> 1028.42]  fast are these things to, to do a lot of updates. But we've also gotten into this world where
[1028.42 --> 1033.58]  everybody's just adding more and more JavaScript and there hasn't been as much attention on, uh,
[1033.58 --> 1039.86]  sort of what the impacts of load and parse time are. Um, and so we're coming back around. That used
[1039.86 --> 1044.38]  to be a huge issue. Then people forgot about it, coming back around to it. I've seen a ton of
[1044.38 --> 1050.30]  articles in the last few weeks looking at, uh, this, I think, you know, the one that sparked it
[1050.30 --> 1056.38]  was Adi Azmani, uh, from Google did an article on the cost of JavaScript in 2018 that blew up. And he
[1056.38 --> 1064.56]  sort of talked a lot about what, um, how expensive it is, particularly on less than cutting edge devices.
[1064.90 --> 1070.68]  And, um, then there's been lots of follow-ons. How do you do this? What is code splitting good
[1070.68 --> 1074.74]  enough? What, what sort of other things? Uh, another article I saw on this that I thought
[1074.74 --> 1081.48]  was really interesting was looking at the impact of the push to make everything HTTPS.
[1082.12 --> 1089.04]  And the fact that that essentially kills your ability to do, uh, create local caching servers
[1089.04 --> 1093.52]  because local caching servers are essentially a man in the middle. Uh, so it's better for security,
[1093.52 --> 1098.84]  but you know, this article was highlighting, you know, if he was, he did something in rural,
[1098.84 --> 1108.94]  rural Uganda and their connection to the internet is a satellite internet access. And so there's a
[1108.94 --> 1116.22]  ping latency of half, uh, yeah, half a second and lots and lots of dropped packets. And so not being
[1116.22 --> 1123.04]  able to have a local caching server essentially kills their ability to access the internet for a very
[1123.04 --> 1129.98]  large number of things. Um, and so, you know, there are pros and cons to this, but it, it got me
[1129.98 --> 1137.24]  thinking a lot about the people who are not in the first world. And this has come up before on the
[1137.24 --> 1144.10]  podcast. I was this last week I was in Costa Rica. Um, T-Mobile lets you access data for free if you're
[1144.10 --> 1149.32]  on one of their main plans from like a hundred countries, but the speed of access in Costa Rica is
[1149.32 --> 1156.22]  like 2g. So I'm on, you know, a fast phone, I'm on an iPhone, but I had 2g internet and it was amazing
[1156.22 --> 1164.54]  how slow things were and just appallingly bad. And it reminded me how much you get used to
[1165.98 --> 1174.00]  bandwidth being, feeling essentially free. Things are so fast. And so I, you know, this re sparking of
[1174.00 --> 1179.04]  the interest in, you know, we, we actually need to cut down. We need to have a JavaScript budget.
[1179.04 --> 1183.96]  We need to think about the impacts of all these millions of libraries we're pulling in. Uh, we
[1183.96 --> 1188.20]  need to, you know, code splitting is, is a nice thing and our tooling is, is improving for that.
[1188.60 --> 1196.76]  Um, but you know, having all of these things front of mind when we're developing, because if we're
[1196.76 --> 1201.70]  developing things that are not just for folks who are in countries with ridiculously fast internet
[1201.70 --> 1206.86]  access, which the U S even though, well, actually I don't know about rural parts of the U S certainly
[1206.86 --> 1215.16]  in California, you know, even with just mobile access, it's ridiculously fast. Like 4g LTE is
[1215.16 --> 1222.10]  wicked fast, but not everybody has that. Yeah. This is something that's been on top of my mind
[1222.10 --> 1227.38]  recently. We had Ben Halpert on the change log this week talking about dev two, which is a,
[1227.38 --> 1232.00]  a developer community platform he founded. You may know him as the practical dev on Twitter.
[1232.84 --> 1239.20]  And he's taken huge steps to make dev two very fast. Um, but not just fast in the Americas,
[1239.20 --> 1244.66]  but fast all around the world. And so he's really, really leveraging CDNs in order just to bring his
[1244.66 --> 1251.18]  content, uh, as close to the edges, you know, as close to the users as possible. Um, and it made me
[1251.18 --> 1254.92]  rethink a little bit of some of our architectures. Now we try to make change all.com as fast as possible
[1254.92 --> 1259.00]  and as accessible as possible as well. And I think we're doing a pretty good job on that,
[1259.06 --> 1265.84]  but we definitely have the speed of light problem, um, having an American based server and we can serve
[1265.84 --> 1270.50]  those pages really, really fast, but latency is just something we cannot solve. Of course we CDN all
[1270.50 --> 1277.22]  of our assets, but I'm, I'm referring to rendered pages. So something that's a very important. And
[1277.22 --> 1281.58]  often, like you said, Kevin, we just don't think about it very much. Um, maybe cause we're on fast
[1281.58 --> 1287.06]  networks, but also maybe cause we're just geographically close to, you know, uh, AWS is
[1287.06 --> 1293.26]  us East one where most of the internet gets served from. Right. Right. Okay. For my story of the week,
[1294.00 --> 1302.58]  view CLI 3.0. And, uh, as has been said a few times, this was probably a bad week to try out this
[1302.58 --> 1307.26]  segment as there hasn't been huge news in our space this week, but definitely some releases,
[1307.26 --> 1312.74]  definitely some stuff going on conversations being had. One of the big releases, uh, from August
[1312.74 --> 1319.64]  10th, which is pretty close, I guess that's this week was view CLI 3.0. So Evan, you writing on,
[1319.64 --> 1325.22]  uh, on medium about the release says that it's a completely different beast from its previous
[1325.22 --> 1328.86]  version. So this is the command line interface that's built into view or provided with view,
[1328.86 --> 1334.76]  um, specific for that tool set. And this is a trend that we've seen really started, I think,
[1334.76 --> 1340.36]  by the Ember team years ago, having Ember CLI, and we've seen it kind of matriculate across to all
[1340.36 --> 1346.36]  the different front end frameworks. React has one, Angular has one, now view has one. And of course
[1346.36 --> 1352.66]  this is 3.0. So the CLI is not new, but the guts, the feature set, all these things are brand new.
[1353.44 --> 1359.88]  Um, and some cool stuff going on. So the goal of that rewrite that they did was twofold. The first
[1359.88 --> 1365.54]  one was to reduce configuration fatigue of modern front end tooling, which I think we can all agree.
[1365.90 --> 1370.28]  And maybe JS fatigue isn't a thing, but configuration fatigue is definitely a thing.
[1371.00 --> 1375.92]  Um, and this is especially when they're mixing multiple tools together, which is what tends to
[1375.92 --> 1380.50]  happen on the front end. And then they wanted to incorporate best practices in the tool chain as
[1380.50 --> 1387.68]  much as possible. So it becomes a default for any view app. There's a lot more details. Uh, one of the
[1387.68 --> 1392.32]  big things that I noticed was that they've pre-configured web pack features, all that stuff.
[1392.36 --> 1395.94]  You know, if you're going to pre-configure web pack for me, I'm just going to give you a big fat
[1395.94 --> 1400.24]  kiss because I'm going to love that because I do not want to configure web pack. And they've
[1400.24 --> 1404.88]  pre-configured hot module replacement, code splitting, tree shaking, efficient long-term caching,
[1405.06 --> 1410.90]  error overlays, et cetera. So all the good stuff there ready for you to go. Um, the cool thing about
[1410.90 --> 1420.04]  this is they've been very cognizant of developers need to tweak those configurations. So what happens
[1420.04 --> 1426.06]  a lot of times when you have tools that kind of wrap other tools is they will hide, they'll sweep
[1426.06 --> 1430.52]  all of the complexity under the table, which is what we want, right? Because we don't want to deal
[1430.52 --> 1435.34]  with the complexity. We want to provide a better experience, but then when it comes time and you
[1435.34 --> 1441.12]  actually get to using it and you actually need to reach underneath the table and tweak that thing,
[1441.30 --> 1447.46]  you either have to eject, which is basically say, okay, I'm no longer going to stick with this tool.
[1447.54 --> 1455.24]  I'm going to like stop the world and fork it or, uh, vendor it or something like that. Uh, or you just
[1455.24 --> 1458.98]  don't have the option. Like you just can't reach underneath the hood and tweak things as you will.
[1458.98 --> 1465.14]  So they've taken great pains to make this configurable, uh, with no need to eject,
[1465.36 --> 1471.78]  which I know is hard to do and an admirable goal. So, uh, hopefully they've achieved it.
[1471.82 --> 1477.22]  It definitely looks very good. So we'll link up the announcement post. Uh, this seems like big news.
[1477.58 --> 1481.62]  I'm not a view user cable. I thought maybe I was stealing this one from you when I put it into the
[1481.62 --> 1486.14]  document. Cause I know you're, uh, you've been using view quite a bit lately and thought a little bit
[1486.14 --> 1490.88]  would be on your radar. Yeah. There's actually, there's something pretty interesting about it too,
[1491.26 --> 1497.54]  uh, that you didn't cover yet, which is that it adds a GUI access to a lot of the CLI pieces.
[1498.26 --> 1504.92]  So it gives you sort of a, you know, within the ecosystem, like if you're installing plugins,
[1505.52 --> 1511.38]  whatever, normally you just do that on the CLI, NPM, et cetera. It lets you do a lot of that stuff
[1511.38 --> 1516.00]  from a GUI and manages the configuration and updating your package JSON and all that sort of
[1516.00 --> 1524.24]  thing, which to me personally, I couldn't care less cause I'm a terminal guy. But one of the
[1524.24 --> 1531.14]  things that view has historically done very well is making this advanced JavaScript framework feel
[1531.14 --> 1538.04]  accessible to people who do not consider themselves hardcore coders. Um, it's way easier if you're coming
[1538.04 --> 1542.54]  from a design background, it's way easier if you're coming from a less of a coding background,
[1542.54 --> 1547.54]  you know, folks routinely say that the view is, you know, they can pick up view far faster than if
[1547.54 --> 1552.74]  they try to do react or something. And I think this is leaning into that trend as well of saying, Hey,
[1552.82 --> 1556.90]  you know, a huge part of what you're doing with a non-trivial application is configuring and pulling
[1556.90 --> 1562.56]  in plugins. Let's make that more accessible to folks who are newer, to folks who are more visually
[1562.56 --> 1567.12]  oriented, to folks who don't live in their command line. Yeah, that is very cool. And definitely a
[1567.12 --> 1573.32]  blind spot for me as also a command line junkie. Um, I didn't even pick up on the, on the GUI,
[1573.40 --> 1577.32]  uh, in the post. I mean, I saw it, but I was like, Oh, that's cool looking, but I didn't think about it
[1577.32 --> 1582.22]  very much. So that is definitely great for accessibility and really for making more difficult
[1582.22 --> 1586.12]  things easier, which is what we're definitely trying to do as library and framework authors.
[1586.12 --> 1591.32]  So very cool. Check that out. Um, as for my pitch, I'm going to pitch this as the story of the week.
[1591.32 --> 1598.32]  And here's my two reasons. Uh, the first one is 15,000 claps on medium. So, uh, pretty big deal.
[1598.40 --> 1604.94]  Secondly, I found this, although we did log in on change log news, but I was, I was re, uh, introduced
[1604.94 --> 1613.66]  to this by basically going to the R javascript and sorting by top and then setting week as my, uh,
[1614.06 --> 1618.54]  my filter. And so there's a, there's a life hack if you're ever going to be on the story of the week
[1618.54 --> 1623.18]  again. And this was number one. So, uh, I think it's pretty much unequivocally the story of the
[1623.18 --> 1629.38]  week. Sorry guys. I think I went, can I give a pro tip on, on finding stories too? Yes, please do.
[1629.98 --> 1637.16]  Uh, there's this tool called nuzzle and you, uh, Oh, off into it with Twitter. And then it looks at
[1637.16 --> 1642.40]  your Twitter timeline and what everybody's posting. And then it sorts links by the ones that are talked
[1642.40 --> 1648.12]  about the most on Twitter. And I used that to, to find, and I had to go back a little ways to find NDB,
[1648.12 --> 1653.14]  but I did find it. Now we're giving up all of our secrets and someone else is going to start their
[1653.14 --> 1660.90]  own story of the week podcast and totally dominate us. Can I, uh, give a little site slightly self
[1660.90 --> 1668.62]  serving, uh, story or a pro tip on this? What if I said, no, just kidding. Go ahead. Then I wouldn't,
[1668.62 --> 1677.16]  um, please do. So the slightly serving, uh, self serving pro tip is if you sign up to the
[1677.16 --> 1684.26]  newsletter that I publish, you'd see a lot of this, like that UI piece of the CLI, uh, in the last
[1684.26 --> 1691.18]  episode of July was in my newsletter. So it's a little self-serving, but if you go to zendev.com
[1691.18 --> 1695.50]  slash Friday front end dot HTML, you can sign up and you hear about all of this every Friday,
[1695.50 --> 1700.50]  but then when you have to listen to our podcasts anymore, no, we do, we do so much more cool stuff.
[1700.50 --> 1712.24]  So I have some pretty awesome news to share. We are now partnered with Algolia. If you've ever
[1712.24 --> 1718.00]  searched hacker news, T spring, medium Twitch, or even product hunt, then you've experienced the
[1718.00 --> 1724.58]  results of Algolia search API. And as we expand our content, we knew that one day we'd have to either
[1724.58 --> 1729.52]  roll our own search solution on top of postgres, or we can partner up with Algolia. And I'm happy to
[1729.52 --> 1734.86]  report that phase one of our search is now powered by Algolia. We're able to fine tune our indexing,
[1735.14 --> 1740.32]  gain insights from search patterns and analytics. We can create custom query rules to influence ranking
[1740.32 --> 1745.20]  behavior, as well as improve our search experience by adding synonyms and alternative correction to
[1745.20 --> 1749.26]  queries. Sure. We could build search ourselves, but that would mean we would be busy doing that
[1749.26 --> 1753.52]  instead of shipping shows like you're listening to right now. Huge thanks to our friends at Algolia
[1753.52 --> 1758.30]  for working with us. Check the show notes for a link to get started for free or learn more by heading to
[1758.30 --> 1759.26]  Algolia.com.
[1772.14 --> 1781.62]  Okay. Next up, we are going to do a segment called What the What? WG. And I'll just say that again
[1781.62 --> 1787.50]  because it's fun. What the what? WG. I get it. So the idea, yeah, you get it? So the idea here is
[1787.50 --> 1795.30]  that we were going to discuss some of the stuff that What WG has been up to lately. So for those
[1795.30 --> 1803.16]  who do not know what the What WG is, stands for the Web Hypertext Application Technology Working Group,
[1803.62 --> 1809.18]  which is why they use an acronym because nobody wants to say that five times fast. And it's a community of
[1809.18 --> 1813.36]  people interested in evolving the web through standards and tests. Now there's kind of an in
[1813.36 --> 1822.38]  and out between the What WG and the W3C or the World Wide Web Consortium. Who does what and why and
[1822.38 --> 1827.80]  when and how. So before I get into some of the standards that the What WG, I can't even say it,
[1827.80 --> 1832.62]  the What WG are working on, K-Ball is going to explain to us a little bit, as much as you can,
[1832.70 --> 1837.80]  K-Ball, some of the history there and really what the difference is between the two and all the
[1837.80 --> 1841.58]  millions of dollars. Help us out. Yeah. So I started researching this when you brought up
[1841.58 --> 1847.10]  What WG because I'd seen a little bit flow by as you're reading stuff of like, oh, controversy,
[1847.26 --> 1853.14]  What WG and W3C fighting about this or that or, you know, people trash talking one or the other.
[1853.14 --> 1865.76]  So the history is related to XHTML. W3C started going down the road of XHTML and XML that is very,
[1865.76 --> 1870.26]  very rigid and unambiguous. And they started pushing more and more in that direction. And
[1870.26 --> 1877.68]  browser vendors basically said, what instead of What WG, they said, What TH, right? This is going to
[1877.68 --> 1882.62]  break backwards compatibility, which is the key value prop or one of the key value props of the web
[1882.62 --> 1891.80]  is that anybody can throw this stuff up and it just keeps working. And so in 2004, a bunch of
[1891.80 --> 1897.02]  browser vendors kind of banded together and said, Well, you know what, y'all are failing us because
[1897.02 --> 1901.10]  you're trying to do this in a way that's not going to keep the value prop of the web, we're going to
[1901.10 --> 1911.30]  create our own specification. And they kind of tried to work together. But they had very different
[1911.30 --> 1916.72]  approaches to it. So W3C likes to kind of create frozen specifications. So if you remember, the whole,
[1916.72 --> 1922.18]  like, we're going to have HTML5, and that's going to be like the new version of HTML5, and it's going
[1922.18 --> 1928.42]  to be frozen. That was what W3C wanted. And what WG said, You know what, we're changing all the time,
[1928.52 --> 1934.84]  this should be a living standard, we should be constantly evolving it. So they kind of split
[1934.84 --> 1944.60]  in different ways. And the split was a little bit. There's not a this was a bad breakup, in a lot of
[1944.60 --> 1951.60]  ways. So there's, there's a lot of breaking up is hard to do. If you if you start looking through like
[1951.60 --> 1957.22]  forum stuff, or GitHub issues or things where this standards are being debated, there's a lot of bad
[1957.22 --> 1965.40]  blood, as far as I can tell. But what seems to happen now, according to what WG and this is a
[1965.40 --> 1971.44]  direct quote, they say the W3C publishes some forked versions of our specifications. We've requested
[1971.44 --> 1975.40]  that they stop publishing these, but they have refused, they copy most of our fixes into their
[1975.40 --> 1980.38]  forks, but their forks are usually weeks to months behind. They also make intentional changes and
[1980.38 --> 1985.34]  sometimes unintentional changes to their versions. We highly recommend not paying any attention to the
[1985.34 --> 1997.70]  W3C forks of what WG standards. Wow. So they're essentially, yeah. But most the vast majority
[1997.70 --> 2005.66]  of the work seems to be happening in for HTML, in particular happening in what WG. And while W3C keeps
[2005.66 --> 2012.44]  publishing updates, they appear to be primarily bad forks of the work that what WG is doing.
[2012.44 --> 2020.62]  Hmm. So what WG is worth watching and paying attention to, it's mostly people working for
[2020.62 --> 2025.44]  the browser vendors. So a lot of these times, specific vendors will add features. And we'll
[2025.44 --> 2030.04]  talk about one of those here soon with auto capitalized. And they will add it to their browser
[2030.04 --> 2035.70]  and put it out in the wild for a while and kind of prove it out as something that's useful or good
[2035.70 --> 2042.18]  for whatever reason. And then the what WG will go back and standardize around that if everybody
[2042.18 --> 2048.66]  agrees that that is something worth standardizing around. And so it's interesting. I mean, we talk
[2048.66 --> 2054.22]  about bleeding edge. It's not that bleeding because some of these things already exist in certain,
[2054.44 --> 2061.40]  you know, only in Chrome or works best in edge, that kind of thing. But as we see specific features
[2061.40 --> 2067.74]  and changes formalized and turn into specs, then the other browsers are more likely to add it as
[2067.74 --> 2072.40]  well. So it's interesting, especially if you want to stay up on like the new stuff going into
[2072.40 --> 2081.20]  the web platform is to find out what the what WG is working on, or at least considering and then also
[2081.20 --> 2086.20]  what has been added as of recent. So with that in mind, let's talk about a couple of things here.
[2086.20 --> 2091.22]  And the first one is the one that's really been on my plate lately, which is why I've been thinking
[2091.22 --> 2098.96]  about this and was excited to find out that it might be coming to browser soon, which is lazy
[2098.96 --> 2106.60]  loading images and iframes. Now, if you're on Lighthouse or any sort of like performance tool,
[2107.18 --> 2112.26]  one of the very first recommendations they will say is you should be lazy loading offscreen images.
[2112.26 --> 2120.74]  So for example, changelog.com has a whole bunch of avatars and images on the newsfeed for news items
[2120.74 --> 2126.78]  that you may never scroll down to. And when you load our page, we are going to go down,
[2127.00 --> 2132.28]  you know, the browser is going to go down and fetch all of those images into the page no matter what,
[2133.10 --> 2140.30]  unless you tell it not to. Unfortunately, there's no built in way to tell it not to,
[2140.30 --> 2145.42]  you have to basically do some JavaScript, which I think is a very big hack, which includes not
[2145.42 --> 2151.98]  adding a source attribute to your image tags until the JavaScript adds it for you, basically.
[2152.42 --> 2156.76]  And there's lots of ways of doing this. The most modern way is to use intersection observer,
[2157.08 --> 2163.14]  which as we've learned lately, has some issues as well. But this is something that like pretty much
[2163.14 --> 2171.56]  every website wants to do in terms of performance is we have 75 images and the user has only seen
[2171.56 --> 2177.26]  three of those. Do not waste time and bandwidth downloading all those images. So I've been
[2177.26 --> 2182.18]  complaining for a while now, as I want to do is just to complain mostly to Adam and other members
[2182.18 --> 2188.00]  of the changelog development team. Why is this not a browser feature? Like every browser performance
[2188.00 --> 2194.22]  tool says you should be doing this. So like pretty much every website wants it. And then everybody
[2194.22 --> 2201.00]  has to go implement it for themselves, which sucks. Jared, you said you had to do it with some sort of
[2201.00 --> 2206.46]  observer or something. Is that what you said? Well, so there's a different, yeah, intersection
[2206.46 --> 2212.40]  observer is the most modern way of doing this. So basically using that API, which is in modern
[2212.40 --> 2221.34]  browsers to detect when a element that has a or an image comes onto the viewport. So instead of
[2221.34 --> 2225.98]  loading them all, you wait till they're on screen. And so intersection observer is a way of detecting
[2225.98 --> 2230.94]  when something has come into the viewport or is close to the viewport. And so then it will go out
[2230.94 --> 2235.52]  and grab the image. And so basically what it does at that time is it takes the data dash source
[2235.52 --> 2240.74]  attribute, which is the URL of the image, and it just sets it as the source. And the browser goes ahead
[2240.74 --> 2245.60]  and does that. So that's a modern way of doing it. I think there was a, I mean, there's people
[2245.60 --> 2249.58]  been doing this for years because like I said, everybody tried or everybody has to, or wants to.
[2250.54 --> 2255.34]  And I'm not sure how they used to do it. K-Ball, do you know how older implementations of a lazy
[2255.34 --> 2259.68]  load would, would detect onscreen elements, or maybe they would just defer the loading?
[2259.92 --> 2263.08]  You do it basically the way that the polyfill for intersection observer works,
[2263.08 --> 2267.82]  which is you literally like check over and over again. Is this thing in my viewport?
[2267.82 --> 2272.68]  Which, yeah, that's what you set. Yeah. You set up, you set up an interval, right? And it just
[2272.68 --> 2276.18]  checks every now and then. So there you go. And yeah, because intersection observer,
[2276.54 --> 2282.40]  Nick just linked to it there in the chat. If you go to can I use, you'll find that it's on most
[2282.40 --> 2288.02]  modern browsers. I think maybe Safari is the mobile Safari and Safari are the one that it's not on.
[2288.12 --> 2291.72]  I don't remember, but you have to use a polyfill if you're going to use the modern way.
[2291.72 --> 2297.50]  Wouldn't you just want to pull like on a scroll event or something? Or does it,
[2297.70 --> 2299.68]  is there a reason to do it all the time?
[2300.72 --> 2303.20]  No, you could, yeah, you can do that. You still need to debounce.
[2303.72 --> 2308.44]  So the overarching theme here is it's a lot of work, right? And everybody needs to be doing it.
[2308.80 --> 2315.10]  And so that's like prime candidacy to, to, to, you know, who knows the best in terms of like when
[2315.10 --> 2321.98]  a user would desire an image to be actually fetched, probably the, the software closest to
[2321.98 --> 2329.02]  the user, right? Probably the browser itself. That's my take. Yeah. And so that's, uh, thankfully
[2329.02 --> 2336.86]  the what WG has been working on this and there's a draft spec. Um, if you are on the Git hubs,
[2336.96 --> 2343.20]  it's on the what WG repo in the HTML or the what WG organization, the HTML repo and it's pull request
[2343.20 --> 2347.62]  3752. We'll link that up. If you want to read it, you get, you dive into the details here and you
[2347.62 --> 2351.68]  realize why these things don't necessarily move very fast. Cause there's so many different things
[2351.68 --> 2358.68]  for them to consider. And, uh, and so it's a very active process, but there is a draft spec for
[2358.68 --> 2365.56]  lazy loading of images and iframes, uh, built right into the browser. So basically what you'll do is add
[2365.56 --> 2371.08]  an attribute to your images. I think it's like lazy load equals true, or there's a few different
[2371.08 --> 2377.12]  things that you can do in order to, how to, how to control it. But it's something that is coming
[2377.12 --> 2383.98]  and is not here quite yet, but it's actively being worked on so that in a future, uh, in an unknown
[2383.98 --> 2390.52]  future, uh, we won't have to be working quite so hard to, to do this for people. So Jared, do you know
[2390.52 --> 2400.64]  how, how they manage the ongoing split of things between W3C and what WG is HTML ended up in what WG,
[2400.64 --> 2410.96]  but CSS is in W3C working groups. Right. And JavaScript things seem to be split randomly across the two.
[2412.44 --> 2417.82]  Do you have any sense of like, I don't know the politics. I feel like, uh, maybe if we had
[2417.82 --> 2423.42]  Feras on this episode or maybe even Alex would know the actual split out. Um, I know what, what WG
[2423.42 --> 2429.32]  works on, which like you said, HTML, the DOM, a fetch, right? These different things. They have a list
[2429.32 --> 2436.42]  of like, these are our territory URL stream storage. And then like you said, CSS is on the W3C side.
[2436.46 --> 2440.90]  I'm not sure what else is on the W3C side, but you would think that you would want all of these
[2440.90 --> 2446.26]  things to be worked on together because like where I have CSS in a silo, it seems like that's,
[2446.36 --> 2451.80]  that's not good, but no, I do not know why or how that all shook out. Well, in different JavaScript
[2451.80 --> 2461.90]  APIs are like split across the two, I think, um, like audio APIs and things like that are in W3C,
[2461.90 --> 2470.34]  but you know, access HTML requests or whatever is in what WG and the notifications API is what WG,
[2470.50 --> 2473.72]  but yeah, it, it seems pretty random from the outside.
[2473.72 --> 2479.80]  Yeah. And it's very opaque as well. So yeah, as I proposed this segment, like, Hey, let's talk
[2479.80 --> 2483.38]  about what they've been up to and what they're doing, because I think that's, I think that's
[2483.38 --> 2488.96]  helpful to shine a light on. At least people know, okay, lazy load, Hey, it's coming soon. Um, or this,
[2489.06 --> 2493.82]  you know, stuff gets rejected. Right. And one of the things Chris asked was like, well, how do you even
[2493.82 --> 2497.72]  do that? How do you even look at it? And basically you're just scrolling. And in terms of the what WG,
[2497.82 --> 2503.34]  you're just going through GitHub issues and clicking on different tags, like additional slash or a proposal.
[2503.72 --> 2506.96]  Seeing what's been merged, seeing what's been going on. Some things are approved,
[2507.48 --> 2511.80]  lots of, lots of discussion going on. So this could be like a full-time job participating.
[2511.94 --> 2515.60]  And I think a lot of the people who are participating work like Jake Archibald, for instance,
[2516.10 --> 2523.14]  work at like web platform teams for Google, for Apple, for Microsoft. And so it really is
[2523.14 --> 2527.68]  a full-time job by multiple people to, to do these things.
[2528.90 --> 2533.58]  They have, I'm just going through their list. They have a spec on quirks mode.
[2533.72 --> 2543.10]  It includes such fun things as defining quirky colors and, uh, quirk lengths or quirky lengths.
[2543.44 --> 2551.08]  All these other basically backwards compatibility things for a really old HTML, but a really old
[2551.08 --> 2554.28]  CSS. Yeah. Sounds fun.
[2554.62 --> 2559.54]  They also do have a console and I, a console spec, and I didn't realize that that was actually
[2559.54 --> 2559.92]  a spec.
[2559.92 --> 2563.82]  Yeah. I noticed that as well. And I was kind of scrolling through the different areas to
[2563.82 --> 2569.66]  see what has the most activity in terms of the, what WG, uh, organization and the console
[2569.66 --> 2575.66]  one is like, there's just nothing good. It's like, you know, tumbleweed. Uh, a lot of them,
[2575.70 --> 2579.36]  there's like the fetch one has some activity. And then like the quirks mode one is completely
[2579.36 --> 2584.50]  in terms of people like proposing things, talking about things, merging docs, and then the HTML
[2584.50 --> 2589.52]  and then the fetch. And a few of them are like super active. So yeah, not, they do have a console
[2589.52 --> 2593.92]  working group or whatever it's called, but there's just not much, not much activity going on there.
[2594.56 --> 2599.00]  So one other example I wanted to pull in. So we had the image lazy loading, which is a proposal
[2599.00 --> 2605.10]  that is have a spec drafted. It's not there yet. Um, so it's probably, who knows, it could be years
[2605.10 --> 2611.40]  maybe before these things are found in enough browsers to, to use them. But, um, here's an example of,
[2611.40 --> 2617.60]  I guess the process working, which is the auto capitalize attribute. And so this is one that's
[2617.60 --> 2621.92]  been merged. Uh, we'll link to this as well. If you want to read through, uh, everything yourself,
[2621.92 --> 2627.42]  but it's past tense has been merged as even on Mozilla developer network docs, all that kind of
[2627.42 --> 2632.86]  stuff is finished. And it's kind of cool watching the way this works. So the auto capitalized attribute
[2632.86 --> 2641.38]  is, uh, in iOS specifically on input fields, right? So you can, uh, set auto capitalized equal to
[2641.38 --> 2647.92]  true or whatever the values are. And it will instruct the browser's keyboard or the devices
[2647.92 --> 2654.54]  keyboard to capitalize first words and whatnot on behalf of the user. Cause on mobile devices,
[2654.68 --> 2658.48]  you know, these things are more cumbersome. So Apple just added that. They didn't ask anybody's
[2658.48 --> 2662.66]  advice. They didn't like, you know, put it out there as like, this is something everybody should
[2662.66 --> 2667.06]  do. They just put it into iOS. And I think it's been there for years, but it doesn't exist
[2667.06 --> 2671.60]  anywhere else. It's just there, but IMS has a big enough market share. And so therefore
[2671.60 --> 2676.44]  mobile Safari has enough people using it that it became something that developers have been
[2676.44 --> 2679.76]  adding to their sites. Has anybody used this attribute or had to deal with it?
[2680.40 --> 2682.00]  No, not yet, but I hate it.
[2682.86 --> 2687.84]  Yeah. I hate, I hate it when I run into, actually, it's not true that I haven't used it. I have
[2687.84 --> 2691.00]  used it to say auto capitalized false. So let's turn it off.
[2691.00 --> 2698.38]  I turn it off Apple. It's terrible. So here's where I've also turned it off once and specifically
[2698.38 --> 2703.64]  on email fields where they will auto capitalize like the first letter of an email address. And
[2703.64 --> 2709.14]  if your site isn't set up to like normalize those or downcase them before searching, it
[2709.14 --> 2715.10]  won't find the user because you have case sensitive searching or something like that. So yes, it
[2715.10 --> 2719.62]  can be annoying. Um, but now it can be annoying in all the browsers.
[2721.00 --> 2727.34]  Because there, it has been merged into the what WG's HTML spec. And I'll just read this,
[2727.34 --> 2731.74]  uh, this comment on it because it is kind of, I think, instructive of how these things
[2731.74 --> 2736.64]  kind of shake out. So this is on the, on the issue, the Chrome team. This is a member of
[2736.64 --> 2740.78]  the Chrome team. He says that the Chrome team is currently attempting to update our implementation
[2740.78 --> 2745.26]  of the auto capitalized attribute in Chrome for Android. And then in parentheses, currently
[2745.26 --> 2750.36]  a non-standard extension introduced by Apple. He says to match the behavior of iOS Safari,
[2750.36 --> 2755.50]  specifically to add support for auto capitalized on editable regions inheritance from the form
[2755.50 --> 2759.78]  owner for and text area elements, blah, blah, blah, blah. He says, as part of this work,
[2759.78 --> 2765.28]  we would like to standardize this attribute in the HTML spec. He says the goal with this
[2765.28 --> 2770.64]  spec change is to document iOS Safari's behavior. So ideally Apple won't have to make any changes
[2770.64 --> 2775.32]  to their implementation so that other browsers such as Chrome for Android can implement the
[2775.32 --> 2780.78]  attribute with the same behavior. So this is, this is how this process happens. I think often,
[2780.78 --> 2784.82]  or if at least heard it happens often. And here's a good example is somebody goes out and implements
[2784.82 --> 2790.26]  a thing. In this case, Apple, we know Chrome leads the way on many new features, some which end up,
[2790.26 --> 2795.86]  you know, getting into other browsers. Some that don't sometimes speaking of Apple, a lot of times
[2795.86 --> 2802.22]  Apple's the last holdout on specific features that lots of us developers want. Um, but in this case,
[2802.22 --> 2806.34]  they added it and despite the three of us, I don't know, Chris, if you've dealt with this,
[2806.34 --> 2811.62]  uh, being on IOT and back and mostly, uh, not liking it and turning it off. Uh, apparently it
[2811.62 --> 2816.64]  serves a valid use for enough users that this is something that, uh, they decided to formalize
[2816.64 --> 2822.08]  around. And so the goal here was not to like make Apple change their, their behavior. Cause probably
[2822.08 --> 2826.02]  they wouldn't do it anyways, but to just say, okay, this is a feature that we think should be in
[2826.02 --> 2831.10]  all browsers and Apple has led the way. And so we're just going to formalize a specification,
[2831.10 --> 2836.96]  basically using exactly the way that Apple has implemented. And so they move forward with that.
[2837.02 --> 2844.14]  They all got agreement. You can read all the comments and it rolled out. So interesting just
[2844.14 --> 2848.20]  seeing the ins and outs of such a small thing, right? Like it's a single attribute on a few
[2848.20 --> 2855.62]  element types and, uh, 40 conversations here, uh, six commits to get this thing merged.
[2855.62 --> 2861.76]  So a lot of work going in behind the scenes that I think maybe we take for granted. Um,
[2861.98 --> 2868.38]  maybe we get mad about, but a lots of effort involved in even the smallest changes to these
[2868.38 --> 2874.40]  issues, the improvements in the way that we deal with specifications and updates. And the fact we
[2874.40 --> 2879.46]  now have, you know, browsers that are evergreen and all sort of at least more or less collaborating.
[2879.46 --> 2885.76]  Like, I feel like that is an under noticed reason why the web has become so powerful,
[2885.76 --> 2892.22]  right? Like we've gotten so much better as an industry at working together to improve these
[2892.22 --> 2895.94]  things, but it is often just behind the scenes.
[2896.74 --> 2901.16]  Good point. Yeah, it's definitely gotten better. And I think the workflow specifically around GitHub,
[2901.70 --> 2906.06]  these things were, you know, a lot of these things have been transparent for a long time,
[2906.06 --> 2911.88]  but there's something about a common platform that everybody knows how to use and is, uh, very
[2911.88 --> 2917.60]  accessible that makes them more transparent. Like I would have never in the past dug into this stuff,
[2917.60 --> 2922.46]  but the fact that it's like, Oh, it's just a GitHub issues, start reading them. You know,
[2922.52 --> 2927.32]  here's the labels, like it all is very familiar. I feel like the transparency and the, even though
[2927.32 --> 2933.42]  they're driven very much by the big players, like the ability for people to get involved is better than ever.
[2936.06 --> 2946.38]  This episode is brought to you by our friends at indeed. Indeed is the world's number one job site
[2946.38 --> 2952.22]  with a seemingly simple mission of helping people get jobs. That seems pretty simple, right? Well,
[2952.22 --> 2958.34]  beneath the layers of simplicity is a company solving very complex problems to help folks like you and
[2958.34 --> 2963.80]  me to get jobs. And speaking of jobs, they are in need of talented people themselves, passionate people
[2963.80 --> 2968.10]  to work together, to make their mission of helping people get jobs possible. Here's the conversation
[2968.10 --> 2972.90]  I had with Brian Cheney, director of talent attraction about indeed and how they're more than just a job
[2972.90 --> 2978.14]  board. People think that they know indeed the perception is that we're just a job board and
[2978.14 --> 2984.30]  we've gone so far beyond jobs. And so one of the cool things that an engineer would find out
[2984.30 --> 2992.46]  working on indie products is that we've got layers and layers of data. We have over eight petabytes
[2992.46 --> 3000.90]  of data generated every day. And just to touch on some of what you can slice and analyze, we have data
[3000.90 --> 3007.60]  scientists that focus on pulling that data, really interpreting it and empowering other areas of the
[3007.60 --> 3014.48]  business to use the data. And I think the kicker is that most people haven't seen a lot of change from
[3014.48 --> 3020.72]  indeed over the last few years. And there's so much that's been changing under the hood. And so to
[3020.72 --> 3027.02]  understand all the things that we're touching on and building and the layers beneath that job search
[3027.02 --> 3034.70]  process and helping people really, really using machine learning to match people with the jobs that
[3034.70 --> 3041.24]  they're likely going to be a fit for. That's those are the exciting things that we get to build and really
[3041.24 --> 3047.54]  allows people to make a difference in hundreds of millions of people's lives. So if you think you
[3047.54 --> 3054.48]  are a good fit for indeed's mission of helping people get jobs, head to indeed.jobs slash changelog to
[3054.48 --> 3060.06]  learn more and take that first step. Once again, it's indeed.jobs slash changelog.
[3071.24 --> 3077.54]  All right, everyone, it is now pro tip time. This is where we share our pro tips. Pretty straightforward.
[3078.34 --> 3082.56]  Whether or not we're actual pros, that's for you to decide. These can be life hacks, they can be
[3082.56 --> 3087.32]  lessons learned from doing dumb things. Not that you would do that. But I surely have done some dumb
[3087.32 --> 3092.66]  things. And let's share them so other people can learn and perhaps take away things and avoid
[3092.66 --> 3096.10]  fails, if possible. So Chris, pro tip time.
[3096.10 --> 3110.40]  So I have some pro tips. I use a Mac, if you use a Mac, maybe a thing you need to do is copy and or
[3110.40 --> 3119.94]  paste text files, source files, or what have you in their entirety. And so I discovered not too long
[3119.94 --> 3124.88]  ago, and maybe this is one of those things that everybody knows except me. But I discovered that
[3124.88 --> 3134.94]  there were actually a couple command line tools with that common Mac OS that help you do just this
[3134.94 --> 3149.54]  thing. And so they are PB paste and PB copy. And so PB paste will, it outputs to standard out. It takes
[3149.54 --> 3154.98]  whatever is in the clipboard and it sends it to standard out. And so you can pipe it to whatever
[3154.98 --> 3162.44]  you want to pipe it to. And so maybe you want to pipe that to a file. And so if you copy like some
[3162.44 --> 3169.10]  source and then you go to your command line, you say PB paste, and then you do like a, you know,
[3169.18 --> 3175.64]  the right, I don't even know if that's less than or greater than, but you're pasting to the right
[3175.64 --> 3180.92]  or you're, you're piping to the right with the, with the direction. And you say, you know,
[3181.08 --> 3186.66]  foo.js, it will, you know, paste the contents of your clipboard into a new file, foo.js.
[3187.50 --> 3189.84]  I wrote like a little tiny
[3189.84 --> 3200.84]  ZSH function called paste, which does just this. It takes its first parameter and it says PB paste and it,
[3200.84 --> 3206.36]  and it writes to this, this new file. And so I say paste foo.js. It takes whatever's in my clipboard,
[3206.46 --> 3212.82]  throws it in a new file foo.js. Likewise, PB copy, you can cat a file and then pipe it to PB copy.
[3212.82 --> 3219.06]  And that file's content will end up in your clipboard. And again, I wrote a little function
[3219.06 --> 3226.76]  to help with that. So it just accepts its first parameter and it cats it, this, this file in it,
[3226.76 --> 3232.14]  it, it, it pipes it off to your, to your clipboard, which is really cool. Along the same lines,
[3232.22 --> 3239.34]  there's another little thing called Z and people may or may not know about Z. Maybe we talked about
[3239.34 --> 3244.84]  Z before. I don't know, but there's this command line tool for your shell called Z. It's like,
[3245.50 --> 3252.86]  just search GitHub for Z. And it basically looks at all your shell history. It looks where you've been.
[3252.86 --> 3261.18]  And if you say something like Z, um, you know, node or something, it'll find, uh, the, the last
[3261.18 --> 3266.68]  directory, um, that you were in called node and it'll just pop you right back there. And so it's a
[3266.68 --> 3274.86]  great way to, um, navigate to frequently visited directories or working copies. Um, and it's really
[3274.86 --> 3282.84]  neat. Um, another tool I use is called, uh, and this is apparently there's science behind this,
[3282.84 --> 3289.58]  I can't say whether or not that's true, but it's, it's brain.fm and what it is, it's a service that
[3289.58 --> 3297.40]  you pay a nominal fee for and they give you a mobile app and a web app. And it's like, um,
[3298.32 --> 3306.74]  best way to maybe explain it is, uh, AI generated, it's generative music. Uh, there's many different
[3306.74 --> 3312.46]  styles, but it's, there's some science behind it that says, if you listen to this music, it'll help you
[3312.46 --> 3321.46]  for example, focus on a task or it'll help you relax, um, because of various tones and tempos and
[3321.46 --> 3328.74]  frequencies in the music. And so I don't know about that, but I wanted to try it. And so I did try it
[3328.74 --> 3337.24]  and I found out that it's really helpful, um, when I'm trying to focus on coding and it helps me get
[3337.24 --> 3344.40]  and stay kind of into, into the flow. Um, you know, I, I feel like, you know, if, if you do a lot of coding,
[3344.84 --> 3349.42]  maybe you recognize that sometimes you get into this flow state and I feel like the, the, the music
[3349.42 --> 3355.60]  generated by brain.fm may, may help you do that. Maybe it won't, maybe you'll find it boring, but it's
[3355.60 --> 3361.00]  supposed to be actually like kind of, it's not supposed to engage with you. It's supposed to be kind of in
[3361.00 --> 3367.90]  the background. Um, and so, uh, a lot of, of, you know, popular music or, or even like maybe you
[3367.90 --> 3374.36]  listen to, I don't know, techno or trance or something with that beat, um, you know, kind of
[3374.36 --> 3380.08]  drives you forward to, to help, but maybe sometimes that type of music is a little too engaging. And,
[3380.08 --> 3385.54]  uh, the brain.fm music is kind of like, it's like techno elevator music or something. It's just, uh,
[3385.60 --> 3389.78]  it's, it's, it's really interesting. You just, just throw it on the background, forget about it. And,
[3389.78 --> 3397.62]  um, it, it helps me focus. Um, and so, yeah, check that out. Um, it's cool. And the last thing,
[3397.70 --> 3403.86]  there is a thing called astral. Uh, if you're like me, you have like a million GitHub stars and, um,
[3404.42 --> 3410.88]  you may not, you know, what was that thing I was thinking of and how do I find it? I don't even know
[3410.88 --> 3416.48]  how to do that with GitHub. So there's this app called astral app. It's astral app.com. It's just
[3416.48 --> 3424.16]  like a, an OAuth style GitHub app and it helps you manage and view all your stars. And you can even
[3424.16 --> 3432.24]  tag your stars into categories and like sort stuff by language. And it's really neat. So, um, if you
[3432.24 --> 3438.32]  are like me and have a lot of stars, check out astral app and that will help you like manage them
[3438.32 --> 3444.30]  and, and find the things. And those are my pro tips. Very cool. I've also used brain FM and I,
[3444.38 --> 3449.74]  I do think it is a good programming music. So I'm with you on that one. I was going to say the same
[3449.74 --> 3456.16]  thing. I haven't used, I haven't used brain FM, but I use a similar surface called focus at will.
[3456.48 --> 3461.86]  It is also excellent. I didn't know that it's, it's cool to find out that, that people are actually
[3461.86 --> 3466.84]  using it besides me and I'm not just some sort of like crackpot. Um, but I'm glad, glad to,
[3466.92 --> 3471.78]  maybe I'm a crackpot, but it's, I'm glad to hear that it's working. You're amongst crackpots. You
[3471.78 --> 3480.80]  have crackpot friends. Nick. Yeah. So, uh, I've got two quick pro tips. Uh, the first one is a tool
[3480.80 --> 3487.80]  called JS code shift, uh, which is really cool. It's a way to create, uh, what they call code mods for,
[3488.00 --> 3491.52]  for your code. If you need to do some kind of repetitive change throughout your code base,
[3491.52 --> 3497.14]  um, you can do that, uh, in a lot of different ways, like find and replace, uh, which I'll
[3497.14 --> 3503.16]  typically do in like a Vim macro or, or something like that. Um, but if you want a reproducible way
[3503.16 --> 3506.94]  to make changes to your code, that is very safe because you're actually going to be using,
[3506.94 --> 3513.64]  uh, the abstract syntax tree to, to do it, JS code shift and code mods are for you. Uh, and it's
[3513.64 --> 3518.20]  just a really cool way to, to be able to traverse the tree and the tool does all of the traversing for
[3518.20 --> 3522.28]  you. So you just have to know what tokens you want to look for. Uh, for example, you could look
[3522.28 --> 3527.62]  for import statements in your code, uh, and then change those in some programmatically. So you can
[3527.62 --> 3534.96]  be guaranteed that you're not going to change some commented out, um, import or a value in a string
[3534.96 --> 3540.46]  somewhere, but you're actually going to be changing the, um, like the from string on an import statement
[3540.46 --> 3546.12]  to a new value. You can be very specific about what you want, make those changes, and then, uh, have
[3546.12 --> 3551.40]  that as a code mod that you can share with friends and, uh, have a reproducible way of doing that. So
[3551.40 --> 3556.62]  really cool. Uh, and then the second thing is two factor authentication in one password. If you
[3556.62 --> 3561.18]  haven't been using it, uh, it's amazing. If you haven't been using one password, it's also amazing.
[3561.70 --> 3566.28]  Uh, my life revolves around that. That's the first thing I need on every device to get anything else,
[3566.28 --> 3572.08]  but they have kind of hidden in there a way to do two factor authentication, where if you were going
[3572.08 --> 3576.88]  to use authenticator or Authy or one of those other apps in the past, you can just do it within one
[3576.88 --> 3581.34]  password. And the big benefit that you get is when one password auto fills your username and password,
[3581.50 --> 3586.40]  it puts the one-time token on your clipboard. And then you can just paste that in when that screen
[3586.40 --> 3592.62]  comes up and it works on iOS and on a Mac and it's just great. So, uh, I recommend you using that
[3592.62 --> 3597.66]  one password will also tell you if, uh, an application that you have a saved login for has two factor
[3597.66 --> 3601.40]  authentication and you don't have that set up. It will tell you about that so that you can go in and
[3601.40 --> 3607.48]  be safe. That's it. Is it technically two factor if it's the same thing doing it?
[3608.52 --> 3614.24]  That is a good question, but it would be my phone in both cases. So I guess it's what level of
[3614.24 --> 3620.18]  abstraction that you have there. Have you guys ever had the situation where you do a SMS based two
[3620.18 --> 3626.20]  factor off and then your max continuity feature brings the SMS right back onto your Mac and it's
[3626.20 --> 3631.14]  right there in your notification center. And you're like, Oh, I guess it's, I guess it's one
[3631.14 --> 3640.60]  factor again. Yep. Security is hard. All right, K-ball, you're up. All right. Mine is less of a tool
[3640.60 --> 3648.40]  and more of a life hack. Uh, and that is to identify and validate your assumptions at every
[3648.40 --> 3655.30]  level of your life. And this can play out in the technical sense. Like the first step to debugging a
[3655.30 --> 3660.92]  problem for me is to go in and sort of identify for me, what am I assuming? And just check that
[3660.92 --> 3666.58]  those things are true. So often, particularly if I'm helping, uh, when like a junior dev or something,
[3666.58 --> 3672.50]  like we can find it, it's almost like, uh, you know, being a rubber duck, we find it just by
[3672.50 --> 3677.84]  saying, what are we assuming? Can we validate that those assumptions are actually true? Usually the bug
[3677.84 --> 3683.68]  comes from one of those assumptions, not actually being true, but this plays out throughout your life.
[3683.68 --> 3689.64]  It's not just code, right? So some of my biggest personal breakthroughs have been from discovering
[3689.64 --> 3694.28]  that there was something, some mental model I had that I had just been assuming this was the way the
[3694.28 --> 3700.00]  world worked or the way that I had to be doing things or, or something and discovering that that
[3700.00 --> 3705.26]  was only an assumption, not actually the truth and that I could change that. Uh, you know, this occurs
[3705.26 --> 3710.12]  in things like, uh, money and pricing. You know, if you run your own business or you're a consultant,
[3710.12 --> 3714.56]  you probably have an assumed idea of how much money you can charge for things. And usually
[3714.56 --> 3720.64]  you haven't validated that. Uh, when I discovered that assumption that, you know, I had an assumption
[3720.64 --> 3728.56]  that as a consultant, I had to charge things by the hour. Um, and I ran into this, uh, writer and
[3728.56 --> 3732.96]  guy named Jonathan Stark, whose big thing is like hourly billing is nuts. It's a crazy thing to do.
[3733.00 --> 3739.20]  It sets up all your incentives wrong. So you should be charging in other ways, uh, value-based pricing
[3739.20 --> 3744.08]  or project-based pricing or even retainers. Um, and kind of highlighting all the ways in which
[3744.08 --> 3749.60]  hourly building sets you up, hourly billing sets you up for failure and sets your incentives
[3749.60 --> 3755.08]  at cost purposes to the people you're working with or working for. Uh, and that just totally
[3755.08 --> 3761.76]  shifted the way I conceived of my business and has made my life so much better. Um, so every level of
[3761.76 --> 3768.92]  your life, figure out what are the assumptions you're making, uh, and then test them. And they might be
[3768.92 --> 3773.16]  right. But if they're not, you're probably screwing yourself over somehow.
[3773.96 --> 3780.18]  That's definitely a good pro tip. Hey, you and I should talk, uh, business at some point in terms
[3780.18 --> 3784.34]  of billing and all that kind of jazz. Cause I've been running a consultancy, one man consultancy
[3784.34 --> 3789.96]  like yourself for many years. And so we bounce ideas off each other, but let's do it. Let's do that
[3789.96 --> 3799.30]  for later. So my pro tip is how to validate an email address. And here is the, the long,
[3799.42 --> 3803.98]  the hard earned experience on how you validate an email address. And the only thing that you can
[3803.98 --> 3811.24]  reliably do to validate an email address is that you send it an email, you send it an email. That's
[3811.24 --> 3815.46]  the only way you can do it. I know what you're thinking. I have the best regular expression for
[3815.46 --> 3820.54]  this. No, you do not. You think you do. Your regular expression is invalid. It is not good
[3820.54 --> 3825.60]  enough. You know, the old adage, the developer, when faced with a problem thought, I know I'll use
[3825.60 --> 3829.54]  regular expressions. Now he has two problems. Well, that's what you have. You have two problems
[3829.54 --> 3836.16]  and I've known this for years. And yet I was still convinced to add a regular expression based email
[3836.16 --> 3842.22]  validation server side. First of all, never trust the client, right? You can do all you want there,
[3842.22 --> 3847.30]  but they can bypass all your checks. Got to be server side. I put a regular expression based
[3847.30 --> 3852.00]  email validation. And I thought this one's pretty good. In fact, man, I don't know what came over me.
[3852.04 --> 3857.98]  I was actually even talked into like copy pasting one off of a gist and it looked pretty good. And it
[3857.98 --> 3863.70]  covered most of the bases. And, uh, sure enough, a couple of weeks back, actually it was probably last
[3863.70 --> 3869.46]  week, got an email from a prospective user saying, Hey, I'm trying to sign up for changelog weekly,
[3869.46 --> 3874.40]  but it says my email address isn't valid. And it obviously is valid because I'm emailing you with
[3874.40 --> 3880.70]  it right now. And I thought, I'm an idiot. Why did I put a regular expression based email verification
[3880.70 --> 3888.10]  on my system? So don't do that. And, uh, I know you can find one on stack overflow. I'll tell you
[3888.10 --> 3892.40]  right now, it's not good enough. Email addresses are so complicated. There's so many valid things.
[3892.40 --> 3899.70]  If you're going to do it and I'll admit that I kept it in there, but I just check that there's
[3899.70 --> 3906.26]  some stuff and then an at sign and some stuff. And that's pretty much what you're going to be able
[3906.26 --> 3910.86]  to do. And that's just to basically make sure that you don't get some junk into your database,
[3910.86 --> 3916.40]  but still, all you got to do is send them an email. And if they click on it, well, that's a valid
[3916.40 --> 3923.80]  email address. And if they don't click on it, then who cares? So that's a hard learned lesson.
[3924.14 --> 3931.34]  If you want to validate an email address, send it an email. Problem solved. Until bots start clicking
[3931.34 --> 3936.24]  on emails, then we're going to have a whole new issue. But so far, so far, I don't think there's
[3936.24 --> 3941.34]  bots that will sign up for your thing. And then also, uh, we'll, we'll create a fake email address,
[3941.34 --> 3946.40]  sign up for your thing, and then access that email address and click on the link. When we get there,
[3947.08 --> 3950.52]  then we'll have to come up with something else. But until then, just send an email.
[3951.58 --> 3956.50]  All right. That's our show for this week. Like we said, make sure if you're at JSConf, don't miss us.
[3956.88 --> 3962.50]  Find K-Ball, find Nick next to me, run around like a chicken with a head cut off. Find Sue, say hi.
[3962.60 --> 3968.52]  We'd love to connect with you. We have stickers. Uh, we'll have a limited run t-shirts. We have a live
[3968.52 --> 3973.88]  show on Tuesday. Participate in that. And, uh, it will be a lots of fun, but thanks for listening
[3973.88 --> 3977.94]  today. And we will see you live at JSConf next week. And then the following week,
[3978.26 --> 3981.76]  Baras is back and he's got an awesome show all about the decentralized web.
[3982.20 --> 3984.52]  So look forward to that and we will see you next time.
[3987.70 --> 3990.82]  All right. Thank you for tuning in to JS Party this week. Tune in live
[3990.82 --> 3996.30]  on Thursdays at 1 p.m. U.S. Eastern at changelaw.com slash live.
[3996.30 --> 3999.30]  Join the community and Slack with us in real time during the shows.
[3999.66 --> 4003.70]  Head to changelaw.com slash community. And do us a favor, share this show with a friend,
[4004.00 --> 4008.70]  or you don't have a podcast, go into Overcast and favorite it. And thank you to Fastly,
[4008.78 --> 4013.12]  our bandwidth partner. Head to fastly.com to learn more. And we move fast to fix things
[4013.12 --> 4017.92]  around here at changelaw because of Rollbar. Check them out at rollbar.com. We're hosted on Leno
[4017.92 --> 4022.28]  cloud servers. Head to leno.com slash changelaw. Check them out and support this show.
[4022.28 --> 4026.98]  Our music is produced by Breakmaster Cylinder, and you can find more shows just like this
[4026.98 --> 4030.30]  at changelaw.com. Thanks for tuning in. We'll see you next week.
