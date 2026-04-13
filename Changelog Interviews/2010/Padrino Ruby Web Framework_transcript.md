[0.00 --> 2.96]  Hi, this is Rick Olson, and you're listening to the ChangeLog Podcast.
[18.14 --> 21.82]  Welcome to the ChangeLog, episode 0.2.7.
[22.06 --> 23.30]  I'm Adam Stokowiak.
[23.54 --> 24.44]  And I am Wendelin.
[24.62 --> 25.68]  This is the ChangeLog.
[25.90 --> 27.92]  We cover what's fresh and new in the world of open source.
[27.92 --> 31.36]  If you found us on iTunes, we're also on the web at thechangelog.com.
[31.58 --> 32.48]  And we're also up on GitHub.
[33.04 --> 35.06]  Yep, head to github.com forward slash explore.
[35.16 --> 39.04]  You'll find some training repos, some feature repos from our blog, as well as our audio podcasts.
[39.40 --> 41.90]  And if you're on Twitter, follow ChangeLogShow.
[42.08 --> 43.36]  And I'm Adam Stok.
[43.82 --> 46.22]  And I am Penguin, P-E-N-G-W-Y-N-N.
[46.64 --> 48.24]  Back to Ruby this episode.
[48.50 --> 52.44]  Taking a hiatus from some of the JavaScript coverage to talk with the Padrino team.
[52.72 --> 53.60]  Yeah, it was awesome.
[54.18 --> 57.60]  Yeah, Padrino is a cool, lightweight framework built on top of Sinatra.
[57.60 --> 61.14]  Kind of like Rails Lite or Sinatra Plus, however you want to see it.
[61.60 --> 63.24]  I wonder why they didn't call that Sinatra Moore.
[64.14 --> 66.32]  That was the original, I guess, gem behind it.
[66.64 --> 67.96]  Padrino is Godfather.
[68.84 --> 70.94]  So I think it's a take on the whole Sinatra name.
[71.06 --> 71.98]  Yeah, it fits.
[72.08 --> 72.52]  It fits.
[72.72 --> 73.18]  It does fit.
[73.24 --> 74.30]  It's a classy little framework.
[74.50 --> 76.12]  I think it fits the Sinatra vibe.
[76.60 --> 78.18]  I've been having fun with it on a couple of projects.
[78.76 --> 80.20]  I'm excited about what it offers, too.
[80.20 --> 86.58]  All this expandability without the complexity of engines and subprojects.
[86.74 --> 87.56]  And what a mess.
[87.98 --> 94.20]  Yeah, and usually when you bite off a Sinatra application, it seems like there's times when you miss a couple of things from Rails.
[94.36 --> 95.68]  And I haven't found that with Padrino yet.
[96.46 --> 96.96]  Fun episode.
[97.06 --> 97.66]  Should we get to it?
[97.92 --> 98.58]  Let's do it.
[98.58 --> 107.90]  All righty.
[107.96 --> 115.74]  We're joined today by Arthur Chu and Nathan Eskenazi, two of the brains behind Padrino RB, new Ruby Web Framework.
[116.24 --> 119.98]  Arthur, why don't you give us a little background on yourself and your role on the team?
[121.02 --> 121.22]  Hi.
[121.40 --> 122.66]  Well, my name is Arthur Chu.
[122.66 --> 124.32]  I'm a recent UCI graduate.
[124.60 --> 127.96]  Currently working at a company called Stuck Pixel in Newport Beach.
[128.58 --> 131.08]  I'm one of the main core developers of Padrino.
[132.04 --> 133.52]  Yeah, and I'm Nathan.
[133.86 --> 136.00]  I also recently graduated from UCI.
[136.54 --> 142.52]  I've been working for startups and doing various entrepreneurial type things since I was in high school, actually.
[143.04 --> 145.28]  And I've been using Ruby for two years.
[146.22 --> 148.02]  Recently, I started using Sinatra a lot.
[148.36 --> 150.82]  And so I'm also one of the core developers of Padrino.
[151.42 --> 156.36]  I focus primarily on the core gem and also the helper's gem.
[156.96 --> 157.40]  Cool.
[157.40 --> 162.36]  Before we dive into the project, why don't you give us an idea of how big the team is and where you're located?
[163.18 --> 163.36]  Sure.
[163.48 --> 166.16]  So there's actually six of us now on the core team.
[167.00 --> 169.24]  And it started out – it's kind of interesting.
[169.36 --> 172.38]  It started out with – I built this gem called Sinatra Moore.
[172.94 --> 175.74]  And it was actually just me and Arthur working on that originally.
[175.74 --> 179.98]  And then we were joined – the third core team member was this guy in Italy.
[180.70 --> 184.72]  And he actually loved it so much that he became a really passionate contributor.
[185.40 --> 187.90]  And we converted Sinatra Moore over to Padrino.
[188.58 --> 190.22]  And so it was just the three of us for a while.
[190.38 --> 192.50]  And then three more added on.
[192.52 --> 193.46]  Just recently, actually.
[193.46 --> 199.82]  Just very recently, we have Joshua, the guy who created Usher, which is – so that was great.
[200.14 --> 204.40]  Lori Holden, who's – she used to be a MIRB core team member.
[204.78 --> 208.10]  And now she's going to be helping us with the routing and the tests for Padrino.
[208.10 --> 217.38]  And finally, we have Skade Florian Gilcher, who is just another very, very talented Sinatra developer.
[217.84 --> 222.10]  He found us early on and we added him to the project because he was so interested in helping contribute.
[222.74 --> 222.86]  And –
[222.86 --> 226.46]  I believe he's also one of the main guys for the German Ruby group.
[226.76 --> 227.14]  That's right.
[227.26 --> 230.44]  And so we've actually – we're actually located different places.
[230.54 --> 231.60]  Me and Arthur are in Irvine.
[232.34 --> 233.26]  David's in –
[233.26 --> 233.50]  Italy.
[233.50 --> 233.78]  Italy.
[233.96 --> 237.46]  And then I believe that Joshua right now is –
[237.46 --> 238.08]  Canada, Toronto.
[238.54 --> 238.88]  Toronto.
[239.20 --> 241.06]  And Lori's out in Colorado, too, as well.
[241.20 --> 242.22]  So we're a distributed team.
[242.68 --> 245.70]  Well, that definitely explains why the IRC channel is so well-manned.
[246.10 --> 249.74]  No matter what time of day I'm in there, it's just like 30 people in the IRC.
[249.92 --> 250.12]  Yeah.
[250.12 --> 251.84]  It's funny because it's actually perfect.
[252.08 --> 254.74]  Right when I'm going to bed, David is waking up and going to work.
[254.98 --> 257.92]  So the second I'm off the IRC, David's in there helping people.
[258.02 --> 260.62]  And then when he leaves, he tags me back in and I'm back.
[260.68 --> 261.60]  So it's kind of convenient.
[262.36 --> 265.96]  So usually the first question that comes up when I'm talking about Padrino,
[265.96 --> 268.66]  because Adam and I are big fans, is why Padrino?
[269.04 --> 269.76]  We've got Sinatra.
[269.98 --> 271.10]  We've got Rameis.
[271.20 --> 272.06]  We've got Rails.
[272.52 --> 274.72]  Why Padrino in this day and age?
[275.24 --> 275.36]  Yeah.
[275.54 --> 277.16]  Well, that's an excellent question, actually.
[277.48 --> 282.06]  And that's something, obviously, that comes up right away very often whenever we're talking
[282.06 --> 283.46]  to people about Padrino.
[283.92 --> 288.64]  And the simplest answer is that we never actually set out to create a framework originally.
[289.18 --> 291.92]  We were all just really big Sinatra fans, to be honest.
[291.92 --> 294.90]  I mean, I used Rails a lot, and Arthur used Rails.
[295.06 --> 300.28]  And we always felt like there was something very enticing about the Sinatra philosophies.
[300.64 --> 300.76]  Yeah.
[300.84 --> 301.80]  It actually, it's a funny thing.
[301.92 --> 303.42]  It started with Nathan and I.
[303.48 --> 305.92]  We were actually working on a little pet project before.
[306.72 --> 308.34]  And then we wanted to try something different.
[308.56 --> 311.40]  And then instead of just using Rails, we decided, like, hey, let's give Sinatra a go.
[311.84 --> 315.50]  And then Nathan suggested, you know, like, there's a lot of things from Rails that we did miss a lot.
[315.50 --> 320.66]  And Sinatra being as bare bone as it is, like, we wanted to bring some of those extra functionality back.
[321.10 --> 323.32]  And that's sort of what led us to this point now.
[323.74 --> 323.82]  Right.
[323.96 --> 326.16]  So, I mean, what happened was, essentially, we started with Sinatra.
[326.42 --> 327.22]  We were loving it.
[327.42 --> 330.02]  We were both using it for all our projects as best we could.
[330.28 --> 334.78]  And I just kept running into the same, let's say, you know, six pain points over and over again.
[334.98 --> 336.22]  I needed helpers.
[336.48 --> 337.52]  I needed form builders.
[337.52 --> 344.12]  I needed a reloader for the development that wasn't shotgun so that it didn't reload the entire thing every time.
[344.22 --> 345.90]  I wanted, like, more intelligent reloading.
[346.40 --> 348.54]  I wanted a mailer that was integrated.
[348.98 --> 356.16]  There was just a number of things that, basically, I loved Sinatra, but I just couldn't, I just kept having to rebuild into each project.
[356.68 --> 363.32]  And so, as we started to notice that, we were like, hey, you know, it would make sense for us to take these things, extract them out of our projects,
[363.32 --> 370.26]  and sort of create, like, a combination, a comprehensive set of these extensions that we need for every project.
[370.38 --> 371.44]  Hence the name Sinatra Moore.
[371.50 --> 371.64]  Yeah.
[371.70 --> 373.86]  And so, originally, we actually didn't plan to make a framework.
[374.18 --> 378.82]  We were looking simply to create sort of like, it's almost like Merb Core, Merb Moore.
[378.92 --> 380.46]  We imagined Sinatra was Sinatra Core.
[380.64 --> 383.72]  And we loved it because it was one file, you know, implementation.
[384.10 --> 384.58]  It was thin.
[384.64 --> 385.28]  It was lightweight.
[385.46 --> 390.58]  And then Sinatra Moore would be additional features on top of Sinatra for people who needed them.
[390.98 --> 392.46]  And so, we always viewed it like that.
[392.46 --> 396.48]  Even to this day, to be honest, I don't really view Padrino as an entirely new framework.
[396.78 --> 404.86]  I view it as a sort of a natural extension to what Sinatra already could do, but to give it a little more power and a little more flexibility.
[405.60 --> 411.98]  And I think people can see that very quickly when they start using Sinatra, that there are just some great things from Rails that you're going to miss.
[412.52 --> 421.30]  And so, that's what we were trying to do with Padrino is just give people those things by default instead of having to have them hunt it down, you know, all the individual extensions to get those things.
[421.30 --> 421.66]  Exactly.
[421.66 --> 427.80]  We still want to keep the whole elegance of Sinatra, yet at the same time still provide some of the, at least the powers and features that Rails provided.
[428.10 --> 429.68]  So, I mean, that's what gave birth to Padrino.
[430.24 --> 430.34]  Yeah.
[430.66 --> 435.62]  You know, one of the things that I was pleasantly surprised about was that it's still Sinatra under the hood.
[436.02 --> 441.90]  So, if you're in a Padrino app and you have a code sample from Sinatra, 90% of it still applies.
[442.02 --> 443.58]  I mean, it's still Sinatra.
[443.58 --> 445.32]  Yeah, that's absolutely right.
[445.38 --> 460.74]  And it even goes a little one step further, which is something I had mentioned in a blog post I had recently, which is that not only is it just Sinatra, but since everything we have is a superset of Sinatra, you can follow the Sinatra tutorials using Padrino and you won't run into almost anything that would break it.
[460.74 --> 463.44]  I mean, all the routing still works the same way that you learned.
[463.90 --> 465.56]  All the basic features are still there.
[465.88 --> 469.54]  There's nothing that we take from Sinatra and we say, oh, that's not going to work.
[469.54 --> 476.82]  All we do is we take Sinatra, we leave it there, and we just extend it naturally with more powerful features on top.
[477.30 --> 480.94]  And so, when you're working with Padrino, you really are working with Sinatra.
[481.24 --> 482.20]  I mean, they're synonymous.
[482.66 --> 484.20]  And you can still use Sinatra extensions.
[484.76 --> 486.58]  You can still use all the same rack middleware.
[487.56 --> 488.94]  This is really the great thing about Padrino.
[489.04 --> 490.54]  We did not reinvent the wheel at all.
[490.80 --> 496.68]  We simply provided extensions and tools on top of the existing foundation that we loved with Sinatra.
[496.68 --> 508.72]  You know, web development and desktop development 10 years ago, we were touting these components and how there was going to be this marketplace where you get these reusable parts like they exist in the real world in manufacturing, right?
[509.28 --> 515.10]  One of the things that I love about Padrino is that since it's still Sinatra, it still has this rack heritage under the hood.
[515.22 --> 522.92]  You can mix and match rack middleware to build your application, but also you can mount other Padrino applications in the subdirectory.
[522.92 --> 526.94]  Talk a bit about how you can stack Padrino apps on top of each other.
[527.96 --> 536.00]  So, yeah, this is actually a great part of Padrino is that we built it from the beginning to be a little more Django-esque in a few ways.
[536.36 --> 539.10]  And I'll talk about the one that you just mentioned, the mounting of apps.
[539.44 --> 541.74]  I always liked the idea of MIRB slices.
[541.90 --> 542.76]  They were interesting.
[543.04 --> 544.84]  And I liked the idea of the Rails engines.
[544.84 --> 552.94]  But the problem that we saw was I didn't really understand why we couldn't just have true mountable apps, which is something Django has for Python.
[553.46 --> 561.72]  And so I was very interested in exploring early on whether we could create truly isolated mountable applications in Padrino.
[561.84 --> 564.14]  And that's exactly what we ended up being able to do.
[564.14 --> 571.98]  So with Padrino, you can actually, when you generate an application, you're actually generating a project, kind of like similar to the Python-esque idea.
[572.36 --> 574.88]  And a project can contain any number of sub-applications.
[575.16 --> 580.92]  Each application can have models, views, controllers, separated namespaces, different components.
[581.48 --> 584.68]  And they'll all be mounted separately on sub-URIs.
[584.82 --> 587.82]  And this will all run from the single Padrino project.
[588.46 --> 591.52]  This is a great, this is very nice being able to stack applications.
[591.52 --> 600.40]  And then on top of that, if you take middleware, which we're big fans of, anytime we can, rather than building a Padrino extension, we'll look to build a rack middleware.
[600.64 --> 607.86]  Because we're a big believer in sort of creating agnostic things, not tying people down to a particular component or framework.
[608.40 --> 612.46]  So we're very interested in allowing you to stack middlewares to create functionality.
[612.46 --> 620.90]  And then on top of that, mount applications so that you can really keep your applications lightweight and sort of separate your concerns.
[620.90 --> 622.20]  Definitely keep it very clean, too.
[622.36 --> 622.50]  Yeah.
[623.10 --> 629.26]  So those are really important pieces of the thought process going into the beginnings of Padrino.
[629.88 --> 639.02]  We were really curious to see how difficult it would be to create true mountable apps rather than sort of pseudo apps, the way that Rails engines worked.
[639.40 --> 640.78]  And we came pretty close.
[640.78 --> 647.70]  I was actually fairly pleased with the progress we've made so far that we're going to continue to make towards 1.0.
[647.70 --> 647.74]  Yeah.
[648.22 --> 654.66]  I think the average Ruby web developer probably doesn't leverage middleware as much as he should or she should.
[656.00 --> 661.82]  Mention some of your favorite middleware rack applications that you like to use.
[662.68 --> 667.94]  I think, well, there's a rack recapture that I use at work right now.
[668.42 --> 671.22]  It just pretty much allows you to use a recapture inside your app.
[671.22 --> 673.62]  And we actually have a few, actually.
[674.24 --> 679.52]  For 9.12, we have a template feature that allows you to just easily generate plugins.
[679.70 --> 685.58]  And then we use a lot of rack apps in there that just pretty much sets it all up for you into your Padrino application.
[685.78 --> 688.28]  So it just configures everything out of the box for you.
[688.98 --> 690.34]  But in terms of through rack app.
[690.34 --> 693.94]  Yeah, I mean, there are a wide array of rack middlewares.
[694.36 --> 699.80]  And I would actually really, like you were saying, a lot of Ruby developers right now don't take full advantage of these.
[699.92 --> 712.50]  But you would actually be, I mean, people would really be surprised to see how many awesome pluggable middlewares there are that can really expand the functionality of your application in a great way that doesn't require any additional complexity in your own code.
[712.50 --> 715.84]  I mean, one example is this thing called, I found recently, rack bundle.
[716.30 --> 720.36]  And what rack bundle does is it's sort of like asset bundler for Rails.
[720.56 --> 724.84]  But what it does is it's a middleware that will actually take all your JavaScript and CSS files.
[725.30 --> 731.80]  And it can minimize them and it will rewrite to have a single compressed JavaScript and a single compressed CSS.
[732.26 --> 733.60]  But it will do that at the rack level.
[733.88 --> 737.90]  And it doesn't require a single change in your application level code.
[738.24 --> 739.10]  So that's just one example.
[739.20 --> 740.92]  I mean, there is a lot of great middlewares.
[740.92 --> 744.82]  Another one I've been using recently and it's pretty cool too is Rack OmniAuth.
[745.16 --> 748.80]  It allows you to do just authentication through either Facebook or off to and Twitter.
[748.98 --> 753.76]  And it makes it really clean and really easy just to implement it right into your application right away.
[754.10 --> 758.26]  And it also comes with other features for Basecamp and other ones like Google.
[758.78 --> 761.88]  And they have a couple other ones that I can't list off the top of my head.
[762.06 --> 763.24]  But, I mean, it's pretty great.
[763.36 --> 770.68]  I mean, coderack.org is a great site to take a look at for a list of pretty comprehensive rack apps they can use and even GitHub itself.
[770.68 --> 773.60]  So, yeah, I mean, I encourage other developers to check it out.
[773.80 --> 773.94]  Yeah.
[774.02 --> 784.20]  And as we mentioned, but I would like to restate because it's pretty interesting, is for .9, .12, we're actually going to – we recognize that a lot of people aren't familiar with middleware to the level that they should be.
[784.20 --> 785.90]  So we're actually going to create a plug-in system.
[786.46 --> 791.64]  So people could, for instance, write Padrino Gen Plugin Hop Toad, for instance.
[791.88 --> 799.16]  And we'll automatically download and configure the Rack Hop Toad middleware for people so they don't have to learn how to configure that themselves.
[799.16 --> 806.12]  And so we have this idea with Padrino is we really want people to be able to use whatever they want, but we want to make it extremely easy and integrated for them to do it.
[806.40 --> 813.78]  And so we have agnostic generators, which we haven't talked about too much yet, but we also are going to have these sort of cherry-pickable plug-ins.
[814.24 --> 815.56]  And they're not like Rails plug-ins.
[815.74 --> 820.66]  They just insert Rack Middlewares and sort of existing libraries into your app and configure them for you.
[820.66 --> 824.90]  Yeah, it's actually leverages store a lot, so it just pretty much just writes a code inside your app for you.
[825.28 --> 827.88]  If you guys want to take a look at it, it's actually on GitHub.
[828.12 --> 830.18]  It's Padrino Recipes, Padrino-recipes.
[830.64 --> 836.76]  It's a list of a couple of plug-ins that we've already made so far that allows you to just instantly just drop these plug-ins right into your project.
[837.42 --> 840.18]  Are these available on Edge or are these live today?
[842.12 --> 843.54]  They're on a branch right now on Edge.
[843.78 --> 845.96]  Yeah, right now they're actually on a separate branch.
[845.96 --> 852.44]  We're still sort of fine-tuning some of the tests and sort of fixing some of the bugs.
[852.68 --> 856.04]  So it's not going to be in our next release, but it's going to be in the one after that.
[856.28 --> 857.76]  But we've already started building a library.
[857.88 --> 860.54]  We have, I think, 15 or 20 almost already.
[861.38 --> 865.80]  Different plug-ins for everything from HopToad to ReCAPTCHA to CarrierWave.
[865.88 --> 866.48]  RackBug.
[866.70 --> 866.90]  Yeah.
[867.10 --> 868.00]  A lot of RackHunt drives.
[868.00 --> 873.20]  So that's going to be a big feature in, let's say, the next couple of releases.
[873.20 --> 877.20]  So let's back up a minute and talk about the agnosticism and the generators.
[877.46 --> 884.28]  So one of the cool selling points for Padrino was when you generate your project, you can specify your ORM layer.
[884.40 --> 889.64]  You can specify your JavaScript libraries, your style sheet and templating libraries.
[890.54 --> 893.68]  What's the full gamut of support that you guys have in that area?
[893.68 --> 901.74]  Well, we support mocks, scripts, testing frameworks, ORMs, and stylesheet engines.
[901.74 --> 903.52]  Oh, stylesheet engines and also renderers as well.
[903.64 --> 911.70]  What we did when we first built Padrino is we took a look at all of the different things that you even can choose when you're building an application in Ruby.
[912.44 --> 913.90]  I mean, we basically made a list.
[914.02 --> 920.68]  I mean, there's obviously the easy ones, persistence and mock, but there's also the more nuanced ones like SAS or less support for stylesheets.
[920.68 --> 929.90]  And so we made a list of these and we made a list of the components we had used that we actually thought were sort of the most common, the most popular components.
[930.50 --> 940.50]  And so what we did was we have generators that essentially support any of these popular components for anything from persistence engines to test frameworks.
[940.50 --> 946.84]  And the best part of it is that we really worked hard on was that it's actually fully integrated with the rest of your generators.
[947.22 --> 952.00]  So for instance, let's say you choose ActiveRecord for your ORM.
[952.52 --> 953.58]  We don't leave you hanging.
[953.70 --> 957.14]  We actually provide you all of the necessary tasks to develop with ActiveRecord.
[957.40 --> 960.00]  If you generate a model, it'll be generated with ActiveRecord.
[960.10 --> 963.84]  If you generate a model test, it'll be done in the testing framework that you specified.
[963.84 --> 975.40]  So throughout the entire development cycle, we fully integrated each of the components so that you don't even have to, you know, you don't have to at any point copy and paste boilerplate code.
[975.52 --> 976.70]  We've done all that for you.
[976.78 --> 977.80]  It's built right into the generator.
[978.12 --> 984.68]  This was an important point when we were building Padrino because especially with Sinatra, everyone is opinionated and they're opinionated differently.
[985.14 --> 989.42]  So one person is going to swear by S-C-Q-U-E-L, SQL ORM.
[989.58 --> 990.90]  Some people are going to swear by Data Mapper.
[990.90 --> 993.00]  Some people are going to love Mongo ID.
[993.74 --> 1002.08]  And we didn't want to go down the Rails route of sort of being very strict on giving suggestions.
[1002.26 --> 1004.14]  We wanted to go almost the exact opposite route.
[1004.36 --> 1012.48]  We wanted to make using any of these extremely easy, but we wanted to give you the choice to use any of the ones that you wanted at your discretion, not ours.
[1012.56 --> 1014.14]  So that was important when we were building it.
[1014.14 --> 1021.90]  Yeah, and also in most of the generation, like we include a couple comments to show you like extra little features that you can use with like these different components that you like to choose.
[1022.02 --> 1032.10]  So we definitely make it very easy for users to come in and quickly see like some of the basic commands you can use with these either ORMs or maybe testing frameworks and just a basic setup for them to use.
[1032.10 --> 1038.56]  In addition, not just models, admin or admin gem as well is fully integrated with the generators.
[1038.82 --> 1048.20]  So if you made something with Data Mapper, the admin sees that right away and just generates an account model based on the ORM you choose and just pretty much all seamlessly work together.
[1048.20 --> 1051.30]  So what exactly is the sweet spot for this?
[1051.40 --> 1055.90]  I mean, you mentioned earlier how it's more like package like projects.
[1056.28 --> 1061.62]  And I know in Rails projects, you often want to throw out an application and you also have something else you want to put underneath it.
[1061.70 --> 1066.10]  But you run into problems with like engines and sub projects and stuff like that.
[1066.22 --> 1069.26]  Why this versus, you know, doing that in Rails?
[1069.36 --> 1072.34]  Why did you choose the projects kind of route and what's the sweet spot for it?
[1072.34 --> 1083.90]  Well, I would say we primarily chose the projects route because I'm a big believer and I think our team in general is a big believer in keeping things very separated and sort of focused.
[1084.34 --> 1092.82]  So rather than having one large app, I love this idea of building lots of smaller apps that are well tested and work in isolation.
[1092.82 --> 1096.64]  It's the same modular philosophy that exists just in general in programming.
[1096.64 --> 1115.86]  And so rather than having, let's say, one huge application that deals with authentication, authorization, you know, pictures, uploading, blog, everything, we were very interested in allowing you to use middleware to do the authentication, middleware to do authorization, create an app for the blog, create an app for the forum, create an app for your primary application.
[1116.24 --> 1122.08]  Keep things very, very separated, very easily testable and isolated from each other, you know, so there's not a lot of coupling.
[1122.08 --> 1124.98]  So that was our primary reason for doing that.
[1125.04 --> 1130.68]  And also, I've done some Python development myself and I think also some of the other team members have.
[1131.06 --> 1141.90]  And personally, I just really enjoyed the sort of the setup that you get with Django where you can easily, let's say, someone builds a blog and I want to use it.
[1141.94 --> 1145.12]  I can just take that blog app and stick it right into my existing project.
[1145.44 --> 1146.38]  No questions asked.
[1146.80 --> 1150.20]  I have all the assets, everything I need, all the models.
[1150.20 --> 1157.72]  And it's just, it's very nice to be able to have that type of separation and control over each individual application.
[1157.96 --> 1163.24]  So that's sort of where the original thought process for the project structure came from.
[1164.34 --> 1167.06]  So Padrino, Italian for Godfather, correct?
[1167.68 --> 1168.06]  That's right.
[1168.06 --> 1168.24]  Yep.
[1168.94 --> 1174.06]  So let's talk about Sinatra and the Padrino, the Sinatra heritage that Padrino shares.
[1174.22 --> 1179.14]  We've interviewed Aaron Quint from the SammyJS project that borrowed a lot of ideas from Sinatra.
[1179.90 --> 1185.16]  How, I guess, revolutionary has Sinatra been to web development?
[1185.16 --> 1191.44]  Well, I guess, especially in Ruby development, it's definitely brought the learning curve down a lot.
[1191.92 --> 1199.76]  For most people that just started getting into Ruby and definitely into Rails, there's just always that big curve to just understand how to just develop in Rails.
[1200.10 --> 1203.28]  And with Sinatra, it makes it pretty much plain and simple.
[1203.38 --> 1208.48]  You just have a, you have an HTTP verb and a block and it just makes it really clear for you to see what's going on.
[1208.48 --> 1218.46]  And whereas Rails, you need to understand a lot of the magic behind it, like how the generators work, where everything belongs, and just a lot of nitty-gritty details that most people, like, when they start, can't pick up right away.
[1218.90 --> 1220.68]  And that's why I really appreciate Sinatra.
[1220.86 --> 1221.56]  It's really simple.
[1221.92 --> 1226.22]  One RV file and you can already have a little tiny web app going, like, right off the bat.
[1226.74 --> 1226.86]  Yeah.
[1226.96 --> 1231.14]  I'm a big believer also just in principle, in sort of graduated complexity.
[1231.54 --> 1235.86]  The idea that when you start out building an app, it should be really dead simple.
[1235.86 --> 1239.88]  If I want to create an app that just says, hello world, I should be able to do that in five lines of code.
[1240.02 --> 1248.88]  There's no need to have, you know, 80 files, a routes file, generate a controller if all I want to do is print, you know, hello world or some basic JSON to the screen.
[1249.22 --> 1258.10]  And the reason I like graduated complexity in particular is I think, as Arthur touched on, the learning curve is extremely important when you're doing web development.
[1258.10 --> 1266.44]  Whenever I try to teach people Rails or Ruby application development, they always run into all these hurdles because they have to learn, like, 30 sort of metal models at once in a sense.
[1267.00 --> 1268.44]  And so I love Sinatra.
[1269.10 --> 1275.18]  Even though I was already fairly proficient at Rails, when I went to Sinatra, it was like a breath of fresh air for me personally.
[1275.34 --> 1277.74]  I mean, you know, the DSL was extremely simple.
[1278.24 --> 1280.54]  You know, five lines of code could generate a web server.
[1281.08 --> 1285.64]  The whole philosophy was agnostic and very lightweight.
[1285.64 --> 1289.26]  It was extremely fast as far as performance numbers when I benchmarked.
[1289.56 --> 1292.66]  There was just something very, very right about the foundation with Sinatra.
[1293.62 --> 1296.52]  And so I just fell in love with it right from the get-go.
[1296.96 --> 1302.60]  And, you know, I would have Rails apps and I would be working on consulting jobs and I would need to build an app.
[1302.70 --> 1306.66]  And I knew I should have used Rails because it was a much better fit.
[1306.82 --> 1313.32]  But I would find myself trying to find a way to use Sinatra because for some reason it just felt more fun.
[1313.38 --> 1314.26]  It felt more natural.
[1314.26 --> 1318.72]  And so, yeah, for me, the graduated complexity is huge.
[1318.84 --> 1321.26]  I mean, I love this idea with Sinatra and now Padrino.
[1321.68 --> 1323.84]  You know, you can come in with no Ruby experience whatsoever.
[1324.26 --> 1328.78]  You read the Sinatra book and you could be building basic web applications within a couple days.
[1329.10 --> 1330.88]  I mean, within a day you can build Hello World.
[1330.98 --> 1333.64]  But within three or four days you could probably build a basic web service.
[1333.64 --> 1349.24]  And then with Padrino now being a natural extension of Sinatra, you can take all that Sinatra knowledge and you can start cherry picking Padrino knowledge and you can continue to build on a very, very sort of gradual process towards building arbitrarily large applications.
[1349.24 --> 1352.12]  And that's something that just isn't really possible with Rails.
[1352.52 --> 1356.24]  I mean, you could learn, let's say, Rack, then learn Sinatra, then learn Rails.
[1356.34 --> 1359.66]  But each time you have to sort of discard existing knowledge and start again.
[1360.00 --> 1364.50]  Whereas with this, you can build everything from Hello World to the most complex e-commerce site.
[1364.82 --> 1369.18]  And you're still using the same foundation with Sinatra and then on top of that, Padrino.
[1369.18 --> 1372.96]  So for me, that's the most revolutionary part of Sinatra.
[1373.88 --> 1375.16]  So what are you guys building with Padrino?
[1376.34 --> 1380.86]  For the time being, I mean, we're kind of both working for different companies, building different things.
[1381.00 --> 1381.52]  Do you want to start our thing?
[1381.52 --> 1386.92]  Yeah, actually, I think for me, I'm actually building a couple of sites for this company called StockPixel.
[1387.02 --> 1388.06]  They do mobile app development.
[1388.22 --> 1394.00]  So I'm actually converting a lot of their mobile apps on the iPhone and Android into websites.
[1394.20 --> 1396.22]  So that's what I'm currently doing with Padrino right now.
[1396.22 --> 1401.32]  Yeah, so I work for a company, as I said, it's a small company.
[1401.66 --> 1408.66]  And I have a main application, which is actually still in Rails because it's very large and I haven't had time to convert it yet.
[1408.82 --> 1414.84]  But I have a lot of web services that I'm building on the side to interact with various components, JSON, XML components.
[1416.66 --> 1418.20]  And those I've all built in Padrino.
[1418.76 --> 1421.64]  I have contract work that I do on the side, too, freelancing.
[1422.04 --> 1423.56]  I build all of those sites in Padrino.
[1423.56 --> 1430.18]  David, who's in Italy, he actually runs his own consulting firm called Lipsy Soft.
[1430.74 --> 1435.98]  And he has a team, I think, of something like 10 or 15 people, from what I understand.
[1436.24 --> 1437.46]  And they build –
[1437.46 --> 1439.36]  They run a few e-commerce sites, actually.
[1439.40 --> 1443.02]  They actually run – I think they built already 15, 20 apps in Padrino for their clients.
[1443.60 --> 1444.90]  So we all do different things with it.
[1444.90 --> 1451.20]  But honestly, I mean, it's pretty – between Sinatra and Padrino, you can pretty much build any web application that you need.
[1451.58 --> 1459.62]  So, yeah, I mean, I have yet to run into anything that I was building where I was like, oh, Padrino isn't going to work for that.
[1459.68 --> 1465.08]  Because, like I said, it's very, very modular, but it extends all the way up to an arbitrary level of complexity.
[1465.08 --> 1473.30]  So I've actually really been enjoying sort of the conversion from using Rails for my apps to using Padrino for my apps.
[1473.30 --> 1475.46]  Yeah, I'd have to agree with that.
[1475.66 --> 1483.82]  So at one point, Adam and I were kicking around the idea of using Graham Ashton's Nesta CMS that's built on top of Sinatra for the changelog blog.
[1483.92 --> 1485.64]  We've since decided to stay on Tumblr.
[1485.76 --> 1488.70]  But I wanted to give it a go for my own personal blog.
[1488.90 --> 1496.22]  And just to extend a Sinatra app that's kind of outgrown the one-file architecture is kind of painful.
[1496.22 --> 1501.90]  So just as an intellectual exercise, I ported Nesta over to Padrino, called it Presto.
[1502.06 --> 1503.22]  And I'm actually loving it.
[1503.30 --> 1510.96]  I mean, it's one of those things where it's a joy, again, to dive down into a web application and just have it be that configurable and that extensible.
[1511.98 --> 1517.74]  Yeah, I mean, an example of eating our own dog food, we have a Padrino website, padrinorb.com.
[1517.94 --> 1521.12]  And obviously, right from the get-go, we knew we were going to use Padrino to build that.
[1521.12 --> 1526.86]  But I was actually, to be honest, even surprised as I was building it, because we were building it during some of the earlier stages of Padrino,
[1527.16 --> 1531.64]  how actually fun and easy it was to build this site, because it's actually fairly complex.
[1531.64 --> 1539.92]  I mean, it's actually a full CMS, and it's a full blog, and it has tags, and it has a full back-end for managing the content and everything.
[1539.92 --> 1542.92]  And it was actually really a pleasure to build.
[1543.52 --> 1547.18]  You know, me, Arthur, and David worked on that for a long time.
[1547.26 --> 1553.78]  And it was actually one of the first ways that we really stress-tested and polished Padrino was through our own Padrino website.
[1554.24 --> 1555.44]  And that's actually open source.
[1555.54 --> 1560.32]  It's actually available through the Padrino GitHub account right now, Padrino website.
[1560.32 --> 1565.70]  And so you can actually download that and modify it if people are interested in seeing sort of a real Padrino app.
[1566.56 --> 1571.62]  But yeah, I found during building that, I mean, at the time, we found things we needed to add, obviously.
[1572.12 --> 1577.80]  But, you know, during the process of building that website, now that it's relatively complete, you know, Padrino has been rounded out.
[1577.80 --> 1592.96]  And I really – I had a lot of fun building it, and that was actually part of the reason why I was so committed to continuing development of Padrino was because there was something qualitatively different, the experience that I had developing that website from some of the Rails apps I'd done before.
[1593.08 --> 1596.06]  It was just – something about it was just a little more fun, a little more relaxed.
[1596.78 --> 1598.78]  And yeah, so it was just for me personally –
[1598.78 --> 1599.56]  It's a realm of happiness.
[1600.12 --> 1601.04]  Exactly, just like Ruby.
[1601.84 --> 1602.16]  Awesome.
[1602.62 --> 1605.12]  So this is about the point where we ask our radar question.
[1605.12 --> 1606.38]  So what's on your open source radar?
[1606.44 --> 1610.96]  What's out there that you're just dying to play with, I guess, inside or outside the Padrino world?
[1612.40 --> 1615.74]  There's actually a lot of interesting things out there that I'm looking to play with right now.
[1615.88 --> 1619.38]  There's one, Node.js, Express.js, I think.
[1619.86 --> 1622.48]  That's the one that's a Sinatra clone for Node.js.
[1622.58 --> 1623.36]  That looks pretty interesting.
[1623.82 --> 1624.82]  Definitely want to try that out sometime.
[1625.86 --> 1626.98]  Yeah, that's really interesting.
[1627.12 --> 1633.60]  Another one I'm really interested in is that the framework Bowline, which is – it's pretty amazing, actually.
[1633.60 --> 1635.12]  I'm very interested in starting to play with it.
[1635.20 --> 1638.80]  It allows you to use HTML and CSS to develop desktop applications.
[1639.32 --> 1640.16]  But they look native.
[1640.28 --> 1642.58]  It uses WX widgets under the covers.
[1643.28 --> 1648.80]  And so that was very interesting to me because I've actually always had sort of a pet project,
[1649.06 --> 1652.56]  sort of a hobby of doing desktop applications in various languages.
[1652.80 --> 1654.18]  And I play with WX Ruby.
[1654.32 --> 1655.36]  I play with Shoes.
[1655.36 --> 1660.14]  I do mostly web development professionally, but it's always been fun to play around with these things.
[1660.38 --> 1666.40]  And now that I can use Bowline to develop desktop applications that look native,
[1666.60 --> 1671.38]  but I can write them in HTML and CSS, that opens up a whole new world of possibilities there.
[1671.78 --> 1673.16]  So that's been really interesting to me.
[1673.60 --> 1678.84]  And in particular, in the Padrino-related world, I'm very, very interested in –
[1678.84 --> 1683.12]  we've been playing a lot with MongoDB, which is, I guess, that new now,
[1683.16 --> 1685.12]  but it's starting to get more established, I guess, in a sense.
[1685.18 --> 1688.50]  But it's still kind of a newcomer as far as the database world goes.
[1688.62 --> 1693.78]  And I've been having a lot of fun doing most of my new sites in MongoDB
[1693.78 --> 1696.46]  and then MongoID for the ORM layer.
[1696.94 --> 1698.56]  And that's actually fully supported by Padrino.
[1699.52 --> 1701.12]  And that's been really interesting to me, too.
[1701.12 --> 1703.48]  You guys also support MongoMapper out of the box, right?
[1703.78 --> 1704.38]  That's right.
[1704.54 --> 1707.20]  Yeah, we support a pretty good array now of different things.
[1707.20 --> 1711.52]  And we're actually working on support for various other ones, Cassandra, Riek.
[1712.44 --> 1715.60]  Just to add on to that, I mean, we also have a page on our Padrino site
[1715.60 --> 1718.98]  that shows how to make or add components onto Padrino itself.
[1719.26 --> 1720.50]  So it's fairly easy.
[1720.66 --> 1724.24]  So people out there that want to contribute, like maybe an ORM or a script
[1724.24 --> 1726.66]  or some other component that they would like that they don't see in Padrino,
[1726.92 --> 1728.78]  we make it fairly easy for them to add it themselves
[1728.78 --> 1731.42]  and then just send a pull request and we'll definitely pull it in.
[1731.80 --> 1735.28]  Yeah, I mean, we have essentially step-by-step guides for how to build in anything
[1735.28 --> 1738.58]  from the ORM layer to a new testing framework.
[1738.80 --> 1740.04]  Or even just translations, too.
[1740.60 --> 1740.76]  Right.
[1741.26 --> 1743.32]  So yeah, it's a very open-ended question.
[1743.52 --> 1745.22]  There's a lot of awesome open-source stuff out there.
[1746.32 --> 1749.92]  And unfortunately, I wish there was more time in the day to play with them all.
[1750.98 --> 1754.78]  So where are you guys going to be where folks can catch up with you in person?
[1754.96 --> 1756.18]  What about the Padrino Roadshow?
[1756.18 --> 1760.20]  What talks are you guys going to be giving on the framework?
[1761.60 --> 1764.10]  Well, recently me and Nathan went out to OC Ruby.
[1764.46 --> 1766.62]  We're probably going to check out LA Ruby.
[1766.88 --> 1772.22]  And I think June 22nd, I'm going to be going to LA Web Dev.
[1772.90 --> 1773.74]  It's somewhere in LA.
[1774.28 --> 1777.20]  Yeah, so we're staying local right now for us.
[1777.34 --> 1778.18]  And I believe that there's a...
[1779.24 --> 1781.16]  We're hoping to get some of the other core team members
[1781.16 --> 1785.00]  to be able to do sort of their local ones as well.
[1785.08 --> 1789.94]  And I'm hoping once we hit 1.0 or maybe next year for, let's say,
[1790.00 --> 1791.36]  RailsConf or next year's RubyConf,
[1791.42 --> 1792.72]  I don't know where Padrino will be, hopefully,
[1793.36 --> 1795.12]  in a really good state at that point.
[1795.36 --> 1799.24]  I would love to start to consider to be able to start to present
[1799.24 --> 1801.36]  at sort of larger venues.
[1801.72 --> 1802.88]  That would be really interesting to me.
[1802.88 --> 1805.88]  But if I remember correctly, I mean, you guys could probably cut Josh
[1805.88 --> 1807.58]  going to Lone Star, I think.
[1808.28 --> 1809.46]  I'm not too sure about that.
[1809.78 --> 1810.56]  Yeah, we'll definitely be there.
[1810.56 --> 1813.28]  We're media sponsors for Lone Star since it's in our backyard.
[1814.12 --> 1815.76]  Yeah, so I think Josh submitted a talk,
[1815.86 --> 1819.70]  but I'm not actually sure if he ended up committing to doing that.
[1819.86 --> 1824.24]  But yeah, we're definitely interested in getting Padrino out
[1824.24 --> 1825.74]  in any way that we can.
[1825.82 --> 1827.66]  Hopefully, we can start speaking at more conferences in the future.
[1829.14 --> 1829.82]  Well, nice work.
[1829.82 --> 1834.24]  It's definitely a fun framework with all the buzz around Rails 3.
[1835.22 --> 1838.52]  Rails 3 does not equal the Ruby web development community,
[1838.72 --> 1840.30]  and Padrino is definitely worth a look.
[1840.98 --> 1841.60]  Well, thanks, guys.
[1841.66 --> 1842.14]  Appreciate it.
[1842.20 --> 1842.72]  I know it's late.
[1843.04 --> 1843.82]  Actually, it's early for you.
[1843.88 --> 1844.72]  It's late for us.
[1844.88 --> 1846.08]  Normally, we're talking to Europe.
[1846.94 --> 1847.50]  That's right.
[1847.76 --> 1849.02]  Well, thanks for joining us this evening.
[1849.32 --> 1849.62]  Of course.
[1849.78 --> 1850.06]  Thank you.
[1850.14 --> 1850.86]  It's been great to be on.
[1850.94 --> 1851.56]  Thanks for having us.
[1851.56 --> 1860.76]  Thank you for listening to this edition of The Change Log.
[1861.88 --> 1865.44]  Point your browser to tale.thechangelog.com
[1865.44 --> 1868.54]  to find out what's going on right now in open source.
[1869.82 --> 1873.02]  Also, be sure to head to github.com forward slash explore
[1873.02 --> 1875.26]  to catch up on trending and feature repos
[1875.26 --> 1878.30]  as well as the latest episodes of The Change Log.
[1878.30 --> 1883.08]  Safe in your arms
[1883.08 --> 1886.76]  As a dark passion show
[1886.76 --> 1891.22]  Was mine alone
[1891.22 --> 1896.84]  Open, open
[1896.84 --> 1901.14]  For us to try
[1901.14 --> 1902.80]  Bring it back
[1902.80 --> 1904.10]  Bring it back
[1904.10 --> 1907.72]  To our ground
[1907.72 --> 1908.90]  Open
[1908.90 --> 1914.24]  For us to try
[1914.24 --> 1915.80]  Bring it back
[1915.80 --> 1917.44]  To our ground
[1917.44 --> 1918.16]  If
[1918.16 --> 1918.62]  For us to try
[1918.68 --> 1931.66]  This
[1931.66 --> 1932.20]  Will
[1932.20 --> 1932.32] вин
[1932.32 --> 1932.54] ficient
[1932.54 --> 1933.08]  The
[1933.08 --> 1933.54]  Will
[1933.54 --> 1934.30]  Fall
[1934.36 --> 1934.58] ably
[1934.64 --> 1935.22]  Your
[1935.22 --> 1936.50]  Family
[1936.50 --> 1937.32] п
[1937.40 --> 1938.24]  Fil
[1938.24 --> 1938.58]  I
[1938.58 --> 1940.84]  Will
[1942.06 --> 1944.40]  Or
