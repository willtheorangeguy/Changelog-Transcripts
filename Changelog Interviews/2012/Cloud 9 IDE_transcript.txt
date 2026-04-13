[0.00 --> 4.14]  This episode of The Change Log is brought to you by Pusher.com.
[4.64 --> 10.76]  Pusher is a hosted API for quickly adding scalable real-time functionality to web and mobile apps.
[11.14 --> 16.86]  If you're building anything that needs to get data from the server back to the client asynchronously,
[17.16 --> 18.92]  you need to check out Pusher.
[19.38 --> 21.62]  They've got a number of tutorials to help you get started,
[21.86 --> 25.28]  everything from a quick start guide to building a real-time chat client,
[25.56 --> 28.56]  push notifications, activity streams, and more.
[28.56 --> 34.82]  Use our coupon code THECHANGELOG to save 15% off your first month.
[35.12 --> 38.88]  Join the real-time web today and get your free API account.
[39.36 --> 40.76]  Head to Pusher.com.
[40.76 --> 41.16]  Pusher.com.
[53.96 --> 54.40]  Pusher.com.
[54.40 --> 55.40]  Pusher.com.
[55.40 --> 55.72]  Pusher.com.
[55.72 --> 55.98]  Pusher.com.
[55.98 --> 56.40]  Pusher.com.
[56.40 --> 56.46]  Pusher.com.
[56.46 --> 58.86]  Welcome to The Change Log, episode 0.8.3.
[58.98 --> 59.90]  I'm Adam Stachowiak.
[60.16 --> 60.96]  And I'm Wynn Nethelen.
[61.18 --> 62.12]  This is The Change Log.
[62.18 --> 63.72]  We cover what's fresh and new in open source.
[64.18 --> 67.00]  If you found us on iTunes, we're also up on the web at thechangelog.com.
[67.22 --> 68.26]  We're also up on GitHub.
[68.60 --> 70.22]  You can head to github.com slash explore.
[70.30 --> 74.24]  You'll find some trending repos, some feature repos from our blog, as well as the audio podcast.
[74.60 --> 78.46]  And if you're on Twitter, follow The Change Log and me, Adam Stach.
[79.12 --> 81.20]  And I'm Penguin, P-E-N-G-W-I-N-N.
[81.60 --> 85.14]  Speaking of Explorer, you'll notice that there's no more player on Explorer.
[85.88 --> 91.02]  So the folks at GitHub, we've decided to remove the player from there to save a few kilobytes across the site.
[91.10 --> 92.72]  So I'm sure you'll appreciate that.
[92.72 --> 95.72]  So you have to link back to the website to listen to the episodes now.
[95.82 --> 96.66]  But no biggie.
[96.72 --> 97.28]  We're still there.
[97.74 --> 98.60]  Yeah, we're still there.
[99.42 --> 100.36]  Fun episode this week.
[100.36 --> 103.16]  We talked to Ruben Daniels from Cloud9.
[103.92 --> 110.84]  Got the scoop on some, what's the latest ACE developer tools in their Cloud9 suite?
[111.08 --> 113.18]  Man, you know, I'm so excited about what this is going to do.
[113.26 --> 116.70]  I think this is just, you know, an editor in the cloud.
[116.70 --> 123.52]  I mean, you as a Vim person, you must just love what this is going to do for just taking your environment anywhere.
[124.40 --> 124.78]  Be cool.
[124.96 --> 127.64]  It's going to take a while to get me off of text mode.
[127.76 --> 129.76]  I've got to tell you, I'm loving it more and more.
[129.76 --> 140.38]  But for those folks that want to just open up a browser and have their editor anywhere, it's amazing just the sheer feat of what they've done in the browser with Cloud9.
[140.82 --> 141.70]  I'm just amazed.
[142.16 --> 144.52]  It behaves like a native application in many ways.
[144.68 --> 149.42]  It kind of reminds me of whenever everybody was like in the enterprise trying to go to thin clients, right?
[149.44 --> 150.44]  It's kind of the same thing.
[150.54 --> 152.24]  Your dev environment isn't your local machine anymore.
[152.30 --> 152.98]  It's on the server.
[153.38 --> 155.00]  It's like pants, legs, width.
[155.00 --> 159.38]  We just, in the industry, keep oscillating back and forth between fat and thin clients.
[159.46 --> 159.90]  We sure do.
[159.90 --> 161.46]  It's like bootcut and skinny jeans, you know?
[161.52 --> 161.98]  That's true.
[162.66 --> 163.48]  It's a fun episode this week.
[163.52 --> 164.08]  Should we get to it?
[164.54 --> 165.18]  Let's do it.
[165.18 --> 178.08]  We're chatting today with Ruben Daniels and Matt Pardee from Cloud9.
[178.24 --> 180.08]  So why don't you guys introduce yourselves.
[180.20 --> 181.04]  Ruben, why don't you go first?
[182.20 --> 182.80]  So I'm Ruben.
[182.90 --> 185.92]  I'm the CEO and co-founder of Cloud9 IDE.
[186.82 --> 192.32]  And a developer myself, but today also doing all the stuff that CEOs do.
[192.32 --> 194.48]  And I'm Matt Pardee.
[194.74 --> 203.40]  I am the developer evangelist for Cloud9 and also a developer on the platform and wearer of many hats at Cloud9.
[204.12 --> 210.58]  We should mention you guys are co-workers with Tim Caswell, friend of the show that was on a couple of episodes back talking about Lua and Lovett.
[211.80 --> 216.26]  So for folks that don't know, I guess Cloud9, they've probably used it, might not even know it.
[216.30 --> 219.76]  It's the editor that powers the readme editor on GitHub.
[219.88 --> 220.18]  Is that right?
[221.10 --> 221.50]  Definitely.
[221.50 --> 224.38]  It's a very, very powerful editor.
[224.76 --> 229.48]  And we work together with Chris from GitHub to integrate it.
[229.80 --> 240.32]  And yeah, it's a multifunctional editor having all sorts of themes and everything from multi-selections to all sorts of strange language support.
[241.10 --> 244.32]  Let's talk a bit about your business and business model behind it.
[244.42 --> 249.14]  So Cloud9 is an open source editor, the IDE, but it also has a platform behind it.
[249.14 --> 249.52]  Is that right?
[250.44 --> 250.96]  That's correct.
[250.96 --> 256.78]  We decided that we wanted to make as much as we possibly could open source.
[257.34 --> 261.78]  So not only the editor is open source, but also actually the IDE application.
[262.32 --> 269.68]  And then the software that we use to manage and scale the platform itself, we kept close to provide the service.
[269.68 --> 270.50]  What sort of server architecture?
[270.50 --> 273.16]  What sort of server architecture are you employing?
[273.16 --> 281.94]  So it's a multi-tiered architecture where we have a proxy in the front that's dynamically scaled based on the need.
[281.94 --> 290.98]  We have a second layer, which is what we call IDE servers that do multi-user, multi-workspace servers that get the request from the proxy.
[291.56 --> 300.10]  And then behind that, we have another layer where people's code is run, actually, and all the things that they do on the console as well.
[300.10 --> 307.10]  So I didn't hear node in that, but I'm assuming it's a node server based on Tim's employment there.
[308.76 --> 309.58]  Everything's node.
[310.38 --> 310.60]  Yeah.
[310.60 --> 313.12]  All these different layers, each is node.
[314.14 --> 317.32]  Are you guys employing node in the build process for the IDE as well?
[318.38 --> 318.76]  Yeah.
[318.96 --> 320.56]  All the build scripts are in node.
[320.56 --> 324.10]  The connectors are in node.
[324.10 --> 335.28]  One of the cool things that we've been working on is this virtual file system layer that sits between the IDE server and the servers behind it.
[335.72 --> 345.18]  And this virtual file system allows the IDE server to connect over SSH to a node process that runs there and perform all sorts of tasks,
[345.18 --> 350.58]  like reading files, starting processes, doing file watching, and things like that.
[350.66 --> 352.86]  And VFS is actually open source on GitHub.
[353.52 --> 354.72]  So let's talk about that for a moment.
[354.72 --> 361.64]  The virtual file system, what sorts of file systems is it virtualizing, I guess is the question.
[362.06 --> 372.08]  So it virtualizes a local file system, and SSH is one of the things that we've been adding, and we'll add some more in the future.
[372.08 --> 377.72]  It's basically the start of a complete set of support for these things.
[378.00 --> 388.02]  I think we'll come out with some integrations with commercial services that have REST APIs for all their file access soon.
[388.74 --> 394.78]  Matt, is that your role to onboard, I guess, integration partners to figure out how they could latch onto the platform and extend it?
[394.78 --> 399.20]  Yeah, so we'll be ramping up that process later.
[399.20 --> 408.96]  But, yeah, I'll be working with making sure that our platform is ready for all developers to get on board with and that it makes sense.
[409.88 --> 418.26]  And it's kind of a new frontier for development and getting partners onto this kind of platform.
[418.26 --> 429.28]  And so we have to make it make sense and make sure people understand the workflow and how they can kind of latch into their existing services or technologies
[429.28 --> 434.72]  and really take advantage of this freedom and power of developing in the cloud.
[435.34 --> 437.90]  So, Ruben, some folks may be taking a double take.
[438.06 --> 442.22]  You've been on the show before in a previous incarnation of the brand, Ajax.org.
[442.22 --> 448.42]  Why don't you talk a bit about the transition between that brand and the new brand and if it involved a pivot at all?
[449.54 --> 451.98]  Well, yes, I mean, definitely.
[452.82 --> 458.76]  So, Ajax.org, we used when we were creating an Ajax framework, actually.
[459.22 --> 460.78]  So the name made sense.
[460.86 --> 461.76]  It was a little bit generic.
[462.04 --> 465.40]  But we created an open source framework to build UIs in the browser.
[466.26 --> 470.46]  And we thought it was a great framework, just not a great business.
[470.46 --> 474.38]  So at a certain point, we created the IDE with this framework.
[474.62 --> 482.14]  And we noticed that you can actually create a business building an IDE and support all the open source work that you're doing.
[482.54 --> 489.72]  And we raised a little bit of money from Excel, Excel Partners, a famous VC here in the Valley.
[490.80 --> 497.68]  So we had the funds as well to start going and doing this work on the IDE.
[497.68 --> 507.08]  So we pivoted the company, basically, going from building this UI framework to building an IDE and selling it as well online.
[508.50 --> 513.66]  So you guys had Ajax.org as the domain name for that previous incarnation.
[514.12 --> 516.70]  Hard to improve upon that, but you have with C9.io.
[516.88 --> 517.50]  Just notice that.
[517.58 --> 519.60]  That's a great short domain.
[519.60 --> 526.74]  Looking at the screenshots for Cloud 9 IDE, it looks a lot like Sublime or Google Chrome.
[526.90 --> 527.90]  This runs in the browser?
[529.10 --> 529.56]  Yeah.
[529.64 --> 532.96]  I mean, we definitely looked at Chrome for the tabs.
[534.02 --> 537.48]  And how Chrome deals with tabs is very, very cool.
[537.88 --> 538.96]  So we copied that.
[538.96 --> 545.54]  And there are also some aspects of Sublime that are very new and very interesting.
[545.92 --> 555.74]  And, you know, if somebody innovates on a certain type of interaction, it makes only sense to look at that and use this inspiration for your own.
[556.18 --> 560.20]  So we've done that with the new version of Cloud 9.
[560.52 --> 565.74]  You'll notice that there's a lot of things that were inspired by other things that are already pre-existing.
[565.74 --> 573.38]  So some of the things that are given in a text editor, keyboard shortcuts, syntax highlighting.
[573.62 --> 574.66]  Talk a bit about those features.
[575.54 --> 575.94]  Right.
[576.02 --> 578.34]  So, yeah, we spend a lot of time on those.
[578.50 --> 580.66]  People seem to be really, really passionate about it.
[580.96 --> 587.56]  And we get a lot of people supporting us with, you know, creating new syntax highlighters.
[587.92 --> 592.88]  And they're all, you know, issuing pull requests on Ace to do that.
[592.88 --> 599.02]  I think we have about 50 syntax highlighters now, somewhere there.
[600.08 --> 602.44]  And a lot of themes as well.
[602.96 --> 604.44]  They're really passionate about that too.
[605.28 --> 607.30]  And so are we actually.
[609.16 --> 612.62]  So what was the other part of your question again?
[612.74 --> 612.84]  Sorry.
[612.84 --> 617.66]  So the keyboard shortcuts, I noticed that you support both Vim and Emacs key bindings.
[617.76 --> 620.28]  How much of, how configurable is that?
[620.40 --> 623.62]  And did the browsers tend to get in the way in different platforms on some of those?
[623.88 --> 624.12]  Right.
[624.22 --> 625.24]  Yeah, that's been a challenge.
[625.66 --> 627.26]  The browsers do get in the way.
[627.40 --> 631.02]  You have to work around some of the shortcuts that you would otherwise choose.
[631.82 --> 634.78]  But overall, it's been doable.
[634.78 --> 642.60]  We've been able to be creative with key combinations to have the shortcuts that we want.
[643.14 --> 646.74]  There's a default set and then in D- and Emacs and Vim set.
[647.84 --> 654.10]  And generally, we build a system so that it's really, really easy to create these type of sets.
[654.36 --> 655.44]  And you can do that in a plugin.
[656.00 --> 661.04]  In the future, we'll also have a UI to set these type of key bindings.
[661.12 --> 663.74]  But right now, that's something that you can easily do in a plugin.
[663.74 --> 668.92]  I noticed the browser is telling me to unlock extra features by installing a Chrome extension.
[669.78 --> 671.54]  Is that how you get around some of those limitations?
[672.32 --> 680.08]  That's mostly for cut, copy, and paste via context menus, which is, you could say, an edge case,
[680.16 --> 681.84]  but still something that a lot of people do.
[681.96 --> 686.34]  And currently, if you don't have that plugin installed and you right-click and you do copy,
[686.72 --> 689.62]  it will only be available within that browser frame.
[689.62 --> 694.96]  If you go to another place outside that, you won't be able to paste that content.
[695.08 --> 698.08]  If you use command C or command V, you can.
[698.72 --> 700.94]  But with the context menu, you can't.
[701.30 --> 703.30]  So that unlocks that.
[703.30 --> 709.16]  I think everyone in the company had an aneurysm when they found out that you couldn't actually do that,
[709.40 --> 710.44]  that it wasn't available.
[712.42 --> 713.84]  But yeah, it's true.
[714.16 --> 719.96]  And I think there's probably some more features that will come out as browsers move along
[719.96 --> 724.60]  that we can integrate better by installing a Cloud9 plugin, so to speak,
[724.60 --> 730.74]  on a Chrome Web Store or other browser environments that are doing the same thing, like Mozilla.
[730.74 --> 737.12]  Yeah, what you really notice is that browser vendors are noticing that to build real applications
[737.12 --> 743.34]  with HTML5, CSS, the way to be the presentation of those applications,
[743.64 --> 746.20]  you need to integrate better with the operating system.
[746.20 --> 752.34]  And we notice that ourselves, being able to access the file system or start processes locally
[752.34 --> 757.22]  is essential for, in our case, the offline use case.
[758.10 --> 763.28]  So with this next release, which, you know...
[763.28 --> 764.66]  Will be out by the time this airs?
[764.78 --> 765.18]  Exactly.
[767.38 --> 773.58]  So with the new version of Cloud9, you're able to go offline when you want to.
[773.58 --> 777.58]  And the way that we've implemented that is that you download a small little node app
[777.58 --> 783.38]  that you run persistently on your computer, and it will automatically sync all your files
[783.38 --> 786.88]  from the cloud to local and from local to the cloud.
[787.20 --> 790.80]  So as soon as you're offline, the changes are saved locally,
[790.98 --> 794.16]  and the moment that you go online again, they're moved to the cloud.
[794.38 --> 799.96]  Now, this type of solution, we feel, should in the future just be very simple to code
[799.96 --> 800.82]  within the browser.
[800.82 --> 806.48]  And I know that many of the browser vendors are already working on these type of APIs
[806.48 --> 807.96]  to make that possible.
[808.74 --> 812.92]  So in the online scenario, do you have any multi-user features baked in
[812.92 --> 815.52]  where it would support a pairing scenario?
[816.44 --> 817.12]  Good question.
[818.32 --> 818.84]  Yes.
[819.00 --> 823.64]  And that's been our vision and, I think, the promise of an IDE in the cloud,
[823.90 --> 827.28]  to very, very easily work together in teams.
[827.28 --> 833.22]  And we are ourselves a company where, I think, in 10 countries or something like that,
[833.62 --> 834.58]  we have developers.
[835.04 --> 838.34]  And working together sometimes can be a little bit of a pain.
[838.88 --> 841.12]  Like, you're stuck with something that someone else built,
[841.28 --> 845.34]  and you're trying to get their help, but you have to do some screen sharing solution,
[845.54 --> 846.38]  and then you can type.
[846.38 --> 855.32]  So we tried to build a solution where you can do real-time collaborative editing on documents,
[855.86 --> 859.92]  multiple documents, and even your entire workspace in the cloud.
[860.06 --> 866.32]  So you'll just be able to go to Cloud9, copy the URL of the workspace that you're in,
[866.38 --> 867.86]  and then share it with someone else.
[867.86 --> 870.78]  And you can start typing, give that person read-write access.
[871.50 --> 878.84]  And they'll be able to not only type the code, but also run the program within your workspace.
[880.02 --> 884.18]  And what we even added is the ability to debug code together.
[884.30 --> 891.26]  So you can set a breakpoint, hit it, and both participants or multiple participants will see what's going on.
[891.26 --> 895.20]  And they can both step through, inspect variables, and these type of things.
[895.74 --> 901.18]  So we feel that that's a very, very new way of developing code for people that are remote.
[902.50 --> 906.22]  We've got a lot of code repository options baked in.
[906.36 --> 909.54]  GitHub, Bitbucket, Mercurial, even FTP.
[909.78 --> 914.76]  Hopefully nobody's still using that sort of live to save-to-live workflow.
[915.20 --> 916.24]  You'd be surprised.
[916.94 --> 918.56]  I know, I say that facetiously.
[918.56 --> 923.62]  Also, a lot of deployment options, Joanne, Heroku, some of the usual cloud suspects.
[924.40 --> 925.28]  What about CI?
[925.58 --> 928.04]  Is that still something that you would integrate in with your code repository?
[928.28 --> 931.62]  Or do you have any plans for continuous integration in with your editor?
[933.08 --> 941.42]  So let me answer that question first by talking about our test panel, which is something new.
[942.20 --> 946.46]  And the test panel allows people to very easily run all the tests within their project.
[946.46 --> 948.38]  And it's a very pluggable architecture.
[948.72 --> 952.16]  We're launching with just a way to run a node unit test.
[952.52 --> 956.80]  But we already have a plug-in for Selenium as well.
[956.96 --> 964.00]  So you can add all sorts of tests there that you can run automatically, even at every save or with some pattern that you specify.
[964.00 --> 968.82]  So what about support for pre-processing languages?
[969.08 --> 971.46]  Compass, SAS, even CoffeeScript.
[971.82 --> 981.54]  Looks like a lot of times in the front end it seems heavy to have to install a lot of tools and, I guess, dial tone to get those projects in place.
[981.62 --> 983.16]  That could just be baked into my editor.
[983.16 --> 985.62]  Yeah, so I'll talk about that.
[986.16 --> 993.64]  We worked on upgrading our console interface, which is built into Cloud9 at the bottom of the IDE.
[994.40 --> 1002.70]  And we enabled the ability to run NPM packages right from the terminal in the console.
[1002.70 --> 1018.24]  And we already actually allowed users to use NPM to install packages from npm.js.org right into their Cloud9 project, either locally or as a global NPM package.
[1018.96 --> 1029.90]  And now we built in the ability so that when you type in an NPM package such as Coffee, for instance, that it will go and search and find that package that you have installed.
[1030.50 --> 1032.02]  If it finds it, then it will run it.
[1032.02 --> 1037.18]  And if it has a standard input prompt, then you can actually interact with that.
[1037.46 --> 1056.26]  So this is great news for developers who work with Express and they want to scaffold a lot of applications or they work with Coffee and they want to either, you know, build their entire CoffeeScript project or just even interact with the REPL directly from the console.
[1056.26 --> 1060.22]  And so we give them a little prompt that indicates what process is running.
[1060.22 --> 1066.66]  And they can type in whatever CoffeeScript they want and get the feedback right away.
[1067.38 --> 1068.46]  And this is really great.
[1068.82 --> 1077.90]  Developers can kind of reconsider how they use NPM packages in general because it is now a part of their cloud development process.
[1077.90 --> 1084.70]  And so you can almost think of some of these packages as general software packages.
[1085.22 --> 1098.86]  You know, you can code your own NPM package to compile CoffeeScript or build different things and put it on npmjs.org and then install it in your Cloud9 application.
[1098.86 --> 1105.78]  And they have now over 10,000 packages out there that you can try on Cloud9.
[1105.78 --> 1113.26]  Many of them have the ability to be run from the command line and that's what we look for.
[1113.26 --> 1126.50]  So it's really exciting for people who do less and CoffeeScript development and so on and so forth because now the console can accommodate for those kinds of, for that kind of thing.
[1126.50 --> 1135.92]  So it sounds like CoffeeScript and Stylus and less would be supported pretty trivially, but some of the Ruby-based languages like Compass and SAS would be a bigger stretch.
[1135.92 --> 1136.92]  Yeah, exactly.
[1136.92 --> 1141.80]  So we do have to make some limitations about what you can install in a shared environment.
[1141.80 --> 1153.00]  But yeah, for the other things that come with NPM, then those usually can be run in a shared environment like we provide.
[1154.06 --> 1162.64]  So the nice thing with this new release is that we're giving everyone that's a premium user a full environment.
[1162.64 --> 1173.76]  So anybody that gets a premium account gets one environment in their workspace where they can just run any type of executable.
[1174.28 --> 1179.56]  And they get an individual environment per project that they create.
[1180.46 --> 1187.40]  So if they want to run Ruby or Python or PHP or anything really, they can just do that.
[1187.52 --> 1190.96]  And it runs completely isolated from any other project.
[1190.96 --> 1196.38]  So those security restrictions that we need to have on the shared environment are lifted.
[1196.66 --> 1204.46]  And we can run, we run Python in interactive mode and that just all works fine right from within the console of Cloud9.
[1205.24 --> 1208.36]  Any integration with services like GIST or PacePin?
[1209.28 --> 1212.96]  Not yet, but we definitely want to do that.
[1212.96 --> 1221.24]  And I think that that's something that we can do once we have sort of the basic workflows that we envision ready.
[1222.24 --> 1227.06]  So you guys are pretty excited about the release that just came out prior to this airing.
[1227.38 --> 1231.18]  What's on the roadmap of what you can talk about for the next six months?
[1231.18 --> 1237.34]  I think that one of the most important things is API stability.
[1238.46 --> 1254.26]  We've seen with Eclipse and Visual Basic and many of these other tools that the ecosystem, a lot of people just being able to change and create plugins for these type of IDEs is really, really important.
[1254.26 --> 1258.86]  And we have several hundred plugins right now for Cloud9.
[1259.56 --> 1266.18]  But to really be able to create durable plugins, you need to have a stable API and a well-documented API as well.
[1266.68 --> 1271.42]  So our goal for the next three months or so is to actually do that and build that.
[1271.86 --> 1279.22]  We already started with a lot of things that we've done with this release are to cater for that.
[1279.22 --> 1282.66]  One of those things is Architect, which is another open source library.
[1283.74 --> 1288.90]  And it's sort of, I think that Rick, our CTO, called it COM for JavaScript.
[1289.68 --> 1299.20]  But it's really a plugin system that's very, very generic and very nice and creates a loose coupling between different modules,
[1299.76 --> 1306.92]  having sort of a service-like architecture within, in this case, a node process.
[1306.92 --> 1312.38]  Having started my development career in the late 90s, COM for JavaScript might not be the best marketing slogan.
[1316.20 --> 1320.82]  It might not be the best marketing slogan, but it's at least a way to understand what it is.
[1323.26 --> 1324.88]  Let's talk about the anatomy of a plugin.
[1325.40 --> 1328.48]  Is it purely client-side code that plugs into the open source IDE?
[1328.72 --> 1334.24]  Or do you have anything like the equivalent of a Heroku add-on that would be a server-side addition as well?
[1334.24 --> 1340.22]  So currently, actually, Architect only runs on the server.
[1341.20 --> 1345.58]  And our work for the next month or so is to get it on the client as well.
[1345.64 --> 1348.14]  So we have the same architecture on the client in the server.
[1348.22 --> 1351.08]  And that's something that we can do because we run JavaScript on both ends.
[1351.08 --> 1359.34]  And a plugin is a very simple module with only a couple of calls to initialize it.
[1360.00 --> 1364.32]  And it can ask for or request other services.
[1364.48 --> 1368.80]  And those services will implement a certain API, which it can then use.
[1371.52 --> 1373.90]  Matt, maybe you can elaborate a little bit more on this.
[1373.90 --> 1379.24]  Yeah, so I got my feet wet with Architect recently.
[1379.76 --> 1386.58]  And it's a wonderfully elegant, simple solution for any level node application that you want to build.
[1387.16 --> 1395.34]  And it happened to suit our needs for Cloud9 because we wanted this idea of isolation and reusability.
[1395.34 --> 1402.52]  And, you know, when I started working with Architect after it had kind of been created, I was really blown away.
[1402.64 --> 1404.98]  You can start from a really simple foundation.
[1406.20 --> 1411.50]  And, for instance, if you wanted to create the kind of, you know, proverbial to-do application,
[1412.20 --> 1420.10]  you might have a database module and a, you know, an HTTP module to actually serve the web page.
[1420.10 --> 1429.94]  And then you may even have an authentication module because you only want certain people to access the application and or access the database, rather.
[1430.90 --> 1437.38]  And what Architect allows you to do is allows you to put those three separate modules into each one of their components
[1437.38 --> 1443.66]  and then add to a pool of resources by registering themselves and saying,
[1443.86 --> 1445.70]  this is what I'm providing to the rest of the world.
[1445.70 --> 1449.52]  And then every other module can say, this is what I want to consume.
[1450.50 --> 1458.70]  And so the HTTP module might only need to interact with the authentication module to allow people to access the web page.
[1459.04 --> 1463.08]  And then there might be a separate controller that will access the database.
[1463.66 --> 1469.26]  The great thing about it is that it simplifies the process, but it also makes it so that you don't have to really consider your application
[1469.26 --> 1476.68]  as starting from a web-based interface and then going back to the authentication interface
[1476.68 --> 1478.68]  and then going back to the database interface.
[1479.22 --> 1483.14]  You can consider all of these things as part of one big pool.
[1484.12 --> 1490.12]  And so it may be a little bit of a tweak on people's mental models of how an application works,
[1490.12 --> 1495.56]  but once you actually start working with it, you realize that it frees your mind to think of other possibilities
[1495.56 --> 1499.32]  so that if you have another part of your application that wants to use the database,
[1499.86 --> 1502.94]  it's already available for you if you just ask for it.
[1503.42 --> 1508.28]  And it might seem trivial or just like a basic idea, but when you just say,
[1508.42 --> 1512.40]  I want to have this database that already exists over here, then you can use that.
[1512.52 --> 1518.22]  And even better, you can then use that database module as part of another application really effortlessly.
[1518.22 --> 1523.84]  You don't have to cut and paste different parts of your scripts or application code.
[1524.48 --> 1528.06]  You can just take it out and put it back into something else.
[1528.24 --> 1534.16]  And we even facilitate that process by making it so you can separate these different components
[1534.16 --> 1540.32]  into either a plugin that exists as part of your application or you can even install it via NPM.
[1541.24 --> 1547.98]  And so we even have different components like we've created an HTTP module called Architect HTTP.
[1548.22 --> 1550.46]  that I believe is available on NPM.
[1550.92 --> 1554.66]  And so when you download this application, you know, Architect from GitHub,
[1554.76 --> 1560.06]  and we have some examples that go along with it, you can just do NPM install on one of the demos,
[1560.54 --> 1564.92]  and it will install the needed plugins from NPM directly.
[1564.92 --> 1570.42]  So it makes your entire, not even your application scale really easily,
[1570.42 --> 1576.24]  but it also makes the process of developing your application scale really well as well so that everyone else can,
[1576.38 --> 1581.46]  you know, work on different components and update those components as needed.
[1581.88 --> 1592.42]  I think that one of the limitations that we found just using the basic require system is that we couldn't easily use and test only parts of the system.
[1592.42 --> 1597.00]  And so that's one thing that this system provides.
[1597.46 --> 1602.42]  Another thing is that it also allows for out-of-process parts.
[1603.34 --> 1611.14]  So I could take a plugin and run it out of process and still use the same way of communicating between them.
[1611.14 --> 1613.88]  And I think that that can be very powerful.
[1613.88 --> 1621.48]  You, of course, have to be very careful with that and make sure that the plugins that you do that with are architected for this type of behavior.
[1621.48 --> 1629.10]  So, yeah, we're really excited about architect and using that both on the server and the client.
[1629.90 --> 1639.64]  And what we are looking to sort of evolve Cloud9 into in the next couple of months is an environment where it's really easy to develop these types of plugins,
[1639.64 --> 1653.44]  try them out and start and stop them without having to restart the server and then also being able to provide a way to easily get them running in a secure way on the online platform.
[1653.44 --> 1656.72]  Let's talk about the average workflow for a moment.
[1656.86 --> 1666.00]  So signing into Cloud9, if I authenticate with GitHub, then I see all my public repos, I guess private repos as well.
[1667.12 --> 1671.78]  And then if I click on one of those to get started, I have to clone that to the Cloud9 servers.
[1671.82 --> 1672.20]  Is that right?
[1673.06 --> 1673.84]  Yeah, that's correct.
[1673.84 --> 1680.28]  And then as I make changes or invite other people to collaborate on that project, how do changes get upstream back to GitHub?
[1681.20 --> 1685.30]  So there's the command line that we touched upon a little while ago.
[1685.48 --> 1698.00]  And you can type git commit or git push, and that will commit back to your origin, which will be your GitHub repository somewhere else.
[1698.38 --> 1702.00]  So essentially when you clone, it sets it up as a remote here on Cloud9?
[1702.52 --> 1702.92]  Yes.
[1702.92 --> 1704.12]  The origin is still back at GitHub?
[1704.54 --> 1705.36]  Yeah, definitely.
[1707.30 --> 1709.88]  It's a really nice command line console at the bottom of the screen.
[1710.02 --> 1718.74]  This is one of those things that normally web-based editors make massive trade-offs, but this seems to, I guess, combine the best of both worlds.
[1719.46 --> 1727.96]  That's what we're trying to do, and we've had people being really enthusiastic about not having to change windows, but just having that all in one UI.
[1727.96 --> 1731.12]  And there are all sorts of shortcuts to switch easily.
[1731.12 --> 1737.90]  Shift-Esc, we'll go to the console, control, escape, we'll open up the output.
[1737.90 --> 1742.64]  So it's a very nice way to work generally.
[1742.64 --> 1743.16]  Yeah.
[1743.16 --> 1752.36]  So one of the common features in editors is what Microsoft calls IntelliSense and code completion and Xcode.
[1752.50 --> 1753.52]  You guys have anything like that?
[1753.52 --> 1760.28]  I think that this feature is the most requested feature by our users.
[1760.28 --> 1767.00]  I mean, we have 120,000 users now, and we often ask them, what would you like?
[1767.00 --> 1777.22]  And this type of solution offers a way to very quickly type things without having to know what the APIs are exactly.
[1777.72 --> 1780.10]  So we spent a lot of time on building that.
[1780.20 --> 1786.56]  In the past few months, we hired some very intelligent guys that got their PhD in this area.
[1786.56 --> 1799.38]  And they built a solution for JavaScript that I think can match the solution that exists out there for Java and other strongly typed languages.
[1799.70 --> 1806.02]  But they managed to do it for the weekly type JavaScript using another open source project of ours called Treehugger.
[1806.02 --> 1818.12]  Treehugger allows you to query code with a query language, very similar to you have query languages for databases or XML.
[1818.38 --> 1831.82]  But in this case, you query code and you can match code based on its structure, its so-called AST, rather than just the characters that are there.
[1831.82 --> 1838.86]  So we use that, and that will be available for many other languages later on.
[1838.96 --> 1845.48]  But right now, it's there for JavaScript, and we have Node.js documentation support in there as well.
[1846.14 --> 1851.50]  So that means that when you want to try out some Node.js calls and you don't remember what they're like,
[1851.54 --> 1858.80]  you just type in the first letters or just type alt space or control space, and you get help in articulation immediately.
[1858.80 --> 1867.98]  Just from a consumer perspective, it seems like a lot of IDEs are tied to the platform for which they're developing,
[1868.50 --> 1873.06]  Visual Studio for Microsoft and Xcode for Coco and the Apple platforms.
[1873.70 --> 1880.04]  It appears that if you had somewhere where you could pick off customers at the fringe,
[1880.08 --> 1883.86]  it would be in the Eclipse market, a market that you're going after.
[1883.86 --> 1893.56]  So Eclipse, I think, is mostly catered towards Java, and it's indeed a very big group of developers.
[1894.52 --> 1902.44]  But outside of Vim, just my own observations, it appears that Eclipse has the most try-to-be-all-things-to-all-people approach.
[1903.34 --> 1903.98]  Right, right.
[1903.98 --> 1911.12]  I think that there's value in being specific and providing tools for certain environments.
[1911.88 --> 1918.08]  And I don't think that a lot of script languages or dynamic languages have good IDEs.
[1918.84 --> 1928.80]  So there are a lot of people now that are using text editors with these basic, basic forms of autocomplete or other tools,
[1929.62 --> 1931.42]  and they don't know any better.
[1931.42 --> 1941.34]  So what we're trying to do with Cloud9 is provide the richness that people in the Java and .NET community know they can have from their IDE
[1941.34 --> 1944.94]  and provide that for the people that are writing in these script languages.
[1945.52 --> 1946.42]  And it is possible.
[1946.66 --> 1948.44]  So that's our focus right now.
[1948.72 --> 1955.86]  But on the longer term, we'll definitely also support those bigger languages.
[1957.34 --> 1960.74]  Regular listeners know that we normally end with a few questions.
[1960.74 --> 1962.84]  One of those is, what's your text editor?
[1963.00 --> 1964.24]  I think I know the answer to that one.
[1964.96 --> 1967.46]  So let me ask you, Matt, first, who's your programming hero?
[1968.70 --> 1970.16]  Oh, man, that's a good question.
[1971.34 --> 1975.14]  You know, I'm going to say Linus Torvalds.
[1975.14 --> 1986.78]  And the reason is because I think that he's often misunderstood in the way that he responds to developers
[1986.78 --> 1989.28]  and what we see a lot of times online.
[1990.32 --> 1997.34]  But I have to say the deeper that I go into Git, because I'm a Mac guy and I don't use Linux,
[1997.34 --> 2003.46]  so the more I go into Git, the more profound respect I have for what he did there.
[2003.88 --> 2008.68]  And I'm not the type of guy who adds up what a programmer did over his lifetime,
[2008.90 --> 2013.08]  and it's kind of just still relevant to me that I use Git every day.
[2013.08 --> 2023.10]  So, you know, my answer might be a little bit more short-sighted than some of the giants in the programming history books.
[2023.40 --> 2027.96]  But I really have a lot of respect for the thinking that he did on Git
[2027.96 --> 2033.30]  and how one person's idea like that can impact millions of developers.
[2033.30 --> 2042.56]  And I think Git is great, and obviously what Linux has done for everyone else in the world is also pretty incredible.
[2042.98 --> 2044.76]  So, yeah, I'll go with Linus.
[2045.66 --> 2046.20]  What about you, Reuben?
[2049.22 --> 2050.18]  Good question.
[2053.20 --> 2055.50]  I crowdsourced this question right now.
[2056.86 --> 2058.94]  People don't have an answer.
[2059.62 --> 2061.08]  Are you doing a phone-a-friend on Twitter?
[2061.08 --> 2064.52]  I'm using Skype.
[2068.82 --> 2070.32]  Can I have a different question?
[2070.86 --> 2073.66]  You can email it to me, and I can put it in the show notes.
[2074.76 --> 2075.12]  Okay.
[2075.80 --> 2076.16]  All right.
[2076.30 --> 2076.76]  I'll do that.
[2077.86 --> 2078.14]  Cool.
[2078.28 --> 2079.40]  Well, nice work, guys.
[2079.46 --> 2082.34]  It's a great editor, and it's a great platform that you guys are building,
[2082.34 --> 2086.10]  and I look forward to where you guys take it in the next few months.
[2086.96 --> 2087.92]  Thank you very much, Wyn.
[2088.20 --> 2089.50]  It's great being on your show,
[2089.50 --> 2092.72]  and I'd love to have everyone try it out on C9 Antonio.
[2093.16 --> 2093.82]  Yeah, thanks, Wyn.
[2093.82 --> 2123.80]  We'll see you next time.
