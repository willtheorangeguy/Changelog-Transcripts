[0.00 → 8.26] At the end of the day, it does not really matter which of these testing frameworks you use, as long as your team likes it, because they all work.
[8.48 → 10.00] They're all going to test your code.
[10.54 → 17.32] And if you are getting really worked up about one's better than the other, I mean, like, find something better to do, right?
[17.50 → 22.40] Find something else to worry about, because, like, any of these are going to be able to test your code.
[22.40 → 27.48] A lot of the testing frameworks out there in JavaScript, they're all mature now, like the popular ones.
[27.64 → 28.56] They've been around the block.
[28.56 → 31.98] So it's really hard to go wrong with any of them.
[34.76 → 37.46] Bandwidth for Changelog is provided by Vastly.
[37.80 → 39.64] Learn more at Fastly.com.
[39.88 → 42.16] Our feature flags are powered by Launch Darkly.
[42.44 → 44.24] Check them out at LaunchDarkly.com.
[44.48 → 46.34] And we're hosted on Leno cloud servers.
[46.74 → 50.26] Get $100 in hosting credit at Leno.com slash Changelog.
[50.78 → 53.52] This episode is brought to you by DigitalOcean.
[53.98 → 54.54] Droplets.
[54.78 → 55.54] Managed Kubernetes.
[55.90 → 56.74] Managed databases.
[57.28 → 57.84] Spaces.
[57.84 → 59.00] Object storage.
[59.26 → 60.52] Volume block storage.
[60.78 → 64.26] Advanced networking like virtual private clouds and cloud firewalls.
[64.26 → 70.74] Developer tooling like the robust API and CLI to make sure you can interact with your infrastructure the way you want to.
[71.16 → 74.64] DigitalOcean is designed for developers and built for businesses.
[74.64 → 81.74] Join over 150,000 businesses that develop, manage, and scale their applications with DigitalOcean.
[82.06 → 85.48] Head to do.co slash Changelog to get started with a $100 credit.
[85.48 → 87.98] Again, do.co slash Changelog.
[87.98 → 101.46] Welcome, everyone.
[101.46 → 106.12] Welcome, everyone.
[106.50 → 111.62] You're listening to JS Party, a weekly celebration of JavaScript and the web.
[111.62 → 114.00] We record live on Thursdays.
[114.08 → 116.18] Join us, why don't you, on our YouTube channel.
[116.30 → 118.66] That's YouTube.com slash Changelog.
[118.74 → 122.58] Subscribe there and interact with us during the show at ChangeLog.com slash community.
[123.20 → 124.18] Okay, let's do this.
[124.24 → 125.74] Hey, it's party time, you all.
[125.74 → 142.72] Hello, party people.
[143.10 → 146.60] We're back again this week, and it's a very exciting show.
[146.86 → 149.78] It's like a throwback show and a reflection show.
[149.96 → 152.16] It's a good kind of end of year show.
[152.16 → 159.50] We have a very special not guest today, and I say not guest because he is a not guest.
[160.04 → 161.38] He is Chris Miller.
[161.74 → 165.24] You may know him as Bone Skull, and we're going to be talking to him.
[165.60 → 166.86] He's a panellist, obviously.
[167.02 → 169.10] Well, maybe not obviously if you're listening for the first time.
[170.04 → 175.68] But we're going to be talking to him about an important project in the web ecosystem called Mocha.
[176.08 → 181.76] It's an NPM package that is a test runner, and it's an important package, an important project,
[181.76 → 185.24] because Mocha is celebrating its 10-year anniversary.
[186.26 → 193.26] And for a JavaScript package to have survived 10 years and still be relevant is kind of miraculous.
[194.04 → 198.70] And so we're going to learn a little bit about what's the secret sauce to its success,
[198.70 → 205.54] as well as dive into what's it like to maintain a project that has such a long arc,
[205.54 → 209.44] you know where folks are using it across multiple node versions.
[210.22 → 212.98] And, you know, what's it like to kind of even maintain something like that?
[213.28 → 217.38] And we're also going to learn about what's it like to, you know, make your maintainers happy.
[217.66 → 220.12] So lots to like, lots to dive into.
[220.48 → 223.98] And so welcome, Chris, and we're joined by Divya as well.
[224.10 → 224.56] Hello, Divya.
[224.84 → 225.14] Hello.
[225.72 → 226.02] Hello.
[226.48 → 226.82] Yeah.
[226.98 → 230.42] So Chris, talk to us about Mocha.
[230.42 → 230.46] Mocha.
[231.46 → 233.74] So how did you get involved with the project?
[234.04 → 237.78] Oh, actually, before that, can you just define what the project is in your own words?
[238.32 → 238.62] Yeah.
[238.84 → 241.58] So, okay, Mocha is, it's a test framework.
[242.18 → 246.10] So there is like a test runner component of it.
[246.10 → 251.42] So you can run Mocha on the command line, and it will run your tests.
[251.98 → 253.34] But mainly, it's a framework.
[253.34 → 260.98] And so what that provides is an API for you to use to organize your tests.
[261.52 → 265.94] And it also provides a reporting structure.
[265.94 → 272.26] So you can, you know, actually get the output of what happened when you run those tests.
[272.26 → 281.22] So that's kind of the main part is this, you know, ways to organize your tests and the reporting output.
[281.50 → 282.10] That's really great.
[282.10 → 284.26] And so, I mean, sounds simple.
[284.60 → 284.78] Yeah.
[285.04 → 290.74] What do you think has been the key to like Mocha's longevity within the ecosystem?
[291.30 → 298.66] If I remember correctly, when Mocha was kind of making its way into the scene, it was the first, it was like Node first.
[299.44 → 308.80] And I think Node was kind of just starting to like, people were just starting to take Node seriously, you know, within companies.
[308.80 → 315.02] And you were starting to see Node.js get adopted here and there for people's, I would say, non-critical production projects.
[315.76 → 317.98] And, you know, so what was it like?
[318.04 → 319.76] And I guess, actually, you weren't part of the project.
[319.76 → 325.04] But I'm curious if you knew, like, what the secret to kind of its creation and its success has been.
[325.04 → 330.36] Well, so, yeah, as we have established, it's kind of old.
[330.70 → 332.28] Node is not much older than Mocha.
[332.48 → 340.52] But, you know, in those early years, there weren't too many choices, right, for test frameworks.
[340.52 → 342.02] It was one of the first.
[342.18 → 346.24] And I think it has that advantage of being kind of first to market, right?
[346.94 → 349.30] So it was one of the first ones.
[349.60 → 353.12] And it, yeah, it focuses on Node.
[353.24 → 354.30] It's written in Node.
[354.58 → 356.22] That's kind of its sweet spot.
[357.10 → 361.36] And it really just, it was really just kind of the first tool out there.
[361.36 → 370.28] And so it also brought with it, and this is part of the history I don't quite have a handle on.
[370.70 → 377.02] So there's another test framework called Jasmine, which is, I think, about as old as Mocha is.
[377.34 → 380.04] But they both have a very similar API.
[380.86 → 387.28] They call it BDD or behavioural driven development style API, where it's supposed to be very declarative.
[387.28 → 393.64] And so it introduced, but also Jasmine was focused on the browser.
[394.28 → 401.60] And so I think maybe what happened is that API from Jasmine inspired Mocha's API.
[402.22 → 405.02] But Mocha was focused on Node instead of the browser.
[405.24 → 409.52] And so it really introduced Node users to this style.
[409.66 → 411.90] And a lot of people really seemed to like it.
[411.90 → 417.44] First, like personally, when I saw that API, I was like, well, it's kind of odd.
[417.54 → 422.92] I'm not used to writing tests, you know, with describe, you know.
[423.06 → 424.30] I'm in another language.
[424.52 → 427.32] Like I came from Python or what have you.
[427.42 → 431.02] And so we would write a suite, and it would be called suite.
[431.20 → 433.38] And we'd have a test, and it'd be called test.
[433.66 → 439.00] And it was also kind of an introduction to this idea of callbacks.
[439.00 → 448.72] So if you're, again, coming from another server side language, maybe like Python, you probably don't have a lot of closures you're passing around.
[448.88 → 454.90] And so in Mocha, you see you have your kind of declarative API, and you're passing a function.
[455.16 → 457.92] And within that function, then you're making more functions.
[458.34 → 464.90] And it was just kind of like, I think, in some ways, a very gentle introduction to this callback style.
[464.90 → 470.28] Also, a lot of people, as I said, really like this declarative type of API.
[470.78 → 477.02] And so, you know, by virtue of being one of the first, I think it really, really took off.
[477.52 → 478.60] Yeah, that makes a lot of sense.
[478.68 → 488.32] I actually do remember that distinctly, where we were using Jasmine, and then Node came along for being compliant with, you know,
[488.32 → 493.30] like, you could write Jasmine style tests for your Node apps, you know?
[493.64 → 500.32] And so there wasn't this, like, so I feel like JavaScript developers got this cool, like, burst of when, like, productivity,
[500.60 → 505.34] because they got to write JavaScript in the server for the first time, right?
[505.40 → 509.02] Because, like, it's this experience where you're always developing in two different languages.
[509.02 → 516.72] And now all of a sudden, you can, like, you have an isomorphic app, or a universal app, or a full-stock JavaScript app,
[516.82 → 520.60] or as many developers would now call it, just an app, right?
[520.78 → 523.50] Like, I don't, you know, we don't even have to give it a fancy name.
[523.84 → 525.68] But I remember that was super cool.
[526.24 → 530.24] And so, like, and it's funny to hear you talk about this, the inspiration behind these APIs,
[530.42 → 534.10] because, like, Jasmine is, like, super influenced by jQuery, right?
[534.10 → 535.66] To, like, bring everything back to jQuery.
[535.66 → 539.72] Like, you know, so it's interesting how, like, you have these echoes of influences.
[540.44 → 540.56] Right.
[540.90 → 543.04] And Mocha, and maybe Jasmine as well.
[543.28 → 549.58] Again, this is where I'm not sure of the connections, but at least I know Mocha was influenced by Spec.
[549.72 → 553.38] If I don't, I'm not a Ruby person, so I don't really know.
[553.78 → 559.02] But I do know that Spec is a test framework for Ruby, and it kind of looks like Mocha.
[559.02 → 565.20] So if you were running tests in Ruby, you could come over to Node and say, oh, hey, look at that.
[565.68 → 571.60] And the original author of Mocha, TJ, he may have been a Ruby developer before he moved over to Node.
[571.66 → 572.10] I'm not sure.
[572.58 → 574.64] But I know there's that connection as well.
[575.26 → 576.14] That's super cool.
[576.48 → 581.28] And so I guess, you know, before we dive into anything, I am super, super curious.
[581.98 → 586.64] Like, how are people testing Node before Mocha?
[586.64 → 588.08] Their Node apps before Mocha?
[588.46 → 590.72] And more so, I don't know, you may or may not know this.
[590.72 → 597.66] And then also, how do you, as a library author of a testing framework, test your framework in that language?
[597.92 → 599.24] Like, it's this meta problem.
[599.90 → 601.28] I'm not sure, really.
[601.48 → 605.00] You know, I came to Node about the time I came to Mocha.
[605.20 → 606.74] So maybe about five years ago.
[606.88 → 610.32] So I'm not sure, like, what people were using to test before then.
[610.32 → 617.66] I imagine a project like tap or Node tap or something was pretty old.
[618.74 → 621.34] I know there was one a long time ago called Node unit.
[622.04 → 624.14] And I think that didn't really take off.
[624.30 → 626.04] So I'm not entirely sure.
[626.80 → 630.24] So I'm dying to know, how do you test your testing framework?
[630.42 → 634.10] Like, it's the super meta problem of, like, you know, circular referencing.
[634.46 → 636.76] Like, you can't use Mocha to test Mocha.
[636.76 → 637.46] Or can you?
[637.64 → 638.14] Or do you?
[638.32 → 639.40] Like, how does that work?
[639.78 → 640.58] Yes, yes.
[640.78 → 643.16] So you can use Mocha to test Mocha.
[643.28 → 643.74] And we do.
[644.18 → 645.10] Is it safe, though?
[645.82 → 646.26] Yeah.
[646.42 → 648.68] I mean, the world's not going to explode or anything.
[648.86 → 652.12] You know, there's not going to be some, like, rift in the space time continuum.
[652.12 → 655.22] Because Mocha is testing itself or anything like that.
[655.76 → 657.88] I think all test frameworks do this.
[657.94 → 661.30] I'm not sure of one that actually didn't use itself to test itself.
[661.98 → 664.56] Of course, Mocha is unit tests, right?
[664.56 → 671.78] And essentially, when your Mocha is running its own tests, it will say, okay, Mocha.
[672.08 → 673.52] And then there'll be a test.
[673.64 → 674.20] And it will go.
[674.48 → 678.06] And this unit test will pull in bits and pieces of Mocha.
[678.46 → 680.14] And it will test the units.
[680.34 → 684.26] So it's just like any other unit test against any other app.
[684.30 → 685.62] It's just like a module.
[685.76 → 686.78] You just pull it in.
[686.88 → 687.46] It's a library.
[687.76 → 690.92] And you instantiate classes and run methods and stuff.
[691.12 → 691.70] That's it.
[691.70 → 699.16] But when it comes to, like, testing, like, more end-to-end type tests.
[699.84 → 705.42] So, I mean, what we do is we have Mocha, a fork, a copy of Mocha.
[705.76 → 710.28] And so then we make assertions about the output.
[711.20 → 713.78] And there are various different ways we do that.
[713.78 → 717.68] Further, testing Mocha in a browser context.
[718.28 → 723.38] So there is a test runner called Karma, which some of you may be familiar with.
[724.20 → 735.18] And Karma is a way to, I suppose, just automate the opening of a browser and execution of unit tests or what have you.
[735.18 → 745.42] And so it's not a thing like Selenium where you would mimic a browser user, and you would, you know, move the mouse around and click on things.
[745.56 → 746.34] It's not for that.
[746.50 → 750.00] It's more of a unit or end-to-end test type thing.
[750.68 → 755.04] And so Mocha uses Karma to test itself in the browser.
[755.04 → 760.12] And the way you do that is you pull in a plug-in and that plug-in is called Karma Mocha.
[760.30 → 762.12] And that adds Mocha support to Karma.
[762.62 → 764.02] And so it's kind of those weird things.
[764.32 → 770.22] So Mocha depends on Karma and Karma Mocha, which depends on Mocha.
[770.34 → 772.92] And so there was a little bit of fiddling we had to do to get that to work.
[773.18 → 779.62] But, yeah, it's like Mocha can use the surrounding ecosystem to help test itself.
[779.62 → 781.88] And that's one of the examples.
[782.02 → 792.56] Another example of this is somebody wrote a GitHub action to add annotations to Mocha test failures when you send a pull request.
[792.68 → 799.20] So if you send a pull request, a test fails, it will, like, send this information to the GitHub Actions API.
[799.60 → 807.22] And it will display the test failure in line under, like, the line of code where it failed, which is really cool.
[807.22 → 815.02] And that's something that somebody built for Mocha just for their own use, not for Mocha's use.
[815.14 → 815.80] And I saw it.
[815.84 → 816.76] I was like, hey, that's cool.
[816.90 → 817.56] I'm going to use that.
[817.74 → 823.58] And so we find stuff that people build on top of Mocha or build for Mocha.
[823.86 → 827.74] And a lot of times we find we can use it for our own purposes.
[827.98 → 828.52] It's really neat.
[829.26 → 830.06] Super cool.
[830.34 → 831.04] That's awesome.
[831.04 → 843.96] I mean, just hearing how I feel like there's, like, this back-channel universe in, like, maintainer land where, you know, folks that have projects within the same ecosystem or, you know, they're constantly kind of collaborating.
[844.48 → 848.32] And, you know, it's just fascinating to hear you talk about, like, the backstory there.
[848.32 → 859.46] It's also fascinating because there's often a sense from user land that you're competing against other frameworks out there that it's like, oh, we're Mocha.
[859.76 → 868.28] And if you use Mocha, you can't use this other testing framework or whatever, which seems to not be the case because a lot of the times they feed into each other.
[868.48 → 873.30] So, like, if Mocha introduces something, another testing library would be like, oh, that's a really great idea.
[873.40 → 874.30] We're going to use that.
[874.30 → 878.42] And it's sort of an ecosystem that feeds itself.
[879.38 → 891.22] And I'm hearing, like, less of that, that, like, competitive streak that users tend to assume is the case where you're like, oh, you're competing testing libraries.
[892.00 → 892.70] But no, you aren't.
[892.70 → 904.86] Because oftentimes just because a user picks one over another, it doesn't mean that one testing library suffers as a result, which is interesting to see.
[905.34 → 905.76] Right.
[905.88 → 907.78] I mean, that's a good question.
[907.78 → 914.94] If there's any competition, like, I feel like it comes from the users who are really enthusiastic.
[915.76 → 915.98] All right.
[916.06 → 925.02] So you see that with frameworks, right, with, like, somebody who's going to be really into view and write some blog posts about how React sucks or something like that.
[925.08 → 925.30] Right.
[925.30 → 929.08] And you'll see that from time to time.
[929.32 → 937.74] And just with, I suppose, any other type of project where there are multiple choices in the same ecosystem, and you could go either way.
[937.74 → 944.14] But, yeah, there's certainly we kind of share the ideas.
[944.14 → 952.06] Like, if you pull in a JavaScript testing framework, like, there's kind of two styles, right?
[952.42 → 957.42] There's this Mocha Jasmine Jest style with this BDD thing.
[957.52 → 960.70] And then there's, like, the Tap style or the Ava style.
[961.20 → 963.84] And there's just, like, these two things.
[963.96 → 965.44] And there's, like, two camps.
[966.00 → 969.34] And there may be some, like, I don't know.
[969.34 → 976.22] There's definitely people who prefer one or the other of those styles of writing tests.
[976.98 → 978.78] And, you know, I mean, that's a thing.
[978.84 → 980.04] But, again, it's just a preference.
[980.30 → 991.62] Like, I maintain that it really, at the end of the day, like, it does not really matter which of these testing frameworks you use as long as your team likes it.
[992.10 → 993.44] Because they all work.
[993.70 → 995.66] Like, they're all going to test your code.
[995.66 → 1003.86] And if you are getting really worked up about one's better than the other, I mean, like, find something better to do, right?
[1004.02 → 1005.40] Find something else to worry about.
[1005.50 → 1009.26] Because, like, any of these are going to be able to test your code.
[1009.38 → 1015.10] And they're all, a lot of the testing frameworks out there in JavaScript, they're all mature now, like the popular ones, right?
[1015.24 → 1016.44] They've been around the block.
[1016.72 → 1020.26] So it's really hard to go wrong with any of them, I think.
[1020.42 → 1021.24] So, yeah.
[1021.24 → 1036.40] Do you ever hear, as frameworks have taken on more popularity and so on, there's, like, there's testing libraries like Jest, for example, that are very specific for, like, snapshot testing and so on.
[1036.50 → 1049.04] Do you hear, like, or have you ever seen conversations around how Mocha doesn't necessarily address certain things that other libraries have and that it should, but it doesn't?
[1049.04 → 1050.86] I mean, yeah.
[1051.00 → 1051.86] So, sure.
[1052.60 → 1055.96] Like, Mocha doesn't come with an assertion library, right?
[1056.10 → 1058.22] Pretty much every other framework does.
[1058.60 → 1061.92] So every other framework is going to have some way to make an assertion.
[1062.54 → 1063.18] Mocha doesn't.
[1063.86 → 1068.38] And, you know, I'm sure from day one people were like, well, why don't you add an assertion library?
[1068.90 → 1071.16] I said, well, that's kind of the design choice.
[1071.24 → 1074.68] We want to let a user choose, essentially.
[1075.68 → 1078.14] And it keeps the project smaller, right?
[1078.14 → 1082.92] So there's stuff like Mocha doesn't do X out of the box.
[1083.12 → 1084.02] And it doesn't.
[1084.18 → 1090.84] And, well, it's because, you know, a lot of people don't necessarily need X out of the box.
[1091.44 → 1095.56] And if they want to do X, it's not so hard to get it working.
[1096.02 → 1099.70] You can get Mocha working with pretty much anything that I've seen, right?
[1099.78 → 1101.72] Somebody's got a way to do it.
[1102.40 → 1105.28] And it's more of a design philosophy.
[1105.28 → 1107.58] It's not a batteries included project.
[1107.58 → 1109.12] It doesn't really need to be.
[1109.24 → 1110.96] There are plenty of people who are happy with that.
[1111.52 → 1112.58] I'm happy with that.
[1112.68 → 1116.24] If you want to do snapshot testing, well, you can use Mocha to do snapshot testing.
[1116.60 → 1118.04] It just doesn't do it out of the box.
[1118.54 → 1118.58] Right.
[1118.58 → 1128.36] So there are a lot of things that Mocha and the maintainers have said no to just because it's, well, somebody's written this already.
[1128.54 → 1130.16] And it exists out there.
[1130.22 → 1133.72] And it doesn't need to be part of the core library.
[1134.14 → 1139.96] And, yeah, I mean, again, if you're, like, talking about, well, Mocha doesn't do X.
[1139.96 → 1143.48] Yeah, but it can.
[1144.14 → 1146.66] And so you just, you pull in another library to do it.
[1146.74 → 1147.98] That's all there is.
[1148.16 → 1152.50] So I don't, in my mind, it's not like a huge deal because there is such a huge ecosystem around Mocha.
[1152.50 → 1158.96] It's actually fascinating because I have personally only ever used Mocha with an assertion library.
[1159.18 → 1161.04] I've never just used Mocha as is.
[1161.42 → 1170.72] So I'm genuinely curious if that is a common scenario where people use Mocha without an assertion library, or they always reach for one.
[1171.08 → 1172.66] I see most people using them, yeah.
[1173.08 → 1176.48] So most people, like the most popular assertion library out there is Chai.
[1176.78 → 1177.04] Yeah.
[1177.16 → 1178.56] And most people seem to want to use that.
[1178.56 → 1183.46] You don't have to because Node comes with the assert built in.
[1184.52 → 1187.30] And so you can just use that if you don't want to bother with it.
[1187.42 → 1188.10] And it's fine.
[1188.86 → 1189.60] But, you know.
[1189.84 → 1190.06] Yeah.
[1190.10 → 1197.50] So you don't have to necessarily, like, bring in an assertion library because you could just use Node's native assert for that.
[1197.70 → 1203.48] But I think Chai does introduce some niceties in regard to an API that some people like.
[1204.02 → 1204.42] Yeah.
[1204.70 → 1204.98] Yeah.
[1205.20 → 1206.22] I love Chai so much.
[1206.22 → 1209.46] Like, I have to say, though, like, I feel like the Mocha is.
[1210.14 → 1219.88] I'm so happy to hear that the maintainers practice this, like, store this resistance model because, you know, it's so easy to, like, want to make your tool do everything.
[1220.08 → 1229.50] Have it be like the kitchen sink, you know, or like a Swiss Army knife where it's like it does 10 things badly, you know, like nothing well, you know.
[1229.50 → 1244.56] But I would say the architecture of the plugin architecture for me is what I think has made Mocha, like, still relevant because I think people can continue extending it and extending it because it's got such a like, strong core framework, you know.
[1244.56 → 1250.94] What do you think has kind of, like, led to the success of it managing to still be relevant today, right?
[1250.98 → 1260.40] Because it's amazing how, like, it's, like, still extremely popular as are the like, the packages that came up with it, like Chai and all these other things.
[1260.40 → 1264.02] Like, do you think it's the API being simple or, like, is it something else?
[1264.74 → 1267.92] Or is it just, like, that it was the first to market and we got early adoption?
[1268.34 → 1270.68] It's a combination of those things, I think.
[1270.74 → 1272.80] I think it's pretty simple.
[1272.94 → 1277.34] If you're writing code in Node and your project's pretty small, it's pretty fast.
[1277.76 → 1284.40] Once your project gets very large, we've recently introduced some ways to handle larger test suites.
[1285.36 → 1288.98] But, yeah, it's, I think, pretty stable.
[1288.98 → 1290.46] I like to think so.
[1290.82 → 1292.44] We try not to break stuff.
[1292.66 → 1294.92] We try not to add too many things.
[1295.42 → 1299.44] We try to adhere to Silver as closely as possible.
[1300.14 → 1304.02] And we keep up to date with new Node versions.
[1304.64 → 1308.54] So, I mean, part of it is just being actively maintained.
[1309.00 → 1314.94] If people weren't looking at it, you know, it would die by the wayside, right?
[1314.94 → 1318.20] Because it wouldn't, you know, it wouldn't get security patches.
[1318.20 → 1319.64] Like, all sorts of things.
[1319.98 → 1324.06] So, you know, just being maintained is a good thing there.
[1324.32 → 1330.48] You know, you may see other test frameworks, and I'm not going to name any names because I'm not really sure.
[1330.94 → 1333.56] But, you know, maybe they haven't had a commit in six months.
[1333.98 → 1338.34] But, you know, Mocha, there's been times when the foot's been off the gas pedal a bit.
[1338.34 → 1340.06] But we're still working on it.
[1340.06 → 1342.38] And I'm still trying to make it better.
[1343.26 → 1348.22] Another one of those things is we try to, it's kind of complex.
[1348.54 → 1352.00] But we do still support, like, IE11, right?
[1352.00 → 1358.06] When I started with Mocha, it was actually, it was not even written in ES5.
[1358.46 → 1359.70] It was ES3 compatible.
[1359.92 → 1363.76] So, that means it would run in, like, IE6 or something, right?
[1364.30 → 1372.82] And so, it really kind of kept support for those older browsers for quite a while.
[1372.82 → 1378.90] And we've been able to kind of maintain that support without too much of a hassle.
[1379.92 → 1384.98] But, you know, the supporting older node versions can be a little more difficult.
[1385.58 → 1395.98] And we try to now, once a node version goes unmaintained, you know, within some time period thereafter, we drop official support.
[1396.08 → 1400.50] It doesn't mean it's not going to work, but we just take it out of our CI build.
[1401.06 → 1401.92] That's so cool.
[1401.92 → 1408.88] I mean, it's such a good segue into what I wanted to ask you about next, which is, like, how many versions of node do you support right now?
[1409.32 → 1422.08] And especially if you're, like, supporting IE11, what's that even like to support, like, the latest version of node and then going back X number of, like, do you just have to practice restraint when you're writing the code?
[1422.20 → 1425.54] Essentially, you can't, like, there's just, like, no new JavaScript.
[1425.90 → 1428.54] Like, no new, basically.
[1428.54 → 1432.16] So up until a few months ago, it was...
[1432.16 → 1435.50] No babble, no build tools, no, like...
[1435.50 → 1435.72] Right.
[1435.80 → 1437.76] Up until a few months ago, it was...
[1437.76 → 1439.40] We did that with the help of ESLint.
[1439.58 → 1444.48] And so we have code that is not going to be run in the browser.
[1444.62 → 1446.98] And that's, like, the command line interface.
[1446.98 → 1453.54] And so in that code, we could use things like coast and let.
[1453.54 → 1458.88] But in the code that got shipped to the browser, we could not.
[1459.28 → 1468.92] And so we would have, like, we have this honking ESLint config that says, you can use, like, ES2015 in these files, but not these files.
[1469.58 → 1472.82] And so that was kind of the status quo for a long time.
[1473.38 → 1477.30] Several months ago, we actually ended up pulling in a build tool.
[1477.30 → 1488.52] So now we can actually use modern JavaScript anywhere, and it all just gets, you know, transpired and rolled up like anything else.
[1489.04 → 1491.76] But, yeah, that's kind of where it was at.
[1491.84 → 1494.20] It was like, okay, you have to use var.
[1494.36 → 1498.58] You can't use the class keyword in all of this code that would get shipped to the browser.
[1498.58 → 1508.58] And it was inconvenient, but not, like, so frustrating that it was really holding the project back, I think.
[1508.94 → 1515.34] What would hold the project back more is having to support older versions of Node, actually.
[1516.18 → 1519.30] Because, like, there are certain incompatibilities.
[1519.68 → 1521.62] There's missing language features.
[1521.62 → 1528.02] And because there was not a build step for so long, we didn't want to add just, like, a build step for Node.
[1528.44 → 1530.36] And we still don't have a build step for Node.
[1530.62 → 1543.38] But it's a little more difficult because if we do want to use ES2015 or even newer stuff like async await, you know, if we're going to support all the way back to Node 4 or something, I don't know.
[1543.84 → 1545.12] We're not going to be able to do that.
[1545.52 → 1548.82] And so, yeah, we did support very old Node versions.
[1549.00 → 1549.94] That's not the case anymore.
[1549.94 → 1557.72] I think I'm happy with that, like, as a maintainer because it's just, like, another thing I don't need to worry about.
[1557.96 → 1563.98] You know, there are versions of Mocha that work with Node 0.10 or 0.8 or 0.12.
[1564.36 → 1566.76] And you can go out there and download them and run them and they work.
[1567.20 → 1568.62] And great, there you go.
[1569.02 → 1570.44] So you're set, right?
[1570.44 → 1582.10] So it's like, I don't necessarily think that we have to keep support for versions all the way back to Node 0.4 because, you know, there are Mocha versions that support this.
[1582.30 → 1591.36] And if you, for some reason, are starting new development and expect it to run in Node 0.4, then, I mean, you've got bigger problems.
[1591.36 → 1595.70] So you can just go use the Mocha that runs in that version if you want.
[1595.94 → 1601.30] But I don't see it, like, being necessary for us to keep supporting.
[1601.58 → 1609.76] However, in the case of IE11, like, people are, like, writing new code that needs to run in IE11 for whatever corporate reason.
[1609.98 → 1612.16] And that's just kind of the way of things right now.
[1612.16 → 1614.78] So we still support IE11.
[1615.28 → 1615.80] Oh, wow.
[1615.98 → 1617.50] Well, you heard it here, folks.
[1618.36 → 1620.14] Maintainers having user empathy.
[1620.86 → 1631.92] Like, it's so, like, nice to hear that you all are going the extra mile to support people who also need to support, like, IE11 use cases, you know?
[1632.08 → 1635.88] And so it's just really great to see that type of forward-thinking.
[1636.28 → 1638.22] Because it's really not everywhere in the ecosystem.
[1638.50 → 1640.82] I don't want to name names, but there are, like, projects.
[1640.82 → 1648.86] Well, I would say there's one popular maintainer that, like, uses arrow functions and just really doesn't give two craps about anything.
[1649.26 → 1650.58] And they have widely adopted packages.
[1650.80 → 1651.92] And I'm like, WTF?
[1652.16 → 1652.72] Like, you know?
[1653.00 → 1656.66] So, like, care about people and, you know, whatever else.
[1656.74 → 1658.38] So I'm really happy to hear that.
[1658.88 → 1660.84] Jordan Harland is also the same.
[1661.22 → 1662.40] He's very on the same.
[1662.64 → 1664.14] Like, he writes, like, ECMAScript 3.
[1664.42 → 1666.26] And he's, like, the editor of, like, ECMAScript.
[1666.42 → 1670.02] And he doesn't even get to write modern JavaScript for his packages, you know?
[1670.02 → 1670.46] Yeah.
[1670.72 → 1672.96] He's much more extreme than I am, though.
[1673.50 → 1673.94] Yeah.
[1674.80 → 1685.68] I think that's probably, like, one, like, huge reason to go back to your comment earlier, Amal, about the longevity of a project.
[1686.38 → 1688.44] Because it's really easy.
[1688.44 → 1695.84] And I think this is a common scenario now where you look at a project and if something is old, you're like, oh, it's been around, like, forever.
[1696.02 → 1696.94] We want something new.
[1697.12 → 1698.66] And we want something that's up-to-date.
[1698.66 → 1725.16] But I think if you look at just projects over time, the ones that have cared a lot about backwards compatibility and making sure that things work, and that users remain satisfied and that this particular project can see its way through the course of, like, a project lifecycle, however long that is, that speaks to whether or not that project will be around in, like, five years or ten years.
[1725.16 → 1735.36] Which I think is, like, very taken for granted in a way where people just assume, oh, we're using the latest tool, so people will use us and will continue to use us.
[1735.44 → 1744.20] But I think this is just a general sense with being a human, which is that you forget that your future, your current is going to be a past at some point.
[1744.20 → 1746.48] And so you don't really think about that.
[1746.60 → 1748.72] And you're always like, oh, it's obviously current.
[1748.88 → 1755.22] But, like, moving forward, the syntax might change and the thing that you built is no longer, like, edgy.
[1755.52 → 1760.72] And will you continue to, like, keep that standard, like, keep it backwards compatible?
[1761.02 → 1762.84] And the answer is oftentimes no.
[1763.46 → 1763.74] Right.
[1764.36 → 1764.60] Yeah.
[1764.66 → 1770.08] Backwards compatibility is important to Mocha in a very specific way.
[1770.08 → 1779.32] So what we try to do is not cause a major – I mean, this is, like, we have major releases, right?
[1779.34 → 1781.00] There are things that have to break.
[1781.66 → 1793.34] But unless there's, like, some terrible bug where it's, like, false positive or a false negative type situation, we don't want tests that used to pass.
[1793.34 → 1795.88] We don't want them to start failing.
[1796.34 → 1801.84] Or tests that were failing, we don't want them to suddenly start passing with a major release.
[1802.50 → 1806.64] And so just, like, changes that cause those to happen.
[1806.78 → 1809.12] I mean, personally, I'm just – I'm totally anti.
[1809.26 → 1811.48] I don't want to ship anything like that.
[1811.86 → 1813.54] I want to maintain backwards compatibility.
[1813.54 → 1826.48] I want tests that, you know, assuming you've upgraded your Node version, I want tests that you wrote in, you know, a Mocha, like, a major – seven majors ago or whatever.
[1826.78 → 1828.72] Mocha is version eight now.
[1829.06 → 1834.32] We want those tests to still work if there wasn't, you know, something wrong with them.
[1834.32 → 1845.52] But that's what we focus on is just kind of making sure that a change that we make won't cause a bunch of people – and there are a bunch of people that use Mocha.
[1845.66 → 1858.60] We don't want to cause a bunch of work for other people to go back and have to fix a bunch of tests because we decided, well, the API isn't pure enough here, and it's just not right, and we just need to change it.
[1858.82 → 1859.84] Like, that's not okay.
[1860.40 → 1864.08] So, yeah, that's how we look at it.
[1864.32 → 1877.42] Hey there, party animals.
[1877.56 → 1878.12] Jared here.
[1878.64 → 1881.08] I want to take a moment to tell you about Changelog++.
[1881.78 → 1888.14] It's our membership program where you can directly support JS Party and all the podcasts we create here at Changelog.
[1888.88 → 1894.00] Ditch the ads, get closer to the metal, and enjoy supporting JS Party into the future.
[1894.32 → 1897.56] Once again, that's changelog.com slash plus.
[1897.88 → 1899.14] We'd love to have you with us.
[1899.14 → 1900.14] All right.
[1900.14 → 1901.14] All right.
[1901.14 → 1916.04] So, Chris and Divya.
[1916.04 → 1917.04] Wow.
[1917.04 → 1918.04] Mind blown.
[1918.04 → 1920.36] We're talking about empathy.
[1920.88 → 1923.12] We're talking about writing code.
[1923.60 → 1924.80] Two of my favourite subjects.
[1925.26 → 1928.00] And we're talking about, like, doing good by our users.
[1928.74 → 1936.56] And that's a perfect segue into our second segment, which is how to be good to your maintainers.
[1936.78 → 1937.08] Right?
[1937.08 → 1942.32] And so, Chris has been a maintainer of this project for almost five years or five years.
[1942.70 → 1949.38] And he's been around long enough to know, I would say, what makes for good open source stewardship.
[1949.94 → 1955.02] And when I say stewardship, I mean that, like, as a user of an open source project, you know, we're all kind of stewards of it.
[1955.02 → 1960.88] Whether it's just we're reporting bugs or hopefully supporting the project in some way.
[1961.62 → 1967.64] And so, with that said, Chris, tell us about, like, what makes you happy as a maintainer?
[1968.00 → 1971.64] Like, how does stewards of your project make you happy as a maintainer, to be specific?
[1972.18 → 1973.62] I think it is.
[1973.80 → 1974.24] Well, yeah.
[1974.28 → 1974.98] It's a couple of things.
[1974.98 → 1983.32] Because, one, you know, maintainers, they like those that have any interest in fixing other people's problems.
[1983.98 → 1986.50] Maintainers like good bug reports.
[1986.50 → 1990.42] So, a clear reproduction plan.
[1991.06 → 1996.74] What not to do is, hey, I'm encountering this error with your project.
[1997.38 → 2001.46] And when I do X, it does Y.
[2001.46 → 2001.88] Right.
[2002.58 → 2006.80] But the X is pretty vague.
[2007.08 → 2008.28] You don't share any code.
[2008.46 → 2012.08] You don't share, like, Stack Overflow calls it.
[2012.66 → 2016.96] And minimal, it's like MOVE or something like that.
[2017.46 → 2021.26] Minimal complete, I don't remember what it's called for.
[2021.40 → 2024.82] But it's just like the simplest way you can reproduce this problem.
[2024.92 → 2025.82] That would be great.
[2025.82 → 2035.68] So, what I would want to do, if you have some bug, I would want to see, okay, if it's in code and it has a particular setup.
[2035.80 → 2037.68] If it's not, like, trivially reproducible.
[2037.82 → 2042.54] If I can't just take this code and copy and paste it and, like, run Mocha and make it happen.
[2042.70 → 2044.58] Like, if there's more to it than that.
[2044.70 → 2049.94] So, maybe you have an integration with, like, some sort of other project or framework.
[2049.94 → 2053.74] And I think this goes for not just Mocha, but lots of open source projects.
[2053.88 → 2057.48] So, if you're using Project X with, like, Babel or something, right?
[2057.98 → 2060.88] Like, you need to give us a repo.
[2061.16 → 2066.30] And that repo should have all the stuff in it that you need to reproduce the problem.
[2066.38 → 2068.44] It should have, you know, a package JSON.
[2068.72 → 2070.68] It should have, like, Babel in the dependencies.
[2070.96 → 2072.36] I should type NPM install.
[2072.56 → 2074.64] And I should run NPM test and show me the problem.
[2075.18 → 2078.94] Now, I wish there was a like, maybe it wants some tooling or something.
[2078.94 → 2081.16] I wish there was an easier way to do this.
[2081.52 → 2086.70] And maybe there are, I'm sure there are, like, even cloud services that you could just set up in this way.
[2086.78 → 2092.04] Maybe you don't even have to, like, go and get a repo and publish it on GitHub and send me to it.
[2092.38 → 2095.68] Maybe you can just go to, like, I don't know, something like CodePen or I don't know.
[2095.80 → 2100.70] Some site up there that allows you to do this sort of thing and just throw that in the browser.
[2100.88 → 2101.86] I can go and take a look.
[2101.98 → 2103.08] I can reproduce it.
[2103.40 → 2104.28] That would be awesome.
[2104.76 → 2105.60] That's what I like to see.
[2105.60 → 2112.62] Furthermore, I might not have the time or just maybe it's like an edge case or something.
[2112.82 → 2114.92] And it's like, okay, yeah, that's a problem.
[2115.40 → 2116.14] I agree.
[2116.36 → 2117.40] It should be fixed.
[2117.74 → 2119.20] I don't really have time to do it.
[2119.52 → 2120.80] Can you fix it, please?
[2120.90 → 2125.12] And I love it when somebody says, okay, yeah, I'll send a pull request.
[2125.24 → 2126.84] And they send a pull request, and they fix it.
[2126.94 → 2130.34] And the pull request, you know, they read the contributing guidelines.
[2130.34 → 2134.66] And it says you must add a test if you add any code or change any code.
[2134.76 → 2135.66] It better have a test.
[2135.94 → 2138.90] And if they do all that stuff, like, I love it.
[2138.92 → 2140.80] Just, it's just like to follow the rules.
[2140.94 → 2141.50] Help out.
[2141.64 → 2144.44] Like, you know, it's your project too, right?
[2144.96 → 2146.34] So you found a bug.
[2146.48 → 2147.84] You're telling me about the bug.
[2148.36 → 2149.82] Like, I want you to fix it.
[2149.84 → 2150.92] I want you to get involved.
[2151.28 → 2152.56] I'm not going to be able to do it.
[2152.74 → 2154.50] You're not paying me for support, right?
[2154.50 → 2158.36] So it's like, I love it when people help out like that.
[2158.48 → 2161.84] And they help me say, yes, that is a problem.
[2161.98 → 2164.60] And yes, I would accept a pull request to fix it.
[2164.88 → 2166.22] And that's awesome.
[2167.04 → 2169.68] So that's one way, like, you can help.
[2169.98 → 2176.88] Issue tracker, and you are very vague, or I can't just, like, glance at the thing and think about,
[2177.26 → 2178.88] I don't know, a rubber duck, right?
[2179.58 → 2181.46] The rubber duck is reading your bug report.
[2181.46 → 2184.32] Is that rubber duck going to be able to reproduce your bug?
[2184.66 → 2189.46] If you just can't, like, reach in there, only using the information in there and figure,
[2190.08 → 2194.06] and, like, reproduce the issue, it's not very helpful to the maintainer.
[2194.18 → 2196.94] And so with issues like that, they'll just sit there.
[2197.28 → 2200.46] And I'll say, you know, I don't know.
[2200.60 → 2201.76] I need more information.
[2201.76 → 2203.62] And then I don't get any more information.
[2203.92 → 2207.72] And then there's, like, a bot that comes along and says, this issue is stale.
[2207.72 → 2209.10] And it closes the issue eventually.
[2209.10 → 2212.16] And we have to use, you know, bots like that.
[2212.32 → 2213.68] It helps keep us sane.
[2213.78 → 2215.10] There's some people that don't.
[2215.22 → 2219.92] Some people are happy with a repo with 5,000 GitHub issues in it.
[2220.24 → 2224.26] There's some people who hate the things that automatically close issues.
[2224.68 → 2227.06] Well, like, the issue doesn't get deleted.
[2227.62 → 2228.44] It's still there.
[2228.88 → 2234.92] If it's still a problem, then somebody come along and fix it or comment or send a pull request or something.
[2234.92 → 2238.48] Just because the issue is closed doesn't mean it's, like, fixed, right?
[2239.16 → 2240.58] So I don't know.
[2240.88 → 2242.20] There are a lot of things you can do.
[2242.34 → 2245.78] I think a lot of them, unfortunately, are, like, kind of, like, unwritten.
[2246.12 → 2252.12] Certainly each project has its own rules or own contributing guidelines.
[2252.12 → 2256.98] But people don't, like, read these, right, most of the time.
[2257.60 → 2258.90] And I don't know.
[2259.00 → 2266.46] I guess I wish there was just better education around just kind of general etiquette.
[2266.72 → 2270.78] Like, general, like, how to be a good open source participant.
[2270.78 → 2284.78] I would be happy with even, like, requiring, like, people take some sort of, like, class or something before they can start bothering people on GitHub, right?
[2285.00 → 2285.56] I don't know.
[2285.62 → 2287.56] Maybe that's just something I just thought of.
[2287.56 → 2303.12] But, like, if you can go, and you can get some education and understand, well, this is how maintainers kind of expect you to behave and this is how you can be helpful, I would love to see something like that.
[2303.12 → 2309.88] And make sure that there's a baseline that people participating on GitHub can understand it.
[2311.04 → 2313.08] I don't think that's ever going to happen.
[2313.40 → 2315.66] But it sure would be nice.
[2315.66 → 2324.80] It's hilarious you say that because I was having this conversation, ironically, with Jordan Harland and as well as Maggie Pint a few months ago.
[2325.36 → 2329.94] But, you know, it's a project that I don't have time for, but I would love to work on this one day.
[2330.26 → 2338.62] But essentially, I really think there should be, like, a badging program, you know, where people get a community badge for, like, not being a douchebag.
[2338.82 → 2341.94] And, like, kind of, it's like a COC, like, wide thing.
[2341.94 → 2345.60] It's like an unofficial COC, essentially, but, like, using GitHub org for it.
[2346.16 → 2358.48] And, you know, having folks be able to, you know, like, read and then, like, sign, like, read a manifesto or, like, guidelines of, like, how to be a good contributor and user of a project.
[2358.48 → 2360.88] And then they get a badge, they get added to an org.
[2361.10 → 2369.38] And then, like, maybe people with a badge get prioritized by maintainers because, you know, they know that, like, this is somebody who signed a code of conduct, and they're, like, being a nice person.
[2369.70 → 2376.24] And in the event that, like, this, like, in the event that someone is a problematic person, then, like, they would get their badge revoked or whatever.
[2376.46 → 2379.90] And there's incentive for people not to be a-holes, basically, right?
[2379.90 → 2383.28] You know, it would be nice to have something like that, but I totally agree.
[2383.64 → 2388.74] Like, the entitlement that I see with people, it's just out of this world.
[2389.04 → 2391.72] Like, people just feel so, so entitled.
[2392.06 → 2394.02] Like, oh, this is a bug.
[2394.12 → 2394.50] Fix this.
[2394.56 → 2395.28] This is my problem.
[2395.38 → 2399.14] I need you to, like, you know, drop everything and do it now, you know?
[2399.24 → 2402.48] And then there's also a lot of mis education around, like, what is GitHub even?
[2402.48 → 2410.92] Like, people see issues, and then they see, they think all of them are, like, here's, like, 5,000 things that are wrong with this project, you know?
[2411.12 → 2412.36] Like, I've seen that before.
[2412.66 → 2416.86] And it's like, no, no, no, no, that's just, like, the backlog, you know?
[2417.48 → 2420.80] And, like, lots of issues is a good thing, kind of, you know?
[2421.24 → 2431.24] I think, like, to the previous point around, like, how to write good issues, that's been, like, a perpetual problem where oftentimes someone is, like,
[2431.24 → 2433.08] it doesn't work in this particular thing.
[2433.16 → 2435.12] And then you're, like, can you give me more examples?
[2435.44 → 2436.70] What machine are you on?
[2437.12 → 2438.46] What system are you running?
[2439.10 → 2441.66] And people don't automatically give you that information.
[2441.96 → 2444.72] And so the issue templates are really useful.
[2444.72 → 2453.26] And I know lots of projects use it as a way of when you open a new issue, it sometimes gives you a prompt, whether it's, like, a feature request or a bug report.
[2453.48 → 2457.94] And then it gives you, like, sort of markdown template of how to write things.
[2457.94 → 2466.84] But I often find that that can also be a hurdle because often when people see a template, they're, like, oh, writing, I have to write this in Markdown and that's really annoying.
[2467.26 → 2468.98] And I talk about Vue a lot.
[2469.12 → 2478.96] But I found that Vue's issue template is actually really neat because when you open a new issue, you're taken to a page that's not on GitHub.
[2478.96 → 2486.70] It's sort of a web page that has a form so it looks a little clearer as to what you're filling in.
[2486.80 → 2495.42] Because when you fill in Markdown, usually you're just typing in straight the details and you sort of have to parse it yourself, at least in the GitHub view.
[2495.60 → 2498.54] So this is kind of, like, it pulls you into a different form.
[2498.78 → 2501.40] So you see all the form fields you need to fill on.
[2501.52 → 2502.56] You're a bit more intentional.
[2502.56 → 2511.46] And I think the part I like the most about this specific one is that at the top, it tells you, like, hey, did you read the docs?
[2511.54 → 2512.58] Did you watch tutorials?
[2512.76 → 2514.34] Did you ask this question on the forums?
[2514.48 → 2516.18] Did you, like, do all these things?
[2516.64 → 2524.60] And, like, if your question was not answered or if you believe it has to do with, you know, an implementation detail, then open the issue.
[2524.60 → 2541.52] So, like, sure, people can still open the issue regardless, but I like that call out because oftentimes, like, for example, that happens a lot in open source projects where someone will, like, say, oh, there's an issue with your API, but, like, they had a typo, or they didn't use it properly.
[2541.76 → 2551.02] And it's really frustrating for a maintainer to go in and then realize that because you're like, I could have been doing this other thing, but I don't want to.
[2551.64 → 2553.42] It's like a different kind of work, you know?
[2553.42 → 2557.78] And so it's shifting the onus back on the user.
[2558.04 → 2559.68] And Amal mentioned this a little as well.
[2560.14 → 2570.96] The fact that people who use open source projects often assume that the work is, like, because it's free, so I can expect a lot from the person who's building it.
[2571.46 → 2574.40] But I think people always forget there's no such thing as a free lunch.
[2574.66 → 2578.94] So, like, someone's going to do the work and someone has to bear the brunt.
[2579.04 → 2580.30] And it's really frustrating.
[2580.30 → 2596.22] I'm actually curious, has GitHub sponsors, like, the introduction of that had any effect on, like, Mocha development and how exactly you plan, like, funding and, like, splitting of responsibilities and so on?
[2596.22 → 2599.10] You know, are we using GitHub sponsors?
[2599.54 → 2600.16] I think we have a button there.
[2600.16 → 2600.84] I actually don't know.
[2601.00 → 2601.98] Yeah, I think you have a button.
[2602.24 → 2603.62] But I don't know if you're using it.
[2604.06 → 2606.66] Yeah, I don't think we're actually using GitHub sponsors.
[2606.90 → 2609.20] I think it just goes to our Open Collective page.
[2609.36 → 2611.94] So Mocha was one of the first collectives on Open Collective.
[2611.94 → 2615.50] And so we get donations through that platform.
[2616.10 → 2634.04] And, you know, right now we are in the process of finding a like, a UX, UI designer type person to work on our website and help us with our documentation and organization thereof and all sorts of cool stuff.
[2634.04 → 2637.94] And so we're going to use some of the donations to fund that work.
[2638.38 → 2640.44] It's just, like, work that would not happen.
[2640.64 → 2644.06] Like, work that nobody's going to come along and just do for us, right?
[2644.22 → 2644.42] Right.
[2644.74 → 2646.86] So, yeah.
[2647.02 → 2650.66] So, yeah, GitHub sponsors, no, we haven't really used it.
[2650.74 → 2654.18] We just, I think we added the link to Open Collective there.
[2654.96 → 2657.44] But, you know, donations are cool.
[2657.92 → 2659.52] And they help us do stuff like that.
[2659.74 → 2667.12] But they're, you know, none of us are trying to make a living, you know, off of, no, like, like, Evan You, right?
[2667.24 → 2671.16] We're not trying to live off of the work we do on this project.
[2671.88 → 2675.50] Evan You is, like, the most baller person I know of.
[2675.66 → 2676.60] I don't know him personally.
[2676.78 → 2680.16] I just, like, quite literally, like, super baller, you know?
[2680.26 → 2683.42] Like, he's just like, yep, I'm going to make a developer salary.
[2683.42 → 2688.66] Like, and it's going to be doing what I love, you know, on my terms.
[2689.24 → 2690.48] Thank you very much.
[2690.66 → 2692.18] Sign here, please, you know?
[2692.48 → 2693.66] That's not a common scenario.
[2693.86 → 2699.14] Like, it's actually really, it's so hard to have a steady income through open source.
[2699.26 → 2705.42] Like, I actually don't think that there are many people out there who are able to have that.
[2706.02 → 2707.04] It's very rare.
[2707.50 → 2707.64] Yeah.
[2708.12 → 2710.36] It is kind of like the Holy Grail, though.
[2710.82 → 2711.18] Yes.
[2711.38 → 2711.60] Yeah.
[2711.60 → 2713.54] It's like what we wanted for years.
[2713.72 → 2719.00] It's like just to get enough funding that I could go and quit and just do this and, you
[2719.00 → 2722.20] know, be, essentially be my own boss, right?
[2722.38 → 2725.98] And, but things don't really work out that way, right?
[2726.10 → 2726.98] Most of the time.
[2727.26 → 2733.38] The closest is probably just, the closest is just if you work at a company, and you're paid
[2733.38 → 2734.82] to do open source work.
[2734.82 → 2741.36] And that's kind of not, I mean, I don't consider it the same thing because you're not managing
[2741.36 → 2742.88] the finances in that case.
[2742.94 → 2743.92] The company is.
[2744.88 → 2750.58] But I think that's been the closest, most accessible to people to work at a company that
[2750.58 → 2753.72] works on an open source project so you can be paid to work on open source.
[2754.12 → 2754.42] Yeah.
[2754.42 → 2756.86] I think it's the most realistic.
[2757.38 → 2758.06] Yes, definitely.
[2758.06 → 2761.70] Whether we should settle for that is another question.
[2762.78 → 2763.58] That's a good point.
[2763.68 → 2763.84] Yeah.
[2764.46 → 2764.76] Yeah.
[2765.16 → 2766.30] That's a very good point.
[2766.74 → 2771.56] We've talked about like what's helpful, I think, especially when reporting issues.
[2771.56 → 2773.86] And we've talked about like what not to do a little bit.
[2773.86 → 2779.74] How about like if folks are interested in like becoming a maintainer or like helping out
[2779.74 → 2783.84] occasionally, like a side gig, you know, like a side gig maintainer.
[2784.16 → 2788.88] Like, hey, I'm not full-time on this project, but sometimes I respond to issues that are like,
[2789.08 → 2789.76] you know, duplicate.
[2790.08 → 2794.98] You know how folks, like a lot of newbies especially, like they don't check the issues.
[2795.18 → 2798.38] Like they don't check to see if there's a pre-existing condition.
[2798.76 → 2802.12] If there's a pre-existing issue, you know, they like to file a new one.
[2802.12 → 2805.12] And so maintainers have to often like close and dupe and link.
[2805.32 → 2809.06] And, you know, and so if I wanted to like just be helpful and answer a bunch of open
[2809.06 → 2811.58] questions, like, I don't know, like, is there a path for me?
[2811.68 → 2812.74] Is that, was that annoying?
[2812.86 → 2813.50] Is that helpful?
[2813.70 → 2818.16] Like, I'm just curious, like how much help is like welcome and how, and at what point
[2818.16 → 2822.32] is it just like annoying and obnoxious, you know, because it is time to like onboard
[2822.32 → 2824.48] people, the unfortunate downside.
[2824.82 → 2830.14] But yeah, I mean, I can speak to how I see that.
[2830.14 → 2833.20] It's not going to be the same for other projects.
[2833.38 → 2836.84] But first, like, thank you for wanting to help.
[2837.14 → 2838.92] You're probably not going to enjoy this.
[2839.88 → 2845.46] It's just like managing, like triaging issues is not that much fun, especially if you'd
[2845.46 → 2846.14] rather be coding.
[2846.14 → 2849.42] So like, yeah, there's that.
[2849.82 → 2855.08] And so like, I've had some people who come along and say they're interested in it, but
[2855.08 → 2856.64] it never, they never really sticks.
[2857.02 → 2864.90] I think in order for that to happen, like it's really hard to triage the issues unless
[2864.90 → 2868.96] you have a deep understanding of the code base, unfortunately.
[2868.96 → 2874.80] So, you know, we have ways to automatically label issues.
[2875.46 → 2879.30] And some of that is the GitHub issue templates, right?
[2879.94 → 2883.70] But you need to understand the project to understand really how serious something is.
[2884.12 → 2887.08] So that's kind of a hurdle, right?
[2887.10 → 2890.20] And you have to get there first, and then you can look at the issues.
[2890.20 → 2896.74] So there are a handful of maintainers of Mocha and, you know, we all kind of look at the
[2896.74 → 2901.00] issues, but nobody's just sitting there all day looking at the issues.
[2901.62 → 2907.44] Nobody's that's, you know, I don't think people just want to do that.
[2907.82 → 2912.46] I don't think that's fun for a lot of people, maybe for some people, but a lot of people who
[2912.46 → 2913.42] would rather be coding.
[2913.58 → 2915.24] It's just not so much fun.
[2915.24 → 2921.70] So, I mean, to get that level of knowledge where you can, you know, become a maintainer,
[2921.82 → 2928.76] you really just need to, you need to look at the issues, find some open bugs and fix those
[2928.76 → 2929.10] bugs.
[2929.10 → 2936.68] Because if you are working on triaging stuff, like you're going to have so many questions
[2936.68 → 2940.84] for the other maintainers if you don't understand the project.
[2941.22 → 2944.62] And so that doesn't really help that much, right?
[2944.62 → 2950.42] Because the time we would have spent triaging the issues ourselves is now spent helping
[2950.42 → 2951.38] you triage your issues.
[2951.62 → 2957.36] And so you really need to be able to kind of be self-directed and have this level of knowledge.
[2957.42 → 2960.52] So you got to get in, you got to send pull requests, you got to fix stuff.
[2961.02 → 2966.62] You know if I see somebody that sent and had merged like, you know, several pull requests,
[2966.62 → 2972.78] maybe even just like one or two, like really significant ones, I will go and ask them because
[2972.78 → 2977.86] they've demonstrated that they can navigate the code base, and they can, they can be helpful.
[2977.86 → 2979.56] And that's all we really need.
[2979.62 → 2984.74] It's not like, I wouldn't say it's a really high bar, but it's, it's just one that people
[2984.74 → 2987.60] aren't, they don't really have that time for.
[2987.60 → 2993.04] And they, you know, it's, it's very rare that I'll get pull requests, multiple pull
[2993.04 → 2994.46] requests from a single person.
[2995.06 → 2996.20] Nadia has a book.
[2996.48 → 2996.90] What is it called?
[2996.90 → 2999.32] Nadia Equal, Working in the Open.
[2999.62 → 3000.34] Working, yeah.
[3000.44 → 3001.32] Working in the Open.
[3001.88 → 3002.86] Working in public.
[3003.14 → 3008.68] And I read that recently, and it goes over some of this, some of these ideas about casual
[3008.68 → 3016.34] contributors and how in, in, in certain types of projects, she calls them stadium projects
[3016.34 → 3019.76] where it's very few maintainers and many, many, many users.
[3019.90 → 3029.26] And Mocha is, is one of these, you know, these sorts of very casual pull requests people that,
[3029.34 → 3035.04] that come along once and send a pull request don't end up like really contributing much and
[3035.04 → 3041.12] and can in fact, you know, be problematic because it's just like more, more work.
[3041.20 → 3047.08] Like Mocha right now, it has like 50 open pull requests and some of them are very old
[3047.08 → 3049.96] because we haven't had, had really time to look at it.
[3050.06 → 3054.52] They're either trivial, they're maybe not well-written, maybe they're missing tests.
[3054.94 → 3058.46] It's like people send pull requests, and you never hear from them again.
[3058.56 → 3063.78] And so it's just, you know, it's a heck of a situation that, that we have ourselves in
[3063.78 → 3064.72] on GitHub, I think.
[3065.04 → 3067.90] You know, a lot of projects have, have issues like this.
[3068.18 → 3069.34] So, wow.
[3069.42 → 3073.50] I didn't, I never thought that like pull request and run was a concept, like, you know,
[3073.68 → 3076.86] like it's a bit of PR and never come back.
[3077.82 → 3078.46] Oh yeah.
[3078.54 → 3082.48] I thought people would want to be eager and like, you know, would want to get that
[3082.48 → 3084.74] version, you know, got to get those points, right.
[3084.78 → 3086.98] Got to get those, those, those green marks.
[3086.98 → 3094.78] I think it's sometimes depended, like, so I've not done this in like exact thing before where
[3094.78 → 3095.90] I've done a pull request.
[3095.90 → 3097.18] Because I was using a library.
[3097.40 → 3098.04] I forget what it was.
[3098.12 → 3101.42] I think it was called cleave, which is, I forget what it does.
[3101.42 → 3105.60] But, um, I remember putting in a pull request and being excited about it.
[3105.60 → 3108.22] Because I was like, oh, you should support this particular currency or whatever.
[3108.74 → 3114.70] Uh, and the maintainer did not reply for a long time to the point where I just stopped
[3114.70 → 3115.36] caring.
[3115.36 → 3116.64] I switched jobs.
[3117.00 → 3118.96] I was no longer working on the thing.
[3119.14 → 3121.58] I couldn't be bothered about the thing anymore.
[3121.74 → 3125.96] And I think like months down the road, the maintainer was like, oh, can you update this?
[3125.96 → 3127.58] And I was like, it's been months.
[3127.80 → 3134.32] I don't really want to go back and like, remember what I did and have to, it's a lot of cognitive
[3134.32 → 3134.58] load.
[3134.66 → 3136.64] I think there's a back and forth process here for sure.
[3137.06 → 3142.74] Meaning that sometimes like maintainers can't get to certain things, but sometimes I prefer
[3142.74 → 3144.40] having a bot tell me that.
[3144.40 → 3147.84] So if there's like a bot that's like, Hey, thanks for your PR.
[3148.22 → 3149.86] Someone will be in touch with you or whatever.
[3150.16 → 3150.98] It'll take a while.
[3151.22 → 3152.44] Just hang in there.
[3152.60 → 3155.00] It's better than like not hearing anything.
[3155.00 → 3158.26] Because I think when you don't hear anything, it's one very discouraging.
[3158.48 → 3163.42] Cause now I'm just like, I don't really want to submit a PR ever again to this project
[3163.42 → 3165.26] or engage in any way.
[3165.62 → 3172.38] Because I think as much as I like to think there's an idealism of doing things because
[3172.38 → 3176.30] you want to, or because it's, it's for the overall community.
[3176.30 → 3176.66] Good.
[3176.66 → 3183.82] I think there's a sense of I'm doing this because it will help me and my thing, which
[3183.82 → 3185.44] comes into open source often.
[3185.44 → 3190.10] So a lot of contributors to libraries are like, I'm working on a thing for work or for
[3190.10 → 3193.22] myself and doing this thing will help my use case.
[3193.22 → 3195.60] So there's some like selfishness associated.
[3196.26 → 3201.08] And also sometimes the selfishness has to do with like, I want to have my name on the
[3201.08 → 3204.62] list of contributors in GitHub, like in the stats.
[3205.16 → 3210.84] And so I think it's fair to acknowledge that sometimes and take that into account, especially
[3210.84 → 3215.96] when we're looking at contributions and like, I don't know whether that be merging them in,
[3216.06 → 3220.30] asking people to update them or whatever, like following up overall.
[3220.30 → 3224.18] I feel like I said a lot in that, but yeah.
[3224.58 → 3229.64] You know, you send a pull request, and it sits for six months or a year or longer.
[3230.00 → 3233.04] And then somebody comes along and says, hey, can you update this?
[3233.08 → 3235.80] And you're like, you don't even bother responding, right?
[3236.10 → 3236.36] Okay.
[3236.44 → 3237.98] So yeah, A, that's what happens.
[3238.12 → 3243.50] But B, like, that's fine because you don't care anymore.
[3243.64 → 3248.12] And they didn't really like to have the time to look at it.
[3248.12 → 3249.80] And so it's fine.
[3249.90 → 3251.64] And that's just how it is.
[3251.72 → 3252.92] It's like, whatever.
[3253.38 → 3259.84] You know if we have these old pull requests, like maybe I'm still interested in it, and I'll
[3259.84 → 3262.18] ask and say, hey, do you have time to look at this?
[3262.28 → 3265.16] If not, you know, just don't reply.
[3265.48 → 3267.92] And then we'll do whatever with it.
[3267.92 → 3273.54] But it's, you know, in her book, she said something like she did analysis, and they found
[3273.54 → 3280.26] like 90% of contributors across all of GitHub were one-time contributors or something like
[3280.26 → 3280.44] that.
[3280.44 → 3285.46] And so that is a challenge.
[3285.94 → 3290.02] It's like we, yeah, maintainers are hard to come by.
[3290.10 → 3298.74] People who are dedicated to the project and just set, I mean, I think a big time is just
[3298.74 → 3303.54] setting that time aside for it and wanting to do so.
[3303.54 → 3308.12] Because, you know, there have been periods where I have not wanted to touch Mocha and
[3308.12 → 3308.74] I didn't.
[3309.38 → 3311.94] And, you know, there was nobody breathing down.
[3312.06 → 3315.36] I mean, certainly people on the issue tracker were like, what's going on?
[3315.58 → 3318.64] But I mean, nobody else was like telling me I had to go do it.
[3318.92 → 3323.22] And so, you know, it's hard to find that.
[3323.44 → 3328.46] It's, I think it's also hard to find somebody who's willing to stick it out.
[3328.46 → 3334.10] And if I want to give myself any credit, like, I mean, I've stuck with the project for five
[3334.10 → 3334.42] years.
[3334.68 → 3336.08] And so that's cool.
[3336.52 → 3338.24] And not everybody will do that.
[3338.44 → 3340.08] Many have come and gone, right?
[3340.56 → 3347.54] Yeah, I think, I mean, from a user standpoint who's contributed PRs before, I'm one of those
[3347.54 → 3350.02] people who've contributed once or twice.
[3350.28 → 3352.88] And like, that's my main thing.
[3352.88 → 3360.70] And a lot of it has to do with what was the reception like when I did contribute the PR
[3360.70 → 3366.84] and like the back and forth process of the review and like kind of liaising with the
[3366.84 → 3369.56] team as to like how to merge that thing in.
[3370.22 → 3377.98] And there's often times where it's this strange relationship that you have where when you work
[3377.98 → 3382.76] on a project, sometimes it's one person, in which case the relationship is fairly straightforward.
[3382.88 → 3386.98] But oftentimes it's like there's a team of people and then there's you.
[3387.68 → 3390.88] And so the team will have to review it.
[3391.00 → 3394.60] And the team will also be like, how does this fit in with what we're working on?
[3394.82 → 3402.08] And then it's sort of like you're like an outlier person who contributes to the thing.
[3402.32 → 3404.58] And there have been times that I feel awkward about.
[3404.72 → 3410.20] I think this was specifically like I contributed to DuckDuckGo back when they're, I actually
[3410.20 → 3415.32] don't know if they changed it, but this is like four years ago, three, a while back when
[3415.32 → 3419.08] their repo was public, and they were accepting submissions.
[3419.08 → 3425.50] And it was a really awkward process because I made a change and then there was some discussion,
[3425.50 → 3429.92] but I wasn't part of that discussion because I wasn't on the core team.
[3429.92 → 3434.10] So I wouldn't know what was happening because they were like, we talked about it separately
[3434.10 → 3436.00] and we decided to go down this route.
[3436.00 → 3439.34] And I was like, do you want me to do that work or are you going to do that?
[3439.42 → 3441.44] Like, I don't understand because I'm not there.
[3442.12 → 3447.82] And so there are times when as a user, you feel this sense of like, where do you stand
[3447.82 → 3449.50] in regard to the project?
[3449.74 → 3455.12] And also like, to be honest, this sense, like, I don't think anyone cares if I wrote this or
[3455.12 → 3455.32] not.
[3455.32 → 3458.48] Like I would write it and then no one would care.
[3458.64 → 3463.96] They would forget who I am, which kind of sucks from a user standpoint because you don't
[3463.96 → 3465.70] feel as invested thereby.
[3466.12 → 3466.46] It's true.
[3466.60 → 3470.02] And I think that some of it is like even reputation.
[3470.02 → 3477.32] It's like, if you have made yourself known somewhere else, maybe people recognize your username
[3477.32 → 3479.12] and they'll give you more attention.
[3479.12 → 3488.32] I've definitely had that happen where like I send PRs and people will actually respond
[3488.32 → 3488.98] pretty quickly.
[3489.48 → 3491.00] And I was like, oh, hey, cool.
[3491.56 → 3495.28] And I send plenty of drive by PRs because it's something I want fixed.
[3496.76 → 3498.90] And it's like, it's a bug.
[3498.98 → 3500.34] And so I'm going to try to fix the bug.
[3500.44 → 3500.62] Sure.
[3500.62 → 3506.76] But I think like trying to build, like if you are a library author, I think trying to
[3506.76 → 3514.32] build relationships with the people who maintain the libraries you depend on is cool.
[3514.68 → 3515.84] And the other way as well.
[3516.18 → 3521.70] So like Mocha doesn't use TypeScript, but TypeScript uses Mocha, right?
[3521.70 → 3526.46] So all of TypeScript's huge test suite, those are Mocha tests.
[3526.46 → 3530.20] And so I know that they're like a big user of it.
[3530.34 → 3538.52] And so, you know, trying to kind of cultivate a back and forth with the TypeScript team, I
[3538.52 → 3544.14] think has been very beneficial for both of us.
[3544.36 → 3551.66] Like I can go, like recently, I knew there was a Mocha issue in the TypeScript repo.
[3552.04 → 3554.28] And so I went, and I sent a pull request to fix it.
[3554.28 → 3557.48] And of course, it got attention right away and got merged quickly.
[3558.12 → 3562.88] Like it's probably not most people's experience sending a pull request to TypeScript.
[3564.24 → 3564.42] Yeah.
[3564.82 → 3566.58] Look at you, Chris.
[3566.88 → 3570.46] You're like, you're in the HOV lane on GitHub.
[3570.46 → 3570.94] It is.
[3571.16 → 3571.58] I love it.
[3572.26 → 3573.90] There's, it's, it's social media.
[3574.08 → 3574.72] That's reputation.
[3575.00 → 3576.02] Right, right.
[3576.24 → 3576.54] You know?
[3576.66 → 3577.74] Well, you know what?
[3577.78 → 3582.78] I'm super, like, it's just, it's been such a pleasure to like talk with you about all this.
[3582.78 → 3583.88] And it's been super fun.
[3583.88 → 3588.80] And like, you know, I'm so happy that such an important project has such, I would say,
[3588.90 → 3590.82] forward-thinking leaders and leadership.
[3591.22 → 3596.36] I really think, like Divya said earlier, it comes down to like forward-thinking and like
[3596.36 → 3600.20] avoiding fads and really kind of being in it for the long haul.
[3600.20 → 3603.14] I think for these projects to like to have the level of adoption that they do.
[3603.26 → 3605.36] And, you know, it's been really great to learn about that.
[3605.92 → 3612.16] So I think one corny joke that I've been holding back on for the past 10 minutes.
[3612.30 → 3613.20] Can I, can I do it?
[3614.56 → 3615.58] Am I going to hate it?
[3615.58 → 3617.14] No, no, it's not that one.
[3617.74 → 3618.14] Okay.
[3618.68 → 3619.64] We'll have to link.
[3620.12 → 3624.06] We'll put a secret link into the show, show notes for what the other one is about.
[3624.20 → 3624.92] I won't say it.
[3624.92 → 3630.14] I promised, I promised Chris, I, I already used up my token for the day, essentially.
[3630.48 → 3639.02] But anyway, so the joke is once, twice, three times a PR.
[3639.02 → 3641.66] Do you guys know that song?
[3641.98 → 3655.70] You once, twice, three times a lady, and I love you.
[3655.70 → 3656.82] I have no idea.
[3657.18 → 3658.20] Oh my God.
[3658.40 → 3658.78] All right.
[3659.16 → 3659.72] Then you know what?
[3659.74 → 3661.94] Is that like, is that Neil Diamond or something?
[3661.96 → 3662.82] I think so.
[3662.90 → 3665.66] It's like one of those classic, you know, singers.
[3666.30 → 3667.00] Lionel Richie.
[3667.00 → 3671.56] Uh, but yeah, that should be your goal, you know, just try to, try to have consistent,
[3671.56 → 3675.20] uh, like if you're interested in actually contributing, it'd be nice to like, stick
[3675.20 → 3677.68] with, like get over the hump and stick with it, you know?
[3677.98 → 3680.26] But anyway, thank you so much for your time, Chris.
[3680.30 → 3681.36] It's been amazing.
[3681.52 → 3683.24] Where can people find you on the internet?
[3683.82 → 3687.22] Well, Bone Skull, B-O-N-E-S-K-U-L-L.
[3687.60 → 3688.80] And, uh, I'm on GitHub.
[3688.80 → 3695.20] I also have a website that I never post on, um, which is BoneSkull.com.
[3695.20 → 3697.96] And, um, yeah.
[3698.48 → 3703.46] Otherwise, like I hang out in some slacks in the Opens Foundation slack is one.
[3703.78 → 3705.24] So you can go and sign up for that.
[3705.32 → 3710.16] And it's, uh, also there's a Mocha Gitter, uh, chat room.
[3710.48 → 3712.86] Um, that's like our official chat room.
[3712.86 → 3715.24] And so you can pop in there as well.
[3715.24 → 3717.90] And those are some good places to find me.
[3718.36 → 3721.52] And, uh, on Twitter, you can tweet at me.
[3721.78 → 3727.04] And that's Bone Skull with a zero instead of an O because somebody took it already.
[3727.30 → 3734.10] And they like signed up for Twitter once and posted one tweet, um, about eight years ago.
[3734.34 → 3737.20] And, um, they won't give me the username.
[3737.44 → 3737.96] Anyway.
[3738.22 → 3739.32] So yeah.
[3739.70 → 3740.94] Bone Skull with a zero on Twitter.
[3740.94 → 3743.66] I thought the zero was intentional, but, you know.
[3743.84 → 3744.34] Yeah, same.
[3744.42 → 3744.72] Me too.
[3745.30 → 3747.16] I'm learning, learning, learning things today.
[3747.26 → 3748.54] You know, I like the zero.
[3749.02 → 3751.50] Uh, you know, it's pretty elite.
[3751.60 → 3751.84] Yeah.
[3751.98 → 3752.22] I mean.
[3753.22 → 3753.76] All right.
[3753.80 → 3754.78] Well, that's it, folks.
[3754.82 → 3756.26] We'll catch you next week.
[3756.42 → 3757.10] Thanks, everyone.
[3757.10 → 3757.92] Bye.
[3760.36 → 3763.08] This is our last episode of 2020.
[3763.56 → 3769.04] We like to take two weeks off at the end of each year to relax, re-energize, and gear up for an awesome new year.
[3769.18 → 3769.80] Fingers crossed.
[3769.80 → 3778.70] We want to thank you for listening to JS Party, for hanging out during the live shows, for suggesting excellent topics and guests, and helping make the JavaScript community awesome.
[3779.34 → 3786.00] If you're longing for more JavaScript content during the break, I personally recommend our episode on the builder patter for your career.
[3786.32 → 3788.28] Let's replace your kidney with React.
[3788.66 → 3790.28] What's new and what's next, JS?
[3790.76 → 3793.62] And lesser known things browsers can do in 2020.
[3794.40 → 3797.14] I'll link those episodes up in the show notes for you.
[3797.14 → 3799.38] It's a great time to catch up on the goodness.
[3800.26 → 3804.90] Music for JS Party is provided by the Mysterious Break master Cylinder, and we are brought to you by awesome sponsors.
[3805.58 → 3808.22] Thanks again to Vastly, Linde, and Launch Darkly.
[3808.72 → 3809.54] That's our show.
[3810.12 → 3811.44] We'll talk to you again next year.
[3815.76 → 3820.28] Bye.
