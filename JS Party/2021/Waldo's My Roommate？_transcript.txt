[0.00 --> 6.90]  The struggle here is we wanted to build something that met a need that we had on the Preact team,
[7.02 --> 10.54]  which was like, Preact is tiny, and it's really good if you want to do a lightweight project.
[10.78 --> 12.58]  So where's our tooling for that?
[13.34 --> 16.58]  Where is our, you know, we have a webpack-based tool that's like, you know,
[16.58 --> 20.18]  used in production by a bunch of high-profile sites, but that's the heavyweight tool, right?
[20.20 --> 21.14]  Where's the prototyping tool?
[21.88 --> 22.94]  So that was the one hand.
[22.94 --> 28.76]  But then the other hand is myself and a bunch of others who just sort of happen to be on the Preact team.
[29.34 --> 33.88]  We've been kind of on the sidelines in the bundler ecosystem for a little while,
[34.22 --> 39.10]  you know, prodding people, kind of trying to get consensus on a direction that we can move in
[39.10 --> 44.70]  to further this idea of like writing modern code and shipping modern code and getting these things right.
[47.52 --> 50.14]  Bandwidth for Change Log is provided by Fastly.
[50.14 --> 52.34]  Learn more at Fastly.com.
[52.58 --> 54.84]  Our feature flags are powered by LaunchDarkly.
[55.14 --> 56.94]  Check them out at LaunchDarkly.com.
[56.94 --> 59.18]  And we're hosted on Leno cloud servers.
[59.44 --> 62.92]  Get $100 in hosting credit at Leno.com slash Change Log.
[62.92 --> 65.12]  What's up, JS Party people?
[65.24 --> 70.00]  Have you ever wondered if you could be offering a faster, less buggy experience for your customers?
[70.46 --> 75.22]  Well, with Raygun Error and Performance Monitoring, you have all the information you need at your
[75.22 --> 80.46]  fingertips to quickly find and fix errors and performance issues across your tech stack down
[80.46 --> 81.24]  to the line of code.
[81.54 --> 85.30]  Raygun makes it easy to monitor the impact of your performance improvements, quickly identify
[85.30 --> 90.04]  issues across web and mobile apps, and see how your code performs in the hands of your customers.
[90.04 --> 94.12]  This saves you time, this saves you money, and this saves your sanity.
[94.46 --> 99.08]  Head to Raygun.com to join thousands of customer-centric software teams who use Raygun every single day.
[99.40 --> 103.26]  Again, Raygun.com to give them a try with a free 14-day trial.
[103.26 --> 123.56]  Welcome, everyone.
[123.90 --> 129.04]  You're listening to JS Party, a weekly celebration of JavaScript and the web.
[129.04 --> 134.94]  We are giving away two free tickets to the Test.js Summit on January 28th and 29th.
[135.02 --> 138.08]  All you have to do is follow us on Twitter to be entered to win.
[138.20 --> 139.94]  We are at jspartyfm.
[140.12 --> 142.00]  Follow that account now before you forget.
[142.58 --> 144.04]  We have an excellent show for you today.
[144.16 --> 146.82]  If I do say so myself, let's get right into it.
[146.86 --> 148.26]  Hey, it's party time, y'all.
[148.26 --> 159.58]  Hello out there.
[159.72 --> 160.98]  Welcome to JS Party.
[161.10 --> 161.70]  It's 2021.
[162.30 --> 162.98]  We are here.
[163.08 --> 163.46]  I'm Jared.
[163.54 --> 164.86]  I'm your internet friend.
[164.86 --> 170.46]  And I'm joined as not always, but as often by one of my internet friends, Nick Neesey is in the house.
[170.52 --> 170.94]  What's up, Nick?
[171.48 --> 172.02]  Ahoy hoy.
[172.50 --> 173.60]  Ahoy hoy to you.
[173.76 --> 174.30]  Ahoy hoy.
[174.30 --> 178.72]  We are joined by a special guest today, Jason Miller.
[179.04 --> 181.10]  You may know him as DevelopIt.
[181.26 --> 181.60]  Hello.
[181.98 --> 184.12]  He is making the web faster at Google.
[184.32 --> 185.76]  He's the creator of Preact.
[186.04 --> 187.50]  JS, the P very important there.
[188.16 --> 189.46]  And he's on the podcast.
[189.76 --> 190.36]  So welcome, Jason.
[190.74 --> 191.00]  Hi.
[191.44 --> 192.42]  I'm happy to be here.
[192.84 --> 193.90]  We're very happy to have you.
[194.02 --> 196.14]  And we are happy to talk about your new thing.
[196.30 --> 200.96]  We'll talk about Preact, I guess, by proxy because it's involved in WMR.
[200.96 --> 203.78]  But Preact was not what prompted the call.
[204.08 --> 205.12]  WMR is.
[206.20 --> 216.60]  And WMR is a cool, tiny little all-in-one development tool for modern web apps, which brings a question to my mind, which I'll ask in a second.
[216.98 --> 218.90]  But the first question before I go.
[218.90 --> 220.30]  I know what that question's going to be.
[220.30 --> 224.44]  Well, I got two questions queued up, so I guess you can guess which one's which.
[224.50 --> 227.38]  The first one is, what does WMR stand for?
[227.50 --> 232.68]  And I know that that's not controversial, but it's like ambiguous because you're not really sure yet.
[232.72 --> 234.12]  You've got some multiple things going on.
[234.16 --> 236.28]  Tell us what WMR stands for, Jason.
[236.70 --> 239.98]  Yeah, I can never remember what the team decided on.
[240.62 --> 242.30]  To say it was an argument would be a miscategorization.
[242.30 --> 249.26]  It's more, you know, the NPM header, how they scroll through random definitions of what NPM might mean.
[249.62 --> 253.26]  We essentially just have a joke where we continue to do that in our chat.
[254.00 --> 262.46]  So I think like the dry, boring version is originally I started this project as a joke.
[262.46 --> 272.68]  And the joke was it was going to be called warm module replacement, which is like less hot than hot module replacement.
[274.08 --> 276.40]  Like it's a module replacement that you can touch.
[276.56 --> 276.96]  I don't know.
[277.14 --> 279.20]  It seemed funny at the time.
[279.52 --> 280.80]  And the NPM name was free.
[280.98 --> 286.40]  And then we spent a week or two trying to come up with a better name and failed.
[286.40 --> 291.02]  And so we called the company Apple or we called the project WMR.
[292.46 --> 294.76]  You know, this is probably something that we can help out with.
[295.98 --> 296.38]  Yeah.
[296.48 --> 297.78]  So like there's a lot of funny ones.
[297.88 --> 301.04]  I forget the one there's like wet module replacement.
[301.52 --> 301.78]  Okay.
[301.80 --> 308.36]  Or somebody suggested web modules runtime, which that feels kind of reasonable.
[308.66 --> 309.04]  Right.
[309.12 --> 310.00]  That one's almost too normal.
[310.48 --> 312.94]  So here's what we did, Jason.
[312.94 --> 321.36]  We saw this conundrum and we're fans of the NPM scrolling title or not scrolling, but, you know, random acronym replacement.
[321.36 --> 323.22]  And so we thought we'd help you out.
[323.30 --> 329.80]  We assembled a crack team of marketers and came up with some alternate replacements for you.
[329.86 --> 331.52]  So we're going to pitch you a few.
[331.66 --> 332.74]  You let us know if you like these.
[333.34 --> 335.28]  The first one is Windows me returns.
[337.80 --> 338.88]  Yeah, I would take that.
[339.02 --> 339.58]  That's a good one.
[340.30 --> 341.64]  Whales meet rodents.
[342.28 --> 342.60]  Okay.
[342.78 --> 343.80]  Doesn't make any sense at all.
[344.02 --> 345.80]  Well, what's the there's a program language.
[345.92 --> 346.42]  It's a rodent.
[346.56 --> 347.02]  The go.
[347.58 --> 348.28]  That's a gopher.
[348.58 --> 349.60]  And a gopher is a rodent.
[349.66 --> 351.52]  So I think you're I think you're on point there.
[351.58 --> 351.70]  Yeah.
[352.12 --> 354.16]  If a gopher is a rodent or is it a type of.
[354.86 --> 355.30]  I don't know.
[355.38 --> 356.56]  I do believe it is.
[356.64 --> 359.56]  If a capybara is a rodent, then a gopher is definitely a rodent.
[359.88 --> 362.56]  I think they are both of the rodentia family.
[362.96 --> 364.12]  I know nothing about science.
[364.12 --> 365.10]  I know that's gone.
[365.86 --> 366.88]  I got big teeth.
[367.14 --> 367.34]  I don't know.
[367.34 --> 367.90]  It's the genus.
[368.04 --> 368.84]  It's the or a phylum.
[369.00 --> 369.44]  I don't know.
[369.62 --> 370.32]  I don't know what's going on.
[370.38 --> 371.94]  Is it a platypus or is it not a platypus?
[372.06 --> 372.88]  That's all we care about.
[372.88 --> 374.62]  A couple other ones for you.
[374.84 --> 377.08]  WMR wicked Mr. Renderer.
[377.38 --> 378.14]  Yeah, I like that.
[378.22 --> 378.70]  I like that one.
[378.88 --> 383.22]  We tried a recursive acronym in the style of genus, not Unix, but it didn't work out at
[383.22 --> 383.46]  all.
[383.74 --> 386.56]  Windows or WMR means reboot.
[386.76 --> 388.72]  See, it doesn't even finish it.
[390.24 --> 391.26]  Where's my Roomba?
[392.22 --> 392.62]  Yeah.
[392.98 --> 396.98]  So that would make sense because when I Googled this after we created and launched the project,
[396.98 --> 400.44]  I was seeing if we had gotten any form of notoriety.
[401.06 --> 401.14]  Yeah.
[401.18 --> 406.42]  Apparently WMR was already a thing that I wasn't aware of called Where's My Refund, which is
[406.42 --> 408.12]  like a service offered by the IRS.
[408.82 --> 409.22]  Oh, wow.
[409.26 --> 409.52]  Yeah.
[409.60 --> 411.92]  I'm not American, so I didn't know that.
[412.02 --> 413.42]  It's like your tax returns or something?
[413.96 --> 414.22]  Yeah.
[414.48 --> 414.62]  So.
[415.42 --> 415.76]  Okay.
[415.86 --> 417.42]  Well, the last one, this one is yours, Nick.
[417.60 --> 418.68]  Waldo's my roommate.
[421.28 --> 422.84]  Do you actually have a roommate named Waldo?
[422.92 --> 425.16]  That actually answers the question also, where's Waldo?
[425.44 --> 426.18]  He's right here.
[426.18 --> 426.62]  Yeah, nice.
[427.98 --> 428.52]  All right.
[428.54 --> 429.62]  He's just never wearing stripes.
[429.92 --> 430.08]  Whatever.
[430.28 --> 431.42]  I guess he just got over it.
[432.18 --> 436.82]  So what we can do is when the show goes live out there on the internet, so we can put
[436.82 --> 440.80]  a poll out and find out which of these are the best WMR, and then you'll be required
[440.80 --> 442.40]  to use that from here on out.
[442.46 --> 443.22]  I think that's a fair.
[443.70 --> 448.58]  Just set up a bot to PR the headline change in the Read Me every week.
[448.58 --> 449.06]  Just constantly.
[449.66 --> 449.88]  Yeah.
[449.88 --> 451.22]  Or we'll just have Nick do it.
[451.86 --> 452.08]  Yeah.
[452.88 --> 453.76]  I got the time.
[454.32 --> 455.12]  He's got the time.
[455.12 --> 467.34]  Nick will write a Neovim plug-in, which writes a bot, which submits the PR.
[467.50 --> 468.36]  That's the way Nick does it.
[468.46 --> 468.60]  Okay.
[469.34 --> 469.66]  Nice.
[469.66 --> 473.92]  Well, I would say enough tomfoolery, but there'll probably be some more upcoming.
[474.26 --> 478.64]  But in between the ridiculousness, let's get some actual content out there.
[479.66 --> 481.16]  WMR, who cares what it stands for?
[481.50 --> 485.90]  As I said, your little tagline is a tiny all-in-one development tool for modern web apps.
[485.98 --> 490.06]  And so that begs the question then, what is a modern web app?
[490.10 --> 491.42]  That's the one you knew I was going to ask, right?
[491.48 --> 491.76]  Yeah, that's right.
[491.76 --> 493.52]  So have at it.
[493.56 --> 494.42]  What's a modern web app?
[494.52 --> 495.98]  So there's probably two answers for that.
[496.20 --> 499.02]  One is, it's a web app that you're building now.
[499.94 --> 505.10]  Because modern is a time frame, and that time frame is recent.
[505.86 --> 506.14]  Okay.
[506.90 --> 508.24]  That's a good, safe answer.
[508.44 --> 508.78]  Yeah.
[508.90 --> 510.08]  That's the lame answer.
[510.42 --> 510.84]  Right.
[510.84 --> 520.80]  The maybe more appropriate answer is, it's a web app where the thing that you have front of mind,
[521.02 --> 529.66]  and the constraints that you have on your mind as you develop, are modern browsers, modern UX, modern dependencies.
[529.66 --> 540.74]  Sort of this general assumption that this is not going to be, you know, trying to use code from the late 2000s.
[540.76 --> 545.92]  This is not going to be trying to service, necessarily, browsers from the late 2000s.
[546.36 --> 551.70]  Certainly, it would be written in modern JavaScript, which, yeah, you know, another recursive definition there.
[551.94 --> 554.94]  But, you know, ES 2017 or newer kind of thing.
[554.94 --> 574.40]  And the most important one, I think, at least for me, is the tool chain is optimized to give you the best experience possible for, you know, ES modules and TypeScript and some of these things that are now omnipresent on NPM.
[574.74 --> 583.04]  But there are still large swaths of modules on NPM that have not moved over to those things or that sort of exist from an era prior to all of that.
[583.04 --> 593.86]  And so, you know, in a typical bundler setup, especially in like an ahead of time bundling setup, generally, there is layers of abstraction added in.
[594.02 --> 596.90]  So, you know, you import a thing and you're not actually importing that thing.
[596.98 --> 600.20]  You're importing like a compiled version of that thing.
[600.20 --> 619.90]  And WMR basically takes the stance that some of those layers of abstraction actually hurt newer, more readable dependencies in code you might write in order to support older, maybe less readable.
[619.90 --> 625.62]  And in WMR's case, we hope slightly less important to your project modules.
[626.12 --> 633.58]  And so the idea is like, OK, well, let's build a tool that tries to still sort of support some of the older stuff.
[633.96 --> 643.70]  But the focus, if we have to choose, the focus is always going to be on make the sort of more recent, newer stuff as good as it can be.
[643.70 --> 646.98]  So don't don't detract from it just in order to have compatibility.
[647.78 --> 655.58]  So if you were to liken it to something that already exists just for context or for frame of reference, like what kind of a thing is it?
[655.64 --> 661.16]  Would you say it's kind of like a create react app or it's kind of like a next JS or like it's kind of like a webpack?
[661.28 --> 664.68]  Like what's it kind of like that people would be like, OK, it's like this, but different.
[664.68 --> 672.68]  It's weirdly probably closest to Webpack, but that might be sort of an awkward comparison.
[673.64 --> 676.76]  Like in terms of existing tools, it's closest to Vite or Vite.
[676.98 --> 679.40]  Never got clarity on how that's pronounced.
[679.92 --> 680.04]  Right.
[680.12 --> 682.02]  Vue's new bundler and Snowpack.
[682.54 --> 687.08]  And also ESDevServer or ModernDevServer, I can't remember which is the more recent name.
[687.54 --> 691.48]  It exists in that space of like ESM first.
[691.86 --> 692.34]  Gotcha.
[692.60 --> 694.02]  Bundlers slash non-bundlers.
[694.76 --> 699.04]  And I guess the thing that makes it maybe sort of like Webpack in that regard.
[699.40 --> 700.58]  Actually, I shouldn't say Webpack.
[700.74 --> 702.46]  It's closest to Parcel in that regard.
[702.88 --> 710.26]  WMR really, really, really tries to remove itself from your field of view as a developer.
[710.58 --> 712.44]  So it tries to sort of stay out of the way.
[712.90 --> 718.44]  Normally, when you start a project with a bundler, like a Webpack or a rollup, your first job is configure the bundler.
[718.44 --> 724.20]  You know, tell it the semantics of your project and your file structure and what you're trying to build.
[724.74 --> 726.50]  There's good reasons why bundlers allow that, right?
[726.56 --> 728.76]  Rollup and Webpack are super versatile tools.
[729.30 --> 729.40]  Right.
[729.40 --> 740.44]  But that's also, you know, as somebody who has like a fairly severe ADHD sufferer and who does a lot of prototyping to manage to be productive.
[740.44 --> 743.88]  Despite that, all of those like stop, configure.
[743.88 --> 750.30]  Those are all steps that kind of get in the way of you actually starting a project.
[750.74 --> 753.72]  Or they, at the very least, they eat into the time that you might spend.
[753.84 --> 759.10]  If, you know, if you have two hours to prototype something, you really don't want to spend the first hour and a half configuring your bundler.
[759.26 --> 761.96]  I've definitely failed hackathons for that very reason.
[761.96 --> 764.78]  So it's very much about greasing the skids, right?
[764.86 --> 765.98]  Like, just get me running.
[766.62 --> 770.66]  No config or zero, you know, out of the box, pre-configured for you.
[771.28 --> 773.78]  Don't make me think style tooling.
[774.32 --> 774.54]  Yeah.
[774.60 --> 779.58]  And the interesting take here, because like we have micro bundle, which is basically written by the same people.
[780.38 --> 787.66]  Obviously, that micro bundle is, it's basically a configuration for rollup that you install as a command line tool so you don't have to also install rollup.
[787.66 --> 795.64]  And that one is very strictly like, we are just rollup, but with heavy handed defaults that make sense for a lot of modules.
[796.36 --> 798.40]  WMR kind of tried to flip that on its head.
[798.66 --> 802.36]  We do support configuration, which is already different from micro bundle.
[802.92 --> 809.86]  But instead of basically saying we're going to give you what we think is right out of the box as defaults,
[809.86 --> 819.42]  what WMR does is it tries to extract all of the possible configuration defaults from what you write.
[819.76 --> 829.96]  So rather than saying, you know, this is how you reference entry modules in your HTML, like this is how you bundle and then reference stuff from HTML.
[830.68 --> 835.90]  Instead, we flip that on its head and we say, we will look at your HTML and find the modules that you have referenced there.
[836.02 --> 838.32]  And that's how we'll figure out how to bundle your application.
[838.32 --> 843.14]  So Parcel was definitely a trailblazer in this regard, and they still do this very well.
[843.70 --> 849.38]  They really try and like give you a bundler that incorporates the web's defaults as its defaults.
[849.44 --> 853.32]  So you don't have to, you know, sort of tell the bundler, yes, I am building for the browser.
[853.60 --> 855.32]  Yes, these are the semantics of a browser.
[855.48 --> 859.02]  Those are things that you can actually just know up front in a bundler.
[859.82 --> 865.84]  And it even tries to take that, I could probably get into the semantics of why this ends up mattering later.
[865.84 --> 870.88]  But like, you know, Webpack has like the optimized chunks configuration or whatever.
[870.98 --> 874.28]  You can kind of tell it like, oh, collapse such and such as stuff if it's below this threshold.
[874.92 --> 874.98]  Right.
[876.06 --> 877.60]  Rollup doesn't have that.
[877.60 --> 883.68]  But we grafted it into rollup, which is what powers WMR's production output.
[884.58 --> 891.46]  So we basically, like for CSS files, as an example, WMR will try to not produce CSS files below one kilobyte.
[891.46 --> 901.38]  Because in general, that's going to be the point at which the headers for your request are approaching the size of the response body itself.
[901.54 --> 907.44]  And you start to see really, really diminishing returns in terms of like G's of compression, which has a threshold of about a K.
[907.44 --> 919.86]  So it basically tried to work back from like compression thresholds, TCP window sizes, you know, all these sorts of things that like, oh, there's like actual specifications that define these things.
[919.86 --> 922.78]  Or at the very least, there's convention that defines these things.
[923.00 --> 925.84]  Why don't we just have that be what defines the defaults for the tool?
[925.84 --> 938.58]  So it really tries to like, stay out of your way, not by telling you what to do, but by finding concrete, I don't want to say evidence based, I feel like that's, that's giving it too much credit.
[938.84 --> 946.40]  Finding concrete sort of obvious defaults that you're going to tell the bundler at some point anyway, when you're doing your optimization.
[946.96 --> 949.56]  And just saying, yeah, screw it, we're just going to do that by default.
[949.70 --> 951.36]  Like that, that's a logical default to have.
[951.36 --> 954.74]  I kind of think I'm listening to you talk about it.
[954.74 --> 960.66]  It almost sounds like akin to like a compiler doing type inference where it's like, I think you must be using an int right now.
[960.72 --> 966.70]  So I'm just going to infer that that's what it is and not make you declare it like you might in some other typed languages.
[966.70 --> 975.26]  This is kind of like config inference or style inference to a certain degree, not trying to give you too much credit again, but it's kind of akin to that, right?
[975.28 --> 977.14]  Like you're like, well, find out what they're doing.
[977.14 --> 983.60]  And also what's the best practice here that they don't want to defer from that or divert from that and just do that.
[983.60 --> 986.70]  But also like what style are you using?
[986.74 --> 988.56]  I'll just go ahead and just do that.
[989.22 --> 989.32]  Right.
[989.40 --> 993.26]  And so like the similarity there is actually, it's pretty reasonable.
[993.26 --> 1001.48]  You could almost think of WMR as let's say in production mode only because development mode is this whole other story.
[1001.58 --> 1009.68]  But in production mode, it's almost like WMR looks at your code base and generates a rollup config that is optimal for that code base and then runs it.
[1010.24 --> 1012.08]  That's actually sort of how it works.
[1012.08 --> 1019.74]  It's a little bit more complex and contextual than that, but at least in terms of our production output, you can kind of think of it like that, right?
[1019.74 --> 1036.86]  Like in a normal bundler, you would configure entry points and your minifier and your node modules resolution and like all the weird like, oh, you know, but the React is modules commonly used from ESM with named imports, but it doesn't have any.
[1036.86 --> 1047.86]  So like patch that instead, we just do all that on the fly based on the code that you wrote, because like you already wrote code that essentially said, oh, you know, import type of from React is.
[1048.92 --> 1053.76]  So we don't need configuration to know that you're trying to use named imports from a common JS module.
[1054.10 --> 1054.86]  It's right there in the code.
[1055.20 --> 1056.74]  So that's the one angle.
[1057.16 --> 1065.02]  And the other whole piece of this is during development, WMR doesn't actually really bundle at all.
[1065.02 --> 1073.70]  And so this is where the Skypack or Snowpack and Vite and modern dev server comparison kind of comes into play.
[1075.22 --> 1078.08]  WMR, like it's really similar to those tools.
[1079.00 --> 1093.02]  And to be honest, throughout the entire development of this project, since we started in May, I want to say April, May, we've been kind of discussing stuff with the authors of those tools behind the scenes saying like, hey, like at some point, maybe we should just like consolidate these things.
[1093.02 --> 1103.22]  But I think the logical thing and the thing that's going to be most beneficial for the ecosystem right now is to just kind of let these flowers bloom for a little bit and then see what are the similarities?
[1103.50 --> 1104.82]  What did we end up duplicating?
[1104.98 --> 1106.10]  How can we collaborate better?
[1106.84 --> 1113.50]  And so what we try to do with WMR is working back from that model of in development, you're not bundling.
[1113.62 --> 1116.16]  We're just shipping modules over the wire as HTTP requests.
[1116.16 --> 1120.88]  We tried to optimize the pathway for every module from disk to browser.
[1121.80 --> 1135.84]  And so instead of pulling a module off disk, running it through Babel, running it through Terser, running it through a source code transformer that finds import statements and rewrites them because very imports don't work in browsers.
[1135.84 --> 1150.14]  Instead of doing all those steps, generally in sequence, generally with different tools, we actually wrote our own Babel compatible AST transformer and rollup compatible plugin API.
[1150.66 --> 1158.02]  So if you're built a rollup plugin, that whole API is actually supported by WMR, even though WMR is not running rollup.
[1158.02 --> 1160.90]  We just call all the same hooks in the same order.
[1161.08 --> 1162.94]  We expose the same acorn parsing stuff.
[1163.42 --> 1168.08]  But at the end of the day, what it means is we read a module off disk and put it in a memory cache.
[1168.60 --> 1179.04]  We pass it through at most one AST transformation that will parse all the code, but will in almost no cases will it stringify all the code.
[1179.14 --> 1182.58]  It's only going to like re-serialize mutated AST nodes.
[1182.68 --> 1183.94]  So it's extremely fast.
[1183.94 --> 1187.50]  But actually, in most cases, no AST transformations.
[1187.92 --> 1194.12]  We're using Guy Bedford's ES module Lexer to do basically token based transformations.
[1194.38 --> 1196.52]  So we don't make a whole graph of your code.
[1196.64 --> 1198.76]  We literally just know that like, oh, this is an import statement.
[1198.90 --> 1200.16]  Here's the string that was imported.
[1200.76 --> 1201.94]  What are you going to do with this string?
[1202.64 --> 1206.96]  And then that all feeds back through this rollup based plugin API or rollup compatible plugin API.
[1206.96 --> 1218.08]  But the idea is like, basically WMR should get modules into the browser as roughly as fast as it can read the module off disk and stream it to the browser.
[1218.24 --> 1223.12]  It really shouldn't be adding any overhead to each request in order to do transformations.
[1223.12 --> 1230.56]  And that originally actually just comes from, I work on Glitch a lot.
[1232.04 --> 1232.74]  It's cheap.
[1233.60 --> 1235.44]  It's just a habit I've gotten into.
[1235.86 --> 1235.90]  Yeah.
[1235.90 --> 1249.10]  And Glitch has a static like mode, but the static mode doesn't support like JSX or TypeScript or Bary imports or ES modules or node modules for that matter, which it's just slightly too limited.
[1249.84 --> 1255.32]  And so I originally was, I started WMR as like a better Glitch static, right?
[1255.36 --> 1262.98]  So basically a static file server that like does some intelligent stuff with JavaScript, but very little, just what's necessary to make it usable.
[1262.98 --> 1265.56]  And so that's kind of the premise there.
[1265.80 --> 1270.98]  That's also where this whole concept of not having to install dependencies came from.
[1271.40 --> 1282.74]  So like it's a pain in the butt to manage your package JSON and especially on Glitch, every edit you make to the package JSON redownloads all the node modules via pnpm and populates them in the node modules directory.
[1282.74 --> 1293.46]  In WMR, if you don't run npm install and you import a package in your code, we just go and fetch it from the registry and stream it to disk.
[1294.40 --> 1300.80]  And interestingly, we stream it to disk knowing that you're only going to use it as like a source code package.
[1300.88 --> 1303.54]  So we don't run package install scripts because that's unsafe.
[1303.54 --> 1310.18]  We don't even write temp files, test files, unused source stuff to disk.
[1310.42 --> 1319.86]  You basically get a node modules directory that only contains package.json's, JS and TS files, and TypeScript definitions, which is kind of nice.
[1320.40 --> 1323.98]  Something about that just sounds like almost too good to be true kind of a thing.
[1324.14 --> 1327.94]  Like is that, I mean, you're thinking like what could go wrong?
[1328.08 --> 1329.94]  Something has to be able to go wrong there, right?
[1329.94 --> 1336.08]  Yeah, I mean, like there was definitely some pushback we got in the initial announcement saying, oh, we're doing streaming install.
[1336.16 --> 1340.18]  Because I think people think, oh, streaming install, they're running npm install in the background.
[1340.42 --> 1343.80]  And we don't actually use the npm client at all in any form.
[1344.56 --> 1345.36]  This actually does.
[1345.80 --> 1348.84]  So you're just literally fetching the source files and that's not even that.
[1348.90 --> 1352.26]  So it's fetching the tarball direct from the npm registry.
[1352.46 --> 1352.72]  Okay.
[1352.72 --> 1354.54]  And it streams it.
[1355.34 --> 1366.54]  And as each file in the tarball passes through our streaming untar and un-gzip mechanics, those files get analyzed and conditionally written to disk.
[1366.60 --> 1372.18]  So if you have something like a shell script or an executable, it never even makes it out of memory.
[1372.56 --> 1380.16]  So I don't want to say it's secure, but it definitely avoids all the foot guns that would immediately jump to mind for like, hey, streaming auto install.
[1380.16 --> 1382.44]  It's also just really fast.
[1383.12 --> 1393.30]  So basically, we can get your dependency installed and shipped to the browser or whatever file from it you were importing as fast as we can get that tarball from npm because it's streaming.
[1393.64 --> 1394.66]  Sounds like an awesome feature.
[1394.74 --> 1397.86]  It kind of goes along with what you're talking about with the inference where it's like you're using this.
[1398.06 --> 1399.26]  Okay, we'll get it for you.
[1399.52 --> 1400.14]  And that's it.
[1400.58 --> 1406.90]  But we know not only are you using the Preact package, but we know that you're using it from WMR.
[1406.90 --> 1416.28]  And we know that, as an example, the Preact package has an export app, which defines what is externally accessible, what files are externally accessible.
[1417.14 --> 1424.12]  And so we know that in a properly spec-compliant bundler, you can't import files that aren't in the export map.
[1424.60 --> 1433.36]  So we just won't write those files to disk because they frankly don't exist, unless they're TypeScript definitions because TypeScript kind of made of its own thing there.
[1433.36 --> 1433.76]  But that's fine.
[1433.78 --> 1434.60]  That's very few files.
[1435.50 --> 1438.86]  But we can sort of infer like, oh, this isn't just a random package.
[1438.96 --> 1440.70]  It's just not a command line tool that you're installing.
[1440.84 --> 1442.44]  It's not arbitrary code.
[1442.78 --> 1445.02]  It's source text that you're going to want to import.
[1445.28 --> 1445.34]  Yeah.
[1446.12 --> 1454.70]  And so when we do that, again, with the inference thing, we stream it to disk and we send you the file because you're waiting on this request in the browser.
[1454.80 --> 1457.60]  The browser will either have reloaded or hot module updated or whatever.
[1457.74 --> 1459.86]  And you're sitting there waiting for this dependency to download.
[1460.46 --> 1462.36]  We get the dependency to the browser right away.
[1462.36 --> 1472.48]  It runs through a extremely lightweight roll-up pass, but doesn't do any minification, doesn't do any mangling, anything like that.
[1473.10 --> 1480.52]  It basically just concatenates modules together that wouldn't have been individually addressable anyway, so that we're not shipping like thousands of VS modules over the wire.
[1481.26 --> 1484.22]  But sort of like as close to zero milliseconds as we can get there.
[1484.22 --> 1495.14]  And then behind the scenes, after you've actually requested that module and after it's been loaded in the browser, we then schedule it to go off into a minification and Brotley compression pass.
[1495.14 --> 1498.58]  And so if you import Preact, you'll get Preact right away.
[1499.00 --> 1514.80]  But then after a second-ish or two of idle time, WMR will have already generated a hyper-optimized version of that dependency and written it back to disk so that the next time you request it, you get the optimized Brotley compressed version, but just streamed from disk.
[1514.92 --> 1516.78]  There's no overhead on the request itself.
[1516.78 --> 1519.42]  Yeah, it's sort of a funky setup.
[1520.08 --> 1527.70]  You said that when it goes to the browser in that either development or production build, I guess probably both, it's just basically the concatenated files.
[1527.82 --> 1530.22]  It's not actually running like ES modules in the browser.
[1530.66 --> 1531.10]  Is that right?
[1531.64 --> 1533.90]  So it does use native ESM for everything.
[1534.38 --> 1534.66]  Okay.
[1535.02 --> 1544.02]  So actually, that's one of the reasons why the roll-up bundling process is done, even for the unoptimized version, is that's where we convert CommonJS and UMD to ESM.
[1544.64 --> 1544.94]  Gotcha.
[1544.94 --> 1545.02]  Gotcha.
[1545.46 --> 1552.80]  So I guess I'm a little behind on actually using direct ESM because I do it through TypeScript.
[1553.42 --> 1558.70]  And I ran the Create WMR project and kind of played around with that a little bit.
[1558.70 --> 1565.22]  It looks like there's kind of a mix of like, like I'm specifically looking at the imports and like there's some with file extension, some without.
[1565.48 --> 1569.44]  And I was wondering, like, is it doing rewrites of those for me automatically or?
[1569.78 --> 1569.98]  Yes.
[1569.98 --> 1570.26]  Yes.
[1570.58 --> 1570.86]  Yes.
[1570.94 --> 1576.66]  So, and that has shaped a little bit since this tool was originally created.
[1577.34 --> 1583.84]  So we always have rewritten bare specifiers just because the browser is going to, it just is a syntax error in the browser.
[1583.84 --> 1586.72]  And there's no way for us to patch that in on the front end.
[1586.72 --> 1596.98]  So like if you do like import foo, the module foo, we will rewrite that to, I think it's import a URL like slash at NPM slash foo.
[1597.44 --> 1597.48]  Okay.
[1597.48 --> 1598.22]  You know, it's a pattern.
[1598.36 --> 1599.02]  It always looks like that.
[1599.08 --> 1600.50]  You kind of get used to seeing on the front end.
[1600.50 --> 1605.92]  And in your browser's network console, you'll just see foo because it shows the base name, not the path name.
[1605.92 --> 1629.08]  In the case of something like TypeScript or if you're using JavaScript files and you don't want to use file extensions, WMR in its current state will infer the file extension and like, you know, correct it.
[1629.08 --> 1643.52]  So in the browser, you know, if you imported slash utils and the file on disk was called utils.ts in the browser, I believe you will see slash utils.ts.
[1644.12 --> 1645.46]  I actually have to check.
[1647.38 --> 1647.82]  Interesting.
[1648.42 --> 1648.58]  Yeah.
[1648.68 --> 1653.90]  And so basically that happens because I had mentioned we support the rollup plugin API during development.
[1654.44 --> 1657.82]  Originally, we did not do file extension inference.
[1657.82 --> 1664.46]  So if you wanted to import a file that had an extension, whether it's TypeScript, JavaScript, TSX, whatever, you just type the file out with the extension.
[1665.28 --> 1676.06]  I actually personally really liked that approach because I know that behind the scenes, that means that WMR never ever has to read a directory or call into Node's file system API to check if something exists.
[1676.42 --> 1678.78]  Basically, when you do an import, we call a read file.
[1678.98 --> 1679.28]  That's it.
[1680.20 --> 1683.96]  So even if you're writing TypeScript, you would do like a .ts extension for all of those?
[1683.96 --> 1688.94]  Or you could also use a .js extension, but that's a TypeScriptism.
[1689.34 --> 1693.68]  The .js extension when there's a .ts file on disk is the .ts file.
[1694.16 --> 1694.44]  Okay.
[1695.04 --> 1702.04]  But that was actually one of the reasons why we ended up going down the road of implementing file extension inference.
[1702.80 --> 1704.38]  So you kind of treat it like ASI a little bit.
[1704.94 --> 1705.62]  Yeah, exactly.
[1706.06 --> 1707.22]  You don't have to use it.
[1707.28 --> 1710.42]  And it is faster if you don't use it, but you can use it.
[1710.42 --> 1721.80]  And so one weird case where this actually rears its head is like if you have a script tag in an HTML document, the correct thing to do in WMR is to include the full file extension of that script, regardless of what it is.
[1721.92 --> 1723.44]  If it doesn't exist, don't put it.
[1723.52 --> 1726.72]  If it's a .tsx, it would be, you know, slash foo.tsx.
[1726.72 --> 1734.44]  And that's just like we're trying to steer people towards the spec, which says like there is no magic.
[1734.62 --> 1735.76]  A URL is just a URL.
[1736.12 --> 1737.72]  There is no such thing as inference.
[1738.46 --> 1748.78]  But we also, you know, to the earlier point, we are aware that a lot of people are used to the semantics of things like Create React app, which are essentially the semantics of Webpack.
[1748.78 --> 1753.68]  And so as kind of a way to bridge that gap, we do the inference.
[1753.88 --> 1757.98]  You can, there's a debug environment variable that you can set to one.
[1758.48 --> 1763.34]  And that will print out all of the plugins that got executed on every request.
[1763.52 --> 1771.16]  And you can actually see in real time like, oh, wow, I just round tripped through the file extension resolver three times just because I didn't want to type .tsx.
[1771.16 --> 1776.18]  And so we're not, we won't show the performance stats on it because it's on a per request basis.
[1776.32 --> 1782.52]  It's very minimal, but you can still see like, you know, this is what I've opted into by choosing that thing.
[1784.44 --> 1795.84]  The other piece of this is I think the file extensions thing, especially for TypeScript, is still just sort of in the last stages of kind of settling out.
[1795.84 --> 1796.62]  Mm-hmm.
[1796.62 --> 1815.82]  The nice thing with specifying full file extensions is at least in VS Code and I think JetBrains, if you have any imports that have a file extension in your module and you use like the auto import thing, like you click a suggested result and it imports, that new import will also use a file extension.
[1815.94 --> 1819.34]  So it's smart enough to see like, oh, this person is typing file extensions out.
[1819.70 --> 1824.22]  I don't think it does on a project wide basis by default yet, which would be like a nice next step.
[1824.22 --> 1824.94]  Mm-hmm.
[1825.18 --> 1825.98]  That's sort of why you see that.
[1826.02 --> 1831.72]  And I think right now the template, I think we ship .js by default.
[1832.14 --> 1832.38]  Yep.
[1832.88 --> 1838.42]  Although TypeScript is supported by WMR itself by default, we don't scaffold it by default.
[1839.20 --> 1839.56]  Yeah.
[1839.66 --> 1849.00]  I noticed that there was a tsconfig in there that it created and then I just went into, there's a header.js file and I just renamed it to header.ts and it still worked.
[1849.36 --> 1849.38]  So.
[1849.82 --> 1849.96]  Yeah.
[1850.02 --> 1851.42]  So that's actually an interesting point.
[1851.42 --> 1855.24]  So like WMR, you know, obviously there's a whole bunch of stuff that it's doing, it's goals or whatever.
[1855.86 --> 1858.88]  But the other piece is, this is coming from the Preact team.
[1858.98 --> 1864.04]  And the Preact team, we still by and large write everything in vanilla JavaScript.
[1864.04 --> 1875.76]  But over the past year or two have all but replatformed onto JS doc based TypeScript that is actually just JavaScript.
[1876.56 --> 1883.18]  To the point where WMR itself is written in JS and JS doc, but is strictly typed.
[1883.34 --> 1883.64]  Gotcha.
[1883.64 --> 1883.76]  Yeah.
[1884.20 --> 1886.50]  Like a type error breaks the pill.
[1887.58 --> 1889.78]  Which is less crazy than you'd think.
[1889.78 --> 1894.30]  Because there's this clever thing where you can stick all your types as ambient types in the source directory.
[1894.66 --> 1900.04]  And then just reference them without even having to import anything from your JS doc annotations.
[1900.04 --> 1910.76]  And the TypeScript team has been really good over the past year about like extending the JS doc functionality and finding like that nice balance of like JS doc that isn't entirely TypeScript specific.
[1910.76 --> 1914.64]  And so we've like, we're all on board on that.
[1914.78 --> 1920.68]  Like even the main Preact code base right now is basically being rewritten to use this strict variant.
[1921.26 --> 1934.20]  And so we kind of wanted to scaffold something that kind of shows people like, hey, like you can turn on CheckJS and get all these lovely compilerisms that you wouldn't expect from a standard JavaScript environment as long as you're using an editor that cares about TypeScript.
[1934.20 --> 1940.34]  And then the other piece is we support CSS modules and some import prefixes.
[1940.54 --> 1945.30]  Like you can do like, I think it's a URL colon and then the path to something.
[1945.46 --> 1952.90]  And it will, when the thing you import is the URL of that file, which I think Parcel supports the same thing.
[1953.28 --> 1955.58]  How does TypeScript handle an import that looks like that?
[1955.90 --> 1957.74]  Well, so that's, that's what the TS config is actually for.
[1957.74 --> 1971.38]  So when you install WMR or actually it's not the TS config, when you install WMR, we ship ambient types in the WMR package that define ambient module definitions using wildcard statements for URL colon star.
[1971.56 --> 1973.68]  Same thing for CSS modules.
[1973.86 --> 1982.90]  If you import, you know, star.module.css, the import, like the value generated by the import will be an object mapping of class names.
[1983.48 --> 1983.72]  Nice.
[1983.72 --> 1989.04]  And again, so like we are providing you the thing and it's, it's technically configurable.
[1989.16 --> 1990.76]  You could turn this off, but like that's the default.
[1990.94 --> 1994.20]  So we provide you the type definitions for that default, which is, it's nice.
[1994.26 --> 2000.76]  This is something that like, I think we always wanted to do it in Preact CLI, but we didn't have the .module.css thing, that convention.
[2001.40 --> 2008.20]  And we maybe couldn't guess as much about the type of code you were trying to write to be able to infer these things.
[2013.72 --> 2020.98]  Hey there, party animals.
[2021.12 --> 2021.68]  Jared here.
[2021.98 --> 2024.62]  I want to take a moment to tell you about Changelog++.
[2025.36 --> 2031.70]  It's our membership program where you can directly support JS Party and all of the podcasts we create here at Changelog.
[2032.46 --> 2037.54]  Ditch the ads, get closer to the metal, and enjoy supporting JS Party into the future.
[2038.26 --> 2041.12]  Once again, that's changelog.com slash plus plus.
[2041.46 --> 2042.60]  We'd love to have you with us.
[2042.60 --> 2063.96]  So as I mentioned, I was playing with the create WMR or NPM init WMR, which was really cool.
[2064.22 --> 2066.54]  And playing with the project that it creates there.
[2066.82 --> 2071.34]  I really love just how, like you said, I wasn't spending any time configuring things.
[2071.34 --> 2073.36]  I was just going and I wanted to use TypeScript.
[2073.44 --> 2076.18]  So I renamed the file to .ts and it just worked.
[2076.42 --> 2077.58]  And that was really awesome.
[2078.14 --> 2084.06]  But the create WMR package or the project template that it uses ships with Preact.
[2084.14 --> 2087.16]  And I was curious about the relationship between WMR and Preact.
[2087.22 --> 2089.78]  And is that a requirement or can it really work with anything?
[2090.20 --> 2090.34]  Yeah.
[2090.38 --> 2091.44]  Tell us a little bit about that.
[2091.86 --> 2092.96]  It's definitely not a requirement.
[2092.96 --> 2104.50]  The struggle here is we wanted to build something that met a need that we had on the Preact team, which was like, Preact is tiny and it's really good if you want to do a lightweight project.
[2104.76 --> 2106.54]  So where's our tooling for that?
[2107.24 --> 2112.56]  Where is our, you know, we have a webpack based tool that's like, you know, used in production by a bunch of high profile sites.
[2112.56 --> 2114.62]  But it's that's the heavyweight tool, right?
[2114.66 --> 2115.58]  Where's the prototyping tool?
[2116.32 --> 2117.40]  So that was the one hand.
[2117.56 --> 2123.22]  But then the other hand is myself and a bunch of others who just sort of happen to be on the Preact team.
[2123.22 --> 2131.58]  We've been kind of on the sidelines in the bundler ecosystem for a little while, at least, you know, leading through 2019 and 2020.
[2132.34 --> 2143.48]  You know, prodding people, kind of trying to get consensus on a direction that we can move in to further this idea of like writing modern code and shipping modern code and getting these things right.
[2143.48 --> 2159.34]  Where like, I feel like everybody in the community at this point is at least mostly, you know, rallying around like, we want to start shipping modern code, given that it's supported in the overwhelming majority of browsers, you know, 95% of browsers support ES 2017.
[2159.34 --> 2178.26]  And so like, from my, this is actually like, the thing that my Google work has been focused on for the last like two years has been going and finding all like the choke points there and trying to do the research and outline a solution that's, it might not be the perfect solution, but it might be the way forward.
[2178.84 --> 2187.30]  So part of that is like, trying to convince folks to use export maps, the new node feature as a way to publish modern JavaScript packages.
[2187.30 --> 2194.44]  So you can publish a package that has modern and legacy JavaScript, and now bundlers have a way to use one if they know how to get to it.
[2194.88 --> 2206.90]  And there's various reasons why I, you know, in the article that I released in December and the video that went along with it, kind of explain how that could be justified, right?
[2206.96 --> 2213.06]  Like, node started supporting export maps in 12.7 and node 12.9.
[2213.56 --> 2215.36]  And that version of node supports ES 2019.
[2215.36 --> 2220.74]  So if you ship an export map, it only works in a version of node that supports modern JS.
[2221.52 --> 2226.42]  And thus, you would assume that that code would be potentially modern JS because it's a modern package.
[2227.44 --> 2228.62]  So we kind of extrapolated that.
[2228.72 --> 2231.86]  Okay, well, what if bundlers also jumped on that same assumption?
[2232.10 --> 2238.00]  Could this be finally the modern field that we've been not able to standardize for five years?
[2238.00 --> 2258.96]  And so that and the timing of browser support kind of converging on that 2017 baseline, there was a very clear need for a tool or really a bunch of tools to basically, like, stake the claim here saying, like, actually, it's not just that we can ship smaller bundles using modern code, but also, like, we can do a better development experience.
[2258.96 --> 2266.78]  You know, we can ship readable code in development that's not one line of a valve for a two megabyte module.
[2266.78 --> 2284.02]  And so the non-preact part was just getting a tool out there that demonstrates, in addition to what Snowpack and Vite and some others have demonstrated, getting a tool out there that demonstrates that, like, there is even more that we could do if we double down on this.
[2284.02 --> 2292.48]  Like, WMR ships HTTP2 out of the box, you know, on the overwhelming majority of machines, it will set up certificates for you.
[2292.82 --> 2299.62]  And basically, at some point, you will get prompted to enter your administrator password, which I know scares the crap out of people, rightfully so.
[2300.04 --> 2304.62]  But this is using literally the de facto standard module that implements this thing.
[2304.72 --> 2306.42]  It's relatively safe, all things considered.
[2306.70 --> 2313.50]  But we ship that out of the box because we know that H2 with ES modules is the fastest and best experience during development.
[2314.02 --> 2323.30]  And then also showing, like, when you platform on ES modules, things like hot module reloading and asset references can also get easier.
[2323.30 --> 2330.66]  So, like, hot module reloading is just you dynamically import the current module with a query string parameter to bust the cache.
[2331.14 --> 2331.62]  That's it.
[2332.42 --> 2336.32]  You know, there's some weird logic that we do right now to repatch exports onto the old module.
[2336.50 --> 2340.96]  But even that, we're actively pursuing avenues of getting rid of that piece.
[2340.96 --> 2349.96]  The goal there is to show, like, not only can we ship something that's truly good, but also, like, we can ship something that's actually fairly easy to understand.
[2350.44 --> 2350.50]  Right?
[2350.54 --> 2355.36]  Like, sitting here, you know, I said dynamically import the current module and replace it.
[2355.42 --> 2357.32]  Like, you can kind of picture how that would work.
[2357.58 --> 2357.76]  Yeah.
[2358.16 --> 2359.62]  Dynamic import, object assign.
[2360.50 --> 2360.72]  You know?
[2360.90 --> 2363.02]  And that's roughly accurate.
[2363.72 --> 2364.12]  Yeah.
[2364.12 --> 2366.42]  You know, minus some weird...
[2366.42 --> 2368.56]  Close enough approximation about what's exactly happening.
[2369.08 --> 2369.26]  Right.
[2369.58 --> 2380.32]  And so there's just a lot less guesswork between you and the actual generated code that you run in the browser, which is potentially less surface area to have things go wrong in.
[2380.32 --> 2397.40]  And so then, getting back to kind of the Preact thing, our goal with this was basically keep WMR as agnostic as it can possibly be to Preact so that all of the little pieces inside WMR...
[2397.40 --> 2405.84]  Because WMR is literally just built as, like, 20 roll-up plugins and a couple of standalone libraries we haven't yet published yet.
[2405.98 --> 2407.22]  But, like, they're all independent.
[2407.74 --> 2413.14]  Keep that totally separate so that, you know, Vite can grab the plugin API and use it.
[2413.32 --> 2421.02]  Or, you know, I've actually just this morning been making the rounds looking at all of the export maps implementations in these bundlers, finding some issues with them.
[2421.02 --> 2435.66]  And it's very clear that, like, it's not to say that WMR gets this right, but having a package, possibly WMR's export maps implementation, that just gets extracted out and published to NPM as, like, a here's how you resolve export maps type package, that's valuable.
[2436.08 --> 2443.02]  And it would be really shameful for us to, like, do the work of building this and hopefully getting things correct, but have it be weirdly Preact-specific, right?
[2443.08 --> 2444.92]  Like, that doesn't make sense to me.
[2444.92 --> 2455.30]  And so we tried to keep the core and essentially everything about WMR Preact-agnostic, except when it came to scaffolding.
[2455.80 --> 2462.92]  So by default, we scaffold the JSX support so that it generates...
[2464.18 --> 2468.04]  It's actually generating tag templates, which is unique.
[2468.44 --> 2470.68]  And I don't know that that's been done elsewhere before.
[2471.10 --> 2472.66]  But again, it's that first mantra.
[2472.66 --> 2473.72]  It's the modern side, yeah.
[2473.72 --> 2474.60]  Yeah, exactly.
[2474.92 --> 2478.58]  But the tag templates, by default, they are bound to Preact.
[2478.90 --> 2484.88]  It takes two seconds to rebind them to another library like Vue or React or your own custom thing.
[2485.40 --> 2489.10]  But the default is Preact just because we have to serve both needs.
[2490.08 --> 2498.90]  And then the create WMR package, which that was built the day before launch just so that people could use the tool easily.
[2498.90 --> 2507.84]  But the create WMR package scaffolds a Preact app because that's the one that we were most confident people would be able to, like, poke around with and try.
[2507.92 --> 2514.08]  Even if you're not a Preact user, even if you're, like, a React user or a Vue user, like, you can get a feel for it.
[2514.08 --> 2514.36]  Mm-hmm.
[2514.36 --> 2517.60]  And it lets us show off hot module reloading and some things like that.
[2517.60 --> 2525.20]  And then the last piece is WMR in about the last two months leading up to the launch.
[2525.26 --> 2526.80]  Like, originally, we were going to launch it in August.
[2526.80 --> 2530.92]  And we kind of had to sit down and decided, like, oh, you know what?
[2531.82 --> 2532.96]  Maybe there's more we can do here.
[2533.08 --> 2535.90]  Maybe we can ship more than just a good hot module replacement solution.
[2536.40 --> 2543.06]  And we kind of went back to the drawing board and added things like the pre-rendering and the CSS optimization stage.
[2543.58 --> 2551.78]  And a lot of that, a lot of the reason why you see Preact as the default now is because Preact was the testbed that we used for all of this.
[2551.78 --> 2561.78]  So, create WMR will scaffold a project that when you do WMR build or NPM run build, you don't need JavaScript to run the output at all.
[2562.52 --> 2566.24]  And Preact in the scaffolded thing is how that works.
[2566.68 --> 2570.02]  But the API is actually completely independent.
[2570.56 --> 2577.70]  Like, pre-rendering in WMR is just you export a function called pre-render from whatever the first script tag in your HTML file is.
[2577.70 --> 2589.00]  And that function, it's an async function, so it returns a promise resolving to an object with an HTML string property and a links property that is an array of strings.
[2589.96 --> 2592.80]  And so, the HTML is the stuff that you pre-rendered.
[2592.92 --> 2594.02]  However, you chose to do that.
[2594.14 --> 2595.64]  It could just be returning a string if you wanted.
[2596.16 --> 2598.80]  But you can see how that would work in Vue and React and Svelte and whatever.
[2599.28 --> 2604.10]  And then the links property is if you want other URLs to then go and pre-render.
[2604.10 --> 2607.80]  And WMR won't pre-render if it's already pre-rendered stuff.
[2608.02 --> 2611.80]  But that's actually the guts of how our automatic pre-rendering works.
[2612.50 --> 2614.34]  And it has nothing to do with Preact.
[2614.52 --> 2618.24]  It happens that Preact can use that in a way that is extremely optimal.
[2618.94 --> 2622.24]  We don't ever have to parse the HTML because we generated it.
[2622.60 --> 2626.16]  And the thing that looks for links happens during the generation of the HTML.
[2627.08 --> 2629.44]  But it's just an array of strings.
[2629.44 --> 2634.80]  And so, like, anybody, I think there was somebody working on a Svelte test for this.
[2635.10 --> 2637.60]  We've got one bug we need to fix for compiling Svelte templates.
[2637.80 --> 2640.94]  But, like, you could easily adopt this to any framework.
[2641.12 --> 2650.18]  And so, my hope here would be, like, because WMR supports config files and anyone can create their own replacement for create WMR.
[2650.40 --> 2651.54]  It's a really simple package.
[2651.54 --> 2658.68]  Somebody could create, like, a package that scaffolds a WMR-based React app or Vue app or Svelte app.
[2658.88 --> 2662.92]  And it would be just as much of a first-class citizen as Preact.
[2663.00 --> 2670.46]  It just would have a config file, like a one-line config file that just says, like, export default React plugin.
[2671.14 --> 2671.54]  Right.
[2671.86 --> 2672.78]  Very minimal changes.
[2672.94 --> 2674.94]  So, somebody could create that.
[2675.02 --> 2677.08]  And somebody will probably create that.
[2677.62 --> 2678.20]  Yeah, that's my hope.
[2678.20 --> 2679.36]  Or fork WMR.
[2679.52 --> 2688.12]  But, like, forking WMR, we lose out on a lot of the, like, shared momentum aspect and collaboration aspect.
[2688.42 --> 2690.70]  Not to say that WMR is necessarily the place where it should happen.
[2690.78 --> 2690.92]  Right.
[2691.10 --> 2695.96]  But the hope was, like, if everybody's using plugins on top of the tool, that we can make the tool better.
[2696.36 --> 2701.80]  And at some point, when we take all the pieces of the tool and publish them to NPM as independent things, everyone benefits.
[2701.80 --> 2710.38]  Kind of leads me to a meta question around collaboration versus, you know, competition and, like, the decision here to start a new tool.
[2710.62 --> 2712.16]  Of course, it was like, well, Preact needs something.
[2712.42 --> 2712.68]  You know?
[2712.82 --> 2713.68]  We need our story.
[2713.82 --> 2716.48]  And so, it makes sense that the Preact team would make their own story.
[2716.58 --> 2725.12]  And I like how you're building it in a way that can be reused and collaborated as much as possible but still be, like, Preact's tool.
[2725.12 --> 2734.14]  But, like you said, there's Snowpack, there's these other efforts out there, and the decision was we're going to build at this level of abstraction.
[2734.40 --> 2737.92]  We're going to experiment so that there's more things.
[2738.10 --> 2748.02]  But then, for example, the Export Maps level, you're like, well, if we extract this into a library, everybody who's doing Vite or doing these other tools could use the Export Maps library.
[2748.16 --> 2749.44]  And we could collaborate at that level.
[2749.44 --> 2754.84]  How do we know which layers of abstraction is, like, we need a thousand ideas to flourish?
[2754.96 --> 2758.90]  And how do we know, like, hey, one good idea, we can all collaborate, let's team up.
[2759.40 --> 2761.66]  Like, where do we draw those lines?
[2761.76 --> 2764.46]  It seems to me like a very difficult thing to decide.
[2764.76 --> 2766.52]  It is an extremely hard problem.
[2766.78 --> 2767.90]  It is a distributed problem.
[2768.32 --> 2771.42]  I have this terrible habit of throwing myself at distributed problems.
[2772.34 --> 2777.76]  For some reason, Google seems to be willing to keep me on staff, partly to do that.
[2777.76 --> 2777.94]  Yeah.
[2777.94 --> 2783.22]  And so, like I mentioned, I was making the rounds looking at everybody's Export Maps implementations.
[2783.66 --> 2784.78]  Rollup just landed it.
[2784.98 --> 2789.12]  I think Lars from the Modern Web server implemented it in Rollup.
[2789.20 --> 2789.30]  Yay.
[2789.84 --> 2796.24]  But part of the reason why I'm doing that, and this is not to say that I'm the most objective person to be doing this,
[2796.24 --> 2803.22]  but I'm hoping that I can go and sort of do the survey, write the doc that kind of gives the lay of the land, publish that,
[2803.34 --> 2810.92]  and then whether or not WMR is the right implementation from which to derive the common implementation,
[2810.92 --> 2819.22]  I will have kind of one place that summarizes all of the current implementations.
[2819.22 --> 2829.06]  I think the difficulty is always with the thing you said, which is like, okay, Export Maps is an easy one because that's a spec.
[2829.22 --> 2830.50]  It's something that Node put there.
[2830.68 --> 2834.92]  So obviously there's value in a shared implementation of a spec in a reference implementation, essentially.
[2834.92 --> 2842.08]  And bundlers aren't necessarily able to use Node's implementation because it is not independent of Node,
[2842.18 --> 2844.10]  so it's not technically a pure reference implementation.
[2845.22 --> 2847.20]  And that's not to disparage it, but it's just...
[2847.20 --> 2847.54]  Factual.
[2847.54 --> 2848.60]  It fits their need.
[2848.84 --> 2848.98]  Right.
[2848.98 --> 2849.06]  Right.
[2850.26 --> 2852.86]  The other things are hairier.
[2853.04 --> 2857.62]  So we wrote that custom AST transformer that is largely Babel compatible.
[2858.02 --> 2859.04]  What do we do with that?
[2859.24 --> 2859.32]  Right?
[2859.36 --> 2860.70]  Like, is that a WMR thing?
[2860.80 --> 2866.36]  We literally built it to optimize WMR's performance while still supporting Babel plugins.
[2866.48 --> 2872.40]  But like, does the community need a sort of potentially lighter weight Babel alternative?
[2873.20 --> 2874.42]  Not sure about that, right?
[2874.42 --> 2880.24]  My default answer would be no, that's actually something we don't need or potentially don't want.
[2881.02 --> 2882.22]  Yeah, that gets tricky.
[2882.56 --> 2884.48]  And all these things were also written in JavaScript.
[2884.80 --> 2889.34]  And right now there's that whole move towards like, okay, could we use a faster language?
[2889.78 --> 2897.72]  We even have an experimental PR from a while back that uses ESBuild for JS transformations and minification, which was very fast.
[2898.72 --> 2900.08]  Which is a Go tool, right?
[2900.26 --> 2901.26]  Yeah, it's written in Go.
[2901.52 --> 2903.46]  It has a great JavaScript interface.
[2903.46 --> 2905.46]  We used it prior to it being pluggable.
[2905.72 --> 2913.96]  But for our need, because we use Terser for minification and we use this custom Babel-y thing for transformation, it does both of those things.
[2913.96 --> 2916.58]  And it does them faster than both of those things by a lot.
[2917.78 --> 2918.80]  So I think there's potential there.
[2918.96 --> 2920.46]  But we didn't want to...
[2921.04 --> 2925.90]  This is actually the reason why WMR wasn't published as WMR and 16 packages that power WMR.
[2925.90 --> 2929.14]  There's lots of packages in there that are independent and publishable.
[2929.76 --> 2937.54]  But where the rationale or the logic for why we would publish those things as independent is not clear.
[2937.90 --> 2939.82]  Or we already know that we don't want to.
[2940.38 --> 2947.72]  So some of the stuff that's in there is stopgaps while we wait for the ecosystem to settle so that we can use someone else's thing.
[2948.28 --> 2948.50]  Gotcha.
[2948.50 --> 2950.28]  Yeah, I don't have a clear answer on that.
[2950.34 --> 2951.36]  Not a clear answer.
[2951.52 --> 2953.24]  That's a difficult decision.
[2953.48 --> 2954.72]  And like you said, it's a distributed problem.
[2954.78 --> 2957.12]  So it's not as if you just get to decide that, right?
[2957.18 --> 2962.66]  Like everybody collaborates or doesn't and they make their decisions and this team makes that decision.
[2962.82 --> 2964.72]  And sometimes it's the right, sometimes it's the wrong.
[2964.72 --> 2969.06]  And it's just an interesting, I think, mind space to consider those things.
[2969.20 --> 2969.98]  But that's meta.
[2970.08 --> 2972.18]  Bringing it back down to kind of ground floor here.
[2972.96 --> 2975.82]  For somebody who's just like, oh, WMR looks cool.
[2976.06 --> 2977.90]  I really like how you don't even have to...
[2977.90 --> 2979.90]  Like I was actually playing with it as well with Nick.
[2979.94 --> 2984.14]  And I was like, I haven't seen this NPM init thing where like I didn't even...
[2984.14 --> 2985.64]  I expect to like install dash G.
[2985.64 --> 2986.72]  That's for some reason I'd use it too.
[2986.92 --> 2987.20]  Yeah.
[2987.42 --> 2989.76]  I don't even like just to put an emphasis on it.
[2989.80 --> 2992.68]  You don't like NPM install dash G WMR at all.
[2992.68 --> 2999.18]  Like you just init a new project, NPM init WMR and then your project name and it just is done.
[2999.36 --> 3000.94]  And even the project name is optional.
[3001.16 --> 3005.48]  If you run NPM init WMR in a directory, we'll make the directory a WMR app.
[3006.12 --> 3008.16]  So cool stuff like that is what gets people excited.
[3008.24 --> 3008.56]  Go ahead, Nick.
[3008.76 --> 3013.28]  I was going to say when I ran it and then CD'd into the directory, it ran so fast.
[3013.36 --> 3015.58]  So I ran NPM install just assuming I had to do that.
[3016.16 --> 3019.32]  Then I looked in the node modules directory and there was like nothing there.
[3019.34 --> 3019.84]  It was great.
[3020.02 --> 3020.28]  Right.
[3020.28 --> 3025.28]  So lots of cool stuff like ground floor for people who are like, this is a pretty neat tool.
[3026.20 --> 3027.84]  What else is cool about it?
[3027.86 --> 3031.88]  And I guess before you answer that, it gives its breadth, right?
[3031.92 --> 3033.50]  So it says from development to production.
[3033.70 --> 3034.66]  So there's the breadth of the tool.
[3034.76 --> 3038.52]  Like you're going to use this to dev, but you're also going to deploy production apps with this,
[3038.60 --> 3040.04]  but it doesn't give the scale.
[3041.02 --> 3042.12]  You've mentioned prototypes.
[3042.42 --> 3043.92]  You've mentioned like hackathons.
[3043.92 --> 3051.34]  If I'm reaching for a tool tomorrow to build a modern web app, like what kind of web app would I use WMR?
[3051.48 --> 3053.98]  And maybe where does it stop scaling or does it stop the scaling?
[3054.08 --> 3055.28]  Is there a complexity?
[3055.72 --> 3059.60]  Like if I'm building a modern Gmail, would I maybe reach for something?
[3059.68 --> 3061.90]  I'm building a modern Gmail right now with WMR.
[3062.10 --> 3062.48]  You are?
[3062.48 --> 3063.92]  That's hilarious.
[3064.88 --> 3065.02]  Yeah.
[3065.14 --> 3065.38]  Okay.
[3065.52 --> 3073.16]  So nothing to do with my employer, but it's just like I, what I want is something that is not just a mail client because I'm sick of just a mail client.
[3073.16 --> 3073.44]  Yeah.
[3073.44 --> 3081.40]  I want a work client that has all of my tasks and my calendar and my emails and to-dos and does time-based notifications and stuff like that.
[3081.40 --> 3084.70]  So maybe that answers the scale question, like, but WMR is your tool.
[3084.84 --> 3089.46]  So of course you're going to use your own tool, but if I'm not you and I'm, is there a scale problem or not?
[3089.52 --> 3096.26]  Like, is it just, it's, it's smooth for prototypes, but you could build a complex multifaceted web app with this thing.
[3097.00 --> 3098.76]  So there's, there's two halves to this.
[3098.82 --> 3100.70]  The first is it's new.
[3101.20 --> 3106.52]  And so, you know, like with every new tool, there's obviously always going to be warts.
[3106.52 --> 3117.22]  I don't know whether me not running into them is more because I know what the warts are, or maybe it's the other half, which is that I don't tend to be the person using the legacy packages.
[3117.98 --> 3120.40]  I, I mostly write my software.
[3120.54 --> 3134.20]  I don't install a lot of it with the exception of like UI toolkits, which was always the big challenge with WMR that we had to overcome because they're big and early and they use weird, weird package semantics that aren't always correct.
[3134.20 --> 3137.18]  But they, those work in WMR at least.
[3137.58 --> 3144.32]  The other piece is the actual physical scaling of the development time approach of shipping ES modules.
[3144.58 --> 3150.90]  There have been some maybe not super scientific kind of experiments.
[3151.44 --> 3156.46]  And right now the answers we have are whatever the opposite of definitive is.
[3156.46 --> 3169.08]  It's just, we know that if you ship, you know, 10,000 individual ES modules, especially if you're using HTTP one, that's going to be somewhat slow.
[3169.08 --> 3178.80]  And I'm actually in a, in a unique position where I am building WMR on one hand with the Preact team and we're relying on that.
[3178.80 --> 3186.36]  But then also I'm talking to the Chrome and V8 teams on the other side who are investigating module streaming performance.
[3186.36 --> 3193.58]  And so we're actually using this and things that look like this in benchmarks right now.
[3193.88 --> 3193.98]  Gotcha.
[3194.16 --> 3200.30]  So there's a, there's a bit of a cart and horse situation there from the performance standpoint for scaling up many thousands of modules.
[3200.30 --> 3215.52]  But even today for fairly large size projects, the way that this constraint ends up working is that your NPM dependencies actually don't scale one-to-one with the number of files on disk because we, we do compile those with rollup.
[3215.52 --> 3220.20]  And so like in a typical project, you'll kind of, you'll add a bunch of dependencies to your project.
[3220.36 --> 3222.32]  And then at a certain point, it mostly plateaus, right?
[3222.32 --> 3226.24]  Like you're not constantly re-adding new dependencies from NPM as you work.
[3226.48 --> 3231.42]  You kind of end up with like your framework-y substrate and then a couple of random things that get added over time.
[3232.06 --> 3234.04]  But that number doesn't grow super fast.
[3234.38 --> 3237.06]  And those all get cached in the HTTP cache and on disk.
[3237.26 --> 3238.50]  So they're relatively fast.
[3239.02 --> 3243.72]  And then the number that does change relative to your files on disk is your source files.
[3243.72 --> 3246.60]  So that's kind of the thing that you would want to keep in mind.
[3246.86 --> 3254.08]  I don't know that today I would necessarily jump to using WMR on a project that has 2000 source files.
[3255.64 --> 3259.02]  I don't have any reason not to suggest doing that.
[3259.46 --> 3260.02]  Just don't know.
[3261.18 --> 3261.60]  Yeah, exactly.
[3261.70 --> 3265.68]  But like that would be the scaling characteristics that I would, that I would be concerned about.
[3265.74 --> 3265.90]  Right.
[3266.60 --> 3268.86]  Not concerned from like, should I do this standpoint?
[3268.98 --> 3271.40]  But like how long is this going to take during development standpoint?
[3271.40 --> 3278.78]  And like hot module reloading helps with that because that's, now you're only talking about the first load that might be waiting to stream modules to disk.
[3278.94 --> 3284.00]  And this all changes as the semantics of browser module streaming parsing change.
[3284.34 --> 3285.34]  But that's the main one.
[3285.52 --> 3289.34]  The other side of the coin, which is what about production?
[3289.74 --> 3289.86]  Yeah.
[3289.86 --> 3297.26]  I don't think I'm like overstating WMR's abilities.
[3297.96 --> 3302.26]  I don't think it would be overstating WMR's abilities to say that it is fairly solid.
[3302.52 --> 3308.38]  Because in production, WMR is just a fairly sane rollup config.
[3309.10 --> 3313.70]  Like it's, you know, it's not, we're actually, we don't hit the custom code pathways.
[3313.80 --> 3315.42]  We're not running through our own plugin runner.
[3315.42 --> 3316.74]  We're not doing those things.
[3317.24 --> 3319.96]  It's pretty similar to a standard rollup config.
[3320.12 --> 3322.60]  We use our node modules resolution.
[3323.48 --> 3327.58]  But we actually do that so that it's never going to be different in production than it was in development.
[3327.58 --> 3328.62]  Because that would be very awful.
[3329.76 --> 3331.82]  And, you know, some similar things for transpiling.
[3331.96 --> 3335.72]  Like we use the custom transpiler, again, because we don't want it to be different.
[3336.26 --> 3339.36]  But then when we go to minify, like we minify with Terser, standard tool.
[3339.60 --> 3341.08]  We bundle with rollup, standard tool.
[3341.08 --> 3346.48]  By default, the browser support for WMR is modern browsers, you know, question mark.
[3346.94 --> 3349.94]  Essentially Edge 16 plus stuff that supports script type module.
[3350.34 --> 3356.12]  But there is a one file plugin that runs those bundles through Babel.
[3356.30 --> 3358.92]  And so now they, and creates copies of them.
[3358.96 --> 3363.54]  So now you have their modern files certify a script type module to 95% of browsers.
[3363.54 --> 3373.06]  And then it creates a second set of files that it automatically injects script no module tags for and serves to legacy browsers and polyfills them.
[3373.58 --> 3380.44]  So in terms of the, you know, the production output quality, the production output, like what has been taken into consideration.
[3380.44 --> 3386.22]  There's not really a consequential difference between what WMR can produce and what other tools can produce.
[3386.56 --> 3386.58]  Yeah.
[3386.76 --> 3391.48]  Really, honestly, the main thing to point out is just the production output is rollup based.
[3391.96 --> 3396.36]  And rollup, it is the gold standard for production output at this point.
[3396.48 --> 3397.66]  It's not the default.
[3398.38 --> 3399.52]  And so that's always something to consider.
[3399.62 --> 3405.44]  It's like usually this for people would mean moving away from a webpack configuration and onto a rollup one.
[3405.44 --> 3408.58]  But I think there's lots of reasons why one might consider doing that.
[3408.86 --> 3411.46]  So that's something to kind of consider.
[3412.16 --> 3421.28]  Another aspect of scale in terms of app complexity, which I think also affects the production story, is not just module count or that kind of complexity.
[3421.66 --> 3426.86]  But as soon as you start to want to do like maybe custom server responses.
[3427.56 --> 3431.30]  I know there's like a plugin interface for middlewares and stuff.
[3431.36 --> 3432.08]  So you can proxy.
[3432.36 --> 3433.76]  You can add some headers.
[3433.76 --> 3440.76]  Surely you can shoot yourself at that point once you start to extend it to like return arbitrary responses based on logic.
[3440.88 --> 3445.64]  Now you're basically running a dynamic web server and you can, of course, have production issues there, right?
[3446.32 --> 3447.28]  Yeah, that's a good point.
[3447.50 --> 3453.50]  And so I don't think we've properly put verbiage around this in the readme and in some of our stuff.
[3453.66 --> 3457.28]  But in the launch announcement and in the couple of videos I did, we want to be clear.
[3457.28 --> 3460.80]  Like WMR serve, like our production style server.
[3461.18 --> 3467.96]  We did not build that as a suggestion that you should use that to serve your application in production.
[3468.28 --> 3469.42]  I wouldn't do that.
[3469.42 --> 3478.44]  Because like at the end of the day, the best outcome is it's the POCA module and the serve module, both by Luke Edwards, which are great modules.
[3478.44 --> 3480.20]  But that's all it's doing.
[3480.36 --> 3482.44]  Like it's, you know, it's that and then an HTTP2 server.
[3482.66 --> 3486.14]  And really in production, you shouldn't be serving HTTP2 from Node.
[3486.16 --> 3487.52]  You should be serving it from your CDN.
[3487.96 --> 3491.20]  And at that point, why serve your files from Node in the first place?
[3491.32 --> 3495.78]  Deploy them to a CDN, you know, deploy them to Netlify, to Cloudflare.
[3496.04 --> 3498.56]  Now they've got pages or Firebase, wherever.
[3498.56 --> 3508.76]  However, the prod server that we bundled, its goal was to give you a very accurate local representation of what prod would be like.
[3509.50 --> 3512.66]  That's actually why we have the middleware support so you can add proxies and stuff.
[3512.90 --> 3515.44]  It's because in production, you might have that set up.
[3515.72 --> 3518.92]  But I don't think it would make sense to do that through WMR.
[3519.20 --> 3524.12]  We're the development and bundling side of things and we'll get you to production, but we aren't production.
[3524.12 --> 3524.48]  Right.
[3524.58 --> 3528.28]  Like it produces production assets, but it is not your production server.
[3529.32 --> 3532.54]  Yeah, and that's actually a dividing line that I think we could make clearer.
[3533.10 --> 3534.58]  And you had mentioned Next.js early on.
[3534.66 --> 3536.56]  Next.js, it is a server.
[3536.88 --> 3539.36]  It is a runtime that your application runs in.
[3539.76 --> 3543.82]  WMR, really, we have no intention of being that.
[3543.92 --> 3550.16]  There was an SSR plugin that I built, more as like an experiment to see, could you do it?
[3551.12 --> 3556.32]  But even then, I think if we ever actually formalized going down that road,
[3556.32 --> 3563.96]  it would still be, we will generate a server as a JS file that you're going to go and host yourself.
[3563.96 --> 3564.16]  Right.
[3564.20 --> 3567.54]  And it'll, or it'll be like a piece of middleware that you're going to mount into your own node
[3567.54 --> 3569.92]  server because WMR is not a stack.
[3570.08 --> 3571.32]  That's kind of the dividing line.
[3571.32 --> 3575.44]  That's a good distinction from an outsider reading the readme and checking it out.
[3575.70 --> 3577.96]  And like I said, is it, is it like a Next.js?
[3578.08 --> 3581.96]  Because I'm trying to figure out like, is this going to host a hybrid application or not?
[3582.44 --> 3584.00]  I mean, it can, obviously it could.
[3584.20 --> 3584.58]  It can, yeah.
[3584.58 --> 3586.08]  But does it want to be that?
[3586.42 --> 3588.88]  And I think the answer to that sounds like no, it doesn't really want to be that.
[3588.88 --> 3589.00]  No.
[3589.14 --> 3593.54]  And to the point where like, I think in order to do that, we would end up having to compromise
[3593.54 --> 3595.62]  on being good at generating static apps.
[3596.18 --> 3600.96]  And if there was a need there, I would rather have it be a separate tool or, or like a tool
[3600.96 --> 3602.92]  that uses WMR for bundling, but that's it.
[3603.12 --> 3607.88]  And like, there's a bunch of folks right now who are trying out wiring up Eleventy, the
[3607.88 --> 3613.54]  static site generator, and then just using WMR as the front end thing.
[3613.54 --> 3617.90]  So like you can have Eleventy with a script type module tag that just points at WMR or
[3617.90 --> 3620.64]  even use WMR's middleware thing to proxy to Eleventy.
[3621.18 --> 3625.22]  But then when you do like a production build, you're just saying, hey, WMR, give me your
[3625.22 --> 3625.58]  assets.
[3625.84 --> 3626.06]  Okay.
[3626.42 --> 3627.60]  Those are in Eleventy now.
[3627.86 --> 3629.24]  Eleventy is ultimately the stack.
[3629.80 --> 3632.74]  And to me, that just fits a lot better with the model.
[3633.20 --> 3635.64]  It's generative, not runtime.
[3636.00 --> 3636.10]  Gotcha.
[3636.76 --> 3637.32]  Anything, Nick?
[3637.80 --> 3639.06]  No, that sounds really interesting.
[3639.06 --> 3644.84]  I like that's kind of a use case I was thinking of is using WMR with Eleventy kind of just
[3644.84 --> 3649.96]  as like a side project fun idea and a way to get to use this a little bit more.
[3650.40 --> 3651.66]  It does seem like a good fit.
[3652.24 --> 3657.24]  But especially like, because we have that thing where we start from HTML files and in
[3657.24 --> 3659.44]  development, we don't even look at the HTML file.
[3659.52 --> 3662.20]  It's just that first script tag request when it comes into the HP server.
[3662.30 --> 3662.86]  We deal with that.
[3663.10 --> 3664.40]  It lends itself quite well.
[3664.40 --> 3669.12]  You would get hot module replacement in Eleventy, which is normally a pain in the ass to set
[3669.12 --> 3669.34]  up.
[3669.72 --> 3669.82]  Yeah.
[3670.28 --> 3671.04]  That'd be really cool.
[3671.54 --> 3678.86]  And then the other piece there is there are folks, myself included, who, if you're not
[3678.86 --> 3684.06]  currently using Eleventy or let's say you're building a website that isn't strictly content,
[3684.54 --> 3689.04]  you might want to have page-based routing, kind of in a Next.js style.
[3689.84 --> 3691.68]  And so we have plugins and recipes now.
[3691.68 --> 3695.54]  So it actually, it basically just comes, there's a plugin that lets you import a directory
[3695.54 --> 3698.10]  that returns the files in the directory as an array.
[3698.52 --> 3701.08]  And you could actually build a whole static site generator on top of that.
[3701.18 --> 3703.74]  So we've got demos now showing how to do that.
[3703.86 --> 3707.44]  But like WMR is actually lower level than any of those things.
[3707.44 --> 3710.26]  It's more like if you want to do that, you can.
[3710.52 --> 3713.64]  It's fully supported, but we're not telling you like, this is what it's for.
[3713.64 --> 3719.16]  Well, the project can be found at github.com slash preact.js slash WMR.
[3719.34 --> 3722.76]  Or hey, just hop into your terminal and type npm init WMR.
[3723.18 --> 3725.14]  And you can even leave off to your project name.
[3725.22 --> 3728.14]  It'll just take your current directory and turn it into something cool.
[3728.24 --> 3730.04]  Just be aware that it will blow up your directory.
[3730.90 --> 3732.30]  And that's not like a WMR thing.
[3732.44 --> 3733.46]  Yeah, just go ahead and run that.
[3733.60 --> 3733.94]  I've done that twice now.
[3734.00 --> 3735.32]  Go ahead and run that in your home directory.
[3735.48 --> 3736.46]  Everything will be just fine.
[3736.46 --> 3740.18]  And Jason Miller, thanks so much for joining us.
[3740.48 --> 3742.26]  You can find Jason online.
[3742.52 --> 3746.60]  He's at developer at underscore develop it, depending on the context.
[3747.32 --> 3748.88]  What's the best way to reach you, Jason?
[3749.00 --> 3750.04]  Twitter the best?
[3750.24 --> 3750.40]  GitHub?
[3750.84 --> 3751.50]  Yeah, Twitter's fine.
[3751.94 --> 3752.30]  All right.
[3752.36 --> 3753.82]  So links to Jason in the show notes.
[3753.94 --> 3755.28]  Links to WMR.
[3755.44 --> 3759.16]  All the things discussed on this episode, of course, are right there in your show notes
[3759.16 --> 3759.94]  for easy clickings.
[3760.02 --> 3762.68]  Nick, thanks for hanging out for our first episode back.
[3763.22 --> 3766.30]  Jason, thanks for joining us and for really putting so much work
[3766.30 --> 3767.44]  into these cool new tools.
[3767.70 --> 3770.96]  I mean, I love not having to write cool new tools,
[3771.08 --> 3775.20]  but getting to just use these cool new tools and criticize them and enjoy them.
[3775.26 --> 3779.72]  And so we appreciate all the effort you are putting into pushing the web forward for all of us.
[3780.46 --> 3781.42]  That's our show.
[3781.60 --> 3782.60]  Talk to you again next week.
[3785.86 --> 3788.22]  If you're a first time listener, stick around.
[3788.22 --> 3794.50]  Why don't you subscribe now at jsparty.fm or search for JSParty in your favorite podcast app.
[3794.74 --> 3795.44]  You'll find us.
[3796.24 --> 3798.40]  Oh, and while you're there, maybe leave us a nice review.
[3798.84 --> 3799.40]  We love those.
[3800.10 --> 3803.54]  Also, don't forget, we're giving away those two free tickets to test JS Summit.
[3803.72 --> 3805.56]  Follow at jsparty.fm to enter.
[3805.90 --> 3807.44]  We'll announce the winners real soon now.
[3808.08 --> 3810.82]  Music for JS Party is produced by the Beat Freak, Breakmaster Cylinder,
[3811.04 --> 3812.72]  and we're brought to you by some awesome sponsors.
[3813.00 --> 3816.86]  Special thanks to Fastly, LaunchDarkly, and Linode for their continued support.
[3817.26 --> 3820.64]  Next up on the pod, I sit down with the creator of Developer Roadmaps
[3820.64 --> 3824.12]  to discuss the paths you can take to being a web developer in 2021.
[3824.68 --> 3827.36]  That episode's hitting your podcast feed next week.
[3827.36 --> 3827.86]  Music.
[3827.86 --> 3828.36]  Music.
[3829.30 --> 3829.86]  Music.
[3829.86 --> 3830.44]  Music.
[3830.44 --> 3831.36]  Music.
[3831.36 --> 3831.94]  Music.
[3831.94 --> 3833.50]  Music.
[3833.50 --> 3834.44]  Music.
[3834.44 --> 3835.32]  Music.
[3835.32 --> 3835.94]  Music.
[3835.94 --> 3836.54]  Music.
[3836.54 --> 3837.48]  Music.
[3837.48 --> 3838.38]  Music.
[3838.38 --> 3839.30]  Music.
[3839.30 --> 3839.48]  Music.
[3839.48 --> 3840.38]  Music.
[3840.38 --> 3841.44]  Music.
[3841.44 --> 3842.26]  Music.
[3843.02 --> 3843.50]  Music.
[3843.50 --> 3843.78]  Music.
[3843.78 --> 3845.02]  What I mean is this
[3845.02 --> 3845.92]  250?
[3845.92 --> 3846.88]  Music.
[3847.06 --> 3847.42]  Music.
[3847.66 --> 3848.96]  Music.
[3853.06 --> 3853.46]  Music.
