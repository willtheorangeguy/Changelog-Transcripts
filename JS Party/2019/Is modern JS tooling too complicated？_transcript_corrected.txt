[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.86] Learn more at Fastly.com.
[5.08 → 8.14] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.22 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to Linode.com slash Changelog.
[15.28 → 18.12] This episode is brought to you by Rollbar.
[18.42 → 24.36] Rollbar is real-time error monitoring, alerting, and analytics that helps you resolve production errors in minutes.
[24.68 → 28.60] And I talk with Paul Bigger, the founder of CircleCI, a trusted customer of Rollbar.
[28.60 → 32.94] And Paul says they don't deploy a service without installing Rollbar first.
[33.32 → 34.58] It's that crucial to them.
[34.78 → 36.60] We operate at serious scale.
[37.04 → 42.46] And literally the first thing we do when we create a new service is we install Rollbar in it.
[42.64 → 45.52] We need to have that visibility.
[45.94 → 50.44] And without that visibility, it would be impossible to run at the scale we do.
[50.58 → 52.54] And certainly with the number of people that we have.
[52.72 → 55.70] We're a relatively small team operating a major service.
[55.70 → 61.46] And without the visibility that Rollbar gives us into our exceptions, it just wouldn't be possible.
[61.84 → 62.00] All right.
[62.02 → 66.70] If you want to follow in Paul's footsteps and start deploying with confidence today, head to Rollbar.com slash Changelog.
[67.36 → 70.34] Once again, Rollbar.com slash Changelog.
[70.34 → 81.76] Welcome to JS Party, a weekly celebration of JavaScript and the web.
[81.90 → 88.38] Tune in live on Thursdays at 1 p.m. Eastern, 10 a.m. Pacific at changelog.com slash live.
[88.38 → 93.48] Join the community and Slack with us in real time during the show at changelog.com slash community.
[93.88 → 94.68] Follow us on Twitter.
[94.78 → 96.30] We're at JSPartyFM.
[96.48 → 97.76] And now on to the show.
[97.76 → 114.08] Back by popular demand is this cool format, this debate topic, so to speak.
[114.28 → 118.36] We put a Twitter poll out there asking, do you like our new Yep, Nope segment?
[118.84 → 123.40] And an overwhelming or somewhat underwhelming 65% responded with Yep.
[123.74 → 126.30] So we took the bait, and we're doing it again.
[126.30 → 131.72] And today's show will be a debate on modern JS tooling and whether it is too complicated.
[131.84 → 135.52] So basically the question is, is modern JS tooling too complicated?
[135.62 → 136.38] We have two teams.
[136.66 → 137.04] Wait, wait, wait.
[137.34 → 139.78] Three teams now because we had some changing.
[140.10 → 142.02] We got Team Yep being represented by Divya.
[142.56 → 143.82] Team Nope represented by Michael.
[144.04 → 148.74] And Team It Depends, which is, hey, the moderate represented by Farah.
[148.88 → 149.62] So what's up, everyone?
[149.86 → 150.64] He's like Switzerland.
[150.64 → 152.86] I get to sit in the middle.
[153.06 → 153.56] It's so easy.
[154.56 → 155.96] You're not really picking a side.
[156.18 → 158.42] The rules for this are pretty simple.
[158.50 → 164.86] The first segment, we'll have each person kind of go through four minutes of their position in the argument from their side.
[164.86 → 170.20] And then when we come back to segment two, we'll do sort of shorter format so we can be more conversational.
[170.42 → 175.58] But the thing to keep in mind, listeners, is that the panellists may not be representing their beliefs.
[175.58 → 178.50] They're just instead representing the side they've been assigned.
[179.24 → 181.88] So, you know, it's a good argument that way.
[181.96 → 182.94] So let's get into it.
[182.98 → 184.66] First up, Team Yep.
[184.96 → 185.92] Divya, what do you get?
[186.46 → 186.90] Hooray.
[186.90 → 187.34] Okay.
[187.34 → 187.54] Okay.
[187.82 → 194.22] So the premise of this conversation is, is modern JavaScript tooling too complicated?
[194.68 → 199.32] And I would like to start with a haiku that I wrote specifically for this debate.
[199.42 → 199.88] I love it.
[199.98 → 200.14] Go.
[201.04 → 206.24] Many packages, new frameworks built all the time, config hell, webpack.
[206.24 → 212.12] And so to start the conversation, it's worth talking about what exactly JavaScript tooling is.
[212.12 → 221.24] And JavaScript tooling consists of tools, utilities, libraries that give developers the ability to build code for a specific target.
[221.56 → 227.12] I don't say web specifically or the browser because now there are multiple build targets you can use for JavaScript.
[227.12 → 230.04] So you can build JavaScript for mobile and for the browser.
[230.28 → 232.22] So any target you want.
[232.82 → 236.74] And then JavaScript tooling is often optimized for developer ergonomics.
[236.74 → 249.24] And so tools like hot reload, test suites, like compilation and build config things are all specifically for developers' satisfaction and to make their processes easier.
[250.24 → 259.98] And so in a way, JavaScript tooling and the ecosystem is idyllic because it gives developers the ability to wrangle an otherwise behemoth system.
[260.30 → 263.96] But the problem is that the tooling is overly complex.
[263.96 → 266.42] There are so many tools that you have to work with now.
[266.56 → 272.48] And that's mainly because working with modern JavaScript, you can't just take your code and, like, put it on a browser and it runs.
[272.62 → 274.22] You have to go through multiple steps.
[274.84 → 284.78] So with the current standard, which is, like, ES 2015 and future versions, oftentimes they're not always compatible with browsers because browsers kind of take a long time to implement them.
[285.30 → 288.02] And so as a result, you have to do things like transpiring.
[288.02 → 297.12] And then there's also the issue of modularizing your code, which is often a performance benefit because you don't want to put all of your JavaScript and load them all at once.
[297.22 → 298.50] And so you want to modularize.
[298.90 → 304.06] And so these add additional complexity because you have to think about how exactly you want those systems to work.
[304.34 → 312.00] And what it boils down to with the ecosystem is we have a lot of options, which results in too many choices for developers to make.
[312.00 → 317.50] And that's why we hear the problem of JavaScript fatigue, because there are so many different things that you can do.
[317.88 → 325.90] There are so many different ways in which you can approach building a web application or web things, I think, is how we defined it from the last episode.
[326.22 → 333.30] And so that is a huge problem that has resulted because the modern JavaScript tooling is too complicated.
[333.90 → 335.82] You got a minute and a half left.
[336.30 → 336.82] Okay, cool.
[336.98 → 337.70] I guess I'll just keep going.
[337.70 → 339.38] Do you want to keep going or do you want to pass it on?
[339.38 → 353.54] I have one more point to make, which is that the other thing that's also frustrating, and I talked about this a little bit, that JavaScript tooling also includes frameworks because it's things that we use in order to build web things, which users can then see on their browser.
[354.16 → 358.82] And the thing is, we're currently in a time when people call it the framework wars.
[358.94 → 362.80] I don't know if that's actually a thing, but essentially you have multiple frameworks you can choose from.
[362.80 → 371.38] So not only do you have the choice to make between what transpire tool to use, what build tool to use, and so on, you also have to choose the framework.
[372.04 → 375.92] And these frameworks are great, again, for developer ergonomics.
[376.04 → 385.10] But the other thing is that they introduce abstractions, which actually make building with JavaScript kind of frustrating for a lot because there's a steeper learning curve.
[385.10 → 389.66] Because not only are you learning just JavaScript, you're learning the abstractions that those frameworks introduce.
[390.16 → 398.30] And so the issue, therefore, is that overall, as a JavaScript developer, you have so many things you need to take into consideration and how all of these work together.
[398.54 → 401.92] And as a result, the JavaScript tooling ecosystem is too complicated.
[402.54 → 402.60] Nice.
[402.70 → 404.26] 20 seconds left if you want to use it.
[404.34 → 405.24] If not, we can move.
[405.68 → 406.96] I will open the floor.
[407.26 → 407.60] Nice.
[407.60 → 408.02] All right.
[408.10 → 411.48] Well, let's go then to Michael representing Team Nope.
[411.76 → 418.00] Because Team Fears, which is, these aren't really teams, just people, individuals now, because we had teams originally and that's how it was.
[418.10 → 419.12] But now we're just individuals.
[419.46 → 424.44] So Fears is representing, it depends on the moderate position, which I guess might be the better.
[424.54 → 424.98] We'll see.
[425.58 → 426.88] But, Michael, what do you get for Team Nope?
[427.46 → 428.28] So, yeah.
[428.38 → 428.54] Okay.
[428.62 → 431.28] So I need to start with, like, some context, right?
[431.28 → 437.08] So when you think about programming and just technology in general, you're talking about, like, an ever-expanding field, right?
[437.08 → 440.22] Like, there is more code tomorrow than yesterday.
[440.68 → 443.48] The entire field is growing at a pretty exponential rate.
[443.82 → 445.46] And the future is much bigger than the past.
[445.50 → 448.04] So we should expect this to grow into the future, right?
[448.78 → 455.72] When you think about, like, you know, programming languages or frameworks or whatever that, quote-unquote, die, they often don't actually die.
[456.02 → 460.02] They may lose a couple users, but for the most part, what they actually do is they stagnate.
[460.02 → 466.80] So they have the same amount of usage or the same amount of users as they always did, but the entire field has gotten much, much bigger than them, right?
[467.08 → 473.88] So what that essentially means is that unless you are in a part of the programming ecosystem that is growing, you have a problem.
[474.16 → 475.80] You are effectively sort of dying.
[475.96 → 480.04] If you aren't capturing at least as much growth as the entire field is growing, that can be problematic.
[480.34 → 483.76] It means that in the future you will just have fewer options than other developers.
[484.34 → 489.78] So I want to come back, like, in that context, I want to come back to this lovely IQ, actually.
[489.98 → 490.56] Like, this is perfect.
[490.94 → 492.02] So many packages.
[492.02 → 493.82] Like, this is said, like, it's a problem.
[494.10 → 495.92] Like, what an amazing problem to have.
[496.28 → 497.52] Like, ask a Haskell programmer.
[497.76 → 503.80] Like, love the fact that when they want to use a package, it does not exist, and they have to write it from scratch every single time, right?
[503.92 → 508.90] So, like, this is like, we've effectively graduated on to second-order problems because we have been successful.
[509.68 → 510.72] New frameworks built all the time.
[511.10 → 515.28] New things being built all the time is a sign of, like, success.
[515.52 → 516.56] It's also a sign of help.
[516.56 → 522.12] If you don't have new things being built all the time replacing the old things, then that's a huge problem, right?
[522.32 → 530.06] One of the strange things that's happened, actually, in the last 10 years is that it used to be that languages really only stagnated and didn't really lose market share.
[530.40 → 532.04] Sorry, lose absolute users.
[532.42 → 533.96] But that actually did happen to Ruby a bit.
[534.22 → 537.16] And, like, you can, if you look in the Ruby ecosystem, like, it's sort of a problem.
[537.28 → 538.86] Like, nothing is replacing Rails.
[539.04 → 539.82] Like, it's just there.
[539.90 → 540.86] It's doing its thing forever.
[541.20 → 543.38] There is not a new thing that is coming in to replace it.
[543.38 → 552.98] In JavaScript, because we're always expanding, because we have all these new use cases that we're handling all the time, that means a huge set of new tools and frameworks always coming in to replace the previous ones.
[553.96 → 559.20] And, like, yes, that is painful to go through as a developer, to always be learning a new thing.
[559.32 → 563.16] But that is literally, like, the job of working in the technology sphere.
[563.44 → 570.00] Like, if you are not learning a new thing, you eventually, like, will just be, you know, like, off in a corner still writing COBOL, which is fine.
[570.10 → 570.58] COBOL is cool.
[570.58 → 574.84] But, like, you know, it may not be the most interesting thing in the world.
[575.28 → 587.08] And as far as, like, some of the sort of configuration he'll stuff goes, I think that a lot of what we complain about with these frameworks is not that there is a framework.
[587.36 → 594.70] It's that the way that these things have been developed is with, like, vertical integration patterns rather than horizontal integration patterns.
[594.70 → 606.72] So we build these frameworks that have these plug-in stacks where everything sort of linearly depends on the next thing, rather than building, like, an ecosystem out of smaller components that are more leverageable independently and interact with each other more independently.
[607.02 → 611.26] So if you look at, like, the earlier days of Node, that was kind of how the whole system worked.
[611.26 → 619.66] And then eventually people started building these frameworks, and then you started to see a lot of packages that were literally just taking some packets from the Node ecosystem and then wrapping it in the plug-in wrapper of some framework.
[620.20 → 622.72] And that is a problematic pattern to be building on.
[622.80 → 626.92] And I think that we are definitely at, like, the height of the sort of cycle for some of these bigger frameworks.
[627.10 → 629.96] And a lot of that needs to sort of implode so that that can then be used.
[629.96 → 638.58] But we're still going to be left with, you know, an NPM with a million plus packages and sorting through all those packages because that's what it's like to work in a healthy ecosystem.
[639.32 → 640.24] How am I doing on time?
[640.70 → 641.72] 22 seconds left.
[642.46 → 649.04] I think I'll hand it over to FIRAS where he can take all sides and win by default.
[650.02 → 653.92] So, FIRAS, you have, I don't want to say the easiest position here, but you can play in the middle, right?
[653.96 → 654.80] You got It Depends.
[654.90 → 656.90] So how do you want to represent It Depends?
[656.90 → 662.80] So I basically get to cherry-pick the best arguments from Divya and Michael and restate them in my own words.
[662.80 → 664.14] This is not fun for anybody.
[665.78 → 667.24] I want to hear this haiku again.
[667.42 → 669.70] Divya, before Franks, can you say that once again?
[670.12 → 671.10] Oh, yeah, of course.
[671.60 → 672.06] Yeah, sure.
[672.50 → 678.04] Many packages, new frameworks built all the time, config hell, webpack.
[678.52 → 684.26] I feel terrible because I essentially threw webpack under the bus here, and I use it a lot, and it's great.
[684.26 → 687.04] And their documentation is wonderful and Sean Locking is wonderful.
[687.56 → 689.98] They do have a huge configuration file.
[690.22 → 692.14] It's like unbelievable to manage.
[692.76 → 693.14] Yeah.
[693.42 → 693.68] Yeah.
[694.18 → 694.92] All right, for us.
[695.04 → 695.66] It depends.
[696.14 → 696.32] Yeah.
[696.46 → 707.08] So I guess I want to just start off by saying that in general, I feel like I'm very sympathetic to this argument that modern JS tooling is too complicated.
[707.08 → 716.16] And I've gone on my fair share of rants about it, especially when dealing with some tool that I feel is more complicated than it needs to be.
[716.46 → 721.88] Whenever that happens, I do tend to feel like we've created a lot of problems for ourselves that we didn't need to create.
[721.88 → 730.70] A lot of times I feel like when nerds are being nerds, they can invent sort of unnecessary problems for themselves.
[731.10 → 738.44] Like an example of this that I encountered a lot a few years ago was people would send a pull request to an open source project that I was in charge of.
[738.84 → 741.38] And they would be like, I converted everything to the newest syntax for you.
[741.46 → 741.90] Here you go.
[742.22 → 747.72] Oh, and also I added like 15 Babel plugins so that we can compile it back to ES5.
[747.72 → 750.18] You know, and they changed every single line in the project.
[750.48 → 752.14] You hated this so much you wrote standard.
[752.86 → 753.18] Yeah.
[754.50 → 759.16] Basically, it's one of those things where it's like we have to ask ourselves, what are we doing?
[759.34 → 760.38] Like, what are we trying to do here?
[760.48 → 765.30] Like when we use these new features, are we being enabled to do something that we weren't able to do before?
[765.90 → 769.42] You know, certainly some language features are actually game changers in that way.
[769.48 → 773.58] You know, they let us completely do something that we couldn't like, you know, like a new browser API, for example.
[773.82 → 775.96] This is not exactly JavaScript, but it's in the browser.
[775.96 → 779.54] If the browser gives you a new API, you can actually do entirely new things.
[779.68 → 786.00] Like suddenly now I can do WebGL or I can do WebRTC or I can, you know, I can draw into a canvas, or I can access Bluetooth devices.
[786.40 → 790.58] Like that's actually, you know, complexity that's worth taking on if it actually gives you something in return.
[790.90 → 796.88] But something like, you know, adding ES classes to your package, you know, converting the old way to using new ES classes.
[797.28 → 798.80] Doing that now maybe makes sense, actually.
[798.86 → 800.50] I'm starting to do that, actually, to all my packages.
[800.50 → 808.58] But doing that like five years ago, back when you just had to take on all this complexity of a build tool chain, doesn't necessarily make sense to me.
[808.68 → 812.24] I'd rather just wait it out, wait a couple of years till it's in more environments and then convert.
[812.70 → 813.86] So that's one thing.
[813.90 → 815.90] I think a lot of the problems is us doing it to ourselves.
[816.46 → 818.02] And so that's what I would like to push back on.
[818.02 → 825.56] And I guess I'll also say that JS is kind of a lot like Perl in some ways, where, you know, Perl's motto is that like there's more than one way to do it.
[825.88 → 829.54] And Python has sort of the opposite motto, like there's only one way to do it.
[829.82 → 832.62] And so in JS, there's always different competing approaches for doing things.
[832.62 → 837.46] And so that is also a source of this complicated tooling because we sort of have a lot of options.
[837.68 → 843.24] And that's not necessarily bad, like Michael was saying, you know, the best can win, and we can have this competition of ideas.
[843.24 → 855.52] But I guess to represent the other side, so the flip side of this is that when you ignore all the ways that we're sort of creating unnecessary complexity and you sort of zoom out and look at the problem we're trying to solve, like we're actually trying to solve pretty hard problems with JavaScript.
[855.92 → 859.02] And so it kind of makes sense that the tooling is going to be a little bit complicated.
[859.52 → 863.84] And, you know, you can definitely find lots of examples where the tooling is just the right amount of complicated.
[864.28 → 867.28] There's this difference between essential complexity and incidental complexity.
[867.90 → 872.56] So essential complexity is like this problem is actually hard and like the solution therefore must be hard.
[872.56 → 873.88] This is like, no, there's no way around it.
[873.94 → 881.64] And then there's like incidental complexity, which is like we just solved it in a bad way, and we created all this extra, you know, garbage that basically people have to deal with forever.
[882.12 → 892.04] You know, we are doing a lot of hard things like trying to make a website that loads instantly and, you know, has 60 frames per second and is accessible and looks great and handles all the error states.
[892.60 → 894.54] You know, no bugs, beautiful animations.
[895.28 → 897.26] That's an example of actually a really hard problem.
[897.74 → 901.56] So I think that complexity is really unavoidable.
[901.56 → 903.64] That's essential complexity a lot of the time.
[904.62 → 905.48] How am I doing on time?
[905.82 → 906.58] You got five seconds.
[906.74 → 907.18] Okay, great.
[907.28 → 908.20] I'll rest my case.
[908.84 → 909.34] Ding, ding, ding.
[909.44 → 909.74] All right.
[909.78 → 911.76] So we have three takes in here.
[911.84 → 914.94] So we began this debate thinking we'd have two teams, but we ended up with three.
[915.02 → 917.48] So we got team yep, team nope, and team it depends.
[917.88 → 926.96] And when we come back, we're going to dive a little bit into more of some back and forth, a little bit shorter segments so we can kind of converse around the complexity and maybe switch sides even.
[926.96 → 927.42] We'll see.
[927.42 → 941.06] This episode is brought to you by Keen.
[941.34 → 943.22] Keen makes customer-facing metrics simple.
[943.58 → 948.74] It's a platform that gives you powerful in-product analytics fast with minimal development time.
[949.04 → 954.16] For example, a DIY solution to build out customer-facing metrics in your product could take six months or more.
[954.36 → 956.16] And with Keen, you can be up and running at the same day.
[956.16 → 971.24] The Keen platform lets you stream events to easily collect and enrich your data, compute with embeddable answers, insights, and metrics, access controls so you can design role-based access to your data, and, of course, a visualization layer to create stunning charts.
[971.66 → 974.56] And we have a special offer just for our JS Party listeners.
[974.94 → 980.12] Go to keen.io slash js party and get your first 30 days of Keen for free.
[980.12 → 986.82] And as a bonus for checking out a 15-minute demo of Keen's customer-facing metrics, they'll send you a free Keen t-shirt.
[987.14 → 989.38] Go to keen.io slash js party.
[989.60 → 991.80] Again, keen.io slash js party.
[1005.08 → 1006.44] We are back.
[1006.44 → 1012.84] The question on our minds here is, is modern JavaScript tooling too complicated?
[1012.98 → 1015.88] So we've got Team Yep, Team Nope, and Team It Depends.
[1016.36 → 1021.08] Now we're moving into more of a section of shorter spurts, more conversational, some interruptions.
[1021.28 → 1025.00] But let's open it back up to Divya with Team Yep.
[1025.72 → 1030.02] What do you want to open up with here for your counter-argument or maybe an attack?
[1030.08 → 1031.18] Who knows what's going to happen here?
[1031.42 → 1033.42] I'm going to stop by appealing to authority.
[1034.08 → 1034.56] Oh, boy.
[1034.56 → 1036.24] I'm going to pull a from.
[1036.30 → 1037.48] Back to Hacker News?
[1038.12 → 1038.78] No, no.
[1038.96 → 1039.26] Okay.
[1039.26 → 1043.84] This is actually a credited source, i.e. Yehuda Katz's blog.
[1044.10 → 1044.42] Okay.
[1045.30 → 1046.24] Bring it on, Yehuda.
[1046.54 → 1047.74] That's not just an opinion.
[1048.16 → 1049.44] That's a fact.
[1051.14 → 1051.54] Exactly.
[1051.68 → 1052.30] It's not an opinion.
[1052.42 → 1052.92] It's a fact.
[1052.92 → 1060.18] He created a framework called Ember.js and therefore whatever he has to say is valid and sits on TC39.
[1060.38 → 1062.02] So I guess valid.
[1062.62 → 1067.92] Anyway, in a blog post that he wrote that was, I can't find what it's called.
[1067.92 → 1069.88] I'll figure out where it's from exactly.
[1070.10 → 1072.54] But the point he was making, and I'm going to quote,
[1072.54 → 1102.54] 
[1102.54 → 1110.10] it's like a critique on the fact that the modern JavaScript tooling is just frustratingly complicated, which is the point that I was making.
[1110.32 → 1118.50] But it's also the point that he's trying to make here is that it's complicated, but we made it such, which is what Farms was mentioning.
[1118.50 → 1125.64] Because we as developers, as JavaScript developers, almost shot ourselves in the foot because we were like, we need all of these things.
[1125.74 → 1126.50] We have these problems.
[1126.50 → 1127.46] We need to solve them.
[1127.56 → 1133.54] And so we've created extra tooling in order to solve those problems, which has been great because, yes, they've solved problems,
[1133.62 → 1143.10] but they've also added extra dependencies and extra things for us to think about whenever we create, when we think about frontend, or we create a project in JavaScript.
[1143.10 → 1157.22] And so the other thing also on top of that is that when you create applications in JavaScript, a lot of the times you pre-optimize your application for problems that you imagine you would have,
[1157.30 → 1158.74] but you might not have at the moment.
[1159.24 → 1162.64] And so you might be like, I want my application to run really fast.
[1162.78 → 1168.68] And so I'm going to optimize for performance, even though you don't have the numbers for you to need to do that just yet.
[1168.68 → 1178.08] Yeah, performance is really important, whatever, but is it worth putting in that extra time and that extra tooling and dependencies in order to optimize for a problem you don't have?
[1178.18 → 1178.72] Maybe not.
[1179.38 → 1189.12] And so in a sense, like within the ecosystem, there's this push towards, yes, like new and doing things better, which is like what Michael was mentioning, which is great.
[1189.22 → 1191.74] But it's also like, do we need to do this all the time?
[1191.74 → 1204.92] If we have a solution that works, do we need to constantly iterate on at the speed that we're currently iterating on in order for the tooling to improve or in order for us to be more effective or to build better applications?
[1205.34 → 1206.86] And I would argue that's not the case.
[1206.94 → 1211.84] A lot of the times we introduce this complexity when we don't need it half the time.
[1212.30 → 1216.48] For instance, React, and I hate to like to throw specific frameworks under the bus or whatever.
[1216.88 → 1218.18] This is a specific part of it.
[1218.18 → 1221.66] They introduced Fibre, which is their new reconciliation algorithm.
[1222.16 → 1230.54] And like to this day, I have no idea why I would use it or like maybe because the applications I've built have never been to the scale that it would require it.
[1230.68 → 1235.52] But I still can't fully grok like why I would use it and like what use case.
[1235.62 → 1242.02] And I've never actually put it in an application of any form because to me, I'm like, that's a solution for a problem I do not have.
[1242.02 → 1244.80] But I know of use cases where people are like, this is great.
[1244.88 → 1248.52] I'm going to start using it even though you don't necessarily need it.
[1249.18 → 1250.80] And I hear this argument a lot.
[1251.04 → 1251.70] Same for TypeScript.
[1252.04 → 1254.06] I'm not someone who uses TypeScript a lot.
[1254.16 → 1255.70] I understand the arguments for it.
[1256.00 → 1260.66] I will not start using TypeScript because I'm like, this is a problem I currently do not have.
[1260.66 → 1268.84] And I don't want to add the added complexity just to be like, oh, it supports TypeScript because that is just not necessary.
[1269.32 → 1276.30] Yeah, that's like a sign of maturity, I think, to be able to be like, I've seen this before.
[1276.56 → 1277.90] I know it's going to happen.
[1278.00 → 1279.18] We're all going to jump on this thing.
[1279.62 → 1280.84] It's going to be super exciting.
[1281.20 → 1284.20] And then in a year from now, we're all going to be jumping on the next thing.
[1284.30 → 1286.12] And I'm just going to opt out of this.
[1286.12 → 1293.90] Yeah, and it makes it really painful too because I've been on teams where you're constantly evolving your tooling.
[1294.56 → 1301.44] And so it just causes like bringing back the term I talked about earlier, this like fatigue because everyone is just frustrated all the time.
[1301.86 → 1304.08] They're like, I have to constantly learn something new.
[1304.26 → 1309.36] And my knowledge from like two years ago is no longer valid now, which is incredibly frustrating.
[1310.02 → 1312.12] And I can say that truly about frameworks.
[1312.12 → 1318.30] So like React, I knew React two years ago, and cannot understand the React today with that knowledge.
[1318.58 → 1329.04] So I just want to point out like a limitation in what I can argue because like I actually just don't even have the facility to argue that frameworks are good and that like and that the complexity of frameworks is fine.
[1329.94 → 1338.30] So I'm like I'm actually like I have to limit my argument to like the complexity of modern tooling and modern JavaScript is too much.
[1338.30 → 1338.52] Right.
[1338.62 → 1352.66] And I think that a lot of what we seem to talk about are like actually problems with these vertical integration patterns where you have so much value tied up in the framework that when it adds a new thing, you have no idea why you would want to use it or if you should use it and why that code now belongs in your app.
[1352.84 → 1358.10] And you also like you're still using a framework that was built on a premise that no longer is valid.
[1358.10 → 1362.82] Like one of the things that I really want to get into is that like we don't have perfect information about the future.
[1363.04 → 1365.42] So we don't know what is going to stick around and what's going to die.
[1365.96 → 1371.26] And that really informs what we can say like we should or should not be doing or adopting because we just don't know.
[1371.78 → 1382.94] Like on Twitter today, or yesterday I was talking with Alex Russell, and he made mention of like think about all the time that we spent trying to work on things that were going to live forever and like none of them did.
[1382.94 → 1395.28] And I think particularly he was talking about Dojo and that's a really fun time in the framework wars because like literally everybody in JavaScript that thought that they were going to be maintaining a JavaScript code base for 10 years worked on Dojo and tried to make Dojo the thing for that.
[1395.46 → 1397.98] And 10 years later Dojo is just dead and nobody uses it.
[1398.32 → 1402.98] But jQuery, the one that like nobody was trying to preserve for the long term, is still pervasive.
[1404.36 → 1411.42] And so like we just we don't have good information so we kind of like have to just let like a lot of stuff happen and have a lot of churn happen.
[1411.42 → 1415.04] The issue that we get into though is that the platform is not static.
[1415.16 → 1416.18] The platform is a moving target.
[1416.70 → 1419.96] And as the platform improves we need to be able to shed a lot of this tooling.
[1420.56 → 1425.30] And the issue with vertical integration patterns is that all the value is locked up inside one giant framework.
[1425.78 → 1428.38] So when the platform catches up you can't just ditch a bunch of that.
[1428.74 → 1431.68] Like I remember when React was launched the whole thing was like about DOM diffing.
[1431.86 → 1434.20] Like the value of it is this virtual DOM thing.
[1434.34 → 1436.92] And like then we made the DOM fast and who gives a shit now.
[1436.92 → 1442.76] But like we're still using React because of like I don't know there's like other features that people rely on in it.
[1442.86 → 1443.98] So we're just using the whole thing.
[1444.24 → 1448.64] The component model has been useful for getting people to sort of all write their components in the same way.
[1448.88 → 1452.80] And then now we have web components, and they can't adopt it because they're on their own pattern.
[1452.96 → 1453.08] Right.
[1453.18 → 1457.14] And we can't like to take this feature upgrade from the platform.
[1457.14 → 1465.20] I think you know there's a ton of other examples of this where like the platform starts to catch up and then frameworks can't.
[1465.32 → 1469.10] I think that like if you want to look for a model that is much better.
[1469.40 → 1469.50] Right.
[1469.58 → 1472.64] Like look at what happened with CSS frameworks for the longest time.
[1472.70 → 1472.80] Right.
[1472.84 → 1476.90] So there was like a new sort of bootstrap thing like every week for a couple of years.
[1477.08 → 1480.90] And there's all these different grid frameworks and flex box frameworks and all these things.
[1481.00 → 1483.08] And they're all just like CSS that you can add into a page.
[1483.08 → 1490.16] And because it's just like that simple add of that CSS into a page when CSS grid happened we just stopped including those.
[1490.66 → 1493.78] And because CSS grid is actually just better than all of those frameworks and components.
[1494.24 → 1500.44] When the platform caught up we were actually able to remove complexity even though we still had this big ecosystem.
[1500.68 → 1503.42] And now we're building like a new better ecosystem on top of grid.
[1503.92 → 1509.66] And that's like that's an argument for change for more things happening for actually more choices at the end of the day.
[1509.78 → 1512.50] And more complexity for you to kind of deal with and sort through.
[1512.50 → 1516.84] But what you end up with is like a tool chain and an application that fits your needs a lot better.
[1516.94 → 1518.36] And it's actually like easier to reason that.
[1518.98 → 1520.44] What about this concept of maturity?
[1520.80 → 1525.84] Like I don't think that the web platform is unmatured.
[1525.96 → 1526.72] It's been around for a while.
[1526.76 → 1527.58] It's got a lot of users.
[1527.92 → 1528.80] A lot of developers.
[1530.24 → 1537.36] But the concept of complexity and progress it's not so much that it's unstable.
[1537.82 → 1538.52] Because it is stable.
[1538.92 → 1540.12] But there's progress happening.
[1540.12 → 1542.08] So that means that tooling will always change.
[1542.18 → 1547.04] Divya you mentioned you know your knowledge of React two years ago will not really help you much today.
[1547.26 → 1548.68] Or something to that extent.
[1549.20 → 1552.18] You know is the state of our JavaScript tooling today.
[1552.26 → 1553.28] While it may be complicated.
[1553.70 → 1554.50] That's what we're debating.
[1555.14 → 1555.98] Is it mature?
[1556.34 → 1557.30] Or is it still maturing?
[1557.98 → 1560.68] I think it's about to completely shift again, actually.
[1561.62 → 1562.34] I mean yeah.
[1562.36 → 1563.88] You just had modules land in the browser.
[1564.12 → 1566.10] Like we haven't really taken that on yet.
[1566.10 → 1569.82] So we're due for like another big sort of shift.
[1570.56 → 1571.06] So yeah.
[1571.12 → 1572.74] I wouldn't say at all that it's stable.
[1572.94 → 1575.38] I mean the platform is changing faster than it's ever changed.
[1576.06 → 1577.36] So would you say that.
[1577.58 → 1578.64] Would you agree with this then?
[1578.72 → 1579.80] As our tooling advances.
[1580.08 → 1582.02] So does the complexity around our tooling.
[1582.48 → 1583.64] Well I wouldn't call the platform tooling.
[1583.78 → 1583.90] Right.
[1583.94 → 1585.68] Like the platform is what we build the tooling on.
[1585.72 → 1586.64] And what we rely upon.
[1586.64 → 1587.96] And to some extent.
[1588.12 → 1591.40] Like if the tooling is masking over deficiencies in the language.
[1591.40 → 1592.68] You can basically say.
[1592.84 → 1594.60] Those things are going to need to change in the future.
[1594.86 → 1595.04] Right.
[1595.40 → 1597.70] Like your sort of know that those are going to need to change in the future.
[1598.14 → 1600.90] You can look at a lot of the patterns that Node developed internally.
[1600.90 → 1602.16] Because they didn't exist yet.
[1602.50 → 1603.76] And now we've had to move beyond.
[1603.88 → 1605.40] Like past them once the platform caught up.
[1605.46 → 1606.20] And that's been really painful.
[1606.50 → 1606.70] Right.
[1607.18 → 1608.56] Buffer is a great example of that.
[1609.22 → 1609.42] Yep.
[1609.74 → 1609.90] Yeah.
[1610.02 → 1610.26] Buffer.
[1610.54 → 1611.96] The standard callback API.
[1612.88 → 1613.32] Streams.
[1613.48 → 1613.76] Jesus.
[1614.64 → 1615.08] Yeah.
[1615.08 → 1617.62] Whenever you're inventing your own error handling mechanism.
[1617.62 → 1619.76] You are covering up a deficiency in the platform.
[1619.76 → 1621.04] That is like just dead.
[1621.36 → 1622.26] But sometimes you have to.
[1622.34 → 1623.32] Like you just have no choice.
[1623.32 → 1623.56] Right.
[1623.60 → 1626.34] Like I don't think that like Facebook stood out going like.
[1626.42 → 1627.16] You know what you should really do.
[1627.18 → 1629.86] Is just like rewrite the DOM as a diffing mechanism in JS.
[1629.86 → 1631.94] Like they had a problem that they needed to solve.
[1632.06 → 1633.10] Because the DOM was too slow.
[1633.34 → 1634.30] And that was how they solved it.
[1634.68 → 1638.68] It's just that because of the way that they decided to present the solution to that problem.
[1638.84 → 1642.08] It was very hard to like to remove that when the platform had caught up.
[1642.48 → 1644.26] One thing we should mention is that.
[1644.26 → 1649.60] It's important to make sure that the tools you're using solve problems that you actually have.
[1649.94 → 1653.30] I think that's a huge source of unintentional complexity.
[1653.58 → 1655.62] Or what I called incidental complexity earlier.
[1655.86 → 1658.26] If you adopt a tool because everyone else is adopting it.
[1658.36 → 1663.32] And that tool was meant for a company that's a thousand times your size.
[1663.90 → 1665.20] You know you're going to have extra complexity.
[1665.34 → 1667.16] That's going to be solving problems you don't have yet.
[1667.16 → 1674.96] And now you might argue that you know maybe it's good to be using a tool that can scale when you're ready to handle that much traffic.
[1675.14 → 1675.78] But let's be honest.
[1676.34 → 1677.96] Your app's probably not going to get that popular.
[1679.42 → 1682.66] If your app gets that popular I guarantee you'll have very different problems.
[1683.06 → 1684.06] Like I mean that's the thing.
[1684.14 → 1688.10] Is that any app of a particular scale is going to have unique problems to that app.
[1688.10 → 1691.86] And this is the issue with cargo cutting culture in tech in general.
[1692.08 → 1694.54] Is that like if you're not Google you don't have Google's problems.
[1694.70 → 1695.82] You probably don't need Kubernetes.
[1696.10 → 1698.56] Unless you're like running a cloud provider you don't need Kubernetes.
[1698.80 → 1699.06] Yes.
[1699.30 → 1699.84] I love this.
[1699.94 → 1700.76] I love that you brought this up.
[1701.22 → 1701.34] Yeah.
[1701.48 → 1705.26] And like unless you're Facebook you probably don't need all of React.
[1705.26 → 1706.60] I mean it's cute.
[1706.60 → 1714.82] So one of the things I'm super impressed by there was a post a few years ago on the high scalability blog.
[1715.06 → 1721.62] Which by the way a lot of people who love to add complexity read this blog because they're like oh what are the biggest players doing?
[1721.70 → 1723.10] Oh we need to adopt that as well.
[1723.32 → 1726.02] But anyway there's this great post on there about Stack Overflow.
[1726.46 → 1727.68] I think it was 2014.
[1728.28 → 1730.60] Maybe their architecture has changed a little bit since then.
[1730.60 → 1738.06] But in 2014 when they wrote this post they were dealing with 560 million page views a month.
[1738.58 → 1742.34] And they were the 54th most popular website in the world.
[1742.88 → 1747.94] They also ran the entire Stack Exchange network which at the time was over 100 different sites.
[1748.20 → 1750.08] All being powered by guess how many servers?
[1750.64 → 1751.50] 25 servers.
[1752.14 → 1756.94] Literally 25 servers that they just like directly SSH into to manage.
[1756.94 → 1762.94] Now you know no Kubernetes, no auto-scaling, no magical fairy dust you know cloud functions.
[1763.14 → 1763.80] It's called caching.
[1764.24 → 1764.56] Caching.
[1764.90 → 1767.28] Caching fixes most of your problems, actually.
[1767.46 → 1771.40] Yeah and this is a site that actually is quite makeable.
[1771.62 → 1775.06] So I mean maybe your problem is not exactly as easy as Stack Overflow's problem.
[1775.18 → 1777.34] I mean Stack Overflow still has writeable stuff.
[1777.42 → 1780.02] I mean a dynamic website so it's not completely static.
[1780.02 → 1786.94] But yeah the point is that they decided for them that they wanted to go with boring well understood technology.
[1787.32 → 1789.04] And that served them incredibly well.
[1789.16 → 1791.44] And I kind of admire the simplicity of it.
[1791.62 → 1796.46] I mean the fact they managed to go that big and still have a system which they can fully understand.
[1796.58 → 1797.54] I mean it's 25 servers.
[1797.88 → 1800.34] They're running basic things like a SQL server you know.
[1800.48 → 1802.58] And that's like a well understood technology.
[1802.58 → 1806.62] I think that people don't think about the idea of like technical risk enough.
[1807.08 → 1813.16] And what is the downside of adopting a tool in a few years when everybody who was using it has moved on.
[1813.28 → 1815.44] And now you're stuck using this tool that no one's maintaining.
[1815.98 → 1820.64] And that you don't even understand how it works because you adopted it you know hastily.
[1820.80 → 1822.86] And now like you're the one who has to fix the bugs in it.
[1823.50 → 1825.20] But that's a good differentiator though right.
[1825.30 → 1830.96] Because that creates a very clear separation between the kind of like I want to use this boring thing because it's a thing that I know.
[1830.96 → 1834.70] Or I want to use this boring thing because like your new crazy thing may not work out.
[1835.14 → 1842.86] Because if you're talking about certain upgrades and certain shifts you have some certainty that it's actually going to be around right.
[1843.10 → 1850.18] Like I moved you know I usually don't adopt new language features when they're not even in like the stable version of Node.js.
[1850.84 → 1855.96] But there were a bunch of applications where like I took async generators in and was like running them I think under a flag.
[1855.96 → 1859.94] Because it was so much better than using streams.
[1860.54 → 1863.12] And I knew that this was going to stick around right.
[1863.20 → 1868.46] Like in the future we will be doing more things with async generators rather than with streams.
[1868.54 → 1871.04] Because that is an older API, and we're moving past it in the language.
[1871.22 → 1872.50] There's some certainty there right.
[1872.74 → 1876.14] And that's a level of certainty that you wouldn't have in adopting something like say TypeScript right.
[1876.20 → 1879.34] Where it's like not actually on a path to be adopted in language and everywhere.
[1879.62 → 1882.96] It is like its own sort of side community, and you don't know what the future of that is.
[1882.96 → 1887.06] And if you look at the future generally of compiled two languages it's not great right.
[1887.96 → 1889.90] Like what happened to CoffeeScript?
[1890.78 → 1894.30] There's this thing I like to say that technical bets are multiplicative.
[1895.16 → 1905.30] So basically every time you make a decision to use a new piece of technology you have to decide what is the likelihood that this thing is going to have a problem that's going to destroy my project.
[1905.60 → 1909.48] Or like be a huge source of work to rewrite basically.
[1909.48 → 1916.06] And so you want to basically you want to know that adopting a new technology is not a pure good.
[1916.18 → 1920.92] There's a trade-off and that trade-off is like what happens when it turns out it was a bad idea.
[1921.04 → 1922.12] And I thought that it was a good idea.
[1922.16 → 1923.66] I mean I obviously thought it was a good idea at the time.
[1923.70 → 1929.94] But what happens if the community disappears, or it's replaced by another model, and we have to rewrite everything.
[1930.62 → 1933.22] So like you can do a certain number of technical bets.
[1933.32 → 1937.46] But you don't want to just every time you have a decision about whether to use a risky technology or a safe technology.
[1937.46 → 1939.20] You don't want to always choose the risky technology.
[1939.34 → 1940.34] That's just a recipe for disaster.
[1940.68 → 1942.98] You want to be very careful about the risk you take on.
[1943.40 → 1948.84] And like your example Michael of like choosing a thing that you know is on the standards track, and you know is very likely to stick around.
[1949.32 → 1950.48] I mean you could have been wrong.
[1950.74 → 1951.98] Like decorators for example.
[1952.18 → 1958.04] Those people thought were on a standards track and now JavaScript decorators are like stuck in whatever stage three or stage two.
[1958.22 → 1958.30] Right?
[1958.60 → 1960.56] They had landed under a flag in nodes.
[1960.78 → 1963.92] They were past like the point where they were going to be changed to that degree.
[1964.32 → 1965.60] For async generators.
[1965.60 → 1966.54] Yeah yeah sure sure sure.
[1966.62 → 1971.46] So you're my point is just that like you know even things that seem like they're sure bets that they're on the standards track.
[1971.64 → 1974.18] You can still kind of get owned if you're not if you're unlucky.
[1974.66 → 1979.10] So like I would say that you know your decision to do that was probably like what like pretty good.
[1979.16 → 1981.48] Like you probably had like a 95% chance that it would work out.
[1981.62 → 1985.06] But you took on a little bit of risk that you decided was worth it because you were getting a much better.
[1985.66 → 1987.30] You were getting quite a bit of benefit from it.
[1987.66 → 1987.90] Right?
[1988.28 → 1988.46] Yeah.
[1988.46 → 1988.76] Yeah.
[1995.60 → 2010.88] This episode is brought to you by Linde our cloud server of choice.
[2011.08 → 2013.02] It is so easy to get started with Linde.
[2013.34 → 2015.26] Servers start at just five bucks a month.
[2015.54 → 2018.46] We host changelog on Linde cloud servers, and we love it.
[2018.46 → 2023.24] We get great 24 7 support Zeus like powers with native SSDs.
[2023.24 → 2028.64] A superfast 40 gigabits per second network and incredibly fast CPUs for processing.
[2029.10 → 2031.18] And we trust Linde because they keep it fast.
[2031.36 → 2032.30] They keep it simple.
[2032.66 → 2035.06] Check them out at Linode.com slash changelog.
[2035.06 → 2045.50] So we're back.
[2045.58 → 2049.38] We've been debating this concept of I guess not really a concept.
[2049.48 → 2052.74] It's the truth based on Divya potentially.
[2052.90 → 2053.92] She may want to switch sides here.
[2054.06 → 2057.02] But is modern JavaScript tooling too complicated?
[2057.62 → 2062.60] I might want to actually throw in a caveat to the question which is like for whom?
[2063.32 → 2063.52] Right?
[2063.52 → 2066.18] So you might have different style developers out there.
[2066.40 → 2069.22] Is it too complicated for a seasoned developer?
[2069.40 → 2074.34] Or is it too complicated for a newer or green developer or somebody who's newer to the field?
[2074.90 → 2078.16] You know maybe one extended version of that could be that question.
[2078.38 → 2079.02] Take it if you like.
[2079.58 → 2081.26] But this is a chance to play round-robin.
[2081.30 → 2082.12] Maybe switch sides.
[2082.80 → 2083.66] Maybe go rogue.
[2083.82 → 2084.54] Pick a different team.
[2084.62 → 2084.88] Whatever.
[2085.16 → 2086.40] So who wants to go first?
[2086.78 → 2088.18] I feel like Michael had an opinion.
[2088.38 → 2089.12] Yeah you should go.
[2089.26 → 2091.06] You're like in the midst of finishing.
[2091.06 → 2098.32] I think that when you start out doing development using something really high level like you were just talking about is what you tend to do.
[2098.48 → 2098.52] Right?
[2098.62 → 2101.78] Like you take an example, and you poke at it, and you make it do the thing that you want to do.
[2102.26 → 2103.84] And you sort of learn from there.
[2103.98 → 2105.40] And you sort of work your way down the stack.
[2105.40 → 2118.36] I think that where you start to run into problems is as you become a better developer, as you become more familiar with your tools, all of that understanding of how those tools work ends up sitting in your head and becoming the context that you program in.
[2118.74 → 2123.36] And you have to at some point limit the amount of complexity that you're going to keep in your head in order to get anything done.
[2123.36 → 2130.04] And so when we talk about complexity, we're not just talking about sort of surface complexity of an API.
[2130.48 → 2134.16] But we're also not really talking about the entire implementation complexity either.
[2134.40 → 2137.72] Because almost nobody keeps the entire implementation in their head when they do this stuff.
[2137.72 → 2140.72] I'm somebody who severely limits my tooling.
[2141.20 → 2154.02] I've moved away from even graphical editors and back to Vim and back to doing all of my development on a remote server just so that I can severely limit the amount of tools in between me and my code and running and reading.
[2154.02 → 2163.46] But that said, it's really, really important to have a diverse and broad and really high growth ecosystem.
[2163.46 → 2170.48] If you don't have all of those things, then you're sitting in a corner of just the technology sphere in general that might die off.
[2170.62 → 2174.84] I mean, we're also talking about risk earlier and the risk that something may or may not be adopted.
[2175.36 → 2184.86] In ecosystems that do not have this growth problem, you literally run the risk of this whole thing that you're working with dying off and not that many people using it in the future.
[2184.86 → 2195.88] So I think that this is a very good problem to have in general and that we shouldn't throw up our hands and say like, oh, JavaScript fatigue or tooling fatigue or whatever.
[2197.28 → 2204.90] You know, we want and frankly, we need an ecosystem of tools that is too many for you to know all of them and to make a decision.
[2204.90 → 2212.02] Because that's the only sort of ecosystem that you can be confident will actually exist in the future and will still be solving the problem that you have.
[2212.02 → 2214.56] I think the growth of the ecosystem is always good.
[2214.66 → 2224.54] The fact that we have a lot of tooling and a lot of options, like that is a good thing because it is a sign, as Michael said, of a healthy language, in this case JavaScript.
[2224.54 → 2236.04] But one thing that I want all of these tooling to be more cognizant of is just is improving JavaScript as a language rather than having these forks of JavaScript, which currently exist.
[2236.36 → 2239.56] So, for instance, like there is tooling that pushes the envelope.
[2239.56 → 2247.72] So like, yeah, I talked about how I don't use TypeScript, but there are a lot of things that people have talked about in the TypeScript world that has helped like optional chaining.
[2247.72 → 2254.84] And I think the knowledge coalescing thing, which is like a lot of it was inspired by what was happening in TypeScript land.
[2255.50 → 2259.66] And same for like CoffeeScript with CoffeeScript had error functions and a couple of other things.
[2260.12 → 2262.54] And then that's like, yes, 2015 now adopts that.
[2262.72 → 2268.46] And so it's really nice because these tooling that existed helped make JavaScript better.
[2268.46 → 2272.34] But I would argue that that's not all tooling and all libraries.
[2272.34 → 2278.04] So oftentimes, like, you know, we were talking about React and not being compatible with Web Components.
[2278.28 → 2282.34] Web Components is a standard that's been in conversation for a long time.
[2282.34 → 2285.52] And Google tried to create like a framework called Polymer.
[2285.52 → 2289.18] And not a lot of people, actually, I think only Google uses Polymer.
[2289.84 → 2296.02] And the frameworks don't necessarily like feed back into improving JavaScript because they're kind of forking off.
[2296.62 → 2302.04] And so React, I think, is, you know, Vue, Angular, like all these frameworks are kind of guilty of this in that.
[2302.34 → 2304.38] They're like, this is the way JavaScript should be.
[2304.56 → 2308.28] And that conversation of like, how can we make JavaScript overall better?
[2308.58 → 2310.18] That feedback doesn't come back in.
[2310.28 → 2321.06] And I think I've heard rumblings of conversations where TC39 has been trying to reach out to framework authors to get their opinions on like how they've been solving specific things.
[2321.28 → 2326.04] And whether and how they can take those ideas and integrate it into the language itself.
[2326.26 → 2329.22] I'm not sure how that conversation is going per se.
[2329.22 → 2337.46] Because, again, I think a lot of the times is whenever you have these frameworks, a lot of it is more I want my framework to win rather than I want JavaScript to win.
[2337.54 → 2345.42] Or that is what the conversation seems to be, which I think is terrible because I'm like, ultimately, we're all JavaScript developers.
[2345.70 → 2348.32] Yeah, you do React, you do Vue, Angular, Ember, whatever.
[2348.60 → 2351.12] But we want the ecosystem to succeed.
[2351.22 → 2352.56] We want the language to succeed.
[2352.98 → 2356.40] And JavaScript is always going to be a first class citizen of the web.
[2356.40 → 2358.60] It's always going to be on the browser.
[2359.16 → 2360.96] And so how can we make it better?
[2361.20 → 2369.40] And I think that's something that I want our modern tooling to be more aware of and to build towards, which I don't think they are.
[2370.22 → 2374.32] Well, what you're saying is that complexity is a given.
[2374.74 → 2378.28] So get over it or find a way around it, for lack of better terms.
[2378.56 → 2379.08] Something like that.
[2379.10 → 2379.72] Is that right, Divya?
[2379.94 → 2381.30] Maybe you said it more softly than I did.
[2381.32 → 2382.54] I'm a bit more abrupt by it.
[2382.54 → 2386.00] Yeah, I think the ecosystem is complex.
[2386.46 → 2399.90] And because of the arguments that we made before, because we have problems and then we find solutions, and then we open source our solution and then other people use the solution, even though they have no context of what the problem was.
[2400.04 → 2404.48] And then that results in overall it being complex.
[2404.48 → 2407.44] But I think the idea is, so there are two ideas.
[2407.62 → 2411.36] There's my application and the way that I use JavaScript is complex.
[2411.50 → 2414.62] And then there's the overall, like, is the ecosystem complex?
[2414.76 → 2423.24] And I think the point Michael was making, and I kind of agree with that, is that the ecosystem is incredibly lush with tools and libraries.
[2423.24 → 2425.58] And so you can choose whichever you want.
[2425.76 → 2428.30] You can choose, like, an incredibly pared down version.
[2428.42 → 2431.50] Like, if you want to use React Lite, there's Preach.
[2431.76 → 2437.20] And, like, if you want to use more declarative framework, you can use Vue.
[2437.28 → 2440.38] And there's all these options you can use at your disposal.
[2440.38 → 2454.58] But I think there's also that part, which is my application or the thing that I'm working on is complex because I choose to, like, add all these extra things to pre-optimize my code base because my application is obviously going to be successful and scale.
[2454.58 → 2457.82] And so, like, that's kind of my issue with it.
[2457.82 → 2473.84] It's just that, in a way, we shouldn't curb the growth of the community because I think the fact that there are so many things means that people are actively contributing and actively working on things and thinking about problems, which I think is a great thing.
[2473.84 → 2486.44] But it's, like, how do we introduce that nuance to show developers, both seasoned and new, that certain tooling is not necessarily needed for every single use case?
[2486.44 → 2503.34] Because a lot of the arguments I've heard for certain libraries have been, you have to use this because your code will be better by it, which I think is incredibly subjective because I'm like, sure, maybe, but will it actually?
[2503.80 → 2512.18] And is it introducing more load and more weight to my code base to solve, like, one thing that I might not even have a problem for?
[2512.66 → 2515.18] So that's where I was coming from, yeah.
[2515.18 → 2524.94] Before Farah jumps in here, I want to mention this topic of you are not Google, Amazon, LinkedIn, et cetera, you know, choosing the right tooling for the job.
[2525.02 → 2529.50] We actually had this conversation on the changelog about two years ago now.
[2529.66 → 2534.00] As a matter of fact, August 4th, 2017, with Oz Nova.
[2534.50 → 2537.22] At the time, his last name was One, Oz One.
[2537.76 → 2543.02] He's actually an instructor at Brad field School of Computer Science, president of, actually, and one of the instructors.
[2543.02 → 2546.16] So if you want to hear more about that, we'll plug that in the show notes.
[2546.34 → 2549.16] But episode 260 of the changelog, we covered that.
[2549.72 → 2556.48] And that actually was based on a very thorough blog post, a very popular blog post as well from Oz.
[2556.86 → 2557.88] So I'll plug that.
[2557.98 → 2558.34] For us, anything?
[2558.34 → 2559.28] No, you go for it, Michael.
[2559.56 → 2566.28] I was just saying, how much of this has really just been about Webpack and React and the actual JavaScript ecosystem?
[2566.28 → 2576.98] And I do feel like Ember deserves a little bit of credit in that as the platform has changed over the last 10 years, they have done massive rewrites in order to accept those changes and to move along with them.
[2577.18 → 2581.80] And not maintain a sort of hostile position to them the way that React has treated Web Components.
[2581.80 → 2584.64] We've got nine minutes left in the show.
[2585.14 → 2587.38] Maybe can we talk about the future, Michael?
[2587.38 → 2591.66] You mentioned Web Components and this very large potential change.
[2592.24 → 2599.48] So if we are on the fence of whether tooling is or is not overly complicated, how can we simplify?
[2599.72 → 2604.66] Michael, you mentioned when you write your own code, and you start a project, you sort of simplify things.
[2604.66 → 2611.22] And so what are other ways that developers out there can sort of resist the complication or lack thereof if there isn't any?
[2611.62 → 2615.46] I feel like this is a terrible time to answer that question.
[2615.96 → 2618.46] Like I would have had a perfect answer like a few years ago.
[2619.16 → 2623.22] But this is a very transitional period for JavaScript and for the web.
[2623.46 → 2628.18] And so I feel like the tool that you probably want to adopt does not exist yet.
[2628.26 → 2629.46] And that is a problem.
[2629.46 → 2635.48] Like I think that most of what we rely on right now in the ecosystem is probably going to implode in the next year or so.
[2636.08 → 2636.48] Implode?
[2636.62 → 2637.48] I mean, it'll keep working.
[2637.62 → 2637.94] Such as?
[2638.60 → 2638.88] No.
[2638.88 → 2642.98] I actually don't think that a lot of it will keep working, to be honest.
[2643.04 → 2644.60] And the registry will go down.
[2644.68 → 2645.56] Can you be more specific?
[2646.20 → 2649.76] I think that like looking at Pike package is sort of enlightening, right?
[2649.90 → 2655.88] Because by literally drawing a line and just saying we're only using these new features that are available on the platform,
[2656.12 → 2660.26] they're able to provide an experience that's just really, perfect.
[2660.50 → 2664.72] Like way nicer than what you can get with like, you know, NPM plus a bundler, for instance.
[2664.86 → 2665.90] Can you go into that a little bit?
[2665.96 → 2666.66] What makes it nicer?
[2666.66 → 2669.38] So they only use the new module syntax.
[2669.88 → 2675.60] And as a result, do not actually need a bundler and a loader because they can be directly loaded from the browser.
[2676.28 → 2679.74] So their job as a package manager is just fundamentally different.
[2679.86 → 2682.04] So in practice, though, when you ship your site, don't you still bundle?
[2682.04 → 2690.72] Because the performance from downloading like 100 separate, you know, modules with 100 separate HTTP requests is still too much.
[2691.46 → 2691.58] Yeah.
[2691.64 → 2692.50] See, that's the thing, though, right?
[2692.56 → 2697.92] Like right now you're coming at this from the point of view of you have two options, right?
[2697.92 → 2700.34] You either like load 100 files or you use a bundler.
[2700.34 → 2708.20] But if all of your dependencies were using these new standards, you would actually have like quite a few options in between, right?
[2708.26 → 2716.90] Like you could actually use much more sophisticated loaders that did some bundling for you dynamically, that loaded a few packages together, but not all of them.
[2716.90 → 2723.26] You know, you can start to rely upon HTTP2 and just say like, oh, yeah, no, we are going to give you every individual file, but we're going to do it all at once.
[2723.40 → 2725.16] So it would be the same as a bundle, for instance.
[2725.82 → 2732.84] Your options open up a lot wider once you say we're just not going to support all the old syntax, essentially.
[2732.84 → 2742.76] And I mean, the reason why I would bring this up is just something to look at and think about because it opens up a lot of possibilities that we don't have with the NPM plus bundler scenario.
[2743.02 → 2751.28] But adopting them would require us to basically drop all of, you know, almost all the current NPM registry and reimplement a lot of things.
[2751.42 → 2756.14] I mean, they wouldn't, a lot of this code would not be substantial code changes, but, you know, quite a few.
[2756.26 → 2759.22] I mean, I'm still writing modules that have a require statement in them.
[2759.22 → 2762.82] So obviously, like, I have not transitioned to that being this tooling does not exist.
[2763.32 → 2767.86] But you can see something is coming up on the horizon that's going to change things pretty fundamentally.
[2768.54 → 2776.12] It doesn't seem like it'll be too hard to, like, switch your app to using this bundler when the time comes if you wanted to, right?
[2776.24 → 2782.18] I guess the question I have is no dependencies in your entire dependency tree can not use the new syntax.
[2782.32 → 2783.00] But they can.
[2783.18 → 2784.36] That's a substantial change.
[2784.36 → 2801.54] But in theory, like, if I'm sitting there using, you know, Browser or Webpack or something like that, and over time, more and more of the modules that I depend upon are shipping an ES module version over time, my, like, Browser or Webpack tooling is just going to keep working just fine.
[2801.90 → 2805.28] I might not be getting the like, these benefits that you talk about from Pike package.
[2805.28 → 2814.10] But, like, one day when, like, most of the things I depend upon are using this ES module syntax, then I can go ahead and swap out Browser or Webpack for this new stuff.
[2814.46 → 2814.58] Right?
[2814.66 → 2817.24] But, I mean, in the meantime, I can continue to ship a working app to my users.
[2817.44 → 2827.42] And my users will be happy that, like, I'm not spending all my time debugging, like, bundler problems, which, you know, isn't helping them, you know, with their problems in life.
[2827.56 → 2829.72] I just don't think that that's how ecosystem upgrades work, though.
[2829.72 → 2835.64] Like, I mean, so we've gone through a few sort of minor upgrades to the platform like this already, right?
[2835.86 → 2839.74] And, you know, we've had upgrades to Node.js as well.
[2839.92 → 2846.02] And when you look at the ecosystem, one, we have not been able to drop anything old, like, basically anything.
[2846.42 → 2854.14] Because somewhere in your giant sort of 800 to 8,000 modules dependency tree is something that relies on that that nobody's touching.
[2854.60 → 2859.06] That's, like, such a transitive dependency and so deep in the web tree that you can't update everything and get at it.
[2859.06 → 2864.08] So things, like, just don't actually go away once you have these giant depth trees that continue to grow.
[2864.48 → 2872.56] So we have to support that stuff indefinitely, which means that if there is a new feature that in order to use we have to drop old support, we just don't have access to it until we make a hard shift.
[2873.10 → 2877.36] The other thing, too, is that when you're building a new ecosystem, you're trying to, like, adopt a new ecosystem feature.
[2877.74 → 2880.14] There are some pretty big advantages to breaking compatibility.
[2880.40 → 2888.40] Like, if you just say, like, we actually don't work with everything before, you incentivize a new group of developers to be the first people to write all of those new things again.
[2888.40 → 2893.66] Like, one of the reasons why Node was so successful in the early days was because we were so incompatible with everything, right?
[2894.16 → 2898.78] Like, we had to, like, take all these old C libraries that use blocking I.O. and rewrite them in pure JavaScript.
[2899.26 → 2901.60] Like, you know, Python and Ruby didn't have to do that.
[2901.68 → 2903.90] And so they ended up with just binding layers for all of that.
[2903.96 → 2905.44] And we ended up with, like, this big ecosystem.
[2905.44 → 2912.84] So are there actually packages that are written using ES module syntax that don't work with old-fashioned bundlers?
[2913.32 → 2915.78] They work with the bundlers, but, like, again, move out of the...
[2915.78 → 2921.34] So think about just not using a bundler, using something that looks very different from the way that current bundlers work.
[2921.36 → 2924.40] Sure, but isn't that a decision that the user at the end makes?
[2924.50 → 2925.60] Like, I'm still confused.
[2925.76 → 2932.40] Like, are there going to be packages that are on NPM that I can't use unless I switch to using a different bundling system?
[2932.40 → 2937.38] Yeah, because the bundling system does not have a way to compile down the old syntax.
[2937.58 → 2938.20] There are also just...
[2938.20 → 2940.14] There are issues that you get into that you can't resolve, right?
[2940.18 → 2940.74] Like, you can't...
[2940.74 → 2943.96] You, like, can't have recursive dependencies, for instance.
[2944.06 → 2945.84] Like, that's a serious problem.
[2946.20 → 2946.72] Most...
[2946.72 → 2951.70] If you have a large enough depth tree with different versions of things, you usually end up with recursive dependencies somewhere.
[2952.38 → 2958.52] I'm still confused, because it seems like, basically, what you're saying is that there's, like, a new bundler that is out there called Pike,
[2958.52 → 2962.30] that if I use it, it actually restricts what modules I can use.
[2962.80 → 2963.56] It's not a bundler.
[2963.82 → 2964.58] Well, whatever you call it.
[2964.62 → 2966.56] It's a tool that helps you ship your JS to your users.
[2966.86 → 2967.48] Whatever you call it.
[2967.52 → 2968.08] What do you want to call it?
[2968.46 → 2969.68] It's basically a package manager.
[2970.08 → 2972.38] I mean, I would call it a pen...
[2972.38 → 2974.54] I'm trying to look at how they describe themselves.
[2975.70 → 2981.34] But it seems to me, like, basically, it's requiring packages to follow, like, a stricter set of rules.
[2981.50 → 2982.96] Basically, you can't use all these other things.
[2982.96 → 2991.66] But then, if I'm using a tool which can handle, like, you know, which is more lax, in other words, it never dropped support for old stuff, then wouldn't I just be fine?
[2991.78 → 2992.44] Now I get the best...
[2992.44 → 2998.34] Now I can continue using all my old stuff, and also, I can use these new things, because they're just using, like, a subset of the language.
[2998.44 → 2999.66] They're only using ES modules.
[2999.92 → 3000.46] So, great.
[3000.46 → 3001.02] I'll just use them.
[3001.06 → 3002.02] I'll just consume them the same.
[3002.38 → 3007.12] It seems like all I get from switching to Pike is I can use fewer modules.
[3007.44 → 3010.16] Unless I really like the other benefits that you talked about.
[3010.26 → 3017.36] But, like, as far as, like, which modules I can select, basically, Pike is a subset of what I can use if I just stick with my current tooling.
[3017.68 → 3018.74] I see what you're saying.
[3018.78 → 3019.00] I'm sorry.
[3019.08 → 3021.52] So, you're saying that if you don't take this upgrade...
[3021.52 → 3021.70] Yeah.
[3021.82 → 3024.26] ...then you can continue to use all of that value in the old ecosystem.
[3024.26 → 3024.50] Yeah.
[3024.64 → 3029.38] And until Pike is so useful, like, I really want the features of Pike, and enough of the ecosystem is updated,
[3029.38 → 3033.10] that now I can sort of do this shift to Pike, like, a couple of years after everybody else,
[3033.22 → 3037.22] and now I get all the sort of, all the benefits, and I had to do none of the suffering of, like,
[3037.48 → 3039.16] trying to be like, ah, I can't use this package.
[3039.32 → 3040.26] Ah, I can't use this package.
[3040.74 → 3041.12] You know what I'm saying?
[3041.78 → 3042.30] Sort of.
[3042.58 → 3042.82] Yeah.
[3043.20 → 3044.68] That's what happens when you get modern, right?
[3044.76 → 3047.62] Once you start moving forward, you have to leave something behind.
[3048.18 → 3048.48] Yeah.
[3048.72 → 3049.44] It's the law of physics.
[3050.28 → 3052.80] So, the question is, like, when do you want to leave stuff behind?
[3052.80 → 3058.16] Like, do you want to just sort of take the leap right now, or do you want to, like, defer it until more of the ecosystem has moved forward?
[3058.62 → 3059.16] I don't know.
[3059.16 → 3062.78] Like, this may just be, like, wearing that in my head with the code that I've been writing lately,
[3062.86 → 3066.66] but I've been working in really restricted environments where you can't take on a ton of dependencies.
[3067.90 → 3071.34] And I've effectively had to write all my dependencies again from scratch,
[3071.36 → 3074.82] because there just aren't enough packages that work like that.
[3074.90 → 3080.04] Like, the average thing that does something tiny in Node pulls in, like, 100 dependencies.
[3081.12 → 3085.34] That's like, I mean, we're incentivized to do that because it is so easy to depend upon all that stuff.
[3085.34 → 3089.72] It's not a bad thing, like, from the point of view of, like, Node.js.
[3090.22 → 3094.40] But, like, when I need that to run in the browser really fast in a tiny bundle size, it's problematic.
[3094.70 → 3099.32] When I need it to run in the Cloudflare worker and I have a limit on the amount of code that I can put in it, it's really problematic.
[3099.32 → 3103.42] And I don't think that we're going to have less of these constrained environments in the future.
[3104.48 → 3106.48] We got three minutes left in the timer here.
[3106.58 → 3107.62] Divya, I haven't heard from you in a while.
[3107.66 → 3108.22] What do you have to say?
[3108.70 → 3110.46] No, I was just listening on this conversation.
[3110.66 → 3118.30] I think, like, it's interesting because I haven't used Pike, so I have no reason, similar to what Fears was saying for switching just yet.
[3118.30 → 3126.90] And if anything, I would wait until there's a reason for me to switch, like, there's an actual problem that I'm trying to solve, which I don't have.
[3126.96 → 3136.36] Because I know that Pike apparently has, like, I've heard a lot about its optimizations for tree shaking and, like, less model dependencies and all of that.
[3136.36 → 3143.26] But I've never noticed a different, like, noticed that need in my applications for me to switch over.
[3143.46 → 3147.36] And I would use that argument for most tooling out there.
[3148.30 → 3149.98] I'm actually excited to try Pike.
[3150.08 → 3152.38] I don't want to come across as, like, a hater or anything.
[3152.64 → 3157.78] I just think that, like I was saying, you have a limited number of technical bets that you can make.
[3158.06 → 3163.22] So, like, if I'm already at my maximum limit, like, I'm like, this thing I'm working on is probably not going to work.
[3163.32 → 3165.82] It's, like, already so hard for me to do it.
[3166.04 → 3173.46] Do I want to add on the additional, like, risk of, like, oh, now I'm using, like, a bundler that, like, you know, is really bleeding edge?
[3173.46 → 3176.62] And, like, do I want to be the one who's filing the bug reports?
[3176.86 → 3180.82] Or do I want the people who came before me to have already figured out all the obvious bugs?
[3181.20 → 3181.38] You know?
[3181.52 → 3183.56] Like, it depends on if I have the bandwidth for that or not.
[3183.58 → 3188.50] And if I don't, then I want to stick with more, like, trusted, you know, reliable tools.
[3188.50 → 3192.38] I think you want to always scrutinize the tooling you use, though.
[3192.44 → 3203.42] So, I think your, you know, your pushback on Pike is wise because you want to understand why you should use it and what problems it really solves and whether it actually creates more for you.
[3203.84 → 3204.06] Exactly.
[3204.20 → 3208.00] Yeah, I mean, Pike right now is not, like, what I would recommend people to use, actually.
[3208.00 → 3228.64] It's just when you look at Pike and sort of understand what it can do in such a simple package by shedding a lot of the features of the past and by, like, wholly kind of adopting the new browser standards for modules, you realize that there's, like, a very large opportunity in the future for us to shed a lot of that and for us to build, like, much simpler, more reliable tooling.
[3229.40 → 3229.86] That makes sense.
[3229.86 → 3231.02] And so, yeah, yeah.
[3231.10 → 3238.28] So, I think that, like, it's done more to just sort of expand, like, what I think that the future is going to look like around this than it is, like, currently a solution to this problem.
[3238.66 → 3245.56] Yeah, and there's something that's really aesthetically nice about that idea of, like, we're just going to get rid of all the legacy crap that's, like, annoying.
[3246.00 → 3252.82] And for those that are listening, if you're new to Pike, like I am, you can find out more details at Pike, P-I-K-A dot dev.
[3253.18 → 3257.96] There's also a lengthy blog post titled A Future Without JavaScript.
[3259.86 → 3260.64] Hang on a second.
[3261.06 → 3261.50] Rewind.
[3262.66 → 3263.86] You already did that, yep, no.
[3264.86 → 3266.92] A Future Without Webpack.
[3267.76 → 3274.22] Written by Fred Scott, I believe the creator behind Pike on DevTools.
[3274.30 → 3279.10] We'll link that up in the show notes and put that on Change All News as well because I hadn't seen this yet.
[3279.14 → 3281.68] And that's something we should be spreading the news about.
[3281.86 → 3283.06] But this is a fun debate.
[3283.12 → 3284.52] I really enjoyed the format.
[3284.52 → 3290.68] I think even having to throw the curveball at ourselves with the, you know, it depends on section for us.
[3290.72 → 3291.82] I think you represent that very well.
[3292.62 → 3293.26] Did you represent it?
[3293.30 → 3293.82] Yep, very well.
[3293.90 → 3294.62] And Michael, nope.
[3294.76 → 3299.48] And I think in the middle there, we sort of all huddled around and said, bummer that it's so complex.
[3299.56 → 3303.40] Let's find ways forward and talking about where we're going actually in the future.
[3303.68 → 3307.66] So listeners, if you want to say hello to us, you can do so on Twitter.
[3307.66 → 3310.42] Remember, we're at jspartyfm.
[3310.54 → 3312.12] You can head back to the show notes.
[3312.22 → 3314.86] There's a link there that says discuss in Change All News.
[3314.98 → 3315.92] We love to hear feedback.
[3316.06 → 3318.12] We love to hear from you, our listeners.
[3318.32 → 3319.26] So we encourage you to do that.
[3319.38 → 3322.38] But Michael, Divya, Frost, thank you so much.
[3322.42 → 3322.72] It was fun.
[3323.14 → 3323.78] Yeah, this was great.
[3323.92 → 3325.22] Yeah, happy to be part of it.
[3326.66 → 3327.14] All right.
[3327.16 → 3329.02] Thank you for tuning in to JS Party this week.
[3329.02 → 3332.10] Tune in live on Thursdays at 1 p.m.
[3332.14 → 3335.18] U.S. Eastern at changelog.com slash live.
[3335.18 → 3338.18] Join the community and Slack with us in real time during the shows.
[3338.46 → 3339.94] Head to changelog.com slash community.
[3340.60 → 3341.28] And do us a favour.
[3341.42 → 3342.60] Share this show with a friend.
[3342.90 → 3344.08] We're just going to have a podcast.
[3344.30 → 3345.88] Go into Overcast and favourite it.
[3346.34 → 3348.60] And thank you to Vastly, our bandwidth partner.
[3348.94 → 3350.46] Head to fastly.com to learn more.
[3350.86 → 3353.48] And we move fast to fix things around here at Changelog because of Rollbar.
[3353.84 → 3355.42] Check them out at rollbar.com.
[3355.52 → 3357.72] We're hosted on Leno cloud servers.
[3358.10 → 3359.70] Head to leno.com slash changelog.
[3359.78 → 3361.16] Check them out and support this show.
[3361.62 → 3363.58] Our music is produced by Break master Cylinder.
[3363.58 → 3367.02] And you can find more shows just like this at changelog.com.
[3367.20 → 3368.16] Thanks for tuning in.
[3368.40 → 3369.18] We'll see you next week.
