[0.00 → 17.76] Welcome to the Changelog episode 0.7.1.
[17.96 → 18.94] I'm Adam Stachowiak.
[19.20 → 19.96] And I'm Winn Netherlands.
[20.08 → 21.00] This is the Changelog.
[21.04 → 22.54] We cover what's fresh and new in open source.
[22.80 → 25.42] If you found us on iTunes, we're also on the web at thechangelog.com.
[25.62 → 26.44] We're also up on GitHub.
[26.44 → 28.60] Head to GitHub.com slash explore your funds.
[28.76 → 31.88] Some trending reposts, some feature reposts from our blog, as well as the audio podcast.
[32.18 → 34.16] And if you're on Twitter, follow ChangeLog Show.
[34.80 → 35.70] And me, Adam Stack.
[36.02 → 38.24] And I'm Penguin, P-E-N-G-W-I-N-N.
[38.88 → 39.76] Fun episode this week.
[39.82 → 42.02] Talk to Alex McCall from Twitter.
[42.46 → 46.46] He's known for Spine, which is an alternative to Backbone.
[46.94 → 49.68] So these single-page JavaScript apps are really catching on.
[50.14 → 50.32] Yeah.
[50.96 → 53.30] This is a fun little conversation you guys had here.
[53.32 → 54.20] It wasn't too long, though, was it?
[54.66 → 55.10] No.
[55.10 → 56.40] It's a couple of weeks back.
[56.56 → 58.74] The original version of Spine was in JavaScript.
[58.88 → 60.28] It was rewritten in CoffeeScript.
[60.46 → 64.20] So if you sling the coffee, you'll be interested in checking out Spine.
[65.40 → 68.08] And also a little controversy if Nathan Smith is listening to this.
[68.24 → 68.78] That's true.
[68.98 → 69.60] Friend of the show.
[69.98 → 70.14] Yeah.
[70.68 → 72.64] A lot of things going over at GitHub these days.
[72.72 → 78.10] We need to get these guys back on the show to talk about some of their recent hires and acquisitions.
[78.86 → 81.58] I mean, it would be nice to talk about, was it Hu bot as well?
[81.66 → 82.32] That's a lot of fun.
[82.32 → 82.88] Yeah.
[83.60 → 85.32] Hu bot, I guess that's how you pronounce it.
[85.50 → 86.14] It reads Hub bot.
[86.30 → 89.34] It's the GitHub robot for Campfire.
[89.44 → 96.28] They have adapters for, we use it for Hip Chat, but they have it for various numbers of real-time chat tools.
[96.40 → 97.84] I guess IRC probably as well.
[98.04 → 99.50] Got to get them back on the show.
[99.50 → 104.02] Yeah, especially, you know, they're reaching out into the .NET world.
[104.28 → 107.40] Azure or Azure is now on GitHub.
[107.58 → 110.70] So hopefully we can talk about some .NET and open source.
[110.94 → 111.56] And some Nougat.
[112.12 → 112.94] Some Nougat.
[113.02 → 115.18] Yeah, we did talk about Nougat a while back.
[115.26 → 116.44] So we do need to talk about that.
[116.74 → 117.00] Yeah.
[117.56 → 118.44] Fun episode this week.
[118.48 → 119.00] Should we get to it?
[119.22 → 119.82] Let's do it.
[119.82 → 129.60] We're chatting today with Alex McCall from Twitter.
[129.80 → 133.88] He's the author of the Spines project and some other things.
[134.16 → 137.88] So Alex, why don't you introduce yourself a little bit more about what you do at Twitter?
[137.88 → 146.88] Well, I work on the front end at Twitter and I do all sorts of JavaScript and Ruby stuff with the ad platform.
[147.70 → 152.68] And in my spare time, I do Spine and also travel and write.
[153.50 → 155.04] I've written a few books for O'Reilly.
[156.00 → 158.10] And in fact, a new one is coming out in December.
[159.98 → 164.62] I've just moved from England to San Francisco, and I've actually just started at Twitter.
[164.76 → 166.12] I've only been here for two weeks.
[166.96 → 167.32] Well, welcome.
[167.88 → 169.02] Congratulations on the move.
[169.18 → 175.92] So I guess the obvious question up front when we're talking about Spine is what relation, if any, does it have to Backbone?
[176.62 → 178.94] Well, Spine was inspired by Backbone.
[180.20 → 182.54] And yeah, without Backbone, there would be no Spine.
[182.80 → 187.68] And obviously, you can tell by the name that it's related.
[188.64 → 195.22] However, Spine does have a different take on JavaScript web applications and moving state to the client side.
[195.22 → 197.48] It's got a completely different model API.
[198.16 → 200.72] It's got this whole asynchronous UI approach.
[200.72 → 205.88] So there is a similarity there, but there's also quite big differences.
[206.50 → 210.54] What's propelling this movement to moving everything to the client in the last few years?
[210.60 → 212.96] This trend that we've got with client-side JavaScript applications.
[212.96 → 218.84] What seems to be the technical advances under the hood that's just empowering this?
[219.10 → 221.54] Well, we've got amazing browsers now.
[221.60 → 224.98] We've got amazing VMs and V8, for example, Chrome.
[224.98 → 232.48] We've got a browser wall, which is propelling software companies like Apple and Google to compete and approve their browsers.
[233.14 → 235.64] And it's all in the aim of a better user experience.
[236.22 → 239.22] These client-side web apps are just really fast.
[240.08 → 242.40] And I think at the end of the game, that's what it's about.
[242.48 → 243.14] It's about speed.
[244.08 → 246.22] Now, Spine's written in CoffeeScript, right?
[247.10 → 248.10] That's correct, yes.
[248.36 → 250.84] Was the first version, was it CoffeeScript from the get-go?
[250.84 → 254.74] No, it was JavaScript originally, and then I ported it to CoffeeScript.
[255.12 → 258.30] Because at the time, I just didn't know about CoffeeScript.
[259.08 → 262.30] What niceties have you found along the way?
[262.80 → 264.82] Well, it's much smaller.
[265.48 → 267.20] Well, I mean, at least the CoffeeScript is smaller.
[267.32 → 269.10] The compiled source is about the same size.
[270.30 → 277.46] And CoffeeScript has a ton of really nice language features that stop you, A, making stupid mistakes.
[277.46 → 283.22] It sort of uses a small subset of JavaScript, so it uses the good parts.
[284.02 → 291.48] So you can avoid having things like semicolons and global variables.
[291.62 → 292.72] It'll sort all that for you.
[292.92 → 295.60] And I found that that's really useful when I've been programming.
[296.80 → 299.46] And I wish I could use...
[299.46 → 301.06] Actually, I better not say that, sorry.
[301.06 → 308.10] I wish I could never write JavaScript again and just use CoffeeScript, because I love it so much.
[309.46 → 312.76] And I use it every day.
[313.62 → 321.92] Let's talk a bit about MVC and how it may be different from some of the MVC frameworks for web apps on the server.
[321.92 → 329.64] When we talk about MVC and a client-side JavaScript application, are the views really views?
[329.76 → 333.86] Or are they, in the case of Backbone, no, they're really more or less view controllers?
[334.06 → 336.14] What's a view in Spine?
[336.62 → 338.94] Well, I guess it's just a terminology thing.
[339.24 → 346.00] In Spine, I call a template a view, whether that be an echo template or a moustache template.
[346.00 → 351.24] In Backbone, views are more like Spine's controllers.
[352.12 → 354.06] And it's just more of a terminology thing.
[355.02 → 359.76] So we were doing a mind map between the two, just for those that may have Backbone experience.
[360.64 → 369.04] So if a view in Backbone is a template, or a controller rather, in Spine, what's the correlation between routers and routers?
[369.04 → 376.88] Routers and routers, well, Spine doesn't really have a separate class to do with routers.
[377.24 → 380.50] You do routing inside your controller.
[381.64 → 381.88] Okay.
[382.34 → 385.06] So much less, more like the Sinatra pattern then, rather.
[385.38 → 386.14] That's correct, yes.
[386.86 → 387.54] You mentioned eco.
[387.84 → 388.96] Is that your favourite emulating?
[389.46 → 390.16] It is.
[390.74 → 395.28] Again, one of the reasons is because the syntax is CoffeeScript.
[395.28 → 401.36] And also, if you have a look at the source of eco, it's spotless.
[401.50 → 402.36] It's really nice.
[403.36 → 408.00] And this is something that a lot of emulating libraries have an issue with.
[409.40 → 412.72] If you look at what's going on behind the scenes, it's pretty nasty.
[412.90 → 413.90] And that's not the case with eco.
[415.12 → 423.76] One of the advantages or the promises of Moustache is to use the same emulating project server-side and client-side.
[423.76 → 425.96] Is that kind of false goal?
[426.80 → 428.10] I think it's a bit of a pipe dream.
[429.28 → 434.70] I mean, I guess I view it the same as using models on the client-side and the server-side.
[435.36 → 437.80] And it would be great if that was the case.
[437.90 → 443.54] But I haven't really seen a practical application actually using that.
[444.32 → 447.32] Because at the end of the day, you're always going to have some differences.
[447.32 → 455.62] And I think what is a little shame about Moustache is that because they've gone down that route, it limits their syntax somewhat.
[456.14 → 458.72] Because they have to be compliant across all these different languages.
[459.84 → 468.66] And if you're not using the template on both the server and client-side, then there's no point having those syntax limitations.
[468.66 → 475.20] So on the Spine project page, you outline the integration with Rails and the asset pipeline.
[475.86 → 479.50] Talk a bit about how that sets up and what that looks like.
[480.14 → 482.16] Well, it's so simple with Rails.
[482.42 → 486.50] It integrates with Rails generators, Rails asset pipeline.
[486.50 → 491.46] We're just basically piping in Spine's JavaScript.
[492.82 → 502.86] And when you do Rails generate Spine new, it will create a new Spine application in the app assets JavaScript folder.
[503.44 → 505.14] And everything is set up there for you.
[505.26 → 507.08] And then you can generate new controllers and models.
[507.54 → 513.78] And the great thing is if you set up a Rails scaffold, and you set up a Spine model on the front end,
[514.20 → 515.82] the two will talk to each other straight away.
[516.82 → 519.12] So Spine sort of works with Rails out of the box.
[519.90 → 525.12] And you've got the same generators for Spine objects as well, controllers views, scaffolds?
[525.36 → 526.10] Yeah, that's correct.
[526.22 → 532.40] Yeah, you can also generate Spine scaffold, which will integrate with the Rails scaffold over Ajax.
[533.12 → 534.34] You also mentioned Hem.
[535.14 → 537.06] Is that your preferred platform?
[537.56 → 541.66] Well, if you're not integrating with Rails, then that is my preferred platform.
[542.32 → 544.72] Hem is not to be used in production.
[544.72 → 546.48] It's just in development.
[547.10 → 548.94] And then you can serve static files in production.
[549.36 → 552.34] But basically what it is like Bundler for Node applications.
[553.10 → 554.58] And it will pull out.
[554.66 → 555.94] You can have NPN dependencies.
[556.64 → 558.04] And you can have local dependencies.
[558.04 → 562.72] And it will pull all those out together and compile them into one JavaScript file.
[562.92 → 565.12] And it also manages your CSS.
[566.60 → 568.80] And so that is my preferred method.
[568.92 → 572.30] If you're not going with Rails and you just want to build a Node app,
[572.68 → 575.92] or you're building like a mobile app, then just use Hem.
[575.92 → 578.20] Are you doing a lot of Node development?
[578.88 → 579.48] I do.
[579.84 → 583.34] In fact, there's a developer here called Michael Jackson,
[583.34 → 587.50] and we're working on a new web framework called Strata,
[588.22 → 591.76] which is going to replace Express in some of our projects.
[592.14 → 594.70] And we're also working with a lot of Node and Fibres
[594.70 → 600.66] and trying to reduce the asynchronous pattern style in Node.
[600.66 → 602.94] You get into callback hell.
[603.44 → 605.96] And so Michael and I have been working a lot with Node
[605.96 → 607.98] to try and solve that problem.
[609.04 → 611.58] So what powers the real-time aspect of Spine?
[613.72 → 615.92] Well, Spine isn't inherently real-time.
[617.26 → 621.28] In fact, yeah, you just need to add real-time support to it.
[622.62 → 623.96] It's the same with Backbone.
[624.26 → 627.52] If you have views that are bound to your models,
[628.02 → 630.28] then adding real-time support is pretty simple.
[630.28 → 631.82] All you have to do is update the models,
[632.04 → 634.60] and then your interface automatically updates.
[635.58 → 639.20] So there's no inherent, I guess, pusher or socket.io support?
[639.46 → 640.44] It's just...
[640.44 → 641.40] That's correct.
[641.90 → 643.52] And, I mean, in a lot of Spine examples,
[643.68 → 647.12] I've used an RPC framework,
[647.52 → 649.40] or you could call it Pub Sub framework,
[649.54 → 651.80] called Turnout, which I produced a few years earlier.
[653.24 → 655.98] And basically, your Ruby models,
[656.14 → 657.94] you just have an observer,
[657.94 → 662.52] and that will basically send messages to Turnout saying,
[662.76 → 664.60] this model's changed, these are new attributes.
[665.20 → 666.74] Turnout will send it out to all the clients,
[667.08 → 668.98] or the clients have to update their models,
[669.10 → 670.60] and then their views automatically update.
[671.36 → 674.32] So adding real-time support is literally like five minutes.
[674.32 → 676.98] What type of applications are you building with Spine?
[677.72 → 681.08] Well, the main reason I developed Spine
[681.08 → 683.00] was for this guide app.
[683.12 → 685.10] I'm trying to digitize the Lonely Planets
[685.10 → 686.40] and put them on the iPhone,
[686.98 → 688.50] and on the iPad, and the desktop.
[690.10 → 692.96] And so this app basically lets you select countries,
[693.12 → 696.34] places, locations, and look at reviews and photos.
[696.34 → 698.20] And it's quite simple,
[698.46 → 703.76] but it's a good stepping stone for other Spine applications.
[704.80 → 708.06] You mentioned local storage here on the Spine project page.
[708.80 → 711.42] What other storage mechanisms does Spine support?
[712.16 → 715.82] So Spine out-of-the-box supports local storage and AJAX.
[717.32 → 718.30] And with local storage,
[718.38 → 720.52] it's just a case of including that in your models,
[720.96 → 722.34] sorry, including a line of code
[722.34 → 724.62] which imports the local storage module.
[725.44 → 727.94] And that'll persist it when the page closes.
[728.22 → 729.50] That'll persist all the model data,
[729.60 → 730.70] and when you reopen the page,
[731.08 → 732.76] it'll all be there and populated.
[733.86 → 734.98] And AJAX is similar.
[735.36 → 736.66] You import the AJAX module
[736.66 → 738.26] and give it an endpoint,
[738.76 → 740.68] and Spine will basically just use
[740.68 → 745.20] standard REST calls like post, put, get
[745.20 → 747.90] on that AJAX endpoint to persist your data.
[748.50 → 750.36] Talk a bit about Spine.app.
[750.36 → 754.08] So Spine.app integrates with HEM,
[754.18 → 756.60] and it's basically just a Spine application generator.
[757.82 → 760.04] And you just do Spine.app,
[760.58 → 762.04] and it'll generate your app.
[762.10 → 763.88] It'll generate all the directory structure,
[764.42 → 766.30] your MVC, your controllers,
[766.54 → 768.70] your views, and your models.
[769.10 → 770.94] And it'll generate public directory,
[771.28 → 774.16] and it'll deal with all your CSS.
[775.06 → 777.20] And Spine.app is actually very useful
[777.20 → 778.90] when it comes to building mobile apps,
[778.90 → 781.28] because Spine has this Spine mobile project,
[781.82 → 783.40] sort of extension to Spine.
[783.92 → 786.72] And Spine.app basically will generate
[786.72 → 789.84] that mobile project directory for you,
[789.92 → 791.54] which you can then sort of wrap up with Phone Gap.
[791.84 → 794.20] So Phone Gap, is that your preferred method
[794.20 → 796.78] for wrapping these for the App Store?
[797.90 → 799.34] Or the Android Marketplace?
[799.62 → 801.68] Yeah, that is my preferred method,
[801.90 → 804.78] mostly because I just haven't looked at other alternatives.
[804.78 → 807.04] But it works very well for me.
[807.70 → 809.42] I'm a Titanium guy myself,
[809.60 → 812.02] but there's no reason why you couldn't take
[812.02 → 813.40] an HTML5 application like this
[813.40 → 816.14] and wrap it in Titanium as well.
[816.34 → 817.90] You know, I'm wondering,
[818.20 → 821.16] once we have a truly positioned fix mechanism
[821.98 → 823.68] to have a toolbar at the bottom of the page,
[823.74 → 825.06] and iOS 5 supports this,
[825.48 → 828.86] how much more use we'll have for native platforms
[828.86 → 831.34] if we want to just circumvent the App Stores
[831.34 → 834.86] and Android Marketplaces and just publish our apps?
[835.30 → 836.00] Well, that's right.
[836.24 → 838.62] I mean, iOS 5 fixed the biggest issue,
[838.76 → 840.44] which was with the scrolling.
[840.62 → 843.00] So now you can have fixed headers and footers.
[843.98 → 847.40] And the only other reason that I'm using Phone Gap
[847.40 → 849.56] and integrating into the marketplace
[849.56 → 852.70] is because I want to access some of the payment APIs,
[852.86 → 854.06] and that's the only way to do it.
[854.06 → 858.72] But if I was just building a mobile web app
[858.72 → 862.36] without needing to access any of the native APIs,
[862.56 → 864.20] then definitely that's what I would do.
[864.28 → 867.36] I would just use pure HTML and host it myself.
[868.50 → 871.16] What range of devices are you aiming to support?
[872.14 → 874.90] At the moment, it's iPhone.
[876.36 → 879.30] Android's WebKit browser is not up to scratch.
[879.30 → 883.82] You know, the transitions look jumpy,
[884.32 → 887.40] and it just doesn't feel great, to be honest.
[888.24 → 890.48] And I think in a few months' time,
[890.62 → 891.78] maybe half a year's time,
[892.26 → 894.68] Android support will be amazing.
[895.70 → 899.90] And then you can write once and deploy everywhere.
[900.08 → 900.92] That's the idea.
[901.70 → 904.94] What type of user interface are you employing in your applications?
[904.94 → 910.58] I know when a lot of HTML5 apps try to mimic native applications,
[910.74 → 911.86] they fall quite short.
[912.10 → 914.70] And so should we just be building something entirely different?
[915.40 → 918.14] Well, I think that's a bit of an excuse
[918.14 → 919.76] to build something a bit crapper.
[920.06 → 923.56] I think it's fine if you're building something completely different,
[923.72 → 926.86] as long as it's as good or better than the native experience.
[927.14 → 929.80] But I find that it's often used as an excuse.
[929.80 → 934.14] And certainly, I've built web apps, mobile web apps,
[934.26 → 936.16] that are very difficult to tell.
[936.30 → 936.82] They're not native.
[937.40 → 939.02] You can emulate pretty much everything.
[939.18 → 940.16] You can emulate the transitions.
[940.68 → 943.84] You can emulate all the CSS styles for the header and footer.
[944.20 → 945.78] And it looks practically identical.
[946.68 → 950.96] So you're still doing the drill-down stack controllers type of user interface,
[951.22 → 956.14] the UI table controller type on the iOS platform,
[956.42 → 957.60] that sort of paradigm?
[957.60 → 963.12] Well, what you mean having tabs and views that sort of flip in and out?
[963.72 → 966.16] I know that like the drill-down where you have a table of options
[966.16 → 967.58] and you click one and it slides.
[968.10 → 968.90] Yes, that's great.
[969.02 → 970.40] Yeah, I'm using that.
[970.60 → 973.78] And that works great for mobile interfaces.
[974.34 → 976.60] So you're writing a CoffeeScript book.
[977.26 → 979.78] Yes, it's called The Little Book on CoffeeScript.
[979.94 → 982.70] And it was actually open-sourced a while back.
[982.70 → 988.22] But O'Reilly have recently approached me to publish it.
[988.54 → 992.10] And it's going to be free online through O'Reilly's site.
[992.34 → 994.80] And you'll be able to pay for a printed version if you want one.
[995.32 → 996.68] So what did you learn writing this book?
[997.56 → 1002.86] Well, I mean, one of the best ways of learning is teaching, right?
[1002.86 → 1006.90] And so I learned a hell of a lot about CoffeeScript just by writing the book.
[1007.92 → 1010.20] And also I learned a lot about CoffeeScript style.
[1010.54 → 1014.48] I was lucky enough to get Jeremy, the creator of CoffeeScript,
[1014.60 → 1015.70] to go through the book.
[1015.76 → 1017.30] And in fact, he's writing one of the chapters.
[1018.42 → 1020.74] And so he taught me a lot about CoffeeScript style
[1020.74 → 1022.74] and what I should and shouldn't do.
[1022.88 → 1024.06] And it makes a lot of sense.
[1024.78 → 1026.74] Maybe give us a couple of pointers on that.
[1026.82 → 1028.50] What makes good CoffeeScript style?
[1028.50 → 1032.34] For example, using and instead of double ampersand.
[1033.00 → 1034.12] It just reads much better.
[1034.52 → 1035.56] What about parentheses?
[1036.52 → 1037.50] Yeah, you don't...
[1039.14 → 1040.22] Drop when optional?
[1040.66 → 1046.46] Yeah, I would drop parentheses unless you need to make it obvious.
[1046.58 → 1048.24] Unless it's not obvious of what's going on.
[1049.14 → 1052.94] And sometimes if you've got like three or four nestled function calls,
[1053.22 → 1054.88] then you definitely want to use parentheses.
[1054.88 → 1059.02] We've also got another book for O'Reilly, JavaScript Web Apps.
[1059.30 → 1059.48] Yeah.
[1059.60 → 1060.56] Talk a bit about that one.
[1061.06 → 1063.42] Well, I wrote this as I was travelling.
[1064.72 → 1069.06] And it's a book about building JavaScript web applications
[1069.06 → 1071.42] and moving states to the client side.
[1072.06 → 1075.10] And the main part of the book is MVC.
[1075.36 → 1080.42] And we take you through building a model view controller interfaces.
[1080.42 → 1083.70] It's not language or library specific.
[1084.82 → 1086.84] All the examples at the end,
[1087.76 → 1093.10] you have spine examples at the end and backbone examples and JavaScript MVC.
[1093.46 → 1095.58] But throughout the book, it's generic.
[1096.24 → 1098.90] What are some of the gotchas of building single page web apps
[1098.90 → 1101.70] that maintain state on the client?
[1102.20 → 1103.62] Well, it's a lot of work.
[1103.76 → 1105.68] And it's also a big paradigm shift.
[1105.80 → 1108.50] It's quite hard for a lot of developers to get their head around.
[1108.50 → 1111.70] You have to move all the rendering to the client.
[1112.24 → 1114.62] And it's very difficult to convert an existing app
[1114.62 → 1116.06] into using this sort of architecture.
[1117.20 → 1118.90] Usually, you have to start from scratch.
[1119.44 → 1120.94] So it's a lot of work.
[1121.10 → 1123.52] But I think the advantages are worth it.
[1124.38 → 1127.36] The really quick UI that you get from it is worth it.
[1127.36 → 1132.08] So what does an architecture for these types of applications look like?
[1132.38 → 1136.00] Do you normally just build out an API first
[1136.00 → 1138.04] and then build a user interface on top of that?
[1138.14 → 1139.92] Or do you still stub out the design first?
[1140.28 → 1142.68] What I do is I start straight out with the design,
[1142.82 → 1143.98] do the CSS and HTML.
[1144.52 → 1147.64] And then I do the models' client side.
[1147.74 → 1149.84] And I basically stub out the data for them.
[1149.84 → 1152.58] And I get everything working client side
[1152.58 → 1154.20] because at the end of the day, that's what matters.
[1154.78 → 1156.02] And then once all that's done,
[1156.52 → 1159.12] then I do look at the server side.
[1159.36 → 1162.24] And I have a much better idea of what models and API
[1162.24 → 1164.52] I need on the server side once the client side is finished.
[1165.38 → 1168.38] What tools do you have to debug these applications on mobile?
[1168.38 → 1175.10] I usually just use Safari and Chrome to develop them
[1175.10 → 1178.86] and sometimes the iOS simulator.
[1179.98 → 1181.10] And that's enough for me.
[1181.24 → 1182.60] I just use the web inspector.
[1183.42 → 1186.10] Are you building applications that install to the home screen?
[1186.36 → 1190.12] And do you do anything special with the meta tags
[1190.12 → 1192.96] that you can do to make a full screen application on iOS?
[1193.60 → 1194.38] Yeah, absolutely.
[1195.14 → 1197.80] For example, Spy Mobile comes with a default set of meta tags
[1197.80 → 1199.94] that prevents you sort of zooming in
[1199.94 → 1204.22] and set the page title, the page icon, and that sort of thing.
[1204.76 → 1206.98] And definitely I'm using those in all sorts of applications.
[1207.68 → 1209.48] You mentioned async earlier.
[1209.78 → 1213.34] What problems do async, I guess,
[1213.90 → 1216.04] present when you're building an async UI?
[1216.56 → 1218.76] Well, again, it's a little bit more complicated.
[1219.46 → 1222.46] So the idea is that you never block the user.
[1222.46 → 1224.32] So they interact with your application
[1224.32 → 1226.26] and you never block their interaction.
[1226.26 → 1228.40] So let's say they are sending an email.
[1228.76 → 1230.38] In Gmail, when you click send an email,
[1230.64 → 1233.94] it waits like two or three seconds saying sending your email.
[1234.44 → 1238.78] And I'm saying that you either lie to the user
[1238.78 → 1240.14] or in the case of email,
[1240.40 → 1243.46] you just put it in the outbox like you would in an IMAP client
[1243.46 → 1244.94] and you don't block the UI
[1244.94 → 1248.32] because I think that's a terrible user experience.
[1248.32 → 1251.18] So when you're building out your views in Spine,
[1251.28 → 1255.70] are you taking advantage of JST just in Rails or around?
[1255.92 → 1257.38] Yes, just in Rails.
[1258.08 → 1260.02] I mean, when it comes to ham,
[1260.10 → 1264.16] you can just use common JS modules rather than use sprockets.
[1264.82 → 1267.52] So do you find yourself always passing data across the wire
[1267.52 → 1268.56] and bind to that?
[1268.88 → 1270.70] Or do you ever pass markup across the wire?
[1271.22 → 1273.46] Always data, just JSON data.
[1273.46 → 1275.90] If you start passing markup across the wire,
[1276.00 → 1277.64] then you haven't got an asynchronous interface
[1277.64 → 1280.54] because you rely on the server to render the page.
[1280.96 → 1282.20] So if somebody updates,
[1282.60 → 1284.58] let's say adds a new comment to a blog post,
[1285.00 → 1287.88] the server has got to respond with that markup.
[1288.02 → 1290.20] Whereas if you're rendering everything client-side,
[1290.30 → 1291.32] you could display instantly.
[1291.96 → 1294.12] So you guys still hiring at Twitter?
[1294.78 → 1295.48] Yes, we are.
[1295.56 → 1298.40] We're hiring every day.
[1298.48 → 1299.76] We've got new people interviewing.
[1299.76 → 1303.18] And if you're interested in working here,
[1303.28 → 1304.56] then you should definitely get in touch.
[1304.90 → 1305.90] It's a great team.
[1306.94 → 1309.66] And it's a fascinating company
[1309.66 → 1312.42] because there's some huge problems to work on.
[1313.48 → 1314.22] One last question.
[1315.24 → 1317.16] So what open source project out there
[1317.16 → 1319.04] just has you excited that you want to play with?
[1320.16 → 1321.36] That's a good question.
[1321.36 → 1326.50] I think it would...
[1326.50 → 1328.08] We'll edit this out,
[1328.14 → 1331.36] but I think it would be Strata,
[1331.58 → 1332.94] but we already talked about that.
[1334.00 → 1335.46] I'll throw another curveball at you.
[1336.38 → 1337.82] Who's your programming hero?
[1339.34 → 1342.14] Jeremy Athenians would definitely be him.
[1342.96 → 1346.06] Yeah, that guy has created Backbone and CoffeeScript.
[1346.18 → 1346.86] I think that's incredible.
[1347.46 → 1349.16] He is a programming stud, that's for sure.
[1349.16 → 1349.60] Sure.
[1349.76 → 1351.64] Well, thanks, Alex, for joining us.
[1352.10 → 1353.20] And good luck at Twitter.
[1353.30 → 1356.94] We look forward to seeing the CoffeeScript book out this,
[1357.38 → 1358.14] I guess later this,
[1358.94 → 1361.02] before the end of the year or early next year?
[1361.36 → 1361.94] In December.
[1362.38 → 1362.98] In December.
[1363.40 → 1364.52] We'll keep an eye out for that.
[1365.44 → 1365.94] Thanks, Alex.
[1366.42 → 1367.26] Thank you very much.
[1367.26 → 1368.26] Thank you.
[1379.16 → 1408.40] Bye-bye.
